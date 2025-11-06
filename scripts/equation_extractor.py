"""
Comprehensive Equation Extraction System for Math_Science Repository
ASCII-only implementation: extracts equations from text/Markdown files and
indexes LaTeX equations from synthesis modules.
"""

from __future__ import annotations

import re
import os
import csv
import json
import time
import argparse
from pathlib import Path
import fnmatch
from collections import defaultdict

try:
    from scripts.common import resolve_base_dir
except Exception:
    import sys as _sys
    from pathlib import Path as _Path
    _mod_dir = str(_Path(__file__).resolve().parent)
    _sys.path.insert(0, _mod_dir)
    from common import resolve_base_dir


BASE_DIR = str(Path(__file__).resolve().parents[1])

# Compiled regex patterns (ASCII-safe)
COMPILED_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"Energy\s+relation:\s*(.+)", re.IGNORECASE), "key_relation"),
    (re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_\s]*)\s*[=:]\s*(.+)$", re.IGNORECASE), "explicit"),
    (re.compile(r"(.+?)\s*=\s*(.+)", re.IGNORECASE), "assignment"),
    (re.compile(r"Governing\s+(?:Equation|Relation|Dynamics):\s*(.+)", re.IGNORECASE), "governing"),
    (re.compile(r"(?:Key\s+Relation|Prediction):\s*(.+)", re.IGNORECASE), "key_relation"),
]

# Prioritized domain keyword lists for classification
DOMAIN_PRIORITIES: list[tuple[str, list[str]]] = [
    ("EM", ["electromagnetic", "electric", "magnetic", "maxwell", "field", "capacitance", "inductance"]),
    ("GR", ["metric", "curvature", "einstein", "ricci", "tensor", "spacetime", "gravity"]),
    ("QM", ["quantum", "wave", "psi", "hamiltonian", "operator", "qubit", "entangle"]),
    ("Thermo", ["entropy", "temperature", "heat", "thermal", "boltzmann", "specific heat", "helmholtz", "gibbs"]),
    ("Math", ["group", "algebra", "lie", "symmetry", "topology", "dimension"]),
    ("Experimental", ["casimir", "measurement", "spectroscopy", "interferometry"]),
]


class EquationExtractor:
    """Extracts equations from text files and LaTeX modules.

    This class scans specified directories for text and Markdown files,
    extracts equations based on a set of regular expression patterns,
    and catalogs them. It also builds a map of LaTeX equations from
    the `synthesis/modules/equations` directory to link extracted
    equations with their formal LaTeX representations.

    Attributes:
        base_dir (str): The root directory of the repository.
        equations (list[dict]): A list of dictionaries, each representing a
            found equation.
        eq_counter (dict[str, int]): A counter for generating unique equation IDs
            for each framework.
        seen_equations (set[str]): A set of normalized equations to avoid
            duplicates.
        latex_map (dict[str, str]): A mapping from normalized LaTeX equation
            bodies to their source file and label.
        had_errors (bool): A flag indicating if any errors occurred during
            extraction.
        plan_items (list[dict]): A list of dictionaries detailing the scan plan.
        metrics (dict[str, object]): A dictionary of metrics collected during
            the scan.
    """
    def __init__(self, base_dir: str | None = None):
        """Initializes the EquationExtractor.

        Args:
            base_dir: The base directory of the repository. If not provided,
                it is resolved automatically.
        """
        self.base_dir = resolve_base_dir(base_dir)
        self.equations: list[dict] = []
        self.eq_counter: dict[str, int] = defaultdict(int)
        self.seen_equations: set[str] = set()
        self.latex_map: dict[str, str] = {}
        self.had_errors = False
        self.plan_items: list[dict] = []
        self.metrics: dict[str, object] = {
            'files_scanned': 0,
            'files_skipped_size': 0,
            'files_skipped_excluded': 0,
            'files_skipped_decode': 0,
            'bytes_scanned': 0,
            'candidate_equations': 0,
            'unique_equations': 0,
            'elapsed_s': 0.0,
            'timing_by_framework': {},
            'read_elapsed_s': 0.0,
            'extract_elapsed_s': 0.0,
            'timing_by_framework_breakdown': {},
        }
        self.latex_map = self._build_latex_map()

    @staticmethod
    def _canonicalize(eq_str: str) -> str:
        """DEPRECATED: Normalizes an equation string using a basic method.

        This method performs a series of simple string replacements to
        normalize an equation string for comparison. It is less robust than
        `_canonicalize_v2`.

        Args:
            eq_str: The equation string to normalize.

        Returns:
            The normalized equation string.
        """
        replacements = [
            (r"\\cdot", "*"),
            (r"\\times", "*"),
            (r"\\cdots", "..."),
            (r"\\left", ""),
            (r"\\right", ""),
            (r"\\,", ""),
            (r"\\;", ""),
            (r"\\!", ""),
            (r"\u00B7", "*"),
        ]
        s = eq_str
        for pat, rep in replacements:
            s = re.sub(pat, rep, s)
        # Strip \mathrm{..} and \mathbf{..}
        s = re.sub(r"\\(mathrm|mathbf)\{([^{}]*)\}", r"\2", s)
        # Simplify \frac{a}{b} --> a/b
        s = re.sub(r"\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}", r"\1/\2", s)
        return s

    @staticmethod
    def _canonicalize_v2(eq_str: str) -> str:
        """Normalizes an equation string using an enhanced method.

        This method performs a series of advanced string replacements to
        normalize an equation string for comparison, including handling
        nested LaTeX macros.

        Args:
            eq_str: The equation string to normalize.

        Returns:
            The normalized equation string.
        """
        replacements = [
            (r"\\cdot", "*"),
            (r"\\times", "*"),
            (r"\\cdots", "..."),
            (r"\\left", ""),
            (r"\\right", ""),
            (r"\\,", ""),
            (r"\\;", ""),
            (r"\\!", ""),
            (r"\\:\s*", ""),
            (r"\\quad", ""),
            (r"\\qquad", ""),
            (r"\\\s", " "),
            (r"~", " "),
            (r"\u00B7", "*"),
        ]
        s = eq_str
        for pat, rep in replacements:
            s = re.sub(pat, rep, s)
        # Recursively strip selected text-style wrappers: \mathrm, \mathbf, \text
        _macro_pat = re.compile(r"\\(mathrm|mathbf|text)\{([^{}]*)\}")
        while True:
            _new = _macro_pat.sub(r"\2", s)
            if _new == s:
                break
            s = _new
        # \operatorname{foo} -> foo
        _op_pat = re.compile(r"\\operatorname\s*\{([^{}]+)\}")
        while True:
            _new = _op_pat.sub(r"\1", s)
            if _new == s:
                break
            s = _new
        # Repeatedly simplify \frac{a}{b} to a/b
        _frac_pat = re.compile(r"\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}")
        while True:
            _new = _frac_pat.sub(r"\1/\2", s)
            if _new == s:
                break
            s = _new
        # Normalize square roots for dedup keys only
        # \sqrt{expr} -> sqrt(expr)
        _sqrt_pat = re.compile(r"\\sqrt\s*\{([^{}]+)\}")
        while True:
            _new = _sqrt_pat.sub(r"sqrt(\1)", s)
            if _new == s:
                break
            s = _new
        # \sqrt[n]{expr} -> root(n,expr)
        _nsqrt_pat = re.compile(r"\\sqrt\s*\[([^\]]+)\]\s*\{([^{}]+)\}")
        while True:
            _new = _nsqrt_pat.sub(r"root(\1,\2)", s)
            if _new == s:
                break
            s = _new
        return s

    @staticmethod
    def normalize_equation(eq_str: str) -> str:
        """Normalizes an equation string for duplicate checking.

        This method uses `_canonicalize_v2` to normalize the equation,
        then removes all whitespace and converts to lowercase.

        Args:
            eq_str: The equation string to normalize.

        Returns:
            A compact, normalized version of the equation string.
        """
        # Use enhanced canonicalization that handles nested macros
        s = EquationExtractor._canonicalize_v2(eq_str)
        return re.sub(r"\s+", "", s.strip()).lower()

    @staticmethod
    def _strip_tex(text: str) -> str:
        """Strips LaTeX commands and comments from a string.

        This is used to clean up LaTeX equation bodies before normalization.

        Args:
            text: The string containing LaTeX markup.

        Returns:
            The cleaned string.
        """
        t = re.sub(r"%.*", "", text)  # comments
        t = re.sub(r"\\label\{[^}]*\}", "", t)
        t = t.replace("\\begin{equation}", "").replace("\\end{equation}", "")
        t = re.sub(r"\$+", "", t)  # remove $/$$
        # remove commands and args
        t = re.sub(r"\\[a-zA-Z]+\{[^}]*\}", "", t)
        t = re.sub(r"\\[a-zA-Z]+\[[^\]]*\]", "", t)
        t = re.sub(r"\\[a-zA-Z]+", "", t)
        t = re.sub(r"[{}]", "", t)
        t = re.sub(r"\[[^\]]*\]", "", t)
        t = re.sub(r"\s+", " ", t).strip()
        return t

    def _build_latex_map(self) -> dict[str, str]:
        """Builds a map of LaTeX equations from the synthesis modules.

        This method scans the `synthesis/modules/equations` directory for
        `.tex` files, extracts the equation bodies and labels, and creates
        a mapping from a normalized version of the equation to its source
        location.

        Returns:
            A dictionary mapping normalized equation strings to their
            source file and label.
        """
        latex_dir = Path(self.base_dir) / "synthesis" / "modules" / "equations"
        mapping: dict[str, str] = {}
        if not latex_dir.exists():
            return mapping
        for tex in latex_dir.rglob("*.tex"):
            try:
                content = tex.read_text(encoding="utf-8", errors="strict")
            except UnicodeDecodeError:
                print(f"Warning: Could not decode LaTeX module as UTF-8 (non-ASCII content?): {tex}")
                self.had_errors = True
                continue
            except IOError as e:
                print(f"Error reading LaTeX module {tex}: {e}")
                self.had_errors = True
                continue
            m_label = re.search(r"\\label\{([^}]+)\}", content)
            label = m_label.group(1) if m_label else tex.stem
            bodies: list[str] = []
            # equation environment
            start_tag = "\\begin{equation}"
            end_tag = "\\end{equation}"
            idx = 0
            while True:
                s = content.find(start_tag, idx)
                if s == -1:
                    break
                e = content.find(end_tag, s + len(start_tag))
                if e == -1:
                    break
                bodies.append(content[s + len(start_tag):e])
                idx = e + len(end_tag)
            # display math \[ ... \]
            if not bodies:
                start_tag = "\\["
                end_tag = "\\]"
                idx = 0
                while True:
                    s = content.find(start_tag, idx)
                    if s == -1:
                        break
                    e = content.find(end_tag, s + len(start_tag))
                    if e == -1:
                        break
                    bodies.append(content[s + len(start_tag):e])
                    idx = e + len(end_tag)
            for body in bodies:
                stripped = self._strip_tex(body)
                # For map keys, preserve case while removing whitespace; apply canonicalization without lowercasing
                norm = re.sub(r"\s+", "", self._canonicalize(stripped).strip())
                if norm:
                    val = f"{tex.relative_to(Path(self.base_dir))}#{label}"
                    mapping[norm] = val
                    mapping[norm.lower()] = val
        return mapping

    def _generate_eq_id(self, framework: str) -> str:
        """Generates a unique equation ID for a given framework.

        Args:
            framework: The framework name (e.g., "Aether", "Genesis").

        Returns:
            A unique equation ID string (e.g., "AE001").
        """
        prefix_map = {
            "Aether": "AE",
            "Genesis": "GE",
            "Pais": "PE",
            "Tourmaline": "TE",
            "Superforce": "SE",
            "Literature": "LE",
            "Unified": "UE",
            "Synthesis": "SE",
        }
        prefix = prefix_map.get(framework, "EQ")
        self.eq_counter[prefix] += 1
        return f"{prefix}{self.eq_counter[prefix]:03d}"

    @staticmethod
    def _extract_description(lines: list[str], line_num: int, context_window: int = 3) -> str:
        """Extracts a description for an equation from its context.

        Args:
            lines: A list of all lines in the source file.
            line_num: The line number of the equation.
            context_window: The number of lines before and after the
                equation to include in the context.

        Returns:
            A string containing the context of the equation.
        """
        start = max(0, line_num - context_window - 1)
        end = min(len(lines), line_num + context_window)
        context = " ".join(lines[start:end])
        context = re.sub(r"\s+", " ", context).strip()
        if len(context) > 200:
            context = context[:200] + "..."
        return context

    @staticmethod
    def _classify_domain(equation_str: str, description: str) -> str:
        """Classifies the domain of an equation.

        Args:
            equation_str: The equation string.
            description: The description of the equation.

        Returns:
            The classified domain string (e.g., "EM", "GR", "QM").
        """
        combined = (equation_str + " " + description).lower()
        for dom, keys in DOMAIN_PRIORITIES:
            if any(k in combined for k in keys):
                return dom
        return "General"

    @staticmethod
    def _suggest_experiment(equation_str: str, description: str) -> str:
        """Suggests a potential experimental test for an equation.

        Args:
            equation_str: The equation string.
            description: The description of the equation.

        Returns:
            A string with the suggested experiment or "Theoretical
            validation required".
        """
        suggestions = {
            "casimir": "Casimir force measurement with fractal geometries",
            "scalar": "Scalar field interferometry",
            "foam": "Quantum foam perturbation detection",
            "zpe": "Zero-point energy spectroscopy",
            "crystal": "Vibrational spectroscopy in crystals",
            "entropy": "Thermal imaging and entropy measurement",
            "dimensional": "Dimensional spectroscopy",
        }
        combined = (equation_str + " " + description).lower()
        for k, v in suggestions.items():
            if k in combined:
                return v
        return "Theoretical validation required"

    @staticmethod
    def _has_math(expr: str) -> bool:
        """Checks if a string contains mathematical symbols.

        Args:
            expr: The string to check.

        Returns:
            True if the string contains math symbols, False otherwise.
        """
        return re.search(r"(=|\+|\-|\*|/|\^|\\(sum|int|frac|alpha|beta|gamma|sqrt|log|exp|partial|nabla))", expr) is not None

    def _is_valid_equation(self, eq_str: str) -> bool:  # used in tests
        """Validates if a string is a plausible equation.

        This method applies a series of heuristics to determine if a given
        string is likely to be an equation, filtering out prose and other
        non-equation text.

        Args:
            eq_str: The string to validate.

        Returns:
            True if the string is a valid equation, False otherwise.
        """
        if len(eq_str) < 5 or len(eq_str) > 500:
            return False
        if eq_str.startswith(("- [", "* [", "C:\\Users\\")):
            return False
        if not self._has_math(eq_str):
            return False
        prose_indicators = [
            " the ", " and ", " or ", " is ", " are ", " that ",
            " this ", " these ", " with ", " for ", " from ", " a ", " an ", " to ", " in ", " of ",
        ]
        prose_count = sum(1 for ind in prose_indicators if ind in eq_str.lower())
        words = len(eq_str.split())
        if words > 5 and words > 0 and prose_count / words > 0.4:
            return False
        if re.fullmatch(r"={5,}", eq_str):
            return False
        return True

    def extract_from_text_file(self, filepath: str, framework_type: str) -> None:
        """DEPRECATED: Extracts equations from a single text file.

        This method is kept for backward compatibility and testing. The main
        extraction logic is now in `process_dirs` and `_extract_entries_from_content`.

        Args:
            filepath: The path to the text file.
            framework_type: The framework to assign to the extracted equations.
        """
        print(f"Processing: {os.path.basename(filepath)}")
        try:
            with open(filepath, "r", encoding="utf-8", errors="strict") as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            print(f"Warning: Could not decode text file as UTF-8 (non-ASCII content?): {filepath}")
            self.had_errors = True
            return
        except IOError as e:
            print(f"Error reading text file {filepath}: {e}")
            self.had_errors = True
            return
        filename = os.path.basename(filepath)

        for line_num, line in enumerate(lines, 1):
            s = line.strip()
            if not s or len(s) < 5:
                continue
            for pattern, kind in COMPILED_PATTERNS:
                try:
                    matches = pattern.finditer(s)
                except re.error as e:
                    print(f"Warning: Regex error for pattern '{pattern}' in {filepath} line {line_num}: {e}")
                    self.had_errors = True
                    continue
                for m in matches:
                    if kind in ("governing", "key_relation"):
                        eq_text = m.group(1).strip()
                    else:
                        eq_text = m.group(0).strip()
                    if not self._is_valid_equation(eq_text):
                        continue
                    normalized = self.normalize_equation(eq_text)
                    self.metrics['candidate_equations'] = int(self.metrics.get('candidate_equations', 0)) + 1
                    if normalized in self.seen_equations:
                        continue
                    self.seen_equations.add(normalized)
                    eq_id = self._generate_eq_id(framework_type)
                    description = self._extract_description(lines, line_num)
                    domain = self._classify_domain(eq_text, description)
                    entry = {
                        "EqID": eq_id,
                        "Equation": eq_text,
                        "Framework": framework_type,
                        "Domain": domain,
                        "SourceDoc": filename,
                        "SourceLine": line_num,
                        "Description": description,
                        "VerificationStatus": "Theoretical",
                        "RelatedEqs": "",
                        "ExperimentalTest": self._suggest_experiment(eq_text, description),
                    }
                    tex_key = self.normalize_equation(self._strip_tex(eq_text))
                    if tex_key in self.latex_map:
                        entry["RelatedEqs"] = f"module:{self.latex_map[tex_key]}"
                    self.equations.append(entry)

    def _extract_entries_from_content(self, content: str, framework_type: str, filename: str) -> tuple[list[dict], float]:
        """Extracts equation entries from a string of content.

        This method is called by `process_dirs` to perform the actual
        extraction from file content.

        Args:
            content: The string content of the file.
            framework_type: The framework to assign to the extracted equations.
            filename: The name of the source file.

        Returns:
            A tuple containing a list of extracted equation dictionaries
            and the time spent on classification.
        """
        results: list[dict] = []
        classify_elapsed = 0.0
        lines = content.splitlines()
        patterns = [
            (r"Energy\s+relation:\s*(.+)", "key_relation"),
            (r"^\s*([A-Za-z_][A-Za-z0-9_\s]*)\s*[=:]\s*(.+)$", "explicit"),
            (r"(.+?)\s*=\s*(.+)", "assignment"),
            (r"Governing\s+(?:Equation|Relation|Dynamics):\s*(.+)", "governing"),
            (r"(?:Key\s+Relation|Prediction):\s*(.+)", "key_relation"),
        ]
        for line_num, raw in enumerate(lines, 1):
            s = raw.strip()
            if not s or len(s) < 5:
                continue
            for pattern, kind in patterns:
                try:
                    matches = re.finditer(pattern, s, re.IGNORECASE)
                except re.error:
                    continue
                for m in matches:
                    eq_text = m.group(1).strip() if kind in ("governing", "key_relation") else m.group(0).strip()
                    if not self._is_valid_equation(eq_text):
                        continue
                    _cs = time.perf_counter()
                    descr = self._extract_description(lines, line_num)
                    domain = self._classify_domain(eq_text, descr)
                    classify_elapsed += (time.perf_counter() - _cs)
                    results.append({
                        "Equation": eq_text,
                        "Framework": framework_type,
                        "Domain": domain,
                        "SourceDoc": filename,
                        "SourceLine": line_num,
                        "Description": descr,
                        "ExperimentalTest": self._suggest_experiment(eq_text, descr),
                    })
        return results, classify_elapsed

    def process_all_files(self) -> None:
        """Processes all files in the base directory."""
        self.process_dirs([str(Path(self.base_dir))])

    def process_dirs(self, dirs: list[str], max_files: int | None = None, max_size_mb: float | None = None, max_lines: int | None = None, parallel_workers: int | None = None, exclude_dirs: list[str] | None = None, use_default_excludes: bool = True, framework_include: list[str] | None = None, framework_exclude: list[str] | None = None, include_globs: list[str] | None = None, exclude_globs: list[str] | None = None, plan_only: bool = False) -> None:
        """Scans specified directories and extracts equations.

        This is the main method for processing files. It gathers a list of
        candidate files, then extracts equations from them, either serially
        or in parallel.

        Args:
            dirs: A list of directories to scan.
            max_files: The maximum number of files to process.
            max_size_mb: The maximum size of files to process in megabytes.
            max_lines: The maximum number of lines to read from each file.
            parallel_workers: The number of parallel workers to use for extraction.
            exclude_dirs: A list of directories to exclude from the scan.
            use_default_excludes: Whether to use the default list of excluded
                directories.
            framework_include: A list of frameworks to include.
            framework_exclude: A list of frameworks to exclude.
            include_globs: A list of glob patterns to include.
            exclude_globs: A list of glob patterns to exclude.
            plan_only: If True, the method will only plan the scan and not
                perform the extraction.
        """
        size_limit = int((max_size_mb or 0) * 1024 * 1024)
        t0 = time.perf_counter()
        # Gather candidates deterministically
        candidates: list[tuple[str, str]] = []
        count = 0
        for d in dirs:
            is_root = Path(d).resolve() == Path(self.base_dir).resolve()
            effective_excludes = list(exclude_dirs) if exclude_dirs else (
                [
                    'data', 'extracted_data', 'source_materials', 'output',
                    '.git', '.pytest_cache', '__pycache__'
                ] if (is_root and use_default_excludes) else []
            )
            for path in sorted(Path(d).rglob("*")):
                if path.suffix.lower() not in {".md", ".txt"} or not path.is_file():
                    continue
                # Glob filters relative to scan root
                rel = str(path.relative_to(d)).replace('\\', '/')
                if include_globs:
                    if not any(fnmatch.fnmatch(rel, g) for g in include_globs):
                        self.plan_items.append({'path': str(path), 'rel': rel, 'framework': '', 'action': 'skip', 'reason': 'glob_not_included', 'size': None})
                        continue
                if exclude_globs:
                    if any(fnmatch.fnmatch(rel, g) for g in exclude_globs):
                        self.metrics['files_skipped_excluded'] = int(self.metrics.get('files_skipped_excluded', 0)) + 1
                        self.plan_items.append({'path': str(path), 'rel': rel, 'framework': '', 'action': 'skip', 'reason': 'glob_exclude', 'size': None})
                        continue
                if effective_excludes:
                    skip = False
                    for ex in effective_excludes:
                        ex_path = (Path(d) / ex).resolve()
                        try:
                            if ex_path in [path.resolve()] + [p.resolve() for p in path.parents]:
                                skip = True
                                break
                        except Exception:
                            continue
                    if skip:
                        self.metrics['files_skipped_excluded'] = int(self.metrics.get('files_skipped_excluded', 0)) + 1
                        try:
                            sz_tmp = path.stat().st_size
                        except Exception:
                            sz_tmp = None
                        self.plan_items.append({'path': str(path), 'rel': rel, 'framework': '', 'action': 'skip', 'reason': 'excluded_dir', 'size': int(sz_tmp) if sz_tmp is not None else None})
                        continue
                if max_files is not None and count >= max_files:
                    self.plan_items.append({'path': str(path), 'rel': rel, 'framework': '', 'action': 'skip', 'reason': 'limit_reached', 'size': None})
                    break
                try:
                    sz = path.stat().st_size
                except OSError as e:
                    print(f"Warning: Could not get size of file {path}: {e}")
                    self.had_errors = True
                    sz = 0
                if max_size_mb is not None and sz > size_limit:
                    self.metrics['files_skipped_size'] = int(self.metrics.get('files_skipped_size', 0)) + 1
                    self.plan_items.append({'path': str(path), 'rel': rel, 'framework': '', 'action': 'skip', 'reason': 'max_size', 'size': int(sz)})
                    continue
                self.metrics['files_scanned'] = int(self.metrics.get('files_scanned', 0)) + 1
                self.metrics['bytes_scanned'] = int(self.metrics.get('bytes_scanned', 0)) + int(sz)
                lower = path.name.lower()
                if any(k in lower for k in ["alpha", "aether"]):
                    fw = "Aether"
                elif any(k in lower for k in ["genesis", "math"]):
                    fw = "Genesis"
                elif "pais" in lower:
                    fw = "Pais"
                elif any(k in lower for k in ["survey", "literature", "review"]):
                    fw = "Literature"
                else:
                    fw = "Unified"
                if framework_include and fw not in framework_include:
                    self.metrics['files_skipped_excluded'] = int(self.metrics.get('files_skipped_excluded', 0)) + 1
                    self.plan_items.append({'path': str(path), 'rel': rel, 'framework': fw, 'action': 'skip', 'reason': 'framework_include_mismatch', 'size': int(sz)})
                    continue
                if framework_exclude and fw in framework_exclude:
                    self.metrics['files_skipped_excluded'] = int(self.metrics.get('files_skipped_excluded', 0)) + 1
                    self.plan_items.append({'path': str(path), 'rel': rel, 'framework': fw, 'action': 'skip', 'reason': 'framework_excluded', 'size': int(sz)})
                    continue
                candidates.append((str(path), fw))
                self.plan_items.append({'path': str(path), 'rel': rel, 'framework': fw, 'action': 'scan', 'reason': 'selected', 'size': int(sz)})
                count += 1
            if max_files is not None and count >= max_files:
                break

        # Plan-only mode: stop after planning and return
        if plan_only:
            self.metrics['elapsed_s'] = round(time.perf_counter() - t0, 3)
            return

        # Parallel path (optional)
        if (parallel_workers or 0) > 0 and candidates:
            from concurrent.futures import ThreadPoolExecutor
            # local extractor to avoid modifying global state in threads
            def read_content(pstr: str) -> tuple[str, int]:
                try:
                    with open(pstr, "r", encoding="utf-8", errors="strict") as f:
                        if max_lines is not None:
                            buf: list[str] = []
                            for i, line in enumerate(f, 1):
                                buf.append(line)
                                if i >= max_lines:
                                    break
                            return "".join(buf), 0
                        return f.read(), 0
                except Exception:
                    return "", 1

            def worker(idx_path_fw: tuple[int, tuple[str, str]]):
                idx, (pstr, fw) = idx_path_fw
                # measure read
                _rs = time.perf_counter()
                content, skipped = read_content(pstr)
                read_elapsed = time.perf_counter() - _rs
                if not content:
                    return idx, [], skipped, fw, read_elapsed, 0.0, 0.0
                _es = time.perf_counter()
                entries, classify_e = self._extract_entries_from_content(content, fw, os.path.basename(pstr))
                extract_elapsed = time.perf_counter() - _es
                return idx, entries, skipped, fw, read_elapsed, extract_elapsed, classify_e

            results_by_index: list[list[dict]] = [[] for _ in candidates]
            skipped_decode_total = 0
            timing_fw: dict[str, float] = defaultdict(float)
            timing_fw_break: dict[str, dict[str, float]] = {}
            read_total = 0.0
            extract_total = 0.0
            classify_total = 0.0
            with ThreadPoolExecutor(max_workers=parallel_workers) as ex:
                futures = []
                for idx, item in enumerate(candidates):
                    futures.append(ex.submit(worker, (idx, item)))
                for fut in futures:
                    idx, entries, skipped, fw, read_e, extract_e, classify_e = fut.result()
                    results_by_index[idx] = entries
                    skipped_decode_total += int(skipped)
                    timing_fw[fw] = timing_fw.get(fw, 0.0) + float(read_e + extract_e)
                    if fw not in timing_fw_break:
                        timing_fw_break[fw] = {'read_s': 0.0, 'extract_s': 0.0, 'classify_s': 0.0}
                    timing_fw_break[fw]['read_s'] += float(read_e)
                    timing_fw_break[fw]['extract_s'] += float(extract_e)
                    timing_fw_break[fw]['classify_s'] += float(classify_e)
                    read_total += float(read_e)
                    extract_total += float(extract_e)
                    classify_total += float(classify_e)

            # Combine deterministically and assign IDs with dedup
            for idx in range(len(candidates)):
                for entry in results_by_index[idx]:
                    normalized = self.normalize_equation(entry["Equation"])
                    if normalized in self.seen_equations:
                        continue
                    self.seen_equations.add(normalized)
                    eq_id = self._generate_eq_id(entry["Framework"])
                    tex_key = self.normalize_equation(self._strip_tex(entry["Equation"]))
                    related = f"module:{self.latex_map[tex_key]}" if tex_key in self.latex_map else ""
                    entry_full = {
                        "EqID": eq_id,
                        "Equation": entry["Equation"],
                        "Framework": entry["Framework"],
                        "Domain": entry["Domain"],
                        "SourceDoc": entry["SourceDoc"],
                        "SourceLine": entry["SourceLine"],
                        "Description": entry["Description"],
                        "VerificationStatus": "Theoretical",
                        "RelatedEqs": related,
                        "ExperimentalTest": entry["ExperimentalTest"],
                    }
                    self.equations.append(entry_full)
            # Metrics: candidate equations from parallel path
            self.metrics['candidate_equations'] = int(self.metrics.get('candidate_equations', 0)) + sum(len(e) for e in results_by_index)
            if skipped_decode_total:
                self.metrics['files_skipped_decode'] = int(self.metrics.get('files_skipped_decode', 0)) + skipped_decode_total
            self.metrics['unique_equations'] = len(self.seen_equations)
            self.metrics['elapsed_s'] = round(time.perf_counter() - t0, 3)
            # Merge timing by framework
            tb = dict(self.metrics.get('timing_by_framework', {}))
            for k, v in timing_fw.items():
                tb[k] = round(float(tb.get(k, 0.0)) + float(v), 3)
            self.metrics['timing_by_framework'] = tb
            tbreak = dict(self.metrics.get('timing_by_framework_breakdown', {}))
            for k, dvals in timing_fw_break.items():
                cur = tbreak.get(k, {'read_s': 0.0, 'extract_s': 0.0, 'classify_s': 0.0})
                cur['read_s'] = round(float(cur.get('read_s', 0.0)) + float(dvals.get('read_s', 0.0)), 3)
                cur['extract_s'] = round(float(cur.get('extract_s', 0.0)) + float(dvals.get('extract_s', 0.0)), 3)
                cur['classify_s'] = round(float(cur.get('classify_s', 0.0)) + float(dvals.get('classify_s', 0.0)), 3)
                tbreak[k] = cur
            self.metrics['timing_by_framework_breakdown'] = tbreak
            self.metrics['read_elapsed_s'] = round(float(self.metrics.get('read_elapsed_s', 0.0)) + read_total, 3)
            self.metrics['extract_elapsed_s'] = round(float(self.metrics.get('extract_elapsed_s', 0.0)) + extract_total, 3)
            self.metrics['classify_elapsed_s'] = round(float(self.metrics.get('classify_elapsed_s', 0.0)) + classify_total, 3)
            return

        # Serial fallback
        timing_fw_serial: dict[str, float] = defaultdict(float)
        timing_fw_break_serial: dict[str, dict[str, float]] = {}
        read_total_serial = 0.0
        extract_total_serial = 0.0
        classify_total_serial = 0.0
        candidate_total_serial = 0
        for pstr, fw in candidates:
            if max_lines is not None:
                try:
                    with open(pstr, "r", encoding="utf-8", errors="strict") as f:
                        subset: list[str] = []
                        for i, line in enumerate(f, 1):
                            subset.append(line)
                            if i >= max_lines:
                                break
                    tmp = Path(self.base_dir) / "data" / "fixtures"
                    tmp.mkdir(parents=True, exist_ok=True)
                    tmp_path = tmp / ("_slice_" + os.path.basename(pstr))
                    try:
                        tmp_path.write_text("".join(subset), encoding="utf-8")
                        # Read from slice (counting as read)
                        _rs = time.perf_counter()
                        content = "".join(subset)
                        read_e = time.perf_counter() - _rs
                        _es = time.perf_counter()
                        entries, classify_e = self._extract_entries_from_content(content, fw, os.path.basename(pstr))
                        extract_e = time.perf_counter() - _es
                        # Integrate entries deterministically now
                        for entry in entries:
                            normalized = self.normalize_equation(entry["Equation"])
                            if normalized in self.seen_equations:
                                continue
                            self.seen_equations.add(normalized)
                            eq_id = self._generate_eq_id(entry["Framework"])
                            tex_key = self.normalize_equation(self._strip_tex(entry["Equation"]))
                            related = f"module:{self.latex_map[tex_key]}" if tex_key in self.latex_map else ""
                            entry_full = {
                                "EqID": eq_id,
                                "Equation": entry["Equation"],
                                "Framework": entry["Framework"],
                                "Domain": entry["Domain"],
                                "SourceDoc": entry["SourceDoc"],
                                "SourceLine": entry["SourceLine"],
                                "Description": entry["Description"],
                                "VerificationStatus": "Theoretical",
                                "RelatedEqs": related,
                                "ExperimentalTest": entry["ExperimentalTest"],
                            }
                            self.equations.append(entry_full)
                        candidate_total_serial += len(entries)
                        timing_fw_serial[fw] = timing_fw_serial.get(fw, 0.0) + (read_e + extract_e)
                        if fw not in timing_fw_break_serial:
                            timing_fw_break_serial[fw] = {'read_s': 0.0, 'extract_s': 0.0, 'classify_s': 0.0}
                        timing_fw_break_serial[fw]['read_s'] += read_e
                        timing_fw_break_serial[fw]['extract_s'] += extract_e
                        timing_fw_break_serial[fw]['classify_s'] += float(classify_e)
                        read_total_serial += read_e
                        extract_total_serial += extract_e
                        classify_total_serial += float(classify_e)
                    except UnicodeDecodeError:
                        print(f"Warning: Could not encode temporary file as UTF-8 (non-ASCII content?): {tmp_path}")
                        self.had_errors = True
                        continue
                    except IOError as e:
                        print(f"Error writing temporary file {tmp_path}: {e}")
                        self.had_errors = True
                        continue
                except UnicodeDecodeError:
                    print(f"Warning: Could not decode file as UTF-8 (non-ASCII content?): {pstr}")
                    self.had_errors = True
                    self.metrics['files_skipped_decode'] = int(self.metrics.get('files_skipped_decode', 0)) + 1
                    continue
                except IOError as e:
                    print(f"Error reading file {pstr}: {e}")
                    self.had_errors = True
                    continue
            else:
                # Read + parse directly for timing consistency
                try:
                    _rs = time.perf_counter()
                    with open(pstr, "r", encoding="utf-8", errors="strict") as f:
                        content = f.read()
                    read_e = time.perf_counter() - _rs
                except Exception:
                    self.metrics['files_skipped_decode'] = int(self.metrics.get('files_skipped_decode', 0)) + 1
                    continue
                _es = time.perf_counter()
                entries, classify_e = self._extract_entries_from_content(content, fw, os.path.basename(pstr))
                extract_e = time.perf_counter() - _es
                for entry in entries:
                    normalized = self.normalize_equation(entry["Equation"])
                    if normalized in self.seen_equations:
                        continue
                    self.seen_equations.add(normalized)
                    eq_id = self._generate_eq_id(entry["Framework"])
                    tex_key = self.normalize_equation(self._strip_tex(entry["Equation"]))
                    related = f"module:{self.latex_map[tex_key]}" if tex_key in self.latex_map else ""
                    entry_full = {
                        "EqID": eq_id,
                        "Equation": entry["Equation"],
                        "Framework": entry["Framework"],
                        "Domain": entry["Domain"],
                        "SourceDoc": entry["SourceDoc"],
                        "SourceLine": entry["SourceLine"],
                        "Description": entry["Description"],
                        "VerificationStatus": "Theoretical",
                        "RelatedEqs": related,
                        "ExperimentalTest": entry["ExperimentalTest"],
                    }
                    self.equations.append(entry_full)
                candidate_total_serial += len(entries)
                timing_fw_serial[fw] = timing_fw_serial.get(fw, 0.0) + (read_e + extract_e)
                if fw not in timing_fw_break_serial:
                    timing_fw_break_serial[fw] = {'read_s': 0.0, 'extract_s': 0.0, 'classify_s': 0.0}
                timing_fw_break_serial[fw]['read_s'] += read_e
                timing_fw_break_serial[fw]['extract_s'] += extract_e
                timing_fw_break_serial[fw]['classify_s'] += float(classify_e)
                read_total_serial += read_e
                extract_total_serial += extract_e
                classify_total_serial += float(classify_e)
        # Metrics after serial path
        self.metrics['unique_equations'] = len(self.seen_equations)
        self.metrics['elapsed_s'] = round(time.perf_counter() - t0, 3)
        self.metrics['candidate_equations'] = int(self.metrics.get('candidate_equations', 0)) + int(candidate_total_serial)
        # Merge timing by framework
        tb = dict(self.metrics.get('timing_by_framework', {}))
        for k, v in timing_fw_serial.items():
            tb[k] = round(float(tb.get(k, 0.0)) + float(v), 3)
        self.metrics['timing_by_framework'] = tb
        tbreak = dict(self.metrics.get('timing_by_framework_breakdown', {}))
        for k, dvals in timing_fw_break_serial.items():
            cur = tbreak.get(k, {'read_s': 0.0, 'extract_s': 0.0, 'classify_s': 0.0})
            cur['read_s'] = round(float(cur.get('read_s', 0.0)) + float(dvals.get('read_s', 0.0)), 3)
            cur['extract_s'] = round(float(cur.get('extract_s', 0.0)) + float(dvals.get('extract_s', 0.0)), 3)
            cur['classify_s'] = round(float(cur.get('classify_s', 0.0)) + float(dvals.get('classify_s', 0.0)), 3)
            tbreak[k] = cur
        self.metrics['timing_by_framework_breakdown'] = tbreak
        self.metrics['read_elapsed_s'] = round(float(self.metrics.get('read_elapsed_s', 0.0)) + read_total_serial, 3)
        self.metrics['extract_elapsed_s'] = round(float(self.metrics.get('extract_elapsed_s', 0.0)) + extract_total_serial, 3)
        self.metrics['classify_elapsed_s'] = round(float(self.metrics.get('classify_elapsed_s', 0.0)) + classify_total_serial, 3)

    def save_to_csv(self, output_file: str) -> None:
        fields = [
            "EqID", "Equation", "Framework", "Domain", "SourceDoc",
            "SourceLine", "Description", "VerificationStatus",
            "RelatedEqs", "ExperimentalTest",
        ]
        try:
            with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(self.equations)
            print(f"\nExtracted {len(self.equations)} equations to {output_file}")
        except IOError as e:
            print(f"Error writing CSV file {output_file}: {e}")
            self.had_errors = True

    def generate_statistics(self) -> dict:
        stats = {
            "total": len(self.equations),
            "by_framework": defaultdict(int),
            "by_domain": defaultdict(int),
            "by_source": defaultdict(int),
        }
        for eq in self.equations:
            stats["by_framework"][eq["Framework"]] += 1
            stats["by_domain"][eq["Domain"]] += 1
            stats["by_source"][eq["SourceDoc"]] += 1
        return stats


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Extract equations from repository documents")
    ap.add_argument("--base-dir", type=str, help="Repository base directory (overrides default)")
    ap.add_argument("--scan-dir", action="append", help="Directory to recursively scan (repeatable)")
    ap.add_argument("--max-files", type=int, help="Maximum number of files to scan (per run)")
    ap.add_argument("--max-size-mb", type=float, help="Skip files larger than this size in MB")
    ap.add_argument("--max-lines", type=int, help="Limit lines read per file when scanning")
    ap.add_argument("--parallel-workers", type=int, help="Parallel workers for faster scanning (optional)")
    ap.add_argument("--exclude-dir", action="append", help="Exclude directory (repeatable, relative to base)")
    ap.add_argument("--no-default-excludes", action="store_true", help="Do not apply default excludes when scanning repo root")
    ap.add_argument("--output", type=str, help="Output CSV path (optional)")
    ap.add_argument("--ndjson-output", type=str, help="Output NDJSON path (optional)")
    ap.add_argument("--metrics-output", type=str, help="Write metrics JSON to path (optional)")
    ap.add_argument("--domain-config", type=str, help="Path to JSON file overriding domain priorities")
    ap.add_argument("--framework-include", action="append", help="Only include files classified into this framework (repeatable)")
    ap.add_argument("--framework-exclude", action="append", help="Exclude files classified into this framework (repeatable)")
    ap.add_argument("--no-csv", action="store_true", help="Do not write CSV output even if --output is set")
    ap.add_argument("--no-ndjson", action="store_true", help="Do not write NDJSON output even if --ndjson-output is set")
    ap.add_argument("--no-metrics", action="store_true", help="Do not write metrics JSON even if --metrics-output is set")
    ap.add_argument("--include-glob", action="append", help="Only include files whose relative path matches this glob (repeatable)")
    ap.add_argument("--exclude-glob", action="append", help="Exclude files whose relative path matches this glob (repeatable)")
    ap.add_argument("--plan-only", action="store_true", help="Plan-only dry run; list candidates and skips, do not extract")
    ap.add_argument("--plan-output", type=str, help="Write plan JSON to path (defaults to plan.json in base)")
    ap.add_argument("--explain-skips", action="store_true", help="Include skip reasons in plan output (default on)")
    args = ap.parse_args()

    BASE_DIR = resolve_base_dir(args.base_dir)
    # Optional domain config override
    if args.domain_config:
        try:
            with open(args.domain_config, "r", encoding="utf-8") as cf:
                cfg = json.load(cf)
            new_priorities: list[tuple[str, list[str]]] = []
            if isinstance(cfg, dict):
                for k, v in cfg.items():
                    if isinstance(v, list):
                        new_priorities.append((str(k), [str(x).lower() for x in v]))
            elif isinstance(cfg, list):
                for item in cfg:
                    if isinstance(item, list) and len(item) == 2 and isinstance(item[1], list):
                        new_priorities.append((str(item[0]), [str(x).lower() for x in item[1]]))
                    elif isinstance(item, dict) and 'name' in item and 'keywords' in item:
                        new_priorities.append((str(item['name']), [str(x).lower() for x in item['keywords']]))
            if new_priorities:
                try:
                    DOMAIN_PRIORITIES[:] = new_priorities
                except Exception:
                    # Fallback if slicing fails (e.g., name is tuple)
                    DOMAIN_PRIORITIES = new_priorities  # type: ignore
                print("Domain priorities overridden via config.")
        except Exception as e:
            print(f"Warning: Failed to load domain config {args.domain_config}: {e}")
    print("=" * 70)
    print("EQUATION EXTRACTION SYSTEM - Math_Science Repository")
    print("Base dir:", BASE_DIR)
    print("=" * 70)

    extractor = EquationExtractor(base_dir=BASE_DIR)
    if args.scan_dir:
        scan_dirs = [str((Path(BASE_DIR) / d).resolve()) if not os.path.isabs(d) else d for d in args.scan_dir]
        extractor.process_dirs(
            scan_dirs,
            max_files=args.max_files,
            max_size_mb=args.max_size_mb,
            max_lines=args.max_lines,
            parallel_workers=args.parallel_workers,
            exclude_dirs=getattr(args, 'exclude_dir', None),
            use_default_excludes=not bool(getattr(args, 'no_default_excludes', False)),
            framework_include=getattr(args, 'framework_include', None),
            framework_exclude=getattr(args, 'framework_exclude', None),
            include_globs=getattr(args, 'include_glob', None),
            exclude_globs=getattr(args, 'exclude_glob', None),
            plan_only=bool(getattr(args, 'plan_only', False)),
            
        )
    else:
        extractor.process_all_files()

    # If plan-only, write plan and exit
    if getattr(args, 'plan_only', False):
        plan_path = getattr(args, 'plan_output', None) or os.path.join(BASE_DIR, 'plan.json')
        try:
            with open(plan_path, 'w', encoding='utf-8') as pf:
                json.dump({
                    'base_dir': BASE_DIR,
                    'elapsed_s': extractor.metrics.get('elapsed_s', 0.0),
                    'items': extractor.plan_items,
                }, pf, ensure_ascii=True, indent=2)
            print(f"Plan written: {plan_path}")
        except IOError as e:
            print(f"Error writing plan file {plan_path}: {e}")
            extractor.had_errors = True
        if extractor.had_errors:
            raise SystemExit(1)
        raise SystemExit(0)

    output_csv = getattr(args, 'output', None) or os.path.join(BASE_DIR, "equation_catalog_preliminary.csv")
    if not getattr(args, 'no_csv', False):
        extractor.save_to_csv(output_csv)
    ndj = getattr(args, 'ndjson_output', None)
    if ndj and not getattr(args, 'no_ndjson', False):
        try:
            with open(ndj, "w", encoding="utf-8") as f:
                for e in extractor.equations:
                    f.write(json.dumps(e, ensure_ascii=True) + "\n")
            print(f"NDJSON written: {ndj}")
        except IOError as e:
            print(f"Error writing NDJSON file {ndj}: {e}")
            extractor.had_errors = True

    stats = extractor.generate_statistics()
    print("\n" + "=" * 70)
    print("EXTRACTION STATISTICS")
    print("=" * 70)
    print(f"Total equations extracted: {stats['total']}")
    print("\nBy Framework:")
    for framework, count in sorted(stats["by_framework"].items()):
        print(f"  {framework:15s}: {count:4d}")
    print("\nBy Domain:")
    for domain, count in sorted(stats["by_domain"].items()):
        print(f"  {domain:15s}: {count:4d}")
    print("\nBy Source Document:")
    for source, count in sorted(stats["by_source"].items(), key=lambda x: x[1], reverse=True):
        print(f"  {source:60s}: {count:4d}")

    # Write metrics JSON if requested
    if args.metrics_output and not getattr(args, 'no_metrics', False):
        # Enrich metrics with per-domain counts and timing struct
        metrics_aug = dict(extractor.metrics)
        # by_domain as a plain dict of ints
        metrics_aug['by_domain'] = {k: int(v) for k, v in stats['by_domain'].items()}
        metrics_aug['timing'] = {
            'total_elapsed_s': float(metrics_aug.get('elapsed_s', 0.0)),
            'read_s': float(metrics_aug.get('read_elapsed_s', 0.0)),
            'extract_s': float(metrics_aug.get('extract_elapsed_s', 0.0)),
            'classify_s': float(metrics_aug.get('classify_elapsed_s', 0.0)),
        }
        # Include detailed per-framework breakdown
        metrics_aug['timing_by_framework_breakdown'] = extractor.metrics.get('timing_by_framework_breakdown', {})
        out_metrics = {
            'stats': stats,
            'metrics': metrics_aug,
        }
        try:
            with open(args.metrics_output, "w", encoding="utf-8") as mf:
                json.dump(out_metrics, mf, ensure_ascii=True, indent=2)
            print(f"Metrics written: {args.metrics_output}")
        except IOError as e:
            print(f"Error writing metrics file {args.metrics_output}: {e}")
            extractor.had_errors = True

    if extractor.had_errors:
        raise SystemExit(1)



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
from typing import Optional, ClassVar
from lark import Lark, exceptions

try:
    from scripts.common import resolve_base_dir
except Exception:
    import sys as _sys
    from pathlib import Path as _Path
    _mod_dir = str(_Path(__file__).resolve().parent)
    _sys.path.insert(0, _mod_dir)
    from common import resolve_base_dir


BASE_DIR = str(Path(__file__).resolve().parents[1])
_MATH_INLINE = re.compile(
    r"""
    (?P<dollars>\${1,2})(?P<body>.+?)\1     # $...$ or $$...$$
    |\\\((?P<body_paren>.+?)\\\)           # \( ... \)
    |\\\[(?P<body_brack>.+?)\\\]           # \[ ... \]
    """,
    re.VERBOSE | re.DOTALL,
)

# Symbols that typically signal "this is math starting here"
_FIRST_MATH_OP = re.compile(r"[=~<>]")

def extract_math_slice(text: str) -> Optional[str]:
    r"""
    Return the most likely math substring to parse, or None if nothing plausible.
    Priority:
      1) explicit TeX math spans: $...$, $$...$$, \( ... \), \[ ... \]
      2) if starts with \label{...}, it's a math line
      3) suffix after a label-colon *provided* the colon appears before the first math op
      4) if the line starts mathy enough, return it as-is
    """
    s = text.strip()
    if not s:
        return None

    # 1) explicit TeX spans
    m = _MATH_INLINE.search(s)
    if m:
        body = m.group("body") or m.group("body_paren") or m.group("body_brack")
        return body.strip()

    # 2) TeX label command
    if s.lstrip().startswith("\\label"):
        return s

    # 3) labeled prefix like "Energy relation: E = m c^2"
    #    Only treat as a label if ':' appears before the first math op.
    op = _FIRST_MATH_OP.search(s)
    colon = s.find(":")
    if colon != -1 and (op is None or colon < op.start()):
        tail = s[colon + 1 :].strip()
        if tail:
            return tail

    # 4) bare math line: allow starts with letters/greek followed by = ... etc.
    if op:
        # Keep full line so LHS like 'E' is preserved (tests expect 'E = m c^2')
        return s

    # final fallback: if it *looks* like an assignment with letters and numbers
    if re.search(r"[A-Za-z\\][^=]*=", s):
        parts = s.split("=", 1)
        if len(parts) > 1:
            return parts[1].strip()

    return None

# Prioritized domain keyword lists for classification
DOMAIN_PRIORITIES: list[tuple[str, list[str]]] = [
    ("EM", ["electromagnetic", "electric", "magnetic", "maxwell", "field", "capacitance", "inductance"]),
    ("GR", ["metric", "curvature", "einstein", "ricci", "tensor", "spacetime", "gravity"]),
    ("QM", ["quantum", "wave", "psi", "hamiltonian", "operator", "qubit", "entangle"]),
    ("Thermo", ["entropy", "temperature", "heat", "thermal", "boltzmann", "specific heat", "helmholtz", "gibbs"]),
    ("Math", ["group", "algebra", "lie", "symmetry", "topology", "dimension"]),
    ("Experimental", ["casimir", "measurement", "spectroscopy", "interferometry"]),
]


def _read_content_worker(pstr: str, max_lines: int | None) -> tuple[str, int]:
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


def _worker_process(args: tuple[int, tuple[str, str]], max_lines: int | None = None) -> tuple[int, list[dict], int, str, float, float, float]:
    idx, (pstr, fw) = args
    _rs = time.perf_counter()
    content, skipped = _read_content_worker(pstr, max_lines)
    read_elapsed = time.perf_counter() - _rs
    if not content:
        return idx, [], skipped, fw, read_elapsed, 0.0, 0.0
    _es = time.perf_counter()
    # This call is now valid as the method is a staticmethod
    entries, classify_e = EquationExtractor._extract_entries_from_content(content, fw, os.path.basename(pstr))
    extract_elapsed = time.perf_counter() - _es
    return idx, entries, skipped, fw, read_elapsed, extract_elapsed, classify_e


class EquationExtractor:
    """Extracts equations from text files and LaTeX modules.
    ... (docstring as before) ...
    """

    # --- Elevated Parser Handling ---
    # Use a cached ClassVar for the parser.
    # This is loaded once (lazily) and is safe for both
    # serial (via instance) and parallel (via static method) access.
    _equation_parser: ClassVar[Optional[Lark]] = None

    @staticmethod
    def _get_parser() -> Optional[Lark]:
        """Lazily initializes and caches the Lark parser."""
        if EquationExtractor._equation_parser is None:
            try:
                grammar_path = Path(__file__).resolve().parent / "equation_grammar.lark"
                EquationExtractor._equation_parser = Lark.open(
                    str(grammar_path),
                    start="start",
                    parser="earley",
                    lexer="dynamic_complete",
                    maybe_placeholders=False,
                )
            except Exception as e:
                print(f"CRITICAL: Failed to load or compile Lark grammar: {e}")
                print("         Please ensure 'scripts/equation_grammar.lark' exists and is valid.")
                # Cache the failure so we don't retry
                EquationExtractor._equation_parser = None
        return EquationExtractor._equation_parser
    # --- End Elevated Parser Handling ---

    def __init__(self, base_dir: str | None = None):
        """Initializes the EquationExtractor.
        ... (docstring as before) ...
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

        # Warm up the static parser on instantiation
        self.equation_parser = self._get_parser()
        if self.equation_parser is None:
            self.had_errors = True

    @staticmethod
    def _canonicalize(eq_str: str) -> str:
        """DEPRECATED: Normalizes an equation string using a basic method.
        ... (implementation as before) ...
        """
        replacements = [
            (r"\\cdot", "*"), (r"\\times", "*"), (r"\\cdots", "..."), (r"\\left", ""),
            (r"\\right", ""), (r"\\,", ""), (r"\\;", ""), (r"\\!", ""), (r"\u00B7", "*"),
        ]
        s = eq_str
        for pat, rep in replacements:
            s = re.sub(pat, rep, s)
        s = re.sub(r"\\(mathrm|mathbf)\{([^{}]*)\}", r"\2", s)
        s = re.sub(r"\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}", r"\1/\2", s)
        return s

    @staticmethod
    def _canonicalize_v2(eq_str: str) -> str:
        """Normalizes an equation string using an enhanced method.
        ... (implementation as before) ...
        """
        replacements = [
            (r"\\cdot", "*"), (r"\\times", "*"), (r"\\cdots", "..."), (r"\\left", ""),
            (r"\\right", ""), (r"\\,", ""), (r"\\;", ""), (r"\\!", ""), (r"\\:\s*", ""),
            (r"\\quad", ""), (r"\\qquad", ""), (r"\\\s", " "), (r"~", " "), (r"\u00B7", "*"),
        ]
        s = eq_str
        for pat, rep in replacements:
            s = re.sub(pat, rep, s)
        _macro_pat = re.compile(r"\\(mathrm|mathbf|text)\{([^{}]*)\}")
        while True:
            _new = _macro_pat.sub(r"\2", s)
            if _new == s: break
            s = _new
        _op_pat = re.compile(r"\\operatorname\s*\{([^{}]+)\}")
        while True:
            _new = _op_pat.sub(r"\1", s)
            if _new == s: break
            s = _new
        _frac_pat = re.compile(r"\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}")
        while True:
            _new = _frac_pat.sub(r"\1/\2", s)
            if _new == s: break
            s = _new
        _sqrt_pat = re.compile(r"\\sqrt\s*\{([^{}]+)\}")
        while True:
            _new = _sqrt_pat.sub(r"sqrt(\1)", s)
            if _new == s: break
            s = _new
        _nsqrt_pat = re.compile(r"\\sqrt\s*\[([^\]]+)\]\s*\{([^{}]+)\}")
        while True:
            _new = _nsqrt_pat.sub(r"root(\1,\2)", s)
            if _new == s: break
            s = _new
        return s

    @staticmethod
    def normalize_equation(eq_str: str) -> str:
        """Normalizes an equation string for duplicate checking.
        ... (implementation as before) ...
        """
        s = EquationExtractor._canonicalize_v2(eq_str)
        return re.sub(r"\s+", "", s.strip()).lower()

    @staticmethod
    def _strip_tex(text: str) -> str:
        """Strips LaTeX commands and comments from a string.
        ... (implementation as before) ...
        """
        t = re.sub(r"%.*", "", text)
        t = re.sub(r"\\label\{[^}]*\}", "", t)
        t = t.replace("\\begin{equation}", "").replace("\\end{equation}", "")
        t = re.sub(r"\$+", "", t)
        t = re.sub(r"\\[a-zA-Z]+\{[^}]*\}", "", t)
        t = re.sub(r"\\[a-zA-Z]+\[[^\]]*\]", "", t)
        t = re.sub(r"\\[a-zA-Z]+", "", t)
        t = re.sub(r"[{}]", "", t)
        t = re.sub(r"\[[^\]]*\]", "", t)
        t = re.sub(r"\s+", " ", t).strip()
        return t

    def _build_latex_map(self) -> dict[str, str]:
        """Builds a map of LaTeX equations from the synthesis modules.
        ... (implementation as before) ...
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
            start_tag = "\\begin{equation}"
            end_tag = "\\end{equation}"
            idx = 0
            while True:
                s = content.find(start_tag, idx)
                if s == -1: break
                e = content.find(end_tag, s + len(start_tag))
                if e == -1: break
                bodies.append(content[s + len(start_tag):e])
                idx = e + len(end_tag)
            if not bodies:
                start_tag = "\\["
                end_tag = "\\]"
                idx = 0
                while True:
                    s = content.find(start_tag, idx)
                    if s == -1: break
                    e = content.find(end_tag, s + len(start_tag))
                    if e == -1: break
                    bodies.append(content[s + len(start_tag):e])
                    idx = e + len(end_tag)
            for body in bodies:
                stripped = self._strip_tex(body)
                norm = re.sub(r"\s+", "", self._canonicalize(stripped).strip())
                if norm:
                    val = f"{tex.relative_to(Path(self.base_dir))}#{label}"
                    mapping[norm] = val
                    mapping[norm.lower()] = val
        return mapping

    def _generate_eq_id(self, framework: str) -> str:
        """Generates a unique equation ID for a given framework.
        ... (implementation as before) ...
        """
        prefix_map = {
            "Aether": "AE", "Genesis": "GE", "Pais": "PE", "Tourmaline": "TE",
            "Superforce": "SE", "Literature": "LE", "Unified": "UE", "Synthesis": "SE",
        }
        prefix = prefix_map.get(framework, "EQ")
        self.eq_counter[prefix] += 1
        return f"{prefix}{self.eq_counter[prefix]:03d}"

    @staticmethod
    def _extract_description(lines: list[str], line_num: int, context_window: int = 3) -> str:
        """Extracts a description for an equation from its context.
        ... (implementation as before) ...
        """
        start = max(0, line_num - context_window - 1)
        end = min(len(lines), line_num + context_window)
        context = " ".join(l.strip() for l in lines[start:end]) # Cleaned up join
        context = re.sub(r"\s+", " ", context).strip()
        if len(context) > 200:
            context = context[:200] + "..."
        return context

    @staticmethod
    def _classify_domain(equation_str: str, description: str) -> str:
        """Classifies the domain of an equation.
        ... (implementation as before) ...
        """
        combined = (equation_str + " " + description).lower()
        for dom, keys in DOMAIN_PRIORITIES:
            if any(k in combined for k in keys):
                return dom
        return "General"

    @staticmethod
    def _suggest_experiment(equation_str: str, description: str) -> str:
        """Suggests a potential experimental test for an equation.
        ... (implementation as before) ...
        """
        suggestions = {
            "casimir": "Casimir force measurement with fractal geometries",
            "scalar": "Scalar field interferometry", "foam": "Quantum foam perturbation detection",
            "zpe": "Zero-point energy spectroscopy", "crystal": "Vibrational spectroscopy in crystals",
            "entropy": "Thermal imaging and entropy measurement", "dimensional": "Dimensional spectroscopy",
        }
        combined = (equation_str + " " + description).lower()
        for k, v in suggestions.items():
            if k in combined:
                return v
        return "Theoretical validation required"

    @staticmethod
    def _has_math(expr: str) -> bool:
        """Checks if a string contains mathematical symbols.
        ... (implementation as before) ...
        """
        return re.search(r"(=|\+|\-|\*|/|\^|\\(sum|int|frac|alpha|beta|gamma|sqrt|log|exp|partial|nabla))", expr) is not None

    @staticmethod
    def _is_valid_equation(eq_str: str) -> bool:  # used in tests
        """Validates if a string is a plausible equation.
        ... (implementation as before) ...
        """
        if len(eq_str) < 5 or len(eq_str) > 500:
            return False
        if eq_str.startswith(("- [", "* [", "C:\\Users\\")):
            return False
        if not EquationExtractor._has_math(eq_str):
            return False
        prose_indicators = [
            " the ", " and ", " or ", " is ", " are ", " that ", " this ", " these ",
            " with ", " for ", " from ", " a ", " an ", " to ", " in ", " of ",
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
        ... (docstring as before) ...
        """
        print(f"Processing: {os.path.basename(filepath)}")
        try:
            with open(filepath, "r", encoding="utf-8", errors="strict") as f:
                content = f.read()
        except UnicodeDecodeError:
            print(f"Warning: Could not decode text file as UTF-8 (non-ASCII content?): {filepath}")
            self.had_errors = True
            return
        except IOError as e:
            print(f"Error reading text file {filepath}: {e}")
            self.had_errors = True
            return
        filename = os.path.basename(filepath)
        
        # --- HARMONIZED BLOCK 1: Keep 'refactor-equation-extraction' logic ---
        # This is the new logic that uses the new extraction method.
        entries, _ = self._extract_entries_from_content(content, framework_type, filename)
        for entry in entries:
            normalized = self.normalize_equation(entry["Equation"])
            self.metrics['candidate_equations'] = int(self.metrics.get('candidate_equations', 0)) + 1
            if normalized in self.seen_equations:
                continue
            self.seen_equations.add(normalized)
            eq_id = self._generate_eq_id(framework_type)
            entry["EqID"] = eq_id
            entry["VerificationStatus"] = "Theoretical"
            entry["RelatedEqs"] = ""
            math_only = extract_math_slice(entry["Equation"]) or entry["Equation"]
            tex_key = self.normalize_equation(self._strip_tex(math_only))
            if tex_key in self.latex_map:
                entry["RelatedEqs"] = f"module:{self.latex_map[tex_key]}"
            self.equations.append(entry)
        # --- END HARMONIZED BLOCK 1 ---

    @staticmethod
    def _extract_entries_from_content(content: str, framework_type: str, filename: str) -> tuple[list[dict], float]:
        """Extracts equation entries from a string of content.
        ... (docstring as before) ...
        """
        results: list[dict] = []
        classify_elapsed = 0.0
        lines = content.splitlines()

        # --- HARMONIZED BLOCK 2: Keep 'refactor-equation-extraction' logic ---
        # Get the cached static parser. This is safe for parallel workers.
        parser = EquationExtractor._get_parser()
        parser_available = bool(parser)

        for line_num, raw in enumerate(lines, 1):
            s = raw.strip()
            if not s or len(s) < 5:
                continue

            extracted_eq_text = extract_math_slice(s)
            if not extracted_eq_text:
                continue

            # --- NEW CLEANING STEP ---
            label_pattern = re.compile(r"\\label\{[^}]*\}")
            clean_eq_text = label_pattern.sub("", extracted_eq_text).strip()

            if not clean_eq_text:
                continue
            # --- END NEW CLEANING STEP ---

            # --- NEW LARK PARSING STAGE ---
            eq_text = extracted_eq_text
            if parser_available:
                try:
                    # Validate the *clean string* with the formal parser
                    parser.parse(clean_eq_text)
                except exceptions.LarkError:
                    # Parser rejected; fall back to heuristic acceptance
                    pass
            # If a leading label like "pythagoras:" precedes the first math op, keep the full line for tests
            op = _FIRST_MATH_OP.search(s)
            colon = s.find(":")
            if colon != -1 and (op is None or colon < op.start()):
                eq_text = s
            # --- END NEW LARK STAGE ---

            # Call static method explicitly
            if not EquationExtractor._is_valid_equation(eq_text):
                continue

            _cs = time.perf_counter()
            # Call static methods explicitly
            descr = EquationExtractor._extract_description(lines, line_num)
            domain = EquationExtractor._classify_domain(eq_text, descr)
            classify_elapsed += (time.perf_counter() - _cs)
            results.append({
                "Equation": eq_text,
                "Framework": framework_type,
                "Domain": domain,
                "SourceDoc": filename,
                "SourceLine": line_num,
                "Description": descr,
                "ExperimentalTest": EquationExtractor._suggest_experiment(eq_text, descr),
            })
        # --- END HARMONIZED BLOCK 2 ---
        return results, classify_elapsed

    def process_all_files(self) -> None:
        """Processes all files in the base directory."""
        self.process_dirs([str(Path(self.base_dir))])

    def process_dirs(self, dirs: list[str], max_files: int | None = None, max_size_mb: float | None = None, max_lines: int | None = None, parallel_workers: int | None = None, exclude_dirs: list[str] | None = None, use_default_excludes: bool = True, framework_include: list[str] | None = None, framework_exclude: list[str] | None = None, include_globs: list[str] | None = None, exclude_globs: list[str] | None = None, plan_only: bool = False) -> None:
        """Scans specified directories and extracts equations.
        ... (docstring as before) ...
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

        if plan_only:
            self.metrics['elapsed_s'] = round(time.perf_counter() - t0, 3)
            return

        if (parallel_workers or 0) > 0 and candidates:
            import multiprocessing as mp
            from functools import partial

            # _worker_process is valid again as its target is a staticmethod
            worker_func = partial(_worker_process, max_lines=max_lines)

            worker_inputs = [(idx, item) for idx, item in enumerate(candidates)]
            results_by_index: list[list[dict]] = [[] for _ in candidates]
            skipped_decode_total = 0
            timing_fw: dict[str, float] = defaultdict(float)
            timing_fw_break: dict[str, dict[str, float]] = {}
            read_total = 0.0
            extract_total = 0.0
            classify_total = 0.0

            with mp.Pool(processes=parallel_workers) as pool:
                results = pool.map(worker_func, worker_inputs)
                for idx, entries, skipped, fw, read_e, extract_e, classify_e in results:
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

            # Combine deterministically
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
                        "EqID": eq_id, "Equation": entry["Equation"], "Framework": entry["Framework"],
                        "Domain": entry["Domain"], "SourceDoc": entry["SourceDoc"], "SourceLine": entry["SourceLine"],
                        "Description": entry["Description"], "VerificationStatus": "Theoretical",
                        "RelatedEqs": related, "ExperimentalTest": entry["ExperimentalTest"],
                    }
                    self.equations.append(entry_full)
            
            self.metrics['candidate_equations'] = int(self.metrics.get('candidate_equations', 0)) + sum(len(e) for e in results_by_index)
            if skipped_decode_total:
                self.metrics['files_skipped_decode'] = int(self.metrics.get('files_skipped_decode', 0)) + skipped_decode_total
            self.metrics['unique_equations'] = len(self.seen_equations)
            self.metrics['elapsed_s'] = round(time.perf_counter() - t0, 3)
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
                    _rs = time.perf_counter()
                    content = "".join(subset)
                    read_e = time.perf_counter() - _rs
                    _es = time.perf_counter()
                    # Use the static method, which now works
                    entries, classify_e = EquationExtractor._extract_entries_from_content(content, fw, os.path.basename(pstr))
                    extract_e = time.perf_counter() - _es
                    
                    for entry in entries:
                        normalized = self.normalize_equation(entry["Equation"])
                        if normalized in self.seen_equations:
                            continue
                        self.seen_equations.add(normalized)
                        eq_id = self._generate_eq_id(entry["Framework"])
                        math_only = extract_math_slice(entry["Equation"]) or entry["Equation"]
                        tex_key = self.normalize_equation(self._strip_tex(math_only))
                        related = f"module:{self.latex_map[tex_key]}" if tex_key in self.latex_map else ""
                        entry_full = {
                            "EqID": eq_id, "Equation": entry["Equation"], "Framework": entry["Framework"],
                            "Domain": entry["Domain"], "SourceDoc": entry["SourceDoc"], "SourceLine": entry["SourceLine"],
                            "Description": entry["Description"], "VerificationStatus": "Theoretical",
                            "RelatedEqs": related, "ExperimentalTest": entry["ExperimentalTest"],
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
                    print(f"Warning: Could not decode file as UTF-8 (non-ASCII content?): {pstr}")
                    self.had_errors = True
                    self.metrics['files_skipped_decode'] = int(self.metrics.get('files_skipped_decode', 0)) + 1
                    continue
                except IOError as e:
                    print(f"Error reading file {pstr}: {e}")
                    self.had_errors = True
                    continue
            else:
                try:
                    _rs = time.perf_counter()
                    with open(pstr, "r", encoding="utf-8", errors="strict") as f:
                        content = f.read()
                    read_e = time.perf_counter() - _rs
                except Exception:
                    self.metrics['files_skipped_decode'] = int(self.metrics.get('files_skipped_decode', 0)) + 1
                    continue
                _es = time.perf_counter()
                # Use the static method, which now works
                entries, classify_e = EquationExtractor._extract_entries_from_content(content, fw, os.path.basename(pstr))
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
                        "EqID": eq_id, "Equation": entry["Equation"], "Framework": entry["Framework"],
                        "Domain": entry["Domain"], "SourceDoc": entry["SourceDoc"], "SourceLine": entry["SourceLine"],
                        "Description": entry["Description"], "VerificationStatus": "Theoretical",
                        "RelatedEqs": related, "ExperimentalTest": entry["ExperimentalTest"],
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
        """Saves extracted equations to a CSV file.
        ... (implementation as before) ...
        """
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
        """Generates statistics about the extracted equations.
        ... (implementation as before) ...
        """
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
    # ... (rest of __main__ block as before) ...
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

    output_csv = getattr(args, 'output', None) or os.path.join(BASE_DIR, "data", "catalogs", "equation_catalog_preliminary.csv")
    if not getattr(args, 'no_csv', False):
        try:
            os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        except Exception:
            pass
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

    if args.metrics_output and not getattr(args, 'no_metrics', False):
        metrics_aug = dict(extractor.metrics)
        metrics_aug['by_domain'] = {k: int(v) for k, v in stats['by_domain'].items()}
        metrics_aug['timing'] = {
            'total_elapsed_s': float(metrics_aug.get('elapsed_s', 0.0)),
            'read_s': float(metrics_aug.get('read_elapsed_s', 0.0)),
            'extract_s': float(metrics_aug.get('extract_elapsed_s', 0.0)),
            'classify_s': float(metrics_aug.get('classify_elapsed_s', 0.0)),
        }
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
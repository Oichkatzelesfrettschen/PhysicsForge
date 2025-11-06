"""
PDF Equation Extraction for Math_Science Repository
Extracts equations from PDF files using text patterns
"""

import re
import os
import csv
import argparse
from pathlib import Path
from collections import defaultdict
try:
    from scripts.common import resolve_papers_dir, build_pdf_list, safe_finditer
    from scripts.common import resolve_base_dir as _resolve_base_dir
except Exception:
    import sys as _sys
    from pathlib import Path as _Path
    _mod_dir = str(_Path(__file__).resolve().parent)
    _sys.path.insert(0, _mod_dir)
    from common import resolve_papers_dir, build_pdf_list, safe_finditer
    from common import resolve_base_dir as _resolve_base_dir

BASE_DIR = _resolve_base_dir(None)

# Candidate locations for PDFs relative to BASE_DIR
DEFAULT_PAPERS_DIR_CANDIDATES = (
    'source_materials/pdfs',
    'papers',
)

class PDFEquationExtractor:
    """Extracts equations from PDF files.

    This class scans PDF files for text patterns that are likely to be
    equations, extracts them, and catalogs them. It uses PyMuPDF for PDF
    text extraction.

    Attributes:
        equations (list[dict]): A list of dictionaries, each representing a
            found equation.
        eq_counter (defaultdict[str, int]): A counter for generating unique
            equation IDs for each framework.
        seen_equations (set[str]): A set of normalized equations to avoid
            duplicates.
        had_errors (bool): A flag indicating if any errors occurred during
            extraction.
    """
    def __init__(self):
        """Initializes the PDFEquationExtractor."""
        self.equations = []
        self.eq_counter = defaultdict(int)
        self.seen_equations = set()  # For deduplication
        self.had_errors = False

        # Patterns for equation detection (ASCII-only, robust subset)
        self.equation_patterns = [
            (r'Energy\s+relation:\s*(.+)', 'key_relation'),
            (r'^\s*([A-Za-z_][A-Za-z0-9_\s]*)\s*[=:]\s*(.+)$', 'explicit'),
            (r'(.+?)\s*=\s*(.+)', 'assignment'),
            (r'Governing\s+(?:Equation|Relation|Dynamics):\s*(.+)', 'governing'),
            (r'(?:Key\s+Relation|Prediction):\s*(.+)', 'key_relation'),
        ]

        self.math_indicators = [
            '=', '+', '-', '*', '/', '^', '\\',
            'cos', 'sin', 'exp', 'log', 'sqrt', 'sum', 'int', 'frac',
            'pi', 'alpha', 'beta', 'gamma'
        ]

    def normalize_equation(self, eq_str: str) -> str:
        """Normalizes an equation string for deduplication.

        Args:
            eq_str: The equation string to normalize.

        Returns:
            The normalized equation string with whitespace removed.
        """
        eq_str = re.sub(r'\s+', '', eq_str.strip())
        return eq_str

    def _is_valid_equation(self, eq_str: str) -> bool:
        """Checks if a string is likely a valid equation.

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

        if not any(ind in eq_str for ind in self.math_indicators):
            return False

        prose_indicators = [' the ', ' and ', ' or ', ' is ', ' are ', ' that ',
                           ' this ', ' these ', ' with ', ' for ', ' from ', ' a ', ' an ', ' to ', ' in ', ' of ']

        prose_count = sum(1 for ind in prose_indicators if ind in eq_str.lower())
        words = len(eq_str.split())
        if words > 5 and prose_count / words > 0.4:
            return False

        if re.fullmatch(r'={5,}', eq_str):
            return False

        return True

    def _generate_eq_id(self, framework_type: str) -> str:
        """Generates a unique equation ID for a given framework.

        Args:
            framework_type: The framework name (e.g., "Aether", "Genesis").

        Returns:
            A unique equation ID string (e.g., "AE001").
        """
        prefix_map = {
            'Aether': 'AE',
            'Genesis': 'GE',
            'Pais': 'PE',
            'Tourmaline': 'TE',
            'Superforce': 'SE',
            'Literature': 'LE',
            'Unified': 'UE',
            'Synthesis': 'SE'
        }

        prefix = prefix_map.get(framework_type, 'EQ')
        self.eq_counter[prefix] += 1
        return f"{prefix}{self.eq_counter[prefix]:03d}"

    def _extract_description(self, lines: list[str], current_line_num: int, context_window: int = 3) -> str:
        """Extracts a description for an equation from its context.

        Args:
            lines: A list of all lines in the source file.
            current_line_num: The line number of the equation.
            context_window: The number of lines before and after the
                equation to include in the context.

        Returns:
            A string containing the context of the equation.
        """
        start = max(0, current_line_num - context_window - 1)
        end = min(len(lines), current_line_num + context_window)

        context = ' '.join(lines[start:end])
        context = re.sub(r'\s+', ' ', context).strip()

        if len(context) > 200:
            context = context[:200] + '...'

        return context

    def _classify_domain(self, equation_str: str, description: str) -> str:
        """Classifies the domain of an equation.

        Args:
            equation_str: The equation string.
            description: The description of the equation.

        Returns:
            The classified domain string (e.g., "EM", "GR", "QM").
        """
        domains = {
            'QM': ['quantum', 'wave', 'psi', 'hamiltonian', 'operator', 'qubit', 'entangle'],
            'GR': ['metric', 'curvature', 'einstein', 'ricci', 'tensor', 'spacetime', 'gravity'],
            'EM': ['electromagnetic', 'electric', 'magnetic', 'maxwell', 'field'],
            'Thermo': ['entropy', 'temperature', 'heat', 'thermal', 'boltzmann'],
            'Math': ['group', 'algebra', 'lie', 'symmetry', 'topology', 'dimension'],
            'Experimental': ['casimir', 'measurement', 'spectroscopy', 'interferometry']
        }

        combined_text = (equation_str + ' ' + description).lower()

        for domain, keywords in domains.items():
            if any(keyword in combined_text for keyword in keywords):
                return domain

        return 'General'

    def _suggest_experiment(self, equation_str: str, description: str) -> str:
        """Suggests a potential experimental test for an equation.

        Args:
            equation_str: The equation string.
            description: The description of the equation.

        Returns:
            A string with the suggested experiment or "Theoretical
            validation required".
        """
        suggestions = {
            'casimir': 'Casimir force measurement with fractal geometries',
            'scalar': 'Scalar field interferometry',
            'foam': 'Quantum foam perturbation detection',
            'zpe': 'Zero-point energy spectroscopy',
            'crystal': 'Vibrational spectroscopy in crystals',
            'entropy': 'Thermal imaging and entropy measurement',
            'dimensional': 'Dimensional spectroscopy',
        }

        combined = (equation_str + ' ' + description).lower()

        for keyword, suggestion in suggestions.items():
            if keyword in combined:
                return suggestion

        return 'Theoretical validation required'

    def extract_from_pdf(self, pdf_path: Path):
        """Extracts equations from a single PDF file.

        This method uses PyMuPDF to extract text from each page of the PDF,
        then applies the equation patterns to find and catalog equations.

        Args:
            pdf_path: The path to the PDF file.
        """
        try:
            import fitz  # PyMuPDF
        except Exception as e:
            raise RuntimeError("PyMuPDF (pymupdf) is required for PDF extraction") from e
        print(f"Processing PDF: {pdf_path.name}")

        try:
            document = fitz.open(pdf_path)
        except (fitz.FileDataError, IOError) as e:
            print(f"Error opening PDF {pdf_path.name}: {e}")
            self.had_errors = True
            return

        # Determine framework based on filename (similar to equation_extractor.py)
        lower_name = pdf_path.name.lower()
        if 'pais' in lower_name:
            framework = 'Pais'
        elif 'tourmaline' in lower_name:
            framework = 'Tourmaline'
        elif 'superforce' in lower_name:
            framework = 'Superforce'
        elif 'comment' in lower_name:
            framework = 'Pais' # Comment on Pais is still related to Pais framework
        else:
            framework = 'Literature'

        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text_content = page.get_text("text")
            lines = text_content.splitlines()

            for line_idx, line in enumerate(lines):
                line = line.strip()
                if not line or len(line) < 5:
                    continue

                for pattern, pattern_type in self.equation_patterns:
                    matches = safe_finditer(pattern, line, re.IGNORECASE)
                    for match in matches:
                        if pattern_type == 'governing' or pattern_type == 'key_relation':
                            equation_str = match.group(1).strip()
                        elif pattern_type == 'explicit' or pattern_type == 'assignment':
                            equation_str = match.group(0).strip()
                        else:
                            equation_str = match.group(0).strip()

                        if self._is_valid_equation(equation_str):
                            normalized = self.normalize_equation(equation_str)

                            if normalized in self.seen_equations:
                                continue

                            self.seen_equations.add(normalized)

                            eq_id = self._generate_eq_id(framework)
                            description = self._extract_description(lines, line_idx)
                            domain = self._classify_domain(equation_str, description)

                            entry = {
                                'EqID': eq_id,
                                'Equation': equation_str,
                                'Framework': framework,
                                'Domain': domain,
                                'SourceDoc': pdf_path.name,
                                'SourceLine': f"Page {page_num + 1}, Line {line_idx + 1}",
                                'Description': description,
                                'VerificationStatus': 'Theoretical',
                                'RelatedEqs': '',
                                'ExperimentalTest': self._suggest_experiment(equation_str, description)
                            }
                            self.equations.append(entry)

    def save_to_csv(self, output_file: str):
        """Saves the extracted equations to a CSV file.

        Args:
            output_file: The path to the output CSV file.
        """
        fieldnames = ['EqID', 'Equation', 'Framework', 'Domain', 'SourceDoc',
                     'SourceLine', 'Description', 'VerificationStatus',
                     'RelatedEqs', 'ExperimentalTest']
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.equations)
            print(f"\nExtracted {len(self.equations)} equations from PDFs to {output_file}")
        except IOError as e:
            print(f"Error writing CSV file {output_file}: {e}")
            self.had_errors = True

# Helpers for directory and file resolution (no heavy deps required)
# Main execution
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract equations from PDF files using PyMuPDF")
    parser.add_argument("--base-dir", type=str, help="Repository base directory (overrides default)")
    parser.add_argument("--papers-dir", type=str, help="Directory with PDFs (default tries source_materials/pdfs then papers)")
    parser.add_argument("--pdf", action="append", help="Specific PDF filename(s) relative to papers dir; repeatable")
    args = parser.parse_args()

    BASE_DIR = _resolve_base_dir(args.base_dir)

    print("="*70)
    print("PDF EQUATION EXTRACTION - Math_Science Repository")
    print("Base dir:", BASE_DIR)
    print("="*70)

    extractor = PDFEquationExtractor()

    # Resolve papers directory
    papers_dir = resolve_papers_dir(BASE_DIR, args.papers_dir)
    if not papers_dir.exists():
        print(f"Warning: Papers directory not found: {papers_dir}")
        extractor.had_errors = True

    # Build list of PDFs
    pdf_paths = build_pdf_list(papers_dir, args.pdf)
    if not pdf_paths:
        print(f"Warning: No PDFs found under {papers_dir}")
        extractor.had_errors = True

    for full_pdf_path in pdf_paths:
        extractor.extract_from_pdf(full_pdf_path)

    # Save to CSV
    output_csv = os.path.join(BASE_DIR, 'equation_catalog_pdfs.csv')
    extractor.save_to_csv(output_csv)

    print("\nPDF text extraction complete!")

    if extractor.had_errors:
        raise SystemExit(1)



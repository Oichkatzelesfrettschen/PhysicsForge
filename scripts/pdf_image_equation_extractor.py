import argparse
import os
import re
import csv
from pathlib import Path
from collections import defaultdict
import os as _os
import warnings as _warnings
try:
    # Suppress noisy third-party update notices and serializer warnings
    _os.environ.setdefault('NO_ALBUMENTATIONS_UPDATE', '1')
    _warnings.filterwarnings('ignore', message='A new version of Albumentations is available', category=UserWarning)
    _warnings.filterwarnings('ignore', message='Pydantic serializer warnings', category=UserWarning)
    from scripts.common import resolve_papers_dir, build_pdf_list
    from scripts.common import resolve_base_dir as _resolve_base_dir
except Exception:
    import sys as _sys
    from pathlib import Path as _Path
    _mod_dir = str(_Path(__file__).resolve().parent)
    _sys.path.insert(0, _mod_dir)
    from common import resolve_papers_dir, build_pdf_list
    from common import resolve_base_dir as _resolve_base_dir

# Base directory (overridable via --base-dir or env var)
BASE_DIR = _resolve_base_dir(None)

DEFAULT_PAPERS_DIR_CANDIDATES = (
    'source_materials/pdfs',
    'papers',
)

class PDFImageEquationExtractor:
    """Extracts equations from images within PDF files using OCR.

    This class scans PDF files, extracts images from each page, and uses
    the pix2tex OCR model to convert images that appear to be equations
    into LaTeX strings.

    Attributes:
        base_dir (str): The root directory of the repository.
        equations (list[dict]): A list of dictionaries, each representing a
            found equation.
        eq_counter (defaultdict[str, int]): A counter for generating unique
            equation IDs for each framework.
        seen_equations (set[str]): A set of normalized equations to avoid
            duplicates.
        had_errors (bool): A flag indicating if any errors occurred during
            extraction.
        ocr_model: The initialized pix2tex OCR model.
        temp_image_dir (Path): The directory for storing temporary images
            extracted from PDFs.
    """
    def __init__(self, base_dir: str):
        """Initializes the PDFImageEquationExtractor.

        Args:
            base_dir: The base directory of the repository.
        """
        self.base_dir = base_dir
        self.equations = []
        self.eq_counter = defaultdict(int)
        self.seen_equations = set()
        self.had_errors = False
        # Lazy import of pix2tex only when needed
        try:
            from pix2tex.cli import LatexOCR  # type: ignore
        except Exception as e:
            raise RuntimeError("pix2tex is required for OCR extraction") from e
        self.ocr_model = LatexOCR() # Initialize OCR model once

        self.temp_image_dir = Path(self.base_dir) / "data" / "temp_pdf_images"
        try:
            self.temp_image_dir.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            print(f"Error creating temporary image directory {self.temp_image_dir}: {e}")
            self.had_errors = True

    def _generate_eq_id(self, framework_type: str) -> str:
        """Generates a unique equation ID for a given framework.

        Args:
            framework_type: The framework name (e.g., "Aether", "Genesis").

        Returns:
            A unique equation ID string (e.g., "AE001").
        """
        prefix_map = {
            'Aether': 'AE', 'Genesis': 'GE', 'Pais': 'PE',
            'Tourmaline': 'TE', 'Superforce': 'SE', 'Literature': 'LE',
            'Unified': 'UE', 'OCR': 'OE' # New prefix for OCR extracted
        }
        prefix = prefix_map.get(framework_type, 'EQ')
        self.eq_counter[prefix] += 1
        return f"{prefix}{self.eq_counter[prefix]:03d}"

    def _classify_framework(self, pdf_name: str) -> str:
        """Classifies the framework based on the PDF filename.

        Args:
            pdf_name: The name of the PDF file.

        Returns:
            The classified framework string.
        """
        lower_name = pdf_name.lower()
        if 'pais' in lower_name:
            return 'Pais'
        elif 'tourmaline' in lower_name:
            return 'Tourmaline'
        elif 'superforce' in lower_name:
            return 'Superforce'
        else:
            return 'OCR' # Default for general OCR extraction

    def _post_process_latex_output(self, latex_str: str) -> str:
        """Applies heuristic corrections to common OCR errors in LaTeX output.

        Args:
            latex_str: The raw LaTeX string from the OCR model.

        Returns:
            The corrected LaTeX string.
        """
        # No heuristic corrections applied for now.
        # This method can be expanded later for specific post-processing needs.
        return latex_str

    def extract_images_from_pdf(self, pdf_path: Path) -> None:
        """Extracts images from a PDF and attempts OCR on them.

        This method uses PyMuPDF to extract images from each page of the PDF,
        saves them as temporary files, and then runs them through the OCR
        model.

        Args:
            pdf_path: The path to the PDF file.
        """
        print(f"Extracting images from PDF: {pdf_path.name}")
        framework = self._classify_framework(pdf_path.name)

        try:
            import fitz  # PyMuPDF
            document = fitz.open(pdf_path)
        except (fitz.FileDataError, IOError) as e:
            print(f"Error opening PDF {pdf_path.name}: {e}")
            self.had_errors = True
            return

        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            image_list = page.get_images(full=True)

            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                # Save image temporarily
                image_filename = self.temp_image_dir / f"{pdf_path.stem}_page{page_num+1}_img{img_index}.{image_ext}"
                try:
                    with open(image_filename, "wb") as f:
                        f.write(image_bytes)
                except IOError as e:
                    print(f"Error writing temporary image file {image_filename}: {e}")
                    self.had_errors = True
                    continue

                try:
                    from PIL import Image
                    with Image.open(image_filename) as pil_image:
                        width, height = pil_image.size
                        if width < 50 or height < 20:
                            continue
                        if width / height > 10 or height / width > 10:
                            continue
                        # Pre-process
                        pil_image = pil_image.convert('L')
                        pil_image = pil_image.point(lambda x: 0 if x < 128 else 255, '1')
                        latex_output = self.ocr_model(pil_image)
                    # Post-process and filter
                    latex_output = self._post_process_latex_output(latex_output)
                    if not latex_output or len(latex_output) < 5 or len(latex_output) > 500:
                        continue
                    math_keywords = r'\\(alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|sum|int|frac|sqrt|left|right|begin|end|text|mathrm|mathbf|mathcal|mathbb|nabla|partial|cdot|times|div|pm|mp|approx|equiv|neq|leq|geq|ll|gg|subset|supset|in|forall|exists|infty|ldots|cdots|vdots|ddots)'
                    if not re.search(math_keywords, latex_output) and not re.search(r'[+\-*/=<>^_{}]', latex_output):
                        continue
                    if self.normalize_equation(latex_output) in self.seen_equations:
                        continue
                    eq_id = self._generate_eq_id(framework)
                    entry = {
                        'EqID': eq_id,
                        'Equation': latex_output,
                        'Framework': framework,
                        'Domain': 'Math/OCR',
                        'SourceDoc': pdf_path.name,
                        'SourceLine': f"Page {page_num + 1}, Image {img_index} ({width}x{height})",
                        'Description': f"OCR extracted equation from image on Page {page_num + 1}",
                        'VerificationStatus': 'OCR_Pending',
                        'RelatedEqs': '',
                        'ExperimentalTest': 'OCR validation required'
                    }
                    self.equations.append(entry)
                    self.seen_equations.add(self.normalize_equation(latex_output))
                except (RuntimeError, Exception) as ocr_e:
                    print(f"OCR failed for image {image_filename.name}: {ocr_e}")
                    self.had_errors = True
                finally:
                    try:
                        os.remove(image_filename)
                    except OSError as e:
                        print(f"Warning: Could not remove temporary image file {image_filename}: {e}")
                        self.had_errors = True

    def normalize_equation(self, eq_str: str) -> str:
        """Normalizes an equation string for deduplication.

        This is a simple version for OCR output, which removes all
        whitespace and converts the string to lowercase.

        Args:
            eq_str: The equation string to normalize.

        Returns:
            The normalized equation string.
        """
        return re.sub(r'\s+', '', eq_str.strip()).lower()

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

            print(f"\nExtracted {len(self.equations)} equations via OCR from PDFs to {output_file}")
        except IOError as e:
            print(f"Error writing CSV file {output_file}: {e}")
            self.had_errors = True

# Main execution
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract equations from PDF images using OCR")
    parser.add_argument("--base-dir", type=str, help="Repository base directory (overrides default)")
    parser.add_argument("--papers-dir", type=str, help="Directory with PDFs (default tries source_materials/pdfs then papers)")
    parser.add_argument("--pdf", action="append", help="Specific PDF filename(s) relative to papers dir; repeatable")
    args = parser.parse_args()

    BASE_DIR = _resolve_base_dir(args.base_dir)

    print("="*70)
    print("PDF IMAGE EQUATION EXTRACTION (OCR) - Math_Science Repository")
    print("Base dir:", BASE_DIR)
    print("="*70)

    extractor = PDFImageEquationExtractor(BASE_DIR)

    papers_dir = resolve_papers_dir(BASE_DIR, args.papers_dir)
    if not papers_dir.exists():
        print(f"Warning: Papers directory not found: {papers_dir}")
        extractor.had_errors = True

    pdf_paths = build_pdf_list(papers_dir, args.pdf)
    if not pdf_paths:
        print(f"Warning: No PDFs found under {papers_dir}")
        extractor.had_errors = True

    for full_pdf_path in pdf_paths:
        extractor.extract_images_from_pdf(full_pdf_path)

    output_csv = os.path.join(BASE_DIR, 'equation_catalog_pdfs_ocr.csv')
    extractor.save_to_csv(output_csv)

    print("\nPDF image OCR extraction complete!")

    if extractor.had_errors:
        raise SystemExit(1)

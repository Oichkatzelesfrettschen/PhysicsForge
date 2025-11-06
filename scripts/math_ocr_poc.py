import argparse
from pathlib import Path
from pix2tex.cli import LatexOCR

def ocr_math_from_image(image_path: Path) -> tuple[str | None, bool]:
    had_errors_local = False
    if not image_path.exists():
        print(f"Error: Image file not found at {image_path}")
        had_errors_local = True
        return None, had_errors_local

    try:
        # Initialize the OCR model
        # This might download a model the first time it's run
        model = LatexOCR()
        
        # Perform OCR
        latex_output = model(image_path)
        
        print(f"Successfully performed OCR on {image_path.name}")
        print(f"LaTeX Output: {latex_output}")
        return latex_output, had_errors_local
    except Exception as e:
        print(f"Error performing OCR on {image_path.name}: {e}")
        had_errors_local = True
        return None, had_errors_local

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proof-of-concept for mathematical OCR using pix2tex.")
    parser.add_argument("--image-file", type=str, required=True, help="Path to the image file containing a mathematical expression.")
    args = parser.parse_args()

    image_file_path = Path(args.image_file)
    had_errors = False
    latex_output, func_had_errors = ocr_math_from_image(image_file_path)
    if func_had_errors:
        had_errors = True

    if had_errors:
        raise SystemExit(1)

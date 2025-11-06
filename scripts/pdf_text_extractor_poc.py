import fitz  # PyMuPDF
import argparse
from pathlib import Path

def extract_text_from_pdf(pdf_path: Path, output_path: Path) -> bool:
    """
    Extracts text from a PDF file and saves it to a text file.
    """
    try:
        document = fitz.open(pdf_path)
        text_content = ""
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text_content += page.get_text("text")  # "text" extracts plain text
            text_content += "\n--- End of Page " + str(page_num + 1) + " ---\n"

        output_path.write_text(text_content, encoding="utf-8")
        print(f"Successfully extracted text from '{pdf_path.name}' to '{output_path}'")
        return True
    except (fitz.FileDataError, IOError, UnicodeEncodeError) as e:
        print(f"Error extracting text from '{pdf_path.name}': {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proof-of-concept for PDF text extraction using PyMuPDF.")
    parser.add_argument("--pdf-file", type=str, required=True, help="Path to the PDF file to extract text from.")
    parser.add_argument("--output-file", type=str, default="extracted_pdf_text.txt", help="Path to save the extracted text.")
    args = parser.parse_args()

    pdf_file_path = Path(args.pdf_file)
    output_file_path = Path(args.output_file)

    had_errors = False
    success = extract_text_from_pdf(pdf_file_path, output_file_path)
    if not success:
        had_errors = True

    if had_errors:
        raise SystemExit(1)

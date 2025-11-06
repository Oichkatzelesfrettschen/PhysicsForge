# Scripts Installation Requirements

This document captures precise, per-script dependency requirements and verification steps for the Python tooling under `scripts/`.

Last updated: 2025-10-23

---

## Core Environment

- Python: 3.11+ (tested with 3.11 and 3.13)
- Pip: 24.x+
- GNU Make: Required for using the `Makefile` commands.
- No external packages are required to run the unit tests and the basic text extraction pipeline.

Verify:

```
python --version
pip --version
pytest -q  # optional, if pytest is installed
```

**Windows Users**: A `bash` environment (e.g., Git Bash, WSL) is required for `make` commands and LaTeX compilation scripts. Install Git Bash from [https://git-scm.com/downloads](https://git-scm.com/downloads) or enable WSL (Windows Subsystem for Linux) and install a Linux distribution.

---

## Optional Feature Sets

Install these only if you need the related features.

- PDF Text Extraction (`scripts/pdf_equation_extractor.py`, `scripts/pdf_text_extractor_poc.py`)
  - Requires: PyMuPDF
  - Install: `pip install pymupdf`

- PDF Image OCR to LaTeX (`scripts/pdf_image_equation_extractor.py`, `scripts/math_ocr_poc.py`)
  - Requires: pix2tex (LaTeX OCR), Pillow (PIL)
  - Install: `pip install pix2tex Pillow`
  - ML backend (PyTorch) for pix2tex:
    - CPU-only (Windows):
      `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`
    - Verify: `python -c "import torch; print(torch.__version__)"`

- Development / Testing
  - `pytest` for running tests locally: `pip install pytest`

An aggregate constraints file is available at the repo root:

```
pip install -r requirements-optional.txt
```

---

## Mapping: Scripts -> Dependencies

- `equation_extractor.py` - stdlib only
- `merge_and_analyze_equations.py` - stdlib only
- `catalog_parity.py` - stdlib only
- `validate_catalog.py` - stdlib only
- `repo_audit.py` - stdlib only
- `pdf_equation_extractor.py` - PyMuPDF (`pymupdf`)
- `pdf_text_extractor_poc.py` - PyMuPDF (`pymupdf`)
- `pdf_image_equation_extractor.py` - pix2tex, Pillow, (PyTorch backend)
- `math_ocr_poc.py` - pix2tex, Pillow, (PyTorch backend)
- `ollama_batch.py` - no Python deps beyond stdlib; requires Ollama CLI installed and in PATH. Install from [https://ollama.com/download](https://ollama.com/download)

---

## Windows Convenience (PowerShell)

Install optional extras:

```
python -m pip install --upgrade pip
pip install -r requirements-optional.txt

# CPU-only PyTorch (if needed by pix2tex)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

**Note**: For `make` commands and LaTeX compilation, a `bash` environment (e.g., Git Bash, WSL) is required. Ensure `make` is available in your `bash` environment.

---

## Verification Checklist

- PyMuPDF:
  - `python -c "import fitz; print(fitz.__doc__[:30])"`
- pix2tex:
  - `python -c "from pix2tex.cli import LatexOCR; print('pix2tex OK')"`
- Pillow:
  - `python -c "from PIL import Image; print('Pillow OK')"`


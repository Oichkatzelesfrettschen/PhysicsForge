import os
from pathlib import Path


def test_pdf_text_dir_resolution(tmp_path: Path, monkeypatch):
    # Arrange a temp base with default pdf folder and one file
    base = tmp_path
    pdf_dir = base / 'source_materials' / 'pdfs'
    pdf_dir.mkdir(parents=True)
    (pdf_dir / 'sample.pdf').write_bytes(b'%PDF-1.4\n% test file')

    # Import module and call helpers (should not require PyMuPDF)
    import scripts.pdf_equation_extractor as tex

    papers = tex.resolve_papers_dir(str(base), None)
    assert papers.exists()
    assert papers.samefile(pdf_dir)

    pdfs = tex.build_pdf_list(papers, None)
    assert len(pdfs) == 1 and pdfs[0].name == 'sample.pdf'


def test_pdf_image_dir_resolution(tmp_path: Path, monkeypatch):
    base = tmp_path
    # Use fallback name to ensure both candidates work
    pdf_dir = base / 'papers'
    pdf_dir.mkdir(parents=True)
    (pdf_dir / 'b.pdf').write_bytes(b'%PDF-1.4\n% test file')

    import scripts.pdf_image_equation_extractor as img

    papers = img.resolve_papers_dir(str(base), None)
    assert papers.exists()
    assert papers.samefile(pdf_dir)

    pdfs = img.build_pdf_list(papers, ["b.pdf"])  # specific list
    assert len(pdfs) == 1 and pdfs[0].name == 'b.pdf'


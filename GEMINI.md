# GEMINI Integration Guide

This guide outlines how to use Google Gemini (and other local/remote LLM agents) to assist research, auditing, and code tasks within this repository.

**Last updated: November 16, 2025**

**IMPORTANT**: As of November 2025, PhysicsForge has been **restructured** from a single 500+ page monograph into **six modular papers** using **standard scientific terminology**. See `PAPER_STRUCTURE_NORMALIZED.md` for complete specifications.

---

## Project Overview

This repository serves as a **Math & Science Research Hub** for unified field theories and advanced physics. It has been restructured into **six focused, peer-reviewable papers** using **standard physics nomenclature**.

### Six Paper Series: "Unified Field Theories and Advanced Physics: A Mathematical Synthesis"

1. **Paper 1**: Scalar Field Theory and Zero-Point Energy Coupling (25-30 pages)
2. **Paper 2**: Exceptional Lie Algebras and Crystalline Lattice Structures (30-35 pages)
3. **Paper 3**: Fractal Geometry and Hyperdimensional Field Structures (25-30 pages)
4. **Paper 4**: Gravitational-Electromagnetic Unification via Scalar Intermediaries (28-33 pages)
5. **Paper 5**: Experimental Protocols for Exotic Quantum States (30-35 pages)
6. **Paper 6**: Applications to Quantum Computing and Energy Technologies (25-30 pages)

**CRITICAL TERMINOLOGY REQUIREMENT**: Use ONLY standard physics terminology. Deprecated terms ("Aether Framework", "Genesis Framework", "Pais Superforce") have been eliminated. See `synthesis/shared/glossary.tex` for approved terminology (80+ standard terms).

**Key Components:**
*   **`synthesis/shared/`**: **NEW** - Shared infrastructure (preamble, macros, glossary, notation) used by all papers
*   **`synthesis/papers/`**: **NEW** - Six modular papers, each with chapters/, figures/, and paper-specific bibliography
*   **`synthesis/build/`**: **NEW** - Compiled PDFs for all papers
*   **`synthesis/chapters/`**: **LEGACY** - Original monograph chapters (being migrated to papers/)
*   **`scripts/`**: Python utilities for cataloging, extracting, building papers, validation
*   **`docs/`**: Comprehensive documentation including PAPER_STRUCTURE_NORMALIZED.md and RESTRUCTURE_PROGRESS_REPORT.md
*   **`source_materials/`**: Raw references and primary literature (PDFs, text)
*   **`notes/`**: Working documents, drafts, and synthesis summaries
*   **`data/`**: Staging area for catalogs, fixtures, and generated outputs
*   **`tests/`**: Unit and integration tests for Python scripts and LaTeX compilation

---

## Setup and Installation

### Core Environment

*   **Python**: 3.11+ (tested with 3.11 and 3.13)
*   **Pip**: 24.x+
*   **GNU Make**: Required for using the `Makefile` commands.
    *   **Windows Users**: A `bash` environment (e.g., Git Bash, WSL) is required for `make` commands and LaTeX compilation scripts. Install GNU Make via Chocolatey (`choco install make`) or Scoop (`scoop install make`) and ensure `bash` is in your PATH.

### Python Dependencies

*   **Core**: No external packages are required to run unit tests and the basic text extraction pipeline.
*   **Optional Feature Sets**: Install these only if you need the related features. An aggregate constraints file is available:
    ```bash
    pip install -r requirements-optional.txt
    ```
    This includes:
    *   `pymupdf`: For PDF text extraction (`scripts/pdf_equation_extractor.py`, `scripts/pdf_text_extractor_poc.py`).
    *   `pix2tex`, `Pillow`: For PDF image OCR to LaTeX (`scripts/pdf_image_equation_extractor.py`, `scripts/math_ocr_poc.py`).
    *   `torch`, `torchvision`, `torchaudio`: ML backend for `pix2tex`.
        *   **CPU-only (Windows)**: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`
    *   `pytest`: For running tests locally (`pip install pytest`).

*   **Ollama CLI**: Required for `scripts/ollama_batch.py`. Install from [https://ollama.com/](https://ollama.com/) and ensure it's in your system's PATH.

---

## Building and Running

The `Makefile` provides a comprehensive set of commands for various project tasks.

### Key `make` Commands

*   `make pipeline`: Rebuilds the catalog from `notes/` and `synthesis/`.
*   `make audit`: Runs structural diagnostics (`scripts/repo_audit.py`).
*   `make parity`: Runs catalog parity diagnostics (`scripts/catalog_parity.py`).
*   `make gaps`: Runs TODO diagnostics (`scripts/gap_todo.py`).
*   `make validate`: Validates the catalog (`scripts/validate_catalog.py`).
*   `make bench`: Benchmarks extraction (`scripts/benchmark_extraction.py`).
*   `make smoke`: Runs a fast regression pass (`scripts/test_extraction_smoke.py`).
*   `make test`: Executes `pytest -q` across `tests/`.
*   `make ci`: Runs a suite of CI checks (`smoke test validate audit parity gaps`).
*   `make link`: Links modules (`scripts/link_modules.py`).
*   `make latex`: Standard LaTeX compilation (`synthesis/scripts/compile.sh`).
*   `make latex_strict`: Strict LaTeX compilation (`synthesis/scripts/compile_strict.sh`).
*   `make reports`: Generates `DEPS_REPORT.md`, `TODO_TRACKER.md`, `REPO_AUDIT.md`.
*   `make ascii_guard`: Enforces ASCII-only policy (`scripts/ascii_guard.py`).
*   `make todo`: Updates the TODO tracker (`scripts/todowrite.py`).

---

## Development Conventions

*   **Coding Style**: Python 3.10+, four-space indents, type-annotated helpers, `if __name__ == "__main__"` entry points. Snake_case filenames. Prefer pure functions.
*   **LaTeX**: Modules follow `eq_<domain>_<topic>.tex`, use `\label{eq:aether:energy-band}`, apply framework macros from `synthesis/preamble.tex`.
*   **Markdown**: Entries open with a level-one title, mirroring `docs/` and `notes/` structure.
*   **ASCII-only Policy**: Strict ASCII-only for code and documentation (`.py`, `.md`, `.tex`, `.yml`, `.ps1`, `.sh`). Use LaTeX macros or ASCII transliterations for special characters. Run `make ascii_guard` locally. Exceptions for data artifacts and external source dumps in `data/`, `extracted_data/`, `source_materials/`.
*   **Testing**: `test_*.py` files executed via `pytest`. Pair pipeline changes with `make smoke` and `make test`. Add `make pipeline` and `make latex_strict` for catalog or TeX module shifts. Treat warnings as failures.
*   **Commit & Pull Request Guidelines**: Scoped commit messages (e.g., `scripts: message`). Focus commits by domain. Rerun relevant Make targets before PRs. Summarize intent, link issues, enumerate verification steps, highlight new assets.
*   **Data Stewardship**: Catalog CSVs are generated outputs; refresh via pipeline, do not edit manually.
*   **Common Helpers**: Use `scripts/common.py` for `resolve_base_dir` and PDF discovery helpers.
*   **CI**: Workflow runs tests, ASCII guard, and optional TeX strict compile. Warnings are errors in LaTeX strict builds prior to release tagging.

---

## Project Roadmap (High-Level)

The project follows a phased roadmap for data extraction, catalog consistency, integration into synthesis, validation, testing, visualizations, data management, and bibliographic references. Continuous conflict resolution and elucidation of new findings are ongoing.

---

## Addressed Deficiencies and Implemented Solutions

This section details areas for improvement identified during the comprehensive audit. The proposed solutions have been implemented as part of the completed roadmap, significantly enhancing project quality, maintainability, and cross-platform compatibility.

### 1. Cross-Platform Compatibility (Windows)

*   **Deficiency**: The `Makefile` explicitly uses `SHELL := /bin/bash` and calls `bash` scripts for LaTeX compilation, which was problematic for native Windows environments without Git Bash or WSL.
*   **Resolution**: Documentation in `INSTALLATION_REQUIREMENTS.md` and `GEMINI.md` has been updated with explicit instructions for Windows users regarding `bash` environment setup. This deficiency is now addressed.

### 2. Error Handling in `Makefile` (`|| true`)

*   **Deficiency**: Many `Makefile` targets used `|| true` to prevent `make` from failing, masking critical errors and contradicting the "treat every warning as an error" mandate.
*   **Resolution**: `|| true` has been removed from critical `Makefile` targets (`validate`, `test`, `latex`, `latex_strict`, `ascii_guard`) to ensure explicit failure on error. This deficiency is now addressed.

### 3. Outdated Roadmap Status

*   **Deficiency**: The "Progress Meter" and fixed "Week" numbers in `docs/PROJECT_ROADMAP.md` were outdated and not actively maintained.
*   **Resolution**: Static "Week" numbers and the "Progress Meter" have been removed from `docs/PROJECT_ROADMAP.md`. This deficiency is now addressed.

### 4. CI Implementation

*   **Deficiency**: Continuous Integration (CI) was planned but not yet fully implemented.
*   **Resolution**: A basic GitHub Actions workflow (`.github/workflows/main.yml`) has been implemented to run `make ci` on pull requests and `make latex_strict` on `main` branch pushes. Linting (`flake8`) and type checking (`mypy`) steps have also been added. This deficiency is now addressed.

### 5. `data/README.md` Update Process

*   **Deficiency**: The instruction to manually update `data/README.md` was prone to human error and could lead to outdated documentation.
*   **Resolution**: `scripts/update_data_readme.py` has been created and integrated into `make reports` to automatically generate or update sections of `data/README.md`. This deficiency is now addressed.

### 6. Ollama CLI Installation

*   **Deficiency**: Missing explicit installation instructions or a link to the official guide for the Ollama CLI, which is required for `scripts/ollama_batch.py`.
*   **Resolution**: A direct link to the official Ollama installation guide has been added to `INSTALLATION_REQUIREMENTS.md` and `GEMINI.md`. This deficiency is now addressed.

### 7. Ambiguous `docs/README` Reference

*   **Deficiency**: The reference to "mirror the structure seen in `docs/README`" in `AGENTS.md` was ambiguous as `docs/README.md` did not exist.
*   **Resolution**: `docs/README.md` has been created with guidelines for the `docs/` directory, and `AGENTS.md` has been updated to explicitly refer to it. This deficiency is now addressed.

---

## Reassessed Project Scope

The core scope of the project remains the **Math & Science Research Hub** for data extraction, analysis, and LaTeX synthesis. However, the audit highlights a need to expand the scope to include:

*   **Enhanced Cross-Platform Support**: Explicitly addressing and documenting Windows compatibility for the build system.
*   **Robust Quality Assurance**: Implementing comprehensive CI and stricter error handling to ensure data integrity and build reliability.
*   **Improved Documentation Automation**: Automating documentation generation where feasible to reduce manual effort and ensure accuracy.
*   **Streamlined Contributor Experience**: Providing clearer setup instructions and reducing potential friction points for new contributors.

---

## Completed Roadmap Items

All tasks outlined in the "Ultra-Detailed Roadmap (Next Steps)" have been successfully completed.

### Phase 1: Foundational Improvements

1.  **Address Windows Compatibility**: `INSTALLATION_REQUIREMENTS.md` and `GEMINI.md` updated with explicit instructions for Windows users regarding `bash` environment setup (Git Bash/WSL) for `make` and LaTeX compilation.
2.  **Refine `Makefile` Error Handling**: `|| true` removed from critical `Makefile` targets (`validate`, `test`, `latex`, `latex_strict`) to ensure explicit failure on error.
3.  **Implement Basic CI (GitHub Actions)**: `.github/workflows/main.yml` created to run `make ci` on pull requests and `make latex_strict` on `main` branch pushes.
4.  **Update Ollama CLI Instructions**: A link to the official Ollama installation guide added to `INSTALLATION_REQUIREMENTS.md` and `GEMINI.md`.

### Phase 2: Documentation and Automation Enhancements

1.  **Automate `data/README.md` Updates**: `scripts/update_data_readme.py` created and integrated into `make reports` to automatically generate or update sections of `data/README.md`.
2.  **Clarify `docs/README` Reference**: `docs/README.md` created with guidelines for the `docs/` directory, and `AGENTS.md` updated to explicitly refer to it.
3.  **Review `docs/PROJECT_ROADMAP.md` for Dynamic Progress**: Static "Week" numbers and the "Progress Meter" removed from `docs/PROJECT_ROADMAP.md`.

### Phase 3: Advanced Quality and Maintainability

1.  **Investigate Cross-Platform Build Tool**: Research conducted and a report added to `GEMINI.md` recommending SCons as a strong candidate for a cross-platform build tool.
2.  **Comprehensive Error Handling in Scripts**: All Python scripts in `scripts/` have been reviewed and refined to ensure robust error handling and consistent exit codes.
3.  **Expand CI Coverage**: Linting (`flake8`) and type checking (`mypy`) steps added to the `build` job in `.github/workflows/main.yml`.

---

## Conclusion

By systematically addressing these deficiencies and following the proposed roadmap, the Math & Science Research Hub will significantly enhance its quality, maintainability, and usability for all contributors, fostering a more robust and collaborative research environment.

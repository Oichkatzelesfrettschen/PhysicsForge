# Math & Science Research Hub

## Project Overview

This repository serves as a **Math & Science Research Hub**, collecting research in early stages of development. It's primarily a **code project** with a strong emphasis on Python scripting for data extraction and analysis, and LaTeX for document synthesis. The project focuses on theoretical physics and advanced mathematics, synthesizing unified field theories, quantum-gravitational models, and crystalline spacetime engineering.

**Key Components:**
*   **`synthesis/`**: PRIMARY WORK AREA - LaTeX book project for the monograph "Unified Field Theories and Advanced Physics: A Mathematical Synthesis."
*   **`scripts/`**: Python utilities for cataloging, extracting, merging, validating, and reporting.
*   **`notes/`**: Working documents, drafts, and synthesis summaries, including project management and research surveys.
*   **`source_materials/`**: Raw references and primary literature (PDFs, text).
*   **`data/`**: Staging area for catalogs, fixtures, and generated outputs.
*   **`extracted_data/`**: Reports and longer-form generated analyses.
*   **`output/`**: Rendered PDFs and reports.
*   **`docs/`**: Guides, roadmaps, and repository documentation.
*   **`tests/`**: Unit and integration tests for Python scripts and LaTeX compilation.
*   **`modules/`**: Reusable LaTeX components, especially equation snippets.

**Theoretical Frameworks Integrated:**
*   **Aether Framework**: Scalar field dynamics, zero-point energy (ZPE), quantum foam, time crystals.
*   **Genesis Framework**: Exceptional Lie groups (E8, E7, E6, F4, G2), Cayley-Dickson algebras, fractal geometries, modular symmetries.
*   **Pais Framework**: Gravitational-electromagnetic unification with scalar-ZPE interactions.
*   **Mathematical Foundations**: Non-associative algebras, hyperdimensional constructs (up to 2048D), Monster Group modular invariants.

## Setup and Installation

### Core Environment

*   **Python**: 3.10+ (tested with 3.11 and 3.13)
*   **Pip**: 24.x+
*   **GNU Make**: Required for using the `Makefile` commands.
    *   **Windows Users**: A `bash` environment (e.g., Git Bash, WSL) is required for `make` commands and LaTeX compilation scripts. Install GNU Make via Chocolatey (`choco install make`) or Scoop (`scoop install make`) and ensure `bash` is in your PATH.
*   **LaTeX Distribution**: MiKTeX or TeX Live.

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

### LaTeX Package Requirements

The `synthesis/preamble.tex` file requires numerous LaTeX packages. MiKTeX's "on-the-fly installation" is recommended. For TeX Live, a full installation scheme is advised. Key packages include `amsmath`, `amssymb`, `mathtools`, `physics`, `tikz`, `pgfplots`, `booktabs`, `xcolor`, `siunitx`, `hyperref`, `cleveref`, `natbib`, `listings`, `geometry`, `fancyhdr`, `titlesec`, `tcolorbox`, `lipsum`, `enumitem`, `caption`, `subcaption`, `inputenc`, and `fontenc`.

A batch installation script for both MiKTeX and TeX Live is available in `INSTALLATION_REQUIREMENTS.md`.

### Pre-commit Hooks

Install pre-commit for local checks:
```bash
pip install pre-commit
pre-commit install
```

## Building and Running

### Building from Source (Arch Linux)

This project can be packaged for Arch Linux using the provided `PKGBUILD` file. The `PKGBUILD` creates a source package that contains the entire project directory.

1.  **Install Dependencies:**

    Before building the package, you need to install the required dependencies. A script is provided to automate this process.

    ```bash
    ./install_deps.sh
    ```

    This script will install all the necessary dependencies from the official repositories and the AUR. You will need to have an AUR helper like `yay` or `paru` installed.

2.  **Build the Package:**

    Once the dependencies are installed, you can build the source package using `makepkg`.

    ```bash
    makepkg
    ```

    This will create a package file with the `.pkg.tar.zst` extension.

3.  **Install the Package:**

    You can install the package using `pacman`.

    ```bash
    sudo pacman -U <package-file>.pkg.tar.zst
    ```

    This will install the source code to `/usr/src/physicsforge`.

4.  **Build the Project:**

    After installing the source package, you can build the project by navigating to the `/usr/src/physicsforge` directory and running `make`.

    ```bash
    cd /usr/src/physicsforge
    make
    ```

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
*   `make ascii_normalize`: Normalize Unicode in docs/summaries to ASCII.

### Python Script Execution

Individual Python scripts can be run directly from the `scripts/` directory. Most scripts accept a `--base-dir` argument (defaulting to `.`) and `--scan-dir` for specifying directories to process.

**Example: Full Catalog Pipeline**
```bash
python scripts/build_catalog_pipeline.py --base-dir . --scan-dir notes --scan-dir synthesis
```

## Development Conventions

### Coding Style & Naming Conventions

*   **Python**: Python 3.10+, four-space indents, type-annotated helpers, `if __name__ == "__main__"` entry points. Snake_case filenames. Prefer pure functions. Use `scripts/common.py` for path resolution.
*   **LaTeX**: Modules follow `eq_<domain>_<topic>.tex`, use `\label{eq:aether:energy-band}`, apply framework macros from `synthesis/preamble.tex`.
*   **Markdown**: Entries open with a level-one title, mirroring `docs/` and `notes/` structure.
*   **ASCII-only Policy**: Strict ASCII-only for code and documentation (`.py`, `.md`, `.tex`, `.yml`, `.ps1`, `.sh`). Use LaTeX macros or ASCII transliterations for special characters. Run `make ascii_guard` locally. Exceptions for data artifacts and external source dumps in `data/`, `extracted_data/`, `source_materials/`.

### Testing Guidelines

*   Tests live in `tests/test_*.py` and run via `pytest`.
*   Pair pipeline changes with `make smoke` and `make test`.
*   Add `make pipeline` and `make latex_strict` for catalog or TeX module shifts.
*   Treat warnings as failures.
*   Extractor determinism: `scripts/equation_extractor.py` supports `--parallel-workers`; parallel results are deterministic across runs.
*   Default excludes apply when scanning the repo root: `data/`, `extracted_data/`, `source_materials/`, `output/`, `.git`, `.pytest_cache`, `__pycache__`. Override with explicit `--exclude-dir` flags.
*   Use `--metrics-output` to emit a JSON object containing both `stats` and `metrics`.

### Commit & Pull Request Guidelines

*   Use scoped commit subjects (e.g., `scripts: message`). Focus commits by domain.
*   Before opening a PR, rerun the relevant Make or validation commands, list them in the description, and highlight regenerated assets (e.g., `equation_catalog.csv`, `CATALOG_PARITY.md`).
*   Include screenshots of significant LaTeX layout changes if applicable.

### Data Stewardship & Configuration

*   Regenerate catalog CSVs via scripts instead of editing by hand.
*   Log optional dependencies in `requirements-optional.txt`.
*   Mirror environment notes in `INSTALLATION_REQUIREMENTS.md` and `docs/`.
*   Keep PowerShell execution policy at least `RemoteSigned` so automation scripts run without prompts.

## Workflow for Adding Content

### Adding a New Equation Module

1.  **Create module file**: `synthesis/modules/equations/eq_[framework]_[descriptor].tex`
2.  **Add full provenance header** (source, framework, domain, status, notes, dependencies).
3.  **Add to catalog**: Run `python scripts/equation_extractor.py` or manually update `equation_catalog.csv`.
4.  **Link in chapter**: Add `\input{modules/equations/eq_...}` in appropriate chapter.
5.  **Test compile**: `cd synthesis && pdflatex test_chNN.tex`.
6.  **Verify references**: Check that `\label{}` works and `\ref{}` resolves correctly.
7.  **Cross-link**: Run `python scripts/link_modules.py` to update related equations.

### Transforming a Chapter to Whitepaper Style

**Target**: 50-65% narrative, 35-50% equations.

**Process**:
1.  **Add opening story** (200-250 words): Historical context or experimental motivation.
2.  **Add worked examples** (3 per chapter): Numerical calculations with intermediate steps.
3.  **Add physical interpretations**: Explain what each equation means physically.
4.  **Add framework attribution**: Use `\aetherattr{}`, `\genesisattr{}`, `\paisattr{}` boxes.
5.  **Modularize equations**: Move inline equations to `modules/equations/` and `\input{}` them.
6.  **Test compile**: Verify PDF generation with `pdflatex test_chNN.tex`.
7.  **Verify agent output**: ALWAYS use bash commands to verify line counts and timestamps (`wc -l`, `ls -lh`, `grep`).

### Running Agents in Parallel

*   **Recommended**: Use 2-3 agents maximum for parallel work.
*   **Verification protocol**: NEVER trust agent claims without verification. Use `wc -l`, `ls -lh`, `grep`, `head` to verify files changed (line counts, timestamps, content spot-checks).

## Troubleshooting

### LaTeX Compilation Errors

*   **"Memory dump file not found" / "pdflatex.fmt not found"**: MiKTeX format files corrupted. Fix by opening MiKTeX Console as Admin -> Tasks -> Update formats, or `initexmf --admin --mklinks && initexmf --admin --dump=pdflatex`.
*   **"Undefined control sequence"**: Check package loading in `preamble.tex`, command spelling, and custom macro definitions.
*   **"Missing \begin{document}"**: Verify `preamble.tex` is included and no stray text before `\begin{document}`.
*   **"Undefined references" / "Citation ... undefined"**: Normal on first compile. Run `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`. Check `\label{}` and `\cite{}` keys.

### Python Script Errors

*   **"Module not found"**: Current scripts use only standard library. Verify Python 3.10+ installed. If new scripts with dependencies are added, document in `requirements.txt`.
*   **"File not found"**: Check `--base-dir` points to repository root. Use absolute paths or ensure correct working directory.
*   **Script runs but no output files**: Check exit code (non-zero indicates errors). Verify write permissions.

### Verification Failures

*   **Agent claimed to modify file but line count unchanged**: CRITICAL: Verify with `wc -l [file]` and `ls -lh [file]`. Check timestamp.

## Release Notes: Version 1.0.0 (2025-10-23)

This is the first stable release of **"Unified Field Theories and Advanced Physics: A Mathematical Synthesis,"** a comprehensive 525-page monograph integrating three theoretical frameworks (Aether, Genesis, Pais) with rigorous mathematics and critical evaluation.

**Summary of Achievements:**
*   **Content**: 30 chapters (6 foundations, 10 frameworks, 5 unification, 5 experiments, 4 applications), 1,300+ equations (98 modular, 60% utilization), 20+ TikZ figures, 40+ tables, 242 bibliography entries.
*   **Quality**: All claims backed by explicit equations and derivations, critical evaluation with TRL levels, cross-framework integration, 100+ experimental predictions, professional typesetting.
*   **Metrics**: PDF Quality Score: 85/100, 525 pages, 3.51 MB PDF size, minimal undefined references (1), all citations resolved.

**Known Limitations:**
*   Speculative content (warp drives, nodespace folding).
*   Limited experimental validation (most predictions TRL 1-3).
*   High energy requirements for many applications.
*   Some framework contradictions not fully resolved.
*   Minimal index entries (expandable in v1.1).

**Changelog from Development:**
*   **Added**: Ch 28 (Energy Technologies), Ch 30 (Spacetime Engineering), comprehensive frontmatter and backmatter, 53 equation modules, 64 specialized citations.
*   **Enhanced**: Ch 15 (Pais Superforce), Ch 27 (Quantum Computing), Ch 29 (Advanced Propulsion).
*   **Fixed**: Duplicate bibliography entries, undefined cross-references and citations, index infrastructure.

## Project Roadmap (High-Level)

The project follows a phased roadmap for data extraction, catalog consistency, integration into synthesis, validation, testing, visualizations, data management, and bibliographic references. Continuous conflict resolution and elucidation of new findings are ongoing.

**Key Phases:**
1.  **Critical Content Completion**: Expanding stub chapters (Ch28, Ch30) and short chapters (Ch15).
2.  **Test Suite Completion**: Creating missing chapter and part tests.
3.  **Module Integration**: Auditing and integrating orphaned equation and figure modules.
4.  **Refinement of Bibliographic References**: Expanding citations across all chapters.
5.  **Backmatter Development**: Expanding appendices, glossary, and index.
6.  **Quality Assurance**: Cross-reference validation, spell/grammar check, final compilation.
7.  **Notes Modularization**: Parallel workstream to organize and deduplicate the `notes/` directory.

**Expected Outcomes:**
*   Repository size: 12 MB -> 7 MB (-41%).
*   File count: 40 -> ~25 files (-37%).
*   Zero content duplication.
*   Clear organizational structure.
*   All placeholders resolved or tracked.

## Contributing Guide

Thank you for contributing! This project enforces strict quality and reproducibility standards.

**Quick Checklist:**
*   Run tests and ASCII guard locally: `make test`, `make ascii_guard`.
*   Run the pipeline (optional deps for PDF/OCR): `make pipeline`.
*   If you touched docs/summaries under `docs/` or `synthesis/`, normalize: `make ascii_normalize`.
*   For LaTeX-heavy changes, run strict compile: `make latex_strict`.
*   Generate reports: `make reports`.

**Pull Requests:**
Include in the PR description:
*   Summary of changes and intent.
*   Commands run locally (tests, pipeline, strict LaTeX, reports).
*   Any assets regenerated (e.g., `equation_catalog.csv`, `CATALOG_PARITY.md`).
*   Screenshots of significant LaTeX layout changes if applicable.

## Catalog Parity

See [Catalog Parity Report](reports/CATALOG_PARITY.md) for details.

## Dependency Audit (scripts)

See [Dependency Audit Report](reports/DEPENDENCY_AUDIT.md) for details.

## TODO / FIXME Tracker

See [TODO / FIXME Tracker Report](reports/TODO_FIXME_TRACKER.md) for details.

## Notes Modularization & Deduplication Plan

**Goals:**
*   Eliminate all duplicate content (-4.7 MB, 41% reduction).
*   Consolidate project management documentation.
*   Standardize naming conventions.
*   Resolve or track all TODOs/FIXMEs.
*   Improve discoverability and maintainability.

**Phases:**
1.  **Immediate Deletions**: Remove critical duplicate `.tex` files.
2.  **Project Management Consolidation**: Merge 16 files into 4 master documents.
3.  **Large File Modularization**: Split `Maximal_Extraction_SET1_SET2.md` into smaller, focused files.
4.  **Naming Standardization**: Rename framework files for consistency and add version metadata headers.
5.  **TODO/FIXME Resolution**: Address identified issues across the repository.
6.  **Survey Consolidation**: Validate no duplication with `bibliography.bib`, extract missing citations, and standardize survey format.
7.  **Documentation & Validation**: Update all `README` files, validate internal links, run full catalog pipeline, verify synthesis compilation, and update `CLAUDE.md`.

**Expected Outcomes:**
*   Repository size: 12 MB -> 7 MB (-41%).
*   File count: 40 -> ~25 files (-37%).
*   Zero content duplication.
*   Clear organizational structure.
*   All placeholders resolved or tracked.
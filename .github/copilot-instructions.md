# GitHub Copilot Instructions

This file provides guidance to GitHub Copilot when working with code in this repository.

## Project Overview

This repository serves as a **Math & Science Research Hub**, collecting research in early stages of development. It's primarily a **code project** with a strong emphasis on Python scripting for data extraction and analysis, and LaTeX for document synthesis.

The project focuses on theoretical physics and advanced mathematics, synthesizing unified field theories, quantum-gravitational models, and crystalline spacetime engineering.

**Key Theoretical Frameworks:**
- **Aether Framework**: Scalar field dynamics, zero-point energy (ZPE), quantum foam, time crystals
- **Genesis Framework**: Exceptional Lie groups (E8, E7, E6, F4, G2), Cayley-Dickson algebras, fractal geometries, modular symmetries
- **Pais Framework**: Gravitational-electromagnetic unification with scalar-ZPE interactions
- **Mathematical Foundations**: Non-associative algebras, hyperdimensional constructs (up to 2048D), Monster Group modular invariants

## Repository Structure

**Key Components:**
- **`synthesis/`**: PRIMARY WORK AREA - LaTeX book project for the monograph "Unified Field Theories and Advanced Physics: A Mathematical Synthesis"
- **`scripts/`**: Python utilities for cataloging, extracting, merging, validating, and reporting
- **`notes/`**: Working documents, drafts, and synthesis summaries
- **`source_materials/`**: Raw references and primary literature (PDFs, text)
- **`data/`**: Staging area for catalogs, fixtures, and generated outputs
- **`extracted_data/`**: Reports and longer-form generated analyses
- **`output/`**: Rendered PDFs and reports
- **`docs/`**: Guides, roadmaps, and repository documentation
- **`tests/`**: Unit and integration tests for Python scripts and LaTeX compilation
- **`modules/`**: Reusable LaTeX components, especially equation snippets

## Technology Stack

- **Python**: 3.10+ (tested with 3.11 and 3.13)
- **Package Manager**: pip
- **Build System**: GNU Make (cross-platform with bash support)
- **LaTeX Distribution**: MiKTeX or TeX Live
- **Testing Framework**: pytest
- **Version Control**: Git with GitHub

## Build Commands

The `Makefile` provides comprehensive commands for various project tasks:

### Essential Commands
- `make help` - Display all available commands with descriptions
- `make pipeline` - Rebuild the catalog from `notes/` and `synthesis/`
- `make test` - Execute pytest across `tests/`
- `make ci` - Run full CI checks (smoke, test, validate, audit, parity, gaps)

### Validation & Quality
- `make validate` - Validate the catalog integrity
- `make audit` - Run structural diagnostics
- `make parity` - Check catalog parity
- `make gaps` - Run TODO diagnostics
- `make ascii_guard` - Enforce ASCII-only policy (CRITICAL)

### LaTeX Compilation
- `make latex` - Standard LaTeX compilation
- `make latex_strict` - Strict LaTeX compilation (warnings as errors)
- `make link` - Link equation modules

### Reporting
- `make reports` - Generate DEPS_REPORT.md, TODO_TRACKER.md, REPO_AUDIT.md
- `make bench` - Benchmark extraction performance
- `make todo` - Update the TODO tracker

## Development Conventions

### Coding Style
- **Python**: 3.10+ compatible, four-space indents, type-annotated helpers
- **Entry Points**: Use `if __name__ == "__main__"` pattern
- **Naming**: Snake_case for filenames and functions
- **Functions**: Prefer pure functions when possible
- **Imports**: Organize with standard library first, then third-party, then local

### LaTeX Conventions
- **Equation Modules**: Follow `eq_<domain>_<topic>.tex` naming pattern
- **Labels**: Use format `\label{eq:framework:specific-name}` (e.g., `\label{eq:aether:energy-band}`)
- **Macros**: Apply framework macros from `synthesis/preamble.tex`
- **Compilation**: Test with both `make latex` and `make latex_strict`

### Markdown Conventions
- **Structure**: Open with a level-one title
- **Organization**: Mirror `docs/` and `notes/` directory structure
- **ASCII-only**: Strictly enforce (see ASCII Policy below)

### ASCII-Only Policy (CRITICAL)

**Strictly enforce ASCII-only** for all code and documentation files:
- **File Types**: `.py`, `.md`, `.tex`, `.yml`, `.yaml`, `.ps1`, `.sh`
- **Special Characters**: Use LaTeX macros or ASCII transliterations
- **Verification**: Run `make ascii_guard` before commits
- **Exceptions**: Data artifacts and external source dumps in `data/`, `extracted_data/`, `source_materials/`

Examples of ASCII transliterations:
- Use `e` not `e` (Unicode variants)
- Use `--` or `---` not em-dashes
- Use `"quotes"` not smart quotes
- Use `'` not curly apostrophes

### Testing Requirements
- **Test Files**: Name as `test_*.py` in `tests/` directory
- **Execution**: Use pytest framework
- **Pipeline Changes**: Pair with `make smoke` and `make test`
- **Catalog/TeX Changes**: Also run `make pipeline` and `make latex_strict`
- **Warnings**: Treat all warnings as failures in strict mode

### Commit & Pull Request Guidelines
- **Commit Messages**: Use scoped format (e.g., `scripts: message`, `docs: message`, `synthesis: message`)
- **Commit Focus**: Keep commits focused by domain/component
- **Pre-commit**: Run relevant Make targets before committing
- **PR Description**: Summarize intent, link issues, enumerate verification steps
- **PR Assets**: Highlight new files or significant changes

### Data Stewardship
- **Catalog CSVs**: These are generated outputs - refresh via pipeline, never edit manually
- **Common Helpers**: Use `scripts/common.py` for `resolve_base_dir` and PDF discovery
- **Data Integrity**: Validate changes with `make validate`

## Cross-Platform Support

### Windows Users
- **Bash Environment**: Git Bash or WSL required for make commands and LaTeX compilation
- **GNU Make**: Install via Chocolatey (`choco install make`) or Scoop (`scoop install make`)
- **PATH**: Ensure bash is in system PATH

### Build Scripts
- **PowerShell**: `win_make.ps1` available as Windows alternative
- **Bash Scripts**: Located in `synthesis/scripts/` for LaTeX compilation

## CI/CD Workflow

- **Automated Tests**: Workflow runs tests, ASCII guard, and optional TeX strict compile
- **Build Validation**: Warnings are errors in LaTeX strict builds prior to release tagging
- **Coverage**: Test coverage reports generated automatically
- **Quality Gates**: All validation checks must pass

## Dependencies

### Core Dependencies (requirements.txt)
```
pytest==7.4.3
pytest-cov>=4.1,<5
pymupdf>=1.22,<2.0
Pillow>=10,<12
pix2tex>=0.1,<1.0
jsonschema>=4.19,<5
bibtexparser>=1.4.0,<2.0.0
lark>=1.1.2
```

### Optional Dependencies
- `pymupdf`: PDF text extraction
- `pix2tex`, `Pillow`: PDF image OCR to LaTeX
- `torch`, `torchvision`, `torchaudio`: ML backend for pix2tex
- `pytest`: Local testing
- **Ollama CLI**: Required for `scripts/ollama_batch.py` (install from https://ollama.com/)

## Common Development Workflows

### Adding New Equations
1. Create `eq_*.tex` file in `synthesis/modules/equations/`
2. Use proper framework header and labels
3. Run `make pipeline` to update catalog
4. Link to appropriate chapter
5. Run `make latex` to verify compilation

### Running Tests
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
make test

# Run quick smoke tests
make smoke

# Run full CI suite
make ci
```

### Making Code Changes
1. Make minimal, focused changes
2. Run `make ascii_guard` to verify ASCII compliance
3. Run relevant tests (`make test` or specific test files)
4. Run validation (`make validate` if catalog affected)
5. Build and verify LaTeX if synthesis changed (`make latex_strict`)
6. Commit with scoped message

### Debugging Build Issues
1. Check working directory (must be project root)
2. Verify dependencies installed
3. Run `make clean` to remove stale artifacts
4. Check `make audit` for structural issues
5. Review build logs in `logs/` directory

## Important Files to Reference

- **`GEMINI.md`**: Detailed integration guide for LLM agents
- **`README.md`**: Project overview and quick start
- **`docs/PROJECT_ROADMAP.md`**: Project roadmap and phases
- **`synthesis/preamble.tex`**: LaTeX macros and package definitions
- **`scripts/common.py`**: Shared Python utilities

## Security & Quality Standards

- **No Secrets**: Never commit secrets, credentials, or sensitive data
- **Security Vulnerabilities**: Address any security issues in code changes
- **Code Review**: Significant changes should be reviewed
- **Documentation**: Update documentation for API or behavior changes
- **Backward Compatibility**: Maintain unless explicitly breaking change

## When Working with This Repository

### Do:
- Follow the ASCII-only policy strictly
- Run `make ascii_guard` before commits
- Use type hints in Python code
- Write focused, minimal commits
- Test changes thoroughly with relevant make targets
- Update documentation when changing behavior
- Use existing helpers from `scripts/common.py`
- Follow established naming conventions
- Check CI status before merging

### Don't:
- Edit catalog CSV files manually
- Commit build artifacts or temporary files
- Use non-ASCII characters in code/docs
- Skip validation checks
- Make broad, unfocused changes
- Remove or modify working tests without reason
- Ignore build warnings in strict mode
- Work from subdirectories (always use project root)

## Getting Help

- **Documentation**: Check `docs/` directory for detailed guides
- **Make Targets**: Run `make help` for all available commands
- **Issues**: Check existing issues for known problems
- **Validation**: Use `make audit` and `make parity` for diagnostics

## Version Control

- **Branch Naming**: Use descriptive names (e.g., `feature/add-equation-module`, `fix/latex-compilation`)
- **Main Branch**: `main` is protected, requires PR review
- **Commit Frequency**: Commit often with clear messages
- **Git Hooks**: Pre-commit hooks enforce ASCII policy and basic validation

## Additional Context

This project represents active theoretical physics research. Code quality, documentation accuracy, and mathematical rigor are paramount. When suggesting code or making changes:

1. **Understand the physics context** before modifying equation-related code
2. **Preserve mathematical notation** and LaTeX formatting conventions
3. **Maintain catalog integrity** - any equation changes must flow through the pipeline
4. **Respect the modular architecture** - equations, derivations, and narrative are separate
5. **Cross-reference thoroughly** - this work builds on decades of physics literature

The repository integrates multiple theoretical frameworks, so changes should respect the existing taxonomy and classification systems.

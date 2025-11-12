# Contributing Guide

Thank you for contributing! This project enforces strict quality and reproducibility standards. Please follow the steps below.

## Quick Checklist

- Run tests and ASCII guard locally:
  - `make test`
  - `make ascii_guard`
- Run the pipeline (optional deps for PDF/OCR):
  - `make pipeline`
- If you touched docs/summaries under `docs/` or `synthesis/`, normalize:
  - `make ascii_normalize`
- For LaTeX-heavy changes, run strict compile:
  - `make latex_strict`
- Generate reports:
  - `make reports`

## Extractor CLI Tips

- Override domain classification with a JSON file:
  - Example fixture: `data/fixtures/domain_config.sample.json`
  - Usage: `python scripts/equation_extractor.py --base-dir . --scan-dir notes --domain-config data/fixtures/domain_config.sample.json`
- Emit metrics and NDJSON artifacts for CI/debugging:
  - `--ndjson-output out.ndjson --metrics-output metrics.json`
  - Metrics JSON contains `stats` and `metrics`; `metrics.by_domain` and `metrics.timing.total_elapsed_s` are asserted in tests.
- Parallel, deterministic scanning:
  - Use `--parallel-workers N` for speed; results remain deterministic.
  - Scanning the repo root applies default excludes (`data/`, `extracted_data/`, `source_materials/`, `output/`, `.git`, `.pytest_cache`, `__pycache__`).
  - Disable with `--no-default-excludes` when scanning the entire tree.
 - Filter by framework hints from filenames:
   - `--framework-include Aether --framework-exclude Genesis`
- Metrics schema:
  - See `docs/METRICS_SCHEMA.md` for fields and invariants.

## Windows Development Notes

- Use `win_make.ps1` as a Make alternative when Bash is not available:
  - Examples:
    - `./win_make.ps1 -Target test -BaseDir .`
    - `./win_make.ps1 -Target quick_pipeline -BaseDir .`
    - `./win_make.ps1 -Target metrics_only -BaseDir .`
- LaTeX builds (`latex`, `latex_strict`) are Linux/WSL only in this repo. Run those targets on Linux CI or within WSL.

## Pre-commit Hooks

Install pre-commit for local checks:

```
pip install pre-commit
pre-commit install
```

## Style and Scope

- Python: 3.10+, snake_case filenames, type hints, pure functions where possible.
- Keep changes focused by domain (scripts, LaTeX, docs, data tooling).
- Enforce ASCII-only in code and docs (see AGENTS.md).

## Pull Requests

Include in the PR description:

- Summary of changes and intent
- Commands run locally (tests, pipeline, strict LaTeX, reports)
- Any assets regenerated (e.g., `equation_catalog.csv`, `CATALOG_PARITY.md`)
- Screenshots of significant LaTeX layout changes if applicable

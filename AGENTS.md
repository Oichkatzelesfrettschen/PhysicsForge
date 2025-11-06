# Repository Guidelines

## Project Structure & Module Organization
Automation lives in `scripts/`, LaTeX assembly in `synthesis/`, and reusable equation snippets in `modules/equations/`. Research notes stay in `notes/`, primary references in `source_materials/`, and generated datasets land in `data/` or `extracted_data/`. Rendered outputs sit in `output/`, while tests live in `tests/`.

## Build, Test, and Development Commands
- `make pipeline` - rebuild the catalog from `notes/` and `synthesis/`.
- `make audit` / `make parity` / `make gaps` - structural, coverage, and TODO diagnostics.
- `make smoke` - fast regression pass; run before sharing branches.
- `make test` - executes `pytest -q` across `tests/` (set `BASE_DIR` when running elsewhere).
- `make latex` / `make latex_strict` - standard and strict LaTeX compiles; use strict before releases.
  
Note: Figure generation and data validation tooling will be added as separate modules. For now, use `make pipeline`, `make reports`, and the validation scripts under `scripts/`.
- `make ascii_guard` - enforce ASCII-only policy on code and docs.
- `make ascii_normalize` - normalize Unicode in docs/summaries to ASCII.

## Coding Style & Naming Conventions
Target Python 3.10+, four-space indents, and type-hinted helpers behind `if __name__ == "__main__"`. Keep filenames snake_case (`scripts/build_catalog_pipeline.py`), avoid mutable globals, and use `scripts/common.py` utilities for path resolution. LaTeX modules follow `eq_<domain>_<topic>.tex`, label like `\label{eq:aether:energy-band}`, and apply framework macros from `synthesis/preamble.tex`. Markdown files start with a level-one title mirroring the structure seen in `docs/` and `notes/`.

ASCII policy: code, scripts, and LaTeX stay ASCII. Use macros (`\alpha`, `\phi`) or transliterations instead of Unicode glyphs, and run `make ascii_guard` (plus `make ascii_normalize` on docs when needed). Data dumps in `data/`, `extracted_data/`, and `source_materials/` may retain upstream Unicode and sit outside the guard.

## Testing Guidelines
Tests live in `tests/test_*.py` and run via `pytest`. Pair pipeline work with `make smoke`, `make test`, and `make pipeline`; add `make latex_strict` for TeX-heavy changes. Capture generated reports such as `VALIDATION_REPORT.md` and call them out in reviews.

Extractor determinism and metrics:
- `scripts/equation_extractor.py` supports `--parallel-workers`; parallel results are deterministic across runs.
- Default excludes apply when scanning the repo root: `data/`, `extracted_data/`, `source_materials/`, `output/`, `.git`, `.pytest_cache`, `__pycache__`. Override with explicit `--exclude-dir` flags.
- Use `--metrics-output` to emit a JSON object containing both `stats` and `metrics`. Tests assert invariants on these fields.

Planning and filters:
- Use `--plan-only` (plus `--plan-output`) to produce `plan.json` with candidate/skip rationale. See `docs/PLAN_SCHEMA.md`.
- Filters available: `--include-glob`, `--exclude-glob`, `--framework-include`, `--framework-exclude`, and the root `--no-default-excludes` toggle.

## Commit & Pull Request Guidelines
Use scoped commit subjects (`scripts: tighten catalog parity threshold`, `[Ch07] Add scalar-field example`) and keep changes domain-focused. Before opening a PR, rerun the relevant Make or validation commands, list them in the description, and highlight regenerated assets (`extracted_data/*.csv`, `output/*.pdf`) or screenshots when layouts shift.

Pre-commit hooks: install local hooks to enforce ASCII and quick tests.

```
pip install pre-commit
pre-commit install
```

EOL normalization and binary classification are defined in `.gitattributes`.

## Data Stewardship & Configuration
Regenerate catalog CSVs via scripts instead of editing by hand, log optional dependencies in `requirements-optional.txt`, and mirror environment notes in `INSTALLATION_REQUIREMENTS.md` and `docs/`. Keep PowerShell execution policy at least `RemoteSigned` so automation scripts run without prompts.


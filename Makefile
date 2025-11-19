# Virtual environment path (optional, not required for most targets)
# To use venv: make venv && source venv/bin/activate
VENV_PATH := $(CURDIR)/venv
PYTHON := python

.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "---------------------------------------------------------------------------"
	@echo " PhysicsForge Makefile - Your portal to project automation.                "
	@echo "---------------------------------------------------------------------------"
	@echo "                                                                           "
	@echo " Core Commands:                                                            "
	@echo "   pipeline        - Full data extraction and catalog generation.          "
	@echo "                     Example: make pipeline                                "
	@echo "   quick_pipeline  - A faster, limited-scope pipeline for quick checks.    "
	@echo "                     Example: make quick_pipeline                          "
	@echo "   test            - Run the full test suite.                              "
	@echo "                     Example: make test                                    "
	@echo "   ci              - Continuous integration: all checks, tests, and build. "
	@echo "                     Example: make ci                                      "
	@echo "                                                                           "
	@echo "---------------------------------------------------------------------------"
	@echo "                                                                           "
	@echo " Validation & Auditing:                                                    "
	@echo "   validate        - Validate the integrity of the equation catalog.       "
	@echo "   audit           - Audit the repository for structural issues.           "
	@echo "   parity          - Check for consistency between catalog and modules.    "
	@echo "   gaps            - Identify TODOs and gaps in the research.              "
	@echo "   lint            - Run all linting checks.                               "
	@echo "                                                                           "
	@echo "---------------------------------------------------------------------------"
	@echo "                                                                           "
	@echo " LaTeX & Synthesis:                                                        "
	@echo "   latex           - Compile the main LaTeX document (legacy monograph).   "
	@echo "   latex_strict    - Compile LaTeX in strict mode (errors fail the build). "
	@echo "   paper1          - Build standalone Chapter 1 demo (LEGACY).             "
	@echo "   paper1-new      - Build Paper 1: Scalar Field Theory & ZPE.             "
	@echo "   paper2          - Build Paper 2: Exceptional Algebras.                  "
	@echo "   paper3          - Build Paper 3: Fractal Geometry.                      "
	@echo "   paper4          - Build Paper 4: EM-Gravity Unification.                "
	@echo "   paper5          - Build Paper 5: Experimental Protocols.                "
	@echo "   paper6          - Build Paper 6: Applications.                          "
	@echo "   papers_all      - Build all six papers.                                 "
	@echo "   papers_clean    - Clean all paper build artifacts.                      "
	@echo "   link            - Link equation modules into the synthesis directory.   "
	@echo "                                                                           "
	@echo "---------------------------------------------------------------------------"
	@echo "                                                                           "
	@echo " Reporting & Metrics:                                                      "
	@echo "   reports         - Generate all project reports (dependencies, TODOs).   "
	@echo "   quick_reports   - Generate a subset of faster reports.                  "
	@echo "   bench           - Benchmark the equation extraction process.            "
	@echo "   metrics_only    - Generate extraction metrics without building catalog. "
	@echo "   plan            - Create an extraction plan without executing it.       "
	@echo "                                                                           "
	@echo "---------------------------------------------------------------------------"
	@echo "                                                                           "
	@echo " Maintenance:                                                              "
	@echo "   clean           - Remove temporary and generated files.                 "
	@echo "   distclean       - A more thorough cleaning, removing caches.            "
	@echo "   ascii_guard     - Check for non-ASCII characters in the codebase.       "
	@echo "   ascii_normalize - Normalize unicode characters to ASCII.                "
	@echo "   update_data_readme - Regenerate the README for the data directory.      "
	@echo "                                                                           "
	@echo "---------------------------------------------------------------------------"

SHELL := /bin/bash

BASE_DIR ?= .
SCANS ?= notes .

.PHONY: pipeline audit parity gaps validate bench smoke test ci link latex latex_strict paper1 clean-paper1 validate-paper1 todo reports ascii_guard ascii_normalize update_data_readme help paper1-new paper2 paper3 paper4 paper5 paper6 papers_all papers_clean

pipeline:
	$(PYTHON) scripts/build_catalog_pipeline.py --base-dir $(BASE_DIR) $(foreach d,$(SCANS),--scan-dir $(d))

audit:
	python scripts/repo_audit.py --base-dir $(BASE_DIR)

parity:
	python scripts/catalog_parity.py --base-dir $(BASE_DIR)

gaps:
	python scripts/gap_todo.py --base-dir $(BASE_DIR)

validate:
	python scripts/validate_catalog.py --base-dir $(BASE_DIR)

bench:
	python scripts/benchmark_extraction.py --base-dir $(BASE_DIR) $(foreach d,$(SCANS),--scan-dir $(d)) || true

# smoke target moved to Enhanced CI/CD section below (line ~212)

test:
	pytest -q

ci: ascii_guard smoke test validate audit parity gaps latex_strict reports

.PHONY: link
link:
	python scripts/link_modules.py --base-dir $(BASE_DIR)

latex:
	bash synthesis/scripts/compile.sh

latex_strict:
	bash synthesis/scripts/compile_strict.sh

# Paper 1: Chapter 1 Standalone Demo (Lions Commentary Integration)
paper1:
	@echo "=== Building Paper 1: Chapter 1 Mathematical Preliminaries ==="
	@mkdir -p output/papers
	cd synthesis/papers && pdflatex -interaction=nonstopmode -halt-on-error paper1_chapter1_demo.tex
	cd synthesis/papers && bibtex paper1_chapter1_demo || true
	cd synthesis/papers && pdflatex -interaction=nonstopmode -halt-on-error paper1_chapter1_demo.tex
	cd synthesis/papers && pdflatex -interaction=nonstopmode -halt-on-error paper1_chapter1_demo.tex
	@mv synthesis/papers/paper1_chapter1_demo.pdf output/papers/ 2>/dev/null || echo "PDF already in place"
	@echo "=== Paper 1 built successfully: output/papers/paper1_chapter1_demo.pdf ==="

clean-paper1:
	@echo "=== Cleaning Paper 1 build artifacts ==="
	cd synthesis/papers && rm -f *.aux *.log *.out *.toc *.bbl *.blg *.pdf
	rm -f output/papers/paper1_chapter1_demo.pdf
	@echo "=== Paper 1 artifacts cleaned ==="

validate-paper1:
	@echo "=== Validating Paper 1 ==="
	@cd synthesis/papers && pdflatex -interaction=nonstopmode paper1_chapter1_demo.tex | grep -i "warning\|error\|undefined" || echo "No warnings/errors found"
	@echo "=== Paper 1 validation complete ==="

quick_pipeline:
	python scripts/equation_extractor.py --base-dir $(BASE_DIR) --scan-dir notes --max-files 30 --max-lines 400 --parallel-workers 4
	python scripts/merge_and_analyze_equations.py --base-dir $(BASE_DIR)
	python scripts/catalog_parity.py --base-dir $(BASE_DIR)

update_data_readme:
	python scripts/update_data_readme.py --base-dir $(BASE_DIR)

reports:
	python scripts/dependency_audit.py --base-dir $(BASE_DIR)
	python scripts/todowrite.py --base-dir $(BASE_DIR)
	python scripts/repo_audit.py --base-dir $(BASE_DIR)
	$(MAKE) update_data_readme
	@echo "Reports generated: DEPS_REPORT.md, TODO_TRACKER.md, REPO_AUDIT.md, data/README.md"

quick_reports:
	python scripts/dependency_audit.py --base-dir $(BASE_DIR)
	python scripts/todowrite.py --base-dir $(BASE_DIR)
	@echo "Quick reports generated: DEPS_REPORT.md, TODO_TRACKER.md"

.PHONY: metrics_only
metrics_only:
	python scripts/equation_extractor.py --base-dir $(BASE_DIR) $(foreach d,$(SCANS),--scan-dir $(d)) --max-files 50 --max-lines 400 --parallel-workers 4 --no-csv --no-ndjson --metrics-output metrics.json
	python scripts/validate_metrics_schema.py metrics.json

.PHONY: plan
plan:
	python scripts/equation_extractor.py --base-dir $(BASE_DIR) $(foreach d,$(SCANS),--scan-dir $(d)) --plan-only --plan-output plan.json
	python scripts/validate_plan_schema.py plan.json

.PHONY: lint
lint:
	$(MAKE) ascii_guard BASE_DIR=$(BASE_DIR)
	$(MAKE) plan BASE_DIR=$(BASE_DIR) SCANS="notes ."
	$(MAKE) metrics_only BASE_DIR=$(BASE_DIR) SCANS="notes ."

.PHONY: clean
clean:
	- rm -f plan.json metrics.json
	- rm -f DEPS_REPORT.md TODO_TRACKER.md REPO_AUDIT.md
	- rm -f data/README.md

.PHONY: distclean
distclean: clean
	- rm -rf __pycache__ .pytest_cache scripts/__pycache__ tests/__pycache__

ascii_guard:
	python scripts/ascii_guard.py --base-dir $(BASE_DIR)

ascii_normalize:
	python scripts/ascii_normalize.py --base-dir $(BASE_DIR) --path docs --path synthesis
todo:
	python scripts/todowrite.py --base-dir $(BASE_DIR)

# ==============================================================================
# GitHub Pages Publishing Targets
# ==============================================================================

.PHONY: svg figures clean-svg web

# Generate SVG figures from TikZ (XDV → SVG with WOFF2 fonts)
svg: figures

figures:
	@echo "=== Generating SVG figures from TikZ ==="
	@mkdir -p build/xdv figures/svg
	@for f in figures/tikz/*.tex; do \
		if [ -f "$$f" ]; then \
			base=$$(basename "$$f" .tex); \
			echo "Processing: $$base"; \
			xelatex --no-pdf -interaction=nonstopmode -halt-on-error \
				-output-directory=build/xdv "$$f" || echo "Warning: xelatex failed for $$f"; \
			xdv_file=""; \
			if [ -f "$${base}.xdv" ]; then \
				xdv_file="$${base}.xdv"; \
				mv "$${base}.xdv" "build/xdv/$${base}.xdv" 2>/dev/null || true; \
			elif [ -f "build/xdv/$${base}.xdv" ]; then \
				xdv_file="build/xdv/$${base}.xdv"; \
			fi; \
			if [ -n "$$xdv_file" ] && [ -f "build/xdv/$${base}.xdv" ]; then \
				dvisvgm --exact --font-format=woff2 -n -a \
					-o "figures/svg/$${base}.svg" "build/xdv/$${base}.xdv" || echo "Warning: dvisvgm failed for $$base"; \
			fi; \
		fi; \
	done
	@echo "=== Copying SVGs to site ==="
	@mkdir -p site/figs
	@cp figures/svg/*.svg site/figs/ 2>/dev/null || echo "No SVGs to copy"
	@echo "=== Figure generation complete ==="

# Build everything for web deployment
web: latex svg
	@echo "=== Preparing site for deployment ==="
	@mkdir -p site/pdf
	@cp synthesis/main.pdf site/pdf/ 2>/dev/null || cp build/main.pdf site/pdf/ || echo "Warning: PDF not found"
	@echo "=== Web build complete. Site ready in site/ ==="

# Clean SVG build artifacts
clean-svg:
	rm -rf build/xdv figures/svg site/figs
	@echo "Cleaned SVG build artifacts"

# Serve locally for testing (requires Python 3)
serve:
	@echo "=== Starting local server at http://localhost:8000 ==="
	@cd site && python3 -m http.server 8000



# ===== Enhanced CI/CD Targets =====

# Fast smoke test for quick validation (combines legacy + new approaches)
.PHONY: smoke
smoke:
	@echo "=== Running smoke tests ==="
	python scripts/test_extraction_smoke.py
	pytest tests/test_ascii_normalize.py tests/test_classify_domain.py -q
	python scripts/ascii_guard.py --base-dir .
	@echo "=== Smoke tests passed ==="

# Parallel test execution for faster CI
.PHONY: test-parallel
test-parallel:
	@echo "=== Running tests in parallel ==="
	pytest -n auto --dist=loadgroup

# Test with coverage report
.PHONY: test-coverage
test-coverage:
	@echo "=== Running tests with coverage ==="
	pytest --cov=scripts --cov-report=term-missing --cov-report=html

# Quick validation before commit
.PHONY: pre-commit
pre-commit: ascii_guard smoke
	@echo "=== Pre-commit validation passed ==="

# CI validation (what runs in GitHub Actions)
.PHONY: ci-check
ci-check: lint test
	@echo "=== CI checks passed ==="

# Show test timing statistics
.PHONY: test-timing
test-timing:
	@echo "=== Test execution timing ==="
	pytest --durations=10

# Security check (requires bandit)
.PHONY: security-check
security-check:
	@echo "=== Running security scan ==="
	@command -v bandit >/dev/null 2>&1 && bandit -r scripts/ -ll || echo "Install bandit: pip install bandit"

# Full comprehensive check
.PHONY: full-check
full-check: ci-check test-coverage security-check
	@echo "=== Full validation complete ==="

# ==============================================================================
# NEW MODULAR PAPER SYSTEM (November 2025)
# Six focused papers with standard physics nomenclature
# ==============================================================================

# Paper 1 (NEW): Scalar Field Theory and Zero-Point Energy Coupling
paper1-new:
	@echo "=== Building Paper 1: Scalar Field Theory and Zero-Point Energy ==="
	@mkdir -p synthesis/build
	cd synthesis/papers/paper1_scalar_field_zpe && \
		pdflatex -interaction=nonstopmode -halt-on-error paper1_main.tex && \
		bibtex paper1_main || true && \
		pdflatex -interaction=nonstopmode -halt-on-error paper1_main.tex && \
		pdflatex -interaction=nonstopmode -halt-on-error paper1_main.tex
	@mv synthesis/papers/paper1_scalar_field_zpe/paper1_main.pdf synthesis/build/paper1_scalar_field_zpe.pdf 2>/dev/null || true
	@echo "=== Paper 1 built: synthesis/build/paper1_scalar_field_zpe.pdf ==="

# Paper 2: Exceptional Lie Algebras and Crystalline Lattice Structures
paper2:
	@echo "=== Building Paper 2: Exceptional Algebras and Crystalline Lattices ==="
	@mkdir -p synthesis/build
	cd synthesis/papers/paper2_exceptional_algebras && \
		pdflatex -interaction=nonstopmode -halt-on-error paper2_main.tex && \
		bibtex paper2_main || true && \
		pdflatex -interaction=nonstopmode -halt-on-error paper2_main.tex && \
		pdflatex -interaction=nonstopmode -halt-on-error paper2_main.tex
	@mv synthesis/papers/paper2_exceptional_algebras/paper2_main.pdf synthesis/build/paper2_exceptional_algebras.pdf 2>/dev/null || true
	@echo "=== Paper 2 built: synthesis/build/paper2_exceptional_algebras.pdf ==="

# Paper 3: Fractal Geometry and Hyperdimensional Field Structures
paper3:
	@echo "=== Building Paper 3: Fractal Geometry and Hyperdimensional Fields ==="
	@mkdir -p synthesis/build
	cd synthesis/papers/paper3_fractal_geometry && \
		pdflatex -interaction=nonstopmode -halt-on-error paper3_main.tex && \
		bibtex paper3_main || true && \
		pdflatex -interaction=nonstopmode -halt-on-error paper3_main.tex && \
		pdflatex -interaction=nonstopmode -halt-on-error paper3_main.tex
	@mv synthesis/papers/paper3_fractal_geometry/paper3_main.pdf synthesis/build/paper3_fractal_geometry.pdf 2>/dev/null || true
	@echo "=== Paper 3 built: synthesis/build/paper3_fractal_geometry.pdf ==="

# Paper 4: Gravitational-Electromagnetic Unification via Scalar Intermediaries
paper4:
	@echo "=== Building Paper 4: Gravitational-EM Unification ==="
	@mkdir -p synthesis/build
	cd synthesis/papers/paper4_em_gravity_unification && \
		pdflatex -interaction=nonstopmode -halt-on-error paper4_main.tex && \
		bibtex paper4_main || true && \
		pdflatex -interaction=nonstopmode -halt-on-error paper4_main.tex && \
		pdflatex -interaction=nonstopmode -halt-on-error paper4_main.tex
	@mv synthesis/papers/paper4_em_gravity_unification/paper4_main.pdf synthesis/build/paper4_em_gravity_unification.pdf 2>/dev/null || true
	@echo "=== Paper 4 built: synthesis/build/paper4_em_gravity_unification.pdf ==="

# Paper 5: Experimental Protocols for Exotic Quantum States
paper5:
	@echo "=== Building Paper 5: Experimental Protocols ==="
	@mkdir -p synthesis/build
	cd synthesis/papers/paper5_experimental_protocols && \
		pdflatex -interaction=nonstopmode -halt-on-error paper5_main.tex && \
		bibtex paper5_main || true && \
		pdflatex -interaction=nonstopmode -halt-on-error paper5_main.tex && \
		pdflatex -interaction=nonstopmode -halt-on-error paper5_main.tex
	@mv synthesis/papers/paper5_experimental_protocols/paper5_main.pdf synthesis/build/paper5_experimental_protocols.pdf 2>/dev/null || true
	@echo "=== Paper 5 built: synthesis/build/paper5_experimental_protocols.pdf ==="

# Paper 6: Applications to Quantum Computing and Energy Technologies
paper6:
	@echo "=== Building Paper 6: Applications ==="
	@mkdir -p synthesis/build
	cd synthesis/papers/paper6_applications && \
		pdflatex -interaction=nonstopmode -halt-on-error paper6_main.tex && \
		bibtex paper6_main || true && \
		pdflatex -interaction=nonstopmode -halt-on-error paper6_main.tex && \
		pdflatex -interaction=nonstopmode -halt-on-error paper6_main.tex
	@mv synthesis/papers/paper6_applications/paper6_main.pdf synthesis/build/paper6_applications.pdf 2>/dev/null || true
	@echo "=== Paper 6 built: synthesis/build/paper6_applications.pdf ==="

# Build all six papers
papers_all: paper1-new paper2 paper3 paper4 paper5 paper6
	@echo "================================================================"
	@echo "All papers built successfully!"
	@echo "================================================================"
	@ls -lh synthesis/build/*.pdf

# Clean all paper build artifacts
papers_clean:
	@echo "=== Cleaning all paper build artifacts ==="
	find synthesis/papers -name "*.aux" -delete
	find synthesis/papers -name "*.log" -delete
	find synthesis/papers -name "*.out" -delete
	find synthesis/papers -name "*.toc" -delete
	find synthesis/papers -name "*.bbl" -delete
	find synthesis/papers -name "*.blg" -delete
	find synthesis/papers -name "*.fls" -delete
	find synthesis/papers -name "*.fdb_latexmk" -delete
	find synthesis/papers -name "*.synctex.gz" -delete
	rm -f synthesis/build/*.pdf
	@echo "=== All paper artifacts cleaned ==="

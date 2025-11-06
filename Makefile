SHELL := /bin/bash

BASE_DIR ?= .
SCANS ?= notes .

.PHONY: pipeline audit parity gaps validate bench smoke test ci link latex latex_strict todo reports ascii_guard ascii_normalize update_data_readme

pipeline:
	python scripts/build_catalog_pipeline.py --base-dir $(BASE_DIR) $(foreach d,$(SCANS),--scan-dir $(d))

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

smoke:
	python scripts/test_extraction_smoke.py

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

"""
Validate an extractor metrics JSON file against a minimal schema contract
without external dependencies. For a full check, consult docs/metrics.schema.json.
"""

from __future__ import annotations

import sys
import json
from pathlib import Path


def fail(msg: str) -> None:
    print(f"Validation failed: {msg}")
    sys.exit(1)


def validate_metrics(path: Path) -> None:
    try:
        obj = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        fail(f"Could not read/parse JSON: {e}")

    if not isinstance(obj, dict):
        fail("Top-level JSON is not an object")

    for k in ("stats", "metrics"):
        if k not in obj:
            fail(f"Missing key: {k}")

    stats = obj["stats"]
    metrics = obj["metrics"]
    if not isinstance(stats, dict) or not isinstance(metrics, dict):
        fail("'stats' or 'metrics' is not an object")

    for k in ("total", "by_framework", "by_domain", "by_source"):
        if k not in stats:
            fail(f"stats missing: {k}")
    for k in ("files_scanned", "bytes_scanned", "candidate_equations", "unique_equations", "elapsed_s", "timing"):
        if k not in metrics:
            fail(f"metrics missing: {k}")

    # Type checks and invariants
    if not isinstance(stats["total"], int):
        fail("stats.total not integer")
    if not isinstance(metrics["elapsed_s"], (int, float)):
        fail("metrics.elapsed_s not number")
    if not (isinstance(metrics.get("unique_equations"), int) and isinstance(metrics.get("candidate_equations"), int)):
        fail("unique_equations/candidate_equations not integers")
    if metrics["unique_equations"] > metrics["candidate_equations"]:
        fail("unique_equations exceeds candidate_equations")

    timing = metrics["timing"]
    for k in ("total_elapsed_s", "read_s", "extract_s"):
        if k not in timing:
            fail(f"timing missing: {k}")
    # classify_s is present in enriched builds, optional here
    for tk in ("total_elapsed_s", "read_s", "extract_s"):
        if not isinstance(timing.get(tk), (int, float)):
            fail(f"timing.{tk} not number")

    print("Validation OK")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_metrics_schema.py METRICS.json")
        sys.exit(2)
    p = Path(sys.argv[1])
    if not p.exists():
        fail(f"File not found: {p}")
    validate_metrics(p)


if __name__ == "__main__":
    main()


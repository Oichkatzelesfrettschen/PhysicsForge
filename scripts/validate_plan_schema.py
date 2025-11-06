"""
Validate an extractor plan JSON file (from --plan-only) without external deps.
Checks structure and basic invariants as described in docs/PLAN_SCHEMA.md.
"""

from __future__ import annotations

import sys
import json
from pathlib import Path


VALID_REASONS = {
    'selected',
    'glob_exclude',
    'glob_not_included',
    'excluded_dir',
    'max_size',
    'limit_reached',
    'framework_include_mismatch',
    'framework_excluded',
}


def fail(msg: str) -> None:
    print(f"Validation failed: {msg}")
    sys.exit(1)


def validate_plan(path: Path) -> None:
    try:
        obj = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        fail(f"Could not read/parse JSON: {e}")

    if not isinstance(obj, dict):
        fail("Top-level JSON is not an object")

    for k in ('base_dir', 'elapsed_s', 'items'):
        if k not in obj:
            fail(f"Missing key: {k}")

    if not isinstance(obj['base_dir'], str):
        fail("base_dir must be a string")
    if not isinstance(obj['elapsed_s'], (int, float)):
        fail("elapsed_s must be a number")
    if not isinstance(obj['items'], list):
        fail("items must be a list")

    for i, it in enumerate(obj['items']):
        if not isinstance(it, dict):
            fail(f"items[{i}] not an object")
        for rk in ('path', 'rel', 'framework', 'action', 'reason', 'size'):
            if rk not in it:
                fail(f"items[{i}] missing: {rk}")
        if not isinstance(it['path'], str) or not isinstance(it['rel'], str):
            fail(f"items[{i}] path/rel must be strings")
        if it['action'] not in ('scan', 'skip'):
            fail(f"items[{i}] action invalid: {it['action']}")
        if it['reason'] not in VALID_REASONS:
            fail(f"items[{i}] reason invalid: {it['reason']}")
        if it['size'] is not None and not isinstance(it['size'], int):
            fail(f"items[{i}] size must be int or null")

    print("Validation OK")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_plan_schema.py PLAN.json")
        sys.exit(2)
    p = Path(sys.argv[1])
    if not p.exists():
        fail(f"File not found: {p}")
    validate_plan(p)


if __name__ == '__main__':
    main()


"""
Optional JSON Schema validator using 'jsonschema' if installed.
Usage:
  python scripts/validate_jsonschema.py metrics path/to/metrics.json
  python scripts/validate_jsonschema.py plan path/to/plan.json
Exits with non-zero code if validation fails or jsonschema is missing.
"""

from __future__ import annotations

import sys
import json
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python scripts/validate_jsonschema.py <metrics|plan> PATH.json")
        sys.exit(2)
    kind = sys.argv[1].strip().lower()
    path = Path(sys.argv[2])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    schema_file = None
    if kind == 'metrics':
        schema_file = Path(__file__).resolve().parents[1] / 'docs' / 'metrics.schema.json'
    elif kind == 'plan':
        schema_file = Path(__file__).resolve().parents[1] / 'docs' / 'plan.schema.json'
    else:
        print("Unknown kind; must be 'metrics' or 'plan'")
        sys.exit(2)

    try:
        import jsonschema  # type: ignore
    except Exception:
        print("jsonschema not installed. Install with 'pip install jsonschema' or see requirements-optional.txt")
        sys.exit(2)

    try:
        inst = json.loads(path.read_text(encoding='utf-8'))
        schema = json.loads(schema_file.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"Error reading JSON: {e}")
        sys.exit(1)

    try:
        jsonschema.validate(inst, schema)
        print("Validation OK")
    except jsonschema.ValidationError as e:  # type: ignore[attr-defined]
        print(f"Validation failed: {e.message}")
        sys.exit(1)


if __name__ == '__main__':
    main()


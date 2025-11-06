"""
Validates the data in the equation_catalog.csv file.

Usage:
  python scripts/validate_data.py --base-dir .
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description="Validate data file")
    ap.add_argument("--base-dir", type=str, default=".", help="Repository root")
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    data_file = base / "equation_catalog.csv"

    if not data_file.exists():
        print(f"Error: Data file not found: {data_file}")
        raise SystemExit(1)

    required_columns = ["id", "equation", "description", "framework"]
    valid_frameworks = ["Aether", "Genesis", "Pais", "Unified", "Math"]

    findings = []
    with open(data_file, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 2):
            for col in required_columns:
                if not row.get(col):
                    findings.append(f"Missing value for required column '{col}' in row {i}")
            
            if row.get("framework") and row["framework"] not in valid_frameworks:
                findings.append(f"Invalid framework '{row['framework']}' in row {i}")

    if findings:
        print("Data validation found the following issues:")
        for finding in findings:
            print(f"- {finding}")
        raise SystemExit(1)
    else:
        print("Data validation passed.")


if __name__ == "__main__":
    main()
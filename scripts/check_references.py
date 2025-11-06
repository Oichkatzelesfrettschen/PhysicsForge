"""
Checks the bibliography.bib file for completeness and consistency.

Usage:
  python scripts/check_references.py --base-dir .
"""

from __future__ import annotations

import argparse
from pathlib import Path

import bibtexparser


def main() -> None:
    ap = argparse.ArgumentParser(description="Check bibliography file")
    ap.add_argument("--base-dir", type=str, default=".", help="Repository root")
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    bib_file = base / "synthesis" / "bibliography.bib"

    if not bib_file.exists():
        print(f"Error: Bibliography file not found: {bib_file}")
        raise SystemExit(1)

    with open(bib_file, encoding="utf-8") as f:
        bib_database = bibtexparser.load(f)

    required_fields = ["author", "title", "year"]
    article_recommended_fields = ["journal", "volume", "pages", "doi"]
    book_recommended_fields = ["publisher", "isbn"]

    findings = []
    for entry in bib_database.entries:
        for field in required_fields:
            if field not in entry:
                findings.append(f"Missing required field '{field}' in entry '{entry['ID']}'")
        
        if entry["ENTRYTYPE"] == "article":
            for field in article_recommended_fields:
                if field not in entry:
                    findings.append(f"Missing recommended field '{field}' for article '{entry['ID']}'")
        elif entry["ENTRYTYPE"] == "book":
            for field in book_recommended_fields:
                if field not in entry:
                    findings.append(f"Missing recommended field '{field}' for book '{entry['ID']}'")

    if findings:
        print("Bibliography check found the following issues:")
        for finding in findings:
            print(f"- {finding}")
        raise SystemExit(1)
    else:
        print("Bibliography check passed.")


if __name__ == "__main__":
    main()

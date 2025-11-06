"""
Generate a prioritized gap TODO from equation_catalog.csv for rows lacking modules.
Groups by Framework and Domain, sorted by ImportanceScore.
"""

from __future__ import annotations

import csv
import argparse
from collections import defaultdict
from pathlib import Path


def load_catalog(p: Path) -> list[dict]:
    if not p.exists():
        return []
    try:
        with p.open('r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: Catalog file not found: {p}")
    except IOError as e:
        print(f"Error reading catalog file {p}: {e}")
    return []


def main() -> None:
    ap = argparse.ArgumentParser(description='Generate gap TODO list from catalog')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--catalog', type=str, default='equation_catalog.csv', help='Catalog path')
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    had_errors = False
    rows = load_catalog(base / args.catalog)
    if not rows:
        print(f"Error: No catalog rows found at {base / args.catalog} or catalog could not be loaded.")
        had_errors = True

    buckets = defaultdict(list)
    for r in rows:
        if not (r.get('RelatedEqs') or '').startswith('module:'):
            key = (r.get('Framework','General'), r.get('Domain','General'))
            buckets[key].append(r)

    # Sort within buckets by ImportanceScore desc
    for key in buckets:
        buckets[key].sort(key=lambda r: int(r.get('ImportanceScore') or 0) if r.get('ImportanceScore', '').isdigit() else 0, reverse=True)

    out = base / 'CATALOG_GAPS_TODO.md'
    try:
        with out.open('w', encoding='utf-8') as f:
            f.write('# Catalog Gaps - TODO\n\n')
            f.write('Prioritized missing modules grouped by Framework/Domain.\n\n')
            for (fw, dom), items in sorted(buckets.items()):
                f.write(f'## {fw} / {dom} - {len(items)} missing\n')
                for r in items[:50]:
                    score = r.get('ImportanceScore', '0')
                    eq = r.get('Equation','')
                    eq_disp = (eq[:120] + '...') if len(eq) > 120 else eq
                    f.write(f"- [{score}] {r.get('EqID','')} - {eq_disp} (source {r.get('SourceDoc','')})\n")
                f.write('\n')
            f.write('\n')
            f.write('Actions:\n')
            f.write('- Use `scripts/auto_create_modules.py` to generate top items.\n')
            f.write('- Manually refine TeX and labels; include via chapters or modules_index_auto.tex.\n')

        print(f'Gap TODO written: {out}')
    except IOError as e:
        print(f"Error writing gap TODO report {out}: {e}")
        had_errors = True

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()



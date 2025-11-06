"""
Validate equation_catalog.csv for schema, consistency, and basic quality gates.
Writes VALIDATION_REPORT.md and exits with non-zero on critical failures.
"""

from __future__ import annotations

import csv
import argparse
from pathlib import Path
from collections import Counter


REQUIRED_FIELDS = [
    'EqID', 'Equation', 'Framework', 'Domain', 'SourceDoc', 'SourceLine',
    'Description', 'VerificationStatus'
]

ALLOWED_DOMAINS = {'QM', 'GR', 'EM', 'Thermo', 'Math', 'Experimental', 'General'}
ALLOWED_STATUS = {'Theoretical', 'Experimental', 'Validated', 'Speculative'}


def load_catalog(path: Path) -> tuple[list[dict], bool]:
    if not path.exists():
        print(f"Error: Catalog not found: {path}")
        return [], True
    try:
        with path.open('r', encoding='utf-8') as f:
            return list(csv.DictReader(f)), False
    except IOError as e:
        print(f"Error reading catalog file {path}: {e}")
        return [], True
    except UnicodeDecodeError:
        print(f"Error: Could not decode catalog file as UTF-8 (non-ASCII content?): {path}")
        return [], True


def validate(rows: list[dict]) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    # Presence of required fields
    if not rows:
        errors.append('Catalog contains no rows')
        return {'errors': errors, 'warnings': warnings, 'stats': {}}

    headers = rows[0].keys()
    for fld in REQUIRED_FIELDS:
        if fld not in headers:
            errors.append(f'Missing required field: {fld}')

    # Unique EqID
    seen = set()
    for r in rows:
        eid = r.get('EqID', '')
        if not eid:
            errors.append('Empty EqID encountered')
        elif eid in seen:
            errors.append(f'Duplicate EqID: {eid}')
        else:
            seen.add(eid)

    # Domain and Status checks
    for r in rows:
        dom = r.get('Domain', 'General')
        if dom not in ALLOWED_DOMAINS:
            warnings.append(f'Unknown Domain: {dom} (EqID {r.get("EqID")})')
        st = r.get('VerificationStatus', 'Theoretical')
        if st not in ALLOWED_STATUS:
            warnings.append(f'Unknown VerificationStatus: {st} (EqID {r.get("EqID")})')

    # Basic distribution stats
    by_fw = Counter(r.get('Framework', 'Unknown') for r in rows)
    by_dom = Counter(r.get('Domain', 'Unknown') for r in rows)
    by_status = Counter(r.get('VerificationStatus', 'Unknown') for r in rows)

    return {
        'errors': errors,
        'warnings': warnings,
        'stats': {
            'total': len(rows),
            'by_framework': by_fw,
            'by_domain': by_dom,
            'by_status': by_status,
        },
    }


def write_report(base: Path, result: dict) -> tuple[Path | None, bool]:
    out = base / 'VALIDATION_REPORT.md'
    try:
        with out.open('w', encoding='utf-8') as f:
            f.write('# Catalog Validation Report\n\n')
            f.write(f"Total Rows: {result['stats'].get('total', 0)}\n\n")
            if result['errors']:
                f.write('## Errors\n')
                for e in result['errors']:
                    f.write(f'- {e}\n')
                f.write('\n')
            if result['warnings']:
                f.write('## Warnings\n')
                for w in result['warnings']:
                    f.write(f'- {w}\n')
                f.write('\n')
            f.write('## Stats\n')
            for sec in ['by_framework', 'by_domain', 'by_status']:
                f.write(f'### {sec}\n')
                for k, v in result['stats'].get(sec, {}).most_common():
                    f.write(f'- {k}: {v}\n')
                f.write('\n')
        return out, True
    except IOError as e:
        print(f"Error writing validation report {out}: {e}")
        return None, False


def main() -> None:
    ap = argparse.ArgumentParser(description='Validate equation catalog CSV')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--catalog', type=str, default='equation_catalog.csv', help='Catalog path')
    args = ap.parse_args()

    had_errors = False
    try:
        base = Path(args.base_dir).resolve()
    except FileNotFoundError:
        print(f"Error: Repository root directory not found: {args.base_dir}")
        raise SystemExit(1)
    rows, load_had_errors = load_catalog(base / args.catalog)
    if load_had_errors:
        had_errors = True

    result = validate(rows)
    out, report_success = write_report(base, result)
    if not report_success:
        had_errors = True
        print('Validation report generation failed.')
    else:
        print(f'Report written: {out}')
    if result['errors']:
        raise SystemExit(2)
    elif had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()


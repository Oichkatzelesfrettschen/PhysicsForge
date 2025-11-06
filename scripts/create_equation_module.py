"""
Create a LaTeX equation module from an equation_catalog.csv row.
Usage:
  python scripts/create_equation_module.py --eqid AE001 --base-dir .
Writes synthesis/modules/equations/eq_<eqid>_auto.tex
"""

from __future__ import annotations

import csv
import argparse
from pathlib import Path
import re


def load_row(catalog: Path, eqid: str) -> dict | None:
    try:
        with catalog.open('r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                if row.get('EqID') == eqid:
                    return row
    except FileNotFoundError:
        print(f"Error: Catalog file not found: {catalog}")
    except IOError as e:
        print(f"Error reading catalog file {catalog}: {e}")
    return None


def safe_label(text: str) -> str:
    t = re.sub(r"[^a-zA-Z0-9:_-]", "-", text)
    return t.lower()


def write_module(base: Path, row: dict) -> Path | None:
    mod_dir = base / 'synthesis' / 'modules' / 'equations'
    mod_dir.mkdir(parents=True, exist_ok=True)
    eqid = row['EqID']
    fname = mod_dir / f"eq_{eqid.lower()}_auto.tex"
    framework = row.get('Framework', 'General')
    domain = row.get('Domain', 'General')
    status = row.get('VerificationStatus', 'Theoretical')
    label = safe_label(f"eq:{framework}:{eqid}")
    src = f"{row.get('SourceDoc','')} (line {row.get('SourceLine','')})"
    eq = row.get('Equation', '')
    desc = row.get('Description', '')
    body = f"""
% Auto-generated from equation_catalog.csv
% EqID: {eqid}
% Framework: {framework} | Domain: {domain} | Status: {status}
% Source: {src}
% Description: {desc[:120]}
\begin{{equation}}
  {eq}
  \label{{{label}}}
\end{{equation}}
""".strip() + "\n"
    try:
        fname.write_text(body, encoding='utf-8')
        return fname
    except IOError as e:
        print(f"Error writing module {fname}: {e}")
        return None


def main() -> None:
    ap = argparse.ArgumentParser(description='Create LaTeX module from catalog row')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--catalog', type=str, default='equation_catalog.csv', help='Catalog CSV path')
    ap.add_argument('--eqid', type=str, required=True, help='Equation ID to export')
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    had_errors = False
    row = load_row(base / args.catalog, args.eqid)
    if row:
        out = write_module(base, row)
        if out is None:
            had_errors = True
            print('Module writing failed.')
        else:
            print(f'Wrote module: {out}')

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()


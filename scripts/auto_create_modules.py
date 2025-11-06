"""
Auto-create LaTeX equation modules for catalog rows lacking module links.

Usage examples:
  python scripts/auto_create_modules.py --base-dir . --limit 50 --min-score 10
  python scripts/auto_create_modules.py --base-dir . --framework Aether
"""

from __future__ import annotations

import csv
import argparse
from pathlib import Path
from typing import Iterable


def load_catalog(catalog: Path) -> list[dict]:
    if not catalog.exists():
        return []
    with catalog.open('r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def needs_module(row: dict) -> bool:
    rel = (row.get('RelatedEqs') or '').strip()
    return not rel or not rel.startswith('module:')


def write_module(base: Path, row: dict) -> tuple[Path | None, bool]:
    mod_dir = base / 'synthesis' / 'modules' / 'equations'
    mod_dir.mkdir(parents=True, exist_ok=True)
    eqid = row['EqID']
    fname = mod_dir / f"eq_{eqid.lower()}_auto.tex"
    framework = row.get('Framework', 'General')
    domain = row.get('Domain', 'General')
    status = row.get('VerificationStatus', 'Theoretical')
    label = f"eq:{framework}:{eqid}".lower()
    src = f"{row.get('SourceDoc','')} (line {row.get('SourceLine','')})"
    eq = row.get('Equation', '')
    desc = row.get('Description', '')
    body = f"""
% Auto-generated from equation_catalog.csv
% EqID: {eqid}
% Framework: {framework} | Domain: {domain} | Status: {status}
% Source: {src}
% Description: {desc[:160]}
\begin{{equation}}
  {eq}
  \label{{{label}}}
\end{{equation}}
""".strip() + "\n"
    try:
        fname.write_text(body, encoding='utf-8')
        return fname, True
    except IOError as e:
        print(f"Error writing module {fname}: {e}")
        return None, False


def generate_index(base: Path) -> tuple[Path | None, bool]:
    eq_dir = base / 'synthesis' / 'modules' / 'equations'
    index_path = base / 'synthesis' / 'modules' / 'modules_index_auto.tex'
    index_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        '% Auto-generated index of equation modules',
    ]
    if eq_dir.exists():
        for tex in sorted(eq_dir.glob('eq_*_auto.tex')):
            # modules_index_auto.tex lives in synthesis/modules, so use path relative to that folder
            rel = tex.relative_to(base / 'synthesis' / 'modules')
            lines.append(f"\\input{{{rel.as_posix()[:-4]}}}")  # strip .tex
    try:
        index_path.write_text("\n".join(lines) + "\n", encoding='utf-8')
        return index_path, True
    except IOError as e:
        print(f"Error writing index {index_path}: {e}")
        return None, False


def main() -> None:
    ap = argparse.ArgumentParser(description='Auto-create LaTeX modules for missing catalog rows')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--catalog', type=str, default='equation_catalog.csv', help='Path to catalog CSV')
    ap.add_argument('--limit', type=int, default=0, help='Maximum modules to create (0=all)')
    ap.add_argument('--min-score', type=int, default=None, help='Minimum ImportanceScore required')
    ap.add_argument('--framework', type=str, default=None, help='Filter by Framework')
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    had_errors = False
    rows = load_catalog(base / args.catalog)
    if not rows:
        raise SystemExit(f"No catalog rows found at {base / args.catalog}")

    # Filter
    filtered: Iterable[dict] = (r for r in rows if needs_module(r))
    if args.min_score is not None:
        def ok(r: dict) -> bool:
            try:
                return int(r.get('ImportanceScore') or 0) >= args.min_score
            except ValueError:
                return False
        filtered = (r for r in filtered if ok(r))
    if args.framework:
        fw = args.framework.lower()
        filtered = (r for r in filtered if (r.get('Framework','').lower() == fw))

    # Sort by ImportanceScore desc if available
    try:
        sorted_rows = sorted(filtered, key=lambda r: int(r.get('ImportanceScore') or 0), reverse=True)
    except ValueError:
        sorted_rows = list(filtered)

    count = 0
    for row in sorted_rows:
        _, success = write_module(base, row)
        if not success:
            had_errors = True
            continue
        count += 1
        if args.limit and count >= args.limit:
            break
    idx, success = generate_index(base)
    if not success:
        had_errors = True
        print(f'Created {count} modules. Index generation failed.')
    else:
        print(f'Created {count} modules. Index: {idx}')

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

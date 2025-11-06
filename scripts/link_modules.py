"""
Link catalog rows to auto-generated LaTeX modules by EqID.
If RelatedEqs is empty, fill with module:<path>#<label> for eq_<eqid>_auto.tex
Writes equation_catalog.csv in-place and equation_catalog_linked.csv backup.
"""

from __future__ import annotations

import csv
import argparse
from pathlib import Path
import re


def read_label(tex_path: Path) -> tuple[str, bool]:
    had_errors_in_label = False
    try:
        s = tex_path.read_text(encoding='utf-8', errors='strict')
    except UnicodeDecodeError:
        print(f"Warning: Could not decode LaTeX module as UTF-8 (non-ASCII content?): {tex_path}")
        had_errors_in_label = True
        return tex_path.stem, had_errors_in_label
    except IOError as e:
        print(f"Error reading LaTeX module {tex_path}: {e}")
        had_errors_in_label = True
        return tex_path.stem, had_errors_in_label
    m = re.search(r"\\label\{([^}]+)\}", s)
    return (m.group(1) if m else tex_path.stem), had_errors_in_label


def build_eqid_map(base: Path) -> tuple[dict[str, str], bool]:
    eq_dir = base / 'synthesis' / 'modules' / 'equations'
    mapping: dict[str, str] = {}
    had_errors_in_map = False
    if not eq_dir.exists():
        return mapping, had_errors_in_map
    for tex in eq_dir.glob('eq_*_auto.tex'):
        # Expect filename: eq_<eqid>_auto.tex
        name = tex.stem  # eq_ae001_auto
        parts = name.split('_')
        if len(parts) >= 3:
            eqid = parts[1].upper()
            label, label_had_errors = read_label(tex)
            if label_had_errors:
                had_errors_in_map = True
            rel = tex.relative_to(base).as_posix()
            mapping[eqid] = f"{rel}#{label}"
    return mapping, had_errors_in_map


def link_catalog(base: Path, catalog_path: Path, eq_map: dict[str, str]) -> tuple[Path | None, bool]:
    rows = []
    try:
        with catalog_path.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or []
            for r in reader:
                rows.append(r)
    except FileNotFoundError:
        print(f"Error: Catalog file not found: {catalog_path}")
        return None, False
    except IOError as e:
        print(f"Error reading catalog file {catalog_path}: {e}")
        return None, False

    updated = 0
    for r in rows:
        if not (r.get('RelatedEqs') or '').strip():
            eqid = (r.get('EqID') or '').upper()
            if eqid in eq_map:
                r['RelatedEqs'] = f"module:{eq_map[eqid]}"
                updated += 1

    # Write backup and in-place
    linked = base / 'equation_catalog_linked.csv'
    try:
        with linked.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except IOError as e:
        print(f"Error writing linked catalog backup {linked}: {e}")
        return None, False

    try:
        with catalog_path.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except IOError as e:
        print(f"Error writing updated catalog {catalog_path}: {e}")
        return None, False

    print(f'Linked {updated} rows to modules')
    return linked, True


def main() -> None:
    ap = argparse.ArgumentParser(description='Link catalog rows to LaTeX modules by EqID')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--catalog', type=str, default='equation_catalog.csv', help='Catalog CSV path')
    args = ap.parse_args()
    base = Path(args.base_dir).resolve()
    had_errors = False
    eq_map, map_had_errors = build_eqid_map(base)
    if map_had_errors:
        had_errors = True

    linked, link_success = link_catalog(base, base / args.catalog, eq_map)
    if not link_success:
        had_errors = True
        print('Linked catalog generation failed.')
    else:
        print(f'Wrote linked catalog: {linked}')

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()


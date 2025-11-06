"""
Catalog <-> LaTeX module parity checker.
Produces CATALOG_PARITY.md summarizing:
 - Catalog entries without module links
 - Modules not referenced by catalog
"""

from __future__ import annotations

import csv
import argparse
from pathlib import Path
import re


def strip_tex(text: str) -> str:
    t = re.sub(r"%.*", "", text)
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", "", t)
    t = re.sub(r"\$+", "", t)
    t = re.sub(r"[{}]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def normalize(s: str) -> str:
    s = re.sub(r"\s+", " ", s.strip())
    s = s.replace(' = ', '=').replace('= ', '=').replace(' =', '=')
    return s


def load_modules(base: Path) -> dict[str, str]:
    eq_dir = base / 'synthesis' / 'modules' / 'equations'
    mapping: dict[str, str] = {}
    if not eq_dir.exists():
        return mapping
    for tex in eq_dir.rglob('*.tex'):
        try:
            content = tex.read_text(encoding='utf-8', errors='strict')
        except UnicodeDecodeError:
            # Skip non-UTF-8 module files
            continue
        m_label = re.search(r"\\label\{([^}]+)\}", content)
        label = m_label.group(1) if m_label else tex.stem
        bodies = []
        # Simple substring search to avoid regex escape issues on Python 3.13
        start_tag = "\\begin{equation}"
        end_tag = "\\end{equation}"
        idx = 0
        while True:
            s = content.find(start_tag, idx)
            if s == -1:
                break
            e = content.find(end_tag, s + len(start_tag))
            if e == -1:
                break
            bodies.append(content[s+len(start_tag):e])
            idx = e + len(end_tag)
        if not bodies:
            # Try display math \[ ... \]
            start_tag = "\\["
            end_tag = "\\]"
            idx = 0
            while True:
                s = content.find(start_tag, idx)
                if s == -1:
                    break
                e = content.find(end_tag, s + len(start_tag))
                if e == -1:
                    break
                bodies.append(content[s+len(start_tag):e])
                idx = e + len(end_tag)
        for body in bodies:
            norm = normalize(strip_tex(body))
            if norm:
                mapping[norm] = f"{tex.relative_to(base)}#{label}"
    return mapping


def load_catalog(catalog: Path) -> list[dict]:
    rows: list[dict] = []
    if not catalog.exists():
        return rows
    with catalog.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows.extend(reader)
    return rows


def write_report(base: Path, catalog_rows: list[dict], module_map: dict[str, str]) -> Path | None:
    out = base / 'CATALOG_PARITY.md'
    without_link = [r for r in catalog_rows if not r.get('RelatedEqs')]

    # Build reverse: module bodies set
    module_paths = set(module_map.values())

    # Find modules not referenced by any catalog row (by path in RelatedEqs)
    referenced = set()
    for r in catalog_rows:
        rel = r.get('RelatedEqs', '')
        if rel.startswith('module:'):
            referenced.add(rel.split('module:', 1)[1])
    unreferenced = sorted(module_paths - referenced)

    try:
        with out.open('w', encoding='utf-8') as f:
            f.write('# Catalog <-> Module Parity\n\n')
            f.write(f'- Catalog rows: {len(catalog_rows)}\n')
            f.write(f'- Module equations indexed: {len(module_map)}\n')
            f.write(f'- Rows without module link: {len(without_link)}\n')
            f.write(f'- Unreferenced modules: {len(unreferenced)}\n\n')

            f.write('## Rows Without Module Link (first 50)\n')
            for r in without_link[:50]:
                eq = r.get('Equation', '')
                eq_disp = (eq[:100] + '...') if len(eq) > 100 else eq
                f.write(f"- {r.get('EqID','')} | {r.get('Framework','')} | {eq_disp}\n")
            f.write('\n')

            f.write('## Unreferenced Modules\n')
            for p in unreferenced[:200]:
                f.write(f'- {p}\n')
            f.write('\n')

            f.write('## Actions\n')
            f.write('- Add missing LaTeX modules for high-priority catalog rows.\n')
            f.write('- Adjust extractor normalization if equations differ due to macro formatting.\n')
            f.write('- Ensure chapters input the module files instead of re-embedding equations.\n')
        return out
    except IOError as e:
        print(f"Error writing parity report {out}: {e}")
        return None, False


def main() -> None:
    ap = argparse.ArgumentParser(description='Check parity between catalog and LaTeX modules')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--catalog', type=str, default='equation_catalog.csv', help='Path to catalog CSV')
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    had_errors = False
    module_map = load_modules(base)
    catalog_rows = load_catalog(base / args.catalog)
    out = write_report(base, catalog_rows, module_map)
    if out is None:
        had_errors = True
        print('Parity report generation failed.')
    else:
        print(f'Parity report written: {out}')

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()




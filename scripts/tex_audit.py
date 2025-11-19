"""
TeX Audit: recursively scan all .tex files and report structure, packages,
equation/label statistics, include graph, duplicates, encoding issues.

Outputs TEX_AUDIT.md at the repository root.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
from collections import Counter


DOC_RE = re.compile(r"\\documentclass(?:\[[^\]]*\])?\{([^}]+)\}")
PKG_RE = re.compile(r"\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}")
INC_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")


EQ_ENVS = [
    "equation", "equation*", "align", "align*", "gather", "gather*",
    "multline", "multline*", "eqnarray"
]


def find_env_spans(text: str, env: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    btag = f"\\begin{{{env}}}"
    etag = f"\\end{{{env}}}"
    i = 0
    while True:
        s = text.find(btag, i)
        if s == -1:
            break
        e = text.find(etag, s + len(btag))
        if e == -1:
            break
        spans.append((s + len(btag), e))
        i = e + len(etag)
    return spans


def audit_tex_file(base: Path, path: Path) -> tuple[dict, bool]:
    had_errors_local = False
    try:
        content = path.read_text(encoding='utf-8', errors='strict')
    except UnicodeDecodeError:
        print(f"Warning: Could not decode TeX file as UTF-8 (non-ASCII content?): {path}")
        had_errors_local = True
        content = ""
    except IOError as e:
        print(f"Error reading TeX file {path}: {e}")
        had_errors_local = True
        content = ""

    rel = path.relative_to(base).as_posix()
    size = 0
    try:
        size = path.stat().st_size
    except OSError as e:
        print(f"Warning: Could not stat file {path}: {e}")
        had_errors_local = True

    non_ascii = sum(1 for ch in content if ord(ch) > 127)
    braces_delta = content.count('{') - content.count('}')

    docclass = DOC_RE.search(content)
    docclass_name = docclass.group(1) if docclass else ''

    pkgs = []
    for m in PKG_RE.finditer(content):
        # Packages may be comma-separated
        for pkg in m.group(1).split(','):
            p = pkg.strip()
            if p:
                pkgs.append(p)

    includes = [m.group(1).strip() for m in INC_RE.finditer(content)]
    include_resolved = []
    include_missing = []
    for inc in includes:
        candidate = inc
        if not os.path.splitext(candidate)[1]:
            candidate = inc + '.tex'
        inc_path = (path.parent / candidate).resolve()
        try:
            if inc_path.exists():
                include_resolved.append(str(inc_path.relative_to(base).as_posix()))
            else:
                include_missing.append(inc)
        except OSError as e:
            print(f"Warning: Error resolving include path {inc_path}: {e}")
            had_errors_local = True
            include_missing.append(inc)

    # Equation envs and labels
    eq_count = 0
    eq_with_label = 0
    for env in EQ_ENVS:
        for s, e in find_env_spans(content, env):
            eq_count += 1
            if LABEL_RE.search(content[s:e]):
                eq_with_label += 1

    labels = [m.group(1) for m in LABEL_RE.finditer(content)]

    return {
        'file': rel,
        'size': size,
        'non_ascii': non_ascii,
        'braces_delta': braces_delta,
        'docclass': docclass_name,
        'packages': pkgs,
        'includes': includes,
        'include_resolved': include_resolved,
        'include_missing': include_missing,
        'equations': eq_count,
        'eq_with_label': eq_with_label,
        'labels': labels,
    }, had_errors_local


def audit_repo(base: Path) -> tuple[dict, bool]:
    files = []
    had_errors_local = False
    try:
        files = list(base.rglob('*.tex'))
    except OSError as e:
        print(f"Error traversing directory {base}: {e}")
        had_errors_local = True

    reports = []
    pkg_counter = Counter()
    label_counter = Counter()
    missing_includes = []
    by_docclass = Counter()
    total_eq = 0
    total_eq_with_label = 0
    for p in files:
        rep, file_had_errors = audit_tex_file(base, p)
        if file_had_errors:
            had_errors_local = True
        reports.append(rep)
        pkg_counter.update(rep['packages'])
        label_counter.update(rep['labels'])
        missing_includes.extend((rep['file'], m) for m in rep['include_missing'])
        if rep['docclass']:
            by_docclass[rep['docclass']] += 1
        total_eq += rep['equations']
        total_eq_with_label += rep['eq_with_label']

    duplicate_labels = [lbl for lbl, cnt in label_counter.items() if cnt > 1]
    return {
        'files': reports,
        'pkg_counter': pkg_counter,
        'duplicate_labels': duplicate_labels,
        'missing_includes': missing_includes,
        'by_docclass': by_docclass,
        'total_tex': len(files),
        'total_eq': total_eq,
        'total_eq_with_label': total_eq_with_label,
    }, had_errors_local


def write_report(base: Path, data: dict) -> tuple[Path | None, bool]:
    out = base / 'TEX_AUDIT.md'
    try:
        with out.open('w', encoding='utf-8') as f:
            f.write('# TeX Audit\n\n')
            f.write(f"Total TeX files: {data['total_tex']}\n")
            f.write(f"Total equations: {data['total_eq']} (with labels: {data['total_eq_with_label']})\n\n")

            f.write('## Documentclasses\n')
            for k, v in data['by_docclass'].most_common():
                f.write(f'- {k}: {v}\n')
            f.write('\n')

            f.write('## Packages (top 30)\n')
            for pkg, cnt in data['pkg_counter'].most_common(30):
                f.write(f'- {pkg}: {cnt}\n')
            f.write('\n')

            if data['duplicate_labels']:
                f.write('## Duplicate Labels\n')
                for lbl in sorted(data['duplicate_labels']):
                    f.write(f'- {lbl}\n')
                f.write('\n')

            if data['missing_includes']:
                f.write('## Missing Includes\n')
                for (src, inc) in data['missing_includes'][:200]:
                    f.write(f'- {src}: {inc}\n')
                f.write('\n')

            f.write('## Files\n')
            for rep in sorted(data['files'], key=lambda r: r['file']):
                f.write(f"### {rep['file']}\n")
                f.write(f"- Size: {rep['size']} bytes\n")
                f.write(f"- Non-ASCII chars: {rep['non_ascii']}\n")
                if rep['braces_delta'] != 0:
                    f.write(f"- Brace imbalance: {rep['braces_delta']}\n")
                if rep['docclass']:
                    f.write(f"- Documentclass: {rep['docclass']}\n")
                if rep['packages']:
                    f.write(f"- Packages: {', '.join(sorted(set(rep['packages'])))}\n")
                f.write(f"- Equations: {rep['equations']} (with labels: {rep['eq_with_label']})\n")
                if rep['include_resolved']:
                    f.write(f"- Includes resolved: {len(rep['include_resolved'])}\n")
                if rep['include_missing']:
                    f.write(f"- Includes missing: {len(rep['include_missing'])} - {', '.join(rep['include_missing'][:5])}\n")
                f.write('\n')

        return out, True
    except IOError as e:
        print(f"Error writing TeX audit report {out}: {e}")
        return None, False


def main() -> None:
    ap = argparse.ArgumentParser(description='Audit TeX structures across the repository')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    args = ap.parse_args()

    had_errors = False
    try:
        base = Path(args.base_dir).resolve()
    except FileNotFoundError:
        print(f"Error: Repository root directory not found: {args.base_dir}")
        raise SystemExit(1)
    data, audit_had_errors = audit_repo(base)
    if audit_had_errors:
        had_errors = True

    out, report_success = write_report(base, data)
    if not report_success:
        had_errors = True
        print('TeX audit report generation failed.')
    else:
        print(f'Audit written: {out}')

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()



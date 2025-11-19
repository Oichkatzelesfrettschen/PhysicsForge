"""
TODO/FIXME/TBD scanner that writes a consolidated tracker to the repo root.

Usage:
  python scripts/todowrite.py --base-dir . [--include notes scripts synthesis docs] [--exclude extracted_data]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

PATTERNS = [
    (re.compile(r"\bFIXME\b", re.IGNORECASE), "FIXME"),
    (re.compile(r"\bTODO\b", re.IGNORECASE), "TODO"),
    (re.compile(r"\bTBD\b", re.IGNORECASE), "TBD"),
]

TEXT_EXTS = {
    ".md", ".txt", ".tex", ".py", ".ps1", ".sh", ".yml", ".yaml", ".json",
}


def iter_files(base: Path, include: list[str] | None, exclude: list[str] | None) -> tuple[list[Path], bool]:
    include_set = {p.strip("/\\") for p in (include or [])}
    exclude_set = {p.strip("/\\") for p in (exclude or [])}
    
    found_files = []
    had_errors_local = False
    try:
        for p in base.rglob("*"):
            try:
                if not p.is_file():
                    continue
            except OSError as e:
                print(f"Warning: Could not stat path {p}: {e}")
                had_errors_local = True
                continue

            if include_set and not any((base / inc) in [p] + list(p.parents) for inc in include_set):
                continue
            if any((base / exc) in [p] + list(p.parents) for exc in exclude_set):
                continue
            if p.suffix.lower() not in TEXT_EXTS:
                continue
            # Skip generated or cache content
            if any(seg in {"__pycache__", ".git"} for seg in p.parts):
                continue
            found_files.append(p)
    except OSError as e:
        print(f"Error traversing directory {base}: {e}")
        had_errors_local = True
    return found_files, had_errors_local


def scan_file(p: Path) -> tuple[list[tuple[int, str, str]], bool]:
    hits: list[tuple[int, str, str]] = []
    had_errors_local = False
    try:
        with p.open("r", encoding="utf-8", errors="strict") as f:
            for i, line in enumerate(f, 1):
                for rx, kind in PATTERNS:
                    if rx.search(line):
                        hits.append((i, kind, line.rstrip()))
    except UnicodeDecodeError:
        print(f"Warning: Could not decode file as UTF-8 (non-ASCII content?): {p}")
        had_errors_local = True
    except IOError as e:
        print(f"Error reading file {p}: {e}")
        had_errors_local = True
    except Exception as e:
        print(f"Unexpected error scanning file {p}: {e}")
        had_errors_local = True
    return hits, had_errors_local


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate TODO/FIXME tracker")
    ap.add_argument("--base-dir", type=str, default=".", help="Repository root")
    ap.add_argument("--include", action="append", help="Path prefixes to include (repeatable)")
    ap.add_argument("--exclude", action="append", help="Path prefixes to exclude (repeatable)")
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    had_errors = False
    try:
        base = Path(args.base_dir).resolve()
    except FileNotFoundError:
        print(f"Error: Repository root directory not found: {args.base_dir}")
        raise SystemExit(1)
    include = args.include or ["notes", "scripts", "synthesis", "docs"]
    exclude = args.exclude or ["extracted_data", "data/catalogs"]

    results: dict[str, list[tuple[int, str, str]]] = {}
    files_to_scan, iter_had_errors = iter_files(base, include, exclude)
    if iter_had_errors:
        had_errors = True

    for p in files_to_scan:
        hits, scan_had_errors = scan_file(p)
        if scan_had_errors:
            had_errors = True
        if hits:
            results[str(p.relative_to(base))] = hits

    out = base / "TODO_TRACKER.md"
    try:
        with out.open("w", encoding="utf-8") as f:
            f.write("# TODO / FIXME Tracker\n\n")
            f.write(f"Base: `{base}`\n\n")
            total = sum(len(v) for v in results.values())
            by_kind = {k: 0 for _, k in PATTERNS}
            for _, hits in results.items():
                for _, kind, _ in hits:
                    by_kind[kind] = by_kind.get(kind, 0) + 1
            f.write("## Summary\n")
            f.write(f"- Total findings: {total}\n")
            for kind, count in sorted(by_kind.items(), key=lambda x: x[0]):
                f.write(f"- {kind}: {count}\n")
            f.write("\n")

            f.write("## Findings by File\n")
            for relpath in sorted(results.keys()):
                f.write(f"\n### `{relpath}`\n")
                for line_no, kind, text in results[relpath]:
                    f.write(f"- L{line_no:>5} [{kind}] {text}\n")

        print(f"TODO tracker written: {out}")
    except IOError as e:
        print(f"Error writing TODO tracker file {out}: {e}")
        had_errors = True

    if had_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()


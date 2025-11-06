"""
ASCII Guard: scan code/docs for non-ASCII characters.
Fails with non-zero exit when any offending line is found.

Default include paths: scripts, tests, synthesis, docs, .github, root docs.
Excludes: data, extracted_data, source_materials, output.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


DEFAULT_INCLUDE = [
    "scripts",
    "tests",
    "docs",
    ".github",
]

DEFAULT_FILES = [
    "README.md",
    "INSTALLATION_REQUIREMENTS.md",
    "AGENTS.md",
    "gemini.md",
    "Makefile",
]

DEFAULT_EXCLUDE = [
    "data",
    "extracted_data",
    "source_materials",
    "output",
]

ALLOWED_NON_ASCII = {
    Path("tests/test_ascii_normalize.py"),
}
TEXT_EXTS = {
    ".md", ".txt", ".tex", ".py", ".ps1", ".sh", ".yml", ".yaml", ".json", ".csv", ".mk", "", ".cfg", ".ini"
}


def is_text_file(p: Path) -> bool:
    if p.suffix.lower() in TEXT_EXTS:
        return True
    return False


def iter_paths(base: Path, include: list[str], extra_files: list[str], exclude: list[str]) -> Iterable[Path]:
    inc = [base / i for i in include]
    exc = [base / e for e in exclude]
    for root in inc:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if any(e in p.parents for e in exc):
                continue
            if is_text_file(p):
                yield p
    for f in extra_files:
        p = base / f
        if p.exists() and p.is_file():
            yield p


def main() -> None:
    ap = argparse.ArgumentParser(description="ASCII-only guard for repository")
    ap.add_argument("--base-dir", type=str, default=".", help="Repository root")
    ap.add_argument("--include", action="append", help="Include dir (repeatable)")
    ap.add_argument("--exclude", action="append", help="Exclude dir (repeatable)")
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    include = args.include or DEFAULT_INCLUDE
    exclude = args.exclude or DEFAULT_EXCLUDE
    files = list(iter_paths(base, include, DEFAULT_FILES, exclude))

    violations: list[str] = []
    for p in files:
        rel_p = p.relative_to(base)
        if rel_p in ALLOWED_NON_ASCII:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except UnicodeDecodeError:
            # Treat undecodable files as binary; skip
            continue
        for i, ch in enumerate(text):
            if ord(ch) > 127:
                # Compute line/col
                # Simple counting approach
                line_no = text.count("\n", 0, i) + 1
                col = i - (text.rfind("\n", 0, i) if text.rfind("\n", 0, i) != -1 else -1)
                violations.append(f"{p}:{line_no}:{col} non-ASCII char U+{ord(ch):04X}")
                # Skip rest of line for brevity
                nl = text.find("\n", i)
                if nl == -1:
                    break
                else:
                    i = nl

    if violations:
        print("ASCII Guard: non-ASCII found in the following locations:")
        for v in violations[:200]:
            print(" -", v)
        print(f"Total violations: {len(violations)}")
        raise SystemExit(1)
    print("ASCII Guard: OK (no non-ASCII in code/docs)")


if __name__ == "__main__":
    main()

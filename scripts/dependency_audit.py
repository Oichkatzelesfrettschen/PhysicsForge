"""
Lightweight dependency auditor for the Python tooling.
Scans `scripts/` for imports and reports which optional deps are used and whether
they are importable in the current environment. Writes DEPS_REPORT.md to repo root.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
from pathlib import Path

KNOWN_OPTIONAL = {
    "fitz": "pymupdf",
    "pix2tex": "pix2tex",
    "PIL": "Pillow",
}

IMPORT_RX = re.compile(r"^(?:from\s+([\w\.]+)\s+import|import\s+([\w\.]+))")


def find_imports(scripts_dir: Path) -> tuple[set[str], bool]:
    mods: set[str] = set()
    had_errors_in_imports = False
    if not scripts_dir.exists():
        print(f"Error: Scripts directory not found: {scripts_dir}")
        return mods, True
    for p in scripts_dir.rglob("*.py"):
        try:
            content = p.read_text(encoding="utf-8", errors="strict")
            for line in content.splitlines():
                m = IMPORT_RX.match(line.strip())
                if not m:
                    continue
                mod = (m.group(1) or m.group(2) or "").split(".")[0]
                if mod:
                    mods.add(mod)
        except UnicodeDecodeError:
            print(f"Warning: Could not decode script file as UTF-8 (non-ASCII content?): {p}")
            had_errors_in_imports = True
            continue
        except IOError:
            print(f"Error reading script file {p}")
            had_errors_in_imports = True
            continue
        except Exception as e:
            print(f"Unexpected error processing script file {p}: {e}")
            had_errors_in_imports = True
            continue
    return mods, had_errors_in_imports


def is_importable(modname: str) -> bool:
    return importlib.util.find_spec(modname) is not None


def main() -> None:
    ap = argparse.ArgumentParser(description="Audit optional dependencies used by scripts")
    ap.add_argument("--base-dir", type=str, default=".", help="Repository root")
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    scripts_dir = base / "scripts"
    had_errors = False
    mods, imports_had_errors = find_imports(scripts_dir)
    if imports_had_errors:
        had_errors = True
    mods = sorted(list(mods))

    out = base / "DEPS_REPORT.md"
    try:
        with out.open("w", encoding="utf-8") as f:
            f.write("# Dependency Audit (scripts)\n\n")
            f.write(f"Base: `{base}`\n\n")
            f.write("## Optional Modules\n")
            for mod in mods:
                if mod in KNOWN_OPTIONAL:
                    pkg = KNOWN_OPTIONAL[mod]
                    ok = is_importable(mod)
                    status = "OK" if ok else "MISSING"
                    f.write(f"- {mod} (pip: `{pkg}`): {status}\n")
            f.write("\n")
            f.write("## All Top-level Imports (union)\n")
            for mod in mods:
                f.write(f"- {mod}\n")

        print(f"Dependency report written: {out}")
    except IOError as e:
        had_errors = True

    if had_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()


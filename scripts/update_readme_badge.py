"""
Update README CI badge with a concrete GitHub repo slug.

Usage:
  python scripts/update_readme_badge.py OWNER/REPO

Reads README.md, replaces the first occurrence of
  https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg
with the provided slug.
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2 or '/' not in sys.argv[1]:
        print("Usage: python scripts/update_readme_badge.py OWNER/REPO")
        sys.exit(2)
    slug = sys.argv[1]
    readme = Path('README.md')
    if not readme.exists():
        print("README.md not found")
        sys.exit(1)
    text = readme.read_text(encoding='utf-8')
    old = "https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg"
    new = f"https://github.com/{slug}/actions/workflows/ci.yml/badge.svg"
    if old not in text:
        print("Placeholder badge not found in README.md")
        sys.exit(1)
    readme.write_text(text.replace(old, new, 1), encoding='utf-8')
    print(f"Updated badge to: {new}")


if __name__ == '__main__':
    main()


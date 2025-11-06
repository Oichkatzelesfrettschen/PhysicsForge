"""
ASCII Normalizer: replaces common Unicode punctuation, arrows, math symbols,
greek letters, and superscripts/subscripts with ASCII equivalents.

Usage:
  python scripts/ascii_normalize.py --base-dir . --path docs --path synthesis

By default processes `.md` files only. Use `--ext` to add extensions.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_PATHS = ["docs", "synthesis"]
DEFAULT_EXTS = {".md"}


MAP = {
    # dashes and ellipsis
    "\u2013": "-",  # en dash
    "\u2014": "-",  # em dash
    "\u2015": "-",  # horizontal bar
    "\u2011": "-",  # non-breaking hyphen
    "\u2026": "...",
    # arrows
    "\u2192": "->",
    "\u2190": "<-",
    "\u2194": "<->",
    # math symbols
    "\u00D7": "x",   # multiplication sign
    "\u2260": "!=",  # not equal
    "\u2248": "~",   # approximately
    "\u221A": "sqrt",  # square root
    "\u222B": "integral",   # integral
    "\u2211": "sum",   # summation
    "\u220F": "prod",  # product
    "\u2207": "nabla",
    "\u2202": "partial",
    # greek letters (subset common)
    "\u03B1": " alpha",
    "\u03B2": " beta",
    "\u03B3": " gamma",
    "\u03B4": " delta",
    "\u03B5": " epsilon",
    "\u03B6": " zeta",
    "\u03B7": " eta",
    "\u03BA": " kappa",
    "\u03BC": " mu",
    "\u03BE": " xi",
    "\u03C0": " pi",
    "\u03C1": " rho",
    "\u03C3": " sigma",
    "\u03C6": " phi",
    "\u03C8": " psi",
    "\u03C9": " omega",
    "\u0394": " Delta",
    "\u039B": " Lambda",
    # superscripts/subscripts digits and signs
    "\u00B2": "^2",
    "\u00B3": "^3",
    "\u00B9": "^1",
    "\u2074": "^4",
    "\u2075": "^5",
    "\u2076": "^6",
    "\u207B": "^-",
    "\u2080": "_0",
    "\u2081": "_1",
    "\u2082": "_2",
    "\u2083": "_3",
    "\u2084": "_4",
    "\u2085": "_5",
    "\u2086": "_6",
    "\u2087": "_7",
    "\u2088": "_8",
    "\u2089": "_9",
    # checkmarks/crosses
    "\u2713": "[OK]",
    "\u2717": "[X]",
    # box drawing to ASCII dashes
    "\u2500": "-",
    "\u2502": "|",
    "\u251C": "+",
    "\u2524": "|",
    "\u2534": "+",
    "\u252C": "|",
    "\u2514": "+",
    "\u2510": "+",
    "\u2518": "+",
}


def normalize_text(s: str) -> str:
    for k, v in MAP.items():
        s = s.replace(k, v)
    # Collapse duplicate math words created by adjacent ASCII+symbol pairs
    dedup = {
        'sqrtsqrt': 'sqrt',
        'integralintegral': 'integral',
        'sumsum': 'sum',
        'prodprod': 'prod',
        'productprod': 'prod',
        'nablanabla': 'nabla',
        'partialpartial': 'partial',
    }
    for a, b in dedup.items():
        s = s.replace(a, b)
    # Collapse chained superscripts like ^1^6 -> ^16
    import re as _re
    prev = None
    while prev != s:
        prev = s
        s = _re.sub(r"\^([0-9])\^", r"^\1", s)
    # Collapse multiple spaces
    s = ' '.join(s.split())
    return s


def main() -> None:
    ap = argparse.ArgumentParser(description="Normalize Unicode in docs to ASCII")
    ap.add_argument("--base-dir", type=str, default=".", help="Repository root")
    ap.add_argument("--path", action="append", help="Path to process (repeatable)")
    ap.add_argument("--ext", action="append", help="File extension(s) like .md (repeatable)")
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    paths = args.path or DEFAULT_PATHS
    exts = set(args.ext or []) or DEFAULT_EXTS

    had_errors = False

    total = 0
    changed = 0
    for rel in paths:
        root = base / rel
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if p.is_file() and p.suffix.lower() in exts:
                total += 1
                try:
                    text = p.read_text(encoding="utf-8", errors="strict")
                except UnicodeDecodeError:
                    print(f"Error: Could not decode file as UTF-8 (non-ASCII content?): {p}")
                    had_errors = True
                    continue
                new = normalize_text(text)
                if new != text:
                    p.write_text(new, encoding="utf-8")
                    changed += 1
                    print(f"Normalized: {p}")
    print(f"Processed: {total}, Changed: {changed}")

    if had_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()




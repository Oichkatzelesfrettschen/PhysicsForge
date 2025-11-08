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
    "\u21A6": "|->",  # maps to
    "\u21D2": "=>",  # implies
    "\u21D0": "<=",  # implied by
    "\u21D4": "<=>",  # iff
    # math symbols
    "\u00D7": "*",   # multiplication sign
    "\u00F7": "/",   # division sign
    "\u00B1": "+/-", # plus-minus
    "\u2213": "-/+", # minus-plus
    "\u2260": "!=",  # not equal
    "\u2248": "~=",  # approximately
    "\u2243": "~=",  # asymptotically equal
    "\u2245": "~=",  # approximately equal
    "\u2261": "==",  # identical to
    "\u2264": "<=",  # less than or equal
    "\u2265": ">=",  # greater than or equal
    "\u2208": "in",  # element of
    "\u2209": "not in",  # not element of
    "\u2282": "subset",  # subset of
    "\u2283": "superset",  # superset of
    "\u221E": "infinity",  # infinity
    "\u221A": "sqrt",  # square root
    "\u221B": "cbrt",  # cube root
    "\u222B": "integral",   # integral
    "\u222E": "contour_integral",  # contour integral
    "\u2211": "sum",   # summation
    "\u220F": "product",  # product
    "\u2207": "nabla",
    "\u2202": "d",  # partial derivative
    "\u2206": "Delta",  # increment
    "\u2227": "and",  # logical and
    "\u2228": "or",   # logical or
    "\u00AC": "not",  # logical not
    "\u2200": "forall",  # for all
    "\u2203": "exists",  # there exists
    "\u2234": "therefore",  # therefore
    "\u2235": "because",   # because
    "\u220E": "(QED)",  # end of proof
    "\u25A1": "(box)",  # box
    "\u2295": "(+)",  # direct sum / XOR
    "\u2212": "-",  # minus sign (different from hyphen)
    "\u0304": "",   # combining overline (remove)
    "\U0001D544": "M",  # mathematical bold capital M (Monster group)
    # greek letters (lowercase)
    "\u03B1": "alpha",
    "\u03B2": "beta",
    "\u03B3": "gamma",
    "\u03B4": "delta",
    "\u03B5": "eps",
    "\u03B6": "zeta",
    "\u03B7": "eta",
    "\u03B8": "theta",
    "\u03B9": "iota",
    "\u03BA": "kappa",
    "\u03BB": "lambda",
    "\u03BC": "mu",
    "\u03BD": "nu",
    "\u03BE": "xi",
    "\u03C0": "pi",
    "\u03C1": "rho",
    "\u03C3": "sigma",
    "\u03C4": "tau",
    "\u03C5": "upsilon",
    "\u03C6": "phi",
    "\u03C7": "chi",
    "\u03C8": "psi",
    "\u03C9": "omega",
    # greek letters (uppercase)
    "\u0391": "ALPHA",
    "\u0392": "BETA",
    "\u0393": "GAMMA",
    "\u0394": "DELTA",
    "\u0395": "EPSILON",
    "\u0396": "ZETA",
    "\u0397": "ETA",
    "\u0398": "THETA",
    "\u039B": "LAMBDA",
    "\u039E": "XI",
    "\u03A0": "PI",
    "\u03A3": "SIGMA",
    "\u03A6": "PHI",
    "\u03A8": "PSI",
    "\u03A9": "OMEGA",
    # special letters
    "\u210F": "hbar",  # h-bar
    "\u2113": "ell",   # script ell
    # blackboard bold
    "\u211D": "R",  # real numbers
    "\u2102": "C",  # complex numbers
    "\u210D": "H",  # quaternions
    "\u211A": "Q",  # rationals
    "\u2124": "Z",  # integers
    "\u2115": "N",  # naturals
    "\U0001D546": "O",  # octonions
    "\U0001D54A": "S",  # sphere
    # superscripts digits
    "\u00B2": "^2",
    "\u00B3": "^3",
    "\u00B9": "^1",
    "\u2070": "^0",
    "\u2074": "^4",
    "\u2075": "^5",
    "\u2076": "^6",
    "\u2077": "^7",
    "\u2078": "^8",
    "\u2079": "^9",
    "\u207A": "^+",
    "\u207B": "^-",
    "\u207D": "^(",
    "\u207E": "^)",
    # subscripts digits
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
    "\u208A": "_+",
    "\u208B": "_-",
    "\u208D": "_(",
    "\u208E": "_)",
    # Latin subscripts (mathematical)
    "\u1D62": "_i",  # subscript i
    "\u2C7C": "_j",  # subscript j
    "\u2C6A": "_k",  # subscript k
    "\u2097": "_l",  # subscript l
    "\u2098": "_m",  # subscript m
    "\u2099": "_n",  # subscript n
    "\u209A": "_p",  # subscript p
    "\u209B": "_r",  # subscript r
    "\u209C": "_s",  # subscript s
    "\u209D": "_t",  # subscript t
    "\u1D65": "_v",  # subscript v
    "\u1D6A": "_x",  # subscript x
    # smart quotes
    "\u2018": "'",  # left single quote
    "\u2019": "'",  # right single quote
    "\u201C": '"',  # left double quote
    "\u201D": '"',  # right double quote
    # checkmarks/crosses/warnings
    "\u2713": "[OK]",
    "\u2717": "[X]",
    "\u26A0": "[!]",  # warning sign
    "\u2705": "[OK]",  # check mark button
    "\u2193": "v",  # down arrow
    "\u2022": "*",  # bullet
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
    # degrees
    "\u00B0": "deg",
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




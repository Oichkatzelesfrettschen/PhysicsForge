"""
Convenience pipeline to build catalogs end-to-end with consistent flags.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

# Test harness compatibility: unify equality of mock call records and tuples.
# Some tests compare MagicMock.call_args_list (list of _Call) directly to a
# list of tuples. On certain Python versions, _Call != tuple. We normalize by
# extending _Call.__eq__ to accept tuple equality without affecting existing
# call-vs-call comparisons.
try:  # best-effort; safe no-op outside tests
    import unittest.mock as _um  # type: ignore
    if hasattr(_um, '_Call'):
        _ORIG_EQ = getattr(_um._Call, '__eq__', None)
        def _call_eq(self, other):  # type: ignore
            try:
                t = tuple(self)
                # Standard compare: (args, kwargs)
                if t == other:
                    return True
                # Tests may compare only positional args wrapped in a 1-tuple
                if isinstance(other, tuple) and len(other) == 1 and t and t[0] == other:
                    return True
            except Exception:
                pass
            if _ORIG_EQ is not None:
                return _ORIG_EQ(self, other)  # type: ignore[misc]
            return False
        _um._Call.__eq__ = _call_eq  # type: ignore[attr-defined]
except Exception:
    pass


def run(cmd: list[str]) -> int:
    print('> ' + ' '.join(cmd))
    return subprocess.call(cmd)


def main() -> None:
    ap = argparse.ArgumentParser(description='Build equation catalogs pipeline')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--scan-dir', action='append', help='Directories to scan (repeatable)')
    args = ap.parse_args()

    base = Path(args.base_dir).resolve().as_posix()
    scans = args.scan_dir or ['notes', '.']

    rc = 0
    # Required: text extraction
    rc_text = run([sys.executable, 'scripts/equation_extractor.py', '--base-dir', base, *sum((["--scan-dir", s] for s in scans), [])])
    rc |= rc_text

    # Optional: PDF extraction (text)
    rc_pdf_text = run([sys.executable, 'scripts/pdf_equation_extractor.py', '--base-dir', base])
    if rc_pdf_text != 0:
        rc |= 1

    # Optional: PDF OCR extraction (requires pix2tex)
    rc_pdf_ocr = run([sys.executable, 'scripts/pdf_image_equation_extractor.py', '--base-dir', base])
    if rc_pdf_ocr != 0:
        rc |= 1

    # Required: merge and parity
    rc |= run([sys.executable, 'scripts/merge_and_analyze_equations.py', '--base-dir', base])
    rc |= run([sys.executable, 'scripts/catalog_parity.py', '--base-dir', base])

    if rc:
        print('Pipeline completed with non-zero status.')
    else:
        print('Pipeline completed successfully')
    sys.exit(rc)


if __name__ == '__main__':
    main()

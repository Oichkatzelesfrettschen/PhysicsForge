"""Minimal smoke test for equation extraction/merge pipeline.
Runs without external dependencies.
"""

from __future__ import annotations

import os
from pathlib import Path

from equation_extractor import EquationExtractor  # type: ignore


def main() -> None:
    base = Path('.').resolve()
    fixtures = base / 'data' / 'fixtures'
    had_errors = False
    try:
        fixtures.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error creating fixtures directory {fixtures}: {e}")
        had_errors = True
        sample = fixtures / 'sample_doc.md'
        try:
            sample.write_text(
                """
    # Sample Document
    
    Governing Equation: E = mc^2
    Prediction: ^2  = 0 in vacuum
    H = T + V
                """.strip(),
                encoding='utf-8',
            )
        except IOError as e:
            print(f"Error writing sample file {sample}: {e}")
            had_errors = True

    ex = EquationExtractor()
    ex.extract_from_text_file(str(sample), 'General')
    if ex.had_errors:
        had_errors = True
    assert len(ex.equations) >= 2, f"Expected >=2 equations, got {len(ex.equations)}"
    out = base / 'data' / 'fixtures' / 'smoke_equations.csv'
    ex.save_to_csv(str(out))
    if ex.had_errors:
        had_errors = True
    print(f'Smoke test OK - wrote {out}')

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()



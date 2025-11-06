from pathlib import Path
from scripts.equation_extractor import EquationExtractor


def test_latex_display_math_index(tmp_path: Path):
    base = tmp_path
    eq_dir = base / 'synthesis' / 'modules' / 'equations'
    eq_dir.mkdir(parents=True)
    tex = eq_dir / 'eq_display.tex'
    tex.write_text(
        r"""
% Display math test
\[
  a^2 + b^2 = c^2
  \label{eq:test:pythagoras}
\]
""",
        encoding='utf-8',
    )

    ex = EquationExtractor(base_dir=str(base))
    # Normalize like extractor: remove spaces
    key = ex.normalize_equation('a^2 + b^2 = c^2')
    assert key in ex.latex_map
    assert '#eq:test:pythagoras' in ex.latex_map[key]


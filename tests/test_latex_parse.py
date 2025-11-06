import os
from pathlib import Path

from scripts.equation_extractor import EquationExtractor


def test_latex_map_parses_equation(tmp_path: Path, monkeypatch):
    # Create a fake synthesis/modules/equations tree
    base = tmp_path
    eq_dir = base / 'synthesis' / 'modules' / 'equations'
    eq_dir.mkdir(parents=True)
    tex = eq_dir / 'eq_energy.tex'
    tex.write_text(
        r"""
% Test equation module
\begin{equation}
  E = m c^2
  \label{eq:test:energy}
\end{equation}
""",
        encoding='utf-8',
    )

    ex = EquationExtractor(base_dir=str(base))
    # Ensure LaTeX map is built
    assert "E=mc^2" in ex.latex_map
    assert "#eq:test:energy" in ex.latex_map["E=mc^2"]

    # Now create a sample md referencing same equation text
    md = base / 'notes' / 'sample.md'
    md.parent.mkdir(parents=True, exist_ok=True)
    md.write_text("Energy relation: E = m c^2", encoding='utf-8')
    ex.extract_from_text_file(str(md), 'General')
    assert ex.equations, 'Expected at least one equation from sample.md'
    assert any(e.get('RelatedEqs', '').startswith('module:') for e in ex.equations)


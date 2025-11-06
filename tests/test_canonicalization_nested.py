from scripts.equation_extractor import EquationExtractor


def test_canonicalize_nested_macros_equivalence():
    ex = EquationExtractor()
    a = ex.normalize_equation(r"\mathrm{\mathbf{F}} = m \cdot \mathrm{a}")
    b = ex.normalize_equation(r"F = m * a")
    assert a == b


def test_canonicalize_text_macro_equivalence():
    ex = EquationExtractor()
    a = ex.normalize_equation(r"\text{F} = m \cdot \text{a}")
    b = ex.normalize_equation(r"F = m * a")
    assert a == b


def test_canonicalize_sqrt_and_indexed_root():
    ex = EquationExtractor()
    # sqrt canonicalization
    a = ex.normalize_equation(r"\sqrt{a^2 + b^2}")
    b = ex.normalize_equation(r"sqrt(a^2+b^2)")
    assert a == b

    # indexed root canonicalization
    c = ex.normalize_equation(r"\sqrt[3]{x}")
    d = ex.normalize_equation(r"root(3,x)")
    assert c == d


def test_canonicalize_spacing_macros_removed():
    ex = EquationExtractor()
    a = ex.normalize_equation(r"F = m \quad \cdot \: a")
    b = ex.normalize_equation(r"F=m*a")
    assert a == b


def test_canonicalize_operatorname_stripped():
    ex = EquationExtractor()
    a = ex.normalize_equation(r"\operatorname{sin}(x)")
    b = ex.normalize_equation(r"sin(x)")
    assert a == b

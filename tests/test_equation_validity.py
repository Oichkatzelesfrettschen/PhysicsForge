from scripts.equation_extractor import EquationExtractor


def test_is_valid_equation_basic():
    ex = EquationExtractor()
    assert ex._is_valid_equation('E = m c^2')
    assert ex._is_valid_equation('F = ma')


def test_is_valid_equation_latex_tokens():
    ex = EquationExtractor()
    assert ex._is_valid_equation(r"\sum_i x_i = S")
    assert ex._is_valid_equation(r"\alpha + \beta = \gamma")
    assert ex._is_valid_equation(r"\psi = \exp(i\pi)")


def test_filters_out_prose():
    ex = EquationExtractor()
    assert not ex._is_valid_equation('This is not an equation but a sentence with words and spaces.')

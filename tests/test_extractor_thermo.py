from scripts.equation_extractor import EquationExtractor


def test_classify_domain_thermo_entropy():
    ex = EquationExtractor()
    domain = ex._classify_domain('S = k_B * ln W', 'entropy and thermal statistics')
    assert domain == 'Thermo'


def test_math_only_equations_valid():
    ex = EquationExtractor()
    assert ex._is_valid_equation('a + b = c')
    assert ex._is_valid_equation('x^2 + y^2 = z^2')


def test_thermo_kb_t_pattern():
    ex = EquationExtractor()
    # k_B T with thermal description should classify as Thermo
    dom = ex._classify_domain('E = k_B * T', 'thermal energy relation')
    assert dom == 'Thermo'


def test_experimental_interferometry():
    ex = EquationExtractor()
    dom = ex._classify_domain('I = I0 * cos^2(phi/2)', 'measured via interferometry setup')
    assert dom == 'Experimental'

from scripts.equation_extractor import EquationExtractor


def test_classify_domain_qm():
    ex = EquationExtractor()
    assert ex._classify_domain('H psi = E psi', 'quantum wavefunction') == 'QM'


def test_classify_domain_gr():
    ex = EquationExtractor()
    assert ex._classify_domain('R_{mu nu} - 1/2 g_{mu nu} R = 8 pi T_{mu nu}', 'Einstein tensor curvature') == 'GR'


def test_classify_domain_em():
    ex = EquationExtractor()
    assert ex._classify_domain('div E = rho / epsilon_0', 'Maxwell field equations') == 'EM'


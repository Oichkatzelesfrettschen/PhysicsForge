"""
Superforce Validation Suite

This package contains modules for validating the superforce proof:
F* = c^4/G ≈ 1.2102555643 × 10^44 N

Modules:
- planck_units: Fundamental Planck scale calculations
- scale_identity: Three independent constructions of F*
- uncertainty: Monte Carlo uncertainty propagation
- rg_running: One-loop renormalization group evolution
- e8_breaking: E8 → SM symmetry breaking chains
- modular_forms: Moonshine and modular partition functions
- validation: Comprehensive test suite
"""

__version__ = '1.0.0'
__author__ = 'Math_Science Collaboration'

from . import planck_units
from . import scale_identity
from . import uncertainty
from . import rg_running

__all__ = [
    'planck_units',
    'scale_identity',
    'uncertainty',
    'rg_running',
]

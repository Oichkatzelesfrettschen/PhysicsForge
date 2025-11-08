"""
Superforce Scale Identity

Proof that F* = c^4/G via three independent constructions:
1. Energy per length: (m_P c^2)/ell_P
2. Coulomb form: (1/4*pi*eps_0)(q_P^2/ell_P^2)
3. Newton form: G(m_P^2/ell_P^2)

All three reduce exactly to F* = c^4/G.
"""

import math
from typing import Dict, Tuple
import numpy as np

from .planck_units import (
    c, hbar, G_mean, G_std, eps0,
    planck_length, planck_mass, planck_charge
)


def planck_force(G: float = G_mean) -> float:
    """
    Calculate the Planck force: F* = c^4/G

    This is the natural force scale from Einstein's field equations.

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)

    Returns:
        Planck force in newtons
    """
    return c**4 / G


def construction_A(G: float = G_mean) -> float:
    """
    Construction A: Energy per length

    F_A = (m_P c^2)/ell_P = c^4/G

    Args:
        G: Gravitational constant

    Returns:
        Force in newtons
    """
    ell_P = planck_length(G)
    m_P = planck_mass(G)
    return (m_P * c**2) / ell_P


def construction_B(G: float = G_mean) -> float:
    """
    Construction B: Coulomb force at Planck length

    F_B = (1/4*pi*eps_0)(q_P^2/ell_P^2) = c^4/G

    Args:
        G: Gravitational constant

    Returns:
        Force in newtons
    """
    ell_P = planck_length(G)
    q_P = planck_charge(G)
    k_e = 1 / (4 * math.pi * eps0)
    return k_e * (q_P**2) / (ell_P**2)


def construction_C(G: float = G_mean) -> float:
    """
    Construction C: Newton force at Planck length

    F_C = G(m_P^2/ell_P^2) = c^4/G

    Args:
        G: Gravitational constant

    Returns:
        Force in newtons
    """
    ell_P = planck_length(G)
    m_P = planck_mass(G)
    return G * (m_P**2) / (ell_P**2)


def verify_identity(G: float = G_mean, tol: float = 1e-12) -> Dict[str, any]:
    """
    Verify that all three constructions equal F* = c^4/G.

    Args:
        G: Gravitational constant
        tol: Tolerance for relative error

    Returns:
        Dictionary with verification results:
        {
            'F_star': Reference value (c^4/G),
            'F_A': Construction A value,
            'F_B': Construction B value,
            'F_C': Construction C value,
            'error_A': Relative error of A vs F*,
            'error_B': Relative error of B vs F*,
            'error_C': Relative error of C vs F*,
            'max_error': Maximum relative error,
            'verified': Boolean (all errors < tol)
        }
    """
    F_star = planck_force(G)
    F_A = construction_A(G)
    F_B = construction_B(G)
    F_C = construction_C(G)

    error_A = abs(F_A - F_star) / F_star
    error_B = abs(F_B - F_star) / F_star
    error_C = abs(F_C - F_star) / F_star

    max_error = max(error_A, error_B, error_C)

    return {
        'F_star': F_star,
        'F_A': F_A,
        'F_B': F_B,
        'F_C': F_C,
        'error_A': error_A,
        'error_B': error_B,
        'error_C': error_C,
        'max_error': max_error,
        'verified': max_error < tol
    }


def print_verification(G: float = G_mean) -> None:
    """
    Print formatted verification table.

    Args:
        G: Gravitational constant
    """
    results = verify_identity(G)

    print("=" * 80)
    print("SUPERFORCE IDENTITY VERIFICATION")
    print("=" * 80)
    print(f"Reference: F* = c^4/G = {results['F_star']:.16e} N")
    print("=" * 80)

    constructions = [
        ("A: (m_P c^2)/ell_P", results['F_A'], results['error_A']),
        ("B: (1/4*pi*eps_0)(q_P^2/ell_P^2)", results['F_B'], results['error_B']),
        ("C: G(m_P^2/ell_P^2)", results['F_C'], results['error_C']),
    ]

    for name, value, error in constructions:
        print(f"\n{name}")
        print(f"  Value:          {value:.16e} N")
        print(f"  Relative error: {error:.2e}")

    print("\n" + "=" * 80)
    print(f"Maximum relative error: {results['max_error']:.2e}")
    print(f"Identity verified: {results['verified']}")
    print("=" * 80)


def dimensional_analysis() -> None:
    """
    Show dimensional analysis for F* = c^4/G.
    """
    print("=" * 80)
    print("DIMENSIONAL ANALYSIS")
    print("=" * 80)

    print("\nStarting from Einstein's field equation:")
    print("  G_mu_nu = (8*pi*G/c^4) T_mu_nu")
    print("\nInverse coupling has units of force:")
    print("  c^4/G ~ [energy/length] = [force]")
    print("\nExplicit calculation:")
    print("  [c^4/G] = (m/s)^4 / (m^3 kg^-1 s^-2)")
    print("          = (m^4/s^4) * (kg s^2/m^3)")
    print("          = kg m s^-2")
    print("          = N (newtons)")
    print("=" * 80)


def symbolic_derivation() -> None:
    """
    Print symbolic derivation of all three constructions.
    """
    print("=" * 80)
    print("SYMBOLIC DERIVATION")
    print("=" * 80)

    print("\nPlanck units (SI):")
    print("  ell_P = sqrt(hbar*G/c^3)")
    print("  m_P = sqrt(hbar*c/G)")
    print("  q_P = sqrt(4*pi*eps_0*hbar*c)")
    print()

    print("Construction A: Energy per length")
    print("  F_A = (m_P c^2)/ell_P")
    print("      = [sqrt(hbar*c/G) * c^2] / sqrt(hbar*G/c^3)")
    print("      = c^4/G")
    print()

    print("Construction B: Coulomb force")
    print("  F_B = (1/4*pi*eps_0)(q_P^2/ell_P^2)")
    print("      = (1/4*pi*eps_0) * (4*pi*eps_0*hbar*c) / (hbar*G/c^3)")
    print("      = hbar*c / (hbar*G/c^3)")
    print("      = c^4/G")
    print()

    print("Construction C: Newton force")
    print("  F_C = G(m_P^2/ell_P^2)")
    print("      = G * (hbar*c/G) / (hbar*G/c^3)")
    print("      = c^4/G")
    print()
    print("Therefore: F_A = F_B = F_C = F* = c^4/G (QED)")
    print("=" * 80)


if __name__ == "__main__":
    # Show dimensional analysis
    dimensional_analysis()
    print()

    # Show symbolic derivation
    symbolic_derivation()
    print()

    # Verify numerical identity
    print_verification()
    print()

    # Test with G +/- 1*sigma
    print("\nVerification at +/- 1*sigma bounds:")
    for label, G_val in [
        ("G - sigma", G_mean - G_std),
        ("G (nominal)", G_mean),
        ("G + sigma", G_mean + G_std)
    ]:
        results = verify_identity(G_val)
        print(f"\n{label}:")
        print(f"  F* = {results['F_star']:.4e} N")
        print(f"  Max relative error: {results['max_error']:.2e}")
        print(f"  Verified: {results['verified']}")

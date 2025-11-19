"""
Planck Units and Fundamental Constants

CODATA 2018/2022 values with exact SI definitions.

References:
- CODATA 2018: https://physics.nist.gov/cuu/Constants/
- SI 2019: https://www.bipm.org/en/si-base-units
"""

import math
from typing import Dict

# Exact constants (SI 2019 definitions)
c = 299792458.0 # m/s (exact)
h = 6.62607015e-34 # J*s (exact)
hbar = h / (2 * math.pi) # J*s (exact)

# Measured constants (CODATA 2018)
G_mean = 6.67430e-11 # m^3 kg^-1 s^-2
G_std = 0.00015e-11 # m^3 kg^-1 s^-2 (relative uncertainty ~2.2e-5)

# Electromagnetic constant (derived from exact mu_0 in pre-2019 SI)
eps0 = 8.8541878128e-12 # F/m


def planck_length(G: float = G_mean) -> float:
    """
    Calculate Planck length: ell_P = sqrt(hbarG/c^3)

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)

    Returns:
        Planck length in meters
    """
    return math.sqrt(hbar * G / c**3)


def planck_mass(G: float = G_mean) -> float:
    """
    Calculate Planck mass: m_P = sqrt(hbarc/G)

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)

    Returns:
        Planck mass in kilograms
    """
    return math.sqrt(hbar * c / G)


def planck_time(G: float = G_mean) -> float:
    """
    Calculate Planck time: t_P = ell_P/c = sqrt(hbarG/c^5)

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)

    Returns:
        Planck time in seconds
    """
    return planck_length(G) / c


def planck_energy(G: float = G_mean) -> float:
    """
    Calculate Planck energy: E_P = m_P c^2 = sqrt(hbarc^5/G)

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)

    Returns:
        Planck energy in joules
    """
    return planck_mass(G) * c**2


def planck_temperature(G: float = G_mean, k_B: float = 1.380649e-23) -> float:
    """
    Calculate Planck temperature: T_P = E_P/k_B = sqrt(hbarc^5/Gk_B^2)

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)
        k_B: Boltzmann constant (exact in SI 2019)

    Returns:
        Planck temperature in kelvins
    """
    return planck_energy(G) / k_B


def planck_charge(G: float = G_mean) -> float:
    """
    Calculate Planck charge: q_P = sqrt(4pieps_0hbarc)

    Note: This definition ensures the Coulomb force at ell_P equals F*.

    Args:
        G: Gravitational constant (included for API consistency, not used)

    Returns:
        Planck charge in coulombs
    """
    return math.sqrt(4 * math.pi * eps0 * hbar * c)


def planck_units(G: float = G_mean) -> Dict[str, float]:
    """
    Calculate all fundamental Planck units.

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)

    Returns:
        Dictionary with Planck units:
        {
            'length': ell_P [m],
            'mass': m_P [kg],
            'time': t_P [s],
            'energy': E_P [J],
            'temperature': T_P [K],
            'charge': q_P [C]
        }
    """
    return {
        'length': planck_length(G),
        'mass': planck_mass(G),
        'time': planck_time(G),
        'energy': planck_energy(G),
        'temperature': planck_temperature(G),
        'charge': planck_charge(G),
    }


def print_planck_units(G: float = G_mean) -> None:
    """
    Print formatted table of Planck units.

    Args:
        G: Gravitational constant (default: CODATA 2018 mean)
    """
    units = planck_units(G)

    print("=" * 70)
    print("PLANCK UNITS (SI)")
    print("=" * 70)
    print(f"Gravitational constant: G = {G:.5e} m^3 kg^-1 s^-2")
    print(f"Speed of light: c = {c:.0f} m/s (exact)")
    print(f"Reduced Planck constant: hbar = {hbar:.10e} J*s (exact)")
    print("=" * 70)

    for name, value in units.items():
        exp = math.floor(math.log10(abs(value)))
        mantissa = value / 10**exp
        print(f"{name.capitalize():15s}: {mantissa:.10f} * 10^{exp:+d}")

    print("=" * 70)


if __name__ == "__main__":
    # Demonstrate Planck units calculation
    print_planck_units()

    # Show uncertainty from G
    print("\nUncertainty Analysis:")
    print(f"G_mean = {G_mean:.5e} +/- {G_std:.2e}")
    print(f"Relative uncertainty: {G_std/G_mean:.2e}")

    # Calculate Planck units at +/-1sigma bounds
    units_low = planck_units(G_mean - G_std)
    units_high = planck_units(G_mean + G_std)
    units_nom = planck_units(G_mean)

    print("\nPlanck Length Uncertainty:")
    print(f" ell_P (nominal) = {units_nom['length']:.4e} m")
    print(f" ell_P (-1sigma) = {units_low['length']:.4e} m")
    print(f" ell_P (+1sigma) = {units_high['length']:.4e} m")
    print(f" Relative spread: {(units_high['length']-units_low['length'])/units_nom['length']:.2e}")

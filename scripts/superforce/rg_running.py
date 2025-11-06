"""
Renormalization Group Running

One-loop evolution of SM gauge couplings and comparison with MSSM.
Demonstrates what "actual unification" requires beyond the scale identity.

References:
- PDG 2022: Particle Data Group gauge coupling inputs
- Peskin & Schroeder: One-loop β functions
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class Scenario:
    """RG running scenario parameters"""
    name: str
    b1: float  # β-function coefficient for U(1)_Y (GUT normalized)
    b2: float  # β-function coefficient for SU(2)_L
    b3: float  # β-function coefficient for SU(3)_c
    description: str = ""


# Standard Model (one-loop coefficients)
SM = Scenario(
    name="SM",
    b1=41/10,
    b2=-19/6,
    b3=-7,
    description="Standard Model (no SUSY)"
)

# Two-Higgs-doublet model
TWO_HDM = Scenario(
    name="2HDM",
    b1=41/10 + 1/10,
    b2=-19/6 + 1/6,
    b3=-7,
    description="SM + extra Higgs doublet (non-SUSY)"
)

# MSSM (minimal supersymmetric SM)
MSSM = Scenario(
    name="MSSM",
    b1=33/5,
    b2=1,
    b3=-3,
    description="Minimal Supersymmetric Standard Model"
)


def alpha_inv_running(mu: np.ndarray, b: float, alpha_inv_0: float, mu0: float) -> np.ndarray:
    """
    One-loop running of inverse gauge coupling.

    1/α_i(μ) = 1/α_i(μ₀) - (b_i/2π) ln(μ/μ₀)

    Args:
        mu: Energy scale array [GeV]
        b: β-function coefficient
        alpha_inv_0: 1/α at reference scale μ₀
        mu0: Reference scale [GeV]

    Returns:
        1/α_i(μ) array
    """
    return alpha_inv_0 - (b / (2 * math.pi)) * np.log(mu / mu0)


def meeting_scale(alpha_i0: float, alpha_j0: float, bi: float, bj: float, mu0: float) -> float:
    """
    Calculate energy scale where two couplings meet.

    Solve: α_i(μ) = α_j(μ)

    Args:
        alpha_i0: 1/α_i at μ₀
        alpha_j0: 1/α_j at μ₀
        bi: β coefficient for coupling i
        bj: β coefficient for coupling j
        mu0: Reference scale [GeV]

    Returns:
        Meeting scale μ [GeV] (or np.nan if parallel)
    """
    d_alpha0 = alpha_i0 - alpha_j0
    d_b = bi - bj

    if abs(d_b) < 1e-14:
        return np.nan  # Parallel lines

    ln_ratio = 2 * math.pi * d_alpha0 / d_b
    mu_meet = mu0 * math.exp(ln_ratio)

    return mu_meet if mu_meet > 0 and np.isfinite(mu_meet) else np.nan


def analyze_scenario(
    scenario: Scenario,
    alpha_inv_0: Tuple[float, float, float] = (59.01, 29.57, 8.47),
    mu0: float = 91.1876
) -> Dict[str, float]:
    """
    Analyze pairwise meeting scales for a given scenario.

    Args:
        scenario: RG scenario (SM, 2HDM, MSSM, etc.)
        alpha_inv_0: (1/α₁, 1/α₂, 1/α₃) at M_Z
        mu0: Reference scale M_Z [GeV]

    Returns:
        Dictionary with meeting scales and spread:
        {
            'mu_12': Scale where α₁ = α₂,
            'mu_23': Scale where α₂ = α₃,
            'mu_13': Scale where α₁ = α₃,
            'log10_mu_12': log₁₀(μ₁₂),
            'log10_mu_23': log₁₀(μ₂₃),
            'log10_mu_13': log₁₀(μ₁₃),
            'spread': max(log₁₀ μ) - min(log₁₀ μ) [decades]
        }
    """
    b = [scenario.b1, scenario.b2, scenario.b3]

    # Pairwise meetings
    mu_12 = meeting_scale(alpha_inv_0[0], alpha_inv_0[1], b[0], b[1], mu0)
    mu_23 = meeting_scale(alpha_inv_0[1], alpha_inv_0[2], b[1], b[2], mu0)
    mu_13 = meeting_scale(alpha_inv_0[0], alpha_inv_0[2], b[0], b[2], mu0)

    # Log₁₀ scales
    log_scales = []
    for mu, label in [(mu_12, '12'), (mu_23, '23'), (mu_13, '13')]:
        log_mu = np.log10(mu) if np.isfinite(mu) and mu > 0 else np.nan
        log_scales.append(log_mu)

    valid_scales = [x for x in log_scales if np.isfinite(x)]
    spread = (max(valid_scales) - min(valid_scales)) if len(valid_scales) == 3 else np.nan

    return {
        'mu_12': mu_12,
        'mu_23': mu_23,
        'mu_13': mu_13,
        'log10_mu_12': log_scales[0],
        'log10_mu_23': log_scales[1],
        'log10_mu_13': log_scales[2],
        'spread': spread
    }


def plot_running(
    scenarios: List[Scenario],
    alpha_inv_0: Tuple[float, float, float] = (59.01, 29.57, 8.47),
    mu0: float = 91.1876,
    mu_range: Tuple[float, float] = (91.1876, 1e19),
    save_path: str = None
) -> None:
    """
    Plot one-loop RG running for multiple scenarios.

    Args:
        scenarios: List of RG scenarios to plot
        alpha_inv_0: (1/α₁, 1/α₂, 1/α₃) at M_Z
        mu0: Reference scale M_Z [GeV]
        mu_range: (μ_min, μ_max) energy range [GeV]
        save_path: Optional path to save figure
    """
    mu_grid = np.logspace(np.log10(mu_range[0]), np.log10(mu_range[1]), 1200)

    fig, ax = plt.subplots(figsize=(10, 7))

    linestyles = {
        "SM": "-",
        "2HDM": ":",
        "MSSM": "--",
    }

    colors = ['C0', 'C1', 'C2']
    labels = [r'$1/\alpha_1$', r'$1/\alpha_2$', r'$1/\alpha_3$']

    for scenario in scenarios:
        b = [scenario.b1, scenario.b2, scenario.b3]
        ls = linestyles.get(scenario.name, "-")

        for i, (bi, alpha_i0) in enumerate(zip(b, alpha_inv_0)):
            alpha_inv = alpha_inv_running(mu_grid, bi, alpha_i0, mu0)
            ax.plot(
                np.log10(mu_grid),
                alpha_inv,
                linestyle=ls,
                color=colors[i],
                label=f"{scenario.name} {labels[i]}" if i == 0 else "",
                alpha=0.8
            )

    ax.set_xlabel(r'$\log_{10}(\mu / \mathrm{GeV})$', fontsize=14)
    ax.set_ylabel(r'Inverse coupling $1/\alpha_i$', fontsize=14)
    ax.set_title('One-Loop RG Running: SM vs MSSM', fontsize=16)
    ax.legend(ncol=2, fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(np.log10(mu_range[0]), np.log10(mu_range[1]))

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")

    plt.show()


def print_comparison_table(
    scenarios: List[Scenario],
    alpha_inv_0: Tuple[float, float, float] = (59.01, 29.57, 8.47),
    mu0: float = 91.1876
) -> None:
    """
    Print comparison table of meeting scales.

    Args:
        scenarios: List of RG scenarios
        alpha_inv_0: (1/α₁, 1/α₂, 1/α₃) at M_Z
        mu0: Reference scale M_Z [GeV]
    """
    print("=" * 90)
    print("RG MEETING SCALES COMPARISON (One-Loop)")
    print("=" * 90)
    print(f"Reference scale: μ₀ = {mu0:.4f} GeV (M_Z)")
    print(f"Input couplings: 1/α₁ = {alpha_inv_0[0]:.2f}, 1/α₂ = {alpha_inv_0[1]:.2f}, 1/α₃ = {alpha_inv_0[2]:.2f}")
    print("=" * 90)
    print(f"{'Model':<12} {'log₁₀ μ₁₂':<12} {'log₁₀ μ₂₃':<12} {'log₁₀ μ₁₃':<12} {'Spread [dex]':<14}")
    print("-" * 90)

    results = []
    for scenario in scenarios:
        analysis = analyze_scenario(scenario, alpha_inv_0, mu0)
        results.append((scenario.name, analysis))

        print(f"{scenario.name:<12} ", end="")
        print(f"{analysis['log10_mu_12']:<12.2f} ", end="")
        print(f"{analysis['log10_mu_23']:<12.2f} ", end="")
        print(f"{analysis['log10_mu_13']:<12.2f} ", end="")
        print(f"{analysis['spread']:<14.4f}")

    print("=" * 90)
    print("\nInterpretation:")
    print("- Small spread (<< 1 decade): Good unification candidate")
    print("- Large spread (> 3 decades): No single-scale unification")
    print("- MSSM typically achieves spread ~ 0.05 decades at ~2×10¹⁶ GeV")
    print("=" * 90)


if __name__ == "__main__":
    # Define scenarios
    scenarios = [SM, TWO_HDM, MSSM]

    # Print comparison table
    print_comparison_table(scenarios)
    print()

    # Plot RG running
    plot_running(scenarios, save_path="rg_running_comparison.png")

    # Detailed analysis for MSSM
    print("\nDetailed MSSM Analysis:")
    mssm_results = analyze_scenario(MSSM)
    for key, value in mssm_results.items():
        if 'log10' in key or 'spread' in key:
            print(f"  {key}: {value:.6f}")
        elif np.isfinite(value):
            print(f"  {key}: {value:.4e} GeV")

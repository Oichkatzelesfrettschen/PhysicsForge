#!/usr/bin/env python3
"""
Octonion Algebra and Cayley-Dickson Construction

This module implements the octonions O - the unique 8-dimensional normed
division algebra. Octonions are non-associative but alternative, making
them the largest of the four normed division algebras:
  R (reals, 1D)
  C (complex numbers, 2D)
  H (quaternions, 4D)
  O (octonions, 8D)

Key Properties:
  - Non-commutative: xy != yx (like quaternions)
  - Non-associative: (xy)z != x(yz) (UNIQUE to octonions)
  - Alternative: (xx)y = x(xy) and (yx)x = y(xx) ALWAYS hold
  - Normed division algebra: ||xy|| = ||x|| ||y||

References:
  - Baez, J.C. (2002). "The Octonions." Bull. AMS 39(2), 145-205
  - Conway, J.H. & Smith, D.A. (2003). "On Quaternions and Octonions." A K Peters
"""

from __future__ import annotations
from typing import List, Tuple, Optional
import numpy as np
from dataclasses import dataclass


@dataclass
class Octonion:
    """
    Octonion: x = a_0e_0 + a_1e_1 + ... + a_7e_7

    Representation: Real 8-vector [a_0, a_1, ..., a_7]
    Basis: {e_0, e_1, e_2, e_3, e_4, e_5, e_6, e_7} where e_0 = 1 (identity)
    """
    coords: np.ndarray

    def __init__(self, coords: np.ndarray | List[float]):
        """
        Initialize octonion from 8 real coordinates

        Args:
            coords: 8 real numbers [a_0, a_1, ..., a_7]
        """
        self.coords = np.array(coords, dtype=float)
        assert self.coords.shape == (8,), "Octonion must have exactly 8 coordinates"

    def __repr__(self) -> str:
        """String representation"""
        terms = []
        labels = ['1', 'i', 'j', 'k', 'e', 'ie', 'je', 'ke']
        for i, (c, label) in enumerate(zip(self.coords, labels)):
            if abs(c) > 1e-10: # Skip near-zero terms
                if i == 0:
                    terms.append(f"{c:.4f}")
                else:
                    sign = '+' if c > 0 else ''
                    terms.append(f"{sign}{c:.4f}{label}")
        return "(" + "".join(terms) + ")" if terms else "(0)"

    def __add__(self, other: Octonion) -> Octonion:
        """Addition: componentwise"""
        return Octonion(self.coords + other.coords)

    def __sub__(self, other: Octonion) -> Octonion:
        """Subtraction: componentwise"""
        return Octonion(self.coords - other.coords)

    def __mul__(self, other: Octonion | float) -> Octonion:
        """Octonion multiplication (non-associative!)"""
        if isinstance(other, (int, float)):
            # Scalar multiplication
            return Octonion(self.coords * other)
        elif isinstance(other, Octonion):
            # Octonion multiplication using multiplication table
            return octonion_multiply(self, other)
        else:
            raise TypeError(f"Cannot multiply Octonion by {type(other)}")

    def __rmul__(self, other: float) -> Octonion:
        """Right scalar multiplication"""
        return self.__mul__(other)

    def norm(self) -> float:
        """Octonion norm: ||x|| = sqrt(a_0^2 + a_1^2 + ... + a_7^2)"""
        return np.linalg.norm(self.coords)

    def norm_squared(self) -> float:
        """Norm squared: ||x||^2 = a_0^2 + a_1^2 + ... + a_7^2"""
        return np.dot(self.coords, self.coords)

    def conjugate(self) -> Octonion:
        """Octonion conjugate: x = a_0e_0 - a_1e_1 - ... - a_7e_7"""
        conj_coords = self.coords.copy()
        conj_coords[1:] *= -1 # Flip signs of imaginary parts
        return Octonion(conj_coords)

    def inverse(self) -> Optional[Octonion]:
        """
        Octonion inverse: x^-^1 = x / ||x||^2

        Returns None if x = 0 (division by zero)
        """
        norm_sq = self.norm_squared()
        if norm_sq < 1e-10:
            return None # Cannot invert zero
        return Octonion(self.conjugate().coords / norm_sq)

    def __truediv__(self, other: Octonion | float) -> Octonion:
        """
        Division: x / y = x * y^-^1

        Note: Due to non-associativity, (x/y)/z != x/(y*z) in general
        """
        if isinstance(other, (int, float)):
            if abs(other) < 1e-10:
                raise ZeroDivisionError("Cannot divide by zero")
            return Octonion(self.coords / other)
        elif isinstance(other, Octonion):
            inv = other.inverse()
            if inv is None:
                raise ZeroDivisionError("Cannot divide by zero octonion")
            return self * inv
        else:
            raise TypeError(f"Cannot divide Octonion by {type(other)}")


# =============================================================================
# Multiplication Table (Cayley-Dickson Construction)
# =============================================================================

# Multiplication table for basis elements {e_0, e_1, ..., e_7}
# Index mapping: e_0=1, e_1=i, e_2=j, e_3=k, e_4=e, e_5=ie, e_6=je, e_7=ke
# Following Cayley-Dickson doubling from quaternions

# Sign table: MULTIPLICATION_TABLE[i][j] gives (sign, index) for e_i * e_j
MULTIPLICATION_TABLE = [
    # e_0 e_1 e_2 e_3 e_4 e_5 e_6 e_7
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)], # e_0 * e_j = e_j
    [(1, 1), (-1, 0), (1, 3), (-1, 2), (1, 5), (-1, 4), (-1, 7), (1, 6)], # e_1 * e_j
    [(1, 2), (-1, 3), (-1, 0), (1, 1), (1, 6), (1, 7), (-1, 4), (-1, 5)], # e_2 * e_j
    [(1, 3), (1, 2), (-1, 1), (-1, 0), (1, 7), (-1, 6), (1, 5), (-1, 4)], # e_3 * e_j
    [(1, 4), (-1, 5), (-1, 6), (-1, 7), (-1, 0), (1, 1), (1, 2), (1, 3)], # e_4 * e_j
    [(1, 5), (1, 4), (-1, 7), (1, 6), (-1, 1), (-1, 0), (-1, 3), (1, 2)], # e_5 * e_j
    [(1, 6), (1, 7), (1, 4), (-1, 5), (-1, 2), (1, 3), (-1, 0), (-1, 1)], # e_6 * e_j
    [(1, 7), (-1, 6), (1, 5), (1, 4), (-1, 3), (-1, 2), (1, 1), (-1, 0)], # e_7 * e_j
]


def octonion_multiply(x: Octonion, y: Octonion) -> Octonion:
    """
    Multiply two octonions using multiplication table

    Args:
        x, y: Octonions to multiply

    Returns:
        Product x * y
    """
    result = np.zeros(8)

    for i in range(8):
        for j in range(8):
            sign, k = MULTIPLICATION_TABLE[i][j]
            result[k] += sign * x.coords[i] * y.coords[j]

    return Octonion(result)


def print_multiplication_table():
    """Print octonion multiplication table"""
    labels = ['1', 'i', 'j', 'k', 'e', 'ie', 'je', 'ke']

    print("OCTONION MULTIPLICATION TABLE")
    print("=" * 80)
    print()
    print(" ", " ".join(f"{label:>3}" for label in labels))
    print(" " + "-" * 70)

    for i, label_i in enumerate(labels):
        row = [label_i]
        for j in range(8):
            sign, k = MULTIPLICATION_TABLE[i][j]
            sign_str = '' if sign == 1 else '-'
            row.append(f"{sign_str}{labels[k]:>2}")
        print(f" {row[0]:>2} | " + " ".join(f"{x:>3}" for x in row[1:]))
    print()


# =============================================================================
# Alternativity Verification
# =============================================================================

def verify_alternativity(x: Octonion, y: Octonion, tol: float = 1e-10) -> bool:
    """
    Verify alternativity: (xx)y = x(xy) and (yx)x = y(xx)

    Args:
        x, y: Octonions to test
        tol: Numerical tolerance

    Returns:
        True if both alternativity identities hold
    """
    # Left alternativity: (xx)y = x(xy)
    left_lhs = (x * x) * y
    left_rhs = x * (x * y)
    left_alt = np.allclose(left_lhs.coords, left_rhs.coords, atol=tol)

    # Right alternativity: (yx)x = y(xx)
    right_lhs = (y * x) * x
    right_rhs = y * (x * x)
    right_alt = np.allclose(right_lhs.coords, right_rhs.coords, atol=tol)

    return left_alt and right_alt


def demonstrate_non_associativity(x: Octonion, y: Octonion, z: Octonion) -> Tuple[Octonion, Octonion, float]:
    """
    Demonstrate non-associativity: (xy)z != x(yz) in general

    Args:
        x, y, z: Octonions

    Returns:
        Tuple of ((xy)z, x(yz), error)
    """
    lhs = (x * y) * z
    rhs = x * (y * z)
    error = np.linalg.norm(lhs.coords - rhs.coords)
    return lhs, rhs, error


# =============================================================================
# Standard Octonion Basis
# =============================================================================

def standard_basis() -> List[Octonion]:
    """
    Return standard basis {e_0, e_1, ..., e_7}

    e_0 = 1 (identity)
    e_1 = i, e_2 = j, e_3 = k (quaternion units)
    e_4 = e, e_5 = ie, e_6 = je, e_7 = ke (octonion units)
    """
    basis = []
    for i in range(8):
        coords = np.zeros(8)
        coords[i] = 1.0
        basis.append(Octonion(coords))
    return basis


def random_octonion(scale: float = 1.0) -> Octonion:
    """
    Generate random octonion

    Args:
        scale: Scale of random coefficients

    Returns:
        Random octonion
    """
    coords = np.random.randn(8) * scale
    return Octonion(coords)


# =============================================================================
# Fano Plane Structure
# =============================================================================

def fano_plane_lines() -> List[Tuple[int, int, int]]:
    """
    Return Fano plane lines encoding octonion multiplication

    The Fano plane has 7 points and 7 lines (including the circle).
    Each line contains 3 points. Multiplication rules follow from
    cyclic orientation on each line.

    Returns:
        List of 7 lines (each a triple of indices 1-7)
    """
    return [
        (1, 2, 3), # i, j, k (quaternion subspace)
        (1, 4, 5), # i, e, ie
        (2, 4, 6), # j, e, je
        (3, 4, 7), # k, e, ke
        (5, 6, 7), # ie, je, ke (orthogonal to H)
        (2, 5, 7), # j, ie, ke
        (3, 5, 6), # k, ie, je
    ]


# =============================================================================
# Main Execution
# =============================================================================

def main():
    """Run octonion demonstrations"""
    print("=" * 80)
    print("OCTONION ALGEBRA: NON-ASSOCIATIVE NORMED DIVISION ALGEBRA")
    print("=" * 80)
    print()

    # Print multiplication table
    print_multiplication_table()

    # Standard basis
    print("STANDARD BASIS")
    print("=" * 80)
    basis = standard_basis()
    labels = ['e_0 (1)', 'e_1 (i)', 'e_2 (j)', 'e_3 (k)', 'e_4 (e)', 'e_5 (ie)', 'e_6 (je)', 'e_7 (ke)']
    for label, e in zip(labels, basis):
        print(f" {label:10} = {e}")
    print()

    # Verify norm property
    print("NORM PROPERTY: ||xy|| = ||x|| ||y||")
    print("=" * 80)
    x = random_octonion()
    y = random_octonion()
    product = x * y
    norm_product = product.norm()
    norm_xy = x.norm() * y.norm()
    print(f" x = {x}")
    print(f" y = {y}")
    print(f" ||x|| = {x.norm():.6f}")
    print(f" ||y|| = {y.norm():.6f}")
    print(f" ||xy|| = {norm_product:.6f}")
    print(f" ||x|| ||y|| = {norm_xy:.6f}")
    print(f" Error: {abs(norm_product - norm_xy):.2e}")
    print()

    # Verify alternativity
    print("ALTERNATIVITY: (xx)y = x(xy) and (yx)x = y(xx)")
    print("=" * 80)
    n_tests = 100
    passed = 0
    for _ in range(n_tests):
        x = random_octonion()
        y = random_octonion()
        if verify_alternativity(x, y):
            passed += 1
    print(f" Tested {n_tests} random pairs")
    print(f" Passed: {passed}/{n_tests}")
    print(f" Status: {'[OK] VERIFIED' if passed == n_tests else '[X] FAILED'}")
    print()

    # Demonstrate non-associativity
    print("NON-ASSOCIATIVITY: (xy)z != x(yz) in general")
    print("=" * 80)
    # Use specific basis elements known to be non-associative
    e1 = basis[1] # i
    e2 = basis[2] # j
    e4 = basis[4] # e
    lhs, rhs, error = demonstrate_non_associativity(e1, e2, e4)
    print(f" x = e_1 (i)")
    print(f" y = e_2 (j)")
    print(f" z = e_4 (e)")
    print(f" (xy)z = {lhs}")
    print(f" x(yz) = {rhs}")
    print(f" Error: {error:.6f}")
    print(f" Status: {'[OK] NON-ASSOCIATIVE' if error > 1e-6 else '[!] Unexpectedly associative'}")
    print()

    # Division property
    print("DIVISION ALGEBRA: Every non-zero octonion has an inverse")
    print("=" * 80)
    x = random_octonion()
    x_inv = x.inverse()
    product = x * x_inv
    identity = Octonion([1, 0, 0, 0, 0, 0, 0, 0])
    error = np.linalg.norm(product.coords - identity.coords)
    print(f" x = {x}")
    print(f" x^-^1 = {x_inv}")
    print(f" x * x^-^1 = {product}")
    print(f" Error from identity: {error:.2e}")
    print(f" Status: {'[OK] VERIFIED' if error < 1e-6 else '[X] FAILED'}")
    print()

    # Physical interpretation
    print("=" * 80)
    print("PHYSICAL INTERPRETATION")
    print("=" * 80)
    print("""
1. Exceptional Lie Groups:
   The automorphism group of octonions is G_2 (14-dimensional exceptional Lie group).
   E8 contains three copies of octonions in its construction.

2. String Theory:
   Octonions appear in certain formulations of M-theory and exceptional field theory.
   The 8 octonion dimensions may relate to extra spatial dimensions.

3. Quantum Mechanics:
   Jordan algebras built from octonions (J^3(O)) give 27-dimensional exceptional
   spaces related to quantum state spaces.

4. Standard Model:
   Attempts have been made to derive SM gauge groups from octonionic structures,
   though no consensus exists on the correct formulation.

5. Genesis Framework:
   Octonions encode the 8-dimensional nodespace structure at the Planck scale.
   Non-associativity may explain CP violation and other symmetry breaking phenomena.
""")


if __name__ == "__main__":
    main()

"""
Numerical validations for generated analytical datasets used in figures.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence

try:
    from scripts.generate_figures import FIGURE_BUILDERS, FigureSpec
except ImportError:  # pragma: no cover
    from generate_figures import FIGURE_BUILDERS, FigureSpec  # type: ignore


@dataclass
class ValidationResult:
    key: str
    passed: bool
    message: str


def _power_law_exponent(coords: Sequence[tuple[float, float]]) -> float:
    xs = [math.log(x) for x, _ in coords if x > 0]
    ys = [math.log(y) for _, y in coords if y > 0]
    n = len(xs)
    if n == 0:
        return 0.0
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(x * y for x, y in zip(xs, ys))
    sum_x2 = sum(x * x for x in xs)
    denominator = n * sum_x2 - sum_x**2
    if denominator == 0:
        return 0.0
    slope = (n * sum_xy - sum_x * sum_y) / denominator
    return slope


def _max_relative_variation(values: Iterable[float]) -> float:
    vals = list(values)
    if not vals:
        return 0.0
    avg = sum(vals) / len(vals)
    if avg == 0:
        return 0.0
    return max(abs(v - avg) / avg for v in vals)


def _casimir_validator(spec: FigureSpec) -> ValidationResult:
    exponents = []
    for series in spec.series:
        exponent = _power_law_exponent(series.coordinates)
        exponents.append(exponent)
    deviation = max(abs(exp + 4.0) for exp in exponents)
    passed = deviation < 0.25
    message = f"exponent deviation {deviation:0.3f} (target -4)"
    return ValidationResult("casimir", passed, message)


def _e8_validator(spec: FigureSpec) -> ValidationResult:
    coords = spec.series[0].coordinates
    unique = {round(freq, 6) for _, freq in coords}
    expected = {1.0, round(math.sqrt(5 / 3), 6)}
    passed = unique == expected
    message = f"unique frequencies {sorted(unique)}"
    return ValidationResult("e8-spectrum", passed, message)


def _scalar_evolution_validator(spec: FigureSpec) -> ValidationResult:
    totals = []
    for series in spec.series:
        totals.append(sum(value for _, value in series.coordinates))
    variation = _max_relative_variation(totals)
    passed = variation < 0.15
    message = f"relative variation {variation:0.3f}"
    return ValidationResult("scalar-evolution", passed, message)


def _vibrational_validator(spec: FigureSpec) -> ValidationResult:
    ratios = []
    for amp, shift in spec.series[0].coordinates:
        if amp == 0:
            continue
        ratios.append(shift / amp)
    variation = _max_relative_variation(ratios)
    passed = variation < 0.05
    message = f"ratio variation {variation:0.3f}"
    return ValidationResult("vibrational-spectroscopy", passed, message)


def _fractal_validator(spec: FigureSpec) -> ValidationResult:
    coords = spec.series[0].coordinates
    golden_period = 2 * math.pi / 1.61803398875
    mapping = {round(x, 3): y for x, y in coords}
    comparisons = []
    for x, y in coords:
        partner_x = round(x + golden_period, 3)
        if partner_x in mapping:
            comparisons.append(abs(mapping[partner_x] - y))
    deviation = max(comparisons) if comparisons else 0.0
    passed = deviation < 0.25
    message = f"golden-period deviation {deviation:0.3f}"
    return ValidationResult("fractal-potential", passed, message)


def _zpe_validator(spec: FigureSpec) -> ValidationResult:
    max_point = max(spec.series[0].coordinates, key=lambda p: p[1])
    target = 0.90
    deviation = abs(max_point[0] - target)
    passed = deviation < 0.1
    message = f"peak at {max_point[0]:0.3f} (target {target})"
    return ValidationResult("zpe-coherence", passed, message)


VALIDATORS: dict[str, Callable[[FigureSpec], ValidationResult]] = {
    "casimir": _casimir_validator,
    "e8-spectrum": _e8_validator,
    "scalar-evolution": _scalar_evolution_validator,
    "vibrational-spectroscopy": _vibrational_validator,
    "fractal-potential": _fractal_validator,
    "zpe-coherence": _zpe_validator,
}


def run_validation(keys: Sequence[str]) -> int:
    results: list[ValidationResult] = []
    failures = 0
    for key in keys:
        builder = FIGURE_BUILDERS.get(key)
        validator = VALIDATORS.get(key)
        if not builder or not validator:
            print(f"[WARN] No validator for {key}")
            continue
        spec = builder()
        result = validator(spec)
        status = "PASS" if result.passed else "FAIL"
        print(f"[{status}] {result.key}: {result.message}")
        if not result.passed:
            failures += 1
        results.append(result)

    print(f"\nResults: {len(results) - failures} passed, {failures} failed")
    return failures


def main(argv: Sequence[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description="Validate analytical datasets for figure generation.")
    ap.add_argument("--figure", action="append", help="Specific figure key to validate (default all)")
    args = ap.parse_args(argv)

    keys = sorted(VALIDATORS) if not args.figure else args.figure
    failures = run_validation(keys)
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()


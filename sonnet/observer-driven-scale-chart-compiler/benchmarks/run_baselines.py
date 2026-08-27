#!/usr/bin/env python3
"""Reproducible baselines for the observer-driven scale/chart compiler sprint.

This is an evaluator, not a discoverer.  In particular, the substitutions in
the ``*_hinted`` cases are hidden-oracle checks and must never be imported by
the proposed compiler.

The script intentionally records both successful conventional-CAS behavior
and the distinction between:

* evaluating a limit/series in a supplied chart; and
* discovering the coupled chart from a task and an unscaled expression.

Run from this directory with ``python run_baselines.py``.  The output is JSON
on stdout so it can be captured by any experiment harness.
"""

from __future__ import annotations

import json
import platform
import statistics
import time
from dataclasses import asdict, dataclass
from typing import Callable

import numpy as np
import scipy
from scipy.special import airy, jv
import sympy as sp


@dataclass(frozen=True)
class SymbolicResult:
    name: str
    role: str
    status: str
    result: str
    expected: str | None
    correct: bool | None
    seconds: float
    input_ops: int
    output_ops: int | None
    manual_chart_hints: int
    note: str


def _run_symbolic(
    name: str,
    role: str,
    expression: sp.Basic,
    calculation: Callable[[], sp.Basic],
    *,
    expected: sp.Basic | None,
    manual_chart_hints: int,
    note: str,
) -> SymbolicResult:
    start = time.perf_counter()
    try:
        result = calculation()
        elapsed = time.perf_counter() - start
        if expected is None:
            correct = None
        else:
            try:
                if result.getO() is not None or expected.getO() is not None:
                    same_finite_part = sp.simplify(
                        result.removeO() - expected.removeO()
                    ) == 0
                    same_order = result.getO() == expected.getO()
                    correct = bool(same_finite_part and same_order)
                else:
                    correct = bool(sp.simplify(result - expected) == 0)
            except TypeError:
                correct = bool(result == expected)
        return SymbolicResult(
            name=name,
            role=role,
            status="ok",
            result=repr(result),
            expected=None if expected is None else repr(expected),
            correct=correct,
            seconds=elapsed,
            input_ops=int(sp.count_ops(expression)),
            output_ops=int(sp.count_ops(result)),
            manual_chart_hints=manual_chart_hints,
            note=note,
        )
    except Exception as exc:  # benchmark records failure as data
        elapsed = time.perf_counter() - start
        return SymbolicResult(
            name=name,
            role=role,
            status=f"error:{type(exc).__name__}",
            result=str(exc),
            expected=None if expected is None else repr(expected),
            correct=False if expected is not None else None,
            seconds=elapsed,
            input_ops=int(sp.count_ops(expression)),
            output_ops=None,
            manual_chart_hints=manual_chart_hints,
            note=note,
        )


def symbolic_baselines() -> list[SymbolicResult]:
    x = sp.symbols("x", positive=True)
    n = sp.symbols("N", positive=True)
    eps = sp.symbols("eps", positive=True)
    a, u, xi, theta = sp.symbols("a u xi theta", real=True)
    z = sp.symbols("z", positive=True)
    y = sp.Function("y")

    cases: list[SymbolicResult] = []

    expr = (1 + a / x) ** x
    cases.append(
        _run_symbolic(
            "exp_amplification",
            "one-parameter positive control",
            expr,
            lambda: sp.limit(expr, x, sp.oo),
            expected=sp.exp(a),
            manual_chart_hints=0,
            note="Gruntz handles the hidden O(1/x) term in this fixed limit.",
        )
    )

    expr = sp.exp(sp.exp(x + sp.exp(-x)) - sp.exp(x))
    cases.append(
        _run_symbolic(
            "deep_exp_log_visibility",
            "deep exp/log positive control",
            expr,
            lambda: sp.limit(expr, x, sp.oo),
            expected=sp.E,
            manual_chart_hints=0,
            note="A deep exp/log expression is not by itself a differentiator.",
        )
    )

    expr = sp.exp(2 * x) * (sp.log(1 + sp.exp(-x)) - sp.exp(-x))
    cases.append(
        _run_symbolic(
            "cancellation_second_order",
            "symbolic cancellation positive control",
            expr,
            lambda: sp.limit(expr, x, sp.oo),
            expected=-sp.Rational(1, 2),
            manual_chart_hints=0,
            note="Symbolic MRV/series logic already recovers the cancelled term.",
        )
    )

    expr = sp.exp(3 * x) * (
        sp.log(1 + sp.exp(-x)) - sp.exp(-x) + sp.exp(-2 * x) / 2
    )
    cases.append(
        _run_symbolic(
            "cancellation_third_order",
            "symbolic cancellation positive control",
            expr,
            lambda: sp.limit(expr, x, sp.oo),
            expected=sp.Rational(1, 3),
            manual_chart_hints=0,
            note="A second cancellation layer also succeeds in stock SymPy.",
        )
    )

    expr = (1 - sp.exp(-x * z)) / z
    cases.append(
        _run_symbolic(
            "nonuniform_fixed_parameter",
            "parameter-nonuniform diagnostic",
            expr,
            lambda: sp.limit(expr, x, sp.oo),
            expected=1 / z,
            manual_chart_hints=0,
            note=(
                "Correct for fixed z>0, but it does not report the transition "
                "z=xi/x or the z=0 value x."
            ),
        )
    )

    phase = n * (z * sp.sin(theta) - theta)
    cases.append(
        _run_symbolic(
            "bessel_phase_unhinted",
            "raw coalescing-saddle diagnostic",
            phase,
            lambda: sp.series(phase, theta, 0, 7),
            expected=None,
            manual_chart_hints=0,
            note=(
                "Returns a Taylor series containing N*(z-1)*theta and "
                "N*theta^3, but no coupled N-dependent chart."
            ),
        )
    )

    direct_bessel = sp.besselj(n, n * z)
    cases.append(
        _run_symbolic(
            "bessel_large_order_direct",
            "non-toy direct-CAS baseline",
            direct_bessel,
            lambda: sp.series(direct_bessel, n, sp.oo, 2),
            expected=None,
            manual_chart_hints=0,
            note=(
                "On SymPy 1.14 this raises because multivariate MRV set "
                "computation is not implemented."
            ),
        )
    )

    hinted_phase = eps ** -3 * (
        (1 + eps**2 * xi) * sp.sin(eps * u) - eps * u
    )
    hinted_expected = (
        u * xi
        - u**3 / 6
        + eps**2 * (u**5 / 120 - u**3 * xi / 6)
        + sp.Order(eps**4)
    )
    cases.append(
        _run_symbolic(
            "bessel_phase_hinted",
            "hidden-oracle verification only",
            hinted_phase,
            lambda: sp.series(hinted_phase, eps, 0, 4),
            expected=hinted_expected,
            manual_chart_hints=2,
            note=(
                "After theta=eps*u, z=1+eps^2*xi, N=eps^-3 are supplied, "
                "SymPy verifies the Airy normal form and residual."
            ),
        )
    )

    wkb_equation = sp.Eq(eps**2 * sp.diff(y(x), x, 2), x * y(x))
    cases.append(
        _run_symbolic(
            "wkb_turning_point_exact",
            "strong conventional baseline",
            wkb_equation,
            lambda: sp.dsolve(wkb_equation),
            expected=None,
            manual_chart_hints=0,
            note=(
                "SymPy solves this exact model in Airy functions with the "
                "x/eps^(2/3) scale; the compiler must exceed this baseline."
            ),
        )
    )

    singular_equation = sp.Eq(eps * sp.diff(y(x), x) + y(x), x)
    cases.append(
        _run_symbolic(
            "singular_perturbation_exact",
            "strong conventional baseline",
            singular_equation,
            lambda: sp.dsolve(singular_equation, ics={y(0): 0}),
            expected=None,
            manual_chart_hints=0,
            note="The simple boundary layer is already solved exactly by SymPy.",
        )
    )

    singular_solution = x - eps + eps * sp.exp(-x / eps)
    cases.append(
        _run_symbolic(
            "singular_perturbation_outer_series",
            "task-relative loss diagnostic",
            singular_solution,
            lambda: sp.series(singular_solution, eps, 0, 3),
            expected=x - eps + sp.Order(eps**3),
            manual_chart_hints=0,
            note=(
                "The pointwise series drops exp(-x/eps); a uniform boundary "
                "task must reject that forgetting near x=0."
            ),
        )
    )

    free_energy = -sp.log(1 + sp.exp(-n * z)) / n
    cases.append(
        _run_symbolic(
            "partition_fixed_phase",
            "fixed-parameter phase diagnostic",
            free_energy,
            lambda: sp.limit(free_energy, n, sp.oo),
            expected=sp.Integer(0),
            manual_chart_hints=0,
            note="The fixed z>0 limit loses the z=xi/N crossover function.",
        )
    )

    partition_hinted = sp.simplify((n * free_energy).subs(z, xi / n))
    cases.append(
        _run_symbolic(
            "partition_competition_hinted",
            "hidden-oracle verification only",
            partition_hinted,
            lambda: partition_hinted,
            expected=-sp.log(1 + sp.exp(-xi)),
            manual_chart_hints=1,
            note="The crossover function is immediate once z=xi/N is supplied.",
        )
    )

    t = sp.symbols("t", positive=True)
    airy_integrand = sp.cos(n * (t**3 / 3 + z * t))
    cases.append(
        _run_symbolic(
            "airy_oscillatory_integral",
            "canonical integral baseline",
            airy_integrand,
            lambda: sp.integrate(airy_integrand, (t, 0, sp.oo)),
            expected=None,
            manual_chart_hints=0,
            note="Stock SymPy returns the integral unevaluated in this form.",
        )
    )

    return cases


def _median_runtime(fn: Callable[[], np.ndarray], repeats: int = 5) -> float:
    fn()
    fn()
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        fn()
        samples.append(time.perf_counter() - start)
    return statistics.median(samples)


def bessel_transition_benchmark(points: int = 200_000) -> dict[str, object]:
    """Evaluate the leading DLMF 10.19.8 transition approximation.

    The formula is used as an oracle/evaluation target.  The proposed compiler
    earns discovery credit only if it derives the 1/3 and 2/3 scales from the
    raw phase; this function itself earns no discovery credit.
    """

    nu = 10_000.0
    a = np.linspace(-2.0, 2.0, points)
    argument = nu + a * nu ** (1.0 / 3.0)

    def conventional() -> np.ndarray:
        return jv(nu, argument)

    def compiled_leading_airy() -> np.ndarray:
        return (
            2.0 ** (1.0 / 3.0)
            * nu ** (-1.0 / 3.0)
            * airy(-(2.0 ** (1.0 / 3.0)) * a)[0]
        )

    def compiled_first_corrected_airy() -> np.ndarray:
        ai, aip = airy(-(2.0 ** (1.0 / 3.0)) * a)[:2]
        p1 = -a / 5.0
        q0 = 3.0 * a**2 / 10.0
        return (
            2.0 ** (1.0 / 3.0)
            * nu ** (-1.0 / 3.0)
            * ai
            * (1.0 + p1 / nu ** (2.0 / 3.0))
            + 2.0 ** (2.0 / 3.0) / nu * aip * q0
        )

    exact = conventional()
    leading = compiled_leading_airy()
    corrected = compiled_first_corrected_airy()
    conventional_seconds = _median_runtime(conventional)
    leading_seconds = _median_runtime(compiled_leading_airy)
    corrected_seconds = _median_runtime(compiled_first_corrected_airy)
    scale = float(np.max(np.abs(exact)))
    leading_max_abs_error = float(np.max(np.abs(leading - exact)))
    corrected_max_abs_error = float(np.max(np.abs(corrected - exact)))

    return {
        "name": "bessel_transition_killer",
        "nu": nu,
        "a_interval": [-2.0, 2.0],
        "points": points,
        "conventional_scipy_jv_seconds_median": conventional_seconds,
        "compiled_leading_airy_seconds_median": leading_seconds,
        "leading_measured_speedup": conventional_seconds / leading_seconds,
        "leading_max_abs_error": leading_max_abs_error,
        "leading_normalized_max_error": leading_max_abs_error / scale,
        "compiled_first_corrected_airy_seconds_median": corrected_seconds,
        "corrected_measured_speedup": conventional_seconds / corrected_seconds,
        "corrected_max_abs_error": corrected_max_abs_error,
        "corrected_normalized_max_error": corrected_max_abs_error / scale,
        "manual_chart_hints_in_this_evaluator": 2,
        "discovery_credit": False,
        "note": (
            "This demonstrates the payoff available after the transition "
            "chart is known.  It is not evidence that the chart was discovered."
        ),
    }


def main() -> None:
    payload = {
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "sympy": sp.__version__,
            "scipy": scipy.__version__,
            "numpy": np.__version__,
        },
        "symbolic": [asdict(item) for item in symbolic_baselines()],
        "numerical": bessel_transition_benchmark(),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

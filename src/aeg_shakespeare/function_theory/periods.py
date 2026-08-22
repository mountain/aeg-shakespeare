"""History lifting, square-root monodromy, and numerical period integration.

Primitive question
------------------
Once a process quotient has produced a curve ``y^2=P(x)``, how do we keep track
of *which sheet* a history occupies while the base coordinate ``x`` moves around
branch points?  Returning to the same base point need not return to the same
lifted state: analytic continuation around a branch point can change ``y`` to
``-y``.  This is the simplest executable model of the distinction

    state return != history return.

Classical shadow
----------------
Classically this is monodromy of the two-sheeted square-root covering.  On a
smooth hyperelliptic curve, periods arise by integrating holomorphic
differentials along closed lifted cycles.  In genus one two independent periods
form the lattice underlying the complex torus; in higher genus the same idea
feeds a period matrix and Jacobian.  See Forster, Farkas--Kra, and the references
collected in ``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
The library does not jump directly to a named elliptic or Abelian function.
Instead it makes the history lift executable:

1. a base path in the complex ``x``-plane is sampled;
2. the square root is continued by choosing, at each step, the sign closest to
   the previously selected value;
3. the resulting lifted path records whether a closed base loop closes on the
   Riemann surface or changes sheet;
4. a differential ``x^k dx/y`` can then be integrated along the lifted history.

This is deliberately a *bounded numerical continuation engine*.  It is useful
for calibrating topology/period structure, but it is not a certified homology
solver or a proof of a period matrix.

Executable contract
-------------------
``lift_square_root_path`` returns every selected sheet value and an explicit
``sheet_multiplier`` when the base loop closes.  ``integrate_lifted_differential``
uses a complex trapezoidal rule along the supplied samples.  ``GenusOneLattice``
packages two already-computed periods and their ratio without pretending to
construct the cycles that produced them.

Boundary
--------
The continuation rule assumes sufficiently fine sampling and no sample at a
branch point.  Numerical integration carries discretization error.  Arbitrary
homology-basis construction, adaptive contour refinement, rigorous error bounds,
Riemann bilinear relations in genus > 1, and Jacobians remain later work.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass
from typing import Iterable

import sympy as sp

from .abelian import HyperellipticDifferential
from .algebraic import HyperellipticProfile


def _complex_eval(
    expr: sp.Expr,
    symbol: sp.Symbol,
    value: complex,
    *,
    digits: int,
) -> complex:
    remaining = sp.sympify(expr).free_symbols - {symbol}
    if remaining:
        raise ValueError(f"numeric continuation requires all parameters fixed: {remaining}")
    return complex(sp.N(sp.sympify(expr).subs(symbol, value), digits))


@dataclass(frozen=True)
class LiftedSquareRootPath:
    """A sampled base path together with one continuously chosen square-root lift."""

    curve: HyperellipticProfile
    x_values: tuple[complex, ...]
    y_values: tuple[complex, ...]

    @property
    def base_closed(self) -> bool:
        if len(self.x_values) < 2:
            return False
        scale = max(1.0, abs(self.x_values[0]), abs(self.x_values[-1]))
        return abs(self.x_values[-1] - self.x_values[0]) <= 1e-10 * scale

    @property
    def sheet_multiplier(self) -> int | None:
        """Return +1/-1 for a closed base loop, or ``None`` if not comparable."""

        if not self.base_closed or not self.y_values:
            return None
        start = self.y_values[0]
        end = self.y_values[-1]
        if abs(start) == 0:
            return None
        same = abs(end - start)
        flipped = abs(end + start)
        return 1 if same <= flipped else -1

    @property
    def lifted_closed(self) -> bool:
        return self.sheet_multiplier == 1


def lift_square_root_path(
    curve: HyperellipticProfile,
    x_values: Iterable[complex],
    *,
    initial_y: complex | None = None,
    digits: int = 50,
    branch_tolerance: float = 1e-24,
) -> LiftedSquareRootPath:
    """Continue one branch of ``sqrt(P(x))`` along a sampled complex path.

    At each sample the principal square root and its negative are compared with
    the previously selected lift.  The closer one is chosen.  This is the
    discrete analogue of analytic continuation along a path.
    """

    xs = tuple(complex(value) for value in x_values)
    if len(xs) < 2:
        raise ValueError("a lifted path requires at least two base samples")

    ys: list[complex] = []
    previous: complex | None = complex(initial_y) if initial_y is not None else None

    for x_value in xs:
        p_value = _complex_eval(curve.polynomial, curve.x, x_value, digits=digits)
        if abs(p_value) <= branch_tolerance:
            raise ValueError("sample path meets or approaches a branch point too closely")
        principal = cmath.sqrt(p_value)
        candidates = (principal, -principal)
        if previous is None:
            selected = principal
        else:
            selected = min(candidates, key=lambda candidate: abs(candidate - previous))
        ys.append(selected)
        previous = selected

    return LiftedSquareRootPath(curve=curve, x_values=xs, y_values=tuple(ys))


def integrate_lifted_differential(
    path: LiftedSquareRootPath,
    differential: HyperellipticDifferential,
    *,
    digits: int = 50,
) -> complex:
    """Numerically integrate ``x^k dx/y`` along an already lifted path."""

    if differential.curve != path.curve:
        raise ValueError("differential and lifted path must belong to the same curve")

    values: list[complex] = []
    for x_value, y_value in zip(path.x_values, path.y_values, strict=True):
        numerator = _complex_eval(
            differential.numerator,
            path.curve.x,
            x_value,
            digits=digits,
        )
        values.append(numerator / y_value)

    total = 0j
    for index in range(len(path.x_values) - 1):
        dx = path.x_values[index + 1] - path.x_values[index]
        total += 0.5 * (values[index] + values[index + 1]) * dx
    return total


@dataclass(frozen=True)
class GenusOneLattice:
    """Two non-collinear periods of a genus-one quotient.

    The object packages period data supplied by explicit cycle computations or
    exact symmetries.  It does not discover a homology basis by itself.
    """

    omega_a: complex
    omega_b: complex

    def __post_init__(self) -> None:
        if abs(self.omega_a) == 0:
            raise ValueError("first period must be nonzero")
        if abs((self.omega_b / self.omega_a).imag) <= 1e-14:
            raise ValueError("genus-one periods must be non-collinear over R")

    @property
    def tau(self) -> complex:
        return self.omega_b / self.omega_a

    @property
    def oriented_area(self) -> float:
        """Signed Euclidean area of the period parallelogram."""

        return float((self.omega_a.conjugate() * self.omega_b).imag)

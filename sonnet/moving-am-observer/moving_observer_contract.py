"""Research-local certificate contract for a moving affine Riccati observer.

This is a calibration fixture, not an AM-native discovery engine.  It makes the
obligations of the proposed S2-prime search explicit before the blind search is
allowed to use them.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from process_geometry.presentation.canonicalization import ConstraintCanonicalization


def coefficient_jet_complexity(coefficients: tuple[sp.Expr, ...], t: sp.Symbol) -> int:
    """Count coefficients with a nonzero exact first derivative."""

    return sum(sp.simplify(sp.diff(coefficient, t)) != 0 for coefficient in coefficients)


@dataclass(frozen=True)
class MovingObserverCertificate:
    """Exact obligations for one local moving-observer lift."""

    observer_rates: tuple[sp.Expr, sp.Expr]
    frozen_normalization_residuals: tuple[sp.Expr, sp.Expr]
    shape: sp.Expr
    transport: sp.Expr
    observed: sp.Expr
    decomposition_residual: sp.Expr
    reconstruction_residual: sp.Expr
    fixed_complexity: int
    canonical_complexity: int

    @property
    def certified(self) -> bool:
        return (
            all(sp.simplify(value) == 0 for value in (
                self.decomposition_residual,
                self.reconstruction_residual,
            ))
            and any(sp.simplify(value) != 0 for value in self.frozen_normalization_residuals)
        )


def riccati_path_certificate(*, cubic_perturbation: sp.Expr = sp.S.Zero) -> MovingObserverCertificate:
    """Certify the moving root observer on ``(x-t)(x-t-1)+eps*x**3``.

    The root normalization and induced connection are derived from the declared
    quadratic carrier.  A cubic perturbation is deliberately left outside that
    carrier, so it must survive in the shape term rather than being erased by
    affine observer transport.
    """

    t, y = sp.symbols("t y", real=True)
    a, b, c = sp.symbols("a b c")
    r, d = sp.symbols("r d", nonzero=True)

    a_path = t * (t + 1)
    b_path = -(2 * t + 1)
    c_path = sp.S.One
    base_rates = {
        a: sp.diff(a_path, t),
        b: sp.diff(b_path, t),
        c: sp.diff(c_path, t),
    }
    path = {a: a_path, b: b_path, c: c_path, r: t, d: sp.S.One}

    normalization = ConstraintCanonicalization(
        observer_parameters=(r, d),
        constraints=(
            a + b * r + c * r**2,
            a + b * (r + d) + c * (r + d) ** 2,
        ),
        label="ordered Riccati roots",
    )
    frozen = tuple(
        sp.simplify(value.subs(path))
        for value in normalization.differentiated_constraints(
            base_rates, {r: sp.S.Zero, d: sp.S.Zero}
        )
    )
    connection = normalization.induced_connection(base_rates)
    r_dot = sp.simplify(connection.rate(r).subs(path))
    d_dot = sp.simplify(connection.rate(d).subs(path))

    x_in_chart = t + y
    physical = sp.expand(
        a_path + b_path * x_in_chart + c_path * x_in_chart**2
        + sp.sympify(cubic_perturbation) * x_in_chart**3
    )
    shape = sp.expand(physical)  # d=1 on this calibrated path
    transport = sp.expand(-r_dot - d_dot * y)
    observed = sp.expand(shape + transport)
    decomposition_residual = sp.expand(observed - shape - transport)
    reconstruction_residual = sp.expand(r_dot + d_dot * y + observed - physical)

    fixed_coefficients = (a_path, b_path, c_path)
    canonical_quadratic_coefficients = tuple(
        sp.expand(observed).coeff(y, degree) for degree in range(3)
    )
    return MovingObserverCertificate(
        observer_rates=(r_dot, d_dot),
        frozen_normalization_residuals=frozen,
        shape=shape,
        transport=transport,
        observed=observed,
        decomposition_residual=decomposition_residual,
        reconstruction_residual=reconstruction_residual,
        fixed_complexity=coefficient_jet_complexity(fixed_coefficients, t),
        canonical_complexity=coefficient_jet_complexity(
            canonical_quadratic_coefficients, t
        ),
    )


__all__ = ["MovingObserverCertificate", "riccati_path_certificate"]

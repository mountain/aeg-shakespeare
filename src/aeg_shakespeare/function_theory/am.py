"""The first optional function-theory layer: the affine A/M calculus.

The distinguished process frame is

    A = d/da,
    M = d/dv + a d/da,

so ``[A,M] = A``.  This module packages that concrete calculus without making
it the universal Shakespeare ontology.  It is intended as one reusable
function-theory backend alongside future alternatives (projective, elliptic,
hyperelliptic, Lie-algebroid, ...).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from ..frame import ProcessFrame


def affine_am_frame(a: sp.Symbol, v: sp.Symbol) -> ProcessFrame:
    """Return the canonical two-generator affine A/M process frame."""

    return ProcessFrame(
        assignments=(a, v),
        generators={
            "A": {a: sp.S.One, v: sp.S.Zero},
            "M": {a: a, v: sp.S.One},
        },
    )


@dataclass(frozen=True)
class AMPowerWeight:
    """One member of the A/M power-weight family.

    The represented expression is

        Phi_(nu,w) = a**nu * exp((w-nu)*v).

    Under the A/M frame,

        M Phi_(nu,w) = w Phi_(nu,w),
        A Phi_(nu,w) = nu Phi_(nu-1,w-1).

    ``nu`` and ``weight`` are symbolic parameters; no claim is made that this
    family exhausts the function theory.
    """

    a: sp.Symbol
    v: sp.Symbol
    nu: sp.Expr
    weight: sp.Expr

    @property
    def expression(self) -> sp.Expr:
        return self.a ** self.nu * sp.exp((self.weight - self.nu) * self.v)


@dataclass(frozen=True)
class AMFunctionTheory:
    """Convenience wrapper for the affine A/M function calculus.

    This object intentionally sits *above* ``ProcessFrame``.  A/M notation is a
    concrete function-theory choice; Shakespeare's literal histories, task
    quotients, grammar discovery, and presentation search do not depend on it.
    """

    a: sp.Symbol
    v: sp.Symbol

    @property
    def frame(self) -> ProcessFrame:
        return affine_am_frame(self.a, self.v)

    def A(self, expr: sp.Expr) -> sp.Expr:
        return self.frame.apply("A", expr)

    def M(self, expr: sp.Expr) -> sp.Expr:
        return self.frame.apply("M", expr)

    def commutator(self, expr: sp.Expr) -> sp.Expr:
        """Return ``[A,M] expr``."""

        return self.frame.commutator("A", "M", expr)

    def power_weight(self, nu: sp.Expr, weight: sp.Expr) -> AMPowerWeight:
        return AMPowerWeight(self.a, self.v, sp.sympify(nu), sp.sympify(weight))

    def shifted_M(self, expr: sp.Expr, shift: sp.Expr) -> sp.Expr:
        """Apply the shifted process operator ``M - shift``."""

        return sp.expand(self.M(expr) - sp.sympify(shift) * sp.sympify(expr))

    def pbw_residual(self, expr: sp.Expr, *, m: int, n: int) -> sp.Expr:
        """Verify the PBW reordering ``M^n A^m = A^m (M-m)^n`` on ``expr``.

        A zero result certifies the identity for the supplied expression.  This
        is exposed as a verifier/helper rather than as a replacement for the
        underlying ordered process histories.
        """

        if m < 0 or n < 0:
            raise ValueError("m and n must be non-negative")

        left = self.frame.iterate("A", expr, m)
        left = self.frame.iterate("M", left, n)

        right = sp.sympify(expr)
        for _ in range(n):
            right = self.shifted_M(right, m)
        right = self.frame.iterate("A", right, m)
        return sp.simplify(sp.expand(left - right))

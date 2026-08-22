"""Algebraic-curve profiles for process quotients.

This module is intentionally modest: it recognizes the common hyperelliptic
form ``y**2 = P(x)`` and records exact algebraic invariants that help downstream
code decide whether elementary, elliptic/Abelian, or higher-genus function
languages may be required.

It is not a general algebraic-geometry engine and it does not make genus the
universal Shakespeare complexity measure.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class HyperellipticProfile:
    """Exact profile of ``y**2 = polynomial(x)`` over symbolic parameters."""

    x: sp.Symbol
    y: sp.Symbol
    polynomial: sp.Expr
    degree: int
    discriminant: sp.Expr
    generic_genus: int | None

    @property
    def relation(self) -> sp.Expr:
        return sp.expand(self.y**2 - self.polynomial)

    @property
    def generically_smooth(self) -> bool:
        """Whether the discriminant is not identically zero."""

        return sp.simplify(self.discriminant) != 0

    @property
    def degeneration_condition(self) -> sp.Expr:
        """Parameter expression whose vanishing marks repeated branch points."""

        return sp.factor(self.discriminant)


def hyperelliptic_profile(
    x: sp.Symbol,
    y: sp.Symbol,
    polynomial: sp.Expr,
) -> HyperellipticProfile:
    """Analyze a process quotient in hyperelliptic form ``y**2 = P(x)``.

    For square-free ``P`` of degree ``d >= 1``, the smooth projective
    hyperelliptic curve has genus ``floor((d-1)/2)``.  With symbolic parameters,
    a nonzero discriminant means that this is the *generic* genus away from the
    displayed degeneration locus.
    """

    polynomial = sp.expand(sp.sympify(polynomial))
    try:
        poly = sp.Poly(polynomial, x)
    except sp.PolynomialError as exc:
        raise ValueError("hyperelliptic polynomial must be polynomial in x") from exc

    degree = int(poly.degree())
    if degree < 1:
        raise ValueError("hyperelliptic polynomial must have positive degree")
    discriminant = sp.factor(sp.discriminant(poly.as_expr(), x))
    generic_genus = (degree - 1) // 2 if discriminant != 0 else None

    return HyperellipticProfile(
        x=x,
        y=y,
        polynomial=polynomial,
        degree=degree,
        discriminant=discriminant,
        generic_genus=generic_genus,
    )

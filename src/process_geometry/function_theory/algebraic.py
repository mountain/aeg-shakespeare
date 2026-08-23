"""Algebraic-curve profiles for process quotients.

Mathematical lineage
--------------------
Elliptic and Abelian function theory historically did not begin as a catalogue
of special functions.  Elliptic integrals led to inversion; inversion exposed
periods; periods produced complex tori; and the resulting function theory was
then algebraized by relations such as the Weierstrass cubic.  Riemann surfaces,
algebraic curves, Abelian integrals, and Jacobians grew from this analytic and
geometric circle of ideas.

Shakespeare uses the same history in reverse as a calibration principle.  A
primitive process may first force a constraint/invariant quotient.  Only after
that quotient is visible do we ask what geometry and what function language are
adequate.  Thus a relation ``y**2 = P(x)`` is not introduced because we already
know the answer is elliptic or hyperelliptic; it is an algebraic shadow emitted
by the process reduction.

Implementation
--------------
This module deliberately implements only a small, exact observable:
``HyperellipticProfile`` records degree, discriminant, generic genus, and the
degeneration condition for ``y**2 = P(x)``.  That is enough for classical tests
to distinguish genus-zero, genus-one, and higher-genus quotient regimes without
preloading the corresponding named function theory.

Boundary
--------
Genus is not a complete process normal form, and this module is not a general
algebraic-geometry engine.  Period lattices, Abel-Jacobi maps, Jacobians, and
function-field compression belong to later layers and should be derived when a
calibration actually requires them.

See ``docs/08-function-theory-genus-hierarchy.md`` and
``docs/09-literate-programming-and-mathematical-lineage.md``.
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

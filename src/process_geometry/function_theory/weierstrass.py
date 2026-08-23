"""Exact cubic algebraization data for a genus-one process quotient.

Mathematical lineage
--------------------
The Weierstrass model is one of the decisive bridges between elliptic function
theory and algebraic curves.  A nonsingular cubic can be written in the short
form

    W^2 = 4 X^3 - g2 X - g3,

and the same invariants ``g2`` and ``g3`` occur in the differential equation of
the Weierstrass ``wp`` function.  The discriminant ``g2^3-27*g3^2`` detects
singularity, while the modular invariant records the complex-isomorphism class.
See NIST DLMF §§23.2, 23.3, and 23.19 and Silverman, *The Arithmetic of
Elliptic Curves*.

Shakespeare reconstruction
---------------------------
This module is downstream of process reduction.  It does not decide that a
problem "should use Weierstrass functions".  Instead, once a process has
already emitted a nonsingular cubic ``y^2=P_3(x)``, we expose the exact affine
change of variables that turns that algebraic quotient into short Weierstrass
form.  The resulting invariants can then be compared with independently
constructed period data.

Boundary
--------
Equal ``j`` is a statement about complex elliptic-curve isomorphism after the
usual field hypotheses; it is not equality of process presentations, physical
systems, period bases, or tasks.  This module does not construct ``wp`` or a
period lattice and does not choose an analytic branch of the Abelian integral.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .algebraic import HyperellipticProfile


@dataclass(frozen=True)
class WeierstrassCubicProfile:
    """Short-Weierstrass invariants and exact coordinate map for ``y^2=P_3(x)``."""

    curve: HyperellipticProfile
    X: sp.Symbol
    W: sp.Symbol
    x_image: sp.Expr
    y_image: sp.Expr
    g2: sp.Expr
    g3: sp.Expr
    discriminant: sp.Expr
    klein_J: sp.Expr
    j_invariant: sp.Expr

    @property
    def relation(self) -> sp.Expr:
        """Return ``W^2 - (4 X^3 - g2 X - g3)``."""

        return sp.expand(self.W**2 - (4 * self.X**3 - self.g2 * self.X - self.g3))

    def transformation_residual(self) -> sp.Expr:
        """Verify the affine map modulo the original cubic relation."""

        pulled = sp.expand(
            self.relation.subs({self.X: self.x_image, self.W: self.y_image})
        )
        reduced = sp.expand(pulled.subs(self.curve.y**2, self.curve.polynomial))
        return sp.factor(reduced)


def weierstrass_cubic_profile(
    curve: HyperellipticProfile,
    X: sp.Symbol,
    W: sp.Symbol,
) -> WeierstrassCubicProfile:
    """Convert a cubic ``y^2=P_3(x)`` to short Weierstrass form exactly.

    Write

        P_3(x) = a x^3 + b x^2 + c x + d.

    The affine change

        X = (3 a x + b) / 12,
        W = a y / 4

    gives

        W^2 = 4 X^3 - g2 X - g3

    with

        g2 = (b^2 - 3 a c) / 12,
        g3 = (-2 b^3 + 9 a b c - 27 a^2 d) / 432.

    ``Klein J`` follows the DLMF convention ``J=g2^3/Delta``; the algebraic
    ``j`` invariant is ``1728*J``.
    """

    if curve.degree != 3:
        raise ValueError("Weierstrass cubic profile requires degree exactly 3")
    if curve.generic_genus != 1:
        raise ValueError("Weierstrass cubic profile requires a generically smooth cubic")
    if X == W:
        raise ValueError("Weierstrass coordinates X and W must be distinct")

    poly = sp.Poly(curve.polynomial, curve.x)
    a, b, c, d = poly.all_coeffs()
    x_image = sp.cancel((3 * a * curve.x + b) / 12)
    y_image = sp.cancel(a * curve.y / 4)
    g2 = sp.factor((b**2 - 3 * a * c) / 12)
    g3 = sp.factor((-2 * b**3 + 9 * a * b * c - 27 * a**2 * d) / 432)
    discriminant = sp.factor(g2**3 - 27 * g3**2)
    if discriminant == 0:
        raise ValueError("short Weierstrass discriminant vanishes identically")
    klein_J = sp.cancel(g2**3 / discriminant)
    j_invariant = sp.cancel(1728 * klein_J)

    profile = WeierstrassCubicProfile(
        curve=curve,
        X=X,
        W=W,
        x_image=x_image,
        y_image=y_image,
        g2=g2,
        g3=g3,
        discriminant=discriminant,
        klein_J=klein_J,
        j_invariant=j_invariant,
    )
    if profile.transformation_residual() != 0:
        raise AssertionError("internal Weierstrass transformation certificate failed")
    return profile

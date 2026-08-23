"""Abelian-integral structure emitted by a hyperelliptic process quotient.

Mathematical lineage
--------------------
Once an algebraic curve ``y^2 = P(x)`` has appeared, classical analysis does
not stop at its genus.  One studies holomorphic differentials, integrates them
along paths, and compares the values after continuation around closed cycles.
For a genus-``g`` hyperelliptic curve a standard holomorphic basis is

    dx/y, x dx/y, ..., x^(g-1) dx/y.

The first homology has rank ``2g``; integrating the ``g`` differentials over a
homology basis produces the period data behind the Jacobian.  In genus one the
same construction gives the two-period lattice of elliptic-function theory.
See Forster, *Lectures on Riemann Surfaces*, and Farkas--Kra, *Riemann
Surfaces*.  For an explicit hyperelliptic differential basis see also the
references collected in ``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
The process-first order is deliberately the reverse of a named special-function
solver.  A process first emits an algebraic quotient.  This module then asks
which canonical differentials the quotient itself carries and how many global
cycle directions can contribute history residuals.

A ``HyperellipticDifferential`` is intentionally represented as a coefficient
of ``dx`` rather than as a SymPy differential object.  This keeps the algebraic
backend simple while retaining the exact mathematical form ``x^k dx/y``.  Its
``pullback_coefficient`` method asks what the differential becomes along a
chosen process ``dx/dt``.  For example, if a reduced process satisfies
``dx/dt = y``, then ``dx/y`` pulls back to ``dt`` exactly.

Boundary
--------
This module does not choose homology cycles, analytically continue square-root
branches, compute period matrices, prove uniformization, or construct a
Jacobian as a complex torus.  ``homology_rank = 2g`` is topological structure;
it is not a numerically computed period lattice.  Concrete cycle integrals
belong in cited calibration tests until a genuinely reusable period engine is
forced by more than one example.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .algebraic import HyperellipticProfile


@dataclass(frozen=True)
class HyperellipticDifferential:
    """One canonical differential ``x^power dx / y`` on a hyperelliptic curve."""

    curve: HyperellipticProfile
    power: int

    def __post_init__(self) -> None:
        if self.power < 0:
            raise ValueError("differential power must be non-negative")

    @property
    def numerator(self) -> sp.Expr:
        return self.curve.x ** self.power

    @property
    def coefficient(self) -> sp.Expr:
        """Return the coefficient of ``dx`` in ``x^power dx/y``."""

        return self.numerator / self.curve.y

    def pullback_coefficient(self, dx_dt: sp.Expr) -> sp.Expr:
        """Return the coefficient of ``dt`` after substituting ``dx=dx_dt*dt``."""

        return sp.cancel(sp.sympify(dx_dt) * self.numerator / self.curve.y)


@dataclass(frozen=True)
class AbelianIntegralProfile:
    """Canonical differential/homology profile of a generic smooth quotient.

    ``abelian_dimension`` is the genus ``g`` and hence the number of independent
    holomorphic differentials.  ``homology_rank`` is ``2g``.  These two numbers
    are the dimensions that later enter the Abel--Jacobi/Jacobian construction;
    no period values are claimed here.
    """

    curve: HyperellipticProfile
    differentials: tuple[HyperellipticDifferential, ...]
    abelian_dimension: int
    homology_rank: int

    def pullback_coefficients(self, dx_dt: sp.Expr) -> tuple[sp.Expr, ...]:
        """Pull every canonical differential back along one reduced process."""

        return tuple(
            differential.pullback_coefficient(dx_dt)
            for differential in self.differentials
        )


def holomorphic_differential_basis(
    curve: HyperellipticProfile,
) -> tuple[HyperellipticDifferential, ...]:
    """Return ``dx/y, x dx/y, ..., x^(g-1) dx/y`` for generic genus ``g``.

    The routine requires the curve profile to have a generic smooth genus.  For
    genus zero the returned basis is empty.
    """

    genus = curve.generic_genus
    if genus is None:
        raise ValueError("holomorphic basis requires a generically smooth curve")
    return tuple(HyperellipticDifferential(curve, power) for power in range(genus))


def abelian_integral_profile(curve: HyperellipticProfile) -> AbelianIntegralProfile:
    """Attach canonical differential and first-homology dimensions to a curve."""

    basis = holomorphic_differential_basis(curve)
    genus = curve.generic_genus
    assert genus is not None
    return AbelianIntegralProfile(
        curve=curve,
        differentials=basis,
        abelian_dimension=genus,
        homology_rank=2 * genus,
    )

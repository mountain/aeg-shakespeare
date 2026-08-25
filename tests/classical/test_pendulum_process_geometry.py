"""Pendulum: constrained process -> energy quotient -> genus-one curve.

Question
--------
Can the classical elliptic geometry of the planar simple pendulum be recovered
without taking an angle variable, ``sin(theta)``, ``cos(theta)``, an elliptic
integral, or an elliptic function as primitive input?

Primitive data
--------------
The test receives only a dimensionless planar position ``q=(qx,qy)``, velocity
``v=(vx,vy)``, the rigid-rod relation ``|q|^2=1``, constant downward gravity,
and an unresolved radial multiplier ``lambda``.  The local process is

    D q = v,
    D v = -e_y + lambda q.

No angular coordinate is supplied.  In particular the familiar equation
``theta'' + sin(theta) = 0`` is deliberately *not* the input representation.

Classical lineage
-----------------
The pendulum is a standard one-degree-of-freedom conservative mechanical
system; eliminating the time variable on an energy level leads to an elliptic
integral, and inversion leads to elliptic functions.  Standard analytic
references for elliptic integrals/functions include [DLMF-19], [DLMF-22], and
[Whittaker-Watson-1927].  For the mechanics background see [Arnold-1989].
The interpretation of the resulting smooth cubic as a genus-one algebraic
curve belongs to the classical Riemann-surface/algebraic-curve correspondence;
see [Forster-1981] and [Silverman-2009].  Exact ideal reduction in this test is
implemented with a Gröbner-basis backend; see [Cox-Little-OShea-2015].

Shakespeare reconstruction
---------------------------
The explanatory order is reversed.  We first require the geometric constraint
to remain true under the process.  Prolonging ``|q|^2-1=0`` produces tangency
and then determines the radial multiplier.  Only after this constrained process
is closed do we verify the energy invariant.  On a fixed energy leaf the
gravity observable

    U = <e_y, q> = qy

and its process derivative

    Y = D U = vy

satisfy, modulo the maintained constraints,

    Y^2 = 2 (E-U) (1-U^2).

The right side is cubic in U.  Its nonzero generic discriminant therefore gives
a smooth genus-one quotient away from E=+/-1.

**Shakespeare interpretation.**  The elliptic-function language is not treated
as the solver we started with; it is a later classical shadow of the quotient
geometry forced by the primitive constrained process.

Calibration statement
---------------------
Passing this file certifies the following exact chain for the chosen
normalization:

1. preservation of the rod relation produces the tangent relation;
2. preservation of tangency uniquely forces
   ``lambda = qy - vx^2 - vy^2``;
3. ``H=(vx^2+vy^2)/2+qy`` is invariant modulo rod+tangency;
4. the reduced observables U=qy and Y=vy obey
   ``Y^2=2(E-U)(1-U^2)`` on an energy leaf;
5. this cubic has generic genus one and discriminant
   ``64(E-1)^2(E+1)^2``.

Proof map
---------
``test_constraint_prolongation_*`` checks step 1.
``test_constraint_force_*`` checks step 2 by exact quotient reduction.
``test_energy_*`` checks step 3.
``test_pendulum_process_quotient_*`` checks steps 4-5.
``test_pendulum_degenerations_*`` checks the singular parameter values.

Boundary
--------
This file does *not* construct the period lattice, prove analytic
uniformization by ``C/Lambda``, construct Weierstrass functions, or prove that
the quotient curve is a complete normal form for every pendulum task.  Those
are later stages in the proposed analysis -> topology -> algebra cycle.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.

[Cox-Little-OShea-2015] D. A. Cox, J. Little, D. O'Shea, *Ideals, Varieties,
and Algorithms*, 4th ed., Springer, 2015. DOI: 10.1007/978-3-319-16721-3.

[DLMF-19] NIST Digital Library of Mathematical Functions, Chapter 19,
“Elliptic Integrals”, https://dlmf.nist.gov/19 .

[DLMF-22] NIST Digital Library of Mathematical Functions, Chapter 22,
“Jacobian Elliptic Functions”, https://dlmf.nist.gov/22 .

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
DOI: 10.1007/978-1-4612-5961-9.

[Silverman-2009] J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed.,
Springer, 2009. DOI: 10.1007/978-0-387-09494-6.

[Whittaker-Watson-1927] E. T. Whittaker and G. N. Watson,
*A Course of Modern Analysis*, 4th ed., Cambridge University Press, 1927,
Chapters XX-XXII.
"""

import sympy as sp

from process_geometry.analysis.algebraic import hyperelliptic_profile
from process_geometry.presentation.constraints import (
    AlgebraicConstraintSet,
    constraint_prolongation,
)
from process_geometry.process.local import ProcessSystem


def pendulum_raw_process():
    """Return the primitive dimensionless constrained process described above."""

    qx, qy, vx, vy, lambda_ = sp.symbols("qx qy vx vy lambda")
    system = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: lambda_ * qx,
            vy: -1 + lambda_ * qy,
        },
        name="D",
    )
    return qx, qy, vx, vy, lambda_, system


def test_constraint_prolongation_derives_tangency_before_solving_force():
    # GIVEN: the rigid relation and the unresolved constrained process.
    qx, qy, vx, vy, lambda_, system = pendulum_raw_process()
    rod = qx**2 + qy**2 - 1

    # DISCOVER: prolong the relation instead of parameterizing the circle.
    chain = constraint_prolongation(system.derive, rod, order=2)

    # ASSERT: the first derivative is tangency; the second sees the multiplier.
    assert sp.expand(chain[1] - 2 * (qx * vx + qy * vy)) == 0
    assert lambda_ in chain[2].free_symbols


def test_constraint_force_is_forced_by_preserving_the_rod_relation():
    qx, qy, vx, vy, lambda_, system = pendulum_raw_process()
    rod = qx**2 + qy**2 - 1
    tangent = sp.expand(system.derive(rod) / 2)
    tangent_rate = sp.expand(system.derive(tangent))

    # DISCOVER: work modulo the geometric relations already forced by history.
    quotient = AlgebraicConstraintSet(
        (qx, qy, vx, vy, lambda_),
        (rod, tangent),
    )
    reduced_rate = quotient.reduce(tangent_rate)
    solutions = sp.solve(sp.Eq(reduced_rate, 0), lambda_)

    # ASSERT: constraint preservation determines the radial force uniquely.
    assert len(solutions) == 1
    assert sp.expand(solutions[0] - (qy - vx**2 - vy**2)) == 0


def test_energy_is_an_invariant_after_constraint_transport():
    qx, qy, vx, vy, lambda_, raw = pendulum_raw_process()
    lambda_solution = qy - vx**2 - vy**2
    system = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: sp.expand(lambda_solution * qx),
            vy: sp.expand(-1 + lambda_solution * qy),
        },
        name="D",
    )

    rod = qx**2 + qy**2 - 1
    tangent = qx * vx + qy * vy
    quotient = AlgebraicConstraintSet((qx, qy, vx, vy), (rod, tangent))
    energy = sp.Rational(1, 2) * (vx**2 + vy**2) + qy

    # ASSERT: D(H)=0 in the constraint quotient, not merely after substitution.
    assert quotient.reduce(system.derive(energy)) == 0


def test_pendulum_process_quotient_forces_a_generic_genus_one_curve():
    qx, qy, vx, vy, E = sp.symbols("qx qy vx vy E")

    # GIVEN: rigid rod, tangency, and one energy leaf.  No angle variable.
    rod = qx**2 + qy**2 - 1
    tangent = qx * vx + qy * vy
    energy_leaf = vx**2 + vy**2 - 2 * (E - qy)
    quotient = AlgebraicConstraintSet(
        (qx, qy, vx, vy, E),
        (rod, tangent, energy_leaf),
    )

    U, Y = sp.symbols("U Y")
    curve_polynomial = sp.expand(2 * (E - U) * (1 - U**2))

    # DISCOVER: U=qy is the gravity observable and Y=D(U)=vy.  Ideal membership
    # certifies the reduced curve rather than inserting a trigonometric identity.
    physical_relation = sp.expand(vy**2 - curve_polynomial.subs(U, qy))
    assert quotient.contains(physical_relation)

    # CLASSICAL SHADOW: a smooth cubic y^2=P_3(x) is genus one.
    profile = hyperelliptic_profile(U, Y, curve_polynomial)
    assert profile.degree == 3
    assert profile.generic_genus == 1
    assert profile.generically_smooth
    assert sp.factor(profile.discriminant) == 64 * (E - 1) ** 2 * (E + 1) ** 2


def test_pendulum_degenerations_are_detected_as_geometry_not_special_function_cases():
    U, Y, E = sp.symbols("U Y E")
    profile = hyperelliptic_profile(U, Y, 2 * (E - U) * (1 - U**2))

    # ASSERT: E=+/-1 are repeated-branch-point degenerations; E=0 is generic.
    assert sp.simplify(profile.discriminant.subs(E, 1)) == 0
    assert sp.simplify(profile.discriminant.subs(E, -1)) == 0
    assert sp.simplify(profile.discriminant.subs(E, 0)) != 0

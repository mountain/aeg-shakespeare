"""Simple pendulum: the observable cubic is a genuine Z2 state quotient.

Retrieval
---------
Problem: planar simple pendulum; information loss in the reduced observable
curve.
Domains: constrained mechanics, algebraic quotients, elliptic curves,
reconstruction.
Classical names / aliases: simple pendulum, energy curve, elliptic integral,
state reduction, reflection symmetry.
Process Geometry roles: observable algebraic quotient, task-relative
representation, quotient fiber, reconstruction boundary.
Prerequisites: elementary constrained mechanics and polynomial ideals.
Related vignettes: ``test_pendulum_process_geometry.py``,
``test_pendulum_discovery_layer.py``, and
``docs/vignettes/simple-pendulum.md``.
Theory Map relation: boundary certificate for the existing H4 pendulum
calibration; no theory promotion.

Problem statement
-----------------
For the dimensionless planar pendulum let

    q=(qx,qy),  v=(vx,vy),

with

    qx^2 + qy^2 = 1,
    qx*vx + qy*vy = 0,
    vx^2 + vy^2 = 2(E-qy).

The established pendulum reconstruction uses the first-order observable

    U=qy,  Y=D(U)=vy,

whose algebraic image satisfies

    Y^2 = 2(E-U)(1-U^2).

This file asks a different question from the earlier quotient-discovery tests:
what information has the map

    pi(qx,qy,vx,vy) = (qy,vy)

forgotten, and which hidden combinations remain reconstructible from its image?

Why this problem is here
------------------------
An algebraically correct reduced curve is not automatically a complete state
representation.  Process Geometry treats quotients as information contracts:
a useful vignette must say what is preserved, what is identified, and what a
future decoder would need.  The pendulum is the first place where that
obligation can be certified exactly rather than left as prose.

Primitive data
--------------
The test receives only the dimensionless constrained energy leaf and the closed
Cartesian pendulum vector field

    D q = v,
    D v = -e_y + lambda q,
    lambda = qy - vx^2 - vy^2.

It uses the already established observable ``(U,Y)=(qy,vy)``.  No angle
coordinate, square-root branch, decoder, or elliptic function is supplied.

Notation and prerequisites
--------------------------
``E`` is the dimensionless conserved energy.  The involution

    iota(qx,qy,vx,vy)=(-qx,qy,-vx,vy)

reflects the hidden horizontal position and velocity simultaneously.  A
``Z2`` quotient means that applying ``iota`` twice is the identity and that the
observable map is invariant under this action.

Classical lineage
-----------------
Reduction by a symmetry or by selected observables generally identifies source
states lying in the same fiber.  For the mechanical pendulum, reflection of the
horizontal coordinate is an elementary symmetry of the Cartesian constrained
system.  Standard mechanics background is [Arnold-1989].  Exact ideal
membership below uses Groebner-basis reduction as in [Cox-Little-OShea-2015].

Process Geometry reconstruction
-------------------------------
The test first verifies that ``iota`` preserves the rod, tangency, energy leaf,
and the closed vector field, while fixing ``qy`` and ``vy``.  Thus the two
states related by ``iota`` have identical first-order observable data throughout
the reduced semantics.

It then asks what polynomial information about the hidden coordinates still
descends to the observable curve.  Modulo the energy leaf,

    qx^2 = 1-qy^2,
    vx^2 = 2(E-qy)-vy^2,
    qx*vx = -qy*vy.

So the even/quadratic hidden data are reconstructible, while the simultaneous
sign of ``(qx,vx)`` is not.

**Process Geometry interpretation.**  The cubic is therefore not merely a
change of coordinates.  It is an observer-relative algebraic state quotient
with a generically two-valued reconstruction.  A full-state decoder must carry
one additional branch choice (or equivalent history/initial-condition data).

Calibration statement
---------------------
Passing this file certifies that:

1. ``iota`` is an involutive symmetry of the closed Cartesian pendulum process
   and of the fixed-energy constraint ideal;
2. the observable map ``(qx,qy,vx,vy)->(qy,vy)`` is invariant under ``iota``;
3. two explicit distinct nondegenerate states on the same energy leaf have the
   same observable pair;
4. ``qx^2``, ``vx^2``, and ``qx*vx`` are exactly reconstructible from
   ``(U,Y,E)`` modulo the source constraints;
5. the familiar cubic relation is exactly the compatibility condition carried
   by those descended quantities.

Proof map
---------
``test_hidden_involution_preserves_process_constraints_and_observables`` checks
items 1-3.
``test_even_hidden_data_descend_but_the_branch_sign_does_not`` checks items 4-5.

Boundary and reconstruction
---------------------------
This file does not construct a global decoder, classify the full scheme-theoretic
fiber at branch/turning points, or prove that this ``Z2`` quotient is sufficient
for every pendulum task.  It also does not reconstruct A/M lift history.

The exact certificate is narrower: away from special fibers, the chosen
first-order observable representation forgets the simultaneous sign of
``(qx,vx)`` while retaining the listed quadratic combinations.  Recovering the
full Cartesian state therefore requires extra branch/history data.

References and onward links
---------------------------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.

[Cox-Little-OShea-2015] D. Cox, J. Little, D. O'Shea, *Ideals, Varieties, and
Algorithms*, 4th ed., Springer, 2015. DOI: 10.1007/978-3-319-16721-3.

Continue with ``test_pendulum_period_history.py`` for the canonical differential
and period-history layer.  See ``docs/vignettes/simple-pendulum.md`` for the
complete family map and the remaining reconstruction obligations.
"""

from __future__ import annotations

import sympy as sp

from process_geometry.presentation.constraints import AlgebraicConstraintSet
from process_geometry.process.local import ProcessSystem


def _pendulum_leaf():
    qx, qy, vx, vy, E = sp.symbols("qx qy vx vy E")
    multiplier = qy - vx**2 - vy**2
    system = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: sp.expand(multiplier * qx),
            vy: sp.expand(-1 + multiplier * qy),
        },
        name="D",
    )
    rod = qx**2 + qy**2 - 1
    tangent = qx * vx + qy * vy
    energy = vx**2 + vy**2 - 2 * (E - qy)
    constraints = AlgebraicConstraintSet(
        (qx, qy, vx, vy, E),
        (rod, tangent, energy),
    )
    return qx, qy, vx, vy, E, system, constraints


def test_hidden_involution_preserves_process_constraints_and_observables():
    qx, qy, vx, vy, E, system, constraints = _pendulum_leaf()
    iota = {qx: -qx, qy: qy, vx: -vx, vy: vy, E: E}

    # ASSERT: all defining source relations are invariant under the reflection.
    for relation in constraints.relations:
        transformed = sp.expand(relation.subs(iota, simultaneous=True))
        assert sp.expand(transformed - relation) == 0

    # ASSERT: the involution commutes with the closed process vector field.
    for variable in (qx, qy, vx, vy):
        transformed_variable = iota[variable]
        left = sp.expand(system.derive(transformed_variable))
        right = sp.expand(system.derive(variable).subs(iota, simultaneous=True))
        assert sp.expand(left - right) == 0

    # The chosen first-order observable is literally fixed by iota.
    assert iota[qy] == qy
    assert iota[vy] == vy

    # Give an exact nondegenerate witness: both hidden coordinates change sign,
    # yet (U,Y,E) is identical and all source constraints vanish.
    state = {
        qx: sp.Rational(3, 5),
        qy: sp.Rational(4, 5),
        vx: -sp.Rational(4, 5),
        vy: sp.Rational(3, 5),
        E: sp.Rational(13, 10),
    }
    reflected = {
        qx: -state[qx],
        qy: state[qy],
        vx: -state[vx],
        vy: state[vy],
        E: state[E],
    }
    assert state != reflected
    for relation in constraints.relations:
        assert sp.simplify(relation.subs(state)) == 0
        assert sp.simplify(relation.subs(reflected)) == 0
    assert (state[qy], state[vy], state[E]) == (
        reflected[qy],
        reflected[vy],
        reflected[E],
    )


def test_even_hidden_data_descend_but_the_branch_sign_does_not():
    qx, qy, vx, vy, E, _, constraints = _pendulum_leaf()

    # ASSERT: quadratic hidden data are exact functions of observable data.
    assert constraints.contains(qx**2 - (1 - qy**2))
    assert constraints.contains(vx**2 - (2 * (E - qy) - vy**2))
    assert constraints.contains(qx * vx + qy * vy)

    # ASSERT: compatibility of the descended quadratic data is precisely the
    # first-order observable cubic already discovered by the earlier vignettes.
    observable_relation = sp.expand(
        vy**2 - 2 * (E - qy) * (1 - qy**2)
    )
    assert constraints.contains(observable_relation)

"""Pendulum discovery I: process -> invariant -> algebraic quotient.

Question
--------
Can Shakespeare remove two pieces of classical prior knowledge from its
pendulum reconstruction: the supplied energy formula and the supplied reduced
cubic relation?

Primitive data
--------------
The test receives only planar position ``q=(qx,qy)``, velocity ``v=(vx,vy)``,
the rigid-rod relation ``|q|^2=1``, constant downward gravity, and an unresolved
radial multiplier ``lambda``. The process is

    D q = v,
    D v = -e_y + lambda q.

No angle, trigonometric function, Hamiltonian, energy formula, elliptic
integral, or algebraic quotient equation is supplied.

Classical lineage
-----------------
For the simple pendulum, conservation of mechanical energy reduces the motion
to a one-dimensional quadrature and hence to an elliptic integral. Standard
mechanics background is [Arnold-1989]. Exact polynomial ideal reduction and
elimination use the classical Groebner-basis machinery of
[Cox-Little-OShea-2015]. The genus-one interpretation of a smooth cubic belongs
to the standard algebraic-curve/Riemann-surface correspondence; see
[Forster-1981].

Shakespeare reconstruction
---------------------------
The order is deliberately reversed.

First, preserving the rod constraint determines the unresolved radial force.
After that local constrained process is closed, Shakespeare generates the
bounded polynomial observer grammar through degree two and asks for null
directions of the process action modulo the geometric constraint ideal. No
invariant template is supplied. The unique nontrivial direction is

    I = vx^2 + vy^2 + 2 qy,

which is twice the usual dimensionless mechanical energy.

Only then do we introduce a symbol ``K`` for the discovered invariant value and
adjoin the leaf ``I=K``. For the still caller-selected observer ``U=qy`` and its
process derivative ``Y=D(U)=vy``, exact elimination of the original Cartesian
assignments discovers

    Y^2 = (K - 2 U) (1 - U^2).

The familiar energy notation ``K=2E`` and genus-one language are classical
shadows added only after the relation has been discovered.

Calibration statement
---------------------
Passing this file certifies that, within a degree-two polynomial observer
budget and the declared algebraic constraints:

1. constraint preservation uniquely closes the radial multiplier;
2. bounded invariant discovery returns the nontrivial first integral
   ``vx^2+vy^2+2*qy`` without an energy template;
3. the derivative certificate vanishes exactly modulo the rod+tangency ideal;
4. the discovered invariant leaf plus ``U=qy`` produces the cubic quotient by
   exact elimination rather than by inserting the known pendulum formula;
5. the resulting generic hyperelliptic profile has genus one.

Proof map
---------
``closed_pendulum_process`` performs constraint closure.
``test_pendulum_discovers_energy_before_the_cubic_quotient`` checks steps 2-5.
The unit tests in ``tests/test_discovery.py`` separately check the generic
observer-basis, invariant-nullspace, and observable-elimination machinery.

Boundary
--------
This test does **not** yet discover that ``qy`` is the optimal observable. It is
selected from the available assignment-level observer candidates by the caller.
Nor does the test automatically choose the genus-one/Abelian function language
or compare it against competing presentations. Those are the next discovery
layers. The claim is narrower: the energy and reduced cubic are no longer
preloaded mathematical answers.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989.

[Cox-Little-OShea-2015] D. Cox, J. Little, D. O'Shea, *Ideals, Varieties, and
Algorithms*, 4th ed., Springer, 2015.

[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
"""

import sympy as sp

from aeg_shakespeare.analysis.algebraic import hyperelliptic_profile
from aeg_shakespeare.discovery import (
    discover_first_order_process_quotient,
    discover_polynomial_invariants,
)
from aeg_shakespeare.presentation.constraints import AlgebraicConstraintSet
from aeg_shakespeare.process.local import ProcessSystem


def closed_pendulum_process():
    """Close the primitive constrained process without supplying its energy."""

    qx, qy, vx, vy, lambda_ = sp.symbols("qx qy vx vy lambda")
    raw = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: lambda_ * qx,
            vy: -1 + lambda_ * qy,
        },
        name="D",
    )
    rod = qx**2 + qy**2 - 1
    tangent = sp.expand(raw.derive(rod) / 2)
    quotient_with_multiplier = AlgebraicConstraintSet(
        (qx, qy, vx, vy, lambda_),
        (rod, tangent),
    )
    tangent_rate = quotient_with_multiplier.reduce(raw.derive(tangent))
    solutions = sp.solve(sp.Eq(tangent_rate, 0), lambda_)
    assert len(solutions) == 1
    lambda_solution = solutions[0]

    closed = ProcessSystem(
        (qx, qy, vx, vy),
        {
            qx: vx,
            qy: vy,
            vx: sp.expand(lambda_solution * qx),
            vy: sp.expand(-1 + lambda_solution * qy),
        },
        name="D",
    )
    geometry = AlgebraicConstraintSet(
        (qx, qy, vx, vy),
        (rod, tangent),
    )
    return qx, qy, vx, vy, closed, geometry


def test_pendulum_discovers_energy_before_the_cubic_quotient():
    qx, qy, vx, vy, system, geometry = closed_pendulum_process()

    discovery = discover_polynomial_invariants(
        system,
        constraints=geometry,
        max_degree=2,
    )
    assert len(discovery.invariants) == 1
    invariant = discovery.invariants[0]
    assert invariant.certified
    assert geometry.reduce(
        invariant.expression - (vx**2 + vy**2 + 2 * qy)
    ) == 0

    K, U, Y = sp.symbols("K U Y")
    invariant_leaf = AlgebraicConstraintSet(
        (qx, qy, vx, vy, K),
        geometry.relations + (invariant.expression - K,),
    )
    quotient = discover_first_order_process_quotient(
        system,
        qy,
        observable_symbol=U,
        derivative_symbol=Y,
        constraints=invariant_leaf,
        parameters=(K,),
    )

    assert quotient.complete_certificates
    assert len(quotient.relations) == 1
    discovered_relation = quotient.relations[0].relation
    expected_relation = sp.expand(
        Y**2 - (K - 2 * U) * (1 - U**2)
    )
    ratio = sp.cancel(discovered_relation / expected_relation)
    assert ratio != 0
    assert not ratio.free_symbols

    # CLASSICAL SHADOW: only now classify the discovered cubic.
    profile = hyperelliptic_profile(
        U,
        Y,
        sp.expand((K - 2 * U) * (1 - U**2)),
    )
    assert profile.degree == 3
    assert profile.generic_genus == 1
    assert profile.generically_smooth

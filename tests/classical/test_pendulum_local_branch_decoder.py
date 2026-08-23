"""Simple pendulum: a branch bit locally reconstructs the Cartesian flow.

Retrieval
---------
Problem: local reconstruction of the planar simple pendulum from its reduced
elliptic carrier.
Domains: constrained mechanics, algebraic curves, local decoding, dynamical
systems.
Classical names / aliases: simple pendulum, energy curve, elliptic reduction,
reflection branch, local inverse.
Process Geometry roles: observable quotient, decoder, reconstruction contract,
flow intertwining, branch locus.
Prerequisites: the quotient-fiber vignette
``test_pendulum_observable_quotient_fiber.py``.
Related entry: ``docs/vignettes/simple-pendulum.md``.
Theory Map relation: strengthens an existing reconstruction boundary; no new
Theory Map node and no generic decoder API.

Problem statement
-----------------
The pendulum observable quotient keeps

    U = qy,
    Y = vy,

and satisfies

    Y^2 = 2(E-U)(1-U^2).

The preceding quotient-fiber vignette proves that this representation forgets
the simultaneous sign of ``(qx,vx)``.  Is that the *only* missing local state
data away from the vertical configurations ``qx=0``?  Equivalently, can one
additional branch sign reconstruct the full Cartesian state and its vector
field?

Why this problem is here
------------------------
Saying that a quotient is generically two-to-one is weaker than giving a
working decoder.  A Process Geometry representation should state not only what
it forgets but, when possible, what additional data make reconstruction
possible and whether the reconstructed state follows the original process.

This vignette therefore tests a local decoder rather than introducing a package
abstraction.

Primitive data
--------------
The decoder receives only

    (U, Y, E, sigma),

where ``sigma`` is either ``+1`` or ``-1`` and the reduced variables satisfy the
cubic above.  On the open set

    1-U^2 != 0,

set

    r  = sqrt(1-U^2),
    qx = sigma*r,
    qy = U,
    vy = Y,
    vx = -sigma*U*Y/r.

No angle variable, elliptic function, previous Cartesian state, or hidden
velocity sign is supplied separately.

Classical lineage
-----------------
Solving a quotient map locally requires choosing a sheet/branch away from its
ramification or singular reconstruction locus.  Here the elementary circle
constraint already gives ``qx=+/-sqrt(1-qy^2)``; tangency then fixes ``vx`` once
the same branch is chosen.  Standard pendulum mechanics is described in
[Arnold-1989].

Process Geometry reconstruction
-------------------------------
The reduced curve carries its own rational vector field.  If

    P(U)=2(E-U)(1-U^2),

then differentiating ``Y^2=P(U)`` along a nonstationary branch gives

    D U = Y,
    D Y = P'(U)/2 = 3U^2 - 2EU - 1.

The closed Cartesian pendulum on the same energy leaf has multiplier

    lambda = qy - (vx^2+vy^2) = 3U - 2E.

The test applies the reduced derivative to all four decoded Cartesian
coordinates and verifies, modulo ``Y^2=P(U)``, that

    D q = v,
    D v = -e_y + lambda q.

Thus the local decoder does more than satisfy the static rod/energy equations:
it intertwines the reduced flow with the original Cartesian flow.

Calibration statement
---------------------
Passing this file certifies, on the localization ``1-U^2 != 0``, that:

1. either branch ``sigma=+/-1`` reconstructs a state satisfying rod, tangency,
   and energy exactly modulo the reduced cubic;
2. changing ``sigma`` applies precisely the hidden ``Z2`` involution from the
   quotient-fiber vignette;
3. the reduced vector field is ``DU=Y`` and ``DY=3U^2-2EU-1``;
4. the decoded coordinates satisfy the full closed Cartesian pendulum vector
   field modulo the reduced cubic;
5. no second independent hidden sign is needed locally: once ``qx``'s branch is
   chosen, tangency fixes ``vx``.

Proof map
---------
``test_each_branch_reconstructs_the_static_cartesian_constraints`` checks items
1-2 and 5.
``test_local_decoder_intertwines_reduced_and_cartesian_flows`` checks items 3-4.
``test_vertical_configurations_are_an_explicit_decoder_boundary`` records the
localization boundary used by both proofs.

Boundary and reconstruction
---------------------------
The formula is deliberately local.  At ``U=+/-1`` one has ``qx=0`` and the
expression ``vx=-UY/qx`` becomes ``0/0`` on the reduced curve.  Those fibers
must be treated by continuation, a different chart, or explicit history data.
The test does not choose how the branch sign should be transported through such
points.

The vignette also does not invert the Abelian integral, restore dimensional
physical time, reconstruct an A/M lift history, or establish task-universal
sufficiency.  It proves only the exact local state-and-flow decoder on the
stated open set.

References and onward links
---------------------------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.

Continue with ``test_pendulum_period_history.py`` for the Abelian clock and
``docs/vignettes/simple-pendulum.md`` for the family-level reconstruction map.
"""

from __future__ import annotations

import sympy as sp


def _reduced_pendulum():
    U, Y, E = sp.symbols("U Y E")
    polynomial = sp.expand(2 * (E - U) * (1 - U**2))
    dY = sp.expand(sp.diff(polynomial, U) / 2)

    def derive(expression):
        return sp.expand(
            sp.diff(expression, U) * Y
            + sp.diff(expression, Y) * dY
        )

    return U, Y, E, polynomial, dY, derive


def _decoded_state(U, Y, sigma: int):
    assert sigma in (-1, 1)
    radius = sp.sqrt(1 - U**2)
    qx = sigma * radius
    qy = U
    vx = -sigma * U * Y / radius
    vy = Y
    return qx, qy, vx, vy


def _on_curve(expression, Y, polynomial):
    """Reduce expressions that are affine in Y^2 modulo Y^2=P(U)."""

    return sp.simplify(sp.factor(expression).subs(Y**2, polynomial))


def test_each_branch_reconstructs_the_static_cartesian_constraints():
    U, Y, E, polynomial, _, _ = _reduced_pendulum()

    decoded = {}
    for sigma in (-1, 1):
        qx, qy, vx, vy = _decoded_state(U, Y, sigma)
        decoded[sigma] = (qx, qy, vx, vy)

        rod = sp.expand(qx**2 + qy**2 - 1)
        tangent = sp.simplify(qx * vx + qy * vy)
        energy = sp.together(vx**2 + vy**2 - 2 * (E - qy))

        assert sp.simplify(rod) == 0
        assert tangent == 0
        assert _on_curve(energy, Y, polynomial) == 0

        # Tangency has no second independent sign once the qx branch is fixed.
        assert sp.simplify(vx + qy * vy / qx) == 0

    negative = decoded[-1]
    positive = decoded[1]
    assert sp.simplify(negative[0] + positive[0]) == 0
    assert sp.simplify(negative[1] - positive[1]) == 0
    assert sp.simplify(negative[2] + positive[2]) == 0
    assert sp.simplify(negative[3] - positive[3]) == 0


def test_local_decoder_intertwines_reduced_and_cartesian_flows():
    U, Y, E, polynomial, dY, derive = _reduced_pendulum()

    assert sp.expand(dY - (3 * U**2 - 2 * E * U - 1)) == 0

    for sigma in (-1, 1):
        qx, qy, vx, vy = _decoded_state(U, Y, sigma)
        multiplier = 3 * U - 2 * E

        # Dq=v follows directly from the branch decoder and DU=Y.
        assert sp.simplify(derive(qy) - vy) == 0
        assert sp.simplify(derive(qx) - vx) == 0

        # The vertical acceleration already closes polynomially on the reduced
        # carrier; the horizontal one closes after using Y^2=P(U).
        vertical = sp.expand(derive(vy) - (-1 + multiplier * qy))
        horizontal = sp.together(derive(vx) - multiplier * qx)
        assert sp.simplify(vertical) == 0
        assert _on_curve(horizontal, Y, polynomial) == 0


def test_vertical_configurations_are_an_explicit_decoder_boundary():
    U, Y, E, polynomial, _, _ = _reduced_pendulum()

    # U=+/-1 are roots of the observable cubic, hence Y=0 there.  They are
    # exactly the configurations qx=0 where the local tangency decoder divides
    # by qx and must be replaced by continuation or another chart.
    assert sp.simplify(polynomial.subs(U, 1)) == 0
    assert sp.simplify(polynomial.subs(U, -1)) == 0

    for sigma in (-1, 1):
        qx, _, vx, _ = _decoded_state(U, Y, sigma)
        assert sp.simplify(qx.subs(U, 1)) == 0
        assert sp.denom(sp.together(vx)).subs(U, 1) == 0
        assert sp.simplify(qx.subs(U, -1)) == 0
        assert sp.denom(sp.together(vx)).subs(U, -1) == 0

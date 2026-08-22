"""Pendulum discovery III: the primitive geometry proposes its scalar observers.

Question
--------
Can Shakespeare stop being handed the coordinate family ``(qx,qy)`` and instead
construct candidate scalar observers from a smaller piece of primitive geometry?

Primitive data
--------------
This vignette begins after the previous two pendulum discovery stages.  It
receives the already-certified Cartesian process and invariant leaf

    vx^2 + vy^2 + 2 qy = K.

But it no longer receives ``qx`` and ``qy`` as the observer family.  Instead it
receives three named pairable atoms

    q = (qx,qy),   v = (vx,vy),   e = (0,1)

and one caller-declared Euclidean pairing ``pair(-,-)`` on that common sort.
The pairing is permitted to lower a structured recipe to a scalar polynomial
backend expression.

No vector-space addition law, scalar multiplication, basis-change theorem,
angle coordinate, preferred component, energy formula, elliptic function, or
target cubic is supplied by this stage.

Classical lineage
-----------------
The Euclidean planar pendulum is conventionally described using the position
and velocity vectors together with a fixed gravity direction.  Their scalar
products provide coordinate-free observables such as height, speed squared,
and tangency.  See [Arnold-1989].  Exact elimination below uses the algebraic
machinery represented by [Cox-Little-OShea-2015].

Shakespeare reconstruction
---------------------------
The point of the vignette is deliberately smaller than a theory of vector
spaces.  The structured layer knows only that ``q``, ``v``, and ``e`` may be
paired and that the pairing is symmetric.  It therefore proposes the six
depth-one scalar constructions

    pair(q,q), pair(q,v), pair(q,e),
    pair(v,v), pair(v,e), pair(e,e).

Their scalar backend shadows are generated only afterwards.  On the declared
leaf, the constructions ``pair(q,q)``, ``pair(q,v)``, and ``pair(e,e)`` are
stationary and are therefore insufficient for the narrow task of finding an
evolving one-dimensional observer; they remain valid constructions and are not
erased from the proposal set.

The surviving proposals are sent unchanged into the existing first-order
quotient/Pareto search.  The construction ``pair(q,e)`` lowers to ``qy`` and
produces

    Y^2 = (K - 2 U) (1 - U^2).

The competing speed-squared and vertical-velocity constructions also close
algebraically, but carry more expensive backend grammar and/or relations.  Thus
``pair(q,e)`` becomes the unique default Pareto presentation without the caller
naming ``qy``.

Calibration statement
---------------------
Passing this file certifies that:

1. one declared pairing on the structured atoms ``q,v,e`` generates six
   construction-history-preserving scalar proposals;
2. task filtering removes only stationary candidates from *this search task*,
   not from construction identity;
3. the three surviving observers are all evaluated by exact quotient search;
4. ``pair(q,e)`` is the unique default Pareto candidate;
5. its lowering is ``qy`` and its quotient relation is the previously discovered
   genus-one cubic, up to a nonzero scalar multiple.

Proof map
---------
``test_structured_pairing_proposals_select_gravity_observer`` executes the full
structured atom -> pairing construction -> task filter -> quotient -> cost ->
Pareto chain.  Generic pairing behavior is tested separately in
``tests/test_structured_observers.py``.

New reusable abstraction
-------------------------
The only new reusable structure introduced by this vignette is a depth-one
pairing proposal with an explicit construction recipe and a separate scalar
backend lowering.  It is intentionally *not* generalized into a vector-space or
mathematical-theory protocol.

Unresolved manual choice
------------------------
The Euclidean pairing itself, the common pairable sort, and the decomposition of
primitive data into the structured atoms ``q``, ``v``, and ``e`` remain
caller-supplied.  Later examples must decide which of these assumptions deserves
promotion into a broader reusable abstraction.

Boundary
--------
This test does not derive vector-space axioms, bilinearity, positivity, Fourier
analysis, spectral theory, or a general typed construction language.  It also
does not prove that the default structural cost is canonical.  Those questions
are intentionally deferred until independent examples require them.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989.

[Cox-Little-OShea-2015] D. Cox, J. Little, D. O'Shea, *Ideals, Varieties, and
Algorithms*, 4th ed., Springer, 2015.
"""

import sympy as sp

from aeg_shakespeare.discovery import (
    PairableAtom,
    euclidean_pairing,
    generate_pairing_observers,
    nonstationary_observer_proposals,
    search_first_order_process_quotients,
)
from aeg_shakespeare.presentation.constraints import AlgebraicConstraintSet
from aeg_shakespeare.process.local import ProcessSystem


def _same_relation_up_to_scalar(left, right):
    ratio = sp.cancel(sp.expand(left) / sp.expand(right))
    return ratio != 0 and not ratio.free_symbols


def test_structured_pairing_proposals_select_gravity_observer():
    qx, qy, vx, vy, K = sp.symbols("qx qy vx vy K")
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
    leaf = AlgebraicConstraintSet(
        (qx, qy, vx, vy, K),
        (
            qx**2 + qy**2 - 1,
            qx * vx + qy * vy,
            vx**2 + vy**2 + 2 * qy - K,
        ),
    )

    proposals = generate_pairing_observers(
        (
            PairableAtom("q", (qx, qy), sort="plane"),
            PairableAtom("v", (vx, vy), sort="plane"),
            PairableAtom("e", (0, 1), sort="plane"),
        ),
        euclidean_pairing(sort="plane"),
    )
    assert [item.construction.recipe() for item in proposals.proposals] == [
        "pair(q,q)",
        "pair(q,v)",
        "pair(q,e)",
        "pair(v,v)",
        "pair(v,e)",
        "pair(e,e)",
    ]

    dynamic = nonstationary_observer_proposals(
        system,
        proposals.proposals,
        constraints=leaf,
    )
    assert [item.construction.recipe() for item in dynamic] == [
        "pair(q,e)",
        "pair(v,v)",
        "pair(v,e)",
    ]

    search = search_first_order_process_quotients(
        system,
        tuple(item.expression for item in dynamic),
        constraints=leaf,
        parameters=(K,),
    )
    assert len(search.evaluated) == 3
    assert all(candidate.sufficient for candidate in search.evaluated)
    assert len(search.pareto) == 1

    winner = search.pareto[0]
    assert sp.expand(winner.payload.observable - qy) == 0
    structured_winner = next(
        item
        for item in dynamic
        if sp.expand(item.expression - winner.payload.observable) == 0
    )
    assert structured_winner.construction.recipe() == "pair(q,e)"

    relation = winner.payload.quotient.relations[0].relation
    U, Y = winner.payload.quotient.symbols
    expected = sp.expand(Y**2 - (K - 2 * U) * (1 - U**2))
    assert _same_relation_up_to_scalar(relation, expected)

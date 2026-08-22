"""Pendulum discovery II: choose a quotient observer by presentation cost.

Question
--------
Once the pendulum invariant leaf has been discovered, can Shakespeare stop
being told that the gravity-aligned coordinate ``q_y`` is the preferred reduced
observer?

Primitive data
--------------
This vignette begins one stage later than
``test_pendulum_discovery_layer.py``. It receives the already-certified closed
Cartesian pendulum process, the rod/tangency geometry, and the discovered
first-integral leaf

    vx^2 + vy^2 + 2 qy = K.

The candidate family is only the two primitive position components

    qx, qy.

No preference between them, no angle coordinate, and no target cubic equation
is supplied.

Classical lineage
-----------------
Classically the vertical coordinate is natural because gravity singles out a
direction and energy reduction makes the pendulum quadrature especially simple
in that coordinate. See [Arnold-1989]. Algebraic elimination is performed with
the exact Groebner machinery represented by [Cox-Little-OShea-2015].

Shakespeare reconstruction
---------------------------
For every candidate observer ``F`` the library constructs the first process jet

    (U,Y) = (F,D F),

eliminates the Cartesian source assignments on the invariant leaf, retains the
exact pullback certificate, and evaluates the resulting presentation with the
same multi-axis ``PresentationCost`` used elsewhere in Shakespeare.

The baseline cost keeps observer grammar and relation complexity separate. For
both ``qx`` and ``qy`` the observer/first-jet grammar has the same structural
cost. The difference appears in the algebraic closure relation: ``qy`` yields
the cubic

    Y^2 = (K - 2 U) (1 - U^2),

whereas ``qx`` closes only through a substantially larger relation containing
terms through degree six. Therefore the gravity-aligned observer Pareto-
dominates the horizontal one under the transparent default structural cost.

Calibration statement
---------------------
Passing this file certifies that:

1. both primitive position components admit exact first-order algebraic closure
   on the discovered invariant leaf;
2. the search evaluates both rather than silently discarding the larger one;
3. the two candidates have equal baseline observer-grammar/history costs;
4. ``qy`` has strictly lower relation cost and is the unique Pareto candidate;
5. the winning relation is exactly the previously discovered genus-one cubic,
   up to a nonzero scalar multiple.

Proof map
---------
``test_position_observer_search_selects_gravity_coordinate`` executes the full
candidate -> quotient -> cost -> Pareto chain. Generic search behavior is
checked separately in ``tests/test_discovery_selection.py``.

Boundary
--------
The candidate family ``(qx,qy)`` is still supplied by the caller. Shakespeare
does not yet infer that these two assignments form a position vector, nor does
it automatically generate observer families from primitive geometric
operations such as inner product with the distinguished gravity direction.
Thus this vignette removes *which position component* to choose, but not *which
observer grammar* should be proposed. That is the next objectification layer.

The default relation cost is also a transparent proxy, not a theorem that lower
polynomial degree/support is optimal for every task. Different downstream tasks
may replace the cost model.

References
----------
[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Springer, 1989.

[Cox-Little-OShea-2015] D. Cox, J. Little, D. O'Shea, *Ideals, Varieties, and
Algorithms*, 4th ed., Springer, 2015.
"""

import sympy as sp

from aeg_shakespeare.discovery import search_first_order_process_quotients
from aeg_shakespeare.presentation.constraints import AlgebraicConstraintSet
from aeg_shakespeare.process.local import ProcessSystem


def _same_relation_up_to_scalar(left, right):
    ratio = sp.cancel(sp.expand(left) / sp.expand(right))
    return ratio != 0 and not ratio.free_symbols


def test_position_observer_search_selects_gravity_coordinate():
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
    rod = qx**2 + qy**2 - 1
    tangent = qx * vx + qy * vy
    discovered_invariant_leaf = vx**2 + vy**2 + 2 * qy - K
    leaf = AlgebraicConstraintSet(
        (qx, qy, vx, vy, K),
        (rod, tangent, discovered_invariant_leaf),
    )

    search = search_first_order_process_quotients(
        system,
        (qx, qy),
        constraints=leaf,
        parameters=(K,),
    )

    assert len(search.evaluated) == 2
    horizontal, vertical = search.evaluated
    assert horizontal.sufficient and vertical.sufficient
    assert horizontal.cost.grammar == vertical.cost.grammar
    assert horizontal.cost.history == vertical.cost.history == 1.0
    assert vertical.cost.relations < horizontal.cost.relations

    assert len(search.pareto) == 1
    winner = search.pareto[0]
    assert sp.expand(winner.payload.observable - qy) == 0

    relation = winner.payload.quotient.relations[0].relation
    U, Y = winner.payload.quotient.symbols
    expected = sp.expand(Y**2 - (K - 2 * U) * (1 - U**2))
    assert _same_relation_up_to_scalar(relation, expected)

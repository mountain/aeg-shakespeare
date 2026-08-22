import sympy as sp

from aeg_shakespeare.discovery import (
    PairableAtom,
    euclidean_pairing,
    generate_pairing_observers,
    nonstationary_observer_proposals,
)
from aeg_shakespeare.presentation.constraints import AlgebraicConstraintSet
from aeg_shakespeare.process.local import ProcessSystem


def test_pairing_observers_preserve_structured_recipes_before_lowering():
    qx, qy, vx, vy = sp.symbols("qx qy vx vy")
    atoms = (
        PairableAtom("q", (qx, qy), sort="plane"),
        PairableAtom("v", (vx, vy), sort="plane"),
        PairableAtom("e", (0, 1), sort="plane"),
    )
    result = generate_pairing_observers(
        atoms,
        euclidean_pairing(sort="plane"),
    )

    assert not result.rejected
    assert [proposal.construction.recipe() for proposal in result.proposals] == [
        "pair(q,q)",
        "pair(q,v)",
        "pair(q,e)",
        "pair(v,v)",
        "pair(v,e)",
        "pair(e,e)",
    ]
    assert [proposal.expression for proposal in result.proposals] == [
        qx**2 + qy**2,
        qx * vx + qy * vy,
        qy,
        vx**2 + vy**2,
        vy,
        sp.Integer(1),
    ]


def test_pairing_does_not_assume_cross_sort_compatibility():
    x = sp.symbols("x")
    result = generate_pairing_observers(
        (
            PairableAtom("left", (x,), sort="left"),
            PairableAtom("right", (x,), sort="right"),
        ),
        euclidean_pairing(sort="left"),
    )

    assert [proposal.construction.recipe() for proposal in result.proposals] == [
        "pair(left,left)"
    ]
    assert result.rejected == (
        "right: sort 'right' is incompatible with pairing sort 'left'",
    )


def test_nonstationary_filter_is_task_specific_not_a_construction_quotient():
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
    ).proposals

    dynamic = nonstationary_observer_proposals(
        system,
        proposals,
        constraints=leaf,
    )

    assert {proposal.construction.recipe() for proposal in dynamic} == {
        "pair(q,e)",
        "pair(v,v)",
        "pair(v,e)",
    }
    assert len(proposals) == 6  # stationary histories were not erased

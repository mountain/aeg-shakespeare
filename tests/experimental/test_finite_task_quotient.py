"""Exact finite H1/V1 calibration against bounded future signatures.

The experimental quotient should do something the existing bounded
``TaskContinuationSignature`` deliberately cannot do: refine until all finite
continuations are accounted for and return a minimal deterministic task
presentation with explicit distinguishing witnesses.
"""

import pytest

from process_geometry.experimental import minimize_finite_task_process
from process_geometry.presentation.history import (
    signatures_equivalent,
    task_continuation_signature,
)


STATES = ("x", "x-copy", "y", "u", "v", "accept")
STEPS = ("tick",)


def transition(state: str, step: str) -> str:
    assert step == "tick"
    return {
        "x": "u",
        "x-copy": "u",
        "y": "v",
        "u": "accept",
        "v": "v",
        "accept": "accept",
    }[state]


def observe(state: str) -> bool:
    return state == "accept"


def run_class(quotient, class_index: int, continuation: tuple[str, ...]) -> int:
    current = class_index
    for step in continuation:
        current = quotient.transition_class(current, step)
    return current


def test_bounded_signature_can_miss_a_distinction_that_exact_quotient_finds():
    x_depth_one = task_continuation_signature(
        "x", STEPS, transition, observe, depth=1
    )
    y_depth_one = task_continuation_signature(
        "y", STEPS, transition, observe, depth=1
    )
    assert signatures_equivalent(x_depth_one, y_depth_one)

    quotient = minimize_finite_task_process(STATES, STEPS, transition, observe)

    x_class = quotient.class_of("x")
    y_class = quotient.class_of("y")
    assert x_class != y_class
    assert quotient.witness_between(x_class, y_class) == ("tick", "tick")


def test_exact_quotient_merges_states_by_future_semantics_not_identity():
    quotient = minimize_finite_task_process(STATES, STEPS, transition, observe)

    # Literal duplicates merge.
    assert quotient.class_of("x") == quotient.class_of("x-copy")

    # More importantly, y and v also merge: y first moves to v, and from then on
    # both remain forever task-silent. Their state identities and one-step
    # histories differ, but no future task observation can distinguish them.
    assert quotient.class_of("y") == quotient.class_of("v")

    # x is distinguishable from that silent class after two ticks; u is
    # distinguishable after one tick.
    assert quotient.class_of("x") != quotient.class_of("y")
    assert quotient.class_of("u") != quotient.class_of("v")
    assert quotient.class_count == 4


def test_every_distinct_quotient_pair_has_a_sound_future_witness():
    quotient = minimize_finite_task_process(STATES, STEPS, transition, observe)

    expected_pair_count = quotient.class_count * (quotient.class_count - 1) // 2
    assert len(quotient.distinguishing_witnesses) == expected_pair_count

    for witness in quotient.distinguishing_witnesses:
        left_end = run_class(quotient, witness.left_class, witness.continuation)
        right_end = run_class(quotient, witness.right_class, witness.continuation)
        assert (
            quotient.class_observations[left_end]
            != quotient.class_observations[right_end]
        )


def test_induced_transition_is_well_defined_on_merged_class():
    quotient = minimize_finite_task_process(STATES, STEPS, transition, observe)

    x_class = quotient.class_of("x")
    target_class = quotient.transition_class(x_class, "tick")
    assert target_class == quotient.class_of("u")
    assert quotient.class_of(transition("x", "tick")) == target_class
    assert quotient.class_of(transition("x-copy", "tick")) == target_class

    silent_class = quotient.class_of("y")
    assert quotient.transition_class(silent_class, "tick") == silent_class


def test_rejects_transition_that_leaves_declared_finite_carrier():
    with pytest.raises(ValueError, match="leaves declared state carrier"):
        minimize_finite_task_process(
            ("inside",),
            ("step",),
            lambda _state, _step: "outside",
            lambda _state: False,
        )

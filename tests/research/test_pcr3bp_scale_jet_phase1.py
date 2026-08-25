"""PCR3BP dimensional scale-jet and topology/coding audit."""

import importlib.util
import math
from pathlib import Path
import sys


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/pcr3bp-history-cost/phase1_scale_jet.py"
)
SPEC = importlib.util.spec_from_file_location("pcr3bp_scale_jet_phase1", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_dimensional_scale_coordinates_are_a_two_sheeted_local_chart():
    for state in (
        (0.25, 0.31, -0.42, 0.77),
        (0.25, -0.31, -0.42, 0.77),
    ):
        jet = module.scale_jet(state)
        reconstructed = module.reconstruct_state_from_scale_jet(jet)
        assert max(abs(left - right) for left, right in zip(state, reconstructed)) < 2.0e-14
        r1, r2 = module.radii_from_log_scales(jet.u1, jet.u2)
        assert min(module.scale_domain_residuals(r1, r2)) > 0.0

    state = (0.25, 0.31, -0.42, 0.77)
    beta = module.kepler_scale_rates(state)
    epsilon = 1.0e-7
    forward = module.kepler_log_scales_at_position(
        state[0] + epsilon * state[2],
        state[1] + epsilon * state[3],
    )
    backward = module.kepler_log_scales_at_position(
        state[0] - epsilon * state[2],
        state[1] - epsilon * state[3],
    )
    finite_difference = tuple(
        (right - left) / (2.0 * epsilon)
        for left, right in zip(backward, forward)
    )
    assert max(abs(left - right) for left, right in zip(beta, finite_difference)) < 2.0e-9


def test_fixed_jacobi_leaf_closes_the_scale_jet_at_a_gate():
    history = module.simulate_dimensional_history(
        module.phase0.InitialCondition("gate-reconstruction", -0.05, 80.0),
        history_budget=3,
        max_step=0.0005,
    )
    assert history.status == "history-budget"
    for event in history.events:
        reconstructed = module.reconstruct_state_from_scale_jet(
            event.scale_jet,
            jacobi=history.jacobi,
            normal_velocity_sign=event.normal_velocity_sign,
        )
        assert max(
            abs(left - right) for left, right in zip(event.state, reconstructed)
        ) < 2.0e-4


def test_closed_scale_odes_are_exact_but_deck_holonomy_is_nonabelian():
    loop_a = module.based_primary_loop(1, 1)
    loop_b = module.based_primary_loop(2, 1)
    assert module.gate_word_from_positions(loop_a) == "a"
    assert module.gate_word_from_positions(loop_b) == "b"
    assert max(abs(value) for value in module.closed_scale_increment(loop_a)) < 1.0e-15
    assert max(abs(value) for value in module.closed_scale_increment(loop_b)) < 1.0e-15

    word, matrix, scale_increment = module.commutator_calibration()
    assert word == "abAB"
    assert matrix == (13, 8, 8, 5)
    assert matrix != (1, 0, 0, 1)
    assert max(abs(value) for value in scale_increment) < 1.0e-15
    assert abs(module.phase0.hyperbolic_translation_length(matrix) - 2.0 * math.acosh(9.0)) < 1.0e-12


def test_word_prefix_is_not_a_continuation_stable_bellman_state():
    returning, continuing = module.prefix_continuation_red_team()
    assert returning.raw_word[:4] == continuing.raw_word[:4] == "aaaa"
    assert returning.raw_word[4] == "A"
    assert continuing.raw_word[4] == "a"
    assert abs(
        returning.events[4].cost_from_previous
        - continuing.events[4].cost_from_previous
    ) > 1.0
    assert max(returning.max_jacobi_error, continuing.max_jacobi_error) < 5.0e-7

    # Their local scale jets distinguish the hidden physical states before the
    # divergent fifth continuation; the prefix alone does not.
    left = returning.events[3].scale_jet
    right = continuing.events[3].scale_jet
    assert max(
        abs(a - b)
        for a, b in zip(
            (left.u1, left.u2, left.beta1, left.beta2),
            (right.u1, right.u2, right.beta1, right.beta2),
        )
    ) > 0.1

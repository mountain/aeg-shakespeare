"""Blind S2-prime normalization from bounded A/M-history jets."""

import importlib.util
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/moving-am-observer/am_history_jet_search.py"
)
SPEC = importlib.util.spec_from_file_location("am_history_jet_search", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_am_history_jet_obeys_addition_and_multiplication_rules():
    t = sp.Symbol("t", real=True)
    a_history, b_history, c_history = module.riccati_coefficient_histories()

    assert a_history.jet(t) == (t**2 + t, 2 * t + 1)
    assert b_history.jet(t) == (-2 * t - 1, -2)
    assert c_history.jet(t) == (1, 0)
    assert max(history.depth for history in (a_history, b_history, c_history)) == 3


def test_frozen_grammar_blindly_recovers_the_unique_oriented_moving_observer():
    t, y = sp.symbols("t y", real=True)
    result = module.blind_root_normalization_search(
        module.riccati_coefficient_histories()
    )

    assert (result.literal_candidate_count, result.semantic_candidate_count) == (24, 11)
    assert len(result.candidates) == 1
    candidate = result.candidates[0]
    assert (candidate.origin_value, candidate.scale_value) == (t, 1)
    assert (candidate.origin_rate, candidate.scale_rate) == (1, 0)
    assert candidate.observed == y**2 - y - 1
    assert candidate.reconstruction_residual == 0
    assert result.static_candidates == ()
    assert (result.fixed_variation, result.canonical_variation) == (2, 0)


def test_out_of_grammar_completion_payload_survives_blind_normalization():
    t, y = sp.symbols("t y", real=True)
    epsilon = sp.Symbol("epsilon", nonzero=True)
    result = module.blind_root_normalization_search(
        module.riccati_coefficient_histories(),
        cubic_perturbation=epsilon,
    )

    assert len(result.candidates) == 1
    candidate = result.candidates[0]
    assert sp.Poly(candidate.observed, y).coeff_monomial(y**3) == epsilon
    assert sp.Poly(candidate.observed, y).coeff_monomial(y**2) == 3 * epsilon * t + 1
    assert candidate.reconstruction_residual == 0

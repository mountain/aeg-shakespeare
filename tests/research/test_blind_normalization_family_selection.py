"""Held-out selection and ambiguity red teams for moving canonical observers."""

import importlib.util
import inspect
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/moving-am-observer/am_history_jet_search.py"
)
SPEC = importlib.util.spec_from_file_location("am_history_family_search", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_selector_has_no_expected_family_or_observer_oracle_input():
    parameters = inspect.signature(
        module.blind_normalization_family_selection
    ).parameters

    assert tuple(parameters) == (
        "coefficient_histories",
        "families",
        "observer_depth",
    )
    assert tuple(
        family.name for family in module.FROZEN_NORMALIZATION_FAMILIES
    ) == (
        "affine-root-unit",
        "quadratic-root-pair",
        "quadratic-vertex-unit",
    )


def test_held_out_affine_process_selects_the_affine_family_only():
    t, y = sp.symbols("t y", real=True)
    result = module.blind_normalization_family_selection(
        module.affine_coefficient_histories()
    )

    assert len(result.candidates) == 1
    candidate = result.best_candidates[0]
    assert candidate.family == "affine-root-unit"
    assert (candidate.origin_value, candidate.scale_value) == (t, 1)
    assert candidate.observed == y - 1
    assert candidate.reconstruction_residual == 0
    assert (result.fixed_variation, candidate.variation) == (1, 0)
    assert not result.ambiguous


def test_asymmetric_quadratic_selects_the_representable_root_family():
    result = module.blind_normalization_family_selection(
        module.riccati_coefficient_histories()
    )

    assert len(result.best_candidates) == 1
    assert result.best_candidates[0].family == "quadratic-root-pair"
    assert result.best_candidates[0].reconstruction_residual == 0
    assert (result.fixed_variation, result.best_candidates[0].variation) == (2, 0)


def test_centered_quadratic_exposes_equal_cost_canonicalization_ambiguity():
    t = sp.Symbol("t", real=True)
    result = module.blind_normalization_family_selection(
        module.centered_quadratic_histories()
    )

    assert result.ambiguous
    assert len(result.best_candidates) == 2
    assert {candidate.family for candidate in result.best_candidates} == {
        "quadratic-root-pair",
        "quadratic-vertex-unit",
    }
    assert {
        (candidate.origin_value, candidate.scale_value)
        for candidate in result.best_candidates
    } == {(t - 1, 2), (t, 1)}
    assert all(candidate.variation == 0 for candidate in result.best_candidates)
    assert all(
        candidate.reconstruction_residual == 0
        for candidate in result.best_candidates
    )


def test_cubic_completion_is_rejected_instead_of_silently_truncated():
    result = module.blind_normalization_family_selection(
        module.cubic_completion_histories()
    )

    assert result.candidates == ()
    assert result.best_candidates == ()
    assert not result.ambiguous

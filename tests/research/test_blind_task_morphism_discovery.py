"""Discover task-preserving presentation morphisms without a chart oracle."""

import importlib.util
import inspect
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/moving-am-observer/am_history_jet_search.py"
)
SPEC = importlib.util.spec_from_file_location("blind_task_morphism", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def _centered_pair(observer_depth=1):
    result = module.blind_normalization_family_selection(
        module.centered_quadratic_histories(),
        observer_depth=observer_depth,
    )
    candidates = {
        candidate.family: candidate for candidate in result.best_candidates
    }
    return result, (
        candidates["quadratic-root-pair"],
        candidates["quadratic-vertex-unit"],
    )


def test_morphism_search_has_no_expected_map_input():
    parameters = inspect.signature(module.blind_task_morphism_search).parameters
    assert tuple(parameters) == (
        "source",
        "target",
        "physical_sections",
        "morphism_depth",
    )


def test_bounded_am_grammar_blindly_discovers_the_unique_task_morphism():
    t = sp.Symbol("t", real=True)
    _result, (source, target) = _centered_pair()
    search = module.blind_task_morphism_search(
        source,
        target,
        (t - 1, t + 1),
    )

    assert (search.grammar_literal_count, search.grammar_semantic_count) == (24, 11)
    assert len(search.candidates) == 1
    candidate = search.candidates[0]
    assert (candidate.scale, candidate.shift) == (2, -1)
    assert (candidate.scale_rate, candidate.shift_rate) == (0, 0)
    assert candidate.task_residuals == (0, 0)
    assert candidate.reconstruction_residual == 0
    assert candidate.dynamics_residual == 0


def test_corrupted_dynamics_cannot_pass_task_and_reconstruction_checks_alone():
    t, y = sp.symbols("t y", real=True)
    _result, (source, target) = _centered_pair()
    corrupted = module.FamilyCandidate(
        family=target.family,
        origin_value=target.origin_value,
        scale_value=target.scale_value,
        origin_rate=target.origin_rate,
        scale_rate=target.scale_rate,
        observed=target.observed + y,
        reconstruction_residual=target.reconstruction_residual,
        variation=target.variation,
    )
    search = module.blind_task_morphism_search(
        source,
        corrupted,
        (t - 1, t + 1),
    )

    assert search.candidates == ()


def test_task_quotient_is_stable_when_observer_grammar_grows_to_depth_two():
    shallow_result, shallow_pair = _centered_pair(observer_depth=1)
    deep_result, deep_pair = _centered_pair(observer_depth=2)
    deep_literal_count, deep_grammar = module.bounded_observer_grammar(max_depth=2)

    assert (deep_literal_count, len(deep_grammar)) == (156, 60)
    assert len(shallow_result.best_candidates) == 2
    assert len(deep_result.best_candidates) == 2
    assert {
        (candidate.family, candidate.origin_value, candidate.scale_value)
        for candidate in deep_result.best_candidates
    } == {
        (candidate.family, candidate.origin_value, candidate.scale_value)
        for candidate in shallow_result.best_candidates
    }
    assert len(module.task_equivalence_classes(shallow_pair)) == 1
    assert len(module.task_equivalence_classes(deep_pair)) == 1

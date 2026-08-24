"""The centered-quadratic minimum slice becomes one task-relative class."""

import importlib.util
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/moving-am-observer/am_history_jet_search.py"
)
SPEC = importlib.util.spec_from_file_location("am_history_task_quotient", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def _centered_candidates():
    result = module.blind_normalization_family_selection(
        module.centered_quadratic_histories()
    )
    return {
        candidate.family: candidate for candidate in result.best_candidates
    }


def test_equal_cost_lifts_are_exactly_clock_preserving_conjugate():
    candidates = _centered_candidates()
    root = candidates["quadratic-root-pair"]
    vertex = candidates["quadratic-vertex-unit"]
    certificate = module.certify_affine_chart_morphism(root, vertex)

    assert certificate.certified
    assert (certificate.scale, certificate.shift) == (2, -1)
    assert (certificate.scale_rate, certificate.shift_rate) == (0, 0)
    assert certificate.dynamics_residual == 0


def test_physical_stopping_sections_survive_the_chart_morphism():
    t = sp.Symbol("t", real=True)
    candidates = _centered_candidates()
    root = candidates["quadratic-root-pair"]
    vertex = candidates["quadratic-vertex-unit"]
    certificate = module.certify_affine_chart_morphism(root, vertex)
    sections = (t - 1, t + 1)

    root_sections = module.task_section_coordinates(root, sections)
    vertex_sections = module.task_section_coordinates(vertex, sections)
    assert root_sections == (0, 1)
    assert vertex_sections == (-1, 1)
    assert tuple(
        sp.expand(certificate.scale * value + certificate.shift)
        for value in root_sections
    ) == vertex_sections


def test_task_quotient_is_unique_although_coordinate_penalty_is_not_invariant():
    candidates = _centered_candidates()
    best = tuple(candidates.values())
    classes = module.task_equivalence_classes(best)

    assert len(classes) == 1
    assert len(classes[0]) == 2

    t = sp.Symbol("t", real=True)
    sections = (t - 1, t + 1)
    coordinate_penalties = {
        name: sum(
            value**2
            for value in module.task_section_coordinates(candidate, sections)
        )
        for name, candidate in candidates.items()
    }
    assert coordinate_penalties == {
        "quadratic-root-pair": 1,
        "quadratic-vertex-unit": 2,
    }
    # The unequal numbers cannot be a physical selection rule: the exact
    # task-preserving chart morphism maps the same two physical sections.

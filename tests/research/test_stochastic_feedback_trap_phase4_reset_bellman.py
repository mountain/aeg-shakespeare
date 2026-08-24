"""Execute the frozen dimensionful reset-Bellman closure gate."""

import importlib.util
from pathlib import Path
import sys

import pytest


MODULE_PATH = Path(__file__).parents[2] / "sonnet/stochastic-feedback-trap-first-passage/phase4_reset_bellman.py"
SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase4", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_transported_reset_bellman_value_and_unique_policy_are_chart_covariant():
    results = tuple(module.solve_reset_bellman(chart) for chart in module.CHARTS)
    reference = results[0]

    assert {result.optimal_action for result in results} == {"left-reset"}
    assert all(abs(result.optimal_value - reference.optimal_value) < 2.0e-5 for result in results)
    for result in results:
        assert [value.label for value in result.action_values] == ["left-reset", "center-reset", "right-reset"]
        assert all(abs(value.regenerative_value - reference.action_values[index].regenerative_value) < 5.0e-5 for index, value in enumerate(result.action_values))
        bellman_rhs = min(
            value.reset_time + value.mean_absorption_time + value.right_exit_probability * result.optimal_value
            for value in result.action_values
        )
        assert result.optimal_value == pytest.approx(bellman_rhs)
        ordered = sorted(value.regenerative_value for value in result.action_values)
        assert ordered[1] - ordered[0] > 0.006


def test_dimensionful_clock_scales_values_exactly_and_preserves_policy():
    result = module.solve_reset_bellman(module.CHARTS[1])
    physical = result.physical(length=3.0, speed=2.0)

    assert physical.optimal_action == result.optimal_action
    assert physical.optimal_value == pytest.approx(1.5 * result.optimal_value)
    for raw, scaled in zip(result.action_values, physical.action_values):
        assert scaled.regenerative_value == pytest.approx(1.5 * raw.regenerative_value)
        assert scaled.right_exit_probability == raw.right_exit_probability


def test_swapped_absorbing_labels_are_rejected_as_a_different_task():
    with pytest.raises(ValueError, match="retained task payload"):
        module.solve_reset_bellman(module.CHARTS[0], section_labels=("right", "left"))


def test_coordinate_distance_charging_breaks_action_value_covariance():
    results = tuple(module.solve_reset_bellman(chart, coordinate_distance_charge=True) for chart in module.CHARTS)
    left_values = [result.action_values[0].regenerative_value for result in results]

    assert max(left_values) - min(left_values) > 0.25

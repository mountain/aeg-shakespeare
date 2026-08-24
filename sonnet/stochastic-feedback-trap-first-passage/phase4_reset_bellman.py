"""Dimensionful regenerative Bellman closure over transported stopped tasks."""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys


_PHASE3_PATH = Path(__file__).with_name("phase3_first_passage.py")
_SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase3_for_bellman", _PHASE3_PATH)
assert _SPEC and _SPEC.loader
_phase3 = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _phase3
_SPEC.loader.exec_module(_phase3)

CHARTS = _phase3.CHARTS
EPSILON = _phase3.EPSILON


@dataclass(frozen=True)
class ResetAction:
    label: str
    reset_section: float
    reset_time: float


ACTIONS = (
    ResetAction("left-reset", -0.5, 0.25),
    ResetAction("center-reset", 0.0, 0.0),
    ResetAction("right-reset", 0.5, 0.25),
)


@dataclass(frozen=True)
class ActionValue:
    label: str
    mean_absorption_time: float
    right_exit_probability: float
    reset_time: float
    regenerative_value: float


@dataclass(frozen=True)
class BellmanResult:
    chart_name: str
    action_values: tuple[ActionValue, ...]
    optimal_action: str
    optimal_value: float

    def physical(self, *, length: float, speed: float) -> "BellmanResult":
        scale = length / speed
        scaled = tuple(ActionValue(
            value.label,
            scale * value.mean_absorption_time,
            value.right_exit_probability,
            scale * value.reset_time,
            scale * value.regenerative_value,
        ) for value in self.action_values)
        return BellmanResult(self.chart_name, scaled, self.optimal_action, scale * self.optimal_value)


def _backward_fields(chart, node_count: int = 401) -> tuple[list[float], list[float], list[float]]:
    source_nodes = [-1.0 + 2.0 * index / (node_count - 1) for index in range(node_count)]
    nodes = [chart.forward(u) for u in source_nodes]
    lower: list[float] = []
    diagonal: list[float] = []
    upper: list[float] = []
    for index in range(1, node_count - 1):
        left_step = nodes[index] - nodes[index - 1]
        right_step = nodes[index + 1] - nodes[index]
        u = source_nodes[index]
        first = chart.first(u)
        drift = first * (u * u - 2.0) + EPSILON * chart.second(u)
        variance = 2.0 * EPSILON * first * first
        d1 = (
            -right_step / (left_step * (left_step + right_step)),
            (right_step - left_step) / (left_step * right_step),
            left_step / (right_step * (left_step + right_step)),
        )
        d2 = (
            2.0 / (left_step * (left_step + right_step)),
            -2.0 / (left_step * right_step),
            2.0 / (right_step * (left_step + right_step)),
        )
        lower.append(drift * d1[0] + 0.5 * variance * d2[0])
        diagonal.append(drift * d1[1] + 0.5 * variance * d2[1])
        upper.append(drift * d1[2] + 0.5 * variance * d2[2])

    def solve(forcing: float, left_boundary: float, right_boundary: float) -> list[float]:
        rhs = [forcing] * (node_count - 2)
        rhs[0] -= lower[0] * left_boundary
        rhs[-1] -= upper[-1] * right_boundary
        interior = _phase3._solve_tridiagonal(lower[1:].copy(), diagonal.copy(), upper[:-1].copy(), rhs)
        return [left_boundary, *interior, right_boundary]

    mean_time = solve(-1.0, 0.0, 0.0)
    right_probability = solve(0.0, 0.0, 1.0)
    return source_nodes, mean_time, right_probability


def solve_reset_bellman(chart, *, coordinate_distance_charge: bool = False, section_labels: tuple[str, str] = ("left", "right")) -> BellmanResult:
    if section_labels != ("left", "right"):
        raise ValueError("absorbing labels are retained task payload, not chart data")
    source_nodes, mean_time, right_probability = _backward_fields(chart)
    values: list[ActionValue] = []
    for action in ACTIONS:
        index = min(range(len(source_nodes)), key=lambda i: abs(source_nodes[i] - action.reset_section))
        reset_time = action.reset_time
        if coordinate_distance_charge:
            reset_time = abs(chart.forward(action.reset_section) - chart.forward(0.0))
        success_probability = 1.0 - right_probability[index]
        regenerative = (reset_time + mean_time[index]) / success_probability
        values.append(ActionValue(
            action.label,
            mean_time[index],
            right_probability[index],
            reset_time,
            regenerative,
        ))
    optimum = min(values, key=lambda value: value.regenerative_value)
    return BellmanResult(chart.name, tuple(values), optimum.label, optimum.regenerative_value)


__all__ = ["ACTIONS", "CHARTS", "ActionValue", "BellmanResult", "ResetAction", "solve_reset_bellman"]

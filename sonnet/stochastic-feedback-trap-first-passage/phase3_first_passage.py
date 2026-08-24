"""Independent BVP and Monte Carlo checks for chart-covariant first passage."""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
import random


EPSILON = 0.25


@dataclass(frozen=True)
class OddCubicChart:
    linear: float
    cubic: float
    name: str

    def forward(self, u: float) -> float:
        return self.linear * u + self.cubic * u**3

    def first(self, u: float) -> float:
        return self.linear + 3.0 * self.cubic * u**2

    def second(self, u: float) -> float:
        return 6.0 * self.cubic * u

    def inverse(self, w: float) -> float:
        if self.cubic == 0.0:
            return w / self.linear
        # The declared charts have a positive derivative on the task interval.
        # Safeguarded Newton is therefore both unambiguous and much cheaper
        # than solving a symbolic cubic at every Monte Carlo step.
        u = max(-1.0, min(1.0, w / (self.linear + self.cubic)))
        for _ in range(8):
            u -= (self.forward(u) - w) / self.first(u)
            u = max(-1.0, min(1.0, u))
        return u


CHARTS = (
    OddCubicChart(1.0, 0.0, "u"),
    OddCubicChart(1.0, 1.0, "u+u^3"),
    OddCubicChart(2.0, 1.0, "2u+u^3"),
)


def _solve_tridiagonal(lower: list[float], diagonal: list[float], upper: list[float], rhs: list[float]) -> list[float]:
    for index in range(1, len(diagonal)):
        factor = lower[index - 1] / diagonal[index - 1]
        diagonal[index] -= factor * upper[index - 1]
        rhs[index] -= factor * rhs[index - 1]
    result = [0.0] * len(diagonal)
    result[-1] = rhs[-1] / diagonal[-1]
    for index in range(len(diagonal) - 2, -1, -1):
        result[index] = (rhs[index] - upper[index] * result[index + 1]) / diagonal[index]
    return result


def backward_bvp(chart: OddCubicChart, node_count: int, *, transported_nodes: bool) -> float:
    """Solve the target-chart backward equation on a nonuniform finite-difference grid."""

    if node_count < 5 or node_count % 2 == 0:
        raise ValueError("node_count must be odd and at least five")
    if transported_nodes:
        source_nodes = [-1.0 + 2.0 * index / (node_count - 1) for index in range(node_count)]
        nodes = [chart.forward(u) for u in source_nodes]
    else:
        left, right = chart.forward(-1.0), chart.forward(1.0)
        nodes = [left + (right - left) * index / (node_count - 1) for index in range(node_count)]
        source_nodes = [chart.inverse(w) for w in nodes]

    lower: list[float] = []
    diagonal: list[float] = []
    upper: list[float] = []
    rhs = [-1.0] * (node_count - 2)
    for index in range(1, node_count - 1):
        left_step = nodes[index] - nodes[index - 1]
        right_step = nodes[index + 1] - nodes[index]
        u = source_nodes[index]
        first = chart.first(u)
        drift = first * (u * u - 2.0) + EPSILON * chart.second(u)
        variance = 2.0 * EPSILON * first * first

        d1_left = -right_step / (left_step * (left_step + right_step))
        d1_mid = (right_step - left_step) / (left_step * right_step)
        d1_right = left_step / (right_step * (left_step + right_step))
        d2_left = 2.0 / (left_step * (left_step + right_step))
        d2_mid = -2.0 / (left_step * right_step)
        d2_right = 2.0 / (right_step * (left_step + right_step))
        lower.append(drift * d1_left + 0.5 * variance * d2_left)
        diagonal.append(drift * d1_mid + 0.5 * variance * d2_mid)
        upper.append(drift * d1_right + 0.5 * variance * d2_right)

    interior = _solve_tridiagonal(lower[1:], diagonal, upper[:-1], rhs)
    return interior[(node_count - 3) // 2]


@dataclass(frozen=True)
class MonteCarloEstimate:
    mean: float
    standard_error: float
    paths: int
    time_step: float


def monte_carlo_first_passage(chart: OddCubicChart, *, paths: int, time_step: float, seed: int) -> MonteCarloEstimate:
    """Evolve the transformed SDE directly, with chart-specific state and stopping sections."""

    rng = random.Random(seed)
    left, right = chart.forward(-1.0), chart.forward(1.0)
    noise_scale = sqrt(2.0 * EPSILON * time_step)
    samples: list[float] = []
    for _ in range(paths):
        w = chart.forward(0.0)
        elapsed = 0.0
        while left < w < right:
            u = chart.inverse(w)
            first = chart.first(u)
            transformed_drift = first * (u * u - 2.0) + EPSILON * chart.second(u)
            w += transformed_drift * time_step + first * noise_scale * rng.gauss(0.0, 1.0)
            elapsed += time_step
        samples.append(elapsed)
    mean = sum(samples) / paths
    variance = sum((sample - mean) ** 2 for sample in samples) / (paths - 1)
    return MonteCarloEstimate(mean, sqrt(variance / paths), paths, time_step)


def physical_time(dimensionless_value: float, *, length: float, speed: float) -> float:
    return (length / speed) * dimensionless_value


__all__ = ["CHARTS", "EPSILON", "MonteCarloEstimate", "OddCubicChart", "backward_bvp", "monte_carlo_first_passage", "physical_time"]

"""PCR3BP phase 1: dimensional scale jets, topology, and coding audit.

The two primary-centered Kepler clocks are used as local multiplicative
coordinates.  Their first process derivatives form a local observer jet.  The
topological word is still observed independently at dimension-selected boundary
rays, so the experiment can test rather than assume whether scale transport
already contains the lifted history.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
import math
from pathlib import Path
import sys
from typing import Iterable


def _load_phase0():
    name = "pcr3bp_history_cost_phase0_shared"
    if name in sys.modules:
        return sys.modules[name]
    path = Path(__file__).with_name("phase0_history_cost.py")
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


phase0 = _load_phase0()
State = phase0.State
Matrix2 = phase0.Matrix2


@dataclass(frozen=True)
class ScaleJet:
    """Two Kepler clock coordinates and their process rates."""

    u1: float
    u2: float
    beta1: float
    beta2: float
    sheet: int


@dataclass(frozen=True)
class ScaleGateEvent:
    time: float
    cost_from_previous: float
    symbol: str
    state: State
    scale_jet: ScaleJet
    normal_velocity_sign: int


@dataclass(frozen=True)
class DimensionalHistory:
    label: str
    jacobi: float
    initial_state: State
    events: tuple[ScaleGateEvent, ...]
    max_jacobi_error: float
    min_primary_distance: float
    status: str

    @property
    def raw_word(self) -> str:
        return "".join(event.symbol for event in self.events)

    @property
    def reduced_word(self) -> str:
        return phase0.reduce_word(self.raw_word)


def primary_masses(mu: float = phase0.DEFAULT_MU) -> tuple[float, float]:
    return 1.0 - mu, mu


def kepler_log_scales_at_position(
    x: float,
    y: float,
    mu: float = phase0.DEFAULT_MU,
) -> tuple[float, float]:
    """Return ``log(r_i**(3/2) / sqrt(m_i))`` for both primaries."""

    first, second = phase0.primary_positions(mu)
    mass1, mass2 = primary_masses(mu)
    r1 = math.hypot(x - first, y)
    r2 = math.hypot(x - second, y)
    if r1 == 0.0 or r2 == 0.0:
        raise ValueError("Kepler scale is singular at a collision")
    return (
        1.5 * math.log(r1) - 0.5 * math.log(mass1),
        1.5 * math.log(r2) - 0.5 * math.log(mass2),
    )


def kepler_scale_rates(
    state: State,
    mu: float = phase0.DEFAULT_MU,
) -> tuple[float, float]:
    """Evaluate the local multiplicative rates ``beta_i = Z log sigma_i``."""

    x, y, vx, vy = state
    first, second = phase0.primary_positions(mu)
    r1_squared = (x - first) ** 2 + y * y
    r2_squared = (x - second) ** 2 + y * y
    if r1_squared == 0.0 or r2_squared == 0.0:
        raise ValueError("Kepler scale rate is singular at a collision")
    return (
        1.5 * ((x - first) * vx + y * vy) / r1_squared,
        1.5 * ((x - second) * vx + y * vy) / r2_squared,
    )


def scale_jet(state: State, mu: float = phase0.DEFAULT_MU) -> ScaleJet:
    u1, u2 = kepler_log_scales_at_position(state[0], state[1], mu)
    beta1, beta2 = kepler_scale_rates(state, mu)
    sheet = 1 if state[1] > 0.0 else -1 if state[1] < 0.0 else 0
    return ScaleJet(u1, u2, beta1, beta2, sheet)


def radii_from_log_scales(
    u1: float,
    u2: float,
    mu: float = phase0.DEFAULT_MU,
) -> tuple[float, float]:
    mass1, mass2 = primary_masses(mu)
    return (
        mass1 ** (1.0 / 3.0) * math.exp(2.0 * u1 / 3.0),
        mass2 ** (1.0 / 3.0) * math.exp(2.0 * u2 / 3.0),
    )


def scale_domain_residuals(r1: float, r2: float) -> tuple[float, float]:
    """Triangle inequalities for two distances to primaries one unit apart."""

    return r1 + r2 - 1.0, 1.0 - abs(r1 - r2)


def reconstruct_state_from_scale_jet(
    jet: ScaleJet,
    *,
    mu: float = phase0.DEFAULT_MU,
    jacobi: float | None = None,
    normal_velocity_sign: int | None = None,
    tolerance: float = 1.0e-11,
) -> State:
    """Reconstruct the physical state from a local dimensional scale 1-jet.

    Off the primary axis the two radial rates recover both velocity components.
    On the axis their gradients are dependent; the fixed Jacobi leaf and the
    crossing orientation supply the missing normal component.
    """

    r1, r2 = radii_from_log_scales(jet.u1, jet.u2, mu)
    first, _second = phase0.primary_positions(mu)
    dx1 = 0.5 * (r1 * r1 - r2 * r2 + 1.0)
    x = first + dx1
    y_squared = r1 * r1 - dx1 * dx1
    if y_squared < -tolerance:
        raise ValueError("scale coordinates violate the triangle domain")
    if jet.sheet == 0 and abs(y_squared) <= tolerance:
        y_squared = 0.0
    y_abs = math.sqrt(max(0.0, y_squared))
    if y_abs > tolerance and jet.sheet == 0:
        raise ValueError("off-axis reconstruction requires an orientation sheet")
    y = math.copysign(y_abs, jet.sheet) if y_abs > tolerance else 0.0

    moment1 = (2.0 / 3.0) * jet.beta1 * r1 * r1
    moment2 = (2.0 / 3.0) * jet.beta2 * r2 * r2
    vx = moment1 - moment2
    if y_abs > tolerance:
        vy = (moment1 - dx1 * vx) / y
        return x, y, vx, vy

    if jacobi is None or normal_velocity_sign not in (-1, 1):
        raise ValueError(
            "axis reconstruction requires Jacobi value and normal velocity sign"
        )
    vy_squared = 2.0 * phase0.effective_potential(x, 0.0, mu) - jacobi - vx * vx
    if vy_squared < -tolerance:
        raise ValueError("scale jet and Jacobi leaf are inconsistent")
    vy = normal_velocity_sign * math.sqrt(max(0.0, vy_squared))
    return x, 0.0, vx, vy


def _interpolate_state(before: State, after: State, fraction: float) -> State:
    return tuple(
        left + fraction * (right - left)
        for left, right in zip(before, after)
    )  # type: ignore[return-value]


def _dimensional_gate_crossing(
    before: State,
    after: State,
    time: float,
    step: float,
    previous_event_time: float,
    mu: float,
) -> ScaleGateEvent | None:
    """Observe the two outward axis rays selected by the distance-scale domain."""

    y0 = before[1]
    y1 = after[1]
    crosses = (y0 < 0.0 <= y1) or (y1 < 0.0 <= y0)
    if not crosses or y0 == y1:
        return None
    fraction = -y0 / (y1 - y0)
    state = _interpolate_state(before, after, fraction)
    first, second = phase0.primary_positions(mu)
    upward = y1 > y0
    if state[0] < first:
        symbol = "A" if upward else "a"
    elif state[0] > second:
        symbol = "b" if upward else "B"
    else:
        return None
    event_time = time + fraction * step
    return ScaleGateEvent(
        time=event_time,
        cost_from_previous=event_time - previous_event_time,
        symbol=symbol,
        state=state,
        scale_jet=scale_jet(state, mu),
        normal_velocity_sign=1 if upward else -1,
    )


def simulate_dimensional_history(
    condition: phase0.InitialCondition,
    *,
    mu: float = phase0.DEFAULT_MU,
    jacobi: float = phase0.DEFAULT_JACOBI,
    history_budget: int = 8,
    max_time: float = 50.0,
    max_step: float = 0.002,
    min_step: float = 0.00005,
    collision_radius: float = 0.015,
    escape_radius: float = 4.0,
) -> DimensionalHistory:
    state = phase0.initial_state(
        condition.x,
        condition.velocity_angle_degrees,
        jacobi,
        mu,
    )
    initial = state
    initial_jacobi = phase0.jacobi_constant(state, mu)
    time = 0.0
    previous_event_time = 0.0
    events: list[ScaleGateEvent] = []
    min_distance = phase0._min_primary_distance(state, mu)
    max_jacobi_error = abs(initial_jacobi - jacobi)
    status = "time-limit"

    while time < max_time:
        distance = phase0._min_primary_distance(state, mu)
        min_distance = min(min_distance, distance)
        if distance <= collision_radius:
            status = "collision-guard"
            break
        if math.hypot(state[0], state[1]) >= escape_radius:
            status = "escape-guard"
            break
        scale = min(1.0, (distance / 0.12) ** 1.5)
        step = min(max_time - time, max(max_step * scale, min_step))
        following = phase0.rk4_step(state, step, mu)
        event = _dimensional_gate_crossing(
            state,
            following,
            time,
            step,
            previous_event_time,
            mu,
        )
        if event is not None:
            events.append(event)
            previous_event_time = event.time
            if len(events) == history_budget:
                status = "history-budget"
        state = following
        time += step
        min_distance = min(min_distance, phase0._min_primary_distance(state, mu))
        max_jacobi_error = max(
            max_jacobi_error,
            abs(phase0.jacobi_constant(state, mu) - initial_jacobi),
        )
        if status == "history-budget":
            break

    return DimensionalHistory(
        label=condition.label,
        jacobi=jacobi,
        initial_state=initial,
        events=tuple(events),
        max_jacobi_error=max_jacobi_error,
        min_primary_distance=min_distance,
        status=status,
    )


Point = tuple[float, float]


def _line_path(start: Point, end: Point, samples: int = 48) -> tuple[Point, ...]:
    return tuple(
        (
            start[0] + (end[0] - start[0]) * index / samples,
            start[1] + (end[1] - start[1]) * index / samples,
        )
        for index in range(samples + 1)
    )


def based_primary_loop(
    primary: int,
    orientation: int = 1,
    *,
    mu: float = phase0.DEFAULT_MU,
    radius: float = 0.2,
    circle_samples: int = 512,
    base: Point = (0.4, 0.4),
) -> tuple[Point, ...]:
    if primary not in (1, 2) or orientation not in (-1, 1):
        raise ValueError("primary must be 1/2 and orientation must be +/-1")
    center_x = phase0.primary_positions(mu)[primary - 1]
    angle0 = 0.0 if primary == 1 else math.pi
    start = (center_x + radius * math.cos(angle0), radius * math.sin(angle0))
    outward = _line_path(base, start)
    circle = tuple(
        (
            center_x + radius * math.cos(
                angle0 + orientation * 2.0 * math.pi * index / circle_samples
            ),
            radius * math.sin(
                angle0 + orientation * 2.0 * math.pi * index / circle_samples
            ),
        )
        for index in range(circle_samples + 1)
    )
    inward = _line_path(start, base)
    return outward + circle[1:] + inward[1:]


def concatenate_paths(paths: Iterable[tuple[Point, ...]]) -> tuple[Point, ...]:
    combined: list[Point] = []
    for path in paths:
        combined.extend(path if not combined else path[1:])
    return tuple(combined)


def gate_word_from_positions(
    path: tuple[Point, ...],
    mu: float = phase0.DEFAULT_MU,
) -> str:
    symbols: list[str] = []
    first, second = phase0.primary_positions(mu)
    for before, after in zip(path, path[1:]):
        y0, y1 = before[1], after[1]
        if not ((y0 < 0.0 <= y1) or (y1 < 0.0 <= y0)) or y0 == y1:
            continue
        fraction = -y0 / (y1 - y0)
        x = before[0] + fraction * (after[0] - before[0])
        upward = y1 > y0
        if x < first - 1.0e-12:
            symbols.append("A" if upward else "a")
        elif x > second + 1.0e-12:
            symbols.append("b" if upward else "B")
    return phase0.reduce_word(symbols)


def closed_scale_increment(
    path: tuple[Point, ...],
    mu: float = phase0.DEFAULT_MU,
) -> tuple[float, float]:
    start = kepler_log_scales_at_position(*path[0], mu)
    end = kepler_log_scales_at_position(*path[-1], mu)
    return end[0] - start[0], end[1] - start[1]


def commutator_calibration(mu: float = phase0.DEFAULT_MU) -> tuple[str, Matrix2, tuple[float, float]]:
    path = concatenate_paths(
        (
            based_primary_loop(1, 1, mu=mu),
            based_primary_loop(2, 1, mu=mu),
            based_primary_loop(1, -1, mu=mu),
            based_primary_loop(2, -1, mu=mu),
        )
    )
    word = gate_word_from_positions(path, mu)
    return word, phase0.deck_matrix(word), closed_scale_increment(path, mu)


def prefix_continuation_red_team() -> tuple[DimensionalHistory, DimensionalHistory]:
    """Two physical histories with prefix ``aaaa`` and different fifth edges."""

    first = simulate_dimensional_history(
        phase0.InitialCondition("same-prefix-return", -0.05, 60.0),
        history_budget=5,
        max_step=0.0005,
    )
    second = simulate_dimensional_history(
        phase0.InitialCondition("same-prefix-continue", -0.05, 80.0),
        history_budget=5,
        max_step=0.0005,
    )
    return first, second


def main() -> None:
    word, matrix, increment = commutator_calibration()
    print(
        "closed commutator:",
        f"word={word}",
        f"deck={matrix}",
        f"Delta_u={increment}",
    )
    for history in prefix_continuation_red_team():
        fifth = history.events[4]
        fourth_jet = history.events[3].scale_jet
        print(
            f"{history.label}: word={history.raw_word} "
            f"fifth_cost={fifth.cost_from_previous:.6f} "
            f"prefix4_jet=(u1={fourth_jet.u1:.6f}, "
            f"u2={fourth_jet.u2:.6f}, beta1={fourth_jet.beta1:.6f}, "
            f"beta2={fourth_jet.beta2:.6f}) "
            f"max|Delta C|={history.max_jacobi_error:.2e}"
        )


__all__ = [
    "DimensionalHistory",
    "ScaleGateEvent",
    "ScaleJet",
    "based_primary_loop",
    "closed_scale_increment",
    "commutator_calibration",
    "concatenate_paths",
    "gate_word_from_positions",
    "kepler_log_scales_at_position",
    "kepler_scale_rates",
    "prefix_continuation_red_team",
    "radii_from_log_scales",
    "reconstruct_state_from_scale_jet",
    "scale_domain_residuals",
    "scale_jet",
    "simulate_dimensional_history",
]


if __name__ == "__main__":
    main()

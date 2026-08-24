"""PCR3BP phase 0: lift physical trajectories to costed free-group histories.

The implementation deliberately keeps three measurements separate:

* the reduced word length in the branch-cut presentation of ``pi_1``;
* the translation length of the corresponding ``Gamma(2)`` deck element;
* the dimensionless physical clock ``n * Delta t`` (``n=1`` here).

Only the rotating-frame equations, the Jacobi task oracle, and two geometric
branch cuts are primitive inputs.  No symbolic itinerary is supplied to the
integrator.  The words are observed from the numerical trajectories.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
import json
import math
from typing import Iterable


State = tuple[float, float, float, float]
Matrix2 = tuple[int, int, int, int]


@dataclass(frozen=True)
class InitialCondition:
    label: str
    x: float
    velocity_angle_degrees: float


@dataclass(frozen=True)
class Crossing:
    time: float
    symbol: str
    x: float
    y: float


@dataclass(frozen=True)
class HistorySimulation:
    label: str
    jacobi_target: float
    initial_state: State
    elapsed_clock: float
    raw_word: str
    reduced_word: str
    deck_matrix: Matrix2
    hyperbolic_translation_length: float
    max_jacobi_error: float
    min_primary_distance: float
    status: str
    crossings: tuple[Crossing, ...]
    trajectory: tuple[tuple[float, float, float], ...]

    def summary(self) -> dict[str, object]:
        return {
            "label": self.label,
            "status": self.status,
            "clock": self.elapsed_clock,
            "raw_word": self.raw_word,
            "reduced_word": self.reduced_word,
            "word_length": len(self.reduced_word),
            "deck_matrix": self.deck_matrix,
            "hyperbolic_length": self.hyperbolic_translation_length,
            "max_jacobi_error": self.max_jacobi_error,
            "min_primary_distance": self.min_primary_distance,
        }


DEFAULT_MU = 0.1
DEFAULT_JACOBI = 3.55
DEFAULT_HISTORY_BUDGET = 12

DEFAULT_INITIAL_CONDITIONS = (
    InitialCondition("left-parabolic", 0.34, 90.0),
    InitialCondition("left-to-right", 0.20, 20.0),
    InitialCondition("mixed-1", 0.55, 100.0),
    InitialCondition("mixed-2", 0.60, 100.0),
    InitialCondition("mixed-3", 0.40, 160.0),
    InitialCondition("right-parabolic", 0.76, 90.0),
)


def primary_positions(mu: float = DEFAULT_MU) -> tuple[float, float]:
    return -mu, 1.0 - mu


def effective_potential(x: float, y: float, mu: float = DEFAULT_MU) -> float:
    first, second = primary_positions(mu)
    r1 = math.hypot(x - first, y)
    r2 = math.hypot(x - second, y)
    return 0.5 * (x * x + y * y) + (1.0 - mu) / r1 + mu / r2


def jacobi_constant(state: State, mu: float = DEFAULT_MU) -> float:
    x, y, vx, vy = state
    return 2.0 * effective_potential(x, y, mu) - vx * vx - vy * vy


def vector_field(state: State, mu: float = DEFAULT_MU) -> State:
    x, y, vx, vy = state
    first, second = primary_positions(mu)
    dx1 = x - first
    dx2 = x - second
    r1 = math.hypot(dx1, y)
    r2 = math.hypot(dx2, y)
    ax = 2.0 * vy + x - (1.0 - mu) * dx1 / r1**3 - mu * dx2 / r2**3
    ay = -2.0 * vx + y - (1.0 - mu) * y / r1**3 - mu * y / r2**3
    return vx, vy, ax, ay


def _add_scaled(state: State, tangent: State, scale: float) -> State:
    return tuple(value + scale * delta for value, delta in zip(state, tangent))  # type: ignore[return-value]


def rk4_step(state: State, step: float, mu: float = DEFAULT_MU) -> State:
    k1 = vector_field(state, mu)
    k2 = vector_field(_add_scaled(state, k1, 0.5 * step), mu)
    k3 = vector_field(_add_scaled(state, k2, 0.5 * step), mu)
    k4 = vector_field(_add_scaled(state, k3, step), mu)
    return tuple(
        value + step * (d1 + 2.0 * d2 + 2.0 * d3 + d4) / 6.0
        for value, d1, d2, d3, d4 in zip(state, k1, k2, k3, k4)
    )  # type: ignore[return-value]


def initial_state(
    x: float,
    velocity_angle_degrees: float,
    jacobi: float = DEFAULT_JACOBI,
    mu: float = DEFAULT_MU,
) -> State:
    speed_squared = 2.0 * effective_potential(x, 0.0, mu) - jacobi
    if speed_squared <= 0.0:
        raise ValueError("initial point is outside the Jacobi-allowed Hill region")
    angle = math.radians(velocity_angle_degrees)
    speed = math.sqrt(speed_squared)
    return x, 0.0, speed * math.cos(angle), speed * math.sin(angle)


def _ray_crossings(
    before: State,
    after: State,
    time: float,
    step: float,
    mu: float,
) -> tuple[Crossing, ...]:
    """Observe crossings of two upward cuts without assigning orbit labels."""

    x0, y0, _, _ = before
    x1, y1, _, _ = after
    if x0 == x1:
        return ()
    observed: list[tuple[float, Crossing]] = []
    cuts = (
        (primary_positions(mu)[0], "a", "A"),
        (primary_positions(mu)[1], "b", "B"),
    )
    for cut_x, positive, negative in cuts:
        crosses = (x0 < cut_x <= x1) or (x1 < cut_x <= x0)
        if not crosses:
            continue
        fraction = (cut_x - x0) / (x1 - x0)
        cut_y = y0 + fraction * (y1 - y0)
        if cut_y <= 0.0:
            continue
        symbol = positive if x1 > x0 else negative
        observed.append(
            (
                fraction,
                Crossing(time + fraction * step, symbol, cut_x, cut_y),
            )
        )
    observed.sort(key=lambda item: item[0])
    return tuple(crossing for _, crossing in observed)


INVERSE_SYMBOL = {"a": "A", "A": "a", "b": "B", "B": "b"}


def reduce_word(symbols: Iterable[str] | str) -> str:
    stack: list[str] = []
    for symbol in symbols:
        if symbol not in INVERSE_SYMBOL:
            raise ValueError(f"unknown free-group symbol: {symbol!r}")
        if stack and stack[-1] == INVERSE_SYMBOL[symbol]:
            stack.pop()
        else:
            stack.append(symbol)
    return "".join(stack)


DECK_GENERATORS: dict[str, Matrix2] = {
    "a": (1, 2, 0, 1),
    "A": (1, -2, 0, 1),
    "b": (1, 0, -2, 1),
    "B": (1, 0, 2, 1),
}


def _matrix_product(left: Matrix2, right: Matrix2) -> Matrix2:
    a, b, c, d = left
    e, f, g, h = right
    return a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h


def deck_matrix(word: str) -> Matrix2:
    matrix = (1, 0, 0, 1)
    for symbol in reduce_word(word):
        matrix = _matrix_product(matrix, DECK_GENERATORS[symbol])
    return matrix


def hyperbolic_translation_length(matrix: Matrix2) -> float:
    """Return the stable translation length of a PSL(2,R) deck element."""

    trace_half = abs(matrix[0] + matrix[3]) / 2.0
    if trace_half <= 1.0:
        return 0.0
    return 2.0 * math.acosh(trace_half)


def _min_primary_distance(state: State, mu: float) -> float:
    x, y, _, _ = state
    first, second = primary_positions(mu)
    return min(math.hypot(x - first, y), math.hypot(x - second, y))


def simulate_history(
    condition: InitialCondition,
    *,
    mu: float = DEFAULT_MU,
    jacobi: float = DEFAULT_JACOBI,
    history_budget: int = DEFAULT_HISTORY_BUDGET,
    max_time: float = 60.0,
    max_step: float = 0.001,
    min_step: float = 0.00005,
    collision_radius: float = 0.015,
    escape_radius: float = 4.0,
    sample_interval: float = 0.04,
) -> HistorySimulation:
    """Integrate until a fixed raw-history budget or a declared stop event.

    The fourth-order step is reduced near either primary according to the local
    Kepler time scale ``r**(3/2)``.  Conservation of the Jacobi integral remains
    an independent numerical oracle and is reported, not enforced.
    """

    state = initial_state(condition.x, condition.velocity_angle_degrees, jacobi, mu)
    initial = state
    initial_jacobi = jacobi_constant(initial, mu)
    time = 0.0
    min_distance = _min_primary_distance(state, mu)
    max_jacobi_error = abs(initial_jacobi - jacobi)
    crossings: list[Crossing] = []
    trajectory: list[tuple[float, float, float]] = [(0.0, state[0], state[1])]
    next_sample = sample_interval
    status = "time-limit"

    while time < max_time:
        distance = _min_primary_distance(state, mu)
        min_distance = min(min_distance, distance)
        if distance <= collision_radius:
            status = "collision-guard"
            break
        if math.hypot(state[0], state[1]) >= escape_radius:
            status = "escape-guard"
            break

        scale = min(1.0, (distance / 0.12) ** 1.5)
        step = min(max_time - time, max(max_step * scale, min_step))
        following = rk4_step(state, step, mu)
        new_crossings = _ray_crossings(state, following, time, step, mu)
        for crossing in new_crossings:
            crossings.append(crossing)
            if len(crossings) == history_budget:
                status = "history-budget"
                break

        state = following
        time += step
        min_distance = min(min_distance, _min_primary_distance(state, mu))
        max_jacobi_error = max(
            max_jacobi_error,
            abs(jacobi_constant(state, mu) - initial_jacobi),
        )
        if time >= next_sample or status == "history-budget":
            trajectory.append((time, state[0], state[1]))
            next_sample += sample_interval
        if status == "history-budget":
            break

    raw_word = "".join(crossing.symbol for crossing in crossings)
    reduced = reduce_word(raw_word)
    matrix = deck_matrix(reduced)
    elapsed = crossings[-1].time if crossings else time
    return HistorySimulation(
        label=condition.label,
        jacobi_target=jacobi,
        initial_state=initial,
        elapsed_clock=elapsed,
        raw_word=raw_word,
        reduced_word=reduced,
        deck_matrix=matrix,
        hyperbolic_translation_length=hyperbolic_translation_length(matrix),
        max_jacobi_error=max_jacobi_error,
        min_primary_distance=min_distance,
        status=status,
        crossings=tuple(crossings),
        trajectory=tuple(trajectory),
    )


def omega_x_on_axis(x: float, mu: float = DEFAULT_MU) -> float:
    first, second = primary_positions(mu)
    dx1 = x - first
    dx2 = x - second
    return x - (1.0 - mu) * dx1 / abs(dx1) ** 3 - mu * dx2 / abs(dx2) ** 3


def l1_x(mu: float = DEFAULT_MU, *, iterations: int = 100) -> float:
    """Locate the collinear point between the primaries by certified bracketing."""

    first, second = primary_positions(mu)
    left = first + 1.0e-8
    right = second - 1.0e-8
    f_left = omega_x_on_axis(left, mu)
    f_right = omega_x_on_axis(right, mu)
    if not (f_left < 0.0 < f_right):
        raise ValueError("L1 root is not bracketed")
    for _ in range(iterations):
        middle = 0.5 * (left + right)
        if omega_x_on_axis(middle, mu) < 0.0:
            left = middle
        else:
            right = middle
    return 0.5 * (left + right)


def l1_critical_jacobi(mu: float = DEFAULT_MU) -> float:
    point = l1_x(mu)
    return 2.0 * effective_potential(point, 0.0, mu)


def run_default_ensemble(**kwargs: object) -> tuple[HistorySimulation, ...]:
    return tuple(simulate_history(condition, **kwargs) for condition in DEFAULT_INITIAL_CONDITIONS)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit machine-readable summaries")
    parser.add_argument("--history-budget", type=int, default=DEFAULT_HISTORY_BUDGET)
    parser.add_argument("--max-step", type=float, default=0.001)
    args = parser.parse_args()
    results = run_default_ensemble(history_budget=args.history_budget, max_step=args.max_step)
    if args.json:
        print(json.dumps([result.summary() for result in results], indent=2))
        return
    print(f"mu={DEFAULT_MU} C={DEFAULT_JACOBI} C1={l1_critical_jacobi():.12f}")
    print("label               clock  word          |w|   ell_H   max|dC|   min(r_i)")
    for result in results:
        print(
            f"{result.label:18s} {result.elapsed_clock:6.3f}  "
            f"{result.reduced_word:12s} {len(result.reduced_word):3d}  "
            f"{result.hyperbolic_translation_length:6.3f}  "
            f"{result.max_jacobi_error:8.2e}  {result.min_primary_distance:8.4f}"
        )


if __name__ == "__main__":
    main()

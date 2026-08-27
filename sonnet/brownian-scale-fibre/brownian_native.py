"""Native finite-increment and endpoint-fibre calculations for issue #158."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Iterable


Point = tuple[int, ...]


class NativeBrownianDomainError(ValueError):
    """The first finite-increment Brownian grammar does not cover the input."""


class CenteringRequired(NativeBrownianDomainError):
    """A nonzero drift must be represented before fluctuation scaling."""

    def __init__(self, mean: Fraction):
        self.mean = mean
        super().__init__(f"centering-required: exact increment mean is {mean}")


class EndpointFibreBudgetError(RuntimeError):
    """The declared exact endpoint-fibre update budget was exhausted."""


@dataclass(frozen=True)
class FiniteIncrementLaw:
    support: tuple[int, ...]
    weights: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if not self.support:
            raise NativeBrownianDomainError("increment support must not be empty")
        if len(self.support) != len(self.weights):
            raise NativeBrownianDomainError("support and weight counts differ")
        if len(set(self.support)) != len(self.support):
            raise NativeBrownianDomainError("increment support must be unique")
        if any(
            not isinstance(value, int) or isinstance(value, bool)
            for value in self.support
        ):
            raise NativeBrownianDomainError("increment support must contain integers")
        if any(not isinstance(weight, Fraction) for weight in self.weights):
            raise NativeBrownianDomainError("increment weights must be exact fractions")
        if any(weight <= 0 for weight in self.weights):
            raise NativeBrownianDomainError("increment weights must be positive")
        if sum(self.weights, start=Fraction(0)) != 1:
            raise NativeBrownianDomainError("increment weights must sum exactly to one")

    @classmethod
    def symmetric_unit(cls) -> "FiniteIncrementLaw":
        return cls((-1, 1), (Fraction(1, 2), Fraction(1, 2)))

    @property
    def mean(self) -> Fraction:
        return sum(
            (weight * value for value, weight in zip(self.support, self.weights)),
            start=Fraction(0),
        )

    def centered_moment(self, order: int) -> Fraction:
        if order < 1:
            raise NativeBrownianDomainError("moment order must be positive")
        mean = self.mean
        return sum(
            (
                weight * (Fraction(value) - mean) ** order
                for value, weight in zip(self.support, self.weights)
            ),
            start=Fraction(0),
        )


@dataclass(frozen=True)
class ScaleDiscoveryCost:
    law_atoms: int
    exact_weighted_additions: int
    active_orders_tested: int


@dataclass(frozen=True)
class DiffusiveScaleCertificate:
    increment_mean: Fraction
    centered_variance: Fraction
    active_response_order: int
    population_power: int
    scale_exponent: Fraction
    balance_residual: Fraction
    balanced_response_coefficient: Fraction
    exact_identity: str
    claim_boundary: str
    cost: ScaleDiscoveryCost

    @property
    def balanced(self) -> bool:
        return self.balance_residual == 0


def discover_diffusive_scale(law: FiniteIncrementLaw) -> DiffusiveScaleCertificate:
    """Derive the first centered finite-law scale without receiving its value.

    Independent composition makes the local cumulant additive in the number
    of increments.  At zero, its first derivative is the exact mean and its
    second derivative is the exact centered variance.  The fundamental
    theorem of calculus gives an exact double-integral identity, so no local
    expansion is used to identify the active response order.
    """

    mean = law.mean
    if mean != 0:
        raise CenteringRequired(mean)
    first_centered = law.centered_moment(1)
    variance = law.centered_moment(2)
    if first_centered != 0:  # pragma: no cover - protected by exact centering
        raise NativeBrownianDomainError("centered first response did not vanish")
    if variance <= 0:
        raise NativeBrownianDomainError(
            "a nondegenerate centered second response is required"
        )

    population_power = 1
    active_order = 2
    exponent = Fraction(population_power, active_order)
    residual = Fraction(population_power) - active_order * exponent
    return DiffusiveScaleCertificate(
        increment_mean=mean,
        centered_variance=variance,
        active_response_order=active_order,
        population_power=population_power,
        scale_exponent=exponent,
        balance_residual=residual,
        balanced_response_coefficient=variance / 2,
        exact_identity=(
            "kappa(s)=integral_0^s (s-u) kappa_second(u) du after exact "
            "centering"
        ),
        claim_boundary=(
            "scale balance only; no limit law, continuum path law, or heat "
            "equation is certified"
        ),
        cost=ScaleDiscoveryCost(
            law_atoms=len(law.support),
            exact_weighted_additions=2 * len(law.support),
            active_orders_tested=2,
        ),
    )


@dataclass(frozen=True)
class EndpointFibreCost:
    transition_updates: int
    peak_live_fibres: int
    stored_endpoint_fibres: int
    literal_history_count: int


@dataclass(frozen=True)
class EndpointFibreDistribution:
    dimension: int
    horizon: int
    counts: tuple[tuple[Point, int], ...]
    cost: EndpointFibreCost

    def __post_init__(self) -> None:
        if self.dimension < 1:
            raise NativeBrownianDomainError("dimension must be positive")
        if self.horizon < 0:
            raise NativeBrownianDomainError("horizon must be non-negative")
        points = tuple(point for point, _ in self.counts)
        if tuple(sorted(points)) != points or len(set(points)) != len(points):
            raise NativeBrownianDomainError("endpoint fibres must be uniquely sorted")
        if any(len(point) != self.dimension for point in points):
            raise NativeBrownianDomainError("endpoint dimension mismatch")
        if any(count <= 0 for _, count in self.counts):
            raise NativeBrownianDomainError("endpoint fibre counts must be positive")
        if self.total_histories != (2 * self.dimension) ** self.horizon:
            raise NativeBrownianDomainError("endpoint fibres do not conserve history mass")

    @property
    def total_histories(self) -> int:
        return sum(count for _, count in self.counts)

    @property
    def support_size(self) -> int:
        return len(self.counts)

    def count(self, point: Point) -> int:
        if len(point) != self.dimension:
            raise NativeBrownianDomainError("endpoint dimension mismatch")
        return dict(self.counts).get(point, 0)

    def probability(self, point: Point) -> Fraction:
        return Fraction(self.count(point), self.total_histories)


def nearest_neighbour_steps(dimension: int) -> tuple[Point, ...]:
    if dimension < 1:
        raise NativeBrownianDomainError("dimension must be positive")
    steps: list[Point] = []
    for axis in range(dimension):
        for sign in (-1, 1):
            point = [0] * dimension
            point[axis] = sign
            steps.append(tuple(point))
    return tuple(steps)


def _add_points(left: Point, right: Point) -> Point:
    return tuple(a + b for a, b in zip(left, right))


def endpoint_fibres(
    dimension: int,
    horizon: int,
    *,
    max_transition_updates: int = 1_000_000,
) -> EndpointFibreDistribution:
    """Push finite histories to endpoints by chronological process updates."""

    if horizon < 0:
        raise NativeBrownianDomainError("horizon must be non-negative")
    if max_transition_updates < 0:
        raise NativeBrownianDomainError("update budget must be non-negative")
    steps = nearest_neighbour_steps(dimension)
    origin = (0,) * dimension
    counts: dict[Point, int] = {origin: 1}
    transition_updates = 0
    peak_live = 1
    for _ in range(horizon):
        next_counts: dict[Point, int] = {}
        for point, count in counts.items():
            for step in steps:
                transition_updates += 1
                if transition_updates > max_transition_updates:
                    raise EndpointFibreBudgetError(
                        "endpoint-fibre transition budget exhausted"
                    )
                endpoint = _add_points(point, step)
                next_counts[endpoint] = next_counts.get(endpoint, 0) + count
        counts = next_counts
        peak_live = max(peak_live, len(counts))
    return EndpointFibreDistribution(
        dimension=dimension,
        horizon=horizon,
        counts=tuple(sorted(counts.items())),
        cost=EndpointFibreCost(
            transition_updates=transition_updates,
            peak_live_fibres=peak_live,
            stored_endpoint_fibres=len(counts),
            literal_history_count=(2 * dimension) ** horizon,
        ),
    )


def concatenate_endpoint_fibres(
    left: EndpointFibreDistribution,
    right: EndpointFibreDistribution,
    *,
    max_transition_updates: int = 1_000_000,
) -> EndpointFibreDistribution:
    """Induce history concatenation on the endpoint task fibres."""

    if left.dimension != right.dimension:
        raise NativeBrownianDomainError("cannot concatenate different dimensions")
    if max_transition_updates < 0:
        raise NativeBrownianDomainError("update budget must be non-negative")
    counts: dict[Point, int] = {}
    updates = 0
    for left_point, left_count in left.counts:
        for right_point, right_count in right.counts:
            updates += 1
            if updates > max_transition_updates:
                raise EndpointFibreBudgetError(
                    "endpoint-fibre concatenation budget exhausted"
                )
            endpoint = _add_points(left_point, right_point)
            counts[endpoint] = counts.get(endpoint, 0) + left_count * right_count
    return EndpointFibreDistribution(
        dimension=left.dimension,
        horizon=left.horizon + right.horizon,
        counts=tuple(sorted(counts.items())),
        cost=EndpointFibreCost(
            transition_updates=updates,
            peak_live_fibres=len(counts),
            stored_endpoint_fibres=len(counts),
            literal_history_count=left.total_histories * right.total_histories,
        ),
    )


def certify_history_concatenation(
    dimension: int,
    left_horizon: int,
    right_horizon: int,
) -> bool:
    left = endpoint_fibres(dimension, left_horizon)
    right = endpoint_fibres(dimension, right_horizon)
    composed = concatenate_endpoint_fibres(left, right)
    direct = endpoint_fibres(dimension, left_horizon + right_horizon)
    return composed.counts == direct.counts


def literal_endpoint(history: Iterable[Point], dimension: int) -> Point:
    """Evaluate one literal history without applying the endpoint quotient."""

    endpoint = (0,) * dimension
    legal = frozenset(nearest_neighbour_steps(dimension))
    for step in history:
        if step not in legal:
            raise NativeBrownianDomainError("history contains an illegal step")
        endpoint = _add_points(endpoint, step)
    return endpoint


def exhaustive_endpoint_counts(dimension: int, horizon: int) -> tuple[tuple[Point, int], ...]:
    """Small exact certificate path; callers must keep the horizon bounded."""

    if horizon < 0:
        raise NativeBrownianDomainError("horizon must be non-negative")
    if (2 * dimension) ** horizon > 100_000:
        raise EndpointFibreBudgetError("literal history certificate budget exhausted")
    steps = nearest_neighbour_steps(dimension)
    counts: dict[Point, int] = {}
    for history in product(steps, repeat=horizon):
        endpoint = literal_endpoint(history, dimension)
        counts[endpoint] = counts.get(endpoint, 0) + 1
    return tuple(sorted(counts.items()))

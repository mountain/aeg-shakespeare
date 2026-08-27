"""Exact compact-space Brownian red teams for issue #162.

The executable layer stays finite.  Integer-lattice histories are pushed to a
cycle by the deck quotient ``x -> x mod q`` and compared with an independent
direct cycle update.  No transform, matrix, heat kernel, or continuum solver
enters native discovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from typing import Iterable


class CompactBrownianDomainError(ValueError):
    """The compact red-team grammar does not cover the requested input."""


class PeriodicClockObstruction(CompactBrownianDomainError):
    """A terminal-time mixing claim is blocked by a periodic discrete clock."""

    def __init__(self, modulus: int, period: int) -> None:
        self.modulus = modulus
        self.period = period
        super().__init__(
            "periodic-clock-obstruction: "
            f"nearest-neighbour walk on C_{modulus} has period {period}; "
            "use a lazy/continuous clock or a Cesaro observer"
        )


class ReducibleClockObstruction(CompactBrownianDomainError):
    """A stationary law is not a mixing limit when the clock never moves."""

    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        super().__init__(
            "reducible-clock-obstruction: "
            f"stay probability one leaves every state of C_{modulus} absorbing"
        )


class StabilityMechanism(str, Enum):
    SCALE_RENORMALIZED = "scale-renormalized"
    TIME_STATIONARY = "time-stationary"


def _require_modulus(modulus: int) -> None:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 2:
        raise CompactBrownianDomainError("cycle modulus must be an integer >= 2")


def _require_horizon(horizon: int) -> None:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise CompactBrownianDomainError(
            "cycle horizon must be a non-negative integer"
        )


@dataclass(frozen=True)
class CycleEndpointCounts:
    modulus: int
    horizon: int
    counts: tuple[int, ...]
    construction: str

    def __post_init__(self) -> None:
        _require_modulus(self.modulus)
        _require_horizon(self.horizon)
        if len(self.counts) != self.modulus:
            raise CompactBrownianDomainError("one count is required per residue")
        if any(
            isinstance(count, bool) or not isinstance(count, int) or count < 0
            for count in self.counts
        ):
            raise CompactBrownianDomainError(
                "cycle counts must be non-negative integers"
            )
        if self.total_histories != 2**self.horizon:
            raise CompactBrownianDomainError(
                "cycle endpoint counts do not conserve history mass"
            )
        if not self.construction.strip():
            raise CompactBrownianDomainError("cycle construction must be declared")

    @property
    def total_histories(self) -> int:
        return sum(self.counts)

    def probability(self, residue: int) -> Fraction:
        return Fraction(self.counts[residue % self.modulus], self.total_histories)


@dataclass(frozen=True)
class DeckFibrePushforward:
    cycle: CycleEndpointCounts
    deck_fibres: tuple[tuple[tuple[int, int], ...], ...]

    def __post_init__(self) -> None:
        if len(self.deck_fibres) != self.cycle.modulus:
            raise CompactBrownianDomainError(
                "one deck fibre is required per cycle residue"
            )
        for residue, fibre in enumerate(self.deck_fibres):
            if any(lift % self.cycle.modulus != residue for lift, _ in fibre):
                raise CompactBrownianDomainError("a lift is in the wrong deck fibre")
            if sum(count for _, count in fibre) != self.cycle.counts[residue]:
                raise CompactBrownianDomainError(
                    "deck fibre mass does not match the quotient count"
                )


def fold_integer_endpoint_counts(
    line_counts: Iterable[tuple[int, int]],
    *,
    modulus: int,
    horizon: int,
) -> DeckFibrePushforward:
    """Push exact line counts through ``Z -> Z/qZ`` and retain every lift."""

    _require_modulus(modulus)
    _require_horizon(horizon)
    fibres: list[list[tuple[int, int]]] = [[] for _ in range(modulus)]
    seen: set[int] = set()
    for lift, count in line_counts:
        if isinstance(lift, bool) or not isinstance(lift, int):
            raise CompactBrownianDomainError("line endpoints must be integers")
        if lift in seen:
            raise CompactBrownianDomainError("line endpoints must be unique")
        seen.add(lift)
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise CompactBrownianDomainError(
                "line endpoint counts must be positive integers"
            )
        fibres[lift % modulus].append((lift, count))
    ordered_fibres = tuple(tuple(sorted(fibre)) for fibre in fibres)
    counts = tuple(sum(count for _, count in fibre) for fibre in ordered_fibres)
    cycle = CycleEndpointCounts(
        modulus=modulus,
        horizon=horizon,
        counts=counts,
        construction="deck-fibre pushforward from the integer lattice",
    )
    return DeckFibrePushforward(cycle=cycle, deck_fibres=ordered_fibres)


def direct_cycle_endpoint_counts(modulus: int, horizon: int) -> CycleEndpointCounts:
    """Independent chronological update directly on the cycle."""

    _require_modulus(modulus)
    _require_horizon(horizon)
    counts = [0] * modulus
    counts[0] = 1
    for _ in range(horizon):
        next_counts = [0] * modulus
        for residue, count in enumerate(counts):
            next_counts[(residue - 1) % modulus] += count
            next_counts[(residue + 1) % modulus] += count
        counts = next_counts
    return CycleEndpointCounts(
        modulus=modulus,
        horizon=horizon,
        counts=tuple(counts),
        construction="direct chronological nearest-neighbour cycle update",
    )


@dataclass(frozen=True)
class CycleLaw:
    masses: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if len(self.masses) < 2:
            raise CompactBrownianDomainError("a cycle law needs at least two states")
        if any(not isinstance(mass, Fraction) or mass < 0 for mass in self.masses):
            raise CompactBrownianDomainError(
                "cycle masses must be non-negative exact fractions"
            )
        if sum(self.masses, start=Fraction(0)) != 1:
            raise CompactBrownianDomainError("cycle masses must sum exactly to one")

    @classmethod
    def point_mass(cls, modulus: int, residue: int = 0) -> "CycleLaw":
        _require_modulus(modulus)
        masses = [Fraction(0)] * modulus
        masses[residue % modulus] = Fraction(1)
        return cls(tuple(masses))

    @classmethod
    def uniform(cls, modulus: int) -> "CycleLaw":
        _require_modulus(modulus)
        return cls((Fraction(1, modulus),) * modulus)

    @property
    def modulus(self) -> int:
        return len(self.masses)


def cycle_step(law: CycleLaw, *, stay_probability: Fraction) -> CycleLaw:
    """Apply one exact symmetric step, optionally with a declared lazy clock."""

    if not isinstance(stay_probability, Fraction):
        raise CompactBrownianDomainError("stay probability must be an exact Fraction")
    if not 0 <= stay_probability <= 1:
        raise CompactBrownianDomainError("stay probability must lie in [0, 1]")
    move_probability = (1 - stay_probability) / 2
    next_masses = [Fraction(0)] * law.modulus
    for residue, mass in enumerate(law.masses):
        next_masses[residue] += stay_probability * mass
        next_masses[(residue - 1) % law.modulus] += move_probability * mass
        next_masses[(residue + 1) % law.modulus] += move_probability * mass
    return CycleLaw(tuple(next_masses))


def nearest_neighbour_period(modulus: int, *, stay_probability: Fraction) -> int:
    _require_modulus(modulus)
    if not isinstance(stay_probability, Fraction):
        raise CompactBrownianDomainError("stay probability must be an exact Fraction")
    if not 0 <= stay_probability <= 1:
        raise CompactBrownianDomainError("stay probability must lie in [0, 1]")
    if stay_probability > 0:
        return 1
    return 2 if modulus % 2 == 0 else 1


def require_terminal_mixing_clock(
    modulus: int,
    *,
    stay_probability: Fraction,
) -> None:
    if stay_probability == 1:
        raise ReducibleClockObstruction(modulus)
    period = nearest_neighbour_period(
        modulus,
        stay_probability=stay_probability,
    )
    if period != 1:
        raise PeriodicClockObstruction(modulus, period)


def total_variation(left: CycleLaw, right: CycleLaw) -> Fraction:
    if left.modulus != right.modulus:
        raise CompactBrownianDomainError(
            "total variation requires laws on the same cycle"
        )
    return sum(
        (abs(a - b) for a, b in zip(left.masses, right.masses)),
        start=Fraction(0),
    ) / 2


@dataclass(frozen=True)
class BoundedMixingAudit:
    modulus: int
    stay_probability: Fraction
    horizons: tuple[int, ...]
    distances_to_uniform: tuple[Fraction, ...]
    nonincreasing: bool
    claim_boundary: str


def bounded_lazy_mixing_audit(
    modulus: int,
    *,
    horizon: int,
    stay_probability: Fraction = Fraction(1, 2),
) -> BoundedMixingAudit:
    """Record a bounded exact trend; this is deliberately not a limit theorem."""

    _require_modulus(modulus)
    _require_horizon(horizon)
    require_terminal_mixing_clock(
        modulus,
        stay_probability=stay_probability,
    )
    law = CycleLaw.point_mass(modulus)
    uniform = CycleLaw.uniform(modulus)
    distances = [total_variation(law, uniform)]
    for _ in range(horizon):
        law = cycle_step(law, stay_probability=stay_probability)
        distances.append(total_variation(law, uniform))
    return BoundedMixingAudit(
        modulus=modulus,
        stay_probability=stay_probability,
        horizons=tuple(range(horizon + 1)),
        distances_to_uniform=tuple(distances),
        nonincreasing=all(
            right <= left for left, right in zip(distances, distances[1:])
        ),
        claim_boundary=(
            "bounded exact calibration only; no asymptotic mixing theorem is claimed"
        ),
    )


@dataclass(frozen=True)
class WindingResidual:
    modulus: int
    left_history: tuple[int, ...]
    right_history: tuple[int, ...]
    left_lift: int
    right_lift: int
    shared_residue: int
    lost_observer: str


def expose_winding_residual(
    modulus: int,
    left_history: Iterable[int],
    right_history: Iterable[int],
) -> WindingResidual:
    _require_modulus(modulus)
    left = tuple(left_history)
    right = tuple(right_history)
    if left == right or len(left) != len(right):
        raise CompactBrownianDomainError(
            "winding witness needs distinct equal-horizon histories"
        )
    if any(step not in {-1, 1} for step in left + right):
        raise CompactBrownianDomainError("winding histories use only +/-1 steps")
    left_lift = sum(left)
    right_lift = sum(right)
    if left_lift == right_lift or left_lift % modulus != right_lift % modulus:
        raise CompactBrownianDomainError(
            "winding histories need different lifts with one cycle endpoint"
        )
    return WindingResidual(
        modulus=modulus,
        left_history=left,
        right_history=right,
        left_lift=left_lift,
        right_lift=right_lift,
        shared_residue=left_lift % modulus,
        lost_observer="integer lift, winding, and chronological path observables",
    )


@dataclass(frozen=True)
class CompactSpaceClaimBoundary:
    space: str
    quotient_or_homogeneous_space: str
    local_law: str
    long_time_candidate: str
    stability_mechanism: StabilityMechanism
    unavailable_global_actions: tuple[str, ...]
    retained_residuals: tuple[str, ...]
    claim_boundary: str


CIRCLE_GATE = CompactSpaceClaimBoundary(
    space="circle S^1",
    quotient_or_homogeneous_space="R / (2*pi*Z)",
    local_law="Gaussian only on a local/cover chart; globally a wrapped pushforward",
    long_time_candidate="normalized Haar measure dtheta/(2*pi)",
    stability_mechanism=StabilityMechanism.TIME_STATIONARY,
    unavailable_global_actions=(
        "global additive position chart",
        "internal spatial dilation at fixed circumference",
    ),
    retained_residuals=("winding/deck lift", "clock periodicity", "path order"),
    claim_boundary=(
        "finite cycle calibration and continuum semantic contract only; no circle "
        "heat-kernel or continuum mixing theorem"
    ),
)


SPHERE_GATE = CompactSpaceClaimBoundary(
    space="sphere S^2",
    quotient_or_homogeneous_space="SO(3) / SO(2)",
    local_law="Gaussian only in a tangent chart with curvature residual",
    long_time_candidate="normalized Riemannian area measure dA/(4*pi)",
    stability_mechanism=StabilityMechanism.TIME_STATIONARY,
    unavailable_global_actions=(
        "single global additive position chart",
        "internal spatial dilation at fixed radius",
    ),
    retained_residuals=(
        "curvature",
        "chart transition",
        "holonomy",
        "path history",
    ),
    claim_boundary=(
        "initial sphere gate only; no executable continuum Brownian construction, "
        "heat-kernel theorem, or AMP universality result"
    ),
)

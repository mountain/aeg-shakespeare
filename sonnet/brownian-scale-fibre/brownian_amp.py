"""Research-local AMP chart candidates for the Brownian correction (#160).

The executable algebra below is deliberately finite and exact.  Its atoms are
``E_q(s) = exp(q*s)`` with rational ``q`` and rational coefficients.  It does
not lower them to Taylor coefficients, matrices, or Fourier modes.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


class BrownianAMPDomainError(ValueError):
    """An AMP chart or exact finite carrier does not cover the requested input."""


class PositionChartDomainError(BrownianAMPDomainError):
    """A history left the common positive domain of the A/M/P flows."""

    def __init__(
        self,
        *,
        step_index: int,
        value: Fraction,
        offending_increment: Fraction | None,
    ) -> None:
        self.step_index = step_index
        self.value = value
        self.offending_increment = offending_increment
        super().__init__(
            "positive-position-chart-obstruction: "
            f"state {value} at step {step_index} is outside x > 0"
        )


def _require_fraction(value: object, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise BrownianAMPDomainError(f"{name} must be an exact Fraction")
    return value


@dataclass(frozen=True)
class PositivePositionAudit:
    initial: Fraction
    increments: tuple[Fraction, ...]
    states: tuple[Fraction, ...]
    common_domain: str
    generator_ids: tuple[str, ...]
    claim_boundary: str


def audit_positive_position_history(
    initial: Fraction,
    increments: Iterable[Fraction],
) -> PositivePositionAudit:
    """Check whether an additive history stays in the real Log AMP chart.

    A is used to transport the state.  Positivity is the common domain needed
    for the real P flow ``x -> exp(exp(r) Log(x))``; M preserves that domain.
    The function therefore audits the three-generator chart without pretending
    that a symmetric Brownian history stays inside it.
    """

    current = _require_fraction(initial, "initial")
    history = tuple(increments)
    for increment in history:
        _require_fraction(increment, "increment")
    if current <= 0:
        raise PositionChartDomainError(
            step_index=0,
            value=current,
            offending_increment=None,
        )

    states = [current]
    for step_index, increment in enumerate(history, start=1):
        current += increment
        if current <= 0:
            raise PositionChartDomainError(
                step_index=step_index,
                value=current,
                offending_increment=increment,
            )
        states.append(current)
    return PositivePositionAudit(
        initial=initial,
        increments=history,
        states=tuple(states),
        common_domain="x > 0 with the real Log branch",
        generator_ids=("A", "M", "P"),
        claim_boundary=(
            "local chart audit only; it does not make the symmetric Brownian "
            "position process positive"
        ),
    )


@dataclass(frozen=True)
class ObserverProductCost:
    atom_products: int


@dataclass(frozen=True)
class ReplicaPowerResult:
    observer: "ExponentialObserver"
    replicas: int
    factor_compositions: int
    atom_products: int
    power_slice: str
    residual: str


@dataclass(frozen=True)
class ExponentialObserver:
    """A finite exact sum of exponential atoms ``E_q(s)``.

    ``terms`` stores ``(q, c_q)`` and denotes ``sum c_q E_q``.  Multiplication
    uses ``E_p E_q = E_(p+q)`` directly.  This is polynomial-like in named
    exponential atoms, but it is not an ordinary polynomial or a power series.
    """

    terms: tuple[tuple[Fraction, Fraction], ...]

    def __post_init__(self) -> None:
        if not self.terms:
            raise BrownianAMPDomainError("an observer must contain at least one atom")
        exponents = tuple(exponent for exponent, _ in self.terms)
        if exponents != tuple(sorted(exponents)) or len(set(exponents)) != len(
            exponents
        ):
            raise BrownianAMPDomainError(
                "observer exponents must be uniquely sorted"
            )
        for exponent, coefficient in self.terms:
            _require_fraction(exponent, "observer exponent")
            _require_fraction(coefficient, "observer coefficient")
            if coefficient == 0:
                raise BrownianAMPDomainError(
                    "zero coefficients must be removed from the observer"
                )

    @classmethod
    def from_atoms(
        cls,
        atoms: Iterable[tuple[Fraction, Fraction]],
    ) -> "ExponentialObserver":
        combined: dict[Fraction, Fraction] = {}
        for exponent, coefficient in atoms:
            exponent = _require_fraction(exponent, "observer exponent")
            coefficient = _require_fraction(coefficient, "observer coefficient")
            combined[exponent] = combined.get(exponent, Fraction(0)) + coefficient
        terms = tuple(
            (exponent, coefficient)
            for exponent, coefficient in sorted(combined.items())
            if coefficient != 0
        )
        return cls(terms)

    @classmethod
    def constant_one(cls) -> "ExponentialObserver":
        return cls(((Fraction(0), Fraction(1)),))

    @classmethod
    def point_mass(cls, value: Fraction) -> "ExponentialObserver":
        value = _require_fraction(value, "point-mass value")
        return cls(((value, Fraction(1)),))

    @classmethod
    def from_finite_law(
        cls,
        support: Iterable[int],
        weights: Iterable[Fraction],
    ) -> "ExponentialObserver":
        support = tuple(support)
        weights = tuple(weights)
        if len(support) != len(weights) or not support:
            raise BrownianAMPDomainError("law support and weights must align")
        if any(not isinstance(value, int) or isinstance(value, bool) for value in support):
            raise BrownianAMPDomainError("law support must contain integers")
        for weight in weights:
            _require_fraction(weight, "law weight")
        if any(weight <= 0 for weight in weights) or sum(
            weights, start=Fraction(0)
        ) != 1:
            raise BrownianAMPDomainError(
                "law weights must be positive exact fractions summing to one"
            )
        return cls.from_atoms(
            (Fraction(value), weight) for value, weight in zip(support, weights)
        )

    @property
    def mass(self) -> Fraction:
        return sum((coefficient for _, coefficient in self.terms), Fraction(0))

    def coefficient(self, exponent: Fraction) -> Fraction:
        exponent = _require_fraction(exponent, "coefficient exponent")
        return dict(self.terms).get(exponent, Fraction(0))

    def shift_state(self, translation: Fraction) -> "ExponentialObserver":
        """Apply A: ``Z_(X+t) = E_t Z_X`` exactly on the atom exponents."""

        translation = _require_fraction(translation, "translation")
        return ExponentialObserver.from_atoms(
            (exponent + translation, coefficient)
            for exponent, coefficient in self.terms
        )

    def scale_state(self, scale: Fraction) -> "ExponentialObserver":
        """Apply positive M: ``Z_(lambda X)(s) = Z_X(lambda s)``."""

        scale = _require_fraction(scale, "scale")
        if scale <= 0:
            raise BrownianAMPDomainError("multiplicative scale must be positive")
        return ExponentialObserver.from_atoms(
            (scale * exponent, coefficient)
            for exponent, coefficient in self.terms
        )

    def multiply(
        self,
        other: "ExponentialObserver",
    ) -> tuple["ExponentialObserver", ObserverProductCost]:
        """Compose independent laws using ``E_p E_q = E_(p+q)``."""

        if not isinstance(other, ExponentialObserver):
            raise BrownianAMPDomainError("observer multiplication needs two observers")
        atoms = (
            (left_exp + right_exp, left_coeff * right_coeff)
            for left_exp, left_coeff in self.terms
            for right_exp, right_coeff in other.terms
        )
        return (
            ExponentialObserver.from_atoms(atoms),
            ObserverProductCost(atom_products=len(self.terms) * len(other.terms)),
        )

    def replica_power(self, replicas: int) -> ReplicaPowerResult:
        """Apply the exact nonnegative-integer slice of the P action.

        Integer powers describe convolution replicas.  The continuous P flow
        ``Z -> Z^(exp(r))`` is well-defined pointwise for positive real ``Z``,
        but a noninteger power generally leaves this finite atom carrier.  That
        closure failure is returned explicitly rather than hidden by a series.
        """

        if isinstance(replicas, bool) or not isinstance(replicas, int) or replicas < 0:
            raise BrownianAMPDomainError(
                "replica power requires a non-negative integer"
            )
        result = ExponentialObserver.constant_one()
        base = self
        remaining = replicas
        compositions = 0
        atom_products = 0
        while remaining:
            if remaining & 1:
                result, cost = result.multiply(base)
                compositions += 1
                atom_products += cost.atom_products
            remaining >>= 1
            if remaining:
                base, cost = base.multiply(base)
                compositions += 1
                atom_products += cost.atom_products
        return ReplicaPowerResult(
            observer=result,
            replicas=replicas,
            factor_compositions=compositions,
            atom_products=atom_products,
            power_slice="exact nonnegative-integer replica slice",
            residual=(
                "noninteger P flow generally exits the finite exponential-atom family"
            ),
        )


@dataclass(frozen=True)
class PathInformationResidual:
    left_history: tuple[Fraction, ...]
    right_history: tuple[Fraction, ...]
    shared_observer: ExponentialObserver
    lost_observer: str


def expose_path_information_residual(
    left_history: Iterable[Fraction],
    right_history: Iterable[Fraction],
) -> PathInformationResidual:
    """Exhibit two distinct histories collapsed by the endpoint observer."""

    left = tuple(left_history)
    right = tuple(right_history)
    for increment in left + right:
        _require_fraction(increment, "history increment")
    if left == right:
        raise BrownianAMPDomainError("histories must be distinct")
    left_endpoint = sum(left, start=Fraction(0))
    right_endpoint = sum(right, start=Fraction(0))
    if left_endpoint != right_endpoint:
        raise BrownianAMPDomainError("histories must share an endpoint")
    return PathInformationResidual(
        left_history=left,
        right_history=right,
        shared_observer=ExponentialObserver.point_mass(left_endpoint),
        lost_observer="running maximum and chronological order",
    )

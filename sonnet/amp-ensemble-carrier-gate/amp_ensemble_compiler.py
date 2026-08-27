"""Research-local compiler for the finite M/P shadow of an AMP system.

The positive-real maps

    M_b(x) = exp(b) * x
    P_a(x) = x**a

become affine maps ``y -> a*y + b`` in the logarithmic observer ``y=log x``.
This module records that exact normal form and applies it to homogeneous
ensemble assembly.  Addition is deliberately excluded from the finite carrier:
in logarithmic coordinates ``x -> x+t`` contributes ``log(1+t*exp(-y))`` and
therefore an infinite completed ray rather than another affine map.

This is a Sonnet-local executable certificate, not a Public API.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import prod
from typing import Iterable


@dataclass(frozen=True)
class MPNormalForm:
    """The logarithmic action ``y -> exponent*y + log_scale``."""

    exponent: Fraction = Fraction(1)
    log_scale: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        if self.exponent <= 0:
            raise ValueError("the positive-real M/P chart requires exponent > 0")

    def apply_log(self, value: Fraction) -> Fraction:
        return self.exponent * value + self.log_scale

    def then(self, later: "MPNormalForm") -> "MPNormalForm":
        """Apply ``self`` first and ``later`` second."""

        return MPNormalForm(
            exponent=later.exponent * self.exponent,
            log_scale=later.exponent * self.log_scale + later.log_scale,
        )

    def iterate(self, count: int) -> "MPNormalForm":
        """Return the exact normal form of ``count`` repeated applications."""

        if count < 0:
            raise ValueError("iteration count must be nonnegative")
        if count == 0:
            return MPNormalForm()

        exponent = self.exponent**count
        if self.exponent == 1:
            log_scale = count * self.log_scale
        else:
            log_scale = self.log_scale * (exponent - 1) / (self.exponent - 1)
        return MPNormalForm(exponent=exponent, log_scale=log_scale)


def multiplication(log_scale: int | Fraction) -> MPNormalForm:
    """Return the M primitive ``x -> exp(log_scale) * x``."""

    return MPNormalForm(log_scale=Fraction(log_scale))


def power(exponent: int | Fraction) -> MPNormalForm:
    """Return the P primitive ``x -> x**exponent`` on the positive chart."""

    return MPNormalForm(exponent=Fraction(exponent))


def fold_mp(history: Iterable[MPNormalForm]) -> MPNormalForm:
    """Compile a chronological M/P word into two exact rational fields."""

    result = MPNormalForm()
    for step in history:
        result = result.then(step)
    return result


@dataclass(frozen=True)
class EnsembleStage:
    """One homogeneous assembly ``Z -> exp(b) * Z**replicas``.

    Integer ``replicas`` has a literal Cartesian-product interpretation.
    ``log_prefactor`` is kept in the logarithmic observer so compilation stays
    exact without pretending that ``exp(b)`` is rational.
    """

    replicas: int
    log_prefactor: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        if self.replicas < 1:
            raise ValueError("a homogeneous ensemble stage needs replicas >= 1")

    def normal_form(self) -> MPNormalForm:
        return MPNormalForm(
            exponent=Fraction(self.replicas),
            log_scale=self.log_prefactor,
        )


@dataclass(frozen=True)
class EnsembleCostLedger:
    """Costs kept separate from the value certificate.

    ``microstate_count`` is represented symbolically as
    ``base_state_count ** total_replicas``.  The compiler never materializes
    that Cartesian product.
    """

    base_state_count: int
    total_replicas: int
    stage_count: int
    expanded_leaf_count: int
    compiled_state_fields: int = 2
    replay_arithmetic_operations: int = 2

    @property
    def microstate_count_power(self) -> tuple[int, int]:
        return self.base_state_count, self.total_replicas

    @property
    def replica_exponent_bit_length(self) -> int:
        """Exact storage width of the positive integer replica exponent."""

        return self.total_replicas.bit_length()

    @property
    def microstate_count_bit_length_lower_bound(self) -> int:
        """A bound computed without materializing ``base**replicas``.

        If ``b=floor(log2(base))``, then ``base >= 2**b`` and therefore
        ``base**replicas`` needs at least ``b*replicas+1`` binary digits.
        """

        if self.base_state_count == 1:
            return 1
        base_log2_floor = self.base_state_count.bit_length() - 1
        return base_log2_floor * self.total_replicas + 1


@dataclass(frozen=True)
class EnsembleFoldCertificate:
    """Exact task-relative certificate for total partition/free-energy data."""

    normal_form: MPNormalForm
    ledger: EnsembleCostLedger

    def replay_log_partition(self, base_log_partition: Fraction) -> Fraction:
        return self.normal_form.apply_log(base_log_partition)


def compile_homogeneous_ensemble(
    base_state_count: int,
    stages: Iterable[EnsembleStage],
) -> EnsembleFoldCertificate:
    """Fold a nested homogeneous ensemble without enumerating microstates."""

    if base_state_count < 1:
        raise ValueError("base_state_count must be positive")

    frozen_stages = tuple(stages)
    normal = fold_mp(stage.normal_form() for stage in frozen_stages)
    total_replicas = prod(stage.replicas for stage in frozen_stages)
    if normal.exponent != total_replicas:
        raise AssertionError("ensemble exponent and replica product disagree")

    return EnsembleFoldCertificate(
        normal_form=normal,
        ledger=EnsembleCostLedger(
            base_state_count=base_state_count,
            total_replicas=total_replicas,
            stage_count=len(frozen_stages),
            expanded_leaf_count=total_replicas,
        ),
    )


def logarithmic_addition_tail(
    translation: int | Fraction,
    order: int,
) -> tuple[tuple[int, Fraction], ...]:
    """Truncate ``log(1 + translation*q)`` through ``q**order`` exactly.

    Here ``q=exp(-y)=1/x``.  The returned pairs are ``(ray_degree,
    coefficient)`` and form the fixed-observer shadow of Addition in the
    logarithmic M/P chart.
    """

    if order < 0:
        raise ValueError("observer order must be nonnegative")
    t = Fraction(translation)
    return tuple(
        (degree, Fraction((-1) ** (degree + 1), degree) * t**degree)
        for degree in range(1, order + 1)
    )


def monomial_vector_field_bracket(
    left_power: int,
    left_log_degree: int,
    right_power: int,
    right_log_degree: int,
) -> tuple[tuple[tuple[int, int], int], ...]:
    r"""Bracket two fields ``x^m (log x)^n d/dx`` in sparse form.

    The exact identity is

    ``[V_mn,V_pq] = x^(m+p-1) ((p-m)L^(n+q) +
    (q-n)L^(n+q-1)) d/dx``.
    """

    if left_log_degree < 0 or right_log_degree < 0:
        raise ValueError("logarithmic degrees must be nonnegative")

    x_power = left_power + right_power - 1
    terms: dict[tuple[int, int], int] = {}

    leading = right_power - left_power
    if leading:
        terms[(x_power, left_log_degree + right_log_degree)] = leading

    lower = right_log_degree - left_log_degree
    lower_degree = left_log_degree + right_log_degree - 1
    if lower and lower_degree >= 0:
        key = (x_power, lower_degree)
        terms[key] = terms.get(key, 0) + lower

    return tuple(sorted(terms.items()))


def negative_power_closure_witness(depth: int) -> tuple[int, int]:
    r"""Return ``(coefficient, x_power)`` for the ``depth``-th witness.

    From ``V_01 = [A,P]-A`` we obtain ``[A,V_01]=V_-1,0``.  Repeated
    bracketing with ``A`` gives

    ``ad_A^(depth-1)(V_-1,0) = (-1)^(depth-1)(depth-1)! V_-depth,0``.
    """

    if depth < 1:
        raise ValueError("closure depth must be positive")

    coefficient = 1
    for factor in range(1, depth):
        coefficient *= -factor
    return coefficient, -depth

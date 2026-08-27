"""AMP polynomial/matrix compiler for a power-dominant iteration.

For ``f(x)=x**d+t`` on a positive large-``x`` chart, put ``y=log(x)`` and
``q=exp(-y)``.  The induced map is

    F(y) = d*y + log(1+t*q**d),
    g(q) = q**d / (1+t*q**d).

On the finite observer basis ``q, ..., q**K``, composition by ``g`` is an
exact sparse matrix ``C``.  The truncated escape/Bottcher coordinate

    H_K(y) = y + sum(h[k] q**k)

is obtained from the *linear* equation ``(d I - C) h = u``.  This is the
research-local matrix-like realization of an AMP polynomial-like chart.

The implementation deliberately keeps two AMP paths separate.  The native
inverse-state process evaluates the scalar escape limit without coefficients
or matrices.  The exact ``Fraction`` compiler constructs a fixed-chart
polynomial-like readout and sparse replay certificate.  Symbolic expansion and
strong numerical recurrence remain independent cost baselines.  This is not a
public Koopman or Bottcher API.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import cached_property
from math import comb, exp, isfinite, log1p


def _fraction(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


@dataclass(frozen=True)
class SparseSubstitutionMatrix:
    """Truncated matrix of ``q**k -> g(q)**k`` with one-based degrees."""

    order: int
    degree: int
    interaction: Fraction
    entries: tuple[tuple[int, int, Fraction], ...]

    @property
    def nonzero_count(self) -> int:
        return len(self.entries)

    @property
    def dense_entry_count(self) -> int:
        return self.order * self.order

    @property
    def nilpotence_index_bound(self) -> int:
        """Smallest ``r`` guaranteed to satisfy ``C**r=0``."""

        index = 0
        leading_degree = 1
        while leading_degree <= self.order:
            leading_degree *= self.degree
            index += 1
        return index

    def apply(self, coefficients: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
        if len(coefficients) != self.order:
            raise ValueError("coefficient vector has the wrong observer order")
        result = [Fraction(0) for _ in range(self.order)]
        for row, column, value in self.entries:
            result[row - 1] += value * coefficients[column - 1]
        return tuple(result)


def substitution_coefficient(
    row: int,
    column: int,
    degree: int,
    interaction: int | Fraction,
) -> Fraction:
    r"""Return ``[q**row] (q**d/(1+t*q**d))**column`` exactly."""

    if row < 1 or column < 1:
        raise ValueError("matrix degrees are one-based positive integers")
    if degree < 2:
        raise ValueError("the power-dominant gate requires degree >= 2")

    if row % degree or row < degree * column:
        return Fraction(0)
    tail_index = row // degree - column
    t = _fraction(interaction)
    return (
        Fraction((-1) ** tail_index * comb(column + tail_index - 1, tail_index))
        * t**tail_index
    )


def build_substitution_matrix(
    degree: int,
    interaction: int | Fraction,
    order: int,
) -> SparseSubstitutionMatrix:
    if degree < 2:
        raise ValueError("degree must be at least two")
    if order < 1:
        raise ValueError("observer order must be positive")
    t = _fraction(interaction)
    if t <= 0:
        raise ValueError("the frozen benchmark uses a positive interaction")

    entries: list[tuple[int, int, Fraction]] = []
    for column in range(1, order + 1):
        tail_index = 0
        while degree * (column + tail_index) <= order:
            row = degree * (column + tail_index)
            value = substitution_coefficient(
                row,
                column,
                degree,
                t,
            )
            if value:
                entries.append((row, column, value))
            tail_index += 1

    return SparseSubstitutionMatrix(
        order=order,
        degree=degree,
        interaction=t,
        entries=tuple(entries),
    )


def interaction_log_coefficients(
    degree: int,
    interaction: int | Fraction,
    order: int,
) -> tuple[Fraction, ...]:
    r"""Coefficients of ``log(1+t*q**degree)`` through ``q**order``."""

    if degree < 2 or order < 1:
        raise ValueError("invalid degree or observer order")
    t = _fraction(interaction)
    result = [Fraction(0) for _ in range(order)]
    power = 1
    while degree * power <= order:
        result[degree * power - 1] = Fraction((-1) ** (power + 1), power) * t**power
        power += 1
    return tuple(result)


@dataclass(frozen=True)
class EscapeCoordinate:
    """Finite AMP polynomial-like coordinate ``y + sum h_k exp(-k y)``."""

    degree: int
    interaction: Fraction
    order: int
    coefficients: tuple[Fraction, ...]

    @property
    def nonzero_term_count(self) -> int:
        return sum(value != 0 for value in self.coefficients)

    @cached_property
    def _degree_ray_coefficients(self) -> tuple[Fraction, ...] | None:
        if not all(
            degree % self.degree == 0 or coefficient == 0
            for degree, coefficient in enumerate(self.coefficients, start=1)
        ):
            return None
        return self.coefficients[self.degree - 1 :: self.degree]

    @property
    def uses_degree_ray_horner(self) -> bool:
        """Whether support is confined to ``q**(degree*j)``."""

        return self._degree_ray_coefficients is not None

    @property
    def horner_step_count(self) -> int:
        """Number of coefficient slots visited by :meth:`evaluate`."""

        if self._degree_ray_coefficients is not None:
            return len(self._degree_ray_coefficients)
        return len(self.coefficients)

    def evaluate(self, log_state: float) -> float:
        ray_coefficients = self._degree_ray_coefficients
        if ray_coefficients is not None:
            z = exp(-self.degree * log_state)
            correction = 0.0
            for coefficient in reversed(ray_coefficients):
                correction = correction * z + float(coefficient)
            return log_state + z * correction

        q = exp(-log_state)
        correction = 0.0
        for coefficient in reversed(self.coefficients):
            correction = correction * q + float(coefficient)
        return log_state + q * correction


@dataclass(frozen=True)
class ResidualTerm:
    degree: int
    coefficient: Fraction


@dataclass(frozen=True)
class CompilationCost:
    observer_order: int
    dense_matrix_entries: int
    sparse_matrix_entries: int
    coordinate_terms: int
    triangular_divisions: int


@dataclass(frozen=True)
class EscapeCompilationCertificate:
    matrix: SparseSubstitutionMatrix
    source: tuple[Fraction, ...]
    coordinate: EscapeCoordinate
    first_omitted_residual: ResidualTerm | None
    cost: CompilationCost

    def replay_eigenrelation(self) -> bool:
        transported = self.matrix.apply(self.coordinate.coefficients)
        d = Fraction(self.coordinate.degree)
        return all(
            self.source[index] + transported[index]
            == d * self.coordinate.coefficients[index]
            for index in range(self.coordinate.order)
        )


def _residual_terms(
    coordinate: EscapeCoordinate,
    maximum_degree: int,
) -> tuple[ResidualTerm, ...]:
    d = coordinate.degree
    t = coordinate.interaction
    order = coordinate.order
    result: list[ResidualTerm] = []

    for row in range(1, maximum_degree + 1):
        source = Fraction(0)
        if row % d == 0:
            power = row // d
            source = Fraction((-1) ** (power + 1), power) * t**power

        transported = sum(
            substitution_coefficient(row, column, d, t)
            * coordinate.coefficients[column - 1]
            for column in range(1, order + 1)
        )
        target = (
            d * coordinate.coefficients[row - 1]
            if row <= order
            else Fraction(0)
        )
        coefficient = source + transported - target
        if coefficient:
            result.append(ResidualTerm(row, coefficient))

    return tuple(result)


def compile_escape_coordinate(
    degree: int,
    interaction: int | Fraction,
    order: int,
) -> EscapeCompilationCertificate:
    """Solve the finite AMP Koopman eigenproblem by triangular transport."""

    matrix = build_substitution_matrix(degree, interaction, order)
    source = interaction_log_coefficients(degree, interaction, order)

    entries_by_row: dict[int, list[tuple[int, Fraction]]] = {}
    for row, column, value in matrix.entries:
        entries_by_row.setdefault(row, []).append((column, value))

    coefficients = [Fraction(0) for _ in range(order)]
    for row in range(1, order + 1):
        transported = sum(
            value * coefficients[column - 1]
            for column, value in entries_by_row.get(row, ())
        )
        coefficients[row - 1] = (source[row - 1] + transported) / degree

    coordinate = EscapeCoordinate(
        degree=degree,
        interaction=_fraction(interaction),
        order=order,
        coefficients=tuple(coefficients),
    )
    residuals = _residual_terms(coordinate, maximum_degree=2 * order + degree)
    omitted = tuple(term for term in residuals if term.degree > order)

    certificate = EscapeCompilationCertificate(
        matrix=matrix,
        source=source,
        coordinate=coordinate,
        first_omitted_residual=omitted[0] if omitted else None,
        cost=CompilationCost(
            observer_order=order,
            dense_matrix_entries=matrix.dense_entry_count,
            sparse_matrix_entries=matrix.nonzero_count,
            coordinate_terms=coordinate.nonzero_term_count,
            triangular_divisions=order,
        ),
    )
    if not certificate.replay_eigenrelation():
        raise AssertionError("compiled coordinate failed exact replay")
    return certificate


@dataclass(frozen=True)
class DirectIterationResult:
    value: float
    executed_steps: int


class NativeProcessDomainError(ValueError):
    """The certified native evaluator does not cover the requested task."""


class NativeProcessBudgetError(RuntimeError):
    """The native evaluator exhausted its process-level budget."""

    def __init__(self, max_levels: int, tail_bound: float) -> None:
        self.max_levels = max_levels
        self.tail_bound = tail_bound
        super().__init__(
            "native AMP evaluation exhausted "
            f"{max_levels} process levels with tail bound {tail_bound!r}"
        )


@dataclass(frozen=True)
class NativeProcessCost:
    """Per-evaluation primitive ledger, excluding validation."""

    process_levels: int
    initial_exponential_evaluations: int
    degree_power_evaluations: int
    log1p_evaluations: int
    inverse_state_updates: int
    state_scalars: int


@dataclass(frozen=True)
class NativeEscapeEvaluation:
    """Certified truncation of the exact inverse-state process."""

    degree: int
    interaction: Fraction
    initial_log_state: float
    tolerance: float
    value: float
    tail_bound: float
    final_inverse_state: float
    cost: NativeProcessCost

    @property
    def certifies_tail_tolerance(self) -> bool:
        """The analytic truncation tail, not roundoff, meets the request."""

        return self.tail_bound <= self.tolerance


def evaluate_escape_process(
    degree: int,
    interaction: int | Fraction,
    initial_log_state: float,
    *,
    tolerance: float = 1e-15,
    max_levels: int = 64,
) -> NativeEscapeEvaluation:
    r"""Evaluate the escape coordinate by the native AMP recurrence.

    With ``q_0=exp(-y)`` and

    ``q_(n+1) = q_n**d / (1+t*q_n**d)``,

    the exact coordinate is

    ``y + sum(d**(-n-1) * log1p(t*q_n**d), n >= 0)``.

    The first certified domain is ``y >= 0`` and ``t > 0``.  There
    ``0 <= q_(n+1) <= q_n <= 1``, so after ``R`` retained levels the
    remaining analytic tail is at most

    ``d**(-R) * t*q_R**d / (d-1)``.

    No polynomial coefficients, Taylor series, or substitution matrix are
    constructed.  The returned bound excludes floating-point roundoff.
    """

    if degree < 2:
        raise NativeProcessDomainError("degree must be at least two")
    t_exact = _fraction(interaction)
    try:
        t = float(t_exact)
    except OverflowError as error:
        raise NativeProcessDomainError(
            "interaction is outside the binary64 evaluator range"
        ) from error
    if t_exact <= 0 or not isfinite(t):
        raise NativeProcessDomainError(
            "the certified native chart requires a finite positive interaction"
        )
    y = float(initial_log_state)
    if not isfinite(y) or y < 0:
        raise NativeProcessDomainError(
            "the first certified native chart requires finite y >= 0"
        )
    tolerance = float(tolerance)
    if not isfinite(tolerance) or tolerance <= 0:
        raise NativeProcessDomainError("tolerance must be finite and positive")
    if max_levels < 1:
        raise NativeProcessDomainError("max_levels must be positive")

    q = exp(-y)
    powered = q**degree
    if q == 0.0 or powered == 0.0:
        raise NativeProcessDomainError(
            "inverse-state underflow prevents a trustworthy binary64 tail bound"
        )
    value = y
    weight = 1.0 / degree
    tail_bound = float("inf")

    for level in range(1, max_levels + 1):
        interaction_argument = t * powered
        if not isfinite(interaction_argument):
            raise NativeProcessDomainError(
                "interaction correction overflowed the binary64 evaluator"
            )
        value += weight * log1p(interaction_argument)
        q = powered / (1.0 + interaction_argument)
        powered = q**degree
        if q == 0.0 or powered == 0.0:
            raise NativeProcessDomainError(
                "inverse-state underflow prevents a trustworthy binary64 tail bound"
            )
        tail_bound = weight * t * powered / (degree - 1)
        if tail_bound == 0.0:
            raise NativeProcessDomainError(
                "tail-bound underflow requires a higher-precision backend"
            )
        if tail_bound <= tolerance:
            return NativeEscapeEvaluation(
                degree=degree,
                interaction=t_exact,
                initial_log_state=y,
                tolerance=tolerance,
                value=value,
                tail_bound=tail_bound,
                final_inverse_state=q,
                cost=NativeProcessCost(
                    process_levels=level,
                    initial_exponential_evaluations=1,
                    degree_power_evaluations=level + 1,
                    log1p_evaluations=level,
                    inverse_state_updates=level,
                    state_scalars=4,
                ),
            )
        weight /= degree

    raise NativeProcessBudgetError(max_levels, tail_bound)


def direct_normalized_log_iteration_result(
    degree: int,
    interaction: int | Fraction,
    initial_log_state: float,
    iterations: int,
) -> DirectIterationResult:
    """Strong O(N) baseline for ``d**(-N) log(f**N(x))``.

    The normalized value is accumulated without constructing ``d**N`` and the
    loop stops safely once the interaction correction underflows to zero.
    """

    if degree < 2 or iterations < 0:
        raise ValueError("invalid degree or iteration count")
    t = float(_fraction(interaction))
    if t <= 0:
        raise ValueError("the frozen benchmark uses a positive interaction")

    current = float(initial_log_state)
    normalized = current
    inverse_scale = 1.0
    executed_steps = 0
    for _ in range(iterations):
        interaction_argument = t * exp(-degree * current)
        correction = log1p(interaction_argument)
        inverse_scale /= degree
        normalized += correction * inverse_scale
        current = degree * current + correction
        executed_steps += 1
        if correction == 0.0:
            break
    return DirectIterationResult(normalized, executed_steps)


def direct_normalized_log_iteration(
    degree: int,
    interaction: int | Fraction,
    initial_log_state: float,
    iterations: int,
) -> float:
    return direct_normalized_log_iteration_result(
        degree,
        interaction,
        initial_log_state,
        iterations,
    ).value


def expanded_symbolic_term_count(
    degree: int,
    interaction: int | Fraction,
    iterations: int,
) -> int:
    """Exact support count for fully expanded positive ``(x**d+t)`` iterates."""

    if degree < 2 or iterations < 0:
        raise ValueError("invalid degree or iteration count")
    t = _fraction(interaction)
    if iterations == 0 or t == 0:
        return 1
    if t < 0:
        raise ValueError("negative interactions may cancel expanded terms")
    return degree ** (iterations - 1) + 1


@dataclass(frozen=True)
class BenchmarkReport:
    degree: int
    interaction: str
    observer_order: int
    horizon: int
    queries: int
    initial_log_state: float
    direct_normalized_value: float
    compiled_normalized_value: float
    absolute_error: float
    expanded_symbolic_terms: int
    direct_recurrence_steps: int
    compiled_online_series_terms: int
    compiled_horner_steps: int
    native_process_value: float
    native_process_tail_bound: float
    native_process_levels: int
    native_process_log1p_evaluations: int
    compilation_cost: dict[str, int]
    first_omitted_residual: tuple[int, str] | None


def benchmark_report(
    *,
    degree: int = 2,
    interaction: int | Fraction = 1,
    observer_order: int = 20,
    horizon: int = 100,
    queries: int = 1,
    initial_log_state: float = 1.5,
    tolerance: float = 1e-15,
) -> BenchmarkReport:
    if queries < 1:
        raise ValueError("query count must be positive")
    certificate = compile_escape_coordinate(degree, interaction, observer_order)
    direct_result = direct_normalized_log_iteration_result(
        degree,
        interaction,
        initial_log_state,
        horizon,
    )
    direct = direct_result.value
    compiled = certificate.coordinate.evaluate(initial_log_state)
    native = evaluate_escape_process(
        degree,
        interaction,
        initial_log_state,
        tolerance=tolerance,
    )
    residual = certificate.first_omitted_residual
    return BenchmarkReport(
        degree=degree,
        interaction=str(_fraction(interaction)),
        observer_order=observer_order,
        horizon=horizon,
        queries=queries,
        initial_log_state=initial_log_state,
        direct_normalized_value=direct,
        compiled_normalized_value=compiled,
        absolute_error=abs(direct - compiled),
        expanded_symbolic_terms=expanded_symbolic_term_count(
            degree,
            interaction,
            horizon,
        ),
        direct_recurrence_steps=queries * direct_result.executed_steps,
        compiled_online_series_terms=(
            queries * certificate.coordinate.nonzero_term_count
        ),
        compiled_horner_steps=queries * certificate.coordinate.horner_step_count,
        native_process_value=native.value,
        native_process_tail_bound=native.tail_bound,
        native_process_levels=queries * native.cost.process_levels,
        native_process_log1p_evaluations=(
            queries * native.cost.log1p_evaluations
        ),
        compilation_cost=asdict(certificate.cost),
        first_omitted_residual=(
            (residual.degree, str(residual.coefficient)) if residual else None
        ),
    )

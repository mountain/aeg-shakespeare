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

The implementation deliberately uses exact ``Fraction`` arithmetic and keeps
symbolic expansion, strong numerical recurrence, and compiled evaluation as
separate cost baselines.  It is not a public Koopman or Bottcher API.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from math import comb, exp, log1p


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

    def evaluate(self, log_state: float) -> float:
        q = exp(-log_state)
        power = q
        correction = 0.0
        for coefficient in self.coefficients:
            correction += float(coefficient) * power
            power *= q
        return log_state + correction


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
        compilation_cost=asdict(certificate.cost),
        first_omitted_residual=(
            (residual.degree, str(residual.coefficient)) if residual else None
        ),
    )

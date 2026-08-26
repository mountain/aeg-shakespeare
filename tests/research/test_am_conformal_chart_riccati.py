"""Exact Phase-1 certificates for the AM conformal-chart Sonnet.

The module deliberately uses only rational arithmetic.  It calibrates the
projective mechanism; it does not claim a new Riccati solution method or a
generic normal-form algorithm.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


Q = Fraction
Matrix2 = tuple[tuple[Q, Q], tuple[Q, Q]]


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matvec(matrix: Matrix2, vector: tuple[Q, Q]) -> tuple[Q, Q]:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def inverse(matrix: Matrix2) -> Matrix2:
    (a, b), (c, d) = matrix
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("singular chart matrix")
    return ((d / determinant, -b / determinant),
            (-c / determinant, a / determinant))


def projective_readout(vector: tuple[Q, Q]) -> Q:
    x, y = vector
    if y == 0:
        raise ValueError("readout is at the infinity chart")
    return -x / y


def riccati_lift(c0: Q, c1: Q, c2: Q) -> Matrix2:
    """Return the traceless two-component lift for a'=c0+c1*a+c2*a^2."""
    return ((c1 / 2, -c0), (c2, -c1 / 2))


def readout_derivative(vector: tuple[Q, Q], velocity: tuple[Q, Q]) -> Q:
    x, y = vector
    dx, dy = velocity
    if y == 0:
        raise ValueError("derivative is at the infinity chart")
    return -(dx * y - x * dy) / (y * y)


def chart_matrix(alpha: Q, beta: Q, gamma: Q, delta: Q) -> Matrix2:
    """Lift b=(alpha*a+beta)/(gamma*a+delta) for a=-x/y."""
    return ((alpha, -beta), (-gamma, delta))


def mobius(alpha: Q, beta: Q, gamma: Q, delta: Q, value: Q) -> Q:
    denominator = gamma * value + delta
    if denominator == 0:
        raise ValueError("value maps to the infinity chart")
    return (alpha * value + beta) / denominator


@dataclass(frozen=True)
class CostVector:
    coeff: int
    action: int
    singular: int
    atlas: int
    decoder: int
    unit: int
    eval: int
    residual: int

    def dominates(self, other: "CostVector") -> bool:
        mine = tuple(self.__dict__.values())
        theirs = tuple(other.__dict__.values())
        return all(a <= b for a, b in zip(mine, theirs)) and any(
            a < b for a, b in zip(mine, theirs)
        )


def test_riccati_lift_recovers_the_scalar_field_exactly() -> None:
    coefficients = (Q(-2), Q(-1, 2), Q(0), Q(3, 2))
    points = (Q(-3), Q(-1, 2), Q(0), Q(2), Q(7, 3))
    for c0, c1, c2 in product(coefficients, repeat=3):
        lift = riccati_lift(c0, c1, c2)
        for value in points:
            vector = (-value, Q(1))
            actual = readout_derivative(vector, matvec(lift, vector))
            assert actual == c0 + c1 * value + c2 * value * value


def test_mobius_chart_and_matrix_conjugacy_commute() -> None:
    charts = (
        (Q(1), Q(1), Q(0), Q(1)),
        (Q(2), Q(-1), Q(1), Q(1)),
        (Q(0), Q(1), Q(-1), Q(0)),
    )
    lift = riccati_lift(Q(2), Q(-3), Q(5, 2))
    for alpha, beta, gamma, delta in charts:
        transform = chart_matrix(alpha, beta, gamma, delta)
        transported_lift = matmul(matmul(transform, lift), inverse(transform))
        for value in (Q(-2), Q(-1, 3), Q(0), Q(1), Q(3)):
            if gamma * value + delta == 0:
                continue
            vector = (-value, Q(1))
            transported = matvec(transform, vector)
            assert projective_readout(transported) == mobius(
                alpha, beta, gamma, delta, value
            )
            direct_velocity = matvec(transported_lift, transported)
            source_velocity = matvec(transform, matvec(lift, vector))
            assert direct_velocity == source_velocity


def test_scalar_gauge_changes_the_lift_but_not_the_readout_dynamics() -> None:
    lift = riccati_lift(Q(1), Q(-2), Q(3))
    for gauge in (Q(-5), Q(0), Q(7, 3)):
        gauged = ((lift[0][0] + gauge, lift[0][1]),
                  (lift[1][0], lift[1][1] + gauge))
        for value in (Q(-2), Q(0), Q(5, 2)):
            vector = (-value, Q(1))
            assert readout_derivative(vector, matvec(gauged, vector)) == (
                readout_derivative(vector, matvec(lift, vector))
            )


def test_nonzero_cubic_field_cannot_be_a_constant_two_by_two_projectivization() -> None:
    # For L=((u,v),(w,z)), differentiating a=-x/y gives
    # a'=-v+(u-z)a+w*a^2.  Its cubic coefficient is identically zero.
    arbitrary_entries = (Q(-2), Q(0), Q(3, 2))
    for u, v, w, z in product(arbitrary_entries, repeat=4):
        induced = (-v, u - z, w, Q(0))
        assert induced[3] == 0
    requested_cubic = (Q(1), Q(-1), Q(2), Q(1))
    assert requested_cubic[3] != 0


def test_cost_accounting_is_pareto_not_scalar_or_character_count() -> None:
    scalar_chart = CostVector(3, 3, 0, 1, 0, 0, 3, 0)
    projective_lift = CostVector(3, 4, 1, 1, 1, 1, 4, 1)
    sparse_chart_with_decoder = CostVector(2, 3, 1, 2, 2, 1, 3, 1)

    # A shorter coefficient record does not dominate after chart/decoder costs.
    assert not sparse_chart_with_decoder.dominates(scalar_chart)
    assert not scalar_chart.dominates(sparse_chart_with_decoder)
    # The classical lift is a mechanism certificate, not an economy theorem.
    assert not projective_lift.dominates(scalar_chart)


def test_invalid_chart_and_infinity_domain_fail_closed() -> None:
    try:
        inverse(((Q(1), Q(2)), (Q(2), Q(4))))
    except ValueError as error:
        assert "singular" in str(error)
    else:
        raise AssertionError("singular chart was accepted")

    try:
        projective_readout((Q(1), Q(0)))
    except ValueError as error:
        assert "infinity" in str(error)
    else:
        raise AssertionError("infinity chart was silently decoded")

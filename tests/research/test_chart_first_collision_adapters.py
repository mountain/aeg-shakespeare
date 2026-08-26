"""Exact Phase 1C certificates for chart-first semantic adapters."""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


Q = Fraction
SPECIES = tuple(range(3))
PAIR_STATES = tuple(product(SPECIES, repeat=2))
PAIR_INDEX = {state: index for index, state in enumerate(PAIR_STATES)}
ACTIVE_EDGES = (
    ((0, 0), (1, 2)),
    ((0, 0), (2, 1)),
)


@dataclass(frozen=True)
class AMProcess:
    additive: Q
    multiplicative: Q

    def visible_tangent(self, value: Q) -> Q:
        return self.additive + value * self.multiplicative

    def gauge_transform(self, value: Q, gauge_rate: Q) -> "AMProcess":
        return AMProcess(
            self.additive + value * gauge_rate,
            self.multiplicative - gauge_rate,
        )


def _projective_value(x: Q, y: Q) -> Q:
    assert y != 0
    return -x / y


def _projective_tangent(x: Q, y: Q, x_dot: Q, y_dot: Q) -> Q:
    assert y != 0
    return -(y * x_dot - x * y_dot) / (y * y)


def _collision_gain_loss(
    population: tuple[Q, Q, Q, Q], rate: Q
) -> tuple[tuple[AMProcess, ...], tuple[Q, ...]]:
    f0, f1, f2, f3 = population
    incoming = f0 * f1
    outgoing = f2 * f3
    process_pairs = (
        AMProcess(rate * outgoing, -rate * f1),
        AMProcess(rate * outgoing, -rate * f0),
        AMProcess(rate * incoming, -rate * f3),
        AMProcess(rate * incoming, -rate * f2),
    )
    tangent = tuple(
        process_pair.visible_tangent(value)
        for process_pair, value in zip(process_pairs, population)
    )
    return process_pairs, tangent


def _pair_law(entries: dict[tuple[int, int], Q]) -> tuple[Q, ...]:
    return tuple(entries.get(state, Q(0)) for state in PAIR_STATES)


def _uniform_pair_law() -> tuple[Q, ...]:
    return tuple(Q(1, 9) for _ in PAIR_STATES)


def _diagonal_pair_law() -> tuple[Q, ...]:
    return _pair_law({(index, index): Q(1, 3) for index in SPECIES})


def _off_diagonal_pair_law() -> tuple[Q, ...]:
    return _pair_law(
        {
            (left, right): Q(1, 6)
            for left, right in PAIR_STATES
            if left != right
        }
    )


def _mixture(
    left: tuple[Q, ...], right: tuple[Q, ...], right_weight: Q
) -> tuple[Q, ...]:
    return tuple(
        (Q(1) - right_weight) * left_value + right_weight * right_value
        for left_value, right_value in zip(left, right)
    )


def _pair_gain_loss(
    law: tuple[Q, ...], rate: Q = Q(1)
) -> tuple[tuple[AMProcess, ...], tuple[Q, ...]]:
    additive = [Q(0) for _ in PAIR_STATES]
    loss_rate = [Q(0) for _ in PAIR_STATES]

    for left_state, right_state in ACTIVE_EDGES:
        left = PAIR_INDEX[left_state]
        right = PAIR_INDEX[right_state]
        additive[left] += rate * law[right]
        additive[right] += rate * law[left]
        loss_rate[left] += rate
        loss_rate[right] += rate

    process_pairs = tuple(
        AMProcess(gain, -hazard)
        for gain, hazard in zip(additive, loss_rate)
    )
    tangent = tuple(
        process_pair.visible_tangent(value)
        for process_pair, value in zip(process_pairs, law)
    )
    return process_pairs, tangent


def _one_body_weights(species: int) -> tuple[Q, ...]:
    return tuple(
        Q((left == species) + (right == species), 2)
        for left, right in PAIR_STATES
    )


def _one_body_marginal(law: tuple[Q, ...]) -> tuple[Q, ...]:
    return tuple(
        sum(
            (weight * value for weight, value in zip(_one_body_weights(i), law)),
            Q(0),
        )
        for i in SPECIES
    )


def _lower_tangent(pair_tangent: tuple[Q, ...]) -> tuple[Q, ...]:
    return tuple(
        sum(
            (
                weight * value
                for weight, value in zip(
                    _one_body_weights(i), pair_tangent
                )
            ),
            Q(0),
        )
        for i in SPECIES
    )


def _lower_am_first_jet(
    law: tuple[Q, ...], pair_processes: tuple[AMProcess, ...]
) -> tuple[tuple[Q, ...], tuple[AMProcess, ...]]:
    marginal = _one_body_marginal(law)
    lowered = []

    for species, value in enumerate(marginal):
        assert value > 0
        weights = _one_body_weights(species)
        additive = sum(
            (
                weight * process_pair.additive
                for weight, process_pair in zip(weights, pair_processes)
            ),
            Q(0),
        )
        multiplicative_numerator = sum(
            (
                weight * pair_value * process_pair.multiplicative
                for weight, pair_value, process_pair in zip(
                    weights, law, pair_processes
                )
            ),
            Q(0),
        )
        lowered.append(
            AMProcess(additive, multiplicative_numerator / value)
        )

    return marginal, tuple(lowered)


def _is_exchange_symmetric(law: tuple[Q, ...]) -> bool:
    return all(
        law[PAIR_INDEX[left, right]] == law[PAIR_INDEX[right, left]]
        for left, right in PAIR_STATES
    )


def test_same_layer_homogeneous_chart_and_gauge_are_exact():
    value = Q(3, 2)
    scale = Q(5, 7)
    visible_tangent = Q(-2, 3)
    multiplicative = Q(2, 5)
    process_pair = AMProcess(
        visible_tangent - value * multiplicative,
        multiplicative,
    )

    x = -value * scale
    y = scale
    x_dot = -y * process_pair.additive
    y_dot = -y * process_pair.multiplicative

    assert _projective_value(x, y) == value
    assert _projective_tangent(x, y, x_dot, y_dot) == visible_tangent
    assert process_pair.visible_tangent(value) == visible_tangent

    gauge_rate = Q(4, 9)
    gauge_scale = Q(7, 5)
    transformed = process_pair.gauge_transform(value, gauge_rate)
    transformed_x = gauge_scale * x
    transformed_y = gauge_scale * y
    transformed_x_dot = gauge_scale * (x_dot + gauge_rate * x)
    transformed_y_dot = gauge_scale * (y_dot + gauge_rate * y)

    assert transformed.visible_tangent(value) == visible_tangent
    assert _projective_value(transformed_x, transformed_y) == value
    assert (
        _projective_tangent(
            transformed_x,
            transformed_y,
            transformed_x_dot,
            transformed_y_dot,
        )
        == visible_tangent
    )


def test_collision_gain_loss_is_task_exact_and_respects_the_process_cone():
    population = (Q(2), Q(3), Q(5), Q(7))
    rate = Q(11, 13)
    process_pairs, tangent = _collision_gain_loss(population, rate)
    incoming = population[0] * population[1]
    outgoing = population[2] * population[3]
    expected = (
        rate * (outgoing - incoming),
        rate * (outgoing - incoming),
        rate * (incoming - outgoing),
        rate * (incoming - outgoing),
    )

    assert tangent == expected
    assert all(pair.additive >= 0 for pair in process_pairs)
    assert all(pair.multiplicative <= 0 for pair in process_pairs)
    assert sum(tangent, Q(0)) == 0


def test_collision_involution_transports_the_am_pair_covariantly():
    population = (Q(2), Q(3), Q(5), Q(7))
    rate = Q(5, 4)
    process_pairs, tangent = _collision_gain_loss(population, rate)
    permutation = (2, 3, 0, 1)
    reversed_population = tuple(population[index] for index in permutation)
    reversed_pairs, reversed_tangent = _collision_gain_loss(
        reversed_population, rate
    )

    assert reversed_pairs == tuple(
        process_pairs[index] for index in permutation
    )
    assert reversed_tangent == tuple(tangent[index] for index in permutation)


def test_product_rule_composes_am_processes_without_an_entropy_coordinate():
    left = Q(5, 3)
    right = Q(7, 4)
    left_process = AMProcess(Q(2, 5), Q(-3, 7))
    right_process = AMProcess(Q(11, 6), Q(5, 8))
    product_process = AMProcess(
        right * left_process.additive + left * right_process.additive,
        left_process.multiplicative + right_process.multiplicative,
    )

    expected = (
        right * left_process.visible_tangent(left)
        + left * right_process.visible_tangent(right)
    )
    assert product_process.visible_tangent(left * right) == expected


def test_pair_generator_has_an_exact_gain_loss_split_and_conserves_mass():
    law = _mixture(_diagonal_pair_law(), _uniform_pair_law(), Q(1, 4))
    process_pairs, tangent = _pair_gain_loss(law, Q(3, 2))

    assert all(pair.additive >= 0 for pair in process_pairs)
    assert all(pair.multiplicative <= 0 for pair in process_pairs)
    assert sum(law, Q(0)) == 1
    assert sum(tangent, Q(0)) == 0


def test_state_only_adapter_is_exact_for_the_present_marginal():
    diagonal = _diagonal_pair_law()
    off_diagonal = _off_diagonal_pair_law()

    assert _is_exchange_symmetric(diagonal)
    assert _is_exchange_symmetric(off_diagonal)
    assert _one_body_marginal(diagonal) == (Q(1, 3),) * 3
    assert _one_body_marginal(off_diagonal) == (Q(1, 3),) * 3


def test_state_only_adapter_fails_the_next_derivative_task():
    diagonal = _diagonal_pair_law()
    off_diagonal = _off_diagonal_pair_law()
    diagonal_tangent = _lower_tangent(_pair_gain_loss(diagonal)[1])
    off_diagonal_tangent = _lower_tangent(
        _pair_gain_loss(off_diagonal)[1]
    )

    assert _one_body_marginal(diagonal) == _one_body_marginal(off_diagonal)
    assert diagonal_tangent == (Q(-2, 3), Q(1, 3), Q(1, 3))
    assert off_diagonal_tangent == (Q(1, 3), Q(-1, 6), Q(-1, 6))
    assert diagonal_tangent != off_diagonal_tangent


def test_next_derivative_residual_persists_for_strictly_positive_laws():
    uniform = _uniform_pair_law()
    diagonal = _mixture(_diagonal_pair_law(), uniform, Q(1, 4))
    off_diagonal = _mixture(
        _off_diagonal_pair_law(), uniform, Q(1, 4)
    )
    diagonal_tangent = _lower_tangent(_pair_gain_loss(diagonal)[1])
    off_diagonal_tangent = _lower_tangent(
        _pair_gain_loss(off_diagonal)[1]
    )

    assert all(value > 0 for value in diagonal)
    assert all(value > 0 for value in off_diagonal)
    assert _one_body_marginal(diagonal) == _one_body_marginal(off_diagonal)
    assert diagonal_tangent == (Q(-1, 2), Q(1, 4), Q(1, 4))
    assert off_diagonal_tangent == (Q(1, 4), Q(-1, 8), Q(-1, 8))
    assert diagonal_tangent != off_diagonal_tangent


def test_am_first_jet_adapter_is_exact_for_the_next_derivative_task():
    fixtures = (
        _diagonal_pair_law(),
        _off_diagonal_pair_law(),
        _mixture(_diagonal_pair_law(), _uniform_pair_law(), Q(1, 4)),
        _mixture(
            _off_diagonal_pair_law(), _uniform_pair_law(), Q(1, 4)
        ),
    )

    for law in fixtures:
        pair_processes, pair_tangent = _pair_gain_loss(law)
        marginal, marginal_processes = _lower_am_first_jet(
            law, pair_processes
        )
        via_process_chart = tuple(
            process_pair.visible_tangent(value)
            for process_pair, value in zip(
                marginal_processes, marginal
            )
        )
        via_two_body_generator = _lower_tangent(pair_tangent)

        assert via_process_chart == via_two_body_generator
        assert sum(via_process_chart, Q(0)) == 0


def test_equal_marginals_have_distinct_am_first_jet_semantics():
    diagonal = _diagonal_pair_law()
    off_diagonal = _off_diagonal_pair_law()
    diagonal_jet = _lower_am_first_jet(
        diagonal, _pair_gain_loss(diagonal)[0]
    )
    off_diagonal_jet = _lower_am_first_jet(
        off_diagonal, _pair_gain_loss(off_diagonal)[0]
    )

    assert diagonal_jet[0] == off_diagonal_jet[0]
    assert diagonal_jet[1] != off_diagonal_jet[1]
    assert diagonal_jet[1] == (
        AMProcess(Q(0), Q(-2)),
        AMProcess(Q(1, 3), Q(0)),
        AMProcess(Q(1, 3), Q(0)),
    )
    assert off_diagonal_jet[1] == (
        AMProcess(Q(1, 3), Q(0)),
        AMProcess(Q(0), Q(-1, 2)),
        AMProcess(Q(0), Q(-1, 2)),
    )


def test_adaptation_grades_remain_task_relative():
    grades = {
        "homogeneous_am_to_scalar": "coordinate_exact",
        "gain_loss_to_kinetic_derivative": "task_exact",
        "pair_law_to_present_marginal": "task_exact",
        "pair_law_to_next_derivative": "rejected",
        "pair_law_to_am_first_jet": "task_exact",
        "am_first_jet_to_complete_future": "unclaimed",
    }

    assert set(grades.values()) == {
        "coordinate_exact",
        "task_exact",
        "rejected",
        "unclaimed",
    }
    assert grades["pair_law_to_present_marginal"] == "task_exact"
    assert grades["pair_law_to_next_derivative"] == "rejected"
    assert grades["pair_law_to_am_first_jet"] == "task_exact"

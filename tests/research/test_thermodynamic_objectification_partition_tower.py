"""Finite thermodynamic objectification and partition-tower calibrations.

The tests isolate three operations that are easy to conflate:

1. a Boltzmann character turns serial addition of cost into multiplication;
2. a finite fibre sum turns alternative histories into a soft-min cost;
3. a plethystic exponential freely assembles already objectified processes.

Everything here is finite or a truncated formal-power-series identity.  The
tests do not define a framework API, prove a thermodynamic limit, or establish
an arithmetic hierarchy for general dynamical systems.
"""

from fractions import Fraction

import pytest
import sympy as sp


def _thermodynamic_sum(left, right, theta):
    return -theta * sp.log(
        sp.exp(-left / theta) + sp.exp(-right / theta)
    )


def _thermodynamic_product(left, right):
    return left + right


def _finite_free_energy(costs, weights, theta):
    partition = sum(
        weights[item] * sp.exp(-cost / theta)
        for item, cost in costs.items()
    )
    return -theta * sp.log(partition)


def _pushforward_free_energy(costs, fibres, weights, theta):
    targets = tuple(dict.fromkeys(fibres.values()))
    return {
        target: _finite_free_energy(
            {
                item: cost
                for item, cost in costs.items()
                if fibres[item] == target
            },
            {
                item: weights[item]
                for item in costs
                if fibres[item] == target
            },
            theta,
        )
        for target in targets
    }


def _truncated_plethystic_exponential(
    primitive_series,
    grading,
    order,
    *,
    adams_variables=(),
):
    """Return PE[f] modulo ``grading**(order + 1)``.

    A formal plethystic exponential requires a vanishing degree-zero term.
    Otherwise the vacuum can be selected with arbitrary multiplicity and even
    the constant coefficient is an infinite sum.
    """

    constant_term = sp.expand(primitive_series).subs(grading, 0)
    if sp.simplify(constant_term) != 0:
        raise ValueError("plethystic input must have zero vacuum term")

    variables = tuple(dict.fromkeys((grading, *adams_variables)))
    exponent = 0
    for multiplicity in range(1, order + 1):
        adams = {
            variable: variable**multiplicity
            for variable in variables
        }
        exponent += primitive_series.subs(adams, simultaneous=True) / multiplicity

    return sp.series(
        sp.exp(exponent), grading, 0, order + 1
    ).removeO().expand()


def _unit_cell(cost, unit):
    quotient = cost // unit
    return quotient, cost - quotient * unit


def _compose_unit_cells(left, right, unit):
    left_grade, left_residual = left
    right_grade, right_residual = right
    carry, residual = _unit_cell(left_residual + right_residual, unit)
    return left_grade + right_grade + carry, residual


def test_boltzmann_character_realizes_the_thermodynamic_semiring():
    left, right, theta = sp.symbols("x y theta", positive=True)
    weight = lambda cost: sp.exp(-cost / theta)

    assert sp.simplify(
        weight(_thermodynamic_sum(left, right, theta))
        - (weight(left) + weight(right))
    ) == 0
    assert sp.simplify(
        weight(_thermodynamic_product(left, right))
        - weight(left) * weight(right)
    ) == 0

    third = sp.symbols("z", positive=True)
    left_distributive = _thermodynamic_product(
        left, _thermodynamic_sum(right, third, theta)
    )
    right_distributive = _thermodynamic_sum(
        _thermodynamic_product(left, right),
        _thermodynamic_product(left, third),
        theta,
    )
    assert sp.simplify(weight(left_distributive) - weight(right_distributive)) == 0


def test_zero_temperature_degenerates_to_min_plus():
    theta, lower, gap = sp.symbols(
        "theta lower gap", positive=True
    )
    soft_min = lower - theta * sp.log(1 + sp.exp(-gap / theta))

    assert sp.simplify(
        _thermodynamic_sum(lower, lower + gap, theta) - soft_min
    ) == 0
    assert sp.limit(soft_min, theta, 0, dir="+") == lower
    assert _thermodynamic_product(lower, lower + gap) == 2 * lower + gap


def test_same_scale_objectification_flattens_exactly_with_composed_measure():
    theta = sp.symbols("theta", positive=True)
    costs = {
        "a": sp.symbols("C_a", positive=True),
        "b": sp.symbols("C_b", positive=True),
        "c": sp.symbols("C_c", positive=True),
        "d": sp.symbols("C_d", positive=True),
    }
    inner_weights = {
        item: sp.symbols(f"mu_{item}", positive=True)
        for item in costs
    }
    inner_fibres = {"a": "u", "b": "u", "c": "v", "d": "w"}
    outer_fibres = {"u": "left", "v": "left", "w": "right"}
    outer_weights = {
        target: sp.symbols(f"q_{target}", positive=True)
        for target in outer_fibres
    }

    first_push = _pushforward_free_energy(
        costs, inner_fibres, inner_weights, theta
    )
    nested_push = _pushforward_free_energy(
        first_push, outer_fibres, outer_weights, theta
    )

    composite_fibres = {
        item: outer_fibres[inner_fibres[item]]
        for item in costs
    }
    composite_weights = {
        item: inner_weights[item] * outer_weights[inner_fibres[item]]
        for item in costs
    }
    direct_push = _pushforward_free_energy(
        costs, composite_fibres, composite_weights, theta
    )

    for target in direct_push:
        nested_weight = sp.exp(-nested_push[target] / theta)
        direct_weight = sp.exp(-direct_push[target] / theta)
        assert sp.simplify(nested_weight - direct_weight) == 0


def test_outer_measure_must_be_pulled_back_before_flattening():
    theta = sp.Integer(1)
    costs = {"a": sp.Integer(0), "b": sp.Integer(0)}
    inner_fibres = {"a": "u", "b": "v"}
    outer_fibres = {"u": "point", "v": "point"}
    inner_weights = {"a": sp.Integer(1), "b": sp.Integer(1)}
    outer_weights = {"u": sp.Integer(1), "v": sp.Integer(2)}

    first_push = _pushforward_free_energy(
        costs, inner_fibres, inner_weights, theta
    )
    nested = _pushforward_free_energy(
        first_push, outer_fibres, outer_weights, theta
    )["point"]
    naive_direct = _finite_free_energy(costs, inner_weights, theta)
    corrected_direct = _finite_free_energy(
        costs,
        {
            item: inner_weights[item] * outer_weights[inner_fibres[item]]
            for item in costs
        },
        theta,
    )

    assert sp.exp(-nested) == 3
    assert sp.exp(-naive_direct) == 2
    assert sp.exp(-corrected_direct) == sp.exp(-nested)


def test_different_scales_produce_a_power_sum_not_same_scale_flattening():
    inner_scale, outer_scale = sp.symbols(
        "theta_0 theta_1", positive=True
    )
    first_partition, second_partition = sp.symbols(
        "Z_1 Z_2", positive=True
    )
    first_weight, second_weight = sp.symbols("q_1 q_2", positive=True)

    inner_free_energies = {
        "one": -inner_scale * sp.log(first_partition),
        "two": -inner_scale * sp.log(second_partition),
    }
    outer = _finite_free_energy(
        inner_free_energies,
        {"one": first_weight, "two": second_weight},
        outer_scale,
    )
    expected = -outer_scale * sp.log(
        first_weight * first_partition ** (inner_scale / outer_scale)
        + second_weight * second_partition ** (inner_scale / outer_scale)
    )
    assert sp.simplify(
        sp.exp(-outer / outer_scale)
        - sp.exp(-expected / outer_scale)
    ) == 0

    # At equal scales the exponent is one and the hierarchy flattens.  A real
    # scale ratio changes the aggregation law; regrouping alone does not.
    assert sp.simplify(
        sp.exp(-outer.subs(inner_scale, outer_scale) / outer_scale)
        - (first_weight * first_partition + second_weight * second_partition)
    ) == 0
    unequal = sp.exp(-outer.subs(
        {inner_scale: 2, outer_scale: 1, first_weight: 1, second_weight: 1,
         first_partition: 1, second_partition: 2}
    ))
    assert sp.simplify(unequal - 5) == 0


def test_unit_rescaling_is_not_a_new_thermodynamic_level():
    theta, unit_scale = sp.symbols("theta lambda", positive=True)
    costs = {"a": sp.Integer(2), "b": sp.Integer(5)}
    weights = {"a": sp.Rational(1, 3), "b": sp.Rational(2, 3)}

    original = _finite_free_energy(costs, weights, theta)
    rescaled = _finite_free_energy(
        {item: unit_scale * cost for item, cost in costs.items()},
        weights,
        unit_scale * theta,
    )
    assert sp.simplify(
        sp.exp(-rescaled / (unit_scale * theta))
        - sp.exp(-original / theta)
    ) == 0
    assert sp.simplify(rescaled - unit_scale * original) == 0


def test_declared_unit_discretizes_additive_cost_with_a_carry_residual():
    unit = Fraction(2)
    left_cost = Fraction(5, 2)
    right_cost = Fraction(7, 4)
    left_cell = _unit_cell(left_cost, unit)
    right_cell = _unit_cell(right_cost, unit)
    composite_cell = _unit_cell(left_cost + right_cost, unit)

    assert left_cell == (1, Fraction(1, 2))
    assert right_cell == (0, Fraction(7, 4))
    assert composite_cell == (2, Fraction(1, 4))
    assert _compose_unit_cells(left_cell, right_cell, unit) == composite_cell

    # The integer grade alone is additive only on the exact cost lattice.
    assert left_cell[0] + right_cell[0] != composite_cell[0]
    lattice_left = _unit_cell(Fraction(4), unit)
    lattice_right = _unit_cell(Fraction(6), unit)
    assert lattice_left[1] == lattice_right[1] == 0
    assert _compose_unit_cells(
        lattice_left, lattice_right, unit
    ) == _unit_cell(Fraction(10), unit)


def test_partition_cumulant_recovers_the_existing_frontier_cost():
    beta = sp.symbols("beta", real=True)
    probabilities = (
        sp.Rational(1, 2),
        sp.Rational(1, 3),
        sp.Rational(1, 6),
    )
    stopping_costs = (sp.Integer(2), sp.Integer(2), sp.Integer(3))
    partition = sum(
        probability * sp.exp(-beta * cost)
        for probability, cost in zip(probabilities, stopping_costs)
    )
    expected_cost = sum(
        probability * cost
        for probability, cost in zip(probabilities, stopping_costs)
    )
    variance = sum(
        probability * (cost - expected_cost) ** 2
        for probability, cost in zip(probabilities, stopping_costs)
    )
    edges = (
        (sp.Integer(2), (0,)),
        (sp.Rational(1, 2), (1, 2)),
        (sp.Rational(3, 2), (1,)),
        (sp.Rational(5, 2), (2,)),
    )
    derived_stopping_costs = tuple(
        sum(
            edge_cost
            for edge_cost, descendant_leaves in edges
            if leaf in descendant_leaves
        )
        for leaf in range(len(probabilities))
    )
    edge_frontier_volume = sum(
        edge_cost
        * sum(probabilities[leaf] for leaf in descendant_leaves)
        for edge_cost, descendant_leaves in edges
    )
    breakpoints = sorted({sp.Integer(0), *stopping_costs})
    layer_cake_volume = sum(
        (right - left)
        * sum(
            probability
            for probability, cost in zip(probabilities, stopping_costs)
            if cost > left
        )
        for left, right in zip(breakpoints, breakpoints[1:])
    )

    assert partition.subs(beta, 0) == 1
    assert derived_stopping_costs == stopping_costs
    assert sp.simplify(
        -sp.diff(sp.log(partition), beta).subs(beta, 0) - expected_cost
    ) == 0
    assert expected_cost == sp.Rational(13, 6)
    assert edge_frontier_volume == expected_cost
    assert layer_cake_volume == expected_cost
    assert sp.simplify(
        sp.diff(sp.log(partition), beta, 2).subs(beta, 0) - variance
    ) == 0


def test_plethystic_exponential_calibrates_free_multiset_assembly():
    q = sp.symbols("q")
    order = 7

    one_primitive = _truncated_plethystic_exponential(q, q, order)
    assert one_primitive == sum(q**degree for degree in range(order + 1))

    positive_degree_primitives = q / (1 - q)
    partitions = _truncated_plethystic_exponential(
        positive_degree_primitives, q, order
    )
    expected_partition_numbers = (1, 1, 2, 3, 5, 7, 11, 15)
    assert tuple(
        partitions.coeff(q, degree)
        for degree in range(order + 1)
    ) == expected_partition_numbers


def test_objectification_rank_is_visible_only_if_bracketing_is_retained():
    q, inner_fugacity, outer_fugacity = sp.symbols("q u v")
    order = 4
    lower_partition = 1 + q
    rank_one = _truncated_plethystic_exponential(
        inner_fugacity * (lower_partition - 1),
        q,
        order,
        adams_variables=(inner_fugacity,),
    )
    rank_two = _truncated_plethystic_exponential(
        outer_fugacity * (rank_one - 1),
        q,
        order,
        adams_variables=(inner_fugacity, outer_fugacity),
    )

    assert rank_one.coeff(q, 2) == inner_fugacity**2
    assert sp.expand(rank_two).coeff(q, 2) == (
        inner_fugacity**2 * outer_fugacity
        + inner_fugacity**2 * outer_fugacity**2
    )

    # One rank-one object of size two and two rank-one objects of size one are
    # distinct only while the outer assembly boundary is task-visible.
    assert rank_two.subs(outer_fugacity, 1).coeff(q, 2) == 2 * inner_fugacity**2
    assert rank_one.coeff(q, 2) == inner_fugacity**2


def test_vacuum_must_be_removed_before_free_assembly():
    q = sp.symbols("q")
    with pytest.raises(ValueError, match="zero vacuum term"):
        _truncated_plethystic_exponential(1 + q, q, 4)

    assert _truncated_plethystic_exponential((1 + q) - 1, q, 4) == sum(
        q**degree for degree in range(5)
    )

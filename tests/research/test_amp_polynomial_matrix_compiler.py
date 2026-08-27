"""Exact and numerical audit of the AMP polynomial/matrix compiler."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys

import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/amp-polynomial-matrix-compiler/amp_escape_compiler.py"
)
SPEC = importlib.util.spec_from_file_location("amp_escape_compiler", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_sparse_matrix_is_exact_substitution_on_the_amp_ray_basis():
    q = sp.symbols("q")
    degree = 3
    interaction = sp.Rational(2, 3)
    order = 18
    g = q**degree / (1 + interaction * q**degree)

    matrix = module.build_substitution_matrix(
        degree,
        Fraction(2, 3),
        order,
    )
    entries = {(row, column): value for row, column, value in matrix.entries}

    for column in range(1, order + 1):
        expanded = sp.series(g**column, q, 0, order + 1).removeO().expand()
        for row in range(1, order + 1):
            expected = expanded.coeff(q, row)
            actual = entries.get((row, column), Fraction(0))
            assert expected == sp.Rational(actual.numerator, actual.denominator)


def test_substitution_matrix_is_nilpotent_at_a_finite_observer():
    matrix = module.build_substitution_matrix(2, 1, 20)
    vector = (Fraction(1),) + (Fraction(0),) * 19

    for _ in range(matrix.nilpotence_index_bound - 1):
        vector = matrix.apply(vector)
    assert any(vector)

    vector = matrix.apply(vector)
    assert not any(vector)
    assert matrix.nilpotence_index_bound == 5


def test_compiled_coordinate_solves_the_exact_finite_eigenproblem():
    certificate = module.compile_escape_coordinate(2, 1, 10)
    nonzero = {
        degree: coefficient
        for degree, coefficient in enumerate(
            certificate.coordinate.coefficients,
            start=1,
        )
        if coefficient
    }

    assert nonzero == {
        2: Fraction(1, 2),
        6: Fraction(-1, 3),
        8: Fraction(5, 8),
        10: Fraction(-9, 10),
    }
    assert certificate.replay_eigenrelation()
    assert certificate.first_omitted_residual == module.ResidualTerm(
        degree=12,
        coefficient=Fraction(2),
    )


def test_polynomial_like_support_avoids_expanded_iterate_growth():
    x = sp.symbols("x")

    for degree, maximum_iteration in ((2, 5), (3, 3)):
        iterate = x
        for iteration in range(maximum_iteration + 1):
            actual_terms = len(sp.Poly(sp.expand(iterate), x).terms())
            expected_terms = module.expanded_symbolic_term_count(
                degree,
                1,
                iteration,
            )
            assert actual_terms == expected_terms
            iterate = sp.expand(iterate**degree + 1)

    assert module.expanded_symbolic_term_count(2, 1, 100) == 2**99 + 1


def test_compiled_coordinate_converges_to_the_strong_log_recurrence_baseline():
    initial_log_state = 1.5
    direct = module.direct_normalized_log_iteration(
        2,
        1,
        initial_log_state,
        200,
    )

    errors = []
    for order in (6, 10, 14, 20):
        coordinate = module.compile_escape_coordinate(2, 1, order).coordinate
        errors.append(abs(coordinate.evaluate(initial_log_state) - direct))

    assert errors[0] < 4e-6
    assert errors[1] < 2e-8
    assert errors[2] < 5e-11
    assert errors[3] < 5e-13
    assert errors == sorted(errors, reverse=True)


def test_sparse_cost_is_reported_without_hiding_the_strong_baseline():
    report = module.benchmark_report(
        degree=2,
        interaction=1,
        observer_order=20,
        horizon=100,
        queries=100,
        initial_log_state=1.5,
    )

    assert report.compilation_cost == {
        "observer_order": 20,
        "dense_matrix_entries": 400,
        "sparse_matrix_entries": 55,
        "coordinate_terms": 9,
        "triangular_divisions": 20,
    }
    assert report.expanded_symbolic_terms == 2**99 + 1
    assert report.compiled_online_series_terms == 900
    # The strong numerical baseline detects underflow of the correction and
    # stops early; the compiler therefore does not receive a false O(100)
    # per-query advantage on this floating-point task.
    assert report.direct_recurrence_steps < 2_000
    assert report.absolute_error < 5e-13
    assert report.first_omitted_residual == (22, "144/11")


def test_asymptotic_chart_failure_is_not_hidden_by_higher_order():
    initial_log_state = 0.0
    direct = module.direct_normalized_log_iteration(2, 1, initial_log_state, 200)
    order_14 = module.compile_escape_coordinate(2, 1, 14).coordinate.evaluate(
        initial_log_state
    )
    order_20 = module.compile_escape_coordinate(2, 1, 20).coordinate.evaluate(
        initial_log_state
    )

    error_14 = abs(order_14 - direct)
    error_20 = abs(order_20 - direct)
    assert error_14 < 0.06
    assert error_20 > 4.0
    assert error_20 > error_14


def test_invalid_or_cancellation_prone_tasks_fail_closed():
    for args in ((1, 1, 10), (2, 0, 10), (2, -1, 10), (2, 1, 0)):
        try:
            module.build_substitution_matrix(*args)
        except ValueError:
            pass
        else:  # pragma: no cover
            raise AssertionError(f"invalid compiler task was accepted: {args}")

    try:
        module.expanded_symbolic_term_count(2, -1, 5)
    except ValueError:
        pass
    else:  # pragma: no cover
        raise AssertionError("a cancellation-prone term count was accepted")

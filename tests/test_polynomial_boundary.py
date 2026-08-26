"""Regression contract for the repository's literal polynomial vocabulary.

These tests keep three neighboring notions separate:

* a polynomial is a finite-support expression in declared indeterminates;
* the A/M power-weight and resonant families may contain non-polynomial
  functions and therefore are not polynomial modules;
* process histories and task quotients are different semantic objects again.
"""

from __future__ import annotations

import pytest
import sympy as sp

from process_geometry.analysis.am import AMFunctionTheory
from process_geometry.analysis.module import polynomial_am_module
from process_geometry.discovery import PolynomialInvariant, PolynomialObservableBasis
from process_geometry.presentation.constraints import AlgebraicConstraintSet


def _non_polynomial_expressions(x: sp.Symbol) -> tuple[sp.Expr, ...]:
    n = sp.Symbol("n", integer=True, nonnegative=True)
    return (
        sp.exp(x),
        sp.sin(x),
        x**-1,
        1 / (1 - x),
        sp.Sum(x**n, (n, 0, sp.oo)),
    )


def test_polynomial_observable_basis_stores_a_finite_expanded_normal_form():
    x, parameter = sp.symbols("x parameter")
    basis = PolynomialObservableBasis(
        expressions=((x + 1) * (x - 1), parameter * x),
        max_degree=2,
        raw_candidate_count=2,
        quotient_reduced=False,
        variables=(x,),
    )

    assert basis.variables == (x,)
    assert basis.expressions == (x**2 - 1, parameter * x)
    assert all(sp.Poly(expression, x) for expression in basis.expressions)


@pytest.mark.parametrize("expression_index", range(5))
def test_polynomial_observable_basis_rejects_non_polynomial_function_families(
    expression_index: int,
):
    x = sp.Symbol("x")
    expression = _non_polynomial_expressions(x)[expression_index]

    with pytest.raises(ValueError, match="finite polynomial"):
        PolynomialObservableBasis(
            expressions=(expression,),
            max_degree=3,
            raw_candidate_count=1,
            quotient_reduced=False,
            variables=(x,),
        )


def test_compatibility_construction_infers_symbols_before_validation():
    x = sp.Symbol("x")

    with pytest.raises(ValueError, match="finite polynomial"):
        PolynomialObservableBasis(
            expressions=(sp.exp(x),),
            max_degree=3,
            raw_candidate_count=1,
            quotient_reduced=False,
        )


@pytest.mark.parametrize("expression_index", range(5))
def test_polynomial_invariant_rejects_non_polynomial_expressions(
    expression_index: int,
):
    x = sp.Symbol("x")
    expression = _non_polynomial_expressions(x)[expression_index]

    with pytest.raises(ValueError, match="finite polynomial"):
        PolynomialInvariant(
            expression=expression,
            coordinates=(1,),
            derivative_remainder=0,
            variables=(x,),
        )


@pytest.mark.parametrize("expression_index", range(5))
def test_algebraic_constraints_reject_non_polynomials_eagerly(expression_index: int):
    x = sp.Symbol("x")
    expression = _non_polynomial_expressions(x)[expression_index]

    with pytest.raises(ValueError, match="finite polynomial"):
        AlgebraicConstraintSet((x,), (expression,))


def test_empty_constraint_quotient_still_rejects_non_polynomial_reduction():
    x = sp.Symbol("x")
    quotient = AlgebraicConstraintSet((x,), ())

    with pytest.raises(ValueError, match="finite polynomial"):
        quotient.reduce(sp.exp(x))


def test_polynomial_am_module_is_finite_and_separate_from_general_am_functions():
    a, v, weight = sp.symbols("a v weight")
    module = polynomial_am_module(a, 4)

    assert module.basis == (1, a, a**2, a**3, a**4)
    assert all(sp.Poly(expression, a).degree() <= 4 for expression in module.basis)

    power_weight = AMFunctionTheory(a, v).power_weight(2, weight)
    assert power_weight.expression.has(sp.exp)
    with pytest.raises(sp.PolynomialError):
        sp.Poly(power_weight.expression, a, v)


def test_polynomial_am_module_rejects_a_non_symbol_indeterminate():
    x = sp.Symbol("x")

    with pytest.raises(TypeError, match="indeterminate"):
        polynomial_am_module(sp.exp(x), 3)

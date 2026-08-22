import sympy as sp

from aeg_shakespeare.presentation.grammar import (
    discover_generated_grammar,
    discover_generated_presentation,
)
from aeg_shakespeare.presentation.search import SearchBudget
from aeg_shakespeare.process.local import ProcessSystem


def recurrent_system():
    x, p = sp.symbols("x p")
    return x, p, ProcessSystem((x, p), {x: p, p: -x}, name="R")


def proportional(left, right, variables):
    left_poly = sp.Poly(sp.expand(left), *variables)
    right_poly = sp.Poly(sp.expand(right), *variables)
    monomials = sorted(set(left_poly.monoms()) | set(right_poly.monoms()), reverse=True)
    left_vector = sp.Matrix([left_poly.coeff_monomial(m) for m in monomials])
    right_vector = sp.Matrix([right_poly.coeff_monomial(m) for m in monomials])
    return left_vector != sp.zeros(len(monomials), 1) and sp.Matrix.hstack(
        left_vector, right_vector
    ).rank() == 1


def test_generated_presentation_needs_neither_ambient_basis_nor_relation_template():
    x, p, system = recurrent_system()
    budget = SearchBudget(
        max_history_depth=8,
        max_expression_degree=3,
        max_relation_order=8,
        max_new_primitives=8,
    )

    presentation = discover_generated_presentation(system, (x**3,), budget=budget)
    assert presentation.complete
    assert presentation.grammar.dimension == 4
    assert presentation.grammar.growth_profile() == (1, 2, 3, 4)
    assert presentation.relations is not None

    D = sp.Symbol("D")
    assert sp.expand(
        presentation.relations.global_relation.as_expr(D)
        - (D**4 + 10 * D**2 + 9)
    ) == 0
    factors = {
        sp.expand(component.as_expr(D))
        for component in presentation.relations.components
    }
    assert factors == {D**2 + 1, D**2 + 9}

    assert any(
        proportional(primitive, x**3 - 3 * x * p**2, (x, p))
        for primitive in presentation.primitives
    )
    assert any(
        proportional(primitive, 3 * x**2 * p - p**3, (x, p))
        for primitive in presentation.primitives
    )

    decoder = presentation.seed_coordinates[0]
    reconstructed = sp.expand(
        sum(
            coefficient * primitive
            for coefficient, primitive in zip(decoder, presentation.primitives)
        )
    )
    assert sp.expand(reconstructed - x**3) == 0


def test_generated_grammar_exposes_nonlinear_growth_as_residual_not_projection():
    x = sp.Symbol("x")
    system = ProcessSystem((x,), {x: x**2}, name="G")
    budget = SearchBudget(
        max_history_depth=5,
        max_expression_degree=3,
        max_relation_order=5,
        max_new_primitives=8,
    )

    grammar = discover_generated_grammar(system, (x,), budget=budget)
    assert not grammar.closed
    assert grammar.dimension == 3
    assert grammar.growth_profile() == (1, 2, 3)
    assert tuple(sp.expand(item) for item in grammar.basis) == (x, x**2, 2 * x**3)
    assert len(grammar.residuals) == 1
    assert sp.expand(grammar.residuals[0] - 6 * x**4) == 0

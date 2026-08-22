import sympy as sp

from aeg_shakespeare.core import homogeneous_monomials
from aeg_shakespeare.linear import discover_krylov_relation
from aeg_shakespeare.presentation.relations import (
    coefficient_vector,
    decompose,
    discover_operator_relation,
    discover_relation_decomposition,
    discover_relation_kernel,
    discover_return_relation,
    factor_process_relation,
)
from aeg_shakespeare.presentation.search import PresentationCost, SearchBudget
from aeg_shakespeare.process.history import ProcessWord, interpret_history
from aeg_shakespeare.process.local import ProcessSystem


def test_process_word_interpreter_supports_affine_calibration_without_affine_api():
    history = ProcessWord(("add_a", "scale_s", "add_b"))
    a, b, s, x = sp.symbols("a b s x")

    def transition(state, step):
        if step == "add_a":
            return sp.expand(state + a)
        if step == "scale_s":
            return sp.expand(s * state)
        if step == "add_b":
            return sp.expand(state + b)
        raise ValueError(step)

    result = interpret_history(history, x, transition)
    assert sp.expand(result - (s * x + s * a + b)) == 0


def oscillator():
    x, p = sp.symbols("x p")
    return x, p, ProcessSystem((x, p), {x: p, p: -x}, name="R")


def test_return_relation_api_discovers_oscillator_calibration():
    x, _, system = oscillator()
    relation = discover_return_relation(system, x, max_order=4)
    assert relation is not None
    assert relation.order == 2
    D = sp.Symbol("D")
    assert sp.expand(relation.as_expr(D) - (1 + D**2)) == 0


def test_coordinate_backend_accepts_discovered_composite_grammars():
    x, p = sp.symbols("x p")
    basis = (x + p, x - p)
    coordinates = coefficient_vector(x, basis, (x, p))
    assert tuple(coordinates) == (sp.Rational(1, 2), sp.Rational(1, 2))


def test_generic_relation_kernel_recovers_degree_three_calibration():
    x, p, system = oscillator()
    basis = homogeneous_monomials((x, p), 3)

    discovered = {}
    for rate in range(1, 5):
        kernel = discover_relation_kernel(system, basis, (rate**2, 0, 1))
        if kernel.primitives:
            discovered[rate] = kernel

    assert set(discovered) == {1, 3}
    for rate, kernel in discovered.items():
        for primitive in kernel.primitives:
            assert sp.expand(system.derive(system.derive(primitive)) + rate**2 * primitive) == 0


def test_relation_decomposition_discovers_invariant_without_relation_template():
    x, p, system = oscillator()
    basis = homogeneous_monomials((x, p), 2)
    discovery = discover_relation_decomposition(system, basis)
    assert discovery is not None
    assert discovery.complete

    D = sp.Symbol("D")
    assert sp.expand(discovery.global_relation.as_expr(D) - (D**3 + 4 * D)) == 0
    factors = {sp.expand(component.as_expr(D)) for component in discovery.components}
    assert factors == {D, D**2 + 4}

    primitives = discovery.primitives
    assert any(sp.expand(primitive - (x**2 + p**2)) == 0 for primitive in primitives)


def test_relation_decomposition_finds_cubic_process_language_without_templates():
    x, p, system = oscillator()
    basis = homogeneous_monomials((x, p), 3)
    discovery = discover_relation_decomposition(system, basis)
    assert discovery is not None
    assert discovery.complete

    D = sp.Symbol("D")
    assert sp.expand(
        discovery.global_relation.as_expr(D) - (D**4 + 10 * D**2 + 9)
    ) == 0
    factors = {sp.expand(component.as_expr(D)) for component in discovery.components}
    assert factors == {D**2 + 1, D**2 + 9}

    coeffs = decompose(x**3, discovery.primitives, (x, p))
    reconstructed = sp.expand(
        sum(coefficient * primitive for coefficient, primitive in zip(coeffs, discovery.primitives))
    )
    assert sp.expand(reconstructed - x**3) == 0

    assert any(
        sp.expand(primitive - (x**3 - 3 * x * p**2)) == 0
        for primitive in discovery.primitives
    )
    assert any(
        sp.expand(primitive - (3 * x**2 * p - p**3)) == 0
        for primitive in discovery.primitives
    )


def test_relation_factorization_retains_repeated_process_depth():
    operator = sp.Matrix([[1, 1], [0, 1]])
    relation = discover_operator_relation(operator)
    assert relation is not None

    D = sp.Symbol("D")
    assert sp.expand(relation.as_expr(D) - (D**2 - 2 * D + 1)) == 0
    factors = factor_process_relation(relation)
    assert len(factors) == 1
    assert sp.expand(factors[0].as_expr(D) - (D**2 - 2 * D + 1)) == 0


def test_duffing_expression_is_only_a_calibration_of_generic_decompose():
    x, p, system = oscillator()
    basis = homogeneous_monomials((x, p), 3)
    primitives = []
    for rate in (1, 3):
        primitives.extend(
            discover_relation_kernel(system, basis, (rate**2, 0, 1)).primitives
        )

    coeffs = decompose(x**3, primitives, (x, p))
    reconstructed = sp.expand(sum(c * q for c, q in zip(coeffs, primitives)))
    assert sp.expand(reconstructed - x**3) == 0


def test_krylov_backend_recovers_return_relation_before_spectrum():
    X = sp.Matrix([[0, -1], [1, 0]])
    v = sp.Matrix([1, 0])
    relation = discover_krylov_relation(X, v)
    assert relation is not None
    z = sp.Symbol("X")
    assert sp.expand(relation.as_polynomial(z) - (1 + z**2)) == 0


def test_budget_and_cost_are_public_problem_independent_objects():
    budget = SearchBudget(max_history_depth=4, max_expression_degree=3)
    assert budget.max_history_depth == 4

    cheaper = PresentationCost(grammar=2, relations=1, history=3, decoder=1)
    expensive = PresentationCost(grammar=3, relations=1, history=4, decoder=1)
    assert cheaper.dominates(expensive)
    assert cheaper.scalarize() == 7

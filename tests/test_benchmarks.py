import sympy as sp

from aeg_shakespeare import (
    PresentationCost,
    ProcessSystem,
    ProcessWord,
    SearchBudget,
    decompose,
    discover_krylov_relation,
    discover_relation_kernel,
    discover_return_relation,
    homogeneous_monomials,
    interpret_history,
)


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

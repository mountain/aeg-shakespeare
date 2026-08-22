import sympy as sp

from aeg_shakespeare.discovery import (
    discover_first_order_process_quotient,
    discover_polynomial_invariants,
    generate_polynomial_observer_basis,
)
from aeg_shakespeare.presentation.constraints import AlgebraicConstraintSet
from aeg_shakespeare.process.local import ProcessSystem


def _same_relation_up_to_scalar(left, right):
    ratio = sp.cancel(sp.expand(left) / sp.expand(right))
    return ratio != 0 and not ratio.free_symbols


def test_polynomial_observer_basis_removes_constraint_redundancy():
    x, y = sp.symbols("x y")
    circle = AlgebraicConstraintSet((x, y), (x**2 + y**2 - 1,))

    basis = generate_polynomial_observer_basis(
        (x, y),
        max_degree=2,
        constraints=circle,
        include_constant=True,
    )

    assert basis.raw_candidate_count == 6
    assert len(basis.expressions) == 5
    assert basis.quotient_reduced


def test_polynomial_invariant_discovery_recovers_oscillator_energy_without_template():
    x, p = sp.symbols("x p")
    oscillator = ProcessSystem((x, p), {x: p, p: -x})

    result = discover_polynomial_invariants(oscillator, max_degree=2)

    assert len(result.invariants) == 1
    invariant = result.invariants[0]
    assert invariant.certified
    assert sp.expand(invariant.expression - (x**2 + p**2)) == 0


def test_first_order_process_quotient_eliminates_source_assignments_exactly():
    x, y, R, U, Y = sp.symbols("x y R U Y")
    rotation = ProcessSystem((x, y), {x: y, y: -x})
    leaf = AlgebraicConstraintSet((x, y, R), (x**2 + y**2 - R,))

    quotient = discover_first_order_process_quotient(
        rotation,
        x,
        observable_symbol=U,
        derivative_symbol=Y,
        constraints=leaf,
        parameters=(R,),
    )

    assert quotient.complete_certificates
    assert len(quotient.relations) == 1
    assert _same_relation_up_to_scalar(
        quotient.relations[0].relation,
        U**2 + Y**2 - R,
    )

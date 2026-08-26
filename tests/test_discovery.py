import sympy as sp

from process_geometry.discovery import (
    discover_first_order_observable_image,
    discover_polynomial_invariants,
    generate_polynomial_observable_basis,
)
from process_geometry.presentation.constraints import AlgebraicConstraintSet
from process_geometry.process.local import ProcessSystem


def _same_relation_up_to_scalar(left, right):
    ratio = sp.cancel(sp.expand(left) / sp.expand(right))
    return ratio != 0 and not ratio.free_symbols


def test_polynomial_observable_basis_removes_constraint_redundancy():
    x, y = sp.symbols("x y")
    circle = AlgebraicConstraintSet((x, y), (x**2 + y**2 - 1,))

    basis = generate_polynomial_observable_basis(
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

    assert result.observable_basis is result.observer_basis
    assert len(result.invariants) == 1
    invariant = result.invariants[0]
    assert invariant.certified
    assert sp.expand(invariant.expression - (x**2 + p**2)) == 0


def test_first_order_observable_image_eliminates_source_assignments_exactly():
    x, y, R, U, Y = sp.symbols("x y R U Y")
    rotation = ProcessSystem((x, y), {x: y, y: -x})
    leaf = AlgebraicConstraintSet((x, y, R), (x**2 + y**2 - R,))

    image = discover_first_order_observable_image(
        rotation,
        x,
        observable_symbol=U,
        derivative_symbol=Y,
        constraints=leaf,
        parameters=(R,),
    )

    assert image.complete_certificates
    assert len(image.relations) == 1
    assert _same_relation_up_to_scalar(
        image.relations[0].relation,
        U**2 + Y**2 - R,
    )

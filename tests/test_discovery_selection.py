import sympy as sp

from aeg_shakespeare import (
    AlgebraicConstraintSet,
    ProcessSystem,
    search_first_order_process_quotients,
)


def test_first_order_observer_search_reuses_pareto_presentation_costs():
    x, y, R = sp.symbols("x y R")
    rotation = ProcessSystem((x, y), {x: y, y: -x})
    circle_leaf = AlgebraicConstraintSet((x, y, R), (x**2 + y**2 - R,))

    result = search_first_order_process_quotients(
        rotation,
        (x, x**2),
        constraints=circle_leaf,
        parameters=(R,),
    )

    assert len(result.evaluated) == 2
    assert all(candidate.sufficient for candidate in result.evaluated)
    assert all(candidate.payload.algebraically_closed for candidate in result.evaluated)

    linear, quadratic = result.evaluated
    assert linear.cost.relations == quadratic.cost.relations
    assert linear.cost.grammar < quadratic.cost.grammar
    assert result.pareto == (linear,)

import sympy as sp

from aeg_shakespeare.central import (
    ProcessCocycle,
    central_commutator_residual,
    verify_process_cocycle,
)
from aeg_shakespeare.families import ProcessFamily


def _pair_add(left, right):
    return (
        sp.expand(left[0] + right[0]),
        sp.expand(left[1] + right[1]),
    )


def test_process_cocycle_verifies_associative_lifted_composition():
    ax, ay, bx, by, cx, cy, kappa = sp.symbols(
        "a_x a_y b_x b_y c_x c_y kappa",
        real=True,
    )
    a = (ax, ay)
    b = (bx, by)
    c = (cx, cy)

    family = ProcessFamily("T2", _pair_add, identity=(sp.S.Zero, sp.S.Zero))
    cocycle = ProcessCocycle(
        family,
        lambda left, right: sp.expand(
            kappa * (left[0] * right[1] - left[1] * right[0]) / 2
        ),
    )

    certificate = verify_process_cocycle(
        cocycle,
        ((a, b, c),),
        normalization_parameters=(a,),
    )
    assert certificate.exact

    left_assoc = cocycle.compose_lifted(
        cocycle.compose_lifted((a, sp.S.Zero), (b, sp.S.Zero)),
        (c, sp.S.Zero),
    )
    right_assoc = cocycle.compose_lifted(
        (a, sp.S.Zero),
        cocycle.compose_lifted((b, sp.S.Zero), (c, sp.S.Zero)),
    )
    assert family.parameters_equivalent(left_assoc[0], right_assoc[0])
    assert sp.simplify(left_assoc[1] - right_assoc[1]) == 0

    commutator = central_commutator_residual(cocycle, a, b)
    expected = sp.expand(kappa * (ax * by - ay * bx))
    assert sp.simplify(commutator - expected) == 0


def test_central_commutator_refuses_noncommuting_visible_elements():
    x1, v1, t1, x2, v2, t2, m = sp.symbols(
        "x1 v1 t1 x2 v2 t2 m",
        real=True,
    )

    def galilei_compose(left, right):
        x_left, v_left, t_left = left
        x_right, v_right, t_right = right
        return (
            sp.expand(x_left + x_right + v_left * t_right),
            sp.expand(v_left + v_right),
            sp.expand(t_left + t_right),
        )

    family = ProcessFamily(
        "G1",
        galilei_compose,
        identity=(sp.S.Zero, sp.S.Zero, sp.S.Zero),
    )
    cocycle = ProcessCocycle(
        family,
        lambda left, right: sp.expand(
            m * (left[1] * right[0] + sp.Rational(1, 2) * right[2] * left[1] ** 2)
        ),
    )

    first = (x1, v1, t1)
    second = (x2, v2, t2)
    try:
        central_commutator_residual(cocycle, first, second)
    except ValueError as exc:
        assert "visibly commuting" in str(exc)
    else:
        raise AssertionError("expected visible noncommutation to be rejected")

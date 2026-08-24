"""Exact optical symmetry search in the repository's current A/M process API.

This is intentionally only an Addition/Multiplication generator slice.  It
uses ``ProcessFrame`` histories and exact symbolic residuals, but does not
claim the still-missing canonical multi-coordinate A/M lift or AM-Noether map.
"""

import sympy as sp

from process_geometry.process.local import ProcessFrame


def optical_product_am_frame(x, y, vx, vy):
    """Declared product A/M assignment shadow for two optical coordinates."""

    zero = sp.S.Zero
    return ProcessFrame(
        assignments=(x, y, vx, vy),
        generators={
            "A_x": {x: 1, y: zero, vx: zero, vy: zero},
            "M_x": {x: x, y: zero, vx: vx, vy: zero},
            "A_y": {x: zero, y: 1, vx: zero, vy: zero},
            "M_y": {x: zero, y: y, vx: zero, vy: vy},
        },
    )


def exact_invariant_generators(frame, expression):
    """Search the declared process frame using exact residual certificates."""

    return tuple(
        generator
        for generator in frame.names
        if sp.simplify(frame.apply(generator, expression)) == 0
    )


def test_declared_product_frame_has_two_exact_am_relations():
    x, y, vx, vy = sp.symbols("x y vx vy")
    frame = optical_product_am_frame(x, y, vx, vy)
    probe = x**2 * vx + y**2 * vy + x * y

    assert sp.simplify(
        frame.commutator("A_x", "M_x", probe) - frame.apply("A_x", probe)
    ) == 0
    assert sp.simplify(
        frame.commutator("A_y", "M_y", probe) - frame.apply("A_y", probe)
    ) == 0
    assert frame.commutator("A_x", "A_y", probe) == 0


def test_am_generator_search_finds_exact_optical_addition_symmetry():
    x, y, vx, vy = sp.symbols("x y vx vy", real=True)
    frame = optical_product_am_frame(x, y, vx, vy)
    optical_density = (1 + y**2) * sp.sqrt(4 * vx**2 + vy**2)

    # The search receives the whole declared A/M frame.  Exact process
    # residuals, rather than sampled ordinary partial derivatives, select A_x.
    assert exact_invariant_generators(frame, optical_density) == ("A_x",)

    # The finite Addition history agrees with the infinitesimal certificate.
    epsilon = sp.symbols("epsilon")
    assert sp.simplify(optical_density.subs(x, x + epsilon) - optical_density) == 0

    # An x-dependent perturbation is an exact negative control.
    broken = optical_density + x**2
    assert "A_x" not in exact_invariant_generators(frame, broken)


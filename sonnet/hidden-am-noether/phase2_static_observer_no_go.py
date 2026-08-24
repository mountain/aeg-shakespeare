"""No-go certificate for hidden symmetry under static in-group observers."""

from __future__ import annotations

import sympy as sp

from phase1_s1_census import VX, VY, X, Y, unrestricted_generator_matrix
from phase1b_s1_depth_two import (
    classify_unrestricted_linear_stabilizers,
    run_s1b_census,
)


def product_affine_observe(expression, *, x_scale, x_shift, y_scale, y_shift):
    """Pull an expression through one static product-affine A/M observer."""

    if x_scale == 0 or y_scale == 0:
        raise ValueError("observer scales must be invertible")
    return sp.expand(
        expression.subs(
            {
                X: x_scale * X + x_shift,
                VX: x_scale * VX,
                Y: y_scale * Y + y_shift,
                VY: y_scale * VY,
            },
            simultaneous=True,
        )
    )


def stabilizer_dimension(expression):
    return 4 - unrestricted_generator_matrix(expression).rank()


def frozen_s2_static_observer_census():
    census = run_s1b_census()
    frontier = classify_unrestricted_linear_stabilizers(census).genuine_asymmetric
    observers = (
        dict(x_scale=2, x_shift=1, y_scale=3, y_shift=-1),
        dict(x_scale=-1, x_shift=2, y_scale=2, y_shift=1),
        dict(x_scale=3, x_shift=-2, y_scale=-2, y_shift=3),
    )
    failures = []
    for expression in frontier:
        source_dimension = stabilizer_dimension(expression)
        for observer in observers:
            observed = product_affine_observe(expression, **observer)
            target_dimension = stabilizer_dimension(observed)
            if target_dimension != source_dimension:
                failures.append((expression, observer, source_dimension, target_dimension))
    return frontier, observers, tuple(failures)


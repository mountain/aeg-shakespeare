"""Dimensionful end-to-end Bellman check for moving-observer gauges."""

import importlib.util
from pathlib import Path
import sys

import mpmath as mp
import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/moving-am-observer/dimensionful_bellman_calibration.py"
)
SPEC = importlib.util.spec_from_file_location("dimensionful_bellman", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_dimension_audit_and_moving_frame_dynamics_are_exact():
    assert module.LENGTH / module.TIME == module.SPEED
    assert module.LENGTH / module.SPEED == module.TIME
    assert module.SPEED * module.DIMENSIONLESS == module.SPEED

    x, t, length, speed = sp.symbols(
        "x t L V", positive=True, finite=True
    )
    u = (x - speed * t) / length
    physical_x_rate = speed * (u**2 - 1)
    induced_u_rate = sp.simplify((physical_x_rate - speed) / length)
    assert sp.simplify(induced_u_rate - speed / length * (u**2 - 2)) == 0

    # The marked task sections are physical events, not chart coordinates.
    assert sp.simplify((speed * t + length - speed * t) / length) == 1
    assert sp.simplify((speed * t - length - speed * t) / length) == -1


def test_equal_clock_sections_preserve_bellman_value_and_policy():
    sections_u = module.equal_clock_sections(5)
    sections_w = tuple(module.w_of_u(value) for value in sections_u)
    clocks_u = tuple(module.clock_u(value) for value in sections_u)
    clocks_w = tuple(module.clock_w(value) for value in sections_w)

    assert max(
        abs(left - right) for left, right in zip(clocks_u, clocks_w)
    ) < mp.mpf("1e-45")
    value_u, policy_u = module.optimal_resettable_first_hit_task(clocks_u)
    value_w, policy_w = module.optimal_resettable_first_hit_task(clocks_w)
    assert abs(value_u - value_w) < mp.mpf("1e-45")
    assert policy_u == policy_w
    assert policy_u == (1, None, (2, None, (3, None, None)))


def test_bellman_value_has_the_physical_time_scale_L_over_V():
    base_sections = module.equal_clock_sections(5, length=3.5, speed=1.4)
    doubled_sections = module.equal_clock_sections(5, length=7.0, speed=1.4)
    base_clocks = tuple(
        module.clock_u(value, length=3.5, speed=1.4)
        for value in base_sections
    )
    doubled_clocks = tuple(
        module.clock_u(value, length=7.0, speed=1.4)
        for value in doubled_sections
    )
    base_value, base_policy = module.optimal_resettable_first_hit_task(base_clocks)
    doubled_value, doubled_policy = module.optimal_resettable_first_hit_task(
        doubled_clocks
    )

    assert abs(doubled_value - 2 * base_value) < mp.mpf("1e-40")
    assert doubled_policy == base_policy


def test_equal_coordinate_grids_change_both_discrete_value_and_policy():
    equal_u = module.equal_u_sections(5)
    equal_w_as_u = module.equal_w_sections_as_u(5)
    clocks_u = tuple(module.clock_u(value) for value in equal_u)
    clocks_w = tuple(module.clock_u(value) for value in equal_w_as_u)
    value_u, policy_u = module.optimal_resettable_first_hit_task(clocks_u)
    value_w, policy_w = module.optimal_resettable_first_hit_task(clocks_w)

    assert abs(value_u - value_w) > mp.mpf("0.05")
    assert policy_u != policy_w
    assert policy_u == (2, (1, None, None), (3, None, None))
    assert policy_w == (1, None, (2, None, (3, None, None)))

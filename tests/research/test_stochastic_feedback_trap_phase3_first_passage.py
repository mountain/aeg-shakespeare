"""Execute the frozen independent first-passage numerical gate."""

import importlib.util
from pathlib import Path
import sys


MODULE_PATH = Path(__file__).parents[2] / "sonnet/stochastic-feedback-trap-first-passage/phase3_first_passage.py"
SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase3", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_transported_grid_bvps_share_a_refined_continuum_value():
    refinements = {
        chart.name: tuple(module.backward_bvp(chart, count, transported_nodes=True) for count in (101, 201, 401))
        for chart in module.CHARTS
    }
    reference = refinements["u"][-1]

    assert all(abs(values[-1] - reference) < 2.0e-5 for values in refinements.values())
    assert all(abs(values[-1] - reference) < abs(values[0] - reference) + 2.0e-7 for values in refinements.values())


def test_uniform_target_mesh_exposes_chart_dependent_finite_resolution_error():
    identity_uniform = module.backward_bvp(module.CHARTS[0], 101, transported_nodes=False)
    transported = module.backward_bvp(module.CHARTS[1], 101, transported_nodes=True)
    uniform_target = module.backward_bvp(module.CHARTS[1], 101, transported_nodes=False)

    # The red team predicts a finite-resolution split, not which mesh happens
    # to have the smaller signed truncation error at one resolution.
    assert abs(uniform_target - identity_uniform) > 5.0e-5
    assert abs(uniform_target - transported) > 1.0e-5


def test_independently_evolved_chart_monte_carlo_agrees_with_bvp_and_refines_in_time():
    reference = module.backward_bvp(module.CHARTS[0], 401, transported_nodes=True)
    for index, chart in enumerate(module.CHARTS):
        coarse = module.monte_carlo_first_passage(chart, paths=2500, time_step=0.004, seed=8100 + index)
        fine = module.monte_carlo_first_passage(chart, paths=5000, time_step=0.002, seed=9100 + index)
        tolerance = 3.0 * fine.standard_error + 2.0 * abs(fine.mean - coarse.mean)
        assert abs(fine.mean - reference) < tolerance


def test_dimensionful_clock_restoration_is_chart_independent():
    values = [module.backward_bvp(chart, 401, transported_nodes=True) for chart in module.CHARTS]
    physical = [module.physical_time(value, length=3.0, speed=2.0) for value in values]

    assert all(abs(value - 1.5 * values[0]) < 3.0e-5 for value in physical)

"""PCR3BP: numerical calibration of costed lifted free-group histories.

This is the executable companion to
``sonnet/pcr3bp-history-cost/00-phase0-history-cost.md``.  The test keeps the
default CI gate small; the companion script runs the six-trajectory census.
"""

import importlib.util
import math
from pathlib import Path
import sys


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/pcr3bp-history-cost/phase0_history_cost.py"
)
SPEC = importlib.util.spec_from_file_location("pcr3bp_history_cost_phase0", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_l1_jacobi_threshold_places_the_frozen_run_in_the_open_neck_regime():
    assert abs(module.l1_x() - 0.6090351100) < 1.0e-10
    assert abs(module.l1_critical_jacobi() - 3.5969532299) < 1.0e-10
    assert module.DEFAULT_JACOBI < module.l1_critical_jacobi()


def test_free_reduction_and_gamma2_deck_metric_are_distinct_costs():
    assert module.reduce_word("aABb") == ""
    assert module.deck_matrix("aB") == (5, 2, 2, 1)
    assert module.hyperbolic_translation_length(module.deck_matrix("a" * 12)) == 0.0
    assert abs(
        module.hyperbolic_translation_length(module.deck_matrix("aB"))
        - 2.0 * math.acosh(3.0)
    ) < 1.0e-12


def test_open_neck_dynamics_generates_a_mixed_history_without_oracle_projection():
    mixed = module.simulate_history(
        module.InitialCondition("mixed-smoke", 0.55, 100.0),
        history_budget=6,
        max_time=20.0,
        max_step=0.002,
    )

    assert mixed.status == "history-budget"
    assert {symbol.lower() for symbol in mixed.reduced_word} == {"a", "b"}
    assert mixed.hyperbolic_translation_length > 0.0
    assert mixed.max_jacobi_error < 2.0e-6
    assert mixed.min_primary_distance > 0.04


def test_equal_symbol_budget_does_not_identify_deck_length_or_physical_clock():
    pure = module.simulate_history(
        module.InitialCondition("pure-smoke", 0.34, 90.0),
        history_budget=6,
        max_time=20.0,
        max_step=0.002,
    )
    mixed = module.simulate_history(
        module.InitialCondition("mixed-smoke", 0.55, 100.0),
        history_budget=6,
        max_time=20.0,
        max_step=0.002,
    )

    assert pure.status == mixed.status == "history-budget"
    assert len(pure.raw_word) == len(mixed.raw_word) == 6
    assert pure.hyperbolic_translation_length == 0.0
    assert mixed.hyperbolic_translation_length > 0.0
    assert abs(pure.elapsed_clock - mixed.elapsed_clock) > 1.0


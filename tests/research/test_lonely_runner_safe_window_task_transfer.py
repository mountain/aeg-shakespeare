"""Executable Phase-14 task-change calibration."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_SAFE_WINDOW_TASK") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "safe_window_task_transfer.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_safe_window_task_transfer",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_safe_window_task_module_is_research_local_and_loads():
    module = _load()
    assert module.four.K == 4
    assert module.five.K == 5


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 safe-window task transfer",
)
def test_same_canonical_process_requires_task_relative_refinement_at_k4_and_k5():
    module = _load()
    four, five = module.analyze_safe_window_task_transfer()

    assert four.runners == 4
    assert four.symbolic_states == 388
    assert four.first_witness_regions == 261
    assert four.first_witness_tasks == 25
    assert four.point_parents == 60
    assert four.interval_parents == 201
    assert four.split_parents == 50
    assert four.split_parent_fraction == Fraction(50, 261)
    assert four.closer_alternative_histogram == ((1, 211), (3, 49), (7, 1))
    assert four.extended_regions == 365
    assert four.extended_tasks == 47
    assert four.old_generated_coordinates == 33
    assert four.new_next_event_coordinates == 9
    assert four.genuinely_new_coordinates == 1
    assert four.minimum_support_histogram == ((1, 49), (3, 1))
    assert four.completion_union_coordinates == 7
    assert four.completion_union_genuinely_new == 0
    assert four.minimum_support_clean_parents == 49
    assert four.minimum_support_obstructed_parents == 1
    assert four.full_pairwise_clean_parents == 49
    assert four.full_pairwise_obstructed_parents == 1
    assert four.example_split_parent == (((3, "exit"),), "interval")
    assert four.example_closers == (
        (1,),
        (1, 2),
        (1, 2, 3),
        (1, 3),
        (2,),
        (2, 3),
        (3,),
    )
    assert four.example_minimum_support == (
        (1, 2, Fraction(9, 4)),
        (1, 3, Fraction(7, 2)),
        (2, 3, Fraction(14, 9)),
    )
    assert not four.example_minimum_clean
    assert not four.example_full_clean

    assert five.runners == 5
    assert five.symbolic_states == 3_397
    assert five.first_witness_regions == 1_117
    assert five.first_witness_tasks == 33
    assert five.point_parents == 197
    assert five.interval_parents == 920
    assert five.split_parents == 129
    assert five.split_parent_fraction == Fraction(129, 1117)
    assert five.closer_alternative_histogram == ((1, 988), (3, 129))
    assert five.extended_regions == 1_375
    assert five.extended_tasks == 67
    assert five.old_generated_coordinates == 98
    assert five.new_next_event_coordinates == 31
    assert five.genuinely_new_coordinates == 10
    assert five.minimum_support_histogram == ((1, 129),)
    assert five.completion_union_coordinates == 13
    assert five.completion_union_genuinely_new == 1
    assert five.minimum_support_clean_parents == 129
    assert five.minimum_support_obstructed_parents == 0
    assert five.full_pairwise_clean_parents == 129
    assert five.full_pairwise_obstructed_parents == 0
    assert five.example_split_parent == (((4, "exit"),), "interval")
    assert five.example_closers == ((3,), (3, 4), (4,))
    assert five.example_minimum_support == ((3, 4, Fraction(11, 5)),)
    assert five.example_minimum_clean
    assert five.example_full_clean

    print("PHASE14_K4", four)
    print("PHASE14_K5", five)

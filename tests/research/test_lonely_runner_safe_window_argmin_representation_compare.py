"""Exact local cost comparison for the K=4 safe-window argmin obstruction."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_SAFE_WINDOW_TASK") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "safe_window_argmin_representation_compare.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_safe_window_argmin_representation_compare",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_argmin_representation_compare_module_loads():
    module = _load()
    assert module.transfer.four.K == 4


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 argmin representation comparison",
)
def test_pairwise_completion_overrefines_the_real_three_way_closer_task():
    module = _load()
    result = module.analyze_argmin_representation_compare()

    assert len(result.pairwise_coordinates) == 3
    assert result.feasible_complete_sign_states == 13
    assert result.minimum_group_tasks == 7
    assert result.overrefined_states == 6
    assert result.weighted_depth_uniform_states == 26
    assert result.tree_nodes == 13
    assert result.internal_nodes == 4
    assert result.worst_depth == 2
    assert result.peak_frontier == 9
    assert result.widths == (1, 3, 9)
    assert result.terminal_merged_dag_nodes == 11
    assert result.minimum_group_value_count == 7

    print("PHASE14_ARGMIN_COMPARE", result)

"""Opt-in executable calibration for Sonnet 001 Phase 12B."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_FIVE_SPEED_LAZY_DAG") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 five-speed lazy-task-DAG calibration",
)


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "five_speed_lazy_task_dag.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_five_speed_lazy_task_dag",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_five_speed_lazy_task_dag_avoids_static_sign_materialization():
    module = _load()
    result = module.analyze_lazy_task_dag()

    assert result.terminal_regions == 1_117
    assert result.canonical_tasks == 33
    assert len(result.coordinates) == 36

    # The decisive result: adaptive placement never has to split one of the
    # original symbolic terminal closure regions by an unresolved wall.
    assert result.unique_atoms_visited == 1_117
    assert result.closure_refinement_pressure == 0

    assert result.tree_nodes == 235
    assert result.internal_nodes == 78
    assert result.leaves == 157
    assert result.worst_depth == 15
    assert result.peak_frontier == 36
    assert result.widths == (
        1,
        3,
        3,
        3,
        3,
        9,
        21,
        36,
        33,
        21,
        21,
        18,
        21,
        15,
        18,
        9,
    )

    assert result.dag_nodes == 99
    assert result.dag_internal_nodes == 66
    assert result.dag_task_leaves == 33
    assert result.root_coordinate == (0, 4, Fraction(5))

    assert result.usage_cases == 126
    assert result.usage_decision_depth == 317
    assert result.usage_event_depth == 921
    assert result.usage_decision_worst == 11
    assert result.usage_event_worst == 25
    assert result.usage_errors == 0

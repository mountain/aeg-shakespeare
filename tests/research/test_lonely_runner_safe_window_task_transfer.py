"""Executable Phase-14 task-change calibration."""

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

    for result in (four, five):
        assert result.interval_parents > 0
        assert result.split_parents > 0
        assert result.max_closer_alternatives >= 2
        assert result.extended_regions > result.first_witness_regions
        assert result.extended_tasks > result.first_witness_tasks
        assert result.example_split_parent is not None
        assert len(result.example_closers) >= 2

    # The task-change effect is independently present at two runner dimensions,
    # not a single four-speed accident.
    assert four.runners == 4
    assert five.runners == 5

    print("PHASE14_K4", four)
    print("PHASE14_K5", five)

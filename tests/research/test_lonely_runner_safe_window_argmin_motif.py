"""Exact structural audit for the Phase-14 safe-window argmin motif."""

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
    script_path = script_dir / "safe_window_argmin_motif.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_safe_window_argmin_motif",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_argmin_motif_module_loads_without_public_api_changes():
    module = _load()
    assert module.transfer.four.K == 4
    assert module.transfer.five.K == 5


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 safe-window argmin structural audit",
)
def test_real_safe_window_splits_match_two_and_three_event_argmin_geometry():
    module = _load()
    four, five = module.analyze_safe_window_argmin_motifs()

    assert four.matches_exact_argmin_geometry
    assert four.active_closer_runners == (1, 2, 3)
    assert len(four.closer_tasks) == 7
    assert four.minimum_support_size == 3
    assert four.pairwise_separable
    assert not four.clean

    assert five.matches_exact_argmin_geometry
    assert five.active_closer_runners == (3, 4)
    assert len(five.closer_tasks) == 3
    assert five.minimum_support_size == 1
    assert five.pairwise_separable
    assert five.clean

    print("PHASE14_ARGMIN_K4", four)
    print("PHASE14_ARGMIN_K5", five)

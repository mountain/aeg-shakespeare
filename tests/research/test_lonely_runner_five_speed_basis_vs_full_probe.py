"""Executable checks for Sonnet 001 Phase 13C."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_BASIS_VS_FULL_PROBE") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "five_speed_basis_vs_full_probe.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_five_speed_basis_vs_full_probe",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_second_probe_crosses_next_native_threshold():
    module = _load()
    assert module.PREVIOUS_PROBE == Fraction(48, 7)
    assert module.next_outer_threshold_after_previous_probe() == Fraction(7)
    assert module.PROBE_RMAX == Fraction(36, 5)
    assert module.PREVIOUS_PROBE < module.CRITICAL_RMAX < module.PROBE_RMAX


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 minimum-basis/full-grammar frontier probe",
)
def test_second_critical_probe_classifies_basis_vs_full_failure_layer():
    module = _load()
    result = module.analyze_probe()

    assert result.rmax == Fraction(36, 5)
    assert result.symbolic_states > 16_747
    assert result.terminal_regions > 6_203
    assert result.generated_coordinates >= 111
    assert result.canonical_tasks >= 50
    assert result.minimum_coordinates >= 48

    # The exact output is discovery data on the first run.  analyze_probe()
    # independently verifies whichever tree/obstruction is returned.  These
    # invariants ensure the result classifies one of the intended layers.
    if result.minimum_clean:
        assert result.full_clean
        assert not result.full_analysis_required
        assert result.minimum_tree_nodes is not None
        assert result.minimum_obstruction_atomic is None
    else:
        assert result.full_analysis_required
        assert result.minimum_tree_nodes is None
        assert result.minimum_obstruction_atomic is not None

    print("PHASE13C_PROBE", result)

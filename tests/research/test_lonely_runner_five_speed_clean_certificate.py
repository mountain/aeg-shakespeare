"""Executable checks for Sonnet 001 Phase 13B."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_CLEAN_CERTIFICATE") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "five_speed_clean_certificate.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_five_speed_clean_certificate",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_next_probe_crosses_a_process_generated_critical_boundary():
    module = _load()
    assert module.BASELINE_RMAX == Fraction(25, 4)
    assert module.next_outer_contact_threshold() == Fraction(47, 7)
    assert module.PROBE_RMAX == Fraction(48, 7)
    assert module.BASELINE_RMAX < module.CRITICAL_RMAX < module.PROBE_RMAX


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 exact clean-separability frontier probe",
)
def test_generic_clean_criterion_recertifies_baseline_and_first_critical_probe():
    module = _load()
    baseline, probe = module.analyze_baseline_and_probe()

    assert baseline.symbolic_states == 14_773
    assert baseline.terminal_regions == 5_379
    assert baseline.generated_coordinates == 111
    assert baseline.canonical_tasks == 48
    assert baseline.minimum_coordinates == 46
    assert baseline.pairwise_separable
    assert baseline.clean
    assert baseline.clean_tree_nodes == 349
    assert baseline.clean_max_depth == 15
    assert baseline.root_coordinate == (0, 4, Fraction(5))
    assert baseline.max_event_index == 47
    assert baseline.max_contact_center == 7

    # Crossing 47/7 admits a genuinely new center-8 causal ordering, but the
    # generic exact criterion still finds a zero-completion tree.
    assert probe.rmax == Fraction(48, 7)
    assert probe.symbolic_states == 16_747
    assert probe.terminal_regions == 6_203
    assert probe.generated_coordinates == 111
    assert probe.canonical_tasks == 50
    assert probe.minimum_coordinates == 48
    assert probe.pairwise_separable
    assert probe.clean
    assert probe.clean_states_visited == 745
    assert probe.clean_tree_nodes == 745
    assert probe.clean_max_depth == 16
    assert probe.root_coordinate == (0, 3, Fraction(5))
    assert probe.obstruction_atomic is None
    assert probe.max_event_index == 49
    assert probe.max_contact_center == 8

"""Executable checks for Sonnet 001 Phase 12A."""

from __future__ import annotations

from dataclasses import asdict
import importlib.util
import json
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_FIVE_SPEED_TRANSFER") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "five_speed_dimension_transfer.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_five_speed_dimension_transfer",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_five_speed_transfer_module_and_nontrivial_threshold_smoke():
    module = _load()
    assert module.K == 5
    assert module.DELTA.numerator == 1 and module.DELTA.denominator == 6
    assert module.RMAX > 5
    assert module.RMAX < 6


def _assert_deletion_witnesses(
    module,
    result,
    terminals,
    project,
    projection,
    expected_count,
):
    grammar = result.coordinate_grammar
    witnesses = projection.deletion_witnesses
    assert len(grammar) == result.generated_coordinates == 98
    assert len(witnesses) == expected_count

    expected_indices = {
        grammar.index(coordinate)
        for coordinate in projection.minimum_coordinates
    }
    observed_indices = {
        witness.coordinate_index
        for witness in witnesses
    }
    assert observed_indices == expected_indices
    assert tuple(witness.coordinate_index for witness in witnesses) == tuple(
        sorted(observed_indices)
    )

    for witness in witnesses:
        assert module._replay_deletion_witness(
            terminals,
            grammar,
            project,
            witness,
        )
        assert 0 <= witness.coordinate_index < len(grammar)
        assert 0 <= witness.left_terminal_id < result.terminal_regions
        assert 0 <= witness.right_terminal_id < result.terminal_regions
        assert witness.left_terminal_id != witness.right_terminal_id
        assert witness.left_projected_task != witness.right_projected_task
        assert len(witness.common_signs) == len(grammar) - 1
        assert set(witness.common_signs) <= {-1, 0, 1}
        assert witness.left_coordinate_sign in {-1, 0, 1}
        assert witness.right_coordinate_sign in {-1, 0, 1}
        assert witness.left_coordinate_sign != witness.right_coordinate_sign

        # Reinsert the deleted signs.  The resulting two complete records agree
        # on all 97 retained coordinates and differ exactly at the certified one.
        left = list(witness.common_signs)
        right = list(witness.common_signs)
        left.insert(witness.coordinate_index, witness.left_coordinate_sign)
        right.insert(witness.coordinate_index, witness.right_coordinate_sign)
        assert len(left) == len(right) == len(grammar)
        assert [
            index
            for index, (left_sign, right_sign) in enumerate(zip(left, right))
            if left_sign != right_sign
        ] == [witness.coordinate_index]

        # The compact certificate shape contains no closures or custom objects;
        # it survives a standard dataclass-to-JSON serialization round trip.
        payload = json.loads(json.dumps(asdict(witness)))
        assert payload["coordinate_index"] == witness.coordinate_index
        assert len(payload["common_signs"]) == 97


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 five-speed dimension-transfer calibration",
)
def test_five_speed_canonical_transfer_has_strong_minimum_certificates_and_static_red_team():
    module = _load()
    result = module.analyze_five_speed_transfer(include_static_cells=True)
    terminals, replay_grammar, _states, _max_center = (
        module._compile_terminal_regions()
    )
    assert replay_grammar == result.coordinate_grammar

    assert result.symbolic_states == 3_397
    assert result.terminal_regions == 1_117
    assert result.max_event_index == 47
    assert result.max_contact_center == 7
    assert result.generated_coordinates == 98

    assert result.full_certificate.task_count == 154
    assert len(result.full_certificate.minimum_coordinates) == 86
    _assert_deletion_witnesses(
        module,
        result,
        terminals,
        module._full,
        result.full_certificate,
        86,
    )

    assert result.history_free_certificate.task_count == 63
    assert len(result.history_free_certificate.minimum_coordinates) == 36
    _assert_deletion_witnesses(
        module,
        result,
        terminals,
        module._history_free,
        result.history_free_certificate,
        36,
    )

    assert result.canonical_witness.task_count == 33
    assert len(result.canonical_witness.minimum_coordinates) == 36
    _assert_deletion_witnesses(
        module,
        result,
        terminals,
        module._canonical,
        result.canonical_witness,
        36,
    )
    assert (
        result.history_free_certificate.minimum_coordinates
        == result.canonical_witness.minimum_coordinates
    )

    assert result.mode_only.task_count == 2
    assert len(result.mode_only.minimum_coordinates) == 27
    _assert_deletion_witnesses(
        module,
        result,
        terminals,
        module._mode,
        result.mode_only,
        27,
    )

    assert result.canonical_sign_cells == 69_683

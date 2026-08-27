from __future__ import annotations

import json
from pathlib import Path

from run_heldout import run


ROOT = Path(__file__).resolve().parents[1]


def test_committed_heldout_reveals_and_replays() -> None:
    result = run(ROOT)
    assert result["commitment_verified"] is True
    assert result["passed"] is True
    assert result["certificate"]["result"]["coefficient"] == "1/3"
    assert result["replay"]["status"] == "verified"
    stored = json.loads((ROOT / "HELD_OUT_RESULT.json").read_text(encoding="utf-8"))
    assert result == stored


def test_observed_baselines_agree_without_semantic_credit() -> None:
    observed = json.loads(
        (ROOT / "OBSERVED_BASELINES.json").read_text(encoding="utf-8")
    )
    assert len(observed["cases"]) == 3
    for row in observed["cases"]:
        assert row["coefficient"] == row["candidate"]["coefficient"]
        assert row["semantic_or_certificate_credit"] is False
        assert row["candidate"]["replay_status"] == "verified"

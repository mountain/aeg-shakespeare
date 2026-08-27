from __future__ import annotations

import hashlib
import json
from pathlib import Path

from finite_le_semantics import run_corpus


def test_reveal_matches_preimplementation_commitment() -> None:
    root = Path(__file__).parents[1]
    reveal = json.loads((root / "HELD_OUT_REVEAL.json").read_text())
    reveal_bytes = json.dumps(
        reveal, sort_keys=True, separators=(",", ":")
    ).encode()
    commitment = json.loads((root / "HELD_OUT_COMMITMENT.json").read_text())
    assert hashlib.sha256(reveal_bytes).hexdigest() == commitment["payload_sha256"]


def test_held_out_case_evaluates_and_replays() -> None:
    root = Path(__file__).parents[1]
    row = run_corpus(root / "HELD_OUT_CORPUS.json")["cases"][0]
    certificate = row["certificate"]
    assert certificate["status"] == "evaluated"
    assert certificate["q"] == 3
    assert certificate["limit"] == "1/5"
    assert certificate["cancellation_jump"] >= 4
    assert certificate["domain_witnesses"]
    assert row["replay"]["valid"] is True


def test_recorded_held_out_result_matches_recomputation() -> None:
    root = Path(__file__).parents[1]
    recorded = json.loads((root / "HELD_OUT_RESULT.json").read_text())
    row = run_corpus(root / "HELD_OUT_CORPUS.json")["cases"][0]
    certificate = row["certificate"]
    assert recorded["case"] == {
        "id": row["id"],
        "status": certificate["status"],
        "q": certificate["q"],
        "chart": certificate["chart"],
        "limit": certificate["limit"],
        "normal_form": certificate["normal_form"],
        "cancellation_jump": certificate["cancellation_jump"],
        "residual": certificate["residual"],
        "certificate_digest": certificate["certificate_digest"],
        "certificate_bytes": certificate["cost"]["certificate_bytes"],
        "replay_valid": row["replay"]["valid"],
        "replay_steps": row["replay"]["steps"],
    }

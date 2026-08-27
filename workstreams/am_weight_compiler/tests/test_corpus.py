from __future__ import annotations

from pathlib import Path

from am_weight_compiler.corpus import run_corpus


ROOT = Path(__file__).resolve().parents[1]


def test_frozen_public_corpus_and_replay() -> None:
    result = run_corpus(ROOT / "PUBLIC_CORPUS.json", ROOT / "FROZEN_CONTRACT.json")
    assert result["passed"] is True
    assert result["pass_count"] == result["case_count"] == 12
    assert all(row["replay"]["status"] == "verified" for row in result["rows"])

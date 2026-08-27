from __future__ import annotations

import json
from pathlib import Path

from am_weight_compiler.corpus import run_corpus


ROOT = Path(__file__).resolve().parents[1]


def test_stored_public_result_is_reproducible() -> None:
    result = run_corpus(ROOT / "PUBLIC_CORPUS.json", ROOT / "FROZEN_CONTRACT.json")
    stored = json.loads((ROOT / "PUBLIC_RESULT.json").read_text(encoding="utf-8"))
    assert result == stored

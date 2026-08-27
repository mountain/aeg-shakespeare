from __future__ import annotations

import json
from pathlib import Path

from am_weight_compiler.evaluator import evaluate_case
from am_weight_compiler.model import Budgets, digest_json
from am_weight_compiler.replay import replay_certificate


def run(root: Path) -> dict[str, object]:
    reveal = json.loads((root / "HELD_OUT_REVEAL.json").read_text(encoding="utf-8"))
    commitment = json.loads(
        (root / "HELD_OUT_COMMITMENT.json").read_text(encoding="utf-8")
    )
    contract = json.loads((root / "FROZEN_CONTRACT.json").read_text(encoding="utf-8"))
    public = json.loads((root / "PUBLIC_CORPUS.json").read_text(encoding="utf-8"))

    payload_digest = digest_json(reveal["payload"])
    commitment_verified = (
        payload_digest == reveal["commitment"] == commitment["payload_sha256"]
    )
    if not commitment_verified:
        raise SystemExit("held-out commitment mismatch")

    case = reveal["executable_case"]
    budgets = Budgets.from_mapping(contract["budgets"])
    certificate = evaluate_case(case, public["context"], budgets)
    replay = replay_certificate(case, public["context"], budgets, certificate)
    expected = case["expected"]
    passed = (
        certificate["status"] == expected["status"]
        and certificate["result"].get("coefficient") == expected["coefficient"]
        and replay["status"] == "verified"
    )
    return {
        "schema": "process-geometry/am-weight-heldout-result/v0",
        "case_id": case["id"],
        "commitment_verified": commitment_verified,
        "payload_digest": payload_digest,
        "pre_reveal_source_commit": reveal["pre_reveal_source_commit"],
        "passed": passed,
        "certificate": certificate,
        "replay": replay,
    }


if __name__ == "__main__":
    result = run(Path(__file__).resolve().parent)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["passed"] else 1)

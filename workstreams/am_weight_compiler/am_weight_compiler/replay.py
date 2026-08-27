from __future__ import annotations

from typing import Any, Mapping

from .evaluator import evaluate_case
from .model import Budgets, digest_json


def replay_certificate(
    case: Mapping[str, Any],
    corpus_context: Mapping[str, object],
    budgets: Budgets,
    certificate: Mapping[str, Any],
) -> dict[str, object]:
    recomputed = evaluate_case(case, corpus_context, budgets)
    supplied = dict(certificate)
    verified = recomputed == supplied
    return {
        "status": "verified" if verified else "rejected",
        "certificate_digest": supplied.get("certificate_digest"),
        "recomputed_digest": recomputed.get("certificate_digest"),
        "replay_digest": digest_json(
            {
                "source_digest": recomputed["source_digest"],
                "certificate_digest": supplied.get("certificate_digest"),
                "recomputed_digest": recomputed.get("certificate_digest"),
                "verified": verified,
            }
        ),
        "costs": {
            "coefficient_operations": recomputed["costs"]["evaluation"][
                "coefficient_operations"
            ],
            "dependency_requests": recomputed["dependencies"]["request_count"],
        },
    }

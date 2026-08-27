from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from typing import Any, Mapping

from .coefficients import WeightEvaluator
from .model import (
    Budgets,
    EvaluationFailure,
    canonical_json,
    digest_json,
    fraction_text,
    parse_fraction,
    without_expected,
)
from .native import AMTerm, finite_affine_relation, pbw_identity, primitive


SEMANTIC_CARRIER = "completed-am-power-weight/rank-one-rational/v0"


def _with_certificate_size(certificate: dict[str, Any], budgets: Budgets) -> None:
    storage = certificate["costs"]["storage"]
    previous = -1
    while storage["certificate_bytes"] != previous:
        previous = storage["certificate_bytes"]
        storage["certificate_bytes"] = len(canonical_json(certificate).encode("utf-8"))
    if storage["certificate_bytes"] > budgets.max_certificate_bytes:
        raise EvaluationFailure("resource_exceeded", "certificate-budget-exceeded")


def _seal(certificate: dict[str, Any], budgets: Budgets) -> dict[str, Any]:
    certificate["certificate_digest"] = "0" * 64
    _with_certificate_size(certificate, budgets)
    unsigned = {key: value for key, value in certificate.items() if key != "certificate_digest"}
    certificate["certificate_digest"] = digest_json(unsigned)
    return certificate


def _base_certificate(
    case: Mapping[str, Any], context: Mapping[str, object], budgets: Budgets
) -> dict[str, Any]:
    source = without_expected(case)
    return {
        "schema": "process-geometry/am-weight-certificate/v0",
        "case_id": case.get("id"),
        "kind": case.get("kind"),
        "semantic_carrier": SEMANTIC_CARRIER,
        "claim_scope": "frozen-rank-one-rational-completed-am-fragment",
        "source_digest": digest_json(source),
        "context_digest": digest_json({"context": context, "budgets": budgets.as_dict()}),
        "status": "evaluated",
        "result": {},
        "observer": None,
        "dependencies": {"request_count": 0, "weight_count": 0, "weights": []},
        "costs": {
            "compilation": {"nodes": 0, "lattice_denominator": 1},
            "evaluation": {"coefficient_operations": 0},
            "storage": {
                "source_bytes": len(canonical_json(source).encode("utf-8")),
                "certificate_bytes": 0,
            },
        },
    }


def evaluate_case(
    case: Mapping[str, Any],
    corpus_context: Mapping[str, object],
    budgets: Budgets,
) -> dict[str, Any]:
    context = deepcopy(dict(corpus_context))
    context.update(case.get("context_override", {}))
    certificate = _base_certificate(case, context, budgets)
    try:
        kind = case.get("kind")
        if kind == "native-laws":
            left = AMTerm.decode(case["left"], max_abs_power=budgets.max_abs_power)
            right = AMTerm.decode(case["right"], max_abs_power=budgets.max_abs_power)
            pbw_source = AMTerm.decode(
                case["pbw"]["source"], max_abs_power=budgets.max_abs_power
            )
            relation = case["finite_relation"]
            certificate["result"] = {
                "product": left.multiply(right).as_dict(),
                "A_left": left.apply_A().as_dict(),
                "M_left": left.apply_M().as_dict(),
                "pbw": pbw_identity(
                    pbw_source, int(case["pbw"]["m"]), int(case["pbw"]["n"])
                ),
                "finite_relation": finite_affine_relation(
                    parse_fraction(relation["translation"]),
                    parse_fraction(relation["scale"]),
                ),
            }
            certificate["costs"]["compilation"]["nodes"] = 4
        elif kind == "primitive":
            term = AMTerm.decode(case["term"], max_abs_power=budgets.max_abs_power)
            certificate["result"] = primitive(
                term, str(case["generator"]), str(case["extension_policy"])
            )
            certificate["costs"]["compilation"]["nodes"] = 1
        elif kind == "paired":
            left = AMTerm.decode(case["left"], max_abs_power=budgets.max_abs_power)
            right = AMTerm.decode(case["right"], max_abs_power=budgets.max_abs_power)
            certificate["result"] = {"same_canonical_term": left == right}
            certificate["costs"]["compilation"]["nodes"] = 2
        elif kind == "coefficient":
            target = parse_fraction(case["target_weight"], field="target_weight")
            evaluator = WeightEvaluator(case["expression"], target, context, budgets)
            coefficient = evaluator.coefficient()
            certificate["result"] = {"coefficient": coefficient.to_text()}
            certificate["observer"] = {
                "target_weight": fraction_text(target),
                "residual": "weights-above-observer-horizon",
            }
            certificate["dependencies"] = evaluator.meter.dependency_summary()
            certificate["costs"]["compilation"] = {
                "nodes": evaluator.meter.nodes,
                "lattice_denominator": evaluator.lattice_denominator,
            }
            certificate["costs"]["evaluation"] = {
                "coefficient_operations": evaluator.meter.coefficient_operations
            }
        else:
            raise EvaluationFailure("unsupported", "unknown-case-kind")
    except EvaluationFailure as exc:
        certificate["status"] = exc.status
        certificate["result"] = {"failure": exc.code}
    except (KeyError, TypeError, ValueError) as exc:
        certificate["status"] = "unsupported"
        certificate["result"] = {"failure": "malformed-case", "detail": str(exc)}
    return _seal(certificate, budgets)

"""Bounded compiler for C0--C2 and explicit refusal at C3/C4."""

from __future__ import annotations

from dataclasses import dataclass, replace

from .certificate import CarrierDecisionCertificate, CostLedger, Obligation, canonical_json, digest
from .features import FeatureReport, infer_features
from .ir import AbelTask, ScaleExpr, SymbolicIterate
from .model import Carrier, DecisionStatus, FailureCode, capability


@dataclass(frozen=True)
class CompilerBudget:
    max_nodes: int = 512
    max_finite_height: int = 32
    max_certificate_bytes: int = 65536


def _minimum(report: FeatureReport) -> Carrier | None:
    if report.symbolic_height:
        return None
    for carrier in (Carrier.C0, Carrier.C1, Carrier.C2):
        if report.features <= capability(carrier).supports:
            return carrier
    return None


class CarrierCompiler:
    """Issue #142's smallest evidence-supported carrier decision stage."""

    schema = "process-geometry/carrier-decision/v0"

    def __init__(self, budget: CompilerBudget | None = None):
        self.budget = budget or CompilerBudget()

    def compile(self, expr: ScaleExpr, requested: Carrier | None = None) -> CarrierDecisionCertificate:
        expr_data = expr.to_data()
        report = infer_features(expr)
        minimum = _minimum(report)
        status = DecisionStatus.SUFFICIENT
        failures: list[dict[str, str]] = []
        lowering: list[Obligation] = []
        upgrade: list[Obligation] = []
        task: list[Obligation] = []

        if report.node_count > self.budget.max_nodes:
            status = DecisionStatus.RESOURCE_EXCEEDED
            failures.append({"code": FailureCode.NODE_BUDGET.value, "message": "finite expression exceeds declared node budget"})
            minimum = None
        elif report.construction_height is not None and report.construction_height > self.budget.max_finite_height:
            status = DecisionStatus.RESOURCE_EXCEEDED
            failures.append({"code": FailureCode.HEIGHT_BUDGET.value, "message": "finite exp/log construction height exceeds declared budget"})
            minimum = None
        elif isinstance(expr, SymbolicIterate):
            status = DecisionStatus.UNSUPPORTED
            failures.append({"code": FailureCode.SYMBOLIC_HEIGHT.value, "message": "symbolic height is a uniform iteration task and cannot be certified by fixed unrolling"})
            upgrade.append(Obligation("uniform-iteration-normal-form", "provide a genuine symbolic-height constructor and independently replayable comparison law", False, expr.height_symbol))
            minimum = None
        elif isinstance(expr, AbelTask):
            status = DecisionStatus.UNSUPPORTED
            failures.append({"code": FailureCode.ABEL_ASSUMPTIONS.value, "message": "Abel/tetration existence, branch, normalization, and uniqueness are not implemented"})
            upgrade.extend((
                Obligation("abel-existence", "prove existence on the declared domain", False),
                Obligation("abel-normalization", "declare and verify a normalization selecting a solution", bool(expr.normalization), expr.normalization),
                Obligation("abel-effectiveness", "supply a finite effective shadow with replay semantics", False),
            ))
            minimum = None
        elif minimum is None:
            status = DecisionStatus.OUTSIDE_GRAMMAR
            failures.append({"code": "no-effective-carrier", "message": "no executable C0--C2 carrier supports the inferred feature set"})

        if requested in {Carrier.C3, Carrier.C4}:
            code = FailureCode.C3_UNSUPPORTED if requested is Carrier.C3 else FailureCode.C4_UNSUPPORTED
            status = DecisionStatus.UNSUPPORTED
            failures.append({"code": code.value, "message": capability(requested).note})
            upgrade.append(Obligation("effective-backend", "implement construction, comparison, lowering, and independent replay before carrier credit", False, requested.value))
        elif requested is not None and minimum is not None:
            if report.features <= capability(requested).supports and capability(requested).executable:
                lowering.append(Obligation("requested-carrier-closure", "all inferred features are supported by the requested executable carrier", True, requested.value))
            else:
                status = DecisionStatus.UNSUPPORTED
                missing = sorted(report.features - capability(requested).supports)
                failures.append({"code": "requested-carrier-lacks-closure", "message": f"missing capabilities: {missing}"})
                upgrade.append(Obligation("carrier-upgrade", "choose an executable carrier supporting every witnessed feature", False, ",".join(missing)))

        if status is DecisionStatus.SUFFICIENT and minimum is not None:
            lowering.extend(self._positive_obligations(report, minimum))

        syntax_capability = "unsupported-symbolic-height" if report.symbolic_height else "finite-dag-feature-and-height-inference"
        normal_form_capability = "finite-polynomial-collection" if minimum is Carrier.C0 else "explicit-finite-support-only" if minimum is Carrier.C1 else "not-implemented"
        comparison_capability = "exact-rational-weight-order" if minimum in {Carrier.C0, Carrier.C1} else "not-implemented"
        if minimum is Carrier.C2:
            task.extend((
                Obligation("le-normal-form", "construct and independently replay a transseries normal form", False),
                Obligation("le-domain-branches", "declare exp/log domains and branch transport for semantic simplification", False),
                Obligation("le-comparison", "provide an effective comparison law for represented transmonomials", False),
            ))

        claim_scope = (
            "minimum only in the frozen syntax-directed C0--C2 capability matrix; "
            "no semantic field minimality, general LE normal-form theorem, or C3/C4 separation is claimed"
        )
        eliminability = "surreal-runtime-eliminable-for-frozen-syntax-decision" if minimum is not None else None
        provisional_cost = CostLedger(
            input_nodes=report.node_count,
            feature_visits=report.node_count,
            construction_height=report.construction_height,
            compilation_steps=report.node_count + len(report.features) + len(lowering) + len(upgrade) + len(task),
            certificate_bytes=0,
            replay_steps=2 + report.node_count + len(report.features),
            residual_items=len([item for item in lowering + upgrade + task if not item.discharged]),
            decoder_steps=1,
        )
        certificate = CarrierDecisionCertificate(
            schema=self.schema,
            status=status,
            input_digest=digest(expr_data),
            minimum_declared_carrier=minimum,
            requested_carrier=requested,
            construction_height=report.construction_height,
            features=tuple(sorted(report.features)),
            feature_witnesses=tuple(item.to_data() for item in report.witnesses),
            syntax_capability=syntax_capability,
            normal_form_capability=normal_form_capability,
            comparison_capability=comparison_capability,
            lowering_obligations=tuple(lowering),
            upgrade_obligations=tuple(upgrade),
            task_obligations=tuple(task),
            eliminability=eliminability,
            claim_scope=claim_scope,
            failures=tuple(failures),
            cost=provisional_cost,
            certificate_digest="",
        )
        # Charge the complete serialized record.  A 64-character placeholder
        # has the same byte width as the final SHA-256 digest; iterate because
        # writing the decimal byte count can itself change the count's width.
        size = 0
        for _ in range(4):
            sized = replace(
                certificate,
                cost=replace(provisional_cost, certificate_bytes=size),
                certificate_digest="0" * 64,
            )
            new_size = len(canonical_json(sized.to_data()).encode("utf-8"))
            if new_size == size:
                break
            size = new_size
        certificate = replace(certificate, cost=replace(provisional_cost, certificate_bytes=size))
        certificate = replace(certificate, certificate_digest=digest(certificate.payload()))
        final_size = len(canonical_json(certificate.to_data()).encode("utf-8"))
        assert final_size == size
        if final_size > self.budget.max_certificate_bytes:
            return self._certificate_budget_failure(expr, report, requested, final_size)
        return certificate

    def _positive_obligations(self, report: FeatureReport, minimum: Carrier) -> list[Obligation]:
        obligations = [
            Obligation("finite-dag", "source is a finite ScaleExpr DAG within the node budget", True, str(report.node_count)),
            Obligation("capability-closure", "minimum declared carrier contains every inferred feature", True, minimum.value),
        ]
        if minimum is Carrier.C2:
            obligations.append(Obligation("finite-height-induction", "each exp/log node increments a finite construction height", True, str(report.construction_height)))
        if minimum is Carrier.C1:
            obligations.append(Obligation("finite-support", "all ordered monomial support is explicitly finite", True))
        obligations.append(Obligation("larger-runtime-elimination", "certificate and replay require no C3/C4 arithmetic", True, "surreal-eliminable"))
        return obligations

    def _certificate_budget_failure(self, expr: ScaleExpr, report: FeatureReport, requested: Carrier | None, size: int) -> CarrierDecisionCertificate:
        cost = CostLedger(report.node_count, report.node_count, report.construction_height, report.node_count, size, 0, 1, 1)
        base = CarrierDecisionCertificate(
            self.schema,
            DecisionStatus.RESOURCE_EXCEEDED,
            digest(expr.to_data()),
            None,
            requested,
            report.construction_height,
            tuple(sorted(report.features)),
            (),
            "finite-dag-feature-and-height-inference",
            "not-claimed-after-budget-failure",
            "not-claimed-after-budget-failure",
            (),
            (Obligation("certificate-budget", "increase the explicit certificate budget or reduce the source", False, str(size)),),
            (),
            None,
            "no positive carrier claim is emitted after certificate budget failure",
            ({"code": FailureCode.CERTIFICATE_BUDGET.value, "message": "serialized certificate exceeds declared byte budget"},),
            cost,
            "",
        )
        return replace(base, certificate_digest=digest(base.payload()))

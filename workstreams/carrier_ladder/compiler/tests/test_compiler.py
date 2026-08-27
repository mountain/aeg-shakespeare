from __future__ import annotations

from carrier_compiler import (
    AbelTask,
    Add,
    Carrier,
    CarrierCompiler,
    Const,
    Exp,
    GeneralizedPolynomial,
    Log,
    Mul,
    Pow,
    Symbol,
    SymbolicIterate,
    replay_certificate,
)
from carrier_compiler.compiler import CompilerBudget
from carrier_compiler.certificate import canonical_json, digest
from carrier_compiler.model import DecisionStatus, FailureCode


def compile_and_replay(expr, requested=None):
    certificate = CarrierCompiler().compile(expr, requested)
    replay = replay_certificate(expr.to_data(), certificate.to_data())
    return certificate, replay


def test_l0_bessel_polynomial_germ_is_c0_not_surreal():
    theta = Symbol("theta")
    delta = Symbol("delta")
    phase = Add(
        Mul(delta, theta),
        Mul(Const("-1/6"), Pow(theta, 3)),
        Mul(Const("-1/6"), delta, Pow(theta, 3)),
        Mul(Const("1/120"), Pow(theta, 5)),
    )
    cert, replay = compile_and_replay(phase)
    assert cert.status is DecisionStatus.SUFFICIENT
    assert cert.minimum_declared_carrier is Carrier.C0
    assert cert.eliminability == "surreal-runtime-eliminable-for-frozen-syntax-decision"
    assert replay.valid


def test_finite_fractional_monomials_require_c1():
    expr = GeneralizedPolynomial({"-3/2": 2, "1/3": 5})
    cert, replay = compile_and_replay(expr)
    assert cert.minimum_declared_carrier is Carrier.C1
    assert cert.construction_height == 0
    assert replay.valid


def test_finite_nested_exp_log_returns_c2_and_height():
    expr = Exp(Log(Exp(Add(Symbol("x"), Const(1)))))
    cert, replay = compile_and_replay(expr)
    assert cert.minimum_declared_carrier is Carrier.C2
    assert cert.construction_height == 3
    assert cert.eliminability == "surreal-runtime-eliminable-for-frozen-syntax-decision"
    assert any(item.code == "finite-height-induction" for item in cert.lowering_obligations)
    assert replay.valid


def test_requesting_too_small_carrier_is_typed_failure():
    expr = Exp(Symbol("x"))
    cert, replay = compile_and_replay(expr, Carrier.C0)
    assert cert.status is DecisionStatus.UNSUPPORTED
    assert cert.minimum_declared_carrier is Carrier.C2
    assert cert.failures[0]["code"] == "requested-carrier-lacks-closure"
    assert replay.valid


def test_symbolic_height_is_not_fixed_unrolling():
    expr = SymbolicIterate("exp", Symbol("x"), "h")
    cert, replay = compile_and_replay(expr)
    assert cert.status is DecisionStatus.UNSUPPORTED
    assert cert.construction_height is None
    assert cert.minimum_declared_carrier is None
    assert cert.failures[0]["code"] == FailureCode.SYMBOLIC_HEIGHT.value
    assert any(item.code == "uniform-iteration-normal-form" and not item.discharged for item in cert.upgrade_obligations)
    assert replay.valid


def test_abel_gate_keeps_existence_and_normalization_explicit():
    expr = AbelTask("x")
    cert, replay = compile_and_replay(expr)
    assert cert.status is DecisionStatus.UNSUPPORTED
    assert cert.failures[0]["code"] == FailureCode.ABEL_ASSUMPTIONS.value
    assert {item.code for item in cert.upgrade_obligations} == {
        "abel-existence",
        "abel-normalization",
        "abel-effectiveness",
    }
    assert replay.valid


def test_c3_and_c4_are_never_reported_as_executable():
    for carrier, code in (
        (Carrier.C3, FailureCode.C3_UNSUPPORTED),
        (Carrier.C4, FailureCode.C4_UNSUPPORTED),
    ):
        cert, replay = compile_and_replay(Exp(Symbol("x")), carrier)
        assert cert.status is DecisionStatus.UNSUPPORTED
        assert cert.minimum_declared_carrier is Carrier.C2
        assert cert.eliminability == "surreal-runtime-eliminable-for-frozen-syntax-decision"
        assert any(item["code"] == code.value for item in cert.failures)
        assert replay.valid


def test_negative_integer_power_is_explicit_finite_laurent_c1():
    cert, replay = compile_and_replay(Pow(Symbol("N"), -2))
    assert cert.minimum_declared_carrier is Carrier.C1
    assert "negative-integer-power" in cert.features
    assert cert.normal_form_capability == "explicit-finite-support-only"
    assert replay.valid


def test_c2_does_not_claim_normal_form_or_comparison():
    cert, replay = compile_and_replay(Exp(Symbol("x")))
    assert cert.minimum_declared_carrier is Carrier.C2
    assert cert.normal_form_capability == "not-implemented"
    assert cert.comparison_capability == "not-implemented"
    assert {item.code for item in cert.task_obligations} == {
        "le-normal-form", "le-domain-branches", "le-comparison"
    }
    assert cert.cost.residual_items == 3
    assert replay.valid


def test_finite_height_budget_is_typed():
    expr = Symbol("x")
    for _ in range(4):
        expr = Exp(expr)
    cert = CarrierCompiler(CompilerBudget(max_finite_height=3)).compile(expr)
    assert cert.status is DecisionStatus.RESOURCE_EXCEEDED
    assert cert.failures[0]["code"] == FailureCode.HEIGHT_BUDGET.value


def test_replay_rejects_tampered_positive_carrier():
    expr = Exp(Symbol("x"))
    cert = CarrierCompiler().compile(expr).to_data()
    cert["minimum_declared_carrier"] = Carrier.C0.value
    replay = replay_certificate(expr.to_data(), cert)
    assert not replay.valid
    assert "certificate-digest-mismatch" in replay.failures
    assert "carrier-lacks-feature-closure" in replay.failures


def test_replay_rejects_digest_recomputed_overpromotion():
    expr = Add(Symbol("x"), Const(1))
    cert = CarrierCompiler().compile(expr).to_data()
    assert cert["minimum_declared_carrier"] == Carrier.C0.value
    cert["minimum_declared_carrier"] = Carrier.C1.value
    payload = dict(cert)
    payload.pop("certificate_digest")
    cert["certificate_digest"] = digest(payload)
    replay = replay_certificate(expr.to_data(), cert)
    assert not replay.valid
    assert replay.failures == ("carrier-not-minimum-in-frozen-matrix",)


def test_replay_rejects_closed_or_missing_c2_task_obligations():
    expr = Exp(Symbol("x"))
    cert = CarrierCompiler().compile(expr).to_data()
    cert["task_obligations"] = []
    payload = dict(cert)
    payload.pop("certificate_digest")
    cert["certificate_digest"] = digest(payload)
    replay = replay_certificate(expr.to_data(), cert)
    assert not replay.valid
    assert "c2-task-obligations-invalid" in replay.failures


def test_cost_axes_are_separate_and_nonzero_for_positive_case():
    cert = CarrierCompiler().compile(Exp(Symbol("x")))
    assert cert.cost.compilation_steps > 0
    assert cert.cost.certificate_bytes > 0
    assert cert.cost.certificate_bytes == len(canonical_json(cert.to_data()).encode("utf-8"))
    assert cert.cost.replay_steps > 0
    assert cert.cost.residual_items == 3
    assert cert.cost.decoder_steps == 1

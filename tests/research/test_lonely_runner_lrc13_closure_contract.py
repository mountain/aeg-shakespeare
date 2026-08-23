"""Executable closure contract and upstream-snapshot red teams for Sonnet 001.

These tests encode the declaration layer for the hypotheses of the
finite-checking proposition used by the current Lonely Runner computation.
They intentionally do not treat self-reported statuses as verified mathematics.
The frozen upstream K=13 snapshot is a negative audit fixture, not evidence that
LRC(13) has been proved or disproved.
"""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys

import pytest


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "lrc13_closure_contract.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_lrc13_closure_contract",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_frozen_upstream_k13_snapshot_exposes_all_current_blockers():
    m = _load()

    diagnostic = m.diagnose_upstream_k13_snapshot()

    assert len(m.UPSTREAM_K13_PRIME_MANIFEST) == 45
    assert len(diagnostic.manifest.unique_entries) == 44
    assert diagnostic.manifest.duplicate_entries == (293,)
    assert not diagnostic.manifest.valid

    # The duplicate must not inflate the theorem product.  Even the product of
    # all 44 unique candidates is far below the exact B_13 threshold.
    comparison = diagnostic.unique_product_comparison
    assert comparison.cross_multiplication_margin < 0
    assert not comparison.meets_bound
    assert comparison.exact_bound_over_product > 1
    assert comparison.log10_bound_over_product > 0

    assert diagnostic.missing_j_certificates == diagnostic.manifest.unique_entries
    assert diagnostic.compiled_target_k == 9
    assert not diagnostic.compiled_target_matches
    assert diagnostic.results_artifact == "results/result_14"
    assert not diagnostic.results_artifact_present


def test_b13_factorization_and_snapshot_gap_are_exact():
    m = _load()

    # C(14,2)=91=7*13, so ((91**12)/13)**13 is integral with
    # factorization 7**156 * 13**143.
    assert m.lonely_runner_product_bound(13) == Fraction(
        7**156 * 13**143
    )
    comparison = m.diagnose_upstream_k13_snapshot().unique_product_comparison
    assert comparison.product * comparison.bound.denominator < comparison.bound.numerator
    assert comparison.cross_multiplication_margin < 0


def test_validated_contract_rejects_duplicate_and_nonprime_manifests():
    m = _load()
    certificate = m.JEmptyCertificate(
        2,
        m.JEmptyStatus.VERIFIED_EMPTY,
        artifact="memory://j-empty-calibration/2",
    )

    with pytest.raises(ValueError, match="duplicate primes"):
        m.LRCClosureContract(
            k=3,
            primes=(2, 2, 3),
            j_empty_certificates=(certificate,),
            predecessor_lrc_proved=True,
            compiled_target_k=3,
            results_artifact="results/result_3",
            results_artifact_present=True,
        )

    for invalid_manifest in ((2, 9), (1, 2), (True, 3)):
        with pytest.raises(ValueError, match="nonprime entries"):
            m.LRCClosureContract(
                k=3,
                primes=invalid_manifest,
                j_empty_certificates=(),
                predecessor_lrc_proved=True,
                compiled_target_k=3,
                results_artifact="results/result_3",
                results_artifact_present=True,
            )


def test_bound_comparison_is_exact_even_when_b_k_is_not_integral():
    m = _load()

    bound = m.lonely_runner_product_bound(6)
    assert bound.denominator > 1

    # Directly verify the same integer cross multiplication recorded by the
    # report.  Floating logs are deliberately not consulted as a decision rule.
    comparison = m.compare_prime_product_to_bound(6, (2, 3, 5, 7, 11, 13))
    expected_margin = comparison.product * bound.denominator - bound.numerator
    assert comparison.bound == bound
    assert comparison.cross_multiplication_margin == expected_margin
    assert comparison.meets_bound == (expected_margin >= 0)


def test_report_separates_hypothesis_and_reproducibility_declarations():
    m = _load()

    contract = m.LRCClosureContract(
        k=3,
        primes=(2, 3, 5, 7, 11),
        j_empty_certificates=(
            m.JEmptyCertificate(
                2,
                m.JEmptyStatus.VERIFIED_EMPTY,
                artifact="memory://j-empty-calibration/2",
            ),
        ),
        predecessor_lrc_proved=True,
        compiled_target_k=9,
        results_artifact="results/result_4",
        results_artifact_present=False,
    )
    report = contract.report()

    assert report.product_comparison.meets_bound  # 2310 >= B_3 = 1728.
    assert report.bound == Fraction(1728)
    assert report.missing_j_certificates == (3, 5, 7, 11)
    assert any(
        "missing declared J(3, p)-empty" in blocker
        for blocker in report.hypothesis_declaration_blockers
    )
    assert any(
        "compiled target K=9" in blocker
        for blocker in report.reproducibility_blockers
    )
    assert any(
        "results artifact is absent" in blocker
        for blocker in report.reproducibility_blockers
    )
    assert not report.finite_checking_hypotheses_declared_complete
    assert not report.reproducibility_inputs_declared_complete


def test_small_complete_declaration_never_claims_to_verify_theorem_artifacts():
    m = _load()

    primes = (2, 3, 5, 7, 11)
    certificates = tuple(
        m.JEmptyCertificate(
            prime,
            m.JEmptyStatus.VERIFIED_EMPTY,
            artifact=f"results/j_empty_3_{prime}.json",
        )
        for prime in primes
    )
    report = m.LRCClosureContract(
        k=3,
        primes=primes,
        j_empty_certificates=certificates,
        predecessor_lrc_proved=True,
        compiled_target_k=3,
        results_artifact="results/result_4",
        results_artifact_present=True,
    ).report()

    assert report.product_comparison.product == 2310
    assert report.product_comparison.meets_bound
    assert not report.missing_j_certificates
    assert not report.nonempty_j_certificates
    assert not report.hypothesis_declaration_blockers
    assert not report.reproducibility_blockers
    assert report.finite_checking_hypotheses_declared_complete
    assert report.reproducibility_inputs_declared_complete
    assert not hasattr(report, "mathematically_closed")
    assert not hasattr(report, "reproducibly_closed")


def test_contract_rejects_truthy_nonboolean_status_and_nonnative_target_type():
    m = _load()
    base = dict(
        k=3,
        primes=(2, 3, 5, 7, 11),
        j_empty_certificates=tuple(
            m.JEmptyCertificate(
                prime,
                m.JEmptyStatus.VERIFIED_EMPTY,
                artifact=f"results/j_empty_3_{prime}.json",
            )
            for prime in (2, 3, 5, 7, 11)
        ),
        compiled_target_k=3,
        results_artifact="results/result_4",
        results_artifact_present=True,
    )

    with pytest.raises(TypeError, match="predecessor_lrc_proved"):
        m.LRCClosureContract(predecessor_lrc_proved="yes", **base)

    with pytest.raises(TypeError, match="compiled_target_k"):
        m.LRCClosureContract(
            predecessor_lrc_proved=True,
            **{**base, "compiled_target_k": 3.0},
        )

    with pytest.raises(TypeError, match="results_artifact_present"):
        m.LRCClosureContract(
            predecessor_lrc_proved=True,
            **{**base, "results_artifact_present": "yes"},
        )

    with pytest.raises(TypeError, match="results_artifact"):
        m.LRCClosureContract(
            predecessor_lrc_proved=True,
            **{**base, "results_artifact": True},
        )

    with pytest.raises(ValueError, match="expected aggregate output"):
        m.LRCClosureContract(
            predecessor_lrc_proved=True,
            **{**base, "results_artifact": "   "},
        )


def test_declared_verifier_result_requires_an_artifact_locator():
    m = _load()

    with pytest.raises(ValueError, match="artifact locator"):
        m.JEmptyCertificate(2, m.JEmptyStatus.VERIFIED_EMPTY)


def test_declared_nonempty_j_is_an_explicit_hypothesis_blocker():
    m = _load()

    primes = (2, 3, 5, 7, 11)
    certificates = tuple(
        m.JEmptyCertificate(
            prime,
            (
                m.JEmptyStatus.VERIFIED_NONEMPTY
                if prime == 7
                else m.JEmptyStatus.VERIFIED_EMPTY
            ),
            artifact=f"memory://j-status-calibration/{prime}",
        )
        for prime in primes
    )
    report = m.LRCClosureContract(
        k=3,
        primes=primes,
        j_empty_certificates=certificates,
        predecessor_lrc_proved=True,
        compiled_target_k=3,
        results_artifact="results/result_4",
        results_artifact_present=True,
    ).report()

    assert report.nonempty_j_certificates == (7,)
    assert not report.finite_checking_hypotheses_declared_complete
    assert not report.reproducibility_inputs_declared_complete

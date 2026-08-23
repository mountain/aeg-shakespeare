"""Research-local closure contract for the Sonnet 001 LRC computation.

The finite-checking theorem used by the current Lonely Runner computation says
that, for ``k >= 3``, a set ``P`` of primes closes ``LRC(k)`` when

* ``LRC(k - 1)`` is already established;
* ``J(k, p)`` is certified empty for every ``p`` in ``P``; and
* ``prod(P) >= B_k``, where

  ``B_k = ((binom(k + 1, 2) ** (k - 1)) / k) ** k``.

This module turns those hypotheses into an explicit *declaration audit*.  The
product comparison is performed by integer cross multiplication.  Decimal
logarithms are exposed only as human-scale diagnostics and never affect the
audit.

The theorem hypotheses are deliberately separated from two reproducibility
declarations: the C++ executable must be compiled for the intended ``k``, and
the declared aggregate results artifact must exist.  This module does not read
or verify J-empty certificates, predecessor-theorem evidence, generator output,
or an aggregate artifact.  Consequently it exposes only whether the required
claims have been *declared* consistently.  It never reports that a theorem is
mathematically or reproducibly closed; that judgment belongs to a future
independent artifact verifier.

The constants near the end freeze the upstream ``LrcVerifier<13>`` snapshot
inspected on 2026-08-24.  That snapshot is an adversarial input: its manifest
contains a duplicate 293, its unique-prime product is below ``B_13``, the
executable currently selects ``K = 9``, and no ``results/result_14`` aggregate
artifact is present.  Recording these facts is not a claim that ``LRC(13)`` has
been proved or disproved.

This is Sonnet-local research code, not a public Process Geometry API.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from math import comb, isqrt, log10, prod
from typing import Iterable


class JEmptyStatus(str, Enum):
    """Audited status of the proposition ``J(k, p) = empty``."""

    MISSING = "missing"
    VERIFIED_EMPTY = "verified-empty"
    VERIFIED_NONEMPTY = "verified-nonempty"


@dataclass(frozen=True)
class JEmptyCertificate:
    """Declared verifier status and artifact locator for one J-empty claim.

    The referenced artifact is not read by this declaration-layer module.
    """

    prime: int
    status: JEmptyStatus
    artifact: str | None = None

    def __post_init__(self) -> None:
        if not _is_prime(self.prime):
            raise ValueError(f"certificate prime must be prime: {self.prime!r}")
        if not isinstance(self.status, JEmptyStatus):
            raise TypeError("status must be a JEmptyStatus")
        if self.artifact is not None and (
            not isinstance(self.artifact, str) or not self.artifact.strip()
        ):
            raise ValueError("artifact must be a nonempty string or None")
        if self.status is not JEmptyStatus.MISSING and self.artifact is None:
            raise ValueError(
                "a declared verifier result requires an artifact locator"
            )


@dataclass(frozen=True)
class PrimeManifestAudit:
    """Non-throwing diagnostic for a raw prime manifest."""

    entries: tuple[int, ...]
    unique_entries: tuple[int, ...]
    duplicate_entries: tuple[int, ...]
    nonprime_entries: tuple[int, ...]

    @property
    def valid(self) -> bool:
        return not self.duplicate_entries and not self.nonprime_entries


@dataclass(frozen=True)
class ProductComparison:
    """Exact product/bound comparison plus non-authoritative log diagnostics."""

    product: int
    bound: Fraction
    cross_multiplication_margin: int
    meets_bound: bool
    exact_bound_over_product: Fraction
    log10_product: float
    log10_bound: float
    log10_bound_over_product: float


@dataclass(frozen=True)
class ClosureReport:
    """Machine-checkable consistency of a finite-checking declaration.

    ``*_declared_complete`` means only that all required propositions were
    supplied with mutually consistent status labels and that the exact prime
    product gate passed.  It is deliberately not a theorem verdict.
    """

    k: int
    primes: tuple[int, ...]
    bound: Fraction
    product_comparison: ProductComparison
    missing_j_certificates: tuple[int, ...]
    nonempty_j_certificates: tuple[int, ...]
    predecessor_lrc_proved: bool
    compiled_target_k: int | None
    compiled_target_matches: bool
    results_artifact: str
    results_artifact_present: bool
    hypothesis_declaration_blockers: tuple[str, ...]
    reproducibility_blockers: tuple[str, ...]
    finite_checking_hypotheses_declared_complete: bool
    reproducibility_inputs_declared_complete: bool


@dataclass(frozen=True)
class UpstreamK13SnapshotDiagnostic:
    """Frozen audit of the currently inspected upstream K=13 declaration."""

    manifest: PrimeManifestAudit
    unique_product_comparison: ProductComparison
    missing_j_certificates: tuple[int, ...]
    compiled_target_k: int
    compiled_target_matches: bool
    results_artifact: str
    results_artifact_present: bool


def _is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def _ordered_unique(values: Iterable[int]) -> tuple[int, ...]:
    seen: set[int] = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return tuple(result)


def audit_prime_manifest(primes: Iterable[int]) -> PrimeManifestAudit:
    """Diagnose duplicates/nonprimes without normalizing them away silently."""

    entries = tuple(primes)
    unique_entries = _ordered_unique(entries)
    duplicate_entries = tuple(
        value for value in unique_entries if entries.count(value) > 1
    )
    nonprime_entries = tuple(value for value in unique_entries if not _is_prime(value))
    return PrimeManifestAudit(
        entries=entries,
        unique_entries=unique_entries,
        duplicate_entries=duplicate_entries,
        nonprime_entries=nonprime_entries,
    )


def lonely_runner_product_bound(k: int) -> Fraction:
    """Return ``B_k`` exactly as a reduced rational number."""

    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("the finite-checking closure contract requires integer k >= 3")
    inner = Fraction(comb(k + 1, 2) ** (k - 1), k)
    return inner**k


def _log10_positive_integer(value: int) -> float:
    """Stable-enough display log for an arbitrary-size positive integer.

    Only the leading 16 decimal digits are converted to float.  This helper is
    diagnostic; exact decisions use ``cross_multiplication_margin`` instead.
    """

    digits = str(value)
    leading = int(digits[:16])
    return log10(leading) + len(digits) - len(str(leading))


def _log10_fraction(value: Fraction) -> float:
    if value <= 0:
        raise ValueError("log diagnostic requires a positive rational")
    return _log10_positive_integer(value.numerator) - _log10_positive_integer(
        value.denominator
    )


def compare_prime_product_to_bound(
    k: int,
    primes: Iterable[int],
) -> ProductComparison:
    """Compare a prime product with ``B_k`` using exact integer arithmetic.

    This utility validates primality but intentionally accepts no duplicates;
    callers cannot accidentally inflate a theorem product by repeating a prime.
    """

    entries = tuple(primes)
    audit = audit_prime_manifest(entries)
    if audit.duplicate_entries:
        raise ValueError(f"duplicate primes: {audit.duplicate_entries!r}")
    if audit.nonprime_entries:
        raise ValueError(f"nonprime entries: {audit.nonprime_entries!r}")
    if not entries:
        raise ValueError("at least one prime is required")

    bound = lonely_runner_product_bound(k)
    prime_product = prod(entries)
    # product >= numerator / denominator iff product*denominator >= numerator.
    margin = prime_product * bound.denominator - bound.numerator
    ratio = bound / prime_product
    log10_product = _log10_positive_integer(prime_product)
    log10_bound = _log10_fraction(bound)
    return ProductComparison(
        product=prime_product,
        bound=bound,
        cross_multiplication_margin=margin,
        meets_bound=margin >= 0,
        exact_bound_over_product=ratio,
        log10_product=log10_product,
        log10_bound=log10_bound,
        log10_bound_over_product=log10_bound - log10_product,
    )


@dataclass(frozen=True)
class LRCClosureContract:
    """Validated declaration of one finite-checking closure attempt.

    Status fields are provenance metadata, not proof checks.  In particular,
    this class cannot certify an LRC theorem without a separate verifier for the
    referenced mathematical artifacts.
    """

    k: int
    primes: tuple[int, ...]
    j_empty_certificates: tuple[JEmptyCertificate, ...]
    predecessor_lrc_proved: bool
    compiled_target_k: int | None
    results_artifact: str
    results_artifact_present: bool

    def __post_init__(self) -> None:
        lonely_runner_product_bound(self.k)
        if not isinstance(self.predecessor_lrc_proved, bool):
            raise TypeError("predecessor_lrc_proved must be bool")
        if self.compiled_target_k is not None and (
            isinstance(self.compiled_target_k, bool)
            or not isinstance(self.compiled_target_k, int)
        ):
            raise TypeError("compiled_target_k must be int or None")
        if not isinstance(self.results_artifact_present, bool):
            raise TypeError("results_artifact_present must be bool")
        manifest = audit_prime_manifest(self.primes)
        if manifest.duplicate_entries:
            raise ValueError(f"duplicate primes: {manifest.duplicate_entries!r}")
        if manifest.nonprime_entries:
            raise ValueError(f"nonprime entries: {manifest.nonprime_entries!r}")
        if not self.primes:
            raise ValueError("at least one prime is required")

        certificate_primes = tuple(
            certificate.prime for certificate in self.j_empty_certificates
        )
        duplicate_certificates = audit_prime_manifest(
            certificate_primes
        ).duplicate_entries
        if duplicate_certificates:
            raise ValueError(
                f"duplicate J-empty certificate entries: {duplicate_certificates!r}"
            )
        undeclared = tuple(
            prime for prime in certificate_primes if prime not in set(self.primes)
        )
        if undeclared:
            raise ValueError(f"certificates for undeclared primes: {undeclared!r}")
        if not isinstance(self.results_artifact, str):
            raise TypeError("results_artifact must be a string locator")
        if not self.results_artifact.strip():
            raise ValueError("results_artifact must name the expected aggregate output")

    def report(self) -> ClosureReport:
        statuses = {
            certificate.prime: certificate.status
            for certificate in self.j_empty_certificates
        }
        missing = tuple(
            prime
            for prime in self.primes
            if statuses.get(prime, JEmptyStatus.MISSING) is JEmptyStatus.MISSING
        )
        nonempty = tuple(
            prime
            for prime in self.primes
            if statuses.get(prime) is JEmptyStatus.VERIFIED_NONEMPTY
        )
        comparison = compare_prime_product_to_bound(self.k, self.primes)
        compiled_matches = self.compiled_target_k == self.k

        hypothesis_declaration_blockers = []
        if not self.predecessor_lrc_proved:
            hypothesis_declaration_blockers.append(
                f"LRC({self.k - 1}) is not declared established"
            )
        if missing:
            hypothesis_declaration_blockers.append(
                f"missing declared J({self.k}, p)-empty certificates for {missing!r}"
            )
        if nonempty:
            hypothesis_declaration_blockers.append(
                f"J({self.k}, p) is certified nonempty for {nonempty!r}"
            )
        if not comparison.meets_bound:
            hypothesis_declaration_blockers.append(
                f"prime product is below the exact B_{self.k} threshold"
            )

        reproducibility_blockers = []
        if not compiled_matches:
            reproducibility_blockers.append(
                f"compiled target K={self.compiled_target_k!r}, expected {self.k}"
            )
        if not self.results_artifact_present:
            reproducibility_blockers.append(
                f"results artifact is absent: {self.results_artifact}"
            )

        hypotheses_declared = not hypothesis_declaration_blockers
        reproducibility_declared = (
            hypotheses_declared and not reproducibility_blockers
        )
        return ClosureReport(
            k=self.k,
            primes=self.primes,
            bound=comparison.bound,
            product_comparison=comparison,
            missing_j_certificates=missing,
            nonempty_j_certificates=nonempty,
            predecessor_lrc_proved=self.predecessor_lrc_proved,
            compiled_target_k=self.compiled_target_k,
            compiled_target_matches=compiled_matches,
            results_artifact=self.results_artifact,
            results_artifact_present=self.results_artifact_present,
            hypothesis_declaration_blockers=tuple(
                hypothesis_declaration_blockers
            ),
            reproducibility_blockers=tuple(reproducibility_blockers),
            finite_checking_hypotheses_declared_complete=hypotheses_declared,
            reproducibility_inputs_declared_complete=reproducibility_declared,
        )


# Frozen verbatim from upstream main.cpp's LrcVerifier<13> on 2026-08-24.
UPSTREAM_K13_PRIME_MANIFEST = (
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    307,
    311,
    313,
    347,
    379,
    433,
    439,
    443,
    449,
    457,
    461,
    241,
    293,
    293,
    317,
    331,
    337,
    349,
    353,
    359,
    367,
    373,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
)
UPSTREAM_COMPILED_TARGET_K = 9
UPSTREAM_K13_RESULTS_ARTIFACT = "results/result_14"
UPSTREAM_K13_RESULTS_ARTIFACT_PRESENT = False


def diagnose_upstream_k13_snapshot() -> UpstreamK13SnapshotDiagnostic:
    """Audit the frozen upstream snapshot without repairing its duplicate."""

    manifest = audit_prime_manifest(UPSTREAM_K13_PRIME_MANIFEST)
    comparison = compare_prime_product_to_bound(13, manifest.unique_entries)
    return UpstreamK13SnapshotDiagnostic(
        manifest=manifest,
        unique_product_comparison=comparison,
        missing_j_certificates=manifest.unique_entries,
        compiled_target_k=UPSTREAM_COMPILED_TARGET_K,
        compiled_target_matches=UPSTREAM_COMPILED_TARGET_K == 13,
        results_artifact=UPSTREAM_K13_RESULTS_ARTIFACT,
        results_artifact_present=UPSTREAM_K13_RESULTS_ARTIFACT_PRESENT,
    )


def main() -> None:
    diagnostic = diagnose_upstream_k13_snapshot()
    comparison = diagnostic.unique_product_comparison
    print("Sonnet 001 LRC(13) closure-contract audit")
    print(f"  manifest entries:       {len(diagnostic.manifest.entries)}")
    print(f"  unique primes:          {len(diagnostic.manifest.unique_entries)}")
    print(f"  duplicate entries:      {diagnostic.manifest.duplicate_entries}")
    print(f"  product meets B_13:     {comparison.meets_bound}")
    print(f"  log10(B_13/product):    {comparison.log10_bound_over_product:.6f}")
    print(f"  missing J certificates: {len(diagnostic.missing_j_certificates)}")
    print(f"  compiled target K:      {diagnostic.compiled_target_k}")
    print(f"  result_14 present:      {diagnostic.results_artifact_present}")
    print("  LRC(13) status:         OPEN")


if __name__ == "__main__":
    main()

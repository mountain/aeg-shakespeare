"""Lonely Runner Phase 0: exact ground truth before representation search.

Question
--------
Can the first Shakespeare sonnet freeze the exact semantics needed to compare
alternative representations of the Lonely Runner finite search, without already
assuming the existing sieve implementation as ontology?

Primitive data
--------------
Only integer speed tuples, rational times, the standard loneliness threshold
1/(k+1), and for the finite ansatz a prime p and lift denominator l.

No Fourier analysis, zonotope geometry, polynomial-method structure, or upstream
C++ search state is supplied.

Classical lineage
-----------------
The modern computer-assisted route reduces LRC(k) to modular proper/improper
checks followed by lifting and projection.  In particular, Sungkawichai and
Trakulthongchai define (k,p,l)-properness by a gcd certificate or by existence of
a witness on the 1/(lp) rational grid, quotient the initial modulo-p search by
permutations/sign flips/unit scaling, and identify computation of I(k,p,1) as the
main bottleneck for k=13.

Shakespeare reconstruction
---------------------------
This file separates three semantic layers that future presentation search must
not conflate:

1. the exact continuous LR predicate;
2. the exact finite ansatz certificate;
3. bounded future behavior under lift.

The final red team gives two inequivalent modulo-13 tuples with the same current
status at l=1 (both improper) but different properness signatures after all c=2
lifts.  Thus a quotient based only on the current proper/improper bit is unsound;
future task behavior carries additional information.

Calibration statement
---------------------
Passing this file certifies an exact small-instance oracle, the finite ansatz
predicate, the known modulo-p symmetry quotient, and one concrete
current-observation-vs-future-behavior separation.  It does not compute I(13,p,1)
or prove LRC(13).

Proof map
---------
1. Boundary times -> exact continuous feasibility for small integer speeds.
2. Tight tuple -> threshold calibration and strengthened-threshold red team.
3. Rational grid + gcd clause -> exact (k,p,l)-properness certificate.
4. Unit/sign/permutation action -> canonical modulo-p representatives.
5. Two l=1-improper states -> distinct c=2 future properness signatures.

Boundary
--------
The boundary oracle is intentionally O(sum |u_i|) and is only a ground-truth
instrument.  The lift-signature enumeration is exponential in k and is likewise
only a red-team/calibration device.  Neither is proposed as the k=13 solver.

References
----------
[Malikiosis-Santos-Schymura-2025] R. D. Malikiosis, F. Santos, M. Schymura,
Linearly exponential checking is enough for the lonely runner conjecture and some
of its variants, Forum of Mathematics, Sigma 13 (2025), e164.

[Sungkawichai-Trakulthongchai-2026] T. Sungkawichai, T. Trakulthongchai,
Eleven, twelve, and thirteen lonely runners, arXiv:2604.23906 (2026).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
from typing import Literal, Sequence


@dataclass(frozen=True)
class PropernessCertificate:
    """Exact local certificate for the finite (k,p,l) ansatz."""

    reason: Literal["gcd", "witness"]
    witness: Fraction | None = None
    omitted_index: int | None = None
    divisor: int | None = None


def _normalized_speeds(speeds: Sequence[int]) -> tuple[int, ...]:
    values = tuple(abs(int(speed)) for speed in speeds)
    if not values:
        raise ValueError("at least one speed is required")
    if any(speed == 0 for speed in values):
        raise ValueError("relative speeds must be nonzero")
    return values


def distance_to_integer(value: Fraction) -> Fraction:
    """Exact distance on R/Z."""

    residue = value % 1
    return min(residue, 1 - residue)


def lonely_margin(speeds: Sequence[int], time: Fraction) -> Fraction:
    """Return min_i ||u_i t|| exactly."""

    values = _normalized_speeds(speeds)
    return min(distance_to_integer(speed * time) for speed in values)


def standard_threshold(speeds: Sequence[int]) -> Fraction:
    values = _normalized_speeds(speeds)
    return Fraction(1, len(values) + 1)


def boundary_times(
    speeds: Sequence[int],
    threshold: Fraction,
) -> tuple[Fraction, ...]:
    """All circle times where one loneliness inequality is exactly tight.

    For integer speed u, a boundary satisfies

        u t = m +/- threshold  (mod 1).

    Checking these finitely many rational points is exact for positive threshold:
    the feasible set is closed, t=0 is infeasible, and any nonempty feasible set
    therefore has a boundary point among these events.
    """

    values = _normalized_speeds(speeds)
    threshold = Fraction(threshold)
    if not (0 < threshold <= Fraction(1, 2)):
        raise ValueError("threshold must lie in (0, 1/2]")

    events: set[Fraction] = set()
    for speed in values:
        for integer_part in range(speed):
            for sign in (-1, 1):
                event = (Fraction(integer_part) + sign * threshold) / speed
                events.add(event % 1)
    return tuple(sorted(events))


def find_exact_witness(
    speeds: Sequence[int],
    *,
    threshold: Fraction | None = None,
) -> Fraction | None:
    """Exact continuous witness search for small integer-speed instances."""

    values = _normalized_speeds(speeds)
    target = standard_threshold(values) if threshold is None else Fraction(threshold)
    for time in boundary_times(values, target):
        if lonely_margin(values, time) >= target:
            return time
    return None


def grid_witnesses(
    speeds: Sequence[int],
    denominator: int,
    *,
    threshold: Fraction | None = None,
) -> tuple[Fraction, ...]:
    """Return all exact witnesses on (1/denominator) Z / Z."""

    values = _normalized_speeds(speeds)
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    target = standard_threshold(values) if threshold is None else Fraction(threshold)
    return tuple(
        Fraction(numerator, denominator)
        for numerator in range(denominator)
        if lonely_margin(values, Fraction(numerator, denominator)) >= target
    )


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def canonical_mod_p(speeds: Sequence[int], p: int) -> tuple[int, ...]:
    """Canonicalize under permutation, independent signs, and global units.

    This is the exact equivalence used in the current modular LRC implementation.
    We enumerate the global unit action; sign flips fold each nonzero residue into
    the first half of the field; permutation is removed by sorting.
    """

    if not _is_prime(p):
        raise ValueError("p must be prime")
    residues = tuple(int(speed) % p for speed in speeds)
    if not residues or any(residue == 0 for residue in residues):
        raise ValueError("all modulo-p speeds must be nonzero")

    candidates: list[tuple[int, ...]] = []
    for unit in range(1, p):
        folded = []
        for residue in residues:
            transformed = unit * residue % p
            folded.append(min(transformed, (-transformed) % p))
        candidates.append(tuple(sorted(folded)))
    return min(candidates)


def kpl_properness_certificate(
    speeds: Sequence[int],
    *,
    p: int,
    l: int,
) -> PropernessCertificate | None:
    """Implement the exact local properness predicate from the finite ansatz."""

    if not _is_prime(p):
        raise ValueError("p must be prime")
    if l <= 0:
        raise ValueError("l must be positive")

    modulus = p * l
    residues = tuple(int(speed) % modulus for speed in speeds)
    if not residues or any(residue % p == 0 for residue in residues):
        raise ValueError("speeds must lie in Z_{p,l}, hence be nonzero modulo p")

    for omitted in range(len(residues)):
        divisor = l
        for index, residue in enumerate(residues):
            if index != omitted:
                divisor = gcd(divisor, residue)
        if divisor > 1:
            return PropernessCertificate(
                reason="gcd",
                omitted_index=omitted,
                divisor=divisor,
            )

    witnesses = grid_witnesses(residues, modulus)
    if witnesses:
        return PropernessCertificate(reason="witness", witness=witnesses[0])
    return None


def lift_properness_signature(
    base_speeds: Sequence[int],
    *,
    p: int,
    c: int,
) -> tuple[bool, ...]:
    """Bounded future signature over every c-lift of one modulo-p state."""

    if c <= 0:
        raise ValueError("c must be positive")
    base = tuple(int(speed) % p for speed in base_speeds)
    if any(residue == 0 for residue in base):
        raise ValueError("base speeds must be nonzero modulo p")

    signature = []
    for lift_digits in product(range(c), repeat=len(base)):
        lifted = tuple(
            residue + digit * p for residue, digit in zip(base, lift_digits)
        )
        signature.append(
            kpl_properness_certificate(lifted, p=p, l=c) is not None
        )
    return tuple(signature)


# ASSERT: the continuous oracle recognizes the classical tight tuple exactly.
def test_exact_boundary_oracle_and_tight_threshold_red_team() -> None:
    speeds = (1, 2, 3, 4)
    threshold = Fraction(1, 5)

    witness = find_exact_witness(speeds)
    assert witness is not None
    assert lonely_margin(speeds, witness) == threshold

    # (1,...,k) is tight: any strict strengthening must fail.
    assert find_exact_witness(
        speeds,
        threshold=threshold + Fraction(1, 1000),
    ) is None


# ASSERT: finite ansatz semantics is deliberately weaker than continuous truth.
def test_tight_tuple_needs_the_right_ansatz_denominator() -> None:
    speeds = (1, 2, 3)

    # Continuous LRC(3) witness exists at t = 1/4.
    assert find_exact_witness(speeds) == Fraction(1, 4)

    # With p=5 and l=1 the 1/5 grid cannot see that witness.
    assert kpl_properness_certificate(speeds, p=5, l=1) is None

    # Once the denominator contains k+1=4, the same tuple is certified.
    certificate = kpl_properness_certificate(speeds, p=5, l=4)
    assert certificate is not None
    assert certificate.reason == "witness"
    assert certificate.witness == Fraction(1, 4)


# ASSERT: the known modulo-p presentation really quotients its declared symmetry.
def test_mod_p_canonicalization_respects_known_equivalence() -> None:
    p = 17
    original = (1, 4, 7)

    # Global unit x3, independent sign flips, and a permutation.
    transformed = (-3 * 7, 3 * 1, -3 * 4)

    assert canonical_mod_p(original, p) == canonical_mod_p(transformed, p)


# RED TEAM: current proper/improper observation is not a sufficient quotient.
def test_same_current_status_can_have_different_lift_future() -> None:
    p = 13
    left = (1, 2, 3)
    right = (1, 2, 4)

    assert canonical_mod_p(left, p) != canonical_mod_p(right, p)

    # At l=1 both states look identical to the coarsest observer: improper.
    assert kpl_properness_certificate(left, p=p, l=1) is None
    assert kpl_properness_certificate(right, p=p, l=1) is None

    # But their complete c=2 lift behavior differs.  In fact every lift of the
    # right state is already proper, while the tight left state retains survivors.
    left_future = lift_properness_signature(left, p=p, c=2)
    right_future = lift_properness_signature(right, p=p, c=2)

    assert left_future != right_future
    assert not all(left_future)
    assert all(right_future)

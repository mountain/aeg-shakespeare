# Phase 1J-B2 results — the mark is local; the missing estimate is global

**Verdict:** the fixed-molecule one-mark operator gate passes.  A pre-cut
root-visible collision mark is a signed-measure pushforward, costs at most one
factor of the molecule's eligible atom count, and commutes with the paper's
exact Fubini cut when retained as an observable.  The global marked molecule
sum and its identification with hard-sphere collision flux remain open.

**Contract:**
[23-phase1j-b2-marked-molecule-flux-lift-contract.md](./23-phase1j-b2-marked-molecule-flux-lift-contract.md).

**Executable:**
[test_marked_molecule_flux_lift.py](../../tests/research/test_marked_molecule_flux_lift.py).

## 1. The local lemma

For a pre-cut molecule \(M\), signed molecule measure \(\lambda_M^Q\), and
root-visible C-atom \(n\), define

\[
\kappa_{M,n}=(e_n)_\#\lambda_M^Q.
\]

Then

\[
\langle\kappa_{M,n},\psi\rangle
=I_M(Q\psi\circ e_n),
\qquad
\|\kappa_{M,n}\|_{\rm TV}\le I_M(|Q|).
\]

Summing the eligible atoms of this one molecule gives

\[
\left\|\sum_n\kappa_{M,n}\right\|_{\rm TV}
\le |\mathcal C_{\rm root}(M)|I_M(|Q|).
\]

This is elementary but consequential: inserting a mark does not create a new
singular analytic kernel at fixed-molecule level.  The unresolved difficulty
is to preserve sufficient gain while summing the marked operation sequences
and then to identify that sum with the physical collision current.

## 2. Exact certificate ledger

The finite fixture has four integration states, positive factored kernel
weights and signed amplitudes.  Its state weights are

\[
1,\quad-\frac14,\quad\frac23,\quad-\frac16.
\]

Hence

\[
I_M(Q)=\frac54,
\qquad
I_M(|Q|)=\frac{25}{12}.
\]

Two of four atoms are eligible root-visible C-atoms.  The other C-atom is
non-root, and the root-visible O-atom is not a collision mark.

| Exact check | Result |
| --- | --- |
| injective inner-event pushforward TV | \(25/12\), equal to the absolute-integral bound |
| coarser outer-event pushforward TV | \(5/4\le25/12\) because fibers cancel |
| aggregate two-mark TV | \(10/3\le25/6\) |
| direct marked pairing for \(\psi=e.\mathrm{cell}-1\) | \(-2/3\) |
| outer marked direct/iterated pairing | both \(13/4\) |
| inner marked direct/iterated pairing | both \(17/3\) |

The targeted run is:

    10 passed in 0.05s

These are finite exact shadows of pushforward contraction and Fubini.  They
are not numerical evidence for the continuum estimate.

## 3. Red-team findings

### 3.1 Post-cut bulk data loses the event map

Two different inner event maps have the same unmarked integral \(5/4\), yet a
test selecting event cell zero pairs to \(1\) in one lift and \(-1/4\) in the
other.  The collision mark cannot be reconstructed after the event variables
have been forgotten.  It must be installed before cutting/integration.

### 3.2 Full bounded dual control is total variation

A signed event measure with weights \(+1\) and \(-1\) on two fine cells has
total variation \(2\).  The sign test in the unit bounded ball attains \(2\),
while a cylinder algebra that forgets the cell sees exactly zero.  Thus the
Phase 1J-B proposal

\[
\sup_{\|\psi\|_\infty\le K}|\langle\nu,\psi\rangle|
\]

is a total-variation target.  It may be stronger than the weak flux topology
needed for Phase 1F or the particular clipped H-test family.  Future work must
state which test class is actually proved.

### 3.3 Linear marking can erase a reciprocal gain

If \(m\) eligible atoms each inherit an unmarked mass \(1/m\), their aggregate
budget remains exactly one.  Atom count is therefore not harmless without a
strictly stronger molecule gain.

Conversely, the exact shadow

\[
n^2 2^{-n}\le 2^{-n/2}\qquad(n\ge16)
\]

shows how a fixed polylogarithmic cost can be absorbed by a retained positive
power of \(\epsilon\).  This is conditional arithmetic, not verification that
all Deng--Hani--Ma subcases retain that margin after marking.

## 4. What the source audit now isolates

Equation (7.6) supplies the signed integral whose event-map pushforward is
used here.  Proposition 8.14 supplies exact Fubini reordering.  Propositions
7.2 and 8.18 bound molecule/operation complexity on admitted classes.  None of
these statements performs the marked global sum or identifies it with a
collision-boundary current.

The theorem gap is now narrower than Phase 1J-B's original statement:

1. define the root-visible event map uniformly in every signed cumulant term;
2. prove a marked analogue of the operation-sequence estimates, retaining a
   summable gain after the linear mark cost;
3. sum all molecule, cut, deletion, split and error categories;
4. identify the resulting signed event measure with the actual/truncated/
   target flux response and control their residuals; and only then
5. address the logarithmic tail and entropy chain rule.

The first two items form the next theorem-sized gate, Phase 1J-B3:
**marked operation-sequence summation**.  Its proof should audit the marked
versions of the roles played by Proposition 3.25, Proposition 7.5,
Proposition 8.18 and the final Section 9 summation, subcase by subcase.

## 5. Claim boundary

Phase 1J-B2 has earned:

- a precise pre-cut root-visible mark;
- the fixed-molecule pushforward/TV lemma;
- exact covariance of the inserted observable under a Fubini cut;
- a linear eligible-atom cost ledger;
- a three-level test-class distinction; and
- a sharply located B3 target.

It has not earned:

- a global marked molecule or cumulant estimate;
- a hard-sphere trace/history/flux identification;
- total-variation or weak convergence of the collision response;
- removal of the logarithmic clip;
- a nonlinear entropy chain rule;
- a continuum or microscopic H theorem; or
- molecule objectification, arithmetic-rank evidence or a generic API.

Phase 1J-A remains independent and supplies none of these conclusions.

## 6. Repository effect

### Mathematical Core

Unchanged.  Pushforward contraction and Fubini are classical tools used in a
research-local certificate.

### Engineering Architecture

Refined research-locally.  Any eventual continuum evaluator must retain an
event map before molecule cutting and declare its test class.  An unmarked
bulk integral is insufficient for flux reconstruction.

### Theory Map

Unchanged.  B2 strengthens the U4/E adaptation ledger but does not add a V2
object or V5 calculus.

### API

No pressure.  The exact classes remain executable documentation only.

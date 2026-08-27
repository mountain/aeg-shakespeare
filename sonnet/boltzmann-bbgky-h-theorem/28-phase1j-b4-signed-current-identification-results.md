# Phase 1J-B4 results — exact ingredients exist, but their marked identity is missing

**Verdict:** physical signed-current identification does not pass. The source
contains an exact signed Penrose endpoint expansion and an exact local
collision-atom integral identity. It does not contain the path-resolved
marked Penrose identity needed to conclude that the B3 formal current is the
collision current of the truncated hard-sphere dynamics.

This is a narrower and more constructive obstruction than the B3 boundary.
The next proof target is now one explicit commutation theorem, not another
global summability estimate.

**Contract:**
[27-phase1j-b4-signed-current-identification-contract.md](./27-phase1j-b4-signed-current-identification-contract.md).

**Executable:**
[test_signed_collision_current_identification.py](../../tests/research/test_signed_collision_current_identification.py).

## 1. Source correction and advance

The statement of Proposition 5.16 displays the positive bound (5.44), but its
proof first derives

\[
E_{H_\ell}
=\sum_{[M_\ell]} IN^{\mathrm{Pen}}_{M_\ell,H_{\ell-1}}
\]

in equations (5.62)--(5.63). Thus the signed cumulant endpoint identity is
present before absolute values. B3 was correct not to infer a current from
positive domination, but too conservative in leaving even the signed
endpoint formula open.

Proposition 7.5 then proves the other local ingredient. Equations
(7.13)--(7.15) identify the collision-atom integral with the prescribed
collision event, including collision time, outgoing state and the
pre-collisional kernel orientation.

These facts justify every individual marked signed term. The missing step is
to show that summing those marked terms equals marking the path-resolved
truncated dynamics.

## 2. The exact missing theorem

Let \(\widehat S^{\Lambda,\Gamma}\) denote a path-resolved lift of the
truncated dynamics and let \(\operatorname{Cur}_H\) extract the oriented
root-visible gain/loss current. The necessary identity is

\[
\operatorname{Cur}_H(\widehat S^{\Lambda,\Gamma}\mu)
=
\sum_{[M]}\sum_{n\in\mathcal C_H(M)}
(e_n)_\#\lambda_M^{\mathrm{Pen}}
+r_{\mathrm{Pen}}
\]

as finite signed measures, or equivalently after pairing with every declared
bounded event test. The main family should have \(r_{\mathrm{Pen}}=0\);
large-component and later errors require their own current types.

One concrete route is to attach a generating mark to every root-visible
C-atom, repeat the inclusion--exclusion proof of Proposition 5.10 with that
deformation, and differentiate at the neutral mark. The combinatorial
Penrose signs arise from O-atoms, while current orientation arises from the
incoming/outgoing pair; both must survive independently.

## 3. Exact certificate ledger

The finite path fixture has three one-collision paths. Two signed Penrose
terms contain a cancelling ghost path and reconstruct the physical path
measure exactly:

\[
\widehat\lambda_{\mathrm{even}}
+\widehat\lambda_{\mathrm{odd}}
=\widehat\mu_{\mathrm{physical}}.
\]

Linearity then reconstructs the oriented current for every tested bounded
covector. Its total mass is zero, as required for gain minus loss, while its
total variation is \(5/2\).

A path residual with weights \(1/5\) and \(-1/7\) has event-current total
variation \(24/35\), exactly twice its path total variation because each path
has one collision and emits a gain/loss pair.

The targeted run is:

    12 passed in 0.05s

These are sufficient-schema certificates. They do not assert that the source
paper's endpoint operator identity already lives in this path space.

## 4. Red-team results

Four shortcuts fail exactly.

1. A one-collision path and a collision-free path can have the same terminal
   state and endpoint mass but different currents.
2. Two signed path families can have the same absolute majorant and different
   signed currents.
3. Two currents can both have total mass zero and total variation two while a
   bounded channel test pairs to one for the first and zero for the second.
4. Forgetting gain/loss orientation pushes a nonzero oriented pairing to
   zero.

A fifth information-loss fixture gives two histories the same forgotten
endpoint while placing their collision on different channels. No post-cut
endpoint datum reconstructs which marked pairing occurred.

## 5. Residual typing

The executable keeps five path/current axes:

- Penrose remainder;
- truncation;
- contact geometry;
- \(\mathrm{Err}_2\); and
- terminal error.

Once these are actual signed path measures, linear pushforward gives an exact
current decomposition. Deng--Hani--Ma currently provide state-level or
\(L^1\) estimates for several of these axes, not the required path/current
measures. The gap is therefore construction and topology, not scalar
bookkeeping.

## 6. What has and has not advanced

B4 has earned:

- a stronger, corrected source audit;
- exact separation of endpoint, path and current identities;
- the minimal marked Penrose theorem statement;
- a complete actual/truncated/target current ledger;
- a current-TV residual bound conditional on a path residual; and
- twelve exact sufficiency and no-go certificates.

B4 has not earned:

- the physical signed-current identity requested in issue 135;
- current-valued truncation, geometry, \(\mathrm{Err}_2\), or terminal
  estimates;
- logarithmic-tail control;
- an entropy chain rule or hard-sphere H theorem; or
- a Core/Map/API promotion.

The highest-value next step is a one-layer proof audit of Proposition 5.10
with a collision generating mark. Success would establish the main signed
current identity before multi-layer summation. Failure would expose the
precise inclusion--exclusion term at which endpoint transport forgets the
collision observable.

## 7. Repository effect

### Mathematical Core

Unchanged.

### Engineering Architecture

Refined research-locally: path-resolved source measures and current extractors
are now explicit prerequisites for any continuum response adapter.

### Theory Map

Unchanged. The completed negative gate sharpens U4/E evidence only.

### API

No pressure.

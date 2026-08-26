# Phase 1J-A contract — ordered finite collision response through C2

**Status:** frozen and executed research-local contract.

**Executable owner:**
[`test_collision_response_cocycle.py`](../../tests/research/test_collision_response_cocycle.py).

**Result owner:**
[`20-phase1j-a-collision-response-cocycle-results.md`](./20-phase1j-a-collision-response-cocycle-results.md).

## 0. Dependency ledger

Phase 1J-A uses three earned inputs and does not import their stronger
neighbours.

1. [Phase 1G](./14-phase1g-selective-continuation-time-reversal-results.md)
   supplies the reversible XOR carrier, one-body forgetting, and renewed
   independent section.
2. [Phase 1I](./18-phase1i-charted-fibre-calculus-results.md) supplies the
   exact one-step target/fibre response ledger and shows that an adjacent A/M
   order control is not yet a collision-derived response calculus.
3. [Phase 12C](../local-field-projective-process-geometry/24-phase12c-objectification-fibred-change-calculus-results.md)
   supplies only the C0--C4 maturity questions: action skeleton, response
   reconstruction, regular cocycle, future adequacy, and effective
   compression.

Phase 12C is a grading framework, not evidence for the present collision
fixture.  No continuum estimate, entropy formula, or correlation-fibre
objectification is borrowed.

## 1. Revised question

Phase 1I retained exact response data but had no collision-native order or
regular response composition.  Phase 1J-A asks:

> Can two overlapping reversible collision cells induce an order-sensitive
> target process, an exact response relation after microscopic forgetting,
> and a regular retained-law response cocycle without introducing tangent,
> logarithmic, entropy, or continuum structure?

The phase is allowed to stop at C2.  A product character may be exposed after
the response gates pass, but a closed one-form or potential is held out.

## 2. Primitive finite collision carrier

Let

\[
\Gamma=\{0,1\}^3
\]

and define two oriented local collision gates

\[
L(x_0,x_1,x_2)=(x_0,x_1\mathbin{\mathtt{xor}}x_0,x_2),
\]

\[
R(x_0,x_1,x_2)=(x_0,x_1,x_2\mathbin{\mathtt{xor}}x_1).
\]

Both are bijective involutions and preserve the uniform reference law.  Each
acts on one adjacent pair and leaves the third site fixed.  Their shared
middle site makes order observable:

\[
(R\circ L)(1,0,0)=(1,1,1),
\qquad
(L\circ R)(1,0,0)=(1,1,0),
\]

where the displayed products are read chronologically from the inner action.
The executable avoids notation ambiguity by storing collision words in their
execution order.

The source carrier is the simplex of probability laws (F) on (Gamma).
The target observer keeps the three one-site occupancies

\[
\pi(F)=(\mathbb P_F[x_0=1],\mathbb P_F[x_1=1],\mathbb P_F[x_2=1])
\in[0,1]^3.
\]

The renewed section is the independent product law

\[
\sigma(p)(x)=\prod_{i=0}^2p_i^{x_i}(1-p_i)^{1-x_i}.
\]

This section is a declared closure policy, not a consequence of microscopic
dynamics.

## 3. Task and type ledger

The following objects must remain separately typed.

| Object | Type | Meaning |
|---|---|---|
| (U_g) | microscopic law (	o) microscopic law | exact collision pushforward |
| (B_g=\pi U_g\sigma) | target state (	o) target state | renewed target action |
| (\mathcal R_g(p)) | set of target vectors | all responses compatible with the forgotten fibre (\pi^{-1}(p)) |
| (r_g(F)) | target vector | retained-law response section |
| (T_v(y,r)) | target vector | state-dependent transport of a prior response through a later word |

The tasks are:

- **T0:** distinguish the two collision orders at microscopic and target level;
- **T1:** reconstruct the exact next target observation;
- **T2:** compose responses across collision words;
- **T3:** compare the occupancy and parity-character charts without selecting
  a covector.

The target action and response are not two names for the same map.  The first
acts on a renewed target state; the second records the closure defect of a
retained microscopic law.

## 4. C0 target action skeleton

For a gate (g=(i\to j)), independence gives

\[
(B_gp)_j=p_i+p_j-2p_ip_j,
\qquad
(B_gp)_k=p_k\quad(k\ne j).
\]

Collision words form the free monoid on (L,R).  With chronological
concatenation (uv), define

\[
B_{uv}=B_v\circ B_u,
\qquad B_{\varnothing}=\mathrm{id}.
\]

C0 passes only if the closed formula agrees with direct collision pushforward
of (sigma(p)), the word action is associative with its identity, and the
two orders remain distinct on a frozen rational witness.

This is an action skeleton for the renewed target process.  It is not a
microscopic quotient because resection occurs in the definition of each
target step.

## 5. C1 response reconstruction and forgetting

For a retained law (F), define

\[
r_g(F)=\pi U_gF-B_g(\pi F).
\]

Then the exact one-step reconstruction is

\[
\boxed{\pi U_gF=B_g(\pi F)+r_g(F).}
\]

After forgetting (F), the honest response object is the relation

\[
\mathcal R_g(p)
=
\{r_g(F):\pi F=p\}.
\]

C1 does not require this relation to be single-valued.  On the contrary, the
phase must provide two laws with the same one-site occupancies and different
required responses.  A base-only selector passes only on the microscopic
subfamily for which it reconstructs the next observation; the renewed choice
(r=0) is not silently extended to arbitrary correlations.

## 6. C2 regular retained-law response cocycle

For a word (u), put

\[
r_u(F)=\pi U_uF-B_u(\pi F).
\]

A later word (v) transports an earlier target displacement by

\[
T_v(y,r)=B_v(y+r)-B_v(y).
\]

The frozen C2 identity is

\[
\boxed{
r_{u\mathbin{\|}v}(F)
=T_v\bigl(B_u(\pi F),r_u(F)\bigr)+r_v(U_uF).
}
\]

This is regular relative to the retained microscopic law: every term is a
declared function, and the identity composes for every tested prefix and
suffix.  It does not make the forgotten response relation a free additive
monoid.  Because (B_v) is bilinear, (T_v(y,r)) depends on the base (y);
the executable must exhibit a strict failure of

\[
r_{u\mathbin{\|}v}(F)=r_u(F)+r_v(U_uF).
\]

## 7. Frozen chart atlas

Only after C0--C2 pass may the following two charts be compared.

| Cost axis | Occupancy (p) | Parity character (z=1-2p) |
|---|---|---|
| dynamics | bilinear XOR probability | one product on the target site |
| composition | ordered target maps | collision-product character |
| covector | not selected | (d\log z) is only a domain-restricted candidate |
| decoder | identity | affine half-map (p=(1-z)/2) |
| residual | additive correction with nonlinear transport | character difference, not a free additive fibre |

For independent inputs the exact collision character is

\[
z\bigl(p_i+p_j-2p_ip_j\bigr)=z(p_i)z(p_j).
\]

The character includes zero and negative values.  Therefore a logarithmic
chart would exclude part of the frozen carrier and require an analytic
primitive absent from the grammar.  Phase 1J-A records this pressure but does
not select, close, or integrate a one-form.

## 8. Candidate grammar and oracle firewall

Allowed operations are:

- finite probability tables on ({0,1}^3);
- exact rational addition, subtraction, multiplication, and comparison;
- reversible pair-local XOR pushforward;
- marginalization and an explicitly declared independent section;
- finite collision words, target composition, relations, and response
  transport.

Forbidden inputs are:

- logarithm, exponential, entropy, relative H, or a supplied covector;
- differentiation, tangent vectors, jets, or an infinitesimal generator;
- continuum collision traces, BBGKY estimates, or molecular-chaos theorems;
- a generic response/fibre API or arithmetic-rank promotion.

## 9. Frozen executable certificates

The standard-library-only executable must certify:

1. locality, bijectivity, involution, and microscopic noncommutativity of the
   two collision gates;
2. direct independent-section agreement and the C0 free-word target action;
3. an exact rational witness of target order sensitivity;
4. C1 reconstruction on every positive denominator-ten microscopic law;
5. the exact response relation over the denominator-eight half-occupancy
   fibre, including two incompatible responses;
6. the C2 cocycle for every frozen positive law and every frozen
   prefix/suffix pair;
7. a strict counterexample to naive response addition and exact repair by
   state-dependent transport;
8. the parity collision-product identity on the frozen rational corpus;
9. the five-axis chart ledger;
10. separate C0--C4, continuum, H, calculus, and rank grades.

The budget is (<10^4) enumerated probability tables and (<1) second on the
reference CI interpreter.

## 10. Conventional baseline and red teams

Direct pushforward of the independent microscopic product law is the
conventional baseline for the target formula.  The response reconstruction
is also checked directly against microscopic pushforward, not against a
second derived formula.

The required red teams are:

- reverse the two overlapping collision gates;
- retain equal one-site marginals while changing pair correlations;
- use the zero-response renewed selector on correlated laws;
- add consecutive response vectors without nonlinear transport;
- convert the parity product to a logarithm across zero or a sign change;
- call the renewed target action a quotient of the closed microscopic orbit.

## 11. Failure semantics and kill conditions

- **pass:** an exact identity holds on the frozen exhaustive corpus;
- **counterexample:** a frozen exact witness falsifies a proposed descent or
  composition;
- **domain mismatch:** a logarithmic or differential candidate is undefined
  on the admitted carrier;
- **inconclusive:** no C3 covector selection is attempted;
- **rank not earned:** response structure exists, but no new object type with
  independent rank semantics has been shown.

The phase is rejected if collision order disappears, the response relation is
quietly replaced by a base-only function, the cocycle uses naive addition,
or the product character is reported as an H theorem.

## 12. Arithmetic Universality pressure

The fixture supplies two bounded pressures only.

- **U2/U4:** changing from occupancy to a parity character changes which
  process law is primitive and simplifies ordered collision composition.
- **E:** exact response transport is a calculation benefit over carrying an
  untyped discrepancy, but it retains the full microscopic law as its regular
  section.

The mechanism is arithmetic-specific: XOR becomes multiplication under the
parity character.  No U5 claim, cross-domain transfer, anti-encoding theorem,
or new arithmetic rank is earned.

## 13. Repository boundary

### Mathematical Core

Unchanged.  The result is a problem-local positive C0--C2 witness and a
set-valued forgetting obstruction, not a generic covariant process calculus.

### Engineering Architecture

Research-local refinement only.  The executable makes action, relation,
retained response, transport, and claim grades explicit; no public interface
is proposed.

### Theory Map

Unchanged.  The result supplies finite pressure on H4 and the
task-covariant-response transversal, while leaving continuum adequacy and
objectification open.

### Research Program

The finite half of Phase 1J is discharged through C2.  Phase 1J-B remains the
next honest gate.

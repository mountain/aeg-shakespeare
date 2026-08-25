# Phase 0 — \(S^6\) complex structure calibration and arithmetic-tower frontier

**Status:** open Sonnet problem; source verification pending; strong interface
unknown.

**Domains:** complex threefolds, torus fibrations, monodromy, degenerations,
covering spaces, arithmetic process towers, task-relative quotients.

**Theory Map relation:** tests H0/H1/H2 and places pressure on V1/V2.  At
initialization it leaves the Theory Map unchanged.

## 1. The external mathematical object

The source manuscript states that there is a compact connected complex
threefold \(X\) with a holomorphic map

\[
f:X\longrightarrow B=\mathbb P^1
\]

whose regular fibres are complex two-tori.  The base has three distinguished
points

\[
p_0=\infty,\qquad p_1=0,\qquad p_2=1,
\]

and

\[
B^\circ=B\setminus\{p_0,p_1,p_2\}.
\]

The two finite local monodromies have orders \(3\) and \(4\); the monodromy at
the cusp \(p_0\) is unipotent with square-zero logarithm.  The three missing
fibres are filled by different mechanisms:

- a reduced irreducible normal-crossings fibre \(W\) over \(p_0\), whose
  normalization is \(dP_6\) with opposite boundary curves identified;
- a multiplicity-three bielliptic fibre over \(p_1\);
- a multiplicity-four bielliptic fibre over \(p_2\).

The manuscript computes

\[
\pi_1(X)=1,
\qquad
H_*(X;\mathbb Z)\cong H_*(S^6;\mathbb Z),
\]

and then recognizes \(X\) as diffeomorphic to \(S^6\).

These statements are **inputs to be checked**, not results of this Sonnet.
The first obligation is to reproduce the finite monodromy and topology
certificates from a frozen source version.

## 2. Why this is a strong Process Geometry calibration

The recognized output \(S^6\) has very little visible topological memory:
it is simply connected and has no middle homology.  Its proposed construction,
however, retains a rich history:

\[
\text{universal lift}
\longrightarrow
\text{period lattice transport}
\longrightarrow
\text{monodromy quotient}
\longrightarrow
\text{three singular completions}
\longrightarrow
\text{topological recognition}.
\]

This creates a sharp calibration question:

> When the final canonical object appears to have forgotten its construction,
> where is the process information stored, when may it be quotiented, and
> which part must be materialized at the boundary?

The manuscript is unusually useful because an imprecise process account can
fail in several distinguishable ways: it may forget integral lattice data,
identify histories with different holonomy, normalize away gluing data, merge
three inequivalent boundary mechanisms, or confuse final recognition with the
generating process.

## 3. Problem-native primitive audit

### 3.1 Primitive mathematical operations

Before importing Process Geometry vocabulary, the construction uses:

1. lifting the punctured base to a simply connected uniformizing space;
2. transporting a rank-four integral period lattice;
3. acting by the deck/orbifold group on base and fibre data;
4. quotienting by lattice translations and monodromy;
5. completing three boundary points by explicit local models;
6. choosing integral twists that control global topology;
7. computing fundamental group and homology;
8. recognizing the resulting smooth manifold.

Matrices, period coordinates, and named classical constructions are evidence
and verification devices.  They must not silently become the ontology of the
process account.

### 3.2 Observer and task

The terminal task is not merely to produce a complex manifold.  It is to
preserve enough information to verify all of:

\[
\text{complex compatibility},
\quad
\text{integral lattice compatibility},
\quad
\text{boundary compatibility},
\quad
\pi_1(X),
\quad
H_*(X;\mathbb Z),
\quad
X\cong_{\mathrm{diff}}S^6.
\]

Two histories may be identified only if every declared continuation relevant
to these tasks gives the same result.

### 3.3 Research-local process record

For auditing purposes only, use the provisional record

\[
\mathfrak P=
\left(
B^\circ,\widetilde B,\Gamma,\Lambda,\Pi,\rho,
\mathcal C,\ell,U
\right),
\]

where \(\widetilde B\) is the history lift, \(\Gamma\) is the deck/orbifold
action, \(\Lambda\cong\mathbb Z^4\) is the period lattice, \(\Pi\) is the period
map, \(\rho\) is monodromy, \(\mathcal C\) records the three completions,
\(\ell\) records twist data, and \(U(\mathfrak P)=X\) forgets construction
history after completion.

This is a notation local to the Sonnet.  It is not a proposed
ProcessFibration class and carries no API status.

## 4. Key question A — external calibration

Can Process Geometry encode the manuscript losslessly and produce a reusable
criterion or computation that classical terminology alone does not already
provide?

Three candidate pressure points are frozen.

### A1. Task-visible holonomy

For two lifted histories \(h_1,h_2\) with the same observed endpoint, a quotient
is unsafe if some allowed continuation \(\tau\) distinguishes their transported
fibre data:

\[
\operatorname{end}(h_1)=\operatorname{end}(h_2)
\quad\text{but}\quad
R_\tau\!\left(\operatorname{Hol}(h_1)\right)
\ne
R_\tau\!\left(\operatorname{Hol}(h_2)\right).
\]

The target is an auditable continuation-stability test, not the renaming of
monodromy as memory.

### A2. Canonicalization defect at the non-normal fibre

Let

\[
\nu:dP_6\longrightarrow W
\]

be the normalization.  A first concrete carrier of information lost by
normalization is the conductor quotient

\[
\mathcal Q_\nu=
\nu_*\mathcal O_{dP_6}/\mathcal O_W.
\]

The Sonnet should determine which gluing, cohomological, differential, and
future-transport data are visible in \(\mathcal Q_\nu\) or a more appropriate
exact replacement.  Calling the lost data a canonicalization defect is useful
only if it produces a computable invariant or an explicit failure witness.

### A3. Materialization as singular completion

The working hypothesis is that boundary completion converts non-flattenable
transport history into a persistent geometric object:

\[
\mathfrak P^\circ
\longrightarrow
\overline{\mathfrak P}^{\,\mathcal C}.
\]

This interpretation must account separately for finite-order fillings and the
unipotent cusp.  If it cannot distinguish their mechanisms, it is too weak.

### Calibration success criterion

Question A succeeds only if at least one of the following occurs:

1. a stricter safe-quotient criterion is obtained;
2. a canonicalization defect is calculated on \(dP_6\to W\);
3. local monodromy and completion data are compiled into a reusable global
   topology certificate;
4. the process audit exposes a necessary condition or failure surface that is
   difficult to see in the result object alone;
5. the language predicts a difference in a neighboring construction.

If the output only replaces monodromy by memory and degeneration by
materialization, record the result as re-expression and stop the strong
calibration claim.

## 5. Key question B — the complex arithmetic tower

On a chosen history lift carrying a branch of \(\Log z\), define three flows:

\[
\begin{aligned}
A_t(z)&=z+t,\\
M_s(z)&=e^s z,\\
P_r(z)&=\exp\!\left(e^r\Log z\right)=z^{e^r}.
\end{aligned}
\]

Their infinitesimal generators are

\[
A=\partial_z,
\qquad
M=z\partial_z,
\qquad
P=z\log z\,\partial_z.
\]

Adjacent ranks obey exact rescaling relations:

\[
M_sA_tM_s^{-1}=A_{e^s t},
\qquad
P_rM_sP_r^{-1}=M_{e^r s}.
\]

The non-adjacent conjugation does not remain in the three original families:

\[
P_rA_tP_r^{-1}(z)
=
\left(z^{e^{-r}}+t\right)^{e^r}.
\]

With the convention

\[
[f\partial_z,g\partial_z]
=(fg'-gf')\partial_z,
\]

the first brackets are

\[
[A,M]=A,
\qquad
[M,P]=M,
\qquad
[A,P]=(1+\log z)\partial_z.
\]

Further brackets generate \(z^{-1}\partial_z,z^{-2}\partial_z,\ldots\).
Thus the full \(A/M/P\) closure is generically infinite-dimensional.

The central arithmetic question is therefore not whether a three-dimensional
complex manifold has three named arithmetic directions.  It is:

> Does the infinite arithmetic process closure admit a task-sufficient finite
> integral shadow whose action is equivariantly comparable with the rank-four
> monodromy system of the torus fibration?

## 6. What would count as a strict interface

A dimension match is not evidence: every complex two-torus already has a
rank-four integral first-homology lattice.

A strict interface requires explicit objects \(Q_{AMP}\), \(\Gamma_{AMP}\) and
maps

\[
\phi:Q_{AMP}\longrightarrow\Lambda,
\qquad
\psi:\Gamma_{AMP}\longrightarrow\Delta(3,4,\infty)
\]

such that, on the declared domain,

\[
\phi(\gamma\cdot q)
=
\rho\!\left(\psi(\gamma)\right)\phi(q).
\]

The construction must also state:

- which arithmetic histories are identified and why the quotient is
  continuation-stable;
- why the resulting carrier is integral and rank four;
- how branch changes of \(\Log\) act;
- whether the period map has an arithmetic developing-map interpretation;
- whether finite orders \(3,4\) and the square-zero unipotent logarithm are
  predicted or inserted;
- whether the three boundary completions follow from the arithmetic data or
  remain independent geometric choices.

The manuscript's explicit matrices and twist values are hidden comparison
targets for the arithmetic discovery phase.  They may verify a frozen
candidate; they may not be supplied as the candidate grammar if the claim is
structural discovery.

## 7. Staged hypotheses

The hypotheses are ordered by strength:

- **H1 — lossless calibration:** the construction admits an auditable
  lift–transport–quotient–completion–recognition account.
- **H2 — memory growth:** finite-order and unipotent monodromy give bounded
  and polynomial-growth normal forms for task-visible history.
- **H3 — finite shadow:** the infinite \(A/M/P\) closure has a
  continuation-stable finite-rank quotient for a frozen task.
- **H4 — integral equivariance:** that quotient is rank four over
  \(\mathbb Z\) and satisfies the equivariance condition above.
- **H5 — boundary prediction:** the arithmetic shadow selects the two finite
  fillings and the cusp completion rather than merely accommodating them.
- **H6 — global prediction:** arithmetic data predict the twist closure or
  the final \(S^6\) recognition certificate.

H1 and H2 would show organizational and calibration value.  H4 is the first
strict bridge between the two key questions.  H5 and H6 are intentionally
high-risk.

## 8. Kill conditions and negative results

Stop or weaken the relevant claim if:

1. the source's finite matrix or topology certificate cannot be reproduced;
2. the Process Geometry account loses classical data or adds no criterion,
   compression, computation, or failure localization;
3. the proposed arithmetic quotient is not stable under declared
   continuations;
4. rank four appears only because the target torus lattice was supplied in
   advance;
5. the orders \(3,4\) or the unipotent filtration are inserted rather than
   predicted;
6. branch dependence prevents a well-defined global arithmetic action;
7. the singular completions remain arbitrary choices after the proposed
   arithmetic reduction;
8. a neighboring \((m,n,\infty)\) case falsifies a claimed universal
   mechanism.

A complete negative certificate for a frozen arithmetic grammar is a valid
Sonnet result.

## 9. Theory Map and governance

At initialization:

- H0 is tested by the distinction between literal lifted histories and the
  recognized output;
- H1 is tested by task-visible holonomy and continuation-stable quotients;
- H2 is pressured by covering, boundary, and singular completion;
- V1/V2 are tested by the possibility of compressing an infinite arithmetic
  closure into a reusable finite integral primitive.

No arrow is yet supported strongly enough to change the Theory Map.  All
notations and future code remain research-local.  There is no direct path from
this Sonnet to Public API.

## 10. Source boundary

Primary source:

- Levent Alpöge, *A compact complex threefold fibred by tori over the
  projective line, and the six-sphere*,
  <https://alpo.ge/s6.pdf>, accessed 2026-08-25.

The manuscript is treated as a candidate construction pending independent
checking.  Phase 0 must distinguish verbatim source claims, reproduced
certificates, Process Geometry interpretations, and new deductions.

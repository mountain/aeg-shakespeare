# Phase 1I contract — charted finite differences and fibre response

**Status:** frozen research-local contract.  This phase revises the former
Phase 1H next gate before attempting collision-covector selection.

**Executable owner:**
[`test_charted_fibre_lyapunov_calculus.py`](../../tests/research/test_charted_fibre_lyapunov_calculus.py).

**Result owner:**
[`18-phase1i-charted-fibre-calculus-results.md`](./18-phase1i-charted-fibre-calculus-results.md).

## 0. Dependency and cross-reference ledger

Phase 1I has four internal dependencies.

1. [Phase 1D](./08-phase1d-measured-fibration-objectification-synthesis.md)
   separates source fibres, conditional fibre laws, ensembles, closure, and
   objectification.
2. [Phase 1G](./14-phase1g-selective-continuation-time-reversal-results.md)
   proves the exact stopped/continued identity and locates time orientation in
   repeated use of a factorized section.
3. [Phase 1H](./16-phase1h-hidden-lyapunov-mode-results.md) discovers the
   target Lyapunov cone, rejects uniqueness and microscopic lifting, and
   exposes the first/second-jet finite-step ledger.
4. [Phase 12A's fibred finite-part result](../local-field-projective-process-geometry/20-phase12-locale-observer-history-behavior-results.md)
   proves independently that chart forgetting can obstruct descent and that
   differentiation and multiplication need not commute with a task output.

Two adjacent research lines are comparison controls, not dependencies.

- [The A/M function-theory note](../../docs/06-addition-multiplication-function-theory.md)
  retains finite process order, the relation
  \(S_sT_t=T_{e^{st}}S_s\), its infinitesimal shadow \([A,M]=A\), and ordered
  path history.  The
  [A/M first-order task-germ calibration](../../tests/research/test_am_checkpoint_differential_quotient.py)
  separately warns that a local jet is not a continuation-stable global
  quotient.
- The open [AM conformal chart normal-form study](https://github.com/mountain/process-geometry/pull/119)
  supplies a T0 joint-chart/Pareto contract.  It has not yet produced a chart
  theorem.  The open
  [partition-fibre Phase 12B calibration](https://github.com/mountain/process-geometry/pull/122)
  supplies a positive local model of fibred task-exact objectification.  Its
  result is used only as an external red-team pattern until it enters the
  common base.

These references are typed deliberately.  A result in one line may alter the
question asked here without becoming evidence for a Boltzmann theorem.

## 1. Revised question

The previous next gate proposed the direct intersection

\[
\text{target Lyapunov cone}
\cap
\text{collision-product covector law}
\cap
\text{composition/chain rule}.
\]

Phase 12A shows that this order is unsafe: a scalar extraction or derivative
may fail to descend after chart or fibre data are forgotten.  Phase 12B shows
the complementary possibility: a forgetful fibre can become a new object only
after it gains a native composition and exact all-composite lowering.

Phase 1I therefore asks a prior question:

> Can the finite renewed target and its continued correlation fibre support
> an exact process-level finite-difference calculus, and which parts of the
> Phase 1H selector survive a change from the dynamical contrast chart to the
> collision-compositional odds chart?

No continuum transfer or entropy uniqueness is part of this phase.

## 2. Primitive finite carrier

Retain the Phase 1G data:

\[
\Gamma=\{0,1\}_x\times\{0,1\}_h,
\qquad
U(x,h)=(x\mathbin{\mathtt{xor}}h,h),
\]

the one-body observation \(\pi\), and the factorized section

\[
\sigma_\delta(p)=p\otimes(1-\delta,\delta),
\qquad 0<\delta<1/2.
\]

For any microscopic law \(F\), define

\[
p=\pi F,
\qquad
E_\sigma(F)=F-\sigma_\delta(p),
\]

\[
B_\delta=\pi U\sigma_\delta,
\qquad
R_\sigma(F)=\pi U E_\sigma(F).
\]

Then

\[
\pi UF=B_\delta p+R_\sigma(F).
\]

The section, residual, target channel, and fibre response remain distinct
objects.  The response is not a decoder for \(F\).

## 3. Native finite-difference contract

For any declared target observable \(\Phi\), define

\[
\Delta_\Phi^\parallel(p)
=\Phi(B_\delta p)-\Phi(p)
\]

and

\[
\Delta_\Phi^\perp(F)
=\Phi(B_\delta p+R_\sigma(F))-\Phi(B_\delta p).
\]

The phase must certify the exact identity

\[
\boxed{
\Phi(\pi UF)-\Phi(\pi F)
=
\Delta_\Phi^\parallel(p)
+
\Delta_\Phi^\perp(F)
}
\]

before taking a derivative or Taylor expansion.  This is a finite observable
identity on the declared adapter, not a generic differential bundle.

For a target Lyapunov function write

\[
\mathcal D_\Phi(p)
=\Phi(p)-\Phi(B_\delta p)
=-\Delta_\Phi^\parallel(p)\ge0.
\]

The exact microscopic observation is nonincreasing only when

\[
\Delta_\Phi^\perp(F)\le\mathcal D_\Phi(p).
\]

This inequality, rather than global decoding, is the first finite prototype
of a cross-layer H-adequacy budget.

## 4. Taylor and A/M shadow boundary

For a quadratic contrast observable, the vertical finite difference may be
expanded exactly as

\[
\Delta_{K_2}^\perp
=2z(Bp)z(R)+z(R)^2.
\]

The two terms are the first-pairing and curvature shadows in the contrast
chart.  The boxed finite difference remains the native exact object.  Higher
jet depth is required only when a task asks for a local differential
presentation of that finite process.

The executable also includes the independent A/M order control

\[
S_kT_t=T_{kt}S_k,
\qquad
S_kT_t\ne T_tS_k
\]

for \(k\ne1\) and \(t\ne0\).  This does not identify the binary target channel
with a full A/M flow.  It prevents the Phase 1G componentwise split

\[
\Delta p=A+p\odot M
\]

from being promoted to an order-free process calculus.

## 5. Two-chart audit

Use the normalized binary law

\[
p=\left(\frac{1+z}{2},\frac{1-z}{2}\right)
\]

and its odds chart

\[
r=\frac{p_0}{p_1}=\frac{1+z}{1-z}.
\]

The target channel is linear in contrast:

\[
z\longmapsto\lambda z,
\qquad \lambda=1-2\delta.
\]

In odds it is the Möbius map

\[
r\longmapsto
\frac{(1+\lambda)r+(1-\lambda)}
     {(1-\lambda)r+(1+\lambda)}.
\]

Conversely, the distinguished corner odds of an independent tensor product
compose multiplicatively:

\[
r(p\otimes q)=r(p)r(q).
\]

Thus contrast is a dynamical normal form while odds is a composition normal
form for this declared covector.  Phase 1I does not claim that these are the
only charts or that no third chart can improve both tasks.  It certifies that
the Phase 1H minimum polynomial degree is relative to the contrast grammar:

\[
K_2=z^2=\left(\frac{r-1}{r+1}\right)^2
\]

is polynomial in \(z\) and rational, not polynomial, in \(r\).

## 6. Held-out potential control

Only after the two-chart audit is frozen may the classical coefficients be
used.  The formal series

\[
H_u(z)=\sum_{m\ge1}\frac{z^{2m}}{(2m)(2m-1)}
\]

satisfies

\[
H_u'(z)
=\sum_{m\ge1}\frac{z^{2m-1}}{2m-1}
=\frac12\log\frac{1+z}{1-z}.
\]

The executable checks the coefficient identity through frozen depth eight.
The responsible interpretation is:

```text
contrast chart          diagonal target dynamics and modal Lyapunov cone
odds/log-odds chart     multiplicative composition and additive covector
H potential             post-selection integral joining the two charts
```

This is a formal held-out control.  Target contraction alone has not selected
the log-odds covector.

## 7. Fibre-objectification red team

The residuals \(E_\sigma(F)\) form a signed linear space before positivity is
restored.  It is tempting to objectify them under vector addition.  The phase
must reject that move on the probability carrier: two individually admissible
residual perturbations over one base can sum to a signed law with a negative
entry.

This is only a no-go for naive addition.  It does not rule out a different
partial, graph, operadic, measured, or history-indexed composition.  Following
the Phase 12B comparison, a Deng molecule/cumulant object would still need:

1. a stable interaction/response interface;
2. a native composition closed on every legal composite;
3. exact or budgeted lowering of those composites;
4. recollision, exclusion, reference-measure, and cutting residuals;
5. a demonstrated calculation benefit.

Without those obligations, the correlation fibre remains horizontal adapter
data, not a higher arithmetic rank.

## 8. Continuum transfer obligation

For a continuous target equation with generator \(Q(f)\) and correlation
response \(\mathcal R(g)\), the formal infinitesimal shadow would be

\[
\frac{d}{dt}\Phi(f)
=\langle D\Phi(f),Q(f)\rangle
+\langle D\Phi(f),\mathcal R(g)\rangle.
\]

This formula is not asserted until the trace, differentiability, integrability,
and topology are declared.  For \(\Phi=H\), the covector contains \(\log f\),
which is unbounded near \(f=0\).  Bulk \(L^1\) control of a cumulant therefore
does not automatically control the fibre response.  A future Deng-calibrated
phase must provide positivity or weighted-integrability hypotheses, a weak
collision-flux pairing, a truncated/renormalized covector, or another exact
response budget.

## 9. Frozen executable certificates

With \(\delta=1/16\), the executable must certify:

1. the finite fibre-difference identity for every strictly positive
   denominator-eight microscopic law and for \(K_2,K_4\);
2. an exact witness where target dissipation is outweighed by fibre response;
3. the exact vertical first-pairing plus curvature shadow for \(K_2\);
4. contrast/odds round trips and their linear/Möbius target laws;
5. multiplicative corner-odds composition;
6. the held-out formal H/log-odds potential identity through depth eight;
7. noncommutativity and corrected transport in the finite A/M control;
8. failure of naive additive probability-fibre objectification;
9. separate grading of finite, formal, adjacent, continuum, and rank claims.

The test remains standard-library-only and sub-second.

## 10. Kill conditions

Phase 1I must be narrowed or rejected if:

- the stopped-plus-response law fails to reconstruct \(\pi UF\);
- the observable increments fail to add exactly;
- a chart-relative polynomial cost is reported as chart invariant;
- odds multiplication is silently identified with a full tensor-product
  entropy chain rule;
- the held-out log series leaks into target-mode discovery;
- a Taylor jet is called the complete finite process;
- the adjacent A/M order control is called a collision derivation;
- signed residual addition is called probability-fibre composition;
- an \(L^1\) cumulant estimate is paired with \(\log f\) without the missing
  positivity/integrability contract;
- observer order \(s\), continuation depth \(k\), chart policy \(\chi\), and
  arithmetic rank \(r\) are collapsed.

## 11. Repository boundary

### Mathematical Core

Unchanged.  This phase supplies a problem-local exact response identity and
chart-relative red team.  It does not yet justify a generic adapted calculus
or a new Core law.

### Engineering Architecture

Research-local refinement.  The solver order becomes finite process
evaluation, horizontal/vertical response ledger, chart audit, local jet
shadow, objectification red team, then held-out potential comparison.

### Theory Map

Unchanged.  The work refines T0/T1 pressure on H4 and the task-covariant
history-evaluation transversal without promoting a node or edge.

### API

No pressure.  The dataclasses and helpers remain inside one executable essay.

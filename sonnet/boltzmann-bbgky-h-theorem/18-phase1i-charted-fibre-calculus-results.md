# Phase 1I results — charted finite differences and fibre response

**Status:** nine exact research-local certificates passed.  The phase replaces
the direct entropy-selector gate by a prior charted fibre-response calculus.

**Contract:**
[`17-phase1i-charted-fibre-calculus-contract.md`](./17-phase1i-charted-fibre-calculus-contract.md).

**Executable:**
[`test_charted_fibre_lyapunov_calculus.py`](../../tests/research/test_charted_fibre_lyapunov_calculus.py).

## 1. Main result

For the Phase 1G reversible XOR carrier, target projection \(\pi\), factorized
section \(\sigma_\delta\), and renewed target channel

\[
B_\delta=\pi U\sigma_\delta,
\]

write

\[
p=\pi F,
\qquad
E_\sigma(F)=F-\sigma_\delta(p),
\qquad
R_\sigma(F)=\pi U E_\sigma(F).
\]

Then every declared target observable \(\Phi\) satisfies

\[
\boxed{
\Phi(\pi UF)-\Phi(p)
=
\bigl[\Phi(B_\delta p)-\Phi(p)\bigr]
+
\bigl[\Phi(B_\delta p+R_\sigma(F))-\Phi(B_\delta p)\bigr].
}
\]

The first bracket is the target or horizontal finite difference.  The second
is the vertical fibre response.  This identity is exact before any derivative,
Taylor expansion, global decoder, or semantic-equivalence claim.

The executable enumerates all 35 strictly positive microscopic laws with
denominator eight and verifies this identity for both \(K_2\) and \(K_4\).
It therefore checks 70 nontrivial observable ledgers in exact rational
arithmetic, in addition to the named red-team fixtures below.

## 2. Fibre response can reverse target monotonicity

Use the Phase 1G middle state generated from

\[
p_0=(3/4,1/4),
\qquad
\delta=1/16.
\]

Its observed base, stopped target, and continued response are

\[
p=(23/32,9/32),
\]

\[
B_\delta p=(177/256,79/256),
\]

\[
R_\sigma(F)=(15/256,-15/256).
\]

For \(K_2(p)=(p_0-p_1)^2\), the exact ledger is

| contribution | value |
| --- | ---: |
| horizontal target increment | \(-735/16384\) |
| vertical fibre response | \(1695/16384\) |
| exact microscopic observed increment | \(15/256\) |

Thus

\[
-\frac{735}{16384}
+\frac{1695}{16384}
=\frac{15}{256}>0.
\]

The target branch dissipates \(K_2\), but the fibre response is larger and
positive.  This is the exact finite mechanism behind Phase 1H's microscopic
lifting failure.  No contradiction with the target Lyapunov theorem occurs:
the two statements are attached to different process continuations.

If

\[
\mathcal D_\Phi(p)=\Phi(p)-\Phi(B_\delta p),
\]

then target monotonicity transfers to the microscopic observation only under
the additional adapter condition

\[
\Delta_\Phi^\perp(F)\le\mathcal D_\Phi(p).
\]

This inequality is now the finite prototype of an H-response budget.

## 3. The jet ledger is a chart shadow of the finite response

For the same witness,

\[
z(Bp)=49/128,
\qquad
z(R)=15/128.
\]

The vertical response decomposes as

\[
\Delta_{K_2}^\perp
=2z(Bp)z(R)+z(R)^2
\]

with

\[
2z(Bp)z(R)=\frac{735}{8192},
\qquad
z(R)^2=\frac{225}{16384}.
\]

Their sum is \(1695/16384\).  The first term is the local first-pairing
shadow and the second is curvature.  Both are useful, but neither replaces
the exact finite response unless the task explicitly asks for a jet
approximation.

This refines, rather than contradicts, the
[Phase 1H first/second-jet result](./16-phase1h-hidden-lyapunov-mode-results.md):
that calculation was exact in the contrast chart, while Phase 1I identifies
the preceding finite process object whose chart expansion it computes.

## 4. Minimum polynomial complexity is chart-relative

Let

\[
z=p_0-p_1,
\qquad
r=\frac{p_0}{p_1}=\frac{1+z}{1-z},
\qquad
\lambda=1-2\delta.
\]

The exact target laws are

\[
z(B_\delta p)=\lambda z(p)
\]

and

\[
r(B_\delta p)
=
\frac{(1+\lambda)r(p)+(1-\lambda)}
     {(1-\lambda)r(p)+(1+\lambda)}.
\]

The executable checks both expressions and their chart round trips on three
positive laws.  The target dynamics is linear in \(z\) but Möbius in \(r\).

For the distinguished product-corner covector,

\[
r(p\otimes q)=r(p)r(q).
\]

At

\[
p=(3/4,1/4),
\qquad
q=(2/3,1/3),
\]

the corner odds are exactly (3), (2), and (6).  Thus odds simplify the
declared composition task while contrast simplifies the target dynamics.

The Phase 1H winner transforms as

\[
K_2=z^2
=\left(\frac{r-1}{r+1}\right)^2.
\]

It is polynomial of degree two in contrast and a reduced rational expression
in odds.  Hence the phrase *minimum polynomial candidate* must always retain
its chart and grammar qualifier.  Phase 1I does not prove a globally optimal
atlas or exclude another joint normal form; the open
[AM chart-normal-form Sonnet](https://github.com/mountain/process-geometry/pull/119)
owns that broader search question.

## 5. H becomes a potential between two task-adapted charts

After the chart audit was frozen, the classical coefficients were reopened.
Through formal depth eight, exact differentiation gives

\[
\frac{d}{dz}
\sum_{m=1}^{8}
\frac{z^{2m}}{(2m)(2m-1)}
=
\sum_{m=1}^{8}
\frac{z^{2m-1}}{2m-1}.
\]

The right side is the corresponding truncation of

\[
\operatorname{artanh}z
=\frac12\log\frac{1+z}{1-z}.
\]

This supports the following qualified interpretation:

\[
\boxed{
\text{contrast: dynamical chart}
\quad\xrightarrow{\ dH\ }\quad
\text{log odds: compositional covector chart}.
}
\]

Classical binary relative H is therefore not only a positive resummation of
target modes.  It is also a potential whose differential connects the simple
target chart to the simple collision-composition covector.

This remains post-selection.  The target semigroup selects a Lyapunov cone;
it does not by itself select the log-odds covector or prove its integrability
in the full Boltzmann state space.  The logarithmic resonance mechanism in the
[A/M function-theory note](../../docs/06-addition-multiplication-function-theory.md)
is an adjacent structural explanation, not yet a kinetic derivation.

## 6. Ordered A/M is prior to a commuting jet notation

The exact finite control uses a value \(a\), translation \(T_t\), and scaling
\(S_k\).  It verifies

\[
S_kT_t(a)-T_tS_k(a)=(k-1)t
\]

and the corrected law

\[
S_kT_t=T_{kt}S_k.
\]

For \(a=1/2\), \(t=1/3\), and \(k=2\), the two uncorrected orders differ by
\(1/3\).  This is the finite process relation underlying the infinitesimal
shadow \([A,M]=A\).

The control prevents an overstatement: the Phase 1G pair \((A,M)\) records a
componentwise target increment, but does not alone specify an ordered A/M
history or an all-horizon calculus.  A later collision fixture must make
process order physically active rather than importing this adjacent affine
identity as if it were already a collision theorem.

## 7. Correlation residuals have not objectified

At base

\[
p=(1/2,1/2),
\qquad
\delta=1/16,
\]

the signed zero-marginal residual

\[
E=
\begin{pmatrix}
1/32&-1/32\\
-1/32&1/32
\end{pmatrix}
\]

produces an admissible probability law when added once to the factorized
section.  Adding the same residual twice makes an entry (-1/32).  Therefore
ordinary vector addition is not a closed composition on the probability fibre.

This is the statistical-mechanics counterpart of the structural caution in
[Phase 12A](../local-field-projective-process-geometry/20-phase12-locale-observer-history-behavior-results.md):
a linear operation in one ambient presentation need not descend to the desired
task object.  It is also a negative counterpart to the open
[partition-fibre Phase 12B result](https://github.com/mountain/process-geometry/pull/122),
where multiset union is closed and weight lowers exactly for every composite.

The result rejects only naive additive objectification.  Collision molecules
may still support a partial, graph, operadic, measured, or history-indexed
composition.  That question remains open and requires a recollision/exclusion
red team.

## 8. Consequence for Deng--Hani--Ma calibration

The finite result sharpens the continuum target.  It is not enough to prove a
small cumulant in a bulk norm.  A continuum transfer needs a bound on its
observable response after collision-history continuation:

\[
\text{fibre H response}
\le
\text{target H dissipation}
+\text{declared error budget}.
\]

For the H covector, \(\log f\) is unbounded at zero.  The
[Phase 1E bulk/trace obstruction](./10-phase1e-continuum-collision-adapter-seam-results.md)
and [Phase 1F weak collision-flux result](./12-phase1f-weak-mild-continuation-cell-results.md)
therefore remain active dependencies.  Bulk \(L^1\) smallness alone does not
supply either a collision trace or an H-response bound.  Positivity, weighted
integrability, a truncated/renormalized covector, or another weak pairing must
be declared before the finite identity acquires a continuum meaning.

## 9. Executed certificates

Nine exact tests pass:

1. 70 \(K_2/K_4\) fibre-difference ledgers pass on all positive
   denominator-eight microscopic laws;
2. target dissipation and fibre response are shown to have independent signs;
3. the vertical \(K_2\) response equals first pairing plus curvature exactly;
4. contrast and odds charts round-trip and carry linear/Möbius target laws;
5. independent corner odds compose multiplicatively;
6. formal H coefficients integrate the log-odds covector through depth eight;
7. finite A/M words remain ordered and satisfy the transported relation;
8. naive residual addition fails probability-fibre closure;
9. finite, formal, adjacent, continuum, objectification, and rank claims remain
   separately graded.

Together with Phases 1C and 1E--1H, the focused dependency-free suite now has
47 exact certificates.

## 10. What has and has not been earned

Phase 1I has earned:

- a finite exact horizontal/vertical observable-difference identity;
- an explicit fibre-response sign reversal of target \(K_2\) dissipation;
- a precise relation between the finite response and its local jet shadow;
- an exact contrast/odds chart tradeoff;
- a post-selection potential reading of classical binary relative H;
- ordered-A/M and naive-fibre-composition red teams;
- a sharper continuum H-response obligation.

It has not earned:

- a generic semantic-fibre calculus;
- a chart-independent minimum Lyapunov candidate;
- selection of log odds from target dynamics alone;
- a collision-derived noncommutative A/M process;
- objectification of cumulants or Deng molecules;
- a continuum H-response estimate, Boltzmann--Grad transfer, or hard-sphere H
  theorem;
- a new arithmetic rank or API.

## 11. Revised next gate

The direct Phase 1H intersection gate is replaced by two ordered subgates.

### 1J-A — noncommutative finite collision-covector gate

Construct a state-dependent or sequential finite collision fixture in which
the order of Addition- and Multiplication-type target processes is observable.
Freeze a small chart atlas, compare joint costs for dynamics, covector,
composition, decoder, and residual, and ask whether the collision-product
character selects a closed one-form.  Only then integrate it to a candidate
potential.

### 1J-B — continuum fibre-response gate

Locate a Deng molecule/cumulant composition and cutting map, test closure and
all-composite lowering, and formulate an H-response estimate in the exact weak
collision-flux topology already frozen by Phases 1E/1F.  A bulk estimate that
does not control the logarithmic covector fails this gate.

The subgates are related but neither may borrow the other's conclusion.

## 12. Repository effect

### Mathematical Core

Unchanged.  The result is a local exact law and a candidate pattern, not a
generic adapted-calculus theorem.

### Engineering Architecture

Refined research-locally.  Finite process evaluation and fibre response now
precede jet expansion and functional selection.  The evaluator uses only
standard-library `Fraction`; failure claims are exact counterexamples.

### Theory Map

Unchanged.  The result refines T0/T1 H4 and transversal pressure, while the
general effective calculus, V2 objectification, and V5 closure remain open.

### API

No pressure.  No package or Experimental symbol is added.

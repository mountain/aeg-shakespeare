# Phase 12A result — chart forgetting and fibred finite parts


**Status:** first finite Phase 12 execution slice, completed on 2026-08-27.
Only the strict-descent, filtered-fibre, finite-jet, and composition controls
declared below have been executed.  The locale, sobriety, basis, full
coalgebra, and place-indexed workloads in the frozen Phase 12 contract remain
open.

**Contract:**
`19-phase12-locale-observer-history-behavior-task-contract.md`.

**Executable certificate:**
`tests/research/test_locale_observer_history_behavior_duality.py`.

This compact slice does not open a separate Sonnet.  It tests one question
already central to Phase 12:

> Can a task output descend after a frame or chart is forgotten, and if not,
> what finite fibre and residual data make its transport exact?

The answer is mixed and exact.  Strict descent fails in two minimal examples.
Frame-indexed addition and chart-indexed finite parts remain well typed.  For a
meromorphic germ of bounded pole order, a finite principal jet suffices for
chart transport.  The resulting finite-part adapter is linear in one fixed
contract but is not a global arithmetic homomorphism.

---


## 1. Verdict against the four Phase 12A questions

| Question | Exact disposition |
| --- | --- |
| strict descent no-go | passed negatively: the same unmarked projective input has two incompatible frame lifts, and the same unparameterized singular germ has finite parts (0) and (-1/12) in two charts |
| correct fibred object | bounded positive result: the charted germ transports exactly; for pole order (r), the principal part and the ((r+1))-jet of the chart transition suffice to transport the finite part |
| Bernoulli family | exact for the exponential chart family: the constant coefficient of (sum_{n\geq1}n^m e^{-nt}) is ((-1)^mB_{m+1}/(m+1)); this is not yet a generic regularization theorem |
| composition red team | mixed: fixed-contract linearity and log-free linear-scale invariance pass; nonlinear chart forgetting, multiplication, differentiation, and filter/grouping interchange fail |

The phrase *Phase 12A* names this first execution slice.  It does not rename
Gate 12A of the frozen contract.  The slice supplies bounded evidence toward
Gates 12A, 12F, 12G, and 12I but does not pass any full Phase 12 gate.

---


## 2. Prototype no-go — projective frame forgetting

Let (K) be a field of characteristic zero and

\[
\mathbb P^1(K)=K\cup\{\infty\}.
\]

### Theorem 2.1 — addition does not strictly descend

There is no total binary operation

\[
\boxplus:\mathbb P^1(K)^2\longrightarrow\mathbb P^1(K)
\]

which both restricts to ordinary addition on (K) and is strictly equivariant
under every (g\in PGL_2(K)):

\[
g(x\boxplus y)=g(x)\boxplus g(y).
\]

### Exact proof

Apply (g_0(z)=1/z) to (0+1=1).  Strict equivariance would give

\[
\infty\boxplus1=1.
\]

Apply (g_1(z)=1/(z-1)) to (1+2=3).  It would instead give

\[
\infty\boxplus1=\frac12.
\]

This is a contradiction.  It is algebraic, not p-adic-topological, and
therefore applies over (mathbb Q), (mathbb R), and every
(mathbb Q_p).

The executable reproduces both lifts with exact `Fraction` arithmetic.  It
then exhausts 496 small nonsingular rational Möbius matrices and 25 input pairs
to verify the correctly typed law

\[
g(x\boxplus_Fy)=gx\boxplus_{gF}gy.
\]

Here (F=(0,1,\infty)) is an ordered frame and the operation is partial on the
affine chart (A_F=\mathbb P^1(K)\setminus\{\infty_F\}).  The full frame is a
sufficient carrier.  Addition alone needs only the ordered zero/infinity
marks: changing the unit mark by a dilation preserves addition.  Joint
addition and multiplication require the third unit mark.

This sharpens the Phase 10 stabilizer result.  A bare projective point not only
fails to decode its projective process; an ordinary arithmetic operation also
fails to factor through frame forgetting.

---


## 3. Finite-part no-go in two charts

Freeze the rational function

\[
G(q)=\sum_{n\geq1}nq^n=\frac{q}{(1-q)^2},
\qquad |q|<1,
\]

and consider its singular germ at (q=1).

In the affine parameter (u=1-q),

\[
G=u^{-2}-u^{-1},
\qquad \operatorname{FP}_u(G)=0.
\]

In the logarithmic parameter (q=e^{-t}),

\[
G=\frac{e^{-t}}{(1-e^{-t})^2}
=\frac{1}{4\sinh^2(t/2)}
=t^{-2}-\frac1{12}+\frac{t^2}{240}+O(t^4),
\]

so

\[
\operatorname{FP}_t(G)=-\frac1{12}.
\]

Thus the scalar finite part is not constant on the fibre of charted
presentations over the same unparameterized singular germ.  No map

\[
\operatorname{FP}:\{\text{uncharted singular germs}\}\longrightarrow K
\]

can reproduce both extractions.  What transports under a local change of
parameter is the full charted Laurent/asymptotic germ, not its constant term by
itself.

This does not alter ordinary summation:

\[
1+2+3+\cdots=+\infty
\]

in the partial-sum semantics.  The exact typed statement is that zeta analytic
continuation or the declared exponential finite-part contract returns
(-1/12).

---


## 4. The finite-jet transport theorem

The no-go does not force retention of an infinite expansion for every bounded
task.

### Lemma 4.1 — second-order finite-part transport

Let

\[
f(u)=a_{-2}u^{-2}+a_{-1}u^{-1}+a_0+O(u)
\]

and let

\[
u=\alpha t+\beta t^2+\gamma t^3+O(t^4),
\qquad \alpha\ne0.
\]

Then

\[
\operatorname{FP}_t f(u(t))
=a_0-a_{-1}\frac{\beta}{\alpha^2}
+a_{-2}\left(
  \frac{3\beta^2}{\alpha^4}-\frac{2\gamma}{\alpha^3}
\right).
\]

For (G=u^{-2}-u^{-1}) and

\[
u=1-e^{-t}=t-\frac{t^2}{2}+\frac{t^3}{6}+O(t^4),
\]

the two principal coefficients and this three-jet give exactly

\[
\frac5{12}-\frac12=-\frac1{12}.
\]

### Proposition 4.2 — bounded pole order needs bounded transport data

For

\[
f(u)=\sum_{k=-r}^{\infty}a_ku^k
\]

and an invertible formal change of parameter (u(t)=\alpha t+O(t^2)), the
constant coefficient of (f(u(t))) depends only on

\[
(a_{-r},\ldots,a_{-1},a_0)
\]

and the coefficients of (u(t)) through (t^{r+1}).  Indeed, the constant
term of (u^{-k}) uses only the coefficient through order (t^k) after
factoring out (alpha t), while positive powers of (u) cannot contribute a
constant.

Therefore the exact carrier for the bounded finite-part task can be a finite
jet.  The singular principal part is nevertheless a required residual: if it
is discarded before chart transport, nonlinear coordinate terms can no longer
be corrected.

---


## 5. Fibre ledger

Two complementary projections prevent the words *base* and *fibre* from being
used ambiguously.

### 5.1 Descent audit

Let

\[
\pi:\{(g,c):g\text{ is a singular germ in chart }c\}
\longrightarrow
\{\text{uncharted singular germs}\}
\]

forget the chart.  Here the uncharted germ is the base point; chart,
regularizing filter, and subtraction scheme are fibre data.  Finite-part
extraction does not factor through (pi).

### 5.2 Operational bundle

For computation, use a contract base

\[
C=\{c=(\text{filter},\text{singular point},\text{chart class},
       \text{subtraction rule})\}.
\]

The fibre (E_c) contains the charted germs or their task-sufficient jets.
Chart changes are morphisms between fibres.  The task output is a sectionwise
map

\[
\operatorname{FP}_c:E_c\longrightarrow K,
\]

not one untyped scalar map on chart-forgotten objects.

| Datum | Phase 12A role |
| --- | --- |
| unparameterized singular germ | base of the descent no-go |
| filter, chart, subtraction rule | forgotten fibre data in the descent audit; contract index operationally |
| charted Laurent germ | exact covariant total object |
| principal part | residual required for nonlinear chart transport |
| chart transition through order (r+1) | finite transport datum for a pole of order (r) |
| finite part | task-relative output, not an invariant of the uncharted germ |

This is a semantic fibration in the provisional Phase 12 sense only.  It does
not assert a Serre or Hurewicz fibration.

---


## 6. Bernoulli transport family

For (m\geq1), set

\[
R_m(q)=\sum_{n\geq1}n^mq^n
=\left(q\frac{d}{dq}\right)^m\frac{q}{1-q}.
\]

Under the additive--multiplicative chart (q=e^{-t}),

\[
q\frac{d}{dq}=-\frac{d}{dt},
\qquad
R_m(e^{-t})
=\left(-\frac{d}{dt}\right)^m\frac1{e^t-1}.
\]

With the Bernoulli convention (B_1=-1/2), formal inversion of (e^t-1)
gives

\[
\frac1{e^t-1}
=t^{-1}+\sum_{k\geq0}\frac{B_{k+1}}{(k+1)!}t^k.
\]

Consequently,

\[
\operatorname{FP}_t R_m(e^{-t})
=(-1)^m\frac{B_{m+1}}{m+1}.
\]

The executable constructs the exponential series and its Laurent inverse over
`Fraction`, rather than inserting the answer, and checks (m=1,\ldots,8).
It obtains (-1/12,0,1/120,\ldots) exactly.

The equality of this coefficient with (zeta(-m)) is the classical analytic
continuation identity.  Phase 12A does not re-prove the zeta continuation
theorem.  What it proves locally is narrower: Bernoulli values are systematic
constant coefficients generated by this rational (q)-germ family under the
exponential chart transition.  Because the composition audit below is
negative, this family result is not yet a generic composable “AM
regularization” theorem and does not justify a separate Sonnet.

---


## 7. Composition audit

| Operation | Verdict | Exact witness or scope |
| --- | --- | --- |
| addition | preserved inside one fixed chart/filter/subtraction contract | constant-coefficient extraction is linear |
| linear scale (t\mapsto\lambda t) | preserved for log-free Laurent germs | nonzero Laurent degrees remain nonzero |
| nonlinear chart change | not strictly preserved | (u=1-e^{-t}) changes (0) to (-1/12); the jet correction repairs transport |
| differentiation | not a scalar homomorphism | (operatorname{FP}(d t/dt)=1), while differentiating (operatorname{FP}(t)=0) gives (0) |
| multiplication | not preserved | (operatorname{FP}(t^{-1})\operatorname{FP}(t)=0), but (operatorname{FP}(1)=1) |
| index translation | requires a boundary term | (sum(n+1)e^{-nt}=e^t(\sum m e^{-mt}-e^{-t})); both sides have finite part (-7/12) only with the omitted first term retained |
| grouping/filter interchange | not preserved | termwise Abel filtering of Grandi's history gives (1/2); pairing first and filtering zero blocks gives (0) |
| positivity and ordinary limit | not preserved | every filtered summand (ne^{-nt}) is positive for (t>0), while the extracted finite part is negative; ordinary partial sums diverge |

The reindexing row also records why chronology and boundary provenance cannot
be thrown away.  The grouping row is a scheme-dependence witness, not a claim
that an admissible fixed Abel regulator is internally inconsistent.

---


## 8. Objectification and inevitability boundary

The two no-go results rule out **strict conservative objectification** when the
declared task simultaneously requires:

1. ordinary affine arithmetic or finite-part extraction;
2. forgetting the relevant frame or chart contract; and
3. covariance under the full declared transformation family.

Relative to those requirements, retaining a semantic fibre is forced.  There
remain three logically distinct exits:

1. retain the frame/chart and transport between fibres;
2. restrict the symmetry or admissible chart changes;
3. weaken or replace the task so that the forgotten distinctions are
   irrelevant.

Phase 12A supports a **filtered semantic fibration as an exact finite model**:
the filtered germ, principal residual, and bounded transition jet have typed
transport and exact rational certificates.  It does not establish vertical
objectification.  There is no new task-independent primitive, new free
composition, or coherent lowering law for every composite; the multiplication
and differentiation red teams explicitly block a global arithmetic upgrade.

---


## 9. Frozen Phase 12 gate disposition

- **Gate 12A:** partially advanced.  Frame action, chart forgetting, finite-part
  adapter, and transition data are typed; the full locale/history audit remains
  open.
- **Gates 12B--12E:** not executed.
- **Gate 12F:** partially advanced.  Source fibres, contract fibres, residual
  principal parts, and finite jets are separated for this calibration only.
- **Gate 12G:** partially advanced.  Strict descent fails, jet-corrected
  transport succeeds on bounded meromorphic germs, and composition failures
  are explicit.
- **Gate 12H:** not executed; no coupled locale/process square is claimed.
- **Gate 12I:** local verdict only: filtered semantic fibration is the strongest
  earned structure for this slice, with objectification absent.

No full Phase 12 gate is declared passed by this finite slice.

---


## 10. Governance disposition

### Mathematical Core

**Refined in evidence, unchanged in file.**  The exact obstructions sharpen the
existing distinction between task-exact descent and fibred semantic adaptation.
One projective example and one regularization family do not promote a generic
semantic-fibration theorem into the Core.

### Engineering Architecture

**Unchanged.**  The executable is a seconds-scale, research-local exact
certificate using only Python integer and `Fraction` arithmetic.  It creates no
dependency, runtime path, solver abstraction, or storage contract.

### Theory Map

**V2/V4 evidence refined, maturity unchanged.**  The slice supplies an exact
strict-lowering obstruction and a finite-jet repair, but no new free primitive
or all-composite lowering law.

### API

**No pressure.**  No regularizer, germ, jet, chart, or semantic-fibration class
is proposed for Experimental or Public API.

---


## 11. Explicit nonclaims

Phase 12A does not claim:

- that (1+2+3+\cdots) equals (-1/12) in ordinary summation semantics;
- a new proof of analytic continuation of the Riemann zeta function;
- that every regularization scheme has the same finite part;
- that finite-part extraction preserves positivity, ordinary limits,
  multiplication, differentiation, reordering, or arbitrary composition;
- a string-theory, Casimir, p-adic, adelic, or physical application;
- that all asymptotic objects reduce to finite jets without a pole-order and
  task bound;
- that projective-frame and regularization fibres are one geometric object;
- a general AM chart-transport, anomaly, or Bernoulli theorem beyond the
  declared rational-germ/exponential-chart family;
- a locale/coalgebra duality, a new vertical rank, Arithmetic Geometric
  Universality, or an API promotion.

---


## 12. Reproduction

Run:

```bash
pytest -q tests/research/test_locale_observer_history_behavior_duality.py
```

The six tests use exact rational formal-series arithmetic.  They certify the
two projective lifts, 12,400 transported-addition cases, the (0) versus
(-1/12) chart witness, the second-order jet formula, Bernoulli values through
(m=8), and the declared composition red teams.

# Workstream C — baselines, task families, and killer calibration

**Date:** 2026-08-27  
**Parent:** [issue #140](https://github.com/mountain/process-geometry/issues/140)  
**Scope:** public research-local benchmark pressure; no API or theory promotion
from this workstream alone.

## Verdict first

There is a defensible short-sprint software target, but it is narrower than
“automatic transseries” and narrower than “automatic asymptotics”:

> Given a raw finite expression/phase, a large-parameter regime, a task
> neighborhood, and a frozen monomial-chart grammar, derive a coupled chart,
> replay its exact balance certificate, and compile a cheaper evaluator.

The elementary exp/log and cancellation examples are **not** differentiators.
SymPy 1.14 solved all four tested one-variable cases in 0.1 seconds or less.
Simple WKB and first-order boundary-layer equations are also strong baseline
successes: SymPy solved them exactly and exposed the familiar Airy or
exponential scales without our compiler.

The first useful pressure point is instead **coupled, task-relative,
nonuniform scaling**.  On the Bessel transition input

\[
\Phi_N(\theta,z)=N(z\sin\theta-\theta),
\qquad (\theta,z)\approx(0,1),
\]

stock SymPy produced the local Taylor series but not an \(N\)-dependent
coupled chart; direct large-order expansion of \(J_N(Nz)\) raised its documented
multivariate-MRV `NotImplementedError`.  Once the chart is supplied manually,
SymPy verifies the normalized cubic phase immediately.  This is exactly the
gap the compiler must own: **discovery and certification of the chart, not
series arithmetic after the chart is known.**

A machine-local payoff check gives a reason to care.  At \(\nu=10^4\), on
200,000 values \(a\in[-2,2]\), the leading transition approximation

\[
J_\nu(\nu+a\nu^{1/3})
\approx 2^{1/3}\nu^{-1/3}\operatorname{Ai}(-2^{1/3}a)
\]

was about **10.1 times faster** than `scipy.special.jv`, with normalized maximum
error about **0.43%** in the recorded run.  Adding the first documented
\(P_1,Q_0\) correction was still about **8.3 times faster** while reducing that
error to about **0.0012%**.  NIST DLMF §10.19(iii), equations 10.19.8, 10.19.10, and
10.19.11, are the independent mathematical oracle.  The timing is not portable
and the current evaluator hard-codes the known chart and coefficients, so it
earns **zero discovery credit**.  It only shows that a discovered chart can
have visible software value under a repeated-evaluation workload.

## Baseline audit

| System | Verified capability | Boundary relevant to #140 | Local execution |
| --- | --- | --- | --- |
| SymPy 1.14 | Gruntz orders most-rapidly-varying subexpressions and expands in an inferred small variable for one-variable limits; exact ODE solver handles the simple WKB and boundary-layer controls | tested raw Bessel phase gives only a Taylor series; direct `besselj(N,N*z)` large-order series fails because multivariate MRV is not implemented; no task-observer interface that reports the coupled transition chart | executed |
| Sage 10.8 docs | asymptotic rings support explicit power/log/exponential growth groups and multivariate Cartesian products | the user constructs the growth group; variables in the documented multivariate product order tend to infinity independently; no documented task-driven coupled distinguished-limit finder was located | unavailable locally |
| Wolfram Language docs | `Asymptotic`, `AsymptoticIntegrate`, and `AsymptoticDSolveValue` infer asymptotic scales and explicitly cover steepest descent, WKB, boundary layers, and singular perturbations | this is the strongest unresolved baseline.  Without running the exact Airy/Bessel inputs, we must not claim the compiler capability is absent | unavailable locally; **comparison blocker** |
| van der Hoeven / Mathemagix | deep theory and algorithms for automatic exp-log asymptotics and transseries; Newton-polygon and differential-equation machinery are established comparison points | the public Mathemagix progress page describes only “a start of transseries and moulds”; current executable coverage of coupled task-driven chart discovery was not established | unavailable locally |

Primary sources:

- [SymPy series and Gruntz documentation](https://docs.sympy.org/latest/modules/series/series.html)
- [Sage asymptotic rings](https://doc.sagemath.org/html/en/reference/asymptotic/sage/rings/asymptotic/asymptotic_ring.html)
- [Sage growth groups](https://doc.sagemath.org/html/en/reference/asymptotic/sage/rings/asymptotic/growth_group.html)
- [Wolfram `Asymptotic`](https://reference.wolfram.com/language/ref/Asymptotic.html)
- [Wolfram `AsymptoticIntegrate`](https://reference.wolfram.com/language/ref/AsymptoticIntegrate.html)
- [Wolfram `AsymptoticDSolveValue`](https://reference.wolfram.com/language/ref/AsymptoticDSolveValue.html)
- [van der Hoeven, *Transseries and Real Differential Algebra*](https://www.texmacs.org/joris/ln/ln.html)
- [Mathemagix implementation status](https://www.mathemagix.org/mmxweb/web/progress.en.html)
- [NIST DLMF Bessel transition expansion](https://dlmf.nist.gov/10.19#iii)
- [NIST DLMF uniform large-order Bessel expansions](https://dlmf.nist.gov/10.20)

The distinction “not documented/found” is deliberate.  It is not a proof that
a system cannot perform the task.  In particular, the Wolfram comparison must
be executed before any comparative novelty claim.

## Frozen corpus

The machine-readable corpus is in `corpus.json`.  Its four tiers are:

1. **T0 one-parameter visibility:** exponential amplification, deep exp/log,
   and cancellation.  These are regression controls, not novelty evidence.
2. **T1 coupled parameter visibility:** nonuniform exponential integral and
   competing partition-function phases.  The output is a distinguished limit,
   not merely a fixed-parameter limit.
3. **T2 differential pressure:** a generic simple WKB turning point and a
   boundary-layer task whose required uniform accuracy prevents erasing an
   exponentially small fibre.
4. **T3 coalescing saddle:** canonical Airy as the public calibration and the
   Bessel transition as the independent non-toy killer pressure.

Negative controls require the compiler to decline Airy-style refinement for a
regular Gaussian saddle, separated phases, and a pointwise task that genuinely
does not observe a boundary layer.

## Same-information baseline protocol

A fair comparison uses the same four inputs for every system:

```text
raw expression or equation
large/small parameter and regime
task neighborhood and requested order/error
the same allowed chart grammar (when the baseline accepts one)
```

It records two distinct rows:

1. **unhinted discovery:** no scaling exponent, substitution, named normal
   form, target special function, or expected answer is supplied;
2. **hinted verification:** the discovered/known chart is supplied and the CAS
   is asked only to expand, simplify, integrate, or solve.

Only row 1 can support the compiler's discovery claim.  Row 2 measures how
much existing CAS machinery the compiler can reuse as a replaceable verifier.

For systems that have no task-observer input, encode only what their public
interface accepts and mark the interface mismatch.  Do not quietly give our
compiler a uniform-neighborhood task while giving the baseline only a fixed
limit and then call the resulting difference an algorithmic win.

## Oracle firewall and held-out plan

`run_baselines.py` is an **evaluator** and contains hinted oracle substitutions.
The compiler implementation must not import it, inspect benchmark IDs, or read
expected-chart fields.  An adapter may parse only the raw symbolic DAG,
declared variables, units, regime, task, and frozen grammar.

Because the Bessel oracle is present in the shared worktree, Bessel is not the
strict held-out.  A separate case was selected before tuning using a
commit--reveal protocol.  Its canonical-JSON SHA-256 commitment is recorded in
`heldout_commitment.json`:

```text
475733c57a34b3cfe2990445f38965e1d277329b7b38795ae0f85cd289f32a89
```

Reveal occurred after Workstream B froze composite SHA-256
`377972b2f674a06ffb66a9e99a7ac992744d214f520cacff9ac61f1a14253680`.
All 13 manifest files still matched at execution.  The frozen compiler passed:
it discovered scale powers \((-1/4,-1/2,-3/4)\), put all three phase monomials
at order zero, returned a rank-three exact solve, and replayed six successful
certificate checks.  The full result is in `heldout_result.json`.

This is a genuine held-out result, but it remains inside the same exact
polynomial-monomial balance mechanism as Airy.  It is not an independent-domain
success and does not validate Bessel/trigonometric, WKB, boundary-layer,
contour, or general chart discovery.

For later corpus growth, use generated families with oracle answers stored in
an evaluator-only artifact and freeze train/validation/test by content hash.
At least one future case should be selected by a person or agent that did not
write the compiler.

## Bessel killer contract

### Discovery input

```text
phase: N*(z*sin(theta)-theta)
regime: N -> infinity
task neighborhood: theta=0, z=1
task: retain a nonconstant O(1) phase uniformly on a compact scaled window
grammar: theta=N^(-a)u, z=1+N^(-b)xi; a,b positive rationals in frozen bounds
```

The input excludes \(1/3\), \(2/3\), “Airy”, Bessel transition formulas, and
the expected normal form.

### Required discovery output

- critical/degenerated derivative certificate at \((0,1)\);
- exact balance equations derived from the Taylor monomials;
- the unique admissible \((a,b)\) within the grammar;
- transformed phase through the first residual order;
- a domain/order statement, not only an expression;
- compilation cost and retained residual size;
- replayable SymPy certificate independent of the discovery search.

### Evaluation payoff

Compile the leading transition evaluator and compare against
`scipy.special.jv` on a frozen \((\nu,a)\) grid.  Report absolute error,
scale-normalized error, repeated-evaluation time, compilation time, code size,
and switching/fallback cost outside the transition window.  A fast but
uncertified leading formula is at most a numerical prototype.

### Killer failures

- the implementation contains benchmark-name or trigonometric/Bessel special
  cases;
- it reads the expected exponent pair or normal-form name;
- it can verify the chart but cannot derive it;
- it emits the chart without a residual/domain contract;
- the compiled evaluator has no measurable benefit at a declared tolerance;
- a same-information Wolfram baseline already returns an equal or stronger
  chart/certificate at lower total cost.

## S0--S4 alignment and Monday decision

### S0 — now frozen on this workstream

- tiered corpus and negative controls;
- same-information/unhinted-versus-hinted protocol;
- Bessel independent killer contract;
- strict held-out commitment;
- local availability and versions;
- initial cost axes.

### S1 — exact Airy certificate

Workstream C accepts the Airy case only as calibration.  Its baseline row must
show whether each system discovered the exponents or received them.

### S2 — independent pressure

Minimum bundle:

- positive: Bessel transition or generic WKB turning point;
- negative: regular Gaussian saddle or separated partition phases;
- task non-descent: boundary-layer residual or competing-phase crossover.

The exact WKB equation \(\epsilon^2y''=xy\) is too easy to be the sole second
positive case because SymPy already solves it exactly.

### S3 — held-out and cost

- reveal only after compiler freeze;
- no grammar/scoring edits;
- report compile time, repeat time, expression/code size, residual/branch state,
  verifier time, and fallback/decoder cost;
- compare against baselines with identical information.

### S4 — go / narrow / stop thresholds

**Continue** only if all of the following hold:

1. Airy scales are derived with zero oracle hints and replayable exact
   certificate;
2. one independent positive case succeeds without a special-case rule;
3. one negative case returns the correct refusal/ambiguity;
4. the strict held-out passes unchanged;
5. at least one case exhibits visible task or repeated-evaluation benefit;
6. no executed same-information baseline matches the capability with equal or
   stronger certificate and lower total cost.

**Narrow** if exact balance discovery and certificates work, but independent
domain pressure, economy, or baseline differentiation remains incomplete.  The
responsible claim is then “bounded monomial-balance certificate generator,”
not a scale or chart compiler.

**Stop this framing** if expected exponents leak, the compiler only calls
`solve` on hand-written balance equations, negative cases are silently forced,
or Wolfram/another baseline already provides the same-information result with
equal or better total cost.

The strict held-out has now passed, but the current honest outcome remains
**narrow**: the compiler's phase extractor is polynomial, so it cannot yet run
the Bessel killer from its raw `sin` phase; no independent WKB/boundary-layer
discovery has been executed; and Wolfram remains unrun.  A Bessel speedup after
a hand-supplied formula does not change that ceiling.

## Programme U1--U5/E pressure

| Obligation | What this workstream can pressure | Not earned by these results |
| --- | --- | --- |
| U1 generative presentation | a task plus raw phase generates a sufficient local chart inside a frozen grammar | a general arithmetic presentation theorem |
| U2 effective analysis | exact transformed expression, residual, verifier, and compiled numerical evaluator | general transseries closure or a new calculus |
| U3 information--complexity | task-dependent retention of a boundary/crossover scale and separate compile/evaluate/residual costs | entropy, intrinsic complexity, or a universal history ruler |
| U4 statistical--macroscopic | competing partition phases give a small calibration of a finite-size crossover fibre | ensemble equivalence, phase-transition theory, or macroscopic closure |
| U5 objectification | no positive evidence required or expected | a new primitive, rank, or compositional lowering theorem |
| E covariance/economy | exact chart transport within the frozen monomial grammar and amortized Bessel evaluation | canonical charts, full atlas covariance, or economy across domains |

**Universality claim not earned:** every version, including a successful
Bessel run, remains a local U1/U2/E pressure experiment.  It does not establish
Arithmetic Universality, effective V5 closure, a surreal runtime advantage, or
new leverage on 3D Ising.

## Reproduction

From this benchmark directory:

```bash
python run_baselines.py
```

The script emits complete JSON.  `observed_results.json` is one concise
machine-local snapshot; timings must be rerun before publication or comparison.

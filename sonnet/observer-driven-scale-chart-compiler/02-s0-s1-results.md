# Observer-driven scale and chart compiler — S0/S1 results

**Issue:** [#140](https://github.com/mountain/process-geometry/issues/140)  
**Date:** 2026-08-27  
**Disposition:** **NARROW**  
**Strongest responsible software claim:** bounded monomial-balance certificate generator

## 0. Result first

The three parallel workstreams produced a real but deliberately narrow
prototype:

1. a precise descent/minimal-repair semantics for backward task visibility;
2. a finite exact Python/SymPy implementation with typed failures, resource
   budgets, replayable certificates, residuals, and cost counters;
3. oracle-isolated Airy discovery and a strict commit--reveal held-out pass;
4. a baseline corpus showing both the opportunity and the current novelty
   blockers.

This is enough to keep the research line alive, but not enough to call the
prototype a general scale/chart compiler. The honest S4 disposition is
**narrow**, not continue: both positive discovery cases use the same exact
polynomial-monomial balance mechanism; raw trigonometric Bessel, WKB,
boundary-layer, competing-balance, and same-information Wolfram pressure have
not passed.

## 1. Exact mathematical result

Let \(q:H\twoheadrightarrow B\), \(U:H\to H'\), and
\(q':H'\twoheadrightarrow B'\). The output task descends exactly through the
current quotient iff

\[
\ker q\subseteq\ker(q'\circ U).
\]

If it does not descend, the joint map

\[
h\longmapsto(q(h),q'(U(h)))
\]

is the information-minimal exact repair: every other carrier sufficient for
both fields factors uniquely through its image. For a DAG, output predicates
pull back contravariantly and requirements from downstream branches meet by
intersection.

Inside a set-sized non-Archimedean exponential field with real residue, the
critical response window

\[
G_Y=\{x\in1+\mathfrak m:Y\log x\in\mathcal O\}
\]

has response homomorphism

\[
b_Y(x)=\operatorname{st}(Y\log x),
\qquad G_Y/\ker b_Y\cong(\mathbb R,+),
\]

and

\[
\operatorname{st}(x^Y)=e^{b_Y(x)}.
\]

Outside this window the output either saturates to zero or diverges. Scale
changes split into collapse, real rescaling, or opening a former kernel. These
facts are useful semantic pressure but are mainly direct valuation/exponential
field consequences. Surreal numbers are currently **semantically useful,
algorithmically unnecessary, and eliminable from the runtime**.

## 2. Executable certificates

### 2.1 Backward amplification

For \((1+N^{-1})^N\), the compiler records that a base distinction at order
\(N^{-1}\), locally below the \(N^0\) observer, is amplified by the exponent to
an \(N^0\) output effect. Delayed truncation and a bounded Taylor refinement
return the expected constant \(e\), an explicit remainder below the requested
band, and a replayable obligation ledger.

### 2.2 Airy calibration

From the raw phase

\[
N\left(\frac{t^3}{3}-zt\right)
\]

the solver extracted two exact monomials and solved

\[
1+3\,\mathrm{scale}(t)=0,
\qquad
1+\mathrm{scale}(t)+\mathrm{scale}(z)=0.
\]

It returned

\[
t=N^{-1/3}u,\qquad z=N^{-2/3}\xi,
\]

the normalized phase, rank-two solve, and four successful certificate checks.
The solver contains no Airy name, expected exponent, or normal-form dispatch.

### 2.3 Strict held-out

Before reveal, the frozen compiler source/test/contract manifest was committed
as

~~~text
377972b2f674a06ffb66a9e99a7ac992744d214f520cacff9ac61f1a14253680
~~~

and the unrevealed canonical JSON was committed as

~~~text
475733c57a34b3cfe2990445f38965e1d277329b7b38795ae0f85cd289f32a89
~~~

The revealed input was

\[
N\left(\frac{t^4}{4}+\frac{pt^2}{2}-qt\right)
\]

with the monomial chart grammar but no target exponents. Without modifying any
frozen file, the solver returned the unique full-rank chart

\[
t=N^{-1/4}u,\qquad
p=N^{-1/2}\xi,\qquad
q=N^{-3/4}\eta.
\]

All three phase terms have order \(N^0\); the rational constraint matrix has
rank three; six of six replay checks passed. The held-out is genuine, but it
tests the same mechanism as the Airy calibration and therefore does not count
as independent-domain evidence.

### 2.4 Failure behavior

The frozen tests also verify:

- missing or excessive input resources fail closed;
- positive polynomial-order exponentials are outside the evaluator backend;
- underdetermined scale equations request more task information;
- an insufficient Taylor budget returns <code>unsafe</code>, not a certified
  answer;
- exact cancellation is preserved;
- inexact float scale weights are rejected.

The prototype has 12 deterministic tests; all pass on the recorded environment.

## 3. Baseline and economy audit

SymPy 1.14 already succeeds on the one-variable exponential amplification,
deep exp/log, and second-/third-order cancellation controls. It also solves the
simple WKB equation and first-order boundary-layer equation exactly. These
cases are controls, not differentiators.

For the raw Bessel transition phase

\[
N(z\sin\theta-\theta),\qquad (\theta,z)\approx(0,1),
\]

SymPy returns a local Taylor series but not the coupled \(N\)-dependent chart;
direct large-order series for \(J_N(Nz)\) raises the multivariate-MRV
<code>NotImplementedError</code> in the recorded version. Once the chart is
supplied, the normalized phase and residual are easy to verify.

A machine-local repeated-evaluation benchmark at \(\nu=10^4\) and 200,000
points found the supplied leading/corrected Airy evaluators roughly an order
of magnitude faster than <code>scipy.special.jv</code>; the leading normalized
maximum error was about \(4.3\times10^{-3}\), while the first corrected form
reached about \(1.2\times10^{-5}\). These timings demonstrate potential payoff
after the chart is known and receive **zero discovery credit**.

Wolfram documentation advertises automatic asymptotic scales and coverage of
steepest descent, WKB, boundary layers, and singular perturbations. The exact
same-information cases were not executable locally, so Wolfram remains a
comparative novelty blocker. Sage growth groups and asymptotic rings normally
require the user to declare the growth structure. Existing automatic
asymptotics and transseries work prevents any claim that “automatic scale
finding” alone is new.

## 4. Why the result is NARROW

The frozen compiler currently supports:

- one generator \(N\to+\infty\);
- exact rational polynomial orders;
- a bounded local log/exp/power germ;
- all-active-monomial \(O(1)\) phase balancing;
- a unique exact linear solution or typed failure.

It does not yet support:

- analytic-germ extraction from raw <code>sin</code> or general functions;
- competing active subsets, Newton-polytopal ranking, or Pareto chart search;
- multi-parameter partially ordered scales;
- branches, Stokes sectors, contour deformation, or uniform integral error;
- independent WKB/boundary-layer discovery;
- a same-information Wolfram execution;
- a measured end-to-end economy theorem including fallback and decoder cost.

The current public claim is therefore a **bounded monomial-balance certificate
generator**. Calling it a general compiler would exceed the evidence.

## 5. Rust and backend boundary

The Monday prototype stays Python/SymPy. A later Rust core may own only stable,
pure components:

- exact rational scale constraints;
- immutable expression-DAG arenas;
- backward obligation propagation;
- certificate replay primitives and structural cost counters;
- bounded Pareto enumeration.

Python/SymPy should continue to own changing research grammar, domain/branch
assumptions, symbolic adapters, baseline orchestration, and readable proof
artifacts. The FFI boundary should carry a versioned backend-neutral IR and
replayable certificate, not opaque SymPy objects.

Rust migration is gated on cross-domain semantic stability, profiling that
locates a material bottleneck in the pure kernel, differential Python/Rust
tests, and wheel/CI maintenance cost. PyO3/maturin is a plausible packaging
route; no native dependency is introduced by these results.

## 6. Next honest gate

The next branch should remain inside this Sonnet and freeze before execution:

1. a small analytic-germ adapter that derives the local <code>sin</code> phase
   terms without Bessel/Airy special cases;
2. the raw Bessel transition discovery task;
3. a regular Gaussian negative control and at least one competing-balance
   ambiguity;
4. same-information Wolfram execution if access is available;
5. end-to-end compile, verify, repeated-evaluate, residual, fallback, and
   decoder costs.

Only a successful independent case plus a correct negative and honest
baseline/economy comparison would justify changing S4 from **narrow** to
**continue**.

## 7. Governance disposition

**Mathematical Core:** unchanged. The kernel-intersection/minimal-repair result
is exact but elementary and remains research-local.

**Research Programme:** pressures U1, U2, and E. It does not establish
Arithmetic Universality or surreal necessity.

**Research Status:** unchanged at this preliminary phase; a future independent
positive and economy result would justify a repository-wide status update.

**Engineering Architecture:** adds a problem-local exact symbolic prototype,
typed failure, cost ledger, benchmark corpus, and prospective FFI seam. No
generic solver facade or mandatory backend is introduced.

**Theory Map:** T1/local pressure on H1, H4, filtered fibres, task-covariant
evaluation, and the I3--I5 seam. No maturity promotion and no V2
objectification.

**Public API:** no pressure. Even a later positive result would first be an
extraction candidate.

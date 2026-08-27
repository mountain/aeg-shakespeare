# Observer-driven scale and chart compiler — problem frontier

**Issue:** [#140](https://github.com/mountain/process-geometry/issues/140)  
**Date:** 2026-08-27  
**Status:** T1/local research target; Sonnet-local; no Experimental or Public API

## 0. Research question

Can a task-relative compiler propagate an output observer backwards through a
finite expression DAG, retain scale information that downstream operations can
amplify, and discover a distinguished monomial chart with an exact replayable
certificate and explicit failure semantics?

The larger motivation is that an observer sees only a bounded window of a
scale ensemble. Surreal numbers, Hahn fields, transseries, valuations, and
nonstandard structures are relevant semantic comparison models. They are not
assumed to be the runtime representation, and no computational advantage is
credited to surreal arithmetic in this phase.

## 1. Frozen problem contract

The first prototype receives:

~~~text
finite exact expression DAG
one large parameter N -> +infinity
dimensionless regime
output observer and requested residual order
unknown variable scales and fixed scales
finite monomial-chart grammar and resource budget
~~~

It returns one of:

~~~text
certified finite series and residual ledger
certified unique monomial chart and normalized phase
unsafe within Taylor budget
outside the implemented scale/domain grammar
underdetermined or inconsistent balance
resource budget exceeded
~~~

Expected exponents, named normal forms, target special functions, and
case-specific rules are forbidden discovery inputs.
<code>prototype/FROZEN_CONTRACT.json</code> is the machine-readable S0
contract.

## 2. Mathematical seam

For a current task quotient \(q:H\twoheadrightarrow B\), a downstream operator
\(U:H\to H'\), and an output task \(q':H'\twoheadrightarrow B'\), exact descent
exists iff

\[
\ker q\subseteq\ker(q'\circ U).
\]

When descent fails, the information-minimal exact task repair is the joint
image

\[
q^*_{U,q'}:h\longmapsto(q(h),q'(U(h))).
\]

Equivalently, output predicates pull back contravariantly through the DAG and
branch obligations meet by intersection. This is the mathematical core of the
backward observer pass. It does not imply that the information-minimal quotient
has the cheapest encoding.

The non-Archimedean exponent example supplies a sharp amplification witness.
For positive infinite \(Y\), the near-unit elements

\[
x_a=\exp(a/Y)
\]

have the same standard part \(1\), but

\[
x_a^Y=e^a.
\]

The response coordinate \(b_Y(x)=\operatorname{st}(Y\log x)\) is the minimal
exact repair inside the critical response window. This is mainly a valuation
and exponential-field consequence, not a new surreal-specific theorem.

## 3. Initial compiler mechanism

The evaluator uses a finite log-exp-power IR and exact rational powers of
\(N\). Intermediate terms are propagated through the whole expression before
the output observer truncates them. A noninteger power is lowered locally as

~~~text
pow(base, exponent) -> exp(exponent * log(base)).
~~~

Thus a locally hidden \(N^{-1}\) perturbation in
\((1+N^{-1})^N\) is retained because the exponent amplifies it to order
\(N^0\).

For polynomial exponential phases, chart discovery distributes exact
monomials and solves one rational order equation per active term. The initial
task requires every nonzero phase monomial to be \(O(1)\). Candidate subset
search, competing balances, and chart ranking are outside this frozen phase.

## 4. Calibration and evidence firewall

The public calibration is

\[
S_N(t,z)=N\left(\frac{t^3}{3}-zt\right).
\]

The solver must derive

\[
1-3a=0,\qquad 1-a-b=0
\]

and hence \(t=N^{-1/3}u,\ z=N^{-2/3}\xi\) without receiving the exponents or
the word “Airy”.

A strict held-out is selected by commit--reveal. Compiler source, tests,
grammar, scoring, and failure semantics are hashed before the held-out preimage
is disclosed. Any post-reveal grammar or implementation edit receives no
discovery credit.

## 5. Baseline discipline

Every system receives the same raw expression/equation, regime, task
neighborhood, requested order/error, and allowed grammar when its interface
accepts one. Unhinted discovery and hinted verification are separate rows.

Required pressures include:

- SymPy one-variable exp/log and cancellation controls;
- Sage growth-group and asymptotic-ring comparison;
- Wolfram asymptotic-scale, WKB, boundary-layer, and steepest-descent
  comparison;
- automatic asymptotics and transseries work by Richardson and van der Hoeven;
- a non-toy coalescing-saddle pressure case;
- at least one correct refusal or ambiguity result.

## 6. Acceptance and kill conditions

The initial phase passes only if it provides exact replayable certificates,
typed failure, a strict held-out run without grammar edits, and honest total
cost ledgers. It must be narrowed or stopped if:

- expected scales or solved charts leak into discovery;
- the carrier stores the complete source expression as a disguised residual;
- branches, cancellation, or competing balances are resolved by undeclared
  backend heuristics;
- reparameterization changes the result with no typed transport or ambiguity;
- an equal-information baseline matches the capability with no weaker
  certificate and lower total cost;
- surreal arithmetic changes vocabulary but no theorem, algorithm,
  certificate, or reachable workload;
- a held-out result requires post-reveal grammar changes.

## 7. Claim ceiling

This work does not claim a general asymptotic or Process Geometry compiler, a
surreal runtime, a new arithmetic rank, effective V5 closure, a complexity
breakthrough, or leverage on 3D Ising. A successful S0/S1 prototype is at most
a bounded research-local certificate generator and a future extraction
candidate after independent-domain pressure.

# Phase 0 — stochastic first-passage contract

**Status:** frozen T0 contract; no public API pressure.

## 1. Physical primitive and dimensions

Begin with the overdamped feedback-trap model

\[
dx_t=V\left[\left(\frac{x_t-Vt}{L}\right)^2-1\right]dt
     +\sqrt{2D}\,dW_t,
\]

where `[x]=[L]`, `[V]=L/T`, and `[D]=L^2/T`.  In
`u=(x-Vt)/L`, `theta=Vt/L`, the only noise parameter is

\[
\varepsilon=\frac{D}{LV},
\]

which is dimensionless.  Physical first-passage cost is recovered by
`t=(L/V) theta`.

## 2. Stochastic presentation covariance

For a monotone presentation `w=h(u)`, Ito transport gives

\[
dw=\left[h'(u)(u^2-2)+\varepsilon h''(u)\right]d\theta
   +\sqrt{2\varepsilon}\,h'(u)dB_\theta.
\]

Equivalently, the backward generator

\[
\mathcal L_u=(u^2-2)\partial_u+\varepsilon\partial_u^2
\]

must commute with pullback.  Omitting the second-order term is a required
negative control, not a harmless approximation.  For `h=u+u^3`, the missing
drift is exactly `6 epsilon u`.

## 3. Frozen task signature

A first-passage task must declare all of:

- ordered physical absorbing sections;
- initial point or initial probability law;
- reset semantics between queries;
- physical clock scale `L/V`;
- dimensionless noise strength `epsilon`;
- cost functional: expectation, distributional functional, or risk measure;
- section labels retained by the decoder.

Two presentations are task-equivalent only if they transport the full stopped
process: generator, initial law, absorbing sections, labels, and clock ruler.
Endpoint correspondence alone is insufficient.

## 4. Frozen bounded presentation language

```text
atoms                 u, -1, 0, 1
constructors          commutative Add, Mul
expression depth      <= 2
domain                closed interval [-1,1]
admissibility         exact h'(u)>0 certificate on the domain
certificate arithmetic exact symbolic identities before numerics
```

The depth bound may be enlarged only after recording literal and semantic
counts.  Rational, exponential, trigonometric, spline, neural, and arbitrary
coordinate maps are outside Phase 1.

## 5. Oracle firewall

Discovery may not receive:

- the labelled answer `h(u)=u+u^3`;
- a precomputed inverse chart;
- a closed-form mean first-passage solution;
- samples labelled by the intended morphism or optimal policy;
- a general Lie/stochastic-normal-form solver;
- a Bellman value computed in the target chart;
- an observer selected by residual-driven switching.

The named nonlinear chart is available only to post-hoc covariance controls.

## 6. Required controls

1. `epsilon=0` must recover deterministic chain-rule transport and PR #87's
   clock covariance.
2. Exact Ito transport must make generator pullback residual zero.
3. Naive deterministic transport at `epsilon!=0` must leave a nonzero residual.
4. A corrupted drift or diffusion must fail even if absorbing endpoints map.
5. Equal physical-clock discretization must preserve stochastic Bellman output;
   equal coordinate discretization is the negative control.
6. First-passage numerics must be checked by an independent method, initially a
   backward boundary-value solver against Monte Carlo confidence intervals.

## 7. Kill conditions

Stop or revise the branch if:

1. task equivalence can be made to pass only by omitting Ito correction, noise
   pushforward, initial-law Jacobian, or stopping labels;
2. numerical agreement depends on using the same discretization code in both
   charts;
3. the bounded morphism search receives the held-out chart as an oracle;
4. coordinate-dependent mesh or tolerance is reported as physical cost;
5. Monte Carlo uncertainty is smaller than unreported discretization bias;
6. stochastic Bellman covariance fails under independently converged solvers;
7. grammar growth cannot be accompanied by auditable exact negative
   certificates.

## 8. Claim boundary

Phase 0 certifies a well-posed falsifiable interface.  It does not establish a
new stochastic calculus, discover a canonical chart, solve a first-passage
distribution, prove Bellman invariance, or produce a Noether charge.

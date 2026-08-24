# Phase 2 — stopped-process task-quotient result

**Status:** exact covariance pass; naive-transport red team passes.

The frozen depth-three slice gives:

```text
strictly increasing presentations       242
full Itô task transports passing         242
task-equivalence classes                   1

naive no-Itô-correction passes            87  (all affine)
naive no-Itô-correction failures          155  (all nonlinear)
```

For every chart, the exact symbolic residual

\[
\mathcal L_u(q\circ h)-((\mathcal L_wq)\circ h)
\]

vanishes for generic quadratic `q`. The forward chart also retains the ordered
absorbing sections and their labels, maps the initial point, and leaves the
dimensionless clock `theta=Vt/L` unchanged. Strict monotonicity supplies the
inverse-existence certificate without pretending that the inverse is a
polynomial in the grammar.

When `epsilon*h''` is deliberately removed from the transformed drift, the
residual is zero exactly when `h''=0`: all 87 affine charts pass and all 155
nonlinear charts fail. Thus the earlier affine/nonlinear distinction is not a
physical split. It is the observable signature of applying deterministic
transport to a stochastic process.

## Interpretation

The task quotient does not select `u+u^3`; it proves something stronger and
less syntactic. Within this bounded slice, all 242 presentations are gauges of
one labelled stopped process. Canonicalization returns the task-equivalence
class. Choosing a short or convenient representative is downstream
serialization, not canonical physics.

This closes generator-level covariance only. It does not show that a numerical
first-passage solver, reset Bellman recursion, or blind morphism finder respects
the class. The next high-information gate is an independent backward BVP plus
Monte Carlo check in at least one affine and two nonlinear charts, with a
coordinate-uniform mesh retained as an expected-to-fail control.

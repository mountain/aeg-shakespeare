# Phase 2 — stopped-process task-quotient contract

**Status:** frozen before execution.

Depth three leaves 242 strictly increasing presentations, 155 of them
nonlinear. This gate asks whether they are different physical tasks or
coordinate gauges of one stopped diffusion; it does not rank resemblance to
the post-hoc control.

For every certified `w=h(u)`, transport the complete dimensionless task:

```text
drift                 h'(u)(u^2-2) + epsilon h''(u)
diffusion variance    2 epsilon h'(u)^2
absorbing sections    (-1, 1) -> (h(-1), h(1))
section labels        (left, right), in that order
initial point         0 -> h(0)
clock                 theta = Vt/L, unchanged
```

No polynomial formula for `h^{-1}` is required: strict increase on the whole
closed interval is the inverse certificate. The forward map plus its domain is
the presentation morphism.

## Exact acceptance tests

For a generic quadratic observable `q(w)=alpha+beta*w+gamma*w^2`, require:

1. the Itô target generator pulled back by `h` equals the source generator of
   `q(h(u))` exactly;
2. sections, labels, initial point, and clock are transported exactly;
3. all 242 monotone presentations form one task-equivalence class;
4. in the deliberately naive transport that omits `epsilon*h''`, precisely
   the affine presentations pass and every nonlinear presentation fails at
   nonzero symbolic `epsilon`.

The affine/nonlinear split in item 4 is a red-team result, not a desired
classification: it must disappear under the complete Itô semantics.

## Kill and shrink conditions

- Any exact Itô residual among the 242 candidates refutes the claimed
  presentation covariance for this grammar slice.
- Any nonlinear candidate passing the naive deterministic chain rule at
  symbolic nonzero noise falsifies the proposed affine-only red team.
- If equivalence requires discarding section labels, the initial point, or the
  clock, it is not task equivalence.
- If all candidates pass, the conclusion is a canonical **class**, not a
  canonical syntax representative. Representative selection remains a
  separate engineering convention and may not be reported as physics.

Passing this gate licenses the stochastic generator part of the plan. It does
not yet license first-passage values, Monte Carlo agreement, reset Bellman
optimization, or blind discovery.

# Phase 4 — dimensionful reset-Bellman result and closure

**Status:** exact policy/value covariance at the declared BVP resolution;
current research line closed.

For the frozen actions, the independently assembled 401-node BVP and
regenerative Bellman calculation give:

```text
chart       left-reset       center-reset     right-reset      optimum
u           0.566318303      0.572670212      1.096757884      left-reset
u+u^3       0.566313315      0.572666831      1.096755417      left-reset
2u+u^3      0.566317750      0.572671464      1.096760447      left-reset
```

The largest cross-chart discrepancy in the optimal value is below `5.0e-6`.
The runner-up is separated from the optimum by more than `0.006`, so the
policy agreement is not a numerical tie. Substitution of the reported optimum
back into

\[
J=\min_a\{\rho_a+\tau_a+p_aJ\}
\]

closes with the same action and value in every chart.

The source-chart task payload underlying the three action values is:

```text
action          mean tau       right-exit p       reset rho
left-reset      0.316306337    0.000021130        0.25
center-reset    0.572194334    0.000830981        0
right-reset     0.801879205    0.040919404        0.25
```

## Dimensions and red teams

Restoring dimensions multiplies reset times, absorption times, every action
value, and the optimum by `L/V`; probabilities and the `left-reset` policy are
unchanged.

Swapping `left` and `right` labels is rejected as a different task. Charging
reset work by target-coordinate distance instead of physical time produces
left-action values

```text
u           0.816323586
u+u^3       0.941321235
2u+u^3      1.441336236
```

and changes the optimum to `center-reset`. The common changed policy does not
rescue the charge: the action values vary strongly with chart, demonstrating
that coordinate distance is not the retained additive resource.

## What has closed

The experimental chain is now end to end:

```text
bounded A/M candidates
  -> monotone presentation morphisms
  -> full stopped-process task quotient
  -> Ito generator covariance
  -> first-passage observable covariance
  -> dimensionful regenerative Bellman value and policy covariance
```

This supports the refined relation between canonicalization and
Huffman/Bellman optimization. Canonicalization first supplies the task-relative
flat unit—labelled histories measured by an invariant additive resource—and
Bellman then optimizes on that unit. Huffman is the unit-edge, prefix-tree
specialization; no general Huffman/Bellman theorem is claimed here.

Blind recovery of a preferred syntax is deliberately not required: Phase 1
showed that the task has 155 admissible nonlinear spellings, and Phase 2 showed
that they belong to one canonical class. Representative choice is an
engineering convention. Further work should move to a new Sonnet or an API
incubation proposal rather than extend this calibration indefinitely.

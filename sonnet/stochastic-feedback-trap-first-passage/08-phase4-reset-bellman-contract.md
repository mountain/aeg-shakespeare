# Phase 4 — dimensionful reset-Bellman contract

**Status:** frozen before execution; final required closure gate.

The stopped diffusion now becomes a regenerative decision task. At each attempt
the controller chooses one labelled reset section

```text
action label       reset u       dimensionless reset time rho
left-reset         -1/2          1/4
center-reset        0            0
right-reset         1/2          1/4
```

After resetting, the process evolves without intervention until it reaches a
labelled absorbing section. Reaching `left` terminates successfully. Reaching
`right` is a failed attempt and returns to the same decision state. No reward
or action is defined by target-coordinate distance.

For action `a`, let `tau_a` be its mean dimensionless absorption time and
`p_a` its probability of reaching `right`. The stationary Bellman equation is

\[
J=\min_a\{\rho_a+\tau_a+p_aJ\}.
\]

Equivalently, each stationary action has regenerative value

\[
J_a=\frac{\rho_a+\tau_a}{1-p_a},
\]

and the unique minimum, if present, is the optimal policy. Both `tau_a` and
`p_a` must be solved from the transported generator and labelled boundaries;
neither is supplied as an oracle.

## Frozen charts, numerics, and units

```text
epsilon              1/4
charts                u; u+u^3; 2u+u^3
BVP nodes             401 transported nodes
physical clock        t = (L/V) theta
physical reset cost   c_a = (L/V) rho_a
physical value        J_phys = (L/V) J
```

## Acceptance tests

1. Independently assembled BVPs recover `tau_a` and the labelled right-exit
   probability in every chart.
2. Bellman values and the uniquely optimal action agree under all three task
   morphisms within the declared discretization tolerance.
3. Scaling `L/V` scales every action value and the optimum, but leaves the
   policy unchanged.
4. Swapping absorbing labels changes the task and must not pass as a coordinate
   morphism.
5. A coordinate-distance reset charge is retained as a red team and must
   produce chart-dependent action values. It is not a physical complexity.

## Kill and closure conditions

- Different charts select different physical actions under transported costs.
- Value covariance requires changing `epsilon`, endpoint labels, or reset
  sections.
- The physical value fails to scale exactly as `L/V`.
- A coordinate-dependent red-team charge is silently accepted as invariant.

Passing closes the current canonicalization–Bellman research line for this
one-dimensional stochastic task. Blind syntax discovery and general
Huffman/Bellman theorems remain separate future work, not closure blockers.

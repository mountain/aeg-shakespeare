# Phase 3 — first-passage numerical result

**Status:** BVP covariance passes strongly; Monte Carlo passes at calibration
precision; mesh red team passes.

For `epsilon=1/4`, the transported-node backward BVP gives `T(0)`:

```text
chart       n=101            n=201            n=401
u           0.5721524078     0.5721859522     0.5721943339
u+u^3       0.5720961799     0.5721718950     0.5721908196
2u+u^3      0.5721707270     0.5721905310     0.5721954785
```

At 401 nodes, the nonlinear charts differ from the source value by
`3.51e-6` and `1.14e-6`. They approach the same continuum value without a
closed-form first-passage oracle or a polynomial inverse.

## Independent path simulation

Direct target-chart Euler-Maruyama evolution gives:

```text
chart       dt=.004, 2500 paths       dt=.002, 5000 paths (standard error)
u           0.5881984                 0.5796132 (0.0042474)
u+u^3       0.5967472                 0.5837884 (0.0042777)
2u+u^3      0.5979232                 0.5820684 (0.0042277)
```

All refined estimates contain the BVP value within the frozen sampling-plus-
timestep-bias envelope. The downward movement under timestep refinement is
consistent with discrete monitoring overshoot. This is an independent
calibration, not a high-precision Monte Carlo certificate: eliminating the
remaining boundary bias would require Brownian-bridge or boundary-shift
corrections.

## Mesh red team

With 101 nodes uniform in each target coordinate, the three values are

```text
u           0.5721524078
u+u^3       0.5722339455
2u+u^3      0.5722157228
```

Thus equal target-coordinate node counts create finite-resolution differences
of `8.15e-5` and `6.33e-5` relative to the identity chart. These are
discretization effects, not physical time costs. They shrink under refinement
and may even have a smaller signed error accidentally at one resolution; the
red-team claim concerns chart dependence, not a predetermined error sign.

Finally, physical time is restored uniformly as

\[
T_{\rm physical}=(L/V)T.
\]

The result supports lift-first measurement followed by a task quotient: the
generator, stopping sections, and clock define the flat comparison unit;
coordinate-uniform numerical work does not. Resettable Bellman optimization is
still outside this result and is the next conceptual gate.

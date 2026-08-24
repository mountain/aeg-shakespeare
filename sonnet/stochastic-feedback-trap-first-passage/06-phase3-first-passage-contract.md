# Phase 3 — first-passage BVP and Monte Carlo contract

**Status:** frozen before execution.

The symbolic generator quotient is not enough: a numerical method may silently
reintroduce coordinate geometry through its mesh, timestep, or stopping rule.
This gate tests the dimensionless mean first-passage time `T` solving

\[
(u^2-2)T'(u)+\varepsilon T''(u)=-1,
\qquad T(-1)=T(1)=0,
\]

at the retained initial section `u=0`.

## Frozen parameters and charts

```text
epsilon              1/4
initial point         u0 = 0
absorbing interval    [-1, 1], labels retained
charts                u; u+u^3; 2u+u^3
BVP refinements       n = 101, 201, 401 interior-and-boundary nodes
Monte Carlo           seeded Euler-Maruyama, independently evolved per chart
physical clock        theta; dimensional value is (L/V) T
```

The two nonlinear charts are declared before seeing solver output. Their
inverses may be evaluated numerically only for evolving the target-chart SDE;
they are not discovery inputs.

## Acceptance and red-team conditions

1. A source-chart backward BVP supplies the refinement reference, not a closed
   form first-passage oracle.
2. Independently discretized target-chart BVPs on transported nodes converge to
   the same `T(0)` as the source chart.
3. Seeded target-chart Euler-Maruyama estimates agree with the refined BVP
   within a declared combination of sampling uncertainty and timestep bias.
4. Multiplication by `L/V` restores physical time units in every chart.
5. A uniform target-coordinate mesh is retained as a red team. At equal node
   count it must show a measurable chart-dependent truncation error for at
   least one nonlinear chart; it need not have the wrong continuum limit.

## Kill and shrink conditions

- Chart values extrapolate to different continuum limits.
- Agreement requires relabelling the absorbing endpoints or changing the
  dimensionless clock.
- Monte Carlo uncertainty is reported without a timestep refinement check.
- The uniform-target-mesh control is called a physical cost difference rather
  than a discretization artifact.
- A pass is limited to the declared one-dimensional diffusion and these charts;
  it does not establish reset-Bellman policy covariance.

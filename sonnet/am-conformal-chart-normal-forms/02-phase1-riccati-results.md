# Phase 1: Riccati Projective-Mechanism Calibration Results

## Status and boundary

- **Status:** the Phase 1 exact mechanism calibration is complete.
- **Certificate:** `tests/research/test_am_conformal_chart_riccati.py`.
- **Arithmetic:** Python `Fraction`; no floating-point error and no external
  dependency.
- **Strongest claim:** level-1 classical re-expression; no bounded discovery,
  no economy theorem, and no joint-normal-form theorem.

## 1. Positive control

For

$$
\dot a=c_0+c_1a+c_2a^2,
\qquad a=-x/y,
$$

the exact certificate verifies that

$$
\frac d{dt}\binom{x}{y}=
\begin{pmatrix}c_1/2&-c_0\\c_2&-c_1/2\end{pmatrix}
\binom{x}{y}
$$

recovers the original scalar field.  The test exhausts $4^3$ rational
coefficient triples at five rational chart points, for a total of 320
scalar--lift identities.

For three nontrivial Möbius charts, the certificate lifts

$$
b=\frac{\alpha a+\beta}{\gamma a+\delta}
$$

to the homogeneous-coordinate transformation

$$
S=\begin{pmatrix}\alpha&-\beta\\-\gamma&\delta\end{pmatrix},
\qquad L_b=SLS^{-1},
$$

and checks pointwise that the chart readout commutes with the matrix dynamics.
Points where a denominator vanishes are not crossed silently; they are
recorded as infinity-chart boundaries.

## 2. Gauge and no-go

For several rational values of $\gamma$, the certificate verifies that

$$
L\mapsto L+\gamma I
$$

changes the homogeneous lift without changing the dynamics of $a=-x/y$.  This
is a presentation gauge, not a new physical degree of freedom.

The reverse calculation also gives an exact neighboring no-go.  An arbitrary
constant matrix

$$
L=\begin{pmatrix}u&v\\w&z\end{pmatrix}
$$

can produce only

$$
\dot a=-v+(u-z)a+wa^2
$$

under the projective readout.  A generic nonzero cubic term therefore cannot
come from the same constant-coefficient two-dimensional linear lift.  Handling
a cubic scalar field requires a change of dimension, a state-dependent matrix,
a cover, or some other additional structure whose cost must be recorded
separately.

## 3. Cost verdict

The eight-axis `CostVector` now supports strict Pareto-dominance checks:

$$
(C_{coeff},C_{action},C_{singular},C_{atlas},C_{decoder},
C_{unit},C_{eval},C_{residual}).
$$

The red team deliberately constructs a candidate with shorter coefficients but
a more expensive decoder and atlas, confirming that character count alone
cannot make it preferable.  The classical two-dimensional lift also does not
dominate direct scalar evaluation.  Phase 1 therefore establishes a covariance
mechanism, not computational economy.

## 4. Gate 1 verdict

| Gate | Result | Explanation |
| --- | --- | --- |
| 1A exact lift | pass | the scalar field and two-dimensional lift commute exactly |
| Möbius covariance | pass | the chart readout and matrix conjugation commute exactly |
| scalar gauge | pass | projective dynamics is invariant |
| 1C cubic red team | pass | a nonzero cubic term is rejected correctly |
| joint cost accounting | pass | eight-axis Pareto accounting, not character-count scoring |
| 1B bounded discovery | **not run** | the current matrix is classically derived, not recovered by blind search |

Phase 1 is therefore only partially closed: the mechanism and no-go are
complete, but the discoverer remains open.  Before entering pendulum Phase 2,
freeze a low-height chart/lift grammar that cannot see the target matrix and
test whether it can recover a task-equivalent sparse two-component
presentation from the Riccati coefficients.

## 5. Relation to the latest theory

- an invertible same-layer chart preserves an exact round trip;
- cross-layer forgetting uses a semantic adapter and is not covered by this
  certificate;
- a task quotient requires continuation adequacy; and
- whether an observer has a coherent response after a chart change remains
  graded by Phase 12C's C0--C4 ladder and does not follow automatically from
  coordinate covariance.

The Mathematical Core, Engineering Architecture, Theory Map, and Public API
are unchanged by this phase.  The certificate remains research-local.

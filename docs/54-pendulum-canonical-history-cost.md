# Pendulum canonicalization meets Hauffman history geometry

**Status:** T0 research note; first executable bridge; no Theory Map or API promotion.

## 1. The interface

The pendulum and Hauffman lines now meet through a narrower object than either
an elliptic curve or a decision tree:

\[
\boxed{\text{task-relative history quotient equipped with canonical edge measure}.}
\]

The two inputs have different jobs.

```text
process + task
    -> canonical observable quotient
    -> lifted histories modulo task equivalence
    -> canonical clock measure on history segments
    -> admissible stopping tree/DAG
    -> costed Bellman/Hauffman optimization
```

Canonicalization determines the state distinctions and the cost geometry on
which planning is allowed to operate.  Hauffman optimization determines how
those distinctions should be scheduled, shared, and stopped.  Neither layer
subsumes the other.

## 2. What the pendulum contributes

On a fixed energy leaf the selected observable carrier is

\[
C_E:\quad Y^2=2(E-U)(1-U^2),\qquad Y=DU,
\]

with marked differential

\[
\omega=\frac{dU}{Y},\qquad \omega(D)=1.
\]

For any invertible observable reparameterization (X=f(U)), its process
velocity is (Z=DX=f'(U)Y), hence

\[
\frac{dX}{Z}=\frac{f'(U)dU}{f'(U)Y}=\frac{dU}{Y}.
\]

Therefore the history-segment cost

\[
c(\gamma)=\int_\gamma\omega
\]

is unchanged by this presentation change, while (|\Delta U|) generally is
not.  The marked Abelian differential is thus a concrete candidate for the
time-like edge measure of the pendulum history carrier.

This statement is local to orientation-preserving trajectory segments.  Global
histories still require sheet, turning-point, period, and winding data.

## 3. What task quotienting contributes

The reduced state ((U,Y)) forgets the simultaneous Cartesian reflection

\[
(q_x,v_x)\mapsto(-q_x,-v_x).
\]

That bit is irrelevant to a task stated entirely on (C_E), but necessary for
local reconstruction of the Cartesian state.  Consequently there is no single
task-independent Hauffman tree for the pendulum.  The correct order is

\[
\text{lifted histories}\longrightarrow
\text{task quotient}\longrightarrow
\text{prefix/stopping optimization}.
\]

Coding first would spend depth distinguishing histories the task may identify;
quotienting too aggressively would destroy reconstructability.

## 4. Hauffman as the unit-cost special case

For a finite task state (S), an admissible observation (a) with outcome
states (S_j), probabilities (p_j), and canonical first-hit cost
(c_\omega(S,a)) gives

\[
V(S)=\min_a\left[
c_\omega(S,a)+\sum_j p_jV(S_j)
\right].
\]

When every admissible edge has cost one and every node is a tree node, this
reduces to expected prefix depth and classical Huffman reasoning becomes the
unconstrained reference.  The pendulum does not generally have unit edge
costs: different observation boundaries can be separated by different
(\int\omega).  The executable red team shows that changing one first-hit cost
can change the optimal root even while task probabilities remain fixed.

Thus the proposed connection is not

```text
canonicalization = Huffman coding
```

but

```text
canonicalization supplies invariant states and edge costs;
Hauffman/Bellman planning optimizes a task-stopping presentation over them.
```

## 5. What this resolves

This bridge explains four earlier observations at once:

1. the elliptic carrier alone is not complete canonicalization, because global
   history and task-dependent decoder data remain;
2. the observer ODE is local kinematics rather than a future-aware optimizer;
3. the Hauffman tree is not intrinsic until its task quotient and edge costs
   have been canonicalized;
4. process time and representation depth coincide only in the unit-cost
   calibration, not by definition.

## 6. Claim boundary and next experiment

The present test establishes coordinate invariance, refinement additivity,
task-relative branch retention, and the failure of ordinary unit-depth Huffman
under unequal edge costs.  It does **not** establish:

- a canonical observer metric;
- a canonical global lift across all turning points;
- convergence of finite trees to a measured real tree;
- coincidence of the observer direction with an HJB characteristic;
- a general continuous-Huffman theorem.

The next falsifiable experiment should discretize one libration orbit by
equal-(\omega) first-hit sections, compare it with equal-(U) sections under a
nonlinear reparameterization, and solve the same finite stopping task on both.
The expected result is that equal-(U) trees change under reparameterization,
whereas the clock-measured quotient and its optimal cost agree.  Failure of the
latter would reject this proposed interface.

**Experiment completed:** `docs/61-pendulum-section-reparameterization-redteam.md`
executes this prediction for (X=U^3). Equal-clock sections give the same
optimized value and policy below (10^{-30}) tolerance; equal-coordinate
sections change both. The result is local to one regular libration branch.

## 7. Governance

```text
Epistemic maturity: T0
Role: problem-local bridge / extraction candidate
Theory Map Change: none
Experimental/Public API pressure: none
```

The implementation remains in `tests/research/`.  No generic history-cost,
stopping-surface, or continuous-Hauffman noun is added to the package.

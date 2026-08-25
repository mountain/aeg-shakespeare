# AM universal-history recalibration

**Status:** T0 corrective research note; executable four-problem calibration;
no Theory Map or API promotion.

## 1. Why the previous conclusion needed reopening

The previous cross-problem audit correctly observed that canonical quotients may
be trees, DAGs, Cayley graphs, covers, or groupoids.  It then came too close to
using this variation to separate canonicalization from Huffman/Bellman
geometry.

That inference is not valid.  A quotient carrier need not be a tree even when
its free or lifted history space has a common rooted unfolding.  Complexity may
have to be measured before quotienting:

\[
\text{primitive process}
\to
\text{canonical AM lift}
\to
\widetilde{\mathcal H}
\to
\text{measure and optimize}
\to
\widetilde{\mathcal H}/R.
\]

Here (R) may encode endpoint equivalence, task equivalence, period shifts,
monodromy, or objectified reconvergence.  Tree/DAG/groupoid are then different
quotient shadows, not necessarily different complexity foundations.

## 2. An essential correction: universal is not automatically flat

A topological universal cover removes fundamental-group ambiguity but does not
remove local curvature.  Likewise, a rooted history unfolding remembers paths
but does not automatically choose a canonical ruler.

For complexity measurement we need more than universality:

1. a common primitive process frame;
2. an additive cost or cost vector on concatenated histories;
3. invariance, covariance, or explicit transport under admissible presentation
   changes;
4. a task-sufficient stopping section;
5. when scalar comparison is required, a justified scalarization.

The working object is therefore not a bare universal cover but a

\[
\boxed{\text{universal history lift with canonical AM ruler and cost cocycle}.}
\]

"Flat" first means that process units can be transported and compared without
coordinate-dependent distortion.  It does not by itself assert zero Riemannian
curvature of every quotient shadow.

## 3. Four AM recalibrations

### 3.1 Signed translation

Free words in the Addition generator and its inverse form a prefix tree.  The
Multiplication generator is not used in this rank-one calibration.  The
continuation-stable endpoint quotient is net displacement.  `+` and `++-`
reach the same endpoint but cost one and three primitive steps.

Thus the Cayley graph is the canonical endpoint carrier, while time depth and
frontier volume remain properties of the lifted history or an optimized
section through it.  This supports lift-first measurement.

### 3.2 Hard-particle first contact

For adjacent particles,

\[
\tau_i=\frac{x_{i+1}-x_i}{v_i-v_{i+1}}.
\]

Common position translation and velocity boost are Addition-type gauges;
common positive scaling of positions and velocities is a Multiplication-type
gauge.  The vector ((\tau_i)), its argmin stratum, and the first-hit clock are
unchanged.

The canonical quotient therefore supplies invariant walls, while the comparison
history tree supplies the admissible stopping policies.  Canonicalization and
Bellman optimization are consecutive layers, not rivals.

### 3.3 Pendulum

On the observable carrier,

\[
Y=DU,\qquad \omega=\frac{dU}{Y}.
\]

For an affine AM observer change

\[
X=sU+b,\qquad Z=DX=sY,
\]

one has

\[
\frac{dX}{Z}=\frac{dU}{Y}.
\]

The lifted clock is additive and presentation-invariant under this declared
AM shadow.  The elliptic carrier, branch data, and period residual arise after
projection.  This supports measuring stopping cost on lifted clock history.

It does not yet prove that the full clock lift is discovered intrinsically by
AM canonicalization, nor that a preferred observer metric exists.

### 3.4 Abelian period history: the necessary obstruction

The Abelian integral lifts history to an additive space, and quotienting by a
period lattice produces the visible torus.  This strongly supports the
universal-lift part of the hypothesis.

But universality alone does not choose a scalar complexity.  In rank two, the
same lattice displacement has coefficient vector `(0,1)` in the standard basis
and `(-1,1)` in the sheared basis

\[
e_1,\quad e_1+e_2.
\]

Their naive (\ell^1) word costs are one and two.  Both bases generate the same
lattice and the same quotient endpoint.

Therefore:

\[
\boxed{
\text{universal lift + additive composition}
\not\Rightarrow
\text{canonical scalar complexity}.
}
\]

A canonical AM ruler, transported frame, invariant metric, Pareto cost vector,
or task-relative scalarization remains necessary.

## 4. Revised relationship

The evidence now supports the following diagram:

```text
primitive A/M process
    -> many presentations and histories
    -> local canonicalization
    -> canonical observer transport / developing lift
    -> universal history unfolding with cost cocycle
    -> task stopping section
    -> Huffman/Bellman optimization
    -> quotient/objectification/residual shadow.
```

This yields the corrected statement:

\[
\boxed{
\text{Huffman/Bellman optimization acts on a canonically measured universal
history lift; the visible carrier is generally its quotient shadow.}
}
\]

The statement is conditional.  If the canonical ruler or its transport cannot
be constructed, the optimization value remains presentation-relative.

## 5. What "time" and "space" mean upstairs

For a stopping section (\Sigma_T) in the history unfolding:

- time depth is accumulated process cost along a root-to-section history;
- worst time is the maximum such cost;
- expected time integrates it against the declared usage measure;
- spatial frontier is the set or measure of live distinguishable histories at
  a common process-cost cut;
- process volume integrates frontier size across cost depth;
- objectification adds shortcut generators and must charge dictionary/decoder
  cost rather than silently changing the ruler.

Measuring these quantities directly on a quotient can undercount histories,
mix unequal local units, or hide winding and reconvergence.

## 6. Falsifiable next theorem and experiment

For two admissible presentations (P_1,P_2) of the same task, construct AM
canonical lifts and comparison maps

\[
D_i:\widetilde{\mathcal H}_i\to\mathcal U.
\]

The next target is not equality of coordinate trees, but preservation of:

1. task observation;
2. concatenation;
3. residual/deck action;
4. cost cocycle;
5. stopping sufficiency.

If these commute, the optimized values should agree:

\[
V_T(P_1)=V_T(P_2).
\]

The decisive red team is to find two presentations whose quotient-space costs
disagree while their canonically lifted costs agree.  Failure of lifted
agreement would reject the current conjecture or show that the alleged AM ruler
is not canonical.

The first end-to-end instance is executed in
`docs/61-pendulum-section-reparameterization-redteam.md`: one lifted pendulum
history, task stopping sections, clock costs, and finite Bellman optimization
commute under (X=U^3), while equal-coordinate controls do not. This supports one
comparison square only; it is not evidence that all eight arrows commute.

## 7. Effect on the previous audit

This note **refines and partially corrects**
`docs/55-cross-problem-canonical-history-correspondence.md`:

- retained: quotient carriers genuinely split into tree, graph/DAG, and
  cover/groupoid forms;
- corrected: this split does not separate canonicalization from
  Huffman/Bellman at the universal-history level;
- new obstruction: universality does not itself choose a scalar cost;
- surviving claim: stopping optimization is task-relative and downstream of
  canonical lift and ruler construction.

## 8. Governance

```text
Epistemic maturity: T0
Role: corrective cross-problem calibration
Theory Map Change: none
Experimental/Public API pressure: none
```

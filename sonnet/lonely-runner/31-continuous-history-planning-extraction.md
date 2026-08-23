# Continuous history planning — extraction candidate from Hauffman geometry

**Status:** T0 research/extraction candidate; no Theory Map or API promotion.  
**Origin:** the exact A/M contact/Hauffman line in Sonnet 001.  
**Scope:** continuousization of history geometry and planning semantics; not a new Lonely Runner result.

## 1. Why this note exists

The finite Sonnet line has already made three layers executable:

```text
A/M differential contact law
    -> contact-wall arrangement
    -> task-relative stopping / decision tree
    -> weighted-depth optimization
```

The two-relative-speed calibration showed that a constrained wall tree can approach the unrestricted ternary Huffman information bound while remaining executable in the native A/M/contact grammar.  The three-relative-speed calibration then improved several history-geometry axes simultaneously: peak frontier, boundary volume, worst depth, and expected task depth.

Those results suggest a question that is larger than finite Huffman coding but still downstream of the exact Sonnet evidence:

> Is there a controlled continuous limit in which a task-stopping prefix tree becomes a measured history geometry and the finite dynamic-programming recursion becomes a continuous planning equation?

This note records the question without promoting a new framework object.

---

## 2. What is already exact

The current finite objects should remain the calibration baseline.

For a task-stopping tree, depth is a representation/process coordinate and

\[
W(n)=|B_n|
\]

is the live frontier width.  Useful recorded quantities include

\[
W_{\max},\qquad \sum_n W(n),\qquad d_{\max},\qquad \mathbb E[d].
\]

The wall-tree search is already a finite planning problem.  At a task state `S`, an admissible wall/query `a` has outcome states `S_j` with usage probabilities or weights, and exact dynamic programming evaluates a recursion of the form

\[
V(S)=\min_{a\in\mathcal A(S)}
\left[c(S,a)+\sum_j p_jV(S_j)\right].
\]

When `c=1`, `V` is expected remaining decision depth.  This Bellman interpretation does not add mathematics to the finite optimizer; it clarifies the planning semantics already implemented by the dynamic program.

---

## 3. First continuousization candidate: measured real history tree

A prefix tree has a natural order by extension and a natural boundary of complete histories.  A possible continuous limit is a rooted measured real tree

\[
(\mathcal T,d,o,\mu),
\]

where

- `o` is the root;
- `d(o,x)` is continuous process/history depth;
- `mu` is a declared input/task usage measure;
- a depth cut defines a frontier of histories not yet task-complete.

This is a candidate model, not a theorem that every continuous Process Geometry history space is a real tree.  Reconvergence, cycles, DAG structure, noncommutative history, or higher-dimensional arrangements may force a more general carrier.

The earlier documentation proposed a mass-based continuous depth

\[
s(x)=-\kappa^{-1}\log\mu(C_x)
\]

for a history cylinder `C_x`.  In the present note this is one possible coordinate, not a preferred definition.

---

## 4. Frontier complexity in a continuous carrier

Literal cardinality no longer works when a frontier is infinite.  Two candidate replacements should remain distinct.

### 4.1 Measure/partition information

If a depth cut induces a measurable task/history partition

\[
\Pi_s=\{C_\alpha(s)\},
\]

define, when appropriate,

\[
I_\mu(s)=H_\mu(\Pi_s)
=-\sum_\alpha\mu_\alpha(s)\log\mu_\alpha(s).
\]

This requires a probability/usage semantics and is not an intrinsic entropy of the bare process.

### 4.2 Metric covering information

If the frontier carries a task-relevant metric, one may instead inspect

\[
I_\epsilon(s)=\log N_\epsilon(\partial\mathcal T_s).
\]

This is a metric-entropy/covering quantity and need not agree with the probabilistic entropy above.

The distinction is important: the finite Sonnet already showed that terminal class count, live process frontier, and expected code depth are different resources.

---

## 5. A candidate process spacetime integral — interpretation only

The finite research note already suggested a diagnostic

\[
\sum_n \Pr(\tau\ge n) I(n).
\]

A direct continuous analogue is

\[
\mathcal V_{\rm hist}
=\int_0^\infty \Pr(\tau>s) I(s)\,ds.
\]

This has an intuitive interpretation as a usage-weighted history/frontier volume: how much distinction remains alive, integrated over process depth.

**Do not promote the name `ProcessSpacetime` from this formula.**  At this stage the integral is only one multi-axis diagnostic.  Its invariance under representation changes, measure changes, depth reparameterization, and task quotienting is unknown.

---

## 6. Stopping surfaces

Leaves of a finite prefix code form an antichain: every completed history meets one terminal prefix and no terminal prefix extends another.  In a continuous history carrier the analogous object may be a **stopping surface** or stopping section `Sigma` intersecting each relevant history ray at first task sufficiency.

A formal variational target would look like

\[
\inf_\Sigma
\int_{\partial\mathcal T}
 d(o,\Sigma(\xi))\,d\mu(\xi),
\]

subject to task sufficiency and a suitable prefix/first-hit condition.

This is only a research formulation.  The correct continuous object may be an optimal stopping time, free boundary, section of a history fibration, or something else.  `StoppingSurface` must therefore not become an API noun from this note.

---

## 7. Objectification as planning-language growth

The existing history program allows repeated task-relevant subhistories to become candidate primitives.  In planning language, this is analogous to adding a macro-action or option.

A new primitive may:

- reduce expected or worst depth;
- alter the live frontier;
- increase decoder/dictionary cost;
- preserve or destroy transfer to a larger task world.

Thus the representation problem is not merely to optimize a tree in a fixed action language.  It may jointly optimize

\[
\text{planning language} + \text{stopping policy}.
\]

This interpretation is consistent with the Sonnet objectification experiments but does not define generic Process Geometry objectification.

---

## 8. Bellman to HJB — a possible limit, not a current claim

If a sequence of finite task-state spaces converges to a continuous state carrier `M`, admissible decisions converge to controls `u`, and local transitions converge to

\[
\dot z=F(z,u),
\]

then a continuous Bellman limit may take Hamilton--Jacobi--Bellman form

\[
0=\inf_u\{L(z,u)+dV_z(F(z,u))\}.
\]

For history geometry a possible running cost might combine process depth and a frontier penalty, for example

\[
L(z,u)=1+\lambda I(z),
\]

or impose a frontier bound as a constraint rather than scalarizing the Pareto problem.

Nothing in the current repository proves that the Sonnet wall trees possess such a limit.  Establishing one requires a controlled scaling family, convergence notion, and consistency/stability argument.

---

## 9. Relation to canonical observer ODEs

The canonicalization line has a deliberately different semantics:

```text
local canonicalization
    -> differentiated normalization
    -> induced observer ODE
    -> canonical lifted path
```

The observer ODE is **not** a future-aware optimizer and must not be redefined as one.

A later theorem could ask whether, in a special class of problems, the canonical observer direction happens to coincide with a characteristic or optimal direction of a history-planning value function.  That would be a nontrivial connection between local representation kinematics and global planning.  It is not assumed here.

---

## 10. Relation to the process-volume/coarea hypothesis

A separate governed T1 candidate edge studies a bulk/frontier relation

\[
dV = W\,dc
\]

under a declared measure and filtration.  This note should remain downstream of that weaker question.

The planning layer adds choices and optimization:

```text
volume/frontier geometry
    + admissible decisions
    + task stopping semantics
    + usage measure
        -> planning value
```

Conflating these levels would make the theory harder to falsify.

---

## 11. Kill conditions

This continuousization line should be rejected, split, or narrowed if:

1. exact finite wall-tree families do not admit any stable continuous limit under a meaningful scaling regime;
2. reconvergence/DAG effects are essential enough that a real-tree model loses the very space savings history geometry is meant to measure;
3. continuous entropy/covering quantities fail to predict or bound finite frontier behavior under refinement;
4. Bellman/HJB scalarization destroys the observed Pareto distinction between time, peak width, volume, worst depth, and decoder cost;
5. macro-action/objectification search cannot be separated from problem-specific solver design;
6. an alleged observer/HJB connection requires redefining the observer connection as an optimizer rather than proving an independent coincidence.

---

## 12. Concrete next experiment

Do not start from a generic HJB solver.

Instead construct a one-parameter family of solved A/M contact-planning problems with increasingly fine contact/wall resolution but fixed task semantics where possible.  For each member record:

1. exact admissible wall grammar;
2. exact task quotient;
3. optimal finite Bellman value;
4. frontier profile and cumulative boundary volume;
5. an embedding of task states into a common continuous parameter space;
6. convergence or non-convergence of rescaled value/frontier functions.

Only if a stable limit appears should an HJB/eikonal candidate be derived from the discrete recursion.

---

## 13. Governance

```text
Epistemic maturity: T0
Role: extraction candidate
Theory Map Change: none
Experimental/Public API pressure: none
```

Do not add generic classes or public names for real history trees, stopping surfaces, process spacetime, continuous Huffman geometry, or HJB planning from this note.  The immediate purpose is to make the next falsifiable experiment precise while preserving the semantics of the already validated finite Sonnet line.

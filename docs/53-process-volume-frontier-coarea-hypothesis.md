# Process volume, frontier measure, and clock — a coarea hypothesis

**Theory edge:** TE-0001  
**Status:** T1 — Precise Conjecture  
**Role:** foundational candidate  
**Evidence provenance:** discrete history/Huffman calibrations + classical one-degree-of-freedom Hamiltonian calibration  
**Code/API status:** no generic implementation; no Experimental/Public API pressure  
**Theory Map effect:** candidate `connect` edge between H3 (entropy/intrinsic complexity) and H4 (analysis of variation); Core Theory unchanged

This record is intentionally narrow. It does **not** identify energy with computational complexity, action with machine memory, or a logarithm of volume with thermodynamic entropy. It asks whether the repository's discrete bulk/frontier distinction and a classical continuous coarea/action identity are instances of a reusable process-geometric pattern once the measure and filtration are declared.

---

## 1. Source pressure

### 1.1 Discrete history geometry

For a finite prefix/history presentation, let `B_n` be the live or distinguishable frontier at depth `n` and

\[
W(n)=|B_n|.
\]

A corresponding cumulative history volume is

\[
V(N)=\sum_{n\le N}W(n),
\]

so that

\[
\Delta V(N)=W(N).
\]

The repository already records depth as a time-like *representation* coordinate and frontier width as a space-like/boundary quantity, while explicitly refusing to identify either with a machine resource bound without additional assumptions.

### 1.2 Dimensionful pendulum calibration

For the physical simple pendulum, phase-space area below a libration energy is an action variable

\[
\Omega(E)=\oint p\,d\theta,
\]

with dimension energy times time. Classical one-degree-of-freedom Hamiltonian mechanics gives

\[
\boxed{\frac{d\Omega}{dE}=T(E)},
\]

where `T(E)` is the orbit period. The research calibration `tests/research/test_pendulum_process_volume_complexity.py` records this identity and the separatrix boundary where the bulk action remains finite while the period diverges.

The formal resemblance

\[
\Delta V=W
\qquad\leftrightarrow\qquad
\frac{d\Omega}{dE}=T
\]

is the pressure for this record. The resemblance alone is not the claim.

---

## 2. Candidate edge

### Source

**H3 — entropy / intrinsic complexity.** Boundary growth, coding depth, distinguishability growth, and representation lower-bound questions.

### Target

**H4 — analysis of variation.** Measures/differentials when justified, process clocks, flows, observer paths, and global analytic structure.

### Proposed construction

Let a process or process presentation carry:

1. a declared measurable carrier `(P, mu)`;
2. a declared filtration/cost/scale
   \[
   c:P\to\mathbb R;
   \]
3. sufficient regularity to form sublevel volumes
   \[
   V(a)=\mu\{x\in P:c(x)\le a\}.
   \]

Where the derivative or an appropriate Radon--Nikodym/coarea density exists, define the **frontier density**

\[
W(a)=\frac{dV}{da}.
\]

The T1 question is:

> For what classes of Process Geometry presentations does the shell/frontier density induced by a declared measure and filtration agree, under a stated discrete/continuous correspondence, with the task/history boundary complexity required to continue the process? When the process also carries a marked clock differential, under what additional hypotheses can the shell measure be expressed as an integral of that clock over the corresponding process leaf?

No generic equality is asserted outside a declared class.

---

## 3. Classical and executable calibrations

### 3.1 Finite prefix trees

Given the counting measure on prefix states and integer depth filtration,

\[
V(N)=\sum_{n\le N}|B_n|,
\qquad
\Delta V(N)=|B_N|.
\]

This is exact and discrete. `BoundaryProfile` and the Sonnet Huffman/history experiments are concrete shadows of this structure.

### 3.2 Simple pendulum

For one librating degree of freedom, choose the symplectic area measure and energy filtration. Then

\[
V(E)=\Omega(E)
\]

and

\[
W(E)=T(E).
\]

The equality follows from classical action-angle/Hamilton--Jacobi theory. What is project-specific is treating it as a dimensional calibration for the same bulk/frontier vocabulary used in finite history geometry.

### 3.3 Separatrix red team

As the pendulum approaches its libration separatrix,

\[
\Omega(E)\to\Omega_{\rm sep}<\infty,
\qquad
T(E)\to\infty.
\]

Therefore this hypothesis must **not** collapse bulk complexity and frontier or time complexity into one scalar. A useful process-volume theory must retain at least their derivative/filtration relation and permit finite bulk with divergent frontier density.

---

## 4. Dimensional interpretation

The pendulum introduces a distinction that finite coding examples cannot supply. If the filtration has energy dimension and the frontier has time dimension, then

\[
[V]=[E][T]=\text{action}.
\]

A dimensionless count-like quantity can be formed only after choosing a declared reference action/cell `A_*`, for example

\[
N=V/A_*.
\]

Only then are logarithmic quantities such as

\[
\log N
\]

information-like on dimensional grounds.

**Non-claim:** the theory does not choose a universal `A_*`, does not require a quantum cell, and does not call `log N` thermodynamic entropy without additional statistical semantics.

---

## 5. Relation to history/Huffman planning

The finite Sonnet line already distinguishes root-to-stop depth, frontier width, boundary volume, expected depth under a usage measure, and executable admissibility of a decision tree.

A possible continuous-planning extension would replace a discrete prefix tree by a measured real tree or another continuous history carrier, and a finite Bellman recursion by an optimal-control limit. That extension remains a Sonnet extraction candidate. It is **not part of TE-0001** and this record does not assert an HJB equation or identify a canonical observer ODE with an optimizer.

---

## 6. Information contract

### Preserves / records

For a declared `(P,mu,c)`:

- cumulative sublevel process volume `V`;
- shell/frontier density `W` where defined;
- transformation behavior under admitted reparameterizations of `c` and `mu`;
- in calibrated cases, the relation between shell measure and a process clock.

### Does not determine

- a canonical filtration;
- a canonical measure;
- a machine-model time or memory complexity;
- an entropy without a declared normalization/measure;
- a planning policy;
- an observer metric or connection.

---

## 7. Controlled vocabulary

### `process volume`

Used only relative to a declared measure on a declared process/presentation carrier. No intrinsicness claim is made.

### `frontier measure` / `frontier density`

Used for a derivative, difference, coarea density, or boundary measure relative to the declared filtration. It is not automatically machine space complexity.

### `clock`

Means a marked differential or integrated process parameter whose normalization is explicitly stated. The pendulum period is one calibrated example.

### `coarea hypothesis`

Names the research question that bulk and frontier descriptions may be related by a reusable measure/filtration construction. It does not claim a new coarea theorem beyond classical measure/differential geometry.

---

## 8. Kill conditions

The current formulation must be rejected, split, or narrowed if any of the following survives careful audit:

1. **Filtration non-naturality becomes fatal.** Two equally admissible filtrations produce frontier quantities with no declared transformation law or task-semantic comparison.
2. **Measure non-naturality becomes fatal.** Equally admissible measures produce incompatible volume/frontier orderings and no application semantics selects among them.
3. **Clock correspondence is one-dimensional only.** Independent continuous processes show that shell measure and process-clock data have no reusable relationship outside one-degree-of-freedom integrable mechanics.
4. **Discrete/continuous mismatch.** A controlled refinement limit of exact history trees fails to converge, even weakly or after normalization, to the proposed continuous volume/frontier quantities.
5. **Representation failure.** Presentations declared equivalent for the task yield incompatible `V/W` data not accounted for by an explicit density or coordinate transformation.
6. **Entropy overclaim.** Any proposed information interpretation depends on an unstated reference cell, probability measure, or partition.
7. **Dominated vocabulary.** Standard coarea/action/entropy language already captures every reusable distinction, leaving no Process Geometry-specific edge beyond problem-local analogy.

---

## 9. Promotion criteria

### T1 -> T2

Require all of:

1. a second continuous positive calibration independent of the pendulum and not merely another one-degree-of-freedom potential with the same action-angle ontology;
2. one explicit negative/nonintegrable/dissipative or stochastic boundary where the stronger clock interpretation fails or changes form;
3. one controlled bridge from a discrete history geometry to a continuous measured carrier, with the transformation of bulk/frontier quantities made explicit;
4. a clear equivalence notion for admissible reparameterizations of measure and filtration.

### T2 -> T3

Would require an abstract theorem, functorial/naturality statement, obstruction result, or universal property independent of the motivating pendulum/Huffman examples.

---

## 10. Theory Map effect

```text
operation: connect
maturity: T1
role: foundational candidate
source: H3 entropy / intrinsic complexity
target: H4 analysis of variation
Core Theory: unchanged
```

The candidate edge should be drawn, if at all, as dashed/research-only until T2. It does not replace the existing H3 or H4 nodes and does not imply that every process admits a useful volume, filtration, differential, or clock.

---

## 11. Software pressure

None at present.

Do **not** introduce public or experimental abstractions named:

```text
ProcessSpacetime
ProcessComplexityMetric
ComplexityEnergy
ProcessEntropy
ProcessVolume
FrontierMeasure
ContinuousHuffmanTree
StoppingSurface
```

solely because of this record. Concrete research helpers may remain local to the calibrating tests/Sonnets until independent domains force a smaller reusable software contract.

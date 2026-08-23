# Myhill–Nerode and the Topological Threshold

**Status:** exact discrete calibration plus a refinement of the Process Geometry research program; no new public API is proposed.

## 0. Why this note exists

`42-process-geometry-from-distinguishability.md` proposed the broad research chain

\[
\text{Process}
\to
\text{Distinguishability}
\to
\text{Topology}
\to
\text{Entropy / Complexity}
\to
\text{Presentation}.
\]

That chain captures an important direction, but it is too linear if read literally.

The Myhill–Nerode theorem shows that in an exact finite/discrete setting, **future distinguishability can already determine the unique minimal task-sufficient presentation before topology or entropy is introduced**. Topology becomes necessary when the research question changes from exact extensional equivalence to locality, finite observational margin, robustness, limits, continuity, and asymptotic distinguishability.

A more accurate first-principles picture is therefore

```text
Process / histories
        |
        v
future or observer distinguishability
        |
        +------------------------------+
        |                              |
        v                              v
continuation-stable equivalence        resource-indexed neighborhoods
        |                              |
        v                              v
exact quotient                         topology / local structure
        |                              |
        v                              +--> continuity / boundary / compactness
minimal presentation                  +--> covers / homotopy / quotient topology
                                       +--> topological dynamics / entropy
                                       +--> stronger uniform/metric structure
                                       +--> differential structure when justified
```

This note establishes the left branch with Myhill–Nerode and asks exactly what is required, and what is gained, when the right branch crosses the **topological threshold**.

---

## 1. Myhill–Nerode: an exact Process Geometry calibration

Let \(\Sigma\) be a finite alphabet and

\[
L\subseteq \Sigma^*
\]

be a language.

Interpret a word

\[
x\in\Sigma^*
\]

as a finite process history. The primitive process is continuation by right concatenation:

\[
x\xrightarrow{z}xz.
\]

The declared task is acceptance in \(L\).

Two histories are future-indistinguishable when no admissible continuation can separate them:

\[
x\sim_L y
\quad\Longleftrightarrow\quad
\forall z\in\Sigma^*,
\;
(xz\in L \iff yz\in L).
\]

This is exactly the process/task pattern

\[
h_1\sim_Q h_2
\iff
\text{all task-relevant continuations agree}.
\]

The relation \(\sim_L\) is a right congruence:

\[
x\sim_L y
\Longrightarrow
xz\sim_L yz
\qquad
\forall z\in\Sigma^*.
\]

That compatibility is essential. An arbitrary equivalence relation can compress histories; a continuation-stable equivalence lets the quotient inherit a well-defined process.

The quotient

\[
\Sigma^*/{\sim_L}
\]

therefore carries transitions

\[
[x]\xrightarrow{a}[xa],
\qquad a\in\Sigma.
\]

The accepting classes are those containing words in \(L\).

The Myhill–Nerode theorem then states:

> \(L\) is regular if and only if \(\sim_L\) has finite index. When the index is finite, its equivalence classes are precisely the states of the unique minimal deterministic finite automaton for \(L\), up to isomorphism.

Thus, for this process class,

\[
\boxed{
\text{future distinguishability}
\to
\text{continuation-stable quotient}
\to
\text{minimal presentation}
}
\]

is not a heuristic. It is a theorem.

### 1.1 What it teaches Process Geometry

The important lesson is stronger than “automata minimization resembles a task quotient.” It identifies three structural requirements that should survive generalization:

1. **Task extensionality.** Histories are identified by every future experiment relevant to the task, not by syntactic similarity.
2. **Process compatibility.** The equivalence is stable under admissible continuation, so process semantics descends to the quotient.
3. **Minimality by distinguishability.** Every pair of distinct quotient classes has a future witness that distinguishes them; no smaller deterministic task-sufficient presentation can exist.

The third point is especially important. The quotient is not merely safe compression. It is the **coarsest process-compatible quotient that remains task complete**.

### 1.2 A candidate general pattern

For a general process \(P\) with histories \(\mathcal H(P)\) and task \(Q\), one can ask for a relation

\[
h_1\equiv_Q h_2
\]

such that:

- all allowed task experiments give the same answer on \(h_1,h_2\);
- every admissible continuation preserves equivalence;
- inequivalent classes possess a distinguishing continuation or experiment.

When these hold, the Myhill–Nerode construction suggests a canonical target:

\[
\mathcal H(P)/{\equiv_Q}.
\]

Whether such a quotient exists, is finite, or is computable is domain-dependent. But the theorem gives the finite discrete research program a precise calibration and a stringent minimality target.

---

## 2. Why topology is not needed yet

The Myhill–Nerode quotient only asks an exact binary question:

\[
\text{Can some continuation distinguish }x\text{ from }y?
\]

There is no notion of “slightly distinguishable,” “stable under perturbation,” “approaching,” or “near a decision boundary.” Exact extensional equivalence plus continuation compatibility is sufficient.

This is useful discipline for Process Geometry:

> Do not introduce topology merely because a quotient exists.

Topology enters when the observer or process supplies a **family of finite-resolution/local distinctions** whose refinements matter.

Examples include:

- observation to tolerance \(\varepsilon\);
- finite time/window depth \(T\);
- bounded query or experiment budgets;
- numerical perturbations of state or parameters;
- increasingly precise sensor histories;
- local continuation families;
- robustness of a task decision under nearby histories.

These structures produce neighborhoods rather than one final equivalence relation.

---

## 3. What topology requires

Let \(X\) denote the carrier under study: it may be raw states, histories, or an exact task quotient. Suppose the observer structure proposes, for each \(x\in X\), a collection of candidate neighborhoods

\[
\mathcal N_O(x).
\]

To deserve a topology, these neighborhoods need more than informal similarity. At minimum they must support the standard local refinement logic of a neighborhood basis.

### 3.1 Point inclusion

Every proposed neighborhood of \(x\) must actually contain \(x\):

\[
U\in\mathcal N_O(x)
\Longrightarrow
x\in U.
\]

Operationally, a state must be observationally compatible with itself at every admissible resource level.

### 3.2 Directed finite refinement

If two observational neighborhoods are valid around the same point, there must be a finer admissible observation contained in both:

\[
U,V\in\mathcal N_O(x)
\Longrightarrow
\exists W\in\mathcal N_O(x)
\text{ with }
W\subseteq U\cap V.
\]

This says observational precision can reconcile finitely many local requirements rather than producing unrelated notions of nearness.

### 3.3 Local inheritance

If \(y\) lies in a neighborhood \(U\) of \(x\), there should be a sufficiently fine neighborhood of \(y\) that remains inside \(U\):

\[
y\in U
\Longrightarrow
\exists V\in\mathcal N_O(y)
\text{ with }
V\subseteq U,
\]

in the appropriate basis formulation.

This is what turns local recognizability into open-set structure rather than a collection of isolated tolerance tests.

### 3.4 Resource refinement

When neighborhoods come from observation budgets such as \((T,\varepsilon)\), stronger observation should refine weaker observation in a controlled way. Schematically,

\[
r_1\preceq r_2
\Longrightarrow
U_{r_2}(x)\subseteq U_{r_1}(x).
\]

A single fixed tolerance relation need not be transitive and need not itself define a quotient. The entire directed family of tolerances may nevertheless generate a topology or, more naturally in some cases, a uniformity or quasi-uniformity.

### 3.5 Compatibility with exact quotients

If one first forms an exact task quotient

\[
q:X\to X/{\sim_Q},
\]

then observer neighborhoods intended to descend to the quotient should respect the equivalence classes, or the quotient should carry the corresponding quotient topology.

This keeps “exactly the same task state” separate from “topologically nearby task states.”

### 3.6 Compatibility with process evolution

This is the specifically **process-geometric** condition.

If an admissible evolution or continuation acts as

\[
F_t:X\to X,
\]

then the induced topology should normally make the relevant \(F_t\) continuous, or should make explicit why continuity fails.

Continuity says that a finite distinction at the future can be pulled back to a finite distinction now:

\[
F_t^{-1}(U)\text{ open whenever }U\text{ is open}.
\]

Equivalently, sufficiently indistinguishable initial states do not become observationally discontinuous under an infinitesimal change of input without that instability being visible as a real feature of the process.

Without some compatibility between dynamics and local structure, we may have an observer topology on a set, but not yet a useful topology **of the process**.

---

## 4. What topology does *not* require

The following are stronger properties, not entry conditions.

### 4.1 Hausdorffness is not required

Partial observation may leave two distinct states impossible to separate by disjoint robust observations. The resulting non-Hausdorff structure may be exactly the correct geometry of the observer.

This suggests reading separation axioms operationally.

- **\(T_0\)**: distinct states differ by at least one observable open property.
- **\(T_1\)**: each state can be excluded locally from the other.
- **Hausdorff**: distinct states admit disjoint robust observational neighborhoods.

The failure of these axioms can measure genuine observational deficiency rather than mathematical pathology.

The Kolmogorov \(T_0\) quotient is particularly suggestive: topologically indistinguishable points are identified. This is another classical instance of “identify exactly what no allowed observation can distinguish,” although it is not the same construction as Myhill–Nerode future equivalence.

### 4.2 A metric is not required

Topology answers which distinctions are local and robust. It does not assign a numerical distance between them.

If the observer family carries a coherent quantitative resolution, one may obtain a uniformity, quasi-uniformity, pseudometric, or metric later. That extra structure is what supports quantitative statements involving \(\varepsilon\), rates, conditioning, or completion.

### 4.3 Differential structure is not required

A topology gives neighborhoods and continuity, not tangent vectors or derivatives. A differentiable process geometry requires additional local regularity and compatible charts or intrinsic notions of variation.

This is why the Analysis/Observer Connection program should remain a later layer.

---

## 5. What topology buys

Crossing the topological threshold adds several capabilities that exact quotienting alone does not provide.

### 5.1 Robustness and boundary

For a task region \(A\subseteq X\), topology distinguishes

\[
\operatorname{int}(A),
\qquad
\partial A,
\qquad
\overline A.
\]

This gives precise language for:

- states whose task outcome is stable under small observational variation;
- threshold states where arbitrarily small changes can alter the outcome;
- limit states approachable by task-valid histories.

This is a natural bridge from exact correctness to numerical and physical robustness.

### 5.2 Convergence and limiting processes

Topology permits a coordinate-independent notion of convergence. Sequences, and more generally nets/filters, can represent increasingly refined histories or observer estimates.

This makes it possible to ask whether:

- finite approximations converge to a process object;
- increasingly precise presentations stabilize;
- a singular regime lies in the closure of regular regimes;
- a continuation procedure has a meaningful limit.

Completion itself requires stronger uniform/metric structure, but topology supplies the first notion of limiting behavior.

### 5.3 Continuity as semantic stability

A map between process spaces or presentations can now be judged by whether it preserves local distinctions:

\[
f:X\to Y
\]

is continuous when observable distinctions in \(Y\) pull back to observable distinctions in \(X\).

This gives a stronger semantic criterion for presentation maps and model transformations than bare set-theoretic correspondence.

Topological conjugacy then supplies a presentation-independent notion of “the same dynamics”:

\[
h\circ f = g\circ h
\]

with \(h\) a homeomorphism.

This is an exact example of geometry providing invariants beyond coordinates.

### 5.4 Connectedness and decomposition

Connected components identify regions that cannot be split into disjoint robust observational pieces. This can distinguish genuine phase/components from arbitrary coordinate partitions.

Path-connectedness, when available, introduces continuous families of process states and makes homotopy questions meaningful.

### 5.5 Compactness and finite observational control

Compactness turns arbitrary open-cover control into finite subcover control.

Operationally, it can support statements of the form:

> a global process property that is locally certified everywhere can be controlled by finitely many observational regimes.

The exact computational consequence depends on the domain; compactness should not be equated automatically with algorithmic finiteness. But it is a first local-to-global finiteness principle.

### 5.6 Quotients, coverings, and universal covers

Topology makes quotient maps, covering maps, homotopy classes, and fundamental groups available.

This point matters directly to the broader AEG program. A classical universal covering space is not automatic: standard existence results require hypotheses such as connectedness, local path connectedness, and semilocal simple connectedness (or more sophisticated generalized covering theories when these fail).

Therefore the arithmetic-universality program must eventually answer two separate questions:

1. which Process Geometries actually admit a suitable universal cover;
2. whether the resulting universal/standard objects belong to arithmetic-generated families.

The second conjecture cannot silently assume the first.

### 5.7 An open-set language for local-to-global structure

Once open sets exist, one can attach data to regions

\[
U\mapsto \mathcal F(U)
\]

and ask whether compatible local data glue globally.

This is the point at which presheaf/sheaf language may eventually become relevant for local observers, local presentations, or local process laws.

Topology supplies the domain of local patches; it does **not** automatically supply a sheaf. The gluing law remains additional structure to be discovered and tested.

---

## 6. Topology and entropy: the next threshold

Topology alone does not produce topological entropy. One also needs dynamics and an appropriate finiteness/control framework.

For a continuous map

\[
f:X\to X,
\]

an open cover \(\mathcal U\) can be refined along time:

\[
\mathcal U^{(n)}
=
\mathcal U
\vee f^{-1}\mathcal U
\vee\cdots\vee f^{-(n-1)}\mathcal U.
\]

The growth of the minimum number of open sets required to distinguish orbit histories is the classical route to topological entropy, especially clean on compact spaces.

Process Geometry reads this as:

> topology supplies robust local distinctions; dynamics propagates them through time; entropy measures the asymptotic growth of distinctions that remain necessary.

Thus the conceptual order is

\[
\boxed{
\text{local distinguishability}
\to
\text{topology}
\to
\text{continuous process action}
\to
\text{growth of refined distinctions}
\to
\text{topological entropy}.
}
\]

This is stronger and more precise than saying merely that “distinguishability implies entropy.”

A quantitative separated/spanning-set formulation may instead require metric or uniform structure. These alternatives should be compared rather than conflated.

---

## 7. Topology and presentation complexity

Myhill–Nerode gives an exact finite-state lower bound:

\[
\#\text{states of any DFA for }L
\ge
\#(\Sigma^*/{\sim_L}),
\]

with equality achieved by the minimal DFA.

Topology suggests a more general but harder analogue. At finite observational resolution, suppose a process requires \(N(n)\) robustly distinguishable orbit/history classes at depth \(n\). Then any task-sufficient presentation must contain enough distinguishable representational capacity to preserve those classes.

The research program is to turn this intuition into exact lower bounds in progressively richer categories:

```text
Myhill–Nerode          exact number of discrete task states
source coding          exact/asymptotic code-length bounds
symbolic dynamics      growth of distinguishable words/orbits
open-cover entropy     coordinate-free asymptotic distinction growth
metric entropy         probability-weighted distinction growth
continuous geometry    still-open links to computation and materialization cost
```

The goal is not to call all of these the same complexity. It is to determine when the intrinsic distinction structure controls a lower bound for concrete presentation cost.

---

## 8. A revised hierarchy for Process Geometry

The emerging hierarchy should therefore be stated by required structure rather than by metaphor.

### Level 0 — process and continuation

Primitive operations, histories, admissible continuations, relations.

### Level 1 — exact distinguishability quotient

Task/future equivalence compatible with continuation.

Canonical calibration: Myhill–Nerode.

Possible output: minimal exact process presentation.

### Level 2 — topology

Resource-indexed local distinguishability satisfying neighborhood/refinement conditions, with process evolution compatible through continuity.

New outputs: robustness, boundaries, convergence, compactness, connectedness, quotient/covering/homotopy structure.

### Level 3 — uniform / metric structure

Quantitative observational resolution and coherent comparison of neighborhoods.

New outputs: distance, rates, conditioning, separated/spanning sets, quantitative stability, completion where appropriate.

### Level 4 — entropy / intrinsic complexity

Growth of distinctions under process evolution, topological or measure-relative as appropriate.

New output: asymptotic lower-bound candidates for task-sufficient materialization.

The ordering between Levels 3 and 4 is not absolute: open-cover topological entropy needs topology and dynamics but no metric, while metric formulations use stronger quantitative structure.

### Level 5 — differential geometry

Additional local regularity permits tangent directions, derivatives, ODE-defined observer paths, connections, and curvature.

No level should be imported merely because the next level is mathematically familiar.

---

## 9. Consequences for the name “Process Geometry”

This calibration strengthens the first-principles case for the name while narrowing its meaning.

`Geometry` should not mean “every process is secretly a manifold.” It means that process/observer distinguishability can generate a hierarchy of intrinsic relational structures:

\[
\text{quotient}
\to
\text{locality/topology}
\to
\text{uniform/metric structure}
\to
\text{entropy}
\to
\text{differential structure},
\]

when the necessary hypotheses are present.

The Myhill–Nerode case shows that the theory already has a rigorous zero-dimensional/discrete anchor. The topological threshold explains what extra structure is required before words such as continuity, boundary, compactness, covering, and topological entropy become legitimate.

This suggests a conservative formulation:

> **Process Geometry studies the intrinsic structures forced by process continuation and observer-relative distinguishability, and the task-sufficient presentations that realize those structures. Topology is the first genuinely local layer, not an axiom of every process.**

---

## 10. Near-term calibration tasks

The theory can now be tested with a small exact ladder before any new public API is introduced.

1. **Myhill–Nerode executable calibration.** Reconstruct a minimal DFA solely from continuation distinguishability and verify minimality against a standard automaton implementation.
2. **Non-\(T_0\) observer calibration.** Construct a process with distinct states that all permitted observations fail to separate, then verify that the observer topology collapses exactly those distinctions under its \(T_0\) reflection.
3. **Non-Hausdorff but meaningful calibration.** Find a partial-observation process where non-Hausdorffness records genuine unresolved state identity rather than a bug.
4. **Topology without metric calibration.** Use a natural non-metrically-specified observer family to show why topology is the correct first local structure.
5. **Continuity red team.** Give an observer neighborhood system that satisfies topological basis axioms but makes process evolution discontinuous; this should demonstrate why topology alone is insufficient for a process-geometric model.
6. **Entropy calibration.** On a finite symbolic process, compare distinguishable-history growth, open-cover/topological entropy, and minimal presentation growth without assuming they are identical.

Only after these calibrations survive should a generic `ProcessGeometry`, `ObserverTopology`, or related API be considered for Experimental incubation.
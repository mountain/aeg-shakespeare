# Objectification, Semantic Compression, and Rank Lowering

**Status:** foundational research note; extension of the Process Geometry program, not a public API contract.

## 0. Thesis

The distinguishability program explains how a process may safely forget differences. It does not, by itself, explain one of the strongest lessons supplied by the arithmetic tower:

> A successful semantic compression can become a new object; that object can then act as a new primitive and freely generate a new process language.

But this rank raising is legitimate only under a second, equally important condition:

> **Every legal higher-rank composition must admit a coherent semantic interpretation back into lower-rank process semantics.**

The resulting cycle is

\[
\boxed{
\text{free lower-rank process}
\to
\text{semantic compression}
\to
\text{objectification}
\to
\text{new primitive}
\to
\text{free higher-rank composition}
\xrightarrow{\text{rank lowering}}
\text{lower-rank semantics}.
}
\]

The point is not merely that a high-rank symbol can be expanded. The entire high-rank composition law must be semantically grounded below.

This supplies the missing **vertical axis** of Process Geometry. The horizontal axis remains observer-relative distinguishability, quotient, topology, entropy, metric, and differential structure within a fixed rank.

---

## 1. The vertical process tower

Let \(\Sigma_r\) be the primitive vocabulary at process rank \(r\). A free or weakly free construction produces process histories

\[
\mathcal H_r \simeq \mathsf F_r(\Sigma_r),
\]

where \(\mathsf F_r\) may be a term algebra, free category, word tree, path space, free group-like construction, or another domain-appropriate generator.

A task or observer supplies a semantic relation

\[
h_1\sim_{Q_r}h_2,
\]

and hence a quotient or semantic completion

\[
\mathcal C_r
=
\mathcal H_r/{\sim_{Q_r}}.
\]

Some stable semantic classes may become candidates for objectification:

\[
\operatorname{Obj}_r:
\mathcal S_r\subseteq\mathcal C_r
\longrightarrow
\Sigma_{r+1}.
\]

Then a new free process language appears:

\[
\mathcal H_{r+1}
\simeq
\mathsf F_{r+1}(\Sigma_{r+1}).
\]

The essential new structure is a **rank-lowering interpretation**

\[
\boxed{
\llbracket - \rrbracket_{r+1\downarrow r}:
\mathcal H_{r+1}
\longrightarrow
\widehat{\mathcal C}_r,
}
\]

where \(\widehat{\mathcal C}_r\) is a lower-rank semantic domain large enough to interpret legal higher-rank compositions. It may be the original quotient, a closure under derived operations, a completion, or another explicitly declared semantic target.

Without this interpretation, rank raising is syntactic rather than semantic.

---

## 2. Objectification is more than compression

Semantic compression identifies lower-rank histories that no longer need to remain distinct:

\[
\mathcal H_r
\to
\mathcal C_r.
\]

Objectification performs a second step:

\[
\mathcal C_r
\to
\Sigma_{r+1}.
\]

It turns some semantic class into a reusable generator.

The difference is fundamental.

A quotient says:

> these lower-rank histories may be treated as the same for the declared semantics.

Objectification says:

> this stabilized meaning may now participate as an atomic unit in a new generative language.

Thus objectification changes the process ontology itself:

\[
\Sigma_r
\longrightarrow
\Sigma_{r+1}.
\]

The primitive vocabulary is not fixed once and for all.

---

## 3. The decisive constraint: composition must lower

Suppose a new high-rank primitive \(T\in\Sigma_{r+1}\) objectifies a lower-rank semantic class \([h]\in\mathcal C_r\). It is not enough to know

\[
\llbracket T\rrbracket_{r+1\downarrow r}
\sim_{Q_r}
h.
\]

A high-rank language is useful precisely because \(T\) can be composed with other high-rank objects:

\[
T\circ T,
\qquad
S\circ T,
\qquad
T\circ S,
\qquad
\Phi(T,S),
\ldots
\]

Therefore the rank-lowering interpretation must extend from generators to **all legal high-rank terms**.

Schematically, if \(\circ_{r+1}\) is a high-rank composition and \(\star_r\) is its lower-rank semantic realization, then

\[
\boxed{
\llbracket A\circ_{r+1}B\rrbracket_{r+1\downarrow r}
\simeq
\llbracket A\rrbracket_{r+1\downarrow r}
\star_r
\llbracket B\rrbracket_{r+1\downarrow r}.
}
\]

The equality sign may be literal equality, equality in a quotient, task equivalence, isomorphism, homotopy, numerical tolerance, or another declared semantic relation. The category of equality is part of the contract.

This is the core constraint:

> **rank raising must preserve compositional interpretability.**

If generators lower individually but their legal compositions do not, the higher-rank ontology is not semantically grounded.

---

## 4. Relations must lower as well

Suppose the high-rank presentation asserts a relation

\[
A \equiv_{r+1} B.
\]

A sound rank-lowering interpretation should send that relation to valid lower-rank semantics:

\[
\llbracket A\rrbracket_{r+1\downarrow r}
\sim_{Q_r}
\llbracket B\rrbracket_{r+1\downarrow r}.
\]

Thus lowering must respect not only composition but also the relations that define the high-rank process language.

A candidate high-rank presentation therefore carries at least three semantic obligations:

1. **generator meaning** — every primitive has a lower-rank interpretation;
2. **composition soundness** — legal high-rank compositions lower coherently;
3. **relation soundness** — high-rank equalities or rewrite laws remain valid when interpreted below.

These are stronger than ordinary naming or memoization.

---

## 5. Rank lowering is not necessarily an inverse

It is tempting to require

\[
\llbracket\operatorname{Obj}_r([h])\rrbracket=h.
\]

That is usually too literal.

Objectification may intentionally forget lower-rank history accidents. The correct requirement is generally semantic:

\[
\boxed{
\llbracket\operatorname{Obj}_r([h])\rrbracket
\sim_{Q_r}
h.
}
\]

The lowering map may return a canonical representative, an equivalence class, a derived process, or a lower-rank completion rather than the original trace.

Conversely, merely returning some representative is too weak if composition is not preserved.

The likely mathematical structure may resemble a semantics-preserving homomorphism, functor, lax functor, interpretation, adjunction, elaboration, or compiler lowering. Which of these is correct should be discovered from independent domains rather than imposed now.

---

## 6. Conservative and non-conservative rank raising

A useful distinction is whether the high-rank language introduces genuinely new semantics.

### Conservative objectification

Every high-rank term has a lower-rank interpretation and no new semantic fact is created merely by moving upward:

\[
\mathcal H_{r+1}
\xrightarrow{\llbracket-\rrbracket}
\widehat{\mathcal C}_r.
\]

The higher rank changes representation, search, law visibility, and generative convenience, but remains semantically grounded in the lower rank.

### Non-conservative extension

A higher-rank system may intentionally add new primitives or completion operations whose semantics cannot be expressed in the original lower-rank domain without extension.

Then the lower target must be enlarged explicitly:

\[
\mathcal C_r
\hookrightarrow
\widehat{\mathcal C}_r.
\]

This should be recorded as an ontology extension rather than hidden inside the word “objectification.”

The distinction is important for auditability.

---

## 7. What qualifies a semantic class for objectification?

The following are candidate gates.

### 7.1 Semantic stability

The class is meaningful under a declared task or observer semantics.

### 7.2 Continuation compatibility

Its identity remains stable under the continuations for which it will be reused. Myhill–Nerode right congruence is the exact finite calibration.

### 7.3 Compositional reuse

The object participates in a higher-rank grammar rather than serving only as a stored label.

### 7.4 Generative novelty

The higher-rank grammar permits meaningful combinations not explicitly enumerated in the histories used to discover the object.

### 7.5 Compositional rank lowering

Every legal higher-rank combination admits coherent lower-rank semantics.

### 7.6 Relation soundness

High-rank laws remain valid when lowered.

### 7.7 Complexity advantage

Objectification yields a declared benefit in description length, search branching, execution, proof structure, reconstruction, or another cost axis.

### 7.8 Boundary evidence

There is a known red team where the candidate object fails to remain stable, compositional, or useful.

---

## 8. Objectification is not a macro, cache, or cluster

A macro abbreviates syntax. A cache stores a result. A cluster groups similar observations. A quotient names an equivalence class.

None of these alone creates a new process rank.

A genuine objectified primitive must support

\[
\boxed{
\text{new composition}
+
\text{stable semantics}
+
\text{compositional lowering}.
}
\]

This gives a falsifiable distinction between ontology growth and implementation convenience.

---

## 9. Free expansion and rank lowering

Two directions should not be conflated.

### Free expansion

At a fixed rank, generators create a space of possible histories:

\[
\Sigma_r
\xrightarrow{\mathsf F_r}
\mathcal H_r.
\]

This is generative.

### Rank lowering

A higher-rank history is interpreted in lower-rank semantics:

\[
\mathcal H_{r+1}
\xrightarrow{\llbracket-\rrbracket_{r+1\downarrow r}}
\widehat{\mathcal C}_r.
\]

This is semantic/elaborative.

The complete vertical cycle is therefore

\[
\boxed{
\Sigma_r
\xrightarrow{\mathsf F_r}
\mathcal H_r
\xrightarrow{\text{semantic compression}}
\mathcal C_r
\xrightarrow{\operatorname{Obj}_r}
\Sigma_{r+1}
\xrightarrow{\mathsf F_{r+1}}
\mathcal H_{r+1}
\xrightarrow{\llbracket-\rrbracket_{r+1\downarrow r}}
\widehat{\mathcal C}_r.
}
\]

This is a stronger and cleaner formulation than calling the downward map simply “free unfolding.”

---

## 10. Relation to universal covering

Free expansion is more primitive than a universal cover.

A generator system may produce a history-resolving object such as a word tree, prefix tree, Cayley graph/tree, path space, or free category. Relations then identify histories.

Only after suitable topology is present, and only under appropriate hypotheses, can such a history-resolving object coincide with or model a classical universal covering space.

Thus

\[
\boxed{
\text{free expansion}
\to
\text{history-resolving space}
\to
\text{universal cover in suitable topological classes}.
}
\]

Rank lowering is a different structure: it connects levels of process ontology, not sheets of one covering space.

---

## 11. The two axes of Process Geometry

The theory now has two independent but coupled directions.

### Vertical axis — ontology growth

\[
\boxed{
\text{free generation}
\to
\text{semantic compression}
\to
\text{objectification}
\to
\text{rank raising}
\to
\text{compositional rank lowering}.
}
\]

This axis asks how the primitive vocabulary itself changes.

### Horizontal axis — distinguishability geometry

At each rank \(r\):

\[
\boxed{
\mathcal H_r
\to
\text{observer/task distinguishability}
\to
\text{exact quotient or topology}
\to
\text{entropy / metric / differential structure where justified}.
}
\]

This axis asks how histories at a fixed ontology level are related and what distinctions are intrinsic.

The axes interact:

- horizontal semantic compression supplies candidates for vertical objectification;
- vertical objectification creates a new generator set;
- the new generator set creates a new free process space;
- that space acquires a new horizontal distinguishability geometry;
- rank lowering lets the new geometry remain semantically auditable against lower-rank processes.

This cycle can repeat.

---

## 12. Presentation revisited

This two-axis view deepens the meaning of `Presentation`.

A presentation may specify:

1. generators treated as primitive;
2. relations among generated histories;
3. task/observer semantics that justify semantic identification;
4. an interpretation or lowering semantics into another presentation/rank;
5. reconstruction or verification obligations;
6. operational costs.

Schematically,

\[
\boxed{
\text{Presentation}
\approx
(\text{generators},\text{relations},\text{semantics},\text{lowering},\text{cost}).
}
\]

This is why presentation search may search over **ontologies**, not merely coordinate systems.

---

## 13. Arithmetic as a model organism

The arithmetic/hyperoperation tower supplied the motivating pattern:

\[
\text{successor/repetition}
\to
\text{addition}
\to
\text{multiplication}
\to
\text{exponentiation}
\to\cdots.
\]

The structural lesson is not that all of these operations are globally reducible to one another without domain qualifications. It is that a repeated lower-rank process can acquire a stable semantic identity, become primitive at a higher rank, and support further composition whose meaning can be interpreted back through lower-rank process laws.

Arithmetic is therefore a model organism for **semantic objectification and rank raising**.

This is distinct from the stronger Arithmetic Geometric Universality conjecture.

### Objectification Universality question

Do broad classes of mathematical, computational, physical, or learned processes repeatedly exhibit

\[
\text{regularity}
\to
\text{semantic compression}
\to
\text{objectification}
\to
\text{new generative rank}
\]

with compositional rank lowering?

### Arithmetic Geometric Universality question

When process geometries admit distinguished universal or standard models, do important Lie-type models arise from arithmetic/hyperoperation-generated geometries?

The first concerns ontology growth. The second concerns geometric classification.

---

## 14. Learning as ontology growth

A learner that discovers only

\[
h_1\sim h_2
\]

has learned a compression.

A stronger learner discovers a stable process class, objectifies it as a new primitive, composes it in new situations, and can lower those new compositions back to previously grounded semantics for verification.

Thus a stronger learning loop is

```text
observe repeated process structure
    -> discover task-stable semantic class
    -> objectify as a new primitive
    -> compose freely at the new rank
    -> lower novel compositions for semantic verification
    -> retain or reject the new object
    -> repeat
```

The decisive evidence of ontology growth is **counterfactual compositional reuse**: the object supports valid new combinations rather than merely compressing histories already seen.

---

## 15. Complexity across ranks

Rank raising introduces a tradeoff rather than an automatic speedup.

A lower-rank history may have cost

\[
C_r(h),
\]

while its objectified use at higher rank has cost

\[
C_{r+1}(T).
\]

But a complete accounting also includes:

- object discovery cost;
- semantic compression cost;
- higher-rank search/branching cost;
- rank-lowering or verification cost;
- loss of lower-rank detail;
- cost of maintaining relations among new primitives;
- benefit from shorter compositions and novel reusable structure.

A rank-aware presentation cost should therefore measure the entire vertical cycle.

---

## 16. Interaction with topology and entropy

Topology remains a horizontal threshold, not the definition of Process Geometry.

Once observer-relative locality exists at ranks \(r\) and \(r+1\), new questions arise:

- Is objectification continuous?
- Is rank lowering continuous?
- Does rank lowering preserve limits or compact families?
- What happens to connected components or homotopy classes under rank raising?
- Does objectification reduce effective distinguishability by internalizing repeated structure?
- Does free higher-rank composition create new distinguishability growth?
- How do topological or metric entropies compare across ranks?

These are genuine geometric questions about ontology change.

No general monotonicity is assumed.

---

## 17. Red-team boundaries

The following are explicitly **not** claimed.

1. Every semantic quotient should be objectified.
2. Every recurring pattern is a semantic object.
3. Naming a macro constitutes rank raising.
4. Caching constitutes objectification.
5. Every objectification is conservative.
6. Rank lowering must reproduce the literal original history.
7. Rank lowering is always an inverse.
8. Lowering a generator individually is sufficient; composition soundness is required.
9. Every high-rank composition has a finite low-rank expansion; semantic interpretation may use a closure or completion.
10. Free expansion is a universal cover.
11. Every process has a unique rank hierarchy.
12. Higher rank is always cheaper.
13. Arithmetic already proves Objectification Universality.
14. Objectification Universality implies Arithmetic Geometric Universality.

---

## 18. Near-term exact calibrations

Before introducing a generic objectification API, the theory should survive several independent calibrations.

### A. Arithmetic rank lowering

Choose a restricted arithmetic domain where repeated lower-rank operations and higher operations have exact compositional interpretation. Make the domain restrictions explicit.

### B. Compiler/IR calibration

Treat a higher-level intermediate representation as an objectified process language and compilation/lowering as compositional semantic preservation. Use this to separate genuine lowering from textual macro expansion.

### C. Automata/state abstraction calibration

Start with Myhill–Nerode-style exact semantic compression, then ask when quotient states can themselves become generators of a higher process rather than merely minimal states.

### D. Rewrite-system calibration

Objectify a confluent lower-rank process pattern and verify that higher-rank rewrite laws lower to valid lower-rank rewrite semantics.

### E. Failure case

Construct a tempting recurring pattern whose atoms can each be expanded but whose higher-rank composition law has no coherent lower-rank interpretation. This should be rejected as false objectification.

Only after such independent pressure should concepts such as `SemanticObject`, `Objectification`, `Rank`, or `Lowering` enter Experimental.

---

## 19. Revised working definition of Process Geometry

The previous distinguishability-based definition should now be widened:

> **Process Geometry studies how process histories are freely generated, semantically identified, objectified into new primitives, and organized into higher process ranks whose compositions remain interpretable at lower ranks; within and between these ranks it studies the intrinsic structures induced by observer-relative distinguishability, including quotients, topology, complexity, and—where justified—metric and differential geometry.**

A shorter operational formulation is:

> **Compress semantics into reusable objects, let those objects generate new process spaces, and preserve meaning through compositional rank lowering. Study the geometry of the distinctions that survive at every level.**

This two-axis picture is currently the strongest first-principles justification for the name **Process Geometry**.
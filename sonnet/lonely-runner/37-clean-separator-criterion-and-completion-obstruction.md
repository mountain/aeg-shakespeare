# Phase 13A — clean-separator criterion and completion obstruction

**Status:** exact finite theory layer implemented.  
**Implementation:** `sonnet/lonely-runner/python/clean_separator_theory.py`.  
**Executable red teams:** `tests/research/test_lonely_runner_clean_separator_theory.py`.  
**Purpose:** turn the Phase-12 zero-refinement phenomenon into a precise decision property before searching for its first failure.

## 1. The object left after canonicalization and task objectification

Phases 11–12 have separated three layers:

```text
canonical process regions
-> observer/task quotient
-> compiled predicate geometry.
```

After the first two steps, let

\[
\mathcal R=\{R_a\}
\]

be the finite exact canonical regions currently relevant to a bounded task, with task map

\[
T:\mathcal R\to\mathcal Y.
\]

Let

\[
\mathcal C=\{c_1,\ldots,c_m\}
\]

be a declared family of process-generated ternary coordinates.  A region need not decide every coordinate.  Its partial signature is

\[
\sigma_a(c_j)\in\{-1,0,+1,\bot\},
\]

where `bot` means that `R_a` does not force one sign of `c_j`.

This is the correct abstraction of the Phase-12 terminal closures: they are exact geometric objects carrying **partial**, not complete, sign information.

---

## 2. Clean separator

For a current region family

\[
S\subseteq\mathcal R,
\]

call coordinate `c` **clean on S** when:

1. `c` is already resolved on every region in `S`:
   \[
   \sigma_a(c)\ne\bot\qquad(a\in S);
   \]
2. at least two signs occur on `S`.

Querying a clean coordinate partitions

\[
S=S_{-}\sqcup S_0\sqcup S_{+}
\]

without refining, splitting, or completing any region.

This isolates exactly what Phase 12B was doing when its measured closure-refinement pressure stayed zero.

---

## 3. Exact recursive criterion

Define `Clean(S)` recursively:

\[
\boxed{
\operatorname{Clean}(S)
\iff
\begin{cases}
\text{true}, & T\text{ is constant on }S,\\[2mm]
\exists c\text{ clean on }S\text{ such that }\\
\qquad\operatorname{Clean}(S_s)\text{ for every nonempty sign branch }s,
& \text{otherwise.}
\end{cases}
}
\]

### Proposition — zero-completion decision criterion

For a finite partial-sign task system `(R,T,C,sigma)`, the following are equivalent:

1. `Clean(R)` holds;
2. there exists a finite exact decision tree for `T` whose every internal query is already resolved on every region reaching that node;
3. the task can be classified using the declared coordinates with zero region completion/refinement.

### Proof

`1 -> 2` follows by recursively choosing the witnessing clean coordinate in the definition and terminating on task-pure subsets.

`2 -> 1` follows by induction from the root of any zero-refinement tree: its root coordinate must be resolved on every root region and must split the mixed task family; each child subtree gives the recursive hypothesis.

`2 <-> 3` is definitional for the current representation grammar: querying a coordinate that is already resolved on every current region only routes existing regions, whereas a query with `bot` on some region requires either splitting/refining that region or replacing the grammar by a richer primitive.

The implementation is an exact memoized recursion over region subsets.  Candidate ordering is only a search heuristic; when one clean root fails, all other possible clean roots are tried before non-cleanseparability is certified.

---

## 4. Why pairwise task separation is insufficient

A tempting weaker condition is:

> every pair of regions carrying different tasks has some coordinate that is resolved on both and has opposite signs.

This does **not** imply clean separability.

The smallest red team has three regions `A,B,C` and three coordinates:

```text
       c0    c1    c2
A       0     ⊥     0
B       1     0     ⊥
C       ⊥     1     1
```

Every cross-task pair is separable:

```text
A/B by c0
B/C by c1
A/C by c2
```

but no coordinate is resolved on all three regions.  Therefore the mixed root family has no clean query at all.

So

\[
\boxed{
\text{pairwise distinguishability}
\not\Rightarrow
\text{zero-completion decision geometry}.
}
\]

This is the first abstract red team showing that the Phase-12 clean property contains real global structure rather than merely restating task sufficiency.

---

## 5. Recursive obstruction certificate

Failure need not be atomic at the root.  A mixed family can have several legal clean root coordinates, while every such choice eventually enters a non-clean child.

The exact solver therefore returns a recursive `CleanObstruction` rather than only `False`.

For an obstructed mixed family `S`, the certificate records:

- every possible clean root coordinate on `S`;
- for each such coordinate, one sign branch that is itself obstructed;
- recursively, the same evidence for that child;
- at an atomic obstruction, a mixed-task family with no clean coordinate at all.

Verification is inductive and independent of the search procedure.

This certificate has a direct interpretation:

> every zero-refinement decision strategy over the declared coordinate grammar is blocked; some execution path must eventually query an unresolved coordinate, introduce a new primitive, or fail to distinguish the task.

That is the finite representation-theoretic object we were missing when speaking loosely about “genuine completion pressure.”

---

## 6. Relation to `F_comp`

The obstruction is deliberately **grammar-relative**.

If a clean tree fails for coordinate family `C`, it does not prove that the physical process itself needs a larger state.  A different composite primitive or a different task quotient can remove the obstruction.

Therefore the appropriate causal interpretation is

```text
canonicalize process
-> objectify task
-> declare current generated predicate grammar C
-> test Clean(R)
     true  -> F_comp = 0 relative to this decision layer
     false -> certified completion pressure relative to C
-> only then search for a minimum refinement / richer primitive.
```

This is much closer to the docs-38/39 rule than the old contact-center criterion, because both process lift freedom and task/certificate provenance have already been removed before completion is diagnosed.

---

## 7. A useful quantitative extension

The Boolean criterion immediately suggests a family of exact complexity functionals on clean trees.

For example, define clean worst depth recursively by

\[
h(S)=
\begin{cases}
0,&T\text{ pure},\\
1+\min_{c\in A(S)}\max_s h(S_s),&\text{if a clean tree exists},
\end{cases}
\]

where `A(S)` is the set of clean coordinates.

Likewise one can minimize tree nodes, weighted decision depth, or a Huffman-style space-time tuple while **forbidding completion**.

If no clean tree exists, these quantities become infinite and the obstruction certificate identifies where a completion-aware optimizer must take over.

This gives a cleaner future decomposition of representation cost:

\[
\boxed{
\text{clean decision cost}
\quad\oplus\quad
\text{completion cost when Clean fails}.
}
\]

---

## 8. Next executable gate

Phase 13B should do two things in this order:

1. translate the five-speed Phase-12 terminal closures at `u5/u1<25/4` into the generic partial-sign system and have the independent exact criterion certify `Clean(R)`;
2. widen the five-speed domain by **critical process boundaries**, not arbitrary decimal increments, until the exact solver returns its first recursive obstruction.

At that first failure, preserve:

```text
obstructed canonical region family
current task labels
all clean root alternatives
recursive failing child for each alternative
first unresolved coordinates that can repair the obstruction.
```

That artifact would be the first defensible post-canonicalization Sonnet candidate for genuine `F_comp`.

`K=13` remains frozen.

## Claim boundary

Phase 13A proves only a finite equivalence about partial-sign decision systems and supplies exact positive/negative certificates.  It does not prove that the five-speed family remains clean beyond the Phase-12 sweep, that a completion obstruction must eventually occur, or that one coordinate grammar is universal.
# Phase 11B0 — canonical state versus compiled wall program

**Status:** first cost red team after Phase 11A.  
**Executable calibration:** `tests/research/test_lonely_runner_canonical_contact_cost.py`.  
**Purpose:** prevent a false inference from successful canonicalization to execution-speed dominance.

## 1. The distinction Phase 11A creates

Phase 11A shows that the universal-cover contact-center coordinate is not required in the exact dynamic state.  The process can evolve on

\[
(\mathbf u,\boldsymbol\phi),
\qquad
\phi_i=t u_i\bmod1,
\]

using one center-free event rule.

That is a statement about **state ontology and representation growth**.  It is not yet a statement about the cheapest way to answer the first-witness query.

The existing pair-difference/Huffman work has already compiled many future contact comparisons into a shallow static decision program.  A fair red team therefore asks whether direct canonical evolution is actually cheaper on the same usage world.

---

## 2. Exact matched-world comparison

Use the exact Phase-7f usage world

```text
1 <= u1 < u2 < u3 < u4 <= 8,
u4/u1 < 8,
```

containing 55 speed quadruples.

The canonical torus event map reaches the first witness after a total of

\[
\boxed{280}
\]

events over those 55 inputs, hence

\[
\boxed{E[d]_{\rm canonical}=280/55\approx5.091.}
\]

This is expected: quotienting the deck sheet changes the state representation, not the physical order of contact events.

The already-frozen Phase-7f exact time-first 21-wall tree has usage-weighted depth

\[
\boxed{135},
\]

or

\[
\boxed{E[d]_{\rm compiled}=135/55\approx2.455.}
\]

Thus direct canonical event evolution performs about

\[
\frac{280}{135}\approx2.07
\]

times as many event/decision steps under this coarse depth metric.

So the first cost red team is deliberately negative:

\[
\boxed{
\text{canonicalization removes artificial state growth}
\not\Rightarrow
\text{canonical dynamics is the cheapest execution representation}.
}
\]

---

## 3. This strengthens rather than weakens the reconstruction

The result clarifies the role of the old wall/Huffman machinery.

The wrong dichotomy would be

```text
canonical torus process  versus  wall/Huffman process.
```

The more accurate architecture is

```text
canonical torus process
    = semantic / generative ground truth

pair-ratio predicates + decision DAG
    = selectively materialized / compiled shortcuts
```

The static wall program can be faster because one predicate can summarize the relative order of contacts that direct event evolution would discover only after several transitions.

What changes after docs 38/39 is **where those predicates are allowed to enter**.  They should be derived after canonicalization as task-relative accelerators, not treated as primitive state coordinates whose growth defines the process ontology.

---

## 4. Revised interpretation of completion

This suggests that the old center-depth additions mixed two notions:

1. **semantic completion** — the current carrier genuinely cannot represent the task-relevant residual;
2. **materialization / compilation** — the carrier is already semantically complete, but an extra derived predicate makes execution cheaper.

For the canonical torus event carrier, center-3 and center-4 do not force new state coordinates merely for correctness.  Therefore the old new-wall additions should now be retested as possible **compiled accelerators** rather than automatically called semantic completion.

This is a stricter test of `F_comp` after canonicalization:

> If the canonical carrier can evolve exactly without a new coordinate, a new wall is not semantic completion merely because a static finite decision representation wants it.

Whether AEG should eventually expose a separate public notion of materialization is outside this Sonnet experiment; no API change is proposed here.

---

## 5. Next experiment should be a compiler, not another center layer

The next useful question is now precise:

> Starting only from the canonical event rule and task semantics, can Shakespeare *derive* the useful pair-ratio predicates that the old hand-staged center-depth construction discovered?

At a canonical state, runner `i` has next-contact time increment

\[
\Delta t_i=\frac{d(\phi_i)}{u_i}.
\]

A branch occurs only when two candidate events exchange order:

\[
\frac{d(\phi_i)}{u_i}
\ ?\
\frac{d(\phi_j)}{u_j}.
\]

Along a symbolic history these comparisons induce exact rational ratio walls.  This gives a new derivation route:

```text
canonical event state
-> next-event competition
-> symbolic equality locus
-> candidate ratio predicate
-> task-relevance test
-> materialize only if it improves history geometry
-> reconverge equivalent descendants
```

This is substantially closer to the validated C1–C4 order:

\[
\text{canonicalize}
\to
\text{evolve/decompose}
\to
\text{derive only genuine/useful residual structure}.
\]

It also supplies a clean red team: if this lazy compiler cannot rediscover the old 21/26/29-wall advantages without being told the center hierarchy, then the proposed reconstruction has not yet explained the successful old representation.

---

## 6. Priority after this result

The immediate priority changes slightly from the Phase-11A roadmap.

The simple-root / adjacent-ratio `A_{k-1}` carrier remains mathematically natural, but the higher-value next step is now:

```text
Phase 11B1
canonical event-map symbolic/lazy predicate generation
    -> compare generated predicates with frozen wall sets
    -> measure whether they recover the 135-depth compiled advantage
```

Only after that should we decide whether rewriting the continuous speed carrier in simple-root coordinates materially improves the compiler.

The current tactical order is therefore

```text
11A   canonical torus state                      PASSED bounded red team
11B0  direct-dynamics cost red team               PASSED, negative on speed
11B1  lazy compiler from canonical event dynamics NEXT
11B2  simple-root / adjacent-ratio carrier         conditional
11C   task quotient / persistent compiled DAG      after B1
11D   recompute ren/res/comp after canonicalization
```

`K=13` remains frozen.

## Claim boundary

The `280` versus `135` comparison is a matched bounded four-speed depth comparison, not a runtime benchmark.  It establishes only that canonicalization and compilation solve different problems: the former removes representation freedom; the latter can reduce execution depth.  The next Sonnet objective is to derive the latter from the former rather than choosing between them.

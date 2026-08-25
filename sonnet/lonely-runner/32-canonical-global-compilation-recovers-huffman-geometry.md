# Phase 11B2 — canonical global compilation recovers the frozen Huffman geometry

**Status:** exact bounded global-compilation calibration passed.  
**Implementation:** `sonnet/lonely-runner/python/canonical_global_compilation.py`.  
**Fast CI check:** 27-wall objectification / 2,211 sign cells.  
**Opt-in exact DP:** set `AEG_RUN_LR_CANONICAL_GLOBAL_COMPILATION=1`.  
**Open-frontier policy:** `K=13` remains frozen.

## 1. Remaining gap after Phase 11B1

Phase 11B1 closed the **content-generation** side of the reconstruction:

```text
canonical torus dynamics
-> lazy symbolic next-event competition
-> 33 unresolved generated ratio coordinates
-> exact task-separation lower bounds
-> 27 globally minimum task coordinates
-> 81 final first-witness semantics.
```

But Phase 11B0 had already shown that direct canonical event evolution is slower in decision depth than the old compiled wall program on the matched 55-input usage world.

Therefore one final question remained before the canonical-first reconstruction could be considered mechanically equivalent to the successful old route:

> If we materialize only the 27 coordinates discovered by the canonical compiler, can Huffman/decision-tree optimization recover the old execution geometry without importing its tree or predicate order?

The answer is yes, exactly.

---

## 2. Objectify the 27-coordinate global wall carrier

Take the 261 exact terminal regions produced by the horizon-free symbolic compiler.  Refine each region only where one of the 27 globally minimum coordinates is still unresolved.

Every resulting complete ternary sign record has a unique first-witness task.  After merging identical records, the global carrier contains

\[
\boxed{2,211\text{ exact sign cells}}
\]

and still exactly

\[
\boxed{81\text{ task semantics}.}
\]

This is already smaller than the earlier persistent center-4 carrier:

```text
old persistent carrier    29 predicates / 3,067 cells / 81 tasks
new global carrier        27 predicates / 2,211 cells / 81 tasks
```

The difference is expected.  The old persistent representation intentionally retained the union of local minimum completion supports so that refinement could be patched incrementally.  The new carrier is optimized globally after the canonical process has closed.

These are different representation objectives, not contradictory counts.

---

## 3. Re-run the exact time-first tree optimization from scratch

Use the same 55-input usage world as the previous four-speed Huffman calibrations:

```text
1 <= u1 < u2 < u3 < u4 <= 8,
u4/u1 < 8.
```

No old tree, root choice, decision order, or 29-predicate placement is supplied.

Run the same lexicographic exact dynamic program over the new 2,211 cells, minimizing

1. usage-weighted decision depth;
2. total tree nodes / boundary volume;
3. worst depth;
4. internal decision nodes.

The optimum is

```text
weighted depth      135
tree nodes          391
worst depth          10
internal nodes      130
peak frontier        75
terminal-merged DAG 211
```

with width profile

```text
1, 3, 3, 9, 27, 48, 63, 75, 66, 48, 48
```

and root

\[
\boxed{u_4/u_1\ ?\ 4.}
\]

---

## 4. Exact identity with the old Phase-9D execution geometry

These are not merely similar numbers.  They match the frozen center-4 Phase-9D placement result coordinate-for-coordinate at the metric level:

| metric | old 29-predicate persistent carrier | new 27-predicate global carrier |
| --- | ---: | ---: |
| tasks | 81 | 81 |
| weighted depth | 135 | 135 |
| tree nodes | 391 | 391 |
| internal nodes | 130 | 130 |
| worst depth | 10 | 10 |
| peak frontier | 75 | 75 |
| terminal-merged DAG nodes | 211 | 211 |
| root | `u4/u1 ? 4` | `u4/u1 ? 4` |

The global carrier uses fewer primitive coordinates and fewer exact sign cells, yet the optimum execution geometry is unchanged.

This tells us that the two globally redundant Phase-8C local-minimum walls were useful for the **incremental persistent construction**, but they were never needed by the final optimal static execution tree.

---

## 5. The canonical-first loop is now closed end-to-end

For this bounded four-speed first-witness problem we can now run the entire representation chain in the desired causal order:

\[
\boxed{
\begin{aligned}
&\text{raw lifted process}\\
&\to \text{deck quotient / canonical torus state}\\
&\to \text{center-free exact event dynamics}\\
&\to \text{lazy symbolic process expansion}\\
&\to \text{process-generated equality loci}\\
&\to 33\text{ unresolved candidate walls}\\
&\to 27\text{ exact globally minimum task walls}\\
&\to 2,211\text{ exact global sign cells}\\
&\to \text{Huffman / decision-tree placement}\\
&\to 135/391/10/130\text{ optimum execution geometry}.
\end{aligned}
}
\]

Nothing in this chain receives a contact-center horizon or the old staged wall basis as a discovery input.

The old results remain essential as independent red teams:

- `81` task semantics;
- emergent closure at center 4;
- globally relevant `21+5+1` wall set;
- the `19/11` center-4 distinction;
- final Huffman placement metrics.

All are recovered by the canonical-first route.

---

## 6. What the reconstruction says about `F_comp`

We can now sharpen the representation-relative completion interpretation.

For the canonical dynamic carrier

\[
(\mathbf u,\boldsymbol\phi),
\]

no new process-state axis is needed when the trajectory crosses center 3 or center 4.  The event rule is already semantically complete.

The ratio predicates that appear later are generated because we choose to **compile future dynamics into a shallower task program**.  They are valuable materializations, but their necessity is different from semantic incompleteness of the canonical state.

Thus, for this carrier and this task, the old statement

```text
new center -> completion wall
```

should be replaced by

```text
canonical dynamics already complete
-> symbolic task compiler discovers useful derived predicates
-> materialize a globally or incrementally chosen subset
-> Huffman places them.
```

This does not imply that `F_comp` is universally zero in Sonnet 001.  A future task quotient may discard information from the canonical state and thereby create genuine representation-relative completion pressure again.  But contact-center sheet depth by itself is no longer evidence for such pressure.

---

## 7. Persistent versus global representation becomes an explicit design choice

The comparison also resolves a tension in the old Phase 8–10 notes.

Two representations can now be distinguished cleanly:

### Incremental persistent carrier

Optimizes future patchability:

```text
21 old global walls
+ union of 7 locally minimum center-3 supports
+ 1 center-4 wall
= 29 predicates, 3,067 cells.
```

Its strength is local update / provenance reuse.

### Final global compiled carrier

Optimizes final task sufficiency:

```text
27 globally forced coordinates
= 2,211 cells.
```

Its strength is irredundant static content.

Both compile to the same best current-use Huffman geometry.

This makes `persistent refinement cost` and `final global representation size` genuinely separate Pareto axes, rather than two imperfect measurements of the same object.

---

## 8. The next research gate changes again

The original Phase-11 roadmap proposed a simple-root / adjacent-ratio coordinate audit relatively early.  That is no longer the highest-value next step.

The canonical-first mechanism has now reproduced both **content** and **placement** of the successful old four-speed representation.  The next important question is whether this mechanism survives an independent pressure direction.

There are two credible choices:

1. **runner-dimension lift:** repeat the canonical lazy compiler at five relative speeds on a tightly bounded solved world, testing whether process-generated coordinates remain sparse enough to objectify;
2. **task change on the same four-speed process:** change the observer/task while retaining the same canonical dynamics, testing whether the compiler derives a genuinely different wall basis and whether `F_comp` reappears after task quotienting.

The second is the cleaner representation-relative red team; the first is more directly connected to eventual Lonely Runner scaling.

Before either, we should freeze Phase 11A–B2 as the new Sonnet-001 four-speed canonical baseline and update the Sonnet README so that the old Phase-6 status no longer hides the completed representation programme.

`K=13` should remain frozen until an independent transfer gate is defined.

---

## 9. Current judgment

The Sonnet 001 reconstruction now supports a much stronger statement than the initial Phase-11 hypothesis:

> The static wall/Huffman representation is not a rival ontology to the canonical torus process.  It is an exact task-directed compilation of that process.  On the complete bounded four-speed calibration, a horizon-free symbolic compiler independently discovers the globally minimum 27 predicate contents and, after exact Huffman placement, reproduces the full frozen Phase-9D execution geometry.

This gives a concrete mechanism for the docs-38/39 order

\[
\boxed{
\text{canonicalize}
\to
\text{evolve}
\to
\text{derive task distinctions}
\to
\text{materialize selectively}
\to
\text{place history optimally}.
}
\]

The canonicalization restart is therefore no longer only interpretive.  It reproduces the successful old representation from a more primitive process description.

## Claim boundary

No new Lonely Runner theorem is proved.  The 27-coordinate minimum, 2,211-cell carrier, and recovered Huffman metrics are exact results for the declared ordered four-speed domain `u4/u1 < 8` at `delta=1/5`.  The heavy decision-tree DP is kept opt-in so routine multi-version CI is not burdened by a research calibration.

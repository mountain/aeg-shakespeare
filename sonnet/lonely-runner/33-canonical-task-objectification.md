# Phase 11C — canonical task objectification removes history-only wall pressure

> **Phase-15A terminology and certificate correction.**  The projection called
> `canonical witness` below is a boundary/mode **task label**.  It does not by
> itself reconstruct event rank, lifted contact center, or witness time.  The
> 27/19/19/12 coordinate counts have also been re-certified with complete-sign
> deletion witnesses rather than relying on partial singleton separators.  See
> [`40-global-closure-contract-and-theory-audit.md`](40-global-closure-contract-and-theory-audit.md).

**Status:** exact bounded task-projection calibration implemented.  
**Implementation:** `sonnet/lonely-runner/python/canonical_task_objectification.py`.  
**Fast executable check:** `tests/research/test_lonely_runner_canonical_task_objectification.py`.  
**Opt-in Huffman check:** set `AEG_RUN_LR_CANONICAL_TASK_HUFFMAN=1`.
**Scope:** ordered four-speed domain, `delta=1/5`, `u4/u1<8`; `K=13` remains frozen.

## 1. Why Phase 11B was still deliberately over-complete

Phase 11B reconstructed the old first-witness task exactly as

\[
(\text{event rank},\ \text{lifted contact boundary with center},\ \text{mode}).
\]

That was the right comparison task because it let the canonical-first route reproduce the old Phase 8--10 semantics exactly: 81 task classes, the global 27-wall basis, and the frozen Huffman geometry.

But the reconstruction itself had already established that two coordinates in this task record are not obviously part of the canonical witness ontology:

1. **event rank** is a history index;
2. **contact center** is a universal-cover sheet/provenance coordinate.

Phase 11C therefore keeps the canonical torus process fixed and changes only the observer/task projection.

---

## 2. Projection ladder

Use the same 261 exact terminal regions and the same 33 process-generated candidate ratio coordinates from Phase 11B1.

Compare four task projections.

### A. Full legacy certificate

\[
(\text{event rank},\ \text{runner-center-kind boundary},\ \text{mode}).
\]

Exact result:

```text
task classes       81
minimum walls      27
```

### B. History-free lifted certificate

Drop only event rank:

\[
(\text{runner-center-kind boundary},\ \text{mode}).
\]

Exact result:

```text
task classes       36
minimum walls      19
```

### C. Canonical witness

Drop both event rank and contact-center sheet:

\[
\boxed{
(\text{runner-kind boundary},\ \text{mode}).
}
\]

Exact result:

```text
task classes       25
minimum walls      19
```

The 19-wall minimum is **exactly the same set** as for the history-free lifted certificate.

### D. Mode only

Keep only whether the first witness is an interval or isolated point:

```text
task classes        2
minimum walls      12
```

So the representation ladder is

\[
\boxed{
81/27
\to
36/19
\to
25/19
\to
2/12
}
\]

in `(task classes / exact minimum walls)`.

Every minimum-wall count again has the same strong certificate used in Phase 11B1: each retained coordinate is the unique separator for some cross-task terminal pair, and the union of all such mandatory coordinates separates every cross-task pair.

---

## 3. Eight walls are required only by event-rank provenance

The full 27-wall task basis loses exactly eight coordinates when event rank is removed:

\[
\boxed{
\begin{aligned}
\frac{u_3}{u_2}&\ ?\ 4, &
\frac{u_3}{u_2}&\ ?\ 6,\\
\frac{u_4}{u_2}&\ ?\ \frac94, &
\frac{u_4}{u_2}&\ ?\ 4, &
\frac{u_4}{u_2}&\ ?\ 6,\\
\frac{u_4}{u_3}&\ ?\ \frac{14}{9}, &
\frac{u_4}{u_3}&\ ?\ 4, &
\frac{u_4}{u_3}&\ ?\ 6.
\end{aligned}}
\]

No new coordinate replaces them.

This is a global exact counterpart to the earlier Phase-8B observation that some center-depth updates changed only event rank while leaving the actual witness boundary/mode fixed.

The new conclusion is stronger:

> Eight of the globally minimum 27 predicates for the legacy certificate task are not required once history rank is removed from the observer semantics.

They were genuine requirements of the declared old **certificate format**, but not of the history-free first-witness task.

---

## 4. Removing the sheet coordinate reduces task count but not the wall basis further

The next quotient

```text
runner-center-kind boundary
    -> runner-kind boundary
```

reduces task classes

\[
36\to25,
\]

but the exact minimum wall set stays at 19.

This is informative in two directions.

First, it confirms that contact center is representation provenance: several lifted certificate labels become the same canonical witness.

Second, those sheet distinctions were **not themselves responsible for additional primitive wall content** once event rank had already been removed.  The same 19 ratio coordinates suffice for both task projections.

So `task-class count` and `primitive-coordinate count` are again different representation axes.

---

## 5. Exact canonical-witness compilation

Refine the same 261 terminal regions only by the 19 globally minimum canonical-witness coordinates.

After merging identical complete sign records, the carrier contains

\[
\boxed{1,431\text{ exact sign cells}}
\]

for

\[
\boxed{25\text{ canonical witness tasks}.}
\]

Compare with the Phase-11B2 legacy-certificate carrier:

| task | walls | sign cells | tasks |
| --- | ---: | ---: | ---: |
| legacy full certificate | 27 | 2,211 | 81 |
| canonical witness | 19 | 1,431 | 25 |

The reduction is therefore not merely fewer output labels.  It changes the globally sufficient compiled predicate content itself.

---

## 6. Huffman/history geometry improves sharply

On the same frozen 55-input usage world

```text
1 <= u1 < u2 < u3 < u4 <= 8,
u4/u1 < 8,
```

run the exact lexicographic decision-tree optimizer again over the 19-wall / 1,431-cell canonical-witness carrier.

The optimum is

```text
weighted depth       113
tree nodes            94
worst depth             7
internal nodes         31
peak frontier          24
terminal-merged DAG    56
root                    u4/u1 ? 4
```

with width profile

```text
1, 3, 3, 9, 18, 24, 21, 15
```

Against the full legacy certificate compilation:

| metric | legacy certificate | canonical witness |
| --- | ---: | ---: |
| weighted depth | 135 | **113** |
| tree nodes | 391 | **94** |
| worst depth | 10 | **7** |
| internal nodes | 130 | **31** |
| peak frontier | 75 | **24** |
| DAG nodes | 211 | **56** |
| root | `u4/u1 ? 4` | `u4/u1 ? 4` |

The root survives, but almost all downstream history geometry contracts.

This is the first Sonnet-001 result where applying canonicalization to the **task record itself**, rather than only to process state, produces a large simultaneous reduction in both time-like and space-like compiled complexity.

---

## 7. Reinterpretation of the 27-wall result

Phase 11B2 remains correct and important.  Its 27-wall carrier is the exact globally minimum representation of the **legacy full-certificate task**.

Phase 11C shows why that task should not automatically be called canonical.

The correct hierarchy is now

```text
canonical process state
    -> choose observer/task semantics
    -> quotient task provenance
    -> derive task-required predicates
    -> materialize exact sign carrier
    -> optimize Huffman/history placement.
```

So there are at least three distinct notions of completion/representation pressure:

1. process-state sufficiency;
2. task/certificate sufficiency;
3. execution-program materialization.

The old center-depth completion programme mixed portions of (2) and (3).  Phase 11A--C now separates them executablely.

---

## 8. Consequence for `F_ren / F_res / F_comp`

The new evidence suggests that the Sonnet decomposition should not yet be recomputed on the 27-wall legacy task.

The more appropriate carrier is now the canonical-witness task:

\[
(\mathbf u,\boldsymbol\phi)
\quad\text{with observer output}\quad
(\text{runner-kind boundary},\text{mode}).
\]

Relative to this task, eight previously necessary wall directions disappear before any completion analysis is performed.

Therefore a future `F_comp` claim should be made only after both:

```text
process canonicalization
and
task objectification
```

have been applied.

This is a direct executable instance of the docs-38/39 rule

\[
\boxed{\text{canonicalize first; classify residuals second; complete last}.}
\]

---

## 9. Next gate

The clean next pressure direction is now **runner dimension**, not another four-speed quotient.

The four-speed line has established an end-to-end stack:

\[
\boxed{
\text{canonical torus process}
\to
\text{lazy symbolic compiler}
\to
\text{task objectification}
\to
\text{global minimum predicates}
\to
\text{Huffman placement}.
}
\]

The next bounded experiment should lift this exact mechanism to five relative speeds on a deliberately tight solved domain and measure:

- symbolic-state growth;
- generated candidate-coordinate growth;
- task-minimum coordinate growth;
- task projection sensitivity;
- sign-cell growth;
- Huffman geometry where computationally feasible.

No `K=13` data should be touched during that dimension-transfer experiment.

## Claim boundary

No new Lonely Runner theorem is proved.  All `81/27 -> 36/19 -> 25/19 -> 2/12`, `1,431`, and Huffman `113/94/7/31/24/56` values are exact for the declared bounded ordered four-speed domain and its specified task projections.  The result does not assert that the 19-wall canonical-witness basis generalizes unchanged to other runner counts.

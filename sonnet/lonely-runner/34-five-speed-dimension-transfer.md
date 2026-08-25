# Phase 12A — five-speed dimension transfer exposes static-materialization blow-up

> **Phase-15A certificate correction.**  Partial-region singleton separators
> are now used only to propose a basis.  For the base `u5/u1<21/4` domain, the
> 86/36/36/27 coordinate counts are re-certified by synchronized exact
> completion in the full 98-coordinate grammar, with one deletion witness per
> retained coordinate.  Wider sweep counts require their own corresponding
> strong certificates.  See
> [`40-global-closure-contract-and-theory-audit.md`](40-global-closure-contract-and-theory-audit.md).

**Status:** exact bounded dimension-transfer calibration implemented.  
**Implementation:** `sonnet/lonely-runner/python/five_speed_dimension_transfer.py`.  
**Executable calibration:** `tests/research/test_lonely_runner_five_speed_dimension_transfer.py` (opt-in via `AEG_RUN_LR_FIVE_SPEED_TRANSFER=1`).  
**Scope:** five ordered relative speeds, `delta=1/6`, `u5/u1 < 21/4`; `K=13` remains frozen.

## 1. Why this domain is the first nontrivial five-speed pressure test

For five relative speeds the Lonely Runner threshold is

\[
\delta=\frac16.
\]

The latest initial exit is that of the slowest runner:

\[
t_{\rm exit,max}=\frac{1}{6u_1}.
\]

The earliest first enter is that of the fastest runner:

\[
t_{\rm enter,min}=\frac{5}{6u_5}.
\]

If

\[
\frac{u_5}{u_1}<5,
\]

then

\[
\frac{1}{6u_1}<\frac{5}{6u_5}.
\]

Hence all five runners exit the bad set before any can re-enter.  The first witness is forced at the slowest initial exit; the symbolic compiler has no nontrivial ratio choice to discover.

So `u5/u1 < 5` is an analytically trivial transfer domain.  Phase 12A chooses

\[
\boxed{\frac{u_5}{u_1}<\frac{21}{4}=5.25}
\]

as a small exact step beyond that threshold.  This is deliberately a scaling probe, not a large solved-instance benchmark.

---

## 2. The Phase-11 mechanism transfers without changing its rules

The five-speed compiler uses the same causal order frozen at four speeds:

```text
canonical torus contact process
-> lazy next-event symbolic competition
-> process-generated rational equality loci
-> task projection / objectification
-> exact minimum predicate selection.
```

No contact-center horizon and no precomputed ratio alphabet are supplied.

The only structural changes are:

- runner count `4 -> 5`;
- threshold `1/5 -> 1/6`;
- tight relative domain `u5/u1 < 21/4`.

---

## 3. Horizon-free symbolic closure still succeeds

The exact symbolic process closes with

```text
symbolic states          3,397
terminal exact regions   1,117
maximum event index         47
maximum contact center        7
generated coordinates       98
```

The maximum center `7` again emerges from the process rather than being supplied as a horizon.

Compared with the four-speed canonical baseline:

| quantity | four speeds | five speeds | growth |
| --- | ---: | ---: | ---: |
| symbolic states | 388 | 3,397 | 8.76x |
| terminal regions | 261 | 1,117 | 4.28x |
| generated coordinates | 33 | 98 | 2.97x |
| max event index | 18 | 47 | 2.61x |
| emergent max center | 4 | 7 | 1.75x |

The process representation grows materially, but it remains finite and exact on this first nontrivial five-speed domain.

---

## 4. Task objectification remains extremely effective

Apply the same task-projection ladder used in Phase 11C.

### Full legacy-style certificate

```text
task classes       154
minimum walls       86
```

### Drop event rank only

```text
task classes        63
minimum walls       36
```

### Canonical witness: drop event rank and contact-center sheet

```text
task classes        33
minimum walls       36
```

### Mode only

```text
task classes         2
minimum walls       27
```

Thus

\[
\boxed{
154/86
\to
63/36
\to
33/36
\to
2/27
}
\]

in `(task classes / exact minimum walls)`.

As at four speeds, the history-free lifted task and the canonical witness have the **same exact minimum wall set**.  Removing the sheet coordinate changes output semantics but does not require an additional predicate basis once event rank has already been removed.

The minimum claims again use singleton-separator lower-bound witnesses whose union separates every cross-task terminal pair.

---

## 5. The crucial scaling result: semantic complexity does not explode first

Compare the canonical-witness layer:

| quantity | four speeds | five speeds | growth |
| --- | ---: | ---: | ---: |
| canonical task classes | 25 | 33 | 1.32x |
| exact minimum walls | 19 | 36 | 1.89x |
| generated candidates | 33 | 98 | 2.97x |

This is a relatively controlled increase compared with the 8.76x growth of symbolic process states.

So the first dimension-transfer result does **not** support the fear that adding one runner immediately destroys task objectification or predicate sparsity.

The real problem appears one layer later.

---

## 6. Full static sign materialization explodes

If the 36 canonical-witness walls are all materialized globally over the 1,117 terminal regions, exact refinement produces

\[
\boxed{69,683\text{ sign cells}.}
\]

The four-speed canonical carrier had only

\[
1,431\text{ cells}.
\]

Hence

\[
\boxed{
1,431\longrightarrow69,683
\approx48.7\times.
}
\]

while task classes grow only

\[
25\longrightarrow33.
\]

This is the decisive Phase-12A red team.

The bottleneck is no longer:

```text
contact-center depth
or
generated predicate count
or
task-semantic count.
```

It is

\[
\boxed{\text{global static arrangement materialization}.}
\]

Trying to repeat the four-speed `all minimum walls -> all complete sign cells -> exact global tree DP` pipeline literally is therefore the wrong next move.

---

## 7. Reinterpretation of Huffman placement under dimension growth

At four speeds the globally compiled 19-wall canonical task was small enough that full sign-cell materialization was useful and an exact Huffman tree could be optimized over all 1,431 cells.

At five speeds, doing the same would first manufacture 69,683 cells although the process itself reaches only 1,117 terminal regions and only 33 canonical tasks.

This reverses the natural order again if we are not careful.

The correct next representation should preserve the lazy geometry:

```text
1,117 exact terminal regions
+ 36 task-minimum predicates
-> query/refine a predicate only when a current region leaves it unresolved
-> merge states again as soon as future task semantics agree
-> build a persistent/lazy decision DAG
```

rather than

```text
36 predicates
-> materialize every feasible joint sign cell
-> optimize afterward.
```

In other words, **Huffman placement must itself become lazy/persistent under runner-dimension growth**.

---

## 8. New research gate: lazy task decision DAG

Phase 12B should operate directly on the 1,117 terminal closure regions.

A node should carry a set of exact closure/task atoms.  Querying one of the 36 canonical coordinates should:

1. route atoms whose sign is already forced without splitting;
2. refine only atoms for which the queried sign is unresolved;
3. discard infeasible sign refinements immediately by exact cycle closure;
4. stop as soon as all surviving atoms have the same canonical witness task;
5. memoize/reconverge identical residual task-constraint states.

The primary metrics should be

\[
\boxed{
(\text{new refined atoms visited},\
\text{decision DAG nodes},\
\text{weighted depth},\
\text{worst depth},\
\text{peak live frontier}).
}
\]

The first target is simple and falsifiable:

> Can a lazy task DAG solve the complete five-speed canonical task without visiting anything close to the 69,683 fully materialized sign cells?

Only after that should an exact global optimality search be considered.

---

## 9. Current cross-dimensional picture

The canonical-first programme now separates the growth layers clearly:

```text
runner dimension
    -> symbolic process states grow ~8.8x
    -> generated predicates grow ~3x
    -> canonical task classes grow ~1.3x
    -> minimum wall basis grows ~1.9x
    -> naive full sign materialization grows ~48.7x
```

This is exactly the kind of distinction the original Shakespeare programme was intended to expose: the largest apparent complexity jump occurs in a **chosen representation materialization**, not in the task semantics themselves.

## Claim boundary

No new Lonely Runner theorem is proved.  The `3,397 / 1,117 / 98`, projection counts `154/86 -> 63/36 -> 33/36 -> 2/27`, and `69,683` static-cell count are exact for the declared five-speed domain `u5/u1 < 21/4`.  They do not establish asymptotic scaling laws or transfer to the open `K=13` frontier.

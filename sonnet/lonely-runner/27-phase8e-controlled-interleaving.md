# Phase 8E — controlled interleaving closes the center-3 placement gap

**Status:** exact bounded controlled-interleaving calibration passed.  
**Scope:** old 21 center-2 task-relevant walls + exactly seven frozen Phase-8C completion walls; no full 72,241-state center-3 arrangement.  
**Predecessors:** [`25-phase8d2-refinement-aware-placement.md`](25-phase8d2-refinement-aware-placement.md), [`26-phase8e0-activation-geometry.md`](26-phase8e0-activation-geometry.md)

## 1. Question

By the end of Phase 8D the semantic content of the center-2 -> center-3 update was
already frozen:

```text
843 renormalizable states
  6 genuine completion states
  7 distinct new raw completion walls
  6 objectified local completion decoders
 16 total new-wall internal decision nodes.
```

The local persistent graft used exactly those 16 new decisions and matched the
fresh center-3 tree's total decision structure:

```text
376 tree/boundary nodes
125 internal query nodes.
```

But its placement was worse:

```text
local graft: peak/worst = 75/12
fresh tree:  peak/worst = 72/10.
```

Phase 8D.2 then showed that scalar reweighting of the **old prefix only** could
not close this gap in the sampled family.

Phase 8E asks the architectural question:

> can the same frozen seven new process distinctions be interleaved with the old
> 21 wall predicates before complete old-parent resolution, while deriving all
> feasible joint states only from center-2 exact constraints and the already
> certified local completion semantics?

## 2. Constructing the joint old/new process representation

The full center-3 wall arrangement is not enumerated.

For each of the 5,823 exact center-2 full sign systems, multiplicative difference
constraints are refined **only by the seven frozen Phase-8C walls**.  Joint
feasibility therefore lives in a 28-predicate language:

```text
21 old task-relevant wall signs
+7 new completion-wall signs.
```

After quotienting duplicate feasible variants under the 849 old persistent
parents, this produces

\[
\boxed{2,753\text{ feasible joint items}}.
\]

This should be compared conceptually, not as a direct cardinality quotient, with
the full center-3 census of 72,241 realizable sign systems: the interleaving
world materializes only distinctions already justified by the old persistent
representation and local completion analysis.

Task semantics are assigned without a fresh center-3 solver:

- stable parents keep their old task under every feasible new-wall variant;
- the two history-reindex parents use their already-certified updated task;
- the six completion parents are decoded exclusively by the frozen Phase-8C.2
  decoders.

The resulting joint representation contains exactly

\[
\boxed{75\text{ final first-witness task semantics}}.
\]

## 3. Current-usage-only interleaving result

With `lambda=0`, so the primary weighted objective is still the original 55-input
current-task usage distribution, the generic exact decision-tree search is
allowed to choose among all 28 predicates.

It returns:

```text
current weighted depth total  135
completion-child depth total 2708
tree / boundary nodes         376
internal query nodes          125
terminal-merged DAG nodes     200
peak frontier                  72
worst depth                    10.
```

The width profile is

```text
1, 3, 3, 9, 27, 48, 63, 72, 66, 45, 39.
```

Thus

\[
\boxed{
(376,125,200,72,10)
}
\]

matches **all frozen structural metrics** of the independently constructed fresh
center-3 time-first tree that were being used as the placement oracle, while
also keeping current weighted depth exactly at the center-2 value

\[
\boxed{135}.
\]

No fresh center-3 tree was supplied to the construction.

This is the central Phase-8E result.

## 4. What actually moved

The total inventory of decision primitives did not increase:

```text
109 old-wall internal nodes
 16 new-wall internal nodes
---
125 total internals.
```

The local graft already had the same `109 + 16` count.  Controlled interleaving
changes their **history partial order and sharing**, not their number.

In the `lambda=0` tree:

```text
new-wall internal nodes        16
cross-parent new-wall nodes     4
earliest new-wall activation    depth 5.
```

The seven frozen walls first appear at depths

\[
\boxed{5,6,7,7,8,8,9}
\]

(sorted), with occurrence counts

```text
u3/u2 ? 14/11    depth 7   occurrences 1
u3/u2 ? 16/11    depth 8   occurrences 1
u4/u2 ? 7/3      depth 6   occurrences 4
u4/u2 ? 8/3      depth 5   occurrences 4
u4/u3 ? 14/11    depth 7   occurrences 1
u4/u3 ? 14/9     depth 8   occurrences 3
u4/u3 ? 16/9     depth 9   occurrences 2.
```

The occurrence total is again

\[
1+1+4+4+1+3+2=\boxed{16}.
\]

So the placement improvement is not bought by extra new-wall decisions.  Four of
those already-required decisions are simply shared/activated before one old
persistent parent has been fully identified.

## 5. Activation geometry explains why this requires reconvergence

Phase 8E.0 found that no frozen new wall has a **shared clean activation** in the
frozen center-2 tree.  Even walls used by four completion parents become
zero-collateral only after a single active user remains.

Yet the successful interleaved tree contains four cross-parent new-wall nodes.

Therefore the successful representation cannot be described as merely lifting a
new query to an already-clean old node.  It must permit the stronger mechanism:

```text
early new-wall query
    -> temporarily split some old contexts that do not need the distinction
    -> retain exact semantics on both branches
    -> later reconverge/objectify task-equivalent branches
    -> share the decision across actual completion contexts.
```

This is a DAG/history reorganization, not a larger local completion language.

## 6. Comparison with the local graft

The local graft and controlled interleaving have the same persistent object
inventory:

```text
local graft:          376 tree nodes / 125 internals / 200 DAG nodes
controlled lambda=0: 376 tree nodes / 125 internals / 200 DAG nodes.
```

But controlled interleaving improves

```text
peak frontier: 75 -> 72
worst depth:   12 -> 10
completion-child total depth: 2933 -> 2708
```

while preserving

```text
current weighted depth: 135 -> 135.
```

This gives a sharper decomposition of representation optimization:

\[
\boxed{
\text{completion discovers the required decisions};
\quad
\text{interleaving optimizes their partial order and sharing in history}.
}
\]

## 7. Refinement weighting remains multi-axis

The same joint 28-predicate representation was also searched with small
refinement mixtures.

For both `lambda=1/16` and `lambda=1/4` the result is

```text
current weighted total       136
completion-child total      1972
tree / internal / DAG      376 / 125 / 200
peak / worst                 87 / 10
new-wall internal nodes      16
cross-parent activations       8
earliest new wall          depth 4.
```

Again, refinement-time improvement is bought largely through earlier/shared new
wall activation, but frontier space increases sharply.  This reinforces Phase
8D.2's conclusion that current time, continuation time, and frontier geometry
must remain separate cost axes.

## 8. What was *not* imported

The successful `lambda=0` construction did **not** receive:

- the 72,241 full center-3 sign systems;
- the fresh center-3 tree topology;
- any center-3 wall outside the seven frozen completion walls;
- a center-3 global task-relevance scan;
- deeper contact layers;
- `K=13` data.

Its only new semantic information came from the already frozen Phase-8C.2 local
completion decoders.

Thus the fresh placement geometry is reconstructed from a substantially smaller
process-generated representation rather than copied from the oracle.

## 9. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/controlled_interleaving.py
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_controlled_interleaving.py
```

Activation companion:

```text
sonnet/lonely-runner/python/activation_geometry.py
tests/research/test_lonely_runner_activation_geometry.py
```

Recorded exact certification:

```text
workflow: Sonnet Lonely Runner Phase 8E Certification
run id:   32587582896
Python:   3.12.14
8E.0:     1 passed in 36.33 s
8E:       1 passed in 152.67 s
```

Timing is provenance only.  All heavy Phase-8E workflows are restored to manual
`workflow_dispatch` after certification.

## 10. API consequence

Phase 8E does **not** justify a new observer-connection abstraction.  Nothing here
transports a canonical frame.

It does introduce a stronger pressure on the representation layer:

```text
primitive/process distinction
    + task-relative semantic objectification
    + admissible history interleaving / reconvergence
```

must be kept conceptually separate.

A candidate future abstraction is not yet a `PersistentDAG` class but a smaller
notion of **activation/interleaving certificate**: evidence that a process
predicate may enter a history before a coarser presentation state is fully
resolved, together with a certificate that collateral branches are semantically
safe to reconverge.

One Sonnet is not enough to promote that abstraction into `src/`.

## 11. Next question

The bounded center-2 -> center-3 representation loop is now essentially closed:

```text
old persistent representation
    -> local effect detection
    -> canonical decomposition
    -> minimum raw completion
    -> residual objectification
    -> persistent graft
    -> cost red team
    -> controlled interleaving
    -> fresh structural geometry recovered without full fresh census.
```

The next useful pressure should therefore be **scaling/generalization**, not more
center-3 tuning.

Two candidates are now meaningful:

1. center-3 -> center-4 persistence, using the entire frozen Phase-8 machinery
   without redesigning it; or
2. a second unrelated discrete/process problem that tests whether activation +
   reconvergence is reusable outside Lonely Runner.

The first is the natural Sonnet continuation; the second is the stronger API
promotion test.

## 12. Claim boundary

No new Lonely Runner theorem is proved.  Matching the frozen structural metrics
of the fresh tree does not prove tree isomorphism or global optimality beyond the
metrics checked.

The exact bounded statement is:

\[
\boxed{
\text{old persistent geometry + seven process-generated completion walls +
local task decoders suffice to reconstruct the frozen center-3 structural
placement metrics without constructing the full center-3 arrangement.}
}
\]

## 13. References

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

# Phase 8 — persistent Hauffman geometry, canonical decomposition, and refinement-aware placement

**Status:** Phases 8A, 8C, 8C.2, and 8D passed; Phase 8B rejected the proposed discrete observer-transport interpretation.  
**Branch:** `research/canonical-observer-api`  
**Result notes:** [`20-phase8a-discrete-canonical-decomposition.md`](20-phase8a-discrete-canonical-decomposition.md), [`21-phase8b-history-reindex-red-team.md`](21-phase8b-history-reindex-red-team.md), [`22-phase8c-minimum-completion-residuals.md`](22-phase8c-minimum-completion-residuals.md), [`23-phase8c2-residual-objectification.md`](23-phase8c2-residual-objectification.md), [`24-phase8d-persistent-dag-increment.md`](24-phase8d-persistent-dag-increment.md)  
**Open frontier policy:** `K=13` remains a frozen holdout and is not used for representation development.

## 1. Frozen structural result

The center-2 -> center-3 four-speed first-witness refinement has the exact local decomposition

\[
\boxed{
843\,F_{\rm ren}
\oplus
0\,F_{\rm res}
\oplus
6\,F_{\rm comp}.
}
\]

More explicitly:

```text
841 identity-stable states
  2 history/decoder reindex states
  6 genuine completion states.
```

The two nonbranching updates preserve the same witness boundary and mode and only move the event rank by `+2`.  They are not observer transport.  Sonnet 001 therefore still supplies **no discrete evidence for `ObserverConnection`**.

## 2. Observation-locality rule

All representation discovery in this phase may use only:

- the current persistent task state;
- its certified contact/witness prefix;
- pair-difference cycle closure;
- the newly admitted contact layer;
- finite local order relations involving the old causal prefix;
- declared task semantics for quotient certification.

The complete next-layer census, deeper future layers, complete propagators, and `K=13` data are forbidden as representation-selection inputs.

## 3. Phase 8A — local behavioral classification: PASSED

Using only old state plus the new contact layer,

```text
A = forced_earlier
B = effective_unresolved_crossing

stable              = not A and not B
nonbranching_update = A and not B
completion_pressure = B.
```

This yields `841 / 2 / 6` **before** center-3 child semantics are inspected.  The later local red team reopens only 26 of 5,823 old full systems, evaluates 298 center-3 children, and recovers all 75 frozen center-3 first-witness semantics rather than enumerating the complete 72,241-state center-3 geometry.

## 4. Phase 8B — proposed observer transport: REJECTED

Exact witness records are

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval').
```

Same boundary, same mode, event-rank shift `+2`.  The two states therefore belong to `F_ren`; the discrete `F_res` sector is empty.

This negative result is binding.  A future discrete connection claim must exhibit an intrinsic canonical frame that actually moves inside a fixed observer family.

## 5. Phase 8C — minimum raw completion: PASSED

For each of the six `F_comp` parents, allow every varying center-3 process-generated wall sign as a candidate residual and solve the exact cross-task conflict-cover problem.

Minimum raw support sizes are

\[
\boxed{1,2,2,2,3,4}.
\]

Every selected wall is genuinely new at center 3; no minimum signature needs a latent old wall.  Four parents immediately obtain exact task quotients.  Two are over-refined:

```text
3 walls -> 11 raw classes -> 7 task classes
4 walls -> 13 raw classes -> 3 task classes.
```

Thus

```text
completion pressure
    != minimum raw process-generator support
    != minimum task representation.
```

## 6. Phase 8C.2 — task-relative residual objectification: PASSED

Quotient the minimum raw sign language by exact first-witness semantics and search an adaptive decoder that queries only the selected completion walls.

The two over-refined cases close exactly as

\[
\boxed{11\to7},
\qquad
\boxed{13\to3}.
\]

The `13 -> 3` case is especially informative: its minimum raw support contains four walls, yet no decoder path needs all four.  The exact decoder has worst depth three, six internal nodes, and three shared semantic terminals, hence nine terminal-merged DAG nodes.

This freezes the local completion pipeline as

\[
\boxed{
F_{\rm comp}
\to
\text{minimum raw process generators}
\to
\text{task-relative objectified residual}.
}

No universal `Completion` or `ResidualQuotient` package abstraction is promoted by this result.

## 7. Phase 8D — explicit persistent DAG increment: PASSED

Start from the frozen center-2 68-label persistent Hauffman tree:

```text
tree / boundary nodes  328
internal query nodes   109
terminal-merged DAG    177
peak frontier           72
worst depth               9
weighted depth          135  (historical 55-input weights).
```

Reuse every old decision.  The 843 renormalizable states add zero new wall queries.  Replace only the six completion terminals by their Phase-8C.2 decoders.

The six local decoders contribute

```text
16 internal query nodes
38 local path leaves.
```

Therefore the explicit graft has

\[
328-6+16+38=\boxed{376}
\]

prefix-tree nodes and

\[
109+16=\boxed{125}
\]

internal query nodes.  With 75 final task semantics, terminal merging gives

\[
125+75=\boxed{200}
\]

DAG nodes, only `+23` from the center-2 persistent DAG.

Its width profile is

```text
1, 3, 3, 9, 27, 48, 63, 72, 75, 39, 18, 15, 3
```

so

\[
\boxed{\text{peak}=75,\qquad\text{worst}=12.}
\]

## 8. Local completion versus global placement

The separately frozen fresh center-3 time-first tree has

```text
boundary/tree nodes  376
internal nodes       125
peak frontier         72
worst depth            10.
```

The persistent graft therefore discovers **exactly the same total amount of decision structure** (`376/125`) while placing it less efficiently in history (`75/12` rather than `72/10`).

This gives a clean experimental separation:

\[
\boxed{
\text{local completion/objectification answers how much new structure is needed},
}
\]

whereas

\[
\boxed{
\text{global Hauffman optimization answers where that structure should sit in history}.
}
\]

The equality of node counts is a bounded calibration fact, not a graph-isomorphism or universality theorem.

## 9. Red team on the cost distribution

The original 55-input center-2 usage distribution hits **none** of the eight refinement-sensitive parents:

```text
completion inputs       0
history-reindex inputs  0
extra wall queries      0.
```

So its zero incremental cost is a sampling blind spot, not evidence that future refinement is free.

Conditional on the actual local update, the 298 reopened center-3 children consist of 288 completion children and ten history-reindex children.  The exact completion decoders use

\[
\boxed{544}
\]

new wall queries over that local workload:

\[
E[d_{\rm extra}\mid\text{reopened}]
=\frac{544}{298}\approx1.8255,
\]

\[
E[d_{\rm extra}\mid F_{\rm comp}]
=\frac{544}{288}=\frac{17}{9}\approx1.8889,
\]

with maximum extra depth three.

Therefore **current usage weights and refinement/continuation weights must be separate cost axes**.

## 10. API consequence after 8D

The strongest cross-domain abstractions remain deliberately small:

```text
ProcessDirection
ConstraintCanonicalization      # one backend
ObserverConnection              # only when an observer actually moves
CanonicalDecomposition          # backend-neutral result shape.
```

Sonnet 001 strengthens `CanonicalDecomposition` and the need for task-relative objectification after completion.  It does not justify a discrete `ObserverConnection`, a universal completion object, or a generic persistent-DAG class yet.

The most important new API pressure is instead on **cost semantics**: a continuing-process presentation needs current history geometry and future refinement cost to remain distinguishable.

## 11. Next phase — refinement-aware Hauffman reordering

Freeze Phases 8A--8D.  In particular, do **not** change the six completion residuals to improve global tree metrics.

Search only over admissible global wall placement/query order while evaluating at least two independent objectives:

1. current-task/history cost under declared present usage weights;
2. refinement cost under an explicit continuation workload with support on refinement-sensitive states.

First target:

> determine whether global reordering of the already-discovered decision structure can reduce the persistent graft from `peak/worst = 75/12` toward the fresh center-3 `72/10` geometry without rebuilding completion semantics from the full center-3 arrangement.

This is now a **placement problem**, not a representation-completion problem.

A useful red team is to compare three weight schemes separately rather than collapse them:

```text
historical current-task usage           # known blind control here
uniform / structural persistent states
conditional locally reopened children.
```

Only after this placement problem is understood should center-3 -> center-4 incremental growth be attempted.

## 12. Future moving-observer / ODE experiment

The ODE intuition remains separate.  Phase 8B showed that one-to-one semantic update does not imply observer motion.

A future discrete connection experiment requires an actual changing local canonical frame inside a fixed representation family.  History reindexing, decoder changes, residual completion, and global Hauffman reordering are not substitutes for that condition.

## 13. Execution order

```text
8A    local 841 / 2 / 6 behavioral classification             PASSED
8B    discrete observer-transport interpretation              REJECTED
      corrected canonical sectors = 843 / 0 / 6
8C    minimum raw completion support                          PASSED
      sizes = 1,2,2,2,3,4
8C.2  task-relative residual objectification                  PASSED
      strict quotients 11->7 and 13->3
8D    local persistent-DAG graft                              PASSED
      177 -> 200 DAG nodes; tree 328 -> 376
NEXT  refinement-aware global Hauffman placement
THEN  only if justified, center-3 -> center-4 persistence
FUTURE search separately for a genuine discrete moving observer
```

## 14. Claim boundary

No new Lonely Runner theorem is proved.  The current bounded representation result is:

\[
\boxed{
\text{one new contact layer is absorbed by six local completion decoders,
adding 23 explicit DAG objects after semantic objectification.}
}

The persistent graft matches the fresh center-3 optimum's total node counts but not its peak or worst depth.  The next scientific problem is therefore global history placement under a refinement-aware cost, not further enlargement of the local completion language.

## 15. References

[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in R. E. Miller and J. W. Thatcher (eds.), *Complexity of Computer Computations*, The IBM Research Symposia Series, Plenum Press, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

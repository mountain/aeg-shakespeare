# Phase 8D — sparse persistent-DAG increment and refinement-cost separation

**Status:** exact bounded persistent-update calibration passed.  
**Scope:** four relative speeds; center-2 -> center-3 contact-depth refinement; first-witness task; still Gate A.  
**Predecessors:** [`22-phase8c-minimum-completion-residuals.md`](22-phase8c-minimum-completion-residuals.md), [`23-phase8c2-residual-objectification.md`](23-phase8c2-residual-objectification.md)

## 1. Question

Phase 8C.2 leaves six exact local completion decoders attached to six genuinely
branching center-2 persistent states.  The remaining representation question is
no longer whether the next layer is computable, but how much **new history and
object structure** must be allocated if the existing center-2 Hauffman
representation is retained.

The experiment therefore asks:

> can center 3 be absorbed by grafting local completion decoders onto the frozen
> center-2 persistent tree, rather than rebuilding a center-3 tree from the full
> 72,241-state geometry?

## 2. Frozen center-2 persistent representation

Phase 7i already constructed the one-step persistent quotient

\[
849\text{ task-safe states}\to68\text{ persistent terminal labels},
\]

where 60 labels encode current first-witness semantics and eight additional
terminal identities preserve exactly the states that the next contact layer can
reopen.

Under the frozen 55-integer-quadruple usage weights, its time-first Hauffman tree
has

```text
persistent labels      68
tree / boundary nodes  328
internal query nodes   109
terminal-merged DAG    177
peak frontier           72
worst depth               9
weighted depth          135
```

The Phase-8D construction does not alter any of these old decisions.

## 3. Local graft rule

Use the corrected Phase-8A/8B decomposition

\[
843F_{\rm ren}\oplus0F_{\rm res}\oplus6F_{\rm comp}.
\]

The 841 identity-stable parents keep their old terminal semantics.  The two
history-reindex parents keep the same witness geometry and update only decoder
provenance.  Both categories require zero new wall queries.

Only the six completion terminals are replaced.  Their Phase-8C.2 adaptive
decoders contribute in total

```text
16 internal query nodes
38 local decision-tree path leaves.
```

No cross-parent sharing of internal decoder nodes is assumed.  Equal final
first-witness task terminals are shared when counting the persistent DAG.

This gives an explicit conservative construction rather than a global DAG
minimum claim.

## 4. Exact incremental structure

Replacing six old leaves by the six completion trees gives

\[
328-6+16+38
=\boxed{376}
\]

prefix-tree / boundary nodes, and

\[
109+16=\boxed{125}
\]

internal query nodes.

There are 75 final center-3 first-witness semantics.  Terminal merging therefore
gives

\[
125+75=\boxed{200}
\]

persistent DAG nodes, compared with

\[
109+68=177
\]

at center 2.

Thus the explicit object increment is

\[
\boxed{+48\text{ prefix-tree nodes},\qquad+23\text{ terminal-merged DAG nodes}.}
\]

The full updated prefix geometry is

```text
1, 3, 3, 9, 27, 48, 63, 72, 75, 39, 18, 15, 3
```

with

\[
\boxed{\text{peak}=75,\qquad\text{worst depth}=12.}
\]

## 5. Comparison with the fresh center-3 tree

A separately frozen full center-3 time-first optimization from Phase 7h has

```text
boundary/tree nodes   376
internal nodes        125
peak frontier          72
worst depth            10.
```

The local persistent graft therefore reproduces **exactly the same total number
of tree and internal decision nodes** without constructing the full center-3
arrangement, but places them less efficiently in history:

```text
same volume:      376
same internals:   125
persistent peak:   75   vs fresh 72
persistent worst:  12   vs fresh 10.
```

This is a particularly clean separation:

\[
\boxed{
\text{local completion determines how much decision structure is required},
}
\]

while

\[
\boxed{
\text{global Hauffman reordering determines where that structure sits in history}.
}
\]

The equality `376/125` is an observed bounded calibration fact.  It is not a
claim of tree isomorphism or a theorem that local completion always recovers the
node count of a fresh optimum.

## 6. Red team: the historical usage distribution is blind

The original center-2 Hauffman optimization used 55 integer quadruples.  Replaying
those same 55 examples through the updated persistent representation gives

```text
completion inputs       0
history-reindex inputs  0
extra wall queries      0
updated weighted depth  135.
```

This does **not** mean that refinement is free.  None of the 55 historical
samples lies in any of the eight refinement-sensitive center-2 states.

Thus the old usage weights are a valid current-task distribution but an invalid
stand-in for refinement risk.

This is a direct red team against a single scalar expected-depth objective.

## 7. Conditional local-refinement workload

To expose the work hidden by that sampling blind spot, measure the exact decoder
cost on the states that the local refinement algorithm actually reopens.

The 298 center-3 children decompose as

```text
288 children below genuine completion parents
 10 children below the two history-reindex parents.
```

History reindexing adds no new wall query.  Across all completion children, the
six exact adaptive decoders perform

\[
\boxed{544}
\]

new wall queries in total.

Therefore

\[
\boxed{
E[d_{\rm extra}\mid\text{reopened child}]
=\frac{544}{298}
\approx1.8255,
}
\]

and conditional on genuine completion,

\[
\boxed{
E[d_{\rm extra}\mid F_{\rm comp}]
=\frac{544}{288}
=\frac{17}{9}
\approx1.8889.
}
\]

The maximum extra completion depth is only

\[
\boxed{3}.
\]

These are conditional structural workloads, not global probabilities.

## 8. Consequence for Hauffman cost

Phase 8D shows that at least two distributions must be distinguished:

```text
current usage distribution
    -> how often present task paths are traversed

refinement / continuation distribution
    -> how likely retained terminal states are to require future work.
```

The old 55 samples constrain the first but are blind to the second in this
experiment.

A continuing-process cost should therefore remain multi-axis, for example

\[
C(P)=
(
C_{\rm current\ history},
C_{\rm frontier},
C_{\rm decoder},
C_{\rm residual},
C_{\rm refinement}
),
\]

rather than deriving future-update weights automatically from the current-task
sample distribution.

## 9. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/persistent_dag_increment.py
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_persistent_dag_increment.py
```

Recorded exact run:

```text
workflow: Sonnet Lonely Runner Canonical Decomposition
run id:   32586254733
Python:   3.12.14
8D:       1 passed in 21.46 s
```

The same run rechecked Phases 8A--8C.2 before executing 8D.  Timing is provenance
only.

The heavy workflow is restored to manual `workflow_dispatch`.  Routine CI still
parses the mathematical essay through the literate/reference hygiene gate.

## 10. Next experiment — refinement-aware global reordering

Freeze the local completion/objectification layer.  Do **not** change the six
completion residuals merely to improve tree metrics.

Instead search globally over admissible wall query order while pricing both:

1. current-task history geometry; and
2. an explicit refinement workload that has support on the eight sensitive
   parents or their 298 local children.

The first target is to determine whether global reordering can recover the fresh
center-3 `peak=72`, `worst=10` geometry while preserving the persistent local
construction and its sparse update semantics.

This is now a Hauffman placement problem, not a completion-discovery problem.

## 11. Claim boundary

No new Lonely Runner theorem is proved.  The 200-node persistent DAG is an
explicit conservative construction, not a minimum-DAG theorem.  The conditional
`544/298` workload is not a global expected cost.

The bounded result is nevertheless sharper than the earlier persistence claim:

\[
\boxed{
\text{one new process layer adds only 23 explicit DAG objects after semantic
objectification, while global history placement remains separately optimizable.}
}
\]

## 12. References

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

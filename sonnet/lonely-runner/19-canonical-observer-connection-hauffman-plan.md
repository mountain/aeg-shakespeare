# Persistent Hauffman geometry and canonical decomposition — closure plan

**Status:** the four-runner contact-center refinement programme is closed through an exact infinite-tail certificate. Phase 8 closed center 2 -> 3; Phase 9 replayed the rules unchanged at center 3 -> 4; Phase 10 proves that every contact event at every center `n >= 5` is task-irrelevant to the resulting first-witness representation.  
**Branch:** `research/canonical-observer-api`  
**Result notes:** [`20`](20-phase8a-discrete-canonical-decomposition.md), [`21`](21-phase8b-history-reindex-red-team.md), [`22`](22-phase8c-minimum-completion-residuals.md), [`23`](23-phase8c2-residual-objectification.md), [`24`](24-phase8d-persistent-dag-increment.md), [`25`](25-phase8d2-refinement-aware-placement.md), [`26`](26-phase8e0-activation-geometry.md), [`27`](27-phase8e-controlled-interleaving.md), [`28`](28-phase9-10-center4-scaling-and-infinite-tail-closure.md).  
**Holdout:** `K=13` remains frozen and was not used for representation development.

## 1. What survived two refinement steps

The frozen reconstruction pipeline is now

```text
current persistent presentation
    -> local next-layer effect detection
    -> CanonicalDecomposition
    -> minimum process-generated completion support
    -> task-relative objectification
    -> global history placement / controlled interleaving
    -> exact semantic red team
    -> repeat without changing the rules.
```

At center 2 -> 3:

\[
\boxed{843F_{\rm ren}\oplus0F_{\rm res}\oplus6F_{\rm comp}.}
\]

At center 3 -> 4:

\[
\boxed{2746F_{\rm ren}\oplus0F_{\rm res}\oplus7F_{\rm comp}.}
\]

In both steps the apparent nonbranching sector is only history/decoder reindexing: witness boundary and mode remain fixed and event rank shifts by `+2`.  Therefore Sonnet 001 supplies **no discrete evidence for `ObserverConnection`**.

## 2. Phase 8 — center-3 representation closure

The six center-3 completion states require minimum raw wall supports

\[
1,2,2,2,3,4,
\]

all genuinely new at center 3.  Two minimum raw grammars over-refine their tasks and are objectified by exact quotients

\[
11\to7,
\qquad
13\to3.
\]

A local persistent graft has

```text
376 tree nodes / 125 internals / 200 terminal-merged DAG nodes
peak/worst = 75/12,
```

while a fresh center-3 tree has the same `376/125` inventory but `72/10`.  Old-prefix reweighting alone cannot close the placement gap.

Controlled interleaving over only

```text
21 old wall signs + 7 generated completion-wall signs
```

creates 2,753 exact feasible items and 75 task semantics, and recovers

```text
weighted depth 135
376 tree nodes
125 internals
200 DAG nodes
peak/worst 72/10.
```

Thus

\[
\boxed{
\text{completion determines decision content};
\quad
\text{interleaving/reconvergence determines history partial order and sharing}.
}

## 3. Phase 9A — frozen-rule scaling to center 4

The Phase-8E 28-predicate visible language is materialized as

\[
\boxed{2753\text{ persistent cells},\quad75\text{ tasks},\quad13609\text{ exact closure atoms}.}
\]

The generalized detector is first replayed on center 2 -> 3 and reproduces the exact `841/2/6` sets.  Applied unchanged to center 3 -> 4 it gives

\[
\boxed{2744\text{ stable}+2\text{ nonbranching pressure}+7\text{ completion pressure}.}
\]

Only `9/2753 ≈ 0.327%` of current cells are reopened.

## 4. Phase 9B — semantic red team and an important correction

The two nonbranching cells are again history reindexing.  All seven completion cells genuinely branch.

A stale essay draft had recorded task multiplicities `2,2,3,3,4,4,4`.  That assertion was rejected.  The current lazy oracle gives

\[
\boxed{3,3,3,3,3,3,3}.
\]

An independent local full-stratum center-4 oracle agrees with the lazy task set on all nine pressure cells, so the corrected profile is frozen.

The lazy oracle also queries latent older walls.  Phase 9C later removes all of them from every minimum support.  Therefore

\[
\boxed{
\text{solver/certificate trace}\neq\text{task-minimal representation ontology}.
}
\]

Exact closure provenance remains a useful research backend, but the Sonnet evidence does not force a public `ConstraintCell` ontology.

## 5. Phase 9C — one shared center-4 primitive

Every one of the seven center-4 completion cells has minimum support size one, and all choose the same genuinely new ternary wall:

\[
\boxed{\frac{u_4}{u_3}\ ?\ \frac{19}{11}.}
\]

For every branching cell,

```text
sign(u4/u3 - 19/11) = -1, 0, +1
```

maps one-to-one to its three exact task semantics.  Every minimum support has `(new, latent)=(1,0)`.

No universal one-wall-per-layer law is inferred.

## 6. Phase 9D — center-4 persistent update

Appending the discovered wall globally produces the 29-predicate center-4 presentation:

```text
center 3 baseline
  cells/tasks              2753 / 75
  tree/internal/DAG         376 / 125 / 200
  peak/worst/weighted        72 / 10 / 135

center 4
  cells/tasks              3067 / 81
  closure atoms            14967
  tree/internal/DAG         391 / 130 / 211
  peak/worst/weighted        75 / 10 / 135.
```

The semantic update therefore costs only

\[
\boxed{\Delta\text{internal}=5,\quad\Delta\text{DAG}=11,\quad\Delta\text{task}=6}
\]

while current-use weighted depth stays exactly 135.  The new predicate occurs at five internal nodes, two cross-parent, with earliest activation depth six.

## 7. Phase 10A/B — center 5 is an exact no-op

The unchanged center 4 -> 5 detector gives

\[
\boxed{3067\text{ stable}+0+0.}
\]

This zero-pressure result is independently red-teamed by comparing every center-5 enter/exit event against the current witness on every exact closure atom:

\[
14967\times8=119736.
\]

The exact result is

```text
strictly later      119736
earlier/equal            0
unresolved               0.
```

So the complete center-5 contact alphabet cannot change any first-witness semantic.

## 8. Phase 10C — finite representation closes the infinite contact tail

For each positive-speed runner the earliest event among all centers `n >= 5` is its center-5 enter event:

\[
\alpha_{5,\mathrm{enter}}
=5-\delta
=\frac{24}{5}.
\]

For every future event,

\[
\alpha_{n,\mathrm{kind}}\ge\frac{24}{5}.
\]

The finite anchor certificate checks only

\[
14967\times4=59868
\]

closure-atom/runner comparisons.  All are strictly later than the current first witness; none are earlier/equal or unresolved.

Hence

\[
\boxed{
\text{the finite 29-predicate center-4 presentation is sufficient for the first-witness semantics of the entire infinite remaining contact alphabet.}
}
\]

There is no reason to scan center 6, 7, 8, ... separately.

## 9. What this says about Shakespeare

The strongest structural result from Sonnet 001 is now

```text
open-ended process history
    -> task-safe quotient
    -> sparse generated completion
    -> task objectification
    -> history interleaving/reconvergence
    -> repeated frozen-rule update
    -> finite semantic closure of an infinite future tail.
```

This is more informative than a smaller solver tree.  The presentation itself becomes a finite sufficient statistic for an infinite task-relevant future.

But several boundaries remain essential:

- certificate/provenance information can be richer than visible task representation;
- history placement is separate from primitive decision discovery;
- current-use cost, future-refinement cost, and frontier geometry are separate axes;
- Sonnet history reindexing is not observer transport;
- one successful discrete process is not enough to promote activation/reconvergence into `src/`.

## 10. Current API judgment

Retain as research roles:

```text
ProcessDirection
ConstraintCanonicalization      # first concrete backend
ObserverConnection              # only where the canonical observer truly moves
CanonicalDecomposition          # backend-neutral result shape
```

Do **not** yet promote:

```text
Completion
ResidualQuotient
ConstraintCell
PersistentDAG
Activation/Reconnection
scalarized future cost
discrete ObserverConnection.
```

Phase 9–10 strengthens the presentation/history theory, not the observer-connection theory.

## 11. Next research gate

The contact-center axis is closed.  Continuing to center 6 would be redundant.

The next useful experiment should be **independent pressure**, not another Lonely Runner depth layer:

1. choose an unrelated process problem where a representation genuinely grows and later distinctions can reconverge;
2. ask whether the same separation
   `generated completion -> task objectification -> history interleaving/reconvergence`
   appears without importing Sonnet-specific walls;
3. only then consider a public activation/reconvergence abstraction.

Separately, the original observation-path / observer-ODE programme should return to a problem with an actually moving canonical frame.  Sonnet 001 is now a negative control for conflating history geometry with observer connection.

`K=13` remains a frozen holdout rather than a representation-development target.

## 12. Execution ledger

```text
8A    841 / 2 / 6 local classification                         PASSED
8B    discrete observer-transport interpretation               REJECTED
8C    center-3 minimum raw support 1,2,2,2,3,4                 PASSED
8C.2  task objectification 11->7, 13->3                        PASSED
8D    persistent graft 376/125/200                             PASSED
8D.2  old-prefix cost red team                                 PASSED
8E.0  clean activation; no shared-clean activation             PASSED
8E    controlled interleaving recovers 72/10                   PASSED
9A    frozen detector -> 2744 / 2 / 7                          PASSED
9B    2 reindex + seven 3-task completions                     PASSED
9C    seven one-wall completions, common 19/11 wall            PASSED
9D    3067 cells / 81 tasks / 391/130/211                      PASSED
10A   center-5 pressure = 3067 / 0 / 0                         PASSED
10B   119736 center-5 comparisons all strictly later           PASSED
10C   59868 anchors close every contact center n>=5             PASSED
```

## 13. Claim boundary

No new Lonely Runner theorem is proved.  The infinite-tail closure concerns the declared four-runner relative-speed process and its first-witness contact semantics.  It is not a proof that all Lonely Runner questions reduce to 29 predicates, nor a universal finite-presentation theorem.

## 14. References

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

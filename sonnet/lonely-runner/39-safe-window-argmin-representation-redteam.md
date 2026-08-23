# Phase 14C — pairwise completion versus process-native minimum-group observation

**Status:** exact local representation red team passed.  
**Scope:** the single exceptional K=4 safe-window parent from Phase 14A/B.  
**Engineering boundary:** comparison only; no new primitive or public API is introduced.

## 1. Question

Phase 14B identifies one real three-event next-enter race whose seven closer tasks are exactly the seven nonempty minimum subsets of three candidates.  The minimum pairwise grammar contains all three ternary event-time comparisons, but the exact argmin regions are not clean-separable under that grammar.

The next question is deliberately local:

> what representation cost is created if the three pairwise comparisons are completed into ordinary total sign states, compared with simply retaining the minimum group already produced by the canonical process step?

This is not a claim that one seven-way process observation has the same primitive cost as one pairwise comparison.  The purpose is to expose representation over-refinement before any scalar cost model is chosen.

---

## 2. Exact pairwise completion inside the real parent closure

Use the three exact equality coordinates found in Phase 14B:

\[
(u_2/u_1)?9/4,
\qquad
(u_3/u_1)?7/2,
\qquad
(u_3/u_2)?14/9.
\]

Enumerate all `3^3=27` ternary sign assignments and keep only those consistent with the real parent closure.

Exactly

\[
\boxed{13}
\]

complete sign states are feasible.

These are precisely the weak total orderings of three event times.  They map to only

\[
\boxed{7}
\]

safe-window closer tasks.

Hence full pairwise completion creates

\[
\boxed{13-7=6}
\]

extra states whose only role is to remember order among nonminimal events.

That extra order is not part of the closer task.

---

## 3. Optimal pairwise decision tree

Over the 13 exact feasible complete sign states, optimize a ternary comparison tree lexicographically by

1. uniform-state weighted decision depth;
2. tree nodes;
3. worst depth;
4. internal nodes.

The exact optimum is

```text
feasible complete sign states       13
closer tasks                         7
uniform-state weighted depth        26
average depth                     26/13 = 2
worst depth                          2
tree nodes                          13
internal nodes                       4
width profile                     1, 3, 9
peak frontier                        9
terminal-merged DAG nodes           11
```

The depth-2 result does **not** contradict the clean obstruction.

A normal pairwise tree is allowed to ask a comparison even when one exact argmin task-region does not decide that loser/loser relation.  Operationally it splits that task-pure region into several completed sign states, then may stop early once the minimum is known.

A clean tree forbids exactly that representational side effect.

So the distinction is:

```text
ordinary pairwise tree
    may refine task-irrelevant loser order

clean pairwise tree
    may only route already-resolved exact task regions
```

For this real parent, the first exists and the second does not.

---

## 4. Process-native minimum-group representation

The canonical symbolic process already computes the exact next simultaneous minimum group when it advances to the next contact event.

For the exceptional parent its possible values are exactly

\[
\{1\},\{2\},\{3\},
\{1,2\},\{1,3\},\{2,3\},
\{1,2,3\}.
\]

Thus the task quotient itself has seven values and carries no loser-order distinctions.

This is a smaller representation in the specific sense

\[
\boxed{
7\text{ task values}
\quad\text{versus}\quad
13\text{ completed pairwise sign states}.
}
\]

It should **not** yet be summarized as “one minimum-group operation is cheaper than two pairwise comparisons.”  Primitive computational cost, implementation cost, decoder cost and transfer behavior have not been calibrated independently.

---

## 5. Interpretation

The experiment isolates three levels that must remain separate:

1. **information sufficiency:** all three pairwise comparisons are enough to determine the closer;
2. **clean placement:** the seven exact argmin regions cannot be classified by pairwise queries without splitting some loser-order ambiguity;
3. **process-native objectification:** the canonical process transition already has the minimum group as its natural outcome.

The third observation creates research pressure to test a multiway process object in other domains, but it does not create API pressure by itself.

In particular, no `ArgminPrimitive`, `MinimumGroup`, `Race`, or generic `Completion` type is promoted.

---

## 6. Next gate

Further work should now leave this local example rather than optimize it indefinitely.

The correct promotion criterion is independent evidence:

- find an unrelated process problem where pairwise comparisons are sufficient but clean-obstructed for a naturally multiway event task;
- compare its native process object with pairwise completion under matched task semantics;
- only if the same separation reappears should a reusable abstraction be discussed.

Until then the Phase-14 result remains a Sonnet-specific executable calibration.

## Claim boundary

No new Lonely Runner theorem is proved.  The `13 -> 7` over-refinement count and pairwise tree metrics are exact only for the declared exceptional K=4 safe-window parent and the three process-generated comparison coordinates above.

# Phase 12B — lazy task DAG eliminates the five-speed sign-cell explosion

**Status:** exact bounded constructive calibration implemented.  
**Implementation:** `sonnet/lonely-runner/python/five_speed_lazy_task_dag.py`.  
**Executable calibration:** `tests/research/test_lonely_runner_five_speed_lazy_task_dag.py` (opt-in via `AEG_RUN_LR_FIVE_SPEED_LAZY_DAG=1`).  
**Scope:** same five-speed domain as Phase 12A; no `K=13` data.

## 1. The Phase-12A failure mode

Phase 12A transfers the canonical-first mechanism to five relative speeds and finds a controlled semantic/predicate layer:

```text
3,397 symbolic states
1,117 terminal exact regions
98 generated candidate coordinates
33 canonical witness tasks
36 exact-minimum canonical coordinates
```

But fully materializing all 36 coordinate signs produces

\[
69,683
\]

exact sign cells.

That is a `48.7x` jump from the four-speed canonical carrier, even though canonical task classes grow only `25 -> 33`.

So the question for Phase 12B is not whether the task can be represented by 36 walls.  Phase 12A already proves that.  The question is:

> Must those walls be completed into a global joint sign arrangement before a decision program can use them?

The answer is no, strongly.

---

## 2. Operate directly on exact terminal closure regions

Start from the 1,117 terminal regions already produced by the horizon-free canonical compiler.  Each atom carries

```text
exact multiplicative closure
+ canonical witness task.
```

At a decision node, consider one of the 36 exact-minimum canonical coordinates.

For each current atom:

1. if the closure already forces the wall sign, route the atom unchanged;
2. if the sign is unresolved, refine only that atom into feasible sign children by exact closure;
3. reject infeasible sign children immediately;
4. stop when every atom at a node has the same canonical task.

This is a lazy analogue of Huffman placement: predicates are queried only when they are useful along the current history, and geometric completion is delayed until a query actually requires it.

---

## 3. Greedy policy: preserve closure geometry first

The first constructive policy is deliberately simple and auditable rather than globally optimal.

For every candidate predicate at the current node, score lexicographically by:

1. number of additional closure refinements the query would force;
2. total child atom count;
3. worst remaining task count in a child;
4. total remaining task ambiguity;
5. worst child atom count.

Coordinate order breaks exact ties.

Thus the policy explicitly prefers a task distinction that the current symbolic geometry already knows over one that would first require manufacturing new sign cells.

---

## 4. Strong result: the required closure refinement is exactly zero

The completed decision tree classifies all 33 canonical tasks with

\[
\boxed{0}
\]

additional closure refinements.

Equivalently,

```text
starting exact atoms          1,117
unique exact atoms visited    1,117
new split atoms                   0
```

At every selected decision node, the queried coordinate is already forced on every exact region reaching that node.

This is much stronger than merely reducing the `69,683` static sign cells.

The full sign arrangement is not a compressed version of the necessary computation; it is an object that this classifier never needs to construct at all.

---

## 5. The resulting adaptive tree is small

The exact task-safe tree has

```text
tree nodes       235
internal nodes    78
leaves            157
worst depth        15
peak frontier      36
```

with width profile

```text
1, 3, 3, 3, 3, 9, 21, 36, 33, 21, 21, 18, 21, 15, 18, 9
```

The root is

\[
\boxed{\frac{u_5}{u_1}\ ?\ 5.}
\]

This is not an arbitrary computational choice.  It is exactly the analytic threshold identified before the five-speed experiment:

- below `u5/u1 < 5`, every initial exit occurs before the fastest first enter and the first witness is forced;
- above that boundary, contact interleaving becomes nontrivial.

The decision representation therefore rediscovers the first qualitative phase boundary of the canonical process as its root predicate.

---

## 6. Reconvergence gives a 99-node DAG

Merge structurally identical subtrees and merge equal task leaves.

The resulting DAG has

```text
DAG nodes          99
internal nodes     66
task leaves        33
```

So the hierarchy is now

```text
69,683 globally materialized sign cells
    vs
1,117 exact lazy terminal regions
    -> 235-node adaptive decision tree
    -> 99-node reconverged task DAG.
```

The task leaf count is exactly the 33 canonical witness semantics, while only 66 internal decision states remain after structural sharing.

This is the first five-speed evidence that the persistent/reconvergent history idea from the earlier Sonnet programme survives the canonical-first reconstruction and becomes more important under runner-dimension growth.

---

## 7. Exact usage red team on both sides of the threshold

A small deterministic rational usage grid is used only after the continuous-domain classifier is frozen.

Scale-fix `u1=1` and choose the remaining four speeds from

```text
3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 41/8.
```

This gives

\[
\binom94=126
\]

exact usage tuples, including 56 tuples with `u5/u1 > 5` but still below `21/4`.

Against an independent exact torus-event oracle:

```text
classification errors       0 / 126
lazy decision depth total      317
canonical event depth total    921
lazy average depth           2.516
canonical event average      7.310
lazy worst usage depth          11
canonical event worst           25
```

This is not an optimality claim.  The greedy tree was not selected to minimize this usage distribution.  Nevertheless it already gives a substantial execution-depth reduction while preserving exact continuous-domain task correctness.

---

## 8. What Phase 12B changes conceptually

The five-speed bottleneck found in Phase 12A was

\[
\text{minimum predicates}
\to
\text{global joint sign completion}
\to
69,683\text{ cells}.
\]

Phase 12B shows that this arrow is optional.

The better order is

\[
\boxed{
\text{canonical terminal regions}
\to
\text{adaptive predicate placement}
\to
\text{refine only if queried and unresolved}
\to
\text{reconverge equal residual tasks}.
}
\]

On the present calibration the middle refinement step happens zero times.

So the representation lesson is sharper than “use a DAG instead of a tree”:

> **Do not complete a predicate coordinate globally merely because it belongs to a globally sufficient basis.**

Predicate content and predicate materialization are separate decisions.

This is the runner-dimension analogue of the earlier distinction between canonical process state and compiled wall ontology.

---

## 9. Relation to Huffman/history geometry

The current tree is Huffman-like in the sense that it allocates task distinctions adaptively along history, but it is **not** the exact lexicographic Huffman optimum used in the small four-speed carrier.

That distinction should remain explicit.

At five speeds the more important result is currently an existence result:

```text
exact continuous-domain classifier
+ zero closure refinement
+ 235 tree nodes
+ 99 DAG nodes
```

versus a 69,683-cell full materialization baseline.

Only after the lazy representation itself is frozen should we ask whether a stronger dynamic program can improve weighted depth or frontier shape without reintroducing static-cell explosion.

---

## 10. Next gate

The next question is no longer “can the Phase-11 mechanism survive one more runner?”  At this bounded scale, it does.

The next two useful pressures are:

1. **optimize within the lazy region representation:** search for a better space-time Pareto placement while forbidding unnecessary global refinement;
2. **widen the five-speed relative domain:** move beyond `21/4` and measure whether zero-refinement adaptive classification persists or where genuine region completion first becomes unavoidable.

The second is especially informative for `F_comp`: it would identify a representation-growth transition generated by runner-dimensional dynamics rather than by an arbitrary contact-center horizon.

`K=13` should remain frozen.

## Claim boundary

No new Lonely Runner theorem is proved.  The zero-refinement classifier, `235/78/157`, `99/66/33`, root `u5/u1 ? 5`, and `317 vs 921` usage-depth values are exact for the Phase-12A five-speed domain and the stated deterministic greedy policy.  No global optimality or asymptotic scaling claim is made.
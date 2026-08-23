# Phase 12C — clean-separator recursion is stable under five-speed domain widening

> **Phase-15A claim boundary.**  The `Clean` conclusions below remain exact for
> the declared partial-sign systems.  However, a partial singleton-separator
> argument is not a generic proof that the reported basis is cardinality-minimum
> in the complete sign grammar.  Only the base `u5/u1<21/4` counts have received
> the stronger full-coordinate deletion certification so far.  See
> [`40-global-closure-contract-and-theory-audit.md`](40-global-closure-contract-and-theory-audit.md).

**Status:** exact bounded domain-sweep calibration implemented.  
**Implementation:** `sonnet/lonely-runner/python/five_speed_clean_separator_sweep.py`.  
**Executable calibration:** `tests/research/test_lonely_runner_five_speed_clean_separator_sweep.py` (opt-in).  
**Scope:** five ordered relative speeds, `delta=1/6`; `K=13` remains frozen.

## 1. Question after Phase 12B

Phase 12B finds something stronger than a small tree on the first nontrivial five-speed domain `u5/u1 < 21/4`:

> every queried predicate is already decided by every exact terminal region reaching that decision node.

So the adaptive classifier performs **zero closure refinement**.

This can be stated as a recursive geometric property.

Call a coordinate a **clean separator** for a task-labeled region family when:

1. its sign is forced on every region in that family;
2. it splits the family into at least two nonempty sign branches;
3. the residual task ambiguity decreases recursively until every leaf is task-pure.

A recursively clean tree classifies the task without ever completing an unresolved sign coordinate.

Phase 12C asks whether this was an accident of the narrow `21/4` domain.

---

## 2. Exact widening sweep

Recompute from scratch at

\[
\frac{u_5}{u_1}<
\frac{21}{4},\
\frac{11}{2},\
\frac{23}{4},\
6,\
\frac{25}{4}.
\]

At every width the experiment repeats the full causal chain:

```text
horizon-free canonical contact process
-> terminal exact closure regions
-> process-generated candidate coordinates
-> canonical-witness task projection
-> exact singleton-certified minimum coordinate basis
-> clean-separator recursion only.
```

No tree or predicate basis is transferred from the narrower domain.

---

## 3. Exact results

| `u5/u1 <` | symbolic states | terminal regions | generated coords | canonical tasks | min coords | tree nodes | internal | DAG nodes | worst | peak |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `21/4` | 3,397 | 1,117 | 98 | 33 | 36 | 235 | 78 | 99 | 15 | 36 |
| `11/2` | 5,603 | 1,909 | 104 | 41 | 42 | 304 | 101 | 119 | 15 | 48 |
| `23/4` | 7,112 | 2,491 | 105 | 41 | 42 | 304 | 101 | 122 | 15 | 48 |
| `6` | 12,256 | 4,405 | 107 | 42 | 43 | 316 | 105 | 122 | 15 | 48 |
| `25/4` | 14,773 | 5,379 | 111 | 48 | 46 | 349 | 116 | 137 | 15 | 63 |

For every row:

```text
clean-separator recursion       PASSED
additional closure refinements  0
root predicate                  u5/u1 ? 5
max witness event index         47
emergent maximum contact center 7
```

Thus the zero-refinement phenomenon survives the entire tested widening window.

---

## 4. The striking separation of growth rates

Across the sweep from `21/4` to `25/4`, the symbolic process becomes much richer:

\[
3,397\to14,773
\]

states, a growth of about `4.35x`, and terminal regions grow

\[
1,117\to5,379
\]

or about `4.82x`.

But the canonical task and compiled decision representation grow much more slowly:

\[
33\to48\quad\text{tasks},
\]

\[
36\to46\quad\text{minimum coordinates},
\]

\[
235\to349\quad\text{tree nodes},
\]

\[
99\to137\quad\text{DAG nodes}.
\]

The worst decision depth remains exactly

\[
\boxed{15}
\]

throughout the sweep.

So domain widening is generating many more exact process regions without generating a comparable number of task distinctions or adaptive decision states.

---

## 5. Root stability has a direct process meaning

Every independently rebuilt tree chooses

\[
\boxed{\frac{u_5}{u_1}\ ?\ 5}
\]

as its root.

This is the same analytic threshold identified before any symbolic computation:

\[
\frac{1}{6u_1}
\ ?\
\frac{5}{6u_5}.
\]

It compares the slowest initial exit with the fastest first enter.

Therefore the root is not merely a robust learned heuristic.  It is the first bifurcation between

```text
all initial exits complete before any re-entry
```

and

```text
exit / re-entry histories can interleave.
```

The persistence of this root as the domain widens is strong evidence that the task DAG is organizing the canonical process around genuine causal phase boundaries.

---

## 6. No genuine region-completion pressure has appeared yet

The main red-team question was where clean-separator recursion would first fail.

It has not failed through

\[
\boxed{u_5/u_1<25/4.}
\]

At every node in every rebuilt classifier, a useful task separator exists whose sign is already forced on every current terminal closure atom.

Hence the representation requires no operation of the form

```text
current exact region
-> query unresolved task wall
-> split/refine region
```

through the tested window.

This does **not** prove a universal zero-completion theorem.  It gives a precise new empirical/theorem-search target:

> characterize when a task-labeled family of canonical process regions admits recursively clean separation by process-generated predicates.

That property is stronger than pairwise task separability and weaker than globally materializing a complete sign vector.

---

## 7. Relation to Hauffman and decision diagrams

The clean-separator tree can be viewed as a decision structure on **partial sign information**.

A terminal closure region does not need a value for every globally sufficient coordinate.  It carries only the signs forced by its process history.  The decision program chooses a coordinate only when that coordinate is already meaningful on the entire current family.

This suggests that the natural downstream object is closer to a task-directed decision diagram over partial geometric signatures than to a complete hyperplane/sign arrangement.

The structural pipeline is now

\[
\boxed{
\text{canonical process regions}
\to
\text{partial predicate signatures}
\to
\text{clean adaptive decisions}
\to
\text{reconvergent DAG}.
}
\]

This provides a more precise formulation of the earlier persistent-Hauffman intuition.

---

## 8. What should be proved next

Two mathematical questions now dominate engineering scale-up.

### A. Clean-separator criterion

Given task-labeled exact regions `R_a` and process-generated coordinates `c_j`, identify a local condition guaranteeing the existence of a coordinate that is:

- resolved on every current region;
- task-separating;
- recursively preserves the property in each child.

An exact characterization would turn the observed zero-refinement behavior into a theorem about representation closure.

### B. First failure / genuine completion frontier

Continue widening the domain until the clean property first fails.

At that first node, record the unresolved coordinate(s) required to separate distinct tasks.  That would be a much cleaner candidate for genuine representation-relative `F_comp` than the old contact-center completion walls, because it would occur **after process canonicalization and task objectification**.

This is now the preferred operational definition of the next completion experiment.

---

## 9. Current judgment

The five-speed transfer has moved beyond a one-point scaling success.

Within the tested domain window, increasing process complexity is largely absorbed by canonical regions and task quotienting, while the adaptive decision geometry remains compact and requires no new region splitting.

The strongest current statement is therefore:

> On the tested five-speed first-witness domains through `u5/u1 < 25/4`, the canonical task admits a recursively clean decision representation: every task query is already resolved on the process regions where it is asked, so global sign completion and even local closure refinement are unnecessary.

This is a substantially stronger target for later generalization than the raw counts of the Phase-12A static arrangement.

## Claim boundary

No new Lonely Runner theorem is proved.  The sweep results are exact bounded representation statements for the specified five-speed domains.  No asymptotic claim, arbitrary-domain clean-separator theorem, or transfer to `K=13` is asserted.

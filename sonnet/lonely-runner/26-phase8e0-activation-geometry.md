# Phase 8E.0 — clean activation geometry of the seven completion walls

**Status:** exact bounded activation calibration passed.  
**Scope:** frozen center-2 persistent tree; seven Phase-8C new completion walls; no full center-3 census.  
**Successor:** controlled interleaving in [`27-phase8e-controlled-interleaving.md`](27-phase8e-controlled-interleaving.md)

## 1. Question

Phase 8D.2 showed that reweighting only the old 21-wall prefix cannot recover the
fresh center-3 placement target.  Before changing the tree architecture, ask a
more local question:

> at what old history depth can each newly generated completion wall be queried
> without branching any surviving old parent that does not itself use that wall?

This defines a deliberately strict notion of activation relative to the frozen
old tree.

## 2. Exact clean-activation condition

For one new wall `w` and one old persistent-tree node, let the surviving
center-2 parents below the node be `S` and let `U_w` be the completion parents
whose frozen Phase-8C raw support uses `w`.

The wall has a **clean activation** when:

1. `S ∩ U_w` is nonempty; and
2. every parent in `S \ U_w` has an exact wall sign already fixed by its
   center-2 multiplicative difference constraints.

A **shared clean activation** additionally requires at least two active users:

\[
|S\cap U_w|\ge2.
\]

Thus clean activation forbids collateral splitting of any old context that does
not need the wall.

The possible signs are certified one wall at a time from the center-2 exact
constraint geometry.  No center-3 child task semantics are used to select the
activation depth.

## 3. Exact activation records

The seven frozen new walls give:

| wall | completion users | unresolved nonusers at root | earliest clean depth | live parents at clean node | active users there | shared clean? |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `u3/u2 ? 14/11` | 1 | 142 | 9 | 1 | 1 | no |
| `u3/u2 ? 16/11` | 1 | 153 | 9 | 1 | 1 | no |
| `u4/u2 ? 7/3` | 4 | 81 | 3 | 19 | 1 | no |
| `u4/u2 ? 8/3` | 4 | 77 | 3 | 19 | 1 | no |
| `u4/u3 ? 14/11` | 1 | 160 | 5 | 7 | 1 | no |
| `u4/u3 ? 14/9` | 1 | 100 | 8 | 1 | 1 | no |
| `u4/u3 ? 16/9` | 2 | 99 | 7 | 5 | 1 | no |

Hence the sorted earliest clean depths are

\[
\boxed{3,3,5,7,8,9,9}.
\]

More importantly,

\[
\boxed{\text{none of the seven walls has a shared clean activation in the frozen old tree}.}
\]

Even the two walls used by four completion parents become clean only after the
old tree has already separated those users so that a single active user remains.

## 4. Why this negative result matters

If cross-parent reuse were obtainable simply by lifting a new query to an old
node where no irrelevant context was split, one of the multi-user walls should
have exhibited a shared clean activation.

It does not.

Therefore a representation that actually shares a new completion decision
across old parent contexts must relax the zero-collateral rule.  Some old
contexts that do not ultimately need the new distinction must be temporarily
split and later semantically reconverge.

This predicts a DAG/history phenomenon rather than a larger completion language:

```text
new wall queried early
    -> collateral branches in old representation
    -> branches that are task-equivalent reconverge
    -> completion users share one decision history prefix.
```

Phase 8E tests exactly this stronger architecture.

## 5. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/activation_geometry.py
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_activation_geometry.py
```

Recorded exact certification:

```text
workflow: Sonnet Lonely Runner Phase 8E Certification
run id:   32587582896
Python:   3.12.14
8E.0:     1 passed in 36.33 s
```

Timing is provenance only.

## 6. Engineering observation

The current certificate recomputes center-2 difference-constraint closure for
many `(system, wall)` pairs.  This is mathematically harmless but operationally
wasteful.  A future implementation should materialize the center-2 closure as a
reusable system certificate before using activation geometry inside a search
loop.

This is an implementation-pressure result, not a new mathematical abstraction.

## 7. Claim boundary

The absence of shared **clean** activation does not prove that cross-parent
interleaving is impossible.  Clean activation is intentionally stronger than
semantic admissibility: stable contexts are allowed, in principle, to split on
a new wall and later reconverge to the same task.

The exact result is relative to the frozen center-2 persistent tree and the
seven Phase-8C walls.

## 8. References

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

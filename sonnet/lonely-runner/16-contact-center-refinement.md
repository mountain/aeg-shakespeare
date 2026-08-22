# Phase 7g — recursive contact-center refinement inside the pair-difference geometry

**Status:** exact manual research calibration; still Gate A.  
**Question:** when the contact alphabet deepens, does the objectified task geometry grow like the naive pair-product space, or much more slowly?

Executable manual script:

```text
sonnet/lonely-runner/python/pair_difference_refinement.py
```

Manual workflow:

```text
.github/workflows/sonnet-lonely-runner-pair-difference-refinement.yml
```

This experiment is deliberately not in the default five-version CI matrix.

## 1. Why contact-center depth is now the right refinement variable

Phase 7f established a complete four-speed pair-difference geometry for contact centers through `2`.  It transferred exactly through integer speed `13` in the domain

\[
\frac{u_4}{u_1}<8,
\]

and then failed at an explicit speed-14 example because a center-3 contact was required.

That is qualitatively different from sample overfitting.  The correct response is therefore to enlarge the **calculus alphabet** from centers `0..2` to `0..3`, while refining the already-consistent sign graph rather than rebuilding an ambient 3D arrangement from scratch.

## 2. Primitive wall alphabet growth

For `delta=1/5` and `u4/u1<8`, centers through `2` generate seven collision ratios and hence

```text
15 strata per runner-pair ratio.
```

Centers through `3` generate fifteen collision ratios and hence

```text
31 strata per runner-pair ratio.
```

If all six pair coordinates were treated as independent, the raw product would grow from

\[
15^6=11{,}390{,}625
\]

to

\[
31^6=887{,}503{,}681.
\]

That is a factor of about

\[
77.9\times.
\]

A brute-force Cartesian interpretation would already be heading in the wrong direction.

## 3. Refine existing graph strata instead of restarting

Every center-3 pair stratum lies inside exactly one center-2 stratum.  Therefore each of the `5,823` center-2 realizable sign systems can be refined locally only where a newly introduced contact ratio cuts one of its pair intervals.

After every local refinement, incremental multiplicative cycle closure immediately rejects joint edge assignments that cannot arise from any positive speed tuple.

The exact result is

\[
\boxed{
5{,}823
\longrightarrow
72{,}241
}
\]

realizable graph strata.

So while the independent pair product grew by about `77.9x`, the actual A/M graph geometry grew only

\[
\boxed{12.4\times.}
\]

This is already evidence that cycle objectification is doing nontrivial complexity control across calculus depth.

## 4. The task quotient grows much more slowly again

The center-3 graph has

\[
6\times15=90
\]

primitive wall-sign coordinates.

Using exact first-witness contact semantics, only

\[
\boxed{26}
\]

remain task-relevant.

The complete refinement hierarchy is:

| layer | center <= 2 | center <= 3 | growth |
| --- | ---: | ---: | ---: |
| naive independent pair product | 11,390,625 | 887,503,681 | 77.9x |
| realizable pair-difference systems | 5,823 | 72,241 | 12.4x |
| exact task-safe sign strata | 849 | 1,953 | 2.30x |
| first-witness semantics | 60 | 75 | 1.25x |
| task-relevant wall coordinates | 21 | 26 | 1.24x |

This is the strongest scaling signal in the AM-first line so far.

The raw contact alphabet roughly doubles, but after graph consistency and task quotient the semantic presentation expands only modestly.

In particular:

\[
\boxed{
887.5\text{ million raw combinations}
\to
1{,}953\text{ exact task-safe states}.
}
\]

The important number is not the compression ratio by itself; it is the **growth law under refinement**.

## 5. Hauffman/history geometry after refinement

Use all integer quadruples through speed `10` with `u4/u1<8` only as a usage measure after the center-3 geometry and task map are frozen.  There are

\[
146
\]

such inputs.

### Literal center-3 contact process

Over the complete `72,241`-stratum geometry:

```text
peak frontier       71
boundary volume    625
worst depth         16
```

On the 146 usage inputs:

\[
E[d]_{contact}
=
779/146
\approx5.336.
\]

### Time-first exact task tree

Exact dynamic programming over the `26` retained A/M wall signs gives

```text
weighted depth      377
boundary volume     376
worst depth          10
internal nodes      125
```

or

\[
\boxed{E[d]=377/146\approx2.582.}
\]

The root is again a genuine contact comparison:

\[
\boxed{u_4/u_1\ ?\ 4.}
\]

Its peak frontier is `72`, so—as in Phase 7f—the time-optimal point is allowed to spend one unit of peak space.

### Balanced space-time point

Force the first wall to

\[
\boxed{u_3/u_1\ ?\ 6}
\]

and exactly re-optimize every descendant.  The resulting tree has

```text
weighted depth      505
boundary volume     376
peak frontier        63
worst depth          11
```

hence

\[
E[d]=505/146\approx3.459.
\]

Relative to literal contact evolution:

\[
\boxed{
\begin{aligned}
W_{\max}:&\quad71\to63,\\
\sum W(d):&\quad625\to376,\\
d_{\max}:&\quad16\to11,\\
E[d]:&\quad5.336\to3.459.
\end{aligned}
}
\]

Again, the Hauffman object is doing what we wanted: it exposes a genuine space-time Pareto frontier rather than hiding the trade-off in one scalar score.

## 6. Frozen transfer improves substantially with calculus depth

Freeze the entire center-3 construction:

- the fifteen contact ratios;
- pair-difference cycle closure;
- the 26 task-relevant walls;
- the 1,953-stratum task map;
- both decision trees.

Then test every integer quadruple through speed `22` satisfying `u4/u1<8`:

\[
\boxed{5{,}151/5{,}151\text{ exact}.}
\]

No contact wall or task rule is learned on that holdout.

The first observed failure is at

```text
(3, 9, 13, 23)
```

where a center-4 contact is required.

So the hierarchy is now explicit:

```text
center <= 2 geometry
    exact through speed 13
    first new-contact failure at 14

center <= 3 geometry
    exact through speed 22
    first new-contact failure at 23
```

This is precisely the behavior a refinement calculus should have: the failure points announce the next missing process layer rather than appearing as unexplained generalization errors.

## 7. What this suggests mathematically

The representation now has two orthogonal growth mechanisms:

1. **runner dimension** — add vertices/edges to the pair-difference graph;
2. **contact depth** — refine the finite label alphabet on existing edges.

The experiment suggests that neither should be measured by its raw Cartesian product.

Instead the meaningful hierarchy is

\[
\boxed{
\text{primitive wall alphabet}
\to
\text{cycle-realizable gain/sign systems}
\to
\text{task-safe quotient}
\to
\text{Hauffman decision geometry}.
}
\]

The dramatic contraction of refinement growth from `77.9x` raw to `2.30x` task-safe is the first evidence that this hierarchy may remain manageable as the calculus is deepened.

## 8. Next threshold

The next experiment should not immediately move to five runners or center `4` by brute force.

Two structural questions now deserve priority:

1. **incremental task refinement:** can we identify exactly which of the existing 1,953 task-safe classes are split by the eight newly added center-3 ratios, without enumerating all 72,241 refined realizable systems?
2. **decision DAG objectification:** many optimized tree subproblems represent the same residual sign/task state.  Can those repeated subtrees be merged into a DAG and evaluated with the same Hauffman space-time geometry?

If both work, then adding contact depth may become closer to local refinement of an existing presentation than reconstruction of a new search space.

Only after that should we attempt the next runner dimension.

## Claim boundary

No new Lonely Runner theorem is proved.

What is established at four-speed bounded scale is a new scaling statement about the Shakespeare representation itself:

\[
\boxed{
\text{contact-alphabet refinement grows far faster in raw syntax than in exact task semantics.}
}

The pair-difference/cycle quotient plus Hauffman history geometry captures that contraction explicitly and transferably.

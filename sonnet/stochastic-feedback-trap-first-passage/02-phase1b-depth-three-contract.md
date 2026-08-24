# Phase 1b — frozen depth-three enlargement

**Status:** frozen before execution; result unknown.

Phase 1 closed depth two negatively:

```text
604 literal -> 60 semantic -> 16 increasing affine -> 0 nonlinear
```

Depth three is now opened because the held-out control has an A/M derivation
`u*(1+u^2)` at that depth.  The control remains forbidden as a discovery label.

## Exact bounds and execution method

The commutative binary-tree recurrence predicts exact-depth literal counts

```text
depth 0          4
depth 1         20
depth 2        580
depth 3    364,820
cumulative 365,424
```

Literal materialization at depth three is unnecessary.  Addition and
multiplication respect exact polynomial equality, so one representative of each
depth-two semantic class gives a complete semantic closure at depth three.  The
executor must combine all unordered pairs of the 60 frozen semantic values
under both operations, union them with lower depths, and record the exact new
semantic count.

## Discovery output

The run may report only:

- total and new semantic polynomial counts;
- complete strictly increasing census on `[-1,1]`;
- affine versus nonlinear survivor counts;
- degree/depth/cost histograms independent of the hidden chart;
- whether the post-hoc control occurs, checked only after the census is frozen.

It may not rank, prune, or choose a candidate by similarity to `u+u^3`.  If
multiple nonlinear presentations survive, uniqueness has failed at the grammar
level and must be resolved by stopped-process task semantics in a later gate.

## Failure conditions

The enlargement fails if the semantic closure disagrees with the depth-two
baseline, strict monotonicity relies on sampling, or the held-out chart is used
to direct generation.  An empty nonlinear set and a large nonunique set are
both valid research outcomes.

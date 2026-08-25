# Phase 8C.2 — task-relative objectification of completion residuals

**Status:** exact bounded objectification calibration passed.  
**Scope:** four relative speeds; center-2 -> center-3 contact refinement; first-witness task; still Gate A.  
**Predecessor:** [`22-phase8c-minimum-completion-residuals.md`](22-phase8c-minimum-completion-residuals.md)

## 1. Why Phase 8C was not the endpoint

Phase 8C found minimum-cardinality raw contact-wall supports of sizes

\[
1,2,2,2,3,4
\]

for the six genuine completion parents.  Four raw signatures already had one
sign class per task class.  Two did not:

```text
11 raw sign classes -> 7 first-witness task classes
13 raw sign classes -> 3 first-witness task classes.
```

Thus minimum primitive support was still not minimum task representation.

Phase 8C.2 asks whether the excess raw syntax can be quotiented while retaining
an executable decoder that uses only those selected completion walls.

## 2. Objectification rule

For each completion parent, let `r` be the tuple of signs on its Phase-8C
minimum raw completion walls.  Define the declared first-witness task quotient

\[
r_1\sim_Q r_2
\iff
Q(r_1)=Q(r_2).
\]

This is explicitly task-relative.  It does not claim that two raw residuals with
the same current first witness will remain equivalent under every deeper contact
extension.

To prevent the quotient from becoming merely a renamed task label, Phase 8C.2
also constructs an exact adaptive decoder whose only queries are coordinates of
`r`.  The decoder is replayed on every locally realized raw sign key.

The search orders objectives as

```text
minimum internal decision nodes
    -> minimum worst query depth
    -> minimum child-system-weighted path length.
```

Equal task leaves may be shared in the structural DAG.

## 3. Exact six-parent profiles

The dedicated run produced:

| completion walls | local children | raw classes | task quotient | internal nodes | path leaves | DAG nodes | worst depth | weighted mean depth |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 85 | 11 | 7 | 3 | 7 | 10 | 3 | 1.376471 |
| 2 | 9 | 5 | 5 | 2 | 5 | 7 | 2 | 1.555556 |
| 2 | 25 | 5 | 5 | 2 | 5 | 7 | 2 | 1.440000 |
| 2 | 17 | 5 | 5 | 2 | 5 | 7 | 2 | 1.529412 |
| 4 | 143 | 13 | 3 | 6 | 13 | 9 | 3 | 2.391608 |
| 1 | 9 | 3 | 3 | 1 | 3 | 4 | 1 | 1.000000 |

The two previously over-refined cases therefore close exactly as

\[
\boxed{11\to7},
\qquad
\boxed{13\to3}.
\]

The second case is especially informative: although its minimum raw support has
four walls, no decoder path needs all four.  Its exact adaptive decoder has
worst depth three.

## 4. What the DAG is doing

The `11 -> 7` case can already combine all task-equivalent raw keys before
termination: its decision tree has seven path leaves, exactly the quotient class
count.

The `13 -> 3` case is topologically less contiguous in the raw sign grammar.  It
still has thirteen decision-tree path leaves, but all leaves with the same task
can share one terminal object.  Six internal nodes plus three shared task
terminals give only

\[
\boxed{9\text{ DAG nodes}}
\]

instead of treating thirteen raw sign classes as thirteen persistent objects.

This is a concrete example of why Shakespeare distinguishes execution history
from objectified representation: several different query histories can terminate
at the same semantic object.

## 5. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/residual_objectification.py
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_residual_objectification.py
```

Recorded exact workflow:

```text
workflow: Sonnet Lonely Runner Canonical Decomposition
run id:   32585634379
Python:   3.12.14
8A/8B:    1 passed in 8.07 s
8C:       1 passed in 7.56 s
8C.2:     1 passed in 13.92 s
```

Timing is provenance only.  The scientific certificate is exact decoding on all
locally realized raw completion signatures.

The heavy workflow is restored to manual `workflow_dispatch` after this run.
Routine CI continues to audit the essay structure, citations, and Proof map.

## 6. Representation consequence

The completion pipeline is now experimentally separated into three distinct
operations:

\[
\boxed{
\text{completion pressure}
\to
\text{minimum raw process generators}
\to
\text{task-relative residual objectification}.
}
\]

For this bounded Sonnet, the first operation identifies six parents, the second
finds raw wall supports `1,2,2,2,3,4`, and the third closes all six to exactly
their first-witness task classes.

This strengthens the decision not to promote a universal `Completion` class:
raw generators, quotient semantics, and executable decoder are distinct pieces
of evidence.

## 7. Bridge to Phase 8D

The six local decoder structures can now be attached to the already frozen
center-2 persistent Huffman tree rather than rebuilding a center-3 tree from
scratch.

Phase 8D should measure:

- old tree/DAG nodes reused;
- new internal completion-decoder nodes;
- terminal semantic nodes merged/reused;
- incremental boundary volume and peak frontier;
- extra wall-query depth on completion paths;
- expected incremental depth under the frozen 55-input usage distribution;
- comparison with the previously frozen full center-3 time-first tree.

The key question is now quantitative:

> how much representation growth is actually required to absorb one new process
> layer once completion residuals have been objectified?

## 8. Claim boundary

No new Lonely Runner theorem is proved.  The quotient is exact only for the
bounded first-witness task and the center-2 -> center-3 refinement considered
here.  No future-depth equivalence is claimed.

The adaptive decoder is a finite local execution strategy, not a package-level
normal form and not a claim that its objective is the universal Huffman cost.

## 9. References

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

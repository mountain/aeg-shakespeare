# Phase 8 — persistent Hauffman geometry, canonical decomposition, and minimal completion

**Status:** Phase 8A passed; Phase 8B rejected the proposed observer-transport interpretation; Phase 8C minimum raw completion passed; residual objectification is next.  
**Branch:** `research/canonical-observer-api`  
**Result notes:** [`20-phase8a-discrete-canonical-decomposition.md`](20-phase8a-discrete-canonical-decomposition.md), [`21-phase8b-history-reindex-red-team.md`](21-phase8b-history-reindex-red-team.md), [`22-phase8c-minimum-completion-residuals.md`](22-phase8c-minimum-completion-residuals.md)  
**Open frontier policy:** `K=13` remains a frozen holdout and is not used for representation development.

## 1. Current structural result

The center-2 -> center-3 four-speed first-witness refinement now has the exact local structure

\[
\boxed{
841\text{ identity-stable}
+2\text{ history reindex}
+6\text{ genuine completion pressure}.
}
\]

The corresponding canonical sectors are

\[
\boxed{
843\;F_{\rm ren}
\oplus
0\;F_{\rm res}
\oplus
6\;F_{\rm comp}.
}
\]

The two nonbranching updates do **not** move the canonical witness geometry: both preserve the same runner-1 center-1 exit boundary and interval mode and only shift the history event rank by `+2`.  They are decoder/history renormalization, not observer transport.

This negative result is binding.  Sonnet 001 currently supplies no discrete evidence for `ObserverConnection`.

## 2. Observation-locality rule

All Phase-8 discovery before local completion may use only:

- the current persistent task-safe state;
- its certified contact/witness prefix;
- pair-difference cycle closure;
- the newly admitted contact layer;
- finite local order relations involving the old causal prefix;
- declared task semantics.

The complete next-layer census, deeper future contact layers, complete propagators, and `K=13` data are forbidden as representation-selection inputs.

## 3. Phase 8A — behavioral classification: PASSED

From old state plus the new contact layer define

```text
A = forced_earlier
B = effective_unresolved_crossing

stable              = not A and not B
nonbranching_update = A and not B
completion_pressure = B.
```

This local classifier produces `841 / 2 / 6` before center-3 child semantics are evaluated.  Local refinement then verifies two one-to-one changes and six genuine semantic splits while reopening only 26 of the 5,823 old full sign systems and evaluating 298 children rather than the full 72,241-state center-3 census.

## 4. Phase 8B — proposed observer transport: REJECTED

Exact witness records:

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval').
```

Same boundary, same mode, `+2` event rank.  Therefore the two states join the renormalizable sector and `F_res` is empty in this calibration.

Result note 21 records the negative argument and its implication for task semantics: intrinsic witness geometry must be separated from history-location metadata before an observer connection is claimed.

## 5. Phase 8C — minimum raw completion: PASSED

For each of the six genuine `F_comp` parents, generate every varying center-3 pair/contact wall sign available in its local child geometry.  Do not provide a target wall family.

For every cross-task pair of children, a candidate wall covers the conflict when their signs differ on that wall.  Exact dynamic programming over the conflict-cover bitset finds a minimum-cardinality raw wall signature.

The six minimum wall counts are

\[
\boxed{1,2,2,2,3,4}.
\]

Every selected wall is **new at center 3**.  No selected minimum completion needs a latent old wall that had already been quotiented away.

The union of selected local minimum supports contains seven distinct new contact walls:

\[
\begin{aligned}
\frac{u_3}{u_2}&\ ?\ \frac{14}{11},
&\frac{u_3}{u_2}&\ ?\ \frac{16}{11},\\
\frac{u_4}{u_2}&\ ?\ \frac73,
&\frac{u_4}{u_2}&\ ?\ \frac83,\\
\frac{u_4}{u_3}&\ ?\ \frac{14}{11},
&\frac{u_4}{u_3}&\ ?\ \frac{14}{9},
&\frac{u_4}{u_3}&\ ?\ \frac{16}{9}.
\end{aligned}
\]

Four parents reach the exact task quotient directly in their minimum raw sign grammar.  Two remain over-refined:

```text
7 task semantics <- 3 walls -> 11 residual classes
3 task semantics <- 4 walls -> 13 residual classes.
```

Therefore Phase 8C proves minimum **raw generator support**, not minimum task representation.

Dedicated exact run:

```text
workflow: Sonnet Lonely Runner Canonical Decomposition
run id:   32584599992
Python:   3.12.14
8A/8B:    1 passed in 8.04 s
8C:       1 passed in 7.55 s.
```

Full proof map and boundary are in result note 22.

## 6. API consequence

Phase 8 has now separated three layers that must not be conflated:

```text
completion pressure
    !=
minimum raw process-generator support
    !=
minimum task representation.
```

`CanonicalDecomposition` answers the first question.  Phase 8C provides a research-local exact backend for the second.  The two over-refined cases show that a public universal `Completion` abstraction is still premature: a task-relative quotient/objectification may be required after raw closure.

`ObserverConnection` remains supported by continuous examples with genuine observer motion, not by this Sonnet refinement.

## 7. Next step — residual objectification / Phase 8D bridge

The immediate task is the two over-refined completion parents.

For each one:

1. start from its already-minimum raw wall support;
2. compute the exact map from raw ternary sign patterns to child task semantics;
3. search for a compact compound residual/objectification with exactly 7 or 3 semantic values;
4. require a construction recipe from the A/M pair-difference/contact grammar rather than an opaque label;
5. certify exact decoder reconstruction;
6. compare description size and update cost against both the raw wall tuple and the opaque persistent-parent-ID baseline.

For the four parents whose minimum raw signatures already have exactly the correct number of residual classes, freeze those signatures as provisional local completion primitives.

Only after all six residuals are objectified should the center-2 -> center-3 persistent DAG be assembled and its incremental Hauffman geometry measured.

## 8. Persistent Hauffman DAG target

The eventual Phase-8D metrics should separate

```text
old DAG nodes reused
history/decoder reindex updates
new residual primitives allocated
extra process decisions on split paths
incremental peak frontier / boundary volume
incremental expected / worst depth
future refinement cost.
```

The target remains a Pareto geometry rather than a single cost scalar.

## 9. Future moving-observer / ODE experiment

The ODE intuition remains a separate research direction.  Phase 8B demonstrates that one-to-one task change is not enough to trigger it.

A future discrete connection experiment must first exhibit an **actual changing local canonical frame inside a fixed observer family**.  History index shifts, decoder changes, or longer prefixes do not qualify.

Thus a moving contact-frame/observer-ODE experiment is deferred until such a state is independently found.

## 10. Execution order

```text
8A  local 841 / 2 / 6 behavioral classification                PASSED
8B  observer-transport interpretation of the two updates        REJECTED
    corrected canonical sectors = 843 / 0 / 6
8C  minimum raw wall support for six completion states           PASSED
    sizes = 1,2,2,2,3,4; all selected walls new at center 3
8C.2 objectify the two over-refined raw residuals                 NEXT
8D  build persistent DAG and incremental Hauffman geometry
future: search separately for a true moving-observer discrete example
```

## 11. Claim boundary

No new Lonely Runner theorem is proved.  The current exact bounded representation result is:

\[
\boxed{
843\text{ current-representation states}
\oplus
6\text{ completion states},
}
\]

with the six completion states requiring minimum raw process supports of sizes `1,2,2,2,3,4` in the declared center-3 wall grammar.  Two of those raw completions still retain task-irrelevant distinctions and therefore are not yet canonical new primitives.

## 12. References

[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in R. E. Miller and J. W. Thatcher (eds.), *Complexity of Computer Computations*, The IBM Research Symposia Series, Plenum Press, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

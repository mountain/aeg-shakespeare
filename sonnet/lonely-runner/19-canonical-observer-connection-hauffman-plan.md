# Phase 8 — persistent Hauffman geometry, canonical decomposition, and controlled interleaving

**Status:** Phases 8A, 8C, 8C.2, 8D, and 8D.2 passed; Phase 8B rejected the proposed discrete observer-transport interpretation.  
**Branch:** `research/canonical-observer-api`  
**Result notes:** [`20-phase8a-discrete-canonical-decomposition.md`](20-phase8a-discrete-canonical-decomposition.md), [`21-phase8b-history-reindex-red-team.md`](21-phase8b-history-reindex-red-team.md), [`22-phase8c-minimum-completion-residuals.md`](22-phase8c-minimum-completion-residuals.md), [`23-phase8c2-residual-objectification.md`](23-phase8c2-residual-objectification.md), [`24-phase8d-persistent-dag-increment.md`](24-phase8d-persistent-dag-increment.md), [`25-phase8d2-refinement-aware-placement.md`](25-phase8d2-refinement-aware-placement.md)  
**Open frontier policy:** `K=13` remains a frozen holdout and is not used for representation development.

## 1. Frozen local semantics

The exact center-2 -> center-3 decomposition is

\[
\boxed{843F_{\rm ren}\oplus0F_{\rm res}\oplus6F_{\rm comp}.}
\]

More explicitly:

```text
841 identity-stable
  2 history/decoder reindex
  6 genuine completion states.
```

Phase 8B established that the two nonbranching states do not move the canonical witness geometry: they preserve boundary and mode and only shift event rank by `+2`.  Sonnet 001 therefore still provides no discrete evidence for `ObserverConnection`.

All completion semantics below are now frozen.  Later placement experiments must not change them merely to improve tree metrics.

## 2. Phase 8A — local behavioral classification: PASSED

Using only the old persistent state and the newly admitted contact layer,

```text
A = forced_earlier
B = effective_unresolved_crossing

stable              = not A and not B
nonbranching_update = A and not B
completion_pressure = B.
```

This yields `841 / 2 / 6` before center-3 child semantics are inspected.  Only 26 of 5,823 old full systems are reopened; 298 local children recover all 75 frozen center-3 first-witness semantics without enumerating the full 72,241-state center-3 geometry.

## 3. Phase 8B — discrete observer transport: REJECTED

Exact witness records:

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval').
```

Same boundary, same mode, rank `+2`.  These states join `F_ren`; `F_res` is empty in this calibration.

## 4. Phase 8C — minimum raw completion: PASSED

Exact conflict-cover search over locally generated center-3 wall signs gives minimum raw supports

\[
\boxed{1,2,2,2,3,4}.
\]

Every selected wall is new at center 3.  Four raw signatures already equal their task quotient; two remain over-refined:

```text
3 walls -> 11 raw classes -> 7 task classes
4 walls -> 13 raw classes -> 3 task classes.
```

Thus completion pressure, minimum raw generator support, and minimum task representation are distinct operations.

## 5. Phase 8C.2 — residual objectification: PASSED

Task-relative quotient plus exact adaptive decoding closes

\[
\boxed{11\to7},
\qquad
\boxed{13\to3}.
\]

The `13 -> 3` residual has four available raw walls but decoder worst depth only three.  This freezes the local pipeline

\[
F_{\rm comp}
\to
\text{minimum raw process generators}
\to
\text{task-relative objectified residual}.
\]

No universal `Completion` or `ResidualQuotient` package API is inferred.

## 6. Phase 8D — persistent DAG graft: PASSED

Frozen center-2 persistent Hauffman representation:

```text
68 persistent labels
328 tree/boundary nodes
109 internal query nodes
177 terminal-merged DAG nodes
peak/worst = 72/9.
```

Reuse every old query and replace only six completion terminals by the frozen local decoders.  The decoders add 16 internal nodes and 38 local path leaves, giving

\[
\boxed{376\text{ tree nodes},\quad125\text{ internals},\quad200\text{ DAG nodes}.}
\]

The explicit increment is `+48` tree nodes but only `+23` terminal-merged DAG objects.

The graft width profile is

```text
1,3,3,9,27,48,63,72,75,39,18,15,3
```

so `peak/worst = 75/12`.

The separately frozen fresh center-3 time-first tree has the same `376/125` total/internal structure but `peak/worst = 72/10`.  Therefore local completion determines **how much** structure is needed, while global Hauffman placement determines **where** it sits in history.

## 7. Cost red team after 8D

The historical 55-input current-task distribution hits none of the eight refinement-sensitive states; its zero incremental depth is a blind control.

Conditional on the 298 locally reopened children:

```text
288 completion children
 10 history-reindex children
544 new wall queries total
mean extra depth = 544/298 ≈ 1.8255 per reopened child
completion-only mean = 544/288 = 17/9 ≈ 1.8889
worst extra completion depth = 3.
```

Current usage and continuation/refinement workload must therefore remain separate cost axes.

## 8. Phase 8D.2 — refinement-aware old-prefix placement: PASSED

Freeze all completion decoders and reoptimize only the old 21-wall persistent prefix under the proposal weight

\[
w_\lambda
=(1-\lambda)\frac{w_{\rm current}}{55}
+\lambda\frac{w_{\rm refine}}{288}.
\]

Seven exact mixtures were tested:

\[
0,\frac1{16},\frac18,\frac14,\frac12,\frac34,1.
\]

Selected profiles:

| `lambda` | current total | completion-child total | graft nodes | peak | worst |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 135 | 2933 | 376 | 75 | 12 |
| 1/16 | 136 | 2146 | 376 | 93 | 9 |
| 1/4 | 143 | 2027 | 376 | 87 | 10 |
| 1/2 | 163 | 1739 | 376 | 90 | 9 |
| 1 | 234 | 1721 | 427 | 108 | 9 |

A tiny refinement weight improves completion time and worst depth almost for free in current expected depth, but can explode the frontier: `lambda=1/16` changes current total only `135 -> 136`, completion-child total `2933 -> 2146`, worst `12 -> 9`, yet peak `75 -> 93`.

After duplicate profiles are collapsed, every sampled profile is Pareto-nondominated across current depth, refinement depth, volume, peak, and worst.

Most importantly, **no sampled old-prefix-first candidate reaches both `peak <= 72` and `worst <= 10`**.  Refinement-aware scalar reweighting of the old prefix is therefore insufficient in this bounded family.

Recorded exact run: `32586811587`, Python 3.12.14, essay `1 passed in 29.03 s`.

## 9. API consequence

The reusable research surface remains deliberately small:

```text
ProcessDirection
ConstraintCanonicalization      # one backend
ObserverConnection              # only when a canonical observer actually moves
CanonicalDecomposition          # backend-neutral result shape.
```

Sonnet 001 pressures cost semantics more strongly than object taxonomy.  The current evidence requires present-time, continuation-time, and frontier-space metrics to remain distinct; it does not yet justify a new public cost field because only one continuation calibration exists.

## 10. Next phase — controlled interleaving of new completion walls

The old-prefix-first architecture is now the identified bottleneck.

Relax it carefully: allow the seven new center-3 completion walls discovered in Phase 8C to become queryable **before** a complete old persistent parent is known, but only under exact local certificates.

Required guardrails:

1. no fresh center-3 tree is supplied as a construction;
2. no new completion wall outside the frozen Phase-8C union is introduced;
3. an early new-wall query must be evaluable from primitive speed ratios and have a certified old-state/local-contact interpretation;
4. if a stable old state is split by an early new wall, all resulting branches must be certified to reconverge to the same task semantics;
5. if the same new-wall decision is useful in several completion contexts, cross-parent sharing may be objectified explicitly rather than duplicated;
6. only after the interleaved representation is built may it be compared to the frozen fresh `72/10` oracle.

The first target is not to copy the fresh tree but to answer:

> **what is the earliest admissible history depth at which each new completion wall can be activated without importing future task semantics?**

This “activation geometry” is the next missing representation object.

## 11. Relation to the original observer-ODE idea

Controlled interleaving should not be mislabeled observer transport.  It concerns when a newly generated process distinction becomes observable/useful in a decision history.

A true discrete observer-connection experiment remains deferred until an intrinsic canonical frame actually changes inside a fixed observer family.  The Phase-8 history/DAG results are valuable precisely because they separate these mechanisms rather than forcing one vocabulary onto all of them.

## 12. Execution order

```text
8A    local 841 / 2 / 6 behavioral classification             PASSED
8B    discrete observer-transport interpretation              REJECTED
      corrected canonical sectors = 843 / 0 / 6
8C    minimum raw completion support                          PASSED
      sizes = 1,2,2,2,3,4
8C.2  task-relative residual objectification                  PASSED
      strict quotients 11->7 and 13->3
8D    local persistent-DAG graft                              PASSED
      177 -> 200 DAG nodes; 328 -> 376 tree nodes
8D.2  refinement-aware old-prefix placement                   PASSED
      sampled family exposes time/frontier Pareto tradeoff
NEXT  controlled early activation / cross-parent sharing of frozen new walls
THEN  only if justified, center-3 -> center-4 persistence
FUTURE search separately for a genuine discrete moving observer.
```

## 13. Claim boundary

No new Lonely Runner theorem is proved.  The current exact bounded representation result is that one new contact layer can be absorbed by six objectified local completion decoders with only `+23` explicit persistent DAG objects, but an old-prefix-first architecture cannot in the sampled refinement-weight family reproduce the fresh tree's simultaneous frontier/worst placement.

The next scientific issue is therefore **interleaving/activation geometry**, not more completion discovery and not an observer ODE.

## 14. References

[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in R. E. Miller and J. W. Thatcher (eds.), *Complexity of Computer Computations*, The IBM Research Symposia Series, Plenum Press, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

# Phase 8 — persistent Hauffman geometry: closure and scaling gate

**Status:** center-2 -> center-3 representation loop closed. Phases 8A, 8C, 8C.2, 8D, 8D.2, 8E.0, and 8E passed; Phase 8B rejected the proposed discrete observer-transport interpretation.  
**Branch:** `research/canonical-observer-api`  
**Result notes:** [`20-phase8a-discrete-canonical-decomposition.md`](20-phase8a-discrete-canonical-decomposition.md), [`21-phase8b-history-reindex-red-team.md`](21-phase8b-history-reindex-red-team.md), [`22-phase8c-minimum-completion-residuals.md`](22-phase8c-minimum-completion-residuals.md), [`23-phase8c2-residual-objectification.md`](23-phase8c2-residual-objectification.md), [`24-phase8d-persistent-dag-increment.md`](24-phase8d-persistent-dag-increment.md), [`25-phase8d2-refinement-aware-placement.md`](25-phase8d2-refinement-aware-placement.md), [`26-phase8e0-activation-geometry.md`](26-phase8e0-activation-geometry.md), [`27-phase8e-controlled-interleaving.md`](27-phase8e-controlled-interleaving.md)  
**Open frontier policy:** `K=13` remains a frozen holdout and is not used for representation development.

## 1. Frozen canonical decomposition

The exact center-2 -> center-3 task-state decomposition is

\[
\boxed{843F_{\rm ren}\oplus0F_{\rm res}\oplus6F_{\rm comp}.}
\]

More explicitly:

```text
841 identity-stable
  2 history/decoder reindex
  6 genuine completion states.
```

Phase 8B established that the two nonbranching cases preserve the same witness boundary and mode and only shift event rank by `+2`. They are decoder/history renormalization, not observer motion. Sonnet 001 therefore still supplies **no discrete evidence for `ObserverConnection`**.

## 2. Completion pipeline now established

The six genuine completion states were made constructive in three steps.

### 2.1 Minimum raw process support

Exact conflict-cover search over new center-3 contact-wall signs gives minimum support sizes

\[
\boxed{1,2,2,2,3,4}.
\]

Every selected primitive wall is genuinely new at center 3.

### 2.2 Task-relative residual objectification

Four raw supports already equal their task quotient. Two are over-refined:

\[
11\to7,
\qquad
13\to3.
\]

Exact adaptive decoding quotients both while querying only the selected completion walls. In the `13 -> 3` case four raw walls are available but decoder worst depth is only three.

Hence the frozen completion pipeline is

\[
\boxed{
F_{\rm comp}
\to
\text{minimum process-generated support}
\to
\text{task-relative objectified residual}.
}

No universal `Completion` or `ResidualQuotient` API is inferred.

## 3. Persistent graft and cost red team

The frozen center-2 persistent Hauffman representation has

```text
68 persistent labels
328 tree/boundary nodes
109 internal query nodes
177 terminal-merged DAG nodes
peak/worst = 72/9.
```

Grafting the six frozen completion decoders below their six old leaves gives

```text
376 tree nodes
125 internal nodes
200 terminal-merged DAG nodes
peak/worst = 75/12.
```

Thus one new contact layer requires only `+23` explicit DAG objects after semantic merging.

The separately frozen fresh center-3 time-first tree has the same `376/125` total/internal decision structure but `peak/worst = 72/10`. This isolates two different questions:

\[
\boxed{\text{local completion determines how much structure is required},}
\]

\[
\boxed{\text{history placement determines where that structure sits}.}
\]

The old 55-input current-usage distribution hits none of the eight refinement-sensitive states and is therefore a blind refinement-cost control. Conditional on the 298 locally reopened children, the exact new-wall workload is

\[
544/298\approx1.8255
\]

queries per reopened child, or

\[
544/288=17/9\approx1.8889
\]

per genuine completion child, with worst extra depth three.

Current usage and continuation/refinement workloads must therefore remain separate cost axes.

## 4. Phase 8D.2 — old-prefix reweighting is insufficient

Seven exact current/refinement mixtures were tested while keeping the architecture

```text
old persistent prefix
    -> full old parent resolution
    -> local completion decoder.
```

A tiny refinement weight can improve completion time and worst depth at almost no current expected-depth cost, but can badly enlarge the frontier. For example `lambda=1/16` changes

```text
current total:       135 -> 136
completion total:   2933 -> 2146
worst depth:          12 -> 9
peak frontier:        75 -> 93.
```

After duplicate profiles are collapsed, every sampled profile is Pareto-nondominated across current time, refinement time, volume, peak, and worst depth. No sampled old-prefix-first candidate reaches both `peak <= 72` and `worst <= 10`.

Therefore the bottleneck is architectural, not scalar weighting.

## 5. Phase 8E.0 — clean activation geometry

Relative to the frozen old tree, define a new wall to be **cleanly activatable** at a node when at least one completion user survives and every surviving non-user already has a fixed sign on that wall.

The seven walls have earliest clean depths

\[
\boxed{3,3,5,7,8,9,9}.
\]

However no wall has a **shared clean activation**: even the two walls used by four completion parents become zero-collateral only after a single actual user remains.

Thus cross-parent sharing cannot be obtained merely by lifting a new query to a pre-existing zero-collateral old node. It must allow temporary collateral splitting followed by semantic reconvergence.

Recorded certification: workflow run `32587582896`, activation essay `1 passed in 36.33 s`.

## 6. Phase 8E — controlled interleaving closes the placement gap

Construct a joint representation using only

```text
21 old task-relevant wall signs
+7 frozen Phase-8C completion-wall signs.
```

Exact center-2 multiplicative constraints generate only feasible new-wall variants. After quotienting duplicates under the 849 old parents, the joint representation contains

\[
\boxed{2,753\text{ feasible items}}
\]

and exactly

\[
\boxed{75\text{ final task semantics}}.
\]

No full 72,241-state center-3 arrangement or fresh tree topology is supplied.

With the original current-usage weights only (`lambda=0`), exact search over all 28 predicates gives

```text
current weighted depth total  135
completion-child depth total 2708
tree/boundary nodes           376
internal query nodes          125
terminal-merged DAG nodes     200
peak frontier                  72
worst depth                    10.
```

Hence the controlled representation reconstructs **all frozen structural metrics** of the separately constructed fresh center-3 time-first tree without constructing the full fresh arrangement.

The decision inventory is unchanged:

```text
109 old-wall internal nodes
 16 new-wall internal nodes
---
125 total internals.
```

The successful tree merely changes their partial order and sharing. Four of the 16 new-wall nodes are cross-parent activations, and the first new wall appears at depth five. The seven walls first occur at depths

\[
\boxed{5,6,7,7,8,8,9}.
\]

Thus

\[
\boxed{
\text{completion discovers the required decisions};
\quad
\text{interleaving/reconvergence optimizes their history partial order}.
}

Recorded certification: workflow run `32587582896`, controlled-interleaving essay `1 passed in 152.67 s`.

## 7. What Phase 8 has established for Shakespeare

The complete bounded reconstruction is now

```text
old persistent representation
    -> local next-layer effect detection
    -> canonical decomposition
    -> minimum process-generated completion
    -> task-relative residual objectification
    -> persistent graft
    -> current/refinement cost red team
    -> activation geometry
    -> controlled old/new interleaving with semantic reconvergence
    -> fresh structural placement metrics recovered.
```

This is a stronger result than merely discovering a smaller solver tree: the full 72,241-state next-layer arrangement was not required to reconstruct the frozen fresh-tree structural metrics.

## 8. API consequence

The reusable research surface remains deliberately narrow:

```text
ProcessDirection
ConstraintCanonicalization      # one backend
ObserverConnection              # only when a canonical observer actually moves
CanonicalDecomposition          # backend-neutral result shape.
```

Sonnet 001 does **not** justify a discrete observer connection.

The new pressure lies in the presentation/history layer. Future examples may justify a small abstraction around

```text
predicate activation
semantic reconvergence
history interleaving certificate.
```

One Sonnet is not sufficient to promote it into `src/`.

Likewise, current time, refinement time, and frontier-space geometry must remain separate cost axes; no new public scalar cost is frozen.

## 9. Scaling gate — center 3 -> center 4 without redesign

The center-2 -> center-3 loop is now closed. Further center-3 tuning would risk overfitting the representation language.

The next Sonnet experiment must therefore reuse the frozen procedure **without changing its rules**:

```text
current persistent representation
    -> detect locally affected states from next contact layer
    -> classify renormalization / genuine completion
    -> derive minimum raw new-wall support
    -> objectify task-relative residuals
    -> graft locally
    -> measure conditional refinement workload
    -> permit controlled interleaving only from newly certified walls
    -> compare with a fresh center-4 oracle only after construction.
```

Acceptance questions:

1. Does the affected fraction remain sparse?
2. Does `F_res` remain empty or does a genuine same-family transport case finally appear?
3. How many new process-generated walls are required per completion state?
4. Can task objectification again reduce raw syntax?
5. Does local completion again recover the correct amount of decision structure?
6. Can controlled interleaving again recover or approach fresh placement without full arrangement construction?
7. How do tree/DAG increment and conditional refinement workload scale?

**Guardrail:** none of the center-2 -> center-3 thresholds, counts, or hand-selected wall identities may be hard-coded as proposal heuristics for center 4. Only the reusable process/constraint/task rules are allowed.

## 10. Separate API promotion gate

Even if center-3 -> center-4 succeeds, `activation/reconvergence` should not automatically become public API. A second unrelated discrete/process calibration should pressure the same retained semantics before promotion, following Shakespeare's existing abstraction discipline.

## 11. Relation to the observer-ODE line

The original observer-ODE idea remains valid for problems where a canonical observer actually moves. Sonnet 001 has instead revealed a different mechanism:

```text
history reindex
completion
objectification
interleaving/reconvergence.
```

These should remain distinct. A future discrete observer-connection claim requires an intrinsic canonical frame that changes inside a fixed observer family; neither history interleaving nor decision-DAG sharing substitutes for that condition.

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
      genuine time/frontier Pareto tradeoff
8E.0  clean activation geometry                               PASSED
      depths 3,3,5,7,8,9,9; no shared-clean activation
8E    controlled interleaving                                 PASSED
      2,753-item joint world; 376/125/200; peak/worst 72/10
NEXT  center-3 -> center-4 replay with frozen rules
LATER second unrelated activation/reconvergence calibration
FUTURE search separately for a genuine discrete moving observer.
```

## 13. Claim boundary

No new Lonely Runner theorem is proved. Matching the frozen fresh-tree metrics does not prove tree isomorphism or universal optimality.

The exact bounded Phase-8 statement is:

\[
\boxed{
\text{old persistent geometry + seven process-generated completion walls + local task decoders suffice to reconstruct the frozen center-3 structural placement metrics without constructing the full center-3 arrangement.}
}
\]

## 14. References

[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in R. E. Miller and J. W. Thatcher (eds.), *Complexity of Computer Computations*, The IBM Research Symposia Series, Plenum Press, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

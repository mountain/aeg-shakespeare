# Phase 8 — persistent Hauffman geometry, canonical decomposition, and observer-transport red team

**Status:** Phase 8A passed; Phase 8B rejected the proposed observer-transport interpretation; Phase 8C minimal completion is next.  
**Branch:** `research/canonical-observer-api`  
**Result notes:** [`20-phase8a-discrete-canonical-decomposition.md`](20-phase8a-discrete-canonical-decomposition.md), [`21-phase8b-history-reindex-red-team.md`](21-phase8b-history-reindex-red-team.md)  
**Open frontier policy:** `K=13` remains a frozen holdout and is not used for representation development.

## 1. Starting point

Phase 7b--7i established

```text
A/M contact calculus
    -> pair-difference geometry
    -> exact task quotient
    -> Hauffman space-time optimization
    -> local contact-depth refinement
    -> persistent terminal residuals.
```

At center `<=2`, four-speed first-witness geometry has 849 exact task-safe states.  Deepening the contact alphabet to center `<=3` affects only eight of them; local refinement of 26 old full sign systems into 298 children reproduces the 75 semantics known from the complete 72,241-state center-3 census.

The Phase-8 question is whether the AEG Analysis language developed independently on continuous systems can explain this persistent discrete update without inheriting the fully expanded future representation.

This is a Shakespeare/AEG interpretation, not a claim made by the Lonely Runner or Huffman literature [Sungkawichai-Trakulthongchai-2026; Huffman-1952].

## 2. Observation-locality rule

A Phase-8 discovery rule may use only:

- the current task-safe persistent state;
- its certified first-witness/contact prefix;
- pair-difference constraint closure;
- the newly admitted contact layer;
- finite local order relations involving the old causal prefix;
- declared task semantics.

It may not use the complete next-layer census, deeper future contact layers, a complete propagator/history, or `K=13` data while selecting the representation rule.

## 3. Phase 8A — pre-refinement behavioral decomposition: PASSED

Define from old state plus the new contact layer:

`A = forced_earlier`
: a newly admitted event is already forced at or before the old witness.

`B = effective_unresolved_crossing`
: a genuinely new, causally relevant contact wall can cross the old witness prefix while its side is unresolved by the old representation.

Before any center-3 child semantics are evaluated, classify

```text
stable              = not A and not B
nonbranching_update = A and not B
completion_pressure = B
```

The exact local partition is

\[
\boxed{841\;\oplus\;2\;\oplus\;6.}
\]

Only afterwards does the local child red team verify that the two middle states each have one changed task record while all six completion-pressure states genuinely branch.

The important Phase-8A claim is therefore **behavioral and temporal**: the algorithm predicts identity stability, one-to-one change, or branching completion pressure before the refined task semantics are enumerated.

## 4. Phase 8B — observer-transport hypothesis: REJECTED FOR THESE TWO CASES

The two one-to-one changes were initially suspected to be a discrete analogue of the resonant/observer-transport sector.  Phase 8B tested that stronger claim directly.

Their exact witness records are

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval')
```

In both cases:

```text
same witness boundary = True
same witness mode     = True
event-rank shift      = +2
```

The canonical witness geometry does not move.  The deeper contact alphabet merely inserts two earlier history events, so the task tuple's history index is renormalized.

Hence the corrected canonical decomposition is

\[
\boxed{
843\;F_{\rm ren}
\;\oplus\;
0\;F_{\rm res}
\;\oplus\;
6\;F_{\rm comp}.
}
\]

Here

```text
F_ren = 841 identity-stable + 2 history/decoder reindex states
F_res = empty
F_comp = 6 genuinely branching states.
```

This negative result is binding.  Sonnet 001 currently supplies no discrete evidence for `ObserverConnection`.

Dedicated corrected gate:

```text
workflow: Sonnet Lonely Runner Canonical Decomposition
run id:   32584153291
Python:   3.12.14
pytest:   1 passed in 7.95 s
```

The same run printed the two exact witness records above.  Timing is provenance only.

## 5. New API consequence

Phase 8 strengthens one API claim and weakens another:

### Strengthened

`CanonicalDecomposition` has now survived four qualitatively different carriers:

```text
Riccati             Lie directions
coupled scalars      multivariable Lie directions
Restricted Kepler   finite function-module modes
Lonely Runner        persistent finite task states
```

The discrete carrier supports a nontrivial `renormalizable / completion` split even though its resonant sector is empty.

### Not strengthened

`ObserverConnection` remains supported only by the continuous calibrations in which an actual local observer parameter changes to maintain canonicalization.  Sonnet 001 must not be cited as discrete connection evidence on the basis of the center-2 -> center-3 first-witness refinement.

This distinction is now part of the claim ledger and literate-programming contract.

## 6. Phase 8C — minimal completion of the six branching states: NEXT

The next task is constructive representation completion.

For each of the six completion-pressure parents:

1. enumerate only its locally necessary center-3 children;
2. identify the genuinely new contact-wall/sign coordinates on which their task semantics differ;
3. search for the smallest residual signature sufficient to separate all semantic children;
4. apply exact pair-difference cycle closure to eliminate redundant residual coordinates;
5. certify exact reconstruction of the child first-witness semantics;
6. compare the structured residual against the opaque one-ID-per-sensitive-parent baseline used by the earlier 68-label persistent quotient.

The central test is whether

\[
F_{\rm comp}
\longrightarrow
\text{minimal process completion}
\]

can be made explicit and reusable rather than merely detected.

## 7. Phase 8D — persistent Hauffman DAG

After 8C, construct the center-2 -> center-3 persistent DAG and measure **incremental** representation cost:

```text
old nodes reused
new residual nodes allocated
extra wall queries paid only on split paths
incremental boundary volume / peak width
incremental expected / worst depth
residual/decoder size.
```

History reindexing should be represented as decoder/provenance update, not as a new observer node.

The target remains a Pareto geometry rather than a prematurely scalarized cost.

## 8. Future moving-observer / ODE experiment

The original ODE intuition remains potentially valuable, but Phase 8B shows that this particular refinement does not force it.

A future Sonnet experiment may search for a small active contact frame transported by the A/M contact flow, but it must satisfy a stronger entrance condition:

> the locally canonical frame itself must change while its representation family remains fixed.

A changed event rank, decoder coordinate, or history prefix length is insufficient.

Therefore a moving contact-frame / discrete connection experiment is deferred until a problem state exhibiting genuine same-family observer motion is identified.  It is no longer placed automatically after the current six completion states.

## 9. Relation to Hauffman optimization

Hauffman/history geometry still supplies the variational language for executable representations.  For an evolving persistent DAG the relevant axes now include at least

\[
\left(
\text{frontier geometry},
\text{decision depth},
\text{decoder/history-reindex cost},
\text{completion residual size},
\text{future refinement cost}
\right).
\]

Ordinary Huffman coding remains the static limit in which the symbol alphabet is fixed and expected prefix depth is the operative cost [Huffman-1952].

The Phase-8B correction adds an important lesson: **history-coordinate changes belong on the decoder/refinement axis unless an intrinsic observer state actually changes.**

## 10. Execution order

```text
8A  local 841 / 2 / 6 behavioral classification                PASSED
    ↓
8B  test the two one-to-one changes as observer transport       REJECTED
    ↓
    corrected canonical sectors = 843 / 0 / 6
    ↓
8C  derive minimal residuals for the six completion states      NEXT
    ↓
8D  build persistent DAG and incremental Hauffman geometry
    ↓
search separately for a true moving-observer discrete example if one arises
```

Do not move to open-case tuning or claim a discrete connection before these representation questions are settled.

## 11. Claim boundary

No new Lonely Runner theorem is proved.  The exact bounded result is a persistent-representation statement:

\[
\boxed{
841\text{ identity-stable}
+2\text{ history reindex}
+6\text{ genuine completion pressure}.
}
\]

Equivalently, in the current canonical-decomposition language:

\[
\boxed{843\text{ renormalizable},\quad0\text{ resonant},\quad6\text{ completion}.}
\]

The absence of a resonant sector in this example is part of the result, not a missing feature to be engineered away.

## 12. References

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

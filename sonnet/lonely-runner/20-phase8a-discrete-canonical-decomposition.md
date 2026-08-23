# Phase 8A — local pre-refinement decomposition of persistent contact states

**Status:** exact bounded Phase-8A classification passed; its initial `transport-only` interpretation was subsequently rejected by Phase 8B.  
**Scope:** four relative speeds; center-2 -> center-3 contact-depth refinement; first-witness task; still Gate A.  
**Correction:** see [`21-phase8b-history-reindex-red-team.md`](21-phase8b-history-reindex-red-team.md).  
**Open-frontier policy:** no `K=13` data used for classification, tuning, or validation.

## 1. Question

Phase 7h/7i had already established, by complete post-hoc comparison, that deepening the contact alphabet from center `<=2` to center `<=3` affects only eight of the 849 center-2 task-safe states:

```text
841 witness records unchanged
  2 one-to-one changed task records
  6 genuine semantic splits
```

Phase 8A asks a stronger and temporally ordered question:

> can these three **behavioral roles** be identified before the center-3 task space is expanded, using only the old persistent process state and newly admitted local contact events?

The classification is intended as a pressure test for the AEG Analysis decomposition language, but Phase 8A itself does **not** assume in advance that the middle behavioral class is observer transport.

## 2. Primitive representation and locality

The classifier receives only center-2 information already objectified by previous AM-first phases:

- the exact 5,823 realizable center-2 pair-difference sign systems;
- their 849 exact task-safe quotient states;
- each state's certified first-witness/contact prefix;
- exact pair-difference cycle closure;
- newly admitted center-3 enter/exit events;
- exact local order comparisons between new events and the old causal prefix.

It does not receive the 72,241-state center-3 census, center-3 task labels, identities of the eight affected parents, future contact layers, or `K=13` data while selecting the local roles.

## 3. Local predicates

Two local predicates come from the Phase-7h causal analysis.

### A. `forced_earlier`

A newly admitted center-3 event is already forced at or before the old certified first-witness event.

### B. `effective_unresolved_crossing`

A genuinely new contact wall can exchange a center-3 event with an event in the old causal prefix and the old pair-difference state does not determine its side.  Pure enter-enter swaps are removed by the exact first-witness causality argument because they cannot create the first safe instant.

Before any center-3 child semantics are evaluated, define

```text
stable              = not A and not B
nonbranching_update = A and not B
completion_pressure = B
```

## 4. Exact Phase-8A result

The local classifier produces a pairwise-disjoint exhaustive partition

\[
\boxed{
841\;\text{stable}
\;\oplus\;
2\;\text{nonbranching update}
\;\oplus\;
6\;\text{completion pressure}.
}
\]

Only after this partition is fixed are the eight affected parents locally refined.

They contain 26 of the 5,823 old full sign systems.  Exact center-3 refinement plus cycle closure generates only 298 children.  Their first-witness semantics show:

- each of the two nonbranching parents has exactly one changed task record;
- every one of the six completion-pressure parents has several semantic children, with multiplicities `3, 3, 5, 5, 5, 7`;
- reusing unaffected states and evaluating only the 298 local children recovers all 75 center-3 witness semantics known from the frozen complete census.

Thus Phase 8A establishes a genuine **pre-refinement behavioral classifier**.  It does not yet identify the intrinsic mathematical nature of the two one-to-one changes.

## 5. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    analyze_center2_to_center3()
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

Initial dedicated Phase-8A run:

```text
workflow: Sonnet Lonely Runner Canonical Decomposition
run id:   32583659546
Python:   3.12.14
result:   1 passed in 5.82 s
```

A later corrected Phase-8A/8B run `32584153291` also passes the classifier and additionally verifies the history-reindex correction described in note 21.  Runtime figures are provenance only, not performance claims.

## 6. Phase-8B correction to the canonical interpretation

The original working hypothesis mapped the behavioral partition directly to

```text
stable              -> renormalizable
nonbranching update -> resonant / observer transport
completion pressure -> completion
```

Phase 8B explicitly red-teamed the middle arrow and rejected it.

For both nonbranching cases, the old and new witness records have exactly the same boundary `((1,1,'exit'),)` and the same `'interval'` mode.  Only their event ranks change by `+2`: `11->13` and `12->14`.  The observer geometry therefore does not move; the deeper contact alphabet merely inserts two earlier events into history.

The corrected canonical-sector interpretation is consequently

\[
\boxed{
843\;F_{\rm ren}
\;\oplus\;
0\;F_{\rm res}
\;\oplus\;
6\;F_{\rm comp},
}
\]

where the renormalizable sector consists of 841 identity-stable states plus two history/decoder reindex states.

Phase 8A should therefore be cited for the **841/2/6 pre-refinement behavioral partition**; Phase 8B should be cited for the **843/0/6 canonical interpretation**.

## 7. API consequence

The combined 8A/8B result supports `CanonicalDecomposition` as a backend-neutral result carrier in a discrete persistent-history domain, but it provides **no discrete evidence for `ObserverConnection`**.

That negative conclusion is part of the calibration.  A future discrete connection must exhibit an actual changing canonical frame or observer state, not a task tuple whose history-index coordinate changes under alphabet refinement.

## 8. Claim boundary

No new Lonely Runner case is proved.  Phase 8A is an exact bounded representation calibration for one four-speed center-depth step.  It establishes a local behavioral partition before refined semantics are enumerated.  The subsequent Phase-8B correction shows that one-to-one task replacement alone is insufficient evidence for observer transport.

The six genuinely splitting states remain the appropriate target for Phase 8C minimal process completion.

## 9. References

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

# Phase 8A — discrete canonical decomposition of persistent contact states

**Status:** exact bounded cross-domain calibration passed.  
**Scope:** four relative speeds; center-2 -> center-3 contact-depth refinement; first-witness task; still Gate A.  
**Open-frontier policy:** no `K=13` data used for classification, tuning, or validation.

## 1. Question

Phase 7h/7i had already established, by full post-hoc comparison, that deepening
the contact alphabet from center `<=2` to center `<=3` affects only eight of the
849 center-2 task-safe states:

```text
841 witness semantics unchanged
  2 uniform witness replacements
  6 genuine semantic splits
```

The new question is stronger:

> can those three roles be identified **before** the center-3 task space is
> expanded, using only the old persistent process state and the newly admitted
> local contact events?

This is the first discrete cross-calibration of the AEG Analysis working split

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp}
\]

against Sonnet 001's Hauffman/history geometry.  The terminology is a
Shakespeare/AEG interpretation; it is not asserted by the classical Lonely
Runner or Huffman references.

## 2. Frozen primitive representation

The classifier receives only center-2 information already objectified by the
previous AM-first phases:

- the exact 5,823 realizable center-2 pair-difference sign systems;
- their exact 849 task-safe quotient states;
- each state's certified first-witness/contact prefix;
- pair-difference cycle closure;
- the newly admitted center-3 enter/exit events;
- exact local order comparisons between new events and the old causal prefix.

It does **not** receive:

- the 72,241-state full center-3 census;
- center-3 child task labels;
- the identities of the two replacement or six splitting parents;
- future contact layers;
- `K=13` data.

Thus classification obeys the Phase-8 Observation Localization rule.

## 3. Local classifier

Two local predicates were already justified by the Phase-7h causal analysis.

### A. Forced earlier insertion

`forced_earlier(S)` holds when a newly admitted center-3 contact event is
provably at or before the old certified first-witness event under the center-2
constraints.

This says the current witness parameter cannot remain literally unchanged.

### B. Effective unresolved crossing

`effective_unresolved_crossing(S)` holds when a genuinely new contact wall can
exchange a center-3 event with an event in the old causal prefix and the old
pair-difference state does not determine which side of the wall is realized.

Pure enter-enter swaps are discarded before classification: they cannot create
the first safe instant, so their unresolved ordering is task-irrelevant for the
first-witness observer.

The Phase-8A classification is then fixed as

```text
stable              = not A and not B
transport-only      = A and not B
completion-required = B
```

before any center-3 child semantics are evaluated.

## 4. Exact pre-refinement result

The local classifier partitions all 849 center-2 task-safe parents as

\[
\boxed{
841\;\text{stable}
\;\oplus\;
2\;\text{transport-only}
\;\oplus\;
6\;\text{completion-required}.
}
\]

The three sets are pairwise disjoint and exhaustive.

The research essay records this partition in the same backend-neutral
`CanonicalDecomposition` carrier used by the independent continuous classical
calibrations:

```text
renormalizable <- stable
resonant       <- transport-only
completion     <- completion-required
```

At this stage the field correspondence remains a cross-calibration, not a
universal theorem about discrete processes.

## 5. Post-classification red team

Only after the `841/2/6` partition has been fixed are center-3 semantics
consulted.

The eight affected parents contain only

\[
26
\]

of the 5,823 old full sign systems.  Refining those systems locally under the new
contact ratios and applying exact cycle closure generates

\[
298
\]

center-3 children.

Their exact first-witness semantics verify the pre-refinement prediction:

- each of the **2 transport-only** parents has exactly one center-3 semantic
  child, different from its old witness: the representation does not branch,
  but its canonical witness parameter moves;
- each of the **6 completion-required** parents has several distinct semantic
  children: the old task representation is insufficient without an added local
  distinction.

The six split multiplicities are

```text
3, 3, 5, 5, 5, 7.
```

Reusing the 841 stable old semantics and updating only these 298 children
recovers exactly

\[
\boxed{75}
\]

center-3 first-witness semantics, matching the frozen complete-census result.

## 6. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    analyze_center2_to_center3()
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

Dedicated research workflow:

```text
.github/workflows/sonnet-lonely-runner-canonical-decomposition.yml
```

Recorded GitHub Actions run:

```text
run id:    32583659546
job:       canonical-decomposition
Python:    3.12.14
result:    1 passed
pytest:    5.82 s
```

The wall-clock figure is provenance only, not a performance claim.  The
scientific result is the exact classification and local semantic red team.

Routine five-version CI does not repeat this census.  It still parses the Phase
8A essay through `tests/test_canonical_observer_essay_hygiene.py`, checking its
required sections, reference keys/locators, and Proof-map/test correspondence.

## 7. What has actually been established

Within the declared bounded task, Phase 8A establishes an exact local trichotomy:

```text
old persistent task state + next contact layer
    -> stable
     | transport-only
     | completion-required
```

and the local classification predicts the *kind* of next-layer semantic change
before that change is enumerated.

This is stronger than the Phase-7h binary `affected / unaffected` detector.  The
same eight states are found, but the new rule distinguishes the two states that
can be updated without branching from the six states whose task representation
must actually split.

It is therefore the first executable evidence in Sonnet 001 for the structural
pattern

\[
\boxed{
\text{persistent representation}
\to
\text{local transport}
\;\text{or}\;
\text{minimal completion}.
}
\]

## 8. What has not been established

Phase 8A does **not** establish:

- a general discrete Canonical Observer Connection theorem;
- that every uniform witness replacement in every task is observer transport;
- that every semantic split in every task is representation completion;
- a canonical moving contact-frame state for the two transport cases;
- the minimal residual coordinates needed by the six completion cases;
- a persistent decision DAG with measured incremental Hauffman cost;
- any new Lonely Runner theorem or `K=13` improvement.

Those are precisely the tasks of Phases 8B--8D.

## 9. API consequence

The result supports the *shape* of `CanonicalDecomposition` across a fourth,
qualitatively different carrier:

```text
Riccati             Lie directions
coupled scalars      multivariable Lie directions
Restricted Kepler   function-module modes
Lonely Runner 8A    persistent finite task states
```

It does not yet justify a universal decomposition algorithm or a generic
`Canonicalization` protocol.  The discrete case has not produced an
`ObserverConnection` object yet; Phase 8B must first objectify the same-family
transport of the two uniform replacements.

## 10. Next step — Phase 8B

Freeze the Phase-8A classifier.

For each of the two transport-only parents, construct the smallest explicit
local observer state that carries the current canonical first-witness/contact
frame.  The acceptance test is:

1. center-3 changes observer parameters but not observer-family dimension;
2. the update depends only on old local state plus the new contact layer;
3. no new persistent sign/residual coordinate is required;
4. the updated observer reconstructs the exact new witness.

If either case fails these conditions, the `transport-only` interpretation must
be weakened or abandoned rather than protected by terminology.

## 11. Claim boundary

This result is an **exact bounded representation theorem/calibration** for the
specified center-depth step, not a new theorem about the Lonely Runner
Conjecture itself.

Its significance for Shakespeare is cross-domain and methodological:

\[
\boxed{
\text{a local decomposition discovered in continuous AEG Analysis
survives a nontrivial discrete persistent-history red team.}
}
\]

The next question is whether the two non-branching updates can be realized as a
true same-family observer transport rather than merely classified by their
future behavior.

## 12. References

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

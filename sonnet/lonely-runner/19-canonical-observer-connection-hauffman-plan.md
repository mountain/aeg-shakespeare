# Phase 8 — from persistent Hauffman geometry to canonical observer transport

**Status:** Phase 8A implementation staged; exact opt-in research gate not yet recorded as passed.  
**Branch:** `research/canonical-observer-api`  
**Starting point:** Phase 7i persistent Hauffman quotient at four-speed, center-2 -> center-3 contact-depth refinement.  
**Open frontier policy:** `K=13` remains a frozen holdout and is not used for proposal generation, observer design, decomposition tuning, or cost selection.

## 1. Why this crossover matters

Phase 7b--7i established

```text
A/M contact calculus
    -> pair-difference geometry
    -> exact task quotient
    -> Hauffman space-time optimization
    -> local contact-depth refinement
    -> persistent terminal residuals.
```

The frozen center-2 -> center-3 result is

```text
849 center-2 task-safe parents
    841 current witness semantics unchanged
      2 uniform witness replacements
      6 genuine semantic splits
```

Only 26 of 5,823 full center-2 realizable sign systems lie below the eight
affected parents; local refinement produces 298 center-3 children and recovers
the 75 semantics known from the complete 72,241-state census.

Phase 7i additionally showed that retaining eight refinement-sensitive residual
identities enlarges the current quotient only `60 -> 68`, with no extra current
Hauffman tree queries, nodes, or worst depth.

The Phase-8 question is therefore falsifiable:

> can the canonical-observer language developed independently on continuous
> classical problems reconstruct this sparse discrete transport/completion
> structure *before* the refined task space is expanded?

This interpretation is Shakespeare/AEG-specific.  The classical Lonely Runner
and Huffman references orient the underlying problem and coding objective; they
do not assert the observer-connection interpretation [Sungkawichai-Trakulthongchai-2026; Huffman-1952].

## 2. Observation-locality rule

A Phase-8 classifier may use only:

- the center-2 task-safe state;
- its certified first-witness/contact prefix;
- pair-difference constraint closure;
- newly admitted center-3 contact events;
- local order relations between new events and the old causal prefix;
- declared first-witness task semantics.

It may not use the full center-3 census, precomputed center-3 task labels, deeper
future contact layers, a complete propagator/history, or `K=13` data while
choosing the classification rule.

This is the Sonnet-001 form of the Observation Localization Principle.

## 3. Phase 8A — discrete canonical decomposition

### 3.1 Local observations

The existing Phase-7h causal detector already supplies two local predicates:

`A = forced_earlier`
: a new contact is provably at or before the old first-witness event.

`B = effective_unresolved_crossing`
: a genuinely new contact wall can change the old causal prefix and the old
  pair-difference representation does not decide its side.  Pure enter-enter
  swaps are removed by the exact first-witness causality argument.

The Phase-8A classification is fixed **before any center-3 child semantics are
examined**:

```text
stable              = not A and not B
transport-only      = A and not B
completion-required = B
```

Working correspondence to the generic record:

```text
CanonicalDecomposition.renormalizable <- stable
CanonicalDecomposition.resonant       <- transport-only
CanonicalDecomposition.completion     <- completion-required
```

The field names are being cross-calibrated here; this experiment does not yet
prove a general theorem identifying discrete state refinement with smooth
renormalization/resonance.

### 3.2 Implementation now staged

`sonnet/lonely-runner/python/local_contact_refinement.py` now exposes

```python
analyze_center2_to_center3()
```

which performs the old-state-only classification first, asserts that it is a
disjoint exhaustive partition, and only afterwards locally refines affected
states as a red team.

The opt-in executable mathematical essay is

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

It wraps the three state sets in the same generic `CanonicalDecomposition` carrier
used by the Riccati/coupled/Kepler calibrations.  The essay follows the repository
literate-programming template, contains a Proof map and claim boundary, and cites
both the modern Lonely Runner frontier and Huffman's original coding paper.

The heavy gate is intentionally excluded from routine five-version CI:

```text
.github/workflows/sonnet-lonely-runner-canonical-decomposition.yml
```

The workflow installs the current package and runs the essay with
`AEG_RUN_LR_CANONICAL_DECOMPOSITION=1` on Python 3.12.

### 3.3 Acceptance target

The pre-refinement classifier must recover exactly

```text
stable              841
transport-only        2
completion-required   6
```

and the later local red team must independently show:

```text
2 transport-only parents -> one changed semantic each, no branching
6 completion parents     -> multiple new semantics each
26 old full systems reopened
298 center-3 children evaluated
75 total center-3 witness semantics recovered
```

Until the opt-in gate is executed successfully, these remain acceptance targets
encoded as assertions, not a newly recorded experimental result.

## 4. Phase 8B — objectify same-family transport

If 8A passes, each of the two uniform-replacement parents must be represented by
an explicit local observer state whose parameter update:

1. remains inside the same declared representation family;
2. depends only on old local state plus the new contact layer;
3. changes the canonical witness/contact frame;
4. requires no new sign/residual coordinate.

If either case requires representation enlargement, it must be reclassified as
completion rather than protected by analogy with smooth observer transport.

## 5. Phase 8C — minimal completion of the six splits

For each predicted completion parent:

1. find the smallest new contact distinction separating its semantic children;
2. treat that distinction as a candidate completion residual;
3. close only what pair-difference consistency and task semantics require;
4. certify exact reconstruction of the local center-3 child semantics.

The desired output is a structured residual grammar no larger than necessary.
Opaque persistence IDs remain an acceptable baseline, not the target theory.

A strong result would reconstruct or improve the known one-step persistent
pressure

```text
60 current witness labels
    + eight refinement-sensitive residual identities
    -> 68 persistent labels.
```

## 6. Phase 8D — persistent Hauffman DAG

After 8A--8C, construct an explicit center-2 -> center-3 persistent DAG.  Measure
incremental rather than fresh-tree geometry:

```text
old nodes reused
new nodes allocated
transport-only updates
completion nodes allocated
extra wall queries on affected paths
incremental boundary volume / peak width
incremental expected / worst depth
```

The optimization target remains a Pareto frontier.  A current-task-minimal
representation is not automatically optimal for a continuing process whose
observation language will deepen.

## 7. Phase 8E — moving contact observer / ODE only after the discrete gate

Do not impose a continuous observer ODE on the full sign graph in advance.

If 8A--8D show that transport and completion are genuinely sparse, then search
for a small active contact frame containing only causally critical contacts, for
example the current witness boundary, nearest effective enter/exit events, and
nearest unresolved task-relevant crossing.  The A/M law transports their event
times; chart changes occur only at relevant wall crossings.

The hoped-for computation becomes

```text
small observer-state transport
    + sparse chart/wall transitions
    + occasional minimal completion
```

rather than repeated querying of a large fixed wall arrangement.

## 8. Relation to Hauffman optimization

Earlier Sonnet stages used Hauffman/history geometry to choose the order of
fixed admissible process decisions.  Phase 8 asks for a more persistent
variational problem:

\[
\mathcal S
=\sum_n
\left[
C_{\rm frontier}(g_n)
+\lambda C_{\rm transport}(g_n\to g_{n+1})
+\mu C_{\rm completion}(D_{{\rm comp},n})
\right].
\]

This scalar expression is only a schematic diagnostic.  The multi-axis Pareto
geometry remains primary until an independent calibration justifies a
scalarization.  Ordinary Huffman coding is recovered only in the static limit
where the observer family and decision alphabet are fixed and weighted branch
depth is the operative cost [Huffman-1952].

## 9. API discipline

Sonnet 001 must pressure-test, not dictate, the public API.  The current
cross-domain candidates are deliberately small:

```text
ProcessDirection
ConstraintCanonicalization   # one backend only
ObserverConnection           # generic provenance
CanonicalDecomposition       # backend-neutral result shape
```

No `ObserverBundle`, generic `Canonicalization` base protocol, curvature,
holonomy, universal completion engine, or numerical observer ODE is promoted by
this phase.

The new Phase-8A essay is included in
`tests/test_canonical_observer_essay_hygiene.py`, so its narrative sections,
reference resolution, and Proof-map/test correspondence are checked even when
the heavy mathematics is skipped in routine CI.

## 10. Execution order

```text
8A  run manual exact three-way classification gate
    ↓
8B  objectify same-family transport for the two replacements
    ↓
8C  derive minimal residuals for the six splits
    ↓
8D  build persistent DAG and incremental Hauffman geometry
    ↓
freeze discrete semantics
    ↓
8E  test a moving contact-frame / observer-ODE formulation
```

Do not move to five runners, deeper contact alphabets, or open-case tuning before
8A--8D establish whether observer transport actually explains the known local
refinement structure.

## 11. Claim boundary

No new Lonely Runner case is proved here.  No Canonical Observer Connection is
yet established for Lonely Runner.  The `841/2/6` mapping remains a bounded
cross-domain hypothesis until the dedicated opt-in gate passes and the 8B/8C
semantic conditions are checked.

The intended methodological statement is narrower:

\[
\boxed{
\text{known persistent Hauffman refinement data}
\text{ is a frozen oracle for testing observer-connection theory.}
}
\]

A success would connect continuous AEG Analysis with discrete history geometry;
a failure would delimit where the smooth observer language stops transferring.

## 12. References

[Sungkawichai-Trakulthongchai-2026] T. Sungkawichai, T. Trakulthongchai,
"Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026),
https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

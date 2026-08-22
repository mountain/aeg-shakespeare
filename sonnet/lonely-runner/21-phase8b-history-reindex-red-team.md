# Phase 8B — the two nonbranching updates are history reindexing, not observer transport

**Status:** exact bounded red-team result; the proposed discrete observer-transport interpretation is rejected for these two cases.  
**Scope:** four relative speeds; center-2 -> center-3 contact-depth refinement; first-witness task; still Gate A.  
**Predecessor:** [`20-phase8a-discrete-canonical-decomposition.md`](20-phase8a-discrete-canonical-decomposition.md)

## 1. Question

Phase 8A identified, before any center-3 child semantics were inspected, the local partition

```text
841 stable states
  2 nonbranching changed-task states
  6 completion-pressure states
```

using only the old persistent task representation and the newly admitted contact layer.

The two nonbranching states were initially given the working label `transport-only`: perhaps their canonical observer moved inside the same representation family, analogous to the resonant/observer-connection sector in the continuous Riccati or Restricted Kepler calibrations.

Phase 8B asks the stronger question required by that name:

> **does the canonical witness geometry actually move, or is the changed task label only an artifact of inserting new events earlier in the history?**

This distinction is essential.  A history-coordinate/decoder change must not be promoted into an `ObserverConnection` merely because the terminal task tuple changed.

## 2. Probe discipline

The Phase-8A classifier remains frozen.  Only after it selects the two nonbranching parents do we inspect their exact center-3 task records.

For each parent we compare:

```text
old witness event rank
old witness boundary
old witness mode
new witness event rank
new witness boundary
new witness mode
```

The probe does not alter the classification rule, add new contact walls, inspect `K=13`, or search for a representation that makes the observer-transport hypothesis true.

## 3. Exact witness records

The first parent has

```text
old task: (11, ((1, 1, 'exit'),), 'interval')
new task: (13, ((1, 1, 'exit'),), 'interval')
```

The second has

```text
old task: (12, ((1, 1, 'exit'),), 'interval')
new task: (14, ((1, 1, 'exit'),), 'interval')
```

In both cases:

\[
\boxed{
\text{same witness boundary},
\qquad
\text{same witness mode},
\qquad
\Delta(\text{event rank})=+2.
}
\]

The canonical lonely witness is therefore still the same runner-1 center-1 exit event and still certifies an interval witness.  The only change is that two newly represented center-3 contact events have been inserted before it in the enlarged history alphabet.

## 4. Consequence: reject the transport interpretation

The earlier working explanation

```text
2 nonbranching states -> resonant / observer transport
```

is not supported.

Nothing in the observer geometry has moved.  The task tuple changes because its first component is a **history index**, and that index is representation-depth dependent.

The appropriate interpretation is therefore

```text
history / decoder reindexing
    -> current representation remains sufficient
    -> no observer-family motion
    -> no new representation direction.
```

These two states belong with the 841 identity-stable states in the renormalizable/current-representation sector.

Hence the corrected canonical decomposition for this bounded refinement is

\[
\boxed{
\begin{aligned}
F_{\rm ren}:&\quad 843
=841\text{ identity-stable}+2\text{ history-reindex},\\
F_{\rm res}:&\quad 0,\\
F_{\rm comp}:&\quad 6.
\end{aligned}}
\]

The six completion-pressure states remain unchanged by this correction: every one genuinely branches into several next-layer task semantics.

## 5. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/local_contact_refinement.py
```

The returned `LocalRefinementAnalysis` now exposes

```text
stable_parents
history_reindex_parents
completion_required_parents
renormalizable_parents
resonant_parents
history_reindex_cases
```

and asserts for both history-reindex cases:

```text
same_boundary == True
same_mode == True
event_index_shift == 2
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

The essay now constructs the evidence-bearing `CanonicalDecomposition` with exact sector sizes

```text
843 renormalizable
  0 resonant
  6 completion
```

rather than preserving the rejected `841/2/6` semantic-to-canonical mapping.

Dedicated research run:

```text
workflow: Sonnet Lonely Runner Canonical Decomposition
run id:   32584153291
job:      canonical-decomposition
Python:   3.12.14
pytest:   1 passed in 7.95 s
```

The same run independently printed the two exact witness records above.  The duration is provenance only, not a performance claim.

## 6. Why this negative result matters

This is a useful failure of a theoretically attractive analogy.

The continuous AEG Analysis calibrations genuinely contain observer motion:

- Riccati root/separation parameters move to maintain an affine canonical form;
- coupled-scalar relative scale moves to maintain balanced coupling;
- Restricted Kepler has a resonant first-harmonic modulation sector in the stated perturbative shape model.

The first discrete Sonnet crossover does **not** reproduce that middle sector.  It reproduces only:

```text
current-representation renormalization / decoder update
versus
genuine representation completion.
```

This sharpens rather than weakens the API evidence:

1. `CanonicalDecomposition` survives the discrete red team, but with an empty resonant sector;
2. `ObserverConnection` is **not** justified in Sonnet 001 by these two cases;
3. representation-depth-sensitive task coordinates must be separated from the intrinsic observer state;
4. future attempts to discover a discrete connection need an actual changing canonical frame, not merely a changed history index.

## 7. Implication for the task semantics

The result also exposes a representation issue in the current first-witness task tuple:

```text
(event_index, boundary, mode)
```

The `event_index` is useful decoder/provenance data, but it is not invariant under refinement of the contact alphabet.  By contrast, in these two cases

```text
(boundary, mode)
```

is stable.

This suggests a useful future audit:

> distinguish **intrinsic witness semantics** from **history-location metadata** before defining observer motion or future-task equivalence.

Phase 8B does not change the established task oracle retroactively; the index remains part of the existing exact task record.  It only prevents that representation-dependent coordinate from being mistaken for geometric observer motion.

## 8. Next step — Phase 8C

The immediate next target is now the six genuine completion states, not a discrete observer ODE.

For each of the six parents:

1. enumerate only its locally required center-3 children;
2. identify which genuinely new contact wall/sign distinctions separate their task semantics;
3. search for the smallest residual signature sufficient to distinguish all semantic children;
4. apply pair-difference cycle closure and remove redundant residual coordinates;
5. certify exact reconstruction of the child's first-witness semantics;
6. compare the resulting structured residuals against the opaque one-ID-per-parent baseline used by the 68-label persistent quotient.

The goal is to determine whether

\[
F_{\rm comp}
\to
\text{minimal process completion}
\]

can be made constructive in this discrete setting.

Only after a later Sonnet problem actually exhibits a changing local canonical frame should a discrete `ObserverConnection` be reconsidered.

## 9. Claim boundary

Phase 8B does not prove that discrete observer connections never occur in Lonely Runner or in history geometry generally.  It proves only that the two specific nonbranching center-2 -> center-3 updates previously suspected of being transport are **not evidence for one**.

The exact bounded conclusion is:

\[
\boxed{
841\text{ identity stable}
+2\text{ history reindex}
+6\text{ genuine completion pressure},
}
\]

and therefore

\[
\boxed{
843\text{ renormalizable},
\quad0\text{ resonant/transport},
\quad6\text{ completion}.
}
\]

## 10. References

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

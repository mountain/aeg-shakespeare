# Classical re-expression audit after the canonical-observer vertical slice

**Status:** research audit; no public API freeze.

## 1. Purpose

The canonical-observer programme should not become a vocabulary that is imposed
on every existing Shakespeare calibration.  The first three killer examples
showed that `ProcessDirection`, `ObserverConnection`, and
`CanonicalDecomposition` can carry genuinely new structure.  The next task is
therefore adversarial:

> re-read existing `tests/classical/` and identify where the new language is
> mathematically forced, where it is only a harmless reformulation, and where it
> would be actively misleading.

This note records the first audit pass.  Its mathematical evidence is the
executable essays named below; classical background is attributed separately in
§9 rather than being conflated with the Shakespeare interpretation.

## 2. A/M — positive process-direction calibration, negative connection control

The executable essay

```text
tests/classical/test_am_process_direction.py
```

makes the hierarchy explicit:

```text
A/M ProcessFrame
    -> ProcessDirection(alpha*A + beta*M)
    -> assignment ODE shadow
    -> A/M-specific exact path integration.
```

The ordinary equations

\[
\dot a=\alpha+\beta a,
\qquad
\dot v=\beta
\]

are therefore a representation of the process direction rather than its
ontology.

But this example contains no moving canonical observer.  Adding an
`ObserverConnection` would add words rather than mathematics.  It is the first
negative control for the distinction

```text
process trajectory != observer transport.
```

Translation and Dilation finite-family calibrations likewise remain naturally
in `process.finite`: they establish family/character laws before Fourier/Mellin
language and do not need the local observer machinery merely because a
continuous realization exists.

## 3. Pendulum — scalar observable selection is not a dynamic observer

The pendulum discovery sequence, especially

```text
tests/classical/test_pendulum_structured_observers.py
```

already performs a strong canonical-selection experiment:

```text
primitive q,v,e + pairing
    -> structured scalar proposals
    -> task filter
    -> exact first-order quotient
    -> multi-axis presentation cost
    -> pair(q,e) selected.
```

The winning construction `pair(q,e)` lowers to `q_y` and exposes the genus-one
quotient.  This is a *scalar observable* selected for a declared quotient task.
It is not the dynamic observer `g in P_x` of the Canonical Observer Connection
programme.

Consequences for API design:

1. do not retrofit `ObserverConnection` into the existing pendulum selection;
2. do not rename a fixed scalar observable into a moving observer merely for
   theoretical uniformity;
3. treat the pendulum as a static/trivial-connection control;
4. preserve the future naming pressure: existing discovery names such as
   `StructuredObserverProposal` semantically mean scalar **observable**
   proposals, while the new observer theory reserves *observer* for a local
   representation/frame/gauge state.

A package-wide observable/observer rename should be considered separately from
this vertical slice because it touches existing 0.0.x research surface.

## 4. Two-frequency oscillator — refinement is not automatically completion

The executable red team

```text
tests/classical/test_two_frequency_oscillator_refinement_red_team.py
```

begins from an already closed four-dimensional process grammar with relation

\[
(D^2+1)(D^2+2)=0.
\]

Over the base coefficient language it has two quadratic components.  After
adjoining `i` and `sqrt(2)` it has four linear components.  Both are exact and
both span the same grammar.

This should **not** be rewritten as

```text
base representation
    -> defect
    -> forced completion to four linear modes.
```

There is no such forced residual in the test.  The finer splitting improves
maximum relation order while increasing component count, and the two
presentations remain incomparable on the explicit Pareto profile.

Therefore:

```text
representation refinement != F_comp != minimal process completion.
```

A true `F_comp` claim requires the current canonical representation to fail to
absorb a process direction while exact closure/task sufficiency demands the new
direction.  Restricted Riccati and Restricted Kepler satisfy that pressure;
the oscillator extension red team deliberately does not.

This negative control is important because otherwise every coefficient-field
extension, basis refinement, or spectral diagonalization could be mislabeled as
"completion".

## 5. Galilean and magnetic translations — future pressure, not current API

The Galilean and magnetic-translation essays exhibit central residuals that are
invisible in the projected visible motion but retained by a lifted
representation.  They are natural future pressure for:

```text
observer/process lift
path-ordered transport
holonomy / central history residual
```

but they do not yet determine a reusable connection-curvature contract.

In particular, a nonzero cocycle or central generator residual is not by itself
an `ObserverConnection`: the current theory requires observer dynamics to be the
differential consequence of maintaining a local canonical representation.

The correct action for this branch is therefore to leave the existing cocycle
API intact and defer curvature/holonomy promotion.

## 6. Current taxonomy of classical roles

| Classical line | New-framework role | Connection? | Completion? |
| --- | --- | --- | --- |
| Translation / Dilation | finite process-family laws and characters | no | no |
| A/M path calculus | generic process direction + analytic integration | no | no |
| Pendulum discovery | static observable/quotient canonical selection | normally no | no in current sequence |
| Restricted Riccati | moving affine canonical representation | yes | yes, Lie direction `Q` |
| Coupled scalar registers | moving relative ruler | yes | yes, cross matrix directions |
| Restricted Kepler | moving restricted shape module | conceptually yes; backend not yet implemented | yes, second harmonic |
| Two-frequency coefficient refinement | presentation Pareto red team | no | **not forced** |
| Galilean / magnetic translations | lifted central-history pressure | not yet established | not the current question |

The value of the table is the negative entries.  The new theory is useful only
if it can say when *not* to introduce its own machinery.

## 7. API consequences after the audit

The audit strengthens the current narrow design:

- keep `ProcessDirection` independent of observer transport;
- keep exact constraint canonicalization as one backend, not the universal
  definition;
- keep `ObserverConnection` provenance-generic;
- keep `CanonicalDecomposition` evidence-bearing and backend-neutral;
- do not add generic `Completion`, `Curvature`, `Holonomy`, or `ObserverBundle`
  objects yet;
- preserve existing presentation search and finite cocycle abstractions rather
  than routing them artificially through the new vertical slice.

## 8. Next cross-domain gate

The next genuinely new pressure should come from Sonnet 001 rather than another
continuous mechanics example.

The frozen center-2 -> center-3 Lonely Runner census supplies an independent
oracle:

```text
841 stable task parents
  2 uniform witness replacements
  6 genuine semantic splits.
```

Phase 8 should ask whether a local, old-state-only decomposition can rediscover
those three roles as

```text
stable / renormalizable,
transport-only,
completion-required
```

without consulting the full refined census during classification.

If the same decomposition shape survives that discrete history geometry, the
case for a reusable canonical-observer layer becomes much stronger.  If it does
not, the continuous API should remain domain-limited rather than forcing a false
unification.

## 9. References and executable sources

The primary evidence for this audit is executable, not bibliographic:

- `tests/classical/test_am_process_direction.py` — process direction versus ODE
  shadow; cited classical sources: Hall 2015 and Coddington--Levinson 1955.
- `tests/classical/test_pendulum_structured_observers.py` — structured scalar
  observable selection; cited sources include Arnold 1989 and Cox--Little--O'Shea
  2015.
- `tests/classical/test_two_frequency_oscillator_refinement_red_team.py` — exact
  relation refinement and Pareto non-dominance; cited sources include Arnold
  1989 and Axler 2015.
- `tests/classical/test_restricted_riccati_canonical_observer.py` — affine
  canonicalization and forced quadratic completion; cited sources include
  Cariñena--Marmo--Nasarre 1998 and Hall 2015.
- `tests/classical/test_coupled_scalar_canonical_observer.py` — relative-ruler
  transport and matrix completion; cited sources include Hall 2015 and Arnold
  1989.
- `tests/classical/test_restricted_kepler_canonical_decomposition.py` —
  function-module decomposition; cited sources include Goldstein--Poole--Safko
  2002, Arnold 1989, and NIST DLMF §4.21.

Bibliographic anchors used by the new essays:

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed.,
  Springer, 2015; DOI 10.1007/978-3-319-13467-3.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed.,
  Springer, 1989; DOI 10.1007/978-1-4757-2063-1.
- J. F. Carinena, G. Marmo, J. Nasarre, "The nonlinear superposition principle
  and the Wei-Norman method," arXiv:physics/9802041 (1998),
  https://arxiv.org/abs/physics/9802041 .
- Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*,
  3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.
- NIST Digital Library of Mathematical Functions, §4.21,
  https://dlmf.nist.gov/4.21 .

The conceptual labels "static observable", "canonical observer transport", and
"minimal process completion" are Shakespeare/AEG interpretations.  None should
be read as terminology asserted by these classical sources.

# Mathematical Vignette Index

**Status:** problem-oriented retrieval index; intentionally independent of document chronology and API layout.

This index is the human/model entry layer for substantial mathematical examples in Process Geometry. It is organized by recognizable mathematical problem and structure rather than by the order in which repository notes were written.

For vignette completeness requirements, see [`VIGNETTE_CONTRACT.md`](VIGNETTE_CONTRACT.md).

The index is deliberately conservative: an entry records where to start reading; it does not promote the example's interpretation into the Theory Map or Public API.

---

## Addition / Multiplication process calculus

**Problem / domains:** affine process dynamics; Addition and Multiplication; Lie algebra; characters; exact path integration.

**Classical search terms:** affine group, semidirect product, dilation, translation, characters, first-order linear ODE.

**Process Geometry themes:** A/M process frame, ordered histories, process direction, character transport, noncommutative composition.

**Start here:**

- `tests/classical/test_am_process_direction.py`
- `docs/06-addition-multiplication-function-theory.md`

**Related:** `tests/classical/test_am_character_transport.py`, `tests/classical/test_dilation_characters.py`.

**Theory role:** concrete model organism and calibration; not a claim that A/M is the universal function theory.

---

## Simple pendulum: constrained mechanics to elliptic / Abelian structure

**Problem / domains:** planar pendulum, holonomic constraint, first integrals, algebraic curves, elliptic integrals/functions, periods.

**Classical search terms:** simple pendulum, energy integral, elliptic curve, elliptic integral, genus one, Abelian differential, period lattice, Weierstrass form.

**Process Geometry themes:** constraint prolongation, polynomial invariant discovery, observable algebraic quotient, observer selection, canonical differential, lifted history, period obstruction.

**Entry point:** `tests/classical/test_pendulum_process_geometry.py`.

**Discovery / quotient sequence:**

- `tests/classical/test_pendulum_discovery_layer.py`
- `tests/classical/test_pendulum_observer_selection.py`
- `tests/classical/test_pendulum_structured_observers.py`

**Global analytic sequence:**

- `tests/classical/test_pendulum_period_history.py`
- `tests/classical/test_pendulum_period_contour.py`
- `tests/classical/test_pendulum_period_matrix.py`
- `tests/classical/test_pendulum_cycle_intersection.py`
- `docs/13-abelian-history-periods.md`
- `docs/14-history-lift-and-period-cycles.md`
- `docs/15-period-matrix-and-riemann-shape.md`
- `docs/16-lifted-cycle-intersection.md`

**Current open-theory entry:** `docs/52-canonical-completion-hypothesis.md`.

**Theory role:** major H4/global-analysis calibration. The canonical-completion interpretation remains governed separately from the executable pendulum facts.

---

## Even-power and harmonic oscillators

**Problem / domains:** harmonic oscillator, quartic/sextic oscillators, polynomial potentials, recurrence/modules, hyperelliptic curves.

**Classical search terms:** harmonic oscillator, quartic oscillator, sextic oscillator, hyperelliptic curve, genus hierarchy, spectral decomposition.

**Process Geometry themes:** additive process modules, coefficient-language refinement, relation-before-spectrum, genus/function-theory hierarchy, presentation Pareto tradeoffs.

**Start here:**

- `tests/classical/test_harmonic_oscillator_additive_module.py`
- `tests/classical/test_even_power_oscillator_genus_hierarchy.py`

**Related:**

- `tests/classical/test_harmonic_oscillator_coefficient_extension.py`
- `tests/classical/test_two_frequency_oscillator_refinement_red_team.py`
- `docs/22-oscillator-additive-process-module.md`
- `docs/23-oscillator-coefficient-extension.md`
- `docs/24-oscillator-refinement-red-team.md`

**Theory role:** calibration and red team for function-theory hierarchy and the distinction between representation refinement and forced completion.

---

## Riccati, coupled scalar registers, and Kepler canonical observers

**Problem / domains:** Riccati dynamics, moving frames, coupled scalar systems, restricted Kepler dynamics.

**Classical search terms:** Riccati equation, affine action, moving frame, Kepler problem, harmonic decomposition.

**Process Geometry themes:** canonical observer transport, induced observer ODE, residual directions, minimal process completion, horizontal lift.

**Start here:**

- `tests/classical/test_restricted_riccati_canonical_observer.py`
- `tests/classical/test_coupled_scalar_canonical_observer.py`
- `tests/classical/test_restricted_kepler_canonical_decomposition.py`

**Related:** `docs/35-canonical-observer-vertical-slice.md`, `docs/36-classical-reexpression-audit.md`, `docs/37-canonical-observer-claim-ledger.md`.

**Theory role:** principal calibration family for the current canonical-observer program. The pendulum scalar observable is deliberately retained as a negative control for dynamic observer language.

---

## Galilean mechanics and magnetic translations

**Problem / domains:** Galilean boosts, central extensions, Bargmann mass, magnetic translations, flux cocycles.

**Classical search terms:** Galilei group, Bargmann cocycle, central extension, magnetic translation group, projective representation, magnetic flux.

**Process Geometry themes:** finite process families, character obstruction, process cocycle, central history residual, visible motion versus lifted history.

**Start here:** `tests/classical/test_galilean_central_residual.py`.

**Related:**

- `tests/classical/test_galilean_bargmann_cocycle.py`
- `tests/classical/test_galilean_character_obstruction.py`
- `tests/classical/test_galilean_family_action.py`
- `docs/27-galilean-central-residual.md`
- `docs/28-magnetic-translation-central-residual.md`
- `docs/29-process-cocycle-api.md`

**Theory role:** independent pressure for retained central/history data and the public cocycle layer; not yet a generic holonomy/connection theory.

---

## KdV solitons and cross-presentation confluence

**Problem / domains:** Korteweg–de Vries equation, traveling waves, multisoliton scattering, Hirota tau functions, rewrite confluence.

**Classical search terms:** KdV, soliton, traveling wave, Hirota bilinear form, tau function, phase shift, integrability.

**Process Geometry themes:** discovery, history rewrite, critical-pair confluence, cross-presentation completeness, presentation morphism.

**Start here:** `tests/research/test_kdv_traveling_wave_discovery.py`.

**Related:** `docs/35-killer-calibrations-and-dominance-target.md`, `docs/36-kdv-soliton-rewrite-confluence.md`, `docs/37-kdv-tau-rewrite-cross-presentation.md`.

**Theory role:** research calibration and one of the independent domains that forced `PresentationMorphism`.

---

## Resistor networks: boundary response and Y–Delta

**Problem / domains:** electrical resistor networks, boundary inverse problems, star–triangle / Y–Delta transformation.

**Classical search terms:** resistor network, Dirichlet-to-Neumann map, response matrix, Schur complement, Y–Delta transform, star–triangle transform.

**Process Geometry themes:** task-relative equivalence, semantic confluence, heterogeneous presentation morphism, weak-observer red team.

**Start here:** `tests/research/test_resistor_network_presentation_morphism.py`.

**Related:** `docs/38-resistor-network-presentation-morphism.md`.

**Theory role:** independent non-dynamical calibration for presentation morphisms and task semantics.

---

## Braids, Markov moves, and knot-presentation invariance

**Problem / domains:** braid groups, braid closure, Markov moves, Alexander/Burau data, knot presentations.

**Classical search terms:** braid group, Markov theorem, braid stabilization, Burau representation, Alexander polynomial, knot invariant.

**Process Geometry themes:** cross-dimension presentation morphism, task semantics under closure, stabilization, weak topological observer.

**Start here:** `tests/research/test_braid_markov_presentation_morphism.py`.

**Related:** `docs/39-braid-markov-presentation-morphism.md`.

**Theory role:** topology-domain calibration that helped force the minimal `PresentationMorphism` contract.

---

## Future-distinguishability and Myhill–Nerode

**Problem / domains:** regular languages, deterministic automata, exact future equivalence, minimization.

**Classical search terms:** Myhill–Nerode theorem, DFA minimization, right congruence, future equivalence.

**Process Geometry themes:** task distinguishability, exact semantic quotient, minimal presentation, topological threshold.

**Start here:** `docs/43-myhill-nerode-and-the-topological-threshold.md`.

**Implementation entry:** `src/process_geometry/experimental/finite_task_quotient.py`.

**Theory role:** classical exact anchor for H1 and an Experimental finite slice; not a generic quotient theorem for infinite/continuous processes.

---

## AEG rank transitions: Translation to Multiplication

**Problem / domains:** arithmetic operations as process ranks, semantic compression, action objectification, semidirect composition.

**Classical search terms:** translation monoid/group, dilation, affine monoid, semidirect product, endomorphism action.

**Process Geometry themes:** objectification, higher-rank free composition, compositional rank lowering, analytic-closure pressure.

**Start here:**

- `docs/50-aeg-translation-objectification-rank-lowering.md`
- `docs/51-aeg-addition-multiplication-rank-transition.md`

**Theory role:** current V1–V5 arithmetic model organism; generic rank/objectification theory remains more conservative than these examples.

---

## Index maintenance rule

When a substantial new vignette family is added, update this index if a future reader could plausibly search for the problem independently of the repository's current development chronology.

An index entry should expose:

```text
problem/domain vocabulary
classical aliases
Process Geometry structural vocabulary
one explicit start-here artifact
related executable stages
Theory Map role or `unchanged`
```

Do not turn this index into a chronological changelog or a list of every unit test.
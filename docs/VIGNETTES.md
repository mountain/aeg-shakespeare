# Mathematical Vignette Index

**Status:** problem-oriented retrieval index; intentionally independent of document chronology and API layout.

This index is the human/model entry layer for substantial mathematical examples in Process Geometry. It is organized by recognizable mathematical problem and structure rather than by the order in which repository notes were written.

For vignette completeness requirements, see [`VIGNETTE_CONTRACT.md`](VIGNETTE_CONTRACT.md).

For the current all-family audit against `MATHEMATICAL_CORE.md` and
`ENGINEERING_ARCHITECTURE.md`, see
[`36-classical-reexpression-audit.md`](36-classical-reexpression-audit.md).
For the fail-closed per-file Process Geometry construction matrix, see
[`66-classical-process-language-calibration.md`](66-classical-process-language-calibration.md).

The index is deliberately conservative: an entry records where to start reading; it does not promote the example's interpretation into the Theory Map or Public API.

---

## Addition / Multiplication process calculus

**Problem / domains:** affine process dynamics; Addition and Multiplication; Lie algebra; characters; exact path integration.

**Classical search terms:** affine group, semidirect product, dilation, translation, characters, first-order linear ODE.

**Process Geometry themes:** A/M process frame, ordered histories, process direction, character transport, noncommutative composition.

**Start here:**

- `tests/classical/test_am_process_language_calibration.py` — literal A/M
  words, affine sufficient presentation, continuation quotient, decoder,
  units, and boundary;
- `tests/classical/test_am_process_direction.py`
- `docs/06-addition-multiplication-function-theory.md`

**Related:** `tests/classical/test_am_character_transport.py`, `tests/classical/test_dilation_characters.py`.

**Current-core reading:** exact finite character laws and one exact local A/M
calculus slice.  The family spine now supplies a narrow endpoint-prediction
task quotient without erasing literal word histories. `ProcessDirection` is
not observer transport, and no canonical word section, universal
integrability, or universal function theory follows.

**Theory role:** concrete model organism and calibration; not a claim that A/M is the universal function theory.

---

## Simple pendulum: constrained mechanics to elliptic / Abelian structure

**Problem / domains:** planar pendulum, holonomic constraint, first integrals, algebraic curves, elliptic integrals/functions, periods, state reduction and reconstruction.

**Classical search terms:** simple pendulum, nonlinear pendulum, energy integral, elliptic curve, elliptic integral, genus one, Abelian differential, period lattice, Weierstrass form, reflection symmetry.

**Process Geometry themes:** constraint prolongation, polynomial invariant
discovery, observable algebraic image, observable selection, Experimental
structured proposals, A/M presentation transport, unit-framed universal
history, dimensional resource lines, fundamental domains, action-period
coarea, quotient fiber, task-relative continuation memory, reconstruction
boundary, canonical differential, period obstruction.

**Start here:** `docs/vignettes/simple-pendulum.md` — independent physical problem statement, nondimensional bridge, P0–P13 family dependency map, exact-vs-sampled evidence levels, reconstruction boundary, and open obligations.

**Executable foundation:** `tests/classical/test_pendulum_process_geometry.py`.

**Discovery / representation sequence:**

- `tests/classical/test_pendulum_discovery_layer.py`
- `tests/classical/test_pendulum_observer_selection.py`
- `tests/classical/test_pendulum_structured_observers.py`
- `tests/classical/test_pendulum_observable_quotient_fiber.py`

**Global analytic sequence:**

- `tests/classical/test_pendulum_period_history.py`
- `tests/classical/test_pendulum_period_contour.py`
- `tests/classical/test_pendulum_period_matrix.py`
- `tests/classical/test_pendulum_cycle_intersection.py`
- `docs/13-abelian-history-periods.md`
- `docs/14-history-lift-and-period-cycles.md`
- `docs/15-period-matrix-and-riemann-shape.md`
- `docs/16-lifted-cycle-intersection.md`

**Group law / vertical-axis sequence:**

- `tests/research/test_pendulum_elliptic_group_rank_lowering.py`
- `docs/54-pendulum-elliptic-group-rank-lowering.md`

**Lifted clock / branch-locus sequence:**

- `tests/research/test_pendulum_lifted_clock_global_quotient.py`
- `docs/55-pendulum-lifted-clock-global-quotient.md`

**A/M presentation / task-memory sequence:**

- `tests/research/test_pendulum_am_marked_carrier_bridge.py`
- `tests/research/test_pendulum_observer_metric_completion.py` (declared metric
  fiber product and noncanonical Bolza special point)
- `docs/56-am-universal-history-recalibration.md`
- `docs/61-pendulum-section-reparameterization-redteam.md`

**Unit-framed history / fundamental-domain sequence:**

- `tests/research/test_pendulum_unit_history_fundamental_domain.py`
- `docs/53-process-volume-frontier-coarea-hypothesis.md`
- `docs/56-am-universal-history-recalibration.md`
- `docs/62-task-covariant-complexity-coarea.md`

**Current open-theory entry:** `docs/52-canonical-completion-hypothesis.md`.

**Theory role:** major H4/global-analysis calibration. The executable family now places the marked elliptic carrier downstream of a unit-framed lifted history, separates lattice-defined fundamental domains from their dimensional ruler, and calibrates continuous action-period coarea separately from finite deck memory. Supplied chart transport and the task-relative `Z2` result remain exact. The Bolza surface is the noncanonical product-sign quotient of a separately declared metric sheet, not another pendulum/A/M presentation. A raw A/M-history lift, canonical pendulum observer/ruler, global nonlinear equivalence, and stronger completion interpretation remain open research.

---

## Local fields: projective histories, continued fractions, and finite coding

**Problem / domains:** rational A/M/inversion histories viewed at real and
\(p\)-adic places; finite Bruhat--Tits lattice balls; Ruban and Browkin I
continued fractions; projective-cylinder refinement and source coding.

**Classical search terms:** \(p\)-adic valuation, \(PGL_2(\mathbb Q_p)\),
Bruhat--Tits tree, projective line over finite rings, Ruban continued fraction,
Browkin continued fraction, Stern--Brocot tree, Huffman code.

**Process Geometry themes:** place-relative observer rulers, literal history
versus matrix payload, standard-frame projective evaluation, continuation
residual, quotient sections, finite shell growth, task memory, geometry tree
versus coding tree.

**Start here:**
`sonnet/local-field-projective-process-geometry/README.md`, followed by the
numbered Phase 0--5 records.

**Executable sequence:**

- `tests/research/test_local_field_projective_process_geometry.py`
- `tests/research/test_local_field_projective_lattice_ball.py`
- `tests/research/test_real_continued_fraction_geodesic_control.py`
- `tests/research/test_padic_continued_fraction_selector_comparison.py`

**Theory role:** independent finite discrete calibration of the emerging
task-covariant evaluation transversal. It separates full prefix history,
composable projective matrix evaluation, the Bruhat--Tits observer tree,
fixed-depth task cylinders, complete-quotient residuals, and a separately
declared binary coding tree. The exact shell identity and finite Huffman task
refine H2/H3 without an infinite-boundary, entropy-rate, selector-policy,
preferred-algorithm, or API promotion claim.

---

## Even-power and harmonic oscillators

**Problem / domains:** harmonic oscillator, quartic/sextic oscillators, polynomial potentials, recurrence/modules, hyperelliptic curves.

**Classical search terms:** harmonic oscillator, quartic oscillator, sextic oscillator, hyperelliptic curve, genus hierarchy, spectral decomposition.

**Process Geometry themes:** additive process modules, coefficient-language
refinement, relation-before-spectrum, genus/function-theory hierarchy, real
history cover, deck quotient, task sufficiency, branch decoder, unit frame,
action-period law, presentation Pareto tradeoffs.

**Start here:**

- `tests/classical/test_even_power_oscillator_process_calibration.py` —
  declared real continuation task, harmonic phase cover/decoder/unit round-trip,
  and exact even-power action-period law;
- `tests/classical/test_harmonic_oscillator_additive_module.py`
- `tests/classical/test_even_power_oscillator_genus_hierarchy.py`

**Related:**

- `tests/classical/test_harmonic_oscillator_coefficient_extension.py`
- `tests/classical/test_two_frequency_oscillator_refinement_red_team.py`
- `docs/22-oscillator-additive-process-module.md`
- `docs/23-oscillator-coefficient-extension.md`
- `docs/24-oscillator-refinement-red-team.md`

**Current-core reading:** the harmonic modules and relation factorizations are
exact in declared coefficient languages.  The new real-task spine constructs
the harmonic phase cover, deck quotient, position/sign decoder, unit frame,
action-period law, and a literal quarter-period word unfolding.  It does not
claim an intrinsic unfolding of every continuous command history.  The earlier
even-power curves remain algebraic carriers until a complex analytic task and
decoder are supplied.  Their genera `0,1,2` do not measure real orbit-cover
complexity: all regular connected positive-energy real orbits here are
circles.  Coefficient refinement is not forced completion.

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

**Current-core reading:** `observer` here means a local moving
representation/frame chosen by a displayed normalization. It is distinct from
an H1 task observer or task-sufficient history quotient; `canonical` remains
relative to the declared grammar, branch, gauge, and local regular stratum.

**Theory role:** principal calibration family for the current canonical-observer program. The pendulum scalar observable is deliberately retained as a negative control for dynamic observer language.

---

## Planar circular restricted three-body problem: costed lifted histories

**Problem / domains:** planar circular restricted three-body problem, Jacobi
integral, Hill regions, collision-punctured configuration space, numerical
trajectory histories.

**Classical search terms:** PCR3BP / CR3BP, Lagrange point `L1`, zero-velocity
curve, free group `F2`, pair of pants, `Gamma(2)`, hyperbolic uniformization.

**Process Geometry themes:** observer gates, universal-history lift,
dimensionless physical clock, word cost versus deck-translation cost,
Bellman/Huffman claim boundary.

**Start here:**
`sonnet/pcr3bp-history-cost/README.md`, then
`sonnet/pcr3bp-history-cost/00-phase0-history-cost.md` and
`sonnet/pcr3bp-history-cost/01-scale-jet-topology-and-coding-audit.md`.  The
next computation is frozen, but not yet claimed executed, in
`sonnet/pcr3bp-history-cost/02-return-partition-holonomy-contract.md`.

**Executable calibration:**
`tests/research/test_pcr3bp_history_cost_phase0.py` and
`tests/research/test_pcr3bp_scale_jet_phase1.py`.

**Theory role:** phase-0 numerical red team for identifying word length,
hyperbolic length, and physical time.  It refines the separation of H0, H2, and
H3.  Phase 2 will test the thermodynamic-objectification V2/V3 boundary and
gate-presentation covariance; it does not yet assert complete symbolic
dynamics, a Ruelle zeta function, or arithmetic universality.

---

## Galilean mechanics and magnetic translations

**Problem / domains:** Galilean boosts, central extensions, Bargmann mass, magnetic translations, flux cocycles.

**Classical search terms:** Galilei group, Bargmann cocycle, central extension, magnetic translation group, projective representation, magnetic flux.

**Process Geometry themes:** finite process families, character obstruction, process cocycle, central history residual, visible motion versus lifted history.

**Start here:** `tests/classical/test_galilean_central_residual.py`.

**Process-language spine:**
`tests/classical/test_central_payload_process_calibration.py` — literal words,
visible/lifted continuation tasks, central residual memory, exact lowering,
coboundary covariance, and units.

**Related:**

- `tests/classical/test_galilean_bargmann_cocycle.py`
- `tests/classical/test_galilean_character_obstruction.py`
- `tests/classical/test_galilean_family_action.py`
- `docs/27-galilean-central-residual.md`
- `docs/28-magnetic-translation-central-residual.md`
- `docs/29-process-cocycle-api.md`

**Current-core reading:** the finite cocycles exactly compose a declared
central payload forgotten by visible motion. Cocycle representative, gauge,
units, lifted task, and decoder remain problem-local; this is not yet a generic
history-payload, holonomy, or connection theory.

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

## Finite thermodynamic objectification and twisted cycles

**Problem / domains:** finite statistical mechanics, log-sum-exp
coarse-graining, combinatorial multisets, integer partitions, weighted directed
graphs, character-twisted cycle series.

**Classical search terms:** partition function, free energy, thermodynamic
semiring, tropical/min-plus limit, plethystic exponential, Euler product,
transfer matrix, dynamical determinant, graph zeta.

**Process Geometry themes:** task objectification, measure pushforward,
same-scale flattening, unit-cell discretization, free higher-rank assembly,
holonomy information loss, flattening obstruction.

**Start here:**
`docs/63-thermodynamic-objectification-and-partition-towers.md`.

**Executable calibrations:**

- `tests/research/test_thermodynamic_objectification_partition_tower.py`;
- `tests/research/test_finite_twisted_cycle_partition.py`.

**Theory role:** exact finite boundary calibration for V2/V3 and the existing
coarea/frontier line.  The reusable interpretation is a research-local T1
candidate;
it does not define a generic partition API, prove a thermodynamic limit, or
promote Arithmetic Geometric Universality.

---

## Checkpointed adjoints for nonlinear dynamics

**Problem / domains:** reverse/adjoint differentiation of a time-stepped nonlinear ODE under finite checkpoint memory.

**Classical search terms:** adjoint sensitivity, reverse-mode automatic differentiation, checkpointing, recomputation, binomial checkpointing, Revolve, time-space tradeoff.

**Process Geometry themes:** smooth chart covariance, cotangent transport, lifted execution history, task-sufficient checkpoint state, invariant resource cost, Bellman optimization.

**Start here:** `tests/research/test_am_checkpoint_differential_quotient.py` — A/M-first derivation of value, first variation, cotangent pullback, and task-local germs; then a fixed-segmentation pullback-cache Bellman gate with an explicit whole-chain dominance red team.

**Classical baseline:** `tests/research/test_checkpointed_adjoint_canonicalization.py` — smooth-chart covariance and binomial Revolve counts; compatibility evidence only.

**Theory role:** first research-local V5 analytic-closure pressure connecting A/M history variation, differential task germs, objectified pullbacks, and resource-bounded history. The static local Bellman table is not a global Pareto frontier: for the frozen terminal-only task, a two-scalar whole-chain pullback dominates all segmentwise caches. It is not a complete Revolve controller, a Huffman theorem, a generic checkpoint API, or evidence that A/M universality has been established.

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

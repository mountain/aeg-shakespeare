# Classical-model recalibration against the Mathematical Core

**Status:** second-pass research audit after the end-to-end pendulum
calibration, followed by a governed zero-`OPEN` process-language matrix and
three family spines.  It covers the baseline at commit `e25e575` plus the new
calibrations introduced by this branch.  It changes API ownership and
vocabulary without promoting a new Mathematical Core or Theory Map object.

## 0. Why a second pass is necessary

The first version of this record asked a narrow question: which older examples
really forced the then-new canonical-observer language? The repository now has
a stronger reference standard:

1. `MATHEMATICAL_CORE.md` states the primitive-history, declared-task, lift,
   transported-payload, stopping/quotient, decoder, unit, and claim-boundary
   order;
2. `ENGINEERING_ARCHITECTURE.md` turns calculation claims into explicit
   representation, algorithm, evaluator, certificate, failure, baseline, unit,
   and cost obligations;
3. the pendulum P0--P13 family supplies the first end-to-end exact calibration
   of that order.

The present audit therefore re-reads **every one of the 33 executable essays**
under `tests/classical/`. It does not ask whether their equations remain
beautiful. It asks which mathematical object each test actually constructs,
which task it serves, what it preserves and forgets, how it is evaluated, and
where its interpretation must stop.

The baseline executable result is:

```text
tests/classical: 80 passed
exact symbolic / finite tests: pass
sampled numerical pendulum tests: pass at their declared tolerances
```

Passing preserves the local certificates. It does not promote their strongest
historical wording.

## 1. Audit language

The following labels keep four kinds of statement separate.

| Label | Meaning in this record |
| --- | --- |
| **E** | exact classical or exact symbolic/finite executable fact in the declared algebra/domain |
| **N** | sampled numerical result with empirical convergence/reference checks, but no interval certificate |
| **D** | result relative to a declared observer grammar, normalization, cost axes, branch, gauge, or coefficient language |
| **T1** | precise local or reusable hypothesis whose stronger general form remains unproved |
| **T0** | useful Process Geometry interpretation or extraction pressure, not a theorem supplied by the executable fact |

For every family the audit applies the same questions:

```text
primitive data and admissible process
declared task and continuation semantics
construction: lift / image / factor / quotient / transport / completion
equation, invariant, obstruction, or certificate
preserved, forgotten, and reconstructible information
unit/frame covariance and singular strata
symbolic/numerical evaluator, failure mode, baseline, and cost
Mathematical Core / Engineering Architecture / Theory Map effect
```

## 2. Repository-wide findings

### 2.1 The executable mathematics survives

No failing exact identity, factorization, cocycle law, local reconstruction, or
sampled pendulum certificate was found. The current work is principally a
**semantic narrowing and dependency repair**, not a rejection of the classical
examples.

### 2.2 Five separations must now govern the old wording

1. **Algebraic image is not automatically a task-semantic quotient.**
   Eliminating variables to obtain `Y^2=P(X)` proves an exact observable
   relation. A task quotient additionally needs continuation semantics,
   information loss, and a decoder boundary. The pendulum family supplies
   those later; the even-power oscillator genus ladder does not yet do so.
2. **Moving frame is not the H1 task observer.** Riccati, coupled-register, and
   Kepler “observers” are local representation/gauge states selected by
   normalization. They are not by that fact maps from histories to exact
   continuation classes.
3. **Analytic developing cover is not full history unfolding.** Pendulum
   period tests lift the square-root/Abelian clock and measure its kernel. The
   end-to-end audit makes this a downstream analytic model, not a proof that
   the raw process has been intrinsically unfolded.
4. **Retained cocycle is not a generic connection or holonomy theory.**
   Galilean and magnetic translations exactly retain central composition data
   erased by visible motion. They do not select one universal transported
   payload carrier.
5. **Refinement is not forced completion.** Coefficient extension, basis
   change, factor splitting, and lower polynomial degree may improve one cost
   axis while worsening another. Completion is meaningful only relative to a
   declared language/task whose closure fails without the new direction.

### 2.3 Strong words remain local

In these essays:

- `canonical` means selected by the displayed local normalization, ordered
  branch, observer family, and residual gauge;
- `minimal` means minimal in the displayed finite span, module, support, or
  Pareto preorder;
- `quotient` means a task quotient only where task/future semantics and lost
  information have been established; elsewhere `algebraic carrier`, `image`,
  or `factor` is the safer term;
- `history residual` refers to a declared lifted coordinate or payload, not one
  generic history object.

### 2.4 The principal missing fields outside the pendulum

Most non-pendulum files predate the new solver-plan contract. Their exact
algebra is still valid, but they commonly leave one or more of these fields
implicit:

- the downstream task that makes the representation sufficient;
- the decoder or explicit statement that reconstruction is not requested;
- nondimensionalization and inverse physical unit map;
- covariance under admissible frame, gauge, time, or coefficient changes;
- failure outcomes at singular strata;
- total cost beyond one transparent structural proxy.

These are documentation and research obligations. They are not reasons to
invent a generic `Problem`, `Solver`, `Observer`, `HistoryPayload`, or
`CanonicalLift` API.

## 3. Addition, Multiplication, and characters

The family verifies exact composition and response laws before importing
Fourier/Mellin or general representation theory.

| File | Executable fact | Core classification | Recalibrated boundary / next action |
| --- | --- | --- | --- |
| `test_translation_characters.py` | additive family law and exponential character equation | **E** finite-family/character certificate | Character verification only; no completeness measure, synthesis, task quotient, or decoder claim. |
| `test_dilation_characters.py` | multiplicative family and Mellin-character equation for positive scales | **E** under the declared positive domain | `log` is a supplied realization; positivity is a domain condition, not a discovered canonical chart. |
| `test_am_character_transport.py` | scale transports `xi` to `a xi`; a nontrivial scalar character is generically non-invariant | **E** obstruction | Exact pressure for a richer response space, but not a selection of wavelets, Hilbert representations, or a universal next carrier. |
| `test_am_process_direction.py` | `alpha A+beta M` lowers to `a_dot=alpha+beta a`, `v_dot=beta`; constant coefficients use the exact A/M path flow | **E** local calculus plus **T0** process-first interpretation | This is the clean negative control: process direction is not observer transport. General integrability, task sufficiency, units, and cost remain undeclared. |
| `test_am_process_language_calibration.py` | literal positive-affine words lower to an exact continuation-stable affine normal form with scalar decoder, unit covariance, and zero-scale failure | **E** for the declared endpoint-prediction task | Word depth is intentionally forgotten by the task quotient; no canonical/shortest word section, Fourier/Mellin synthesis, or cover is claimed. |

**Family judgment.** This family remains a valid A/M-native model organism and
an exact local analysis slice.  It now has a complete narrow process-language
spine: literal ordered words, affine sufficient presentation, declared future
task, quotient information loss, decoder, units, and boundary.  Topological
and analytic covers are explicitly unnecessary for that finite endpoint task.
It does not establish Arithmetic Geometric Universality, a canonical word
section, or a generic analysis language. No API change follows.

## 4. Oscillators, relation modules, and genus

| File | Executable fact | Core classification | Recalibrated boundary / next action |
| --- | --- | --- | --- |
| `test_harmonic_oscillator_additive_module.py` | the cyclic `D`-invariant scalar-linear span generated by `x` is `span{x,p}` with relation `D^2+1`; the relation survives a seed-basis change | **E**, minimal relative to the declared scalar-linear closure policy and seed | Not a task-minimal state quotient and not evidence that linear span is privileged for arbitrary processes. |
| `test_harmonic_oscillator_coefficient_extension.py` | adjoining `i` splits the already-found relation and gives two exact one-dimensional kernels with a round-trip decoder | **E** after a caller-declared extension; **D** representation choice | The extension is proposed, not discovered; splitting is not automatically cheaper or canonical. |
| `test_even_power_oscillator_genus_hierarchy.py` | supplied energy candidates are exact invariants; their generic energy-leaf curves for powers `2,4,6` have genera `0,1,2` | **E** algebraic carriers; **T0** function-language interpretation | These are not yet task-semantic quotients. Genus is not a universal process-complexity scalar, and no period/Jacobian/decoder is constructed. |
| `test_even_power_oscillator_process_calibration.py` | the real even-power action obeys `d Omega/dE=T`; the harmonic member has an exact quarter-period word unfolding, phase cover, deck kernel, full-state task quotient, position/sign decoder, unit round-trip, and singular boundary | **E** for the declared positive-energy real task and discrete history alphabet; topology and beta integration use stated classical prerequisites | The harmonic topological and analytic covers coincide for this task, but no intrinsic unfolding of every continuous command history is claimed; quartic/sextic complex global decoders are not constructed. |
| `test_two_frequency_oscillator_refinement_red_team.py` | two quadratic and four linear decompositions are exact and Pareto-incomparable on declared axes | **E** plus **D** cost red team | Strong negative control: coefficient refinement is not forced completion. Coefficient-language, compilation, storage, and repeated-evaluation costs remain unpriced. |

**Family judgment.** The exact relation-first programme survives.  The new
real-process spine now supplies the second end-to-end declared continuation
task after the pendulum: for the harmonic member it separates phase cover,
deck quotient, position-only information loss, local decoder, units, clock,
and failure.  It also exposes a new non-identification: the complex genera
`0,1,2` do not measure real orbit-cover complexity, because every regular
connected positive-energy real orbit in this family is a circle.  Raw-history
unfolding and the quartic/sextic complex decoders remain open.

## 5. Galilean mechanics and magnetic translations

| File | Executable fact | Core classification | Recalibrated boundary / next action |
| --- | --- | --- | --- |
| `test_galilean_family_action.py` | boosts shear spacetime-translation characters by `(p,E)->(p,E-vp)` | **E** bare dual action | It intentionally omits the mass-dependent affine term; this is not the full physical representation. |
| `test_galilean_character_obstruction.py` | ordinary character pullback fixes the zero character and cannot create a nonzero affine shift | **E** obstruction | Establishes need for extra retained data, not its unique ontology. |
| `test_galilean_central_residual.py` | `{K,P}=m`, the central term has zero visible Hamiltonian vector field, and the finite boost gives the massive affine label shift | **E** Hamiltonian realization | The visible phase-space projection forgets generator-level central data. No general Poisson or lifted-history API is implied. |
| `test_galilean_bargmann_cocycle.py` | one fixed Galilei convention carries an exact finite mass 2-cocycle whose infinitesimal mixed residual is `m` | **E** lifted composition law | Cocycle representatives may differ by coboundaries; the test fixes one convention and no cohomology classification. |
| `test_magnetic_translation_central_residual.py` | visible translations compose ordinarily while the lift retains the exact flux/area cocycle and central bracket | **E** independent physical calibration | The phase coordinate is a declared lift with gauge/convention dependence. This supports retained payloads, not a generic connection/curvature theorem. |
| `test_central_payload_process_calibration.py` | literal ordered words expose visible versus lifted continuation tasks; the phase residual has exact lowering, coboundary covariance, and inverse-area unit covariance | **E** finite family spine | Cover construction is explicitly not applicable to this finite composition task; genuine path holonomy requires a new topological task. |

**Information contract.** In both organisms the visible action forgets a
central coordinate or generator residual that matters to the lifted task. The
finite cocycle is the exact composition rule for that retained payload. A
visible-endpoint task may discard it; a phase/projective task may not.

**Family judgment.** The public finite cocycle slice remains justified by two
independent exact calibrations. The broader reading—central residual as one
instance of transported task payload—is **T1 pressure**, not a promotion to a
generic `HistoryPayload`, `Connection`, or `Holonomy` object.

## 6. Riccati and coupled moving frames

These files use `observer` in the moving-frame sense. Their task is local
representation normalization and decomposition, not H1 future minimization.

| File | Executable fact | Core classification | Recalibrated boundary / next action |
| --- | --- | --- | --- |
| `test_restricted_riccati_canonical_observer.py` | ordered-root constraints induce affine-frame rates; the quadratic direction remains outside the restricted affine algebra and closes with it as `sl(2)` | **E** local identities plus **D** observer family; **T1/local** completion reading | `canonical` is relative to the nondegenerate ordered-root affine grammar. No global discriminant crossing or PSL(2) solver. |
| `test_riccati_canonical_horizontal_lift.py` | many affine lifts reconstruct one base process; differentiated root normalization selects one local horizontal path and makes one declared coefficient path autonomous | **E** local reconstruction plus **D** jet-count objective | Coefficient-jet count is not invariant under arbitrary reparameterization or a universal complexity. Singular root collisions are outside domain. |
| `test_coupled_scalar_canonical_observer.py` | relative-scale balance induces a diagonal connection; bidirectional cross directions force matrix completion while one-way coupling stays triangular | **E** exact bracket/decomposition plus **D** balance gauge | Positive bidirectional sector and one residual gauge only; not a theorem that coupling forces full `GL(n)`. |
| `test_coupled_diagonal_canonical_horizontal_lift.py` | balance plus determinant-one gauge derives the two frame rates and autonomizes the selected exponential-coupling path | **E** local lift plus **D** normalization/cost | The one-way stratum is an explicit failure boundary; no generic matrix normal form or universal horizontal lift. |

**Family judgment.** The exact local pipeline survives:

```text
declared moving-frame family
  -> local normalization constraints
  -> differentiated frame transport
  -> exact reconstruction
  -> residual decomposition relative to that family.
```

It must not be conflated with

```text
literal histories -> declared continuation task -> minimal task quotient.
```

The Experimental record types remain useful precisely because their general
theory is unsettled. This audit creates no pressure for a generic canonical
observer or lift API.

## 7. Kepler calibrations

| File | Executable fact | Core classification | Recalibrated boundary / next action |
| --- | --- | --- | --- |
| `test_kepler_radial_canonical_horizontal_lift.py` | radial alignment derives `theta_dot=V/X`; the local chart separates a two-dimensional radial shape ODE, conserved `h`, and angle quadrature | **E** local noncollision reconstruction; **D** outward branch/frame | Exact only on `X>0`, away from collision. Physical dimensions and inverse unit map are not audited in this essay. |
| `test_restricted_kepler_canonical_decomposition.py` | the declared `R`-module is closed; squared-shape forcing splits into constant, resonant first harmonic, and second-harmonic complement; the minimal degree-two `R`-closed extension is five-dimensional | **E** finite module facts plus **T1/local** `ren/res/comp` reading | The forcing, module, and first-order ansatz are supplied. No task quotient, general perturbation solver, projection metric, or automatic completion search. |
| `test_perturbed_kepler_eccentricity_canonicalization.py` | the unperturbed contribution cancels from `e_dot`; eccentricity alignment derives periapsis-frame rate and leaves magnitude change with zero residual in that carrier | **E** local noncircular identity plus **D** carrier/frame | The zero-completion statement is carrier/task-relative. Circular, 3D, collision, secular, and global reconstruction regimes remain outside scope. |

**Family judgment.** Kepler supplies the strongest non-pendulum evidence that
local canonicalization can expose a computationally useful decomposition while
retaining reconstruction data. It still lacks the pendulum's complete unit,
task, global-branch, effective-evaluation, and failure contract. That gap
argues for a future family-level Kepler guide, not a package-level solver.

## 8. Pendulum P0--P9 classical files

The later research P10--P13 stages now determine how the older classical files
must be read.

| File | Executable fact | Core classification | Recalibrated boundary / next action |
| --- | --- | --- | --- |
| `test_pendulum_process_geometry.py` | constrained Cartesian closure, energy invariance, and generic smooth cubic relation | **E** primitive/reduction foundation | The cubic is first an observable algebraic carrier; task quotient and reconstruction semantics are supplied by later stages. |
| `test_pendulum_discovery_layer.py` | degree-two bounded search finds energy and exact elimination finds the cubic after `U=q_y` is selected | **E** bounded symbolic discovery | Search completeness is only within the declared polynomial budget; no intrinsic observer or ruler discovery. |
| `test_pendulum_observer_selection.py` | among supplied `q_x,q_y`, the latter wins the declared structural Pareto comparison | **E** adequacy certificates plus **D** candidate grammar/cost | Not a universal canonical observer; relation cost is a proxy and downstream task weights may differ. |
| `test_pendulum_structured_observers.py` | supplied pairable atoms and pairing generate proposals; `pair(q,e)` wins the declared search | **E** bounded construction/provenance plus **D** grammar/cost | The Euclidean pairing, sorts, and atoms remain supplied. Moving-frame `observer` language does not enter. |
| `test_pendulum_observable_quotient_fiber.py` | the hidden `Z2` symmetry preserves process and observable; quadratic hidden data descend while one sign does not | **E** information-loss certificate | This establishes the algebraic factor and generic two-sheet state fiber; task-universal sufficiency is not claimed. |
| `test_pendulum_local_branch_decoder.py` | one branch bit gives an exact local Cartesian state-and-flow decoder away from `U=+/-1` | **E** local round trip | Global branch transport, turning-point charts, and task-universal history reconstruction remain open. |
| `test_pendulum_period_history.py` | `dU/Y` is the marked clock; at `E=0` exact symmetry and Weierstrass invariants give square-lattice structure | **E** local algebra and exact special-leaf symmetry; **T0/T1** lifted-history reading | The Abel developing cover is downstream analytic clock history, not the canonical raw-history unfolding. |
| `test_pendulum_period_contour.py` | a supplied lifted contour closes and its quadrature converges to the beta-value period | **N** numerical estimate with exact reference | Hand-chosen cycle, empirical refinement, no interval error bound or automatic homology discovery. |
| `test_pendulum_period_matrix.py` | two supplied lifted cycles give a sampled `tau` near `i` with positive imaginary part | **N** numerical candidate period matrix | Shape checks are not a proof of a canonical symplectic basis; topology comes from the next file. |
| `test_pendulum_cycle_intersection.py` | sheet continuation removes one false projected crossing and gives sampled intersection `A.B=1`; orientation reversal is a red team | **N** sampled topology/period compatibility | Polygonal transverse-crossing certificate, not deformation-invariant certified homology. |

The later P10--P13 record adds the missing global interpretation:

```text
primitive Cartesian process
  -> (U,Y) marked carrier and local decoder boundary
  -> additive Abel clock on a downstream analytic cover
  -> task-relative lattice kernel / fundamental domain
  -> transported physical unit frame
  -> separate continuous action coarea and finite deck-memory laws.
```

This chain validates much of the older intuition while narrowing it. The
elliptic curve and elliptic functions are downstream quotient geometry and
periodic decoders; they are not the primitive mechanism. The Bolza surface is
the product-sign quotient after adjoining a separate metric sheet, not a second
pendulum state presentation.

## 9. Complete coverage ledger

This section is deliberately mechanical: every executable essay in
`tests/classical/` appears exactly as a stable audit handle.

```text
test_am_character_transport.py
test_am_process_direction.py
test_am_process_language_calibration.py
test_central_payload_process_calibration.py
test_coupled_diagonal_canonical_horizontal_lift.py
test_coupled_scalar_canonical_observer.py
test_dilation_characters.py
test_even_power_oscillator_genus_hierarchy.py
test_even_power_oscillator_process_calibration.py
test_galilean_bargmann_cocycle.py
test_galilean_central_residual.py
test_galilean_character_obstruction.py
test_galilean_family_action.py
test_harmonic_oscillator_additive_module.py
test_harmonic_oscillator_coefficient_extension.py
test_kepler_radial_canonical_horizontal_lift.py
test_magnetic_translation_central_residual.py
test_pendulum_cycle_intersection.py
test_pendulum_discovery_layer.py
test_pendulum_local_branch_decoder.py
test_pendulum_observable_quotient_fiber.py
test_pendulum_observer_selection.py
test_pendulum_period_contour.py
test_pendulum_period_history.py
test_pendulum_period_matrix.py
test_pendulum_process_geometry.py
test_pendulum_structured_observers.py
test_perturbed_kepler_eccentricity_canonicalization.py
test_restricted_kepler_canonical_decomposition.py
test_restricted_riccati_canonical_observer.py
test_riccati_canonical_horizontal_lift.py
test_translation_characters.py
test_two_frequency_oscillator_refinement_red_team.py
```

The hygiene test `tests/test_classical_recalibration_hygiene.py` keeps this
ledger and the per-construction matrix in
`docs/66-classical-process-language-calibration.md` fail-closed when the
directory gains a new executable essay.  It checks coverage, evidence-state
syntax, and the three-way cover separation only; it does not certify any
mathematical claim.

## 10. Recalibration order

The work should proceed in narrow, independently reviewable stages.

### R0 — complete inventory and one unambiguous correction (complete)

- record the original 30-file/65-test baseline and the present 33-file/80-test
  suite after adding the A/M, oscillator, and central-payload process spines;
- keep a fail-closed coverage ledger;
- correct the even-power oscillator wording from “discovered energy” to
  “supplied candidate certified as invariant” and from generic “quotient” to
  “energy-leaf algebraic carrier” where task semantics are absent.
- migrate every classical test to the canonical `process_geometry` namespace;
- name polynomial elimination results as observable algebraic images;
- retain the pendulum-only structured-pairing grammar under Experimental.

### R1 — A/M and oscillator calculation contracts (complete for declared tasks)

- maintain the fail-closed per-file/process-construction matrix in
  `docs/66-classical-process-language-calibration.md`;
- use the harmonic member as the second end-to-end real task calibration,
  with an exact quarter-period literal-history subtask while declining a claim
  about intrinsic unfolding of every continuous history;
- state the task served by each character/module presentation;
- record closure domain, controlled extensions, decoder need, and singular
  coefficient regimes;
- keep cost multi-axis; do not add a universal coefficient-language cost.

### R2 — central lifted payloads (complete for finite composition tasks)

- use the shared central-payload spine to separate visible and lifted tasks,
  certify information loss, lowering, coboundary covariance, and units;
- state visible versus lifted tasks explicitly;
- record units and gauge/coboundary covariance;
- distinguish cocycle representative, central extension class, and physical
  decoder obligations;
- red-team any attempted generic connection/holonomy promotion.

### R3 — moving-frame family

- rename or locally qualify the two meanings of `observer` in exposition;
- add task, chart, branch, unit, and failure contracts;
- test whether coefficient-jet objectives survive admissible time/frame
  changes before giving them broader canonicalization weight.

### R4 — Kepler end-to-end guide

- connect Cartesian primitive data, physical units, radial/eccentricity lifts,
  local decoders, perturbation tasks, numerical evaluators, and singular
  outcomes;
- use the pendulum architecture as a checklist, not as a theorem that the same
  elliptic/global completion must appear.

### R5 — pendulum legacy alignment

- make P0--P9 wording point explicitly to the P10--P13 interpretation;
- retain exact versus sampled evidence labels;
- do not duplicate the family mathematics already owned by
  `docs/vignettes/simple-pendulum.md` and `MATHEMATICAL_CORE.md`.

## 11. Theory, architecture, and API effects

### Mathematical Core

**Unchanged.** The audit applies its distinctions and finds no contradiction
to the present core. The strongest support is negative: older examples become
more coherent when algebraic image, task quotient, moving frame, analytic
cover, unit frame, cost, and decoder are kept separate.

### Engineering Architecture

**Support and refine.** Exact symbolic methods remain effective across the
families, and the sampled pendulum files correctly remain numerical rather than
certified approximate. The audit refines the backlog by locating missing task,
unit, failure, decoder, baseline, and total-cost fields per family.

### Theory Map

**Unchanged.** A/M remains a model organism; canonical-observer records remain
local Experimental slices; cocycles remain exact finite retained-payload
calibrations; the generic history-evaluation transversal remains T0/T1; no
universal continuous/discrete complexity law is inferred.

### API pressure

**Boundary correction, no promotion.** The public Discovery surface now says
`observable` and `algebraic image` for the mature bounded polynomial path.
Historical observer/quotient spellings remain 0.0.x aliases. The structured
pairing proposal grammar moves to `process_geometry.experimental` because its
complete evidence is still pendulum-local. No generic noun, solver facade, or
Theory Map object is introduced.

## 12. Kill conditions for later stages

Any later family-level strengthening must be weakened or rejected if:

- a claimed task presentation identifies states that a declared continuation
  distinguishes;
- a purported decoder fails at an unreported branch or singular stratum;
- a `canonical` choice changes under an allowed frame/gauge transformation
  with no declared equivalence;
- a claimed analysis language is not closed and has no controlled extension;
- a numerical claim lacks convergence/reference evidence or silently crosses a
  branch boundary;
- an apparent cost win disappears after discovery, coefficient-language,
  storage, residual, and decoding costs are charged;
- an algebraic image is promoted to a semantic quotient without a task and
  information contract;
- an analytic or topological cover is identified with full history unfolding
  without a theorem connecting them.

These conditions are more valuable than a forced common abstraction: they let
each classical model tell us where the current theory genuinely applies and
where it must remain open.

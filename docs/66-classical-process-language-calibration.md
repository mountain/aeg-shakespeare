# Classical process-language calibration matrix

**Status:** completed zero-`OPEN` calibration record.  This document is a
fail-closed, per-file inventory of every executable essay in
`tests/classical/`.  It refines the family judgments in
`36-classical-reexpression-audit.md`; it does not promote a new Mathematical
Core, Theory Map node, or public API object.

## 1. What “calibrated” means

An equation is not by itself a Process Geometry calibration.  For a declared
continuation task, the complete comparison order is

```text
primitive process and admissible histories
  -> declared continuation task
  -> task-sufficient lift / moving frame / presentation
  -> transported clock, resource, unit, or residual
  -> stopping section and task quotient
  -> retained decoder and explicit information loss
  -> symbolic or numerical analysis
  -> boundary, failure, baseline, and total-cost statement.
```

Three constructions must be audited independently:

| Axis | Question | Forbidden shortcut |
| --- | --- | --- |
| `Hinf` | Is the raw literal-history unfolding actually constructed? | Calling any convenient phase variable “the history space”. |
| `Ctop` | Is a topological cover, its deck action, and its branch/singular locus constructed or imported explicitly? | Inferring a universal cover from an algebraic equation alone. |
| `Can` | Is an analytic developing cover/clock and its period kernel constructed? | Identifying an Abelian clock with the raw history unfolding. |

They may coincide in a particular declared task, but no repository-wide
theorem identifies them.  Every row below must therefore report all three.

## 2. Evidence states

The matrix uses one primary state per cell so absence cannot be hidden by
prose.

| State | Meaning |
| --- | --- |
| `E` | exact symbolic or finite executable evidence in this file |
| `N` | numerical file-local evidence with the stated non-certified boundary |
| `D` | object/task/branch/gauge is explicitly declared, not intrinsically derived |
| `F` | evidence is supplied by a named companion in the same family |
| `I` | substantial classical theorem is imported and cited, not executed |
| `NA` | explicitly not required for the narrow declared task |
| `OPEN` | absent or unresolved; permitted during a working cycle but forbidden by the completed-matrix regression gate |

`F`, `I`, and `D` are not weaker spellings of `E`.  A row is not
end-to-end merely because its family eventually supplies some missing cells.

Column abbreviations are: primitive process/carrier (`P`), admissible history
(`H`), continuation task (`T`), task lift or moving frame (`L`), raw-history
unfolding (`Hinf`), topological cover (`Ctop`), analytic cover/clock (`Can`),
transported resource/unit/residual (`R`), task quotient and information loss
(`Q`), decoder/reconstruction (`Dec`), analysis/evaluator/certificate (`A`),
and boundary/failure/baseline/cost (`B`).

## 3. Fail-closed per-file matrix

The `Next gate` column names the smallest honest strengthening.  It is not a
promise that every row should grow into a public abstraction.

<!-- CLASSICAL_CALIBRATION_MATRIX:BEGIN -->
| File | Family | P | H | T | L | Hinf | Ctop | Can | R | Q | Dec | A | B | Next gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `test_am_character_transport.py` | A/M | E | F | D | F | F | NA | NA | E | F | NA | E | D | Response-space enlargement remains a separate research task. |
| `test_am_process_direction.py` | A/M | E | E | D | F | F | NA | NA | E | F | F | E | D | Test nonconstant path-flow evaluation without changing the task contract. |
| `test_am_process_language_calibration.py` | A/M | E | E | D | E | E | NA | NA | E | E | E | E | E | Search for a canonical or costed word section only under a declared workload. |
| `test_central_payload_process_calibration.py` | central payload | E | E | D | E | E | NA | NA | E | E | E | E | E | Calibrate a genuinely path-topological task before introducing holonomy. |
| `test_coupled_diagonal_canonical_horizontal_lift.py` | moving frame | E | E | D | E | NA | NA | NA | E | D | E | E | E | Test covariance of the jet-count objective. |
| `test_coupled_scalar_canonical_observer.py` | moving frame | E | D | D | E | NA | NA | NA | E | D | E | E | E | Separate balance-gauge equivalence from task equivalence. |
| `test_dilation_characters.py` | A/M | E | F | D | F | F | NA | NA | E | F | NA | E | E | Mellin synthesis requires a new measure/completeness task. |
| `test_even_power_oscillator_genus_hierarchy.py` | oscillator | E | NA | D | NA | NA | NA | NA | E | NA | NA | E | E | A complex analytic task is optional future work, not missing from genus classification. |
| `test_even_power_oscillator_process_calibration.py` | oscillator | E | E | D | E | E | E | E | E | E | E | E | E | Extend the literal-history certificate beyond the quarter-period alphabet. |
| `test_galilean_bargmann_cocycle.py` | central payload | E | E | D | E | NA | NA | NA | E | E | E | E | D | Apply the linked family gauge/unit contract to a chosen physical convention. |
| `test_galilean_central_residual.py` | central payload | E | F | D | F | F | NA | NA | E | E | F | E | D | Connect the Hamiltonian realization to a dimensioned Bargmann phase decoder. |
| `test_galilean_character_obstruction.py` | central payload | E | F | D | F | F | NA | NA | E | D | F | E | D | Select a richer response space only after a declared task. |
| `test_galilean_family_action.py` | central payload | E | F | D | F | F | NA | NA | E | D | F | E | D | Add the massive affine term only in the lifted physical task. |
| `test_harmonic_oscillator_additive_module.py` | oscillator | E | F | D | E | F | NA | NA | E | D | F | E | D | Price module closure against the linked state-continuation workload. |
| `test_harmonic_oscillator_coefficient_extension.py` | oscillator | F | F | D | E | F | NA | NA | E | D | E | E | D | Price coefficient extension under a repeated evaluation workload. |
| `test_kepler_radial_canonical_horizontal_lift.py` | Kepler | E | E | D | E | NA | NA | NA | E | D | E | E | E | Add physical unit round-trip and global branch outcomes. |
| `test_magnetic_translation_central_residual.py` | central payload | E | E | D | E | NA | NA | NA | E | E | E | E | D | Apply the linked coboundary/unit contract to additional gauges. |
| `test_pendulum_cycle_intersection.py` | pendulum | F | N | F | N | NA | N | F | F | D | NA | N | N | Replace sampled crossings with certified homology evidence. |
| `test_pendulum_discovery_layer.py` | pendulum | F | NA | D | NA | NA | F | F | E | E | F | E | E | Distinguish bounded search completeness from task discovery. |
| `test_pendulum_local_branch_decoder.py` | pendulum | F | D | F | F | NA | E | F | F | E | E | E | E | Add global branch transport through turning charts. |
| `test_pendulum_observable_quotient_fiber.py` | pendulum | F | D | F | F | NA | E | F | F | E | F | E | E | Lift the state-fibre result to a broader history task only if requested. |
| `test_pendulum_observer_selection.py` | pendulum | F | NA | D | NA | NA | F | F | F | D | F | E | E | Price downstream decoder and evaluator costs. |
| `test_pendulum_period_contour.py` | pendulum | F | N | D | N | NA | N | N | N | D | NA | N | N | Add certified quadrature and automatic cycle failure outcomes. |
| `test_pendulum_period_history.py` | pendulum | F | E | D | E | NA | I | E | E | E | NA | E | E | A global state decoder is outside the declared period-law task. |
| `test_pendulum_period_matrix.py` | pendulum | F | N | D | N | NA | I | N | N | D | NA | N | N | Certify a symplectic cycle basis before canonical shape claims. |
| `test_pendulum_process_geometry.py` | pendulum | E | D | F | E | NA | F | F | E | F | F | E | E | Connect primitive flow histories only when a history-sensitive task is declared. |
| `test_pendulum_structured_observers.py` | pendulum | F | NA | D | NA | NA | F | F | F | D | F | E | E | Generalize or retain the proposal grammar as pendulum-local. |
| `test_perturbed_kepler_eccentricity_canonicalization.py` | Kepler | E | E | D | E | NA | NA | NA | E | D | E | E | E | Add circular/collision outcomes and dimensional covariance. |
| `test_restricted_kepler_canonical_decomposition.py` | Kepler | E | NA | D | D | NA | NA | NA | E | NA | E | E | D | Add a trajectory task before asking for histories or covers. |
| `test_restricted_riccati_canonical_observer.py` | moving frame | E | D | D | E | NA | NA | NA | E | D | E | E | E | Add discriminant-crossing outcome and time covariance. |
| `test_riccati_canonical_horizontal_lift.py` | moving frame | E | E | D | E | NA | NA | NA | E | D | E | E | E | Red-team jet count under admissible reparameterization. |
| `test_translation_characters.py` | A/M | E | F | D | F | F | NA | NA | E | F | NA | E | D | Fourier synthesis requires a new measure/completeness task. |
| `test_two_frequency_oscillator_refinement_red_team.py` | oscillator | E | NA | D | E | NA | NA | NA | E | D | E | E | E | Attach the Pareto result to an explicit repeated workload. |
<!-- CLASSICAL_CALIBRATION_MATRIX:END -->

### Family evidence owners for `F`

| Family | Linked evidence owner |
| --- | --- |
| A/M | `test_am_process_language_calibration.py` for literal histories, affine task quotient, decoder, units, and boundary |
| oscillator | `test_even_power_oscillator_process_calibration.py` for phase histories, covers, task quotient, decoder, units, and boundary |
| central payload | `test_central_payload_process_calibration.py`, with the Bargmann and magnetic cocycle files retaining their physical formulas |
| pendulum | `docs/vignettes/simple-pendulum.md`, the P0--P13 family, `test_pendulum_am_marked_carrier_bridge.py`, `test_pendulum_lifted_clock_global_quotient.py`, and `test_pendulum_unit_history_fundamental_domain.py` |

`NA` is always task-relative.  In particular, a period-integration file does
not need a physical-state decoder, an algebraic genus-classification file does
not need a history cover, and a finite cocycle-composition task does not need a
topological or analytic developing cover.  A later broader task must reopen
the cell rather than inherit `NA` automatically.

### Fail-closed `NA` resolution ledger

The following groups justify every `NA` in the matrix.  The hygiene test checks
that every row containing `NA` appears here.  “Reopen” means change the cell
back to `OPEN` on the working branch until the broader task has evidence.

<!-- CLASSICAL_NA_LEDGER:BEGIN -->

- **A/M response-law tasks:** `test_am_character_transport.py`,
  `test_dilation_characters.py`, and `test_translation_characters.py` verify a
  supplied scalar response/obstruction.  `Ctop` and `Can` are unnecessary;
  `Dec` is unnecessary because response evaluation, not state/history
  reconstruction, is the output.  Reopen when Fourier/Mellin synthesis or a
  state-reconstruction task is declared.
- **A/M affine endpoint tasks:** `test_am_process_direction.py` and
  `test_am_process_language_calibration.py` predict affine scalar endpoints.
  `Ctop` and `Can` are unnecessary; literal word history is retained
  independently.  Reopen when winding, monodromy, or path homotopy becomes
  task-visible.
- **Finite central-composition tasks:**
  `test_central_payload_process_calibration.py`,
  `test_galilean_bargmann_cocycle.py`,
  `test_galilean_central_residual.py`,
  `test_galilean_character_obstruction.py`,
  `test_galilean_family_action.py`, and
  `test_magnetic_translation_central_residual.py` evaluate finite composition
  and central residuals.  Topological/analytic covers are unnecessary;
  file-local `Hinf=NA` means literal words are owned by the linked family
  spine.  Reopen when actual path homotopy or connection holonomy is declared.
- **Local moving-frame tasks:**
  `test_coupled_diagonal_canonical_horizontal_lift.py`,
  `test_coupled_scalar_canonical_observer.py`,
  `test_restricted_riccati_canonical_observer.py`,
  `test_riccati_canonical_horizontal_lift.py`,
  `test_kepler_radial_canonical_horizontal_lift.py`, and
  `test_perturbed_kepler_eccentricity_canonicalization.py` certify local chart,
  normalization, transport, and reconstruction identities.  Global history
  unfolding and covers are unnecessary on the declared regular chart.  Reopen
  for discriminant crossing, collision, circular, or global continuation tasks.
- **Oscillator algebra/representation tasks:**
  `test_even_power_oscillator_genus_hierarchy.py`,
  `test_harmonic_oscillator_additive_module.py`,
  `test_harmonic_oscillator_coefficient_extension.py`, and
  `test_two_frequency_oscillator_refinement_red_team.py` classify algebraic
  carriers or compare exact finite representations.  Their non-required
  history/cover/decoder axes are owned by the harmonic process spine or are
  outside the algebraic task.  Reopen for a complex uniformization/Jacobian
  decoder or a history-sensitive repeated workload.
- **Pendulum bounded search tasks:** `test_pendulum_discovery_layer.py`,
  `test_pendulum_observer_selection.py`, and
  `test_pendulum_structured_observers.py` search algebraic candidates under a
  fixed finite budget.  Physical histories and task lifts are unnecessary to
  the search certificate.  Reopen when the candidate grammar itself is learned
  from continuation semantics.
- **Pendulum local state/fibre tasks:**
  `test_pendulum_process_geometry.py`,
  `test_pendulum_observable_quotient_fiber.py`, and
  `test_pendulum_local_branch_decoder.py` certify local carrier, fibre, and
  decoder facts.  Raw history unfolding is unnecessary to those state-local
  claims.  Reopen for a primitive-history equivalence theorem.
- **Pendulum period/topology tasks:**
  `test_pendulum_period_history.py`,
  `test_pendulum_period_contour.py`,
  `test_pendulum_period_matrix.py`, and
  `test_pendulum_cycle_intersection.py` operate on declared analytic lifted
  paths/cycles.  Primitive raw-history unfolding is unnecessary; physical-state
  decoding is not an output of period or intersection evaluation.  Reopen when
  a global physical trajectory decoder is part of the task.
- **Restricted Kepler module task:**
  `test_restricted_kepler_canonical_decomposition.py` exactly decomposes and
  reconstructs one supplied forcing in a finite function module.  Trajectory
  histories, covers, and a continuation task quotient are unnecessary.  Reopen
  when the forcing decomposition must drive a global orbital prediction task.

<!-- CLASSICAL_NA_LEDGER:END -->

## 4. The oscillator vertical slice

The new oscillator spine is the second example, after the pendulum family, to
place a declared continuation task beside a cover, quotient, decoder, unit
map, evaluator, and failure boundary.  Its scope is deliberately the real
harmonic task; the quartic and sextic members add exact real clock laws but not
global complex decoders.

| Process-language object | Harmonic realization | Exact relation | What is forgotten / boundary |
| --- | --- | --- | --- |
| Primitive process | `dx/dt=p/M`, `dp/dt=-M*omega^2*x` | Hamiltonian energy is constant | Positive `M`, `omega`, and nonzero amplitude are declared. |
| Unit frame | `tau=omega*t`, `x=A*X`, `p=M*omega*A*Y` | `X'=Y`, `Y'=-X` | Physical output requires the inverse map. |
| Raw literal history | quarter-period `ProcessWord` over `{R,L}` | concatenation before interpretation | Exact only for the declared discrete subtask; word depth is retained. |
| Admissible lifted history | `tau in R` | `(X,Y)=(cos(tau),-sin(tau))` | This is not the intrinsic unfolding of every continuous command/path history. |
| Topological cover | `R -> S^1` | deck action `tau -> tau+2*pi*k` | At zero energy the orbit collapses and the cover description changes. |
| Analytic clock cover | the same `tau` in this genus-zero task | one clock period is `2*pi` | Equality with the topological cover is task-local, not universal. |
| Full-state task quotient | `tau mod 2*pi` | identical future carrier for every common increment | Integer winding is discarded. |
| Position observable | `U=cos(tau)` | `U(tau)=U(-tau)` | Velocity sign is lost, so `U` alone is not continuation sufficient. |
| Retained decoder | `(U,sigma) -> (U, sigma*sqrt(1-U^2))` | exact away from the branch boundary | The chart is singular at `U=+/-1`. |
| Resource / clock law | `T=dOmega/dE` | beta recurrence for `m=2,4,6` | It is a real period law, not a complex uniformization theorem. |
| Physical lowering | `T_phys=2*pi/omega`, `Omega=2*pi*E/omega` | exact unit round-trip | No numerical or runtime-economy claim is made. |

This slice yields a useful separation.  The complex energy carriers for
`m=2,4,6` have genera `0,1,2`, while every regular connected positive-energy
real orbit is a circle and hence has universal cover `R`.  Complex
function-language genus therefore does **not** measure real history-cover
complexity.  The quartic and sextic cases may require richer complex analytic
languages even though their real periodic continuation task has one clock
period.

## 5. Repository-wide conclusions exposed by the matrix

1. **Literal histories are now executable where the task needs them.** A/M,
   the harmonic quarter-period subtask, and the central-payload finite word
   task preserve ordered `ProcessWord` histories before quotienting.  This does
   not identify those word unfoldings with topological or analytic covers, nor
   does it claim an intrinsic unfolding of every continuous command space.
2. **Continuation semantics is now declared or linked, never inferred from an
   equation.** Stage files that certify algebraic relations, local frames, or
   numerical periods either name their narrow task, link to the family task,
   or mark history semantics `NA`.  `NA` cannot flow to a broader future task.
3. **A cover is task-dependent, not compulsory decoration.** Local moving-
   frame and finite cocycle tasks explicitly mark cover construction `NA`.
   Global periodic tasks must instead expose deck, branch, and decoder data.
4. **Family links do not erase local evidence levels.** `F` makes reuse
   visible while preventing a stage file from claiming its companion's
   theorem as file-local execution.
5. **Zero unclassified cells is an engineering invariant, not a completeness
   theorem.** Every previous `OPEN` is resolved by executable evidence, a
   named family owner, a declared/imported input, or task-relative `NA`.
   Stronger tasks may create new governed gaps, but cannot inherit a status
   without re-audit.

## 6. API and maturity allocation

| Concept | Current owner | Decision after calibration |
| --- | --- | --- |
| Literal finite ordered histories | `process_geometry.process.history.ProcessWord` | Reuse Public API: it preserves words without imposing task semantics, exactly as required by A/M, oscillator, and central-payload spines. |
| Exact finite continuation-stable task minimization | `process_geometry.experimental.FiniteTaskQuotient` | Retain Experimental: the oscillator uses only its declared four-state slice; continuous/general promotion is not justified. |
| Exact local process derivation, finite generated presentations, relation kernels, algebraic profiles, finite cocycles | `process_geometry` public namespaces | Retain: independently calibrated reusable mechanisms. |
| Bounded observable discovery and observable algebraic images | `process_geometry.discovery` | Retain semantic names; do not call every image a task quotient. |
| Structured pendulum pairing proposals and local canonical moving-frame records | `process_geometry.experimental` | Retain Experimental until a second independent organism and covariance tests exist. |
| Named oscillator, pendulum, Kepler, Riccati, Galilean, and magnetic tasks | `tests/classical` plus vignette docs | Keep as executable knowledge; named examples are not package solvers. |
| Intrinsic continuous-history discovery, automatic task quotient, universal cover constructor, global decoder, universal unit/cost schema | no API owner | Outside the completed narrow tasks; promotion requires new constructions and independent calibrations. |

## 7. Completion and regression gates

A family may be described as an **end-to-end task calibration** only when it
has explicit primitive/history data, a declared continuation task, a
task-sufficient construction, resource/unit/residual transport where relevant,
quotient and information-loss semantics, decoder or justified `NA`, analysis
evidence, and boundary/failure/baseline/cost statements.  Each of `Hinf`,
`Ctop`, and `Can` must independently be `E`, `N`, `D`, `F`, `I`, or `NA` in
the completed matrix; an unqualified word `cover` is insufficient. `OPEN` may
appear only while a new calibration cycle is actively resolving it.

`tests/test_classical_recalibration_hygiene.py` parses the marked matrix,
requires every `tests/classical/test_*.py` file exactly once, validates every
state, and fixes the oscillator cover-separation regression.  The test
certifies audit structure only.  It does not convert `D`, `F`, `I`, or `NA`
into file-local mathematical evidence.

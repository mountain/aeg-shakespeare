# Classical process-language calibration matrix

**Status:** governed R1 calibration record.  This document is a fail-closed,
per-file inventory of every executable essay in `tests/classical/`.  It
refines the family judgments in `36-classical-reexpression-audit.md`; it does
not promote a new Mathematical Core, Theory Map node, or public API object.

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
| `OPEN` | absent or unresolved; this is a result, not a test failure |

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
| `test_am_character_transport.py` | A/M | E | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | E | OPEN | OPEN | E | D | Declare the continuation task and response decoder need. |
| `test_am_process_direction.py` | A/M | E | E | OPEN | OPEN | OPEN | OPEN | OPEN | E | OPEN | OPEN | E | D | State task sufficiency, units, and cost for the exact path flow. |
| `test_coupled_diagonal_canonical_horizontal_lift.py` | moving frame | E | E | D | E | NA | NA | NA | E | D | E | E | E | Test covariance of the jet-count objective. |
| `test_coupled_scalar_canonical_observer.py` | moving frame | E | D | D | E | NA | NA | NA | E | D | E | E | E | Separate balance-gauge equivalence from task equivalence. |
| `test_dilation_characters.py` | A/M | E | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | E | OPEN | OPEN | E | E | Add task, decoder policy, and unit covariance on positive scales. |
| `test_even_power_oscillator_genus_hierarchy.py` | oscillator | E | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | E | OPEN | OPEN | E | E | Connect complex carrier genus to a declared analytic task. |
| `test_even_power_oscillator_process_calibration.py` | oscillator | E | E | D | E | OPEN | E | E | E | E | E | E | E | Construct raw-history unfolding or prove when it factors through the phase cover. |
| `test_galilean_bargmann_cocycle.py` | central payload | E | E | D | E | NA | NA | NA | E | E | E | E | D | Audit units and coboundary/gauge covariance. |
| `test_galilean_central_residual.py` | central payload | E | D | D | D | OPEN | OPEN | OPEN | E | E | OPEN | E | D | Supply the lifted decoder and finite-task boundary. |
| `test_galilean_character_obstruction.py` | central payload | E | OPEN | D | OPEN | OPEN | OPEN | OPEN | E | D | OPEN | E | D | Link the obstruction to the retained finite cocycle. |
| `test_galilean_family_action.py` | central payload | E | OPEN | D | OPEN | OPEN | OPEN | OPEN | E | D | OPEN | E | D | State visible versus massive lifted tasks. |
| `test_harmonic_oscillator_additive_module.py` | oscillator | E | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | E | OPEN | OPEN | E | D | Tie module closure to a continuation workload. |
| `test_harmonic_oscillator_coefficient_extension.py` | oscillator | F | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | E | D | E | E | D | Price extension and state which future queries it preserves. |
| `test_kepler_radial_canonical_horizontal_lift.py` | Kepler | E | E | D | E | NA | NA | NA | E | D | E | E | E | Add physical unit round-trip and global branch outcomes. |
| `test_magnetic_translation_central_residual.py` | central payload | E | E | D | E | NA | NA | NA | E | E | E | E | D | Audit gauge covariance and physical phase units. |
| `test_pendulum_cycle_intersection.py` | pendulum | F | N | F | N | OPEN | N | F | F | D | OPEN | N | N | Replace sampled crossings with certified homology evidence. |
| `test_pendulum_discovery_layer.py` | pendulum | F | OPEN | F | OPEN | OPEN | F | F | E | E | F | E | E | Distinguish bounded search completeness from task discovery. |
| `test_pendulum_local_branch_decoder.py` | pendulum | F | D | F | F | OPEN | E | F | F | E | E | E | E | Add global branch transport through turning charts. |
| `test_pendulum_observable_quotient_fiber.py` | pendulum | F | D | F | F | OPEN | E | F | F | E | F | E | E | Lift the state-fibre result to declared history equivalence. |
| `test_pendulum_observer_selection.py` | pendulum | F | OPEN | F | OPEN | OPEN | F | F | F | D | F | E | E | Price downstream decoder and evaluator costs. |
| `test_pendulum_period_contour.py` | pendulum | F | N | F | N | OPEN | N | N | N | D | OPEN | N | N | Add certified quadrature and automatic cycle failure outcomes. |
| `test_pendulum_period_history.py` | pendulum | F | E | F | E | OPEN | I | E | E | E | OPEN | E | E | Construct or explicitly exclude a global analytic decoder. |
| `test_pendulum_period_matrix.py` | pendulum | F | N | F | N | OPEN | I | N | N | D | OPEN | N | N | Certify a symplectic cycle basis before canonical shape claims. |
| `test_pendulum_process_geometry.py` | pendulum | E | D | F | E | OPEN | F | F | E | F | F | E | E | Connect primitive histories to the later task quotient explicitly. |
| `test_pendulum_structured_observers.py` | pendulum | F | OPEN | F | OPEN | OPEN | F | F | F | D | F | E | E | Generalize or retain the proposal grammar as pendulum-local. |
| `test_perturbed_kepler_eccentricity_canonicalization.py` | Kepler | E | E | D | E | NA | NA | NA | E | D | E | E | E | Add circular/collision outcomes and dimensional covariance. |
| `test_restricted_kepler_canonical_decomposition.py` | Kepler | E | OPEN | OPEN | D | OPEN | OPEN | OPEN | E | OPEN | E | E | D | Declare a perturbation task and projection/cost contract. |
| `test_restricted_riccati_canonical_observer.py` | moving frame | E | D | D | E | NA | NA | NA | E | D | E | E | E | Add discriminant-crossing outcome and time covariance. |
| `test_riccati_canonical_horizontal_lift.py` | moving frame | E | E | D | E | NA | NA | NA | E | D | E | E | E | Red-team jet count under admissible reparameterization. |
| `test_translation_characters.py` | A/M | E | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | E | OPEN | OPEN | E | D | Declare synthesis/verification task and decoder policy. |
| `test_two_frequency_oscillator_refinement_red_team.py` | oscillator | E | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | E | D | E | E | E | Attach the Pareto result to an explicit repeated workload. |
<!-- CLASSICAL_CALIBRATION_MATRIX:END -->

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
| Admissible lifted history | `tau in R` | `(X,Y)=(cos(tau),-sin(tau))` | This is not the raw literal-history unfolding. |
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

1. **Raw-history unfolding is an open transversal.** No classical file
   currently executes the literal full-history unfolding described by the
   Mathematical Core.  The pendulum uses a downstream Abelian developing
   cover; the harmonic spine uses a phase cover.  Neither may be silently
   relabelled `Hinf`.
2. **Continuation semantics is the second open transversal.** Many files
   certify algebraic relations, local frames, or finite cocycles without a
   future-equivalence task.  Their mathematics survives, but they are stages,
   not end-to-end process quotients.
3. **A cover is task-dependent, not compulsory decoration.** Local moving-
   frame and finite cocycle tasks explicitly mark cover construction `NA`.
   Global periodic tasks must instead expose deck, branch, and decoder data.
4. **Family links do not erase local evidence levels.** `F` makes reuse
   visible while preventing a stage file from claiming its companion's
   theorem as file-local execution.
5. **The next extraction target is a contract, not a universal solver.** The
   repeatable object is this evidence matrix and its fail-closed validator.
   The missing mathematical constructions remain research work.

## 6. API and maturity allocation

| Concept | Current owner | Decision after calibration |
| --- | --- | --- |
| Exact local process derivation, finite generated presentations, relation kernels, algebraic profiles, finite cocycles | `process_geometry` public namespaces | Retain: independently calibrated reusable mechanisms. |
| Bounded observable discovery and observable algebraic images | `process_geometry.discovery` | Retain semantic names; do not call every image a task quotient. |
| Structured pendulum pairing proposals and local canonical moving-frame records | `process_geometry.experimental` | Retain Experimental until a second independent organism and covariance tests exist. |
| Named oscillator, pendulum, Kepler, Riccati, Galilean, and magnetic tasks | `tests/classical` plus vignette docs | Keep as executable knowledge; named examples are not package solvers. |
| Generic raw-history unfolding, automatic task quotient, universal cover constructor, global decoder, universal unit/cost schema | no API owner | Keep `OPEN`; promotion before constructions and independent calibrations is forbidden. |

## 7. Completion and regression gates

A family may be described as an **end-to-end task calibration** only when it
has explicit primitive/history data, a declared continuation task, a
task-sufficient construction, resource/unit/residual transport where relevant,
quotient and information-loss semantics, decoder or justified `NA`, analysis
evidence, and boundary/failure/baseline/cost statements.  Each of `Hinf`,
`Ctop`, and `Can` must independently be `E`, `N`, `D`, `F`, `I`, `NA`, or
`OPEN`; an unqualified word `cover` is insufficient.

`tests/test_classical_recalibration_hygiene.py` parses the marked matrix,
requires every `tests/classical/test_*.py` file exactly once, validates every
state, and fixes the oscillator cover-separation regression.  The test
certifies audit structure only.  It does not convert `D`, `F`, `I`, or `OPEN`
into mathematical evidence.

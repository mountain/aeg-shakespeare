# Process Geometry — current research status and evidence ledger

**Status:** dated mainline orientation and evidence index; not a frozen
mathematical specification, theory-promotion record, or Public API contract.

**Snapshot:** 2026-08-27, after merge commit `2209008` (PR #119).  Update this
document when a result materially changes the repository-wide picture, not for
every local phase note.

**Required prior reading:** [`MATHEMATICAL_CORE.md`](MATHEMATICAL_CORE.md),
then [`RESEARCH_PROGRAM.md`](RESEARCH_PROGRAM.md).  The Core records the
present mathematical synthesis; the Programme states the conjectural
Arithmetic Generativity direction.  This document answers a different
question: **what has the current mainline actually earned, where is the
evidence, and what has it not earned?**  Continue with
[`ENGINEERING_ARCHITECTURE.md`](ENGINEERING_ARCHITECTURE.md) for feasible
solver decisions and [`THEORY_MAP.md`](THEORY_MAP.md) for theory position and
maturity.

When this ledger and a detailed theorem, certificate, or phase record disagree,
the detailed artifact wins and this ledger must be corrected.

---

## 1. Read the project as three coupled artifacts

Process Geometry is not only a Python package and not only a sequence of
research notes.  The current repository has three coupled outputs:

1. **a mathematical research programme** about histories, task-relative
   distinguishability, semantic compression, fibres, objectification, and
   process-supported analysis, guided by the conjectural Arithmetic
   Generativity obligations in [`RESEARCH_PROGRAM.md`](RESEARCH_PROGRAM.md);
2. **a research software toolkit** implementing deliberately narrow process,
   presentation, discovery, and analysis contracts;
3. **an executable knowledge base** in which classical calibrations, exact
   finite theorems, counterexamples, numerical checks, and failed hypotheses
   remain linked to tests and claim boundaries.

The package still has no universal `solve()` interface and no theorem that all
processes admit one preferred arithmetic presentation.  That absence is a
present research boundary, not a summary of everything already achieved or an
abandonment of the unifying conjecture.  Programme obligations U1--U5 and E
identify which semantic, analytic, information-complexity, statistical,
objectification, covariance, and economy bridges each evidence chain pressures.

---

## 2. One-page verdict

| Layer | Earned on current mainline | Not yet earned |
| --- | --- | --- |
| Mother picture | two-axis foundation (horizontal distinguishability; vertical ontology growth), an emerging task-covariant history-evaluation transversal, the Effective Analysis constraint, and a separately labelled Arithmetic Generativity research programme | one proved universal carrier, one universal calculus, or Arithmetic Universality theorem |
| Exact semantics | finite continuation-stable minimization with distinguishing suffixes; task-relative adapters; explicit residual and decoder ledgers | a generic quotient/adapter category covering infinite, stochastic, continuous, and approximate processes |
| Structural mathematics | exact local and abstract laws, no-go theorems, and finite classifications listed in §3 | a newly promoted framework-wide T3/T4 foundation theorem |
| Analysis | concrete A/M, algebraic, Abelian, moving-frame, stochastic first-passage, and finite nonadditive response calculi | generic smooth V5 analytic closure or one canonical cross-rank derivative |
| End-to-end calibration | pendulum and real harmonic oscillator task spines; complete zero-`OPEN` classical evidence matrix | rigorous global numerical certification for every branch, cycle, and singular regime |
| External computation | a task-semantic pruning representation integrated into pinned Lonely Runner upstream code, with byte-identical outputs and measured speedups across solved and open-frontier workers | a proof of `LRC(13)`, a general-purpose downstream solver, or an independent external adopter |
| Software | installable `process_geometry` package; cross-domain `PresentationMorphism`; exact finite algorithms and bounded discovery components | backward-compatible 1.0 API, mandatory numerical ecosystem, or production solver façade |

The honest maturity statement is therefore:

> The repository contains theorem-level local/abstract results and one real
> downstream computational transfer, while its strongest framework-wide
> ontology and universality claims remain unpromoted research programs.

This is more precise than either “the project is already a mature new
mathematics” or “the project is only a governed research diary.”

---

## 3. Structural-law and obstruction ledger

The repository's T3 gate accepts an abstract theorem, universal property,
classification, functorial statement, or obstruction that no longer depends
on its motivating example.  Results of those forms now exist.  They have not
all received separate T3 promotion records, and none is promoted here as a
new framework-wide Core theorem.  An audit must therefore distinguish **no
foundational T3/T4 promotion yet** from **no theorem-level mathematics**.

| Exact result | Scope and strongest responsible claim | Evidence owner | Current placement |
| --- | --- | --- | --- |
| Interface-refinement monotonicity | for a finite labelled transition system, refining the declared interface refines the coarsest continuation-stable partition; total stable class count and `ceil(log2 N)` cannot decrease | [`MATHEMATICAL_CORE.md` §1.5](MATHEMATICAL_CORE.md#15-stopping-sections-fundamental-domains-and-task-residuals), [`test_padic_continuation_value_fiber.py`](../tests/research/test_padic_continuation_value_fiber.py) | abstract finite law in the Core; no generic infinite extension |
| Finite quotient / predicate correspondence | a surjective finite task quotient retains exactly the Boolean predicates constant on its fibres; nonfactoring predicates are explicit discriminators | [`18-phase11-archimedean-state-observer-duality-results.md`](../sonnet/local-field-projective-process-geometry/18-phase11-archimedean-state-observer-duality-results.md), [`test_archimedean_state_observer_duality.py`](../tests/research/test_archimedean_state_observer_duality.py) | exact finite duality; no infinite cofree observer |
| Projective strict-descent obstruction | no total binary operation on `P^1(K)` can both extend affine addition and be strictly equivariant under all `PGL2(K)` transformations; the operation must retain a frame or weaken its task/symmetry | [`20-phase12-locale-observer-history-behavior-results.md`](../sonnet/local-field-projective-process-geometry/20-phase12-locale-observer-history-behavior-results.md), [`test_locale_observer_history_behavior_duality.py`](../tests/research/test_locale_observer_history_behavior_duality.py) | theorem over characteristic-zero fields; research-local consequence for fibred semantics |
| Finite-part chart obstruction and jet transport | a finite part is not an invariant of an uncharted singular germ; for pole order `r`, the principal coefficients and the `(r+1)`-jet of an invertible chart change suffice for exact finite-part transport | same Phase 12A result and executable certificate | exact formal-local theorem; not a generic regularization calculus |
| Partition abelianization and all-composite weight lowering | ordered compositions quotient to the free commutative partition monoid; multiset union composes fibres and total weight lowers every composite exactly | [`22-phase12b-partition-fibres-rogers-ramanujan-results.md`](../sonnet/local-field-projective-process-geometry/22-phase12b-partition-fibres-rogers-ramanujan-results.md), [`test_partition_fibres_rogers_ramanujan.py`](../tests/research/test_partition_fibres_rogers_ramanujan.py) | fibred task-exact objectification for one declared task; no recovery of order or new arithmetic rank |
| Objectification-to-action implication | all-composite monoid lowering `L:P -> End(X)` induces a typed change action of `P` on `X` | [`24-phase12c-objectification-fibred-change-calculus-results.md`](../sonnet/local-field-projective-process-geometry/24-phase12c-objectification-fibred-change-calculus-results.md), [`test_objectification_fibred_change_calculus.py`](../tests/research/test_objectification_fibred_change_calculus.py) | exact finite/algebraic V4–V5 bridge; not an automatic observer calculus |
| Response nonautomaticity | response fibres may be empty or nonunique; endpoint reconstruction does not imply the cocycle law; a tautological full-endomorphism response need not compress anything | same Phase 12C result | exact obstruction ladder separating action, response, regularity, adequacy, and effectivity |
| Itô transport split | omitting the second-order correction passes exactly for 87 affine charts and fails for 155 nonlinear charts in the frozen stochastic grammar | [`05-phase2-task-quotient-results.md`](../sonnet/stochastic-feedback-trap-first-passage/05-phase2-task-quotient-results.md), [`test_stochastic_feedback_trap_phase2_quotient.py`](../tests/research/test_stochastic_feedback_trap_phase2_quotient.py) | exact bounded covariance/no-go certificate; not a universal stochastic calculus theorem |
| Riccati/projective degree obstruction | a constant two-dimensional linear lift projectivizes to at most a quadratic scalar field, so a generic nonzero cubic term cannot arise from the same mechanism | [`02-phase1-riccati-results.md`](../sonnet/am-conformal-chart-normal-forms/02-phase1-riccati-results.md), [`test_am_conformal_chart_riccati.py`](../tests/research/test_am_conformal_chart_riccati.py) | exact classical mechanism and neighboring no-go; no discovery or economy theorem |

These results matter even if a stronger universality conjecture later fails:
they identify exact descent conditions, necessary residuals, variance rules,
and nonautomaticity boundaries that any replacement theory must respect.

---

## 4. Major evidence chains

### 4.1 Framework and cross-domain software

| Evidence chain | What is established | Boundary |
| --- | --- | --- |
| Exact finite task semantics | stable partition refinement computes the coarsest finite deterministic task quotient and distinguishing continuations | Experimental scope only; no infinite/probabilistic promotion |
| `PresentationMorphism` | KdV, resistor networks, and braid/Markov systems force a common evidence-bearing cross-presentation record | no generic composition, inverse, category, or universal verifier |
| AEG V1–V4 | signed histories compress to Translation objects; Multiplication objectifies repeated-Addition endomorphisms; mixed words lower to `Z ⋊ N_{>0}` with `D_k T_a = T_(ka) D_k` | two arithmetic calibrations do not prove a generic rank ontology or V5 closure |
| Public analysis families | A/M process calculus, algebraic quotient profiles, and Abelian periods/cycles are executable concrete languages | none is declared the universal calculus of Process Geometry |

### 4.2 End-to-end continuous and classical calibration

The [simple pendulum vignette](vignettes/simple-pendulum.md) realizes the full
chain from Cartesian constrained dynamics through a task-visible marked cubic,
clock, analytic lift, period kernel, task-relative fundamental domain, unit
transport, sheet residual, decoder, elliptic readout, and action--period law.
It also explains why the Bolza surface is a product-sign quotient after an
additional metric sheet rather than the pendulum state space.

The harmonic oscillator is the second real-task spine.  It keeps raw
quarter-period words, the real universal cover, the full-state quotient,
position/velocity residual, decoder, unit map, and period/action evaluator
separate.  The exact genus comparison shows that complex function-language
genus does not measure real history-cover complexity.

[`66-classical-process-language-calibration.md`](66-classical-process-language-calibration.md)
now gives a fail-closed per-file matrix for every `tests/classical/` essay.
Every cell is exact, numerical, declared, linked, imported, or explicitly not
applicable; no unclassified `OPEN` cell remains.  This is an audit-completeness
result, not a theorem that every classical problem is solved end to end.

### 4.3 Real downstream computation: Lonely Runner

The Lonely Runner line is the clearest answer to “does any representation in
this repository change an external computation?”  Exact future-repair
semantics led to a requirement-antichain representation and an exact two-slot
transversal pruning certificate.  The rule was frozen on solved cases, patched
into a pinned upstream C++ implementation, and checked by byte-identical
canonical outputs.

- solved frontier `K=8..12`: measured median speedups of about `1.15x–1.21x`;
- frozen open case `K=13, p=199`: the first three workers retained exact output
  equality and showed speedups of `1.047x`, `1.116x`, and `1.205x`;
- `LRC(13)` remains open, and later continuous-contact work has no proved bridge
  back to the modular/lift proof chain.

See [`sonnet/lonely-runner/README.md`](../sonnet/lonely-runner/README.md) and
the Phase 15A audit linked there.  This is a real solver improvement produced
by task-semantic representation work; it is not yet evidence of a general
Process Geometry solver or independent adoption.

---

## 5. Active Sonnet status

| Sonnet | Current completed boundary | Next honest gate |
| --- | --- | --- |
| [`local-field-projective-process-geometry`](../sonnet/local-field-projective-process-geometry/README.md) | bounded Phases 0–12C complete: rational/place carriers, finite Bellman and stable fibres, frame/duality/descent obstructions, partition fibres, and a graded change-action/response calculus | unexecuted locale/cofree/place-indexed workloads or a new independently justified extraction; no generic calculus/API |
| [`boltzmann-bbgky-h-theorem`](../sonnet/boltzmann-bbgky-h-theorem/README.md) | through independent Phases 1J-A/C2 and 1J-B5: finite collision response cocycle; whole-event flux contract; fixed/global formal marking; signed-current audit; bounded one-layer marked Penrose identity with exact root routing, independent sign axes, and signed large-component remainder | carry a layer-indexed mark through the exact signed recurrence (5.62)--(5.63), then construct separately typed truncation, geometry, `Err_2`, and terminal residual currents; C3 covector selection and the logarithmic tail stay separate, and no full physical continuum response estimate or hard-sphere H theorem is claimed |
| [`am-conformal-chart-normal-forms`](../sonnet/am-conformal-chart-normal-forms/00-problem-frontier.md) | Phase 1 exact Riccati lift, Möbius covariance, scalar gauge, cubic no-go, and eight-axis cost accounting | run oracle-isolated bounded discovery (1B) before the pendulum atlas search; no economy theorem yet |
| [`moving-am-observer`](../sonnet/moving-am-observer/README.md) | static-observer no-go followed by blind moving-frame recovery, held-out family selection, task-equivalence quotient, blind morphism discovery, grammar stability, and dimensionful Bellman covariance | broader non-affine/multi-family or stochastic pressure, now separated into its own Sonnet |
| [`stochastic-feedback-trap-first-passage`](../sonnet/stochastic-feedback-trap-first-passage/README.md) | bounded grammar census, exact Itô task quotient, independent BVP/Monte Carlo first-passage comparison, and reset Bellman value/policy covariance complete | calibration is closed; new discovery or API incubation requires a new contract |
| [`brownian-scale-fibre`](../sonnet/brownian-scale-fibre/README.md) | S0/S1 initialized: blind centered finite-law scale balance, typed drift refusal, exact endpoint fibres, and concatenation pushforward | separate lattice point return, continuum neighbourhood recurrence, and singleton hitting before authorizing a Brownian/heat-kernel lowering |
| [`lonely-runner`](../sonnet/lonely-runner/README.md) | exact upstream pruning transfer and bounded K4/K5 contact mechanisms; Phase 15A global audit complete | lift-aware initial search on solved cases, then frozen K13 validation; `LRC(13)` remains open |
| [`hidden-am-noether`](../sonnet/hidden-am-noether/README.md) | bounded static-observer route reached a structural no-go; the viable moving-observer continuation is tracked separately | do not reopen static conjugation without new grammar or task semantics |
| [`pcr3bp-history-cost`](../sonnet/pcr3bp-history-cost/README.md) | Phase 0/1 history, scale-jet, topology, and coding audit complete; Phase 2 contract frozen | execute converged return/absorbing ensemble and twisted partition audit; no numerical result yet |
| [`s6-complex-arithmetic-tower`](../sonnet/s6-complex-arithmetic-tower/README.md) | source and two-sided calibration contract initialized | archive/checksum the mutable manuscript and execute the first independent certificates; no theorem verification yet |

The table records research state, not a recommendation to advance all lines at
once.  A completed negative gate is a result; an initialized Sonnet is not.

---

## 6. Software value and present user stories

The public package is intentionally narrower than the research programme.  Its
current concrete user stories are:

- preserve literal process histories and caller-declared semantics;
- construct finite process families, actions, characters, and cocycles;
- express constraints, grammars, relation kernels, task evidence, morphisms,
  search budgets, and Pareto costs;
- perform bounded invariant/observer/presentation discovery;
- evaluate concrete A/M, algebraic, and Abelian analysis families;
- use explicitly unstable exact finite task minimization and local observer
  records under `process_geometry.experimental`.

These are useful components and executable references, but they do not yet
form a general user-facing problem solver.  The next software-value threshold
is not a larger root namespace.  It is either:

1. another downstream problem where a Process Geometry presentation produces
   a certified net benefit; or
2. an independently adopted narrow component with a clear task and failure
   contract.

---

## 7. Value if the strongest conjectures fail

The programme is not all-or-nothing.  If no universal arithmetic carrier,
canonical lift, or generic cross-rank calculus exists, the surviving assets
are still mathematically and computationally specific:

1. exact criteria and counterexamples for when task outputs descend through a
   quotient, chart, frame, or layer adapter;
2. a typed residual/decoder discipline for information that does not descend;
3. finite minimization, distinguishing-continuation, Pareto, Bellman, and
   presentation-search algorithms with explicit certificates;
4. concrete A/M, algebraic, Abelian, moving-frame, and stochastic calculation
   languages with stated domains and failures;
5. a growing corpus of executable classical mathematics and negative results;
6. a demonstrated method for turning future semantics into an external solver
   improvement in the Lonely Runner line.

A negative universality result would narrow the mother picture; it would not
erase these laws, algorithms, or evidence chains.  Conversely, governance and
calibration quality alone are not substitutes for further theorem and
downstream-use pressure.

---

## 8. Reading routes for agents and reviewers

### Repository orientation

1. [`MATHEMATICAL_CORE.md`](MATHEMATICAL_CORE.md) — definitions, equations,
   information loss, and boundaries;
2. [`RESEARCH_PROGRAM.md`](RESEARCH_PROGRAM.md) — the unifying conjecture,
   decomposed obligations, and kill conditions;
3. this status ledger — achieved results, evidence owners, and active gaps;
4. [`ENGINEERING_ARCHITECTURE.md`](ENGINEERING_ARCHITECTURE.md) — solver and
   certificate decisions;
5. [`THEORY_MAP.md`](THEORY_MAP.md) — dependency and maturity placement;
6. governance and the relevant detailed artifact.

### Audit one mathematical claim

```text
status-ledger row
    -> detailed theorem / phase result
    -> executable test or independent reference
    -> explicit nonclaim / red team
    -> Core and Theory Map effect
```

Do not infer maturity from a file count, commit count, phase number, imported
class name, or the presence of a test alone.

### Project-wide assessment sampling gate

A project-wide assessment must not stop at the Core, maps, indexes, directory
names, or test counts.  In this repository, substantial files under
`tests/classical/` and `tests/research/` are executable mathematical essays
and first-class research deliverables, not only software regressions.

Before rating the mathematical depth or the documentation/code balance, read at
least one complete essay from each of these four evidence modes:

1. **exact algebraic/global reconstruction:** 
   [`test_pendulum_elliptic_group_rank_lowering.py`](../tests/research/test_pendulum_elliptic_group_rank_lowering.py);
2. **units, fundamental domains, residuals, and symbolic analysis:**
   [`test_pendulum_unit_history_fundamental_domain.py`](../tests/research/test_pendulum_unit_history_fundamental_domain.py);
3. **exact finite control with failure and decoder semantics:**
   [`test_padic_selector_policy_bellman.py`](../tests/research/test_padic_selector_policy_bellman.py);
4. **abstract interface pressure and adversarial controls:**
   [`test_objectification_fibred_change_calculus.py`](../tests/research/test_objectification_fibred_change_calculus.py).

Then follow at least one result outside that sample through its phase note,
executable owner, and explicit nonclaim.  The sample is a minimum reading gate,
not a claim that these four files are the only or permanently best results.

Consequently, raw `docs/` versus `src/` line counts are not a meaningful
research-output ratio unless executable essays are classified separately.
Likewise, a large `tests/` tree is not evidence of mathematical depth until
its claims and certificates have actually been read.

### Start implementation work

After the orientation route, read [`API.md`](API.md), the code owner, the
relevant vignette or Sonnet contract, and its executable certificate.  A named
research result does not become a package abstraction unless the governance
promotion chain says so.

---

## 9. Maintenance rule

Update this ledger when a change does one of the following:

- adds or removes a theorem-level structural law or obstruction;
- completes or reopens an end-to-end calibration;
- materially changes an active Sonnet's highest responsible claim;
- produces or invalidates a downstream computational result;
- changes a theory maturity, Experimental/Public API status, or major open
  boundary.

Local parameter sweeps, phase bookkeeping, and mechanical refactors should
link from their own records without expanding this document.  Every positive
summary here must retain a nearby boundary and an evidence owner.

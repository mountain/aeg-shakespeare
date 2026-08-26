# Process Geometry — engineering architecture

**Status:** core engineering and governance document; required reading after
`MATHEMATICAL_CORE.md` and before substantial research implementation,
solver design, numerical work, or theory-bearing API work.

## 0. Purpose

The Mathematical Core asks what the objects mean and why one construction
leads to another.  Engineering architecture asks a different but inseparable
question:

> Given a concrete physical or mathematical problem, which presentation,
> algorithm, evaluator, certificate, error contract, and cost model make the
> problem feasibly computable?

The repository separates the responsibilities as follows:

```text
MATHEMATICAL_CORE.md       meaning: objects, constructions, laws, boundaries
ENGINEERING_ARCHITECTURE.md execution: representations, algorithms, evidence, cost
THEORY_MAP.md              location and maturity of mathematical claims
API.md                     currently exposed software contracts
GOVERNANCE.md              research-to-software promotion
```

This document makes technical decisions for the current repository.  It is not
a claim that one universal solver, one canonical presentation, or one backend
can cover every process.  Architecture changes are expected, but they must be
explicit and auditable rather than emerging accidentally from the latest
vignette.

---

## 1. The feasible-calculation contract

A problem is not computationally specified by an equation alone.  Before an
implementation is called a solver, record the following contract.

```text
Primitive problem
  Variables, operations, constraints, dynamics, admissible histories.

Task
  Requested observable, decision, reconstruction, trajectory, invariant,
  optimum, proof, or classification.

Regime
  Parameter domain, initial/boundary data, singular/degenerate cases, units.

Accuracy
  Exact, certified approximate, numerical tolerance, statistical confidence,
  or search-only.

Resource envelope
  Search bounds, time, memory, precision, expected workload, reuse count.

Baseline
  Conventional algorithm or independent reference against which correctness,
  stability, and cost are judged.

Deliverable
  Result, certificate, decoder/reconstruction data, provenance, cost report,
  and explicit failure status.
```

Engineering feasibility is always relative to this contract.  A method is
feasible only when it terminates or has a declared stopping rule on the stated
domain, stays inside the resource envelope, and returns either a result with
the promised evidence or an explicit failure/inconclusive status.

The words `exact`, `certified`, `stable`, `efficient`, and `solved` are therefore
controlled engineering claims.  A symbolic expression without an evaluator,
a numerical value without error semantics, or an optimized quotient without a
decoder may be useful research output, but it is not a complete solver result.

---

## 2. Required problem-to-solver pipeline

The default engineering path is:

```text
problem contract
    -> primitive process model
    -> task and continuation semantics
    -> units / nondimensionalization
    -> lift and retained residuals
    -> candidate presentations
    -> algorithm selection
    -> symbolic / numerical evaluator
    -> certificate and red team
    -> cost and scaling audit
    -> research, Experimental, or Public packaging
```

The stages are logical gates, not necessarily separate runtime components.

### 2.1 Problem intake and primitive model

Start from the physical or mathematical data before importing the state of an
existing solver.  Declare:

- primitive variables and legal operations;
- algebraic, differential, combinatorial, probabilistic, or geometric
  constraints;
- literal history or continuation interface;
- symmetries and conserved data forced before representation choice;
- the conventional formulation retained as an independent baseline.

Use `process_geometry.process` for already supported literal, finite, or local
process carriers.  A problem-local carrier belongs in a vignette or Sonnet
until independent pressure forces a reusable interface.

### 2.2 Task and adequacy

Specify what must be computed before optimizing its presentation.  Typical
tasks include:

- exact future observation;
- endpoint or event classification;
- reconstruction of full physical state;
- symbolic invariant or relation discovery;
- trajectory or return-map evaluation;
- period, action, phase, or holonomy;
- minimum expected stopping/coding cost;
- proof or counterexample search.

Adequacy must be certified relative to the task.  Algebraic elimination,
bounded continuation signatures, exact finite task quotients, and numerical
agreement provide different strengths of evidence and must not share one
unqualified “equivalent” flag.

### 2.3 Units and nondimensionalization

Normalize early enough that search, tolerance, and cost are meaningful, while
retaining the inverse physical scale map.  Record:

- base dimensions and scale frame;
- dimensionless variables and parameter groups;
- physical reconstruction map;
- how tolerances and costs transform when the frame changes;
- singular scales or regimes where the normalization fails.

A unit frame measures a presentation; it does not choose the quotient,
fundamental domain, or scalar objective.  Moving units require explicit
transport rather than comparison of raw coordinate numbers.

### 2.4 Lift first and declare residuals

Retain history information needed by future calculation before quotienting:
branch, deck sheet, phase, action, derivative/adjoint data, numerical error,
random seed/state, or decoder provenance.  Then state exactly what the task may
forget.

The computational representation should normally have the shape

```text
task presentation + retained residual + decoder
```

rather than a bare quotient.  If no decoder is needed, say why.  If global
reconstruction is impossible or only local, expose that as failure semantics.

When a problem has a composable evaluation layer, record the fuller chain:

```text
literal history
    -> composable evaluation payload
    -> observer/base-frame evaluation
    -> task quotient + retained residual
    -> decoder
```

Test adequacy at every information-losing arrow. Matrix equality, equal
geometric endpoints, equal finite contacts, and equal task futures are
different certificates unless a commuting or continuation theorem connects
them.

### 2.5 Candidate presentation generation

Candidate generation is bounded proposal search, not ontology.  Current
supported mechanisms include:

- literal histories and rewrite systems;
- bounded continuation signatures;
- finite-family characters, actions, and cocycles;
- polynomial observer grammars and invariant nullspaces;
- Gröbner elimination to observable algebraic relations;
- generated grammars and relation kernels;
- structured observer proposals;
- problem-local A/M, algebraic, and Abelian constructions.

Every search declares a finite `SearchBudget` or an equivalent problem-local
bound.  Do not run an open-ended word, relation, observer, or primitive search
inside routine CI.

### 2.6 Presentation selection

Filter for semantic adequacy before comparing economy.  The default cost is
multi-axis:

\[
C(P)=(C_{\mathrm{grammar}},C_{\mathrm{relations}},C_{\mathrm{history}},
C_{\mathrm{decoder}},C_{\mathrm{task\ error}}).
\]

Use the Pareto frontier by default.  Scalarization is permitted only when the
task supplies weights and units.  A lattice basis, expression length, runtime,
or one favored coordinate must not silently choose a universal scalar ruler.

### 2.7 Algorithm and evaluator selection

Choose the algorithm only after the task, regime, representation, and retained
residuals are fixed.  Prefer the smallest method whose guarantees match the
claim:

- exact finite algorithms before approximate simulation on genuinely finite
  tasks;
- exact algebraic residuals before floating-point equality for polynomial
  claims;
- symbolic reduction before numerical evaluation when it reduces dimension,
  exposes invariants, or isolates singularities;
- numerical continuation when global branches or periods cannot be represented
  by one local symbolic chart;
- independent conventional solvers as baselines and red teams, not ontology.

### 2.8 Certification and failure

Every claimed mode needs matching evidence:

| Claim mode | Minimum evidence |
| --- | --- |
| exact finite | exhaustive transition/observation certificate or distinguishing witnesses |
| exact symbolic | residual zero in a declared algebra/domain, relation soundness, or exact round trip |
| certified approximate | a posteriori bound, interval/enclosure, or theorem-backed estimator |
| numerical | convergence/invariant/reference checks, scale-aware tolerance, singular/failure behaviour |
| stochastic | seeds/provenance, confidence or concentration semantics, variance/error study |
| search-only | finite budget, coverage statement, returned witnesses, and explicit incompleteness |

The solver must distinguish at least:

```text
success_exact
success_certified_approximate
success_numerical_estimate
inconclusive_within_budget
outside_declared_domain
singular_or_branch_failure
invalid_problem_contract
```

These are required semantic outcomes, not yet a proposed public enum.

### 2.9 Cost and scaling audit

Report separately:

- discovery/compilation cost;
- repeated evaluation cost;
- live state and stored history;
- dictionary/new-primitive storage;
- precision growth and conditioning;
- decoder/reconstruction cost;
- residual/branch/holonomy memory;
- parallelism and cacheability where measured.

An abbreviated primitive is not free, and one successful small instance is not
an asymptotic result.

---

## 3. Current software architecture

The public namespace pipeline is an engineering decomposition:

```text
Process -> Presentation -> Discovery -> Analysis
```

It serves, but does not define, the Mathematical Core.

| Layer | Current responsibility | Current concrete support | Explicit boundary |
| --- | --- | --- | --- |
| Process | literal or local dynamics before representation choice | `ProcessWord`, finite families/actions/cocycles, `ProcessSystem`, `ProcessFrame` | no universal process protocol |
| Presentation | auditable realization, constraints, relations, task evidence, decoder and cost | histories/rewrites, constraints, grammars, `PresentationMorphism`, `PresentationCost`, `SearchBudget` | presentation is not automatically a task quotient or objectification |
| Discovery | bounded proposal and selection algorithms | polynomial invariants, Gröbner elimination, structured observers, first-order Pareto search | no unbounded or universal representation search |
| Analysis | function and variation languages supported by a presentation | A/M, algebraic profiles, Abelian differentials/periods/cycles | no generic calculus or canonical solver |
| Experimental | exact or unstable theory-to-code probes | finite deterministic task quotient; local canonical-observer records | no compatibility or generality promise |
| Vignettes/Sonnets | full problem-specific solver assembly and red teams | pendulum, KdV, resistor, braid, PCR3BP, stochastic and other calibrations | not Public API merely because executable |

There is intentionally no public `Problem`, `Solver`, `Solution`, or generic
`solve()` façade.  The current evidence has not selected stable semantics for
their carriers, failure modes, numerical backends, or certificates.

### 3.1 Dependency direction

The desired source dependency remains:

```text
process <- presentation <- discovery
    ^           ^
    |           |
    +-------- analysis
```

Problem-specific orchestration may depend on every layer, but lower ontology
must not depend on downstream special functions, search policies, or numerical
backends.

### 3.2 Backend policy

SymPy is the current required exact symbolic backend.  It supplies polynomial
algebra, differentiation, exact linear algebra, factorization, and Gröbner
elimination.  SymPy output is not the definition of process semantics:
certificates must be expressed as residuals, pullbacks, relation preservation,
or round trips that another backend could in principle verify.

The package currently has no required general numerical ODE, optimization,
interval-arithmetic, or probabilistic backend.  Such solvers may be used through
research-local adapters with pinned parameters and independent checks.  A new
required dependency or public adapter needs a separate architecture decision,
benchmark, failure contract, and API review.

---

## 4. Algorithm selection matrix

### 4.1 Exact finite deterministic processes

Use stable partition refinement for exact task minimization when the state
carrier and step alphabet are finite, transitions are total and deterministic,
and task observations are hashable.  The current Experimental
`minimize_finite_task_process` returns the coarsest stable quotient and uses
breadth-first search on the minimized machine to produce pairwise
distinguishing continuations.

Do not extend this conclusion to infinite, nondeterministic, probabilistic,
approximate, or resource-bounded processes without a new algorithm and proof
contract.

### 4.2 Finite history, stopping, and coding problems

Use bounded continuation enumeration, dynamic programming/Bellman recursion,
frontier accounting, and Huffman coding only after the task state, stopping
frontier, probability mass, prefix primitives, and cost unit are fixed.

`TaskContinuationSignature` is a bounded witness, not an exact infinite-future
quotient.  `BoundaryProfile` and Huffman machinery are exact for their declared
finite inputs, not a generic entropy or continuous-complexity engine.

Keep at least these trees separate in a solver record:

```text
literal history tree       admissible operation prefixes
topological cover tree     reduced path classes, when a topology supplies it
observer/evaluation tree   geometric states reached after evaluation
coding tree                prefix decisions for a declared source and decoder
```

A map between two such trees is a construction requiring its own adequacy and
cost certificate. Shared branching terminology or geodesicity is not that map.

The finite local-field Phase 6 calibration now supplies one complete Bellman
instance of this rule.  It freezes a one/two-action contact-lift grammar,
depth-four success section, exact residual-bearing state, shared decoders, and
four Pareto cost axes before exhausting the graph.  Source and scalar changes
select different economies, while matrix and visited-state red teams protect
decoder cost and cycle semantics.  This is problem-local evidence for the
architecture, not a generic control API.

Phase 7 refines the evaluator choice for that grammar.  Exhaustive coefficient
tuples may be replaced exactly by a Ruban-reference normal form with one
optional lift bit; the complete Phase 6 graph and value records are unchanged,
and deeper/new-prime/held-out workloads remain exhaustible.  The bit codec
reduces action payload and compilation search, but exact collisions show that
contact, evaluated next geometry, and local costs do not suffice to compile a
controller.  Keep the residual-bearing Bellman state: a small action alphabet
is not a state-minimization certificate.

Phase 8 supplies the corresponding finite state-minimization audit.  Starting
from contact signatures S0--S2, synchronous exact partition refinement computes
the coarsest extension that preserves a declared policy, scalar value, or full
continuation response and is stable under both lift bits.  A separate bottom-up
response-tree hash and distinguishing suffixes certify the result.  On the
frozen joint workload, the S2-preserving scalar quotient has 8,126 classes for
8,336 tagged states; full decoder semantics has 8,128.  The largest conditional
fibre needs seven bits and the descended transition is partial and many-to-one.
Therefore keep policy-only minimization, base-preserving state extension, and
full reconstruction minimization as separate solver products.  A stable finite
transition quotient is not an objectification or reusable control API.

### 4.3 Constrained polynomial and local differential systems

For polynomial/rational local models:

1. encode the derivation with `ProcessSystem`;
2. encode exact constraints with `AlgebraicConstraintSet`;
3. search a bounded polynomial observer grammar;
4. find invariant directions by exact coefficient linear algebra/nullspaces;
5. eliminate hidden variables with Gröbner methods;
6. certify every relation by pullback/reduction residual;
7. compare adequate first-order presentations on a Pareto frontier.

This path is preferred when it exposes an invariant, reduces dimension, or
produces a closed observable carrier.  Gröbner and grammar growth can be
exponential; degree, variables, ordering, and budget must be reported.  Failure
within a budget is not a proof that no useful non-polynomial observer exists.

### 4.4 Rewriting and relation discovery

Use explicit rewrite traces, generated grammars, relation kernels, and
critical-pair or semantic confluence checks where appropriate.  A normal form
is valid only under the declared rule orientation and termination/confluence
evidence.  Preserve construction provenance when a new primitive is proposed.

### 4.5 A/M-native processes

When the primitive problem is genuinely generated by Addition,
Multiplication, or their actions, test the A/M language before importing a
linear or spectral presentation.  Use exact finite relations, process
operators, commutator/residual checks, function modules, and path flows.

This is a selection rule for A/M-native problems, not a requirement that every
elliptic, Abelian, physical, or combinatorial problem be expressed in A/M
coordinates.  Arithmetic Geometric Universality remains open.

### 4.6 Algebraic and Abelian global analysis

When an exact observable relation defines a nondegenerate algebraic carrier:

1. classify its algebraic profile and degenerations;
2. construct the required differentials symbolically;
3. retain branch/sheet history on lifted paths;
4. integrate supplied cycles numerically or symbolically where possible;
5. construct period and intersection data with orientation checks;
6. quotient by the certified period kernel only after the task is declared;
7. retain decoder data required for physical reconstruction.

Current period/intersection engines contain exact local algebra and sampled
numerical global certificates.  They are not a rigorous interval-certified
general homology or period engine.

### 4.7 General smooth, nonintegrable, and singular dynamics

The repository currently has no generic production ODE/PDE solver.  For
PCR3BP-like, stiff, event-driven, nonintegrable, or singular systems, use a
problem-local adapter to a conventional solver and preserve:

- nondimensionalization and physical reconstruction;
- event and stopping semantics;
- invariant drift and convergence studies;
- branch/return-map provenance;
- comparison under at least two resolutions or an independent method;
- explicit singular, escape, and nonconvergence outcomes.

Process Geometry should contribute task-relative presentations, sections,
partitions, holonomy, residuals, and certificates around the solver.  It should
not relabel an external integrator as a new calculus without demonstrating a
new effective analytic language.

### 4.8 Stochastic processes

Prefer exact enumeration, finite dynamic programming, or symbolic probability
when the declared carrier permits it.  Otherwise use reproducible Monte Carlo
or stochastic numerics with explicit seeds, sample counts, variance/error
estimates, stopping rules, and independent limiting or conservation checks.

A visible transition graph does not make a process Markovian.  Retain enough
history or a certified sufficient statistic before applying Markov algorithms.

### 4.9 Preferred hybrid pattern for physical problems

For many realistic physical problems the preferred architecture is hybrid:

```text
exact primitive/constraint audit
    -> symbolic invariants and reduction
    -> task-relative quotient plus residual
    -> numerical evaluation on the reduced carrier
    -> decoder to physical variables
    -> invariant, convergence, and baseline certificates
```

This retains classical symbolic and numerical calculability while allowing
Process Geometry to change the representation in which the calculation is
performed.

---

## 5. Current technical decisions

The following decisions govern new work until an explicit architecture change
replaces them.

### D1 — No universal solver façade yet

Keep complete solver assemblies problem-local.  Promote shared components only
after independent problems force the same input, output, failure, and
certificate semantics.

### D2 — Task adequacy precedes optimization

Reject or mark inadequate any candidate that loses declared future semantics.
Only adequate candidates enter cost comparison.

### D3 — Lift and residual are explicit

Do not quotient away branch, phase, deck, derivative, error, or decoder data
required by later computation.

### D4 — Exact claims use exact domains

Use Python integers/Fractions or SymPy exact numbers and symbolic residuals for
exact claims.  Floating-point near-zero is not exact evidence.

### D5 — Symbolic backend is replaceable

SymPy may compute certificates, but semantic claims are stated by backend-
independent equations, pullbacks, witnesses, and round trips.

### D6 — Search is bounded and returns provenance

All grammar, observer, relation, primitive, or history searches expose finite
budgets and retain witnesses.  Budget exhaustion returns inconclusive, not
false.

### D7 — Cost stays multi-axis by default

Use Pareto comparison.  A caller may scalarize only with declared task weights,
units, and workload.

### D8 — Units and tolerances are first-class

Every physical numerical solver records normalization, physical restoration,
scale-aware tolerances, and frame transport when units vary.

### D9 — Decoder cost and failure are part of the result

A reduced solution is incomplete for a reconstruction task until branch or
residual data are decoded, or a precise reconstruction boundary is returned.

### D10 — Transformations carry evidence

Cross-presentation transformations use an evidence-bearing record such as
`PresentationMorphism`; type similarity, coordinate invertibility at one point,
or numerical agreement alone is insufficient.

### D11 — Numerical dependencies remain research-local by default

Do not add a mandatory solver backend merely for one vignette.  Promotion
requires independent need, adapter semantics, reproducible benchmarks,
failure/error contracts, and maintenance justification.

### D12 — CI is tiered

Routine CI contains fast semantic regressions, exact certificates, small
deterministic numerical checks, and documentation governance.  Long-running
parameter sweeps, stochastic studies, large symbolic searches, and open-problem
probes remain manually dispatched or explicitly isolated workflows.

### D13 — Reproducibility and provenance are deliverables

Record parameters, seeds, backend/version assumptions, search budgets,
precision, branch choices, and certificate construction.  Generated artifacts
must be regenerable or independently checkable.

### D14 — Architecture, theory, and API promotions are separate

A good algorithm can remain problem-local; a mature mathematical law does not
automatically define a software interface; a reusable component does not prove
the general theory suggested by its name.

### D15 — Geometric and coding trees require an explicit bridge

Do not reuse a history, cover, or observer-geometry tree as a coding or control
tree by name alone. Declare the source/state map, admissible decisions, cost
unit, terminal semantics, and decoder. Changing probabilities while holding
geometry fixed is a required red team for any allegedly geometry-selected
code.

---

## 6. Reference implementation paths

### 6.1 Pendulum

The simple pendulum is the first end-to-end reference for this architecture.

| Stage | Decision | Algorithm/evidence |
| --- | --- | --- |
| Primitive model | Cartesian constrained process, no supplied angle | exact rod, tangency, dynamics, energy |
| Units | \(t_0=\sqrt{\ell/g}\), \(E_0=mg\ell\), \(A_0=E_0t_0\) | dimensionless normalization plus inverse physical map |
| Observer candidates | bounded scalar/structured grammar | exact polynomial/structured proposal search |
| Selected presentation | \(U=q_y,\;Y=DU\) under declared task/cost | first-order closure and Pareto evidence |
| Reduction | \(Y^2=2(E-U)(1-U^2)\) | Gröbner elimination and pullback residuals |
| Local solver | \(DU=Y,\;DY=3U^2-2EU-1\) | exact differentiation modulo the carrier |
| Lift | \(z=\int dU/Y\) with branch history | lifted square-root continuation |
| Global analysis | periods, cycles, intersections, elliptic decoder | exact local algebra plus sampled numerical global checks |
| Task residual | Cartesian sheet mark | exact \(1/0\)-bit continuation census |
| Continuous volume | \(d\Omega=T\,dH\) | exact elliptic-integral identity and unit transport |
| Reconstruction | local Cartesian decoder plus sheet bit | exact away from the vertical branch boundary |
| Red teams | nonlinear observer, lattice shear, metric sheet/Bolza | second-jet, noncanonical-cost, and product-quotient failures |

This path is computationally useful because symbolic reduction lowers the
dimension and exposes exact structure before global numerical integration.  It
is not yet a complete production solver: generic-energy rigorous cycles,
interval-certified periods, global branch-aware reconstruction, and intrinsic
discovery of the lift/ruler remain open.

### 6.2 Finite local-field projective cylinders

The local-field Sonnet is the first independent discrete reference for the
history--evaluation--task--decoder path.

| Stage | Decision | Algorithm/evidence |
| --- | --- | --- |
| Primitive model | rational A/M/inversion prefixes and projective residue refinement | exact `Fraction` histories and two-chart normal forms |
| Units/frame | standard lattice \(\mathbb Z_p^2\), normalized \(v_p(p)=1\) | base vertex plus one-edge refinement ruler |
| Evaluation payload | \(G_n=M(a_0)\cdots M(a_n)\) | exact chronological matrix product |
| Observer geometry | \([G_n\mathbb Z_p^2]\) | normalized lattice class, parent, LCA, and distance certificates |
| Task quotient | fixed-depth projective cylinder | exact parent reduction in \(\mathbb P^1(\mathbb Z/p^d\mathbb Z)\) |
| Continuation residual | next complete quotient for selector reconstruction | exact Möbius round trip; omitted only from the separate cylinder-code task |
| Discrete shell | \(|B_d|-|B_{d-1}|=|S_d|\) | exact finite enumeration and closed count |
| Source/coding | declared root-symmetric or adversarial finite law | exact mass pushforward, Huffman lengths, canonical prefix decoder |
| Selector control | finite contact-lift grammar with complete quotient, matrix/lattice payload, and visited witness | exact Ruban-reference binary normal form, closed evaluation, and state validation |
| Policy-state extension | S0--S2 base plus declared policy/value/full-response semantics | exact stable partition refinement, independent bottom-up hashing, fibre bounds, and distinguishing suffixes |
| Stopping/decoder | exact termination or depth-four cylinder under one precedence | first-column or matrix/residual round trips; cycle and horizon remain distinct |
| Optimization | four-axis Pareto value, no default scalarization | complete reachable-graph census, backward set-valued Bellman recursion, replayable witnesses |
| Baselines/storage | Ruban and Browkin rules plus corpus controller tables | shared evaluator; source/scalar and local-signature red teams; rational-action versus lift-bit tables with state cost retained |
| Cost | digit, tree edge, frontier memory, binary bit, serialization kept separate | exact multi-axis ledgers |
| Red teams | same contact/different continuation; same geometry/different source, scalar, future value, stopping surface, or decoder; dropped payload/residual | Ruban/Browkin outcome split, changed Huffman/controller choice, S0--S2 policy collisions, nonuniform fibres, many-to-one bit transport, decoder-cost and cycle failures |

This path is exact and seconds-scale. It now provides one finite task-local
selector-policy Bellman solver and a closed action evaluator with finite
transfer evidence.  It also provides a coarsest stable finite extension for the
declared policy/value/decoder tasks, while showing that this extension is
nonuniform and nearly as fine as the full tagged carrier.  It supplies no
infinite boundary measure, general selector-control framework, preferred
\(p\)-adic continued fraction, task-independent minimal policy state,
objectification API, or reusable projective/coding API.

---

## 7. Solver-plan record for substantial problems

Before writing substantial solver code, an agent or contributor should record
the following compact plan in the vignette, Sonnet, issue, or PR:

```text
Problem and task:
Primitive process / constraints:
Parameter regime and units:
Mathematical Core relation:

Required lift and residuals:
Candidate presentations:
Adequacy certificates:
Selection cost / Pareto axes:

Chosen algorithm(s):
Symbolic evaluator:
Numerical evaluator:
Decoder / reconstruction:

Error and failure semantics:
Independent baseline:
Red team / degeneration:
Search and runtime budgets:
Reproducibility data:

Current software layer:
Engineering Architecture effect:
Theory Map effect:
API pressure / explicit non-pressure:
```

The plan may be short for an exact finite example.  A realistic continuous or
stochastic claim must fill the numerical, unit, error, and baseline fields.

---

## 8. Architecture governance

### 8.1 Required reading order for agents

For substantial research or implementation, read in order:

1. `MATHEMATICAL_CORE.md`;
2. this document;
3. `THEORY_MAP.md` and the relevant governance file;
4. the problem's vignette, research notes, tests, and current code owner.

The first document prevents computational convenience from redefining the
mathematics.  The second prevents mathematical abstraction from ignoring
feasible evaluation, certification, errors, and cost.

### 8.2 Architecture change operations

A material change should be described as one or more of:

- **support** — another problem uses an existing decision successfully;
- **refine** — narrow a regime, backend, cost, or failure contract;
- **split** — one solver path was hiding distinct algorithmic regimes;
- **connect** — add a certified bridge between layers or backends;
- **replace** — supersede a technical decision with migration evidence;
- **contradict** — demonstrate that a decision fails its declared workload;
- **deprecate** — retain history but stop recommending a component or path;
- **unchanged** — local work requires no architecture revision.

### 8.3 PR requirement

A substantial research, solver, numerical, dependency, performance, or
theory-bearing API PR must include an **Engineering Architecture Change**
section stating:

1. which problem-to-solver stage changes;
2. the mathematical object and task it serves;
3. algorithm and backend choice;
4. exact/numerical/stochastic claim mode;
5. certificate, error, and failure semantics;
6. units, decoder, and residual handling;
7. workload, baseline, budget, and measured cost;
8. dependency and API effects;
9. architecture operation and migration risk.

Mechanical changes may mark this not applicable.  Local research may state
`unchanged` while still reporting its solver plan.

### 8.4 Promotion rule

An architecture pattern may become reusable software only when independent
problems force the same interfaces and stress them differently.  Public
promotion additionally requires stable failure, certificate, unit, decoder,
dependency, and migration semantics.  Repeated use of one helper or one backend
does not satisfy this gate.

---

## 9. Open architecture gaps

The following needs are real but do not yet justify generic APIs:

1. a typed problem/task/result contract spanning exact, numerical, stochastic,
   and search-only modes;
2. a task-sufficient history-lift and residual interface that survives
   non-Markovian, continuous, and holonomy examples;
3. backend-neutral exact certificate protocols;
4. rigorous interval-certified cycle, period, and branch-continuation engines;
5. a reusable event/return-map adapter with invariant and failure semantics;
6. probabilistic task quotients and statistically certified presentation
   comparisons;
7. a benchmark corpus measuring full discovery, compilation, evaluation,
   storage, residual, and decoder costs;
8. certified effective analytic closure across rank lowering;
9. a principled bridge between continuous process volume and finite task
   memory, if one exists.

The correct next step for each gap is a problem-local solver plan and red team,
not an empty framework class.

## References and current contracts

- `docs/MATHEMATICAL_CORE.md`
- `docs/API.md`
- `docs/GOVERNANCE.md`
- `docs/THEORY_GOVERNANCE.md`
- `docs/65-effective-analysis-principle.md`
- `docs/VIGNETTE_CONTRACT.md`
- `docs/vignettes/simple-pendulum.md`
- `sonnet/local-field-projective-process-geometry/README.md`
- `sonnet/local-field-projective-process-geometry/06-phase5-projective-cylinders-discrete-coarea-coding.md`
- `sonnet/local-field-projective-process-geometry/08-phase6-executable-selector-policy-bellman.md`
- `sonnet/local-field-projective-process-geometry/10-phase7-binary-action-normal-form-transfer-results.md`
- `sonnet/local-field-projective-process-geometry/12-phase8-continuation-value-fiber-objectification-results.md`
- `tests/research/test_pendulum_unit_history_fundamental_domain.py`
- `tests/research/test_local_field_projective_lattice_ball.py`
- `tests/research/test_padic_continued_fraction_selector_comparison.py`
- `tests/research/test_padic_selector_policy_bellman.py`
- `tests/research/test_padic_selector_structural_law.py`
- `tests/research/test_padic_continuation_value_fiber.py`
- `tests/experimental/test_finite_task_quotient.py`

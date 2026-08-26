# Process Geometry — arithmetic generativity and universality research programme

**Status:** conjectural research synthesis and experiment-routing document;
not a theorem, not a theory-promotion record, and not a Public API contract.

**Required prior reading:** [`MATHEMATICAL_CORE.md`](MATHEMATICAL_CORE.md),
which records the present objects, constructions, laws, and boundaries.  Read
[`RESEARCH_STATUS.md`](RESEARCH_STATUS.md) next for dated evidence and explicit
nonclaims.  This document answers a different question: **what unifying
possibility is the project deliberately testing, and why do its apparently
distant research lines belong to one programme?**

When this programme, the Mathematical Core, and a detailed proof artifact use
different strengths of language, the proof artifact and Core determine what
has been earned.  This document determines neither maturity nor API status.

---

## 1. Central research wager

Process Geometry is guided by a conjectural synthesis stronger than the claim
that many processes admit geometric representations.

> **Arithmetic generativity.**  Arithmetic primitives, their free process
> compositions, and their objectified higher-rank operations may generate not
> only presentation geometries, but also effective calculi, task-relative
> information structures, complexity measures, statistical constructions,
> and new compositional ranks.

Addition and Multiplication provide the first substantial and computable model
of this mechanism.  They are not assumed to be the final generic ontology.
The broader question is whether arithmetic-generated presentations can serve,
for a sufficiently wide class of declared process--task systems, as
task-sufficient, effectively calculable, and economically responsible process
languages.

This is the project's **Arithmetic Universality** programme.  It is an active
research direction, not an assumption made by the package.

The programme is intentionally more than a proposal for a common geometric
skeleton.  Its target is a compatible executable system:

```text
arithmetic primitives
    -> free compositions and literal histories
    -> presentation freedom, charts, and transported scale
    -> geometry and effective change calculus
    -> task-relative forgetting, fibres, residuals, and decoders
    -> cost, measure, probability, and optimization
    -> objectification and higher-rank free composition.
```

Geometry is one generated layer of this system.  A successful theory must also
say how quantities are evaluated, how changes propagate, how information is
forgotten or retained, how costs are charged, and how a stable process schema
becomes a new primitive without losing effective lowering semantics.

---

## 2. Terminology and scope

The programme keeps four terms separate.

1. **Arithmetic generativity** names the proposed mechanism by which process
   composition and objectification generate geometry, analysis, information,
   complexity, and higher rank.
2. **A/M geometry and calculus** name the present Addition/Multiplication base
   case: the first concrete continuous process geometry and effective function
   language developed by the repository.
3. **The arithmetic tower** names the candidate vertical pattern in which a
   stable lower-rank process or action is objectified into a new primitive with
   free higher-rank composition and compositional lowering.
4. **Arithmetic Universality** names the scope question: how broadly
   arithmetic-generated presentations satisfy the semantic, analytic,
   statistical, and economic obligations below.

The phrase *arithmetic-generated process geometry* is deliberate.  The project
is not renaming the established number-theoretic field of arithmetic geometry.
Nor does *arithmetic* mean an unrestricted permission to encode a target
solver inside a sufficiently large expression.  The primitive grammar,
admissible charts, adapters, residuals, and costs must be frozen for each
claim.

AM is therefore neither demoted to an incidental example nor promoted to an
unproved foundation.  It is the first hard model organism, the current
effective continuous analysis family, and the principal candidate base layer
of a broader arithmetic-generative mechanism.

---

## 3. Universality obligations

The programme decomposes its strongest conjecture into five obligations and
one cross-cutting admissibility condition.  These identifiers route evidence;
they are not maturity levels, and satisfying one does not imply the others.

| ID | Obligation | What would count as real evidence | Typical trivialization to reject |
| --- | --- | --- | --- |
| **U1** | generative presentation | an arithmetic process grammar produces a task-sufficient presentation while preserving declared composition and continuation semantics | an arbitrary redundant encoding whose decoder contains the original solver |
| **U2** | effective analysis | the presentation supports symbolic and/or numerical evaluation, a native change calculus, closure or controlled extension, certificates, and failure semantics | importing ordinary additive tangent or jet machinery without deriving its transport at the relevant arithmetic rank |
| **U3** | information--complexity compatibility | task quotients, residuals, stopping sections, cost cocycles, coding, and optimization coexist on one auditable history presentation | calling distinguishability bits, runtime, entropy, and phase volume the same quantity |
| **U4** | statistical--macroscopic compatibility | conditional fibre laws, transverse ensemble weights, correlations, coarse-graining, and macroscopic response are connected by declared adapters and limits | attaching an arbitrary probability law or closure and crediting it to arithmetic structure |
| **U5** | objectification and rank closure | a stable process schema becomes a reusable primitive with genuinely new free composition and effective all-composite lowering | treating abbreviation, a quotient point, or a stable fibre as a new rank by name alone |
| **E** | covariance and economy | the preceding constructions commute under admissible chart or presentation changes up to declared residual/error, with bounded representation, compilation, decoder, and evaluation costs | rescuing every failure by unbounded fibres, residuals, chart data, or hidden oracle work |

The strongest programme would satisfy all six obligations on a broad and
independently characterized class of processes.  Useful partial theorems may
instead establish one obligation locally, prove an obstruction, or identify a
maximal domain on which a weaker universality statement survives.

---

## 4. Complexity, entropy, and statistical mechanics are one stress programme

The repository studies complexity, entropy, and statistical mechanics not
because all three use logarithms, volumes, or optimization, and not because
they have already been identified.  They test whether one arithmetic-generated
process language can carry increasingly demanding kinds of structure.

```text
arithmetic-generated process history
    -> task evaluation and forgetting
    -> measured/costed fibres and stopping sections
         |-> optimal history and coding laws          complexity
         |-> counting or measuring forgotten fibres  entropy
         `-> conditional laws and transverse tilts   statistical mechanics
                 -> coarse-graining and macroscopic response.
```

- **Complexity pressure** asks whether process composition supplies a
  transportable ruler, whether cost is accumulated before or after quotient,
  whether stopping sections are task-sufficient, and whether Bellman/Huffman
  optimization remains presentation-covariant after compilation and decoding
  costs are charged.
- **Entropy pressure** asks when task-relative multiplicity becomes a counted
  or measured fibre, which reference measure and units make logarithms legal,
  and which information remains as a continuation-visible residual.
- **Statistical-mechanics pressure** asks whether microscopic composition,
  correlation fibres, conditional laws, ensemble mixing, coarse-graining,
  irreversibility, and macroscopic closure can remain inside one effective
  change-and-adaptation language.

The disciplinary nonidentifications in the Mathematical Core are therefore
not a retreat from synthesis.  They make the endpoints of future bridge
theorems well typed.  The programme conjectures a common generative origin; it
does not infer

```text
complexity = entropy = action volume = thermodynamic state count
```

from analogy.  A bridge must declare its task, measure, units, limiting
operation, covariance law, residual, and cost.

The Boltzmann--BBGKY line is especially important in this role.  It is not
merely an application of a finished geometry to a physics problem.  It tests
whether exact equivalence can give way to typed semantic adaptation, whether
forgotten correlations can be located in measured or filtered fibres, and
whether a process-native response calculus survives noninvertible and
probabilistic reduction.

---

## 5. Current evidence routes

This table records why major research lines belong to the programme.  It does
not replace the dated achievements and boundaries in
[`RESEARCH_STATUS.md`](RESEARCH_STATUS.md).

| Pressure route | Primary obligations | Current evidence owners | Programme-level question |
| --- | --- | --- | --- |
| AEG translation, multiplication, and mixed lowering | U1, U5 | [`50-aeg-translation-objectification-rank-lowering.md`](50-aeg-translation-objectification-rank-lowering.md), [`51-aeg-addition-multiplication-rank-transition.md`](51-aeg-addition-multiplication-rank-transition.md) | does arithmetic process composition generate a genuine next-rank language rather than an abbreviation? |
| pendulum, moving observers, and AM chart search | U1, U2, E | [`vignettes/simple-pendulum.md`](vignettes/simple-pendulum.md), [`moving-am-observer`](../sonnet/moving-am-observer/README.md), [`am-conformal-chart-normal-forms`](../sonnet/am-conformal-chart-normal-forms/00-problem-frontier.md) | can a nontrivial physical process acquire a discovered, covariant, and computationally economical arithmetic atlas and calculus? |
| canonical histories, Bellman/Huffman, and downstream pruning | U3, E | [`56-am-universal-history-recalibration.md`](56-am-universal-history-recalibration.md), [`lonely-runner`](../sonnet/lonely-runner/README.md) | can task semantics and arithmetic rulers change a real computation without hiding quotient, decoder, or implementation cost? |
| local-field/projective fibres, partitions, and change actions | U1, U3, U5 | [`local-field-projective-process-geometry`](../sonnet/local-field-projective-process-geometry/README.md) | which presentation data descend, which remain fibred, and when does an objectified action support a higher calculus? |
| stochastic first passage and chart transport | U2, U3, E | [`stochastic-feedback-trap-first-passage`](../sonnet/stochastic-feedback-trap-first-passage/README.md) | which change law is forced when nonlinear charts meet stochastic variation? |
| thermodynamic objectification and partition towers | U3, U4, U5 | [`63-thermodynamic-objectification-and-partition-towers.md`](63-thermodynamic-objectification-and-partition-towers.md) | do measure, ensembles, partition structure, and objectification share an arithmetic-generative interface? |
| Boltzmann--BBGKY and the H-theorem frontier | U2, U4, E | [`boltzmann-bbgky-h-theorem`](../sonnet/boltzmann-bbgky-h-theorem/README.md) | can correlations, semantic adaptation, response, and macroscopic closure be handled without importing the answer as an oracle? |

The same result may support generic Process Geometry while leaving Arithmetic
Universality untouched.  Every evidence report must therefore separate:

```text
generic process-geometry result
arithmetic-specific mechanism
universality obligation pressured
claim not earned.
```

---

## 6. What a defensible universality theorem would require

Mere encodability is too weak.  For a declared class of process--task pairs
\((P,Q)\), a substantive theorem would need an arithmetic-generated
presentation \(A_{P,Q}\) and comparison data satisfying, in an appropriately
typed form:

1. **task adequacy:** every declared observation and continuation is preserved
   exactly or within a declared topology, horizon, and error budget;
2. **compositionality:** legal source composition transports coherently to the
   arithmetic presentation and, across ranks, lowers again;
3. **native variation:** the necessary change law is derived or transported at
   the relevant arithmetic rank rather than assumed from additive calculus;
4. **information accounting:** forgotten data, non-descent, branch choices,
   correlations, and reconstruction obligations remain explicit;
5. **effective evaluation:** symbolic or numerical evaluation terminates or
   fails under a declared certificate and resource contract;
6. **covariance and economy:** competing admissible charts give compatible
   task values, and total lift/search/decoder/evaluation overhead is bounded.

Global presentation by one AM chart is not the only possible successful form.
A more plausible theorem may provide a task-relative arithmetic atlas whose
local AM charts are glued by admissible transition data, with global
obstructions carried by explicit cocycles, fibres, or residuals.  Such a
theorem would still have to bound those additions; otherwise the atlas claim
would collapse into unrestricted encoding.

No present result proves this package for a generic class of processes.

---

## 7. Falsification and anti-immunization rules

The programme loses mathematical content if every counterexample can be
absorbed by adding a larger fibre, a stronger decoder, another chart, or a new
rank.  A universality experiment must freeze in advance:

- the process and task class;
- the arithmetic primitive grammar and allowed objectification steps;
- admissible chart and adapter families;
- residual and decoder budgets;
- symbolic and numerical evaluator contracts;
- baseline representations and total cost axes;
- the failure that would reject or narrow the tested claim.

The following outcomes count against a strong universality claim:

1. the target dynamics or solution is smuggled into a connection, decoder,
   closure, measure, or oracle;
2. task adequacy requires residual growth comparable to retaining the full
   source history without compensating structure or economy;
3. chart transition or change calculus leaves the declared arithmetic language
   in an uncontrolled way;
4. an allegedly intrinsic ruler, entropy, or ensemble depends on an arbitrary
   undeclared frame, measure, scalarization, or limiting path;
5. higher-rank notation supplies no new free composition or no effective
   all-composite lowering;
6. the arithmetic presentation gives no structural theorem, obstruction,
   discovery advantage, or net computational economy over honest baselines.

A negative result may reject only one obligation or process class.  The
surviving exact laws, algorithms, and obstructions remain assets, as recorded
in `RESEARCH_STATUS.md`; but they must not be used rhetorically to preserve a
stronger failed conjecture.

---

## 8. Research and documentation protocol

Every substantial Sonnet or extraction candidate that bears on this programme
should record:

```text
Universality pressure: U1 / U2 / U3 / U4 / U5 / E
Arithmetic-specific mechanism:
Generic Process Geometry result:
Evidence gained:
Universality claim not earned:
Kill condition:
```

Not every Sonnet must pressure Arithmetic Universality.  A problem-local
result may be valuable without doing so, and a generic Process Geometry
obstruction may show that the arithmetic conjecture was posed at the wrong
level.  The field must never be chosen merely because arithmetic terminology
can be overlaid on it.

The repository keeps three registers distinct:

```text
RESEARCH_PROGRAM.md     what unifying possibility is being tested
MATHEMATICAL_CORE.md    what mathematical synthesis is currently responsible
RESEARCH_STATUS.md      what the dated evidence has actually earned
```

`THEORY_MAP.md` locates dependencies and maturity;
`ENGINEERING_ARCHITECTURE.md` makes the effective-calculation obligations
operational; governance controls promotion.  None substitutes for the others.

---

## 9. Current responsible statement

The repository has earned concrete A/M analysis, exact arithmetic
objectification and lowering calibrations, task-relative quotient and fibre
laws, several covariance and non-descent obstructions, and one downstream
computational transfer.  These results justify sustained pressure on the
Arithmetic Generativity programme.

They do not yet establish one universal arithmetic carrier, one universal
calculus, a canonical complexity ruler, a derivation of entropy from process
geometry, a generic statistical closure, or a complete arithmetic rank tower.

The intended stance is therefore:

> propose a common arithmetic-generative origin boldly; keep complexity,
> entropy, action volume, probability, and thermodynamic structure distinct
> until typed bridge laws connect them; and make every universality claim pay
> for its semantics, residuals, decoders, and computation.

# Research and API governance

**Status:** repository policy for future research extraction and API promotion.

Process Geometry is simultaneously an evolving mathematical research program and a software system. **Shakespeare** is the problem-driven research program that supplies Sonnets, pressure tests, and candidate structures; the `process_geometry` package is the software framework that may absorb only the structures that survive governance.

Those roles need different stability rules. Open-ended research should be allowed to invent, discard, and contradict provisional structures; the public API should make only narrow, evidence-backed semantic commitments.

The governing principle is:

> **Sonnets discover problems and structures. Experimental incubates candidate abstractions. The public API makes commitments.**

The default lifecycle is therefore

```text
Sonnet
  -> extraction candidate
  -> Experimental
  -> maturing
  -> Public API
```

This is a one-way promotion path by default. A Sonnet must not promote a new generic abstraction directly into the public API.

## 0.1 The living Theory Map

Engineering governance must be interpreted against the larger and still-evolving theoretical picture in [`THEORY_MAP.md`](THEORY_MAP.md).

The Theory Map currently synthesizes the foundation developed in `docs/42–45` and later alignment notes. It records, among other things:

- the horizontal distinguishability axis: process/history -> task distinguishability -> exact quotient or locality/topology -> entropy/complexity -> analysis where justified;
- the vertical ontology-growth axis: free process -> semantic compression -> objectification -> higher-rank free composition -> compositional rank lowering;
- the proposed semantic/topological/analytic closure questions across ranks;
- the Effective Analysis Principle: an analysis-bearing presentation must
  expose a symbolic and/or numerical calculation path, certificates,
  error/failure semantics, and task-relative cost accounting;
- the distinction between AEG as a model organism and Arithmetic Geometric Universality as a stronger open conjecture.

**The Theory Map is not a frozen standard.** It is expected to change as experiments and mathematics improve. Its role in engineering is to make API choices legible inside the larger research program and to prevent accidental implementation vocabulary from silently becoming ontology.

The required asymmetry is:

```text
API semantic commitment <= evidence-backed portion of the evolving theory
```

A public API must never be used as evidence that an unsettled theoretical claim has become true merely because code now has a class or function with that name.

## 1. Sonnet: the problem space

`sonnet/` is the most permissive research layer. A Sonnet may contain:

- problem-specific mathematical definitions;
- provisional observers, presentations, quotients, morphisms, and cost models;
- competing or mutually incompatible designs;
- one-off scripts and deliberately ugly prototypes;
- failed approaches and negative results;
- temporary interfaces whose names and semantics are expected to change.

A Sonnet API carries **no stability promise** merely because several files use it. Its primary obligation is not reuse but an auditable research chain:

```text
problem
  -> primitive audit
  -> task semantics
  -> hypothesis
  -> candidate presentation / mechanism
  -> intended calculation + conventional baseline
  -> experiment
  -> certificate or failure
  -> stability / cost / transport audit where claimed
  -> red team
  -> claim boundary
```

Research-local code should stay research-local until there is evidence that the same semantic role belongs to Process Geometry rather than only to the problem that revealed it.

A substantial Sonnet conclusion should also state whether it supports, refines, contradicts, or leaves unchanged the current Theory Map. A Sonnet is allowed to contradict it; the contradiction is research evidence, not a governance violation.

## 2. Extraction candidates

When a Sonnet reveals a structure that may be reusable, first record an **extraction candidate** rather than refactoring the core immediately.

The extraction note may be short, but it should answer:

1. What repeated or forced structure was observed?
2. Which semantics appear essential, and which details are implementation accidents of the originating problem?
3. What is the smallest useful contract?
4. What is one positive example?
5. What is one negative or adversarial example?
6. What important boundary remains unresolved?
7. Which existing public abstraction, if any, is close enough that extension is preferable to a new concept?
8. **Where does this structure sit in the current Theory Map, and what part of that interpretation remains hypothetical?**
9. If it claims analysis or computational advantage, what is the smallest
   effective-analysis contract: symbolic/numerical mode, closure, evaluator,
   certificate, units, error/failure semantics, baseline, and cost boundary?

A beautiful abstraction with only a happy-path example is not ready for promotion.

An extraction candidate may be rejected immediately, remain inside its Sonnet, or enter Experimental.

## 3. Experimental: candidate theory, not a compatibility promise

Experimental is the incubation layer for abstractions that have escaped one problem but have not earned a public semantic commitment.

When experimental code is exposed as importable package code, its instability should be explicit, for example through a `process_geometry.experimental` namespace or an equivalently unmistakable location. Experimental symbols should not be re-exported from the stable package root.

Experimental means all of the following are allowed without a compatibility promise:

- renaming;
- changing signatures;
- changing object boundaries;
- merging two abstractions;
- splitting one abstraction;
- moving modules;
- rejecting the abstraction entirely.

Useful maturity states are metadata rather than separate namespaces:

```text
seed -> incubating -> maturing
```

A small status record should normally retain at least:

```yaml
status: incubating
origin:
  - sonnet-00x
consumers:
  - sonnet-00x
  - another-independent-calibration
theory_position:
  - <node/edge in docs/THEORY_MAP.md>
known_boundaries:
  - ...
effective_analysis:
  modes: [exact-symbolic | certified-approximate | numerical | search-only | record-only]
  evidence:
    - ...
  failure_semantics:
    - ...
  cost_boundary:
    - ...
```

The purpose of Experimental is to preserve freedom to discover the right ontology before compatibility pressure freezes the first plausible design.

An experimental abstraction may intentionally test a speculative node in the Theory Map. If so, both the code and its documentation must say that the theory element remains speculative; importability is not promotion of the mathematical claim.

## 4. Cross-problem survival

The strongest normal evidence for promotion is survival across independent problem domains.

Independence is semantic, not merely numerical. Two parameter settings of one model, or two examples that inherit the same solver ontology, do not constitute independent evidence. Prefer domains that force the abstraction from different mathematical directions.

The important criterion is stronger than reuse:

> Independent domains should place **different constraints** on the same abstraction.

For example, `PresentationMorphism` was promoted only after KdV, resistor networks, and braid/Markov calibrations forced different aspects of its minimal semantics: cross-presentation completeness, task-semantic confluence, and heterogeneous source/target spaces.

As a default rule, a generic abstraction should survive at least two genuinely independent domains before public promotion. Three are preferable for broad foundational concepts. An exception requires an unusually strong mathematical necessity and should be stated explicitly in the promotion rationale.

Cross-problem evidence should be interpreted against the Theory Map: repeated reuse is weaker evidence than independent domains forcing the same theoretical role from different directions.

## 5. Red-team requirement

Every abstraction approaching `maturing` must carry three kinds of evidence:

### Happy path

A problem for which the abstraction is natural and useful.

### Negative control

A nearby problem for which the abstraction should *not* be used.

### Adversarial case

A case that superficially resembles the intended semantics but violates a necessary condition or exposes an over-generalization.

The red team should sharpen what the concept is not. If an abstraction expands until every callable, state transformation, coordinate map, or container is an instance of it, it has ceased to carry useful semantics.

For foundational concepts, the red team should also try to distinguish neighboring Theory Map nodes. Examples include:

- bounded distinguishability evidence versus an exact task quotient;
- an algebraic observable image versus a semantic process quotient;
- a candidate primitive versus genuine objectification;
- symbol expansion versus compositional rank lowering;
- a local differential construction versus a general observer connection.
- an exact symbolic closure versus a one-backend simplification success;
- numerical agreement at selected samples versus stable evaluation on a
  declared domain;
- shortened syntax versus lower total cost after compilation, storage,
  residual, and lowering are charged;
- formal cross-rank variation versus certified/effective analytic closure.

## 6. Public API: a semantic commitment

The public API is not a catalogue of mature implementations. It is the set of concepts for which Process Geometry is prepared to make a durable semantic promise.

Implementation stability is therefore necessary only in the ordinary software sense; it is not sufficient for conceptual promotion:

```text
implementation stability != conceptual maturity
```

Before a new generic abstraction enters the public API, the promotion record should normally establish all of the following:

1. **Minimal semantics are clear.** The concept can be stated compactly without referring to one implementation or one motivating problem.
2. **Independent evidence exists.** Normally at least two independent domains reuse the abstraction and constrain it differently.
3. **Red teams exist.** Happy path, negative control, and adversarial boundary have been exercised.
4. **A real design alternative was considered.** The public design is not simply the first prototype that happened to work.
5. **The contract is smaller than the motivating implementations.** Problem-specific power stays outside the generic API unless separately justified.
6. **Migration semantics are known.** It is clear what behavior must remain true if the internal implementation is replaced.
7. **Tests and documentation protect the semantic contract.** Tests should cover meaning, not merely object construction or importability.
8. **Known non-goals are explicit.** A public abstraction should document what it intentionally does not promise.
9. **Theory position is explicit.** The proposal states which node/arrow of the current Theory Map it implements or tests, and distinguishes that from neighboring stronger interpretations.
10. **Theory-change risk is acceptable.** The API remains narrower than unsettled theory so that a later revision of the Theory Map does not force the project to preserve a known-wrong ontology indefinitely.
11. **Its calculation contract is explicit when applicable.** An API that
    claims analysis, computation, stability, or efficiency states whether it is
    exact symbolic, certified approximate, numerical, search-only, or
    record-only; its evaluator, certificates, domain, units, error/failure
    semantics, baseline, and cost boundary are protected independently of one
    backend.

Public promotion is deliberately harder than merging useful code.

### 6.1 Mandatory Theory Impact review

Any change that **adds, renames, generalizes, promotes, or materially changes** an Experimental or Public API must include a short **Theory Impact** section in the PR, AEP, or promotion note.

It must answer the eight questions defined in `THEORY_MAP.md`:

1. **Theory position** — Which node or arrow does this API represent or test?
2. **Maturity** — What is the maturity of that theory element?
3. **Semantic claim** — What mathematical meaning does the API name/signature commit to?
4. **Non-claim** — Which nearby stronger interpretation is explicitly not being claimed?
5. **Evidence** — Which independent domains, certificates, or red teams justify this generality?
6. **Map effect** — Does the result support, refine, split, contradict, or leave unchanged the current Theory Map?
7. **Migration risk** — If the theory changes, can the API evolve without preserving a known-wrong ontology?
8. **Effective-analysis impact** — If the API claims analysis, calculation,
   stability, or efficiency, what are the symbolic/numerical mode,
   certificates, error/failure semantics, baseline, units, and cost boundary?

For a purely mechanical or compatibility-preserving change, the Theory Impact may be one sentence:

> `Theory Impact: none; this preserves the existing semantic contract and does not change its position in the Theory Map.`

For a new foundational abstraction, absence of a meaningful Theory Impact statement is itself evidence that the API is premature.

### 6.2 Names are theory claims

For foundational vocabulary, naming is part of the semantic contract. Words such as `ProcessGeometry`, `TaskQuotient`, `Jet`, `Objectification`, `ProcessRank`, `RankLowering`, `ObserverTopology`, `AnalyticClosure`, `ComputablePresentation`, `CanonicalSolver`, or a generic `Calculus` should not be used for weaker local mechanisms merely because the name is attractive.

`docs/48-foundation-naming-audit.md` records the first vocabulary audit. Future naming changes should be reviewed using the Theory Map rather than by local code aesthetics alone.

## 7. No direct Sonnet -> Public API promotion

The default prohibition is:

```text
Sonnet -X-> Public API
```

A Sonnet may prove that a concept is useful. It cannot by itself show that the concept belongs to the framework rather than to that problem.

If a Sonnet urgently needs shared implementation before cross-domain evidence is available, place the candidate in Experimental or keep it research-local. Do not turn schedule pressure into ontology.

## 8. AEP: lightweight promotion records

For substantial experimental promotion, use a short **AEP (AEG Enhancement Proposal)** or an equivalent promotion note. This is intended as an auditable rationale, not a heavyweight standards process.

A minimal AEP contains:

```text
AEP-NNNN: <name>

Origin
  Sonnet / calibration that first forced the concept

Problem
  What common semantic role is missing?

Theory position
  Which node/arrow in docs/THEORY_MAP.md is represented or tested?
  What is its current maturity?

Minimal semantics
  The smallest proposed contract

Theory Impact
  Semantic claim
  Explicit non-claim
  Evidence
  Map effect: support | refine | split | contradict | unchanged
  Theory-change / migration risk

Effective analysis, if claimed
  exact-symbolic | certified-approximate | numerical | search-only | record-only
  closure / controlled extension
  evaluator / certificate
  domain / units / error and failure semantics
  baseline / workload / cost boundary
  lift / lowering transport

Evidence
  Independent consumers and red teams

Rejected alternatives
  Designs actually considered and why they were rejected

Known boundaries
  What remains intentionally unresolved

Status
  seed | incubating | maturing | accepted | rejected | deprecated
```

AEPs become especially valuable when an abstraction is renamed, merged, rejected, or later deprecated: the repository retains why the decision was made rather than only the final code shape.

The historical name **AEG Enhancement Proposal** may be retained for continuity, but an AEP governs Process Geometry software semantics; acceptance does not imply Arithmetic Universality or any other stronger AEG conjecture.

## 9. Rejection, death, and deprecation are healthy outcomes

Experimental abstractions are expected to die frequently. A low rejection rate would usually mean the incubation layer is not being used aggressively enough.

When an experimental idea fails, prefer an explicit `rejected` status and a short postmortem over silent deletion if the failure teaches a reusable lesson.

Public APIs may also be corrected. If later evidence shows that a public concept has the wrong semantics, use an explicit deprecation/migration path rather than preserving a mistaken ontology indefinitely for cosmetic stability.

A rejected abstraction can still improve the Theory Map. A public deprecation caused by a theory correction should record both the software migration and the theoretical correction that forced it.

## 10. Relationship to existing repository practice

This policy formalizes a discipline that already appears in several earlier decisions:

- the finite-family API freeze deliberately left unresolved central residuals outside the public slice;
- subsequent notes explicitly warned against extending that API before a new executable vignette forced the extension;
- `PresentationMorphism` was promoted only after three independent domains forced a smaller common contract;
- the first Process Geometry naming audit deliberately renamed `ProcessJetSignature` and qualified algebraic observable quotients rather than allowing local implementations to occupy stronger foundation vocabulary;
- the `process_geometry` namespace migration kept old imports as compatibility aliases while making canonical ownership one-way, demonstrating that software identity can change without inventing new theory semantics.

Those decisions should now be treated as instances of this general lifecycle, not as isolated precedents.

Existing public APIs are not retroactively demoted by this note. Future generic extensions and new public abstractions should follow the lifecycle unless a promotion record documents why an exception is justified.

## 11. Operational defaults

When deciding where new work belongs, use these defaults:

| Situation | Default home |
| --- | --- |
| Open-ended problem investigation | `sonnet/` |
| Problem-local prototype | the originating Sonnet |
| Reusable idea with only one convincing domain | Sonnet extraction candidate |
| Reusable idea with initial cross-problem evidence | Experimental |
| Cross-domain abstraction still changing materially | Experimental, `incubating` |
| Semantics stable and promotion gates nearly met | Experimental, `maturing` |
| Evidence-backed long-term semantic commitment | Public API |

Tests follow the same distinction. Research benchmarks and frontier probes may remain Sonnet-local or manually dispatched; public semantic regressions belong in the ordinary test suite.

For analysis-bearing work, tests must also follow the claim mode. Exact
symbolic claims use exact relations, residuals, properties, or round trips;
numerical claims use scale-aware tolerances, convergence/invariant or
independent-reference evidence, and explicit singular/nonconvergence behavior;
efficiency claims report workload and baseline and separate discovery or
compilation cost from repeated evaluation. A field may be marked `not
applicable`, but an unmeasured field cannot support a positive claim.

For API-changing PRs, review is incomplete until the Theory Impact requirement is satisfied. For research-only work, updating the Theory Map is optional unless the result materially changes the larger picture; in that case the research note should propose the map revision explicitly.

## 12. Seven standing rules

The repository governance can be compressed to seven rules:

1. **Sonnets discover; they do not standardize.**
2. **Reusable structures enter Experimental before the public API.**
3. **Experimental abstractions must survive independent problems and red-team cases.**
4. **Public API is a semantic commitment, not merely a stable implementation.**
5. **Every material API change states its position and impact in the evolving Theory Map.**
6. **Promotion, rejection, deprecation, and theory correction leave an auditable rationale.**
7. **Analysis claims preserve calculability: symbolic/numerical mode,
   certificates, error/failure semantics, units, baseline, and cost boundaries
   are part of the contract.**

The purpose of this process is not bureaucracy. It is to protect both sides of Process Geometry: research must remain free enough to discover a better ontology, while the public API must remain small enough that its concepts actually mean something.

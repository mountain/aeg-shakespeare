# Research and API governance

**Status:** repository policy for future research extraction and API promotion.

Shakespeare is both a research program and a software system. Those two roles
need different stability rules. Open-ended problem solving should be allowed to
invent, discard, and contradict provisional structures; the public API should
make only narrow, evidence-backed semantic commitments.

The governing principle is:

> **Sonnets discover problems and structures. Experimental incubates candidate
> abstractions. The public API makes commitments.**

The default lifecycle is therefore

```text
Sonnet
  -> extraction candidate
  -> Experimental
  -> maturing
  -> Public API
```

This is a one-way promotion path by default. A Sonnet must not promote a new
generic abstraction directly into the public API.

## 1. Sonnet: the problem space

`sonnet/` is the most permissive research layer. A Sonnet may contain:

- problem-specific mathematical definitions;
- provisional observers, presentations, quotients, morphisms, and cost models;
- competing or mutually incompatible designs;
- one-off scripts and deliberately ugly prototypes;
- failed approaches and negative results;
- temporary interfaces whose names and semantics are expected to change.

A Sonnet API carries **no stability promise** merely because several files use
it. Its primary obligation is not reuse but an auditable research chain:

```text
problem
  -> primitive audit
  -> task semantics
  -> hypothesis
  -> candidate presentation / mechanism
  -> experiment
  -> certificate or failure
  -> red team
  -> claim boundary
```

Research-local code should stay research-local until there is evidence that the
same semantic role belongs to Shakespeare rather than only to the problem that
revealed it.

## 2. Extraction candidates

When a Sonnet reveals a structure that may be reusable, first record an
**extraction candidate** rather than refactoring the core immediately.

The extraction note may be short, but it should answer:

1. What repeated or forced structure was observed?
2. Which semantics appear essential, and which details are implementation
   accidents of the originating problem?
3. What is the smallest useful contract?
4. What is one positive example?
5. What is one negative or adversarial example?
6. What important boundary remains unresolved?
7. Which existing public abstraction, if any, is close enough that extension is
   preferable to a new concept?

A beautiful abstraction with only a happy-path example is not ready for
promotion.

An extraction candidate may be rejected immediately, remain inside its Sonnet,
or enter Experimental.

## 3. Experimental: candidate theory, not a compatibility promise

Experimental is the incubation layer for abstractions that have escaped one
problem but have not earned a public semantic commitment.

When experimental code is exposed as importable package code, its instability
should be explicit, for example through an `aeg_shakespeare.experimental`
namespace or an equivalently unmistakable location. Experimental symbols should
not be re-exported from the stable package root.

Experimental means all of the following are allowed without a compatibility
promise:

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
known_boundaries:
  - ...
```

The purpose of Experimental is to preserve freedom to discover the right
ontology before compatibility pressure freezes the first plausible design.

## 4. Cross-problem survival

The strongest normal evidence for promotion is survival across independent
problem domains.

Independence is semantic, not merely numerical. Two parameter settings of one
model, or two examples that inherit the same solver ontology, do not constitute
independent evidence. Prefer domains that force the abstraction from different
mathematical directions.

The important criterion is stronger than reuse:

> Independent domains should place **different constraints** on the same
> abstraction.

For example, `PresentationMorphism` was promoted only after KdV, resistor
networks, and braid/Markov calibrations forced different aspects of its minimal
semantics: cross-presentation completeness, task-semantic confluence, and
heterogeneous source/target spaces.

As a default rule, a generic abstraction should survive at least two genuinely
independent domains before public promotion. Three are preferable for broad
foundational concepts. An exception requires an unusually strong mathematical
necessity and should be stated explicitly in the promotion rationale.

## 5. Red-team requirement

Every abstraction approaching `maturing` must carry three kinds of evidence:

### Happy path

A problem for which the abstraction is natural and useful.

### Negative control

A nearby problem for which the abstraction should *not* be used.

### Adversarial case

A case that superficially resembles the intended semantics but violates a
necessary condition or exposes an over-generalization.

The red team should sharpen what the concept is not. If an abstraction expands
until every callable, state transformation, coordinate map, or container is an
instance of it, it has ceased to carry useful semantics.

## 6. Public API: a semantic commitment

The public API is not a catalogue of mature implementations. It is the set of
concepts for which Shakespeare is prepared to make a durable semantic promise.

Implementation stability is therefore necessary only in the ordinary software
sense; it is not sufficient for conceptual promotion:

```text
implementation stability != conceptual maturity
```

Before a new generic abstraction enters the public API, the promotion record
should normally establish all of the following:

1. **Minimal semantics are clear.** The concept can be stated compactly without
   referring to one implementation or one motivating problem.
2. **Independent evidence exists.** Normally at least two independent domains
   reuse the abstraction and constrain it differently.
3. **Red teams exist.** Happy path, negative control, and adversarial boundary
   have been exercised.
4. **A real design alternative was considered.** The public design is not simply
   the first prototype that happened to work.
5. **The contract is smaller than the motivating implementations.** Problem-
   specific power stays outside the generic API unless separately justified.
6. **Migration semantics are known.** It is clear what behavior must remain true
   if the internal implementation is replaced.
7. **Tests and documentation protect the semantic contract.** Tests should cover
   meaning, not merely object construction or importability.
8. **Known non-goals are explicit.** A public abstraction should document what it
   intentionally does not promise.

Public promotion is deliberately harder than merging useful code.

## 7. No direct Sonnet -> Public API promotion

The default prohibition is:

```text
Sonnet -X-> Public API
```

A Sonnet may prove that a concept is useful. It cannot by itself show that the
concept belongs to the framework rather than to that problem.

If a Sonnet urgently needs shared implementation before cross-domain evidence is
available, place the candidate in Experimental or keep it research-local. Do not
turn schedule pressure into ontology.

## 8. AEP: lightweight promotion records

For substantial experimental promotion, use a short **AEP (AEG Enhancement
Proposal)** or an equivalent promotion note. This is intended as an auditable
rationale, not a heavyweight standards process.

A minimal AEP contains:

```text
AEP-NNNN: <name>

Origin
  Sonnet / calibration that first forced the concept

Problem
  What common semantic role is missing?

Minimal semantics
  The smallest proposed contract

Evidence
  Independent consumers and red teams

Rejected alternatives
  Designs actually considered and why they were rejected

Known boundaries
  What remains intentionally unresolved

Status
  seed | incubating | maturing | accepted | rejected | deprecated
```

AEPs become especially valuable when an abstraction is renamed, merged, rejected,
or later deprecated: the repository retains why the decision was made rather
than only the final code shape.

## 9. Rejection, death, and deprecation are healthy outcomes

Experimental abstractions are expected to die frequently. A low rejection rate
would usually mean the incubation layer is not being used aggressively enough.

When an experimental idea fails, prefer an explicit `rejected` status and a
short postmortem over silent deletion if the failure teaches a reusable lesson.

Public APIs may also be corrected. If later evidence shows that a public concept
has the wrong semantics, use an explicit deprecation/migration path rather than
preserving a mistaken ontology indefinitely for cosmetic stability.

## 10. Relationship to existing repository practice

This policy formalizes a discipline that already appears in several earlier
Shakespeare decisions:

- the finite-family API freeze deliberately left unresolved central residuals
  outside the public slice;
- subsequent notes explicitly warned against extending that API before a new
  executable vignette forced the extension;
- `PresentationMorphism` was promoted only after three independent domains
  forced a smaller common contract.

Those decisions should now be treated as instances of this general lifecycle,
not as isolated precedents.

Existing public APIs are not retroactively demoted by this note. Future generic
extensions and new public abstractions should follow the lifecycle unless a
promotion record documents why an exception is justified.

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

Tests follow the same distinction. Research benchmarks and frontier probes may
remain Sonnet-local or manually dispatched; public semantic regressions belong
in the ordinary test suite.

## 12. Five standing rules

The repository governance can be compressed to five rules:

1. **Sonnets discover; they do not standardize.**
2. **Reusable structures enter Experimental before the public API.**
3. **Experimental abstractions must survive independent problems and red-team
   cases.**
4. **Public API is a semantic commitment, not merely a stable implementation.**
5. **Promotion, rejection, and deprecation leave an auditable rationale.**

The purpose of this process is not bureaucracy. It is to protect both sides of
Shakespeare: research must remain free enough to discover a better ontology,
while the public API must remain small enough that its concepts actually mean
something.

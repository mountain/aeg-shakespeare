# Minimal `PresentationMorphism` API

**Status:** first public promotion after three independent calibration domains.

## 1. Why this abstraction is promoted now

Shakespeare has repeatedly delayed generic abstractions until more than one
mathematical family forced the same semantic role.  `PresentationMorphism` now
crosses that threshold.

The pressure comes from three deliberately different settings.

### KdV

The Hirota tau presentation and the parametric soliton-scattering presentation
encode the same pair and three-body interaction data.  The red team showed that
local pairwise rewrite confluence can survive even when an irreducible three-body
tau coefficient is wrong.  Thus a transformation between presentations needs an
explicit statement of **what task semantics is preserved** and what evidence
supports cross-presentation completeness.

### Resistor networks

Schur-complement/Y--Delta reductions can produce syntactically different network
presentations while preserving exactly the same Dirichlet-to-Neumann boundary
response.  Two different intermediate graphs can therefore already be joined in
the declared task semantics before they reach a common graph normal form.

This separates

\[
\text{syntactic confluence}
\quad\text{from}\quad
\text{task-semantic confluence}.
\]

### Braids and links

Markov stabilization sends a presentation in `B_n` to one in `B_(n+1)` while
preserving the isotopy class of the standard closure.  In the executable
calibration the reduced Burau representation changes dimension from `1x1` to
`2x2`, while the chosen closure Alexander observer remains unchanged.

Hence a generic presentation morphism cannot assume that source and target share
one carrier type, coordinate dimension, alphabet, or representation backend.

## 2. The minimal common contract

The three domains jointly force only the following data:

```python
PresentationMorphism(
    source=...,
    target=...,
    task_semantics=...,
    certificate=...,
    witness=...,
    label=...,
)
```

Conceptually,

\[
\boxed{
M:\Pi_{\rm source}\longrightarrow\Pi_{\rm target}
\quad\text{with evidence relative to }Q.
}
\]

The fields mean:

- **`source`** -- the starting presentation;
- **`target`** -- the transformed presentation, possibly of a different type;
- **`task_semantics`** -- a caller-defined description/object specifying what
  observable, quotient, or task meaning is claimed to be preserved;
- **`certificate`** -- caller-defined evidence supporting that preservation;
- **`witness`** -- optional provenance for how the transformation was obtained,
  such as a rewrite trace, parameter map, elimination history, or construction;
- **`label`** -- optional human-readable identification.

The object deliberately does not inspect or reinterpret any of those values.

## 3. Why the certificate is opaque

The three motivating certificates live in different mathematical categories:

```text
KdV:
    symbolic equality / factorization residuals

resistor networks:
    exact matrix equality after Schur complement

braids:
    equality of a closure invariant across different braid indices
```

A generic verifier introduced now would either be vacuous or would smuggle one
of these mathematical categories into presentation ontology.

Therefore `certificate` is intentionally generic.  Verification belongs to the
concrete task/discovery layer that created the morphism.

This also allows later numerical, probabilistic, bounded, or formally checked
certificates without changing the morphism container itself.

## 4. What is explicitly *not* being promoted

The first API does not provide:

- `verified` / `verify()`;
- `compose()`;
- identity morphisms;
- inverses;
- associativity laws;
- a category or groupoid object;
- a universal equivalence relation;
- normal forms;
- automatic cost propagation;
- automatic decoder construction;
- parametric history matching;
- a universal confluence certificate.

The absence of these methods is part of the contract.

Composition is especially postponed.  If two morphisms

\[
\Pi_0\xrightarrow{M_1}\Pi_1\xrightarrow{M_2}\Pi_2
\]

preserve different task semantics or carry different certificate types, it is
not yet clear what evidence must accompany the composite.  A later calibration
must answer that question before Shakespeare gives composition a public meaning.

## 5. Relation to the semantic architecture

`PresentationMorphism` belongs in the **presentation** layer, not `process`,
`discovery`, or `analysis`.

```text
Process -> Presentation -> Discovery -> Analysis
              |
              +-- morphism
```

A process exists independently of how it is represented.  Discovery may propose
or search for morphisms.  Analysis may consume a successful target presentation.
But the fact that one presentation was transformed into another while preserving
some declared task meaning is itself presentation-level information.

## 6. Relation to existing task signatures

`ProcessJetSignature` already gives a bounded notion of task equivalence for
histories that share one process transition semantics.  `PresentationMorphism`
addresses a different problem: source and target may have different internal
state spaces and even different Python types.

The two ideas are compatible rather than redundant:

```text
ProcessJetSignature:
    compare histories under one declared process/task interface

PresentationMorphism:
    carry evidence relating possibly heterogeneous presentations
```

A future cross-presentation task-signature interface may connect them, but the
current API does not assume one.

## 7. First promotion rule

The methodological rule used here is worth keeping:

> Promote a generic presentation abstraction only after independent domains not
> only reuse it, but place *different constraints* on its semantics.

The three calibrations did exactly that:

1. KdV required separating local confluence from cross-presentation completeness;
2. resistor networks required task-semantic rather than syntactic confluence;
3. braid/Markov required heterogeneous source and target presentation spaces.

The resulting API is consequently smaller than any one domain-specific design.
That is intentional.

## 8. Next pressure test

The next question is no longer whether a morphism object exists.  It is whether
**morphism composition** has a stable domain-independent meaning.

A useful next experiment should construct a nontrivial chain

\[
\Pi_0\to\Pi_1\to\Pi_2
\]

in at least two domains and ask what certificate/provenance information must be
retained for the composite to remain auditable and task-sufficient.

Until then, `PresentationMorphism` remains a minimal evidence-bearing record and
nothing stronger.

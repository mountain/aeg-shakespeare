# Mathematical Vignette Contract

**Status:** repository policy for substantial mathematical examples, calibrations, and executable essays.

A Process Geometry vignette is more than a regression test and more than evidence for the Theory Map. A substantial vignette has three independent duties:

1. **Research** — expose a mathematical mechanism to executable calibration, falsification, and comparison.
2. **Exposition** — state one mathematical problem independently and completely enough that a reader can understand the question before learning the repository's answer.
3. **Knowledge entry** — remain a durable retrieval point for future humans and models searching by problem, classical terminology, structural mechanism, or theory role.

These duties are cumulative. A vignette may leave the Theory Map unchanged and still be excellent. Conversely, an important calibration is incomplete as a vignette if it cannot be understood or found without reconstructing repository history.

> **A vignette should be independently readable, executably auditable, and retrievably identifiable.**

This policy complements `09-literate-programming-and-mathematical-lineage.md`, `11-references-and-test-essays.md`, `THEORY_GOVERNANCE.md`, and `GOVERNANCE.md`.

---

## 1. The vignette is a knowledge unit

The primary unit is the mathematical problem and its reconstruction, not the Python file.

A vignette may be one test module, a linked family of modules, or a test plus a companion note. Whatever the physical layout, there must be an explicit entry point answering:

- What is the problem?
- What data and assumptions define it?
- What is classically known or expected?
- What does Process Geometry reconstruct without assuming the answer?
- What exactly is executable here?
- What remains unresolved?
- Where should the reader go next?

Splitting implementation across files is allowed. Splitting the mathematical statement across undocumented chronology is not.

---

## 2. Standalone completeness

A substantial vignette should be understandable by a mathematically competent reader who arrives directly from search, without first reading the repository README or an earlier vignette.

Its entry point should normally contain:

### Identity

Use a human-recognizable problem title before repository-local sequence names. Prefer

```text
Simple pendulum: constrained planar mechanics to a genus-one observable curve
```

over a bare title such as `Pendulum III`.

### Problem statement

State the problem in ordinary domain language before the Process Geometry reconstruction. Identify the mathematical objects, hypotheses or parameter regime, the question, and the output or phenomenon of interest.

### Prerequisites and notation

Define project-local notation and state substantial prerequisites. A vignette need not reteach standard mathematics, but it must not silently assume repository-specific vocabulary.

### Why this problem is here

State the mathematical pressure supplied by the example: classical calibration, negative control, degeneration, cross-domain probe, counterexample, theory-edge test, or pedagogically canonical example.

### Classical answer / lineage

Give enough conventional mathematics that the reader knows what is being reconstructed, while keeping the classical answer out of primitive input when discovery is the point.

### Process Geometry reconstruction

State the process-first route in mathematical dependency order.

### Executable claim and proof map

State exactly what passing the vignette certifies, and map the claim to assertions or certificates.

### Boundary

State what is not established, including information loss or missing reconstruction when relevant.

### References and onward links

Provide authoritative references and stable links to companion vignettes, theory records, and implementation owners when useful.

---

## 3. Retrieval completeness

A vignette must be findable under the vocabulary a future reader is likely to use, not only under the vocabulary Process Geometry eventually assigns to it.

Every substantial entry point should expose a small prose retrieval header near the top:

```text
Problem:
Domains:
Classical names / aliases:
Structural themes:
Process Geometry roles:
Prerequisites:
Related vignettes:
Theory Map relation:
```

This is documentation metadata, not a runtime schema.

When applicable, include three vocabularies:

1. **problem vocabulary** — `simple pendulum`, `quartic oscillator`, `resistor network`;
2. **classical vocabulary** — `elliptic integral`, `genus one`, `Dirichlet-to-Neumann map`;
3. **Process Geometry vocabulary** — `observable algebraic quotient`, `presentation morphism`, `history residual`.

This prevents the repository from becoming searchable only by its own ontology.

Retrieval aliases do **not** promote claims. Listing `Jacobian` or `canonical clock` as a search anchor does not assert a Jacobian theorem or canonicality result. Epistemic status remains controlled by the claim text and Theory Governance.

---

## 4. Educational completeness is not tutorial maximalism

The standard is

```text
self-contained statement
+ explicit notation
+ sufficient lineage
+ visible derivation map
+ references for imported mathematics
```

not re-proving every classical prerequisite.

When a prerequisite is substantial, state it and cite a good entry point. When a repository abstraction is essential, explain its semantics briefly before linking to API documentation.

---

## 5. Completeness has several independent axes

A vignette should be reviewed separately for:

| Axis | Question |
| --- | --- |
| Mathematical statement | Is the original problem stated completely? |
| Exposition | Can a direct reader understand objects, notation, motivation, and result? |
| Executability | Do assertions/certificates audit the derivation? |
| References | Can imported facts and lineage be checked? |
| Retrieval | Can the vignette be found under external and internal vocabularies? |
| Theory relation | Is its Theory Map role stated without over-promotion? |
| Reconstruction | If information is lost, is the decoder/information-loss boundary explicit? |

Strength on one axis does not repair failure on another. A perfect regression test can still be a poor vignette; a beautiful essay can still lack an executable certificate.

---

## 6. Relation to the Theory Map

Every substantial vignette should state its Theory Map relation, but `unchanged` is a first-class result.

Useful roles include:

- `calibrates <node/edge>`;
- `supports <claim>`;
- `red-teams <claim>`;
- `provides a degeneration of <claim>`;
- `compares competing hypotheses`;
- `historical / pedagogical anchor`;
- `Theory Map relation: unchanged`.

A vignette is not required to generate a theory node. This protects educationally important examples from being judged only by abstraction yield.

Conversely, theory promotion should cite complete vignettes where possible so a reader can descend from a map-level claim to an independently readable mathematical problem.

---

## 7. Relation to software extraction

Named mathematical problems normally remain in `tests/classical/`, `tests/research/`, or Sonnets even when they are excellent knowledge artifacts. Reusable implementation moves into `src/` only under `GOVERNANCE.md`.

Do not move a named problem into the public package merely to make it discoverable. Improve indexing and cross-links instead.

---

## 8. Linked vignette families

A mature research line may require several executable files. In that case designate one file or note as the **vignette entry point**.

The entry point should state the complete problem, list the linked stages, distinguish prerequisites from refinements, identify which artifact certifies each stage, and expose retrieval metadata for the family.

Later files may avoid repeating all background if they link back explicitly and still state their local question and claim boundary.

This avoids both extremes: repeating an entire textbook introduction in every file, or forcing a reader to reconstruct the problem from a chronology of `II`, `III`, `cross-calibration`, and `red-team` filenames.

---

## 9. Durable retrieval for future humans and models

Assume future readers may arrive through code search, semantic search, model retrieval, a citation, or a single copied path.

Therefore:

- use explicit mathematical nouns rather than pronouns whose referent is elsewhere;
- state important equations in the entry point rather than only in helper code;
- spell out uncommon abbreviations at first use;
- keep classical names and Process Geometry names adjacent where useful;
- prefer stable cross-links to phrases such as `the previous experiment`;
- state claim status close to the claim;
- retain negative results and boundaries when they disambiguate the example.

The goal is not optimization for one search engine. It is preservation of semantic handles that survive changes in tooling.

---

## 10. Completion gate

Before calling a substantial vignette complete, check:

### Independent statement

- [ ] Human-recognizable problem/title is present.
- [ ] Objects, assumptions, parameter regime, and question are explicit.
- [ ] Project-local notation is defined.
- [ ] The reason for inclusion is stated.

### Mathematical audit

- [ ] Primitive inputs are distinguished from discovered/classical outputs.
- [ ] Executable claim is precise.
- [ ] Proof map corresponds to actual assertions/certificates.
- [ ] Claim boundary and information loss are explicit where relevant.
- [ ] References are authoritative and correctly attributed.

### Retrieval

- [ ] Problem vocabulary is present.
- [ ] Classical aliases/terms are present where useful.
- [ ] Process Geometry structural terms are present where useful.
- [ ] Related vignettes and theory records are linked stably.
- [ ] A direct reader can identify the next useful artifact.

### Governance

- [ ] Theory Map relation is stated, including `unchanged` when appropriate.
- [ ] The vignette does not silently promote theory or software.

---

## 11. Repository policy

For substantial mathematical work, completeness means more than `pytest` passing.

A mathematical vignette is complete only when it functions simultaneously as:

```text
an executable calibration,
a small independent mathematical exposition,
and a durable knowledge-retrieval entry point.
```

These roles are cumulative, not competing.
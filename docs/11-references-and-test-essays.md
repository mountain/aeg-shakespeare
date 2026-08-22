# References and executable mathematical essays

A mathematical test program in Shakespeare is not merely a regression check. It is a small, completed mathematical essay whose executable assertions certify the argument.

This strengthens the literate-programming rule in `docs/09-literate-programming-and-mathematical-lineage.md`.

There is one deliberate distinction. Pure plumbing tests — for example, whether a dataclass rejects a negative bound or whether a public symbol imports — may remain concise unit tests. But **every test whose purpose is to make a mathematical claim, recover a classical structure, or compare mathematical representations should be written as a complete cited mathematical vignette**. In particular this applies to all substantial files in `tests/classical/` and `tests/research/`, and to mathematical calibration files elsewhere in the suite until they are reorganized.

## 1. What a completed test essay must contain

A mathematical test essay should contain, normally in its module docstring, the following parts.

1. **Question.** State the mathematical problem and the representation question being tested.
2. **Primitive data.** State exactly what Shakespeare is allowed to receive as input.
3. **Classical lineage.** Explain how the corresponding mathematics arose or is conventionally presented, without using the classical answer as an input to the discovery step.
4. **Shakespeare reconstruction.** Give the chain of process, relation, quotient, geometry, or function-theory steps that the test will execute.
5. **Theorem/calibration statement.** State precisely what the test certifies.
6. **Proof map.** Explain which executable assertions certify which mathematical steps.
7. **Boundary.** State what is not proved: for example, a genus computation is not by itself a uniformization theorem.
8. **References.** Give complete bibliographic references with a stable URL, DOI, book edition, theorem/section, or other locator whenever possible.

A reader should be able to understand the mathematical point of the file before reading the Python implementation. The intended unit is therefore not “one assertion = one essay”; rather, one coherent test module should read as a finished mathematical miniature whose individual test functions form the proof/checking steps.

## 2. Citation discipline

References are evidence, not decoration.

- Historical claims should cite a history source or the original work when practical.
- Classical mathematical facts should cite a standard monograph, handbook, or primary source.
- A test should identify the relevant chapter, section, theorem, or equation when a source is large.
- Web references should prefer stable institutional sources such as DLMF, arXiv, journal pages, university scans, or publisher pages.
- If a statement is the project's own interpretation, label it **Shakespeare interpretation** rather than attaching a classical citation that appears to endorse the new claim.
- If a result is derived directly in the test, the derivation is primary; a reference is still useful for the classical shadow but must not replace the executable proof.

Bibliographic fields themselves must be audited.  A syntactically complete entry with the wrong edition, page range, DOI, URL, authorship, or publication year is a failed reference, not a cosmetic defect.  Prefer the publisher, journal/DOI landing page, arXiv record, DLMF, or another authoritative catalogue when checking those fields.

## 3. Citation format inside Python tests

Use short keys in the essay and give full entries at the end of the module docstring, for example:

```text
References
----------
[Arnold-1989] V. I. Arnold, Mathematical Methods of Classical Mechanics,
2nd ed., Springer, 1989.

[DLMF-19] NIST Digital Library of Mathematical Functions, Chapter 19,
Elliptic Integrals, https://dlmf.nist.gov/19 .
```

When an exact section is central, include it:

```text
[DLMF-23.2] NIST DLMF, §23.2, Weierstrass Elliptic Functions,
https://dlmf.nist.gov/23.2 .
```

The repository does not require one citation syntax for all prose, but every key used in a test must resolve to a full entry in that test or in an explicitly named bibliography file.

## 4. Tests are proofs, not literature reviews

The bibliography should remain proportional to the argument. A five-step calibration usually needs a few strong references, not dozens of secondary citations.

The preferred hierarchy is:

```text
primitive data
  -> executable derivation
  -> structural assertion
  -> classical identification
  -> citation
```

not

```text
citation
  -> imported formula
  -> assertion that the library reproduces it
```

## 5. Historical reversal is part of the essay

For Shakespeare, mathematical history often reveals which later representation should *not* be treated as primitive.

For the pendulum, for example, the essay should distinguish:

- constrained mechanics as primitive data;
- the reduction to an algebraic energy curve;
- elliptic integration and inversion as the classical analytic development;
- double periodicity / complex-torus structure as the global analytic geometry;
- cubic algebraization as the finite function-field presentation.

The test should execute only the stages currently implemented and should mark later stages as future work rather than silently importing them.

## 6. Cross-artifact consistency is a proof obligation

A substantial result is usually represented in several places at once:

```text
research note / design note
source-level mathematical narrative
implementation
executable essay and assertions
API / release documentation
bibliographic references
```

These views must agree on the mathematical object, notation, sign convention,
hypotheses, status, and claim boundary.  In particular:

- a formula changed in code must be audited wherever the same formula is stated in prose;
- a changed commutator/order convention must be reflected in every affected equation and test;
- a provisional class or alias removed from code must not remain documented as current API;
- an experiment that is merely staged must not be described elsewhere as already passed;
- a heavy/full-census oracle must be distinguished from the cheaper algorithm being claimed;
- a project interpretation must not acquire the epistemic status of a cited classical theorem merely by repetition.

For research lines with several moving pieces, maintain a **claim ledger** mapping each important mathematical statement to its implementation owner, executable certificate, references, and epistemic status.  A row may be promoted only when all of those links are current.  The canonical-observer line provides the first concrete example in `docs/37-canonical-observer-claim-ledger.md`.

Mechanical CI can enforce only part of this obligation.  It should check what is cheaply decidable — required essay sections, citation-key resolution, Proof-map/test correspondence, namespace/API hygiene — while executable mathematics certifies identities and semantic invariants.  Human/research review remains responsible for checking that the prose means exactly what the code proves.

## 7. Release policy

For the `0.0.x` series, a mathematical calibration should not be considered complete until all applicable conditions hold:

- its executable assertions pass in routine CI;
- any dedicated heavy or full-census research gate required by the claim has passed;
- its mathematical essay and references are sufficient for an informed reader to audit the claim independently of the code;
- duplicated mathematical statements in notes/docs have been reconciled with the executable convention;
- its epistemic status has been updated only after those gates pass.

A technically useful unit test is exempt from the essay form only when it makes no substantive mathematical claim beyond implementation behavior.

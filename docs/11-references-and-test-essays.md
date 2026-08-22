# References and executable mathematical essays

A classical or research test in Shakespeare is not merely a regression check.  It is a small, completed mathematical essay whose executable assertions certify the argument.

This strengthens the literate-programming rule in `docs/09-literate-programming-and-mathematical-lineage.md`.

## 1. What a completed test essay must contain

A substantial test under `tests/classical/` or `tests/research/` should contain, normally in its module docstring, the following parts.

1. **Question.** State the mathematical problem and the representation question being tested.
2. **Primitive data.** State exactly what Shakespeare is allowed to receive as input.
3. **Classical lineage.** Explain how the corresponding mathematics arose or is conventionally presented, without using the classical answer as an input to the discovery step.
4. **Shakespeare reconstruction.** Give the chain of process, relation, quotient, geometry, or function-theory steps that the test will execute.
5. **Theorem/calibration statement.** State precisely what the test certifies.
6. **Proof map.** Explain which executable assertions certify which mathematical steps.
7. **Boundary.** State what is not proved: for example, a genus computation is not by itself a uniformization theorem.
8. **References.** Give complete bibliographic references with a stable URL, DOI, book edition, theorem/section, or other locator whenever possible.

A reader should be able to understand the mathematical point of the file before reading the Python implementation.

## 2. Citation discipline

References are evidence, not decoration.

- Historical claims should cite a history source or the original work when practical.
- Classical mathematical facts should cite a standard monograph, handbook, or primary source.
- A test should identify the relevant chapter, section, theorem, or equation when a source is large.
- Web references should prefer stable institutional sources such as DLMF, arXiv, journal pages, university scans, or publisher pages.
- If a statement is the project's own interpretation, label it **Shakespeare interpretation** rather than attaching a classical citation that appears to endorse the new claim.
- If a result is derived directly in the test, the derivation is primary; a reference is still useful for the classical shadow but must not replace the executable proof.

## 3. Citation format inside Python tests

Use short keys in the essay and give full entries at the end of the module docstring, for example:

```text
References
----------
[Arnold-1989] V. I. Arnold, Mathematical Methods of Classical Mechanics,
2nd ed., Springer, 1989, Chapter 3.

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

The bibliography should remain proportional to the argument.  A five-step calibration usually needs a few strong references, not dozens of secondary citations.

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

## 6. Release policy

For the `0.0.x` series, a new classical/research calibration should not be considered complete until both conditions hold:

- its executable assertions pass in CI;
- its mathematical essay and references are sufficient for an informed reader to audit the claim independently of the code.

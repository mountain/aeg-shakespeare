# Release 0.0.1: research preview

Version `0.0.1` is the first installable research preview of AEG Shakespeare.

It is intentionally **pre-alpha**. The package is ready to be installed and used as an experimental toolkit, but its public API is not yet stable and may change between `0.0.x` releases.

## What is being released

The release exposes reusable machinery for:

- literal ordered process histories and explicit rewrite relations;
- bounded task-sufficient process signatures;
- history depth, boundary profiles, and a Huffman prefix-code strategy;
- bounded construction-history-preserving primitive proposals;
- exact algebraic constraint quotients and process prolongation;
- generated finite process grammars, return relations, relation factors, and decoders;
- multi-axis presentation costs and Pareto filtering;
- generic multi-generator `ProcessFrame` and finite `ProcessFunctionModule` objects;
- the first concrete Addition/Multiplication (A/M) function-theory layer;
- small algebraic-quotient profiles used by classical calibration tests.

Named classical systems are not package-level solvers. Pendulum, oscillator, Duffing-like, and related examples remain executable mathematical essays under `tests/`.

## Compatibility contract

For `0.0.x` releases:

- semantic and API changes are expected;
- exact certificates and explicit failure modes are preferred to silent heuristics;
- no backward-compatibility guarantee is made yet;
- public changes should preserve the literate-programming discipline documented in `docs/09-literate-programming-and-mathematical-lineage.md`.

The first compatibility target is the *conceptual layer separation* rather than exact function signatures: literal histories, relation/constraint quotients, task sufficiency, representation search, and optional function theories should remain distinguishable.

## Release verification

A release candidate must pass both a software gate and a mathematical-auditability gate.

Software gate:

1. tests on Python 3.10, 3.11, and 3.12;
2. all public quickstart examples;
3. source distribution and wheel builds;
4. `twine check` on all distributions;
5. installation of the built wheel into a fresh virtual environment;
6. import/version smoke checks from outside the repository source tree.

Mathematical-auditability gate:

1. every substantial file under `tests/classical/` or `tests/research/` reads as a complete mathematical vignette;
2. each vignette states primitive data, theorem/calibration claim, proof map, and boundary;
3. established classical and historical statements carry rigorous references;
4. Shakespeare interpretations are labelled as project interpretations rather than attributed to classical sources.

See `docs/11-references-and-test-essays.md`, `docs/12-test-essay-template.py.txt`, and `docs/REFERENCES.md`.

## Publishing

The tag-triggered publishing workflow is designed for PyPI Trusted Publishing. The Trusted Publisher is configured on PyPI for this repository/workflow/environment.

The publishing identity is:

- GitHub owner: `mountain`;
- repository: `aeg-shakespeare`;
- workflow: `.github/workflows/publish.yml`;
- GitHub environment: `pypi`.

The OIDC `id-token: write` permission is scoped only to the publish job. No PyPI API token is committed to the repository.

## Release sequence

With the Trusted Publisher configured:

```text
main green
  -> create tag v0.0.1
  -> GitHub Actions builds and smoke-tests the distribution
  -> PyPI Trusted Publishing uploads aeg-shakespeare 0.0.1
```

## Public-domain status

The repository is released under the public-domain dedication in `LICENSE` (the Unlicense text). Scholarly citation remains a separate obligation; software citation metadata is in `CITATION.cff` and mathematical references are maintained in the literate tests and `docs/REFERENCES.md`.

# Release 0.0.1: research preview

Version `0.0.1` is the first installable research preview of AEG Shakespeare.

It is intentionally **pre-alpha**.  The package is ready to be installed and used as an experimental toolkit, but its public API is not yet stable and may change between `0.0.x` releases.

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

Named classical systems are not package-level solvers.  Pendulum, oscillator, Duffing-like, and related examples remain executable essays under `tests/`.

## Compatibility contract

For `0.0.x` releases:

- semantic and API changes are expected;
- exact certificates and explicit failure modes are preferred to silent heuristics;
- no backward-compatibility guarantee is made yet;
- public changes should preserve the literate-programming discipline documented in `docs/09-literate-programming-and-mathematical-lineage.md`.

The first compatibility target is the *conceptual layer separation* rather than exact function signatures: literal histories, relation/constraint quotients, task sufficiency, representation search, and optional function theories should remain distinguishable.

## Release verification

A release candidate must pass:

1. tests on Python 3.10, 3.11, and 3.12;
2. source distribution and wheel builds;
3. `twine check` on all distributions;
4. installation of the built wheel into a fresh virtual environment;
5. import/version smoke checks from outside the repository source tree.

The tag-triggered publishing workflow is designed for PyPI Trusted Publishing.  PyPI must be configured to trust the `mountain/aeg-shakespeare` repository, workflow `.github/workflows/publish.yml`, and `pypi` GitHub environment before the first tag is pushed.

## Release sequence

Once the Trusted Publisher is configured:

```text
main green
  -> create tag v0.0.1
  -> GitHub Actions builds distribution
  -> PyPI Trusted Publishing uploads aeg-shakespeare 0.0.1
```

No PyPI API token should be committed to the repository.

## Public-domain status

The repository is released under the public-domain dedication in `LICENSE` (the Unlicense text).  See the repository metadata and README for the same intent.

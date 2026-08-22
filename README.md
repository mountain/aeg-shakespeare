# AEG Shakespeare

**Shakespeare** is a process-representation library for building and searching compact process presentations.

It is not primarily an ODE solver and does not take eigenvectors, Fourier modes, a preferred coordinate system, or a particular special-function vocabulary as its starting ontology. The project starts from process structure, asks how that structure can be represented compactly, searches alternative presentations, and only then admits the analytic or geometric language forced by a successful presentation.

> Process ODE describes computation in a representation; Shakespeare provides machinery for searching for representations in which that computation is cheaper to express.

## Status

Latest PyPI release: **0.0.2**, a **pre-alpha research preview**.  
Current `main` release version: **0.0.2**.

The package is intended to be installable and useful as an experimental mathematical toolkit, but `0.0.x` APIs are not yet covered by backward-compatibility guarantees. Exact certificates, explicit failure modes, and conceptual layer separation take priority over interface stability during this phase.

See [`docs/34-release-0.0.2.md`](docs/34-release-0.0.2.md) for this release contract, [`docs/10-release-0.0.1.md`](docs/10-release-0.0.1.md) for the first-release contract, and [`CHANGELOG.md`](CHANGELOG.md) for release summaries.

## Install

```bash
python -m pip install aeg-shakespeare
```

For development:

```bash
python -m pip install -e '.[dev]'
```

PyPI distribution: `aeg-shakespeare`  
Python package: `aeg_shakespeare`  
Supported CPython versions: **3.10 through 3.14**

SymPy is an algebra/discovery backend. Shakespeare keeps its own process-level semantics and does not define process equality by `sympy.simplify()`.

## Public API direction

The public surface is organized as a mathematical pipeline rather than a flat catalog of symbols:

```text
Process  ->  Presentation  ->  Discovery  ->  Analysis
```

### `aeg_shakespeare.process`

What the process **is**.

- `process.history` — literal ordered histories and caller-supplied semantics;
- `process.finite` — finite parameterized families, characters, actions, and additive process cocycles;
- `process.local` — local/infinitesimal realizations such as `ProcessSystem` and `ProcessFrame`.

### `aeg_shakespeare.presentation`

How process history is **objectified, quotiented, compressed, transformed, and compared**.

- `presentation.history` — explicit rewriting, task signatures, and finite history geometry;
- `presentation.construction` — construction-history-preserving primitive proposals;
- `presentation.constraints` — exact algebraic quotient constraints;
- `presentation.grammar` — generated finite process grammars;
- `presentation.relations` — exact process relations, factors, kernels, and decompositions;
- `presentation.morphism` — task-relative, certificate-carrying transformations between possibly heterogeneous presentations;
- `presentation.search` — budgets, representation cost, Pareto filtering, and presentation search.

The first `PresentationMorphism` API is intentionally minimal: it records source, target, declared task semantics, a caller-defined certificate, and optional construction provenance. It does not yet define universal verification, composition, inverses, normal forms, or a category/groupoid structure.

### `aeg_shakespeare.discovery`

How alternative presentations are **searched**.

The current discovery package contains bounded polynomial invariant/quotient search, structured observer proposals, first-order quotient selection, and explicit coefficient-language extension experiments. These are search procedures, not process ontology.

### `aeg_shakespeare.analysis`

What analytic or geometric language a successful presentation **supports**.

- `analysis.module` — finite process-function modules;
- `analysis.am` — the Addition/Multiplication process calculus;
- `analysis.algebraic` — algebraic quotient profiles and Weierstrass calibration;
- `analysis.abelian` — lifted histories, Abelian integrals, cycle systems, periods, and normalized history quotients.

A representative import therefore looks like:

```python
from aeg_shakespeare.process.history import ProcessWord
from aeg_shakespeare.presentation.grammar import discover_generated_presentation
from aeg_shakespeare.presentation.morphism import PresentationMorphism
from aeg_shakespeare.discovery import discover_polynomial_invariants
from aeg_shakespeare.analysis.am import AMFunctionTheory
```

The package root is now intentionally only a namespace router:

```python
import aeg_shakespeare as sh

sh.process
sh.presentation
sh.discovery
sh.analysis
```

Legacy root-level imports from the early `0.0.x` research-preview surface remain available lazily during the migration and emit `DeprecationWarning`; they are no longer part of the declared public root surface. See [`docs/API.md`](docs/API.md) for the detailed map and migration notes.

## Quick start

The smallest runnable examples are deliberately problem-independent:

```bash
python examples/quickstart.py
python examples/constraint_quickstart.py
python examples/grammar_quickstart.py
```

They demonstrate, respectively:

1. literal process history, an explicit presentation relation, and A/M resonance;
2. exact equality modulo algebraic presentation constraints;
3. generated process grammars and return-relation discovery from a seed.

The examples are entry points, not mathematical proofs. Complete classical and research arguments live under `tests/classical/` and `tests/research/` as cited executable essays.

## Reading the source

Shakespeare uses a **literate-programming** discipline. Mathematically substantial Python modules and tests should explain the mathematical pressure that created an abstraction before presenting its implementation.

```text
classical historical path:
    analytic difficulty -> special construction -> geometry/algebra

Shakespeare reconstruction:
    primitive process -> history/constraint/invariant -> quotient geometry
    -> adequate function language -> classical formula as a shadow
```

The canonical pendulum calibration therefore begins from constrained position/velocity dynamics rather than from `theta`, `sin(theta)`, or a preselected elliptic function. Likewise, the A/M layer begins from **Addition and Multiplication** and their finite/noncommutative process relations before logarithms or familiar harmonic-analysis names are introduced.

A substantial test in `tests/classical/` or `tests/research/` is expected to be a complete mathematical vignette: question, primitive data, classical lineage, Shakespeare reconstruction, calibration statement, proof map, claim boundary, and bibliographic references.

See:

- [`docs/09-literate-programming-and-mathematical-lineage.md`](docs/09-literate-programming-and-mathematical-lineage.md)
- [`docs/11-references-and-test-essays.md`](docs/11-references-and-test-essays.md)
- [`docs/REFERENCES.md`](docs/REFERENCES.md)

## Current research boundary

The current implementation supports a bounded loop from declared process structure to evaluated presentations, plus concrete routes from successful presentations toward process-adapted function theory and global geometry.

Recent calibrations have established several deliberately limited layers:

- finite families, scalar characters, family actions, and additive process cocycles live in the **process** layer;
- rewriting, task quotients, construction histories, grammars, relations, task-relative presentation morphisms, and Pareto cost live in the **presentation** layer;
- invariant/observer/quotient/language proposals live in **discovery**;
- A/M calculus, algebraic quotient profiles, Abelian integrals, lifted cycles, period matrices, and normalized history quotients live in **analysis**.

`PresentationMorphism` was promoted only after independent KdV, resistor-network, and braid/Markov calibrations forced different aspects of the same role: cross-presentation completeness, task-semantic rather than syntactic confluence, and transformations between presentation spaces of different dimensions. The public object remains only an evidence-bearing record; composition and a universal verification semantics are still outside the API.

The separation is intentional. For example, `ProcessCocycle` is a finite-process object; generic cohomology classes, central-extension groups, projective representations, and an automatic finite-to-infinitesimal bridge are not currently public abstractions. Likewise, the existence of oscillator spectral shadows does not make maximal spectral splitting a universal presentation objective.

Physical and mathematical calibration problems do **not** define the package API. Pendulum, oscillator, Galilean mechanics, magnetic translations, KdV, resistor networks, and braid/Markov systems live in tests as probes of the common machinery.

## Development and release checks

```bash
python -m pip install -e '.[dev]'
pytest
python -m build
python -m twine check dist/*
```

CI tests the same release gate on CPython 3.10 through 3.14, installs the built wheel into a fresh virtual environment, and imports the package from outside the repository source tree. See [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

The evolving mathematical story is indexed in [`docs/README.md`](docs/README.md).

## License and citation

Shakespeare is dedicated to the **public domain** using the Unlicense public-domain dedication text in [`LICENSE`](LICENSE). The intent is unrestricted use, modification, publication, redistribution, and reuse of both the software and its accompanying mathematical exposition.

Scholarly attribution is separate from software licensing. Mathematical and historical sources are cited in the literate tests and [`docs/REFERENCES.md`](docs/REFERENCES.md); software citation metadata is provided in [`CITATION.cff`](CITATION.cff).

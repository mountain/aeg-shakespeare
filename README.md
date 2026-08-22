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

How process history is **objectified, quotiented, compressed, and compared**.

- `presentation.history` — explicit rewriting, task signatures, and finite history geometry;
- `presentation.construction` — construction-history-preserving primitive proposals;
- `presentation.constraints` — exact algebraic quotient constraints;
- `presentation.grammar` — generated finite process grammars;
- `presentation.relations` — exact process relations, factors, kernels, and decompositions;
- `presentation.search` — budgets, representation cost, Pareto filtering, and presentation search.

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

The project is intentionally layered:

- `process` owns histories and finite/local process structure;
- `presentation` owns quotienting, grammars, relations, budgets, costs, and search;
- `discovery` owns algorithms that propose or compare representations;
- `analysis` owns process-adapted function and global geometric languages.

Compatibility shims may remain during the `0.0.x` series, but canonical implementations are being physically consolidated under those semantic owners. The repository includes AST hygiene and physical-ownership tests to prevent the old flat module layout from becoming a hidden architecture again.

## License

Released into the public domain. See [`LICENSE`](LICENSE).

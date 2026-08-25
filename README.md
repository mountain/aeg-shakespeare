# Process Geometry

**Process Geometry** is an experimental process-first mathematical library for constructing, comparing, and discovering task-sufficient presentations of processes, and for developing the analytic language supported by those presentations.

The project does not assume that a process arrives with a preferred coordinate system, vector space, Fourier basis, eigenmode decomposition, or special-function vocabulary. It starts from primitive process structure and asks:

1. what histories or compositions can occur;
2. which distinctions matter to an observer or task;
3. what quotient, local, topological, or higher-rank structure those distinctions induce;
4. how that structure can be materialized as an economical **Presentation**;
5. what analysis becomes natural once a successful presentation is found.

The current research foundation has two complementary axes, governed by a
cross-cutting **Effective Analysis Principle**:

```text
horizontal:
    distinguishability
      -> exact quotient / topology
      -> entropy / metric / differential structure when justified
      -> task-sufficient presentations

vertical:
    free process
      -> semantic compression
      -> objectification
      -> new primitive / higher rank
      -> free higher-rank composition
      -> compositional rank lowering
```

The vertical axis is constrained by a strong semantic requirement: every legal higher-rank composition must admit a coherent interpretation back into lower-rank process semantics. Where topology or analysis exists, stronger continuity and analytic-closure questions can be asked across ranks.

The cross-cutting requirement is equally important: when a presentation is
claimed to support analysis, it must expose an effective symbolic and/or
numerical calculation path, with certificates, error or failure semantics, and
task-relative cost accounting.  This is not a claim that every process carries
a differential calculus.  A finite or purely semantic presentation may stop
earlier, but an abstract differential or integral object alone does not satisfy
the project's analysis standard.  See
[`docs/65-effective-analysis-principle.md`](docs/65-effective-analysis-principle.md).

AEG remains the first major model organism for this program because the arithmetic/hyperoperation tower naturally exhibits objectification and rank raising while also supporting function theory and analysis. The stronger conjecture that arithmetic-generated geometries provide universal or standard models is **not** assumed by the package.

## Status

Current release: **`process-geometry==0.0.4`**, a pre-alpha research preview.

Historical releases `0.0.1` and `0.0.2` were published on PyPI under the distribution name **`aeg-shakespeare`**. Starting with `0.0.3`, the distribution identity is **`process-geometry`**. Starting with `0.0.4`, the canonical Python import namespace is **`process_geometry`**.

The package is intended to be installable and useful as an experimental mathematical toolkit, but `0.0.x` APIs are not covered by backward-compatibility guarantees. Exact certificates, explicit numerical failure/error semantics where numerical behavior is claimed, conceptual layer separation, task-relative cost accounting, and research traceability take priority over interface stability during this phase.

See [`docs/47-release-0.0.4.md`](docs/47-release-0.0.4.md) for the current release contract, [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) for research-to-API promotion rules, and [`CHANGELOG.md`](CHANGELOG.md) for release summaries.

## Install

```bash
python -m pip install process-geometry
```

For development:

```bash
python -m pip install -e '.[dev]'
```

The canonical identities for `0.0.4` are:

```text
PyPI distribution:     process-geometry
GitHub repository:     mountain/process-geometry
Python import package: process_geometry
```

Use:

```python
import process_geometry as pg
```

The historical import path remains temporarily available as a compatibility alias:

```python
import aeg_shakespeare  # deprecated; aliases process_geometry
```

The alias preserves deep object identity: a class imported through `aeg_shakespeare.process.history` is the same Python object as the class imported through `process_geometry.process.history`. The compatibility package contains no second implementation tree and emits `DeprecationWarning` on import.

Do not install historical `aeg-shakespeare` distributions side-by-side with `process-geometry`: old distributions provide their own `aeg_shakespeare` package and can shadow the compatibility alias shipped by current Process Geometry releases.

Supported CPython versions: **3.10 through 3.14**.

SymPy is an algebra/discovery backend. Process Geometry keeps its own process-level semantics and does not define process equality by `sympy.simplify()`.

## Public API direction

The public surface is organized as a mathematical pipeline rather than a flat catalog of symbols:

```text
Process  ->  Presentation  ->  Discovery  ->  Analysis
```

### `process_geometry.process`

What the process **is**.

- `process.history` — literal ordered histories and caller-supplied semantics;
- `process.finite` — finite parameterized families, characters, actions, and additive process cocycles;
- `process.local` — local/infinitesimal realizations such as `ProcessSystem` and `ProcessFrame`.

### `process_geometry.presentation`

How process structure is **related, compressed under declared semantics, materialized, transformed, and compared**.

- `presentation.history` — explicit rewriting, bounded task-continuation signatures, and finite history geometry;
- `presentation.construction` — construction-history-preserving candidate primitive proposals;
- `presentation.constraints` — exact algebraic presentation constraints;
- `presentation.grammar` — generated finite process grammars;
- `presentation.relations` — exact process relations, factors, kernels, and decompositions;
- `presentation.morphism` — task-relative, certificate-carrying transformations between possibly heterogeneous presentations;
- `presentation.search` — budgets, presentation cost, Pareto filtering, and presentation search.

A candidate primitive is not called **objectified** merely because it has been proposed: the stronger foundation notion additionally requires a higher-rank compositional language with coherent rank-lowering semantics.

The first `PresentationMorphism` API is intentionally minimal: it records source, target, declared task semantics, a caller-defined certificate, and optional construction provenance. It does not yet define universal verification, composition, inverses, normal forms, or a category/groupoid structure.

### `process_geometry.discovery`

How alternative presentations, observers, and observable structures are **searched**.

The current discovery package contains bounded polynomial invariant discovery, structured observer proposals, algebraic observable-quotient construction, first-order observer-presentation selection, and explicit coefficient-language extension experiments. These are search procedures, not process ontology.

The canonical names distinguish algebraic observable quotients from task/process quotients: `ObservableAlgebraicQuotient`, `discover_first_order_observable_quotient`, and `search_first_order_observer_presentations`. Historical backend names remain aliases during the `0.0.x` transition.

### `process_geometry.analysis`

What analytic or geometric language a successful presentation **supports**.

- `analysis.module` — finite process-function modules;
- `analysis.am` — the Addition/Multiplication process calculus;
- `analysis.algebraic` — algebraic quotient profiles and Weierstrass calibration;
- `analysis.abelian` — lifted histories, Abelian integrals, cycle systems, periods, and normalized history quotients.

Analysis is an operational claim, not a decorative final layer.  Each concrete
analysis family should state its function/observable language, operator action,
closure or controlled-extension rule, evaluator, certificates, and the domain
of any numerical guarantee.  The current families satisfy different local
parts of that contract; they do not establish one universal process calculus.

A representative import therefore looks like:

```python
from process_geometry.process.history import ProcessWord
from process_geometry.presentation.history import TaskContinuationSignature
from process_geometry.presentation.grammar import discover_generated_presentation
from process_geometry.presentation.morphism import PresentationMorphism
from process_geometry.discovery import search_first_order_observer_presentations
from process_geometry.analysis.am import AMFunctionTheory
```

The package root is intentionally only a namespace router:

```python
import process_geometry as pg

pg.process
pg.presentation
pg.discovery
pg.analysis
```

Unsettled theory-to-code probes live outside that contract under
`process_geometry.experimental`.  This currently includes the exact finite
deterministic `FiniteTaskQuotient` and the local canonical-observer evidence
records `ConstraintCanonicalization`, `ObserverConnection`, and
`CanonicalDecomposition`.  The latter previously appeared under Presentation
and Analysis module paths; those paths are now 0.0.x compatibility shims rather
than declared namespace members.

Legacy root-level symbol imports from the early `0.0.x` research-preview surface remain available lazily and emit `DeprecationWarning`; they are no longer part of the declared public root surface. The separate `aeg_shakespeare` namespace is also deprecated and exists only as a migration alias. See [`docs/API.md`](docs/API.md) for the detailed map and migration notes.

## Why “Process Geometry”

The name is not shorthand for “put a manifold on a dynamical system.” The current foundation distinguishes several levels.

At the exact discrete level, future or task distinguishability can induce a continuation-stable quotient. Myhill–Nerode provides the canonical calibration: future-equivalence classes of a regular language are exactly the states of its unique minimal DFA.

Topology enters only when observer-relative neighborhoods admit coherent local refinement and are compatible with process evolution. It then supplies robustness, boundary, convergence, continuity, connectedness, compactness, quotient/covering/homotopy structure, and the substrate for topological entropy.

Across ranks, semantic compression may objectify a stable lower-rank process into a new primitive. That primitive can participate in a new free composition language, but the new language is grounded only if arbitrary legal composites admit **compositional rank lowering** back to lower-rank semantics.

This gives Process Geometry both a horizontal and a vertical structure: geometry of distinctions within a process level, and geometry of objectification and semantic interpretation across process levels.

Effective analysis is not a third ontology axis.  It is the admissibility
condition that prevents either axis from winning abstraction at the cost of
calculation: quotienting must not erase task-visible computational payload, and
rank raising must not count abbreviation as analytic progress unless the new
language remains executable, certifiable, and economical after lowering costs
are charged.

See:

- [`docs/42-process-geometry-from-distinguishability.md`](docs/42-process-geometry-from-distinguishability.md)
- [`docs/43-myhill-nerode-and-the-topological-threshold.md`](docs/43-myhill-nerode-and-the-topological-threshold.md)
- [`docs/44-objectification-semantic-compression-and-rank-lowering.md`](docs/44-objectification-semantic-compression-and-rank-lowering.md)
- [`docs/45-lineage-objectification-and-analytic-closure.md`](docs/45-lineage-objectification-and-analytic-closure.md)
- [`docs/48-foundation-naming-audit.md`](docs/48-foundation-naming-audit.md)
- [`docs/64-first-principles-and-api-boundary-audit.md`](docs/64-first-principles-and-api-boundary-audit.md)
- [`docs/65-effective-analysis-principle.md`](docs/65-effective-analysis-principle.md)

The naming audit is intentionally conservative: it reserves strong theory words such as **task quotient**, **jet**, **objectification**, **process rank**, and **rank lowering** until the corresponding semantics are actually implemented.

## Shakespeare and Sonnets

**Shakespeare** is retained as the repository's problem-driven research program, not as the software distribution identity.

`sonnet/` contains sustained investigations of difficult or open problems. A Sonnet may freely prototype problem-local mathematics and interfaces, but it does not standardize the public API. Reusable structures move through the governance lifecycle:

```text
Sonnet
  -> extraction candidate
  -> Experimental
  -> maturing
  -> Public API
```

The purpose is to let real problems force common structure without freezing the first successful local abstraction.

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

Process Geometry uses a **literate-programming** discipline. Mathematically substantial Python modules and tests should explain the mathematical pressure that created an abstraction before presenting its implementation.

```text
classical historical path:
    analytic difficulty -> special construction -> geometry/algebra

process-first reconstruction:
    primitive process -> history/constraint/invariant -> quotient geometry
    -> adequate function language -> classical formula as a shadow
```

The canonical pendulum calibration therefore begins from constrained position/velocity dynamics rather than from `theta`, `sin(theta)`, or a preselected elliptic function. Likewise, the A/M layer begins from **Addition and Multiplication** and their finite/noncommutative process relations before logarithms or familiar harmonic-analysis names are introduced.

A substantial test in `tests/classical/` or `tests/research/` is expected to be a complete mathematical vignette: question, primitive data, classical lineage, Process Geometry reconstruction, calibration statement, proof map, claim boundary, and bibliographic references.  If it claims a new analysis language or computational advantage, it must also state the symbolic/numerical baseline, applicable effective-analysis gates, units and tolerances, failure semantics, and cost boundary.

See:

- [`docs/09-literate-programming-and-mathematical-lineage.md`](docs/09-literate-programming-and-mathematical-lineage.md)
- [`docs/11-references-and-test-essays.md`](docs/11-references-and-test-essays.md)
- [`docs/REFERENCES.md`](docs/REFERENCES.md)

## Current research boundary

The current implementation supports a bounded loop from declared process structure to evaluated presentations, plus concrete routes from successful presentations toward process-adapted function theory and global geometry.

Recent calibrations have established several deliberately limited layers:

- finite families, scalar characters, family actions, and additive process cocycles live in the **process** layer;
- rewriting, bounded task-distinguishability signatures, construction histories, grammars, relations, task-relative presentation morphisms, and Pareto cost live in the **presentation** layer;
- invariant, observer, algebraic-observable, and language proposals live in **discovery**;
- A/M calculus, algebraic quotient profiles, Abelian integrals, lifted cycles, period matrices, and normalized history quotients live in **analysis**.

`PresentationMorphism` was promoted only after independent KdV, resistor-network, and braid/Markov calibrations forced different aspects of the same role: cross-presentation completeness, task-semantic rather than syntactic confluence, and transformations between presentation spaces of different dimensions. The public object remains only an evidence-bearing record; composition and a universal verification semantics are still outside the API.

The separation is intentional. Current foundation notes about generic `ProcessGeometry`, observer topology, objectification, rank lowering, and analytic closure are research programs, **not** newly promoted public classes. Under [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md), such structures must survive independent domains and red teams before entering the public API.

Physical and mathematical calibration problems do not define the package API. Pendulum, oscillator, Galilean mechanics, magnetic translations, KdV, resistor networks, braid/Markov systems, and Sonnets are probes of common machinery.

## Development and release checks

```bash
python -m pip install -e '.[dev]'
pytest
python -m build
python -m twine check dist/*
```

CI tests the same release gate on CPython 3.10 through 3.14, installs the built wheel into a fresh virtual environment, verifies `importlib.metadata.version("process-geometry")`, imports `process_geometry` from outside the repository source tree, and then verifies the temporary `aeg_shakespeare` alias preserves representative object identity. See [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

The evolving mathematical story is indexed in [`docs/README.md`](docs/README.md).

## License and citation

Process Geometry is dedicated to the **public domain** using the Unlicense public-domain dedication text in [`LICENSE`](LICENSE). The intent is unrestricted use, modification, publication, redistribution, and reuse of both the software and its accompanying mathematical exposition.

Scholarly attribution is separate from software licensing. Mathematical and historical sources are cited in the literate tests and [`docs/REFERENCES.md`](docs/REFERENCES.md); software citation metadata is provided in [`CITATION.cff`](CITATION.cff).

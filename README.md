# AEG Shakespeare

**Shakespeare** is a process-representation library for building and searching compact process presentations.

It is not primarily an ODE solver and it does not treat eigenvectors, Fourier modes, or a particular coordinate system as the starting ontology. The public library exposes problem-independent objects for ordered process histories, explicit history relations, finite task quotients, finite history geometry, operation-generated primitive proposals, algebraic constraints, bounded search, exact relation discovery, finite grammar generation, representation costs, Pareto presentation search, and optional process-generated function theories.

> Process ODE describes computation in a representation; Shakespeare provides machinery for searching for representations in which that computation is cheaper to express.

## Status

Current version: **0.0.1**, the first **pre-alpha research preview**.

The package is intended to be installable and useful as an experimental mathematical toolkit, but `0.0.x` APIs are not yet covered by backward-compatibility guarantees. Exact certificates, explicit failure modes, and conceptual layer separation take priority over interface stability during this phase.

See [`docs/10-release-0.0.1.md`](docs/10-release-0.0.1.md) for the release contract and [`CHANGELOG.md`](CHANGELOG.md) for the release summary.

## Install

After the `0.0.1` release is published to PyPI:

```bash
python -m pip install aeg-shakespeare
```

For development from the repository:

```bash
python -m pip install -e '.[dev]'
```

PyPI distribution: `aeg-shakespeare`  
Python package: `aeg_shakespeare`

SymPy is an algebra/discovery backend. Shakespeare keeps its own process-level semantics and does not define process equality by `sympy.simplify()`.

## Quick start

The smallest runnable examples are deliberately problem-independent:

```bash
python examples/quickstart.py
python examples/constraint_quickstart.py
python examples/grammar_quickstart.py
```

They demonstrate, respectively:

1. literal ordered histories, explicit rewriting, and A/M (Addition/Multiplication) resonance;
2. exact equality modulo algebraic constraints;
3. generated process grammars and return-relation discovery from a seed.

The examples are entry points, not mathematical proofs. Complete classical and research arguments live under `tests/classical/` and `tests/research/` as cited executable essays.

## Reading the source

Shakespeare uses a **literate-programming** discipline. Mathematically substantial Python modules should explain the mathematical pressure that created an abstraction before presenting its implementation. In particular, source docstrings and classical tests should preserve the historical and conceptual reversal that the project is investigating:

```text
classical historical path:
    analytic difficulty -> special construction -> geometry/algebra

Shakespeare reconstruction:
    primitive process -> history/constraint/invariant -> quotient geometry
    -> adequate function language -> classical formula as a shadow
```

This means, for example, that the canonical pendulum calibration begins from constrained position/velocity dynamics rather than from `theta`, `sin(theta)`, or a preselected elliptic function. Likewise, the A/M layer begins from **Addition and Multiplication** and their finite/noncommutative process relations before logarithms or other familiar function names are introduced.

A substantial test in `tests/classical/` or `tests/research/` is expected to be a **complete mathematical vignette**: question, primitive data, classical lineage, Shakespeare reconstruction, precise calibration statement, proof map, claim boundary, and rigorous bibliographic references. Its Python assertions are the executable checking layer of that essay. Public-domain licensing does not remove scholarly attribution obligations.

See:

- [`docs/09-literate-programming-and-mathematical-lineage.md`](docs/09-literate-programming-and-mathematical-lineage.md)
- [`docs/11-references-and-test-essays.md`](docs/11-references-and-test-essays.md)
- [`docs/REFERENCES.md`](docs/REFERENCES.md)

## Public API direction

The library core is intentionally problem-independent. Current public building blocks include:

- `ProcessWord` — an uninterpreted ordered finite process history;
- `WordRewriteRule`, `rewrite_once`, `normalize_word` — explicit oriented relations and certified normalization traces for noncommutative finite histories; no commutativity is assumed unless supplied as a relation;
- `enumerate_process_words`, `process_jet_signature`, `history_process_jet_signature`, `histories_task_equivalent` — finite future-response signatures and bounded task congruence for deciding when distinct histories may be safely merged for a declared task;
- `history_depth`, `boundary_profile`, `BoundaryProfile` — finite history geometry: process depth as the radial axis and prefix-frontier width/information as boundary observables, with an optional caller-supplied exact/task quotient key;
- `huffman_prefix_code`, `PrefixCode`, `PrefixCodeMetrics` — one optional prefix-representation strategy that redistributes code depth after the task-relevant symbol set and weights have been fixed;
- `SymbolicOperation`, `PrimitiveConstruction`, `PrimitiveProposal`, `generate_primitive_proposals` — bounded primitive proposal generation that retains construction trees and costs instead of identifying proposals by final symbolic value;
- `AlgebraicConstraintSet`, `constraint_prolongation` — exact polynomial quotient reduction and repeated process preservation of algebraic constraints;
- `ProcessFrame` — a generic symbolic frame of multiple ordered process generators, without assuming a universal Lie algebra or commutativity;
- `ProcessFunctionModule` — a generic finite process-function module with explicit action tables and exact frame certificates;
- `AMFunctionTheory` — the first concrete optional function theory, where **A means Addition and M means Multiplication**; it exposes their finite relation, `[A,M]=A`, the power-weight lattice, resonant primitives, PBW reordering, and ordered A/M path flow;
- `hyperelliptic_profile` / `HyperellipticProfile` — a small algebraic-quotient profiler for process reductions of the form `y^2=P(x)`, recording degree, discriminant, generic genus, and degeneration locus without pretending to be a general algebraic-geometry engine;
- `interpret_history` — attach caller-defined semantics to a history;
- `ProcessSystem` — a derivation-style symbolic backend for a local process generator;
- `SearchBudget` — explicit finite limits for local representation search;
- `discover_generated_grammar` — grow the exact process span generated by caller-supplied seed expressions and return escaped residuals when a budget prevents closure;
- `discover_generated_presentation` — from seeds alone, discover a finite closed grammar, its relation factors, reusable primitives, and seed decoder when possible;
- `discover_return_relation` — discover exact recurrences among process iterates;
- `discover_operator_relation` — discover the shortest grammar-wide polynomial relation of a finite action;
- `factor_process_relation` — factor a discovered relation while retaining repeated process depth;
- `discover_relation_kernel` — find primitives satisfying an arbitrary declared process relation in a finite grammar;
- `discover_relation_decomposition` — jointly discover relation factors and their primitive subgrammars without a caller-supplied relation template;
- `coefficient_vector` / `decompose` — move exactly between arbitrary independent polynomial grammars, including discovered composite primitives;
- `PresentationCost`, `PresentationCandidate`, `pareto_frontier` — explicit multi-axis representation costs and generic task-sufficient Pareto filtering;
- `search_exact_reconstruction_presentations` — evaluate alternative seed presentations for exact target reconstruction without imposing a universal scalar objective;
- `search_primitive_proposals` — feed construction-history-preserving primitive proposals into the common grammar/relation/decoder/Pareto pipeline;
- `discover_krylov_relation` — a matrix backend showing how linear recurrence structure can be recovered from process histories before spectral interpretation.

The physical and mathematical calibration problems do **not** define the package API. Oscillator, Duffing, affine add/multiply, pendulum, and related systems belong in tests as probes of the common machinery.

## Current research boundary

Shakespeare now has a first end-to-end bounded loop from declared operations to evaluated presentations, plus the first concrete process-generated function-theory branch and the first first-principles constrained-mechanics calibration.

At the literal-history layer, `ProcessWord` remains ordered history and oriented relations are applied explicitly. `normalize_word` keeps the complete rewrite trace and returns cycles or step-budget exhaustion as certificates rather than assuming termination.

At the task layer, a history is not merged merely because its current observation agrees with another one. Finite process-jet signatures compare every allowed continuation through a declared depth; a continuation that exposes hidden state splits the proposed task quotient.

At the history-geometry layer, the remaining distinguishable histories form a finite prefix tree. Shakespeare can measure root-to-node process depth and level/frontier widths, and can optionally apply a Huffman prefix strategy once a task-relevant boundary and usage measure are supplied. Huffman is a representation strategy, not the definition of process equality or primitive discovery.

At the primitive-construction layer, caller-declared operations generate bounded construction trees. Two trees that evaluate to the same SymPy expression remain separate proposals unless the caller explicitly declares a construction symmetry such as commutativity. Construction depth and cost therefore survive objectification.

At the symbolic local-process layer, each proposed seed can grow an exact process grammar. If closure succeeds, Shakespeare discovers the grammar-wide return relation, factors it, constructs primitive subgrammars, and returns exact target decoders. If nonlinear growth escapes the grammar, residual expressions remain visible rather than being projected away.

At the constraint/quotient layer, polynomial relations can be maintained and reduced exactly. The canonical pendulum calibration starts from planar position/velocity plus a rigid-rod relation and unresolved radial force—without `theta`, `sin`, or `cos`. Constraint prolongation determines the force, energy reduction yields a quotient `Y^2=2(E-U)(1-U^2)`, and the generic quotient is detected as genus one with degenerations at `E=±1`.

At the search layer, the resulting candidates are filtered by task sufficiency and compared by explicit multi-axis cost. The Pareto frontier can therefore preserve a trade-off between construction cost, grammar width, process depth, relation complexity, and decoding rather than collapsing them to one score.

At the optional function-theory layer, Addition/Multiplication (A/M) supplies the first concrete arithmetic calculus. It is intentionally downstream of the generic process machinery. Its resonance structure forces logarithmic/Jordan-type extensions, while the pendulum and even-power oscillator calibrations demonstrate another route in which constrained or invariant processes force algebraic curves of different genera. Shakespeare therefore does not assume that every problem should reduce to A/M.

The next threshold is **adaptive proposal priority/objectification** together with a systematic classical calibration suite. Repeated history subtrees, relation compression, task signatures, boundary usage measures, algebraic quotient geometry, and function-theory closure should help determine which constructions deserve to become new primitives and which function language is adequate for the task.

## Development and release checks

```bash
python -m pip install -e '.[dev]'
pytest
python -m build
python -m twine check dist/*
```

CI additionally installs the built wheel into a fresh virtual environment and imports the package from outside the repository source tree. See [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

The evolving mathematical story is indexed in [`docs/README.md`](docs/README.md).

## License and citation

Shakespeare is dedicated to the **public domain** using the Unlicense public-domain dedication text in [`LICENSE`](LICENSE). The intent is unrestricted use, modification, publication, redistribution, and reuse of both the software and its accompanying mathematical exposition.

Scholarly attribution is separate from software licensing. Mathematical and historical sources are cited in the literate tests and [`docs/REFERENCES.md`](docs/REFERENCES.md); software citation metadata is provided in [`CITATION.cff`](CITATION.cff).

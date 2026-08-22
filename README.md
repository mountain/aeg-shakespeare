# AEG Shakespeare

**Shakespeare** is a process-representation library for building and searching compact process presentations.

It is not primarily an ODE solver and it does not treat eigenvectors, Fourier modes, or a particular coordinate system as the starting ontology. The public library exposes problem-independent objects for ordered process histories, bounded search, exact relation discovery, finite grammar analysis, representation costs, and symbolic backends.

> Process ODE describes computation in a representation; Shakespeare provides machinery for searching for representations in which that computation is cheaper to express.

## Package

PyPI distribution:

```text
aeg-shakespeare
```

Python package:

```python
import aeg_shakespeare
```

Current version: **0.0.1**.

SymPy is an algebra/discovery backend. Shakespeare keeps its own process-level semantics and does not define process equality by `sympy.simplify()`.

## Public API direction

The library core is intentionally problem-independent. Current public building blocks include:

- `ProcessWord` — an uninterpreted ordered finite process history;
- `interpret_history` — attach caller-defined semantics to a history;
- `ProcessSystem` — a derivation-style symbolic backend for a local process generator;
- `SearchBudget` — explicit finite limits for local representation search;
- `discover_return_relation` — discover exact recurrences among process iterates;
- `discover_operator_relation` — discover the shortest grammar-wide polynomial relation of a finite action;
- `factor_process_relation` — factor a discovered relation while retaining repeated process depth;
- `discover_relation_kernel` — find primitives satisfying an arbitrary declared process relation in a finite grammar;
- `discover_relation_decomposition` — jointly discover relation factors and their primitive subgrammars without a caller-supplied relation template;
- `coefficient_vector` / `decompose` — move exactly between arbitrary independent polynomial grammars, including discovered composite primitives;
- `PresentationCost` — explicit multi-axis representation cost with optional scalarization;
- `discover_krylov_relation` — a matrix backend showing how linear recurrence structure can be recovered from process histories before spectral interpretation.

The physical and mathematical calibration problems do **not** define the package API. Oscillator, Duffing, affine add/multiply, and related systems live in the test suite as probes of the common machinery.

## Current research boundary

For a caller-supplied finite grammar that is exactly closed under a process action, Shakespeare can now discover a shortest grammar-wide return relation and factor it into smaller process-relation components. The caller no longer has to propose templates such as `D^2 + k^2` in advance.

This is still a bounded finite-grammar result: Shakespeare does **not** yet discover the ambient grammar itself. The next threshold is a costed search that proposes new generators/grammars and then reuses the same relation machinery to decide whether the new presentation is cheaper.

## Development

```bash
python -m pip install -e '.[dev]'
pytest
python -m build
python -m twine check dist/*
```

See [`docs/00-process-presentation-v0.1.md`](docs/00-process-presentation-v0.1.md) for the current computational formulation.

## License

MIT.

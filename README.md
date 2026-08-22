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
- `discover_relation_kernel` — find primitives satisfying an arbitrary declared process relation in a finite grammar;
- `decompose` — express an object in a discovered primitive grammar;
- `PresentationCost` — explicit multi-axis representation cost with optional scalarization;
- `discover_krylov_relation` — a matrix backend showing how linear recurrence structure can be recovered from process histories before spectral interpretation.

The physical and mathematical calibration problems do **not** define the package API. Oscillator, Duffing, affine add/multiply, and related systems live in the test suite as probes of the common machinery.

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

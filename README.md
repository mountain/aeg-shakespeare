# AEG Shakespeare

**Shakespeare** is an experimental process-representation discovery engine.

It is not primarily an ODE solver and it does not treat eigenvectors, Fourier modes, or a particular coordinate system as the starting ontology. The research goal is to start from assignments, primitive operations/processes, ordered histories, relations, and a task, then search for a smaller process presentation in which the same computation is cheaper to express.

> Process ODE describes computation in a representation; Shakespeare searches for a representation in which that computation is cheap.

## Status

Very early research prototype. The current code implements exact, bounded calibration experiments only.

## Package

The intended PyPI distribution name is **`aeg-shakespeare`** and the Python import package is:

```python
import aeg_shakespeare
```

SymPy is an algebra/discovery backend. Shakespeare keeps its own process-level semantics and does not define process equality by `sympy.simplify()`.

## First benchmarks

- **P0 Add/Multiply:** finite affine-history normalization.
- **P1 Linear/Krylov:** discover a shortest return relation before any eigen/Jordan representation is requested.
- **P2 Oscillator:** discover `D^2 x + x = 0` from the action table.
- **P3 Duffing:** discover compact degree-three return sectors without preloading Fourier/eigen language.

Run:

```bash
python -m pip install -e '.[dev]'
pytest
python examples/benchmarks.py
```

See [`docs/00-process-presentation-v0.1.md`](docs/00-process-presentation-v0.1.md) for the current computational formulation.

## License

MIT.

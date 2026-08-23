# Release 0.0.3 — Process Geometry identity

**Status:** release contract for the first PyPI release under the `process-geometry` distribution name.

## 1. Release purpose

Version `0.0.3` changes the software distribution identity from **AEG Shakespeare** to **Process Geometry** after the framework's scope became broader than arithmetic-process calibration or the Shakespeare research program.

This release intentionally separates three identities:

```text
PyPI distribution:     process-geometry
GitHub repository:     mountain/process-geometry
Python import package: aeg_shakespeare   (temporary 0.0.x compatibility namespace)
```

The import namespace is not renamed in this release. Distribution migration and source/import migration are separate engineering changes so that each can be tested and reversed independently.

## 2. Historical distribution boundary

Versions `0.0.1` and `0.0.2` were published on PyPI as `aeg-shakespeare`.

Starting with `0.0.3`, the release target is:

```bash
python -m pip install process-geometry
```

Because `process-geometry==0.0.3` and historical `aeg-shakespeare` releases currently provide the same `aeg_shakespeare` import tree, they should not be installed side-by-side. Existing development environments should uninstall the historical distribution before installing the new one.

The old PyPI distribution is historical; it is not the release target for `0.0.3` or later.

## 3. Public API compatibility

The semantic public pipeline remains:

```text
Process -> Presentation -> Discovery -> Analysis
```

Representative imports remain valid in `0.0.3`:

```python
from aeg_shakespeare.process.history import ProcessWord
from aeg_shakespeare.presentation.morphism import PresentationMorphism
from aeg_shakespeare.discovery import discover_polynomial_invariants
from aeg_shakespeare.analysis.am import AMFunctionTheory
```

This compatibility is deliberate and temporary. A future import-namespace migration must use the governance process and provide an explicit compatibility/migration plan rather than being folded into the distribution rename.

## 4. Why the new name is now justified

The project foundation now has two interacting axes.

### Horizontal: distinguishability geometry

At a fixed process rank:

```text
process/history
  -> observer/task distinguishability
  -> exact quotient or local topology
  -> entropy / metric / differential structure when justified
  -> task-sufficient presentation and analysis
```

Myhill–Nerode supplies the first exact discrete calibration of `future distinguishability -> minimal presentation`; topology enters only after observer neighborhoods satisfy appropriate locality/refinement conditions and are compatible with process evolution.

### Vertical: objectification and rank change

Across process ranks:

```text
free lower-rank process
  -> task-relative semantic compression
  -> objectification
  -> new primitive
  -> free higher-rank composition
  -> compositional rank lowering
```

A higher-rank language is semantically legitimate only if every legal higher-rank composition admits a coherent lower-rank interpretation. Stronger topological and analytic closure conditions can then be studied when the relevant structures exist.

AEG remains the first major model organism for this program because its arithmetic/hyperoperation tower exhibits objectification/rank raising while naturally supporting function theory and analysis. Arithmetic Universality remains a separate conjecture, not a package-wide assumption.

## 5. Shakespeare and Sonnet after the rename

**Shakespeare** remains the problem-driven research program inside the repository rather than the software distribution identity.

`sonnet/` remains the open research workspace in which difficult problems may generate provisional structures. Reusable structures must pass through the repository's Experimental/governance lifecycle before entering the public API.

## 6. Release gates

Before tagging `v0.0.3`:

1. all CPython 3.10–3.14 CI jobs pass;
2. wheel/sdist metadata identify `process-geometry==0.0.3`;
3. `twine check dist/*` passes;
4. the wheel installs outside the source tree and `importlib.metadata.version("process-geometry")` equals `aeg_shakespeare.__version__`;
5. representative public imports succeed from the built wheel;
6. the `process-geometry` PyPI pending Trusted Publisher is configured for owner `mountain`, repository `process-geometry`, workflow `publish.yml`, environment `pypi`;
7. the historical `aeg-shakespeare` distribution is absent from the smoke-test environment.

## 7. Non-goals

Release `0.0.3` does **not**:

- rename `src/aeg_shakespeare`;
- introduce a public `ProcessGeometry` class;
- promote objectification/rank-lowering research objects into the public API;
- claim Arithmetic Universality;
- make `0.0.x` APIs backward-compatible.

The release changes project identity while preserving the current semantic API boundary.
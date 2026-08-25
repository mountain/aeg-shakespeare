# Release checklist

For a `0.0.x` release candidate:

- [ ] package version and public `__version__` agree;
- [ ] PyPI distribution metadata names `process-geometry` and points to `https://github.com/mountain/process-geometry`;
- [ ] Python 3.10, 3.11, 3.12, 3.13, and 3.14 CI pass;
- [ ] sdist and wheel build successfully;
- [ ] `twine check dist/*` passes;
- [ ] the built wheel installs in a fresh environment and imports outside the source tree;
- [ ] representative semantic public entry points pass smoke tests through the canonical `process_geometry` namespace;
- [ ] every released analysis/computation API identifies its claim mode (`exact-symbolic`, `certified-approximate`, `numerical`, `search-only`, or `record-only`) and does not inherit stronger semantics from its name;
- [ ] exact-symbolic public claims have backend-independent semantic tests or certificates rather than relying only on one simplifier;
- [ ] numerical public claims state domain, units/scale, tolerance or error semantics, singular/nonconvergence behavior, and pass an independent-reference, invariant, exact-limit, or convergence check;
- [ ] released efficiency claims name a workload and baseline and separate discovery/compilation cost from repeated evaluation, including storage and decoder/lowering cost where applicable;
- [ ] public quickstart examples use `process_geometry` and run successfully;
- [ ] the canonical implementation tree `src/process_geometry/**` has no dependency on `aeg_shakespeare`;
- [ ] the temporary `aeg_shakespeare` compatibility namespace imports from the built wheel, emits its deprecation signal, and preserves representative deep object identity with `process_geometry`;
- [ ] historical `aeg-shakespeare` distributions are not installed alongside the release smoke environment;
- [ ] new substantial `tests/classical/` and `tests/research/` files are complete mathematical essays with rigorous references;
- [ ] README and release note state that `0.0.x` APIs are experimental;
- [ ] PyPI Trusted Publisher is configured with owner `mountain`, repository `process-geometry`, workflow `publish.yml`, and environment `pypi`;
- [ ] no package credentials or API tokens are stored in the repository.

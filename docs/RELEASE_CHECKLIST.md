# Release checklist

For a `0.0.x` release candidate:

- [ ] package version and public `__version__` agree;
- [ ] PyPI distribution metadata names `process-geometry` and points to `https://github.com/mountain/process-geometry`;
- [ ] Python 3.10, 3.11, 3.12, 3.13, and 3.14 CI pass;
- [ ] sdist and wheel build successfully;
- [ ] `twine check dist/*` passes;
- [ ] the built wheel installs in a fresh environment and imports outside the source tree;
- [ ] representative semantic public entry points pass smoke tests without relying on legacy root compatibility;
- [ ] quickstart examples run against the public API;
- [ ] new substantial `tests/classical/` and `tests/research/` files are complete mathematical essays with rigorous references;
- [ ] README and release note state that `0.0.x` APIs are experimental;
- [ ] for `0.0.3`, the transitional `aeg_shakespeare` import namespace is tested from the `process-geometry` wheel and the historical `aeg-shakespeare` distribution is not installed alongside it;
- [ ] PyPI Trusted Publisher (or pending publisher before the first `process-geometry` release) is configured with owner `mountain`, repository `process-geometry`, workflow `publish.yml`, and environment `pypi`;
- [ ] no package credentials or API tokens are stored in the repository.

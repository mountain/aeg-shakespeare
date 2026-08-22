# Release checklist

For a `0.0.x` release candidate:

- [ ] package version and public `__version__` agree;
- [ ] Python 3.10, 3.11, and 3.12 CI pass;
- [ ] sdist and wheel build successfully;
- [ ] `twine check dist/*` passes;
- [ ] the built wheel installs in a fresh environment and imports outside the source tree;
- [ ] representative public entry points pass smoke tests;
- [ ] quickstart examples run against the public API;
- [ ] new substantial `tests/classical/` and `tests/research/` files are complete mathematical essays with rigorous references;
- [ ] README and release note state that `0.0.x` APIs are experimental;
- [ ] PyPI Trusted Publisher is configured before pushing the release tag;
- [ ] no package credentials or API tokens are stored in the repository.

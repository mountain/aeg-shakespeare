# Release readiness and mathematical essays

For AEG Shakespeare, release readiness has two independent axes:

- **software integrity** — installation, tests, package build, wheel smoke test;
- **mathematical auditability** — substantial classical/research tests are complete cited essays.

A release can be mechanically installable and still be mathematically under-documented.  The `0.0.1` release candidate should therefore be judged against both axes.

Before tagging `v0.0.1`, the current substantial classical/research calibrations should be reviewed against `docs/14-mathematical-essay-quality-gate.md`.  Missing references or an incomplete proof narrative are release blockers for those tests even if their assertions already pass.

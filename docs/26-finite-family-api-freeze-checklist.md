# Finite-family API freeze checklist

This checklist records the gate for the first `ProcessFamily` / `ProcessCharacter` /
`FamilyAction` API slice.

The slice may be merged only if all of the following remain true:

1. Translation I uses `ProcessFamily` + `ProcessCharacter` without a Fourier API.
2. Dilation I reuses the same API without adding a multiplicative-family subclass.
3. A/M I adds only `FamilyAction` plus character transport/obstruction; it does not add a general representation hierarchy.
4. Galilean I handles a two-dimensional target parameter space and shear action without changing the API.
5. The Galilean mass-dependent term remains an explicit unresolved boundary; no cocycle/central-extension object is introduced yet.
6. Public exports and wheel smoke tests include the finite-family entry points.
7. The full existing test suite still passes on all supported Python versions.

If a later vignette needs operator-valued responses or a central residual, that
pressure should be handled in a separate API increment rather than folded into
this freeze retroactively.

# Analytic-germ adapter workstream

This directory is an isolated continuation of the S0/S1 observer-driven scale
compiler experiment.  It does **not** modify the frozen compiler, its manifest,
or its held-out evidence.  The adapter consumes a declared elementary phase,
builds a bounded multivariate Taylor germ at an explicit centre, selects the
smallest total-degree prefix that can determine all requested scales, and then
hands that exact polynomial to the frozen monomial-balance solver.

The strongest implemented claim is deliberately narrow:

> For an explicitly supplied elementary analytic phase, a bounded formal-germ
> adapter can expose a rank-completing principal polynomial and produce an
> exact, replayable scale certificate or a typed refusal.

It is not a general special-function-to-integral-representation compiler and
it does not claim a uniform asymptotic theorem. One versioned exact-shape
registry entry exists solely to exercise the required raw pipeline.

## Oracle boundary

The generic discovery path accepts elementary analytic functions such as
`sin`, `cos`, `exp`, and `log`. It rejects `besselj`, `airyai`, and every other
special or undefined function with `special-function-oracle-required`.

`representation_bridge.py` is a physically separate, versioned registry. Its
sole entry recognizes exactly `besselj(N, N*z)` for positive integer `N` and
real `z`, records the provenance and domain of the classical integer-order
cosine integral, and emits its oscillatory phase

```text
N * (z*sin(theta) - theta)
```

The registry contains no expected exponent or named local normal form. This
translation is registered mathematical knowledge and receives no independent
discovery credit. Noninteger order, the wrong argument shape, and unregistered
`bessely` all fail with typed states.

Fixed-scale symbols are forbidden inside analytic-function arguments. Thus
`sin(N*x)` returns `fixed-scale-inside-analytic-function` instead of receiving
an unsafe Taylor-tail certificate.

## Selection rule

After shifting every declared coordinate to its centre, the adapter introduces
one bookkeeping variable `epsilon`, substitutes every local coordinate by
`epsilon * coordinate`, and asks SymPy for a finite series in `epsilon`.  This
gives an exact total-degree polynomial germ.

Monomials are ordered by total local degree.  The selected germ is the first
complete degree prefix whose exponent matrix has full column rank and whose
exact balance equations are consistent.  Known higher-degree terms must be
strictly below the target order under the inferred chart.  The unseen Taylor
tail receives a conservative formal order bound; no analytic norm bound is
claimed.

If the first rank-completing prefix is inconsistent but two admissible
full-rank subsets induce different charts, the adapter returns
`ambiguous-germ`.  It never chooses one by an undeclared heuristic.

## Bessel transition result

At `(theta, z) = (0, 1)`, with local detuning `delta = z - 1`, the raw phase

```text
N * (z*sin(theta) - theta)
```

produces the principal germ

```text
N * (delta*theta - theta**3/6)
```

and the unchanged exact solver derives

```text
scale(theta) = -1/3
scale(delta) = -2/3.
```

The known degree-four and degree-five terms are both below the target order.
The phase is classified structurally as `degenerate-order-3`; the adapter does
not attach a special-function name.

## Run

From this directory:

```bash
python -m unittest discover -s tests -v
```

The tests add the sibling frozen prototype to `sys.path` only for this isolated
workstream.  Integration should later place the adapter beside the prototype
without changing frozen files.

## Boundaries and risks

- The generic adapter input is a phase; the raw registry currently recognizes
  only one exact integer-order Bessel shape.
- Taylor certification is formal; a uniform contour/error theorem remains
  open.
- Total-degree prefix selection is deterministic but not invariant under every
  nonlinear reparameterization.
- Only polynomial dependence on the declared large/fixed-scale symbols is
  accepted after germ expansion.
- Competing Newton faces are refused rather than ranked.
- The stable Rust boundary remains the exact balance/certificate kernel; this
  changing symbolic adapter belongs in Python/SymPy.

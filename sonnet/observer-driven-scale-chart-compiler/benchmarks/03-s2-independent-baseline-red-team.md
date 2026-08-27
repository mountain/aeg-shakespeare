# S2 independent baseline and red-team report

**Date:** 2026-08-27  
**Frozen gate:** commit
`db9898888402d7be8bbd7458c7e6b7d86d011497`  
**Role:** independent evaluator/red team; no compiler implementation changes

## Verdict first

The baseline evidence and independent replay support a **NARROW** disposition.
The S2 raw-to-local-certificate pipeline passes, but only through the permitted
versioned representation registry.

1. Stock SymPy 1.14.0 does not discover a coupled turning chart from the frozen
   raw input `besselj(N, N*z)`.
2. SymPy does verify the phase germ after an integral representation and phase
   extraction are supplied, and it verifies the normalized cubic phase after
   both scale exponents are additionally supplied. These are useful verifier
   capabilities but receive zero discovery credit.
3. No executable Wolfram kernel or authenticated Wolfram Cloud path is
   available in this environment. Official documentation describes strong
   asymptotic-scale, special-function, stationary-phase, steepest-descent, WKB,
   and boundary-layer capabilities, but documentation is not execution
   evidence for this exact coupled turning-point task.
4. The frozen gate itself assigns **NARROW** when the successful pipeline
   depends on a representation registry. The permitted Bessel bridge is such a
   registry. In addition, the unresolved Wolfram same-information comparison
   blocks an independent comparative-novelty claim.

Independent black-box replay confirms that the implementation recognizes the
raw Bessel expression, selects its domain-valid registry entry, constructs a
germ, chooses the Newton face, derives both rational scales, and replays the
certificate. It fixes the claim at:

> a bounded raw-special-function-to-certified-chart pipeline with a versioned
> representation registry,

not a general asymptotic compiler or a demonstrated capability beyond every
major CAS.

## 1. Frozen oracle firewall

The public S2 gate was frozen before implementation. This workstream did not
change it. The evaluator receives the expected scales, while the discoverer
may receive only:

```text
besselj(N, N*z)
N positive integer, N -> +infinity
z real and local to 1
versioned representation registry with provenance and domain obligations
```

The representation registry may contain an integral identity, its domain, the
integration variable, and the phase-extraction rule. It may not contain the
\(-1/3,-2/3\) scale pair, an Airy lookup answer, or a Bessel-specific branch in
the generic germ solver.

The registered identity is independently supported by
[NIST DLMF 10.9.2](https://dlmf.nist.gov/10.9#E2): for integer order it gives
the cosine integral with phase \(z\sin\theta-n\theta\). DLMF 10.9.6 separately
shows the extra term present at general noninteger order, which is why
integrality is a real domain obligation rather than incidental metadata.

`s2-red-team-contract.json` makes the independent controls exact:

- non-Bessel cubic germ
  \[
  N(2s^3+5\delta s+7s^4),
  \]
  where the quartic term must remain a residual;
- quartic two-parameter cusp
  \[
  N(t^4/4+pt^2/2-qt);
  \]
- unsupported `bessely(N,N*z)`, which must not reuse the Bessel-J registry
  entry;
- `besselj(nu,nu*z)` without an integrality assumption, which must reject the
  integer-order oscillatory representation unless an independently valid
  noninteger bridge is selected.

The last control matters mathematically. For noninteger order, the elementary
integer-order oscillatory integral is not the complete general representation.
A registry that silently drops the correction would appear to discover the
right scale while starting from a false identity.

## 2. SymPy 1.14.0 execution

Environment:

```text
Python 3.12.13
SymPy 1.14.0
Linux x86_64
```

| Probe | Information supplied | Observed result | Discovery credit |
| --- | --- | --- | --- |
| `series(besselj(N,N*z),N,oo,2)` | raw input | `NotImplementedError`: multivariate MRV set computation is not implemented | no |
| `limit(besselj(N,N*z),N,oo)` | raw input | same MRV error | no |
| `.aseries(N,n=2)` | raw input | same MRV error | no |
| `.rewrite(Integral)` | raw input | unchanged `besselj(N,N*z)` | no |
| local series at \(z=1\) | raw input | Taylor coefficients remain \(J_N(N),J_{N\pm1}(N),J_{N\pm2}(N)\); no coupled scale | no |
| direct Bessel series after both scale substitutions | two chart exponents | `PoleError`: expansion around \([\infty,\infty]\) not implemented | no |
| Taylor series of \(N(z\sin\theta-\theta)\) | representation and phase supplied | exact cubic/quintic germ | verification only |
| series after representation, phase, and chart are supplied | four semantic hints | exact normalized phase and first residual | verification only |

The normalized verification row returned

\[
\xi u-\frac{u^3}{6}
+\epsilon^2\left(\frac{u^5}{120}-\frac{\xi u^3}{6}\right)
+O(\epsilon^4).
\]

This is valuable because SymPy can serve as an independent exact certificate
replayer downstream. It does not show that SymPy selected the representation,
the leading Newton face, or either scale.

The official SymPy documentation states that other symbols are treated as
constants and that multivariate limits are not supported. It also describes
Gruntz as choosing an MRV set and one inferred small variable. This matches the
observed boundary: a fixed-\(z\) asymptotic operation is not the uniform
\(z\)-local task required by S2.

Primary source:
[SymPy 1.14 series and Gruntz documentation](https://docs.sympy.org/latest/modules/series/series.html).

## 3. Wolfram execution boundary

The environment audit found:

```text
wolframscript       absent
WolframKernel       absent
math                absent
wolframclient       not installed
Wolfram environment/credential variables  absent
authenticated cloud path                   not detected
```

Consequently the exact S2 input was not executed. No public documentation page
or manually written Airy formula is counted as an executable Wolfram result.

The unresolved executable matrix is:

```wolfram
Asymptotic[
  BesselJ[n, n z],
  n -> Infinity,
  Assumptions -> Element[n, Integers] && n > 0 && Element[z, Reals]
]
```

This is the only raw-special-function row. Its interface still does not
explicitly express the task phrase “uniform near \(z=1\),” so the output must
be inspected for whether it actually supplies a uniform turning-point chart or
only a fixed-\(z\) expansion.

```wolfram
Asymptotic[
  BesselJ[n, n (1 + xi n^(-2/3))],
  n -> Infinity,
  Assumptions -> Element[n, Integers] && n > 0 && Element[xi, Reals]
]
```

This supplies the expected turning scale and is therefore a verification row.

```wolfram
AsymptoticIntegrate[
  Cos[n (theta - z Sin[theta])],
  {theta, 0, Pi},
  n -> Infinity,
  Assumptions -> Element[n, Integers] && n > 0 && Element[z, Reals]
]/Pi
```

This supplies an integral representation and is a
representation-supplied row, not raw-special-function discovery.

Wolfram's official documentation says that `Asymptotic` automatically
infers asymptotic scales and supports special functions; its public Bessel
example is fixed-order \(J_2(x)\), not the coupled large-order
\(J_n(nz)\) turning regime. `AsymptoticIntegrate` explicitly covers
stationary phase and steepest descent, while `AsymptoticDSolveValue`
explicitly covers WKB, boundary layers, and singular perturbations. These
statements make Wolfram the strongest unresolved baseline, not a presumed
failure.

Primary sources:

- [Wolfram `Asymptotic`](https://reference.wolfram.com/language/ref/Asymptotic.html)
- [Wolfram `AsymptoticIntegrate`](https://reference.wolfram.com/language/ref/AsymptoticIntegrate.html)
- [Wolfram `AsymptoticDSolveValue`](https://reference.wolfram.com/language/ref/AsymptoticDSolveValue.html)
- [Wolfram `BesselJ`](https://reference.wolfram.com/language/ref/BesselJ.html)

## 4. Decision table

| S2 implementation outcome | Required disposition |
| --- | --- |
| raw Bessel recognition, valid registry bridge, generic germ path, exact scales, controls, typed failures, and replay all pass | **NARROW** |
| pipeline passes only after an expected exponent or Airy normal form leaks into discovery | **STOP** |
| generic controls fail or domain-invalid representations are silently accepted | **STOP** |
| Wolfram remains unexecuted | no comparative win; **EXPAND blocked** |
| a future executable same-information Wolfram row matches or exceeds the certificate at lower total cost | narrow further or stop the differentiating claim |

### Independent compiler replay

The evaluator-only script `run_s2_compiler_red_team.py` passed the following
checks without modifying the implementation:

- raw `besselj(N,N*z)` with (N) positive integer and (z) real lowered
  through registry
  `dlmf-10.9.2-integer-bessel-cosine-phase`, version 1;
- the registry source contained no `-1/3`, `-2/3`, `Airy`, or `airy`
  literal;
- the generic solver derived
  (	heta=N^{-1/3}widehat	heta) and
  (z-1=N^{-2/3}widehatdelta);
- every local-germ and balance replay check passed;
- the public result split replayed exactly as
  `local_chart_certified=true` and
  `uniform_integral_certified=false`;
- the independent non-Bessel cubic control used the same path and retained
  (7Ns^4) as an (N^{-1/3}) residual;
- the quartic cusp control recovered
  ((-1/4,-1/2,-3/4));
- `bessely(N,N*z)` returned `unsupported-special-function`;
- noninteger `besselj(nu,nu*z)` returned
  `registry-domain-mismatch`.

The bridge still records `full-reconstruction` and `uniform-error` as
undischarged obligations. Therefore its successful status certifies a local
chart, not a reconstructed Bessel evaluator or uniform Bessel asymptotic
theorem. `s2-compiler-red-team-results.json` is the concise snapshot.

An **EXPAND** recommendation would require a later gate with both:

1. an independent representation family not merely selected from the same
   Bessel registry mechanism; and
2. an executed same-information comparison against Wolfram or a comparably
   strong automatic asymptotics system.

## 5. Framework effect

- **Mathematical Core:** unchanged. The result instantiates backward
  task-sensitive retention and a filtered asymptotic fibre, but proves no new
  framework theorem.
- **Engineering Architecture:** refined locally. A versioned representation
  registry must carry provenance, domain predicates, and unresolved proof
  obligations; registry selection, germ construction, chart discovery, and
  certificate replay must remain separately accounted stages.
- **Theory Map:** unchanged. This is local U1/U2/E pressure, not a new stable
  node or API promotion.
- **Universality:** not earned. Neither arithmetic universality, general
  transseries closure, surreal runtime advantage, nor leverage on 3D Ising is
  supported by this baseline.

## 6. Reproduction

```bash
python run_s2_raw_baselines.py
```

`s2-baseline-results.json` records the observed snapshot. Timing is incidental;
the relevant evidence is result shape, typed failure, hint count, and whether a
coupled chart is reported.

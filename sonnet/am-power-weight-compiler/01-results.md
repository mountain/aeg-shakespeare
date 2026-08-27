# Completed AM power--weight compiler: first results

Status: T1 / `EXPAND` within a strict rank-one rational claim ceiling.

Issue: [#146](https://github.com/mountain/process-geometry/issues/146)  
Draft implementation: [#147](https://github.com/mountain/process-geometry/pull/147)

## 1. Result

The first executable completed AM carrier now exists as a research-local
compiler. Its native terms are

\[
\Phi_{\nu,w}=a^\nu e^{(w-\nu)v},
\qquad \nu\in\mathbb Z,
\qquad w\in\mathbb Q,
\]

with exact product and generator actions

\[
\Phi_{\nu,w}\Phi_{\mu,z}=\Phi_{\nu+\mu,w+z},
\qquad
A\Phi_{\nu,w}=\nu\Phi_{\nu-1,w-1},
\qquad
M\Phi_{\nu,w}=w\Phi_{\nu,w}.
\]

The completion does not construct a full coefficient window. After an
observer declares one target weight, the compiler recursively requests only
the dependencies needed for that readout. Exact coefficients live in the
finite group algebra

\[
\mathbb Q[\exp(\mathbb Q)],
\qquad
\exp(q)\exp(r)=\exp(q+r).
\]

This is a power--weight/exponential-polynomial carrier. A jet or matrix may be
an observer product, but neither receives semantic-carrier credit.

## 2. Frozen public gate

All 12 preimplementation cases passed and replayed:

- the product, `A`, `M`, PBW identity, and finite affine relation are exact;
- `power-weight` and `power-character` encodings canonicalize to the same term;
- positive-cone `exp` and `log1p` completion produces exact target weights;
- the `A` resonance produces typed `log-a` with the witness `a>0`;
- the `M` resonance produces typed `v-jordan`;
- missing positivity, negative completion input, excessive lattice
  denominator, excessive target weight, ordinary-only resonance, and symbolic
  height all fail closed with the frozen taxonomy.

The two public completion probes were:

| Case | Exact readout | Dependency requests | Distinct weights | Exact coefficient operations | Certificate |
|---|---:|---:|---:|---:|---:|
| weight-32 log cancellation | `-1/32` | 4 | 2 | 3 | 864 B |
| nested completed exponential | `exp(2)` | 8 | 2 | 7 | 863 B |

The first case is the clearest observer-directed result: it asks directly for
weight 32 of a monomial logarithm and the cancelling finite term, rather than
constructing weights 0 through 32.

## 3. Commit--reveal result

The hidden payload was committed before implementation by

`d578b7ed9f5193cc5b0a0212c3edad025a3b2cee4cf3f90885dd95a412ce5597`.

The evaluator and replay were then remotely frozen at

`a4cd0a7918b4d79ea049852bb829e0feb92d5e2f`.

Only afterwards was the payload revealed:

\[
[x^0]\,x^{-7}\left(
\exp\!\left(\log(1+2x)+x^2\right)
-\left(1+2x+x^2+2x^3+\frac{x^4}{2}+x^5+\frac{x^6}{6}\right)
\right).
\]

The compiler returned

\[
\boxed{\frac13}.
\]

The commitment verified exactly. The certificate used 29 dependency requests
over weights 0 through 7, 111 exact coefficient operations, and 888 bytes; a
fresh semantic replay reproduced the same certificate digest.

This is generalization evidence, not independent-discovery evidence: the
held-out was a nonce-protected preimplementation self-commit.

## 4. Same-information baseline

The declared SymPy baseline obtained all three exact readouts. It was allowed
to materialize a truncated coefficient window but received no credit for AM
carrier semantics, completion-domain witnesses, resonance typing, or replay.

| Case | Baseline window | AM distinct weights | SymPy median | AM median | Interpretation |
|---|---:|---:|---:|---:|---|
| weight-32 cancellation | 33 | 2 | 19.76 ms | 0.37 ms | material support advantage |
| nested exponential | 2 | 2 | 14.46 ms | 0.17 ms | same weight span |
| held-out weight 7 | 8 | 8 | 13.63 ms | 0.76 ms | same weight span |

Timing is a warm, local microbenchmark and is explicitly non-authoritative.
It is not a performance theorem. The defensible economy claim is narrower:
observer-directed extraction avoids a full intervening window on sparse,
distant readouts such as the weight-32 cancellation probe. The other two
cases demonstrate exact semantics and replay, not reduced weight support.

## 5. Evaluation

The frozen scoring rule gives `EXPAND`, for two reasons:

1. a reusable completed-AM task family now has executable, replayable
   semantics rather than only a matrix or polynomial proxy;
2. one frozen workload demonstrates a material dependency-window advantage.

This does **not** establish a general computational advantage over SymPy, a
general AM function theory, multivariable completion, or any surreal-number
runtime claim. In fact, the result sharpens the surreal assessment: no surreal
object was needed for this bounded rational-rank AM layer. Surreal height may
become relevant only at a later rank/iteration boundary; importing it here
would have added ontology without adding capability.

## 6. Next gate

Freeze a separate AM goal front-end and transport corpus. Its job is to map
existing mathematical vignettes and tests into the validated carrier, for
example a future textual request of the form

```text
\goal coefficient weight=7 of exp(log1p(2*x)+x^2)
```

without changing the now-tested evaluator. The front-end must preserve exact
source/context digests, reject ambiguous coordinate identifications, and
compare each transported task with its same-information baseline.

The current implementation consumes the frozen JSON AST; the textual
`\goal` form above is a next-stage interface proposal, not current syntax.

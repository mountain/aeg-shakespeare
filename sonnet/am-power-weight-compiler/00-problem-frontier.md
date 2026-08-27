# Completed AM power--weight compiler

## Problem and task

Can the native Addition/Multiplication affine function language be made into
an exact, replayable coefficient compiler whose semantic carrier is the
power--weight algebra and its observer-directed completion, rather than an
ordinary polynomial, matrix, jet, or generic computer-algebra series?

The primitive continuous processes are

\[
T_t(a,v)=(a+t,v),
\qquad
S_s(a,v)=(e^s a,v+s),
\]

with finite and infinitesimal laws

\[
S_sT_t=T_{e^st}S_s,
\qquad
[A,M]=A.
\]

The native basis is

\[
\Phi_{\nu,w}=a^\nu e^{(w-\nu)v},
\]

not the polynomial calibration module `span(1,a,...,a^n)`. Literal ordered
process words, their symbolic action, and observer coefficient readouts remain
separately typed.

## Primitive audit

- **base coefficient domain:** exact rationals;
- **constant readout extension:** finite rational linear combinations of
  formal `exp(q)` atoms, with `exp(q)exp(r)=exp(q+r)`;
- **power degree:** integer `nu`;
- **exponential character:** rational `lambda = w - nu`;
- **M-weight:** rational `w`;
- **base algebra:** finite support in `(nu,w)`;
- **completion:** allowed only along a declared positive rational weight cone;
- **task:** one exact target weight or bounded weight band;
- **residual:** all weights strictly above the observer horizon;
- **resonance:** a typed extension, never a silent base-algebra element.

The finite-LE chart from issue #144 is not identified with the native AM
frame. Any later bridge must be an explicit task-relative adapter.

## Construction and laws

Multiplication is sparse convolution on the power--weight lattice. The native
operators satisfy

\[
M\Phi_{\nu,w}=w\Phi_{\nu,w},
\qquad
A\Phi_{\nu,w}=\nu\Phi_{\nu-1,w-1},
\]

and replay must verify

\[
M^nA^m=A^m(M-m)^n.
\]

`ExpPositive` and `LogOnePlusPositive` denote elements of the declared
completion. They must answer a finite observer by dependency-directed exact
coefficient extraction. Neither compiler nor replay may call a generic
`limit()` or unrestricted `series()` oracle.

At `nu=-1`, an Addition primitive requires the positive-real logarithmic
extension; at `w=0`, a Multiplication primitive requires the `v` Jordan
extension. With `ordinary-only` policy those inputs fail closed.

## Solver plan

- research-local Python implementation with `Fraction` and a small exact
  formal exponential-constant algebra;
- strict JSON corpus and canonical digests;
- memoized coefficient dependency evaluation;
- specialized monomial coefficient rules where independently replayable;
- compact certificate containing source/context digests, requested and
  visited weights, operator laws, extensions, failures, costs, and claim scope;
- replay from source and context, not from a stored expansion trace;
- same-information SymPy baseline kept non-authoritative;
- seconds-scale unit, corpus, tamper, manifest, and default-CI bridge tests.

## Cost axes

Compilation, coefficient operations, visited weights, maximum live support,
certificate bytes, replay operations, baseline wall time, and baseline peak
support are reported separately. Shorter syntax or a correct coefficient does
not establish economy.

## Evidence firewall

Grammar, coefficient domain, positive-cone semantics, operator laws,
completion rules, resonance policy, budgets, public controls, scoring, and one
self-committed held-out payload freeze before evaluator source. The hidden
payload receives generalization evidence but no independent-discovery credit.

## Claim boundary

The maximum positive claim is a reusable exact compiler for the frozen
rank-one rational AM power--weight fragment. This is pressure on U2 and E, not
evidence for multivariable AM, V5 analytic closure, transseries, hyperseries,
surreal arithmetic, symbolic-height iteration, or Arithmetic Universality.
Mathematical Core, Engineering Architecture, Theory Map, and Public API remain
unchanged at creation.

## Kill conditions

Publish `STOP` if the result requires answer storage, unrestricted series or
limit calls, post-reveal grammar/scoring changes, or full expansion traces.
Publish `ELIMINATE` if it adds no semantic or material software capability
beyond a certificate wrapper around the baseline. Publish `NARROW` if native
laws work but completion/transport is not reusable. Publish `EXPAND` only if
the frozen task family gains replayable semantics or a material measured
dependency/support/certificate advantage.

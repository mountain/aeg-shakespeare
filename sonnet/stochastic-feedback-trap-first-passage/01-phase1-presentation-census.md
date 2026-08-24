# Phase 1 — bounded A/M presentation census

**Status:** executable exact bounded negative certificate.

Phase 1 enumerates every commutative literal A/M tree of depth at most two over
`{u,-1,0,1}`.  Literal syntax is retained before exact polynomial quotienting.

The anticipated structural counts are:

```text
exact depth 0        4
exact depth 1       20
exact depth 2      580
cumulative literal 604
semantic quotient   60
strictly increasing 16
nonlinear increasing 0
```

An admissible presentation must satisfy `h'(u)>0` on the entire closed interval
`[-1,1]`.  The certificate rejects zero derivatives at either endpoint, counts
all exact derivative roots in the interval, and checks the remaining constant
sign at `u=0`.  Numerical sampling is not an admissibility proof.

All 16 strictly increasing semantic presentations are affine.  The named
post-hoc chart `u+u^3` lies outside this depth-two grammar, so Phase 1 produces a
bounded negative certificate for nonlinear moving-presentation discovery.  The
grammar may be enlarged only in a later commit that preserves the exact
`604 -> 60 -> 16 affine -> 0 nonlinear` baseline.

This failure is structural rather than numerical.  Depth two can generate
nonlinear polynomials such as `u^2`, but no nonlinear member has derivative
strictly positive over the complete stopping interval.  The held-out chart has
the factorized history `u*(1+u^2)`, which first enters at depth three under the
frozen binary-tree convention.

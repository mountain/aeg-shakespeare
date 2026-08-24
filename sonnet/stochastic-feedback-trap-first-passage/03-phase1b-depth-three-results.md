# Phase 1b — depth-three execution result

**Status:** exact positive inclusion, negative uniqueness result.

The frozen semantic closure completed with:

```text
cumulative literal trees       365,424
exact semantic polynomials        1,519
strictly increasing on [-1,1]       242
affine increasing                     87
nonlinear increasing                 155
```

Semantic degree histogram:

```text
zero polynomial 1; constants 22; degree 1: 163; degree 2: 487;
degree 3: 503; degree 4: 248; degree 5: 69; degree 6: 20;
degree 7: 5; degree 8: 1
```

Strictly increasing degree histogram:

```text
degree 1: 87; degree 2: 55; degree 3: 97; degree 4: 3
```

The post-hoc control `u+u^3` is present and exactly certified, but it is one of
155 nonlinear survivors.  Therefore grammar membership and strict monotonicity
are insufficient canonicalization principles.  The enlargement succeeds at
representation coverage and fails at uniqueness.

No candidate was ranked by distance to the control, coefficient pattern, or
known inverse.  The next gate must treat all 155 nonlinear presentations as an
unlabelled admissible slice and use stopped-process semantics—generator,
diffusion pushforward, absorbing labels, initial law, and clock—to construct a
task quotient.  If those semantics identify all charts as gauge-equivalent,
canonicalization should return a class.  If they split the set, the split must
be explained by retained task payload rather than syntax cost.

# Phase 1b — depth-two census and generator-grammar red team

**Status:** depth-two bounded census and unrestricted linear-stabilizer filter
complete; legal S2 frontier frozen at 166 semantic expressions.

## 1. Exact bounded census

The frozen depth-two grammar gives:

```text
raw literal expressions          6488
exact semantic quotient          2101
bounded generators                 40
exact residual pairs            84040
zero-residual witnesses           8406
bounded-asymmetric expressions     286
```

Unlike S1a, the bounded search now produces apparent S2 inputs. The first
minimum-cost family includes (xy^2).

## 2. Required red team catches a false frontier

The frozen generator coefficients are only ({-1,0,1}). Yet

\[
(2M_x-M_y)(xy^2)=2xy^2-2xy^2=0.
\]

Thus (xy^2) is not genuinely asymmetric. Its visible continuous symmetry is
absent only from the bounded coefficient proposal grammar. Treating it as a
hidden-observer discovery would violate the Sonnet kill condition that the
observer grammar must not manufacture the frontier.

An exact rational nullspace red team now builds the four basis residuals,
collects their polynomial coefficient matrix, and computes its nullspace. This
red team does not add candidates to discovery ranking; it certifies whether a
bounded-asymmetric expression has any constant linear A/M stabilizer.

## 3. Schedule consequence

The unrestricted rational certificate has now been applied to all 286
bounded-asymmetric expressions:

```text
grammar false negatives     120  nontrivial rational nullspace
genuine S1-asymmetric       166  full rank four
```

The first grammar false negative is (xy^2), with stabilizer
(2M_x-M_y). The first legal S2 input in canonical semantic order is
(-2v_x+xy). Only the 166 full-rank expressions may enter observer search.

This freezes the S1 certificate. S2 may now open, but must report observer
semantics and reconstruction before any transformed zero residual counts as a
hidden symmetry.

## 4. Framework lesson

This is already useful negative evidence: bounded proposal generation can
create apparent canonicalization pressure that is only proposal-language
blindness. A discovery API therefore needs a completeness certificate relative
to a declared generator class, not merely a failure to find a low-cost
generator.

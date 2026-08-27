# Ensemble calibration and computational ledger

Status: exact for homogeneous independent assembly and the declared coarse
observer.

## 1. Power as objectified repeated assembly

Let `Omega` be a finite weighted state space with

\[
Z=\sum_{\omega\in\Omega}w(\omega).
\]

For `N` independent identical copies, Fubini factorization gives

\[
Z_{\Omega^N}=Z^N.
\]

The source ensemble has `|Omega|^N` microstates.  The total-partition observer
does not need to enumerate them: it objectifies repeated identical
Multiplication as one Power operation.  In the free-energy coordinate
`F=log Z`, the same operation is the dilation

\[
F\longmapsto NF.
\]

This is a strict task-relative software advantage.  It is not a lossless
representation of the microscopic ensemble.

## 2. Nested assembly compiler

For stages

\[
Z_{k+1}=e^{b_k}Z_k^{n_k},
\qquad
F_k=\log Z_k,
\]

we have

\[
F_{k+1}=n_kF_k+b_k.
\]

After `h` stages,

\[
F_h=\alpha_hF_0+\beta_h,
\]

with

\[
\alpha_h=\prod_{k=0}^{h-1}n_k,
\qquad
\beta_{k+1}=n_k\beta_k+b_k,
\qquad
\beta_0=0.
\]

The executable folds the history chronologically into `(alpha_h,beta_h)` and
independently records `alpha_h` as the number of base replicas.

## 3. Frozen cost witness

Take a three-state base ensemble and twenty binary homogeneous stages.  Then

\[
\alpha=2^{20}=1{,}048{,}576,
\]

so literal expansion has more than one million base leaves and

\[
3^{1{,}048{,}576}
\]

Cartesian microstates.  The compiled value state is two exact fields:
`(alpha,beta)`.  Replaying a supplied `F_0` uses one multiplication and one
addition.

| Cost axis | Explicit ensemble | AMP-compiled total observer |
|---|---:|---:|
| Base-copy leaves | `1,048,576` | not materialized |
| Microstates | `3^1,048,576` | not materialized |
| Evaluated state | full enumeration or factorized surrogate | 2 fields |
| Width of replica exponent | implicit in expansion | 21 bits |
| Replay after compilation | task dependent | 1 multiply + 1 add |
| Auditable source certificate | full construction or stage list | 20 stages + 2-field normal form |

The certificate is not falsely counted as constant storage: when stage
parameters vary, the stage list remains an `O(h)` audit trail.  Only the
number of evaluated task fields and the scalar-operation count are constant.
Their bit cost still grows with `alpha`, the supplied free energy, and the
requested output precision.  For twenty binary stages, storing `alpha` needs
21 bits, while the unmaterialized microstate count needs more than one million
bits even before individual state records are charged.  Repeated identical
stages also admit the closed iterate formula from Proposition 1.1.

## 4. What this opens and what it does not

The compiler directly helps tasks that ask for:

- total partition/free-energy values of factorizable repeated systems;
- equivalence of long M/P assembly histories;
- repeated scale cascades with a shared homogeneous rule;
- finite shadows of an A/P perturbation around a dominant power regime.

It is insufficient for:

- named microstate reconstruction;
- correlations between replicas;
- interacting assembly where `Z_(A x B) != Z_A Z_B`;
- arbitrary real powers interpreted as literal replica counts;
- a thermodynamic or ordinal limit without a declared topology and observer.

For an interacting system, write the honest residual

\[
R_{AB}=\log Z_{AB}-\log Z_A-\log Z_B.
\]

The M/P compiler handles the factorized backbone; the residual is the new
information that must be transported in a completion or correlation fibre.
This is why the current result does not reduce the general three-dimensional
Ising problem: its hard content is precisely nonflattening interaction across
scales.

## 5. Next computational gate

The smallest nontrivial continuation is a power-dominant interacting map such
as

\[
x\longmapsto x^d+t
\]

near infinity, or its partition analogue.  The target is to compile a finite
observer conjugacy to the pure power map, record the residual support and
error, and compare `N` direct iterations with one compiled power iterate.
Classically this is related to a Böttcher coordinate; in the AMP programme it
tests whether the completed A/P fibre produces reusable iteration leverage
rather than only another formal expansion.

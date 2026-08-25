# Phase 4 — finite prefix-orbit path metric

**Status:** Gate 4 exact finite geometry complete; all 1,092 audited
selector/input/prime histories are nondecreasing lattice rays with zero
backtracking, and paired selectors remain on one common input ray in the
bounded corpus; this supplies no Bellman or Huffman optimum.

**Owner:** [test_padic_continued_fraction_selector_comparison.py](../../tests/research/test_padic_continued_fraction_selector_comparison.py)

## 1. Question and verdict

Phase 3 mapped every Ruban and Browkin I prefix matrix to an exact finite
Bruhat--Tits lattice class.  It did not yet determine whether consecutive
classes form a reduced route, whether selector histories backtrack, or whether
their geometric travel contains optimization slack.

Phase 4 freezes those notions before invoking geodesics, Bellman recursion, or
source coding.  Its finite verdict is sharper than the motivating analogy:

> On the exhausted rational corpus, both selectors already trace compressed
> nondecreasing segments of one input-directed lattice ray.  Their differences
> are depth, compression, and outcome differences, not alternative routes
> through the tree.

This is a positive projective-geometry certificate and a negative optimization
certificate.  A unique geodesic to a selector-dependent prefix state does not
define an optimal selector.

## 2. Exact tree ledger

Phase 1's finite normal forms already provide a parent operation.  For two
vertices \(x,y\), repeatedly apply that operation until their depths agree and
then until the vertices agree.  The result is their lowest common ancestor
\(\operatorname{lca}(x,y)\), and the exact tree distance is

\[
d(x,y)=|x|+|y|-2|\operatorname{lca}(x,y)|.
\]

For digits \(a_0,\ldots,a_{n-1}\), let

\[
G_i=M(a_0)\cdots M(a_{i-1}),
\qquad
V_i=[G_i\mathbb Z_p^2],
\qquad
V_0=[\mathbb Z_p^2].
\]

The finite path ledger records

\[
T=\sum_{i=0}^{n-1}d(V_i,V_{i+1}),
\qquad
D=d(V_0,V_n),
\qquad
E=T-D,
\qquad
B=\frac E2.
\]

Here \(T\) is traveled edge distance, \(D\) is net displacement, \(E\) is
excess travel, and \(B\) is the number of edges traversed back toward the
start after cancelling the final geodesic.  In a tree, \(E\) is always even
and nonnegative.  A synthetic sibling-turn test verifies that the oracle
detects one backtracked edge as \(T=4,D=2,E=2,B=1\); zero audit values are
therefore not caused by an insensitive metric.

## 3. Digits are compressed even-length segments

Each continued-fraction digit matrix has unit determinant.  After normalizing
the minimum entry valuation, every audited prefix therefore lies at even
depth.  A digit transition can skip intermediate tree vertices; the ledger
charges the length of the unique connecting geodesic rather than pretending
that one stored digit is one tree edge.

For every audited digit, with \(V_i\) the vertex before that digit,

\[
\operatorname{lca}(V_i,V_{i+1})=V_i,
\]

and the exact tested step law is

\[
d(V_i,V_{i+1})=
\max\{0,-2v_p(a_i)\},
\]

with the zero digit handled as a stationary step.  Hence all sampled
transitions move outward or stay fixed, all excess travel vanishes, and every
stored digit is a compressed segment along one ray.

The determinant parity observation is algebraic.  The ancestor and step laws
are claimed here only for the declared finite rational audit, not as a theorem
for every admissible \(p\)-adic digit sequence.

## 4. Exhaustive individual-path audit

The domain is unchanged from Phase 3: 182 distinct nonzero reduced rationals
with denominator at most 12 and numerator magnitude at most 12, at
\(p=3,5,7\), stopping at termination, the first exact repeated rational state,
or a sixteen-step horizon.  Phase 3 found no horizon outcomes.

The 182 inputs times two selectors times three primes give 1,092 finite path
ledgers.

| prime | selector | ledgers | total travel = total net | maximum net depth | positive net depth | total excess | backtracked edges |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | Ruban | 182 | 996 | 12 | 180 | 0 | 0 |
| 3 | Browkin I | 182 | 716 | 6 | 180 | 0 | 0 |
| 5 | Ruban | 182 | 912 | 10 | 178 | 0 | 0 |
| 5 | Browkin I | 182 | 532 | 6 | 178 | 0 | 0 |
| 7 | Ruban | 182 | 892 | 10 | 176 | 0 | 0 |
| 7 | Browkin I | 182 | 496 | 6 | 176 | 0 | 0 |

The totals are finite corpus statistics, not expectations under a natural
source distribution.  Browkin has less aggregate travel under the uniform
enumeration convention, but that convention is part of this audit rather than
a selector-independent law.

## 5. Paired selectors do not branch in the bounded corpus

For each fixed rational input and prime, Phase 4 compares every Ruban prefix
vertex with every Browkin prefix vertex.  All pairs are ancestor-comparable.
In particular, the two final recorded vertices are equal or one is an ancestor
of the other; no audited selector pair enters distinct branches.

| prime | equal final vertex | Ruban final shallower | Browkin final shallower | incomparable | sum of final distances | maximum final distance |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 55 | 14 | 113 | 0 | 340 | 8 |
| 5 | 40 | 5 | 137 | 0 | 400 | 8 |
| 7 | 44 | 5 | 133 | 0 | 416 | 8 |

The exact final-distance histograms are

- \(p=3\): \(0:55, 2:90, 4:32, 6:4, 8:1\);
- \(p=5\): \(0:40, 2:100, 4:28, 6:12, 8:2\);
- \(p=7\): \(0:44, 2:86, 4:37, 6:12, 8:3\).

This finite evidence is compatible with the classical picture in which the
rational input determines a projective boundary direction and different
continued-fraction histories materialize different finite depths toward it.
The repository still has not constructed the infinite Bruhat--Tits boundary,
so Phase 4 states only the finite ancestor-comparability certificate.

## 6. The old red teams survive the new geometry

At \(p=5\), the input \(3\) still gives

\[
[3]_R=[-2;1/5]_B.
\]

The Ruban path has depths \((0,0)\) and travel zero.  The Browkin path has
depths \((0,0,2)\) and travel two.  Both are nondecreasing rays.  Ruban is
cheaper here because it stops earlier and materializes less depth, not because
Browkin takes a detour.

For \(-1\), Browkin terminates at the root while Ruban records the exact fixed
complete quotient after reaching depth two.  Again both finite paths have zero
backtracking.  Repeating five copies of Ruban's periodic digit gives the tested
depth sequence

\[
0,0,2,4,6,8,10
\]

with step distances \((0,2,2,2,2,2)\).  Thus a cycle in complete-quotient state
need not be a cycle in the lifted lattice history.  Quotienting by repeated
rational state would erase geometric progress.

## 7. Why Bellman and Huffman do not follow

A Bellman problem requires a common state and terminal contract, admissible
actions, additive stage costs, and explicit failure semantics.  Phase 4 has
two fixed selectors whose finite certificates may stop at different depths or
have different terminal/cycle outcomes.  Each path is already geodesic to its
own final prefix vertex, so there is no route-level backtracking slack to
optimize.  Comparing distances to different final states does not create a
shortest-path control problem.

A Huffman problem additionally requires a source alphabet with a probability
law and a prefix-decodable family of codewords.  The bounded rational list is
an exhaustive test domain, not a justified source distribution, and the digit
histories have not been proved to form the required code.  Calling the table
an expected code-length comparison would import both missing structures by
fiat.

Phase 4 therefore rejects three inferences:

1. geodesic prefix motion does not select Ruban or Browkin globally;
2. smaller finite aggregate travel is not Bellman optimality;
3. digit compression without a source law and decoding contract is not a
   Huffman problem.

## 8. Effective-analysis audit

- **Mode:** exact finite symbolic arithmetic over `Fraction` and integer tree
  labels.
- **Domain:** the Phase 3 rational corpus, \(p=3,5,7\), Ruban and Browkin I,
  and the same sixteen-step outcome oracle.
- **Closure:** prefix matrices, normalized lattice classes, parent reduction,
  lowest common ancestors, exact tree distance, and finite path sums.
- **Evaluator:** individual path ledgers, paired-selector ancestor relations,
  and fixed aggregate tables.
- **Certificates:** a synthetic backtracking control, per-transition ancestor
  and valuation-step identities, zero-defect ledgers, cross-selector
  comparability, and exact histograms.
- **Failure semantics:** cross-prime distances and empty paths are rejected;
  Phase 3's invalid input, cycle, and horizon distinctions remain in force.
- **Cost boundary:** tree edges are distinct from digit count, contact depth,
  serialization bits, runtime, and probability-weighted expected cost.
- **Numerical analysis:** not applicable; no floating-point or finite-precision
  \(p\)-adic approximation is used.

## 9. Claim ledger and postmortem

### Exact finite statements

1. lowest common ancestors and tree distances are computed exactly from the
   finite two-chart normal forms;
2. all 1,092 audited histories have \(T=D\) and zero backtracked edges;
3. every audited transition has its preceding prefix as common ancestor and
   obeys the displayed valuation-step law;
4. paired Ruban/Browkin histories are cross-ancestor-comparable for every
   audited input and prime;
5. the aggregate distances, depth maxima, relation counts, and histograms are
   exactly those displayed above;
6. the \(3\) economy witness and \(-1\) outcome witness remain distinct after
   adding path geometry.

### What the audit changed

The motivating risk was that selector differences might appear as branch
choice or geometric backtracking.  They did not.  In the bounded exact model,
projective geometry supplies a common direction and a precise materialized
depth, while the selector controls how that direction is compressed and when
the process certifies an outcome.  This narrows the next research problem
rather than decorating it with an unsupported optimization vocabulary.

### Claim boundary

Phase 4 proves no general rational or \(p\)-adic ray theorem, convergence rate,
periodicity classification, Lagrange theorem, stochastic optimum, source-code
bound, or preferred selector.  It does not construct the infinite boundary and
does not change the Theory Map or API maturity.

## 10. Next gate

The finite rational geometry calibration is now closed.  A further Bellman or
Huffman phase should begin only as a new, frozen task with all of the following:

1. a finite source distribution over rational inputs or finite projective
   cylinders;
2. an explicit selector-policy action set at each complete quotient;
3. a shared terminal reconstruction/precision contract and failure penalty;
4. separate digit, tree-edge, serialization, and computation costs;
5. for Huffman specifically, a proved prefix-decoding map for the generated
   histories.

Without those ingredients, the responsible continuation is to retain Phase
4's zero-backtracking result as a closure certificate rather than optimize an
undefined objective.

# Phase 1B results — character discovery and finite-scale no-go

Status: character-class discovery passed; logarithmic-scale discovery failed under the frozen finite selector.

This is a bounded structural-discovery result plus a negative uniqueness result. It is not a new theorem about the Boltzmann equation and does not derive kinetic dynamics from microscopic mechanics.

## 1. Firewall outcome

The discovery implementation received:

- exact positive-rational Multiplication histories;
- exponent normal forms for those histories;
- equality of pair-product fibres;
- Addition of one-site covector values;
- exact positive-rational order;
- the frozen degree-two A/M exponent grammar.

It did not call logarithm, exponential, \(f\log f\), a Maxwellian, or the continuous-character oracle. Source inspection is part of the executable certificate.

The classical logarithmic ratio was evaluated only after the survivor space, rational selector, and held-out outcomes were frozen.

## 2. Exact finite discovery

For a multiplicative world

\[
E(p_1,\ldots,p_d;N)
=
\left\{
\prod_jp_j^{n_j}:-N\le n_j\le N
\right\},
\]

the unrestricted control assigns an independent unknown \(\psi_x\) to every point and imposes

\[
\psi_a+\psi_b=\psi_c+\psi_d
\]

whenever \(ab=cd\).

The exact linear-algebra census is:

| World | Points | Unordered pairs | Product fibres | Constraint rank | Survivor dimension |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(E(2;2)\) | 5 | 15 | 9 | 3 | 2 |
| \(E(2,3;2)\) | 25 | 325 | 81 | 22 | 3 |
| \(E(2,3,5;1)\) | 27 | 378 | 125 | 23 | 4 |

In every case the complete unrestricted survivor space is

\[
\psi(n_1,\ldots,n_d)
=
c_0+\sum_{j=1}^d w_jn_j.
\]

Thus pair-product observation removes every nonlinear table direction and leaves exactly a constant gauge plus one additive character weight for each independent Multiplication generator.

## 3. A/M-native grammar coverage

The degree-two grammar contains

\[
1,\quad n_i,\quad n_in_j.
\]

Its monomial and survivor counts are:

| World | Grammar monomials | Surviving coefficient directions |
| --- | ---: | ---: |
| \(E(2;2)\) | 3 | 2 |
| \(E(2,3;2)\) | 6 | 3 |
| \(E(2,3,5;1)\) | 10 | 4 |

Every quadratic coefficient is forced to zero. The remaining native value vectors span the full unrestricted finite survivor space.

This passes the character-class discovery gate: the native grammar neither misses a finite survivor nor relies on a supplied logarithmic formula.

The larger alphabet red team adds one new character direction for the new prime 5. It preserves the structural law while refuting any claim that a fixed two-weight coordinate is universal.

## 4. Conserved-affine quotient

For the Phase 1A six-velocity network, the \(6\times3\) stoichiometric matrix has rank 2. Its left kernel has dimension 4 and is spanned by:

- total population;
- the three momentum coordinates.

The kinetic-label vector is the total-population vector on this unit-speed fixture, so it adds no independent direction.

Adding any of these invariants to a covector leaves every collision affinity unchanged. Likewise:

- adding a constant to the species-blind \(\psi\) is invisible to every \(2\leftrightarrow2\) reaction;
- multiplying a valid covector by a positive scalar preserves the H sign but changes units.

The discovered object is therefore a positive character ray modulo conserved-affine gauge, not a literal formula.

## 5. The finite order selector fails

On the training world \(E(2,3;2)\), normalize the 2-direction weight to one and write the 3-direction weight as \(r\). Exact order preservation gives

\[
\frac32<r<2.
\]

The frozen simplicity selector enumerates reduced positive fractions with numerator and denominator at most 8 and uniquely chooses

\[
r_{\mathrm{train}}=\frac53.
\]

It strictly preserves every order relation in the training world.

### First held-out defect

On \(E(2,3;3)\),

\[
\frac{27}{4}<8,
\]

corresponding to exponent vectors \((-2,3)\) and \((3,0)\). But the selected character gives

\[
-2+3\cdot\frac53=3,
\qquad
3+0\cdot\frac53=3.
\]

A strict activity order has collapsed to equality.

### Positive-H counterexample

On \(E(2,3;4)\), take

\[
A=\frac3{16},
\qquad
B=\frac{16}{81},
\qquad
A<B.
\]

Their exponent vectors are \((-4,1)\) and \((4,-4)\). The frozen character gives

\[
\psi(A)=-\frac73,
\qquad
\psi(B)=-\frac83,
\qquad
\psi(A)>\psi(B).
\]

Hence

\[
(A-B)(\psi(A)-\psi(B))
=
-\frac{13}{3888}<0,
\]

and the corresponding local functional rate is

\[
\dot F=\frac{13}{3888}>0.
\]

This is a genuine held-out H-sign failure, not merely a worse approximation score.

## 6. Nested Archimedean order cones

The exact admissible intervals for \(r\) are:

| Bound \(N\) | Exact interval |
| ---: | --- |
| 1 | \(1<r<2\) |
| 2 | \(3/2<r<2\) |
| 3 | \(3/2<r<5/3\) |
| 4 | \(3/2<r<8/5\) |
| 5 | \(3/2<r<8/5\) |
| 6 | \(11/7<r<8/5\) |

The intervals tighten through rational comparisons between powers of 2 and 3. No finite interval identifies the irrational scale exactly.

After the finite outcome is frozen, the classical continuous-character oracle gives

\[
r_*=\frac{\log3}{\log2}\approx1.5849625,
\]

which lies inside every recorded interval and preserves every held-out order relation.

The mechanism is now clear:

1. collision product fibres force a Multiplication-to-Addition character;
2. a finite multiplicative alphabet leaves independent generator weights;
3. finite order worlds constrain those weights to rational cones;
4. the full Archimedean order forces the ratios
   \[
   \frac{w_p}{w_q}=\frac{\log p}{\log q};
   \]
5. continuity extends the character from the rational multiplicative histories to
   \[
   \chi(x)=c\log x.
   \]

Integrating the positive ray gives

\[
\phi(x)=c(x\log x-x)+ax+b,
\]

so relative entropy appears modulo the already declared affine gauges.

## 7. What was discovered

The finite solver discovered, without the classical formula, that the admissible covector must be a character of Multiplication into Addition.

That is the genuinely process-native content of the logarithm in the H theorem. The logarithm is not selected because it is conventionally associated with entropy; it is selected because collision composition uses products while the functional differential adds one-site covectors.

However, the frozen finite simplicity rule did not discover the correct real scale. The missing selector is not another local collision identity. It is the global ordered and Archimedean structure of positive real Multiplication.

This distinction matters for the arithmetic tower:

- the character law is algebraic and rank-local;
- its real normalization depends on the ordered continuum and units;
- adding another Multiplication generator adds an observer direction until a global comparison law relates it to the others;
- none of these facts alone raises arithmetic rank.

## 8. Red-team outcomes

| Red team | Outcome |
| --- | --- |
| collision algebra without order | independent prime weights remain; uniqueness rejected |
| finite simplicity overfit | \(5/3\) fails held-out strict order and produces \(\dot F>0\) |
| larger prime alphabet | character dimension rises by one as predicted |
| negative orientation | H sign reverses on a nonstationary channel |
| affine gauge | constants and collision invariants leave affinities unchanged |
| regularity removal | ordinary logarithm is not claimed from bare algebraic Cauchy data |

All frozen red teams passed.

## 9. Claim boundary

Earned:

- bounded character-class discovery;
- exact coverage of the unrestricted finite survivor space by the A/M-native grammar;
- structural transfer from one and two Multiplication generators to a held-out three-generator world;
- an exact counterexample to the finite rational simplicity selector;
- identification of Archimedean order as the additional structure needed for logarithmic normalization.

Not earned:

- oracle-free finite discovery of the exact real logarithmic scale;
- a new classification theorem for continuous characters;
- uniqueness without regularity, order, gauge, and unit conventions;
- microscopic derivation, BBGKY closure, or propagation of chaos;
- a cross-rank entropy theorem;
- public API extraction.

## 10. Research decision and next gate

Repeating the same finite rational selector at larger bounds would only compute progressively tighter Diophantine intervals. It cannot return the irrational ratio exactly at a finite stage. Phase 1B therefore closes with a responsible partial result rather than an unbounded brute-force schedule.

The next distinct question is Phase 2:

> Can two exact microscopic ensembles have the same declared one-body state but different next one-body derivatives, and what is the smallest continuation observer that separates them?

That gate moves from the form of H to the BBGKY information seam.


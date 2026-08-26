# Phase 11 results — Archimedean placement and state--observer duality

**Status:** complete for the frozen finite and exact algebraic task.  The
Archimedean axiom is placed in ordered observer semantics rather than the
rational A/M grammar; finite state--predicate duality, quotient/predicate
factorization, A/M predicate transport, finite place observers, and the
rational product formula pass.  No infinite Stone, cofree-observer, adelic,
or objectification theorem is claimed.

**Frozen contract:**
[17-phase11-archimedean-state-observer-duality-task-contract.md](17-phase11-archimedean-state-observer-duality-task-contract.md).

**Executable certificate:**
[test_archimedean_state_observer_duality.py](../../tests/research/test_archimedean_state_observer_duality.py).

---

## 1. Executive verdict

The main correction is a type correction:

> The Archimedean axiom is not a law of the primitive A/M process grammar.  It
> is a cofinality law for an ordered-field observer.  Logical duality reverses
> state maps into predicate pullbacks; changing from the real place to a
> p-adic place changes the observer topology.  These are different axes.

The exact positive dual system found in this phase is finite Stone duality in
its powerset form:

\[
X
\longmapsto
\operatorname{Pred}(X)=\mathcal P(X),
\qquad
f:X\to Y
\longmapsto
f^*:\mathcal P(Y)\to\mathcal P(X).
\]

For finite \(X\), the structure-preserving Boolean maps
\(\mathcal P(X)\to\{0,1\}\) recover exactly the points of \(X\).  Thus there
is a precise, nonmetaphorical state--logic duality on the frozen domain.

The result opens the observer side of the A/M chain as

```text
state generator/action        elementary predicate transformer
free finite history           reverse transport through the history
state evaluation              truth of transported predicates
task quotient                 fibre-constant predicate subalgebra
forgotten residual            nonfactoring discriminator
bounded future behavior       finite recognized language/trace
```

It does not identify arithmetic addition/multiplication with logical
join/meet, and it does not turn the real place into the p-adic place.

---

## 2. Gate 11A — exact placement of the Archimedean axiom

### 2.1 The axiom

For an ordered field \(K\), the Archimedean statement is

\[
\forall x,y>0\;\exists n\in\mathbb N:\quad nx>y.
\]

It says that the additive integer ruler is cofinal.  Equivalently,

\[
\forall\epsilon>0\;\exists n\in\mathbb N:\quad \frac1n<\epsilon.
\]

The reciprocal statement exchanges arbitrarily large integer scales with
arbitrarily small reciprocal scales **inside the same ordered field**.  It
does not change the absolute value or complete the field at another place.

The executable uses 43 distinct positive rationals.  It constructs exact
integer witnesses for all

\[
43^2=1{,}849
\]

ordered positive pairs and 43 reciprocal-smallness queries.  The witness is

\[
n=\left\lfloor\frac yx\right\rfloor+1
\]

or, respectively,

\[
n=\left\lfloor\frac1\epsilon\right\rfloor+1.
\]

This is an executable certificate on the frozen corpus, not a finite proof of
the quantified field axiom.

### 2.2 The A/M carrier precedes the axiom

The rational operations

\[
T_a(z)=z+a,
\qquad
D_k(z)=kz,
\qquad
J_b(z)=\frac b z
\]

and their lowering to \(PGL_2(\mathbb Q)\) require only rational field
arithmetic and admissible denominators.  They do not require:

- a compatible linear order;
- integer cofinality;
- a norm;
- a topology;
- a completion;
- a real or p-adic digit selector.

The Archimedean axiom enters only after the observer asks order-sensitive
questions such as whether one state lies below another, whether an integer
ruler overtakes a scale, or which ordered integer interval contains a state.

### 2.3 Archimedean does not imply complete or connected

The ordinary ordered field \(\mathbb Q\) is the decisive red team.  It is
Archimedean, but it is not complete.  The Pell convergents

\[
1,
\frac32,
\frac75,
\frac{17}{12},\ldots
\]

satisfy the exact certificate

\[
p_n^2-2q_n^2=\pm1,
\qquad
\left|\left(\frac{p_n}{q_n}\right)^2-2\right|=\frac1{q_n^2}.
\]

The executable checks twelve terms and their strictly shrinking consecutive
increments.  Their real limit would square to two, but no rational number
does.  Hence Archimedean cofinality does not close rational Cauchy gaps.

It also does not imply connectedness.  In the order topology on \(\mathbb Q\),
the irrational cut at \(\sqrt2\) separates the field into the two nonempty
open sets

\[
\{q\in\mathbb Q:q<\sqrt2\},
\qquad
\{q\in\mathbb Q:q>\sqrt2\}.
\]

The earlier phrase “the real place has an Archimedean connected topology” is
therefore sharpened as follows:

```text
usual absolute value on Q     Archimedean place
ordered completion of Q       R
order completeness of R       connected real line
real metric choice             hyperbolic/analytic geometry
```

The properties coexist at the real completion, but one does not follow from
the word *Archimedean* alone.

### 2.4 Why p-adic is not the logical negation

The logical negation of the Archimedean sentence is

\[
\exists x,y>0\;\forall n:\quad nx\le y.
\]

It describes an infinitesimal inside an ordered field.  By contrast, a p-adic
absolute value satisfies

\[
|x+y|_p\le\max(|x|_p,|y|_p).
\]

This is an ultrametric law, not a quantifier negation of ordered cofinality.
For a concrete obstruction, \(x^2+1\) has a 5-adic root by Hensel lifting from
\(x=2\bmod5\).  Thus \(-1\) is a square in \(\mathbb Q_5\), which rules out a
field-compatible linear order.  The p-adic side is consequently not an
ordered field containing a positive infinitesimal in the sense of the
negated Archimedean axiom.

The executable constructs eight compatible roots modulo
\(5,5^2,\ldots,5^8\), checks \(r_k^2+1\equiv0\pmod {5^k}\), the compatibility
\(r_{k+1}\equiv r_k\pmod {5^k}\), and the nonvanishing derivative condition.
This is a finite Hensel certificate; the existence of the infinite 5-adic
limit still uses Hensel's theorem.

Gate 11A passes with the seven-layer audit:

| Structure | Layer | Supplied by Archimedean axiom alone? | Additional data |
| --- | --- | ---: | --- |
| rational A/M syntax | process | no | none |
| integer cofinality | ordered field | yes | order |
| integer-part/floor section | selector | no | order and integer section |
| all Cauchy limits | completion | no | completeness |
| connected real line | topology | no | order completeness |
| hyperbolic metric | geometry | no | metric ruler |
| p-adic clopen balls | place observer | no | ultrametric |

---

## 3. Gate 11B — finite state--logic duality

### 3.1 Predicate algebra and inverse image

For a finite state set \(X\), define

\[
\operatorname{Pred}(X)=\mathcal P(X).
\]

A state transformation \(f:X\to Y\) acts on predicates in the reverse
direction:

\[
f^*(P)=f^{-1}(P).
\]

Direct elementwise calculation gives

\[
f^*(P\cap Q)=f^*(P)\cap f^*(Q),
\]

\[
f^*(Y\setminus P)=X\setminus f^*(P),
\]

and

\[
(g\circ f)^*=f^*\circ g^*.
\]

Therefore state evolution is covariant while logical observation is
contravariant.  This is the precise duality used below.

### 3.2 Exact finite point recovery

For \(X=\{0,1,2\}\), the predicate algebra has eight elements.  There are

\[
2^8=256
\]

arbitrary functions

\[
\mathcal P(X)\to\{0,1\}.
\]

The exhaustive test imposes preservation of bottom, top, complement, and
intersection.  Exactly three functions survive, namely

\[
\operatorname{ev}_x(P)=1\iff x\in P,
\qquad x\in X.
\]

This finite theorem also has a direct proof.  The singleton atoms partition
the top element.  A Boolean homomorphism to \(\{0,1\}\) must send exactly one
atom to one: at least one because their join is top, and at most one because
distinct atoms have empty meet.  Preservation of joins then makes the map
evaluation at that unique atom.

The red-team consequence is substantial:

> The naive Boolean-valued double dual is much larger than the state space.
> States return only after the observation maps are required to preserve the
> declared logical structure.

This is the first exact positive answer to what “a dual system generated by
logic” can mean for the current A/M line.  It is finite Stone duality, not a
second arithmetic grammar.

---

## 4. Gate 11C — opening the A/M chain on the observer side

### 4.1 Frozen projective actions

The executable uses

\[
X_p=\mathbb P^1(\mathbb F_p),
\qquad p=3,5,7,
\]

with the three nonsingular generators

\[
T_1=
\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
D_2=
\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad
W=
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

All words through depth three give 40 histories.  Every subset of each
projective line is admitted as a predicate.  The state sizes and predicate
counts are

| \(p\) | states \(|X_p|\) | predicates \(2^{|X_p|}\) | histories |
| ---: | ---: | ---: | ---: |
| 3 | 4 | 16 | 40 |
| 5 | 6 | 64 | 40 |
| 7 | 8 | 256 | 40 |

The full test checks

\[
4\cdot16\cdot40
+6\cdot64\cdot40
+8\cdot256\cdot40
=99{,}840
\]

state--predicate--history memberships.  Every one satisfies

\[
w(x)\in P
\iff
x\in w^*(P).
\]

It also verifies 3,024 two-generator composition/predicate cases.  A forward
chronological history therefore becomes reverse predicate transport exactly.

### 4.2 Two different linear variances

Let a covector \(\ell\) define the hyperplane predicate

\[
H_\ell=\{x:\ell(x)=0\}.
\]

There are two related formulas:

1. pulling the predicate backward along \(g\) gives
   \(g^{-1}(H_\ell)=H_{g^T\ell}\);
2. forwarding the hyperplane with the points gives
   \(g(H_\ell)=H_{g^{-T}\ell}\).

The executable verifies both for all frozen generators, primes, and
projective covectors.  This sharpens Phase 10: \(g^{-T}\) is the forward
incidence action, while \(g^T\) is the backward predicate transformer.
Neither is Boolean complement, and neither changes the place.

### 4.3 The correctly typed chain

The complete finite comparison is now

| Process/state side | Observer/logical side |
| --- | --- |
| primitive action \(g\) | inverse-image transformer \(g^*\) |
| chronological word \(g_n\cdots g_1\) | reverse pullback \(g_1^*\cdots g_n^*\) |
| state \(x\) | structure-preserving truth evaluation \(\operatorname{ev}_x\) |
| forward hyperplane image | contragredient \(g^{-T}\) |
| backward hyperplane test | transpose \(g^T\) |
| state equality under all predicates | equality of logical profiles |

Gate 11C passes on the declared finite projective domains.

---

## 5. Gate 11D — task quotient becomes an observer subalgebra

Let

\[
q:X\twoheadrightarrow Y
\]

be a surjective task quotient.  Then

\[
q^*:\mathcal P(Y)\hookrightarrow\mathcal P(X)
\]

is injective.  Its image consists exactly of saturated predicates: subsets of
\(X\) that are unions of complete \(q\)-fibres.

The proof is exact:

- inverse images preserve all Boolean operations;
- surjectivity makes distinct predicates on \(Y\) have distinct inverse
  images;
- every inverse image is constant on fibres;
- every fibre-constant predicate is the inverse image of the set of coarse
  states whose fibres it contains.

The executable instantiates

\[
\mathbb Z/p^2\mathbb Z\twoheadrightarrow\mathbb Z/p\mathbb Z
\]

at \(p=3,5\).  It enumerates all eight and thirty-two coarse predicates,
respectively, and proves equality with the enumerated fibre unions.

The singleton \(\{0\}\subset\mathbb Z/p^2\mathbb Z\) is the minimal residual
red team.  Since

\[
q(0)=q(p)=0
\]

but the singleton distinguishes \(0\) from \(p\), it cannot factor through
the quotient.

This yields the exact interpretation:

> A residual over a task quotient first appears on the logical side as a
> missing discriminator.  Adding it repairs an observation quotient; it does
> not automatically add a process coordinate.

Translation, unit dilation, and their affine composite commute with both the
fine and coarse quotients in every frozen case.  Their predicate pullbacks
also commute with \(q^*\).  Thus the statement is compositional for the
declared action grammar, not merely a set-count coincidence.

---

## 6. Gate 11E — two place observers and one global compatibility

### 6.1 Real order predicates

The real observer supplies order cuts, intervals, integer cofinality, and an
integer-part section.  On the shared rational input

\[
x=\frac83,
\]

the ordinary real selector gives

\[
\lfloor x\rfloor=2.
\]

This choice depends on the ordered embedding of \(\mathbb Z\).

### 6.2 p-adic cylinder predicates

At \(p=5\), the same rational is integral because its denominator is a unit,
and its first residue is

\[
8\cdot3^{-1}\equiv1\pmod5.
\]

Thus the p-adic residue selector gives 1, not 2.  Neither selector is the
logical complement of the other; they are different marked sections for
different observer bases.

The executable builds all congruence cylinders through depth three for
\(p=3,5\): forty cylinders at \(p=3\) and 156 at \(p=5\).  All 25,936 ordered
cylinder pairs are disjoint or nested.  At each level the complement of one
cylinder is exactly the union of its peer cylinders, giving the finite clopen
certificate.

On shared integer samples, the real cut \(x\le0\) and the p-adic cylinder
\(x\equiv0\pmod p\) overlap, but neither contains the other.  This is an exact
finite witness that the two predicate bases are not one reparameterized
partition.

### 6.3 Product formula

The positive bridge is arithmetic rather than logical.  For every nonzero
rational \(x\), with normalized absolute values,

\[
|x|_\infty\prod_p|x|_p=1.
\]

Only finitely many primes contribute.  The executable verifies the formula
on 126 distinct rationals and separately on 52 prime-power cases.  In
particular,

\[
|p^n|_\infty=p^n,
\qquad
|p^n|_p=p^{-n}.
\]

The earlier observation that the same multiplication history escapes at the
real place while approaching zero at the p-adic place is therefore part of an
exact global balance law.

This is the most promising later route toward an adelic comparison, but the
present phase constructs neither an adelic product topology nor an adelic
solver.  Product compatibility and logical duality remain separately typed.

---

## 7. Gate 11F — bounded behavior and the cofree boundary

For a state \(x\), terminal predicate \(P\), and word \(w\), define

\[
\beta_{x,P}(w)=1\iff w(x)\in P.
\]

At \(p=5\), using the three A/M/Weyl actions, the terminal predicate
\(P=\{0\}\), and all forty words through depth three, the direct state
behaviors equal the reverse-predicate behaviors in all

\[
6\cdot40=240
\]

entries.  The six bounded behavior profiles are distinct, so this one frozen
observer separates all six projective states at the declared depth.

This is a finite language/trace result.  It is not a terminal coalgebra:

- word depth is bounded;
- the alphabet is frozen;
- the terminal predicate is chosen;
- no inverse-limit topology is constructed;
- no universal map from arbitrary observers is proved.

The naive double dual red team is also decisive.  A six-state set has 64
predicates and therefore

\[
2^{64}
\]

arbitrary Boolean-valued functions on its predicate set, but only six
structure-preserving point evaluations.  A bidual return exists only in the
structure-preserving finite Stone sense.

The dual objectification ledger is

```text
finite Boolean point recovery                 yes
bounded behaviors separate frozen states      yes
new task-independent cogenerator              no
infinite cofree observer proved               no
coherent global bidual return                  no
new vertical process rank                      no
```

Gate 11F therefore closes negatively for objectification.

---

## 8. What the result changes in the theory

### 8.1 Supported intuition

The intuition that a logical dual should open a complete “other side” of the
A/M process chain is supported in a precise finite form:

- states dualize to structured logical evaluations;
- forward actions dualize to backward predicate transformers;
- finite histories dualize to bounded response languages;
- task quotients dualize to observer subalgebras;
- residuals become missing discriminators;
- structure-preserving biduality recovers points.

This is more than a metaphor and more than the projective identity
\(g\mapsto g^{-T}\).

### 8.2 Rejected inference

The following single chain is false:

```text
Archimedean real AM geometry
    --logical duality-->
p-adic geometry
    --> new objectified dimension.
```

The correct diagram has two independent directions:

```text
                         state / predicate variance
rational A/M carrier  <------------------------------>  logical observers
        |                                                       |
        +--> real place: order cuts, intervals, floor           |
        |                                                       |
        +--> p-adic place: clopen cylinders, residues, rays     |
        |                                                       |
        +--> product formula: global place compatibility -------+
```

The horizontal arrow is logical duality.  The downward arrows are place
evaluations.  The product formula constrains their joint arithmetic image.

### 8.3 Revised dual objectification criterion

The primal criterion remains

\[
\text{new primitive}
+\text{free composition}
+\text{all-composite lowering}.
\]

On a genuinely dual observer side it should be accompanied by

\[
\text{new cogenerator}
+\text{cofree behavior}
+\text{all-observation pairing}
+\text{coherent bidual return}.
\]

Adding a discriminator that merely reverses an earlier quotient satisfies
neither full criterion.  Phase 11 therefore strengthens rather than weakens
the existing objectification boundary.

---

## 9. Claim and execution ledger

### Exact finite/algebraic results

1. 1,849 Archimedean cofinality and 43 reciprocal-smallness witnesses pass on
   the frozen rational corpus.
2. Twelve Pell convergents carry exact \(\pm1\) incompleteness certificates.
3. Eight compatible Hensel lifts witness the finite approach to a 5-adic
   square root of \(-1\).
4. Of 256 Boolean-valued maps on the eight-element predicate algebra, exactly
   three are Boolean homomorphisms, one for each state.
5. Inverse image preserves Boolean structure and reverses composition on all
   frozen finite functions.
6. All 99,840 A/M history--state--predicate memberships commute.
7. All 3,024 two-generator predicate-composition cases commute.
8. Transpose pullback and contragredient forward incidence both pass on the
   finite projective domains.
9. Forty coarse residue predicates are exactly the fibre-constant predicates
   for the two frozen quotients.
10. All 25,936 p-adic cylinder pairs are nested or disjoint.
11. Real floor and p-adic residue selection disagree exactly on \(8/3\).
12. The rational product formula passes on 126 rational and 52 prime-power
    cases.
13. All 240 bounded direct/dual behavior entries agree, and the six frozen
    states have distinct behavior profiles.

### Theorem-level statements used but not proved by finite exhaustion

- the Archimedean axiom for \(\mathbb Q\);
- irrationality of \(\sqrt2\);
- incompleteness and disconnectedness of \(\mathbb Q\);
- Hensel lifting of a square root of \(-1\) in \(\mathbb Q_5\);
- the normalized product formula for all nonzero rationals;
- finite Stone duality beyond the explicitly enumerated three-state model.

Each has an elementary proof or proof sketch recorded above.  The executable
tests consequences and finite certificates rather than pretending that a
bounded loop proves an infinite theorem.

### Costs

```text
arithmetic                         exact Fraction/integer
finite logic                       exhaustive powerset tables
projective state space             P^1(F_p), p=3,5,7
history horizon                    depth <= 3
p-adic cylinder depth              <= 3
external solver                    none
public API                         none
```

---

## 10. Explicit nonclaims

This result does not claim:

- that p-adic topology is the logical or categorical dual of real topology;
- that an Archimedean ordered field is complete or connected;
- that real floor and p-adic residue selection form a dual pair;
- that arithmetic \(+\) and \(\times\) are categorical coproduct and product;
- that Boolean complement, inverse image, \(g^{-T}\), group inverse, reciprocal,
  and place change are one duality;
- that the full A/M history category is free in a proved categorical sense;
- that its observer category is cofree;
- that bounded response tables construct an infinite language boundary;
- that finite Stone duality proves a Stone representation theorem for the
  real line or Bruhat--Tits boundary;
- that the product formula constructs adeles or an adelic topology;
- that a missing discriminator is a new process dimension;
- that an Experimental or Public API is justified.

---

## 11. Governance disposition

### Mathematical Core Change

**Refine.**  Separate Archimedean cofinality from order completeness and
connectedness; add the finite state--predicate contravariance and
quotient/predicate theorem; retain the distinct projective and place axes.

### Engineering Architecture Change

**Refine.**  Typed solver plans must distinguish forward state transforms,
backward predicate transforms, forward hyperplane transport, place observers,
and quotient-factorization certificates.  Residual predicates remain explicit
rather than being projected away.

### Theory Map Change

**Refine with one positive horizontal edge and one stronger no-go boundary.**
Finite logical duality is exact and process-compatible.  No cofree universal
property, global bidual return, or vertical objectification has been proved.

### API maturity

**No change.**  All logic, finite-field, cylinder, and product-formula helpers
remain private to the research test.  No `StateDual`, `PredicateAlgebra`,
`PlaceObserver`, `CofreeObserver`, or `AdelicCarrier` abstraction is proposed.

---

## 12. Next research gate

Phase 11 fixes the logical variance and reveals two viable continuations that
must remain sequential:

1. **History--language adjunction audit.**  Determine whether the literal A/M
   history grammar has a declared free universal property and whether its
   full, not depth-bounded, response languages form a cofree or terminal-
   coalgebra observer with a unit/counit round trip.
2. **Global place compatibility audit.**  Starting from a rational frame
   certificate, determine whether finitely supported place data satisfying
   the product formula form a useful restricted product carrier before any
   adelic topology or solver claim.

The first must precede objectification; the second must precede any claim that
real and p-adic solver results are globally compatible.  They should not be
collapsed into one “duality” phase.

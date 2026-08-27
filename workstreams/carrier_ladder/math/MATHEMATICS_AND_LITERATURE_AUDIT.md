# Workstream A — mathematics and primary-source audit

**Contract:** process-geometry issue [#142](https://github.com/mountain/process-geometry/issues/142)  
**Frozen frontier:** `36bfc00651342234edfef064cccf99abbcb01b0e`  
**Status:** research-local audit; no Core, Theory Map, architecture, or API promotion  
**Audit date:** 2026-08-27

## 0. Verdict

The proposed `C0 < C1 < C2 < C3 < C4` notation is not a mathematically sound
linear inclusion ladder. It conflates five independent questions:

1. the **ambient universe** (finite syntax, a set-sized Hahn field, a formal
   hyperseries field, or the proper class `No`);
2. the **available operations** (field operations, `exp/log`, derivation,
   composition, hyperlogarithms, hyperexponentials);
3. the **height/index set** (finite construction rank versus ordinal strength);
4. the **normalization principle** (formal support versus Conway simplicity);
5. **effectivity** (finite encoding, executable comparison/truncation, and a
   bounded replay certificate).

The strongest responsible mathematical conclusions are:

- **Finite-DAG eliminability.** Every well-typed finite expression DAG built
  from rational constants, finite-stage LE-transseries inputs, algebraic field
  operations, `exp`, and positive `log` evaluates in some finite construction
  stage of the LE-transseries field. Every fixed finite iterate has the same
  property. This is a structural-induction theorem and yields a finite
  *membership* certificate. It does not establish carrier minimality or an
  analytic-germ bridge.
- **Finite support is not a field carrier.** Exact inversion already takes
  `1-m` to `sum_(n>=0) m^n`. The issue's C1 must use well-based Hahn support (or
  a lazy/truncation presentation), not finite support, if it claims field
  closure.
- **Uniform iteration can separate finite-height LE from a
  transexponential/hyperserial operation.** A positive eventually increasing
  solution of `F(x+1)=exp(F(x))` is transexponential: it outruns every fixed
  finite exponential iterate. Such a uniform object cannot be represented by
  merely unrolling one finite expression DAG.
- **The equation does not separate hyperseries from surreal numbers.** The
  surreal class has now been equipped with hyperlogarithms and
  hyperexponentials of ordinal strengths, while compatible hyperseries fields
  and hyperseries subfields of `No` exist. The same hyperiteration task can
  therefore live in a smaller hyperserial field or in `No` with the additional
  hyperserial structure.
- **Ambient embedding is not effective containment.** The canonical embedding
  of ordinary transseries into `No`, and the representation of surreal numbers
  as hyperseries evaluated at `omega`, do not by themselves supply a finite
  compiler, an inverse lowering algorithm, or a total internal composition
  `No x No -> No`.

Consequently, the workstream disposition is:

```text
L0:       ELIMINATE to C0
L1:       ELIMINATE surreal; C2 is an upper bound, not always the minimum
L2 fixed: ELIMINATE to finite-height LE
L2 uniform formal hyperiteration: genuine pressure beyond C2
C3 versus surreal-with-hyperserial-structure: NARROW / not separated
full-surreal runtime necessity: not earned
```

## 1. Definitions that the compiler may safely expose

### 1.1 Finite expression DAG

Fix variables `X`, rational constants, and nodes

```text
add, sub, mul, inv, exp, log
```

where `log` is typed only on a declared positive domain (or carries an explicit
complex branch, which is outside the first contract). A DAG is *finite* when it
has finitely many nodes. An expression family indexed by a symbolic natural or
ordinal height is not a finite DAG unless the iterate is unrolled at a fixed
index.

### 1.2 Hahn series

For an ordered abelian monomial group `M`, a Hahn field consists of formal sums

\[
  f=\sum_{m\in M} f_m m
\]

whose support is well-based (reverse well-ordered in the dominant-monomial
convention). Support may be infinite or transfinite. Merely saying “finite Hahn
support” specifies a sparse representation class, not a field closed under the
ordinary operations.

**Counterexample 1 (finite-support nonclosure).** Let `0 < m < 1` be a
monomial. In a Hahn field,

\[
 (1-m)^{-1}=1+m+m^2+\cdots .
\]

The left input has finite support; its inverse has infinite well-based support.
Thus C1 as written in #142 is not closed under exact inversion, and analogous
infinite supports appear under `exp` and `log`.

### 1.3 LE-transseries

The logarithmic-exponential transseries field is constructed as a directed
union of Hahn-series stages with finite exponential and logarithmic depth.
Every element belongs to some finite stage, although it may have infinite
well-based support. This is the construction in van den Dries--Macintyre--Marker,
not a claim that each element has finite syntax or finite storage.

### 1.4 Hyperserial structure

A hyperserial field carries named hyperlogarithmic and hyperexponential
operations at declared ordinal strengths, subject to coherence/composition
axioms. This is an operation-bearing structure, not merely a larger set of
numbers. The field of logarithmic hyperseries already has differentiation,
integration, and composition; later hyperserial work adds ordinal-strength
hyperlogarithms and hyperexponentials.

### 1.5 Surreal ambient structure

`No` is a proper class-sized real-closed ordered field with Conway normal forms
and Gonshor exponentiation. Further results equip it with the
Berarducci--Mantova derivation and, more recently, a confluent hyperserial
structure. These are distinct layers. “The surreal numbers” without an
operation signature is not a compiler capability.

## 2. Finite-DAG eliminability

### Theorem A (conditional finite-stage lowering)

Let `T_LE = union T_(p,q)` be an LE-transseries field presented as the directed
union of finite exponential/logarithmic construction stages. Let `D` be a
finite, acyclic, well-typed expression graph whose leaves are rationals or
elements supplied with finite-stage certificates. Suppose every division is by
a certified nonzero input and every real logarithm has a certified positive
input. Then the value at every node of `D`, and in particular its root, belongs
to a finite LE stage.

**Proof.** Topologically order the finite DAG. Give each rational leaf stage
zero and each input leaf its supplied finite stage. Field-operation nodes lie
in a common stage containing the finitely many parent stages. An `exp` or
`log` node lies in a later finite stage by the defining closure construction of
`T_LE`. Induction assigns a finite stage to every node. Since there are only
finitely many nodes, the root stage is finite. QED.

The replayable certificate is the DAG together with:

```text
node id
operation and parents
input stage or inferred stage bound
nonzero / positive / branch obligation
root observer and requested truncation
```

This certificate proves **sufficiency**, not minimality. Stage bounds obtained
from syntax are generally loose.

**Counterexample 2 (syntax is not minimality).** `exp(log(x))` has syntactic
height two but lowers to `x` on a certified positive domain. Conversely, exact
inversion of a finite-support input can require an infinite Hahn support.

### Corollary A.1 (fixed iterates)

For each fixed natural `n`, `exp^[n](x)` and `log^[n](x)` are finite DAGs and
therefore lower to a finite LE stage under the same typing conditions.

There is no uniform stage bound for the family as `n` ranges without bound.
Replacing the fixed integer by a symbolic variable changes the grammar: it
introduces an iteration/solution operator, not another finite `exp` node.

### What Theorem A does not say

The issue's phrase “under a finite observation task” is not enough to imply an
effective lowering theorem. Four additional boundaries are necessary.

1. **Input rank.** If variables range over arbitrary transseries, each assigned
   value has finite rank, but the term has no uniform rank bound independent of
   the assignment.
2. **Analytic bridge.** A formal transseries value and an analytic germ are not
   interchangeable without a stated evaluation/summation theorem.
3. **Observer algorithm.** A finite codomain does not make equality,
   positivity, branch selection, or coefficient extraction automatically
   decidable for opaque analytic inputs.
4. **Infinite operations.** Infinite sums, limits, implicit or differential
   equation solving, integration, and uniform iteration are absent from the
   theorem even when their source formula is written compactly.

The strongest eliminability claim should therefore be:

> All closed, well-typed finite exp/log DAGs over certified finite-stage LE
> inputs, including every fixed finite iterate, are surreal-eliminable for
> formal evaluation and any observer whose requested finite shadow is
> effectively extractable from that LE presentation.

It must not be shortened to “every finite symbolic task is surreal-eliminable.”

## 3. Carrier universe and operation signature are separate axes

### 3.1 Audited relation matrix

| Source | Target | What is established | What is not established |
|---|---|---|---|
| Finite germs | compatible Hahn presentation | Embedding of polynomial/finite-jet data | Closure of finite support under inversion/exp/log |
| Suitable Hahn stages | LE transseries | LE is built as a directed union of special Hahn fields | An arbitrary Hahn field or arbitrary monomial group embeds canonically into LE |
| LE transseries `T` | `No` | A unique ordered exponential-field embedding sending the transseries generator to `omega`, preserving summable families; with BM derivation it is elementary as an ordered differential-field embedding | Effective inverse lowering for arbitrary surreal values; total binary composition on all `No` |
| Logarithmic/hyperseries fields | `No` with hyperoperations | Compatible hyperseries subfields and embeddings commuting with transfinite sums and hyperexp/hyperlog are constructed under explicit hypotheses | Every such field has a finite executable encoding; every surreal-to-hyperseries representation is computable |
| `No` | hyperseries evaluated at `omega` | Every surreal is naturally representable as the value at `omega` of a hyperseries in the 2023 representation theorem | A bounded normal-form algorithm, bounded certificate, or cost domination over a smaller field |

### 3.2 The composition gap

The ordinary transseries embedding `T -> No` is structure-preserving for the
signatures proved in the cited theorems. It must not be silently upgraded to a
total internal composition law on arbitrary surreal outer and inner values.

The hyperserial-field paper's composition has the typed form

\[
  \mathbb L\times \mathbf{No}^{>,\succ}\longrightarrow \mathbf{No},
\]

where the outer argument is a logarithmic hyperseries and the inner argument is
a positive infinitely large surreal. Berarducci--Mantova likewise interpret
transseries as functions evaluated at positive infinite surreal arguments.
Neither statement is the untyped operation

\[
  \mathbf{No}\times\mathbf{No}\longrightarrow\mathbf{No}.
\]

The compiler must record the outer language, the inner domain, and the
preserved operations. A generic `supports_composition=true` flag would be
false documentation.

The same caution applies to derivation. The BM derivation makes `No` a
Liouville-closed H-field and the natural `T -> No` map is elementary as an
ordered differential-field embedding. That does not prove that every proposed
hyperserial composition, every hyperoperator, and every arbitrary surreal
representation has one total, effective chain-rule implementation.

### 3.3 Effectivity is not inherited by embedding

An embedding proves semantic realizability. A compiler needs more:

```text
finite or oracle-declared input representation
normalization and comparison procedure
truncation/observer extraction
operation-cost bound
independent certificate replay
lowering or residual representation
```

The cited surreal/hyperseries constructions use proper classes, transfinite
cuts, and well-based sums. They are powerful existence and structure theorems,
but they are not by themselves algorithms satisfying #142's budget contract.

## 4. Abel equation, tetration, and normalization

The issue writes

\[
  F(x+1)=\exp(F(x)). \tag{T}
\]

This is a tetration/continuous-iteration equation. If `F` has an invertible
branch and `A=F^{-1}`, then `A` satisfies the Abel equation

\[
  A(\exp y)=A(y)+1. \tag{A}
\]

The domain, range, and chosen inverse branch are part of the theorem; they
cannot be omitted.

### Lemma B (the functional equation is highly non-unique)

Suppose `F` solves (T) on a translation-stable domain `D`. If
`h:D -> D` satisfies `h(x+1)=h(x)+1`, then `G=F o h` also solves (T).

**Proof.**

\[
G(x+1)=F(h(x)+1)=\exp(F(h(x)))=\exp(G(x)).
\]

For example,

\[
 h_\varepsilon(x)=x+\varepsilon\sin(2\pi x),
 \qquad |\varepsilon|<(2\pi)^{-1},
\]

is a real-analytic increasing diffeomorphism commuting with translation by
one and fixing every integer. Hence even real analyticity, monotonicity, and
all integer-height normalization values do not give uniqueness whenever the
composition is defined.

The corresponding classical Abel nonuniqueness is explicit in
Bonet--Domanski: after choosing a real-analytic solution `f0`, solutions are
parametrized by real-analytic 1-periodic data. Their theorem also gives exact
conditions for real-analytic solvability for a real-analytic self-map and
recovers Kneser's global real-analytic Abel solution for `phi=exp`.

### Lemma C (conditional growth separation from finite LE height)

Let `F` be a positive eventually increasing germ satisfying (T), and suppose
`F(x0)>1` at some sufficiently large `x0`. Then along the integer translates,

\[
 F(x_0+n)=\exp^{[n]}(F(x_0)).
\]

Thus `F` is transexponential: it eventually dominates every fixed finite
iterate `exp^[k](x)` (after harmless changes of base point). In particular it
cannot be supplied by a bounded-height exp/log unrolling.

This is the mathematically honest C2 pressure. The eventual positivity and
monotonicity (or an equivalent growth normalization) matter: equation (T)
without a domain and regularity class does not itself establish an ordered
asymptotic germ.

Boshernitzan's primary work establishes existence of transexponential
functions in Hardy-field extensions. Later formal hyperseries constructions
supply operation-bearing representatives. These are different existence
theorems and should not be collapsed into one canonical function.

### 4.1 What the surreal construction earns

Bagayoko--van der Hoeven--Mantova construct a surreal hyperexponential
`E_omega` satisfying the translation/exponentiation relation on its declared
positive-infinite surreal domain, using Conway simplicity and uniform cut
equations. It is a strictly increasing bijection with reciprocal
`L_omega`. Bagayoko--van der Hoeven subsequently construct
`E_(omega^alpha)` and `L_(omega^alpha)` for every ordinal `alpha>0`; their
Theorem 1.1 uniquely extends the specified hyperserial skeleton and makes each
extended hyperlogarithm bijective.

The uniqueness is therefore **relative to the selected skeleton, cut
definition, and hyperserial axioms**. It is not uniqueness of solutions to (T)
alone; Lemma B rules that out.

### 4.2 What the surreal construction does not yet earn for this compiler

- It does not make a full surreal runtime necessary: a smaller hyperserial
  field can carry the same named hyperoperation.
- It does not provide a bounded certificate for arbitrary inputs; the defining
  recursions are transfinite.
- It does not establish that the best real-domain numerical evaluator should
  use surreal arithmetic. Kneser/Abel representations are an incomparable
  task-relative carrier for real analytic evaluation.
- It does not select a unique real tetration unless the exact normalization,
  regularity, domain, and branch conditions are stated.

## 5. Replacement for the C0--C4 ladder

Use a capability record, not one ordinal label:

```text
CarrierCapability = {
  universe,
  support_policy,
  exp_log_rank,
  hyperoperator_strengths,
  derivation,
  integration,
  composition_outer_language,
  composition_inner_domain,
  normalization,
  effective_operations,
  observer_extraction,
  replay_budget
}
```

If compact display labels remain useful, revise them as follows.

| Label | Safe meaning | Required refusal |
|---|---|---|
| C0 | Rational Newton weights and finite polynomial/analytic jets under a declared truncation | Exact infinite-series closure |
| C1f | Finite-support generalized polynomial presentation; not a field | Inversion/exp/log when support leaves the finite class |
| C1h | A specified well-based Hahn field or effective lazy Hahn fragment with named monomial group | Claim that arbitrary Hahn carriers embed into C2 |
| C2 | A specified finite-rank LE-transseries stage or the directed union with a per-value finite-rank witness | Symbolic/unbounded iteration and arbitrary solution operators |
| C3(alpha) | A specified hyperserial field with named hyperoperators through declared ordinal strength `alpha` | Any unimplemented strength, composition domain, or finite replay claim |
| C4e | `No` as ordered exponential field (plus only explicitly named extra structure) | Treating ambient size as hyperiteration capability |
| C4h(alpha) | `No` equipped with the proven hyperserial operations through `alpha` | Treating this as an effective runtime or total `No x No` composition |

This is a graph, not a chain:

```text
C0 -> compatible C1h -> C2
                       |\
                       | -> C3(alpha)
                       -> C4e          (transseries embedding)
C3(alpha) -> C4h(alpha)                (for compatible hyperseries embeddings)
C4e  -/-> C3(alpha)                    (ambient exp field lacks named hyperoperators)
```

Even these arrows are typed embeddings/operation extensions, not cost or
effectivity orderings.

## 6. C0--C4 gate corrections

### L0 — Bessel finite germ

Minimum remains C0 for the frozen observer. Any promotion is an error.

### L1 — finite nested exp/log

C2 is a sound upper bound once branches and input ranks are certified. It is
not automatically minimal: simplification can lower instances to C0 or C1h.
The required output is a stage witness plus failed-lowering obligations, not a
feature count alone.

### L2a — fixed finite height

Every fixed `n` is a finite DAG and supplies zero evidence for C3 or C4.

### L2b — uniform symbolic height

The frozen task must include a function/operator symbol and a law over an
unbounded height domain, plus a growth/normalization condition. A positive
eventually increasing solution to (T) gives a genuine bounded-height
obstruction by Lemma C. This can justify C3 pressure.

### L2c — C3/C4 discrimination

Equation (T), even with a standard hyperserial normalization, cannot presently
discriminate a smaller hyperserial field from `No` carrying the same
hyperoperators. A surreal-specific task would need, for example, a Conway
simplicity/birthday output or quantification over arbitrary surreal inputs.
That would separate by task definition, but it would not yet demonstrate a
natural software advantage; it risks baking the desired carrier into the
observer.

Therefore the proposed Abel gate should return one of:

```text
finite-height: surreal-eliminable / C2 upper bound
uniform hyperiteration: C2 obstruction + C3 conditional capability
surreal simplicity requested: C4 normalization required by observer
C3 versus C4 on operation-only task: incomparable-or-not-separated
numerical real-domain task: classical analytic carrier candidate
```

## 7. Exact claims, gaps, and kill conditions

### Earned claims

1. Finite, well-typed exp/log DAGs over finite-stage LE inputs have finite-stage
   lowering certificates.
2. Finite Hahn support is not closed under the advertised field operations.
3. Uniform positive monotone tetration is a genuine transexponential growth
   problem, unlike every fixed iterate.
4. The equation and ambient embeddings do not prove surreal necessity.
5. Current primary sources make C3 and C4h overlap in hyperiteration
   capability; effectivity remains a separate gate.

### Open or conditional claims

- a finite and independently replayable implementation of even a useful
  fragment of `E_omega`/`L_omega`;
- a lower bound comparing total certificate cost across a hyperseries field
  and a surreal representation;
- a natural task whose observer needs Conway simplicity rather than merely a
  hyperoperator;
- a generic analytic-germ-to-transseries bridge with controlled branches and
  error semantics;
- total composition or uniform derivative compatibility beyond the exact
  typed domains proved in the sources.

### Kill conditions for surreal necessity

Return **ELIMINATE** or **NARROW** if any of the following occurs:

- the witness is a fixed finite iterate;
- C1 is credited despite storing the full infinite series in an oracle;
- a `T -> No` or hyperseries-to-`No` embedding is counted as an algorithm;
- C4 means only “the value lies in `No`” without a No-specific operation or
  observer;
- `E_omega` existence is used without its domain and normalization;
- the equation alone is said to give uniqueness;
- a smaller hyperserial field replays the same certificate at equal or lower
  total cost;
- the task asks for Conway simplicity solely in order to force a surreal
  answer and has no independent computational use.

## 8. Recommended disposition

**NARROW.** The corrected carrier-capability compiler is mathematically useful,
and the uniform tetration workload supplies a real C2 obstruction. But the
present L2 gate does not separate hyperseries from surreal numbers, and no
effective C4 advantage is established. The best current result is a strong
eliminability theorem for finite DAGs plus a precise refusal boundary at
symbolic-height hyperiteration.

```text
Mathematical Core: unchanged
Research Programme: pressure on U1/U2/E; no universality promotion
Engineering Architecture: refine carrier label into orthogonal capabilities
Theory Map Change: none; T0/T1 research-local audit
Public API: none
```

## 9. Primary sources

1. L. van den Dries, A. Macintyre, D. Marker, “Logarithmic-exponential
   power series,” *J. London Math. Soc.* 56 (1997), 417--434.
   [DOI](https://doi.org/10.1112/S0024610797005437)
2. L. van den Dries, J. van der Hoeven, E. Kaplan, “Logarithmic
   hyperseries,” *Trans. AMS* 372 (2019), 5199--5241.
   [Author/arXiv manuscript](https://arxiv.org/abs/1810.01810)
3. A. Berarducci, V. Mantova, “Surreal numbers, derivations and
   transseries,” *JEMS* 20 (2018), 339--390.
   [Author manuscript](https://arxiv.org/abs/1503.00315)
4. A. Berarducci, V. Mantova, “Transseries as germs of surreal functions,”
   *Trans. AMS* 371 (2019), 3549--3592.
   [Author manuscript](https://arxiv.org/abs/1703.01995)
5. M. Aschenbrenner, L. van den Dries, J. van der Hoeven, “The surreal
   numbers as a universal H-field,” *JEMS* 21 (2019), 1179--1199.
   [Author manuscript](https://www.texmacs.org/joris/bm/bm.pdf)
6. V. Bagayoko, J. van der Hoeven, V. Mantova, “Defining a surreal
   hyperexponential” (2020).
   [Author manuscript](https://hal.science/hal-02861485)
7. V. Bagayoko, J. van der Hoeven, “The hyperserial field of surreal
   numbers” (2023), Theorem 1.1.
   [Author manuscript](https://arxiv.org/abs/2310.14873)
8. V. Bagayoko, J. van der Hoeven, “Surreal numbers as hyperseries” (2023),
   especially Theorems 1.1--1.2 and the typed composition in section 3.2.
   [Author manuscript](https://arxiv.org/abs/2310.14879)
9. V. Bagayoko, “Hyperseries subfields of surreal numbers” (2024).
   [Author manuscript](https://arxiv.org/abs/2409.16251)
10. M. Boshernitzan, “Hardy fields and existence of transexponential
    functions,” *Aequationes Math.* 30 (1986), 258--280.
    [DOI](https://doi.org/10.1007/BF02189932)
11. J. Bonet, P. Domanski, “Abel's functional equation and eigenvalues of
    composition operators on spaces of real analytic functions,” *Integral
    Equations Operator Theory* 81 (2015), 455--482.
    [Author manuscript](https://jbonet.webs.upv.es/wp-content/uploads/2014/04/BD_eigenvaluessubmitted03032014.pdf)
12. H. Kneser, “Reelle analytische Lösungen der Gleichung
    `phi(phi(x))=e^x` und verwandter Funktionalgleichungen,” *J. Reine Angew.
    Math.* 187 (1950), 56--67.
    [Bibliographic record](https://eudml.org/doc/150158)

No secondary survey or software documentation is used as authority for the
claims above.

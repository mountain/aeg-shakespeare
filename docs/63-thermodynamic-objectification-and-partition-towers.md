# Thermodynamic objectification and partition towers

**Status:** research-local T1 candidate.  The finite algebraic identities below
are exact; their interpretation as a general process-rank or classification
mechanism remains conjectural.  The V2/V3 boundary is refined without a new
Theory Map node, maturity promotion, or API proposal.

**Executable essays:**

- `tests/research/test_thermodynamic_objectification_partition_tower.py`;
- `tests/research/test_finite_twisted_cycle_partition.py`.

## 1. Why the research order changed

The earlier arithmetic-rank line asked how Addition histories become reusable
objects and how Multiplication objectifies a uniform Addition action.  The
partition-function discussion adds a different operation that must be audited
before another PCR3BP orbit census:

> many lower histories are aggregated into one task-visible object, while
> their multiplicity, cost, scale, and transported holonomy may survive as a
> partition payload.

This is not merely an observable placed on an already finished theory.
Partition functions expose three uses of an exponential plus an intervening
pushforward that the notation can hide:

1. a Boltzmann character sends serially additive cost to multiplicative
   weight;
2. a finite fibre pushforward sums alternative Boltzmann masses and reports
   their logarithm as an effective/free cost;
3. a plethystic exponential freely assembles objectified primitives;
4. a cycle exponential turns closed walks and their repetitions into a
   determinant or zeta series.

The pushforward flattens at a fixed scale when the measure is transported
correctly.  Plethystic assembly retains brackets and their degeneracy.  The
cycle exponential may retain a noncommutative holonomy character.  Their
separation supplies the next finite theory gate and determines what PCR3BP
Phase 2 must measure.

## 2. Minimal finite contract

Work first with a finite costed history system

\[
\mathfrak H=(\mathcal H,\circ,C,\mu,Q,\rho).
\]

The declared data are:

- a finite history set, or a finite truncation of a history category, with
  partially defined concatenation \(\circ\);
- an additive cost cocycle
  \(C(h\circ k)=C(h)+C(k)\) whenever concatenation is defined;
- a dimensionless positive ensemble/reference weight \(\mu(h)\);
- a task \(Q\), whose exact semantic quotient is required to be stable under
  every admissible continuation;
- an optional multiplicative payload
  \(\rho(h\circ k)=\rho(h)\rho(k)\), such as deck or connection holonomy.

An arbitrary finite map \(\pi:X\to Y\) supports a mass pushforward.  It is
called **task objectification** here only when its fibres are
continuation-stable for the declared task and the resulting objects have a
grounded composition/lowering semantics.  Otherwise it is only aggregation or
coarse-graining.

The reference weight is part of the contract.  A partition function without a
declared ensemble does not define probabilities, expected cost, or a Huffman
source.  Likewise, taking a logarithm of a dimensionful measure requires a
declared reference unit; the finite tests use dimensionless weights.

Only the cost character \(e^{-C/\theta}\) is automatically multiplicative
under concatenation.  The full Boltzmann mass
\(\mu(h)e^{-C(h)/\theta}\) is multiplicative only when the ensemble weight
itself factorizes, \(\mu(h\circ k)=\mu(h)\mu(k)\).  No such independence is
assumed by default.

## 3. What a declared unit one actually discretizes

Let \(u>0\) be a declared cost unit.  If every admissible history has

\[
C(h)\in u\mathbb N,
\]

then the integer grade \(n(h)=C(h)/u\) is exactly additive:

\[
n(h\circ k)=n(h)+n(k).
\]

For a general nonnegative continuous cost, Euclidean decomposition gives

\[
C(h)=u\,n(h)+r(h),
\qquad 0\le r(h)<u.
\]

Concatenation then obeys the exact carry law

\[
\begin{aligned}
\kappa(h,k)&=\left\lfloor\frac{r(h)+r(k)}u\right\rfloor,\\
n(h\circ k)&=n(h)+n(k)+\kappa(h,k),\\
r(h\circ k)&=r(h)+r(k)-u\kappa(h,k).
\end{aligned}
\]

Thus the pair \((n,r)\), not the integer \(n\) alone, is an exact unit-cell or
hybrid presentation of additive cost; the residual remains continuous in
general.  Forgetting \(r\) is a finite-resolution task quotient and is
legitimate only when the task tolerates that loss.  The unit
does not discretize the physical state or the topology by itself; a section,
event gate, or sampling rule is still required.

This also clarifies the role of objectified unit one.  A chosen unit supplies a
repeatable lower-rank object and an integer assembly grade.  Carries are the
residual information created when the lower process is not exactly commensurate
with that object.  A physical law may select \(u\); dimensional analysis alone
usually supplies only a scale family and does not prove canonicity.

## 4. The thermodynamic semiring

Fix a positive cost scale \(\theta\).  On
\(\overline{\mathbb R}=\mathbb R\cup\{+\infty\}\), define

\[
a\oplus_\theta b
=-\theta\log\left(e^{-a/\theta}+e^{-b/\theta}\right),
\qquad
a\odot b=a+b.
\]

The map

\[
\Phi_\theta(a)=e^{-a/\theta}
\]

is a semiring isomorphism

\[
(\overline{\mathbb R},\oplus_\theta,\odot)
\cong
(\mathbb R_{\ge0},+,\times).
\]

Here \(+\infty\) is the alternative-sum zero, \(0\) is the serial-product
unit, parallel alternatives use \(\oplus_\theta\), and serial additive costs
use \(\odot\).  In the zero-scale limit,

\[
\lim_{\theta\to0^+}a\oplus_\theta b=\min(a,b),
\]

so the finite-temperature law tropicalizes to min-plus Bellman arithmetic.

This is the exact sense in which an additive dynamical cost acquires a
multiplicative scale character.  At a fixed \(\theta\), however, the structure
is isomorphic to the ordinary nonnegative-real semiring.  The isomorphism by
itself is therefore not evidence for a non-flattenable arithmetic rank.

## 5. Finite thermodynamic pushforward

Let \(X\) be finite, \(\pi:X\to Y\), \(C_x\in\mathbb R\),
\(\mu_x>0\), and \(\theta>0\).  Define Boltzmann mass

\[
B_\theta(x)=\mu_xe^{-C_x/\theta}
\]

and, on every positive-mass fibre,

\[
Z_{\pi,\theta}(y)
=\sum_{\pi(x)=y}B_\theta(x),
\qquad
F_{\pi,\theta}(y)=-\theta\log Z_{\pi,\theta}(y).
\]

The free energy is relative to \(\mu\) and \(\theta\); it is not an intrinsic
energy of \(y\).  Rescaling every source weight by \(a>0\) shifts it by
\(-\theta\log a\).  Empty or zero-mass fibres must either be removed from the
codomain or assigned extended cost \(+\infty\).

### 5.1 Same-scale flattening theorem

For a second finite map \(\sigma:Y\to Z\), ordinary mass pushforward is
functorial:

\[
\sigma_*(\pi_*B_\theta)=(\sigma\pi)_*B_\theta.
\]

Equivalently,

\[
-\theta\log\sum_{\sigma(y)=z}
e^{-F_{\pi,\theta}(y)/\theta}
=
-\theta\log\sum_{\sigma\pi(x)=z}
\mu_xe^{-C_x/\theta}.
\]

If the outer level has a separate weight \(q_y>0\), its pullback must appear
in the direct expression:

\[
-\theta\log\sum_{\sigma(y)=z}
q_y e^{-F_{\pi,\theta}(y)/\theta}
=
-\theta\log\sum_{\sigma\pi(x)=z}
\mu_xq_{\pi(x)}e^{-C_x/\theta}.
\]

The executable measure red team obtains masses `3` and `2` when the pullback
factor is respectively retained and incorrectly discarded.

This yields a useful kill theorem:

> Repeated log-sum-exp at one scale, with one coherent measure-transport law,
> is only the associativity of finite mass pushforward.  Regrouping it cannot
> constitute arithmetic rank raising.

### 5.2 Different scales

Suppose an inner object has

\[
F_y=-\theta_0\log Z_y.
\]

Aggregating those objects at \(\theta_1\) gives

\[
F^{(2)}(z)
=-\theta_1\log
\sum_{\sigma(y)=z}q_y Z_y^{m},
\qquad
m=\frac{\theta_0}{\theta_1}.
\]

At \(m=1\) this is the same-scale theorem.  A positive integer \(m\) may have
an ordered-tuple interpretation when the underlying weights factorize.
Noninteger \(m\) has no automatic finite-combinatorial interpretation.

A unit conversion is not a new level.  Simultaneous rescaling

\[
C\mapsto\lambda C,
\qquad
\theta\mapsto\lambda\theta
\]

leaves every Boltzmann mass unchanged and sends \(F\mapsto\lambda F\).  A
claim of distinct characteristic scales must therefore be formulated using
dimensionless ratios and physical/task semantics, not numerical units.

## 6. The exact bridge to frontier/coarea cost

For a normalized finite stopping ensemble with \(T_i\ge0\),

\[
Z_Q(\beta)=\sum_i p_i e^{-\beta T_i},
\qquad
\sum_i p_i=1,
\]

the first two log-partition derivatives are

\[
-\left.\partial_\beta\log Z_Q\right|_{\beta=0}
=\mathbb E[T],
\qquad
\left.\partial_\beta^2\log Z_Q\right|_{\beta=0}
=\operatorname{Var}(T).
\]

Now assume additionally that the outcomes are leaves of a finite rooted prefix
tree, every edge has nonnegative additive cost \(c_e\),

\[
T_i=\sum_{e\in\operatorname{path}(i)}c_e,
\qquad
M_e=\sum_{i\succ e}p_i.
\]

Combining the first identity with the exact finite result in
`docs/62-task-covariant-complexity-coarea.md` gives

\[
\boxed{
-\partial_\beta\log Z_Q(0)
=\sum_i p_iT_i
=\sum_e c_eM_e
=\int_0^\infty\Pr(T>\tau)\,d\tau.
}
\]

Thus the partition function does not replace the process-volume/frontier
picture.  Its first cumulant recovers that exact volume, while higher
cumulants retain fluctuations that the mean frontier volume forgets.  With an
unnormalized base measure the log derivative returns the normalized weighted
mean, not the raw first moment.

## 7. Plethystic objectification is a different exponential

For

\[
f\in\mathbb N[[q_1,\ldots,q_d]],
\qquad f(0)=0,
\]

with finitely many primitive types in every declared grade, define

\[
\operatorname{PE}[f](q_1,\ldots,q_d)
=
\exp\left(
\sum_{k\ge1}\frac{f(q_1^k,\ldots,q_d^k)}k
\right).
\]

In this nonnegative-integral coefficient setting it is the generating series
for free symmetric/multiset assembly.  Over a general coefficient
\(\lambda\)-ring the definition must instead be written

\[
\operatorname{PE}[f]
=\exp\left(\sum_{k\ge1}\frac{\psi_k(f)}k\right),
\]

where the Adams operation \(\psi_k\) acts on coefficients as well as grading
variables.  That more general formal operation need not have a positive
counting interpretation and is not calibrated here.  The displayed
variable-substitution formula and executable tests use nonnegative integer
coefficients with their standard Adams action and verify

\[
\operatorname{PE}[q]=\frac1{1-q}
\]

and

\[
\operatorname{PE}\!\left[\frac q{1-q}\right]
=\prod_{n\ge1}\frac1{1-q^n},
\]

whose coefficients are the integer partition numbers.

A candidate objectification recursion is

\[
Z_{r+1}
=\operatorname{PE}\!\left[u_{r+1}(Z_r-1)\right].
\]

Each rank needs its own fugacity/grading.  The Adams operation acts on those
fugacities as well as on \(q\).  The subtraction of `1` prevents the lower
vacuum from becoming an ungraded zero-cost generator.  A separate formal
vacuum fugacity can regularize that factor, but at fugacity one it has infinite
degeneracy; the current positive-grading contract rejects it.

Plethystic nesting does **not** automatically flatten.  For one lower atom,

\[
[q^2]\operatorname{PE}[q]=1,
\qquad
[q^2]\operatorname{PE}[\operatorname{PE}[q]-1]=2.
\]

The two outer histories are:

```text
one rank-one object containing two atoms
two rank-one objects containing one atom each
```

Forgetting the brackets maps both histories to the same flat two-atom object,
but mass pushforward retains degeneracy `2`.  Reassigning that flat object unit
weight would be a new measure convention, not the same flattening operation.

## 8. Finite twisted cycles

Let a finite directed graph have edge cost \(c_e\), scalar weight \(m_e\),
deck label \(g_e\), and a finite-dimensional representation \(\rho\).  Its
block transfer matrix has entries

\[
K_{\beta,\rho}(i,j)
=\sum_{e:i\to j}m_e e^{-\beta c_e}\rho(g_e).
\]

For any finite matrix \(K\) over a commutative \(\mathbb Q\)-algebra, the
formal identity

\[
\boxed{
\det(I-zK)^{-1}
=\exp\left(\sum_{n\ge1}\frac{z^n}{n}\operatorname{Tr}K^n\right)
}
\]

holds.  The trace power is the character-weighted sum of based closed walks of
length \(n\).  More precisely, the \(k\)-fold repetition of a primitive cycle
of length \(\ell\) occurs with \(\ell\) choices of base point in
\(\operatorname{Tr}K^{k\ell}\); division by \(k\ell\) leaves its `1/k`
repetition weight.  The outer exponential then freely assembles these cycle
objects and yields the corresponding Euler product.

The exact one-vertex, two-loop red team uses the Phase-0 `Gamma(2)` matrices

\[
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},
\qquad
B=\begin{pmatrix}1&0\\-2&1\end{pmatrix}.
\]

The histories `aabb` and `abab` have the same scalar/abelianized weight, but

\[
\operatorname{tr}(A^2B^2)=-14,
\qquad
\operatorname{tr}((AB)^2)=2.
\]

Thus a scalar partition can forget a task-visible deck distinction that a
twisted transfer operator retains.  The trace still forgets a cycle base point
and may merge other nonconjugate histories; it is a declared character, not a
complete word decoder.  Its values can be negative or complex, so a twisted
cycle series is not necessarily a positive Gibbs partition function.

This finite identity does not establish a PCR3BP Markov partition,
hyperbolicity, convergence of a continuous transfer operator, or a Ruelle zeta
function.  Immediate inverse crossings would also require a nonbacktracking
state lift if the intended objects are reduced free-group words.

## 9. Three exponentials and the intervening pushforward

| Construction | Input operation | Output | Exact flattening boundary |
| --- | --- | --- | --- |
| Boltzmann character | serial cost addition | multiplicative weight | fixed-scale character is isomorphic to ordinary positive multiplication |
| finite free-energy pushforward | alternative histories in one fibre | object weight/free energy | same-scale nesting flattens only with coherent measure transport |
| plethystic exponential | graded primitives | free symmetric assemblies | brackets/degeneracies survive until explicitly quotiented |
| cycle exponential | primitive closed cycles and repetitions | trace/determinant series | retains only the declared representation character and cyclic data |

Counting occurrences of `exp` therefore says nothing about arithmetic rank.
A non-flattenable higher level requires a declared obstruction, such as:

- distinct physical/task scales rather than unit conversion;
- retained object type or assembly brackets;
- interactions, exclusions, or relations that break free factorization;
- a symmetry quotient with nontrivial stabilizer weights;
- noncommutative task-visible holonomy;
- a change of ensemble/reference measure;
- a renormalization map whose comparison law is additional structure.

## 10. Free combination, flatness, and universality

The user's geometric intuition can now be stated narrowly.  A **free reference
model** has:

- independently generated primitives;
- additive grading/cost under serial composition;
- factorized weights;
- no interaction relations beyond the declared symmetry of assembly.

For the free symmetric assembly type studied here, its partition series is a
product/plethystic exponential; ordered, cyclic, or other free assembly types
have different universal series.  The shared combinatorial sense of flatness
is the absence of an interaction correction to the declared free assembly
law.  It is not the same as zero metric curvature,
trivial connection holonomy, topological simple connectedness, or the
existence of a canonical scalar ruler.

Its universality is also relative.  A free object is universal for assignments
of its declared generators into another object of the same algebraic type.
That fact motivates the provisional classification coordinate

\[
\boxed{
\text{free reference model}
+\text{objectification/assembly type}
+\text{dynamical relations}
+\text{cost character and ensemble}
+\text{holonomy representation}
+\text{flattening obstruction}
+\text{task residual}.
}
\]

This tuple is a T0 candidate **process-geometry classification language**, not
a complete invariant.  Its T1 precision gate requires a declared comparison
map/equivalence, and an explicit ledger of what the tuple preserves and
forgets; the next PCR3BP finite return graph is intended to make those fields
measurable.  Independent systems plus a negative or degenerate boundary belong
to the later T2 calibration gate.  Arithmetic Geometric Universality remains
a stronger open conjecture.

## 11. Claim ledger and research order

### Exact finite theorems

1. thermodynamic-semiring isomorphism and min-plus degeneration;
2. same-scale weighted pushforward/Fubini law;
3. different-scale power-sum identity and common-unit covariance;
4. unit-cell carry law for discretized additive cost;
5. cumulant/frontier identity for a normalized finite stopping ensemble;
6. the two plethystic coefficient calibrations;
7. finite twisted trace-power and trace-determinant identities.

### T1 candidate

Continuation-stable thermodynamic pushforward, free assembly type, and
task-visible holonomy may form independent coordinates of a reusable
objectification/classification language.

The seven-field classification tuple itself remains T0 until its equivalence,
preservation, and forgetting contracts are completed.

### Interpretations, not theorems

- free factorization is a combinatorial flat reference geometry;
- a retained assembly boundary is a higher process rank;
- the obstruction tuple will classify useful continuous mathematical-physics
  processes.

### Revised execution order

```text
finite thermodynamic and cycle identities        complete in this note
    -> PCR3BP return--partition--holonomy contract
    -> converged finite/sub-Markov return graph
    -> task and gate-presentation red teams
    -> process-geometry classification record
    -> controlled Bellman/Huffman branch
    -> cross-domain universality audit.
```

## 12. Kill conditions

The stronger interpretation must be weakened or stopped if any of the
following occurs:

- a proposed task quotient is not continuation-stable;
- full history weights are factorized although the ensemble measure is not;
- outer weights are not pulled back but same-scale flattening is claimed;
- different fibres silently use different scales inside one semiring;
- a unit change is mistaken for a physical scale transition;
- an interaction/relation is present but free plethystic assembly is used;
- the grading is not positive or locally finite, so formal coefficients
  diverge;
- an infinite history sum lacks the convergence needed to exchange levels;
- scalar partitions erase task-visible holonomy without a twisted payload;
- a gate change does not transform the proposed PCR3BP invariants by the
  declared conjugacy/presentation law;
- the classification tuple cannot distinguish task-distinguishable processes;
- free-object universality is enlarged into arithmetic or analytic
  universality without a stated category, comparison map, and negative case.

## 13. Theory and software effect

```text
Epistemic maturity: T1 candidate; exact finite lemmas underneath
Role: reusable candidate
Evidence: symbolic finite positive cases plus measure, scale, vacuum,
          bracketing, scalarization, and cyclic-information red teams
Theory Map effect: refines the V2/V3 flattening boundary; no node or maturity promotion
Affected pressure: V2/V3 objectification/assembly, V5 closure, H3 complexity
Experimental/Public API pressure: none
```

The result refines the research program without promoting a generic
`PartitionTower`, `ThermodynamicObjectification`, or transfer-operator API.
The next implementation remains research-local and problem-driven.

## References

- D. Ruelle, *Thermodynamic Formalism*, 2nd ed., Cambridge University Press,
  2004.
- R. P. Stanley, *Enumerative Combinatorics*, vol. 2, 2nd ed., Cambridge
  University Press, 2011.
- R. Bowen and O. E. Lanford III, "Zeta functions of restrictions of the shift
  transformation," *Global Analysis*, Proc. Sympos. Pure Math. 14, 1970.

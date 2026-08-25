# Phase 5 — projective cylinders, discrete coarea, and coding

**Status:** Gate 5 exact finite source/coding calibration complete; projective
cylinder refinement, shell growth, root-symmetric mass transport, binary
Huffman construction, and decoding are certified; no selector-policy Bellman
problem, infinite boundary measure, entropy-rate theorem, or API proposal.

**Owner:** [test_local_field_projective_lattice_ball.py](../../tests/research/test_local_field_projective_lattice_ball.py)

## 1. The question left by Phase 4

Phase 4 closed one tempting but invalid route to optimization.  Ruban and
Browkin I did not take competing routes through the finite Bruhat--Tits ball:
on the bounded rational corpus, both materialized nondecreasing segments of
one input-directed ray.  A geodesic to two different stopping depths is not a
Bellman problem, and a list of digit histories without a source law or decoder
is not a Huffman problem.

Phase 5 asks the smaller question that can now be made exact:

> If a task distinguishes all projective cylinders at one fixed depth, what
> is the exact frontier growth, memory lower bound, source law, and binary
> prefix code?

This lets coding enter after its task data are declared.  It also gives an
independent discrete calibration of the Mathematical Core's separation among
history, evaluation geometry, task quotient, unit, and decoder.

## 2. Problem-native primitive audit

The primitive geometric data are:

1. an odd or even prime \(p\);
2. the standard lattice frame \(L_0=\mathbb Z_p^2\);
3. normalized valuation \(v_p(p)=1\), so one tree edge is one unit of lattice
   refinement;
4. primitive covectors modulo \(p^d\), quotiented by units;
5. the parent map induced by reduction from \(p^d\) to \(p^{d-1}\).

The depth-\(d\) task is to distinguish every normalized projective label

\[
S_d=\mathbb P^1(\mathbb Z/p^d\mathbb Z),
\]

and reconstruct its label after binary transmission.  The declared source is
the finite root-symmetric law that assigns equal mass to every element of
\(S_d\).

The following structures are forbidden imports:

- selector digits as codewords before a prefix-decoding theorem;
- the bounded rational test list as a probability law;
- Bruhat--Tits edges as binary code edges;
- an infinite-boundary or Haar-measure theorem inferred from finite counts;
- Bellman actions before a common selector-policy state and terminal task are
  specified.

The classical baselines are [Serre-Trees-1980], [Ludwig-Merten-2026], and
[Huffman-1952] in `docs/REFERENCES.md`; they are not new Process Geometry
ontology.

## 3. Four trees, not one

The current local-field line now forces four different structures to remain
separate.

```text
literal digit-prefix tree
    records every admissible selector history

matrix-evaluation image
    h_n |-> G_n = M(a_0)...M(a_n)

Bruhat--Tits lattice tree
    G_n |-> V_n = [G_n Z_p^2]

binary coding tree
    cylinder label |-> declared prefix codeword
```

The matrix product is a composable evaluation payload and may already identify
different literal histories.  Evaluation at the standard lattice forgets
additional right-integral and homothety information.  Stopping at depth \(d\)
then retains only the corresponding projective cylinder.  A binary coding tree
is introduced only after a source law and decoder are fixed.

None of these arrows makes the Bruhat--Tits tree the full history unfolding.
Nor is it being identified with the topological universal cover of a supplied
visible process.  It is the projective evaluation geometry selected by the
local-field observer.

For continued fractions the exact reconstruction identity remains

\[
\alpha_0=G_n\cdot\alpha_{n+1}.
\]

Thus the next complete quotient \(\alpha_{n+1}\) is retained residual/decoder
data for continuation.  The lattice vertex or finite contact alone cannot
reconstruct the future selector state.

## 4. Exact projective-cylinder refinement

Phase 1's normal forms give

\[
S_d=
\{[r:1]:r\bmod p^d\}
\sqcup
\{[1:pt]:t\bmod p^{d-1}\}.
\]

Consequently

\[
|S_d|=p^d+p^{d-1}=(p+1)p^{d-1}.
\]

The standard root has \(p+1\) children.  Every positive-depth cylinder has
exactly \(p\) children: its coordinate is extended by one base-\(p\) digit in
the same chart.  The executable oracle checks that the union of all children
of \(S_d\) is exactly \(S_{d+1}\), with no collision or omission, for
\(p=2,3,5\) through the declared finite depth.

This is a task quotient: two boundary directions agree at precision \(d\) iff
they lie in the same depth-\(d\) cylinder.  It is not a quotient of all literal
selector histories under all future continuations.

## 5. A discrete coarea calibration

Let \(B_d\) be the radius-\(d\) ball around the standard lattice.  Exact finite
counting gives

\[
|B_d|=1+(p+1)\frac{p^d-1}{p-1}
\]

and therefore

\[
|B_d|-|B_{d-1}|=|S_d|=(p+1)p^{d-1}.
\]

This is a discrete shell-increment identity: increasing longitudinal
resolution by one edge exposes one transverse frontier.  It is a useful
finite coarea calibration, but it is not the pendulum law
\(d\Omega=T\,dH\).  There is no physical period, energy thickness, or common
measure that would identify the two equations.

If the task distinguishes every element of \(S_d\), exact storage needs at
least

\[
b_d=\left\lceil\log_2 |S_d|\right\rceil
\]

bits.  At \(p=3\), depths \(1,2,3\) have respectively \(4,12,36\) cylinders
and lower bounds \(2,4,6\) bits.  The tree depth and transverse memory are
therefore related by the declared branching law but are not the same ruler.

## 6. Root-symmetric finite source

For the coding task, Phase 5 declares

\[
\mu_d(v)=\frac1{|S_d|},\qquad v\in S_d.
\]

This family is projectively consistent under parent reduction.  For \(d>1\),
every parent has \(p\) children and

\[
\sum_{w:\operatorname{parent}(w)=v}\mu_d(w)
=\frac{p}{(p+1)p^{d-1}}
=\mu_{d-1}(v).
\]

At the first sphere, all \(p+1\) masses push to unit mass at the root.  The
test checks these identities exactly with `Fraction`; no floating-point
probabilities or limiting boundary construction are used.

The law is deliberately named *root-symmetric finite source*.  Phase 5 does
not prove uniqueness or extend it to a measure on
\(\mathbb P^1(\mathbb Q_p)\).

## 7. Huffman enters as a separate task tree

Given a finite positive probability vector on \(S_d\), the executable oracle
runs exact binary Huffman merging, constructs a deterministic canonical prefix
code from the resulting lengths, and round-trips a message through the decoder.
The cost unit is one binary decision, not one projective edge or one
continued-fraction digit.

For \(p=3,d=2\), the geometric frontier contains twelve cylinders.  Under the
uniform source, the optimal binary lengths consist of four words of length
three and eight of length four, with exact expected length

\[
\bar\ell_{\mathrm{uniform}}=\frac{11}{3}\ \text{bits}.
\]

Keep the same twelve cylinders and parent relations, but assign mass \(1/2\)
to one cylinder and \(1/22\) to each of the other eleven.  Huffman gives the
heavy cylinder length one and exact expected length

\[
\bar\ell_{\mathrm{skewed}}=\frac{61}{22}\ \text{bits}.
\]

The projective geometry is unchanged while the optimal coding tree changes.
This is the decisive red team against any claim that the Bruhat--Tits tree, its
standard root, or its edge unit already chooses a Huffman tree.

## 8. What this says about selector sections

Ruban and Browkin choose different rational representatives of the same local
contact.  They are sections of the observer quotient

\[
\mathbb Q_p\longrightarrow\mathbb Q_p/p\mathbb Z_p,
\]

not unit frames and not fundamental domains for the Bruhat--Tits tree.  Right
reciprocal continuation can distinguish their representatives, so the section
choice affects the residual evolution even when the finite contact agrees.

Phase 5 codes fixed-depth projective cylinders rather than selector histories.
That choice is intentional: it supplies a complete source alphabet and decoder
without pretending that selector outcomes already share a terminal contract.
The Phase 4 common-ray result explains how selector prefix vertices can be
compared with a cylinder frontier, but it does not yet turn section choice into
an admissible control action.

## 9. Effective-analysis and solver-plan audit

- **Problem/task:** encode and reconstruct one finite depth-\(d\) projective
  cylinder under a declared source law.
- **Primitive process:** projective residue refinement from the standard
  lattice; no selector or coding ontology is assumed.
- **Mode:** exact finite symbolic arithmetic over integers and `Fraction`.
- **Units:** normalized valuation gives the projective edge ruler; binary bits
  give the separate code-cost ruler.
- **Lift/residual:** cylinder labels retain the declared finite contact;
  continued-fraction reconstruction would additionally require the matrix and
  next complete quotient, which this coding task does not claim to provide.
- **Algorithm:** exact frontier enumeration, parent pushforward, binary
  Huffman merging, canonical-code materialization, and prefix decoding.
- **Evaluator:** sphere/ball counts, child partitions, pushed masses, code
  lengths, expected costs, and decoded messages.
- **Certificates:** exact cardinality and shell identities, mass conservation,
  prefix-freeness, and message round trip.
- **Failure semantics:** empty alphabets, nonpositive or nonnormalized weights,
  invalid code lengths, nonbinary streams, and incomplete suffixes are
  rejected.
- **Baseline:** classical finite Bruhat--Tits sphere counts and Huffman coding.
- **Budget:** \(p\in\{2,3,5,7\}\), depth at most four for counts, and a
  twelve-symbol exact coding red team; routine runtime remains seconds-scale.
- **Costs:** longitudinal depth, frontier cardinality, exact memory bound, and
  expected binary length remain separate axes.
- **Decoder:** an explicit canonical prefix table; no implicit geometric
  decoder.
- **Dependencies/API:** standard-library research-local code only; no package
  or API surface change.

## 10. Mathematical Core, architecture, and Theory Map effects

### Mathematical Core — refine

Phase 5 refines the observer/evaluation chain to

```text
literal history -> composable payload -> observer geometry
                -> task cylinder + retained residual -> decoder
```

and supplies an independent discrete shell calibration.  It strengthens, but
does not unify, the distinction between continuous coarea and finite memory.
It also adds concrete negative controls: an evaluation tree is not a history
tree; a quotient section is not a unit or fundamental domain; a geometry tree
is not a coding tree.

### Engineering Architecture — refine

The phase refines the finite stopping/coding path.  Source alphabet,
probability, primitive cost, canonical code, decoder, and exact failures are
all explicit before optimization.  It supports task adequacy before cost,
explicit residuals, exact-domain claims, multi-axis cost, and decoder-inclusive
results.  It introduces no reusable solver façade.

### Theory Map — refine without promotion

The result sharpens the emerging task-covariant evaluation transversal at H2
and H3: projective refinement supplies locality/frontier structure; a declared
source and decoder then supply one finite coding shadow.  The transversal
remains T0/T1, H3 receives no generic entropy object, and no API maturity
changes.

## 11. Claim boundary

Phase 5 proves exact statements only for the finite projective normal forms and
finite binary source-coding tasks implemented by the oracle.  It proves no
infinite Bruhat--Tits boundary completion, invariant boundary probability,
entropy rate, selector code, convergence theorem, Lagrange theorem, Bellman
optimal policy, or preferred \(p\)-adic continued fraction.

The phrase *discrete coarea* refers only to the exact shell increment
\(|B_d|-|B_{d-1}|=|S_d|\).  It is not evidence for a universal
time--space product law.

## 12. Next gate

Huffman has now entered on a complete finite task.  Bellman still has not.  A
responsible selector-policy phase must freeze:

1. a common input/source law and a fixed projective-cylinder precision;
2. a state containing the complete quotient and every residual needed for
   continuation;
3. admissible section/lift actions independent of the two hard-coded classical
   policies;
4. a shared success decoder and explicit cycle, horizon, and failure penalties;
5. separate digit, projective-edge, serialization, decoder, and computation
   costs;
6. an exact comparison with fixed Ruban and Browkin baselines.

Only that contract would turn section choice into a finite control problem.

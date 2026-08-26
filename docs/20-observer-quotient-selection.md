# Observable algebraic-image selection: candidate family to Pareto presentation

**Status:** second discovery-front-end step; bounded candidate family, exact
algebraic-image certificates, reusable multi-axis cost.

## 1. The remaining manual choice after invariant discovery

The first polynomial discovery layer changed the pendulum reconstruction from

```text
supplied energy -> supplied cubic
```

to

```text
constrained process -> discovered invariant
-> invariant leaf -> selected observable -> discovered cubic.
```

One conspicuous prior choice remained: the caller still selected the vertical
coordinate `q_y` before algebraic elimination.

This note removes that choice inside a declared candidate family.

## 2. Fixed task: first-order algebraic closure

For every observable candidate `F`, Process Geometry constructs the first
process pair

\[
(U,Y)=(F,DF)
\]

and asks whether source assignments can be eliminated to leave a certified algebraic relation among `U`, `Y`, and declared leaf parameters.

The fixed task in this search is therefore narrow and explicit:

> find a compact first-order observable algebraic-image presentation.

A candidate is structurally admissible only when at least one exact relation is returned and every pullback certificate vanishes in the source constraint quotient.

This is not yet a claim of sufficiency for every physical or computational task.

## 3. Reusing `PresentationCost`

`search_first_order_observable_presentations` does not introduce a separate
optimization ontology. Each evaluated observable is wrapped in the existing
generic `PresentationCandidate` and compared through `PresentationCost`.

The default baseline uses:

- `grammar`: structural expression cost of `F` and `DF`;
- `relations`: for each eliminated polynomial, total degree plus monomial support;
- `history`: `1`, because the presentation uses the first-order pair `(F,DF)`;
- `decoder`: `0` at this stage;
- `task_error`: `0` for certified algebraic closure and infinity otherwise.

The result is filtered by the existing Pareto mechanism. Callers may replace the cost model; degree-plus-support is a transparent first proxy, not a canonical notion of mathematical simplicity.

## 4. Pendulum discovery II

Start from the invariant leaf already reached in the preceding vignette:

\[
q_x^2+q_y^2=1,
\qquad
q_xv_x+q_yv_y=0,
\qquad
v_x^2+v_y^2+2q_y=K.
\]

Do not declare which position component is preferred. Supply only the candidate
family

\[
\{q_x,q_y\}.
\]

Both candidates admit exact first-order algebraic closure.

For

\[
U=q_y,
\qquad
Y=Dq_y=v_y,
\]

elimination gives the cubic

\[
\boxed{Y^2=(K-2U)(1-U^2).}
\]

For the horizontal observable `q_x`, the corresponding eliminated relation
contains degree-six terms. The two observables have the same baseline grammar
and history cost, but the vertical observable has strictly lower relation cost.
It therefore Pareto-dominates the horizontal observable.

The important change in explanatory order is:

```text
classical:
    gravity suggests vertical coordinate -> derive simple quadrature

Process Geometry:
    position-observable family -> derive every algebraic image
    -> compare certified presentation costs
    -> gravity-aligned coordinate emerges as cheaper.
```

No special rule says that gravity coordinates are good. The asymmetry appears
in the process and is measured after algebraic-image construction.

## 5. What has and has not been automated

The choice

```text
qx versus qy
```

is now executable search.

The earlier choice

```text
why are qx and qy the candidate family?
```

is still supplied by the caller. Bare `ProcessSystem.assignments` do not yet record that `qx,qy` are components of one position object while `vx,vy` are components of velocity.

This exposed the next research experiment: a **structured observable proposal
grammar** accepting primitive geometric data such as vector blocks, pairings,
distinguished directions, and allowed constructions. It remains Experimental
until independent examples justify a stable grammar.

For the pendulum, such a layer should be able to propose

\[
\langle q,q\rangle,
\quad
\langle q,v\rangle,
\quad
\langle v,v\rangle,
\quad
\langle e,q\rangle,
\quad
\langle e,v\rangle
\]

without those scalar observables being hand-written.

That is a narrow bridge from the current polynomial search backend to
construction-preserving proposal generation. It does not, by itself, satisfy
the Mathematical Core's stronger objectification criteria.

## 6. Next threshold

The immediate next target was therefore not a larger special-function library.
It was a bounded structured-construction experiment for observable proposals:

```text
primitive geometric objects + allowed operations
    -> construction-preserving observable proposals
    -> invariant / algebraic-image discovery
    -> presentation cost
    -> task filtering / Pareto selection.
```

The pendulum experiment now tests whether `U=<e,q>` emerges from primitive
vector data rather than assignment names. The grammar remains Experimental
until Euler top, Kepler, or another independent family forces compatible
semantics.

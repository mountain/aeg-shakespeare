# Observer quotient selection: from candidate family to Pareto presentation

**Status:** second discovery-front-end step; bounded candidate family, exact quotient certificates, reusable multi-axis cost.

## 1. The remaining manual choice after invariant discovery

The first polynomial discovery layer changed the pendulum reconstruction from

```text
supplied energy -> supplied cubic
```

to

```text
constrained process -> discovered invariant
-> invariant leaf -> selected observer -> discovered cubic.
```

One conspicuous prior choice remained: the caller still selected the vertical coordinate `q_y` before quotient elimination.

This note removes that choice inside a declared candidate family.

## 2. Fixed task: first-order algebraic closure

For every observer candidate `F`, Shakespeare constructs the first process jet

\[
(U,Y)=(F,DF)
\]

and asks whether source assignments can be eliminated to leave a certified algebraic relation among `U`, `Y`, and declared leaf parameters.

The fixed task in this search is therefore narrow and explicit:

> find a compact first-order algebraic quotient presentation.

A candidate is structurally admissible only when at least one exact relation is returned and every pullback certificate vanishes in the source constraint quotient.

This is not yet a claim of sufficiency for every physical or computational task.

## 3. Reusing `PresentationCost`

`search_first_order_process_quotients` does not introduce a separate optimization ontology. Each evaluated observer is wrapped in the existing generic `PresentationCandidate` and compared through `PresentationCost`.

The default baseline uses:

- `grammar`: structural expression cost of `F` and `DF`;
- `relations`: for each eliminated polynomial, total degree plus monomial support;
- `history`: `1`, because the presentation uses the first process jet;
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

Do not tell Shakespeare which position component is preferred. Supply only the candidate family

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

For the horizontal observer `q_x`, the corresponding eliminated relation contains degree-six terms. The two observers have the same baseline grammar and history cost, but the vertical observer has strictly lower relation cost. It therefore Pareto-dominates the horizontal observer.

The important change in explanatory order is:

```text
classical:
    gravity suggests vertical coordinate -> derive simple quadrature

Shakespeare:
    position-observer family -> derive every quotient
    -> compare certified presentation costs
    -> gravity-aligned coordinate emerges as cheaper.
```

No special rule says that gravity coordinates are good. The asymmetry appears in the process and is measured after quotient construction.

## 5. What has and has not been objectified

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

This exposes the next architectural requirement: **structured observer proposal grammars**. A later layer should accept primitive geometric data such as vector blocks, pairings, distinguished directions, and allowed constructions, then generate observer families while preserving their construction histories.

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

That is the natural bridge from the current polynomial search backend to Shakespeare's existing construction-history/objectification machinery.

## 6. Next threshold

The immediate next target is therefore not a larger special-function library. It is a typed construction layer for observer proposals:

```text
primitive geometric objects + allowed operations
    -> construction-preserving observer proposals
    -> invariant / quotient discovery
    -> presentation cost
    -> objectification / Pareto selection.
```

Once this exists, the pendulum can test whether `U=<e,q>` emerges from the primitive vector process rather than from assignment names. The same machinery can then be carried to Euler top, Kepler, and other constrained systems.

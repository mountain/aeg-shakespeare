# Phase 7b — continuous A/M contact calculus and Huffman history geometry

**Status:** active calibration.  This is the first Sonnet-001 step in which the
A/M **calculus itself** generates the task history.  The earlier Phase-7a finite
orbit experiment used the algebraic shadow of Multiplication but did not yet use
continuous process/contact evolution.

Executable calibration:

```text
tests/research/test_lonely_runner_am_contact_huffman.py
```

## 1. Continuous contact process

Write a positive relative speed as

\[
u=e^v.\]

For Lonely Runner threshold

\[
\delta=\frac1{k+1},
\]

the lifted boundaries of one bad interval are

\[
\tau_{n,\pm}(v)=e^{-v}(n\pm\delta).
\]

Therefore the multiplicative process coordinate satisfies the exact differential
law

\[
\boxed{\frac{d\tau}{dv}=-\tau.}
\]

The infinite contact train of one runner is thus one primitive pattern transported
by the M flow.  It is not a generic list of interval endpoints.

For two contact events

\[
\tau_i=e^{-v_i}\alpha,
\qquad
\tau_j=e^{-v_j}\beta,
\]

the order changes only on the wall

\[
\boxed{v_j-v_i=\log(\beta/\alpha).}
\]

Hence relative M space is cut into contact-order chambers by exact wall-crossing
equations.  The discrete event history is the shadow of this continuous A/M
calculus.

## 2. Contact means before / on / after, not only interval combinatorics

The weak inequality in Lonely Runner matters.  At a contact instant the runner
is safe even if it is bad immediately before or after.

The calibration `(u_1,u_2)=(1,2)` at `delta=1/3` is the smallest useful red team.
At

\[
t=\frac13,
\]

runner 1 exits one bad interval exactly when runner 2 enters another.  There is
no open safe interval after the event, but **at the contact point itself both are
safe**.

Thus an interval-only set model can erase a genuine witness.  The contact process
must retain three states:

```text
bad-before
bad-on-contact
bad-after
```

This is the first place in Sonnet 001 where the contact calculus contains task
information not faithfully represented by a naive open-interval combinatorial
picture.

## 3. Fixed jets fail the transfer discipline

A natural first attempt is to truncate the contact history after a fixed number
of events and use that as a process jet.

On the finite training world of all distinct positive speed pairs bounded by 12:

```text
7-event jet   unsafe
8-event jet   sufficient for the first-witness task
```

But freezing the 8-event jet and moving to the larger held-out world bounded by
16 produces unsafe merges.

So there is no evidence for a universal fixed contact-jet order.  Choosing a
larger and larger fixed derivative/history depth simply recreates the original
state explosion.

The correct object should instead be a **variable-depth stopping geometry**.

## 4. The AM contact stopping tree

For each speed pair, follow the exact contact process and stop at the first event
whose on-contact observer has no bad runner.  The terminal record keeps the
contact event that certifies the lonely witness; the actual time is decoded from
the original speed and the event index.

On the speed-pair world

```text
1 <= u_1 < u_2 <= 12
```

there are 66 literal input pairs.

The scale-free stopping histories have boundary widths

```text
depth:  0 1 2 3 4 5 6 7 8 9 10
width:  1 1 3 3 4 3 3 3 3 1  1
```

Therefore

\[
\boxed{\max_d W(d)=4}
\]

and the peak information width is only

\[
\boxed{\max_d\log_2 W(d)=2\text{ bits}.}
\]

This is the first genuinely space-time geometric compression result in the
AM-first line.  The 66 literal parameter instances do not produce a 66-wide
process frontier; after passing through the continuous contact process, at every
stopping depth only four history shapes remain distinguishable in this
calibration.

The average stopping depth is

\[
\frac{215}{66}\approx3.258
\]

contact events.

Thus the same tree exposes both axes:

- frontier width / information width — space-like representation complexity;
- root-to-stop depth — time-like process complexity.

## 5. Huffman gives a target for further objectification

The 66 inputs collapse to 13 distinct first-witness task classes.  With uniform
weight on literal input pairs, the current `huffman_prefix_code` implementation
gives an optimal binary expected representation depth

\[
\boxed{L_H\approx2.545.}
\]

The current AM contact stopping process has average depth

\[
L_{AM}\approx3.258,
\]

leaving a gap

\[
\boxed{L_{AM}-L_H\approx0.712.}
\]

This gap is not yet a theorem saying that a physical contact computation can be
made exactly that short.  Huffman assumes a freely chosen binary prefix tree once
the task symbols and weights are fixed.  But it gives Shakespeare a concrete
**representation target**:

> the AM contact calculus has already collapsed the space-like frontier; search
> for reusable process primitives / shortcuts that reduce stopping depth toward
> the task-information depth without reopening the frontier.

This is precisely the role intended for history geometry in Shakespeare.

## 6. Representation ladder under the same task

For the same 66 speed pairs, consider three terminal presentations of the first
witness task.

### Literal absolute speed pair

```text
terminal classes: 66
peak information width: log2(66) ~= 6.04 bits
Huffman expected depth: ~= 6.06
```

### Relative M coordinate

Global M scale is removed:

```text
terminal classes: 45
peak information width: log2(45) ~= 5.49 bits
Huffman expected depth: ~= 5.26
```

### Contact-task quotient generated by the continuous process

```text
terminal classes: 13
peak information width: log2(13) ~= 3.70 bits
Huffman expected depth: ~= 2.55
```

Thus the calculus-derived quotient improves both history-geometry axes over the
absolute and simple relative-coordinate presentations on this task.

The stronger stopping-tree result is different again: its *intermediate* frontier
never exceeds four states even though the terminal witness labels have thirteen
classes.  This separation between process frontier and terminal code is exactly
why one scalar class count is not an adequate representation metric.

## 7. What this changes about the optimization problem

The representation objective should no longer be

```text
minimize number of states
```

or

```text
minimize algebraic expression size
```

alone.

For a candidate presentation `P`, the next AM-only search should expose at least

\[
\boxed{
\left(
\text{boundary information profile } I_P(d),
\text{expected stopping depth},
\text{worst stopping depth},
\text{task error},
\text{primitive/decoder cost}
\right).
}
\]

A useful one-number diagnostic may later be a discrete process integral such as

\[
\sum_d \Pr(\text{reach }d)\,I_P(d),
\]

but this should remain secondary to the full Pareto geometry until its meaning is
better calibrated.

## 8. Next experiment: search for contact shortcuts, still inside AM

Do **not** open Gate B yet.

The next discovery problem is now sharply defined:

1. generate continuous A/M contact histories on solved finite worlds;
2. compute their exact stopping/task quotient;
3. mine repeated contact subhistories or wall-comparison motifs as candidate new
   primitives;
4. rebuild the prefix/stopping tree after each proposed objectification;
5. score boundary width and stopping/Huffman depth together;
6. freeze the winning AM presentation;
7. transfer it to a larger solved holdout before touching the open `K=13` data.

The desired result is not another manually chosen quotient.  Shakespeare should
**discover shortcuts because they reduce process-history geometry**.

## 9. Claim boundary

This phase does not yet provide a faster proof of any new Lonely Runner case.
The current continuous calibration is only two-relative-runner geometry.

What it does establish is more foundational for the purpose of this Sonnet:

\[
\boxed{
\text{A/M differential contact flow}
\to
\text{wall-crossing history}
\to
\text{variable stopping tree}
\to
\text{space/time history geometry}
\to
\text{an explicit optimization target}.
}
\]

That is the first point where the new calculus, rather than only finite M
symmetry, participates essentially in the representation search.

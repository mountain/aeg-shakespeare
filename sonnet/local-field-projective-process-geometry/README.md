# Local-field projective process geometry

**Status:** T0 research-local calibration; Phase 0 exact finite certificates;
no Bruhat--Tits reconstruction, no preferred \(p\)-adic continued fraction,
and no Experimental or Public API proposal.

This Sonnet asks whether one rational arithmetic history can acquire two
genuinely different but strictly comparable geometries when the observer
changes place:

\[
\text{rational Addition/Multiplication/inversion histories}
\longrightarrow
\begin{cases}
|\cdot|_\infty & \text{Archimedean scale and real continued-fraction coding},\\
|\cdot|_p & \text{valuation scale and non-Archimedean refinement}.
\end{cases}
\]

The algebraic carrier is already forced by the bilateral AEG lineage.  Pure
left-slot histories remain in the affine/Borel sector stabilizing infinity;
right-slot division introduces inversion and the full projective language.
The new question is not whether \(PGL_2(K)\) can be written down, but whether
the current Process Geometry foundation can explain how an observer, ruler,
and task select an effective local-field presentation without erasing history
or declaring a global canonical form by fiat.

Read in order:

1. [00-problem-frontier.md](00-problem-frontier.md) freezes the primitive
   audit, observer semantics, hypotheses, forbidden imports, and kill
   conditions;
2. [01-phase0-finite-certificates.md](01-phase0-finite-certificates.md)
   records the exact first certificates, the digit-section red team, and the
   next evidence gates;
3. [`tests/research/test_local_field_projective_process_geometry.py`](../../tests/research/test_local_field_projective_process_geometry.py)
   is the seconds-scale executable argument.

## Current result

Phase 0 proves only the following finite or algebraic facts:

- the same rational multiplication history \(1\mapsto p^n\) escapes in the
  Archimedean ruler and approaches zero in the \(p\)-adic ruler;
- residue observations modulo \(p^n\) form a nested \(p\)-ary refinement;
- Addition preserves \(p\)-adic separation while Multiplication transports it
  by the exact valuation cocycle;
- left affine maps fix the projective point at infinity and right inversion
  exchanges zero with infinity;
- finite right-reciprocal histories lower exactly to chronological
  \(2\times2\) matrix products and continued-fraction convergents;
- Möbius maps transport \(p\)-adic resolution by an exact denominator law;
- standard and balanced digit sections reconstruct the same finite semantic
  residue but are preferred by different cost rulers.

The last item is a negative certificate against an observer-free claim of
canonical digits.  It is not evidence against task-relative canonicalization.

## Claim boundary

The nested ball/refinement tree used in Phase 0 is a boundary shadow.  It is
not named or treated as the full Bruhat--Tits tree, whose vertices require
homothety classes of lattices (or an equivalent coset construction).  The
continued-fraction certificate concerns finite right-reciprocal histories; it
does not select among competing \(p\)-adic digit algorithms or claim their
convergence, finiteness, or Lagrange periodicity.

At this stage the study **supports** H0/H1/H2 of the living Theory Map and the
unit/ruler discipline of the Effective Analysis Principle.  It leaves the
Theory Map unchanged.  The residue-resolution tower is horizontal observer
refinement, not yet a vertical arithmetic process-rank transition.

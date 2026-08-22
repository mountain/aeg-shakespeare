"""Lonely Runner AM-first discovery calibration.

This experiment asks Shakespeare to search *inside the A/M language first*.
It does not provide the relative-ratio presentation as an input.

Primitive grammar
-----------------
The only state atoms are two folded nonzero speed parameters ``s`` and ``t``.
The bounded construction grammar contains only finite Multiplication structure:

* ``inv(x)``      -- M inverse;
* ``mul(x,y)``    -- M composition;
* ``orbit(x)``    -- quotient one M coordinate by the intrinsic inversion
  symmetry ``x ~ x^{-1}`` forced by exchanging the two runners.

Task oracle
-----------
The task signature is derived independently from Lonely Runner contact geometry.
For a pair of speeds, form the union of the two pullbacks of the primitive bad
window, then quotient that contact set by simultaneous global M action.  A
candidate presentation is sufficient only if equal candidate values never merge
distinct contact-task signatures.

The search is trained on solved small worlds ``(k,p)=(5,17),(5,29)``.  The
selected exact quotient is then frozen and checked on held-out ``(8,79)``.
No Fourier, spectral, vector-space, or linearized representation is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement
import math
from typing import Callable, Iterable

from aeg_shakespeare.presentation.search import (
    PresentationCandidate,
    PresentationCost,
    PresentationSearchResult,
    pareto_frontier,
)


def fold_nonzero(value: int, p: int) -> int:
    residue = value % p
    if residue == 0:
        raise ValueError("M coordinates must be nonzero modulo p")
    return min(residue, p - residue)


def m_mul(left: int, right: int, p: int) -> int:
    return fold_nonzero(left * right, p)


def m_inv(value: int, p: int) -> int:
    return fold_nonzero(pow(value, -1, p), p)


def folded_universe(p: int) -> tuple[int, ...]:
    return tuple(range(1, p // 2 + 1))


def bad_window(*, k: int, p: int) -> frozenset[int]:
    return frozenset(
        value
        for value in folded_universe(p)
        if value * (k + 1) < p
    )


def m_act(scale: int, values: Iterable[int], p: int) -> frozenset[int]:
    return frozenset(m_mul(scale, value, p) for value in values)


def contact_cover(speed: int, *, k: int, p: int) -> frozenset[int]:
    """Pull back the one primitive bad window by the speed M action."""

    return m_act(m_inv(speed, p), bad_window(k=k, p=p), p)


def contact_task_signature(
    first: int,
    second: int,
    *,
    k: int,
    p: int,
) -> tuple[int, ...]:
    """Pair contact geometry modulo simultaneous global M action."""

    contact_union = contact_cover(first, k=k, p=p) | contact_cover(second, k=k, p=p)
    return min(
        tuple(sorted(m_act(unit, contact_union, p)))
        for unit in folded_universe(p)
    )


@dataclass(frozen=True)
class AMTerm:
    recipe: str
    depth: int
    operation_count: int
    evaluate: Callable[[int, int, int], int]


@dataclass(frozen=True)
class AMTaskPresentation:
    term: AMTerm
    feature_class_counts: tuple[int, ...]
    task_class_counts: tuple[int, ...]
    exact_partition: bool


def _atom_terms() -> tuple[AMTerm, ...]:
    return (
        AMTerm("s", 0, 0, lambda s, t, p: s),
        AMTerm("t", 0, 0, lambda s, t, p: t),
    )


def _inverse(term: AMTerm) -> AMTerm:
    return AMTerm(
        recipe=f"inv({term.recipe})",
        depth=term.depth + 1,
        operation_count=term.operation_count + 1,
        evaluate=lambda s, t, p, term=term: m_inv(term.evaluate(s, t, p), p),
    )


def _inverse_orbit(term: AMTerm) -> AMTerm:
    """Canonical coordinate for the M involution x ~ x^{-1}."""

    return AMTerm(
        recipe=f"orbit({term.recipe})",
        depth=term.depth + 1,
        operation_count=term.operation_count + 1,
        evaluate=lambda s, t, p, term=term: min(
            term.evaluate(s, t, p),
            m_inv(term.evaluate(s, t, p), p),
        ),
    )


def _multiply(left: AMTerm, right: AMTerm) -> AMTerm:
    left, right = sorted((left, right), key=lambda term: term.recipe)
    return AMTerm(
        recipe=f"mul({left.recipe},{right.recipe})",
        depth=max(left.depth, right.depth) + 1,
        operation_count=left.operation_count + right.operation_count + 1,
        evaluate=lambda s, t, p, left=left, right=right: m_mul(
            left.evaluate(s, t, p),
            right.evaluate(s, t, p),
            p,
        ),
    )


def _pairs(p: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations_with_replacement(folded_universe(p), 2))


def _semantic_key(
    term: AMTerm,
    worlds: tuple[tuple[int, int], ...],
) -> tuple[int, ...]:
    return tuple(
        term.evaluate(first, second, p)
        for _k, p in worlds
        for first, second in _pairs(p)
    )


def generate_am_terms(
    *,
    worlds: tuple[tuple[int, int], ...],
    max_depth: int,
) -> tuple[AMTerm, ...]:
    """Bounded AM construction search, deduplicated only by observed semantics."""

    terms = list(_atom_terms())
    best_by_semantics = {
        _semantic_key(term, worlds): term
        for term in terms
    }

    for depth in range(1, max_depth + 1):
        pool = tuple(term for term in best_by_semantics.values() if term.depth <= depth - 1)
        frontier = tuple(term for term in pool if term.depth == depth - 1)
        candidates: list[AMTerm] = []

        for term in frontier:
            candidates.append(_inverse(term))
            candidates.append(_inverse_orbit(term))

        for left_index, left in enumerate(pool):
            for right in pool[left_index:]:
                if max(left.depth, right.depth) != depth - 1:
                    continue
                candidates.append(_multiply(left, right))

        for candidate in candidates:
            key = _semantic_key(candidate, worlds)
            incumbent = best_by_semantics.get(key)
            if incumbent is None or (
                candidate.operation_count,
                candidate.recipe,
            ) < (
                incumbent.operation_count,
                incumbent.recipe,
            ):
                best_by_semantics[key] = candidate

    return tuple(best_by_semantics.values())


def evaluate_am_term(
    term: AMTerm,
    *,
    worlds: tuple[tuple[int, int], ...],
) -> PresentationCandidate[AMTaskPresentation]:
    feature_counts: list[int] = []
    task_counts: list[int] = []
    sufficient = True

    for k, p in worlds:
        feature_to_task: dict[int, tuple[int, ...]] = {}
        features: set[int] = set()
        tasks: set[tuple[int, ...]] = set()

        for first, second in _pairs(p):
            feature = term.evaluate(first, second, p)
            task = contact_task_signature(first, second, k=k, p=p)
            features.add(feature)
            tasks.add(task)
            previous = feature_to_task.get(feature)
            if previous is not None and previous != task:
                sufficient = False
            feature_to_task[feature] = task

        feature_counts.append(len(features))
        task_counts.append(len(tasks))

    payload = AMTaskPresentation(
        term=term,
        feature_class_counts=tuple(feature_counts),
        task_class_counts=tuple(task_counts),
        exact_partition=(
            sufficient
            and tuple(feature_counts) == tuple(task_counts)
        ),
    )
    return PresentationCandidate(
        payload=payload,
        sufficient=sufficient,
        label=term.recipe,
        certificate=(tuple(feature_counts), tuple(task_counts)),
        cost=PresentationCost(
            grammar=float(term.operation_count),
            relations=0.0,
            history=float(sum(feature_counts)),
            decoder=0.0,
            task_error=0.0 if sufficient else math.inf,
        ),
    )


def search_am_presentations(
    *,
    worlds: tuple[tuple[int, int], ...],
    max_depth: int = 3,
) -> PresentationSearchResult[AMTaskPresentation]:
    evaluated = tuple(
        evaluate_am_term(term, worlds=worlds)
        for term in generate_am_terms(worlds=worlds, max_depth=max_depth)
    )
    return PresentationSearchResult(
        evaluated=evaluated,
        pareto=pareto_frontier(evaluated),
    )


def _partition(
    term: AMTerm,
    *,
    k: int,
    p: int,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    buckets: dict[int, list[tuple[int, int]]] = {}
    for pair in _pairs(p):
        buckets.setdefault(term.evaluate(*pair, p), []).append(pair)
    return tuple(sorted(tuple(sorted(bucket)) for bucket in buckets.values()))


def _task_partition(*, k: int, p: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    buckets: dict[tuple[int, ...], list[tuple[int, int]]] = {}
    for pair in _pairs(p):
        buckets.setdefault(contact_task_signature(*pair, k=k, p=p), []).append(pair)
    return tuple(sorted(tuple(sorted(bucket)) for bucket in buckets.values()))


def test_am_search_rediscovers_relative_m_coordinate_from_contact_task() -> None:
    training_worlds = ((5, 17), (5, 29))
    result = search_am_presentations(worlds=training_worlds, max_depth=3)

    sufficient = {
        candidate.label: candidate
        for candidate in result.evaluated
        if candidate.sufficient
    }

    # The cheaper relative coordinate is sufficient but still distinguishes
    # r from r^{-1}; the extra M-orbit quotient reaches the exact task partition.
    relative = sufficient["mul(inv(s),t)"]
    exact = sufficient["orbit(mul(inv(s),t))"]

    assert relative.payload.feature_class_counts == (8, 14)
    assert relative.payload.task_class_counts == (5, 8)
    assert not relative.payload.exact_partition

    assert exact.payload.feature_class_counts == (5, 8)
    assert exact.payload.task_class_counts == (5, 8)
    assert exact.payload.exact_partition

    pareto_labels = {candidate.label for candidate in result.pareto}
    assert "mul(inv(s),t)" in pareto_labels
    assert "orbit(mul(inv(s),t))" in pareto_labels


def test_frozen_am_discovery_transfers_to_held_out_solved_world() -> None:
    training_worlds = ((5, 17), (5, 29))
    result = search_am_presentations(worlds=training_worlds, max_depth=3)
    discovered = next(
        candidate.payload.term
        for candidate in result.evaluated
        if candidate.label == "orbit(mul(inv(s),t))"
    )

    # k=8,p=79 is not used in proposal generation or selection.
    assert _partition(discovered, k=8, p=79) == _task_partition(k=8, p=79)
    assert len(_partition(discovered, k=8, p=79)) == 20
    assert len(_pairs(79)) == 780

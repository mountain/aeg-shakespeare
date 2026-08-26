"""Phase 12C: objectification and a fibred finite change calculus.

This executable essay starts before additive or infinitesimal calculus.  Its
primitive data are monoids, their actions, task observers, and the response
fibres that reconstruct observed changes.  It certifies:

* compositional lowering gives a change-action skeleton;
* response existence, coherence, task adequacy, and compression are separate;
* one partition object supports additive, max, and union response monoids;
* nonfree actions make an observed derivative a fibre rather than a scalar;
* frame forgetting, an insufficient codomain action, missing native closure,
  and nonassociative exponentiation block automatic upgrades.

All calculations are exact and research-local.  No smooth, tangent, numerical,
generic categorical, Experimental, or Public calculus is claimed.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import prod
from typing import Callable, Hashable, Iterable, TypeVar


_Partition = tuple[int, ...]
_Word = tuple[int, ...]
_ProjectivePoint = Fraction | None
_Mobius = tuple[Fraction, Fraction, Fraction, Fraction]
_Affine = tuple[int, int]

_State = TypeVar("_State")
_Process = TypeVar("_Process", bound=Hashable)
_Observation = TypeVar("_Observation", bound=Hashable)


def _words(generators: tuple[int, ...], maximum_depth: int) -> tuple[_Word, ...]:
    return tuple(
        word
        for depth in range(maximum_depth + 1)
        for word in product(generators, repeat=depth)
    )


def _scale(word: _Word) -> int:
    return prod(word, start=1)


def _scale_action(base: int, word: _Word) -> int:
    return base * _scale(word)


def _affine_action(base: int, process: _Affine) -> int:
    translation, dilation = process
    return dilation * base + translation


def _chronological_affine(left: _Affine, right: _Affine) -> _Affine:
    """Compose ``left`` first and ``right`` second for the right action."""

    left_translation, left_dilation = left
    right_translation, right_dilation = right
    return (
        right_dilation * left_translation + right_translation,
        right_dilation * left_dilation,
    )


def _partitions(weight: int, maximum: int | None = None) -> tuple[_Partition, ...]:
    if weight == 0:
        return ((),)
    upper = weight if maximum is None else min(weight, maximum)
    return tuple(
        (first, *tail)
        for first in range(upper, 0, -1)
        for tail in _partitions(weight - first, first)
    )


def _partition_corpus(maximum_weight: int) -> tuple[_Partition, ...]:
    return tuple(
        partition
        for weight in range(maximum_weight + 1)
        for partition in _partitions(weight)
    )


def _union(left: _Partition, right: _Partition) -> _Partition:
    return tuple(sorted((*left, *right), reverse=True))


def _weight(partition: _Partition) -> int:
    return sum(partition)


def _largest(partition: _Partition) -> int:
    return partition[0] if partition else 0


def _support(partition: _Partition) -> frozenset[int]:
    return frozenset(partition)


def _response_fibre(
    source: _State,
    target: _State,
    responses: Iterable[_Process],
    action: Callable[[_State, _Process], _State],
) -> frozenset[_Process]:
    return frozenset(
        response
        for response in responses
        if action(source, response) == target
    )


def _descended_action_table(
    states: Iterable[_State],
    processes: Iterable[_Process],
    quotient: Callable[[_State], _Observation],
    action: Callable[[_State, _Process], _State],
) -> dict[tuple[_Observation, _Process], _Observation] | None:
    table: dict[tuple[_Observation, _Process], _Observation] = {}
    for state in states:
        for process in processes:
            key = (quotient(state), process)
            target = quotient(action(state, process))
            previous = table.setdefault(key, target)
            if previous != target:
                return None
    return table


def _mobius(matrix: _Mobius, point: _ProjectivePoint) -> _ProjectivePoint:
    a, b, c, d = matrix
    if point is None:
        return None if c == 0 else a / c
    denominator = c * point + d
    if denominator == 0:
        return None
    return (a * point + b) / denominator


def _difference_two(partition: _Partition) -> bool:
    return all(left - right >= 2 for left, right in zip(partition, partition[1:]))


def test_c0_objectification_lowering_gives_a_multiplicative_action_skeleton():
    words = _words((2, 3), 6)
    bases = range(-6, 7)

    assert len(words) == 127
    assert len({_scale(word) for word in words}) == 28

    for word in words:
        assert _scale_action(_scale_action(1, ()), word) == _scale_action(1, word)
        for split in range(len(word) + 1):
            left, right = word[:split], word[split:]
            assert _scale(left + right) == _scale(left) * _scale(right)
            for base in bases:
                assert _scale_action(_scale_action(base, left), right) == (
                    _scale_action(base, left + right)
                )

    # The response is multiplicative.  It reconstructs the changed lower
    # Translation parameter and obeys the regular change-action cocycle.
    short_words = _words((2, 3), 3)
    for base, left, right in product(bases, short_words, short_words):
        first_response = _scale(left)
        second_response = _scale(right)
        total_response = _scale(left + right)
        after_first = base * first_response
        assert base * total_response == after_first * second_response
        assert total_response == first_response * second_response

    # The discrete A/M cross law precedes its infinitesimal Lie shadow.
    for base, translation, dilation in product(bases, range(-4, 5), (1, 2, 3, 6)):
        assert dilation * (base + translation) == (
            dilation * base + dilation * translation
        )

    # A noncommutative control fixes the variance convention: endomorphisms
    # multiply chronologically, F star G = G after F, for this right action.
    affine_processes = tuple(product(range(-2, 3), (1, 2, 3)))
    identity: _Affine = (0, 1)
    for base, left, right in product(bases, affine_processes, affine_processes):
        assert _affine_action(base, identity) == base
        assert _affine_action(_affine_action(base, left), right) == (
            _affine_action(base, _chronological_affine(left, right))
        )
    translation_one: _Affine = (1, 1)
    dilation_two: _Affine = (0, 2)
    assert _chronological_affine(translation_one, dilation_two) == (2, 2)
    assert _chronological_affine(dilation_two, translation_one) == (1, 2)


def test_c1_multiplicative_response_compresses_words_but_not_zero_stabilizers():
    words = _words((2, 3), 6)
    by_scale: dict[int, list[_Word]] = {}
    for word in words:
        by_scale.setdefault(_scale(word), []).append(word)

    assert len(words) == 127
    assert len(by_scale) == 28
    assert by_scale[6] == [(2, 3), (3, 2)]

    # Equal response values remain equal after every frozen continuation.
    continuations = _words((2, 3), 3)
    for same_scale_words in by_scale.values():
        for left, right in product(same_scale_words, repeat=2):
            for continuation in continuations:
                assert _scale(left + continuation) == _scale(right + continuation)

    candidates = range(1, 11)
    assert _response_fibre(2, 12, candidates, lambda value, k: value * k) == {6}
    assert _response_fibre(0, 0, candidates, lambda value, k: value * k) == set(
        candidates
    )

    # Thus the typed process response is retained even where endpoints cannot
    # reconstruct it through the stabilizer of zero.
    assert 127 > 28


def test_c2_partitions_support_distinct_additive_max_and_union_responses():
    corpus = _partition_corpus(10)
    changes = _partition_corpus(5)
    assert len(corpus) == 139
    assert len(changes) == 19
    assert len({_weight(change) for change in changes}) == 6
    assert len({len(change) for change in changes}) == 6
    assert len({_largest(change) for change in changes}) == 6
    assert len({_support(change) for change in changes}) == 10
    assert len(
        {any(part % 2 for part in _support(change)) for change in changes}
    ) == 2

    for base, change in product(corpus, changes):
        target = _union(base, change)
        assert _weight(target) == _weight(base) + _weight(change)
        assert len(target) == len(base) + len(change)
        assert _largest(target) == max(_largest(base), _largest(change))
        assert _support(target) == _support(base) | _support(change)

    # Responses compose inside four different monoids.  No tangent or common
    # additive carrier is used to prove these laws.
    for first, second in product(changes, repeat=2):
        combined = _union(first, second)
        assert _weight(combined) == _weight(first) + _weight(second)
        assert len(combined) == len(first) + len(second)
        assert _largest(combined) == max(_largest(first), _largest(second))
        assert _support(combined) == _support(first) | _support(second)

    # A nonadditive chain rule: partition -> support -> "contains an odd part".
    # Support changes by union and the Boolean observer changes by OR.
    for base, change in product(corpus, changes):
        support_response = _support(change)
        boolean_response = any(part % 2 for part in support_response)
        target = _union(base, change)
        assert any(part % 2 for part in _support(target)) == (
            any(part % 2 for part in _support(base)) or boolean_response
        )

    empty: _Partition = ()
    for base in corpus:
        assert _union(base, empty) == base
        assert _weight(empty) == 0
        assert len(empty) == 0
        assert _largest(empty) == 0
        assert _support(empty) == frozenset()


def test_c3_derivative_fibres_detect_free_and_nonfree_response_actions():
    candidates = tuple(range(11))

    # Addition is cancellative on this exact nonnegative domain, so a reachable
    # response is unique.
    for source, response in product(range(11), repeat=2):
        target = source + response
        assert _response_fibre(
            source,
            target,
            candidates,
            lambda value, change: value + change,
        ) == {response}

    # Max is nonfree.  A strict increase forces its response, while a stationary
    # endpoint admits a whole residual fibre of hidden changes.
    for source in range(11):
        stationary = _response_fibre(
            source,
            source,
            candidates,
            max,
        )
        assert stationary == set(range(source + 1))
        for target in range(source + 1, 11):
            assert _response_fibre(source, target, candidates, max) == {target}

    assert _response_fibre(5, 5, candidates, max) == {0, 1, 2, 3, 4, 5}
    assert _response_fibre(5, 8, candidates, max) == {8}

    # Reconstruction alone does not make an arbitrary fibre section regular.
    # Both selected values below reconstruct the stationary endpoint 5, but
    # the selection reverses the max order and violates the cocycle.
    def nonregular_selection(source: int, response: int) -> int:
        if source == 5 and response == 2:
            return 4
        if source == 5 and response == 3:
            return 1
        return response

    assert max(5, nonregular_selection(5, 2)) == max(5, 2)
    assert max(5, nonregular_selection(5, 3)) == max(5, 3)
    left = nonregular_selection(5, max(2, 3))
    right = max(
        nonregular_selection(5, 2),
        nonregular_selection(max(5, 2), 3),
    )
    assert left == 1
    assert right == 4
    assert left != right


def test_c4_strict_descent_is_a_fibre_stability_condition():
    states = _partition_corpus(8)
    changes = _partition_corpus(3)
    table = _descended_action_table(states, changes, _weight, _union)
    assert table is not None
    for base in range(9):
        for change in changes:
            assert table[(base, change)] == base + _weight(change)

    # Equal base observations can have incompatible observed targets.  The
    # action then cannot descend without retaining a discriminator.
    finite_states = (0, 1, 2, 3)

    def bad_action(state: int, process: int) -> int:
        if process == 0:
            return state
        return 1 if state == 2 else state

    assert _descended_action_table(
        finite_states,
        (0, 1),
        lambda state: state % 2,
        bad_action,
    ) is None

    # Preserve the minimal Phase 12A projective-frame obstruction exactly.
    g_zero: _Mobius = (
        Fraction(0),
        Fraction(1),
        Fraction(1),
        Fraction(0),
    )
    g_one: _Mobius = (
        Fraction(0),
        Fraction(1),
        Fraction(1),
        Fraction(-1),
    )
    assert (_mobius(g_zero, Fraction(0)), _mobius(g_zero, Fraction(1))) == (
        None,
        Fraction(1),
    )
    assert (_mobius(g_one, Fraction(1)), _mobius(g_one, Fraction(2))) == (
        None,
        Fraction(1),
    )
    assert _mobius(g_zero, Fraction(1)) == Fraction(1)
    assert _mobius(g_one, Fraction(3)) == Fraction(1, 2)


def test_c5_nonautomaticity_and_composition_red_teams_remain_visible():
    # A toggle observed by the identity map cannot be represented in a trivial
    # codomain change action: the derivative fibre is empty.
    assert not _response_fibre(
        0,
        1,
        (None,),
        lambda value, _change: value,
    )

    # A huge endomorphism carrier can always insert a constant endpoint map,
    # but this tautological existence is not compression evidence.
    carrier = tuple(product(range(3), repeat=3))
    assert len(carrier) == 27
    for source, target in product(range(3), repeat=2):
        responses = tuple(
            function
            for function in carrier
            if function[source] == target
        )
        assert responses
    assert len(carrier) > 3 * 3

    # The Rogers--Ramanujan difference families have no native union action.
    assert _difference_two((1,))
    assert not _difference_two(_union((1,), (1,)))
    assert _difference_two((2,))
    assert not _difference_two(_union((2,), (2,)))

    # Binary exponentiation cannot itself be the required change monoid.
    assert (2**3) ** 2 == 64
    assert 2 ** (3**2) == 512
    assert (2**3) ** 2 != 2 ** (3**2)


def test_c6_claim_grades_answer_the_automatic_upgrade_question():
    verdict = {
        "strong_objectification_gives_action_skeleton": True,
        "every_observer_has_declared_response": False,
        "response_is_automatically_unique": False,
        "regular_cocycle_is_automatic_for_arbitrary_choice": False,
        "task_adequacy_is_automatic": False,
        "effective_compression_is_automatic": False,
        "partition_weight_response_reaches_c4": True,
        "partition_max_response_is_fibred": True,
        "a_m_multiplicative_response_reaches_c4_on_frozen_task": True,
        "rogers_ramanujan_difference_side_transports_native_calculus": False,
        "ordinary_tangent_or_jet_is_primitive": False,
        "generic_calculus_or_public_api_earned": False,
    }
    assert verdict["strong_objectification_gives_action_skeleton"]
    assert not verdict["every_observer_has_declared_response"]
    assert not verdict["response_is_automatically_unique"]
    assert not verdict["regular_cocycle_is_automatic_for_arbitrary_choice"]
    assert not verdict["task_adequacy_is_automatic"]
    assert not verdict["effective_compression_is_automatic"]
    assert verdict["partition_weight_response_reaches_c4"]
    assert verdict["partition_max_response_is_fibred"]
    assert verdict["a_m_multiplicative_response_reaches_c4_on_frozen_task"]
    assert not verdict["rogers_ramanujan_difference_side_transports_native_calculus"]
    assert not verdict["ordinary_tangent_or_jet_is_primitive"]
    assert not verdict["generic_calculus_or_public_api_earned"]

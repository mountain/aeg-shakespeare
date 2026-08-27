"""Phase 1J-A: exact ordered collision response through the C0--C2 gates.

Phase 1I had an exact one-step target/fibre ledger, but its independent A/M
order control was not collision-derived and its residuals had no regular
composition law.  This executable essay replaces that adjacent control by two
overlapping reversible binary collision gates on three sites::

    L(x0, x1, x2) = (x0, x1 xor x0, x2)
    R(x0, x1, x2) = (x0, x1, x2 xor x1).

Each gate is a local involution.  They do not commute because they share the
middle site.  The observer keeps only the three one-site occupancies and the
target action renews an independent microscopic section before each gate.
Correlations forgotten by this observer become an exact, generally set-valued
response relation.

For a retained microscopic law F, collision word u, target action B_u, and
one-site observation pi, define

    r_u(F) = pi(U_u F) - B_u(pi F).

If u is followed by v, the response is transported by

    T_v(y, r) = B_v(y + r) - B_v(y)

and obeys the exact cocycle identity

    r_{uv}(F) = T_v(B_u(pi F), r_u(F)) + r_v(U_u F).

The state dependence in T is essential: naive vector addition fails.  The
parity character z=1-2p turns the independent XOR target law into
multiplication, but no logarithmic covector, potential, entropy, continuum
limit, or generic API is admitted here.

All certificates use ``fractions.Fraction`` and finite enumeration only.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import prod
from typing import Iterator


Q = Fraction
MicroState = tuple[int, int, int]
MicroLaw = tuple[Q, ...]
MacroState = tuple[Q, Q, Q]
Collision = tuple[int, int]
CollisionWord = tuple[Collision, ...]

STATES: tuple[MicroState, ...] = tuple(product((0, 1), repeat=3))
STATE_INDEX = {state: index for index, state in enumerate(STATES)}
LEFT: Collision = (0, 1)
RIGHT: Collision = (1, 2)
GATES = (LEFT, RIGHT)


@dataclass(frozen=True)
class ResponseLedger:
    """Typed target action, retained-law response, and exact reconstruction."""

    base: MacroState
    target: MacroState
    response: MacroState
    exact_next: MacroState


@dataclass(frozen=True)
class ChartAudit:
    """Frozen qualitative cost axes; labels are claims, not timings."""

    dynamics: str
    composition: str
    covector: str
    decoder: str
    residual: str


def _vector_add(left: MacroState, right: MacroState) -> MacroState:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def _vector_subtract(left: MacroState, right: MacroState) -> MacroState:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def _collision_state(state: MicroState, gate: Collision) -> MicroState:
    control, target = gate
    result = list(state)
    result[target] ^= result[control]
    return tuple(result)  # type: ignore[return-value]


def _pushforward(law: MicroLaw, gate: Collision) -> MicroLaw:
    result = [Q(0) for _ in STATES]
    for state, weight in zip(STATES, law):
        result[STATE_INDEX[_collision_state(state, gate)]] += weight
    return tuple(result)


def _push_word(law: MicroLaw, word: CollisionWord) -> MicroLaw:
    for gate in word:
        law = _pushforward(law, gate)
    return law


def _lower(law: MicroLaw) -> MacroState:
    return tuple(
        sum(weight for state, weight in zip(STATES, law) if state[site])
        for site in range(3)
    )  # type: ignore[return-value]


def _independent_section(base: MacroState) -> MicroLaw:
    return tuple(
        prod(
            (base[site] if state[site] else 1 - base[site] for site in range(3)),
            start=Q(1),
        )
        for state in STATES
    )


def _xor_probability(control: Q, target: Q) -> Q:
    return control + target - 2 * control * target


def _target_step(base: MacroState, gate: Collision) -> MacroState:
    control, target = gate
    result = list(base)
    result[target] = _xor_probability(base[control], base[target])
    return tuple(result)  # type: ignore[return-value]


def _target_word(base: MacroState, word: CollisionWord) -> MacroState:
    for gate in word:
        base = _target_step(base, gate)
    return base


def _response(law: MicroLaw, gate: Collision) -> MacroState:
    return _vector_subtract(
        _lower(_pushforward(law, gate)),
        _target_step(_lower(law), gate),
    )


def _word_response(law: MicroLaw, word: CollisionWord) -> MacroState:
    return _vector_subtract(
        _lower(_push_word(law, word)),
        _target_word(_lower(law), word),
    )


def _response_ledger(law: MicroLaw, gate: Collision) -> ResponseLedger:
    base = _lower(law)
    target = _target_step(base, gate)
    response = _response(law, gate)
    return ResponseLedger(
        base=base,
        target=target,
        response=response,
        exact_next=_lower(_pushforward(law, gate)),
    )


def _transport_response(
    base: MacroState,
    response: MacroState,
    word: CollisionWord,
) -> MacroState:
    return _vector_subtract(
        _target_word(_vector_add(base, response), word),
        _target_word(base, word),
    )


def _weak_compositions(
    total: int,
    slots: int,
    prefix: tuple[int, ...] = (),
) -> Iterator[tuple[int, ...]]:
    if slots == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from _weak_compositions(total - first, slots - 1, prefix + (first,))


def _law_from_counts(counts: tuple[int, ...]) -> MicroLaw:
    total = sum(counts)
    assert total > 0
    return tuple(Q(count, total) for count in counts)


def _positive_micro_corpus(total: int) -> tuple[MicroLaw, ...]:
    assert total >= len(STATES)
    return tuple(
        _law_from_counts(tuple(count + 1 for count in excess))
        for excess in _weak_compositions(total - len(STATES), len(STATES))
    )


def _fixed_fibre(base: MacroState, total: int) -> tuple[MicroLaw, ...]:
    return tuple(
        law
        for counts in _weak_compositions(total, len(STATES))
        if _lower(law := _law_from_counts(counts)) == base
    )


def _parity_character(probability: Q) -> Q:
    return 1 - 2 * probability


def _character_chart(base: MacroState) -> MacroState:
    return tuple(_parity_character(value) for value in base)  # type: ignore[return-value]


def test_collision_generators_are_local_reversible_and_noncommuting():
    for gate in GATES:
        control, target = gate
        untouched = ({0, 1, 2} - {control, target}).pop()
        images = {_collision_state(state, gate) for state in STATES}

        assert images == set(STATES)
        for state in STATES:
            collided = _collision_state(state, gate)
            assert _collision_state(collided, gate) == state
            assert collided[untouched] == state[untouched]

    witness = (1, 0, 0)
    left_then_right = _collision_state(_collision_state(witness, LEFT), RIGHT)
    right_then_left = _collision_state(_collision_state(witness, RIGHT), LEFT)
    assert left_then_right == (1, 1, 1)
    assert right_then_left == (1, 1, 0)


def test_c0_target_action_matches_independent_collision_pushforward():
    corpus = (
        (Q(1, 4), Q(1, 3), Q(2, 5)),
        (Q(1, 2), Q(1, 2), Q(1, 2)),
        (Q(3, 5), Q(2, 7), Q(4, 9)),
    )
    words: tuple[CollisionWord, ...] = (
        (),
        (LEFT,),
        (RIGHT,),
        (LEFT, RIGHT),
        (RIGHT, LEFT),
    )

    for base in corpus:
        for gate in GATES:
            assert _target_step(base, gate) == _lower(
                _pushforward(_independent_section(base), gate)
            )
        for prefix in words:
            for suffix in words:
                assert _target_word(base, prefix + suffix) == _target_word(
                    _target_word(base, prefix), suffix
                )


def test_c0_collision_word_action_retains_order():
    base = (Q(1, 4), Q(1, 3), Q(2, 5))

    assert _target_word(base, (LEFT, RIGHT)) == (
        Q(1, 4),
        Q(5, 12),
        Q(29, 60),
    )
    assert _target_word(base, (RIGHT, LEFT)) == (
        Q(1, 4),
        Q(5, 12),
        Q(7, 15),
    )
    assert _target_word(base, (LEFT, RIGHT)) != _target_word(
        base, (RIGHT, LEFT)
    )


def test_c1_retained_law_response_reconstructs_exact_next_observation():
    corpus = _positive_micro_corpus(total=10)

    assert len(corpus) == 36
    for law, gate in product(corpus, GATES):
        ledger = _response_ledger(law, gate)
        assert _vector_add(ledger.target, ledger.response) == ledger.exact_next
        assert all(0 <= value <= 1 for value in ledger.exact_next)


def test_c1_forgetting_makes_the_response_relation_genuinely_set_valued():
    base = (Q(1, 2), Q(1, 2), Q(1, 2))
    fibre = _fixed_fibre(base, total=8)
    responses = {_response(law, LEFT) for law in fibre}

    assert len(fibre) == 57
    assert responses == {
        (0, Q(-1, 2), 0),
        (0, Q(-1, 4), 0),
        (0, 0, 0),
        (0, Q(1, 4), 0),
        (0, Q(1, 2), 0),
    }

    anticorrelated = _law_from_counts((0, 4, 0, 0, 0, 0, 4, 0))
    correlated = _law_from_counts((0, 0, 0, 4, 4, 0, 0, 0))
    renewed = _independent_section(base)
    assert _lower(anticorrelated) == _lower(correlated) == base
    assert _response(anticorrelated, LEFT) == (0, Q(-1, 2), 0)
    assert _response(correlated, LEFT) == (0, Q(1, 2), 0)
    assert _response(renewed, LEFT) == (0, 0, 0)


def test_c2_state_dependent_transport_is_an_exact_response_cocycle():
    corpus = _positive_micro_corpus(total=10)
    words: tuple[CollisionWord, ...] = (
        (),
        (LEFT,),
        (RIGHT,),
        (LEFT, RIGHT),
        (RIGHT, LEFT),
    )

    for law, prefix, suffix in product(corpus, words, words):
        base = _lower(law)
        prefix_target = _target_word(base, prefix)
        prefix_response = _word_response(law, prefix)
        continued_law = _push_word(law, prefix)
        suffix_response = _word_response(continued_law, suffix)
        transported = _transport_response(
            prefix_target,
            prefix_response,
            suffix,
        )

        assert _word_response(law, prefix + suffix) == _vector_add(
            transported,
            suffix_response,
        )


def test_naive_response_addition_fails_but_transported_sum_succeeds():
    law = _law_from_counts((1, 1, 1, 1, 1, 1, 1, 3))
    base = _lower(law)
    left_target = _target_step(base, LEFT)
    left_response = _response(law, LEFT)
    after_left = _pushforward(law, LEFT)
    right_response = _response(after_left, RIGHT)
    transported_left = _transport_response(left_target, left_response, (RIGHT,))
    composite = _word_response(law, (LEFT, RIGHT))

    assert base == (Q(3, 5), Q(3, 5), Q(3, 5))
    assert left_response == (0, Q(-2, 25), 0)
    assert right_response == (0, 0, Q(2, 25))
    assert transported_left == (0, Q(-2, 25), Q(2, 125))
    assert composite == (0, Q(-2, 25), Q(12, 125))
    assert composite == _vector_add(transported_left, right_response)
    assert composite != _vector_add(left_response, right_response)


def test_collision_product_character_is_exact_but_stops_before_a_covector():
    corpus = (
        (Q(1, 4), Q(1, 3), Q(2, 5)),
        (Q(1, 2), Q(1, 2), Q(1, 2)),
        (Q(3, 5), Q(2, 7), Q(4, 9)),
    )

    for base, gate in product(corpus, GATES):
        control, target = gate
        before = _character_chart(base)
        after = _character_chart(_target_step(base, gate))
        expected = list(before)
        expected[target] = before[control] * before[target]
        assert after == tuple(expected)

    # The product character includes zero and negative values.  Turning it
    # into an additive logarithmic covector would require a smaller domain and
    # a new analytic primitive, neither of which is part of C0--C2.
    assert _character_chart((Q(1, 2), Q(1, 4), Q(3, 4))) == (0, Q(1, 2), Q(-1, 2))


def test_chart_atlas_keeps_dynamics_decoder_covector_and_residual_costs_apart():
    atlas = {
        "occupancy": ChartAudit(
            dynamics="bilinear_xor_probability",
            composition="ordered_target_maps",
            covector="not_selected",
            decoder="identity",
            residual="additive_macro_correction_with_nonlinear_transport",
        ),
        "parity_character": ChartAudit(
            dynamics="one_product_on_the_target_site",
            composition="collision_product_character",
            covector="log_candidate_excludes_zero_and_sign_changes",
            decoder="affine_half_map",
            residual="character_difference_not_a_free_additive_fibre",
        ),
    }

    assert atlas["occupancy"].decoder == "identity"
    assert atlas["parity_character"].dynamics == "one_product_on_the_target_site"
    assert atlas["parity_character"].covector.startswith("log_candidate")
    assert atlas["occupancy"].residual.endswith("nonlinear_transport")


def test_phase1j_a_claims_stop_exactly_at_the_c2_gate():
    grades = {
        "C0_action_skeleton": "passed_ordered_collision_word_action",
        "C1_response_reconstruction": "passed_with_retained_micro_law",
        "C1_after_forgetting": "exact_set_valued_relation",
        "C2_regular_cocycle": "passed_state_dependent_transport",
        "C3_closed_covector": "not_selected",
        "C4_effective_compression": "not_tested",
        "continuum_fibre_response": "not_claimed",
        "H_functional": "not_admitted",
        "generic_calculus": "not_claimed",
        "arithmetic_rank": "unchanged",
    }

    assert grades["C0_action_skeleton"].startswith("passed")
    assert grades["C1_after_forgetting"] == "exact_set_valued_relation"
    assert grades["C2_regular_cocycle"] == "passed_state_dependent_transport"
    assert grades["C3_closed_covector"] == "not_selected"
    assert grades["H_functional"] == "not_admitted"

"""Phase 8: exact continuation-value fibres over local p-adic signatures.

Phase 7 proved that the declared coefficient grammar is intrinsically binary,
but also exhibited equal local S2 signatures with disjoint optimal lift bits.
This executable essay asks what exact finite state must be restored above S2
before policy, value, or every admitted continuation descends compositionally.

The construction is deliberately finite and task-relative.  It builds the
binary response machine, refines local-signature kernels to the coarsest stable
partition, extracts distinguishing bit suffixes, and audits the descended
partial bit transports.  A stable finite quotient is not silently renamed a
new manifold dimension, bundle, groupoid, or process rank.

All arithmetic is exact.  The Phase 7 and Phase 6 research owners are imported
by path; no package API is introduced.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
import importlib.util
import json
from math import gcd
from pathlib import Path
import sys
from time import perf_counter
from typing import Literal

import pytest


_PHASE7_PATH = Path(__file__).with_name(
    "test_padic_selector_structural_law.py"
)
_SPEC = importlib.util.spec_from_file_location(
    "_phase7_padic_selector_structural_law",
    _PHASE7_PATH,
)
assert _SPEC is not None and _SPEC.loader is not None
_PHASE7 = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _PHASE7
_SPEC.loader.exec_module(_PHASE7)
_PHASE6 = _PHASE7._PHASE6


_Axis = Literal["digit_steps", "decoder_bits"]
_Mode = Literal[
    "policy_digit",
    "policy_decoder",
    "value_digit",
    "value_decoder",
    "full",
]
_NodeId = tuple[object, ...]


@dataclass(frozen=True, order=True)
class _TaskTag:
    family: str
    prime: int
    precision: int
    horizon: int
    initial: Fraction


@dataclass(frozen=True)
class _Edge:
    bit: int
    outcome: str
    cost: tuple[int, int, int, int] | None
    next_node: _NodeId | None
    terminal_payload: object | None = None


@dataclass(frozen=True)
class _Node:
    node_id: _NodeId
    tag: _TaskTag
    task: object
    state: object
    frontier: tuple[object, ...]
    edges: tuple[_Edge, _Edge]


@dataclass(frozen=True)
class _FamilyCensus:
    tasks: int
    states: int
    actions: int
    exact_edges: int
    precision_edges: int
    cycles: int
    horizons: int
    maximum_states: int
    maximum_actions: int
    maximum_live_step: int


@dataclass(frozen=True)
class _Universe:
    nodes: dict[_NodeId, _Node]
    family_censuses: dict[str, _FamilyCensus]
    compilation_seconds: float


@dataclass(frozen=True)
class _FamilyFibreAudit:
    family: str
    states: int
    base_classes: int
    stable_classes: int
    nontrivial_fibres: int
    maximum_fibre: int
    maximum_residual_bits: int


@dataclass(frozen=True)
class _QuotientAudit:
    level: int
    mode: _Mode
    states: int
    base_classes: int
    initial_classes: int
    stable_classes: int
    refinement_rounds: int
    transport_forced_splits: int
    nontrivial_fibres: int
    maximum_fibre: int
    maximum_residual_bits: int
    fibre_histogram: tuple[tuple[int, int], ...]
    witness_pairs: int
    shortest_suffix: int
    longest_suffix: int
    family_fibres: tuple[_FamilyFibreAudit, ...]
    compilation_seconds: float


@dataclass(frozen=True)
class _TransportAudit:
    level: int
    mode: _Mode
    quotient_classes: int
    live_edges: int
    terminal_edges: int
    invalid_edges: int
    merged_live_targets: int
    excess_live_preimages: int
    mixed_family_classes: int
    behavior_types: int
    types_shared_by_two_families: int
    types_shared_by_all_families: int
    task_specific_types: int


@dataclass(frozen=True)
class _PartitionResult:
    audit: _QuotientAudit
    blocks: dict[_NodeId, int]
    history: tuple[dict[_NodeId, int], ...]


def _corpus(bound: int) -> tuple[Fraction, ...]:
    return tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for denominator in range(1, bound + 1)
                for numerator in range(-bound, bound + 1)
                if numerator != 0 and gcd(abs(numerator), denominator) == 1
            }
        )
    )


def _cost_tuple(cost: object) -> tuple[int, int, int, int]:
    return (
        cost.digit_steps,
        cost.tree_edges,
        cost.digit_bits,
        cost.decoder_bits,
    )


def _node_id(tag: _TaskTag, state: object) -> _NodeId:
    return (
        tag.family,
        tag.prime,
        tag.precision,
        tag.horizon,
        tag.initial,
        state.key,
    )


def _build_edge(tag: _TaskTag, task: object, state: object, bit: int) -> _Edge:
    actions = _PHASE7._closed_admissible_actions(
        state.complete_quotient,
        task.prime,
    )
    by_bit = {
        _PHASE7._lift_bit(state.complete_quotient, task.prime, action): action
        for action in actions
    }
    action = by_bit.get(bit)
    if action is None:
        return _Edge(bit, "invalid", None, None)

    transition = _PHASE6._advance(
        task,
        state,
        action,
        admitted_actions=actions,
    )
    cost = _PHASE6._stage_cost(state, transition)
    terminal_payload: object | None = None
    if transition.outcome in ("success_exact", "success_precision"):
        cost += _PHASE6._terminal_decoder_cost(task, transition)
        terminal_payload = _PHASE6._decode_success(task, transition)
    elif transition.outcome == "cycle":
        terminal_payload = transition.repeated_complete_quotient
    elif transition.outcome == "horizon":
        terminal_payload = transition.next_complete_quotient

    next_node = None
    if transition.outcome == "live":
        if transition.next_state is None:
            raise _PHASE6._ArithmeticOrStateFailure(
                "a live Phase 8 edge omitted its successor"
            )
        next_node = _node_id(tag, transition.next_state)
    return _Edge(
        bit,
        transition.outcome,
        _cost_tuple(cost),
        next_node,
        terminal_payload,
    )


def _aggregate_censuses(censuses: tuple[object, ...]) -> _FamilyCensus:
    return _FamilyCensus(
        tasks=len(censuses),
        states=sum(census.states for census in censuses),
        actions=sum(census.enumerated_actions for census in censuses),
        exact_edges=sum(census.success_exact for census in censuses),
        precision_edges=sum(census.success_precision for census in censuses),
        cycles=sum(census.cycles for census in censuses),
        horizons=sum(census.horizons for census in censuses),
        maximum_states=max(census.states for census in censuses),
        maximum_actions=max(
            census.enumerated_actions for census in censuses
        ),
        maximum_live_step=max(census.maximum_live_step for census in censuses),
    )


def _build_universe() -> _Universe:
    started = perf_counter()
    x12 = _corpus(12)
    holdout = tuple(sorted(set(_corpus(18)) - set(x12)))
    assert (len(x12), len(holdout)) == (182, 224)
    specifications = (
        ("R3", 3, x12, 4, 16),
        ("R5", 5, x12, 4, 16),
        ("R7", 7, x12, 4, 16),
        ("D6", 3, x12, 6, 24),
        ("D8", 3, x12, 8, 24),
        ("P4", 11, x12, 4, 24),
        ("P6", 11, x12, 6, 24),
        ("I", 3, holdout, 6, 24),
    )

    nodes: dict[_NodeId, _Node] = {}
    family_censuses = {}
    for family, prime, inputs, precision, horizon in specifications:
        censuses = []
        for initial in inputs:
            tag = _TaskTag(family, prime, precision, horizon, initial)
            task = _PHASE6._Task(
                prime,
                initial,
                precision=precision,
                horizon=horizon,
                max_states=50_000,
                max_transitions=100_000,
            )
            census, graph_states = _PHASE7._enumerate_closed_graph(task)
            solution = _PHASE7._solve_closed(task, graph_certified=True)
            state_values = {
                state.key: tuple(frontier)
                for state, frontier in solution.state_values
            }
            graph_by_key = {state.key: state for state in graph_states}
            if set(state_values) != set(graph_by_key):
                raise _PHASE6._ArithmeticOrStateFailure(
                    "Bellman recursion and graph exhaustion disagree on states"
                )
            for state in graph_states:
                node_id = _node_id(tag, state)
                edges = (
                    _build_edge(tag, task, state, 0),
                    _build_edge(tag, task, state, 1),
                )
                if any(
                    edge.next_node is not None
                    and edge.next_node not in {
                        _node_id(tag, candidate) for candidate in graph_states
                    }
                    for edge in edges
                ):
                    raise _PHASE6._ArithmeticOrStateFailure(
                        "a live successor escaped its tagged task graph"
                    )
                nodes[node_id] = _Node(
                    node_id,
                    tag,
                    task,
                    state,
                    state_values[state.key],
                    edges,
                )
            censuses.append(census)
        family_censuses[family] = _aggregate_censuses(tuple(censuses))

    if any(
        edge.next_node is not None and edge.next_node not in nodes
        for node in nodes.values()
        for edge in node.edges
    ):
        raise _PHASE6._ArithmeticOrStateFailure(
            "the joint universe omits a live successor"
        )
    return _Universe(nodes, family_censuses, perf_counter() - started)


def _mode_axis(mode: _Mode) -> _Axis | None:
    if mode in ("policy_digit", "value_digit"):
        return "digit_steps"
    if mode in ("policy_decoder", "value_decoder"):
        return "decoder_bits"
    return None


@lru_cache(maxsize=None)
def _bit_word(node: _Node, actions: tuple[Fraction, ...]) -> tuple[int, ...]:
    state = node.state
    bits = []
    for index, action in enumerate(actions):
        bit = _PHASE7._lift_bit(
            state.complete_quotient,
            node.task.prime,
            action,
        )
        bits.append(bit)
        admitted = _PHASE7._closed_admissible_actions(
            state.complete_quotient,
            node.task.prime,
        )
        transition = _PHASE6._advance(
            node.task,
            state,
            action,
            admitted_actions=admitted,
        )
        if transition.outcome != "live":
            if index + 1 != len(actions):
                raise _PHASE6._ArithmeticOrStateFailure(
                    "a value word continues after its terminal"
                )
            break
        if transition.next_state is None:
            raise _PHASE6._ArithmeticOrStateFailure(
                "a live value word omitted its state"
            )
        state = transition.next_state
    return tuple(bits)


@lru_cache(maxsize=None)
def _state_output(node: _Node, mode: _Mode) -> object:
    if mode == "full":
        return ("full_response",)
    if not node.frontier:
        return ("no_success",)
    axis = _mode_axis(mode)
    assert axis is not None
    minimum = min(getattr(value.cost, axis) for value in node.frontier)
    optimal = tuple(
        value
        for value in node.frontier
        if getattr(value.cost, axis) == minimum
    )
    if mode.startswith("policy_"):
        return (
            "policy",
            frozenset(_bit_word(node, value.actions)[0] for value in optimal),
        )
    return (
        "value",
        minimum,
        tuple(
            sorted(
                (value.outcome, _bit_word(node, value.actions))
                for value in optimal
            )
        ),
    )


@lru_cache(maxsize=None)
def _edge_observation(edge: _Edge, mode: _Mode) -> object:
    if edge.outcome == "invalid":
        return ("invalid",)
    if mode.startswith("policy_"):
        return (edge.outcome,)
    if mode.startswith("value_"):
        axis = _mode_axis(mode)
        assert axis is not None and edge.cost is not None
        index = 0 if axis == "digit_steps" else 3
        return (edge.outcome, edge.cost[index])
    return (edge.outcome, edge.cost, edge.terminal_payload)


@lru_cache(maxsize=None)
def _local_signature(node: _Node, level: int) -> object:
    return _PHASE7._signature(node.task, node.state, level)


def _canonical_partition(
    keys: dict[_NodeId, object],
) -> dict[_NodeId, int]:
    labels: dict[object, int] = {}
    result = {}
    for node_id in sorted(keys, key=repr):
        key = keys[node_id]
        if key not in labels:
            labels[key] = len(labels)
        result[node_id] = labels[key]
    return result


def _block_sets(blocks: dict[_NodeId, int]) -> frozenset[frozenset[_NodeId]]:
    grouped: dict[int, set[_NodeId]] = defaultdict(set)
    for node_id, block in blocks.items():
        grouped[block].add(node_id)
    return frozenset(frozenset(values) for values in grouped.values())


def _edge_descriptor(
    edge: _Edge,
    mode: _Mode,
    blocks: dict[_NodeId, int],
) -> object:
    observation = _edge_observation(edge, mode)
    if edge.next_node is None:
        return observation
    return observation + (blocks[edge.next_node],)


def _refine_once(
    universe: _Universe,
    mode: _Mode,
    blocks: dict[_NodeId, int],
) -> dict[_NodeId, int]:
    return _canonical_partition(
        {
            node_id: (
                blocks[node_id],
                tuple(
                    _edge_descriptor(edge, mode, blocks)
                    for edge in node.edges
                ),
            )
            for node_id, node in universe.nodes.items()
        }
    )


def _distinguishing_suffix(
    universe: _Universe,
    mode: _Mode,
    history: tuple[dict[_NodeId, int], ...],
    left: _NodeId,
    right: _NodeId,
) -> tuple[int, ...]:
    first_split = next(
        index
        for index, blocks in enumerate(history)
        if blocks[left] != blocks[right]
    )
    if first_split == 0:
        return ()

    def descend(a: _NodeId, b: _NodeId, round_index: int) -> tuple[int, ...]:
        if round_index == 0:
            return ()
        previous = history[round_index - 1]
        for bit in (0, 1):
            left_edge = universe.nodes[a].edges[bit]
            right_edge = universe.nodes[b].edges[bit]
            left_observation = _edge_observation(left_edge, mode)
            right_observation = _edge_observation(right_edge, mode)
            if left_observation != right_observation:
                return (bit,)
            if (left_edge.next_node is None) != (right_edge.next_node is None):
                return (bit,)
            if left_edge.next_node is None:
                continue
            assert right_edge.next_node is not None
            if previous[left_edge.next_node] != previous[right_edge.next_node]:
                return (bit,) + descend(
                    left_edge.next_node,
                    right_edge.next_node,
                    round_index - 1,
                )
        raise _PHASE6._ArithmeticOrStateFailure(
            "partition split has no distinguishing edge"
        )

    return descend(left, right, first_split)


def _suffix_response(
    universe: _Universe,
    level: int,
    mode: _Mode,
    node_id: _NodeId,
    suffix: tuple[int, ...],
) -> object:
    trace = []
    cursor = node_id
    for bit in suffix:
        edge = universe.nodes[cursor].edges[bit]
        trace.append(_edge_observation(edge, mode))
        if edge.next_node is None:
            return (tuple(trace), "terminal")
        cursor = edge.next_node
    node = universe.nodes[cursor]
    return (
        tuple(trace),
        _local_signature(node, level),
        _state_output(node, mode),
    )


def _certify_stable_partition(
    universe: _Universe,
    level: int,
    mode: _Mode,
    blocks: dict[_NodeId, int],
) -> None:
    grouped: dict[int, list[_NodeId]] = defaultdict(list)
    for node_id, block in blocks.items():
        grouped[block].append(node_id)
    for members in grouped.values():
        first = universe.nodes[members[0]]
        signature = _local_signature(first, level)
        output = _state_output(first, mode)
        descriptors = tuple(
            _edge_descriptor(edge, mode, blocks) for edge in first.edges
        )
        for node_id in members[1:]:
            node = universe.nodes[node_id]
            assert _local_signature(node, level) == signature
            assert _state_output(node, mode) == output
            assert tuple(
                _edge_descriptor(edge, mode, blocks) for edge in node.edges
            ) == descriptors
    assert _block_sets(_refine_once(universe, mode, blocks)) == _block_sets(blocks)


def _partition(universe: _Universe, level: int, mode: _Mode) -> _PartitionResult:
    started = perf_counter()
    base_keys = {
        node_id: _local_signature(node, level)
        for node_id, node in universe.nodes.items()
    }
    initial = _canonical_partition(
        {
            node_id: (base_keys[node_id], _state_output(node, mode))
            for node_id, node in universe.nodes.items()
        }
    )
    history = [initial]
    while True:
        refined = _refine_once(universe, mode, history[-1])
        if len(set(refined.values())) == len(set(history[-1].values())):
            assert _block_sets(refined) == _block_sets(history[-1])
            break
        history.append(refined)
    blocks = history[-1]
    _certify_stable_partition(universe, level, mode, blocks)

    base_to_nodes: dict[object, list[_NodeId]] = defaultdict(list)
    for node_id, base in base_keys.items():
        base_to_nodes[base].append(node_id)
    fibre_sizes = []
    suffix_lengths = []
    witness_pairs = 0
    for members in base_to_nodes.values():
        by_final: dict[int, list[_NodeId]] = defaultdict(list)
        for node_id in members:
            by_final[blocks[node_id]].append(node_id)
        representatives = [values[0] for values in by_final.values()]
        fibre_sizes.append(len(representatives))
        # A spanning witness set is enough to certify every distinct block:
        # compare one canonical representative with each other stable class in
        # the fibre.  The exact extractor itself accepts any requested pair;
        # materializing every quadratic pair would turn a certificate into a
        # needlessly expensive benchmark.
        if representatives:
            left = representatives[0]
            for right in representatives[1:]:
                suffix = _distinguishing_suffix(
                    universe,
                    mode,
                    tuple(history),
                    left,
                    right,
                )
                assert _suffix_response(
                    universe, level, mode, left, suffix
                ) != _suffix_response(universe, level, mode, right, suffix)
                suffix_lengths.append(len(suffix))
                witness_pairs += 1

    histogram = Counter(fibre_sizes)
    maximum_fibre = max(fibre_sizes)
    family_fibres = []
    for family in sorted({node.tag.family for node in universe.nodes.values()}):
        family_nodes = {
            node_id: node
            for node_id, node in universe.nodes.items()
            if node.tag.family == family
        }
        family_base_to_blocks: dict[object, set[int]] = defaultdict(set)
        for node_id, node in family_nodes.items():
            family_base_to_blocks[_local_signature(node, level)].add(
                blocks[node_id]
            )
        family_sizes = tuple(
            len(values) for values in family_base_to_blocks.values()
        )
        family_maximum = max(family_sizes)
        family_fibres.append(
            _FamilyFibreAudit(
                family,
                len(family_nodes),
                len(family_base_to_blocks),
                len({blocks[node_id] for node_id in family_nodes}),
                sum(size > 1 for size in family_sizes),
                family_maximum,
                (family_maximum - 1).bit_length(),
            )
        )
    audit = _QuotientAudit(
        level,
        mode,
        states=len(universe.nodes),
        base_classes=len(base_to_nodes),
        initial_classes=len(set(initial.values())),
        stable_classes=len(set(blocks.values())),
        refinement_rounds=len(history) - 1,
        transport_forced_splits=(
            len(set(blocks.values())) - len(set(initial.values()))
        ),
        nontrivial_fibres=sum(size > 1 for size in fibre_sizes),
        maximum_fibre=maximum_fibre,
        maximum_residual_bits=(maximum_fibre - 1).bit_length(),
        fibre_histogram=tuple(sorted(histogram.items())),
        witness_pairs=witness_pairs,
        shortest_suffix=min(suffix_lengths, default=0),
        longest_suffix=max(suffix_lengths, default=0),
        family_fibres=tuple(family_fibres),
        compilation_seconds=perf_counter() - started,
    )
    return _PartitionResult(audit, blocks, tuple(history))


def _bottom_up_blocks(
    universe: _Universe,
    level: int | None,
    mode: _Mode,
) -> dict[_NodeId, int]:
    """Independently hash an acyclic response tree, optionally with a base."""

    by_remaining: dict[int, list[_NodeId]] = defaultdict(list)
    for node_id, node in universe.nodes.items():
        by_remaining[node.task.horizon - node.state.step].append(node_id)
    labels: dict[object, int] = {}
    result: dict[_NodeId, int] = {}
    for remaining in sorted(by_remaining):
        for node_id in sorted(by_remaining[remaining], key=repr):
            node = universe.nodes[node_id]
            edges = []
            for edge in node.edges:
                observation = _edge_observation(edge, mode)
                if edge.next_node is not None:
                    observation = observation + (result[edge.next_node],)
                edges.append(observation)
            key = (
                None
                if level is None
                else _local_signature(node, level),
                _state_output(node, mode),
                tuple(edges),
            )
            if key not in labels:
                labels[key] = len(labels)
            result[node_id] = labels[key]
    return result


def _transport_audit(
    universe: _Universe,
    level: int,
    mode: _Mode,
    blocks: dict[_NodeId, int],
) -> _TransportAudit:
    representatives: dict[int, _NodeId] = {}
    block_families: dict[int, set[str]] = defaultdict(set)
    for node_id, block in blocks.items():
        representatives.setdefault(block, node_id)
        block_families[block].add(universe.nodes[node_id].tag.family)

    live_edges = terminal_edges = invalid_edges = 0
    target_sources: list[dict[int, set[int]]] = [defaultdict(set), defaultdict(set)]
    for block, node_id in representatives.items():
        node = universe.nodes[node_id]
        for bit, edge in enumerate(node.edges):
            if edge.outcome == "invalid":
                invalid_edges += 1
            elif edge.next_node is None:
                terminal_edges += 1
            else:
                live_edges += 1
                target_sources[bit][blocks[edge.next_node]].add(block)
    merged_targets = sum(
        len(sources) > 1
        for by_target in target_sources
        for sources in by_target.values()
    )
    excess_preimages = sum(
        max(0, len(sources) - 1)
        for by_target in target_sources
        for sources in by_target.values()
    )

    behavior_blocks = _bottom_up_blocks(universe, None, mode)
    type_families: dict[int, set[str]] = defaultdict(set)
    for node_id, behavior in behavior_blocks.items():
        type_families[behavior].add(universe.nodes[node_id].tag.family)
    number_of_families = len({node.tag.family for node in universe.nodes.values()})
    return _TransportAudit(
        level,
        mode,
        quotient_classes=len(representatives),
        live_edges=live_edges,
        terminal_edges=terminal_edges,
        invalid_edges=invalid_edges,
        merged_live_targets=merged_targets,
        excess_live_preimages=excess_preimages,
        mixed_family_classes=sum(
            len(families) > 1 for families in block_families.values()
        ),
        behavior_types=len(type_families),
        types_shared_by_two_families=sum(
            len(families) >= 2 for families in type_families.values()
        ),
        types_shared_by_all_families=sum(
            len(families) == number_of_families
            for families in type_families.values()
        ),
        task_specific_types=sum(
            len(families) == 1 for families in type_families.values()
        ),
    )


@pytest.fixture(scope="module")
def _phase8_analysis() -> tuple[
    _Universe,
    dict[tuple[int, _Mode], _PartitionResult],
    dict[tuple[int, _Mode], _TransportAudit],
]:
    universe = _build_universe()
    partitions = {}
    transports = {}
    for level in (0, 1, 2):
        for mode in (
            "policy_digit",
            "policy_decoder",
            "value_digit",
            "value_decoder",
            "full",
        ):
            result = _partition(universe, level, mode)
            partitions[(level, mode)] = result
            transports[(level, mode)] = _transport_audit(
                universe,
                level,
                mode,
                result.blocks,
            )
            if mode == "full":
                bottom_up = _bottom_up_blocks(universe, level, mode)
                assert _block_sets(bottom_up) == _block_sets(result.blocks)
    return universe, partitions, transports


def test_gate8a_selected_phase7_graphs_are_reconstructed_exactly(
    _phase8_analysis: tuple[
        _Universe,
        dict[tuple[int, _Mode], _PartitionResult],
        dict[tuple[int, _Mode], _TransportAudit],
    ],
):
    universe, _, _ = _phase8_analysis
    expected = {
        "R3": _FamilyCensus(182, 682, 1316, 370, 434, 12, 0, 7, 14, 2),
        "R5": _FamilyCensus(182, 838, 1646, 448, 522, 20, 0, 7, 14, 2),
        "R7": _FamilyCensus(182, 880, 1738, 450, 564, 26, 0, 7, 14, 2),
        "D6": _FamilyCensus(182, 988, 1928, 662, 384, 76, 0, 12, 24, 3),
        "D8": _FamilyCensus(182, 1168, 2288, 842, 204, 256, 0, 17, 34, 4),
        "P4": _FamilyCensus(182, 886, 1750, 446, 574, 26, 0, 7, 14, 2),
        "P6": _FamilyCensus(182, 1342, 2662, 810, 548, 144, 0, 14, 28, 3),
        "I": _FamilyCensus(224, 1552, 3048, 812, 868, 40, 0, 13, 26, 3),
    }
    assert universe.family_censuses == expected
    assert len(universe.nodes) == sum(item.states for item in expected.values())
    assert all(
        edge.outcome in {
            "invalid",
            "live",
            "success_exact",
            "success_precision",
            "cycle",
            "horizon",
        }
        for node in universe.nodes.values()
        for edge in node.edges
    )


def test_gate8b_stable_extensions_are_exact_and_interface_monotone(
    _phase8_analysis: tuple[
        _Universe,
        dict[tuple[int, _Mode], _PartitionResult],
        dict[tuple[int, _Mode], _TransportAudit],
    ],
):
    _, partitions, _ = _phase8_analysis
    for mode in (
        "policy_digit",
        "policy_decoder",
        "value_digit",
        "value_decoder",
        "full",
    ):
        audits = [partitions[(level, mode)].audit for level in (0, 1, 2)]
        assert [audit.base_classes for audit in audits] == sorted(
            audit.base_classes for audit in audits
        )
        assert [audit.stable_classes for audit in audits] == sorted(
            audit.stable_classes for audit in audits
        )
        assert all(audit.stable_classes >= audit.initial_classes for audit in audits)
        assert all(audit.maximum_fibre >= 1 for audit in audits)

    stable_expected = {
        "policy_digit": (2636, 8056, 8126),
        "policy_decoder": (2636, 8056, 8126),
        "value_digit": (2636, 8056, 8126),
        "value_decoder": (6046, 8126, 8126),
        "full": (8128, 8128, 8128),
    }
    for mode, expected in stable_expected.items():
        assert tuple(
            partitions[(level, mode)].audit.base_classes
            for level in (0, 1, 2)
        ) == (866, 5970, 6044)
        assert tuple(
            partitions[(level, mode)].audit.stable_classes
            for level in (0, 1, 2)
        ) == expected

    # Once every exact continuation response is observed, S0 already refines
    # to the same relation as S1 and S2.  Conversely, the four scalar modes
    # induce one common S2-stable relation, two classes coarser than the full
    # decoder-preserving response quotient.
    assert _block_sets(partitions[(0, "full")].blocks) == _block_sets(
        partitions[(1, "full")].blocks
    )
    assert _block_sets(partitions[(1, "full")].blocks) == _block_sets(
        partitions[(2, "full")].blocks
    )
    scalar_modes = (
        "policy_digit",
        "policy_decoder",
        "value_digit",
        "value_decoder",
    )
    scalar_partition = _block_sets(partitions[(2, scalar_modes[0])].blocks)
    assert all(
        _block_sets(partitions[(2, mode)].blocks) == scalar_partition
        for mode in scalar_modes[1:]
    )
    full_blocks = partitions[(2, "full")].blocks
    scalar_blocks = partitions[(2, scalar_modes[0])].blocks
    assert scalar_partition != _block_sets(full_blocks)
    full_to_scalar: dict[int, set[int]] = defaultdict(set)
    for node_id, full_block in full_blocks.items():
        full_to_scalar[full_block].add(scalar_blocks[node_id])
    assert all(len(values) == 1 for values in full_to_scalar.values())


def test_gate8c_s2_retains_nontrivial_witnessed_fibres(
    _phase8_analysis: tuple[
        _Universe,
        dict[tuple[int, _Mode], _PartitionResult],
        dict[tuple[int, _Mode], _TransportAudit],
    ],
):
    _, partitions, _ = _phase8_analysis
    for mode in (
        "policy_digit",
        "policy_decoder",
        "value_digit",
        "value_decoder",
        "full",
    ):
        audit = partitions[(2, mode)].audit
        assert audit.nontrivial_fibres > 0
        assert audit.maximum_residual_bits > 0
        assert audit.witness_pairs > 0
        assert audit.longest_suffix <= 8

    expected = {
        "policy_digit": (6172, 8126, 3, 1954, 726, 70, 7, 2082, 0, 3),
        "policy_decoder": (6154, 8126, 3, 1972, 726, 70, 7, 2082, 0, 3),
        "value_digit": (6424, 8126, 3, 1702, 726, 70, 7, 2082, 0, 3),
        "value_decoder": (6970, 8126, 3, 1156, 726, 70, 7, 2082, 0, 3),
        "full": (6044, 8128, 3, 2084, 728, 70, 7, 2084, 1, 3),
    }
    for mode, values in expected.items():
        audit = partitions[(2, mode)].audit
        assert audit.states == 8336
        assert audit.base_classes == 6044
        assert (
            audit.initial_classes,
            audit.stable_classes,
            audit.refinement_rounds,
            audit.transport_forced_splits,
            audit.nontrivial_fibres,
            audit.maximum_fibre,
            audit.maximum_residual_bits,
            audit.witness_pairs,
            audit.shortest_suffix,
            audit.longest_suffix,
        ) == values

    family_expected = {
        "D6": (988, 800, 988, 42, 24, 5),
        "D8": (1168, 978, 1166, 42, 24, 5),
        "I": (1552, 1202, 1548, 96, 28, 5),
        "P4": (886, 768, 886, 22, 11, 4),
        "P6": (1342, 1216, 1334, 22, 11, 4),
        "R3": (682, 494, 682, 42, 24, 5),
        "R5": (838, 680, 838, 32, 15, 4),
        "R7": (880, 746, 880, 14, 11, 4),
    }
    for mode in expected:
        assert {
            item.family: (
                item.states,
                item.base_classes,
                item.stable_classes,
                item.nontrivial_fibres,
                item.maximum_fibre,
                item.maximum_residual_bits,
            )
            for item in partitions[(2, mode)].audit.family_fibres
        } == family_expected


def test_gate8d_transport_is_well_defined_but_not_a_group_action(
    _phase8_analysis: tuple[
        _Universe,
        dict[tuple[int, _Mode], _PartitionResult],
        dict[tuple[int, _Mode], _TransportAudit],
    ],
):
    _, partitions, transports = _phase8_analysis
    for mode in (
        "policy_digit",
        "policy_decoder",
        "value_digit",
        "value_decoder",
        "full",
    ):
        quotient = partitions[(2, mode)].audit
        transport = transports[(2, mode)]
        assert transport.quotient_classes == quotient.stable_classes
        assert transport.terminal_edges > 0
        assert transport.invalid_edges > 0
        assert transport.excess_live_preimages > 0
        assert transport.task_specific_types > 0
        assert transport.types_shared_by_two_families > 0
        assert quotient.nontrivial_fibres < quotient.base_classes


    expected = {
        "policy_digit": (8126, 6744, 9226, 282, 56, 56, 194, 435, 144, 12, 291),
        "policy_decoder": (8126, 6744, 9226, 282, 56, 56, 194, 395, 138, 12, 257),
        "value_digit": (8126, 6744, 9226, 282, 56, 56, 194, 437, 144, 12, 293),
        "value_decoder": (8126, 6744, 9226, 282, 56, 56, 194, 3687, 331, 0, 3356),
        "full": (8128, 6744, 9230, 282, 56, 56, 194, 8058, 194, 0, 7864),
    }
    for mode, values in expected.items():
        transport = transports[(2, mode)]
        assert (
            transport.quotient_classes,
            transport.live_edges,
            transport.terminal_edges,
            transport.invalid_edges,
            transport.merged_live_targets,
            transport.excess_live_preimages,
            transport.mixed_family_classes,
            transport.behavior_types,
            transport.types_shared_by_two_families,
            transport.types_shared_by_all_families,
            transport.task_specific_types,
        ) == values


def _report() -> dict[str, object]:
    universe = _build_universe()
    reports = {}
    transports = {}
    for level in (0, 1, 2):
        for mode in (
            "policy_digit",
            "policy_decoder",
            "value_digit",
            "value_decoder",
            "full",
        ):
            result = _partition(universe, level, mode)
            reports[f"S{level}:{mode}"] = asdict(result.audit)
            transports[f"S{level}:{mode}"] = asdict(
                _transport_audit(universe, level, mode, result.blocks)
            )
    return {
        "states": len(universe.nodes),
        "compilation_seconds": universe.compilation_seconds,
        "families": {
            key: asdict(value)
            for key, value in universe.family_censuses.items()
        },
        "quotients": reports,
        "transports": transports,
    }


if __name__ == "__main__":
    print(json.dumps(_report(), indent=2, sort_keys=True))

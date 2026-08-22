"""Finite history geometry and prefix-code representation strategies.

This module makes one representation scheme explicit: ordered process histories
form a prefix tree, process time can be measured by root-to-node depth, and the
number of distinguishable prefixes at each depth gives a finite boundary/frontier
profile.  A Huffman code is provided as one optional way to redistribute depth
when a probability/usage measure on task-relevant outcomes is supplied.

The tree geometry is a representation object, not a claim that every notion of
computational time or space is identical to tree depth or boundary width.
Likewise Huffman coding is a strategy layered on top of history/task structure;
it is not part of Shakespeare's process ontology.
"""

from __future__ import annotations

from dataclasses import dataclass
import heapq
import itertools
import math
from typing import Callable, Generic, Hashable, Mapping, Sequence, TypeVar

from .core import ProcessWord

StepT = TypeVar("StepT")
SymbolT = TypeVar("SymbolT", bound=Hashable)
KeyT = TypeVar("KeyT", bound=Hashable)


@dataclass(frozen=True)
class BoundaryProfile:
    """Finite prefix-frontier profile of a history family.

    ``widths[d]`` is the number of distinguishable prefixes at process depth
    ``d``.  The root is depth zero.  ``information_widths`` stores
    ``log2(width)`` and is therefore the number of bits needed merely to name a
    frontier element under an ideal uniform code; it is not by itself a memory
    bound for an arbitrary execution model.
    """

    widths: tuple[int, ...]
    information_widths: tuple[float, ...]

    @property
    def max_depth(self) -> int:
        return len(self.widths) - 1

    @property
    def peak_width(self) -> int:
        return max(self.widths, default=0)

    @property
    def peak_information_width(self) -> float:
        return max(self.information_widths, default=0.0)

    def exponential_growth_rates(self) -> tuple[float, ...]:
        """Return ``log(width[d]) / d`` for positive depths.

        Natural logarithms are used so this can be compared with ordinary
        exponential-growth/entropy rates.  Empty frontiers contribute
        ``-inf``.
        """

        rates: list[float] = []
        for depth, width in enumerate(self.widths[1:], start=1):
            rates.append(math.log(width) / depth if width > 0 else -math.inf)
        return tuple(rates)


def history_depth(
    history: ProcessWord[StepT],
    step_cost: Mapping[StepT, float] | Callable[[StepT], float] | None = None,
) -> float:
    """Return unweighted or caller-weighted process depth of one history."""

    if step_cost is None:
        return float(history.depth)

    if callable(step_cost):
        cost_of = step_cost
    else:
        cost_of = step_cost.__getitem__

    total = 0.0
    for step in history:
        value = float(cost_of(step))
        if not math.isfinite(value) or value < 0:
            raise ValueError("step costs must be finite and non-negative")
        total += value
    return total


def boundary_profile(
    histories: Sequence[ProcessWord[StepT]],
    *,
    max_depth: int | None = None,
    quotient_key: Callable[[ProcessWord[StepT]], Hashable] | None = None,
) -> BoundaryProfile:
    """Compute finite frontier widths for a set of literal histories.

    Parameters
    ----------
    histories:
        Histories whose prefix closure defines the finite tree.
    max_depth:
        Optional truncation depth.  By default the deepest supplied history is
        used.
    quotient_key:
        Optional caller-defined key for identifying prefixes at each depth.
        This is the hook through which exact normal forms or task-sufficient
        quotient labels can be reflected in the boundary geometry.  Shakespeare
        does not infer such a quotient merely from symbolic equality.
    """

    histories = tuple(histories)
    if max_depth is None:
        bound = max((history.depth for history in histories), default=0)
    else:
        if max_depth < 0:
            raise ValueError("max_depth must be non-negative")
        bound = max_depth

    identify = quotient_key or (lambda word: word)
    widths: list[int] = []
    information: list[float] = []

    for depth in range(bound + 1):
        prefixes: set[Hashable] = set()
        if depth == 0:
            prefixes.add(identify(ProcessWord()))
        else:
            for history in histories:
                if history.depth < depth:
                    continue
                prefix = ProcessWord(history.steps[:depth])
                prefixes.add(identify(prefix))
        width = len(prefixes)
        widths.append(width)
        information.append(math.log2(width) if width > 0 else -math.inf)

    return BoundaryProfile(tuple(widths), tuple(information))


@dataclass(frozen=True)
class PrefixCodeMetrics:
    """Geometry/information metrics of one finite prefix presentation."""

    expected_depth: float
    worst_depth: int
    kraft_sum: float
    entropy: float
    redundancy: float
    leaf_count: int


@dataclass(frozen=True)
class PrefixCode(Generic[SymbolT]):
    """A finite binary prefix code together with its source weights."""

    codes: Mapping[SymbolT, tuple[int, ...]]
    weights: Mapping[SymbolT, float]

    def __post_init__(self) -> None:
        if set(self.codes) != set(self.weights):
            raise ValueError("codes and weights must have identical symbol sets")
        for code in self.codes.values():
            if not code or any(bit not in (0, 1) for bit in code):
                raise ValueError("binary codes must be non-empty tuples of 0/1")
        if not self.is_prefix_free():
            raise ValueError("codes are not prefix-free")

    def is_prefix_free(self) -> bool:
        codewords = tuple(self.codes.values())
        for i, left in enumerate(codewords):
            for j, right in enumerate(codewords):
                if i == j:
                    continue
                if len(left) <= len(right) and right[: len(left)] == left:
                    return False
        return True

    def metrics(self) -> PrefixCodeMetrics:
        total = sum(float(weight) for weight in self.weights.values())
        if total <= 0:
            raise ValueError("total code weight must be positive")

        expected = 0.0
        entropy = 0.0
        for symbol, raw_weight in self.weights.items():
            probability = float(raw_weight) / total
            if probability > 0:
                expected += probability * len(self.codes[symbol])
                entropy -= probability * math.log2(probability)

        kraft = sum(2.0 ** (-len(code)) for code in self.codes.values())
        worst = max((len(code) for code in self.codes.values()), default=0)
        return PrefixCodeMetrics(
            expected_depth=expected,
            worst_depth=worst,
            kraft_sum=kraft,
            entropy=entropy,
            redundancy=expected - entropy,
            leaf_count=len(self.codes),
        )

    def encode(self, symbols: Sequence[SymbolT]) -> tuple[int, ...]:
        bits: list[int] = []
        for symbol in symbols:
            try:
                bits.extend(self.codes[symbol])
            except KeyError as exc:
                raise KeyError(f"symbol has no prefix code: {symbol!r}") from exc
        return tuple(bits)

    def decode(self, bits: Sequence[int]) -> tuple[SymbolT, ...]:
        """Decode a concatenation of codewords; reject incomplete prefixes."""

        inverse = {code: symbol for symbol, code in self.codes.items()}
        out: list[SymbolT] = []
        prefix: tuple[int, ...] = ()
        valid_prefixes = {
            code[:length]
            for code in inverse
            for length in range(1, len(code) + 1)
        }

        for raw_bit in bits:
            if raw_bit not in (0, 1):
                raise ValueError("encoded stream must contain only 0/1")
            prefix = prefix + (int(raw_bit),)
            if prefix in inverse:
                out.append(inverse[prefix])
                prefix = ()
            elif prefix not in valid_prefixes:
                raise ValueError("bit stream does not match the prefix code")

        if prefix:
            raise ValueError("bit stream ends in an incomplete codeword")
        return tuple(out)


@dataclass(frozen=True)
class _HuffmanNode(Generic[SymbolT]):
    symbol: SymbolT | None = None
    left: "_HuffmanNode[SymbolT] | None" = None
    right: "_HuffmanNode[SymbolT] | None" = None

    @property
    def is_leaf(self) -> bool:
        return self.symbol is not None


def huffman_prefix_code(weights: Mapping[SymbolT, float]) -> PrefixCode[SymbolT]:
    """Build a deterministic binary Huffman code for a finite weighted boundary.

    The symbol set is fixed by the caller.  This routine therefore optimizes
    code depth *after* the representation/task layer has decided which outcomes
    remain distinguishable; it does not discover new process primitives.
    """

    if not weights:
        raise ValueError("at least one symbol is required")

    normalized: dict[SymbolT, float] = {}
    for symbol, raw_weight in weights.items():
        weight = float(raw_weight)
        if not math.isfinite(weight) or weight < 0:
            raise ValueError("Huffman weights must be finite and non-negative")
        normalized[symbol] = weight
    if sum(normalized.values()) <= 0:
        raise ValueError("at least one Huffman weight must be positive")

    counter = itertools.count()
    heap: list[tuple[float, int, _HuffmanNode[SymbolT]]] = []
    for symbol, weight in normalized.items():
        heapq.heappush(heap, (weight, next(counter), _HuffmanNode(symbol=symbol)))

    if len(heap) == 1:
        _weight, _serial, node = heap[0]
        assert node.symbol is not None
        return PrefixCode(codes={node.symbol: (0,)}, weights=normalized)

    while len(heap) > 1:
        left_weight, _left_serial, left = heapq.heappop(heap)
        right_weight, _right_serial, right = heapq.heappop(heap)
        parent = _HuffmanNode(left=left, right=right)
        heapq.heappush(
            heap,
            (left_weight + right_weight, next(counter), parent),
        )

    root = heap[0][2]
    codes: dict[SymbolT, tuple[int, ...]] = {}

    def visit(node: _HuffmanNode[SymbolT], prefix: tuple[int, ...]) -> None:
        if node.is_leaf:
            assert node.symbol is not None
            codes[node.symbol] = prefix
            return
        assert node.left is not None and node.right is not None
        visit(node.left, prefix + (0,))
        visit(node.right, prefix + (1,))

    visit(root, ())
    return PrefixCode(codes=codes, weights=normalized)

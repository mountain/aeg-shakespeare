"""Bounded A/M-history jet and blind moving-normalization search.

The search receives coefficient histories and a frozen observer grammar.  It
does not receive the expected observer, its rates, or labelled samples.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement

import sympy as sp

from process_geometry.presentation.canonicalization import ConstraintCanonicalization


@dataclass(frozen=True)
class AMHistory:
    """A finite expression history with compositional value/rate semantics."""

    operation: str
    arguments: tuple["AMHistory", ...] = ()
    atom: sp.Expr | None = None

    @classmethod
    def constant(cls, value: int) -> "AMHistory":
        return cls("constant", atom=sp.Integer(value))

    @classmethod
    def clock(cls) -> "AMHistory":
        return cls("clock")

    def __add__(self, other: "AMHistory") -> "AMHistory":
        return AMHistory("add", (self, other))

    def __mul__(self, other: "AMHistory") -> "AMHistory":
        return AMHistory("mul", (self, other))

    def jet(self, clock: sp.Symbol) -> tuple[sp.Expr, sp.Expr]:
        """Evaluate the 1-jet using only A/M composition rules."""

        if self.operation == "constant":
            return sp.sympify(self.atom), sp.S.Zero
        if self.operation == "clock":
            return clock, sp.S.One
        left_value, left_rate = self.arguments[0].jet(clock)
        right_value, right_rate = self.arguments[1].jet(clock)
        if self.operation == "add":
            return (
                sp.expand(left_value + right_value),
                sp.expand(left_rate + right_rate),
            )
        if self.operation == "mul":
            return (
                sp.expand(left_value * right_value),
                sp.expand(left_rate * right_value + left_value * right_rate),
            )
        raise ValueError(f"unknown A/M operation: {self.operation}")

    @property
    def depth(self) -> int:
        if not self.arguments:
            return 0
        return 1 + max(argument.depth for argument in self.arguments)


@dataclass(frozen=True)
class ObserverCandidate:
    origin: AMHistory
    scale: AMHistory
    origin_value: sp.Expr
    scale_value: sp.Expr
    origin_rate: sp.Expr
    scale_rate: sp.Expr
    observed: sp.Expr
    reconstruction_residual: sp.Expr


@dataclass(frozen=True)
class BlindSearchResult:
    literal_candidate_count: int
    semantic_candidate_count: int
    candidates: tuple[ObserverCandidate, ...]
    static_candidates: tuple[ObserverCandidate, ...]
    fixed_variation: int
    canonical_variation: int | None


@dataclass(frozen=True)
class NormalizationFamily:
    """One frozen exact normalization schema in the bounded selector."""

    name: str
    carrier_degree: int
    kind: str


@dataclass(frozen=True)
class FamilyCandidate:
    """A family/observer pair passing every exact discovery obligation."""

    family: str
    origin_value: sp.Expr
    scale_value: sp.Expr
    origin_rate: sp.Expr
    scale_rate: sp.Expr
    observed: sp.Expr
    reconstruction_residual: sp.Expr
    variation: int


@dataclass(frozen=True)
class FamilySelectionResult:
    """All certified candidates and the unresolved minimum-cost slice."""

    candidates: tuple[FamilyCandidate, ...]
    best_candidates: tuple[FamilyCandidate, ...]
    fixed_variation: int

    @property
    def ambiguous(self) -> bool:
        return len(self.best_candidates) > 1


@dataclass(frozen=True)
class ChartMorphismCertificate:
    """Exact moving-chart conjugacy without reparameterizing the clock."""

    scale: sp.Expr
    shift: sp.Expr
    scale_rate: sp.Expr
    shift_rate: sp.Expr
    dynamics_residual: sp.Expr

    @property
    def certified(self) -> bool:
        return sp.simplify(self.dynamics_residual) == 0


@dataclass(frozen=True)
class DiscoveredTaskMorphism:
    """A bounded A/M affine morphism passing task, lift, and dynamics checks."""

    scale_history: AMHistory
    shift_history: AMHistory
    scale: sp.Expr
    shift: sp.Expr
    scale_rate: sp.Expr
    shift_rate: sp.Expr
    task_residuals: tuple[sp.Expr, ...]
    reconstruction_residual: sp.Expr
    dynamics_residual: sp.Expr


@dataclass(frozen=True)
class MorphismSearchResult:
    """Exact census and survivors of one blind presentation-morphism search."""

    grammar_literal_count: int
    grammar_semantic_count: int
    candidates: tuple[DiscoveredTaskMorphism, ...]


FROZEN_NORMALIZATION_FAMILIES = (
    NormalizationFamily("affine-root-unit", 1, "affine_root_unit"),
    NormalizationFamily("quadratic-root-pair", 2, "quadratic_root_pair"),
    NormalizationFamily("quadratic-vertex-unit", 2, "quadratic_vertex_unit"),
)


def riccati_coefficient_histories() -> tuple[AMHistory, AMHistory, AMHistory]:
    """Declare ``t(t+1), -(2t+1), 1`` as finite A/M histories."""

    t = AMHistory.clock()
    one = AMHistory.constant(1)
    minus_one = AMHistory.constant(-1)
    return (
        t * (t + one),
        minus_one * ((t + t) + one),
        one,
    )


def affine_coefficient_histories() -> tuple[AMHistory, ...]:
    """Held-out affine carrier ``x'=x-t``."""

    t = AMHistory.clock()
    return (AMHistory.constant(-1) * t, AMHistory.constant(1))


def centered_quadratic_histories() -> tuple[AMHistory, ...]:
    """Held-out symmetric carrier ``x'=(x-t)^2-1``."""

    t = AMHistory.clock()
    one = AMHistory.constant(1)
    minus_one = AMHistory.constant(-1)
    return (t * t + minus_one, minus_one * (t + t), one)


def cubic_completion_histories() -> tuple[AMHistory, ...]:
    """A degree-three process outside every frozen normalization family."""

    return (*riccati_coefficient_histories(), AMHistory.constant(1))


def bounded_observer_grammar(
    *, max_depth: int = 1
) -> tuple[int, tuple[AMHistory, ...]]:
    """Bounded grammar, semantically quotiented by exact clock polynomial."""

    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    t = sp.Symbol("t", real=True)
    seeds = (
        AMHistory.constant(-1),
        AMHistory.constant(0),
        AMHistory.constant(1),
        AMHistory.clock(),
    )
    semantic: dict[sp.Expr, AMHistory] = {}
    for history in seeds:
        semantic[history.jet(t)[0]] = history
    literal_count = len(seeds)
    for _depth in range(1, max_depth + 1):
        basis = tuple(semantic.values())
        generated: list[AMHistory] = []
        for left, right in combinations_with_replacement(basis, 2):
            generated.extend((left + right, left * right))
        literal_count += len(generated)
        for history in generated:
            value, _rate = history.jet(t)
            semantic.setdefault(sp.expand(value), history)
    ordered = tuple(semantic[value] for value in sorted(semantic, key=sp.srepr))
    return literal_count, ordered


def blind_root_normalization_search(
    coefficient_histories: tuple[AMHistory, AMHistory, AMHistory],
    *,
    cubic_perturbation: sp.Expr = sp.S.Zero,
) -> BlindSearchResult:
    """Search the frozen grammar by exact identities, with no answer labels."""

    t, y = sp.symbols("t y", real=True)
    a_symbol, b_symbol, c_symbol = sp.symbols("a b c")
    r, d = sp.symbols("r d", nonzero=True)
    coefficient_jets = tuple(history.jet(t) for history in coefficient_histories)
    a, b, c = (jet[0] for jet in coefficient_jets)
    base_rates = {
        symbol: jet[1]
        for symbol, jet in zip(
            (a_symbol, b_symbol, c_symbol), coefficient_jets, strict=True
        )
    }
    normalization = ConstraintCanonicalization(
        observer_parameters=(r, d),
        constraints=(
            a_symbol + b_symbol * r + c_symbol * r**2,
            a_symbol + b_symbol * (r + d) + c_symbol * (r + d) ** 2,
        ),
        label="blind ordered Riccati roots",
    )
    connection = normalization.induced_connection(base_rates)
    literal_count, grammar = bounded_observer_grammar()
    candidates: list[ObserverCandidate] = []

    for origin in grammar:
        q, q_rate = origin.jet(t)
        for scale in grammar:
            s, s_rate = scale.jet(t)
            anchor_scale = sp.expand(s).subs(t, 0)
            if anchor_scale.is_positive is not True:
                continue
            substitutions = {
                a_symbol: a,
                b_symbol: b,
                c_symbol: c,
                r: q,
                d: s,
            }
            if any(
                sp.expand(constraint.subs(substitutions)) != 0
                for constraint in normalization.constraints
            ):
                continue
            induced_rates = (
                sp.simplify(connection.rate(r).subs(substitutions)),
                sp.simplify(connection.rate(d).subs(substitutions)),
            )
            if induced_rates != (q_rate, s_rate):
                continue

            x_in_chart = sp.expand(q + s * y)
            physical = sp.expand(
                a + b * x_in_chart + c * x_in_chart**2
                + sp.sympify(cubic_perturbation) * x_in_chart**3
            )
            observed = sp.expand(
                physical / s - q_rate / s - s_rate * y / s
            )
            reconstruction = sp.cancel(
                q_rate + s_rate * y + s * observed - physical
            )
            candidates.append(
                ObserverCandidate(
                    origin=origin,
                    scale=scale,
                    origin_value=q,
                    scale_value=s,
                    origin_rate=q_rate,
                    scale_rate=s_rate,
                    observed=observed,
                    reconstruction_residual=reconstruction,
                )
            )

    static = tuple(
        candidate
        for candidate in candidates
        if t not in candidate.origin_value.free_symbols
        and t not in candidate.scale_value.free_symbols
    )
    fixed_variation = sum(t in value.free_symbols for value in (a, b, c))
    canonical_variation = None
    if len(candidates) == 1:
        polynomial = sp.Poly(candidates[0].observed, y)
        canonical_variation = sum(
            t in coefficient.free_symbols for coefficient in polynomial.all_coeffs()
        )
    return BlindSearchResult(
        literal_candidate_count=literal_count,
        semantic_candidate_count=len(grammar),
        candidates=tuple(candidates),
        static_candidates=static,
        fixed_variation=fixed_variation,
        canonical_variation=canonical_variation,
    )


def _family_constraints(
    family: NormalizationFamily,
    coefficients: tuple[sp.Symbol, ...],
    origin: sp.Symbol,
    scale: sp.Symbol,
) -> tuple[sp.Expr, ...]:
    if family.kind == "affine_root_unit":
        return (coefficients[0] + coefficients[1] * origin, scale - 1)
    if family.kind == "quadratic_root_pair":
        polynomial = lambda value: sum(  # noqa: E731 - local symbolic schema
            coefficient * value**degree
            for degree, coefficient in enumerate(coefficients[:3])
        )
        return (polynomial(origin), polynomial(origin + scale))
    if family.kind == "quadratic_vertex_unit":
        return (
            coefficients[1] + 2 * coefficients[2] * origin,
            coefficients[2] * scale - 1,
        )
    raise ValueError(f"unknown normalization family: {family.kind}")


def blind_normalization_family_selection(
    coefficient_histories: tuple[AMHistory, ...],
    *,
    families: tuple[NormalizationFamily, ...] = FROZEN_NORMALIZATION_FAMILIES,
    observer_depth: int = 1,
) -> FamilySelectionResult:
    """Apply every frozen family without receiving an expected family label."""

    t, y = sp.symbols("t y", real=True)
    r, d = sp.symbols("r d", nonzero=True)
    coefficient_symbols = sp.symbols(f"p0:{len(coefficient_histories)}")
    coefficient_jets = tuple(history.jet(t) for history in coefficient_histories)
    coefficient_values = tuple(jet[0] for jet in coefficient_jets)
    coefficient_rates = {
        symbol: jet[1]
        for symbol, jet in zip(
            coefficient_symbols, coefficient_jets, strict=True
        )
    }
    actual_degree = max(
        degree
        for degree, value in enumerate(coefficient_values)
        if sp.expand(value) != 0
    )
    _literal_count, grammar = bounded_observer_grammar(max_depth=observer_depth)
    candidates: list[FamilyCandidate] = []

    for family in families:
        # A family may not silently discard a higher completion direction.
        if actual_degree != family.carrier_degree:
            continue
        constraints = _family_constraints(family, coefficient_symbols, r, d)
        normalization = ConstraintCanonicalization(
            observer_parameters=(r, d),
            constraints=constraints,
            label=family.name,
        )
        connection = normalization.induced_connection(coefficient_rates)
        for origin in grammar:
            q, q_rate = origin.jet(t)
            for scale in grammar:
                s, s_rate = scale.jet(t)
                if sp.expand(s).subs(t, 0).is_positive is not True:
                    continue
                substitutions = {
                    **dict(zip(coefficient_symbols, coefficient_values, strict=True)),
                    r: q,
                    d: s,
                }
                if any(
                    sp.expand(constraint.subs(substitutions)) != 0
                    for constraint in constraints
                ):
                    continue
                induced_rates = (
                    sp.simplify(connection.rate(r).subs(substitutions)),
                    sp.simplify(connection.rate(d).subs(substitutions)),
                )
                if induced_rates != (q_rate, s_rate):
                    continue
                x_in_chart = sp.expand(q + s * y)
                physical = sp.expand(sum(
                    coefficient * x_in_chart**degree
                    for degree, coefficient in enumerate(coefficient_values)
                ))
                observed = sp.cancel(
                    physical / s - q_rate / s - s_rate * y / s
                )
                reconstruction = sp.cancel(
                    q_rate + s_rate * y + s * observed - physical
                )
                observed_coefficients = sp.Poly(observed, y).all_coeffs()
                candidates.append(FamilyCandidate(
                    family=family.name,
                    origin_value=q,
                    scale_value=s,
                    origin_rate=q_rate,
                    scale_rate=s_rate,
                    observed=sp.expand(observed),
                    reconstruction_residual=reconstruction,
                    variation=sum(
                        t in coefficient.free_symbols
                        for coefficient in observed_coefficients
                    ),
                ))

    fixed_variation = sum(
        t in coefficient.free_symbols for coefficient in coefficient_values
    )
    minimum = min((candidate.variation for candidate in candidates), default=None)
    best = tuple(
        candidate for candidate in candidates if candidate.variation == minimum
    )
    return FamilySelectionResult(
        candidates=tuple(candidates),
        best_candidates=best,
        fixed_variation=fixed_variation,
    )


def certify_affine_chart_morphism(
    source: FamilyCandidate,
    target: FamilyCandidate,
) -> ChartMorphismCertificate:
    """Certify the chart map forced by equality of physical reconstruction."""

    y = sp.Symbol("y", real=True)
    scale = sp.cancel(source.scale_value / target.scale_value)
    shift = sp.cancel(
        (source.origin_value - target.origin_value) / target.scale_value
    )
    scale_rate = sp.cancel(
        (
            source.scale_rate * target.scale_value
            - source.scale_value * target.scale_rate
        ) / target.scale_value**2
    )
    shift_rate = sp.cancel(
        (
            (source.origin_rate - target.origin_rate) * target.scale_value
            - (source.origin_value - target.origin_value) * target.scale_rate
        ) / target.scale_value**2
    )
    target_coordinate = sp.expand(scale * y + shift)
    transported_rate = sp.expand(
        scale_rate * y + scale * source.observed + shift_rate
    )
    target_rate = sp.expand(target.observed.subs(y, target_coordinate))
    return ChartMorphismCertificate(
        scale=scale,
        shift=shift,
        scale_rate=scale_rate,
        shift_rate=shift_rate,
        dynamics_residual=sp.cancel(transported_rate - target_rate),
    )


def task_equivalence_classes(
    candidates: tuple[FamilyCandidate, ...],
) -> tuple[tuple[FamilyCandidate, ...], ...]:
    """Quotient exact minimizers by clock-preserving affine conjugacy."""

    remaining = list(candidates)
    classes: list[tuple[FamilyCandidate, ...]] = []
    while remaining:
        representative = remaining.pop(0)
        equivalent = [representative]
        survivors: list[FamilyCandidate] = []
        for candidate in remaining:
            certificate = certify_affine_chart_morphism(representative, candidate)
            if (
                certificate.certified
                and representative.reconstruction_residual == 0
                and candidate.reconstruction_residual == 0
            ):
                equivalent.append(candidate)
            else:
                survivors.append(candidate)
        classes.append(tuple(equivalent))
        remaining = survivors
    return tuple(classes)


def task_section_coordinates(
    candidate: FamilyCandidate,
    physical_sections: tuple[sp.Expr, ...],
) -> tuple[sp.Expr, ...]:
    """Represent physical stopping sections in one observer chart."""

    return tuple(
        sp.cancel((section - candidate.origin_value) / candidate.scale_value)
        for section in physical_sections
    )


def blind_task_morphism_search(
    source: FamilyCandidate,
    target: FamilyCandidate,
    physical_sections: tuple[sp.Expr, ...],
    *,
    morphism_depth: int = 1,
) -> MorphismSearchResult:
    """Discover ``z=alpha*y+beta`` without receiving the expected map."""

    y = sp.Symbol("y", real=True)
    literal_count, grammar = bounded_observer_grammar(max_depth=morphism_depth)
    source_sections = task_section_coordinates(source, physical_sections)
    target_sections = task_section_coordinates(target, physical_sections)
    candidates: list[DiscoveredTaskMorphism] = []

    for scale_history in grammar:
        scale, scale_rate = scale_history.jet(sp.Symbol("t", real=True))
        if sp.expand(scale).subs(sp.Symbol("t", real=True), 0).is_zero is True:
            continue
        for shift_history in grammar:
            shift, shift_rate = shift_history.jet(sp.Symbol("t", real=True))
            target_coordinate = sp.expand(scale * y + shift)
            task_residuals = tuple(
                sp.expand(scale * source_value + shift - target_value)
                for source_value, target_value in zip(
                    source_sections, target_sections, strict=True
                )
            )
            if any(residual != 0 for residual in task_residuals):
                continue
            reconstruction_residual = sp.cancel(
                source.origin_value + source.scale_value * y
                - target.origin_value
                - target.scale_value * target_coordinate
            )
            if reconstruction_residual != 0:
                continue
            transported_rate = sp.expand(
                scale_rate * y + scale * source.observed + shift_rate
            )
            dynamics_residual = sp.cancel(
                transported_rate
                - target.observed.subs(y, target_coordinate)
            )
            if dynamics_residual != 0:
                continue
            candidates.append(DiscoveredTaskMorphism(
                scale_history=scale_history,
                shift_history=shift_history,
                scale=scale,
                shift=shift,
                scale_rate=scale_rate,
                shift_rate=shift_rate,
                task_residuals=task_residuals,
                reconstruction_residual=reconstruction_residual,
                dynamics_residual=dynamics_residual,
            ))
    return MorphismSearchResult(
        grammar_literal_count=literal_count,
        grammar_semantic_count=len(grammar),
        candidates=tuple(candidates),
    )


__all__ = [
    "AMHistory",
    "BlindSearchResult",
    "ChartMorphismCertificate",
    "DiscoveredTaskMorphism",
    "FROZEN_NORMALIZATION_FAMILIES",
    "FamilyCandidate",
    "FamilySelectionResult",
    "MorphismSearchResult",
    "NormalizationFamily",
    "ObserverCandidate",
    "affine_coefficient_histories",
    "blind_normalization_family_selection",
    "blind_task_morphism_search",
    "blind_root_normalization_search",
    "bounded_observer_grammar",
    "centered_quadratic_histories",
    "cubic_completion_histories",
    "certify_affine_chart_morphism",
    "riccati_coefficient_histories",
    "task_equivalence_classes",
    "task_section_coordinates",
]

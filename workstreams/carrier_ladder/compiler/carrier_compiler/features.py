"""Exact, syntax-directed feature and construction-height inference."""

from __future__ import annotations

from dataclasses import dataclass

from .ir import AbelTask, Add, Const, Exp, GeneralizedPolynomial, Log, Mul, Pow, ScaleExpr, Symbol, SymbolicIterate, children, walk


@dataclass(frozen=True)
class FeatureWitness:
    feature: str
    path: str
    node: str

    def to_data(self) -> dict[str, str]:
        return {"feature": self.feature, "path": self.path, "node": self.node}


@dataclass(frozen=True)
class FeatureReport:
    node_count: int
    construction_height: int | None
    features: frozenset[str]
    witnesses: tuple[FeatureWitness, ...]
    symbolic_height: bool


def construction_height(expr: ScaleExpr) -> int | None:
    """Return maximum finite exp/log nesting, or None for symbolic height."""

    if isinstance(expr, (SymbolicIterate, AbelTask)):
        return None
    heights = [construction_height(child) for child in children(expr)]
    if any(height is None for height in heights):
        return None
    child_height = max(heights, default=0)
    return child_height + 1 if isinstance(expr, (Exp, Log)) else child_height


def infer_features(expr: ScaleExpr) -> FeatureReport:
    witnesses: dict[str, FeatureWitness] = {}

    def add(feature: str, path: str, node: ScaleExpr) -> None:
        witnesses.setdefault(feature, FeatureWitness(feature, path, type(node).__name__))

    for path, node in walk(expr):
        add("rational", path, node)
        if isinstance(node, (Const, Symbol, Add, Mul)):
            add("finite-polynomial-germ", path, node)
        elif isinstance(node, Pow):
            if node.exponent.denominator == 1 and node.exponent >= 0:
                add("integer-power", path, node)
                add("finite-polynomial-germ", path, node)
            else:
                add("ordered-rational-monomial", path, node)
                if node.exponent.denominator == 1:
                    add("negative-integer-power", path, node)
        elif isinstance(node, GeneralizedPolynomial):
            add("ordered-rational-monomial", path, node)
            add("finite-generalized-polynomial-support", path, node)
        elif isinstance(node, (Exp, Log)):
            add("finite-exp-log", path, node)
            add("finite-construction-height", path, node)
        elif isinstance(node, SymbolicIterate):
            add("symbolic-height", path, node)
            add("iteration-normal-form", path, node)
        elif isinstance(node, AbelTask):
            add("symbolic-height", path, node)
            add("abel-functional-equation", path, node)

    height = construction_height(expr)
    return FeatureReport(
        node_count=sum(1 for _ in walk(expr)),
        construction_height=height,
        features=frozenset(witnesses),
        witnesses=tuple(sorted(witnesses.values(), key=lambda item: item.feature)),
        symbolic_height=height is None,
    )

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Any, Mapping, Sequence

from .model import (
    Budgets,
    EvaluationFailure,
    ExpQCoefficient,
    Meter,
    digest_json,
    lcm,
    parse_fraction,
)


Expr = Mapping[str, Any]


class WeightEvaluator:
    """Demand-driven exact coefficients in one normalized rational weight lattice."""

    def __init__(
        self,
        expression: Expr,
        target: Fraction,
        context: Mapping[str, object],
        budgets: Budgets,
    ) -> None:
        self.expression = expression
        self.target = target
        self.context = context
        self.budgets = budgets
        self.meter = Meter(budgets)
        self._keys: dict[int, str] = {}
        self._minimum_cache: dict[int, Fraction] = {}
        self._coefficient_cache: dict[tuple[int, Fraction], ExpQCoefficient] = {}
        self._validate_syntax(expression)
        self.lattice_denominator = self._lattice_denominator(expression, target)
        if self.lattice_denominator > budgets.max_lattice_denominator:
            raise EvaluationFailure(
                "resource_exceeded", "lattice-denominator-budget-exceeded"
            )
        if abs(target) > budgets.max_target_weight:
            raise EvaluationFailure("resource_exceeded", "target-weight-budget-exceeded")

    def coefficient(self) -> ExpQCoefficient:
        return self._coefficient(self.expression, self.target)

    def _node_key(self, node: Expr) -> str:
        identity = id(node)
        if identity not in self._keys:
            self._keys[identity] = digest_json(node)[:16]
        return self._keys[identity]

    def _validate_syntax(self, node: Expr) -> None:
        self.meter.nodes += 1
        if self.meter.nodes > self.budgets.max_nodes:
            raise EvaluationFailure("resource_exceeded", "node-budget-exceeded")
        op = node.get("op")
        if op == "finite":
            terms = node.get("terms")
            if not isinstance(terms, list):
                raise EvaluationFailure("unsupported", "malformed-finite-series")
            for term in terms:
                if not isinstance(term, dict):
                    raise EvaluationFailure("unsupported", "malformed-finite-series")
                parse_fraction(term.get("weight"), field="weight")
                parse_fraction(term.get("coefficient"), field="coefficient")
            return
        if op in {"add", "multiply"}:
            arguments = node.get("arguments")
            if not isinstance(arguments, list) or len(arguments) < 2:
                raise EvaluationFailure("unsupported", f"malformed-{op}")
            for argument in arguments:
                if not isinstance(argument, dict):
                    raise EvaluationFailure("unsupported", f"malformed-{op}")
                self._validate_syntax(argument)
            return
        if op in {"shift", "scale"}:
            argument = node.get("argument")
            if not isinstance(argument, dict):
                raise EvaluationFailure("unsupported", f"malformed-{op}")
            parse_fraction(node.get("by" if op == "shift" else "coefficient"))
            self._validate_syntax(argument)
            return
        if op in {"exp", "log1p"}:
            argument = node.get("argument")
            if not isinstance(argument, dict):
                raise EvaluationFailure("unsupported", f"malformed-{op}")
            self._validate_syntax(argument)
            return
        if op == "symbolic-iterate":
            raise EvaluationFailure("unsupported", "symbolic-height-outside-am-fragment")
        raise EvaluationFailure("unsupported", "unknown-expression-operation")

    def _collect_weights(self, node: Expr, weights: list[Fraction]) -> None:
        op = node["op"]
        if op == "finite":
            weights.extend(parse_fraction(term["weight"]) for term in node["terms"])
        elif op in {"add", "multiply"}:
            for argument in node["arguments"]:
                self._collect_weights(argument, weights)
        elif op == "shift":
            weights.append(parse_fraction(node["by"]))
            self._collect_weights(node["argument"], weights)
        elif op in {"scale", "exp", "log1p"}:
            self._collect_weights(node["argument"], weights)

    def _lattice_denominator(self, node: Expr, target: Fraction) -> int:
        weights = [target]
        self._collect_weights(node, weights)
        denominator = 1
        for weight in weights:
            denominator = lcm(denominator, weight.denominator)
        return denominator

    def _index(self, weight: Fraction) -> int:
        value = weight * self.lattice_denominator
        if value.denominator != 1:
            raise EvaluationFailure("unsupported", "weight-outside-normalized-lattice")
        return value.numerator

    def _weight(self, index: int) -> Fraction:
        return Fraction(index, self.lattice_denominator)

    def _minimum(self, node: Expr) -> Fraction:
        identity = id(node)
        cached = self._minimum_cache.get(identity)
        if cached is not None:
            return cached
        op = node["op"]
        if op == "finite":
            nonzero = [
                parse_fraction(term["weight"])
                for term in node["terms"]
                if parse_fraction(term["coefficient"])
            ]
            value = min(nonzero) if nonzero else Fraction(0)
        elif op == "add":
            structural = min(self._minimum(argument) for argument in node["arguments"])
            start = self._index(structural)
            horizon = start + self.budgets.max_target_weight * self.lattice_denominator
            value = structural
            for index in range(start, horizon + 1):
                candidate = self._weight(index)
                if not self._coefficient(node, candidate).is_zero:
                    value = candidate
                    break
        elif op == "multiply":
            value = sum((self._minimum(argument) for argument in node["arguments"]), Fraction(0))
        elif op == "scale":
            scalar = parse_fraction(node["coefficient"])
            value = self._minimum(node["argument"]) if scalar else Fraction(0)
        elif op == "shift":
            value = parse_fraction(node["by"]) + self._minimum(node["argument"])
        elif op == "exp":
            value = Fraction(0)
        elif op == "log1p":
            value = self._minimum(node["argument"])
        else:
            raise EvaluationFailure("unsupported", "unknown-expression-operation")
        self._minimum_cache[identity] = value
        return value

    def _require_completion(self, node: Expr, *, strict: bool) -> None:
        if not bool(self.context.get("positive_cone")):
            raise EvaluationFailure("unsupported", "positive-cone-required")
        minimum = self._minimum(node)
        if minimum < 0 or (strict and minimum <= 0):
            raise EvaluationFailure("unsupported", "completion-input-not-positive")

    def _finite_monomial(self, node: Expr) -> tuple[Fraction, Fraction] | None:
        if node.get("op") != "finite":
            return None
        combined: dict[Fraction, Fraction] = {}
        for term in node["terms"]:
            weight = parse_fraction(term["weight"])
            coefficient = parse_fraction(term["coefficient"])
            combined[weight] = combined.get(weight, Fraction(0)) + coefficient
        nonzero = [(weight, coefficient) for weight, coefficient in combined.items() if coefficient]
        if len(nonzero) == 1 and nonzero[0][0] > 0:
            return nonzero[0]
        return None

    def _coefficient(self, node: Expr, weight: Fraction) -> ExpQCoefficient:
        cache_key = (id(node), weight)
        cached = self._coefficient_cache.get(cache_key)
        if cached is not None:
            return cached
        self.meter.visit(self._node_key(node), weight)
        op = node["op"]
        if op == "finite":
            total = Fraction(0)
            for term in node["terms"]:
                if parse_fraction(term["weight"]) == weight:
                    total += parse_fraction(term["coefficient"])
                    self.meter.bump_operation()
            result = ExpQCoefficient.rational(total)
        elif op == "add":
            result = ExpQCoefficient.zero()
            for argument in node["arguments"]:
                result = result + self._coefficient(argument, weight)
                self.meter.bump_operation()
        elif op == "scale":
            result = self._coefficient(node["argument"], weight).scale_rational(
                parse_fraction(node["coefficient"])
            )
            self.meter.bump_operation()
        elif op == "shift":
            result = self._coefficient(
                node["argument"], weight - parse_fraction(node["by"])
            )
        elif op == "multiply":
            result = self._product_coefficient(node["arguments"], weight)
        elif op == "exp":
            result = self._exp_coefficient(node["argument"], weight)
        elif op == "log1p":
            result = self._log1p_coefficient(node["argument"], weight)
        else:
            raise EvaluationFailure("unsupported", "unknown-expression-operation")
        self._coefficient_cache[cache_key] = result
        return result

    def _product_coefficient(
        self, arguments: Sequence[Expr], target: Fraction
    ) -> ExpQCoefficient:
        if len(arguments) == 1:
            return self._coefficient(arguments[0], target)
        first = arguments[0]
        rest = arguments[1:]
        first_min = self._minimum(first)
        rest_min = sum((self._minimum(argument) for argument in rest), Fraction(0))
        start = self._index(first_min)
        stop = self._index(target - rest_min)
        if stop < start:
            return ExpQCoefficient.zero()
        total = ExpQCoefficient.zero()
        for index in range(start, stop + 1):
            left_weight = self._weight(index)
            left = self._coefficient(first, left_weight)
            if left.is_zero:
                continue
            right = self._product_coefficient(rest, target - left_weight)
            total = total + left * right
            self.meter.bump_operation(2)
        return total

    def _exp_coefficient(self, argument: Expr, weight: Fraction) -> ExpQCoefficient:
        self._require_completion(argument, strict=False)
        index = self._index(weight)
        if index < 0:
            return ExpQCoefficient.zero()
        monomial = self._finite_monomial(argument)
        if monomial is not None:
            mono_weight, coefficient = monomial
            mono_index = self._index(mono_weight)
            if index % mono_index:
                return ExpQCoefficient.zero()
            exponent = index // mono_index
            self.meter.bump_operation()
            return ExpQCoefficient.rational(coefficient**exponent / factorial(exponent))
        constant = self._coefficient(argument, Fraction(0))
        if not constant.is_rational:
            raise EvaluationFailure("unsupported", "non-rational-exp-constant")
        if index == 0:
            return ExpQCoefficient.exp_atom(constant.rational_value())
        total = ExpQCoefficient.zero()
        for k in range(1, index + 1):
            source = self._coefficient(argument, self._weight(k))
            if source.is_zero:
                continue
            prior = self._coefficient_for_exp(argument, index - k)
            total = total + source.scale_rational(k) * prior
            self.meter.bump_operation(3)
        return total.divide_rational(index)

    def _coefficient_for_exp(self, argument: Expr, index: int) -> ExpQCoefficient:
        key = (id(argument), "exp", index)
        cached = getattr(self, "_exp_cache", {}).get(key)
        if cached is not None:
            return cached
        if not hasattr(self, "_exp_cache"):
            self._exp_cache: dict[tuple[object, ...], ExpQCoefficient] = {}
        result = self._exp_coefficient(argument, self._weight(index))
        self._exp_cache[key] = result
        return result

    def _log1p_coefficient(self, argument: Expr, weight: Fraction) -> ExpQCoefficient:
        self._require_completion(argument, strict=True)
        index = self._index(weight)
        if index <= 0:
            return ExpQCoefficient.zero()
        monomial = self._finite_monomial(argument)
        if monomial is not None:
            mono_weight, coefficient = monomial
            mono_index = self._index(mono_weight)
            if index % mono_index:
                return ExpQCoefficient.zero()
            exponent = index // mono_index
            sign = Fraction(1 if exponent % 2 else -1)
            self.meter.bump_operation()
            return ExpQCoefficient.rational(sign * coefficient**exponent / exponent)
        total = self._coefficient(argument, weight).scale_rational(index)
        for k in range(1, index):
            source = self._coefficient(argument, self._weight(index - k))
            if source.is_zero:
                continue
            prior = self._coefficient_for_log1p(argument, k)
            total = total - prior.scale_rational(k) * source
            self.meter.bump_operation(3)
        return total.divide_rational(index)

    def _coefficient_for_log1p(self, argument: Expr, index: int) -> ExpQCoefficient:
        key = (id(argument), "log1p", index)
        cached = getattr(self, "_log_cache", {}).get(key)
        if cached is not None:
            return cached
        if not hasattr(self, "_log_cache"):
            self._log_cache: dict[tuple[object, ...], ExpQCoefficient] = {}
        result = self._log1p_coefficient(argument, self._weight(index))
        self._log_cache[key] = result
        return result

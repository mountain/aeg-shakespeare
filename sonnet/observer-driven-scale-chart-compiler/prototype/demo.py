"""Two minimal, inspectable compiler demonstrations."""

import json

from scale_compiler import (
    Observer,
    Scale,
    Series,
    Var,
    balance_summary,
    compilation_summary,
    compile_expression,
    exp,
)
from scale_compiler.balance import infer_distinguished_scaling


def main() -> None:
    N = Var("N")
    bindings = {"N": Series.monomial(1)}
    observer = Observer(require_remainder_below=Scale(-3), max_taylor_order=16)
    report = compile_expression((1 + N ** -1) ** N, bindings, observer)
    print(json.dumps(compilation_summary(report), indent=2, sort_keys=True))

    t = Var("t")
    z = Var("z")
    airy = exp(-N * (t ** 3 / 3 - z * t))
    chart = infer_distinguished_scaling(
        airy,
        unknown_scales=("t", "z"),
        fixed_scales={"N": Scale(1)},
    )
    print(json.dumps(balance_summary(chart), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

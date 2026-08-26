# Phase 1：Riccati 射影机制校准结果

## 状态与边界

- **状态：** 完成 Phase 1 的精确机制校准。
- **证书：** `tests/research/test_am_conformal_chart_riccati.py`。
- **算术：** Python `Fraction`，无浮点误差、无外部依赖。
- **最高主张：** level-1 classical re-expression；没有 bounded discovery，
  没有 economy theorem，也没有联合标准型定理。

## 1. 阳性对照

对

$$
\dot a=c_0+c_1a+c_2a^2,
\qquad a=-x/y,
$$

精确证书验证

$$
\frac d{dt}\binom{x}{y}=
\begin{pmatrix}c_1/2&-c_0\\c_2&-c_1/2\end{pmatrix}
\binom{x}{y}
$$

确实给回原标量场。测试穷举 $4^3$ 组有理系数和五个有理 chart 点，
共 320 个标量—提升等式。

对三组非平凡 Möbius chart，证书把

$$
b=\frac{\alpha a+\beta}{\gamma a+\delta}
$$

提升为齐次坐标变换

$$
S=\begin{pmatrix}\alpha&-\beta\\-\gamma&\delta\end{pmatrix},
\qquad L_b=SLS^{-1},
$$

并逐点验证 chart 读出与矩阵动力学交换。分母为零的点不被偷偷跨过，
而是登记为 infinity-chart 边界。

## 2. Gauge 与 no-go

对多个有理 $\gamma$，证书验证

$$
L\mapsto L+\gamma I
$$

改变齐次 lift，却不改变 $a=-x/y$ 的动力学。这是表征 gauge，不是新的
物理自由度。

反向计算还给出一个精确邻近 no-go。任意常矩阵

$$
L=\begin{pmatrix}u&v\\w&z\end{pmatrix}
$$

在射影读出下只能产生

$$
\dot a=-v+(u-z)a+wa^2.
$$

所以一般非零三次项不可能来自同一个常系数二维线性提升。若要处理
三次标量场，必须改变维数、允许状态依赖矩阵、覆盖或其他结构，并把
新增成本单独登记。

## 3. 成本判决

八轴 `CostVector` 已能执行严格 Pareto 支配检查：

$$
(C_{coeff},C_{action},C_{singular},C_{atlas},C_{decoder},
C_{unit},C_{eval},C_{residual}).
$$

红队刻意构造“系数更短但 decoder/atlas 更贵”的候选，确认它不能仅凭
字符数胜出。经典二维 lift 本身也不支配直接标量求值。因此 Phase 1
证明的是 covariance mechanism，而非计算经济性。

## 4. Gate 1 判决

| Gate | 结果 | 说明 |
| --- | --- | --- |
| 1A exact lift | 通过 | 标量场与二维 lift 精确交换 |
| Möbius covariance | 通过 | chart 读出与矩阵共轭精确交换 |
| scalar gauge | 通过 | 射影动力学不变 |
| 1C cubic red team | 通过 | 非零三次项被正确拒绝 |
| joint cost accounting | 通过 | 八轴 Pareto，不按字符数评分 |
| 1B bounded discovery | **未执行** | 当前矩阵由经典推导给出，未由盲搜索恢复 |

因此 Phase 1 只能部分关闭：机制与 no-go 已完成，发现器仍开放。进入
单摆 Phase 2 之前，应先冻结一个不接触目标矩阵的低高度 chart/lift
grammar，检验它能否从 Riccati 系数恢复任务等价的稀疏二分量表示。

## 5. 对最新理论的关系

- 同层可逆 chart 保持 exact round-trip；
- 跨层遗忘使用 semantic adapter，不由本证书覆盖；
- task quotient 需要 continuation adequacy；
- chart 后 observer 是否有 coherent response，仍按 Phase 12C 的 C0--C4
  分级，不由坐标协变自动推出。

Mathematical Core、Engineering Architecture、Theory Map 与 Public API
均不因本阶段改变。证书保持 research-local。

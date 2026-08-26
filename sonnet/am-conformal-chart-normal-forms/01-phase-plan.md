# AM 共形 chart 与联合标准型：阶段计划

本文件把 [`00-problem-frontier.md`](00-problem-frontier.md) 的问题契约转成逐阶段闸门。后续阶段不得通过事后改变任务、grammar、oracle 或成本标尺来制造成功。

## Phase 0 — 冻结对象、等价性与成本

### 目标

建立第一个可执行但尚不搜索物理新结构的 contract。

### 必须冻结

- **任务：** 输入、输出、容许误差、物理时间或事件语义；
- **atlas：** chart 定义域、重叠区、奇点与标记点；
- **变换分类：** 共形 chart、Möbius、gauge、覆盖、时间重参数化、任务商分别登记；
- **候选 grammar：** 生成元、复合深度、系数高度、局部域和去重规则；
- **单位：** $(0,1,\infty)$ 标架与物理单位的运输规则；
- **模块：** polynomial-like 候选语法、matrix-like 基底与允许的 gauge；
- **成本：** 符号、作用、奇点、atlas、decoder、单位、求值与 residual 八轴；
- **oracle：** 哪些经典对象只可用于验证，哪些可作为公开基线输入。

### 首个证书

对每个候选 $\phi$ 自动验证：

$$
\phi^{-1}\circ\phi=\operatorname{id},
\qquad
\pi\circ\phi^{-1}\circ\phi=\pi
$$

于声明域成立，并记录导数、共形因子、单位像、奇点像与 chart 切换条件。

### Gate 0

只有当至少一个非平凡候选能通过 exact round-trip、读出、单位和作用运输证书，且成本可被稳定重算时，才进入 Phase 1。否则 Sonnet 停在定义审计。

## Phase 1 — Riccati/射影阳性对照与邻近 no-go

### 1A. 精确阳性对照

从

$$
a=-x/y,
\qquad
\dot a=c_0+c_1a+c_2a^2
$$

独立推导二维矩阵提升，并验证任意允许 Möbius chart 下的矩阵共轭/联络变换。显式检查 $L\mapsto L+\gamma I$ 的 scalar gauge 不改变射影读出。

### 1B. 发现测试

不给 proposal generator 目标矩阵；只提供 Riccati 系数、AM 原始作用、射影读出与被冻结 grammar。记录它能否在预算内恢复任务等价的稀疏二分量表示。

### 1C. 邻近红队

加入一般三次标量场，检验算法是否错误地声称同一二维线性提升。若只能通过增加维数、覆盖或非共形变换处理，必须明确登记。

### Gate 1

- exact symbolic 证书通过；
- 发现器与手给 oracle 严格隔离；
- Riccati 阳性和三次红队都得到正确分类；
- 报告的是 joint cost，而非矩阵条目数。

Phase 1 最高只允许 **level-1 re-expression**；若受限搜索自行恢复结构，可在冻结域内报告 bounded discovery，不外推。

## Phase 2 — 单摆的共形 atlas 与 period/module 联合搜索

### 2A. 保留第一性入口

从现有 Cartesian 单摆原始量、约束与任务读出开始，复核如何得到

$$
Y^2=2(E-U)(1-U^2),
\qquad
dt=dU/Y.
$$

该载体是 baseline，不是新 Sonnet 的发现结果。

### 2B. 冻结任务族

至少分开：

- 平衡点附近的小振幅任务；
- 普通有界振荡的周期/轨道求值；
- 旋转区；
- separatrix 邻域的长时钟与退化测试。

每一族单独声明能量域、精度、查询工作负载与容许 atlas 数。

### 2C. 原生 chart 搜索

proposal generator 只接收任务可见标记、AM grammar 与成本标尺。它搜索：

- 分支/标记点的低高度 Möbius 配置；
- 由 Addition/Multiplication 有限作用生成的局部 chart；
- chart 与有限 period/module 基底的共同选择；
- 必要的 atlas 切换策略。

Legendre 参数、交比的经典配对、$j$-不变量、周期比和命名椭圆函数先留在 oracle 侧。

### 2D. 精确校准与数值压力

- 在 $E=0$ 做 exact calibration，但不向 proposal generator 提供 $\tau=i$；
- 在普通能量区比较符号长度、作用稀疏性、decoder 和数值条件；
- 向平衡点与 separatrix 双向逼近，记录 chart 失效、周期退化和切换成本；
- 验证物理时间恢复，而不只验证几何轨道。

### Gate 2

进入下一阶段需同时满足：

1. chart、carrier、module、unit、clock 和 decoder 的 exact commuting certificates；
2. 至少一个预先冻结工作负载上出现严格 Pareto 改进；
3. 在退化区没有把失效域或 atlas 切换隐藏起来；
4. 发现结果可由独立经典 oracle 复核；
5. 明确指出不能被 chart 消去的模量/周期/monodromy 数据。

若只得到经典归一化的正确复述，阶段以 level-1 结论关闭。

## Phase 3 — PCR3BP 局部任务压力测试

### 3A. 选择而非混合任务

从下列任务中逐一立项，不能一次声称覆盖全部：

- 固定时间窗的状态传播；
- 声明截面上的 Poincaré 返回；
- 近某主星但避开碰撞的局部段；
- 含碰撞极限的正则化段。

每项冻结质量参数、Jacobi 常数区间、初值域、容差、终止条件与 baseline。

### 3B. 变换审计

候选管线必须把

1. 共形 chart；
2. 分歧覆盖；
3. 时间重参数化；
4. 变分方程/monodromy 的基底 gauge

作为四个不同开关分别消融。任何收益都按来源归因。

### 3C. 联合成本

比较局部 polynomial-like 系数描述与 matrix-like 变分/返回作用表，同时计入 atlas、事件定位、物理时间恢复、条件数和 residual。

与 [`../pcr3bp-history-cost/`](../pcr3bp-history-cost/) 只交换已证实的 task/cost 接口；不得借用其尚未通过 Phase 2 的 Bellman/Huffman 叙事。

### Gate 3

- 至少一个明确局部任务上，结果相对标准坐标/标准正则化有可重复的净改进；
- 独立积分与守恒量/返回 residual 检验通过；
- collision、branch 与 chart-boundary 失败模式被显式触发；
- 不出现全局可积性或唯一最优 chart 的越界结论。

负结果同样有效：它可以表明 AM 原生 chart grammar 未带来超越经典局部正规化的收益。

## Phase 4 — 抽象提取候选

只有 Phase 1–3 中至少两个独立问题迫使出同一接口，才可提出 research-local abstraction：

$$
\text{task}
\longrightarrow
(\text{conformal atlas},\text{carrier},\text{module},\text{decoder},\text{cost})
\longrightarrow
\text{certified Pareto frontier}.
$$

### Gate 4

- **Precision gate：** 定义、域、等价关系和失败条件无歧义；
- **Calibration gate：** 至少两个独立原型有 exact/numerical evidence；
- **Abstraction gate：** 抽象减少重复并预测新测试，不只是重新命名；
- **Foundation gate：** 可从 histories、tasks、lifts、quotients、observers 与 units 回译。

通过后也只能建立 extraction candidate，经 `experimental/` 成熟；禁止从 Sonnet 直接进入公共 API。

## 第一批建议产物

在 Phase 0/1 完成前，产物应保持很小：

- `chart_contract.py`：声明域、Möbius/局部共形候选、往返与单位运输；
- `riccati_projective_certificate.py`：精确二维提升、gauge 与三次红队；
- `cost_schema.py`：八轴成本和 Pareto 支配；
- 小型 exact tests：只含有理/符号样例，不启动昂贵搜索。

文件名仅为计划，不在本初始化提交中创建。

## 决策记录

| 决策 | 理由 | 重新开放条件 |
| --- | --- | --- |
| 先 Riccati，后单摆 | 先校准两过程量—一物理量与 chart/gauge 机制 | 精确原型暴露定义错误 |
| 单摆不从角变量开局 | 保持现有 Cartesian 第一性路线 | 明确任务证明角变量是原始观测 |
| PCR3BP 只作局部任务 | 避免由 chart 改良暗示全局可积性 | 出现经过证书支持的全局 atlas 方案 |
| 成本保持 Pareto 向量 | 不替工作负载臆造权重 | 用户/任务提供冻结权重 |
| 经典标准型置于 oracle 侧 | 防止答案泄露成“发现” | 某阶段明确改为基线复现实验 |
| 暂不更新 Theory Map/API | 当前仅有问题契约 | 通过 Gate 4 与治理流程 |

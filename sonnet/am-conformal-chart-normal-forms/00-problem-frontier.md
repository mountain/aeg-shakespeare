# AM 共形 chart 与联合标准型：问题前沿

## 当前状态

- **成熟度：** T0 初始化；问题契约与校准路线，尚无新定理。
- **作用域：** `sonnet/` 研究局部；不改变 Mathematical Core、Theory Map 或公共 API。
- **最高可负责主张：** 我们已经把“在固定共形类中选择低成本 chart”与“polynomial-like / matrix-like 联合标准型”写成可证伪的研究问题；尚未证明存在普遍最优 chart，也未证明单摆或 PCR3BP 的净计算成本一定下降。

## 1. 问题原生陈述

过程几何不是先把物理方程换一种记号，而是先选择承载过程的表征空间，再由读出把过程量投影为物理量。一个物理量通常可由两个过程量表示；例如在一个射影 chart 中

$$
a=-\frac{x}{y}.
$$

同一物理读出可在不同 chart 中具有不同表达。这里固定以下工作前提：

> 在声明的 AM 共形 atlas 的正则重叠区上，chart 转换是共形的；选择 chart 可以改变系数、稀疏性、奇点位置、基底和数值条件，但不能免费改变任务、拓扑、模量、单值化数据或物理单位。

核心问题是：给定一个物理任务、一个 AM 过程表征及其共形 atlas，是否存在一个可发现、可验证的 chart 与有限模块基底，使

1. **polynomial-like 部分**成为低复杂度的标量载体、系数或递推；
2. **matrix-like 部分**成为低复杂度的作用表、转移矩阵或周期基底；
3. 二者在同一变换律下闭合；
4. 物理读出、单位、时钟与全局恢复仍然严格正确；
5. 总符号—数值成本相对可信基线出现严格的 Pareto 改进。

这不是“任意换元能否美化公式”的问题，而是一个受约束的联合标准型与 presentation-search 问题。

## 2. 原始对象与任务语义

每个实例必须先冻结以下输入：

- 原始物理过程或历史语言，以及允许观测的任务；
- AM 过程空间 $P$、其复/共形结构 $J$，以及已声明的 Addition/Multiplication 作用；
- 物理读出 $\pi:P\to X$ 或任务读出 $\mathcal O$；
- 正则域、奇点集、边界、分支点和需要保留的标记点；
- 单位与有序射影标架，特别是 $(0,1,\infty)$ 中物理单位 $1$ 的运输；
- 基线 chart、基线求解器、精度、预算和工作负载。

一个候选 chart $\phi:U\to V$ 只有在声明域上满足共形可逆性，并且其提升动力学 $\widetilde F_\phi$ 与物理动力学 $F$ 满足

$$
\pi_*\widetilde F_\phi=F
$$

时，才是任务等价候选。离散过程则使用相应的交换图或逐步读出等式。chart 往返、读出、单位、时钟与分支选择都必须进入证书。

## 3. 必须分开的五类变换

本 Sonnet 不允许把下列操作统称为“换 chart”：

| 操作 | 允许的效果 | 必须另行记账的结构 |
| --- | --- | --- |
| 共形 chart 转换 | 在正则重叠区重写局部坐标 | atlas 切换、奇点、单位与 decoder |
| 射影/Möbius 变换 | 重排射影标架与有限标记点 | 交比、物理单位、无穷点 |
| 模块基底或 gauge 变换 | 共轭/重写 matrix-like 作用 | 基底恢复与条件数 |
| 分歧覆盖 | 单值化或碰撞正则化 | 覆盖次数、deck 数据、分支选择 |
| 时间重参数化 | 改变积分时钟 | 物理时间恢复与代价 |

任务商也不是 chart 转换：它可以忘掉历史信息，必须由任务等价性单独证明。

## 4. 联合标准型候选

一个候选由

$$
\mathfrak N=(\phi,\,\mathcal B,\,p,\,R,\,D)
$$

组成，其中 $\phi$ 是 chart，$\mathcal B$ 是有限模块基底，$p$ 是 polynomial-like 标量数据，$R$ 是 matrix-like 作用数据，$D$ 是物理 decoder。理想情况下，chart 转换与基底变换共同作用为

$$
p\mapsto p^{\phi},
\qquad
R\mapsto G^{-1}R^{\phi}G-G^{-1}\dot G,
$$

其中是否出现导数项取决于任务是代数作用、微分方程还是联络问题。公式只是候选变换契约；各阶段必须从具体原始过程重新推导，不能当作普遍定理。

### 4.1 Polynomial-like

暂指在所选 chart 中由有限生成、低次数或低递推复杂度描述的标量载体，包括 AM 函数论已有的指数—多项式 weight chain。它不等同于普通多项式，也不预设所有任务都能落入有限维链。

### 4.2 Matrix-like

暂指多个过程分量、局部基底或周期/monodromy 数据的有限作用表。它不仅记录加法可交换性所诱导的线性组合，还必须记录 chart、gauge、覆盖与 decoder 如何改变该表。

### 4.3 联合而非分别最简

只把 $p$ 的次数降到最低，可能使 $R$ 稠密、decoder 昂贵或 chart 数目增加；只把 $R$ 对角化，也可能引入分支函数、坏条件数或破坏物理单位。因此标准型使用成本向量而不是单一“最短公式”：

$$
C(\mathfrak N)=(
C_{\rm coeff},
C_{\rm action},
C_{\rm singular},
C_{\rm atlas},
C_{\rm decoder},
C_{\rm unit},
C_{\rm eval},
C_{\rm residual}
).
$$

除非工作负载给出权重，否则只报告 Pareto 前沿。

## 5. 搜索纪律

### 5.1 原生语言优先

先搜索由 Addition/Multiplication 原始作用、任务可见标记点和有限 chart grammar 生成的候选；随后才与不受限的经典变换搜索比较。不能先解出问题，再把经典答案包装成“发现”。

### 5.2 Oracle 防火墙

- Legendre 型、椭圆函数、周期比、Levi–Civita 或其他已知答案可作为后验 oracle 与基线；
- 除非当前阶段明确把它们列为输入，否则不得把其参数、分支点配对、周期基底或正则化映射直接喂给 proposal generator；
- 候选生成、评分、验证与 oracle 比较必须留有可审计边界。

### 5.3 有界 grammar

“所有共形映射”不可执行。Phase 0 必须冻结一个有限或可枚举 grammar，例如由 AM 有限作用、任务可见标记点、低高度 Möbius 变换和声明的局部 chart 复合而成。扩大 grammar 必须记为新的实验阶段，不能事后选择。

## 6. 第一校准：射影/Riccati 原型

若

$$
a=-\frac{x}{y},
\qquad
\dot a=c_0+c_1a+c_2a^2,
$$

则经典二维提升

$$
\frac{d}{dt}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}
c_1/2 & -c_0\\
c_2 & -c_1/2
\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
$$

在 $y\neq0$ 上给回同一 Riccati 方程；加上标量矩阵 $\gamma I$ 不改变射影读出。这一例只承担四项校准：

- 两个过程量如何读出一个物理量；
- polynomial-like 系数如何进入 matrix-like 作用；
- Möbius chart 与矩阵共轭如何配合；
- scalar gauge 为什么是表征冗余而非新物理。

它是标准理论的阳性对照，不构成 AM 新发现。三次标量场将作为邻近红队，防止从 Riccati 原型不当地推出“所有非线性都可二维线性化”。

## 7. 第二校准：单摆

单摆必须从现有第一性路线开始：Cartesian 原始量与物理约束先行，随后才形成任务载体。当前可比基线为

$$
Y^2=2(E-U)(1-U^2),
\qquad
dt=\frac{dU}{Y}.
$$

研究问题不是预先宣布 Legendre 化，而是检验：

1. 从任务可见的分支/标记数据出发，受限 grammar 能否发现低成本共形 chart；
2. chart 是否把 polynomial-like 载体与 period/module 基底同时简化；
3. 物理单位、时钟、分支与 decoder 的新增成本是否抵消表面简化；
4. $E=0$ 的方格周期情形能否作为精确校准，但不把 $\tau=i$ 泄露给发现器；
5. 平衡点、普通振荡、旋转与 separatrix 退化区是否需要不同 atlas，而非一个伪全局 chart。

交比、$j$-不变量、周期格与 monodromy 是不可被 chart 免费消去的候选剩余量；本 Sonnet 要通过证书确定它们在任务成本中的实际角色。

## 8. 第三校准：平面圆型限制性三体问题

PCR3BP 是独立压力测试，不是单摆结论的装饰性应用。每次实验先声明局部区域与任务，例如短时传播、Poincaré 返回或近碰撞段，再比较：

- 基线物理/旋转坐标；
- 纯共形 chart 变化；
- 必要时单独登记的分歧覆盖；
- 必要时单独登记的时间重参数化；
- polynomial-like 局部系数与 matrix-like 变分/monodromy 表的联合成本。

不能把碰撞正则化偷偷计作 Möbius chart 的收益，也不能由局部 chart 的改善推出全局可积性。现有 [`pcr3bp-history-cost/`](../pcr3bp-history-cost/) 作为相邻 Sonnet，继续独立记录 word、clock、deck 与 hyperbolic cost；两条研究线在有共同证书前不合并。

## 9. 可证伪假设

- **H1 — chart covariance：** 每个合格候选都有精确的读出、单位、时钟与往返证书。
- **H2 — 有效精简：** 至少一个非平凡任务上存在严格 Pareto 改进，而不只是字符数变短。
- **H3 — 联合标准型：** 标量载体与有限作用表需要共同选择，分别最简一般不等于联合最简。
- **H4 — 共形剩余：** 模量、交比、周期、monodromy 或标记单位形成不能由 chart 消去的任务相关残差。
- **H5 — 局部性边界：** PCR3BP 的最佳对象更可能是 task-local atlas，而不是单一全局标准 chart。

## 10. Kill conditions 与红队

出现任一情况必须缩小或关闭相应主张：

- 所谓简化只减少书写长度，却增加 decoder、atlas、分支或数值成本；
- 候选在任务域上不共形、不单射，或把覆盖/时间变换伪装成 chart；
- 把移动后的单位重新设为 $1$ 却不计额外归一化；
- 物理读出、时钟或 task-equivalence 交换图失败；
- 将奇点移出当前坐标纸后便不再追踪；
- proposal generator 接触到被冻结的经典答案；
- 优势仅来自普通 Möbius 归一化，AM 原生 grammar 没有额外贡献；
- 从局部改良不当地推出全局标准型、全局可积性或拓扑消失；
- 在匹配预算下，原生 AM 搜索始终弱于基线。负结果仍应保留。

## 11. 证书要求

每个阶段至少提交：

- chart 定义域、重叠区、Jacobian/共形性与往返证书；
- 过程作用的 pushforward/pullback 等式；
- 物理读出、单位、时钟、分支与 decoder 证书；
- polynomial-like 载体和 matrix-like 作用的变换证书；
- 对照基线、冻结预算、完整成本向量和 Pareto 比较；
- 奇点、退化区、坏条件数和跨 chart 切换红队；
- 发现输入日志与 oracle 防火墙审计。

## 12. 理论与工程影响边界

若校准成功，它可能细化 Mathematical Core 中的 presentation search、单位协变、观察者/decoder 与 effective analysis，也可能给 Engineering Architecture 增加共形 atlas 和联合模块成本的研究局部 schema。

当前不更新 Theory Map：本研究保持 T0/T1、横向且局部。只有在 Riccati、单摆和 PCR3BP 三层证据中至少两类独立问题迫使出同一接口，并通过精度、校准、抽象与基础闸门后，才允许提出 extraction candidate；任何公共 API 仍须经过 Experimental 层。

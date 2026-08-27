# Workstream A — 数学语义、下降障碍与尺度纤维

**对应追踪：** process-geometry [#140](https://github.com/mountain/process-geometry/issues/140) Workstream A  
**状态：** research-local S0/S1 数学结果；不主张理论或 API 晋级  
**日期：** 2026-08-27

## 0. 结论先行

这一线索形成了一个严格而很小的数学内核，但需要压低纯数学的新颖性主张。

1. **真正适合编译器的基础不是“surreal 算术”，而是任务观察的逆向拉回。** 给定当前商、后续算子和输出任务，后续任务在输入端诱导一个更细的等价关系；它是使任务下降的、信息意义下最小的精确修复。
2. **surreal 指数例子是一个锋利的非下降证书。** 对无限尺度 $Y$，有限观察把 $x=\exp(a/Y)$ 都看成 $1$，但后续乘方把它们精确分成 $e^a$。所需最小响应坐标是
   \[
   b_Y(x)=\operatorname{st}(Y\log x).
   \]
3. **$G_Y$ 只能称为临界响应窗。** 它不是 $\operatorname{st}(x^Y)$ 的完整定义域；窗外有饱和到 $0$ 和发散到无穷两种行为。
4. **尺度转换不是普通流形 atlas。** 缩小尺度会塌缩响应，可比尺度给出实数重标定，放大尺度会打开旧核中的新纤维；最后一种转换不能通过旧尺度商下降。
5. **上述纯数学主要是商因子分解、赋值论与非阿基米德指数域的直接推论。** 它不应被包装成 surreal 特有的新定理。潜在新增压力在于：把任务谓词的逆向拉回、最小修复、定义域、残差和成本组织成可执行的 chart/scale 编译过程，并在独立问题上得到净计算收益。

这与 #140 的 claim ceiling 一致：当前最多是 **T1 目标、Sonnet-local、精确符号 + 有界搜索**。

---

## 1. 原始数学契约

### 1.1 有界观察，而非必然有限集合

“有限观察者”容易混淆两件事：有限分辨能力与有限基数。这里用更保守的词 **有界观察**。

令 $H$ 为原始状态或历史集合。一个当前观察是满射

\[
q:H\twoheadrightarrow B.
\]

它诱导等价关系

\[
h\sim_q h'
\quad\Longleftrightarrow\quad
q(h)=q(h').
\]

纤维 $F_b=q^{-1}(b)$ 是当前观察遗忘的数据。$B$ 可以是有限集，也可以是实数、符号表达式或其他任务载体；只有在 $B$ 有限时，才能直接继承有限任务商的算法与位数下界。

若任务包含部分定义、分支失败或越界，必须先把状态总化到带标签的结果空间，例如

\[
R^{\bot}=R\sqcup
\{\text{outside-domain},\text{branch-failure},\text{inconclusive}\}.
\]

失败状态也是可见语义，不能在等价关系中静默删除。

### 1.2 后续任务与逆向可见性

令

\[
U:H\longrightarrow H'
\]

为一个后续算子，$q':H'\twoheadrightarrow B'$ 为输出任务商。输出任务在输入端诱导响应

\[
r_{U,q'}=q'\circ U:H\longrightarrow B'.
\]

若存在 $h,h'\in H$ 使

\[
q(h)=q(h'),
\qquad
q'(U(h))\ne q'(U(h')),
\]

则称 $(h,h')$ 为一个 **逆向可见性证书**：当前被遗忘的区别会被未来算子重新放大为任务可见区别。

这就是“未来运算迫使当前几何升级”的最小精确定义。

### 1.3 算子下降判据

**命题 1（精确下降）。** 存在唯一映射

\[
\bar U:B\longrightarrow B'
\]

使

\[
q'\circ U=\bar U\circ q
\]

当且仅当

\[
\ker q\subseteq\ker(q'\circ U),
\]

即 $q'\circ U$ 在每个 $q$-纤维上为常值。

**证明。** 若交换式成立，同一 $q$-纤维显然有相同输出。反之，令

\[
\bar U(b)=q'(U(h)),\qquad h\in q^{-1}(b).
\]

纤维常值保证良定义，满射性保证唯一。∎

这是 #124 中算子下降问题的集合论核心；若还要求代数、拓扑、测度或计算结构下降，需要分别增加同态、连续、可测或有效性条件。

### 1.4 任务意义下的信息最小修复

若下降失败，定义

\[
q^{\!*}_{U,q'}:H\longrightarrow
B^{\!*}:=\operatorname{im}(q,q'\circ U),
\qquad
h\longmapsto(q(h),q'(U(h))).
\]

于是

\[
\ker q^{\!*}_{U,q'}
=
\ker q\cap\ker(q'\circ U).
\]

第一投影恢复旧观察，第二投影使输出任务下降。

**命题 2（信息最小性）。** 若另一个修复 $s:H\to S$ 同时足以恢复 $q$ 和 $q'\circ U$，即存在 $a:S\to B$、$c:S\to B'$ 使

\[
q=a\circ s,
\qquad
q'\circ U=c\circ s,
\]

则存在唯一映射

\[
\theta:\operatorname{im}s\longrightarrow B^{\!*}
\]

使 $q^{\!*}_{U,q'}=\theta\circ s$。

因此 $q^{\!*}_{U,q'}$ 是所有精确充分修复中 **等价关系最粗、所含信息最少** 的一个。

这里的“最小”只指信息预序，不指：

- 最短编码；
- 最少内存；
- 最低编译成本；
- 最快求值；
- 最简单坐标。

实现仍需在同一最小任务商的不同 presentation 之间做多轴成本比较。

对任务族 (\mathcal T=\{t_i:H\to R_i\}_{i\in I})，相同构造给出

\[
\ker q^{\!*}_{\mathcal T}
=
\ker q\cap\bigcap_{i\in I}\ker t_i.
\]

若 $I$ 或任务结果不可有效表示，这个信息论构造可以存在而没有可行软件实现。

### 1.5 谓词形式与编译器的逆向律

令 $\operatorname{Obs}(B')$ 是输出任务允许的谓词/观察代数。算子 $U$ 诱导逆像

\[
U^*:P\longmapsto P\circ U.
\]

当前商 $q$ 足够，当且仅当每个输出谓词的逆像都在输入上按 $q$-纤维常值。若使用全体集合谓词，这等价于命题 1；若使用受限观察代数，则得到更弱、任务专属的下降条件。

对复合 $H\xrightarrow{U}H'\xrightarrow{V}H''$，有严格反变律

\[
(V\circ U)^*=U^*\circ V^*.
\]

等价关系的写法是：给定输出要求 $E_{\rm out}$，输入要求为

\[
U^*E_{\rm out}
=
\{(h,h'):U(h)\,E_{\rm out}\,U(h')\}.
\]

若输入还必须保留既有观察 $E_q=\ker q$，则

\[
E_{\rm in}=E_q\cap U^*E_{\rm out}.
\]

在表达式 DAG 的分叉处，对所有下游分支取交。这个“拉回 + 交”的律，才是第一版 backward observer compiler 最干净的数学核心。它也是 Phase 11“正向状态 / 反向谓词”律在尺度表达式上的直接延伸。

**重要边界：** 若用数值容差定义 $d(x,y)\le\varepsilon$，该关系一般不满足传递性，不能直接当作商。近似模式必须使用明确的 uniformity、覆盖、区间证书或 task-relative adapter；不得把容差球静默升级为等价类。

---

## 2. 非阿基米德指数域中的临界响应定理

### 2.1 集合论安全的工作域

先不直接在真类 $\mathbf{No}$ 上谈群商。令 $F$ 为一个集合大小的有序非阿基米德指数域，含有实数截面 $\mathbb R$，并满足：

1. 指数是有序群同构
   \[
   \exp:(F,+)\overset\sim\longrightarrow(F_{>0},\cdot),
   \qquad \log=\exp^{-1};
   \]
2. 有限元构成凸赋值环
   \[
   \mathcal O=\{x\in F:\exists n\in\mathbb N,\ |x|\le n\};
   \]
3. 无穷小构成极大理想
   \[
   \mathfrak m=\{x\in F:\forall n\ge1,\ |x|<1/n\};
   \]
4. 剩余域通过标准部
   \[
   \operatorname{st}:\mathcal O\twoheadrightarrow\mathbb R,
   \qquad\ker(\operatorname{st})=\mathfrak m
   \]
   与 $\mathbb R$ 识别；
5. 指数与剩余结构相容：
   \[
   \exp(\mathfrak m)\subseteq1+\mathfrak m,
   \qquad
   \operatorname{st}(\exp s)
   =e^{\operatorname{st}(s)}
   \quad(s\in\mathcal O).
   \]

这些条件在 surreal 的 Gonshor 指数下成立；无穷小处的指数、对数由通常幂级数给出。若要严格实例化 surreal，可在 NBG 类理论中工作，或选取包含给定 $Y$ 的、对 $\exp/\log$ 封闭的集合大小子域（例如合适的 $\mathrm{No}_\lambda$，其中 $\lambda$ 为足够大的 epsilon number）。软件运行时则应使用更小的有效 transseries/Hahn 片段。

### 2.2 临界响应窗、核与尺度坐标

固定正无限元 $Y\in F$，即 $Y>n$ 对所有自然数 $n$。定义

\[
G_Y
=
\{x\in1+\mathfrak m:Y\log x\in\mathcal O\},
\]

\[
b_Y:G_Y\longrightarrow\mathbb R,
\qquad
b_Y(x)=\operatorname{st}(Y\log x),
\]

以及

\[
K_Y=\ker b_Y
=
\{x\in G_Y:Y\log x\in\mathfrak m\}.
\]

术语上应称 $G_Y$ 为 **尺度 $Y$ 的临界响应窗**。它选取乘方输出既不饱和到零、也不发散到无穷的近单位扰动。

### 2.3 群与商定理

**定理 3（尺度响应商）。** (G_Y) 是 (1+\mathfrak m) 的乘法子群，(b_Y) 是满射群同态，并且

\[
G_Y/K_Y\cong(\mathbb R,+).
\]

**证明。** (1+\mathfrak m) 在乘法和求逆下封闭。由指数群同构，

\[
\log(xz)=\log x+\log z,
\qquad
\log(x^{-1})=-\log x.
\]

故 (Y\log x,Y\log z\in\mathcal O) 推出 (xz,x^{-1}\in G_Y)，并且

\[
b_Y(xz)=b_Y(x)+b_Y(z).
\]

对任意 (a\in\mathbb R)，令

\[
x_a=\exp(a/Y).
\]

因 (a/Y\in\mathfrak m)，有 (x_a\in1+\mathfrak m)，且

\[
Y\log x_a=a,
\qquad b_Y(x_a)=a.
\]

所以 (b_Y) 满射。第一同构定理给出结论。∎

### 2.4 乘方可见性与最小修复

对 (x>0) 定义

\[
x^Y:=\exp(Y\log x).
\]

**定理 4（临界窗内的输出定律）。** 对所有 (x\in G_Y)，

\[
\operatorname{st}(x^Y)
=
\exp_{\mathbb R}(b_Y(x)).
\]

并且对 (x,z\in G_Y)，以下条件等价：

\[
\operatorname{st}(x^Y)=\operatorname{st}(z^Y),
\]

\[
b_Y(x)=b_Y(z),
\]

\[
xz^{-1}\in K_Y.
\]

**证明。** 写 (s=Y\log x\in\mathcal O)。由指数与标准部相容，

\[
\operatorname{st}(x^Y)
=\operatorname{st}(\exp s)
=e^{\operatorname{st}(s)}
=e^{b_Y(x)}.
\]

实指数是单射，故输出相等当且仅当 (b_Y) 相等；同态核判据给出第三个等价条件。∎

因此，若当前观察是 (q_0(x)=\operatorname{st}(x))，那么 (q_0\equiv1) 于 (G_Y)，无法下降乘方任务；而 (b_Y) 恰好是任务

\[
x\longmapsto\operatorname{st}(x^Y)
\]

的最小精确修复，因为输出 (e^{b_Y(x)}) 与 (b_Y(x)) 携带同一等价关系。

最短的非下降证书是

\[
x_a=\exp(a/Y),
\qquad
\operatorname{st}(x_a)=1,
\qquad
x_a^Y=e^a.
\]

这比 $(1+1/Y)^Y$ 的渐近说法更干净：它是指数域中的精确等式。

### 2.5 窗外的饱和与发散

令 (x\in1+\mathfrak m)，(s=Y\log x)。三种情形必须分别返回：

1. (s\in\mathcal O)：(x\in G_Y)，输出落在有限非零实响应窗，定理 4 适用；
2. (s) 为正无限：(x^Y=\exp s) 为正无限，实标准部任务越界；
3. (s) 为负无限：(x^Y=\exp s) 为正无穷小，标准部饱和为 (0)。

因此编译器必须逆向传播 **定义域和饱和状态**，不能只传播阶。若输出任务允许扩展值 $[0,+\infty]$，需要另建带饱和标签的商，不能把它与临界窗 $G_Y/K_Y$ 混为一谈。

---

## 3. 尺度转换三分律

固定两个正无限尺度 $Y,Z$，令

\[
\lambda=Z/Y>0.
\]

### 定理 5（尺度转换三分律）

#### A. 降低敏感度：(\lambda\in\mathfrak m)

有

\[
G_Y\subseteq G_Z,
\qquad
G_Y\subseteq K_Z,
\qquad
b_Z|_{G_Y}=0.
\]

证明：若 (s=Y\log x\in\mathcal O)，则

\[
Z\log x=\lambda s\in\mathfrak m.
\]

也就是说，$Y$-尺度可见的有限响应在较低敏感度 $Z$ 下全部塌缩。

#### B. 可比尺度：(\lambda\in\mathcal O\setminus\mathfrak m)

令 (c=\operatorname{st}(\lambda)>0)。则

\[
G_Y=G_Z,
\qquad
K_Y=K_Z,
\qquad
b_Z=c\,b_Y.
\]

证明：$\lambda$ 与 $1/\lambda$ 均有限，所以 $Y\log x$ 有限当且仅当 $Z\log x$ 有限；标准部乘法给出比例律。

此时两个尺度商由实线性重标定 (a\mapsto ca) 同构。

#### C. 提高敏感度：(\lambda) 为正无限

有

\[
G_Z\subseteq K_Y.
\]

但 (b_Z:G_Z\to\mathbb R) 仍满射：对任意 (a\in\mathbb R)，

\[
x_a=\exp(a/Z)
\]

满足

\[
b_Y(x_a)=0,
\qquad
b_Z(x_a)=a.
\]

所以不存在映射 (\phi:\mathbb R\to\mathbb R) 使

\[
b_Z=\phi\circ b_Y
\quad\text{于 }G_Z.
\]

较高敏感度不是旧尺度坐标上的函数；它打开了旧核 (K_Y) 内部的一整条新响应纤维。

### 3.1 几何含义的负责表述

这个三分律支持如下有限陈述：

- 尺度变换可以是塌缩；
- 可以是可逆重标定；
- 也可以要求打开旧商的核。

它**不**支持在当前阶段宣称已建立“流形之后的普遍几何”。这些尺度窗的变化包含单射、商塌缩和不下降，显然不全是固定维数、局部可逆的流形 chart 转换。当前最多得到一个精确的尺度索引纤维模型和一个普通 atlas 的反例压力。

---

## 4. 与 #124、#125 和现有 Core 的接合

### 4.1 对 #124：算子下降与最小保留数据

本稿的命题 1、2 给出 #124 中最基础的一般答案：

\[
\text{下降}
\Longleftrightarrow
\text{输出任务在输入商纤维上常值},
\]

\[
\text{最小精确修复}
=
\text{旧观察与未来任务的联合像}.
\]

在指数例子中，旧商是标准部，未来任务是无限乘方后的标准部，修复坐标是 $b_Y$，修复纤维是 $K_Y$ 的陪集。

这并不解决 #124 的全部内容：组合相干、跨 presentation 的 intertwining、holonomy、有效压缩和成本仍是独立门。

### 4.2 对 #125：I3 尺度塔的正例与 I4/I5 的边界

三分律为 #125 的 I3 “filtered/refined change system”提供一个精确非阿基米德正例：尺度变细时会打开旧核中的响应。

但它没有自动给出：

- 加法切空间；
- jet 乘法或高阶链式法则；
- 一般导数与积分；
- 收敛或数值稳定；
- 有效 V5 analytic closure。

$b_Y$ 值域偶然是 $(\mathbb R,+)$，源于 $\log$、剩余域与所选任务；不能据此推断所有尺度纤维的第一层都自然线性化。

### 4.3 对对象化的边界

尺度响应纤维本身只是一个横向任务修复。要成为新的纵向算术 rank，仍需：

```text
稳定交互/响应接口
    -> 可复用 primitive
    -> 新的自由组合
    -> 所有组合的有效 lowering
```

目前没有这些证据。把 $b_Y$ 或 $K_Y$ 命名为新 rank 会违反现有 Core 的对象化门槛。

### 4.4 对 Effective Analysis Principle

这个内核只通过：

- E1：任务、定义域、保留/遗忘信息明确；
- E2 的一小部分：精确符号等式与非下降证书。

它还没有通过：

- 一般表达式语言的闭包或 controlled extension；
- 数值有效性；
- 相对基线的净计算经济；
- chart transport 下的完整 evaluator/error/cost 相容。

所以它只能成为编译器 S1 的语义证书，不能单独构成软件突破。

---

## 5. 新颖性审计

### 5.1 明确属于既有数学的部分

| 本稿结构 | 既有数学位置 | 结论 |
| --- | --- | --- |
| 商上算子下降 | 商映射、核关系、同余、coequalizer/factorization | 基础事实，不新 |
| 任务谓词逆向传播 | 逆像、最弱前置条件、数据流/抽象解释式逆向分析 | 原理不新 |
| $(\mathcal O,\mathfrak m,\operatorname{st})$ | 自然赋值环、剩余域、标准部 | 不新 |
| $G_Y/K_Y\cong\mathbb R$ | 指数群同构 + 剩余映射的第一同构定理 | 很可能是直接推论/folklore |
| $\exp(a/Y)^Y=e^a$ | 非阿基米德指数域中的精确缩放 | 不应主张新 |
| 尺度三分律 | 赋值可比性与剩余映射 | 直接推论 |
| log-exp/transseries 运行语义 | transseries、Hahn 场、Hardy field、surreal normal form | 已有深厚理论 |
| 自动渐近尺度 | Richardson、van der Hoeven 等 automatic asymptotics | 已有算法先例 |

关键一手边界：

- Mantova–Matusinski 的综述明确给出 surreal 的实剩余域、normal form，以及无穷小上的指数/对数幂级数：[arXiv:1608.03413](https://arxiv.org/abs/1608.03413)。
- Bournez–Guilmant 证明 $\mathrm{No}_\lambda$ 对 $\exp/\log$ 封闭当且仅当 $\lambda$ 是 epsilon number，并讨论集合大小、可计算性友好的子域：[arXiv:2201.08199](https://arxiv.org/abs/2201.08199)。
- Berarducci–Mantova 已把 surreal 与 transseries/Hardy 型导数连接起来，并证明相应 Liouville 闭性：[arXiv:1503.00315](https://arxiv.org/abs/1503.00315)。
- Berarducci–Mantova 还证明 transseries 可解释为正无限 surreal 上的函数，并指出一般 surreal 与 composition 的边界：[arXiv:1703.01995](https://arxiv.org/abs/1703.01995)。
- Bagayoko–van der Hoeven 把任意 surreal 描述为在 $\omega$ 处的 hyperseries 值，进一步说明 surreal 更像统一语义域，而不是天然的有限运行时：[arXiv:2310.14879](https://arxiv.org/abs/2310.14879)。
- Richardson 已有自动计算 exp-log 函数所需渐近尺度的算法先例；因此“自动找一个 scale”本身不是足够差异点：[论文条目](https://inria.hal.science/inria-00073832v1/document)。

### 5.2 可能形成 Process Geometry 新贡献的位置

潜在新增不应陈述为新数系或新赋值定理，而应是一个组合性、可执行的研究命题：

> 在冻结的表达式 DAG、输出任务、定义域、scale/chart grammar 与资源预算下，系统能否通过逆向拉回任务谓词，计算信息最小的尺度修复；再在该修复的多个 presentation 中自动选择一个带证书、失败语义与净成本优势的 chart？

它必须同时区别于：

1. 只做 forward leading-term truncation；
2. 由用户预先给 growth group 或 expansion variable；
3. 由名称规则硬编码 Airy/WKB 正规形；
4. 只求 dominant balance，不跟踪任务商、残差和 branch；
5. 只给正确变换，不核算编译与 decoder 成本。

只有这一组合在独立 held-out 任务上显示覆盖或成本优势，才可能形成真实的软件贡献。

### 5.3 surreal 的负责分类

当前最佳分类是：

```text
数学语义：有用，但非必要
运行时表示：当前可消去，且不宜实现完整 No
新增定理来源：目前没有证据表明 surreal 特有
未来价值：统一极端尺度、normal form 与更高超指数层级的比较语义
```

如果有限 log-exp/Hahn carrier 能完成所有冻结 workload，surreal 只应作为语义解释和远期压力保留。只有当一个任务需要普通 transseries 片段无法统一表达、而 surreal/hyperseries 结构带来新定理、证书或可达任务时，才重新评估“必要”。

---

## 6. 编译器必须保持的数学不变量

1. **任务充分性**  
   编译后等价关系必须包含在所有声明输出任务的核中；任何被合并的输入在声明任务上结果相同。

2. **定义域/失败守恒**  
   log 正性、分母非零、分支、饱和、越界和 inconclusive 状态不能被 chart 或后端静默消除。

3. **反变组合律**  
   对复合 DAG，逆向义务满足 ((V\circ U)^*=U^*V^*)；分支要求取交。

4. **最小修复边界**  
   输出必须区分“信息最小商”与“所选低成本编码”；不可由前者推出后者。

5. **任务单调性**  
   增加输出任务或收紧精度时，所需等价关系只能变细，不能变粗。

6. **尺度转换相容**  
   可比尺度按剩余实数比例运输；尺度塌缩和打开旧核必须返回不同的 typed transition，而非伪装成可逆 chart。

7. **chart 协变/多解性**  
   合法重参数化若给出多个不可比 adequate chart，应返回 Pareto 集或歧义状态；不能依赖枚举顺序任取一个“canonical”答案。

8. **残差可重放**  
   cancellation、tie、branch、单位与舍弃尺度都要保留足以重放证书的 provenance。

9. **精确/近似分离**  
   精确等价、渐近阶、区间包围和浮点接近必须有不同 claim mode。

10. **lowering/round trip**  
    变换后表达式及其 decoder 在声明任务上与原表达式交换，或给出显式误差界。

11. **后端独立语义**  
    SymPy 等可以生成证书，但等价与成功由可重放方程、约束和残差定义，而不是由一次 simplify 的返回值定义。

12. **成本守恒**  
    编译、搜索、表达式增长、精度增长、存储、残差、branch、decoder 与重复求值分别记账。

---

## 7. Kill conditions 与边界

除 #140 已列条件外，Workstream A 建议冻结以下数学 kill conditions：

1. 把 $G_Y$ 误称为乘方标准部的全域，遗漏 $0/\infty$ 饱和区；
2. 直接在真类 $\mathbf{No}$ 上做未声明集合论的商或算法复杂度论证；
3. 将“信息最小”偷换为“计算最省”；
4. 将数值容差关系当成可商的等价关系；
5. 将 $b_Y$ 值域的加法性推广为任意过程尺度纤维都线性；
6. 把尺度三分律称为一个普通可逆 atlas；
7. 只保留量级而丢失符号/系数，导致 cancellation 与 competing balance 误判；
8. 在复数、负底数或多值 log/power 中不显式保留 branch；
9. 多参数尺度只有偏序，却被强行压成一条全序；
10. 运行时 carrier 为通过测试而存下完整原表达式或目标答案；
11. 现有 automatic asymptotics 从相同输入得到相同 chart 与不弱证书，而本系统无额外任务/残差/成本能力；
12. held-out 问题需要看答案后扩 grammar；
13. 任何“surreal 必要性”只改变术语，不改变可证命题、算法、证书或可达 workload。

### 可推广边界

- **直接推广：** 任何满足本稿指数-剩余相容条件的非阿基米德指数域；剩余域也可从 $\mathbb R$ 换成一般 $k$。
- **需扩展 carrier：** 多参数偏序尺度、带 cancellation 的向量值 leading data、分段定义、branch cut、Stokes 扇区、resurgence。
- **不自动推广：** 复指数域、振荡相位、非交换过程、随机尺度、PDE、临界现象和 3D Ising 的核心复杂度。
- **更高超运算：** Phase 12C 已有明确反例：二元 exponentiation 非结合，不能直接充当相同形状的 change monoid。需要一元作用、定边迭代、operad 或其他有类型组合。

---

## 8. 对 S0/S1 的可交付接口

### 8.1 Workstream B 可直接实现的最小记录

```text
ObserverRequirement
  domain predicate
  exact output equivalence / declared task predicates
  requested asymptotic band or exact mode

BackwardObligation
  pulled-back domain
  pulled-back equivalence/predicate family
  equality / dominance / balance constraints
  branch / cancellation residuals

RepairCertificate
  old observer q
  downstream task t
  repaired map q_star
  proof that ker(q_star) = ker(q) ∩ ker(t)
  non-descent witness when q alone fails

ScaleTransitionCertificate
  Y, Z, relation of Z/Y
  group-window inclusion
  kernel inclusion or real rescaling
  witness if finer response does not descend
```

命名应保持研究局部，不建议当前使用 `Surreal`、`Jet`、`Calculus`、`CanonicalCompiler` 等泛化名。

### 8.2 Airy 校准与本数学内核的关系

Airy 指数

\[
S_N(t,z)=N\left(\frac{t^3}{3}-zt\right)
\]

的 $a=1/3,b=2/3$ 平衡，是 scale constraint solver 的正控制；它本身不使用定理 3–5 的 surreal 指数窗。

两者真正共享的是：

- 输出任务决定哪些项必须同时可见；
- 后续指数会把指数中的 $O(1)$ 差别变成乘法可见差别；
- 因而需要从输出指数任务逆向保留输入尺度；
- chart 由 balance constraint 解出，而非由 forward truncation 或名字规则给出。

所以 surreal 例子应作为 **非下降/放大单元证书**，Airy 作为 **chart discovery 集成证书**；不要声称 Airy scaling 是由 surreal 数所独有地推出。

---

## 9. Core / Programme / Status / Architecture / Map / Governance 影响

### Mathematical Core

**当前：unchanged。** 复用 §1.1 task equivalence、§1.5 filtered fibres、前向状态/反向谓词、保留 residual 与对象化边界。若 S1/S2 成功，可提出一个研究记录：一般 exact task repair 的 kernel-intersection 定理及尺度实例；但它本身多为基础因子分解，不足以单独改变 Core。

### Research Programme

**压力：U1、U2、E。**

- U1：能否从任务自动生成充分 presentation；
- U2：能否得到可执行的尺度/表达式分析；
- E：chart covariance 与全成本经济。

**未获得：** Arithmetic Universality、surreal 必要性、新 arithmetic rank。

### Research Status

**创建时 unchanged。** S0/S1 若完成，应只记录为新的 Sonnet-local 精确语义与 Airy 发现证书；只有第二独立正例、负例、held-out 和基线/成本审计完成后，才考虑更新 repository-wide verdict。

### Engineering Architecture

**研究局部连接。** 对应 candidate generation、task adequacy、exact symbolic certificate、typed failure、Pareto cost 和 benchmark corpus。不得创建通用 `solve()`；SymPy 是可替换证书生成后端。

### Theory Map

**T1 目标，当前无晋级。** 压力位于 H1（task quotient）、H4（analysis）、task-covariant evaluation transversal、filtered fibres，以及 #125 的 I3–I5 seam。尺度纤维仍是横向任务修复，不是 V2 objectification。

### Theory Governance

“最小”限定为 kernel refinement 的信息预序；“精确”限定为声明指数域与临界窗；“自动”限定为冻结 grammar 与无 oracle 的 bounded search；“surreal”限定为比较语义。至少两个独立正例和一个负例前不应超过 T1/local。

### Software Governance / API

**无 Public/Experimental 压力。** 第一实现留在 Sonnet；通过独立任务后最多形成 extraction candidate。完整 surreal、通用 scale fibre、Jet、Calculus 或 CanonicalCompiler 都不应进入 API。

---

## 10. 简短复盘

- **是否支持最初直觉：** 支持一个严格的局部版本——更高敏感度的运算确实会打开旧观察商的核，迫使保留尺度纤维；但这还不是一般“几何超越流形”定理。
- **真正关键点：** 不是 (\mathbf{No}) 本身，而是输出任务对输入谓词/等价关系的反向拉回，以及由此得到的信息最小修复。
- **软件判据：** 若该律只能重述 dominant balance，价值有限；若它能在冻结 grammar 中自动发现 chart，同时正确保留 cancellation、branch、定义域和 residual，并在 held-out 上优于相同信息的基线，才形成可见推进。
- **下一步：** Workstream B 应先实现 `kernel intersection / pulled-back obligation / typed domain` 三件事；surreal 只做精确放大证书，Airy 做无 oracle 的 chart discovery，二者不要混为同一个新定理。

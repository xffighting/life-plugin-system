<div align="center">

# Life Plugin System · 人生外挂系统

**给你的人生,装一个能被 AI 操作的操作系统。**

*An AI-agent-native operating system for the one life you get.*

[快速开始](#5-分钟开始) · [架构](docs/architecture.md) · [路线图](ROADMAP.md) · [贡献](governance/CONTRIBUTING.md) · `MIT`

</div>

---

> 大多数工具帮你**记录**人生。这一套,帮你**运行**人生——并且让 AI 真正参与运行。

你不缺又一个笔记软件。你缺的是一个**内核**:一个能把每天的事实、判断、关系与产出,持续编译成"更好的下一步"的系统;一个结构清晰到连 AI Agent 都能安全读写、长期维护的系统。

这,就是 Life Plugin System。

---

## 一、不是模板包,是一套有内核的系统

普通的人生模板三个月就乱成垃圾场,因为它没有**治理**。这套系统从地基起就是一套工程:

```
            ┌──────────────────────────────┐
            │   内核 · 一部可修订的宪法      │  ← 人生最高判据，冲突时在此裁决
            └──────────────────────────────┘
                          │
   输入  ──▶  处理  ──▶  沉淀  ──▶  产出  ──▶  反馈
  (事实)     (目标)     (知识)     (项目)     (复盘)
                          │
   ── 脊柱：八经纬域 · 概念字典 · 数据账册 · AI 协同 ──
```

- **五层数据流**:信息进来不会乱跑,沿 `输入 → 处理 → 沉淀 → 产出 → 反馈` 一条流水线变成行动,再被复盘校准。
- **一根脊柱贯穿全层**:八条人生经纬 + 概念治理字典 + 结构化数据账册 + AI 协同层,像总线一样连接每一层。
- **三权分立**:目标牵引方向、项目驱动推进、复盘校准航线——三者不可混用,混用即"违宪"。
- **自带免疫系统**:概念字典消灭模糊词,入网七步约束每一份新内容,健康度指标(孤立节点 < 5%、目标-项目连接率 100%)定期体检。**它越用越清晰,而不是越用越乱。**

> 详见 [docs/architecture.md](docs/architecture.md) —— 这是整套系统最值得一读的部分。

## 二、它把"时间"锻造成"会复利的资产"

财富是资产,不是工资。人生也是。所以系统把这套思考**写进了数据结构**——每个目标都强制携带四个字段:

| 字段 | 它逼你回答的问题 |
|---|---|
| `leverage` | 这件事靠哪种杠杆?(判断 > 媒体/代码 > 资本 > 劳力) |
| `asset_type` | 它在攒什么复利资产?(受众/专长/系统/股权/关系) |
| `compounding` | 一次投入,是否持续产出? |
| `passive_income` | 你睡着时,它还在为你工作吗? |

于是每次记录,系统都在追问那个最贵的问题:**"有没有更高杠杆的方式,做同一件事?"**

## 三、为 AI Agent 而生,不是事后插一个聊天框

别的"AI 笔记"是给软件硬塞一个对话框。这套系统从设计起就是 **agent-native**——它有协议、有契约、有闸门,让 Agent 能**安全地读、写、维护**你的整个人生图谱:

- **入网七步协议**:任何新内容必须 判型 → 命名 → 建卡 → 连接 → 登记 → 归位。这不是给人看的规范,是**给 Agent 执行的状态机**。见 [skills/content-intake.md](skills/content-intake.md)。
- **双轨制(Markdown ↔ CSV)**:人读 Markdown,机器读注册表;同一份事实两种载体,Agent 索引零歧义。
- **脱敏硬闸**:[automations/deid_gate.py](automations/deid_gate.py) 是发布前的硬闸,邮箱/电话/金额/凭证命中即拦(退出码 1)。Agent 产出对外前必须过闸。
- **即用 Prompts 与 Skills**:`prompts/` 拿来即用,`skills/` 自带 输入/输出/步骤/质量检查,可直接对接 Claude Code、Agent SDK。

协同纪律写进了宪法:**只读优先 · 建议先行 · 隐私拦截 · 痕迹留存**。AI 是协作者,不是裁判,最终决策权永远在你手里。

## 四、隐私,默认留在本地

五级隐私(`public / internal / private / sensitive / secret`)+ 白名单导出 + fail-closed 默认:**真实人生数据永远留在你本地,公开的只有方法与模板。** 这是 Agent 时代该有的默认姿态。详见 [governance/SECURITY.md](governance/SECURITY.md)。

## 5 分钟开始

1. 安装 [Obsidian](https://obsidian.md)(免费)。
2. 把 `obsidian/sample-vault/` 作为一个 Vault 打开。
3. 读 `START_HERE.md`,跟着走。
4. 拷一份 `templates/goal.md`,建你的第一个目标(认真填那四个杠杆字段)。
5. 把 `prompts/daily-review.md` 交给你的 AI,开始第一次复盘。

## 目录结构

```
docs/          架构与设计思想（先读这里）
templates/     空白模板（含杠杆/复利字段）
prompts/       即用提示词（每日复盘、内容复用）
skills/        AI Agent 技能（含入网七步协议）
automations/   低风险脚本（发布前脱敏硬闸）
obsidian/      虚构示例 Vault（5 分钟跑起来）
governance/    贡献规范、安全与隐私
ROADMAP.md     路线图（build-in-public）
```

## 它属于谁

属于把人生当作一项**长期工程**来经营的人,属于想让 AI 真正接管重复决策的建造者。
如果你只想要一个待办清单,这套对你太重了——这是外挂,不是魔法。

---

<div align="center">

⭐ Star 追踪更新 · 🍴 Fork 你自己的 stack · 🛠 [提交你的模块](governance/CONTRIBUTING.md) · ☕ Sponsor 让它长得更快

**MIT** · 随便用、改、商用,保留署名即可,风险自负。
本项目提供方法与模板,不构成任何医疗、法律、财务或投资建议。

</div>

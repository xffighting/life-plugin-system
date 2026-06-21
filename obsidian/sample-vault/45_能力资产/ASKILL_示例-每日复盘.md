---
id: ASKILL-示例-每日复盘
type: agent_skill
status: active
created: 2026-01-12
updated: 2026-02-10
domain: 复盘
parent: 45_能力资产/03_AI_Agent_Skills
related: [[[REVIEW_示例-周复盘]]]
privacy: public
next_action: 把它接进你 AI 助手的每日定时任务
---

# 每日复盘(示例 AI Agent Skill)

> 演示"AI Agent Skill":有输入/输出/步骤/质量检查,可被 Agent 调用。
> 可执行提示词见仓库 `prompts/daily-review.md`。

## 输入
- 今天的关键事实(3–5 条)、情绪状态、推进的目标/项目、卡住的事。

## 输出
- 事实摘要 / 判断更新 / 杠杆检查 / 明日 1 件事 / 一句话收尾。

## 步骤
1. 读输入,浓缩成 3 条最重要事实。→ verify:只留事实,不带评价。
2. 给出判断更新,区分"事实"与"解读"。
3. 做杠杆检查:今天花时间最多的事靠哪种杠杆?有无更高杠杆做法。
4. 给出明日最有复利的 1 件事。

## 质量检查
- 不说安慰式套话;若在用劳力硬扛可自动化的事,直接指出。

## 类型边界
- 这是 AI Agent Skill(有输入/输出/步骤/质检);"每天复盘"这件事本身是"实践活动",两者分开记。

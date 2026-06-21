---
id: PROJECT-<语义化短名>
type: project
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
domain: <所属经纬域>
serves_goal: <GOAL-... 必填，无目标的项目不开>
goals: []
projects: []
people: []
organizations: []
human_capabilities: []
practices: []
agent_skills: []
tool_capabilities: []
sops: []
sources: []
agents: []
tools: []
channels: []
metrics: []
evidence: []
review_cycle: weekly
tags: []
parent: 20_行事务
related: []
next_action: <下一步,不可留空>
privacy: private
---

# <项目名:为某目标服务的一组持续行动>

## 模板用途
记录为目标服务的一组持续行动。

## 专属字段
- 服务目标:
- 项目边界:
- 里程碑:
- 风险:
- 交付物:

## 正文说明
- 背景:
- 当前状态:
- 判断依据:
- 可验证结果:

## 图谱连接
- 目标 / 项目 / 人物 / 组织 / 能力 / 实践 / AI Agent Skill / 信息源 / 证据 / 复盘

## 下一步动作
- 下一步:
- 截止或复盘时间:
- 需要谁或什么资源:

## 常见误区提醒
- 不要创建没有目标牵引的项目;无目标的项目最多停留 7 天。

## 入账提醒
创建正式 `project` 节点后,同步更新 project_registry;如为图谱正式节点,同步 graph_nodes.csv 与必要的 graph_edges.csv。

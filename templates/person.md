---
id: PERSON-<语义化短名>
type: person
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
domain: 人际关系
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
review_cycle: monthly
tags: []
parent: 35_人际经纬
related: []
next_action: <下次跟进动作>
privacy: private          # 真实人物默认 private 或 sensitive
# —— 人际维护字段（必填）——
relationship_layer: <家人/挚友/合作者/弱连接>
communication_preference: <沟通偏好>
risk_boundary: <风险边界>
next_followup: <YYYY-MM-DD>
---

# <人物名>

## 模板用途
记录人物节点,注意隐私和维护下一步。

## 专属字段
- 基础身份:
- 关系分层:
- 业务关联:
- 沟通偏好:
- 风险边界:
- 维护机制:

## 互动记录(脱敏摘要)
- <日期>:

## 图谱连接
- 目标 / 项目 / 人物 / 组织 / 能力 / 实践 / AI Agent Skill / 信息源 / 证据 / 复盘

## 下一步动作
- 下一步:
- 下次跟进时间:
- 需要谁或什么资源:

## 常见误区提醒
- 不要把微信、电话等渠道当成人物关系本身。

## 入账提醒
创建正式 `person` 节点后,同步更新 person_registry;如为图谱正式节点,同步 graph_nodes.csv 与必要的 graph_edges.csv。真实联系方式不入公开仓库。

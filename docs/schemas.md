# 数据 Schema 与双轨制

> 系统采用 **Markdown ↔ CSV 双轨制**:人读 Markdown 卡片(带双链),机器读 CSV 注册表(可索引、可被脚本/Dashboard/AI 调用)。同一份事实,两种载体,入网时同步。

## 为什么要两套

- Markdown 卡片:有叙事、有上下文、有双链,适合人思考。
- CSV 注册表:结构化、可查询,适合机器和 AI 跑统计、查孤立节点、做脱敏。

## 核心注册表

| 文件 | 作用 | 关键字段 |
|---|---|---|
| `graph_nodes.csv` | 所有节点的索引 | id, type, title, domain, status, privacy, parent, related |
| `graph_edges.csv` | 节点间的硬连接 | from, to, edge_type |
| `goal_registry.csv` | 目标专表 | id, metric, leverage, asset_type, compounding, passive_income |
| `*_registry.csv` | 各类型专表 | 按类型扩展(person/project/review/...) |

## 节点类型(type)

`goal · project · person · organization · review · knowledge_asset · agent_skill · human_capability · practice · tool_capability · sop · source · agent · tool · channel · metric · evidence · domain`

## 关系类型(edge_type)

`parent_of · serves · produces · proves · nourishes · executes · uses · references · relates_to`

## 隐私分级(privacy)

`public · internal · private · sensitive · secret` —— 详见 [governance/SECURITY.md](../governance/SECURITY.md)。

> 示例:`obsidian/sample-vault/60_数据账册/` 下有 `graph_nodes.csv` 与 `goal_registry.csv` 的**虚构样例**。真实注册表(含真实人物/组织)只留本地,公开版只给 schema。

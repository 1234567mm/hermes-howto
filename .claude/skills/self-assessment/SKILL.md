---
name: self-assessment
version: 2.0.0
description: >
  Assess Hermes Agent proficiency level and generate a personalized learning path.
  Trigger when: user runs /self-assessment, asks to assess their level,
  asks where to start learning, or asks which modules to study.
  DO NOT trigger for general questions about Hermes features.
---

# Self-Assessment & Learning Path Advisor

Comprehensive interactive assessment that evaluates Hermes Agent proficiency across 10 feature areas, identifies specific skill gaps, and generates a personalized learning path.

## Instructions

### Step 1: Welcome & Choose Assessment Mode

Present the user with a choice of assessment depth. Use natural language to ask:

**"欢迎来到 Hermes Agent 技能评估！请选择评估模式："**

- **Quick Assessment（8 题，约 2 分钟）** — 得到 Beginner/Intermediate/Advanced 综合等级和学习路径推荐
- **Deep Assessment（10 个领域，约 5 分钟）** — 得到每个领域的详细评分、熟练度分析和个性化学习路径

If user chooses **Quick Assessment**, go to Step 2A.
If user chooses **Deep Assessment**, go to Step 2B.

---

### Step 2A: Quick Assessment

Present 8 questions one at a time. Wait for each answer before presenting the next.

Use natural language to ask each question, or use AskUserQuestion if available.

**Question 1** (topic: Quickstart & CLI)
"你已经安装并运行过 Hermes Agent 吗？"
- A: 是的，我定期使用 `hermes` 命令
- B: 试过一两次，但不太熟
- C: 还没安装，不知道怎么开始

**Question 2** (topic: Memory)
"你用过 `/init` 命令在项目中创建 HERMES.md 文件吗？"
- A: 是的，我会用它来设置项目规则
- B: 知道这个命令但还没用过
- C: 不知道这个命令是什么

**Question 3** (topic: Skills)
"你创建或安装过含有 SKILL.md 的自定义 Skill 吗？"
- A: 是的，我理解 description 字段如何控制自动调用
- B: 用过别人的 Skill，但没有自己创建
- C: 没用过，不知道 Skill 是什么

**Question 4** (topic: Delegation)
"你用 `delegate_task` 把任务交给子代理执行过吗？"
- A: 是的，我设计过多代理工作流
- B: 试过简单的任务委托
- C: 没用过，不知道怎么委托

**Question 5** (topic: MCP)
"你配置过 MCP Server 并在 Hermes 中调用它的工具吗？"
- A: 是的，我配置并实际调用过 MCP 工具
- B: 了解 MCP 但没有实际配置过
- C: 不了解 MCP 是什么

**Question 6** (topic: Voice & Messaging)
"你通过语音模式或消息平台（Telegram/Discord/Slack）使用过 Hermes 吗？"
- A: 是的，我用过至少一种语音或消息集成
- B: 知道这些功能但没有实际配置使用
- C: 没有，我只用 CLI 文本模式

**Question 7** (topic: Cron)
"你设置过定时任务让 Hermes 在你离线时自动执行吗？"
- A: 是的，我有在跑的定时任务
- B: 看过文档但没有实际设置
- C: 不知道 Hermes 有定时任务功能

**Question 8** (topic: Advanced - SOUL, Toolsets, Plugins, Providers, Context Refs)
"你修改过 SOUL.md，或配置过 Toolsets、Plugins、Provider 或 Context Refs 吗？"
- A: 是的，我做过高级定制（至少一种）
- B: 知道这些功能存在但没有使用过
- C: 完全没接触过这些高级功能

**Scoring for Quick Assessment:**
- A = 2 points
- B = 1 point
- C = 0 points
- Maximum: 16 points

| Total Score | Level | Recommended Start | Recommended Modules |
|-------------|-------|------------------|---------------------|
| 0-5 | Beginner | 01-quickstart | 01-05 |
| 6-11 | Intermediate | 06-voice | 06-10 |
| 12-16 | Advanced | 11-plugins | 11-14 |

Go to Step 3 with the results.

---

### Step 2B: Deep Assessment

Present 10 questions, one per feature area. Each question has 3 options (A/B/C) mapping to 2/1/0 points.

**Question 1** (topic: Quickstart & CLI)
"你对 Hermes Agent 的安装和基本使用有多熟悉？"
- A: 我能独立完成安装、配置 `hermes login`，并熟练使用 `/help`, `/doctor` 等命令 (2 pts)
- B: 我安装过并用过几次，但对高级配置不太熟 (1 pt)
- C: 我刚接触或还没有安装过 Hermes (0 pts)

**Question 2** (topic: Memory)
"你对 Hermes 的内存系统和 HERMES.md 文件有多了解？"
- A: 我能创建和管理 HERMES.md，理解 5 种内存类型的区别，会用 `/init` 和 `/memory` (2 pts)
- B: 我知道 HERMES.md 的存在但没有深入使用 (1 pt)
- C: 我不知道 HERMES.md 是什么 (0 pts)

**Question 3** (topic: Skills)
"你对 Hermes Skills 系统有多熟悉？"
- A: 我能创建 SKILL.md 文件，理解 auto-invocation 和 description 的关系，会用内置技能如 `/simplify`, `/batch` (2 pts)
- B: 我用过内置技能但没有创建过自定义 Skill (1 pt)
- C: 我不知道 Skills 是什么 (0 pts)

**Question 4** (topic: Delegation)
"你对任务委托和子代理有多了解？"
- A: 我能用 `delegate_task` 创建子代理，理解 general-purpose/Plan/Explore/Bash 的区别，有并行委托经验 (2 pts)
- B: 我知道子代理的概念但没有实际使用过 (1 pt)
- C: 我不知道什么是委托和子代理 (0 pts)

**Question 5** (topic: MCP)
"你对 MCP（Model Context Protocol）集成有多熟悉？"
- A: 我能配置 MCP Server（`mcp add/remove/list`），理解 Tool/Resource/Server 的关系 (2 pts)
- B: 我知道 MCP 但没有实际配置过 Server (1 pt)
- C: 我不了解 MCP 是什么 (0 pts)

**Question 6** (topic: Voice)
"你对语音模式有多熟悉？"
- A: 我能配置语音输入输出，会用 Telegram/Discord 做语音交互 (2 pts)
- B: 我知道语音模式但没有实际使用 (1 pt)
- C: 我只用文本模式，没有用过语音 (0 pts)

**Question 7** (topic: Messaging Gateway)
"你对消息网关集成有多熟悉？"
- A: 我配置过 Telegram/Discord/Slack 机器人集成，理解跨平台消息路由 (2 pts)
- B: 我知道消息网关但没有实际配置过 (1 pt)
- C: 我没有用过消息平台集成 (0 pts)

**Question 8** (topic: Cron)
"你对定时任务和自动化有多熟悉？"
- A: 我能创建 cron 任务（`cron add/run/list`），配置 webhook 触发，理解 cron 表达式格式 (2 pts)
- B: 我知道有定时任务功能但没有实际设置 (1 pt)
- C: 我不知道 Hermes 能做定时任务 (0 pts)

**Question 9** (topic: SOUL & Toolsets)
"你对 SOUL 人格系统和 Toolsets 有多了解？"
- A: 我能创建 SOUL.md 配置人格，会创建和管理 Toolsets (2 pts)
- B: 我知道这些功能但没有实际使用 (1 pt)
- C: 我不了解 SOUL 和 Toolsets (0 pts)

**Question 10** (topic: Plugins, Providers, Checkpoints, Context Refs)
"你对高级功能模块有多熟悉？"
- A: 我能使用 plugin 命令安装插件，配置多个 Provider，理解 Checkpoint 恢复和 Context Ref 语法 (2 pts)
- B: 我用过其中一些功能但不太全面 (1 pt)
- C: 我主要只用核心功能 (0 pts)

**Scoring for Deep Assessment:**
- Each question: A=2, B=1, C=0 points
- Maximum: 20 points

**Per-Topic Scoring Table:**

| # | Feature Area | Max Points | Your Score | Mastery |
|---|-------------|------------|------------|---------|
| 1 | Quickstart & CLI | 2 | — | — |
| 2 | Memory | 2 | — | — |
| 3 | Skills | 2 | — | — |
| 4 | Delegation | 2 | — | — |
| 5 | MCP | 2 | — | — |
| 6 | Voice | 2 | — | — |
| 7 | Messaging Gateway | 2 | — | — |
| 8 | Cron | 2 | — | — |
| 9 | SOUL & Toolsets | 2 | — | — |
| 10 | Plugins/Providers/Checkpoints/Context Refs | 2 | — | — |

**Overall Level Calculation:**
- 0-6 total points = Level 1: Beginner
- 7-13 total points = Level 2: Intermediate
- 14-20 total points = Level 3: Advanced

**Mastery Levels per Topic:**
- 2/2 = Proficient (熟练)
- 1/2 = Developing (发展中)
- 0/2 = None (未掌握)

Go to Step 3 with the detailed results.

---

### Step 3: Present Results

Present a formatted results summary.

#### For Quick Assessment:

```markdown
## Hermes Agent 技能评估结果

### 综合等级：** Beginner / Intermediate / Advanced **

你得到了 **X/16** 分。

### 技能档案

| 领域 | 状态 |
|------|------|
| Quickstart & CLI | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |
| Memory | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |
| Skills | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |
| Delegation | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |
| MCP | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |
| Voice & Messaging | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |
| Cron | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |
| Advanced (SOUL/Toolsets/Plugins) | [✅ 熟练 / ⚠️ 部分 / ❌ 需学习] |

### 你的起点推荐

根据你的等级，建议从 **Module XX** 开始学习。
预计完成时间：约 X 小时。
```

#### For Deep Assessment:

```markdown
## Hermes Agent 技能评估结果

### 综合等级：** Beginner / Intermediate / Advanced **
**总分：X/20**

### 技能档案

| # | 领域 | 得分 | 熟练度 | 状态 |
|---|------|------|--------|------|
| 1 | Quickstart & CLI | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 2 | Memory | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 3 | Skills | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 4 | Delegation | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 5 | MCP | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 6 | Voice | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 7 | Messaging Gateway | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 8 | Cron | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 9 | SOUL & Toolsets | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |
| 10 | Plugins/Providers/Checkpoints/Context Refs | X/2 | [Proficient/Developing/None] | [✅/⚠️/❌] |

### 优势领域
[列出得分 2/2 的领域]

### 优先补强领域
[列出得分 0/2 的领域，按依赖顺序排列]

### 复习建议
[列出得分 1/2 的领域]
```

---

### Step 4: Generate Personalized Learning Path

Based on the results, generate a learning path that addresses the user's gaps.

**Path generation rules:**
1. Skip mastered topics (score 2/2)
2. Prioritize by dependency order: Quickstart → Memory → Skills → Delegation/MCP/Cron → Voice/Messaging → Advanced
3. Estimate time based on module complexity
4. Group into 2-3 topic phases

**Learning Path Format:**

```markdown
## 你的个性化学习路径

**预计总时间**：约 X 小时

### Phase 1: 基础入门（约 X 小时）
[如果需要学习 Quickstart 和 Memory]

**Quickstart (01-quickstart)** — 预计 30 分钟
- 教程：01-quickstart/README.md
- 重点：安装、配置 `hermes login`、基本 slash 命令
- 成功标准：能独立完成安装并运行第一个对话

**Memory (02-memory)** — 预计 45 分钟
- 教程：02-memory/README.md
- 重点：HERMES.md 创建、`/init` 和 `/memory` 命令、5 种内存类型
- 成功标准：能在项目中创建并维护 HERMES.md

### Phase 2: 核心功能（约 X 小时）
[如果需要学习 Skills, Delegation, MCP, Cron]

...

### Phase 3: 高级特性（约 X 小时）
[如果需要学习 Voice, Messaging, SOUL, Toolsets, Plugins 等]

...
```

---

### Step 5: Offer Follow-up Actions

Ask the user what they'd like to do next:

**"接下来你想做什么？"**

- **A: "开始学习第一个推荐模块"** — Read the first recommended module README and guide them through the first exercise
- **B: "用 /lesson-quiz [topic] 测试某个模块"** — Explain how to use lesson-quiz to verify understanding
- **C: "重新评估"** — Go back to Step 1 for a fresh assessment

If **A**: Read the README.md of the first recommended module and provide guidance.
If **B**: Explain the lesson-quiz command format: `/lesson-quiz [topic]` (e.g., `/lesson-quiz memory`, `/lesson-quiz 02`).
If **C**: Go back to Step 1.

---

## Error Handling

### User provides invalid input
Acknowledge the input and re-ask the question in a clearer format.

### User wants to skip a question
Note the question as "not answered" and continue. Exclude from scoring.

### User wants to quit mid-assessment
Present partial results for answered questions and offer next steps based on what was completed.

### User disagrees with assessment result
Acknowledge their perspective. Present the path for their perceived level with a note about recommended topics they may have missed.

## Module Reference

This assessment covers 14 modules:

| Module | Topic | Quiz Command |
|--------|-------|--------------|
| 01 | Quickstart | `/lesson-quiz quickstart` or `/lesson-quiz 01` |
| 02 | Memory | `/lesson-quiz memory` or `/lesson-quiz 02` |
| 03 | Skills | `/lesson-quiz skills` or `/lesson-quiz 03` |
| 04 | Delegation | `/lesson-quiz delegation` or `/lesson-quiz 04` |
| 05 | MCP | `/lesson-quiz mcp` or `/lesson-quiz 05` |
| 06 | Voice | `/lesson-quiz voice` or `/lesson-quiz 06` |
| 07 | Messaging Gateway | `/lesson-quiz messaging` or `/lesson-quiz 07` |
| 08 | Cron | `/lesson-quiz cron` or `/lesson-quiz 08` |
| 09 | SOUL/Personality | `/lesson-quiz soul-personality` or `/lesson-quiz 09` |
| 10 | Toolsets | `/lesson-quiz toolsets` or `/lesson-quiz 10` |
| 11 | Plugins | `/lesson-quiz plugins` or `/lesson-quiz 11` |
| 12 | Checkpoints | `/lesson-quiz checkpoints` or `/lesson-quiz 12` |
| 13 | Providers | `/lesson-quiz providers` or `/lesson-quiz 13` |
| 14 | Context Refs | `/lesson-quiz context-refs` or `/lesson-quiz 14` |

## Validation

### Triggering phrases:
- "assess my level"
- "self-assessment"
- "where should I start"
- "what level am I"
- "learning path"
- "what should I learn"
- "check my skills"
- "skill assessment"

### NOT triggering:
- "help me with [specific feature]"
- "explain how to use MCP"
- "create a skill"
- "review my code"

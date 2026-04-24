---
name: lesson-quiz
version: 2.0.0
description: >
  Test your knowledge of a specific Hermes Agent topic with an interactive quiz.
  Trigger when: user runs /lesson-quiz, asks to quiz on a topic, wants to test understanding,
  or says "quiz me on [topic]".
  DO NOT trigger for general questions about Hermes features.
---

# Lesson Quiz

Interactive quiz that tests understanding of a specific Hermes Agent module with 8 questions, provides per-question feedback, and identifies areas to review.

## Instructions

### Step 1: Determine the Lesson

If the user provided a lesson as an argument (e.g., `/lesson-quiz memory` or `/lesson-quiz 02`), map it to the lesson directory:

**Topic slug mapping:**

| Slug | Module | Description |
|------|--------|-------------|
| `quickstart` | 01-quickstart | Getting started with Hermes Agent |
| `memory` | 02-memory | Persistent context and memory management |
| `skills` | 03-skills | Reusable capabilities and skill configuration |
| `delegation` | 04-delegation | Task delegation and subagents |
| `mcp` | 05-mcp | MCP server integration |
| `voice` | 06-voice | Voice interaction mode |
| `messaging` | 07-messaging-gateway | Messaging platform integrations |
| `cron` | 08-cron | Scheduled tasks and automation |
| `soul-personality` | 09-soul-personality | Personality configuration |
| `toolsets` | 10-toolsets | Tool collections |
| `plugins` | 11-plugins | Plugin system |
| `checkpoints` | 12-checkpoints | Session snapshots and recovery |
| `providers` | 13-providers | AI provider configuration |
| `context-refs` | 14-context-refs | Context reference syntax |

**Number mapping:**

| Number | Slug |
|--------|------|
| 01 | quickstart |
| 02 | memory |
| 03 | skills |
| 04 | delegation |
| 05 | mcp |
| 06 | voice |
| 07 | messaging |
| 08 | cron |
| 09 | soul-personality |
| 10 | toolsets |
| 11 | plugins |
| 12 | checkpoints |
| 13 | providers |
| 14 | context-refs |

**If no argument was provided**, present a selection prompt using natural language:

```
可用的 quiz topic：

  01 · quickstart        07 · messaging
  02 · memory           08 · cron
  03 · skills           09 · soul-personality
  04 · delegation       10 · toolsets
  05 · mcp              11 · plugins
  06 · voice            12 · checkpoints
                          13 · providers
                          14 · context-refs

请输入 topic 名称或编号（例如：memory, 02, mcp）。
```

**Fallback logic** (if input cannot be recognized):
```
无法识别的输入。请输入有效的 topic 名称或编号。

可用的 topic：quickstart, memory, skills, delegation, mcp, voice, messaging, cron, soul-personality, toolsets, plugins, checkpoints, providers, context-refs
```

---

### Step 2: Read the Quiz Content

Read the YAML file for the selected topic:
- Path: `.claude/skills/lesson-quiz/topics/{topic}.yaml`

Parse the questions and prepare for presentation.

---

### Step 3: Present the Quiz

Present 8 questions in 4 rounds (2 questions per round). For each question:

1. Read the question text and 4 options clearly
2. Wait for the user's answer (A, B, C, or D)
3. **Immediately** show whether the answer was correct or incorrect
4. Provide the explanation from the question bank

**Question format:**

```
--- 第 N 题（共 8 题）---

[category: 概念理解 / 实践应用]

问题：[question text]

A. [option A]
B. [option B]
C. [option C]
D. [option D]

请输入你的答案（A/B/C/D）：
```

**After each answer:**
```
✅ 正确！[explanation]
```
或
```
❌ 错误。正确答案是 [correct_answer]。
[explanation]
```

---

### Step 4: Score and Present Results

After all 8 questions, calculate the score and present final results.

**Scoring:**
- Each correct answer = 1 point
- Total possible = 8 points

**Grade scale:**
- 7-8: Mastered — Excellent understanding
- 5-6: Partial — Good grasp, review recommended
- 0-4: Review Needed — Significant gaps

**Final results format:**

```markdown
## 📊 测验结果：[topic]

**得分：X / 8**

| 题号 | 类别 | 题目摘要 | 你的答案 | 结果 |
|------|------|---------|---------|------|
| 1 | 概念 | [short question] | [A/B/C/D] | ✅/❌ |
| 2 | 实践 | [short question] | [A/B/C/D] | ✅/❌ |
| ... | ... | ... | ... | ... |

**等级：[Mastered / Partial / Review Needed]**

---

### Recommended Next Steps

[Based on score:]

**如果 Mastered (7-8)：**
恭喜！你已掌握这个模块。可以继续学习下一个模块。

**如果 Partial (5-6)：**
建议复习以下题目后再试：
- Q[X]: [topic of weak question]
- Q[Y]: [topic of weak question]

**如果 Review Needed (0-4)：**
建议重新学习本模块的以下章节：
- [link to relevant README section]
```

---

### Step 5: Offer Follow-up

After presenting results, ask:

**"接下来你想做什么？"**

- **A: "重新测验"** — Retake the same quiz
- **B: "测验另一个 topic"** — Go back to Step 1 for topic selection
- **C: "继续学习"** — Suggest continuing to the next module in the learning path

If **A**: Restart the quiz with the same topic (skip topic selection).
If **B**: Go back to Step 1.
If **C**: Recommend the next module based on the learning path.

---

## Error Handling

### Invalid topic argument
Show the full topic list and ask for a valid selection.

### User wants to quit mid-quiz
Present partial results for answered questions only. Offer to resume later.

### Invalid answer format
Prompt again: "请输入 A、B、C 或 D。"

### YAML file not found
Error message: "找不到该 topic 的测验文件。请检查 topic 名称是否正确。"

## Topic Files Reference

| Topic | File Path |
|-------|-----------|
| quickstart | topics/quickstart.yaml |
| memory | topics/memory.yaml |
| skills | topics/skills.yaml |
| delegation | topics/delegation.yaml |
| mcp | topics/mcp.yaml |
| voice | topics/voice.yaml |
| messaging | topics/messaging.yaml |
| cron | topics/cron.yaml |
| soul-personality | topics/soul-personality.yaml |
| toolsets | topics/toolsets.yaml |
| plugins | topics/plugins.yaml |
| checkpoints | topics/checkpoints.yaml |
| providers | topics/providers.yaml |
| context-refs | topics/context-refs.yaml |

## Validation

### Triggering phrases:
- "quiz me on [topic]"
- "lesson quiz"
- "test my knowledge of [topic]"
- "practice quiz"
- "/lesson-quiz [topic]"
- "how well do I know [topic]"
- "do I understand [topic]"

### NOT triggering:
- "assess my level" (use /self-assessment instead)
- "explain [topic] to me"
- "help me with [topic]"
- "teach me [topic]"

---
name: self-assessment
description: Determine your Hermes Agent proficiency level. Usage: /self-assessment
version: 1.0.0
---

# Self-Assessment Skill

This skill helps you find your starting level based on your Hermes Agent knowledge.

## How It Works

When you invoke `/self-assessment`, you will be asked 8 questions covering key Hermes Agent topics:

1. **CLI experience** - Command-line interface familiarity
2. **Memory systems** - Persistent context and memory management
3. **Skills** - Reusable capabilities and skill configuration
4. **Delegation/subagents** - Task routing and subagent management
5. **MCP (Model Context Protocol)** - Third-party integrations
6. **Voice mode** - Audio interaction with the agent
7. **Messaging** - Messaging platform integrations (Slack, Teams, etc.)
8. **Cron/scheduling** - Scheduled task execution

## Scoring

Each question has multiple-choice answers mapped to three proficiency levels:

- **Beginner** - New to the topic
- **Intermediate** - Some experience with the topic
- **Advanced** - Extensive experience with the topic

Your final level is determined by the **mode** (most common) of your 8 answers.

## Level Definitions

| Level | Score Range | Recommended Modules |
|-------|-------------|-------------------|
| Beginner | 0-2 | 01-05 |
| Intermediate | 3-5 | 06-10 |
| Advanced | 6-8 | 11-14 |

## How to Use

1. Run `/self-assessment` in your conversation
2. Answer each question honestly
3. Receive your proficiency level and module recommendations
4. Start learning from your recommended module range

## What Happens Next

Based on your assessment result, you will receive personalized guidance on which learning modules to start with. You can then proceed at your own pace through the modules that match your current skill level.

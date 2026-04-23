<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="resources/logos/hermes-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%23%201%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/wchao-hermes/hermes-howto?style=flat&color=gold)](https://github.com/wchao-hermes/hermes-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wchao-hermes/hermes-howto?style=flat)](https://github.com/wchao-hermes/hermes-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)](CHANGELOG.md)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-Compatible-purple)](https://hermes-agent.dev)

🌐 **Language / Ngôn ngữ / 语言 / Мова:** [English](README.md) | [Tiếng Việt](vi/README.md) | [中文](zh/README.md) | [Українська](uk/README.md)

# Master Hermes Agent in a Weekend

Go from basic chat to orchestrating agents, skills, MCP servers, voice, and messaging integrations — with visual tutorials, copy-paste templates, and a guided learning path.

**[Get Started in 15 Minutes](#get-started-in-15-minutes)** | **[Find Your Level](#not-sure-where-to-start)** | **[Browse the Feature Catalog](INDEX.md)**

---

## Table of Contents

- [The Problem](#the-problem)
- [How Hermes How To Fixes This](#how-hermes-how-to-fixes-this)
- [How It Works](#how-it-works)
- [Not Sure Where to Start?](#not-sure-where-to-start)
- [Get Started in 15 Minutes](#get-started-in-15-minutes)
- [What Can You Build With This?](#what-can-you-build-with-this)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## The Problem

You installed Hermes Agent. You ran a few prompts. Now what?

- **The official docs describe features — but don't show you how to combine them.** You know skills exist, but not how to chain them with delegation, voice, and MCP into a workflow that actually saves hours.
- **There's no clear learning path.** Should you learn MCP before delegation? Memory before personality? You end up skimming everything and mastering nothing.
- **Examples are too basic.** A "hello world" skill doesn't help you build a production customer service pipeline that uses messaging gateway, voice, and scheduled tasks.

You're leaving 90% of Hermes Agent's power on the table — and you don't know what you don't know.

---

## How Hermes How To Fixes This

This isn't another feature reference. It's a **structured, visual, example-driven guide** that teaches you to use every Hermes Agent feature with real-world templates you can copy into your project today.

| | Official Docs | This Guide |
|--|---------------|------------|
| **Format** | Reference documentation | Visual tutorials with Mermaid diagrams |
| **Depth** | Feature descriptions | How it works under the hood |
| **Examples** | Basic snippets | Production-ready templates you use immediately |
| **Structure** | Feature-organized | Progressive learning path (beginner to advanced) |
| **Onboarding** | Self-directed | Guided roadmap with time estimates |
| **Self-Assessment** | None | Interactive quizzes to find your gaps and build a personalized path |

### What you get:

- **14 tutorial modules** covering every Hermes Agent feature — from quickstart to context references
- **Copy-paste configs** — skills, delegation templates, MCP configs, voice settings, messaging gateway integrations, and full plugin bundles
- **Mermaid diagrams** showing how each feature works internally, so you understand *why*, not just *how*
- **A guided learning path** that takes you from beginner to power user in 11-13 hours
- **Built-in self-assessment** — run quizzes after each module to identify gaps

**[Start the Learning Path](LEARNING-ROADMAP.md)**

---

## How It Works

### 1. Find your level

Take the self-assessment quiz or pick your current experience level. Get a personalized roadmap based on what you already know.

### 2. Follow the guided path

Work through 14 modules in order — each builds on the last. Copy templates directly into your project as you learn.

### 3. Combine features into workflows

The real power is in combining features. Learn to wire skills + delegation + MCP + voice + messaging gateway + cron into automated pipelines that handle customer service, monitoring, and integrations.

### 4. Test your understanding

Run quizzes after each module. The quiz pinpoints what you missed so you can fill gaps fast.

---

## Not Sure Where to Start?

Take the self-assessment or pick your level:

| Level | You can... | Start here | Time |
|-------|-----------|------------|------|
| **Beginner** | Start Hermes Agent and chat | [Quickstart](01-quickstart/) | ~2.5 hours |
| **Intermediate** | Use Memory and Skills | [Skills](03-skills/) | ~3.5 hours |
| **Advanced** | Configure MCP and Delegation | [Delegation](04-delegation/) | ~5 hours |

**Full learning path with all 14 modules:**

| Order | Module | Level | Time |
|-------|--------|-------|------|
| 1 | [Quickstart](01-quickstart/) | Beginner | 30 min |
| 2 | [Memory](02-memory/) | Beginner+ | 45 min |
| 3 | [Skills](03-skills/) | Intermediate | 1 hour |
| 4 | [Delegation](04-delegation/) | Intermediate+ | 1.5 hours |
| 5 | [MCP](05-mcp/) | Intermediate+ | 1 hour |
| 6 | [Voice](06-voice/) | Intermediate | 1 hour |
| 7 | [Messaging Gateway](07-messaging-gateway/) | Advanced | 1.5 hours |
| 8 | [Cron](08-cron/) | Intermediate | 45 min |
| 9 | [SOUL/Personality](09-soul-personality/) | Intermediate | 1 hour |
| 10 | [Toolsets](10-toolsets/) | Advanced | 1.5 hours |
| 11 | [Plugins](11-plugins/) | Advanced | 2 hours |
| 12 | [Checkpoints](12-checkpoints/) | Intermediate | 45 min |
| 13 | [Providers](13-providers/) | Intermediate | 1 hour |
| 14 | [Context Refs](14-context-refs/) | Advanced | 1 hour |

**[Complete Learning Roadmap](LEARNING-ROADMAP.md)**

---

## Get Started in 15 Minutes

```bash
# 1. Clone the guide
git clone https://github.com/wchao-hermes/hermes-howto.git
cd hermes-howto

# 2. Copy your first skill
mkdir -p ~/.hermes/skills
cp -r 03-skills/example-skill ~/.hermes/skills/

# 3. Try it — interact with the skill in Hermes Agent

# 4. Ready for more? Set up project memory:
cp 02-memory/project-HERMES.md /path/to/your-project/HERMES.md

# 5. Configure a provider:
cp 13-providers/provider-examples/standard-providers.yaml ~/.hermes/providers/
```

Want the full setup? Here's the **1-hour essential setup**:

```bash
# Skills (15 min)
cp -r 03-skills/* ~/.hermes/skills/

# Project memory (15 min)
cp 02-memory/project-HERMES.md ./HERMES.md

# Delegation templates (15 min)
cp -r 04-delegation/* ~/.hermes/delegation/

# MCP servers (15 min)
export GITHUB_TOKEN="***"
hermes mcp add github -- npx -y @modelcontextprotocol/server-github

# Weekend goal: add voice, messaging gateway, cron, plugins
# Follow the learning path for guided setup
```

---

## What Can You Build With This?

| Use Case | Features You'll Combine |
|----------|------------------------|
| **Customer Service Bot** | Messaging Gateway + Voice + Skills + MCP |
| **Scheduled Monitoring** | Cron + Delegation + Checkpoints + Providers |
| **Multi-agent Pipeline** | Delegation + SOUL/Personality + Toolsets + Plugins |
| **Voice Assistant** | Voice + Memory + Skills + MCP |
| **Team Onboarding** | Memory + Plugins + Context Refs |
| **DevOps Automation** | Cron + MCP + Checkpoints + Providers |
| **Complex Refactoring** | Checkpoints + Planning + Delegation |

---

## FAQ

**Is this free?**
Yes. MIT licensed, free forever. Use it in personal projects, at work, in your team — no restrictions beyond including the license notice.

**Is this maintained?**
Actively. The guide is synced with every Hermes Agent release.

**How is this different from the official docs?**
The official docs are a feature reference. This guide is a tutorial with diagrams, production-ready templates, and a progressive learning path. They complement each other — start here to learn, reference the docs when you need specifics.

**How long does it take to go through everything?**
11-13 hours for the full path. But you'll get immediate value in 15 minutes — just copy a skill template and try it.

**Can I contribute?**
Absolutely. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome new examples, bug fixes, documentation improvements, and community templates.

**Can I read this offline?**
Yes. Clone the repo and read locally, or generate an offline version using the scripts.

---

## Start Mastering Hermes Agent Today

You already have Hermes Agent installed. The only thing between you and 10x productivity is knowing how to use it. This guide gives you the structured path, the visual explanations, and the copy-paste templates to get there.

MIT licensed. Free forever. Clone it, fork it, make it yours.

**[Start the Learning Path](LEARNING-ROADMAP.md)** | **[Browse the Feature Catalog](INDEX.md)** | **[Get Started in 15 Minutes](#get-started-in-15-minutes)**

---

<details>
<summary>Quick Navigation — All Features</summary>

| Feature | Description | Folder |
|---------|-------------|--------|
| **Feature Catalog** | Complete reference with installation commands | [INDEX.md](INDEX.md) |
| **Quickstart** | Getting started guide | [01-quickstart/](01-quickstart/) |
| **Memory** | Persistent context | [02-memory/](02-memory/) |
| **Skills** | Reusable capabilities | [03-skills/](03-skills/) |
| **Delegation** | Task delegation | [04-delegation/](04-delegation/) |
| **MCP Protocol** | External tool access | [05-mcp/](05-mcp/) |
| **Voice** | Voice interaction | [06-voice/](06-voice/) |
| **Messaging Gateway** | Messaging platform integrations | [07-messaging-gateway/](07-messaging-gateway/) |
| **Cron** | Scheduled tasks | [08-cron/](08-cron/) |
| **SOUL/Personality** | Agent personality configuration | [09-soul-personality/](09-soul-personality/) |
| **Toolsets** | Tool collections | [10-toolsets/](10-toolsets/) |
| **Plugins** | Bundled features | [11-plugins/](11-plugins/) |
| **Checkpoints** | Session snapshots & rewind | [12-checkpoints/](12-checkpoints/) |
| **Providers** | AI provider configuration | [13-providers/](13-providers/) |
| **Context Refs** | Context references | [14-context-refs/](14-context-refs/) |

</details>

<details>
<summary>Feature Comparison</summary>

| Feature | Invocation | Persistence | Best For |
|---------|-----------|------------|----------|
| **Skills** | Auto-invoked | Filesystem | Automated workflows |
| **Delegation** | Auto-delegated | Isolated context | Task distribution |
| **Memory** | Auto-loaded | Cross-session | Long-term learning |
| **MCP Protocol** | Auto-queried | Real-time | Live data access |
| **Voice** | User-initiated | Session | Hands-free interaction |
| **Messaging Gateway** | Event-triggered | Real-time | Platform integrations |
| **Cron** | Scheduled | Persistent | Recurring tasks |
| **SOUL/Personality** | Configured | Persistent | Custom behavior |
| **Toolsets** | Auto-available | Session | Extended capabilities |
| **Plugins** | One command | All features | Complete solutions |
| **Checkpoints** | Manual/Auto | Session-based | Safe experimentation |
| **Providers** | Configured | Persistent | AI backend selection |
| **Context Refs** | Auto-injected | Per-request | Dynamic context |

</details>

<details>
<summary>Installation Quick Reference</summary>

```bash
# Skills
cp -r 03-skills/* ~/.hermes/skills/

# Memory
cp 02-memory/project-HERMES.md ./HERMES.md

# Delegation
cp -r 04-delegation/* ~/.hermes/delegation/

# MCP
export GITHUB_TOKEN="***"
hermes mcp add github -- npx -y @modelcontextprotocol/server-github

# Voice (configure in settings)
# See 06-voice/README.md

# Messaging Gateway
# See 07-messaging-gateway/README.md

# Cron
# See 08-cron/README.md

# Plugins
/hermes plugin install pr-review

# Checkpoints (auto-enabled, configure in settings)
# See 12-checkpoints/README.md

# Providers
cp 13-providers/provider-examples/*.yaml ~/.hermes/providers/

# Context Refs
# See 14-context-refs/README.md
```

</details>

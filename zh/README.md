<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
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
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-兼容-purple)](https://hermes-agent.dev)

🌐 **语言 / Language / Ngôn ngữ / Мова:** [English](../README.md) | [Tiếng Việt](../vi/README.md) | [中文](README.md) | [Українська](../uk/README.md)

# 一个周末掌握 Hermes Agent

从基础聊天到编排 agents、skills、MCP servers、voice 和消息集成 — 配有可视化教程、可直接复制粘贴的模板和循序渐进的学习路径。

**[15分钟入门](#15分钟入门)** | **[确定你的水平](#不知道从哪里开始)** | **[浏览功能目录](../INDEX.md)**

---

## 目录

- [问题](#问题)
- [Hermes How To 如何解决](#hermes-how-to-如何解决)
- [如何运作](#如何运作)
- [不知道从哪里开始？](#不知道从哪里开始)
- [15分钟入门](#15分钟入门)
- [你能用它构建什么？](#你能用它构建什么)
- [常见问题](#常见问题)
- [贡献](#贡献)
- [许可证](#许可证)

---

## 问题

你安装了 Hermes Agent。你运行了一些提示。现在怎么办？

- **官方文档描述功能 — 但不展示如何组合它们。** 你知道 skills 存在，但不知道如何将它们与 delegation、voice 和 MCP 连接成真正节省时间的 workflow。
- **没有明确的学习路径。** 应该先学 MCP 还是 delegation？Memory 还是 personality？你最终只能浏览一切却什么都学不精。
- **例子太基础。** 一个 "hello world" skill 无法帮助你构建一个使用消息网关、语音和定时任务的生产级客户服务管道。

你正在浪费 Hermes Agent 90% 的能力 — 而你不知道自己不知道什么。

---

## Hermes How To 如何解决

这不是另一份功能参考文档。这是一份**结构化的、可视化的、以示例为导向的指南**，教你使用 Hermes Agent 的每个功能，并提供可立即复制到项目中的真实模板。

| | 官方文档 | 本指南 |
|--|---------|--------|
| **格式** | 参考文档 | 带 Mermaid 图的可视化教程 |
| **深度** | 功能描述 | 内部工作原理 |
| **示例** | 基础代码片段 | 可立即投入生产的模板 |
| **结构** | 按功能组织 | 从入门到进阶的学习路径 |
| **入门** | 自我导向 | 带时间估算的引导路线 |
| **自我评估** | 无 | 互动测验找出差距 |

### 你将获得：

- **14个教程模块** 涵盖 Hermes Agent 的每个功能 — 从快速入门到上下文引用
- **即用型配置** — skills、 delegation 模板、MCP 配置、语音设置、消息网关集成和完整的插件包
- **Mermaid 图** 显示每个功能如何内部运作，让你理解*为什么*，而不只是*如何*
- **引导式学习路径** 在 11-13 小时内让你从初学者成为高级用户
- **内置自我评估** — 每个模块后运行测验找出差距

**[开始学习路径](../LEARNING-ROADMAP.md)**

---

## 如何运作

### 1. 确定你的水平

参加自我评估测验或选择你当前的体验水平。根据你已经知道的获得个性化路线。

### 2. 遵循引导路径

按顺序完成 14 个模块 — 每个都建立在前一个的基础上。学习时直接将模板复制到你的项目中。

### 3. 将功能组合成工作流

真正的力量在于组合功能。学习将 skills + delegation + MCP + voice + 消息网关 + cron 连接成自动化管道，处理客户服务、监控和集成。

### 4. 测试你的理解

每个模块后运行测验。测验会指出你遗漏的内容，让你快速填补。

---

## 不知道从哪里开始？

参加自我评估测验或选择你的水平：

| 级别 | 你能... | 从这里开始 | 时间 |
|------|--------|-----------|------|
| **初学者** | 启动 Hermes Agent 并聊天 | [快速入门](../01-quickstart/) | ~2.5 小时 |
| **中级** | 使用 Memory 和 Skills | [Skills](../03-skills/) | ~3.5 小时 |
| **高级** | 配置 MCP 和 Delegation | [Delegation](../04-delegation/) | ~5 小时 |

**完整学习路径，包含全部14个模块：**

| 顺序 | 模块 | 级别 | 时间 |
|------|------|------|------|
| 1 | [快速入门](../01-quickstart/) | 初学者 | 30 分钟 |
| 2 | [Memory](../02-memory/) | 初学者+ | 45 分钟 |
| 3 | [Skills](../03-skills/) | 中级 | 1 小时 |
| 4 | [Delegation](../04-delegation/) | 中级+ | 1.5 小时 |
| 5 | [MCP](../05-mcp/) | 中级+ | 1 小时 |
| 6 | [Voice](../06-voice/) | 中级 | 1 小时 |
| 7 | [消息网关](../07-messaging-gateway/) | 高级 | 1.5 小时 |
| 8 | [Cron](../08-cron/) | 中级 | 45 分钟 |
| 9 | [SOUL/Personality](../09-soul-personality/) | 中级 | 1 小时 |
| 10 | [Toolsets](../10-toolsets/) | 高级 | 1.5 小时 |
| 11 | [Plugins](../11-plugins/) | 高级 | 2 小时 |
| 12 | [Checkpoints](../12-checkpoints/) | 中级 | 45 分钟 |
| 13 | [Providers](../13-providers/) | 中级 | 1 小时 |
| 14 | [Context Refs](../14-context-refs/) | 高级 | 1 小时 |

**[完整学习路线图](../LEARNING-ROADMAP.md)**

---

## 15分钟入门

```bash
# 1. 克隆本指南
git clone https://github.com/wchao-hermes/hermes-howto.git
cd hermes-howto

# 2. 复制你的第一个 skill
mkdir -p ~/.hermes/skills
cp -r 03-skills/example-skill ~/.hermes/skills/

# 3. 试试看 — 在 Hermes Agent 中与 skill 互动

# 4. 想要更多？设置项目 memory：
cp 02-memory/project-HERMES.md /你的项目路径/HERMES.md

# 5. 配置 provider：
cp 13-providers/provider-examples/standard-providers.md ~/.hermes/providers/
```

想要完整设置？这是**1小时 essential 设置**：

```bash
# Skills（15分钟）
cp -r 03-skills/* ~/.hermes/skills/

# 项目 memory（15分钟）
cp 02-memory/project-HERMES.md ./HERMES.md

# Delegation 模板（15分钟）
cp -r 04-delegation/* ~/.hermes/delegation/

# MCP 服务器（15分钟）
export GITHUB_TOKEN="***"
hermes mcp add github -- npx -y @modelcontextprotocol/server-github

# 周末目标：添加 voice、消息网关、cron、plugins
# 按照学习路径进行引导设置
```

---

## 你能用它构建什么？

| 用例 | 将组合的功能 |
|------|-------------|
| **客服机器人** | 消息网关 + 语音 + Skills + MCP |
| **定时监控** | Cron + Delegation + Checkpoints + Providers |
| **多代理管道** | Delegation + SOUL/Personality + Toolsets + Plugins |
| **语音助手** | Voice + Memory + Skills + MCP |
| **团队入职** | Memory + Plugins + Context Refs |
| **DevOps 自动化** | Cron + MCP + Checkpoints + Providers |
| **复杂重构** | Checkpoints + Planning + Delegation |

---

## 常见问题

**这个免费吗？**
是的。MIT 许可证，永久免费。在个人项目、工作、团队中使用 — 除了包含许可证通知外没有任何限制。

**这个有维护吗？**
积极维护。本指南与每个 Hermes Agent 发行版同步。

**这与官方文档有什么不同？**
官方文档是功能参考。本指南是带图表、生产级模板和循序渐进学习路径的教程。它们互补 — 从这里开始学习，需要细节时参考文档。

**完成全部需要多长时间？**
完整路径 11-13 小时。但你会在 15 分钟内获得即时价值 — 只需复制一个 skill 模板并尝试。

**我可以贡献吗？**
当然。查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解指南。我们欢迎新的示例、错误修复、文档改进和社区模板。

---

## 今天就开始掌握 Hermes Agent

你已经安装了 Hermes Agent。你和 10 倍生产力之间的唯一区别就是知道如何使用它。本指南为你提供了结构化路径、可视化解释和可复制粘贴的模板。

MIT 许可证。永久免费。克隆它，fork 它，让它成为你的。

**[开始学习路径](../LEARNING-ROADMAP.md)** | **[浏览功能目录](../INDEX.md)** | **[15分钟入门](#15分钟入门)**

---

<details>
<summary>快速导航 — 所有功能</summary>

| 功能 | 描述 | 文件夹 |
|------|------|--------|
| **功能目录** | 带安装命令的完整参考 | [INDEX.md](../INDEX.md) |
| **快速入门** | 入门指南 | [01-quickstart/](../01-quickstart/) |
| **Memory** | 持久上下文 | [02-memory/](../02-memory/) |
| **Skills** | 可重用能力 | [03-skills/](../03-skills/) |
| **Delegation** | 任务委托 | [04-delegation/](../04-delegation/) |
| **MCP Protocol** | 外部工具访问 | [05-mcp/](../05-mcp/) |
| **Voice** | 语音交互 | [06-voice/](../06-voice/) |
| **消息网关** | 消息平台集成 | [07-messaging-gateway/](../07-messaging-gateway/) |
| **Cron** | 定时任务 | [08-cron/](../08-cron/) |
| **SOUL/Personality** | Agent 个性配置 | [09-soul-personality/](../09-soul-personality/) |
| **Toolsets** | 工具集合 | [10-toolsets/](../10-toolsets/) |
| **Plugins** | 捆绑功能 | [11-plugins/](../11-plugins/) |
| **Checkpoints** | 会话快照和回滚 | [12-checkpoints/](../12-checkpoints/) |
| **Providers** | AI 提供商配置 | [13-providers/](../13-providers/) |
| **Context Refs** | 上下文引用 | [14-context-refs/](../14-context-refs/) |

</details>

<details>
<summary>功能比较</summary>

| 功能 | 调用方式 | 持久性 | 最适合 |
|------|---------|--------|--------|
| **Skills** | 自动调用 | 文件系统 | 自动化工作流 |
| **Delegation** | 自动委托 | 隔离上下文 | 任务分发 |
| **Memory** | 自动加载 | 跨会话 | 长期学习 |
| **MCP Protocol** | 自动查询 | 实时 | 实时数据访问 |
| **Voice** | 用户发起 | 会话 | 免手操作 |
| **消息网关** | 事件触发 | 实时 | 平台集成 |
| **Cron** | 定时 | 持久 | 周期性任务 |
| **SOUL/Personality** | 配置 | 持久 | 自定义行为 |
| **Toolsets** | 自动可用 | 会话 | 扩展能力 |
| **Plugins** | 一条命令 | 所有功能 | 完整解决方案 |
| **Checkpoints** | 手动/自动 | 基于会话 | 安全实验 |
| **Providers** | 已配置 | 持久 | AI 后端选择 |
| **Context Refs** | 自动注入 | 每次请求 | 动态上下文 |

</details>

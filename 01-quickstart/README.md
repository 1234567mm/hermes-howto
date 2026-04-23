<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Quickstart

Get Claude Code running in 15 minutes. This module covers installation, your first conversation, and essential configuration.

## Overview

Claude Code is an AI coding assistant that runs in your terminal. It combines a powerful LLM with deep file system access, git integration, and tool execution to help you write, review, and refactor code.

```mermaid
graph LR
    A["User Input"] --> B["Claude Code CLI"]
    B --> C["File System"]
    B --> D["Git"]
    B --> E["Shell/Tools"]
    B --> F["LLM Backend"]
    F --> B
```

## What You'll Learn

| Module | Topic | Time |
|--------|-------|------|
| [Installation](installation.md) | Install Claude Code | 5 min |
| [First Conversation](first-conversation.md) | Run your first prompt | 5 min |
| [Configuration](configuration.md) | Configure for your workflow | 5 min |

## Quick Comparison

| Feature | Manual Coding | Claude Code |
|---------|---------------|-------------|
| **Speed** | Write each line manually | Generate full functions |
| **Consistency** | Varies by developer | Follows project patterns |
| **Search** | `grep` + manual review | Ask and get context |
| **Debugging** | Add logs, trace manually | Explain the issue |
| **Documentation** | Often skipped | Generated inline |

## System Requirements

- **OS**: macOS 12+, Linux (Ubuntu 20.04+), Windows with WSL
- **Shell**: Bash, Zsh, Fish, or PowerShell
- **Network**: Internet connection for LLM access

## Next Steps

After completing this module, continue to [Slash Commands](../02-slash-commands/README.md) to learn about built-in shortcuts.

## Getting Help

If you encounter issues:

- Run `/doctor` in Claude Code to diagnose problems
- Run `/help` to see all available commands
- Visit [docs.claude.com](https://docs.claude.com) for full documentation

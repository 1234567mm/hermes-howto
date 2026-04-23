# Memory System

Persistent context management for Hermes Agent sessions.

## Overview

Memory enables Hermes to retain context across sessions through filesystem-based HERMES.md files. Unlike temporary conversation context, memory files persist indefinitely and are shared across team members when committed to version control.

## Quick Reference

| Command | Purpose |
|---------|---------|
| `/init` | Initialize new HERMES.md with template |
| `/memory` | Edit memory files in system editor |

## Memory Types

| Type | Location | Scope |
|------|----------|-------|
| Managed Policy | System-wide (OS-specific) | Organization |
| Project Memory | `./HERMES.md` or `./.hermes/HERMES.md` | Team |
| Project Rules | `./.hermes/rules/*.md` | Team (modular) |
| User Memory | `~/.hermes/HERMES.md` | Personal |
| Local Memory | `./HERMES.local.md` | Personal (git-ignored) |
| Auto Memory | `~/.hermes/projects/<project>/memory/` | Automatic learnings |

## Files in This Module

- [memory-file.md](memory-file.md) - HERMES.md and MEMORY.md file formats
- [memory-tool.md](memory-tool.md) - /init and /memory commands
- [memory-providers.md](memory-providers.md) - Memory hierarchy and providers

## Architecture

```mermaid
graph TB
    A[Hermes Session] --> B[Memory System]
    B --> C[HERMES.md Files]
    B --> D[Auto Memory]
    C --> E[Project Memory]
    C --> F[User Memory]
    E --> G[Team Standards]
    F --> H[Personal Preferences]
```

## Quick Start

```bash
# Initialize project memory
hermes /init

# Edit existing memory
hermes /memory
```

## Example Usage

```markdown
# Ask Hermes to remember something
Remember that we use TypeScript strict mode in this project.

# Hermes prompts for memory location:
# 1. Project memory (./HERMES.md)
# 2. Personal memory (~/.hermes/HERMES.md)
```

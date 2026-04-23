# Memory Providers

## Overview

Memory providers define where memory is stored and how it is loaded. Hermes Agent uses a hierarchical system with multiple provider levels, each serving different scopes.

## Memory Hierarchy

Memory files are loaded in precedence order (highest to lowest):

```mermaid
graph TD
    A["Managed Policy<br/>/Library/HermesAgent/HERMES.md"] -->|highest| B["Managed Drop-ins<br/>managed-settings.d/"]
    B --> C["Project Memory<br/>./HERMES.md"]
    C --> D["Project Rules<br/>./.hermes/rules/*.md"]
    D --> E["User Memory<br/>~/.hermes/HERMES.md"]
    E --> F["User Rules<br/>~/.hermes/rules/*.md"]
    F --> G["Local Memory<br/>./HERMES.local.md"]
    G --> H["Auto Memory<br/>~/.hermes/projects/.../memory/"]
    style A fill:#fce4ec
    style H fill:#fff3e0
```

## Provider Locations

### Managed Policy (Highest Priority)

| Platform | Location |
|----------|----------|
| macOS | `/Library/Application Support/HermesAgent/HERMES.md` |
| Linux/WSL | `/etc/hermes-agent/HERMES.md` |
| Windows | `C:\Program Files\HermesAgent\HERMES.md` |

Purpose: Organization-wide policies and security standards.

### Managed Drop-ins (v2.1.83+)

Location: Alongside managed policy in `managed-settings.d/` directory

Files are merged alphabetically. Enables modular policy management.

### Project Memory

| Location | Scope |
|----------|-------|
| `./HERMES.md` | Project root |
| `./.hermes/HERMES.md` | Alternative project location |

Purpose: Team-shared context, committed to git.

### Project Rules

Location: `./.hermes/rules/*.md` (recursive subdirectories supported)

Purpose: Modular, topic-specific project instructions.

### User Memory

Location: `~/.hermes/HERMES.md`

Purpose: Personal preferences across all projects.

### User Rules

Location: `~/.hermes/rules/*.md`

Purpose: Personal rules for all projects.

### Local Project Memory

Location: `./HERMES.local.md`

Purpose: Personal project-specific preferences (git-ignored).

### Auto Memory (Lowest Priority)

Location: `~/.hermes/projects/<project>/memory/`

Purpose: Hermes's automatic notes and learnings during sessions.

## Settings File Hierarchy

Memory-related settings (`autoMemoryDirectory`, `hermesMdExcludes`) follow this precedence:

| Level | Location | Scope |
|-------|----------|-------|
| 1 (highest) | Managed policy | Organization |
| 2 | `managed-settings.d/` | Modular policy |
| 3 | `~/.hermes/settings.json` | User |
| 4 | `.hermes/settings.json` | Project (git-tracked) |
| 5 (lowest) | `.hermes/settings.local.json` | Local overrides |

## hermesMdExcludes

Exclude irrelevant HERMES.md files in large monorepos:

```json
{
  "hermesMdExcludes": [
    "packages/legacy-app/HERMES.md",
    "vendors/**/HERMES.md"
  ]
}
```

## autoMemoryDirectory

Customize auto memory location:

```json
{
  "autoMemoryDirectory": "/path/to/custom/memory"
}
```

> Note: Only configurable in user or local settings.

## Loading Behavior

### Startup Loading

- All HERMES.md files loaded automatically at session start
- Earlier in hierarchy = higher precedence
- Auto memory loads first 200 lines / 25KB of MEMORY.md

### Context During Session

- Subdirectory HERMES.md loaded when accessing those directories
- Topic-specific auto memory files loaded on demand

### Worktree Behavior

All worktrees in same git repository share one auto memory directory.

## Subagent Memory

Subagents can be configured to load specific memory scopes:

```yaml
memory: user      # User-level only
memory: project   # Project-level only
memory: local     # Local memory only
```

## Comparison Table

| Provider | Scope | Shared | Priority | Version Control |
|----------|-------|--------|----------|----------------|
| Managed Policy | Organization | Yes | 1 | No |
| Managed Drop-ins | Organization | Yes | 2 | No |
| Project Memory | Team | Yes | 3 | Yes |
| Project Rules | Team | Yes | 4 | Yes |
| User Memory | Personal | No | 5 | No |
| User Rules | Personal | No | 6 | No |
| Local Memory | Personal | No | 7 | No |
| Auto Memory | Personal | No | 8 | No |

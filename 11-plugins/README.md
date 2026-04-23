<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Plugins

Plugins extend Hermes with custom functionality through structured packages that can include tools, skills, and agent configurations.

## Overview

Plugins enable you to:

- **Package capabilities** — Bundle tools, skills, and agents together
- **Share functionality** — Distribute reusable plugin packages
- **Enable/disable easily** — Toggle plugins without losing configuration
- **Version management** — Track and update plugin versions

```mermaid
graph TB
    Hermes[Hermes] --> Plugins[Plugin System]
    Plugins --> PluginA[Plugin A]
    Plugins --> PluginB[Plugin B]
    Plugins --> PluginC[Plugin C]
    PluginA --> |tools| Tool1[Tool 1]
    PluginA --> |tools| Tool2[Tool 2]
    PluginA --> |skills| Skill1[Skill 1]
    PluginB --> |tools| Tool3[Tool 3]
    PluginB --> |agents| Agent1[Agent 1]
```

## What You'll Learn

| | Topic | Description |
|---|-------|-------------|
| | [plugin-format.md](plugin-format.md) | Plugin package structure and manifest |
| | [plugin-examples/](plugin-examples/) | Example plugin implementations |

## Key Concepts

### Plugin vs Skill vs Toolset

| Component | Contents | Scope | Use Case |
|-----------|----------|-------|----------|
| **Plugin** | Tools + Skills + Agents | Feature packages | Complete capabilities |
| **Skill** | Instructions + Templates | Expertise | Domain-specific tasks |
| **Toolset** | Tool definitions | Tool collections | Related commands |

### Plugin Structure

```
my-plugin/
├── PLUGIN.md              # Plugin manifest
├── skills/
│   └── my-skill/
│       └── SKILL.md
├── tools/
│   └── my-tool.md
└── agents/
    └── my-agent.md
```

### Plugin Types

| Type | Description |
|------|-------------|
| **Built-in** | Ships with Hermes |
| **Community** | Shared via plugin registry |
| **Local** | Installed from local paths |
| **Remote** | Installed from git URLs |

## Plugin Management

| Task | Command |
|------|---------|
| List plugins | `plugin list` |
| Install | `plugin install <name>` |
| Uninstall | `plugin uninstall <name>` |
| Enable | `plugin enable <name>` |
| Disable | `plugin disable <name>` |
| Update | `plugin update <name>` |

## File Locations

| Type | Location | Scope |
|------|---------|-------|
| **Project plugins** | `.claude/plugins/` | Current project |
| **User plugins** | `~/.claude/plugins/` | All projects |

## Verify Your Understanding

1. Run `/lesson-quiz plugins` to test your knowledge
2. Review areas needing reinforcement
3. Proceed to next module

## Next Steps

- [plugin-format.md](plugin-format.md) — Create your first plugin
- [plugin-examples/](plugin-examples/) — Reference implementations

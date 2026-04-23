<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Skills System

Skills are reusable, filesystem-based capabilities that extend Hermes Agent's functionality. They package domain-specific expertise, workflows, and best practices into discoverable components that Hermes Agent automatically uses when relevant.

## Overview

**Skills** transform general-purpose agents into specialists. Unlike prompts (conversation-level instructions for one-off tasks), Skills load on-demand and eliminate the need to repeatedly provide the same guidance across multiple conversations.

### Key Benefits

- **Specialize Hermes Agent**: Tailor capabilities for domain-specific tasks
- **Reduce repetition**: Create once, use automatically across conversations
- **Compose capabilities**: Combine Skills to build complex workflows
- **Scale workflows**: Reuse skills across multiple projects and teams
- **Maintain quality**: Embed best practices directly into your workflow

## What You'll Learn

|| Module | Topic |
||--------|-------|
|| [Skill Format](skill-format.md) | SKILL.md structure and frontmatter fields |
|| [Skill Lifecycle](skill-lifecycle.md) | Progressive disclosure, loading, invocation control |
|| [Skill Examples](skill-examples/) | Bundled skill implementations |

## Skill Types & Locations

|| Type | Location | Scope | Best For |
||------|----------|-------|----------|
| **Personal** | `~/.hermes/skills/<skill-name>/SKILL.md` | Individual | Personal workflows |
| **Project** | `.hermes/skills/<skill-name>/SKILL.md` | Team | Team standards |
| **Plugin** | `<plugin>/skills/<skill-name>/SKILL.md` | Where enabled | Bundled features |

## Skills vs Other Features

|| Feature | Invocation | Best For |
||---------|------------|----------|
| **Skills** | Auto or `/name` | Reusable expertise, workflows |
| **Slash Commands** | User-initiated `/name` | Quick shortcuts |
| **Subagents** | Auto-delegated | Isolated task execution |
| **Memory (CLAUDE.md)** | Always loaded | Persistent project context |
| **MCP** | Real-time | External data/service access |
| **Hooks** | Event-driven | Automated side effects |

## Next Steps

After completing this module, continue to [Subagents](../04-subagents/README.md) to learn about delegated AI agents.

## Bundled Skills

Hermes Agent ships with built-in skills:

|| Skill | Description |
||-------|-------------|
| `/simplify` | Review changed files for reuse, quality, and efficiency |
| `/batch <instruction>` | Orchestrate large-scale parallel changes |
| `/debug [description]` | Troubleshoot current session |
| `/loop [interval] <prompt>` | Run prompt repeatedly on interval |

## Additional Resources

- [Official Skills Documentation](https://code.claude.com/docs/en/skills)
- [Agent Skills Architecture Blog](https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills)
- [Slash Commands Guide](../01-slash-commands/README.md) - User-initiated shortcuts
- [Subagents Guide](../04-subagents/README.md) - Delegated AI agents
- [Memory Guide](../02-memory/README.md) - Persistent context

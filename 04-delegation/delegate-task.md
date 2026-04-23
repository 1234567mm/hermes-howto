<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# delegate_task Tool

Spawn specialized subagents to execute tasks in parallel with isolated context windows.

## Overview

The `delegate_task` tool creates subagents with their own context windows, allowing parallel execution of specialized tasks without context pollution.

## Signature

```
delegate_task(task: string, agent?: string, agentId?: string)
```

## Parameters

|| Parameter | Type | Required | Description |
||-----------|------|----------|-------------|
| `task` | string | Yes | Task description for the subagent |
| `agent` | string | No | Agent name to use (e.g., "code-reviewer") |
| `agentId` | string | No | Resume an existing agent session |

## Usage Patterns

### Explicit Agent Delegation

```
delegate_task("Review the authentication module for security issues", "secure-reviewer")
```

### Implicit Delegation

```
delegate_task("Analyze performance bottlenecks in the data pipeline")
```

Hermes automatically selects an appropriate agent based on task description.

### Resume an Agent

```
delegate_task("Continue analyzing the codebase", agentId="abc123")
```

## Return Value

```
{
  agentId: "abc123",
  result: "Task completed. Found 3 security issues..."
}
```

## Parallel Execution

Spawn multiple subagents simultaneously:

```
# Agent 1: Code review
delegate_task("Review recent changes in src/auth/", "code-reviewer")

# Agent 2: Test creation
delegate_task("Write tests for the auth module", "test-engineer")

# Agent 3: Documentation
delegate_task("Update auth module documentation", "documentation-writer")
```

All three run in parallel, returning results when complete.

## Built-in Agents

|| Agent | Tools | Best For |
||-------|-------|----------|
| `general-purpose` | All | Complex multi-step tasks |
| `Explore` | Read, Grep, Glob | Read-only exploration |
| `Bash` | Bash | Shell command isolation |

## Configuration

Agents are defined in YAML with frontmatter:

```yaml
---
name: code-reviewer
description: Expert code review specialist
tools: Read, Grep, Glob, Bash
---

Your system prompt here defining the agent's role,
capabilities, and approach.
```

## Agent Locations

|| Location | Scope |
||----------|-------|
| `.claude/agents/` | Project-specific |
| `~/.claude/agents/` | User-wide |

## Examples

### Simple Delegation

```
delegate_task("Find all TODO comments in the codebase")
```

### Specialized Agent

```
delegate_task("Review the payment processing code", "secure-reviewer")
```

### With Context

```
delegate_task("""
1. Read src/database/schema.sql
2. Analyze the table relationships
3. Propose optimizations for the query patterns
""")
```

### Resume Previous Work

```
delegate_task("Continue where we left off - implement the remaining endpoints", agentId="prev-123")
```

## Keyboard Shortcuts

|| Shortcut | Action |
||----------|--------|
| `Ctrl+B` | Background a running subagent |
| `Ctrl+F` | Kill all background agents |

## Next Steps

- [when-to-delegate.md](when-to-delegate.md) — Decision framework
- [delegation-examples/](delegation-examples/) — Ready-to-use agents

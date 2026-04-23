# Feature Catalog

Complete reference of all Hermes Agent features with installation commands.

## Quick Install Commands

| Feature | Command | Module |
|---------|---------|--------|
| Memory | `cp 02-memory/memory-file.md ~/.hermes/memories/MEMORY.md` | 02 |
| Skills | `cp -r 03-skills/skill-examples/* ~/.hermes/skills/` | 03 |
| Delegation | `cp -r 04-delegation/delegation-examples/* ~/.hermes/agents/` | 04 |
| MCP | `cp -r 05-mcp/mcp-examples/* ~/.hermes/mcp/` | 05 |
| Voice | `cp 06-voice/voice-setup.md ~/.hermes/voice-config.md` | 06 |
| Messaging Gateway | `cp -r 07-messaging-gateway/bot-patterns/* ~/.hermes/gateway/` | 07 |
| Cron | `cp -r 08-cron/cron-examples/* ~/.hermes/cron/` | 08 |
| SOUL/Personality | `cp -r 09-soul-personality/personality-examples/* ~/.hermes/soul/` | 09 |
| Toolsets | `cp -r 10-toolsets/toolset-examples/* ~/.hermes/toolsets/` | 10 |
| Plugins | `cp 11-plugins/plugin-examples/code-review-plugin.md ~/.hermes/plugins/` | 11 |
| Checkpoints | (auto-enabled) | 12 |
| Providers | `cp 13-providers/provider-examples/standard-providers.md ~/.hermes/providers/` | 13 |
| Context Refs | `cp -r 14-context-refs/context-ref-examples/* ~/.hermes/context-refs/` | 14 |

## Feature Details

### 01 - Quickstart

Install and configure Hermes Agent for first-time use.

**Installation:**
```bash
# Install Hermes Agent
curl -fsSL https://hermes.com/install.sh | sh

# Verify installation
hermes --version
```

**Description:** Quickstart covers installation, initial configuration, and first conversation setup. Get up and running in 15 minutes.

---

### 02 - Memory

Persistent context management for Hermes sessions.

**Installation:**
```bash
# Install memory template
mkdir -p ~/.hermes/memories
cp 02-memory/memory-file.md ~/.hermes/memories/MEMORY.md

# Install auto-memory structure
mkdir -p ~/.hermes/projects/default/memory
```

**Description:** Memory enables Hermes to retain context across sessions through filesystem-based files. Includes CLAUDE.md for manual instructions and MEMORY.md for auto-generated learnings.

**Key Files:**
- `memory-file.md` - MEMORY.md and CLAUDE.md format reference
- `memory-tool.md` - /init and /memory commands
- `memory-providers.md` - Memory hierarchy and providers

---

### 03 - Skills

Reusable, filesystem-based capabilities that extend Hermes functionality.

**Installation:**
```bash
# Install all skill examples
cp -r 03-skills/skill-examples/* ~/.hermes/skills/

# Verify skills installed
ls ~/.hermes/skills/
```

**Skill Examples Available:**
- `brave-search.json` - Web search capability
- `database-query.json` - Database operations
- `dev-stack.json` - Development stack integration
- `filesystem-readonly.json` - Read-only file access
- `filesystem-readwrite.json` - Full file access
- `github-full.json` - GitHub API full access
- `github-readonly.json` - GitHub read-only
- `slack-notify.json` - Slack notifications

**Description:** Skills package domain-specific expertise, workflows, and best practices into discoverable components that Hermes automatically uses when relevant.

---

### 04 - Delegation

Create specialized subagents that work in parallel on focused tasks.

**Installation:**
```bash
# Install delegation examples
cp -r 04-delegation/delegation-examples/* ~/.hermes/agents/
```

**Example Files:**
- `standard-providers.md` - Standard agent provider configurations

**Description:** Delegation is Hermes's core unique feature - the ability to create specialized subagents that work in parallel with their own context windows.

**Built-in Subagents:**
| Agent | Purpose |
|-------|---------|
| general-purpose | Complex multi-step tasks |
| Plan | Research for plan mode |
| Explore | Read-only codebase exploration |
| Bash | Terminal commands in isolated context |

---

### 05 - MCP (Model Context Protocol)

Connect Hermes to external tools, data sources, and services.

**Installation:**
```bash
# Install MCP server configurations
cp -r 05-mcp/mcp-examples/* ~/.hermes/mcp/
```

**Example Files:**
- `README.md` - MCP server overview
- `conversation-flows.md` - Flow patterns
- `error-handling.md` - Error handling strategies
- `response-formatters.md` - Output formatting

**Description:** MCP provides a standardized interface for connecting Hermes to external tools and services including filesystems, databases, APIs, and specialized CLIs.

**Server Management:**
| Task | Command |
|------|---------|
| Add server | `hermes mcp add <name> <command> [args]` |
| Remove server | `hermes mcp remove <name>` |
| List servers | `hermes mcp list` |
| Start server | `hermes mcp start <name>` |
| Stop server | `hermes mcp stop <name>` |

---

### 06 - Voice

Real-time voice interaction with Hermes.

**Installation:**
```bash
# Install voice configuration
cp 06-voice/voice-setup.md ~/.hermes/voice-config.md
```

**Description:** Voice Mode transforms Hermes into a spoken dialogue partner combining speech-to-text for input and text-to-speech for output.

**Setup Options:**
| Method | Description |
|--------|-------------|
| CLI | Direct voice in terminal |
| Telegram | Voice through Telegram bot |
| Discord | Voice through Discord bot |

**Related Files:**
- `voice-setup.md` - Audio device and backend configuration
- `voice-cli.md` - Command line voice interaction
- `voice-telegram.md` - Telegram voice integration
- `voice-discord.md` - Discord voice integration

---

### 07 - Messaging Gateway

Connect Hermes to Telegram, Discord, and Slack.

**Installation:**
```bash
# Install bot patterns for all platforms
cp -r 07-messaging-gateway/bot-patterns/* ~/.hermes/gateway/

# Set environment variables
export TELEGRAM_BOT_TOKEN=your_token
export DISCORD_BOT_TOKEN=your_token
export SLACK_BOT_TOKEN=your_token
```

**Bot Patterns Available:**
- `creative-partner.md` - Creative brainstorming patterns
- `debugging-buddy.md` - Debug assistance patterns
- `senior-reviewer.md` - Code review patterns
- `tech-mentor.md` - Technical guidance patterns

**Platform Support:**
| Platform | Setup Complexity | Max Message |
|----------|-----------------|-------------|
| Telegram | Low | 4096 chars |
| Discord | Medium | 2000 chars |
| Slack | Medium | 30000 chars |

**Configuration Files:**
- `telegram-setup.md` - Telegram bot setup
- `discord-setup.md` - Discord bot setup
- `slack-setup.md` - Slack bot setup

---

### 08 - Cron & Automation

Schedule automated tasks, webhook triggers, and recurring jobs.

**Installation:**
```bash
# Install cron job templates
cp -r 08-cron/cron-examples/* ~/.hermes/cron/
```

**Cron Examples Available:**
- `daily-project-summary.yaml` - Daily summary job
- `file-watch-trigger.yaml` - File change trigger
- `github-push-trigger.yaml` - GitHub push event
- `hourly-health-check.yaml` - Hourly health check
- `interval-backup.yaml` - Periodic backup
- `pr-review-trigger.yaml` - PR review trigger
- `weekly-report.yaml` - Weekly report generation

**Description:** Schedule recurring tasks using cron expressions. Supports time-based scheduling, webhook triggers, and event-driven automation.

**Common Cron Expressions:**
| Expression | Meaning |
|------------|---------|
| `0 * * * *` | Every hour |
| `0 9 * * *` | Daily at 9 AM |
| `0 9 * * 1-5` | Weekdays at 9 AM |
| `*/15 * * * *` | Every 15 minutes |

**Job Management:**
| Task | Command |
|------|---------|
| List jobs | `hermes cron list` |
| Add job | `hermes cron add <name> <schedule> <task>` |
| Remove job | `hermes cron remove <name>` |
| Run now | `hermes cron run <name>` |

---

### 09 - SOUL/Personality

Define Hermes's unique personality, communication style, and behavioral patterns.

**Installation:**
```bash
# Install personality templates
cp -r 09-soul-personality/personality-examples/* ~/.hermes/soul/

# Set as active personality
cp 09-soul-personality/personality-examples/tech-mentor.md ~/.hermes/soul/ACTIVE.md
```

**Personality Examples Available:**
- `code-reviewer.md` - Code review focused personality
- `debugger.md` - Debugging specialist personality
- `documentation-writer.md` - Technical writing personality
- `researcher.md` - Research focused personality
- `secure-reviewer.md` - Security focused personality
- `test-engineer.md` - Testing specialist personality

**Description:** SOUL (Systemic Operational Utility Layer) defines how Hermes thinks and communicates. It transforms generic AI responses into consistent, branded interactions.

**File Locations:**
| Type | Location |
|------|----------|
| User SOUL | `~/.hermes/soul/` |
| Project SOUL | `.hermes/SOUL.md` |

---

### 10 - Toolsets

Curated collections of related tools organized by capability domain.

**Installation:**
```bash
# Install toolset examples
cp -r 10-toolsets/toolset-examples/* ~/.hermes/toolsets/
```

**Toolset Examples Available:**
- `blog-draft/` - Blog drafting tools
- `brand-voice/` - Brand voice consistency tools
- `code-review/` - Code review tools (includes `code-review.md`)

**Description:** Toolsets group related tools into logical collections that can be enabled, disabled, or swapped as a unit.

**Built-in Toolsets:**
| Toolset | Description |
|---------|-------------|
| core | Essential tools (file, search, terminal) |
| git | Version control operations |
| docker | Container management |
| kubernetes | K8s cluster operations |
| cloud | Cloud provider CLIs |

**Toolset Management:**
| Task | Command |
|------|---------|
| List toolsets | `hermes toolset list` |
| Enable toolset | `hermes toolset enable <name>` |
| Disable toolset | `hermes toolset disable <name>` |
| Show tools | `hermes toolset show <name>` |

---

### 11 - Plugins

Extend Hermes with custom functionality through structured packages.

**Installation:**
```bash
# Install plugin examples
cp 11-plugins/plugin-examples/code-review-plugin.md ~/.hermes/plugins/

# Install from registry
hermes plugin install <plugin-name>
```

**Plugin Example:**
- `code-review-plugin.md` - Code review plugin configuration

**Description:** Plugins package tools, skills, and agent configurations together for distribution and reuse.

**Plugin Structure:**
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

**Plugin Management:**
| Task | Command |
|------|---------|
| List plugins | `hermes plugin list` |
| Install | `hermes plugin install <name>` |
| Uninstall | `hermes plugin uninstall <name>` |
| Enable | `hermes plugin enable <name>` |
| Disable | `hermes plugin disable <name>` |

---

### 12 - Checkpoints

Preserve conversation state at key moments for recovery, branching, and review.

**Installation:**
```bash
# Checkpoints are auto-enabled by default
# No installation needed - state is preserved automatically
```

**Description:** Checkpoints capture full conversation history, file system state, tool execution results, and agent context at specific moments.

**Checkpoint Types:**
| Type | Trigger | Retention |
|------|---------|-----------|
| Manual | User/agent request | Until explicitly deleted |
| Auto | Periodic or event | Configurable TTL |
| Branch | After branching | Preserved indefinitely |

**Checkpoint Management:**
| Task | Command |
|------|---------|
| Create checkpoint | `hermes checkpoint create [name]` |
| List checkpoints | `hermes checkpoint list` |
| Restore | `hermes checkpoint restore <id>` |
| Branch | `hermes checkpoint branch <id>` |
| Delete | `hermes checkpoint delete <id>` |

**File Locations:**
| Type | Location | Scope |
|------|---------|-------|
| Project checkpoints | `.hermes/checkpoints/` | Current project |
| User checkpoints | `~/.hermes/checkpoints/` | All projects |

---

### 13 - Providers

Configure backend AI services and switch between LLM backends.

**Installation:**
```bash
# Install provider configurations
cp 13-providers/provider-examples/standard-providers.md ~/.hermes/providers/
```

**Example Files:**
- `standard-providers.md` - Standard provider configurations

**Description:** Providers enable flexible switching between different LLM backends including Anthropic, OpenAI, Google, and self-hosted options.

**Supported Providers:**
| Provider | Context Window | Multimodal | Function Calling |
|----------|---------------|------------|------------------|
| Anthropic | 200K | Yes | Yes |
| OpenAI | 128K | Yes | Yes |
| Google | 32K | Yes | Yes |
| Ollama | Varies | Varies | Limited |

**Provider Management:**
| Task | Command |
|------|---------|
| List providers | `hermes provider list` |
| Show config | `hermes provider show <name>` |
| Set default | `hermes provider default <name>` |
| Test connection | `hermes provider test <name>` |

**File Locations:**
| Type | Location | Scope |
|------|---------|-------|
| Project providers | `.hermes/providers/` | Current project |
| User providers | `~/.hermes/providers/` | All projects |

---

### 14 - Context Refs

Reference external content - files, URLs, documentation - directly within prompts.

**Installation:**
```bash
# Install context ref examples
cp -r 14-context-refs/context-ref-examples/* ~/.hermes/context-refs/
```

**Example Files:**
- `ref-usage-examples.md` - Reference usage patterns

**Description:** Context refs enable referencing external content directly in prompts for targeted, grounded responses, reducing hallucination by providing authoritative source material.

**Reference Types:**
| Type | Syntax | Use Case |
|------|--------|----------|
| File | `file://path/to/file` | Local source files |
| URL | `https://example.com` | Web content |
| Section | `file://path#L5-L15` | Specific lines |
| Function | `file://path#function-name` | Code definitions |

**Context Ref Management:**
| Task | Command |
|------|---------|
| List refs | `hermes ref list` |
| Add ref | `hermes ref add <name> <target>` |
| Remove ref | `hermes ref remove <name>` |
| Refresh | `hermes ref refresh <name>` |

**File Locations:**
| Type | Location | Scope |
|------|---------|-------|
| Project refs | `.hermes/refs/` | Current project |
| User refs | `~/.hermes/refs/` | All projects |

---

## Hermes Agent CLI Reference

| Command | Description |
|---------|-------------|
| `hermes --version` | Check installed version |
| `hermes doctor` | Diagnose configuration issues |
| `hermes model` | Switch between AI models |
| `hermes model list` | List available models |
| `hermes tools` | Configure available tools |
| `hermes tools list` | Show installed tools |
| `hermes gateway` | Messaging gateway commands |
| `hermes setup` | Run full setup wizard |
| `hermes help` | Show help and available commands |

### Global Flags

| Flag | Description |
|------|-------------|
| `--verbose` | Enable verbose output |
| `--config <path>` | Use specific config file |
| `--project <path>` | Set project directory |
| `--model <name>` | Specify model to use |

### Environment Variables

| Variable | Description |
|----------|-------------|
| `HERMES_CONFIG` | Path to config file |
| `HERMES_PROJECT` | Default project path |
| `HERMES_MODEL` | Default model |
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |

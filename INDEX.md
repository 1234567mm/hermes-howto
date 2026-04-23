# Hermes Agent Examples - Complete Index

This document provides a complete index of all example files organized by feature type.

## Summary Statistics

- **Total Files**: 100+ files
- **Categories**: 14 feature categories
- **Plugins**: 3 complete plugins
- **Skills**: 6 complete skills
- **Delegation Templates**: 5 templates
- **Ready to Use**: All examples

---

## 01. Quickstart (5 files)

Getting started with Hermes Agent.

| File | Description | Use Case |
|------|-------------|----------|
| `setup.md` | Initial setup guide | First-time configuration |
| `first-conversation.md` | Basic interaction | Learning the interface |
| `configuration.md` | Core settings | Environment setup |
| `quick-commands.md` | Essential commands | Productivity shortcuts |
| `README.md` | Documentation | Setup and usage guide |

**Installation Path**: Project root

**Usage**: Follow the setup sequence in order

---

## 02. Memory (6 files)

Persistent context and project standards.

| File | Description | Scope | Location |
|------|-------------|-------|----------|
| `project-HERMES.md` | Team project standards | Project-wide | `./HERMES.md` |
| `directory-api-HERMES.md` | API-specific rules | Directory | `./src/api/HERMES.md` |
| `personal-HERMES.md` | Personal preferences | User | `~/.hermes/HERMES.md` |
| `memory-saved.png` | Screenshot: memory saved | - | Visual reference |
| `memory-ask-hermes.png` | Screenshot: ask Hermes | - | Visual reference |
| `README.md` | Documentation | - | Reference |

**Installation**: Copy to appropriate location

**Usage**: Automatically loaded by Hermes

---

## 03. Skills (28 files)

Auto-invoked capabilities with scripts and templates.

### Code Review Skill (5 files)
```
code-review/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-metrics.py            # Code metrics analyzer
│   └── compare-complexity.py         # Complexity comparison
└── templates/
    ├── review-checklist.md           # Review checklist
    └── finding-template.md           # Finding documentation
```

**Purpose**: Comprehensive code review with security, performance, and quality analysis

**Auto-invoked**: When reviewing code

---

### Documentation Generator Skill (2 files)
```
doc-generator/
├── SKILL.md                          # Skill definition
└── generate-docs.py                  # Python doc extractor
```

**Purpose**: Generate comprehensive documentation from source code

**Auto-invoked**: When creating/updating documentation

---

### Customer Service Skill (4 files)
```
customer-service/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── response-template.py          # Response generator
│   └── sentiment-analysis.py         # Sentiment analyzer
└── templates/
    ├── ticket-template.md            # Support ticket format
    └── escalation-template.md        # Escalation format
```

**Purpose**: Handle customer inquiries with consistent responses

**Auto-invoked**: When handling support requests

---

### Refactor Skill (5 files)
```
refactor/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-complexity.py         # Complexity analyzer
│   └── detect-smells.py              # Code smell detector
├── references/
│   ├── code-smells.md                # Code smells catalog
│   └── refactoring-catalog.md        # Refactoring patterns
└── templates/
    └── refactoring-plan.md           # Refactoring plan template
```

**Purpose**: Systematic code refactoring with complexity analysis

**Auto-invoked**: When refactoring code

---

### Hermes MD Skill (1 file)
```
hermes-md/
└── SKILL.md                          # Skill definition
```

**Purpose**: Manage and optimize HERMES.md files

---

### Blog Draft Skill (3 files)
```
blog-draft/
├── SKILL.md                          # Skill definition
└── templates/
    ├── draft-template.md             # Blog draft template
    └── outline-template.md           # Blog outline template
```

**Purpose**: Draft content with consistent structure

**Plus**: `README.md` - Skills overview and usage guide

**Installation Path**: `~/.hermes/skills/` or `.hermes/skills/`

---

## 04. Delegation (9 files)

Task delegation to specialized agents.

| File | Description | Tools | Use Case |
|------|-------------|-------|----------|
| `code-reviewer.md` | Code quality analysis | read, grep, diff | Comprehensive reviews |
| `test-engineer.md` | Test coverage analysis | read, write, bash | Test automation |
| `documentation-writer.md` | Documentation creation | read, write, grep | Doc generation |
| `security-reviewer.md` | Security review (read-only) | read, grep | Security audits |
| `implementation-agent.md` | Full implementation | read, write, bash, grep, edit, glob | Feature development |
| `debugger.md` | Debugging specialist | read, bash, grep | Bug investigation |
| `data-scientist.md` | Data analysis specialist | read, write, bash | Data workflows |
| `clean-code-reviewer.md` | Clean code standards | read, grep | Code quality |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.hermes/delegation/`

**Usage**: Automatically delegated by main agent

---

## 05. MCP Protocol (5 files)

External tool and API integrations.

| File | Description | Integrates With | Use Case |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub integration | GitHub API | PR/issue management |
| `database-mcp.json` | Database queries | PostgreSQL/MySQL | Live data queries |
| `filesystem-mcp.json` | File operations | Local filesystem | File management |
| `multi-mcp.json` | Multiple servers | GitHub + DB + Slack | Complete integration |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.mcp.json` (project scope) or `~/.hermes.json` (user scope)

**Usage**: Tools are automatically available once configured

---

## 06. Voice (5 files)

Voice interaction capabilities.

| File | Description | Use Case |
|------|-------------|----------|
| `voice-config.md` | Voice settings | Configuration guide |
| `speech-to-text.md` | Speech recognition | Voice input handling |
| `text-to-speech.md` | Speech synthesis | Voice output |
| `voice-commands.md` | Voice shortcuts | Voice-controlled actions |
| `README.md` | Documentation | Setup and usage guide |

**Installation**: Configure in `~/.hermes/settings.json`

**Usage**: Voice commands and dictation

---

## 07. Messaging Gateway (8 files)

Messaging platform integrations.

| File | Description | Platform | Use Case |
|------|-------------|----------|----------|
| `slack-integration.md` | Slack bot setup | Slack | Team communication |
| `discord-integration.md` | Discord bot setup | Discord | Community engagement |
| `telegram-integration.md` | Telegram bot setup | Telegram | Direct messaging |
| `webhook-config.md` | Webhook handlers | Multiple | Event-driven |
| `message-templates.md` | Response templates | All | Consistent messaging |
| `channel-routing.md` | Route by channel | Multiple | Smart routing |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation**: Configure in `~/.hermes/messaging.json`

**Usage**: Multi-platform messaging automation

---

## 08. Cron (5 files)

Scheduled task automation.

| File | Description | Use Case |
|------|-------------|----------|
| `cron-setup.md` | Cron configuration | Initial setup |
| `scheduled-tasks.md` | Task definitions | Recurring automation |
| `cron-expressions.md` | Expression syntax | Time scheduling |
| `monitoring-cron.md` | Health checks | Scheduled monitoring |
| `README.md` | Documentation | Setup and usage guide |

**Installation**: Configure in `~/.hermes/cron.json`

**Usage**: Automatic scheduled execution

---

## 09. SOUL/Personality (6 files)

Agent personality configuration.

| File | Description | Use Case |
|------|-------------|----------|
| `personality-config.md` | Personality settings | Custom behavior |
| `tone-settings.md` | Tone adjustments | Communication style |
| `response-templates.md` | Response patterns | Consistent output |
| `behavior-rules.md` | Behavior configuration | Decision making |
| `custom-personality.md` | Create personality | Brand voice |
| `README.md` | Documentation | Setup and usage guide |

**Installation**: Configure in `~/.hermes/personality.json`

**Usage**: Customize agent behavior and communication

---

## 10. Toolsets (6 files)

Tool collections for extended capabilities.

| File | Description | Tools Included |
|------|-------------|----------------|
| `web-tools.md` | Web scraping tools | fetch, parse, extract |
| `file-tools.md` | File operations | read, write, glob, grep |
| `api-tools.md` | API utilities | request, auth, parse |
| `data-tools.md` | Data processing | transform, filter, aggregate |
| `custom-toolset.md` | Create toolset | Build your own |
| `README.md` | Documentation | Setup and usage guide |

**Installation**: Configure in `~/.hermes/toolsets.json`

**Usage**: Extended capabilities on demand

---

## 11. Plugins (3 complete plugins, 40 files)

Bundled collections of features.

### PR Review Plugin (10 files)
```
pr-review/
├── .hermes-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── review-pr.md                  # Comprehensive review
│   ├── check-security.md            # Security check
│   └── check-tests.md               # Test coverage check
├── agents/
│   ├── security-reviewer.md         # Security specialist
│   ├── test-checker.md              # Test specialist
│   └── performance-analyzer.md      # Performance specialist
├── mcp/
│   └── github-config.json           # GitHub integration
└── README.md                        # Plugin documentation
```

**Features**: Security analysis, test coverage, performance impact

**Commands**: Contextual commands activated by plugin

**Installation**: `hermes plugin install pr-review`

---

### DevOps Automation Plugin (15 files)
```
devops-automation/
├── .hermes-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── deploy.md                    # Deployment
│   ├── rollback.md                  # Rollback
│   ├── status.md                    # System status
│   └── incident.md                  # Incident response
├── agents/
│   ├── deployment-specialist.md     # Deployment expert
│   ├── incident-commander.md       # Incident coordinator
│   └── alert-analyzer.md           # Alert analyzer
├── mcp/
│   └── kubernetes-config.json      # Kubernetes integration
└── README.md                        # Plugin documentation
```

**Features**: Kubernetes deployment, rollback, monitoring, incident response

**Installation**: `hermes plugin install devops-automation`

---

### Customer Service Plugin (14 files)
```
customer-service/
├── .hermes-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── handle-ticket.md            # Ticket handling
│   ├── escalate.md                 # Escalation
│   ├── summarize.md                # Conversation summary
│   └── follow-up.md                # Follow-up actions
├── skills/
│   ├── response-generator/         # Response generation
│   └── sentiment-analyzer/         # Sentiment analysis
├── messaging/
│   └── gateway-config.json         # Multi-platform setup
└── README.md                        # Plugin documentation
```

**Features**: Ticket handling, multi-platform messaging, sentiment analysis

**Installation**: `hermes plugin install customer-service`

**Plus**: `README.md` - Plugins overview and usage guide

---

## 12. Checkpoints (2 files)

Save conversation state and explore alternative approaches.

| File | Description | Content |
|------|-------------|---------|
| `README.md` | Documentation | Comprehensive checkpoint guide |
| `checkpoint-examples.md` | Real-world examples | Database migration, performance optimization, UI iteration, debugging |

**Key Concepts**:
- **Checkpoint**: Snapshot of conversation state
- **Rewind**: Return to previous checkpoint
- **Branch Point**: Explore multiple approaches

**Usage**: Checkpoints are created automatically with every user prompt

---

## 13. Providers (5 files)

AI provider configuration.

| File | Description | Use Case |
|------|-------------|----------|
| `openai-config.md` | OpenAI integration | GPT models |
| `anthropic-config.md` | Anthropic integration | Claude models |
| `local-provider.md` | Local model setup | Self-hosted |
| `multi-provider.md` | Multiple providers | Fallback routing |
| `README.md` | Documentation | Setup and usage guide |

**Installation**: Configure in `~/.hermes/providers.json`

**Usage**: Select and configure AI backends

---

## 14. Context Refs (4 files)

Dynamic context references.

| File | Description | Use Case |
|------|-------------|----------|
| `context-injection.md` | Inject context | Dynamic data |
| `context-templates.md` | Template context | Structured prompts |
| `context-priority.md` | Priority handling | Important context first |
| `README.md` | Documentation | Setup and usage guide |

**Installation**: Configure in `~/.hermes/context-refs.json`

**Usage**: Automatic context injection per request

---

## Documentation Files (15 files)

| File | Location | Description |
|------|----------|-------------|
| `README.md` | `/` | Main examples overview |
| `INDEX.md` | `/` | This complete index |
| `QUICK_REFERENCE.md` | `/` | Quick reference card |
| `LEARNING-ROADMAP.md` | `/` | Guided learning path |
| `README.md` | `/01-quickstart/` | Quickstart guide |
| `README.md` | `/02-memory/` | Memory guide |
| `README.md` | `/03-skills/` | Skills guide |
| `README.md` | `/04-delegation/` | Delegation guide |
| `README.md` | `/05-mcp/` | MCP guide |
| `README.md` | `/06-voice/` | Voice guide |
| `README.md` | `/07-messaging-gateway/` | Messaging guide |
| `README.md` | `/08-cron/` | Cron guide |
| `README.md` | `/09-soul-personality/` | Personality guide |
| `README.md` | `/10-toolsets/` | Toolsets guide |
| `README.md` | `/11-plugins/` | Plugins guide |
| `README.md` | `/12-checkpoints/` | Checkpoints guide |
| `README.md` | `/13-providers/` | Providers guide |
| `README.md` | `/14-context-refs/` | Context refs guide |

---

## Complete File Tree

```
hermes-howto/
├── README.md                                    # Main overview
├── INDEX.md                                      # This file
├── QUICK_REFERENCE.md                           # Quick reference card
├── LEARNING-ROADMAP.md                           # Learning path
├── CLAUDE.md                                    # Claude Code guidance
│
├── 01-quickstart/                               # Quickstart
│   ├── setup.md
│   ├── first-conversation.md
│   ├── configuration.md
│   ├── quick-commands.md
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-HERMES.md
│   ├── directory-api-HERMES.md
│   ├── personal-HERMES.md
│   ├── memory-saved.png
│   ├── memory-ask-hermes.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   ├── doc-generator/
│   ├── customer-service/
│   ├── refactor/
│   ├── hermes-md/
│   ├── blog-draft/
│   └── README.md
│
├── 04-delegation/                               # Delegation
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── security-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-voice/                                    # Voice
│   ├── voice-config.md
│   ├── speech-to-text.md
│   ├── text-to-speech.md
│   ├── voice-commands.md
│   └── README.md
│
├── 07-messaging-gateway/                        # Messaging Gateway
│   ├── slack-integration.md
│   ├── discord-integration.md
│   ├── telegram-integration.md
│   ├── webhook-config.md
│   ├── message-templates.md
│   ├── channel-routing.md
│   └── README.md
│
├── 08-cron/                                     # Cron
│   ├── cron-setup.md
│   ├── scheduled-tasks.md
│   ├── cron-expressions.md
│   ├── monitoring-cron.md
│   └── README.md
│
├── 09-soul-personality/                         # SOUL/Personality
│   ├── personality-config.md
│   ├── tone-settings.md
│   ├── response-templates.md
│   ├── behavior-rules.md
│   ├── custom-personality.md
│   └── README.md
│
├── 10-toolsets/                                 # Toolsets
│   ├── web-tools.md
│   ├── file-tools.md
│   ├── api-tools.md
│   ├── data-tools.md
│   ├── custom-toolset.md
│   └── README.md
│
├── 11-plugins/                                  # Plugins
│   ├── pr-review/
│   ├── devops-automation/
│   ├── customer-service/
│   └── README.md
│
├── 12-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 13-providers/                                # Providers
│   ├── openai-config.md
│   ├── anthropic-config.md
│   ├── local-provider.md
│   ├── multi-provider.md
│   └── README.md
│
├── 14-context-refs/                             # Context Refs
│   ├── context-injection.md
│   ├── context-templates.md
│   ├── context-priority.md
│   └── README.md
│
└── scripts/                                     # Build and validation
    ├── build_epub.py
    ├── check_cross_references.py
    ├── check_links.py
    ├── check_mermaid.py
    └── tests/
```

---

## Feature Categories Summary

| Category | Files | Description |
|----------|-------|-------------|
| Quickstart | 5 | Getting started |
| Memory | 6 | Persistent context |
| Skills | 28 | Auto-invoked capabilities |
| Delegation | 9 | Task distribution |
| MCP | 5 | External integrations |
| Voice | 5 | Voice interaction |
| Messaging Gateway | 8 | Platform integrations |
| Cron | 5 | Scheduled tasks |
| SOUL/Personality | 6 | Agent personality |
| Toolsets | 6 | Tool collections |
| Plugins | 40+ | Bundled solutions |
| Checkpoints | 2 | Session snapshots |
| Providers | 5 | AI backend config |
| Context Refs | 4 | Dynamic context |

**Total**: 100+ files across 14 categories

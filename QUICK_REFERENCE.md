# Hermes Agent Examples - Quick Reference Card

## Installation Quick Commands

### Quickstart
```bash
# Initial setup
# Follow 01-quickstart/setup.md

# Verify installation
hermes --version
```

### Memory
```bash
# Project memory
cp 02-memory/project-HERMES.md ./HERMES.md

# Personal memory
cp 02-memory/personal-HERMES.md ~/.hermes/HERMES.md
```

### Skills
```bash
# Personal skills
cp -r 03-skills/code-review ~/.hermes/skills/

# Project skills
cp -r 03-skills/code-review .hermes/skills/
```

### Delegation
```bash
# Install all
cp -r 04-delegation/* ~/.hermes/delegation/

# Install specific
cp 04-delegation/code-reviewer.md ~/.hermes/delegation/
```

### MCP
```bash
# Set credentials
export GITHUB_TOKEN="***"
export DATABASE_URL="postgresql://..."

# Install config (project scope)
cp 05-mcp/github-mcp.json .mcp.json

# Or user scope: add to ~/.hermes.json
```

### Voice
```bash
# Configure voice settings
cp 06-voice/voice-config.md ~/.hermes/voice.json

# Configure speech-to-text
cp 06-voice/speech-to-text.md ~/.hermes/stt.json

# Configure text-to-speech
cp 06-voice/text-to-speech.md ~/.hermes/tts.json
```

### Messaging Gateway
```bash
# Slack integration
cp 07-messaging-gateway/slack-integration.md ~/.hermes/messaging/slack.json

# Discord integration
cp 07-messaging-gateway/discord-integration.md ~/.hermes/messaging/discord.json

# Telegram integration
cp 07-messaging-gateway/telegram-integration.md ~/.hermes/messaging/telegram.json

# Configure routing
cp 07-messaging-gateway/channel-routing.md ~/.hermes/messaging/routing.json
```

### Cron
```bash
# Install scheduled tasks
cp 08-cron/scheduled-tasks.json ~/.hermes/cron.json

# Configure monitoring
cp 08-cron/monitoring-cron.md ~/.hermes/cron-monitor.json
```

### SOUL/Personality
```bash
# Configure personality
cp 09-soul-personality/personality-config.md ~/.hermes/personality.json

# Customize tone
cp 09-soul-personality/tone-settings.md ~/.hermes/tone.json

# Create custom personality
cp 09-soul-personality/custom-personality.md ~/.hermes/my-personality.json
```

### Toolsets
```bash
# Install toolsets
cp 10-toolsets/web-tools.md ~/.hermes/toolsets/web.json
cp 10-toolsets/file-tools.md ~/.hermes/toolsets/file.json
cp 10-toolsets/api-tools.md ~/.hermes/toolsets/api.json
```

### Plugins
```bash
# Install from examples
hermes plugin install pr-review
hermes plugin install devops-automation
hermes plugin install customer-service
```

### Checkpoints
```bash
# Checkpoints are created automatically with every user prompt
# To rewind, use:
/checkpoint list
/rewind <checkpoint-id>

# Or use the checkpoint menu
```

### Providers
```bash
# Configure providers
cp 13-providers/openai-config.md ~/.hermes/providers/openai.json
cp 13-providers/anthropic-config.md ~/.hermes/providers/anthropic.json

# Multi-provider setup
cp 13-providers/multi-provider.md ~/.hermes/providers.json
```

### Context Refs
```bash
# Configure context injection
cp 14-context-refs/context-injection.md ~/.hermes/context-refs.json

# Configure templates
cp 14-context-refs/context-templates.md ~/.hermes/context-templates.json
```

---

## Feature Cheat Sheet

| Feature | Install Path | Usage |
|---------|-------------|-------|
| Skills | `.hermes/skills/*/SKILL.md` | Auto-invoked |
| Delegation | `.hermes/delegation/*.md` | Auto-delegated |
| Memory | `./HERMES.md` | Auto-loaded |
| MCP | `.mcp.json` (project) or `~/.hermes.json` (user) | Real-time data |
| Voice | `~/.hermes/voice.json` | Voice commands |
| Messaging Gateway | `~/.hermes/messaging/*.json` | Multi-platform |
| Cron | `~/.hermes/cron.json` | Scheduled tasks |
| SOUL/Personality | `~/.hermes/personality.json` | Custom behavior |
| Toolsets | `~/.hermes/toolsets/*.json` | Extended tools |
| Plugins | Via `hermes plugin install` | Bundles all |
| Checkpoints | Built-in | Safe exploration |
| Providers | `~/.hermes/providers.json` | AI backend |
| Context Refs | `~/.hermes/context-refs.json` | Dynamic context |

---

## Common Use Cases

### Customer Service Bot
```bash
# Complete plugin
hermes plugin install customer-service

# Configure messaging
cp 07-messaging-gateway/* ~/.hermes/messaging/

# Configure voice
cp 06-voice/voice-config.md ~/.hermes/voice.json

# Set up skills
cp -r 03-skills/customer-service ~/.hermes/skills/
```

### DevOps Automation
```bash
# Complete plugin
hermes plugin install devops-automation

# Commands: contextual automation

# Set up monitoring
cp 08-cron/monitoring-cron.md ~/.hermes/cron-monitor.json

# Configure MCP
cp 05-mcp/kubernetes-config.json ~/.hermes/mcp/k8s.json
```

### Voice Assistant
```bash
# Configure voice
cp 06-voice/voice-config.md ~/.hermes/voice.json
cp 06-voice/speech-to-text.md ~/.hermes/stt.json
cp 06-voice/text-to-speech.md ~/.hermes/tts.json

# Set up personality
cp 09-soul-personality/custom-personality.md ~/.hermes/my-voice.json

# Add toolsets
cp 10-toolsets/web-tools.md ~/.hermes/toolsets/
```

### Scheduled Monitoring
```bash
# Set up cron
cp 08-cron/scheduled-tasks.json ~/.hermes/cron.json
cp 08-cron/monitoring-cron.md ~/.hermes/monitoring.json

# Configure delegation
cp -r 04-delegation/monitoring-* ~/.hermes/delegation/

# Set up checkpoints
# Auto-enabled for safe experimentation
```

### Multi-Platform Messaging
```bash
# Configure all platforms
cp 07-messaging-gateway/slack-integration.md ~/.hermes/messaging/slack.json
cp 07-messaging-gateway/discord-integration.md ~/.hermes/messaging/discord.json
cp 07-messaging-gateway/telegram-integration.md ~/.hermes/messaging/telegram.json

# Configure routing
cp 07-messaging-gateway/channel-routing.md ~/.hermes/messaging/routing.json

# Message templates
cp 07-messaging-gateway/message-templates.md ~/.hermes/messaging/templates/
```

---

## File Locations Reference

```
Your Project/
├── .hermes/
│   ├── skills/                # Skills go here
│   ├── delegation/            # Delegation templates
│   ├── settings.json          # Project settings
│   └── plugins/               # Project plugins
├── .mcp.json                  # MCP configuration (project scope)
├── HERMES.md                  # Project memory
└── src/
    └── api/
        └── HERMES.md          # Directory-specific memory

User Home/
├── .hermes/
│   ├── skills/                # Personal skills
│   ├── delegation/            # Personal delegation templates
│   ├── hooks/                 # Hook scripts
│   ├── voice.json             # Voice configuration
│   ├── messaging/             # Messaging configurations
│   ├── cron.json              # Scheduled tasks
│   ├── personality.json       # Personality config
│   ├── toolsets/              # Tool collections
│   ├── providers.json         # AI providers
│   ├── context-refs.json      # Context references
│   ├── settings.json          # User settings
│   └── HERMES.md              # Personal memory
└── .hermes.json               # User MCP config (user scope)
```

---

## Finding Examples

### By Category
- Quickstart: `01-quickstart/`
- Memory: `02-memory/`
- Skills: `03-skills/`
- Delegation: `04-delegation/`
- MCP: `05-mcp/`
- Voice: `06-voice/`
- Messaging: `07-messaging-gateway/`
- Cron: `08-cron/`
- Personality: `09-soul-personality/`
- Toolsets: `10-toolsets/`
- Plugins: `11-plugins/`
- Checkpoints: `12-checkpoints/`
- Providers: `13-providers/`
- Context Refs: `14-context-refs/`

### By Complexity
- Simple: Quickstart, Memory
- Medium: Skills, Delegation, Cron, Checkpoints
- Advanced: MCP, Voice, Messaging, Personality, Toolsets
- Complete: Plugins, Providers, Context Refs

---

## Learning Path

### Day 1
```bash
# Read overview
cat README.md

# Initial setup
# Follow 01-quickstart/setup.md

# Verify
hermes --version
```

### Day 2-3
```bash
# Set up memory
cp 02-memory/project-HERMES.md ./HERMES.md
vim HERMES.md

# Install skills
cp -r 03-skills/* ~/.hermes/skills/
```

### Day 4-5
```bash
# Set up delegation
cp -r 04-delegation/* ~/.hermes/delegation/

# Configure MCP
export GITHUB_TOKEN="***"
cp 05-mcp/github-mcp.json ~/.hermes/mcp.json
```

### Week 2
```bash
# Set up voice
cp 06-voice/voice-config.md ~/.hermes/voice.json

# Configure messaging
cp 07-messaging-gateway/slack-integration.md ~/.hermes/messaging/slack.json

# Set up cron
cp 08-cron/scheduled-tasks.json ~/.hermes/cron.json
```

### Week 3+
```bash
# Customize personality
cp 09-soul-personality/custom-personality.md ~/.hermes/my-brand.json

# Install toolsets
cp 10-toolsets/web-tools.md ~/.hermes/toolsets/web.json

# Install complete plugin
hermes plugin install pr-review
```

---

## CLI Reference

### Basic Commands
```bash
hermes                    # Start interactive session
hermes --version          # Show version
hermes --help             # Show help
```

### Configuration Commands
```bash
hermes config show        # Show current config
hermes config set <key> <value>  # Set config value
hermes plugins list       # List installed plugins
hermes plugins install <name>    # Install plugin
```

### Session Commands
```bash
hermes checkpoint list    # List checkpoints
hermes checkpoint save <name>    # Save checkpoint
hermes rewind <id>        # Rewind to checkpoint
```

### Provider Commands
```bash
hermes provider list      # List providers
hermes provider add <name> # Add provider
hermes provider set-default <name>  # Set default
```

---

## Tips & Tricks

### Customization
- Start with examples as-is
- Modify to fit your needs
- Test before sharing with team
- Version control your configurations

### Best Practices
- Use memory for team standards
- Use delegation for complex tasks
- Use plugins for complete workflows
- Use cron for recurring tasks
- Use voice for hands-free workflows

### Troubleshooting
```bash
# Check file locations
ls -la ~/.hermes/skills/
ls -la ~/.hermes/delegation/

# Verify YAML syntax
head -20 ~/.hermes/delegation/code-reviewer.md

# Test MCP connection
echo $GITHUB_TOKEN

# Check voice config
hermes voice test

# Verify cron syntax
hermes cron validate
```

---

## Feature Matrix

| Need | Use This | Example |
|------|----------|---------|
| Auto workflow | Skills | `03-skills/code-review/` |
| Task distribution | Delegation | `04-delegation/code-reviewer.md` |
| Team standards | Memory | `02-memory/project-HERMES.md` |
| External data | MCP | `05-mcp/github-mcp.json` |
| Hands-free | Voice | `06-voice/voice-config.md` |
| Multi-platform | Messaging Gateway | `07-messaging-gateway/slack-integration.md` |
| Recurring tasks | Cron | `08-cron/scheduled-tasks.md` |
| Custom behavior | SOUL/Personality | `09-soul-personality/custom-personality.md` |
| Extended tools | Toolsets | `10-toolsets/web-tools.md` |
| Complete solution | Plugins | `11-plugins/pr-review/` |
| Safe experiment | Checkpoints | `12-checkpoints/README.md` |
| Model flexibility | Providers | `13-providers/multi-provider.md` |
| Dynamic context | Context Refs | `14-context-refs/context-injection.md` |

---

## Quick Links

- Main Guide: `README.md`
- Complete Index: `INDEX.md`
- Learning Path: `LEARNING-ROADMAP.md`
- Claude Code Guidance: `CLAUDE.md`

---

## Common Questions

**Q: Which should I use first?**
A: Start with Quickstart, then Memory and Skills.

**Q: Can I mix features?**
A: Yes! They work together. Memory + Skills + Delegation = powerful.

**Q: How do I share with team?**
A: Commit `.hermes/` directory to git.

**Q: What about secrets?**
A: Use environment variables, never hardcode.

**Q: Can I modify examples?**
A: Absolutely! They're templates to customize.

---

## Checklist

Getting started checklist:

- [ ] Read `README.md`
- [ ] Complete quickstart setup
- [ ] Install 1 skill
- [ ] Set up project `HERMES.md`
- [ ] Install 1 delegation template
- [ ] Configure 1 MCP integration
- [ ] Set up voice (optional)
- [ ] Configure messaging (optional)
- [ ] Try a complete plugin
- [ ] Customize for your needs
- [ ] Share with team

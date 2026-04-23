# Plugin Format

Plugins are distributed packages that extend Hermes with tools, skills, and agent configurations.

## Structure

```
plugin-name/
├── PLUGIN.md              # Required: Plugin manifest
├── skills/                # Optional: Skill definitions
│   └── skill-name/
│       └── SKILL.md
├── tools/                 # Optional: Tool definitions
│   └── tool-name.md
└── agents/                # Optional: Agent configurations
    └── agent-name.md
```

## PLUGIN.md Manifest

```markdown
---
name: my-plugin
version: 1.0.0
description: A useful Hermes plugin
author: Your Name
homepage: https://example.com
license: MIT
enabled: true
requires:
  - other-plugin>=2.0.0
skills:
  - ./skills/my-skill
tools:
  - ./tools/my-tool
agents:
  - ./agents/my-agent
---
```

## Manifest Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique plugin identifier |
| `version` | string | Yes | Semantic version |
| `description` | string | Yes | Plugin purpose |
| `author` | string | No | Author information |
| `homepage` | string | No | Project URL |
| `license` | string | No | License type |
| `enabled` | boolean | No | Default enabled state |
| `requires` | array | No | Plugin dependencies |

## Examples

### Minimal Plugin

```markdown
---
name: minimal-plugin
version: 1.0.0
description: A minimal plugin example
---
# Minimal Plugin

This plugin does one simple thing.
```

### Full Plugin

```
---
name: code-review-plugin
version: 2.1.0
description: Comprehensive code review capabilities
author: Team
license: Apache-2.0
enabled: true
requires:
  - git-tools>=1.0.0
skills:
  - ./skills/code-review
  - ./skills/security-scan
tools:
  - ./tools/linter
  - ./tools/coverage
agents:
  - ./agents/reviewer
---
```

### Multi-Platform Plugin

```markdown
---
name: cross-platform-dev
version: 1.0.0
description: Development tools for multiple platforms
platforms:
  - linux
  - macos
  - windows
tools:
  - ./tools/linux-build
  - ./tools/macos-build
  - ./tools/windows-build
---
```

## Plugin Lifecycle

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Install  │ ──► │ Enable   │ ──► │ Active   │
└──────────┘     └──────────┘     └──────────┘
                    │                  │
                    ▼                  ▼
               ┌──────────┐     ┌──────────┐
               │ Disable  │ ──► │ Inactive │
               └──────────┘     └──────────┘
                    │
                    ▼
               ┌──────────┐
               │ Uninstall│
               └──────────┘
```

## Validation

Validate plugin structure:

```
plugin validate ./path/to/plugin
```

Checks:
- Manifest syntax and required fields
- Referenced files exist
- Version format is valid semver
- Dependencies are available
- Skills/tools/agents are valid

## Best Practices

1. **Version pinning** — Specify version constraints for dependencies
2. **Clear descriptions** — Help users understand plugin purpose
3. **Platform targeting** — Use `platforms` field for OS-specific plugins
4. **Idempotent enabling** — Plugin should enable cleanly multiple times

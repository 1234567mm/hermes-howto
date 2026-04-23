<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Configuration

Customize Claude Code for your workflow.

## Configuration File

Claude Code stores settings in `.claude/settings.json`:

```bash
# View current config
claude /config
```

### Default Location

| Environment | Path |
|-------------|------|
| Project | `.claude/settings.json` |
| Home | `~/.claude/settings.json` |

## Essential Settings

### Model Selection

```json
{
  "model": "opus-4.7"
}
```

Available models:

| Model | Best For | Speed |
|-------|----------|-------|
| `opus-4.7` | Complex tasks, code generation | Slowest |
| `sonnet-4.6` | Balance of speed and quality | Medium |
| `haiku-4` | Quick tasks, simple edits | Fastest |

### Theme

```json
{
  "theme": "dark"
}
```

Options: `dark`, `light`, `system`

### Permission Level

```json
{
  "permissions": {
    "allowBash": "all",
    "allowWrite": "/Ask",
    "allowNetwork": "all"
  }
}
```

## Claude.md Project Context

Create a `CLAUDE.md` file in your project root to provide context:

```bash
# Initialize
claude /init
```

### Example CLAUDE.md

```markdown
# Project Overview

This is a Python web API using FastAPI.

## Key Files

- `src/main.py` - API entry point
- `src/routes/` - Route handlers
- `tests/` - Test files

## Conventions

- Use type hints on all functions
- Format with `ruff`
- Run tests with `pytest`

## Commands

- Start: `uvicorn src.main:app`
- Test: `pytest`
- Lint: `ruff check`
```

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `CLAUDE_CODE_MODEL` | Default model | `sonnet-4-20250514` |
| `CLAUDE_CODE_PERMISSIONS` | Permission mode | `Ask` |
| `CLAUDE_CODE_THEME` | Color theme | `dark` |
| `EDITOR` | External editor | `vim` |

### Setting Variables

```bash
# Linux/macOS
export CLAUDE_CODE_MODEL=opus-4.7

# Windows (WSL)
export CLAUDE_CODE_MODEL=opus-4.7
```

## Allowed Tools

Control which tools Claude can use without asking:

```json
{
  "permissions": {
    "allowBash": "all",
    "allowBashNames": ["git *", "npm *", "uv *"],
    "allowWrite": "tracked",
    "allowNetwork": "Ask"
  }
}
```

Permission levels:

| Level | Description |
|-------|-------------|
| `all` | Always allowed |
| `Ask` | Always ask |
| `tracked` | Only tracked files |
| `none` | Never allowed |

## API Configuration

### Use Claude API Key

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

### Use Different Endpoint

```json
{
  "apiKey": "sk-ant-...",
  "baseURL": "https://api.anthropic.com"
}
```

## Git Integration

### Auto-commit Settings

```json
{
  "git": {
    "autoCommit": true,
    "autoPush": false,
    "commitMessage": "Auto-commit by Claude Code"
  }
}
```

### Branch Behavior

```json
{
  "git": {
    "defaultBranch": "main",
    "createBranch": true
  }
}
```

## Comparison Table

| Feature | Claude Code | Claude.ai Web |
|---------|-------------|---------------|
| Terminal access | Yes | No |
| File editing | Yes | No |
| Git operations | Yes | No |
| Tool execution | Yes | No |
| Persistent memory | Via CLAUDE.md | Yes |
| Multi-file context | Large | Limited |

## Validation

Check your configuration:

```bash
claude /doctor
```

This runs diagnostics and reports any issues.

## Next Steps

- [Slash Commands](../02-slash-commands/README.md) - Built-in shortcuts
- [Memory](../02-memory/README.md) - Persistent context
- [Skills](../03-skills/README.md) - Automate tasks

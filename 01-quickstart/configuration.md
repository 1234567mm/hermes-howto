<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Configuration

Customize Hermes Agent for your workflow.

## Configuration File

Hermes Agent stores settings in `.hermes/settings.json`:

```bash
# View current config
hermes /config
```

### Default Location

| Environment | Path |
|-------------|------|
| Project | `.hermes/settings.json` |
| Home | `~/.hermes/settings.json` |

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

## HERMES.md Project Context

Create a `HERMES.md` file in your project root to provide context:

```bash
# Initialize
hermes /init
```

### Example HERMES.md

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
| `HERMES_MODEL` | Default model | `opus-4.7` |
| `HERMES_PERMISSIONS` | Permission mode | `Ask` |
| `HERMES_THEME` | Color theme | `dark` |
| `EDITOR` | External editor | `vim` |

### Setting Variables

```bash
# Linux/macOS
export HERMES_MODEL=opus-4.7

# Windows (WSL)
export HERMES_MODEL=opus-4.7
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

| Feature | Hermes Agent | Hermes.ai Web |
|---------|--------------|---------------|
| Terminal access | Yes | No |
| File editing | Yes | No |
| Git operations | Yes | No |
| Tool execution | Yes | No |
| Persistent memory | Via HERMES.md | Yes |
| Multi-file context | Large | Limited |

## Validation

Check your configuration:

```bash
hermes doctor
```

This runs diagnostics and reports any issues.

## Next Steps

- [Memory](../02-memory/README.md) - Persistent context
- [Skills](../03-skills/README.md) - Automate tasks

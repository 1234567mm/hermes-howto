# Memory Files

## Overview

Memory files (HERMES.md and MEMORY.md) store persistent context for Hermes Agent sessions. There are two distinct systems: HERMES.md files for manually curated instructions, and MEMORY.md for auto-generated learnings.

## File Types

### HERMES.md

Manually maintained memory files that you create and update.

| Location | Scope | Git-Tracked |
|----------|-------|-------------|
| `./HERMES.md` or `./.hermes/HERMES.md` | Project | Yes |
| `~/.hermes/HERMES.md` | User (all projects) | No |
| `./HERMES.local.md` | Project local | No (git-ignored) |

### MEMORY.md

Auto-generated memory written by Hermes during sessions.

| Location | Purpose |
|----------|---------|
| `~/.hermes/projects/<project>/memory/MEMORY.md` | Main auto memory entrypoint |
| `~/.hermes/projects/<project>/memory/*.md` | Topic-specific auto memory |

## HERMES.md Structure

```markdown
# Project Configuration

## Project Overview
- Name: Your Project
- Tech Stack: Node.js, PostgreSQL, React
- Team Size: 5 developers

## Development Standards
- Use TypeScript strict mode
- Run tests before committing
- Follow conventional commits

## Architecture
@docs/architecture.md
@docs/api-standards.md
```

## HERMES.md Features

### Imports with @

Reference external files using `@path/to/file`:

```markdown
# Project Documentation
See @README.md for overview
See @docs/api.md for API standards
@~/.hermes/my-instructions.md
```

- Relative and absolute paths supported
- Recursive imports up to 5 levels deep
- First-time external imports trigger approval

### Path-Specific Rules

Apply rules to specific paths using YAML frontmatter:

```markdown
---
paths: src/api/**/*.ts
---

# API Rules

- All endpoints require input validation
- Use Zod for schema validation
```

### Modular Rules

Organize rules in `.hermes/rules/` directory:

```
.hermes/
├── HERMES.md
└── rules/
    ├── code-style.md
    ├── testing.md
    └── security.md
```

## MEMORY.md Structure

MEMORY.md is written by Hermes automatically. Only the first 200 lines (or 25KB) are loaded at session start.

```
~/.hermes/projects/<project>/memory/
├── MEMORY.md              # Entrypoint (loaded at startup)
├── debugging.md           # Topic file (loaded on demand)
└── api-conventions.md     # Topic file (loaded on demand)
```

## Auto Memory vs HERMES.md

| Aspect | HERMES.md | MEMORY.md |
|--------|-----------|-----------|
| Who writes | You | Hermes automatically |
| Purpose | Instructions, standards | Learned patterns |
| Updates | Manual | Automatic during sessions |
| Version control | Yes (project level) | No |
| Loading | All at startup | First 200 lines / 25KB |

## Best Practices

### Do

- Be specific and actionable
- Group related rules under headings
- Use imports to avoid duplication
- Commit project HERMES.md to git

### Don't

- Store secrets or credentials
- Include sensitive data
- Make rules too vague
- Duplicate content across files

## Example Templates

### Project HERMES.md

```markdown
# Project Name

## Overview
- Tech Stack: [list]
- Team Size: [number]

## Standards
- Code style: [conventions]
- Testing: [requirements]
- Git workflow: [process]

## Commands
| Command | Purpose |
|---------|---------|
| npm test | Run tests |
| npm run build | Build |
```

### Personal HERMES.md

```markdown
# My Development Preferences

## About Me
- Experience: [level]
- Languages: [preferred]
- Style: [communication]

## Code Preferences
- Error handling: [style]
- Comments: [when to use]
- Testing: [approach]
```

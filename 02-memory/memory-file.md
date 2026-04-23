# Memory Files

## Overview

Memory files (CLAUDE.md and MEMORY.md) store persistent context for Claude Code sessions. There are two distinct systems: CLAUDE.md files for manually curated instructions, and MEMORY.md for auto-generated learnings.

## File Types

### CLAUDE.md

Manually maintained memory files that you create and update.

| Location | Scope | Git-Tracked |
|----------|-------|-------------|
| `./CLAUDE.md` or `./.claude/CLAUDE.md` | Project | Yes |
| `~/.claude/CLAUDE.md` | User (all projects) | No |
| `./CLAUDE.local.md` | Project local | No (git-ignored) |

### MEMORY.md

Auto-generated memory written by Claude during sessions.

| Location | Purpose |
|----------|---------|
| `~/.claude/projects/<project>/memory/MEMORY.md` | Main auto memory entrypoint |
| `~/.claude/projects/<project>/memory/*.md` | Topic-specific auto memory |

## CLAUDE.md Structure

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

## CLAUDE.md Features

### Imports with @

Reference external files using `@path/to/file`:

```markdown
# Project Documentation
See @README.md for overview
See @docs/api.md for API standards
@~/.claude/my-instructions.md
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

Organize rules in `.claude/rules/` directory:

```
.claude/
├── CLAUDE.md
└── rules/
    ├── code-style.md
    ├── testing.md
    └── security.md
```

## MEMORY.md Structure

MEMORY.md is written by Claude automatically. Only the first 200 lines (or 25KB) are loaded at session start.

```
~/.claude/projects/<project>/memory/
├── MEMORY.md              # Entrypoint (loaded at startup)
├── debugging.md           # Topic file (loaded on demand)
└── api-conventions.md     # Topic file (loaded on demand)
```

## Auto Memory vs CLAUDE.md

| Aspect | CLAUDE.md | MEMORY.md |
|--------|-----------|-----------|
| Who writes | You | Claude automatically |
| Purpose | Instructions, standards | Learned patterns |
| Updates | Manual | Automatic during sessions |
| Version control | Yes (project level) | No |
| Loading | All at startup | First 200 lines / 25KB |

## Best Practices

### Do

- Be specific and actionable
- Group related rules under headings
- Use imports to avoid duplication
- Commit project CLAUDE.md to git

### Don't

- Store secrets or credentials
- Include sensitive data
- Make rules too vague
- Duplicate content across files

## Example Templates

### Project CLAUDE.md

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

### Personal CLAUDE.md

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

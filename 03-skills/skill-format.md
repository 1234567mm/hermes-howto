<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Skill Format

Every skill lives in a directory containing a required `SKILL.md` file with YAML frontmatter. This document explains the format and structure.

## Basic Directory Structure

```
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md      # Example output showing expected format
└── scripts/
    └── validate.sh    # Script Claude can execute
```

## SKILL.md Format

```yaml
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
Provide clear, step-by-step guidance for Claude.

## Examples
Show concrete examples of using this Skill.
```

## Required Fields

| Field | Rules |
|-------|-------|
| **name** | Lowercase letters, numbers, hyphens only (max 64 characters). Cannot contain "anthropic" or "claude". |
| **description** | What the Skill does AND when to use it (max 1024 characters). Critical for auto-invocation matching. |

## Optional Frontmatter Fields

```yaml
---
name: my-skill
description: What this skill does and when to use it
argument-hint: "[filename] [format]"        # Hint for autocomplete
disable-model-invocation: true              # Only user can invoke
user-invocable: false                       # Hide from slash menu
allowed-tools: Read, Grep, Glob             # Restrict tool access
model: opus                                 # Specific model to use
effort: high                                # Effort level override
context: fork                               # Run in isolated subagent
agent: Explore                              # Which agent type
shell: bash                                 # Shell for commands
hooks:                                      # Skill-scoped hooks
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate.sh"
paths: "src/api/**/*.ts"               # Glob patterns limiting activation
---
```

| Field | Description |
|-------|-------------|
| `name` | Lowercase letters, numbers, hyphens only (max 64 chars). |
| `description` | What the Skill does AND when to use it (max 1024 chars). |
| `argument-hint` | Hint shown in `/` autocomplete menu (e.g., `"[filename] [format]"`). |
| `disable-model-invocation` | `true` = only user can invoke via `/name`. Claude will never auto-invoke. |
| `user-invocable` | `false` = hidden from `/` menu. Only Claude can auto-invoke. |
| `allowed-tools` | Comma-separated list of tools without permission prompts. |
| `model` | Model override while skill is active (e.g., `opus`, `sonnet`). |
| `effort` | Effort level: `low`, `medium`, `high`, or `max`. |
| `context` | `fork` to run skill in a forked subagent context. |
| `agent` | Subagent type when `context: fork` (e.g., `Explore`, `Plan`). |
| `shell` | Shell for commands: `bash` (default) or `powershell`. |
| `hooks` | Hooks scoped to this skill's lifecycle. |
| `paths` | Glob patterns limiting when skill auto-activates. |

## Skill Content Types

### Reference Content

Adds knowledge Claude applies to your current work—conventions, patterns, style guides.

```yaml
---
name: api-conventions
description: API design patterns for this codebase
---

When writing API endpoints:
- Use RESTful naming conventions
- Return consistent error formats
- Include request validation
```

### Task Content

Step-by-step instructions for specific actions. Often invoked directly with `/skill-name`.

```yaml
---
name: deploy
description: Deploy the application to production
context: fork
disable-model-invocation: true
---

Deploy the application:
1. Run the test suite
2. Build the application
3. Push to the deployment target
```

## String Substitutions

Skills support dynamic values resolved before content reaches Claude:

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` or `$N` | Access specific argument by index (0-based) |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing the SKILL.md file |
| `` !`command` `` | Dynamic context injection — runs shell command and inlines output |

**Example:**

```yaml
---
name: fix-issue
description: Fix a GitHub issue
---

Fix GitHub issue $ARGUMENTS following our coding standards.
1. Read the issue description
2. Implement the fix
3. Write tests
4. Create a commit
```

## Injecting Dynamic Context

The `` !`command` `` syntax runs shell commands before skill content is sent to Claude:

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

## Your task
Summarize this pull request...
```

## Supporting Files

Skills can include multiple files. Keep `SKILL.md` under **500 lines** and reference supporting files using relative paths.

```
my-skill/
├── SKILL.md              # Main instructions (required)
├── templates/            # Templates for Claude to fill in
│   └── output-format.md
├── examples/             # Example outputs showing expected format
│   └── sample-output.md
├── references/           # Domain knowledge and specifications
│   └── api-spec.md
└── scripts/              # Scripts Claude can execute
    └── validate.sh
```

## Best Practices

### Writing Descriptions

Be specific and include trigger terms:

```yaml
# Bad (vague)
description: "Helps with documents"

# Good (specific with trigger terms)
description: "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."
```

### Keep Skills Focused

One Skill = one capability:

- :white_check_mark: "PDF form filling"
- :x: "Document processing" (too broad)

### Naming Conventions

- Lowercase letters, numbers, hyphens only
- Max 64 characters
- Cannot contain "anthropic" or "claude"
- Use descriptive, action-oriented names (e.g., `code-review`, `deploy`, `refactor`)

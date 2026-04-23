<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Code Review Skill

Comprehensive code review with security, performance, and quality analysis.

## Skill Files

- [SKILL.md](code-review/SKILL.md) - Main skill definition
- [templates/review-checklist.md](code-review/templates/review-checklist.md) - Review checklist template

## What This Skill Covers

1. **Security Analysis** - Authentication/authorization, data exposure, injection vulnerabilities
2. **Performance Review** - Algorithm efficiency, memory optimization, caching opportunities
3. **Code Quality** - SOLID principles, design patterns, naming conventions
4. **Maintainability** - Code readability, cyclomatic complexity, type safety

## Usage

```
/code-review src/auth/login.ts
```

Or let Claude auto-invoke when you mention code review, security analysis, or performance optimization.

## Example Output

```markdown
### Summary
- Overall quality: 3/5
- Key findings: 4
- Recommended focus: Security hardening

### Critical Issues
- **Issue**: SQL injection vulnerability
- **Location**: auth/repository.ts:42
- **Impact**: User credentials could be stolen
- **Severity**: Critical
- **Fix**: Use parameterized queries
```

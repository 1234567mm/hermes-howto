# Context Reference Examples

Practical examples of using context refs in prompts.

## Code Review

```
Review file://src/auth.py#authenticate for:
- Security vulnerabilities
- Error handling completeness
- Input validation
```

## Documentation Grounding

```
Based on docs://guides/deployment, explain:
1. Prerequisites
2. Environment setup
3. Deployment steps
```

## API Comparison

```
Compare the authentication methods:
- file://docs/api-v1/auth.md
- file://docs/api-v2/auth.md

Highlight breaking changes.
```

## Code Modification

```
file://src/parser.py#L50-L80 shows the current parser.
Refactor it to support:
- XML input
- Streaming mode
- Error recovery
```

## Multi-File Analysis

```
Analyze dependencies across:
- file://src/models/user.py
- file://src/services/auth.py
- file://src/routes/auth.py

Create a dependency diagram.
```

## URL Reference

```
Summarize the key points from https://example.com/api-guidelines
and apply them to file://src/api-design.md
```

## Cached References

```
Using cached references to docs://api/reference:
1. List all endpoints
2. Identify authentication requirements
3. Document rate limits
```

## Version-Specific References

```
Compare implementation patterns in:
- file://src/v1/middleware.py
- file://src/v2/middleware.py

Explain what changed and why.
```

# Context Reference Syntax

Reference external content in prompts using structured syntax.

## Basic Syntax

### File References

```
file://path/to/file
file://path/to/file#L10           # Line 10
file://path/to/file#L10-L20       # Lines 10-20
file://path/to/file#function-name # Specific function
```

### URL References

```
https://example.com/page
https://example.com/page#section
```

### Documentation References

```
docs://api/endpoints
docs://guides/getting-started
docs://reference/algorithm
```

## Line Range Syntax

| Syntax | Meaning |
|--------|---------|
| `file.md#L5` | Single line 5 |
| `file.md#L5-L15` | Lines 5 through 15 |
| `file.md#L-5` | Last 5 lines |
| `file.md#L5-L` | Line 5 to end |

## Code-Specific References

### Function/Class

```
file://src/utils.py#parse_config    # Function
file://src/models.py#User           # Class
file://src/models.py#User.__init__ # Method
```

### Import Statements

```
file://src/main.py#imports          # All imports
```

### Decorators

```
file://src/api.py#@app.route        # Specific decorator
```

## Documentation References

### Built-in Doc Paths

| Path | Content |
|------|---------|
| `docs://api` | API reference |
| `docs://guides` | User guides |
| `docs://reference` | Technical reference |
| `docs://changelog` | Version history |

### Custom Doc Paths

Reference project documentation:

```
docs://internal/onboarding
docs://team/architecture
docs://runbook/deployment
```

## URL References

### Basic URL

```
https://api.example.com/docs
```

### With Anchor

```
https://example.com/guide#introduction
```

### Query Parameters

```
https://api.example.com/v1/users?format=json
```

## Combining References

### Multiple Files

```
file://src/auth.py#authenticate
file://src/models.py#User
file://src/utils.py#validate_token
```

### Mixed Sources

```
file://src/api.py
https://external-api.com/docs
docs://internal/auth-guide
```

## Inline References

Reference content inline within prompts:

```
Based on file://README.md#L1-L20, explain the project structure
```

```
Review file://src/main.py#handle_request for error handling patterns
```

```
Compare https://api-v1.example.com to https://api-v2.example.com
```

## Caching References

References are cached for performance:

| Strategy | Behavior |
|----------|----------|
| `cache://ref` | Cache reference content |
| `no-cache://ref` | Fetch fresh each time |
| `ttl:3600://ref` | Cache for 1 hour |

## Best Practices

1. **Be specific** — Reference exact lines/sections when possible
2. **Pre-cache URLs** — Cache frequently used web content
3. **Version refs** — Include version in doc refs for stability
4. **Combine wisely** — Too many refs can overwhelm context
5. **Refresh stale refs** — Update cached content when source changes

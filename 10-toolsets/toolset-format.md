# Toolset Format

Toolsets are defined by a `TOOLSET.md` manifest file with structured metadata and tool definitions.

## Structure

```markdown
---
name: docker-tools
version: 1.0.0
description: Container management and orchestration tools
enabled: true
tools:
  - name: container-list
    command: docker ps
    description: List running containers
  - name: image-list
    command: docker images
    description: List local images
  - name: logs
    command: docker logs
    description: Fetch container logs
---
```

## Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique identifier for the toolset |
| `version` | string | Yes | Semantic version (1.0.0) |
| `description` | string | Yes | Human-readable description |
| `enabled` | boolean | No | Default enabled state (true) |
| `tools` | array | Yes | List of tool definitions |

## Tool Definition

Each tool in the `tools` array supports:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Tool identifier within toolset |
| `command` | string | Yes | Executable and arguments |
| `description` | string | Yes | What the tool does |
| `env` | object | No | Environment variables |
| `timeout` | number | No | Max execution seconds |
| `requires` | array | No | Other toolsets required |

## Examples

### Minimal Toolset

```yaml
---
name: minimal-toolset
version: 1.0.0
description: A minimal toolset example
tools:
  - name: hello
    command: echo "Hello"
    description: Print greeting
---
```

### Full-Featured Toolset

```yaml
---
name: cloud-ops
version: 1.2.0
description: Cloud infrastructure operations
enabled: false
tools:
  - name: deploy
    command: kubectl apply -f
    description: Deploy Kubernetes manifests
    timeout: 300
    requires: ["kubectl-config"]

  - name: scale
    command: kubectl scale
    description: Scale deployments
    env:
      NAMESPACE: default

  - name: logs
    command: kubectl logs
    description: Fetch pod logs
    timeout: 60
```

### Multi-Environment Toolset

```yaml
---
name: deployment-tools
version: 2.0.0
description: Multi-environment deployment tools
tools:
  - name: deploy-staging
    command: deploy.sh staging
    description: Deploy to staging
    env:
      DEPLOY_ENV: staging

  - name: deploy-prod
    command: deploy.sh production
    description: Deploy to production
    env:
      DEPLOY_ENV: production
      CONFIRM_REQUIRED: "true"
```

## Validation

Run validation to check your toolset configuration:

```
toolset validate ./path/to/toolset
```

Checks performed:
- YAML syntax validity
- Required fields present
- Version format (semver)
- Command executability
- Circular dependencies

## Best Practices

1. **Name spacing** — Use prefixes to avoid conflicts (e.g., `docker-`, `k8s-`)
2. **Error handling** — Include error output in command definitions
3. **Timeouts** — Set appropriate timeouts for long-running operations
4. **Documentation** — Clear descriptions help discoverability

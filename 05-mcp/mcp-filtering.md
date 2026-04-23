<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# MCP Filtering

Control which MCP tools are available to Hermes agents.

## Filtering Overview

MCP servers can expose many tools. Filtering lets you:

- **Restrict dangerous operations** — Prevent file writes or deletions
- **Limit scope** — Only allow read operations
- **Reduce noise** — Hide unused tools
- **Security** — Control access based on trust level

## Filtering Configuration

Configure in `.claude/mcp_servers.json`:

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/project"],
      "filter": {
        "tools": {
          "include": ["read_file", "list_directory", "search_files"],
          "exclude": ["write_file", "delete_file", "move_file"]
        }
      }
    }
  }
}
```

## Filter Rules

### Include Only Specified Tools

Only allow specific tools:

```json
"filter": {
  "tools": {
    "include": ["read_file", "list_directory"]
  }
}
```

### Exclude Specific Tools

Allow all but exclude some:

```json
"filter": {
  "tools": {
    "exclude": ["write_file", "delete_file", "move_file"]
  }
}
```

### Include with Wildcards

Use glob patterns:

```json
"filter": {
  "tools": {
    "include": ["read_*", "list_*", "search_*"]
  }
}
```

## Filter Modes

### Per-Server Filtering

Apply different filters to each server:

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/project"],
      "filter": {
        "tools": {
          "include": ["read_file", "list_directory"]
        }
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "filter": {
        "tools": {
          "include": ["github_get_issue", "github_search_issues"],
          "exclude": ["github_create_issue", "github_create_pull_request"]
        }
      }
    }
  }
}
```

### Global Filtering

Apply rules to all servers:

```json
{
  "mcp": {
    "globalFilter": {
      "tools": {
        "exclude": ["delete_*", "destroy_*"]
      }
    }
  }
}
```

## Tool Naming

Tools are named `{server}_{tool_name}`:

| Server | Tool | Full Name |
|--------|------|-----------|
| filesystem | read_file | `filesystem_read_file` |
| github | create_issue | `github_create_issue` |
| postgresql | query | `postgresql_query` |

## Filtering by Category

### Read-Only Filesystem

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/project"],
    "filter": {
      "tools": {
        "include": [
          "read_file",
          "read_multiple_files",
          "list_directory",
          "directory_tree",
          "search_files",
          "get_file_info"
        ]
      }
    }
  }
}
```

### Read-Write Filesystem

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/project"],
    "filter": {
      "tools": {
        "include": [
          "read_file",
          "read_multiple_files",
          "list_directory",
          "directory_tree",
          "search_files",
          "get_file_info",
          "write_file",
          "create_directory",
          "move_file"
        ],
        "exclude": ["delete_file", "delete_directory"]
      }
    }
  }
}
```

### GitHub Read-Only

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "filter": {
      "tools": {
        "include": [
          "github_get_issue",
          "github_search_issues",
          "github_list_pulls",
          "github_get_file"
        ]
      }
    }
  }
}
```

## Practical Examples

### Safe Development Environment

```
Configure the filesystem server to only allow read operations
```

Resulting config:

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/project"],
    "filter": {
      "tools": {
        "include": [
          "read_file",
          "read_multiple_files",
          "list_directory",
          "directory_tree",
          "search_files"
        ]
      }
    }
  }
}
```

### CI/Build Environment

```
Allow filesystem read and docker/podman operations, no file modifications
```

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem"],
    "filter": {
      "tools": {
        "include": ["read_*", "list_*"]
      }
    }
  }
}
```

## Viewing Filtered Tools

### List Available Tools

```
Show me all MCP tools currently available after filtering
```

### Check Specific Server Tools

```
List the tools available from the filesystem server
```

## Debugging Filters

### Validate Configuration

```
Check my MCP filtering configuration for errors
```

### Test Filter Application

```
Show me what tools would be available if I applied this filter
```

## Common Filter Patterns

| Use Case | Include | Exclude |
|----------|---------|---------|
| Read-only | `read_*`, `list_*`, `search_*`, `get_*` | `write_*`, `create_*`, `delete_*`, `move_*` |
| No deletions | `*` | `delete_*`, `remove_*`, `destroy_*` |
| No state changes | `read_*`, `list_*`, `search_*` | `create_*`, `update_*`, `delete_*` |
| Audit mode | `*` | - |

## Next Steps

- [mcp-examples/](mcp-examples/) — Complete filtered configurations
- [mcp-servers.md](mcp-servers.md) — Server configuration reference

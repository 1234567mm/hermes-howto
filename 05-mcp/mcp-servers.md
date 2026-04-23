<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# MCP Servers

Detailed configuration and management for MCP servers.

## Server Configuration File

Servers are configured in `.claude/mcp_servers.json`:

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/project"],
      "allowedDirectories": ["/project"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxxxxxxxxxxx"
      }
    }
  }
}
```

## Configuration Reference

### Server Entry

| Field | Required | Description |
|-------|----------|-------------|
| `command` | Yes | Executable path (absolute or relative to PATH) |
| `args` | No | Array of command-line arguments |
| `env` | No | Environment variables object |
| `allowedDirectories` | No | Directories the server can access |
| `timeout` | No | Request timeout in seconds (default: 60) |
| `auto-approve` | No | Tools that bypass confirmation |

### Environment Variables

Store secrets in environment variables:

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_TOKEN": {
        "type": "env",
        "name": "GITHUB_TOKEN"
      }
    }
  }
}
```

### Allowed Directories

Restrict filesystem servers to specific directories:

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem"],
    "allowedDirectories": [
      "/project/src",
      "/project/tests",
      "/project/docs"
    ]
  }
}
```

## Server Management Commands

| Task | Command |
|------|---------|
| Add server | `mcp add <name> <command> [args...]` |
| Remove server | `mcp remove <name>` |
| List servers | `mcp list` |
| Start server | `mcp start <name>` |
| Stop server | `mcp stop <name>` |
| Restart server | `mcp restart <name>` |
| Update server | `mcp update <name> <config>` |

## Built-in Server Management

### List All Servers

```
Show me all configured MCP servers and their status
```

Output format:

| Server | Status | Tools | Type |
|--------|--------|-------|------|
| filesystem | running | 12 | filesystem |
| github | running | 8 | api |
| slack | stopped | 0 | api |

### Server Lifecycle

```
Restart the github MCP server
```

```
Stop the filesystem server and clear its tool cache
```

## Popular MCP Servers

### Filesystem

Read, write, and search local files with permission controls.

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/project"],
    "allowedDirectories": ["/project"]
  }
}
```

### GitHub

Integrate with GitHub for issues, PRs, and repository operations.

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_TOKEN": "ghp_xxxxxxxxxxxx"
    }
  }
}
```

**Available Tools:**
- `github_create_issue` — Create a new issue
- `github_search_issues` — Search issues and PRs
- `github_get_issue` — Get issue details
- `github_create_pull_request` — Create a PR
- `github_list_pulls` — List pull requests

### Slack

Send messages and manage Slack channels.

```json
{
  "slack": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-slack"],
    "env": {
      "SLACK_BOT_TOKEN": "xoxb-xxxxxxxxxxxx",
      "SLACK_TEAM_ID": "T1234567"
    }
  }
}
```

### Brave Search

Web search via Brave Search API.

```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "BSAxxxxxxxxxxxx"
    }
  }
}
```

### PostgreSQL

Query PostgreSQL databases directly.

```json
{
  "postgresql": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres"],
    "env": {
      "DATABASE_URL": "postgresql://user:pass@localhost:5432/dbname"
    }
  }
}
```

### SQLite

Query SQLite databases.

```json
{
  "sqlite": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sqlite"],
    "env": {
      "DB_PATH": "/path/to/database.db"
    }
  }
}
```

### Everything

Desktop search via Everything IPC.

```json
{
  "everything": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-everything"]
  }
}
```

## Server Scopes

### Project Level

Located at `.claude/mcp_servers.json` in your project directory.

### User Level

Located at `~/.claude/mcp_servers.json` for all projects.

## Protocol Details

### MCP Protocol Version

Current: `2024-11-05`

Servers must implement the latest protocol for full compatibility.

### Transport

MCP uses JSON-RPC over stdio by default. Alternative transports:

| Transport | Use Case |
|-----------|----------|
| `stdio` | Local servers, default |
| `http` | Remote servers with SSE |
| `websocket` | Bidirectional communication |

### Request/Response Flow

```mermaid
sequenceDiagram
    participant H as Hermes
    participant B as MCP Bridge
    participant S as MCP Server

    H->>B: Call tool
    B->>S: JSON-RPC request
    S->>S: Execute operation
    S-->>B: JSON-RPC response
    B-->>H: Tool result
```

## Next Steps

- [mcp-filtering.md](mcp-filtering.md) — Control tool access
- [mcp-examples/](mcp-examples/) — Complete server configurations

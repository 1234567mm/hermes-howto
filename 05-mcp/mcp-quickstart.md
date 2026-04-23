<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# MCP Quick Start

Get started with Model Context Protocol (MCP) servers in minutes.

## Prerequisites

- Hermes installed and configured
- Node.js 18+ (for most JavaScript-based MCP servers)
- Basic understanding of tools in Hermes

## Step 1: Check MCP Status

```
Show me the current MCP configuration and available servers
```

This displays:
- Installed servers and their status
- Number of tools available from each server
- Any configuration errors

## Step 2: Add Your First Server

### Filesystem Server (Recommended First Server)

The filesystem server provides safe file operations with configurable permissions.

```
Add the filesystem MCP server with read-only access to the project directory
```

This creates a server configuration:

```json
{
  "name": "filesystem",
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"],
  "allowedDirectories": ["/path/to/project"]
}
```

### GitHub Server

```
Add the GitHub MCP server with my API token
```

Configuration:

```json
{
  "name": "github",
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_TOKEN": "your-token-here"
  }
}
```

## Step 3: Verify Server Connection

```
List all MCP tools currently available
```

You should see tools from your newly added server. For example, with the filesystem server:

| Tool | Description |
|------|-------------|
| `read_file` | Read file contents |
| `read_multiple_files` | Read multiple files at once |
| `list_directory` | List directory contents |
| `directory_tree` | Show directory structure |
| `search_files` | Search file contents |

## Step 4: Use MCP Tools

### Basic File Operations

```
Use the filesystem server to read package.json and show me its dependencies
```

```
Search all TypeScript files in the src directory for the string "TODO"
```

### Combining with Main Tools

MCP tools work alongside Hermes's built-in tools:

```
Read the config file using the filesystem server, then create a test plan based on its contents
```

## Server Configuration Options

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique server identifier |
| `command` | string | Executable to run |
| `args` | string[] | Command arguments |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `env` | object | Environment variables |
| `allowedDirectories` | string[] | Directories the server can access |
| `timeout` | number | Request timeout in seconds |
| `auto-approve` | string[] | Tools that don't require confirmation |

## Common Server Installations

### npm-based Servers

```bash
npx -y @modelcontextprotocol/server-filesystem /path/to/dir
npx -y @modelcontextprotocol/server-github
npx -y @modelcontextprotocol/server-slack
npx -y @modelcontextprotocol/server-brave-search
```

### Python-based Servers

```bash
pip install mcp-server-filesystem
mcp-server-filesystem /path/to/dir
```

## Troubleshooting

### Server Won't Start

1. Check the server command is correct
2. Verify Node.js/Python is installed
3. Check environment variables are set

```
Show me the MCP server logs for the filesystem server
```

### Tools Not Appearing

1. Verify server is running: `mcp list`
2. Restart the server: `mcp stop <name> && mcp start <name>`
3. Check filtering rules aren't blocking tools

### Permission Denied

1. Verify `allowedDirectories` includes the target path
2. Check file/directory permissions
3. Review filtering configuration

## Next Steps

- [mcp-servers.md](mcp-servers.md) — Detailed server configuration
- [mcp-filtering.md](mcp-filtering.md) — Control tool access
- [mcp-examples/](mcp-examples/) — Ready-to-use configurations

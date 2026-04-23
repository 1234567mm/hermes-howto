<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Installation

Install Hermes Agent on your system in under 5 minutes.

## Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| macOS 12+ | Fully supported | Native app or CLI |
| Linux (Ubuntu 20.04+) | Fully supported | CLI only |
| Windows (WSL) | Fully supported | Use WSL2 terminal |
| Windows (native) | Coming soon | Not yet available |

## Installation Methods

### macOS

**Option 1: Download from website**

1. Visit [hermes-agent.dev](https://hermes-agent.dev)
2. Click "Download for macOS"
3. Open the downloaded `.dmg` file
4. Drag Hermes Agent to your Applications folder

**Option 2: Homebrew**

```bash
brew install --cask hermes
```

### Linux

**Option 1: Install script**

```bash
curl -sSL https://storage.googleapis.com/hermes-agent/hermes.sh | sh
```

**Option 2: Manual install**

```bash
# Download the binary
curl -O https://storage.googleapis.com/hermes-agent/hermes-linux-x86_64

# Make it executable
chmod +x hermes-linux-x86_64

# Move to your PATH
sudo mv hermes-linux-x86_64 /usr/local/bin/hermes
```

### Windows (WSL)

If using WSL (Windows Subsystem for Linux), install Hermes Agent within your Linux environment using the Linux installation steps above.

> **Note**: Make sure you're running the install command inside WSL, not in PowerShell or CMD.

## Verification

After installation, verify Hermes Agent is working:

```bash
hermes --version
```

You should see output like:

```
Hermes Agent v1.0.0
```

## First Launch

On first launch, you'll be prompted to:

1. **Sign in** - Authenticate with your Nous Research account or API key
2. **Choose settings** - Select defaults for your workflow
3. **Grant permissions** - Allow file system and git access

```mermaid
sequenceDiagram
    participant User
    participant CLI as Hermes CLI
    participant Auth as Nous Auth

    User->>CLI: hermes
    CLI->>Auth: Sign in
    Auth-->>User: Login page
    User->>Auth: Enter credentials
    Auth-->>CLI: Auth token
    CLI->>User: Ready!
```

## Authentication

Hermes Agent supports multiple AI providers. Free accounts get limited usage; Pro plans offer higher limits.

| Plan | Monthly Usage | Features |
|------|---------------|----------|
| Free | Limited | Basic features |
| Pro | Higher limits | Full access |
| Max | Highest limits | Priority access |

### CLI Login

```bash
hermes login
```

This opens a browser window for OAuth authentication.

## Troubleshooting

### "Command not found"

If `hermes` is not found after installation:

```bash
# Add to your PATH (for manual installs)
export PATH="$PATH:/usr/local/bin"

# Or rehash your shell
hash -r
```

### Permission denied

```bash
# Make sure the binary is executable
chmod +x /usr/local/bin/hermes
```

### Network issues

If you have connectivity problems:

1. Check your internet connection
2. Ensure firewall allows connections to `*.nousresearch.com`
3. Try `hermes login` again

### Run diagnostics

```bash
hermes doctor
```

This command checks your installation health and suggests fixes.

## Next Steps

Once installed, proceed to [First Conversation](first-conversation.md) to run your first prompt.

## See Also

- [Configuration](configuration.md) - Customize your setup
- [Memory](../02-memory/README.md) - Persistent context

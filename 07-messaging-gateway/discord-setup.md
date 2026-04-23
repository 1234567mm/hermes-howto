<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Discord Setup

Configure your Discord bot to work with Hermes Messaging Gateway.

## Overview

Discord bots offer rich interaction through servers, channels, threads, and Discord-specific features like slash commands, buttons, and embeds. Ideal for communities and team collaboration.

## Prerequisites

- A Discord account
- A Discord server where you have admin permissions
- Access to the [Discord Developer Portal](https://discord.com/developers/applications)

## Step 1: Create a Discord Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**
3. Enter a name for your application
4. Navigate to **Bot** in the left sidebar
5. Click **Reset Token** to get your bot token
6. Copy and securely store the token

**Important**: Never share your bot token. It provides full control of your bot.

## Step 2: Configure Bot Permissions

1. In the Developer Portal, go to **OAuth2 > URL Generator**
2. Select the following scopes:
   - `bot`
   - `applications.commands`
3. Select the following bot permissions:
   - **General**: View Channels, Send Messages, Embed Links
   - **Text**: Read Message History, Add Reactions, Use Slash Commands
4. Copy the generated OAuth2 URL
5. Open the URL and authorize the bot in your server

## Step 3: Configure Hermes

Add your bot token to the environment:

```bash
export DISCORD_BOT_TOKEN="your-bot-token-here"
```

Or add to your Hermes configuration file (`~/.hermes/config.yaml`):

```yaml
messaging:
  discord:
    enabled: true
    bot_token: "${DISCORD_BOT_TOKEN}"
```

## Step 4: Start the Gateway

Run the Hermes gateway for Discord:

```bash
hermes gateway discord --port 8080
```

The gateway connects to Discord via WebSocket (gateway API), so no webhook URL is needed for basic functionality.

## Step 5: Register Slash Commands

Register Hermes commands globally or for specific servers:

```bash
# Register globally (may take up to 1 hour to propagate)
hermes gateway discord register-commands --global

# Register for specific server
hermes gateway discord register-commands --guild 123456789012345678
```

Default commands:

| Command | Description |
|---------|-------------|
| `/ask` | Ask Hermes a question |
| `/help` | Show help information |
| `/status` | Check Hermes status |
| `/clear` | Clear conversation history |
| `/memory` | Show memory information |

## Discord-Specific Features

### Threads

Hermes supports Discord threads:

```yaml
messaging:
  discord:
    threads:
      enabled: true
      auto_create: true
      prefix: "hermes-"
```

Create a thread:
- User right-clicks message > **Create Thread**
- Or use `/thread` command to create new thread

### Server Roles

Control access via Discord roles:

```yaml
messaging:
  discord:
    roles:
      allowed:
        - "Hermes Users"
        - "Admins"
      denied:
        - "Banned"
```

### Embeds

Hermes can send rich embed messages:

```yaml
messaging:
  discord:
    embeds:
      color: 0x5865F2  # Discord blurple
      footer: "Hermes Gateway"
      timestamp: true
```

## Button Interactions

Discord buttons are supported for interactive conversations:

### Button Types

| Type | Description |
|------|-------------|
| Primary | Blurple buttons for main actions |
| Secondary | Gray buttons for less important actions |
| Success | Green buttons for confirmations |
| Danger | Red buttons for destructive actions |
| Link | Buttons that open URLs |

### Example Button Response

When Hermes responds with buttons:

```
Here's the information you requested:

[Details] [More Info] [Dismiss]
```

## Message Components Configuration

```yaml
messaging:
  discord:
    components:
      buttons:
        max_per_row: 5
        style: "primary"
      selects:
        max_options: 25
        placeholder: "Select an option..."
```

## Modal Interactions

Hermes supports Discord modals for forms:

```yaml
messaging:
  discord:
    modals:
      enabled: true
      forms:
        feedback:
          title: "Feedback Form"
          components:
            - label: "Your feedback"
              custom_id: "feedback_text"
              style: "paragraph"
              required: true
```

## Permissions Configuration

Configure bot permissions precisely:

```yaml
messaging:
  discord:
    permissions:
      default:
        send_messages: true
        embed_links: true
        attach_files: true
        use_application_commands: true
      admin:
        bypass_filter: true
        clear_messages: true
```

## Rich Presence

Set bot activity status:

```yaml
messaging:
  discord:
    presence:
      status: "online"  # online, idle, dnd, invisible
      activity:
        type: "playing"  # playing, watching, listening, competing
        name: "with Hermes"
```

## Channel Types

| Channel | Support | Notes |
|---------|---------|-------|
| Text Channels | Yes | Full support |
| Voice Channels | No | Text only in voice |
| Threads | Yes | Auto-created supported |
| DMs | Yes | Single-user conversations |
| Group DMs | Partial | Limited features |

## Webhook Integration

For webhook-based message handling:

```yaml
messaging:
  discord:
    webhook:
      enabled: true
      endpoint: "/discord/webhook"
      secret: "${DISCORD_WEBHOOK_SECRET}"
```

## Troubleshooting

### Bot Not Appearing in Server

1. Generate invite link with correct permissions
2. Ensure you're authorizing with correct account
3. Check if server has admin restrictions

### "Application Did Not Respond"

- Slash command registered but gateway not responding
- Check gateway is running: `hermes gateway discord status`
- Verify bot token is valid

### "Missing Permissions"

1. Check bot role is above user roles
2. Verify channel permissions allow bot actions
3. Re-authorize with more permissions

### Slash Commands Not Showing

- Global commands take up to 1 hour to appear
- Use `register-commands --guild` for immediate testing
- Bot must be online for commands to register

### Message Not Sending

- Check if bot has Send Messages permission
- Verify channel is not read-only
- Ensure bot role has correct position in hierarchy

## Rate Limits

Discord has strict rate limits:

| Action | Limit |
|--------|-------|
| Send Message | 5/5 seconds (bucket) |
| Edit Message | 5/5 seconds |
| Delete Message | 5/5 seconds |
| Reaction | 1/0.25 seconds |
| Slash Command Acknowledge | 3/3 seconds |

Hermes queues messages to respect these limits automatically.

## Configuration Reference

```yaml
messaging:
  discord:
    enabled: true
    bot_token: "${DISCORD_BOT_TOKEN}"
    
    # Gateway connection
    gateway:
      intents:
        - message_content
        - guild_messages
        - direct_messages
        - guild_members
        
    # Slash commands
    commands:
      global: true
      guild_id: null  # Set for server-specific
      
    # Features
    threads:
      enabled: true
      auto_create: false
    embeds:
      enabled: true
      color: 0x5865F2
    buttons:
      enabled: true
    modals:
      enabled: true
      
    # Access control
    roles:
      allowed: []
      denied: []
      
    # Presence
    presence:
      status: "online"
      activity:
        type: "playing"
        name: "with Hermes"
```

## Next Steps

- [telegram-setup.md](telegram-setup.md) — Back to Telegram
- [slack-setup.md](slack-setup.md) — Add Slack integration
- [bot-patterns/](bot-patterns/) — Reusable bot patterns

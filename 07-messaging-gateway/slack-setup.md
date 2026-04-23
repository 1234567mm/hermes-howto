<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Slack Setup

Configure your Slack app to work with Hermes Messaging Gateway.

## Overview

Slack apps provide enterprise-grade messaging with channels, threads, apps, and extensive API capabilities. Ideal for team collaboration and workplace integration.

## Prerequisites

- A Slack workspace (Free, Pro, or Enterprise)
- Admin access to manage apps (or request IT to approve)
- Access to [Slack API](https://api.slack.com/apps)

## Step 1: Create a Slack App

1. Go to [Slack API](https://api.slack.com/apps) and click **Create New App**
2. Select **From scratch**
3. Enter app name and choose your workspace
4. Click **Create App**

## Step 2: Configure App Credentials

1. Navigate to **Basic Information** > **App Credentials**
2. Copy and securely store:
   - `App ID`
   - `Client ID`
   - `Client Secret`
   - `Signing Secret`

Configure Hermes with these credentials:

```bash
export SLACK_CLIENT_ID="your-client-id"
export SLACK_CLIENT_SECRET="your-client-secret"
export SLACK_SIGNING_SECRET="your-signing-secret"
export SLACK_BOT_TOKEN="your-bot-token"
```

Or in `~/.hermes/config.yaml`:

```yaml
messaging:
  slack:
    enabled: true
    client_id: "${SLACK_CLIENT_ID}"
    client_secret: "${SLACK_CLIENT_SECRET}"
    signing_secret: "${SLACK_SIGNING_SECRET}"
    bot_token: "${SLACK_BOT_TOKEN}"
```

## Step 3: Enable Bot User

1. Navigate to **Bot Users**
2. Click **Add Bot User**
3. Set display name and default username
4. Enable **Always Online** if desired

## Step 4: Configure Permissions (OAuth & Permissions)

1. Go to **OAuth & Permissions**
2. Add these scopes to **Bot Token Scopes**:

| Scope | Description |
|-------|-------------|
| `chat:write` | Send messages as the bot |
| `channels:history` | Read messages in public channels |
| `channels:read` | Access channel information |
| `groups:history` | Read messages in private channels |
| `im:history` | Read direct messages |
| `im:read` | Access direct message info |
| `mpim:history` | Read group DMs |
| `app_mentions:read` | Read @mentions of the app |
| `reactions:read` | Read reactions |
| `reactions:write` | Add reactions |
| `files:read` | Read files |
| `files:write` | Upload files |
| `users:read` | Get user information |

3. Click **Save Changes**
4. Click **Install to Workspace** or **Request to Install**
5. Copy the **Bot User OAuth Token** (`xoxb-...`)

## Step 5: Enable App Home Messages

Enable DM functionality:

1. Go to **App Home**
2. Enable **Messages Tab**
3. Set **Home Tab** enabled if needed

## Step 6: Set Up Event Subscriptions

1. Go to **Event Subscriptions**
2. Toggle **Enable Events** ON
3. Set **Request URL** to your gateway endpoint:
   ```
   https://your-domain.com/slack/events
   ```
4. For local development, use ngrok:
   ```bash
   ngrok http 8080
   ```
5. Add these **Subscribe to Bot Events**:
   - `app_mention`
   - `message.channels`
   - `message.groups`
   - `message.im`
   - `message.mpim`

## Step 7: Register Slash Commands

1. Go to **Slash Commands**
2. Click **Create New Command**
3. Configure each command:

| Command | Description | Request URL |
|---------|-------------|-------------|
| `/ask` | Ask Hermes a question | `https://your-domain.com/slack/events` |
| `/help` | Show help | `https://your-domain.com/slack/events` |
| `/status` | Check status | `https://your-domain.com/slack/events` |
| `/clear` | Clear conversation | `https://your-domain.com/slack/events` |
| `/memory` | Memory info | `https://your-domain.com/slack/events` |

## Step 8: Start the Gateway

```bash
hermes gateway slack --port 8080
```

## Slack-Specific Features

### Threads

Slack threads are fully supported:

```yaml
messaging:
  slack:
    threads:
      enabled: true
      reply_broadcast: false
```

Reply in thread:

```bash
# When mentioning bot in a thread
@Hermes Can you explain this?

# Bot responds in thread
```

### Channels

Hermes responds in channels when mentioned:

```yaml
messaging:
  slack:
    channels:
      allowed:
        - "C0123456789"  # Channel ID
        - "C9876543210"
      require_mention: true
```

### Direct Messages

DM conversations are always available:

```yaml
messaging:
  slack:
    dm:
      enabled: true
      greeting: "Hi! How can I help you today?"
```

### Block Kit

Hermes supports Slack Block Kit for rich messages:

```yaml
messaging:
  slack:
    blocks:
      enabled: true
      template:
        - type: "section"
          text: "Here's the information:"
        - type: "actions"
          elements:
            - type: "button"
              text: "View Details"
              action_id: "view_details"
```

### Interactive Components

Buttons, select menus, and modals:

```yaml
messaging:
  slack:
    interactive:
      enabled: true
      buttons:
        max_columns: 3
      selects:
        max_options: 10
```

## App Distribution

If building for multiple workspaces:

```yaml
messaging:
  slack:
    distribution:
      enabled: true
      client_id: "${SLACK_CLIENT_ID}"
```

Use OAuth 2.0 authorization flow for installation.

## Shortcuts

Add shortcuts to the message input:

```yaml
messaging:
  slack:
    shortcuts:
      - name: "Ask Hermes"
        callback_id: "shortcut_ask"
        description: "Ask a question"
      - name: "Summarize"
        callback_id: "shortcut_summarize"
        description: "Summarize conversation"
```

## Workflows

Connect Hermes to Slack Workflows:

```yaml
messaging:
  slack:
    workflows:
      enabled: true
      trigger:
        name: "Hermes Query"
        callback_id: "workflow_hermes"
```

## Message Formatting

| Format | Example | Result |
|--------|---------|--------|
| Bold | `*text*` | **text** |
| Italic | `_text_` | _text_ |
| Code | `` `code` `` | `code` |
| Code Block | ` ```code``` ` | Code block |
| Link | `<https://url|text>` | Link |

## Block Kit Elements

### Section Block

```json
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "Welcome to Hermes!"
  }
}
```

### Actions Block

```json
{
  "type": "actions",
  "elements": [
    {
      "type": "button",
      "text": { "type": "plain_text", "text": "Approve" },
      "action_id": "approve"
    }
  ]
}
```

### Context Block

```json
{
  "type": "context",
  "elements": [
    {
      "type": "mrkdwn",
      "text": "Last updated: Just now"
    }
  ]
}
```

## Troubleshooting

### "This app is unavailable"

- App not approved in workspace
- Contact workspace admin to approve

### Bot Not Responding to Mentions

1. Check Events Subscriptions are enabled
2. Verify Request URL returns `200 OK`
3. Ensure `app_mention` event is subscribed
4. Check bot has `chat:write` scope

### "channel_not_found"

- Bot not added to channel
- Invite bot to channel: `/invite @BotName`

### DM Not Working

- Check App Home is configured
- Ensure `im:read` and `im:history` scopes added

### Interactive Actions Not Working

1. Go to **Interactivity**
2. Toggle **Interactivity** ON
3. Set **Request URL** to:
   ```
   https://your-domain.com/slack/interactive
   ```

## Rate Limits

| Action | Limit |
|--------|-------|
| Post Message | 1/second (burst 10) |
| API Calls | 100/minute (tier 3) |
| File Upload | 10/minute |

## Configuration Reference

```yaml
messaging:
  slack:
    enabled: true
    client_id: "${SLACK_CLIENT_ID}"
    client_secret: "${SLACK_CLIENT_SECRET}"
    signing_secret: "${SLACK_SIGNING_SECRET}"
    bot_token: "${SLACK_BOT_TOKEN}"
    
    # Event handling
    events:
      url: "/slack/events"
      request_url: "https://your-domain.com/slack/events"
      
    # Interactive components
    interactive:
      enabled: true
      url: "/slack/interactive"
      
    # Features
    threads:
      enabled: true
      reply_broadcast: false
    dm:
      enabled: true
      greeting: "Hello! How can I help?"
      
    # Channel configuration
    channels:
      allowed: []
      denied: []
      require_mention: true
      
    # Block Kit
    blocks:
      enabled: true
      
    # Shortcuts
    shortcuts:
      enabled: true
```

## Next Steps

- [telegram-setup.md](telegram-setup.md) — Back to Telegram
- [discord-setup.md](discord-setup.md) — Back to Discord
- [bot-patterns/](bot-patterns/) — Reusable bot patterns

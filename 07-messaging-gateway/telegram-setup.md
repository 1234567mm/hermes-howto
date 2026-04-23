<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Telegram Setup

Configure your Telegram bot to work with Hermes Messaging Gateway.

## Overview

Telegram bots provide the easiest platform integration with Hermes. They offer a familiar chat interface with rich features like inline buttons, files, and voice messages.

## Prerequisites

- A Telegram account
- Access to [@BotFather](https://t.me/BotFather) on Telegram

## Step 1: Create Your Bot

1. Open Telegram and search for **@BotFather**
2. Send the command: `/newbot`
3. Follow the prompts:
   - **Name**: Your bot's display name (e.g., "My Hermes Bot")
   - **Username**: Unique username ending in `bot` (e.g., `myhermesbot`)
4. BotFather will provide your **bot token**: `123456789:ABCdefGhIJKlmNoPQRsTUVwxYZ`

**Important**: Save this token securely. It provides full control of your bot.

## Step 2: Configure Hermes

Add your bot token to the environment:

```bash
export TELEGRAM_BOT_TOKEN="your-bot-token-here"
```

Or add to your Hermes configuration file (`~/.hermes/config.yaml`):

```yaml
messaging:
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
```

## Step 3: Set Up Webhook

Hermes uses webhooks to receive Telegram updates. Start the gateway:

```bash
hermes gateway telegram --port 8080
```

Telegram will send updates to your webhook URL. For local development, use a tunneling service:

```bash
# Using ngrok
ngrok http 8080

# Using cloudflared
cloudflared tunnel --url http://localhost:8080
```

Register your webhook:

```bash
hermes gateway telegram set-webhook --url https://your-domain.com/telegram
```

## Step 4: Configure Bot Profile

Set up your bot's profile for better discoverability:

| Setting | Command | Example |
|---------|---------|---------|
| Profile photo | `/setuserpic` | Upload an image |
| Description | `/setdescription` | "Hermes-powered assistant" |
| Commands | `/setcommands` | See below |
| About | `/setabouttext` | Brief bot description |

Recommended command list for Hermes:

```
help - Get help with available commands
start - Start a conversation with Hermes
status - Check Hermes status
memory - View memory information
```

## Step 5: Test Your Bot

1. Open Telegram and search for your bot by its username
2. Send `/start` to begin a conversation
3. Verify you receive a response from Hermes

## Bot Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Start conversation | `/start` |
| `/help` | Show help message | `/help` |
| `/status` | Check system status | `/status` |
| `/memory` | Memory info | `/memory` |
| `/model` | Show current model | `/model` |
| `/clear` | Clear conversation | `/clear` |

## Inline Buttons

Hermes supports Telegram inline buttons for quick actions:

### Reply Keyboard

```
[Help] [Status] [Memory]
[Settings] [Cancel]
```

### Inline Keyboard

```
[View History] [Share] [Delete]
```

Button configuration in Hermes:

```yaml
messaging:
  telegram:
    reply_markup:
      keyboard:
        - - text: Help
          callback_data: action_help
        - - text: Status
          callback_data: action_status
      resize_keyboard: true
      one_time_keyboard: false
```

## Groups and Supergroups

To use Hermes in groups:

1. **Privacy Mode**: BotFather enables privacy mode by default. Disable it for group functionality:
   ```
   /setprivacy
   ```
   Select "Disable" to allow the bot to see all messages.

2. **Group Configuration**:
   ```yaml
   messaging:
     telegram:
       group_mode:
         enabled: true
         prefix_required: true  # Require /command to activate
         allowed_groups:
           - "-1001234567890"   # Group chat ID
   ```

3. **Admin Commands in Groups**:
   - `/here` - Register bot in current group
   - `/allgroups` - List all allowed groups
   - `/deny` - Remove group access

## Voice Messages

Telegram voice messages are processed automatically:

1. Telegram sends voice as OGG audio
2. Gateway converts to text (STT)
3. Hermes processes the text
4. Response sent back as text or voice

Enable voice processing:

```yaml
messaging:
  telegram:
    voice:
      enabled: true
      auto_reply: true
```

## File Handling

Receive and process files from Telegram:

| File Type | Handling | Max Size |
|-----------|----------|----------|
| Images | Process as vision input | 10 MB |
| Documents | Pass as attachments | 20 MB |
| Audio | Transcribe if voice enabled | 20 MB |
| Video | Extract audio track | 20 MB |

## Webhook Security

### Validate Updates

Hermes validates all incoming Telegram updates:

```yaml
messaging:
  telegram:
    webhook:
      secret_token: "your-secret-token"  # Set via BotFather
      ip_whitelist:
        - 149.154.160.0/20
        - 91.108.4.0/22
```

### Reject Unauthorized Requests

Only accept requests from Telegram's servers:

```bash
# Verify webhook certificate
hermes gateway telegram verify-cert
```

## Troubleshooting

### Bot Not Responding

1. Check bot token is correct
2. Verify webhook is set: `https://api.telegram.org/bot<TOKEN>/getWebhookInfo`
3. Ensure gateway is running
4. Check logs: `hermes logs --component gateway`

### "Bot was blocked by the user"

- User has blocked the bot
- Cannot send proactive messages without user initiation

### "Chat not found"

- Webhook may be sending to wrong chat
- Verify chat_id in configuration

### Rate Limiting

Telegram limits message frequency. Hermes handles this automatically, but for high-traffic bots:

- Send messages in bursts of 30/minute
- Use content distribution for broadcasts
- Implement message queuing

## Configuration Reference

```yaml
messaging:
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    
    # Webhook configuration
    webhook:
      enabled: true
      url: "https://your-domain.com/telegram"
      secret_token: "${TELEGRAM_SECRET}"
    
    # Message handling
    parse_mode: "Markdown"
    disable_web_page_preview: false
    
    # Features
    reply_to_message: true
    allow_mentions: true
    
    # Privacy and groups
    group_mode:
      enabled: false
      prefix_required: true
    
    # Voice processing
    voice:
      enabled: true
      auto_reply: true
```

## Next Steps

- [discord-setup.md](discord-setup.md) — Add Discord integration
- [slack-setup.md](slack-setup.md) — Add Slack integration
- [bot-patterns/](bot-patterns/) — Reusable bot patterns

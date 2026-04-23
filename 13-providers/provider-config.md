# Provider Configuration

Configure LLM providers for Hermes.

## Provider Configuration File

```yaml
providers:
  - name: anthropic
    type: anthropic
    api_key: ${ANTHROPIC_API_KEY}
    models:
      default: claude-3-5-sonnet-latest
      Sonnet: claude-3-5-sonnet-latest
      Opus: claude-3-opus-latest
    settings:
      max_tokens: 8192
      temperature: 0.7
      top_p: 0.9

  - name: openai
    type: openai
    api_key: ${OPENAI_API_KEY}
    base_url: https://api.openai.com/v1
    models:
      default: gpt-4o
      fast: gpt-4o-mini
    settings:
      max_tokens: 4096
      temperature: 0.7

  - name: ollama
    type: ollama
    base_url: http://localhost:11434
    models:
      default: llama3.2
      coding: codellama
```

## Configuration Fields

### Provider Level

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Provider identifier |
| `type` | string | Yes | Provider type (anthropic, openai, etc.) |
| `api_key` | string | No | API key (or env var reference) |
| `base_url` | string | No | Custom endpoint URL |
| `models` | object | Yes | Model name mappings |
| `settings` | object | No | Default model settings |

### Model Level

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `default` | string | Yes | Default model identifier |
| `<name>` | string | No | Named model variant |

### Settings Level

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `max_tokens` | number | Provider default | Max response length |
| `temperature` | number | 0.7 | Response randomness |
| `top_p` | number | 1.0 | Nucleus sampling |
| `top_k` | number | Provider default | Top-k sampling |

## Environment Variables

Reference API keys securely:

```yaml
api_key: ${ANTHROPIC_API_KEY}
```

Set in shell:
```bash
export ANTHROPIC_API_KEY=sk-...
export OPENAI_API_KEY=sk-...
```

## Examples

### Anthropic Only

```yaml
providers:
  - name: anthropic
    type: anthropic
    api_key: ${ANTHROPIC_API_KEY}
    models:
      default: claude-3-5-sonnet-latest
    settings:
      max_tokens: 8192
```

### Multi-Provider with Fallback

```yaml
providers:
  - name: primary
    type: anthropic
    api_key: ${ANTHROPIC_API_KEY}
    models:
      default: claude-3-5-sonnet-latest

  - name: fallback
    type: openai
    api_key: ${OPENAI_API_KEY}
    models:
      default: gpt-4o
    fallback_order: 1
```

### Ollama Local

```yaml
providers:
  - name: local
    type: ollama
    base_url: http://localhost:11434
    models:
      default: llama3.2
      coding: codellama
    settings:
      max_tokens: 4096
```

### Provider with Custom Endpoint

```yaml
providers:
  - name: custom-llm
    type: openai-compatible
    api_key: ${CUSTOM_API_KEY}
    base_url: https://api.custom-llm.com/v1
    models:
      default: custom-model
```

## Testing Configuration

```bash
# Test provider connectivity
provider test anthropic

# Test specific model
provider test openai --model gpt-4o

# Show current configuration
provider show

# Validate config file
provider validate ~/.claude/providers/default.yaml
```

## Best Practices

1. **Use environment variables** — Never hardcode API keys
2. **Set defaults explicitly** — Clear default model selection
3. **Configure fallbacks** — Plan for provider outages
4. **Match settings to model** — Different models have different optimal settings
5. **Test after changes** — Verify configuration works

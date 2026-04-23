# Provider Configuration Examples

Ready-to-use provider configurations.

## Standard Setup

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
```

## Development Setup (Cost-Conscious)

```yaml
providers:
  - name: anthropic
    type: anthropic
    api_key: ${ANTHROPIC_API_KEY}
    models:
      default: claude-3-5-haiku-latest
      Sonnet: claude-3-5-sonnet-latest
    settings:
      max_tokens: 4096
      temperature: 0.5

  - name: openai
    type: openai
    api_key: ${OPENAI_API_KEY}
    models:
      default: gpt-4o-mini
      standard: gpt-4o
```

## Multi-Provider with Fallback

```yaml
providers:
  - name: primary
    type: anthropic
    api_key: ${ANTHROPIC_API_KEY}
    models:
      default: claude-3-5-sonnet-latest
    priority: 1

  - name: fallback
    type: openai
    api_key: ${OPENAI_API_KEY}
    models:
      default: gpt-4o
    priority: 2
    fallback_order: 1
```

## Ollama Local Development

```yaml
providers:
  - name: ollama-local
    type: ollama
    base_url: http://localhost:11434
    models:
      default: llama3.2
      coding: codellama
      reasoning: deepseek-r1
    settings:
      max_tokens: 4096
      temperature: 0.7

  - name: cloud
    type: anthropic
    api_key: ${ANTHROPIC_API_KEY}
    models:
      default: claude-3-5-sonnet-latest
    # Use for production when local is unavailable
```

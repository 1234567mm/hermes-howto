<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Voice Setup

Configure audio devices and backends for Hermes Voice Mode.

## Overview

Voice Mode requires proper audio configuration for both input (microphone) and output (speakers). Hermes supports multiple backends to accommodate different operating systems and preferences.

## Audio Configuration

### Microphone Setup

1. **Identify your microphone**
   ```bash
   # Linux (ALSA)
   arecord -l
   
   # macOS
   system_profiler SPAudioDataType
   
   # List available in PulseAudio
   pactl list sources short
   ```

2. **Set default input device** (Linux)
   ```bash
   # Edit ~/.asoundrc or set environment variable
   export AUDIO_INPUT_DEVICE="plughw:1,0"
   ```

3. **Test microphone**
   ```bash
   # Record a short clip
   arecord -d 5 -f cd test.wav
   
   # Play back to verify
   aplay test.wav
   ```

### Speaker/Audio Output Setup

1. **Identify your output device**
   ```bash
   # Linux (PulseAudio)
   pactl list sinks short
   
   # ALSA
   aplay -l
   ```

2. **Set default output device** (Linux)
   ```bash
   export AUDIO_OUTPUT_DEVICE="plughw:0,0"
   ```

3. **Test speakers**
   ```bash
   speaker-test -t sine -f 440
   ```

## Backend Selection

Hermes supports multiple STT/TTS backends:

| Backend | STT Engine | TTS Engine | Quality | Latency |
|---------|------------|------------|---------|---------|
| **default** | System default | System default | Medium | Medium |
| **google** | Google Speech | Google TTS | High | Low |
| **openai** | Whisper API | OpenAI TTS | High | Low |
| **coqui** | Coqui STT | Coqui TTS | Medium | Low |
| **espeak** | espeak | espeak | Low | Low |

### Configuring Backend

```bash
# Via environment variable
export HERMES_STT_BACKEND="openai"
export HERMES_TTS_BACKEND="openai"

# Or in configuration file (~/.hermes/config.yaml)
voice:
  stt_backend: "openai"
  tts_backend: "openai"
```

## Platform-Specific Setup

### Linux (Ubuntu/Debian)

```bash
# Install audio utilities
sudo apt-get install alsa-utils pulseaudio

# Install a TTS engine (example: espeak)
sudo apt-get install espeak

# Configure PulseAudio
pulseaudio --start
```

### macOS

```bash
# macOS handles audio automatically
# Ensure microphone permission granted in System Preferences
```

### Windows (WSL)

```bash
# WSL2 audio requires additional setup
# Install PulseAudio on Windows or use WSL integration tools

# Option: Use Windows native audio with WSL2
# Requires: PulseAudio server on Windows side
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `AUDIO_INPUT_DEVICE` | Microphone device identifier | System default |
| `AUDIO_OUTPUT_DEVICE` | Speaker device identifier | System default |
| `HERMES_STT_BACKEND` | Speech-to-text backend | "default" |
| `HERMES_TTS_BACKEND` | Text-to-speech backend | "default" |
| `HERMES_VOICE_LANG` | Language code | "en" |
| `HERMES_TTS_VOICE` | TTS voice identifier | Backend default |

## Troubleshooting

### No Audio Input

1. Check microphone is not muted:
   ```bash
   # PulseAudio
   pavucontrol
   
   # ALSA
   amixer sset Mic unmute
   ```

2. Verify microphone permission:
   ```bash
   ls -la /dev/snd/
   groups  # Ensure user is in audio group
   sudo usermod -a -G audio $USER
   ```

### No Audio Output

1. Check speakers are not muted:
   ```bash
   amixer sset Master unmute
   pavucontrol
   ```

2. Verify correct output device selected

### High Latency

- Switch to local backend (espeak, coqui) for lower latency
- Check network connectivity if using cloud backends
- Reduce audio buffer size in backend configuration

### STT Not Recognizing

- Speak clearly and at normal pace
- Check microphone distance (6-12 inches optimal)
- Reduce background noise
- Adjust input gain levels

## Next Steps

- [voice-cli.md](voice-cli.md) — Start voice interaction
- [voice-telegram.md](voice-telegram.md) — Configure Telegram voice
- [voice-discord.md](voice-discord.md) — Configure Discord voice

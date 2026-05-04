# JARVIS.md — What is Jarvis?

Jarvis is the **voice communication layer** for Hermes Agent. Think of it as a sophisticated two-way radio between you and your AI team.

## What it does

- Listens for "hey Jarvis" (wake word detection)
- Transcribes your speech to text using Whisper (runs entirely offline)
- Sends your query to Hermes Agent and waits for the response
- Speaks Hermes's reply back to you using Edge TTS (AriaNeural female voice)
- Logs every voice exchange to `CORE/daily/YYYY/MM/DD/voice.md` for later review

## What it doesn't do

Jarvis is not a brain — it doesn't make decisions, run code, or manage memory. All of that lives in Hermes Agent. Jarvis just handles the audio.

## Voice persona

Jarvis uses a female voice (Microsoft AriaNeural). The personality is defined in SOUL.md.

## Architecture

```
Wake word → VAD → Whisper STT → Hermes Agent → Edge TTS → Speaker
                                            ↓
                            voice.md (daily log)
```

## Config

- Runtime config: `~/.config/jarvis/config.json`
- If missing, copy from `examples/config.json`
- TTS engine: edge (free, no API key)
- Wake word: "jarvis" (configurable aliases)

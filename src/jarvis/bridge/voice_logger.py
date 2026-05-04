"""Appends each voice session to the daily voice.md in the jarvis-claw PARA daily folder."""
from __future__ import annotations

import threading
from datetime import datetime
from pathlib import Path

JARVIS_CLAW = Path("/Users/alishafique/Code/jarvis-claw/data/WORKSPACES/CORE/daily")
_LOCK = threading.Lock()


def _today_folder() -> Path:
    today = datetime.now()
    folder = JARVIS_CLAW / today.strftime("%Y") / today.strftime("%m") / today.strftime("%d")
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def append_voice_entry(transcript: str, response: str) -> None:
    """Append a voice exchange to CORE/daily/YYYY/MM/DD/voice.md (thread-safe)."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"\n## {timestamp}\nUser: {transcript}\nZenu: {response}\n"
    voice_file = _today_folder() / "voice.md"

    with _LOCK:
        # If file doesn't exist, write the header first
        if not voice_file.exists():
            header = f"# Voice — {datetime.now().strftime('%Y-%m-%d')}\n\n"
            voice_file.write_text(header, encoding="utf-8")
        voice_file.write_text(voice_file.read_text(encoding="utf-8") + entry, encoding="utf-8")

"""Hermes bridge — speaks to Hermes Agent via subprocess and returns the response."""
from __future__ import annotations

import subprocess
import os
import sys
import threading
from pathlib import Path


HERMES_CLI = os.environ.get(
    "HERMES_CLI", os.path.expanduser("~/.local/bin/hermes")
)
TIMEOUT_SEC = 120


def call_hermes(query: str) -> str:
    """Send a voice query to Hermes Agent and return the response text.

    Uses `hermes chat -q "..."` — the CLI's non-interactive query mode.
    Falls back to echo if Hermes is not installed.
    """
    try:
        proc = subprocess.run(
            [HERMES_CLI, "chat", "-q", query],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SEC,
            env={**os.environ, "NO_COLOR": "1"},
        )
        if proc.returncode == 0:
            return proc.stdout.strip()
        else:
            stderr = proc.stderr.strip()
            # Fallback: echo the query so something is spoken
            return f"Sorry, Hermes had an error: {stderr[:100]}"
    except subprocess.TimeoutExpired:
        return "Sorry, Hermes took too long to respond."
    except FileNotFoundError:
        return "Hermes CLI not found. Install it or set HERMES_CLI env var."
    except Exception as e:
        return f"Sorry, I couldn't reach Hermes: {e}"

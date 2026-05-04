"""Jarvis Hermes bridge — voice queries → Hermes Agent → spoken response."""
from .hermes_bridge import call_hermes
from .voice_logger import append_voice_entry

__all__ = ["call_hermes", "append_voice_entry"]

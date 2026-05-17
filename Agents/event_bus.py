"""agents/event_bus.py — Bus d'événements pub/sub en mémoire pour inter-agents."""

import json
import weakref
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Callable


class EventBus:
    """Bus d'événements simple en mémoire (thread-safe pour usage local)."""

    _instance: weakref.ref | None = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None or cls._instance() is None:
            obj = super().__new__(cls)
            cls._instance = weakref.ref(obj)
            return obj
        return cls._instance()

    def __init__(self, history_limit: int = 0):
        if hasattr(self, "_handlers"):
            return
        self._handlers: dict[str, list[Callable[[dict], None]]] = defaultdict(list)
        self._history: list[dict] = []
        self._history_limit = history_limit

    def subscribe(self, topic: str, handler: Callable[[dict], None]) -> None:
        """Enregistre un handler pour un topic."""
        self._handlers[topic].append(handler)

    def unsubscribe(self, topic: str, handler: Callable[[dict], None]) -> None:
        """Désenregistre un handler."""
        if handler in self._handlers[topic]:
            self._handlers[topic].remove(handler)

    def publish(self, topic: str, payload: dict) -> None:
        """Publie un événement sur un topic."""
        event = {
            "topic": topic,
            "ts": datetime.now(timezone.utc).isoformat(),
            "payload": payload,
        }
        self._history.append(event)
        if self._history_limit and len(self._history) > self._history_limit:
            self._history = self._history[-self._history_limit:]
        for handler in self._handlers.get(topic, []):
            try:
                handler(payload)
            except Exception as e:
                print(f"[event_bus] Handler error on {topic}: {e}", flush=True)

    def get_history(self, topic: str | None = None, limit: int = 100) -> list[dict]:
        """Retourne l'historique des événements, filtrable par topic."""
        items = self._history
        if topic:
            items = [e for e in items if e["topic"] == topic]
        return items[-limit:]

    def snapshot(self) -> dict:
        """Snapshot complet du bus pour persistance/debug."""
        return {
            "topics": list(self._handlers.keys()),
            "history_count": len(self._history),
            "history": self._history,
        }


def get_bus() -> EventBus:
    """Retourne l'instance unique du bus."""
    return EventBus()

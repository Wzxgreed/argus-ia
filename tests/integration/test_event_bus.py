#!/usr/bin/env python3
"""Integration tests for the event bus."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

import pytest
from agents.event_bus import EventBus


def test_publish_subscribe():
    bus = EventBus()
    received = []

    def handler(payload):
        received.append(payload)

    bus.subscribe("test_topic", handler)
    bus.publish("test_topic", {"msg": "hello"})

    assert len(received) == 1
    assert received[0] == {"msg": "hello"}


def test_multiple_subscribers():
    bus = EventBus()
    calls = []

    def h1(p):
        calls.append("h1")

    def h2(p):
        calls.append("h2")

    bus.subscribe("multi", h1)
    bus.subscribe("multi", h2)
    bus.publish("multi", {})

    assert set(calls) == {"h1", "h2"}


def test_get_history():
    bus = EventBus(history_limit=3)
    bus.publish("hist", {"n": 1})
    bus.publish("hist", {"n": 2})
    bus.publish("hist", {"n": 3})
    bus.publish("hist", {"n": 4})

    hist = bus.get_history("hist")
    assert len(hist) == 3
    assert hist[0]["payload"] == {"n": 2}
    assert hist[-1]["payload"] == {"n": 4}


def test_singleton():
    b1 = EventBus()
    b2 = EventBus()
    assert b1 is b2

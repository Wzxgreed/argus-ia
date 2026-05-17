#!/usr/bin/env python3
"""
track_ollama.py — Met à jour le compteur d'usage Ollama Cloud localement.
Usage:
  python3 scripts/track_ollama.py --calls 1 --tokens-in 1500 --tokens-out 800
  python3 scripts/track_ollama.py --reset-window    # Reset fenêtre 5h
  python3 scripts/track_ollama.py --reset-weekly    # Reset compteur hebdo
"""
import argparse
import json
import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
USAGE_FILE = BASE_DIR / "data" / "ollama_usage.json"
CONFIG_FILE = BASE_DIR / "data" / "ollama_config.json"


def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def save_json(path: Path, data: dict):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def reset_window(usage: dict) -> dict:
    now = now_utc()
    usage["window_5h_start"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    usage["window_5h_calls"] = 0
    usage["window_5h_tokens_input"] = 0
    usage["window_5h_tokens_output"] = 0
    return usage


def reset_weekly(usage: dict) -> dict:
    now = now_utc()
    monday = now - timedelta(days=now.weekday())
    usage["week_start"] = monday.strftime("%Y-%m-%d")
    usage["weekly_calls"] = 0
    usage["weekly_tokens_input"] = 0
    usage["weekly_tokens_output"] = 0
    return usage


def increment(usage: dict, calls: int, tokens_in: int, tokens_out: int) -> dict:
    # Reset fenêtre 5h si nécessaire
    window_start_str = usage.get("window_5h_start")
    if window_start_str:
        window_start = datetime.fromisoformat(window_start_str.replace("Z", "+00:00"))
        if (now_utc() - window_start).total_seconds() >= 5 * 3600:
            usage = reset_window(usage)

    # Reset hebdo si nécessaire
    week_start_str = usage.get("week_start")
    monday = now_utc() - timedelta(days=now_utc().weekday())
    if week_start_str != monday.strftime("%Y-%m-%d"):
        usage = reset_weekly(usage)

    usage["window_5h_calls"] = usage.get("window_5h_calls", 0) + calls
    usage["window_5h_tokens_input"] = usage.get("window_5h_tokens_input", 0) + tokens_in
    usage["window_5h_tokens_output"] = usage.get("window_5h_tokens_output", 0) + tokens_out
    usage["weekly_calls"] = usage.get("weekly_calls", 0) + calls
    usage["weekly_tokens_input"] = usage.get("weekly_tokens_input", 0) + tokens_in
    usage["weekly_tokens_output"] = usage.get("weekly_tokens_output", 0) + tokens_out
    return usage


def check_alerts(usage: dict, config: dict) -> list:
    alerts = []
    win_pct = usage["window_5h_calls"] / config["window_5h_limit"] if config.get("window_5h_limit") else 0
    weekly_pct = usage["weekly_calls"] / config["weekly_limit"] if config.get("weekly_limit") else 0

    if win_pct >= 1.0:
        alerts.append(f"🚨 QUOTA 5H ATTEINT : {usage['window_5h_calls']}/{config['window_5h_limit']} appels")
    elif win_pct >= 0.9:
        alerts.append(f"⚠️  90% du quota 5h utilisé : {usage['window_5h_calls']}/{config['window_5h_limit']}")
    elif win_pct >= 0.7:
        alerts.append(f"⚡ 70% du quota 5h utilisé : {usage['window_5h_calls']}/{config['window_5h_limit']}")

    if weekly_pct >= 1.0:
        alerts.append(f"🚨 QUOTA HEBDO ATTEINT : {usage['weekly_calls']}/{config['weekly_limit']} appels")
    elif weekly_pct >= 0.9:
        alerts.append(f"⚠️  90% du quota hebdo utilisé : {usage['weekly_calls']}/{config['weekly_limit']}")

    return alerts


def main():
    parser = argparse.ArgumentParser(description="Tracker usage Ollama Cloud")
    parser.add_argument("--calls", type=int, default=1, help="Nombre d'appels à ajouter")
    parser.add_argument("--tokens-in", type=int, default=0, help="Tokens input")
    parser.add_argument("--tokens-out", type=int, default=0, help="Tokens output")
    parser.add_argument("--reset-window", action="store_true", help="Reset fenêtre 5h")
    parser.add_argument("--reset-weekly", action="store_true", help="Reset compteur hebdo")
    parser.add_argument("--status", action="store_true", help="Afficher le statut")
    args = parser.parse_args()

    usage = load_json(USAGE_FILE)
    config = load_json(CONFIG_FILE)

    if args.reset_window:
        usage = reset_window(usage)
        save_json(USAGE_FILE, usage)
        print(f"✅ Fenêtre 5h reset — {usage['window_5h_start']}")
        return

    if args.reset_weekly:
        usage = reset_weekly(usage)
        save_json(USAGE_FILE, usage)
        print("✅ Compteur hebdo reset")
        return

    if args.status:
        print(f"📊 Ollama Cloud Usage")
        print(f"   Fenêtre 5h : {usage.get('window_5h_calls', 0)}/{config.get('window_5h_limit', '∞')} appels")
        print(f"   Hebdo      : {usage.get('weekly_calls', 0)}/{config.get('weekly_limit', '∞')} appels")
        print(f"   Tokens IN  : {usage.get('window_5h_tokens_input', 0):,}")
        print(f"   Tokens OUT : {usage.get('window_5h_tokens_output', 0):,}")
        alerts = check_alerts(usage, config)
        for a in alerts:
            print(f"   {a}")
        return

    # Incrément par défaut
    usage = increment(usage, args.calls, args.tokens_in, args.tokens_out)
    save_json(USAGE_FILE, usage)

    alerts = check_alerts(usage, config)
    print(f"✅ +{args.calls} appel(s) tracké(s)")
    print(f"   Fenêtre 5h : {usage['window_5h_calls']}/{config.get('window_5h_limit', '∞')}")
    print(f"   Hebdo      : {usage['weekly_calls']}/{config.get('weekly_limit', '∞')}")
    for a in alerts:
        print(f"   {a}")


if __name__ == "__main__":
    main()

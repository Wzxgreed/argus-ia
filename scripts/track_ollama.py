#!/usr/bin/env python3
"""
track_ollama.py — Met à jour le compteur d'usage Ollama Cloud localement.
Usage:
  python3 scripts/track_ollama.py --calls 1 --tokens-in 1500 --tokens-out 800
  python3 scripts/track_ollama.py --reset-daily    # Reset compteur journalier
  python3 scripts/track_ollama.py --reset-monthly  # Reset compteur mensuel
"""
import argparse
import json
import os
from datetime import datetime, timezone
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


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def reset_daily(usage: dict) -> dict:
    usage["daily_calls"] = 0
    usage["daily_tokens_input"] = 0
    usage["daily_tokens_output"] = 0
    usage["date"] = today_str()
    # Archive dans l'historique
    history = usage.get("history", [])
    if len(history) > 90:
        history = history[-90:]
    usage["history"] = history
    return usage


def reset_monthly(usage: dict) -> dict:
    usage["monthly_calls"] = 0
    usage["monthly_tokens_input"] = 0
    usage["monthly_tokens_output"] = 0
    return usage


def increment(usage: dict, calls: int, tokens_in: int, tokens_out: int) -> dict:
    usage["daily_calls"] = usage.get("daily_calls", 0) + calls
    usage["daily_tokens_input"] = usage.get("daily_tokens_input", 0) + tokens_in
    usage["daily_tokens_output"] = usage.get("daily_tokens_output", 0) + tokens_out
    usage["monthly_calls"] = usage.get("monthly_calls", 0) + calls
    usage["monthly_tokens_input"] = usage.get("monthly_tokens_input", 0) + tokens_in
    usage["monthly_tokens_output"] = usage.get("monthly_tokens_output", 0) + tokens_out
    usage["date"] = today_str()
    return usage


def check_alerts(usage: dict, config: dict) -> list:
    alerts = []
    daily_pct = usage["daily_calls"] / config["daily_limit"] if config.get("daily_limit") else 0
    monthly_pct = usage["monthly_calls"] / config["monthly_limit"] if config.get("monthly_limit") else 0

    if daily_pct >= 1.0:
        alerts.append(f"🚨 QUOTA JOURNALIER ATTEINT : {usage['daily_calls']}/{config['daily_limit']} appels")
    elif daily_pct >= 0.9:
        alerts.append(f"⚠️  90% du quota journalier utilisé : {usage['daily_calls']}/{config['daily_limit']}")
    elif daily_pct >= 0.7:
        alerts.append(f"⚡ 70% du quota journalier utilisé : {usage['daily_calls']}/{config['daily_limit']}")

    if monthly_pct >= 1.0:
        alerts.append(f"🚨 QUOTA MENSUEL ATTEINT : {usage['monthly_calls']}/{config['monthly_limit']} appels")
    elif monthly_pct >= 0.9:
        alerts.append(f"⚠️  90% du quota mensuel utilisé : {usage['monthly_calls']}/{config['monthly_limit']}")

    return alerts


def main():
    parser = argparse.ArgumentParser(description="Tracker usage Ollama Cloud")
    parser.add_argument("--calls", type=int, default=1, help="Nombre d'appels à ajouter")
    parser.add_argument("--tokens-in", type=int, default=0, help="Tokens input")
    parser.add_argument("--tokens-out", type=int, default=0, help="Tokens output")
    parser.add_argument("--reset-daily", action="store_true", help="Reset compteur journalier")
    parser.add_argument("--reset-monthly", action="store_true", help="Reset compteur mensuel")
    parser.add_argument("--status", action="store_true", help="Afficher le statut")
    args = parser.parse_args()

    usage = load_json(USAGE_FILE)
    config = load_json(CONFIG_FILE)

    if args.reset_daily:
        usage = reset_daily(usage)
        save_json(USAGE_FILE, usage)
        print(f"✅ Compteur journalier reset — {usage['date']}")
        return

    if args.reset_monthly:
        usage = reset_monthly(usage)
        save_json(USAGE_FILE, usage)
        print("✅ Compteur mensuel reset")
        return

    if args.status:
        print(f"📊 Ollama Cloud Usage ({usage.get('date', '—')})")
        print(f"   Journalier : {usage.get('daily_calls', 0)}/{config.get('daily_limit', '∞')} appels")
        print(f"   Mensuel    : {usage.get('monthly_calls', 0)}/{config.get('monthly_limit', '∞')} appels")
        print(f"   Tokens IN  : {usage.get('daily_tokens_input', 0):,}")
        print(f"   Tokens OUT : {usage.get('daily_tokens_output', 0):,}")
        alerts = check_alerts(usage, config)
        for a in alerts:
            print(f"   {a}")
        return

    # Incrément par défaut
    usage = increment(usage, args.calls, args.tokens_in, args.tokens_out)
    save_json(USAGE_FILE, usage)

    alerts = check_alerts(usage, config)
    print(f"✅ +{args.calls} appel(s) tracké(s)")
    print(f"   Journalier : {usage['daily_calls']}/{config.get('daily_limit', '∞')}")
    print(f"   Mensuel    : {usage['monthly_calls']}/{config.get('monthly_limit', '∞')}")
    for a in alerts:
        print(f"   {a}")


if __name__ == "__main__":
    main()

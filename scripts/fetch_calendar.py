#!/usr/bin/env python3
"""
fetch_calendar.py — Calendrier earnings et événements économiques pour la watchlist.

Sources:
- yfinance (earnings dates via .calendar)
- FMP si clé API disponible (economic calendar)

Usage:
    python scripts/fetch_calendar.py

Output:
    Merge dans data/YYYY-MM-DD.json (section "calendar")
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yfinance as yf

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def fetch_earnings_dates(tickers: list) -> list:
    events = []
    for t in tickers:
        try:
            stock = yf.Ticker(t)
            cal = stock.calendar
            if cal is not None and not cal.empty:
                # yfinance calendar = DataFrame avec Earnings Date
                for _, row in cal.iterrows():
                    try:
                        # Format peut varier
                        date_val = row.get("Earnings Date") or row.get("Earnings Date Low") or row.get("earningsDate")
                        if pd.isna(date_val):
                            continue
                        if isinstance(date_val, str):
                            date_str = date_val[:10]
                        elif hasattr(date_val, "strftime"):
                            date_str = date_val.strftime("%Y-%m-%d")
                        else:
                            continue
                        events.append({
                            "ticker": t,
                            "event_type": "earnings",
                            "date": date_str,
                            "source": "yfinance",
                        })
                    except Exception:
                        continue
        except Exception as e:
            events.append({"ticker": t, "event_type": "earnings", "error": True, "reason": str(e)})
    return events


def build_economic_calendar() -> list:
    """
    Calendrier économique statique des prochains événements majeurs US.
    En production, remplacer par appel API (FMP, TradingEconomics, etc.)
    """
    # Ce bloc est un placeholder — à enrichir avec une vraie source
    return []


def generate_alerts(events: list, days_ahead: int = 5) -> list:
    today = datetime.now(timezone.utc).date()
    alerts = []
    for ev in events:
        if ev.get("error"):
            continue
        try:
            ev_date = datetime.strptime(ev["date"], "%Y-%m-%d").date()
            delta = (ev_date - today).days
            if 0 <= delta <= days_ahead:
                alerts.append({
                    "ticker": ev["ticker"],
                    "event_type": ev["event_type"],
                    "date": ev["date"],
                    "days_until": delta,
                    "action": "generate_preview",
                })
        except Exception:
            continue
    return alerts


def main():
    config = load_config()
    tickers = [t["ticker"] for t in config["tickers"]]
    date_str = today_str()
    data_path = DATA_DIR / f"{date_str}.json"

    print("[fetch_calendar] Fetching calendar data...", file=sys.stderr)

    earnings_events = fetch_earnings_dates(tickers)
    economic_events = build_economic_calendar()
    alerts = generate_alerts(earnings_events, days_ahead=5)

    calendar_block = {
        "earnings": earnings_events,
        "economic": economic_events,
        "alerts": alerts,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Merge
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            snapshot = json.load(f)
    else:
        snapshot = {
            "meta": {
                "date": date_str,
                "source": "yfinance",
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            },
            "prices": {},
            "macro": {},
        }

    snapshot["calendar"] = calendar_block
    snapshot["meta"]["fetched_at"] = datetime.now(timezone.utc).isoformat()

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False, default=str)

    # Mettre à jour latest.json
    latest_link = DATA_DIR / "latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(data_path.relative_to(DATA_DIR))

    print(f"[fetch_calendar] Written {len(earnings_events)} earnings events, {len(alerts)} alerts to {data_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    # Lazy import pandas pour fetch_calendar
    import pandas as pd
    sys.exit(main())

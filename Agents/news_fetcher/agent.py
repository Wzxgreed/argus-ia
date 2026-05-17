#!/usr/bin/env python3
"""
agent_news_fetcher.py — Fetch unifié des news pour toute la watchlist.

Récupère les news Yahoo Finance une seule fois pour tous les tickers,
puis les sauvegarde dans data/news_YYYY-MM-DD.json.
Les autres agents (geo, event-driven, watchman) lisent ce fichier.

Usage:
    python agents/news_fetcher/agent.py

Output:
    data/news_YYYY-MM-DD.json  (symlink latest)
    data/news_latest.json
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from yahoo_client import YahooClient

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    print("[news] Starting unified news fetch...", file=sys.stderr)
    config = load_config()
    tickers = [t["ticker"] for t in config.get("tickers", [])]

    client = YahooClient()
    all_news = {}
    total_items = 0

    for ticker in tickers:
        print(f"[news] Fetching news for {ticker}...", file=sys.stderr)
        items = client.get_news(ticker, limit=15)
        all_news[ticker] = items
        total_items += len(items)
        print(f"[news]   {ticker}: {len(items)} items", file=sys.stderr)

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report = {
        "meta": {
            "date": date_str,
            "tickers": tickers,
            "total_items": total_items,
            "source": "yahoo_rest",
        },
        "news": all_news,
    }

    output_path = DATA_DIR / f"news_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "news_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(
        f"[news] Report → {output_path} | {total_items} items across {len(tickers)} tickers",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

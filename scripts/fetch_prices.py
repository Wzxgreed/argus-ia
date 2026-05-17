#!/usr/bin/env python3
"""
fetch_prices.py — Snapshot quotidien des prix et métriques watchlist.

Sources:
- Yahoo Finance via yahoo_worker.py (subprocess yfinance + timeout OS)
  → évite les hangs au niveau C (libcurl) non-interruptibles par Python
- FMP (optionnel, pour consensus, insider trades, earnings dates)

Usage:
    python scripts/fetch_prices.py

Output:
    data/YYYY-MM-DD.json  (merge avec le bloc macro ensuite)
"""

import json
import subprocess
import sys
import tempfile
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from fmp_client import FMPClient

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
WORKER_PATH = BASE_DIR / "scripts" / "yahoo_worker.py"

WORKER_TIMEOUT = 120  # seconds — yfinance import peut prendre 60–90s


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def fetch_ticker_subprocess(ticker: str) -> dict:
    """
    Lance yahoo_worker.py dans un subprocess avec timeout.
    Si le worker bloque au niveau C (libcurl), le timeout OS le tue proprement.
    """
    try:
        result = subprocess.run(
            [sys.executable, str(WORKER_PATH), ticker],
            capture_output=True,
            text=True,
            timeout=WORKER_TIMEOUT,
        )
        if result.returncode != 0:
            return {
                "ticker": ticker,
                "error": True,
                "reason": f"Worker exit code {result.returncode}: {result.stderr[:200]}",
            }
        data = json.loads(result.stdout)
        data["timestamp"] = datetime.now(timezone.utc).isoformat()
        return data
    except subprocess.TimeoutExpired:
        return {
            "ticker": ticker,
            "error": True,
            "reason": f"Timeout ({WORKER_TIMEOUT}s) — yfinance/libcurl hang",
        }
    except json.JSONDecodeError as e:
        return {
            "ticker": ticker,
            "error": True,
            "reason": f"JSON decode error: {e}",
        }
    except Exception as e:
        return {
            "ticker": ticker,
            "error": True,
            "reason": str(e),
        }


def main():
    config = load_config()
    tickers = [t["ticker"] for t in config["tickers"]]

    date_str = today_str()
    output_path = DATA_DIR / f"{date_str}.json"

    # --- FMP client (optionnel) ---
    fmp = FMPClient()
    fmp_active = bool(fmp.api_key)
    if fmp_active:
        print(f"[fetch_prices] FMP API key found — enriching with institutional data", file=sys.stderr)
    else:
        print(f"[fetch_prices] FMP API key not found — Yahoo Finance only", file=sys.stderr)

    snapshot = {
        "meta": {
            "date": date_str,
            "source": "yahoo_worker (subprocess)" + (" + fmp" if fmp_active else ""),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "tickers_requested": tickers,
            "tickers_ok": 0,
            "tickers_ko": 0,
        },
        "prices": {},
    }

    # --- Parallel fetching with ThreadPoolExecutor ---
    max_workers = min(4, len(tickers))
    print(
        f"[fetch_prices] Fetching {len(tickers)} tickers with {max_workers} workers (timeout {WORKER_TIMEOUT}s)...",
        file=sys.stderr,
    )

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_ticker_subprocess, t): t for t in tickers}

        for future in as_completed(futures):
            ticker = futures[future]
            try:
                data = future.result()
            except Exception as e:
                data = {"ticker": ticker, "error": True, "reason": str(e)}

            # Enrich with FMP if available and Yahoo succeeded
            if not data.get("error") and fmp_active:
                print(f"[fetch_prices] Enriching {ticker} with FMP data...", file=sys.stderr)
                data = fmp.enrich_ticker(ticker, data)

            snapshot["prices"][ticker] = data
            if data.get("error"):
                snapshot["meta"]["tickers_ko"] += 1
                print(f"[fetch_prices]   {ticker}: KO — {data.get('reason', 'unknown')}", file=sys.stderr)
            else:
                snapshot["meta"]["tickers_ok"] += 1
                close = data.get("price", {}).get("close")
                rsi = data.get("technical", {}).get("rsi14")
                print(f"[fetch_prices]   {ticker}: OK (close=${close}, RSI={rsi})", file=sys.stderr)

    # Écriture atomique
    with tempfile.NamedTemporaryFile(mode="w", dir=DATA_DIR, delete=False, suffix=".json") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False, default=str)
        temp_path = f.name
    os.replace(temp_path, output_path)

    # Symlink latest.json
    latest_link = DATA_DIR / "latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(
        f"[fetch_prices] Written {output_path} ({snapshot['meta']['tickers_ok']} OK, {snapshot['meta']['tickers_ko']} KO)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

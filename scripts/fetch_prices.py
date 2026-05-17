#!/usr/bin/env python3
"""
fetch_prices.py — Snapshot quotidien des prix et métriques watchlist.

Sources:
- Yahoo Finance via yahoo_worker_daemon.py (subprocess pré-chauffé)
  → évite les hangs au niveau C (libcurl) et le coût d'import répété de yfinance
- FMP (optionnel, pour consensus, insider trades, earnings dates)

Usage:
    python scripts/fetch_prices.py

Output:
    data/YYYY-MM-DD.json  (merge avec le bloc macro ensuite)
"""

import json
import os
import select
import subprocess
import sys
import tempfile
import threading
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
WORKER_PATH = BASE_DIR / "scripts" / "yahoo_worker_daemon.py"

FETCH_TIMEOUT = 60  # seconds max par ticker (yfinance déjà importé, le fetch est rapide)
WORKER_READY_TIMEOUT = 180  # seconds pour que le daemon charge yfinance


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


class YahooWorkerPool:
    """
    Pool de daemons yahoo_worker pré-chauffés.
    Chaque daemon charge yfinance une seule fois, puis sert plusieurs tickers.
    """

    def __init__(self, num_workers: int = 2):
        self.num_workers = num_workers
        self.workers = []
        self.locks = []
        self._idx = 0

        print(
            f"[fetch_prices] Starting {num_workers} yahoo_worker daemon(s)...",
            file=sys.stderr,
        )

        for i in range(num_workers):
            proc = subprocess.Popen(
                [sys.executable, str(WORKER_PATH)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )
            # Attendre le signal "ready"
            ready_line = self._readline(proc.stdout, WORKER_READY_TIMEOUT)
            if ready_line is None:
                raise RuntimeError(
                    f"Worker {i} timed out after {WORKER_READY_TIMEOUT}s during startup"
                )
            try:
                ready = json.loads(ready_line)
                if ready.get("status") != "ready":
                    raise RuntimeError(f"Worker {i} failed to start: {ready}")
            except json.JSONDecodeError:
                raise RuntimeError(f"Worker {i} sent invalid JSON: {ready_line[:200]}")

            self.workers.append(proc)
            self.locks.append(threading.Lock())
            print(f"[fetch_prices]   Worker {i} ready", file=sys.stderr)

    @staticmethod
    def _readline(stdout, timeout: float) -> str | None:
        """Lit une ligne sur stdout avec timeout (select)."""
        fd = stdout.fileno()
        ready, _, _ = select.select([fd], [], [], timeout)
        if ready:
            return stdout.readline()
        return None

    def fetch(self, ticker: str) -> dict:
        """Assigne un ticker à un worker en round-robin et retourne le résultat."""
        idx = self._idx % self.num_workers
        self._idx += 1
        worker = self.workers[idx]
        lock = self.locks[idx]

        with lock:
            try:
                req = json.dumps({"action": "fetch", "ticker": ticker}) + "\n"
                worker.stdin.write(req)
                worker.stdin.flush()

                line = self._readline(worker.stdout, FETCH_TIMEOUT)
                if line is None:
                    return {
                        "ticker": ticker,
                        "error": True,
                        "reason": f"Worker timeout ({FETCH_TIMEOUT}s) for {ticker}",
                    }
                if not line.strip():
                    return {
                        "ticker": ticker,
                        "error": True,
                        "reason": "Worker EOF (unexpected)",
                    }

                data = json.loads(line)
                data["timestamp"] = datetime.now(timezone.utc).isoformat()
                return data

            except json.JSONDecodeError as e:
                return {
                    "ticker": ticker,
                    "error": True,
                    "reason": f"JSON decode error: {e}",
                }
            except Exception as e:
                return {"ticker": ticker, "error": True, "reason": str(e)}

    def close(self):
        """Arrête proprement tous les workers."""
        for i, worker in enumerate(self.workers):
            try:
                worker.stdin.write(json.dumps({"action": "exit"}) + "\n")
                worker.stdin.flush()
                worker.wait(timeout=5)
            except Exception:
                worker.kill()
            finally:
                worker.stdin.close()
                worker.stdout.close()
                worker.stderr.close()
                worker.wait()
        self.workers.clear()
        self.locks.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


def main():
    config = load_config()
    tickers = [t["ticker"] for t in config["tickers"]]

    date_str = today_str()
    output_path = DATA_DIR / f"{date_str}.json"

    # --- FMP client (optionnel) ---
    fmp = FMPClient()
    fmp_active = bool(fmp.api_key)
    if fmp_active:
        print(
            f"[fetch_prices] FMP API key found — enriching with institutional data",
            file=sys.stderr,
        )
    else:
        print(
            f"[fetch_prices] FMP API key not found — Yahoo Finance only",
            file=sys.stderr,
        )

    snapshot = {
        "meta": {
            "date": date_str,
            "source": "yahoo_worker_daemon (warm)" + (" + fmp" if fmp_active else ""),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "tickers_requested": tickers,
            "tickers_ok": 0,
            "tickers_ko": 0,
        },
        "prices": {},
    }

    # --- Parallel fetching via daemon pool ---
    num_workers = min(2, len(tickers))
    with YahooWorkerPool(num_workers=num_workers) as pool:
        print(
            f"[fetch_prices] Fetching {len(tickers)} tickers with {num_workers} daemon(s)...",
            file=sys.stderr,
        )

        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = {executor.submit(pool.fetch, t): t for t in tickers}

            for future in as_completed(futures):
                ticker = futures[future]
                try:
                    data = future.result()
                except Exception as e:
                    data = {"ticker": ticker, "error": True, "reason": str(e)}

                # Fallback FMP si Yahoo daemon a échoué
                if data.get("error") and fmp_active:
                    print(
                        f"[fetch_prices]   {ticker}: Yahoo KO — trying FMP fallback...",
                        file=sys.stderr,
                    )
                    quote = fmp.get_quote(ticker)
                    if isinstance(quote, list) and quote:
                        q = quote[0]
                        data = {
                            "ticker": ticker,
                            "error": False,
                            "source": "fmp_fallback",
                            "price": {
                                "close": q.get("price"),
                                "open": q.get("open"),
                                "high": q.get("dayHigh"),
                                "low": q.get("dayLow"),
                                "previous_close": q.get("previousClose"),
                                "volume": q.get("volume"),
                                "change_pct": q.get("changesPercentage"),
                            },
                            "technical": {},
                            "fundamentals": {
                                "market_cap": q.get("marketCap"),
                                "pe_ratio": q.get("pe"),
                                "beta": q.get("beta"),
                            },
                            "options": {},
                        }
                        data = fmp.enrich_ticker(ticker, data)
                        print(
                            f"[fetch_prices]   {ticker}: FMP fallback OK (close=${data['price']['close']})",
                            file=sys.stderr,
                        )

                # Enrich with FMP if available and Yahoo succeeded
                elif not data.get("error") and fmp_active:
                    data = fmp.enrich_ticker(ticker, data)

                snapshot["prices"][ticker] = data
                if data.get("error"):
                    snapshot["meta"]["tickers_ko"] += 1
                    print(
                        f"[fetch_prices]   {ticker}: KO — {data.get('reason', 'unknown')}",
                        file=sys.stderr,
                    )
                else:
                    snapshot["meta"]["tickers_ok"] += 1
                    close = data.get("price", {}).get("close")
                    rsi = data.get("technical", {}).get("rsi14")
                    source_note = " [FMP fallback]" if data.get("source") == "fmp_fallback" else ""
                    print(
                        f"[fetch_prices]   {ticker}: OK{source_note} (close=${close}, RSI={rsi})",
                        file=sys.stderr,
                    )

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

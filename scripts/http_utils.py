#!/usr/bin/env python3
"""
http_utils.py — Wrapper HTTP avec retry + backoff + caching pour Yahoo et FMP.

Fonctionnalités :
  • Retry exponentiel : 3 tentatives max, backoff 1s → 2s → 4s
  • Caching basé sur la date : les réponses sont stockées dans data/cache/
    et réutilisées le même jour (TTL = fin de journée UTC)
  • Timeout garanti sur tous les appels

Usage :
    from http_utils import http_get
    data = http_get("https://query1.finance.yahoo.com/v8/finance/chart/AAPL")
"""

import hashlib
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "data" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_TIMEOUT = 15
MAX_RETRIES = 3
BACKOFF_BASE = 1.0  # secondes


def _cache_key(url: str, params: dict | None) -> str:
    """Génère une clé de cache unique pour l'URL + params."""
    key_str = url + json.dumps(params or {}, sort_keys=True)
    return hashlib.md5(key_str.encode()).hexdigest() + ".json"


def _cache_path(url: str, params: dict | None) -> Path:
    """Chemin du fichier de cache pour cette requête."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    day_dir = CACHE_DIR / today
    day_dir.mkdir(parents=True, exist_ok=True)
    return day_dir / _cache_key(url, params)


def _is_cache_valid(cache_path: Path) -> bool:
    """Le cache est valide s'il existe et qu'on est le même jour UTC."""
    if not cache_path.exists():
        return False
    # Vérifier que le fichier n'est pas vide
    if cache_path.stat().st_size == 0:
        return False
    return True


def _read_cache(cache_path: Path) -> dict | list | None:
    """Lit la réponse depuis le cache."""
    try:
        with open(cache_path, "r", encoding="utf-8") as f:
            cached = json.load(f)
        return cached.get("data")
    except Exception:
        return None


def _write_cache(cache_path: Path, data: dict | list) -> None:
    """Écrit la réponse dans le cache."""
    try:
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump({"cached_at": datetime.now(timezone.utc).isoformat(), "data": data}, f)
    except Exception:
        pass


def http_get(
    url: str,
    params: dict = None,
    headers: dict = None,
    timeout: int = DEFAULT_TIMEOUT,
    session: requests.Session = None,
    use_cache: bool = True,
) -> dict:
    """
    GET avec retry exponentiel + caching + timeout.

    Retourne {"error": True, "reason": "..."} en cas d'échec,
    ou le JSON de la réponse en cas de succès.
    """
    cache_path = _cache_path(url, params)

    # 1. Vérifier le cache
    if use_cache and _is_cache_valid(cache_path):
        cached = _read_cache(cache_path)
        if cached is not None:
            return cached

    # 2. Retry avec backoff
    sess = session or requests
    last_error = "Unknown error"

    for attempt in range(MAX_RETRIES):
        try:
            resp = sess.get(url, params=params, headers=headers, timeout=timeout)
            resp.raise_for_status()
            data = resp.json()

            # Écrire dans le cache
            if use_cache:
                _write_cache(cache_path, data)

            return data

        except requests.exceptions.Timeout:
            last_error = f"Timeout ({timeout}s)"
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            # Ne pas retry sur 4xx (client error)
            if 400 <= status < 500:
                return {"error": True, "reason": f"HTTP {status}: {e.response.text[:200]}"}
            last_error = f"HTTP {status}: {e.response.text[:200]}"
        except Exception as e:
            last_error = str(e)

        # Attendre avant retry (sauf dernier essai)
        if attempt < MAX_RETRIES - 1:
            sleep_time = BACKOFF_BASE * (2 ** attempt)
            time.sleep(sleep_time)

    # Tous les retries épuisés
    return {"error": True, "reason": f"Max retries ({MAX_RETRIES}) exceeded. Last: {last_error}"}


def clear_old_cache(days: int = 7) -> None:
    """Nettoie les caches de plus de N jours."""
    today = datetime.now(timezone.utc).date()
    for day_dir in CACHE_DIR.iterdir():
        if not day_dir.is_dir():
            continue
        try:
            dir_date = datetime.strptime(day_dir.name, "%Y-%m-%d").date()
            delta = (today - dir_date).days
            if delta > days:
                import shutil
                shutil.rmtree(day_dir)
        except Exception:
            continue


if __name__ == "__main__":
    # Test rapide
    print("Testing http_utils...")
    result = http_get(
        "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
        {"period1": "1700000000", "period2": "1800000000", "interval": "1d"},
        use_cache=True,
    )
    if result.get("error"):
        print(f"Error: {result.get('reason')}")
    else:
        print(f"Success: chart result received")
        print(f"Cache file: {_cache_path('https://query1.finance.yahoo.com/v8/finance/chart/AAPL', {'period1': '1700000000', 'period2': '1800000000', 'interval': '1d'})}")

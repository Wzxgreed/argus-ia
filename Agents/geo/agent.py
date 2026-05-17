#!/usr/bin/env python3
"""
agent_geo.py — Agent Politique / Géopolitique.

Protocol : `Agents/AGENT_GEO.md`

Scan les news pour détecter les événements politiques majeurs, cartographie
l'exposition de chaque ticker, et génère des scénarios avec probabilités.

Usage:
    python agents/geo/agent.py

Output:
    data/geo_risk_YYYY-MM-DD.json
"""

import sys
from pathlib import Path
_scripts = Path(__file__).resolve().parent.parent / 'scripts'
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

import json
import os
import re
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

# Regex patterns for political event detection
POLITICAL_PATTERNS = {
    "tariff": re.compile(r"tariffs?\s+(\d+)%?", re.IGNORECASE),
    "sanctions": re.compile(r"sanctions?\s+(?:on|against|sur)\s+(Russia|Iran|China|North Korea)", re.IGNORECASE),
    "war": re.compile(r"war|conflict|invasion|ceasefire|Hormuz|Gaza|Ukraine", re.IGNORECASE),
    "budget": re.compile(r"budget\s+(?:DoD|Pentagon|NATO|military|defense)\s+\$?\d+", re.IGNORECASE),
    "election": re.compile(r"election\s+\d{4}|midterms?|primary|poll", re.IGNORECASE),
    "chips": re.compile(r"CHIPS\s+Act|antitrust|EU\s+regulation|DMA|DSA", re.IGNORECASE),
    "energy": re.compile(r"oil\s+embargo|OPEC|energy\s+crisis|gas\s+pipeline", re.IGNORECASE),
}

# Sector exposure mapping
SECTOR_EXPOSURE = {
    "XOM": {"sectors": ["Energy"], "keywords": ["oil", "OPEC", "Iran", "Hormuz", "energy crisis"]},
    "RTX": {"sectors": ["Defense"], "keywords": ["NATO", "Pentagon", "defense budget", "war", "Hormuz"]},
    "NVDA": {"sectors": ["Tech"], "keywords": ["tariff", "China", "CHIPS Act", "antitrust"]},
    "VRT": {"sectors": ["Tech", "Infrastructure"], "keywords": ["tariff", "China", "energy", "permits"]},
    "IREN": {"sectors": ["Crypto", "Financial"], "keywords": ["regulation", "SEC", "mining", "energy"]},
    "AAPL": {"sectors": ["Tech"], "keywords": ["tariff", "China", "CHIPS Act", "antitrust", "DMA"]},
}


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_ticker_news(ticker: str, limit: int = 10) -> list[dict]:
    """Lit les news depuis data/news_latest.json (produit par agent_news_fetcher.py)."""
    news_path = DATA_DIR / "news_latest.json"
    if not news_path.exists():
        return []
    try:
        with open(news_path.resolve(), "r", encoding="utf-8") as f:
            data = json.load(f)
        items = data.get("news", {}).get(ticker, [])
        return items[:limit]
    except Exception:
        return []


def detect_political_events(news_items: list[dict]) -> list[dict]:
    """
    Analyse les news et détecte les événements politiques.
    Retourne une liste d'événements avec score.
    """
    events = []
    seen_titles = set()

    for item in news_items:
        title = item.get("title", "")
        summary = item.get("summary", "")
        text = f"{title} {summary}"

        if not title or title in seen_titles:
            continue
        seen_titles.add(title)

        score = 0
        matched_patterns = []

        for pattern_name, pattern in POLITICAL_PATTERNS.items():
            if pattern.search(text):
                score += 2  # +2 par pattern matched
                matched_patterns.append(pattern_name)

        if score > 0:
            # Ajuste le score selon la gravité
            if any(w in text.lower() for w in ["war", "invasion", "embargo", "sanctions"]):
                score += 3
            if any(w in text.lower() for w in ["tariff", "25%", "50%", "100%"]):
                score += 2

            events.append({
                "title": title,
                "summary": summary,
                "publisher": item.get("publisher", ""),
                "score": min(score, 10),
                "patterns": matched_patterns,
                "url": item.get("link", ""),
            })

    # Deduplicate by title and keep highest score
    unique_events = {}
    for ev in events:
        if ev["title"] not in unique_events or unique_events[ev["title"]]["score"] < ev["score"]:
            unique_events[ev["title"]] = ev

    return sorted(unique_events.values(), key=lambda x: x["score"], reverse=True)


def assess_ticker_exposure(ticker: str, events: list[dict]) -> dict:
    """
    Évalue l'exposition d'un ticker aux événements politiques détectés.
    """
    exposure = SECTOR_EXPOSURE.get(ticker, {"sectors": [], "keywords": []})
    relevant_events = []
    max_score = 0

    for ev in events:
        text = f"{ev['title']} {ev['summary']}".lower()
        # Check if event keywords match ticker exposure
        if any(kw in text for kw in exposure.get("keywords", [])):
            relevant_events.append(ev)
            if ev["score"] > max_score:
                max_score = ev["score"]

    # Default score if no direct match but sector exposed
    geo_risk_score = max_score if max_score > 0 else 2  # base risk for exposed sectors

    return {
        "ticker": ticker,
        "geo_risk_score": geo_risk_score,
        "exposed": len(relevant_events) > 0 or len(exposure.get("sectors", [])) > 0,
        "flag": "🔴" if geo_risk_score >= 7 else "🟡" if geo_risk_score >= 4 else "🟢",
        "relevant_events": relevant_events[:3],
        "sectors": exposure.get("sectors", []),
    }


def build_scenarios(ticker: str, event: dict) -> list[dict]:
    """Construit 3 scénarios pour un événement donné."""
    scenarios = [
        {
            "name": "Optimiste",
            "probability": 0.20,
            "impact_pct": +10,
            "description": f"Résolution diplomatique rapide de : {event['title']}",
        },
        {
            "name": "Central",
            "probability": 0.55,
            "impact_pct": -2,
            "description": f"Tension prolongée mais maîtrisée : {event['title']}",
        },
        {
            "name": "Pessimiste",
            "probability": 0.25,
            "impact_pct": -18,
            "description": f"Escalade majeure : {event['title']}",
        },
    ]
    return scenarios


def main():
    print("[geo] Starting geopolitical scan...", file=sys.stderr)

    config = load_config()
    tickers = [t["ticker"] for t in config.get("tickers", [])]

    all_events = []
    ticker_assessments = {}

    for ticker in tickers:
        print(f"[geo] Scanning {ticker}...", file=sys.stderr)
        news = get_ticker_news(ticker)
        events = detect_political_events(news)
        all_events.extend(events)

        assessment = assess_ticker_exposure(ticker, events)
        ticker_assessments[ticker] = assessment

        if assessment["relevant_events"]:
            print(
                f"[geo]   {ticker}: Score {assessment['geo_risk_score']}/10 "
                f"{assessment['flag']} — {len(assessment['relevant_events'])} event(s)",
                file=sys.stderr
            )

    # Deduplicate global events
    global_events = {}
    for ev in all_events:
        if ev["title"] not in global_events:
            global_events[ev["title"]] = ev

    # Build report
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report = {
        "meta": {
            "date": date_str,
            "events_detected": len(global_events),
            "tickers_flagged": sum(1 for a in ticker_assessments.values() if a["exposed"]),
        },
        "events": list(global_events.values())[:10],  # Top 10
        "ticker_exposure": ticker_assessments,
    }

    # Write report
    output_path = DATA_DIR / f"geo_risk_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "geo_risk_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    flagged = [t for t, a in ticker_assessments.items() if a["geo_risk_score"] >= 7]
    print(
        f"[geo] Report written → {output_path} | "
        f"Events: {len(global_events)} | Flagged: {len(flagged)}",
        file=sys.stderr
    )

    if flagged:
        print(f"[geo] 🔴 High geo-risk tickers: {', '.join(flagged)}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
agent_event_driven.py — Agent Event-Driven.

Protocol : `agents/event_driven/protocol.md`

Détecte et analyse les événements corporates structurants :
M&A, buybacks, spin-offs, activism (13D filings), changements de guidance,
settlements, FDA decisions.

Usage:
    python agents/event_driven/agent.py

Output:
    data/events_YYYY-MM-DD.json  (symlink latest)
    Alertes/EVENT_DRIVEN.md      (dashboard humain, optionnel)
"""

import sys
from pathlib import Path
_scripts = Path(__file__).resolve().parent.parent / 'scripts'
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
ALERTES_DIR = BASE_DIR / "Alertes"

# Keywords pour détection d'événements corporates
EVENT_KEYWORDS = {
    "merger": [
        "to acquire", "acquisition of", "merger with", "merger agreement",
        "to be acquired", "buyout", "takeover", "acquired by",
        "enters into merger", "definitive agreement", "all-cash deal",
    ],
    "buyback": [
        "buyback", "share repurchase", "stock repurchase",
        "authorization to repurchase", "$.* billion.* buyback",
        "buyback program", "repurchase program",
    ],
    "guidance_change": [
        "revised guidance", "updated guidance", "guidance update",
        "outlook update", "raises guidance", "lowers guidance",
        "cuts guidance", "withdraws guidance", "profit warning",
        "expects revenue", "expects earnings", "sees revenue",
    ],
    "activism": [
        "13d filing", "activist investor", "activist stake",
        "board nomination", "proxy fight", "letter to board",
        "push for sale", "urges sale", "demands changes",
        "starboard", "elliott", "icahn", "pershing", "third point",
    ],
    "spinoff": [
        "spin-off", "spin off", "spin-off", "divestiture",
        "to separate", "to split", "carve-out",
    ],
    "settlement": [
        "settlement", "reaches settlement", "agrees to pay",
        "class action settlement", "regulatory settlement",
        "doj settlement", "sec settlement", "fines", "to pay fine",
    ],
    "fda": [
        "fda approval", "fda rejection", "clinical trial results",
        "phase 3", "breakthrough therapy", "complete response letter",
        "crl", "drug approved", "drug rejected",
    ],
    "management_change": [
        "new ceo", "ceo departure", "ceo resign", "chief executive",
        "appointed ceo", "named ceo", "executive departure",
        "cfo departure", "cto departure", "new cfo",
    ],
}


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_ticker_news(ticker: str, limit: int = 15) -> list[dict]:
    """Lit les news depuis data/news_latest.json (produit par agent_news_fetcher.py)."""
    news_path = DATA_DIR / "news_latest.json"
    if not news_path.exists():
        return []
    try:
        with open(news_path.resolve(), "r", encoding="utf-8") as f:
            data = json.load(f)
        items = data.get("news", {}).get(ticker, [])
        news = []
        for item in items[:limit]:
            news.append({
                "title": item.get("title", ""),
                "summary": item.get("summary", ""),
                "publisher": item.get("publisher", ""),
                "link": item.get("link", ""),
            })
        return news
    except Exception as e:
        print(f"[event] Error reading news for {ticker}: {e}", file=sys.stderr)
        return []


def detect_events(news_items: list[dict]) -> list[dict]:
    """
    Analyse les news et détecte les événements corporates.
    Retourne une liste d'événements classifiés.
    """
    events = []
    seen_titles = set()

    for item in news_items:
        title = item.get("title", "")
        summary = item.get("summary", "")
        text = f"{title} {summary}".lower()

        if not title or title in seen_titles:
            continue
        seen_titles.add(title)

        for event_type, keywords in EVENT_KEYWORDS.items():
            for kw in keywords:
                if re.search(kw.lower(), text):
                    # Score de confiance
                    confidence = 5
                    if event_type == "merger" and any(w in text for w in ["agreement", "deal", "billion", "acquire"]):
                        confidence = 8
                    if event_type == "guidance_change" and any(w in text for w in ["raises", "lowers", "cuts", "withdraws"]):
                        confidence = 9
                    if event_type == "activism" and any(w in text for w in ["13d", "filing", "board"]):
                        confidence = 8
                    if event_type == "fda" and any(w in text for w in ["approval", "rejection"]):
                        confidence = 10

                    events.append({
                        "title": title,
                        "summary": summary,
                        "publisher": item.get("publisher", ""),
                        "event_type": event_type,
                        "confidence": min(confidence, 10),
                        "url": item.get("link", ""),
                        "matched_keyword": kw,
                    })
                    break  # Un seul event_type par news item

    # Deduplicate by title + event_type
    unique_events = {}
    for ev in events:
        key = f"{ev['title']}|{ev['event_type']}"
        if key not in unique_events or unique_events[key]["confidence"] < ev["confidence"]:
            unique_events[key] = ev

    return sorted(unique_events.values(), key=lambda x: x["confidence"], reverse=True)


def assess_event_impact(event: dict, ticker: str) -> dict:
    """
    Évalue l'impact estimé d'un événement sur le ticker.
    """
    event_type = event["event_type"]
    title = event["title"].lower()

    impact_direction = "neutral"
    impact_score = 0  # −10 à +10
    timeline = "unknown"
    probability = 50

    if event_type == "merger":
        if "to be acquired" in title or "acquired by" in title or "buyout" in title:
            impact_direction = "positive"
            impact_score = 7
            timeline = "3–12 months"
            probability = 60
        elif "to acquire" in title:
            impact_direction = "neutral_negative"  # Acquéreur souvent pénalisé
            impact_score = -2
            timeline = "3–12 months"
            probability = 60
        else:
            impact_direction = "positive"
            impact_score = 5
            timeline = "3–12 months"
            probability = 50

    elif event_type == "buyback":
        impact_direction = "positive"
        impact_score = 4
        timeline = "1–12 months"
        probability = 95  # Buyback annoncé = quasi certain

    elif event_type == "guidance_change":
        if any(w in title for w in ["raises", "raise", "boosts", "stronger"]):
            impact_direction = "positive"
            impact_score = 6
            timeline = "immediate"
            probability = 100
        elif any(w in title for w in ["lowers", "cuts", "weakens", "misses"]):
            impact_direction = "negative"
            impact_score = -6
            timeline = "immediate"
            probability = 100
        elif any(w in title for w in ["withdraws", "withdraw", "pulls"]):
            impact_direction = "negative"
            impact_score = -7
            timeline = "immediate"
            probability = 100
        else:
            impact_direction = "neutral"
            impact_score = 0
            timeline = "immediate"
            probability = 80

    elif event_type == "activism":
        impact_direction = "positive"
        impact_score = 5
        timeline = "3–18 months"
        probability = 55

    elif event_type == "spinoff":
        impact_direction = "positive"
        impact_score = 4
        timeline = "6–12 months"
        probability = 80

    elif event_type == "settlement":
        if any(w in title for w in ["reaches settlement", "settlement agreement"]):
            impact_direction = "positive"
            impact_score = 3
            timeline = "immediate"
            probability = 100
        else:
            impact_direction = "negative"
            impact_score = -3
            timeline = "immediate"
            probability = 100

    elif event_type == "fda":
        if "approval" in title:
            impact_direction = "positive"
            impact_score = 9
            timeline = "immediate"
            probability = 100
        elif "rejection" in title or "crl" in title or "complete response" in title:
            impact_direction = "negative"
            impact_score = -8
            timeline = "immediate"
            probability = 100
        else:
            impact_direction = "neutral"
            impact_score = 0
            timeline = "immediate"
            probability = 50

    elif event_type == "management_change":
        if any(w in title for w in ["ceo departure", "ceo resign", "executive departure"]):
            impact_direction = "negative"
            impact_score = -4
            timeline = "1–3 months"
            probability = 100
        elif any(w in title for w in ["new ceo", "appointed ceo"]):
            impact_direction = "neutral"
            impact_score = 0
            timeline = "1–6 months"
            probability = 100
        else:
            impact_direction = "neutral"
            impact_score = 0
            timeline = "1–3 months"
            probability = 100

    return {
        "impact_direction": impact_direction,
        "impact_score": impact_score,
        "timeline": timeline,
        "probability": probability,
    }


def main():
    print("[event] Starting event-driven scan...", file=sys.stderr)

    config = load_config()
    tickers_data = config.get("tickers", [])

    all_events = []
    ticker_events = {}

    for ticker_data in tickers_data:
        ticker = ticker_data["ticker"]
        print(f"[event] Scanning {ticker}...", file=sys.stderr)

        news = get_ticker_news(ticker)
        events = detect_events(news)

        ticker_events[ticker] = []
        for ev in events:
            impact = assess_event_impact(ev, ticker)
            ev.update(impact)
            ticker_events[ticker].append(ev)
            all_events.append(ev)

        if events:
            print(
                f"[event]   {ticker}: {len(events)} event(s) detected — "
                f"top: {events[0]['event_type']} (confidence {events[0]['confidence']}/10)",
                file=sys.stderr
            )

    # Build report
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Summarize by ticker
    ticker_summary = {}
    for ticker, events in ticker_events.items():
        if events:
            top_event = events[0]
            ticker_summary[ticker] = {
                "event_count": len(events),
                "top_event_type": top_event["event_type"],
                "top_event_confidence": top_event["confidence"],
                "top_event_impact_score": top_event["impact_score"],
                "events": events,
            }

    report = {
        "meta": {
            "date": date_str,
            "tickers_scanned": len(tickers_data),
            "tickers_with_events": len(ticker_summary),
            "total_events": len(all_events),
        },
        "ticker_events": ticker_summary,
        "all_events": all_events[:20],  # Top 20 globaux
    }

    # Write report
    output_path = DATA_DIR / f"events_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "events_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    # Write human-readable dashboard
    event_md = ALERTES_DIR / "EVENT_DRIVEN.md"
    with open(event_md, "w", encoding="utf-8") as f:
        f.write(f"# Event-Driven Dashboard — {date_str}\n\n")
        f.write(f"**Tickers scannés :** {len(tickers_data)} | **Avec événements :** {len(ticker_summary)}\n\n")

        if ticker_summary:
            f.write("## Événements par ticker\n\n")
            for ticker, summary in sorted(
                ticker_summary.items(),
                key=lambda x: abs(x[1]["top_event_impact_score"]),
                reverse=True,
            ):
                f.write(f"### {ticker}\n")
                f.write(f"- **Top événement :** {summary['top_event_type']} (confiance {summary['top_event_confidence']}/10)\n")
                f.write(f"- **Impact estimé :** {summary['top_event_impact_score']:+d}/10\n")
                f.write(f"- **Nombre d'événements :** {summary['event_count']}\n")
                for ev in summary["events"][:3]:
                    f.write(f"  - [{ev['event_type'].upper()}] {ev['title']}\n")
                f.write("\n")
        else:
            f.write("Aucun événement corporate détecté aujourd'hui.\n")

    print(
        f"[event] Report written → {output_path} | "
        f"Dashboard → {event_md} | "
        f"Events: {len(all_events)} | Tickers: {len(ticker_summary)}",
        file=sys.stderr
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
agent_geo.py — Agent Politique / Géopolitique.

Protocol : `Agents/AGENT_GEO.md`

Scan les news pour détecter les événements politiques majeurs, cartographie
l'exposition de chaque ticker, et génère des scénarios avec probabilités.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from agents.base import BaseAgent
from agents.schemas import GeoEvent, GeoRiskReport, Meta, TickerExposure


class GeoAgent(BaseAgent):
    name = "geo"
    output_schema = GeoRiskReport

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

    SECTOR_EXPOSURE = {
        "XOM": {"sectors": ["Energy"], "keywords": ["oil", "OPEC", "Iran", "Hormuz", "energy crisis"]},
        "RTX": {"sectors": ["Defense"], "keywords": ["NATO", "Pentagon", "defense budget", "war", "Hormuz"]},
        "NVDA": {"sectors": ["Tech"], "keywords": ["tariff", "China", "CHIPS Act", "antitrust"]},
        "VRT": {"sectors": ["Tech", "Infrastructure"], "keywords": ["tariff", "China", "energy", "permits"]},
        "IREN": {"sectors": ["Crypto", "Financial"], "keywords": ["regulation", "SEC", "mining", "energy"]},
        "AAPL": {"sectors": ["Tech"], "keywords": ["tariff", "China", "CHIPS Act", "antitrust", "DMA"]},
    }

    def get_ticker_news(self, ticker: str, limit: int = 10) -> list[dict]:
        news_path = self.data_dir / "news_latest.json"
        if not news_path.exists():
            return []
        try:
            with open(news_path.resolve(), "r", encoding="utf-8") as f:
                data = json.load(f)
            items = data.get("news", {}).get(ticker, [])
            return items[:limit]
        except Exception:
            return []

    def detect_political_events(self, news_items: list[dict]) -> list[GeoEvent]:
        events: list[GeoEvent] = []
        seen_titles: set[str] = set()

        for item in news_items:
            title = item.get("title", "")
            summary = item.get("summary", "")
            text = f"{title} {summary}"

            if not title or title in seen_titles:
                continue
            seen_titles.add(title)

            score = 0
            matched_patterns: list[str] = []

            for pattern_name, pattern in self.POLITICAL_PATTERNS.items():
                if pattern.search(text):
                    score += 2
                    matched_patterns.append(pattern_name)

            if score > 0:
                if any(w in text.lower() for w in ["war", "invasion", "embargo", "sanctions"]):
                    score += 3
                if any(w in text.lower() for w in ["tariff", "25%", "50%", "100%"]):
                    score += 2

                events.append(GeoEvent(
                    title=title,
                    summary=summary,
                    publisher=item.get("publisher", ""),
                    score=min(score, 10),
                    patterns=matched_patterns,
                    url=item.get("link", ""),
                ))

        unique_events: dict[str, GeoEvent] = {}
        for ev in events:
            key = ev.title
            if key not in unique_events or unique_events[key].score < ev.score:
                unique_events[key] = ev

        return sorted(unique_events.values(), key=lambda x: x.score, reverse=True)

    def assess_ticker_exposure(self, ticker: str, events: list[GeoEvent]) -> TickerExposure:
        exposure = self.SECTOR_EXPOSURE.get(ticker, {"sectors": [], "keywords": []})
        relevant_events: list[GeoEvent] = []
        max_score = 0

        for ev in events:
            text = f"{ev.title} {ev.summary}".lower()
            if any(kw in text for kw in exposure.get("keywords", [])):
                relevant_events.append(ev)
                if ev.score > max_score:
                    max_score = ev.score

        geo_risk_score = max_score if max_score > 0 else 2

        return TickerExposure(
            ticker=ticker,
            geo_risk_score=geo_risk_score,
            exposed=len(relevant_events) > 0 or len(exposure.get("sectors", [])) > 0,
            flag="🔴" if geo_risk_score >= 7 else "🟡" if geo_risk_score >= 4 else "🟢",
            relevant_events=relevant_events[:3],
            sectors=exposure.get("sectors", []),
        )

    def run(self) -> GeoRiskReport:
        self.log("INFO", "start")
        tickers = self.tickers()
        all_events: list[GeoEvent] = []
        ticker_assessments: dict[str, TickerExposure] = {}

        for ticker in tickers:
            news = self.get_ticker_news(ticker)
            events = self.detect_political_events(news)
            all_events.extend(events)

            assessment = self.assess_ticker_exposure(ticker, events)
            ticker_assessments[ticker] = assessment

            if assessment.relevant_events:
                self.log(
                    "INFO",
                    "ticker_scanned",
                    ticker=ticker,
                    score=assessment.geo_risk_score,
                    events=len(assessment.relevant_events),
                )

        global_events: dict[str, GeoEvent] = {}
        for ev in all_events:
            if ev.title not in global_events:
                global_events[ev.title] = ev

        flagged = [t for t, a in ticker_assessments.items() if a.geo_risk_score >= 7]
        self.log(
            "INFO",
            "complete",
            events=len(global_events),
            flagged=len(flagged),
        )

        return GeoRiskReport(
            meta=Meta(date=self.date_str, agent=self.name),
            events=list(global_events.values())[:10],
            ticker_exposure=ticker_assessments,
        )


if __name__ == "__main__":
    sys.exit(GeoAgent.cli_entry())

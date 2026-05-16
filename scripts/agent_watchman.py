#!/usr/bin/env python3
"""
agent_watchman.py — Surveillance proactive des événements à venir par ticker.

Périmètre :
  • Earnings dates (calendrier FMP + Yahoo, 30j)
  • News scan proactif : CEO, M&A, guidance, partnerships, investor day, FDA, etc.
  • Insider trades significatifs (FMP, >$1M ou >0.5% float)
  • Upgrades / downgrades récents (FMP)
  • Contrats gouvernementaux, sanctions, tarifs (news regex)

Seuils d'action :
  ≤ 3 jours → 🔴 Critique → génère _preview.md + alerte
  ≤ 7 jours → 🟡 Proche → log UPCOMING_EVENTS.md
  ≤ 30 jours → 🟢 Radar → log UPCOMING_EVENTS.md

Output :
  data/upcoming_events_YYYY-MM-DD.json  (symlink latest)
  Alertes/UPCOMING_EVENTS.md            (dashboard humain)
  Actions/[TICKER]/[TICKER]_YYYY-MM-DD_preview.md  (auto-généré si ≤ 3j)
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yfinance as yf

from fmp_client import FMPClient

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
ALERTES_DIR = BASE_DIR / "Alertes"

# Keywords futurs (anglais + français) pour la détection proactive
FUTURE_KEYWORDS = [
    "will announce", "scheduled to", "expects to", "upcoming",
    "investor day", "annual meeting", "shareholder meeting",
    "to report", "earnings call", "conference call",
    "new contract", "awarded contract", "government contract",
    "partnership with", "joint venture", "collaboration with",
    "new ceo", "new chief executive", "appointed ceo", "named ceo",
    "ceo departure", "ceo resign", "executive departure",
    "fda approval", "phase 3", "clinical trial results",
    "guidance update", "revised guidance", "outlook update",
    "stock split", "dividend increase", "buyback program",
    "tariff", "sanction", "export ban", "trade war",
    "acquisition of", "to acquire", "merger with", "spin-off",
    "new facility", "expansion", "capacity increase",
    "insider buying", "insider purchase", "director bought",
    "13f", "institutional holding", "new stake",
    "upgrade to", "downgrade to", "price target raised", "price target cut",
    "analyst reiterates", "bullish", "bearish",
]

# Seuils insider trades
INSIDER_VALUE_THRESHOLD = 1_000_000   # $1M
INSIDER_SHARES_PCT_THRESHOLD = 0.005  # 0.5% du float


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def parse_date(date_val) -> str | None:
    """Parse divers formats de date en YYYY-MM-DD."""
    if date_val is None:
        return None
    if isinstance(date_val, str):
        # Essaie plusieurs formats
        for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y", "%d/%m/%Y"):
            try:
                return datetime.strptime(date_val[:10] if len(date_val) > 10 else date_val, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        return None
    if hasattr(date_val, "strftime"):
        return date_val.strftime("%Y-%m-%d")
    return None


def days_until(date_str: str) -> int | None:
    """Calcule le nombre de jours entre aujourd'hui et date_str."""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
        return (d - datetime.now(timezone.utc).date()).days
    except Exception:
        return None


def is_future_date(date_str: str) -> bool:
    """Vérifie que la date est aujourd'hui ou dans le futur."""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
        return d >= datetime.now(timezone.utc).date()
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Source 1 — Earnings Calendar (FMP + Yahoo)
# ---------------------------------------------------------------------------

def fetch_earnings_fmp(fmp: FMPClient, ticker: str) -> list[dict]:
    """Récupère le calendrier earnings via FMP Stable API."""
    data = fmp._get("earnings-calendar", {
        "symbol": ticker,
        "from": today_str(),
        "to": (datetime.now(timezone.utc) + timedelta(days=30)).strftime("%Y-%m-%d")
    })
    if isinstance(data, list):
        events = []
        seen_dates = set()
        for item in data:
            date = parse_date(item.get("date"))
            if not date or date in seen_dates or not is_future_date(date):
                continue
            # Accepter même sans estimate (Starter plan peut ne pas les fournir)
            eps = item.get("epsEstimate")
            rev = item.get("revenueEstimate")
            seen_dates.add(date)
            details = f"Earnings {item.get('fiscalDateEnding', '')}"
            if eps:
                details += f" — Est EPS ${eps}"
            if rev:
                details += f", Rev ${rev}"
            events.append({
                "type": "earnings",
                "date": date,
                "details": details,
                "source": "fmp",
                "severity": "high",
            })
        return events
    return []


def fetch_earnings_yahoo(ticker: str) -> list[dict]:
    """Récupère le calendrier earnings via Yahoo Finance."""
    try:
        stock = yf.Ticker(ticker)
        cal = stock.calendar
        if cal is None:
            return []
        events = []
        seen = set()
        # Nouveau format yfinance : dict avec Earnings Date = [date, ...]
        if isinstance(cal, dict):
            raw_dates = cal.get("Earnings Date")
            if raw_dates:
                if not isinstance(raw_dates, list):
                    raw_dates = [raw_dates]
                for d in raw_dates:
                    date = parse_date(d)
                    if date and date not in seen:
                        seen.add(date)
                        # Extraire les estimates si dispo
                        eps_low = cal.get("Earnings Low")
                        eps_high = cal.get("Earnings High")
                        rev_avg = cal.get("Revenue Average")
                        details = "Earnings date"
                        if eps_low and eps_high:
                            details += f" — Est EPS ${eps_low:.2f}-${eps_high:.2f}"
                        if rev_avg:
                            details += f", Rev ${rev_avg/1e9:.1f}B"
                        if is_future_date(date):
                            events.append({
                                "type": "earnings",
                                "date": date,
                                "details": details,
                                "source": "yfinance",
                                "severity": "high",
                            })
        # Ancien format DataFrame (rare mais au cas où)
        elif hasattr(cal, "iterrows"):
            for _, row in cal.iterrows():
                date_val = row.get("Earnings Date") or row.get("Earnings Date Low") or row.get("earningsDate")
                date = parse_date(date_val)
                if date and date not in seen and is_future_date(date):
                    seen.add(date)
                    events.append({
                        "type": "earnings",
                        "date": date,
                        "details": "Earnings date (Yahoo Finance)",
                        "source": "yfinance",
                        "severity": "high",
                    })
        return events
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Source 2 — News Scan Proactif
# ---------------------------------------------------------------------------

def scan_news_proactive(ticker: str) -> list[dict]:
    """
    Lit les news depuis data/news_latest.json (produit par agent_news_fetcher.py)
    pour détecter les événements futurs.
    """
    news_path = DATA_DIR / "news_latest.json"
    if not news_path.exists():
        return []

    try:
        with open(news_path.resolve(), "r", encoding="utf-8") as f:
            data = json.load(f)
        news = data.get("news", {}).get(ticker, [])
    except Exception:
        return []

    events = []
    seen_titles = set()
    for item in news:
        title = (item.get("title") or "").lower()
        summary = (item.get("summary") or "").lower()
        if not title:
            continue
        if title in seen_titles:
            continue
        seen_titles.add(title)
        text = title + " " + summary
        matched = [kw for kw in FUTURE_KEYWORDS if kw in text]
        if matched:
            severity = "medium"
            if any(k in text for k in ["ceo", "acquisition", "merger", "fda", "guidance", "bankruptcy"]):
                severity = "high"
            date_mention = None
            date_patterns = [
                r"(\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]* \d{1,2}\b)",
                r"(\bq[1-4]\s+20\d{2}\b)",
                r"(\bnext\s+(?:week|month|quarter)\b)",
            ]
            for pat in date_patterns:
                m = re.search(pat, text)
                if m:
                    date_mention = m.group(1)
                    break
            raw_title = item.get("title", "")
            pub_date = item.get("published")
            events.append({
                "type": f"news_{'_'.join(matched[0].split())}",
                "date": None,
                "details": f"News: {raw_title}" + (f" [event: {date_mention}]" if date_mention else ""),
                "source": "yahoo_news",
                "severity": severity,
                "news_date": parse_date(pub_date),
            })
    return events


# ---------------------------------------------------------------------------
# Source 3 — Insider Trades (FMP)
# ---------------------------------------------------------------------------

def fetch_insider_trades(fmp: FMPClient, ticker: str) -> list[dict]:
    """
    Récupère les insider trades récents via FMP.
    Filtre les transactions significatives (>$1M ou >0.5% float).
    """
    data = fmp._get("insider-trading", {"symbol": ticker, "limit": 20})
    if not isinstance(data, list):
        return []
    events = []
    for item in data:
        transaction = item.get("transactionType", "").lower()
        # On garde seulement les achats/ventes (pas les grants, exercises)
        if "purchase" not in transaction and "sale" not in transaction:
            continue
        value = item.get("dollarValue", 0) or 0
        shares = item.get("securitiesTransacted", 0) or 0
        price = item.get("transactionPrice", 0) or 0
        # Si value n'est pas fourni, calculer
        if value == 0 and shares and price:
            value = shares * price
        if value >= INSIDER_VALUE_THRESHOLD:
            side = "buy" if "purchase" in transaction else "sell"
            events.append({
                "type": f"insider_{side}",
                "date": parse_date(item.get("transactionDate")),
                "details": f"Insider {side.upper()} {shares:,} shares @ ${price:.2f} = ${value:,.0f} ({item.get('reportingName', 'Unknown')})",
                "source": "fmp_insider",
                "severity": "high" if value >= 5_000_000 else "medium",
                "value": value,
            })
    return events


# ---------------------------------------------------------------------------
# Source 4 — Upgrades / Downgrades (FMP)
# ---------------------------------------------------------------------------

def fetch_upgrades_downgrades(fmp: FMPClient, ticker: str) -> list[dict]:
    """Récupère les changements de ratings analystes récents."""
    data = fmp._get("upgrades-downgrades", {"symbol": ticker, "limit": 10})
    if not isinstance(data, list):
        return []
    events = []
    for item in data:
        old_rating = item.get("previousRating", "")
        new_rating = item.get("newRating", "")
        firm = item.get("publishingFirm", "")
        # Seulement si c'est un changement significatif (upgrade/downgrade, pas reiterate)
        if old_rating and new_rating and old_rating != new_rating:
            # Déterminer si upgrade ou downgrade
            upgrade_terms = ["buy", "overweight", "outperform", "strong buy"]
            downgrade_terms = ["sell", "underweight", "underperform", "strong sell"]
            old_up = any(t in old_rating.lower() for t in upgrade_terms)
            new_up = any(t in new_rating.lower() for t in upgrade_terms)
            old_down = any(t in old_rating.lower() for t in downgrade_terms)
            new_down = any(t in new_rating.lower() for t in downgrade_terms)
            direction = None
            if (old_down or not old_up) and new_up:
                direction = "upgrade"
            elif (old_up or not old_down) and new_down:
                direction = "downgrade"
            elif "hold" in old_rating.lower() and new_up:
                direction = "upgrade"
            elif "hold" in old_rating.lower() and new_down:
                direction = "downgrade"
            if direction:
                events.append({
                    "type": f"analyst_{direction}",
                    "date": parse_date(item.get("publishedDate")),
                    "details": f"{firm}: {old_rating} → {new_rating}",
                    "source": "fmp_analyst",
                    "severity": "medium",
                })
    return events


# ---------------------------------------------------------------------------
# Consolidation & scoring
# ---------------------------------------------------------------------------

def consolidate_events(ticker: str, events: list[dict]) -> list[dict]:
    """
    Déduplique et priorise les événements.
    Retourne une liste triée par severity et days_until.
    """
    # Dédup simple : même type + même date
    seen = set()
    deduped = []
    for ev in events:
        key = f"{ev['type']}:{ev.get('date', 'none')}"
        if key in seen:
            continue
        seen.add(key)
        ev["ticker"] = ticker
        ev["days_until"] = days_until(ev["date"]) if ev.get("date") else None
        deduped.append(ev)
    # Tri : severity puis days_until (None = 999)
    severity_order = {"high": 0, "medium": 1, "low": 2}
    def sort_key(x):
        sev = severity_order.get(x.get("severity", "low"), 2)
        days = x.get("days_until")
        return (sev, days if days is not None else 999)
    deduped.sort(key=sort_key)
    return deduped


# ---------------------------------------------------------------------------
# Auto-generation helpers
# ---------------------------------------------------------------------------

def generate_preview(ticker: str, event: dict) -> Path | None:
    """Génère un _preview.md si earnings ou event majeur est dans ≤ 3 jours."""
    days = event.get("days_until")
    if days is None or days > 3:
        return None
    if event["type"] not in ("earnings", "news_ceo_departure", "news_new_ceo", "news_fda_approval", "insider_buy", "insider_sell"):
        # Pour l'instant, previews auto seulement pour earnings + event structurant immédiat
        pass

    action_dir = BASE_DIR / "Actions" / ticker
    action_dir.mkdir(parents=True, exist_ok=True)
    date_str = today_str()

    content = f"""# {ticker} — Preview Événement ({event['type']})

> **Date :** {date_str}
> **Événement :** {event['details']}
> **Date prévue :** {event.get('date', 'ASAP')} ({days}j)
> **Source :** {event['source']}

---

## Prédictions (à compléter avant l'événement)

| Métrique | Prédiction | Consensus | Surprise attendue |
|----------|-----------|-----------|-------------------|
| Revenue  | $XX.XB    | $XX.XB    | [beat/miss/in-line] |
| EPS      | $X.XX     | $X.XX     | [beat/miss/in-line] |
| Guidance | [raise/lower/maintain] | — | — |
| GM       | XX.X%     | XX.X%     | — |

---

## Scénarios post-événement

| Scénario | Probabilité | Impact cours | Action |
|----------|------------|--------------|--------|
| Beat + guidance up | 30% | +8-12% | Renforcer / acheter |
| In-line | 45% | +1-3% | Hold |
| Miss / guidance down | 25% | -8-15% | Réviser stop-loss |

---

## ⚡ Règle
Sauvegarder les prédictions ci-dessus dans `Actions/SUIVI_EARNINGS_PREDICTIONS.md`.
Après l'événement, comparer prédictions vs réalité dans ce fichier.
"""
    preview_path = action_dir / f"{ticker}_{date_str}_preview.md"
    preview_path.write_text(content, encoding="utf-8")
    print(f"[watchman] Auto-generated preview → {preview_path}", file=sys.stderr)
    return preview_path


def generate_update_for_event(ticker: str, event: dict) -> Path | None:
    """Génère un _update.md immédiat pour un événement déjà survenu (CEO, insider, etc.)."""
    if event.get("days_until") is not None and event["days_until"] > 0:
        return None  # C'est un event futur, pas un event passé
    # Seulement pour les news CEO/insider/analyst qui sont déjà arrivés
    if event["type"] not in ("news_ceo_departure", "news_new_ceo", "insider_buy", "insider_sell", "analyst_upgrade", "analyst_downgrade"):
        return None

    action_dir = BASE_DIR / "Actions" / ticker
    action_dir.mkdir(parents=True, exist_ok=True)
    date_str = today_str()

    content = f"""# {ticker} — Mise à jour Flash ({event['type']})

> **Date :** {date_str}
> **Événement :** {event['details']}
> **Source :** {event['source']}
> **Impact estimé :** [À compléter]

---

## Analyse rapide

**Thèse impactée ?** [Oui / Non / Partiellement]
**Direction de l'impact :** [Positif / Négatif / Neutre]
**Révision prix cible :** [Oui → nouveau $XX / Non]

---

## Actions recommandées

- [ ] Relire `data/latest.json` pour données actualisées
- [ ] Scanner news complémentaires sur le sujet
- [ ] Mettre à jour `INDEX.md` si la thèse change
- [ ] Logger dans `Actions/{ticker}/REFRESH_LOG.md` si structurant
"""
    update_path = action_dir / f"{ticker}_{date_str}_update.md"
    update_path.write_text(content, encoding="utf-8")
    print(f"[watchman] Auto-generated flash update → {update_path}", file=sys.stderr)
    return update_path


# ---------------------------------------------------------------------------
# Markdown dashboard
# ---------------------------------------------------------------------------

def build_dashboard(all_events: list[dict]) -> str:
    """Construit le markdown UPCOMING_EVENTS.md."""
    today = today_str()
    critical = [e for e in all_events if e.get("days_until") is not None and e["days_until"] <= 3]
    near = [e for e in all_events if e.get("days_until") is not None and 3 < e["days_until"] <= 7]
    radar = [e for e in all_events if e.get("days_until") is not None and 7 < e["days_until"] <= 30]
    undated = [e for e in all_events if e.get("days_until") is None]

    def row(ev):
        days = ev.get("days_until")
        days_str = f"{days}j" if days is not None else "?"
        return f"| {ev['ticker']} | {ev['type']} | {ev.get('date', '—')} | {days_str} | {ev['details'][:60]}... | {ev['source']} |\n"

    md = f"""# 🔭 Événements à venir — Watchlist Argus-IA

> **Date :** {today}
> **Tickers scannés :** {len({e['ticker'] for e in all_events})}
> **Événements détectés :** {len(all_events)}

---

## 🔴 ≤ 3 jours — Action immédiate requise

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
"""
    for ev in critical:
        md += row(ev)
    if not critical:
        md += "| — | — | — | — | — | — |\n"

    md += """
---

## 🟡 ≤ 7 jours — Surveillance renforcée

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
"""
    for ev in near:
        md += row(ev)
    if not near:
        md += "| — | — | — | — | — | — |\n"

    md += """
---

## 🟢 ≤ 30 jours — Radar

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
"""
    for ev in radar:
        md += row(ev)
    if not radar:
        md += "| — | — | — | — | — | — |\n"

    md += """
---

## ❓ Sans date précise — Détectés dans les news

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
"""
    for ev in undated:
        md += row(ev)
    if not undated:
        md += "| — | — | — | — | — | — |\n"

    md += """
---

## Workflow

1. **Chaque matin** : lire cette page. Si un événement passe de 🟢 → 🟡 ou 🟡 → 🔴, préparer l'analyse.
2. **🔴 ≤ 3j** : `agent_watchman.py` génère automatiquement un `_preview.md` si c'est un earnings ou un catalyseur structurant.
3. **Post-événement** : lire `data/latest.json` + `data/transcripts_NLP_latest.json` puis générer `_earnings.md` ou `_update.md`.
4. **Nouveau CEO / Insider major / Analyste** : `agent_watchman.py` génère automatiquement un `_update.md` flash.
"""
    return md


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("[watchman] Starting proactive watchman scan...", file=sys.stderr)
    config = load_config()
    tickers = [t["ticker"] for t in config.get("tickers", [])]
    fmp = FMPClient()
    fmp_active = bool(fmp.api_key)

    all_events = []
    previews_generated = 0
    updates_generated = 0

    for ticker in tickers:
        print(f"[watchman] Scanning {ticker}...", file=sys.stderr)
        ticker_events = []

        # 1. Earnings (Yahoo principal, FMP fallback)
        earnings_events = fetch_earnings_yahoo(ticker)
        if not earnings_events and fmp_active:
            earnings_events = fetch_earnings_fmp(fmp, ticker)
        ticker_events.extend(earnings_events)

        # 2. News proactif
        news_events = scan_news_proactive(ticker)
        ticker_events.extend(news_events)

        # 3. Insider trades (FMP)
        if fmp_active:
            insider_events = fetch_insider_trades(fmp, ticker)
            ticker_events.extend(insider_events)

        # 4. Upgrades/downgrades (FMP)
        if fmp_active:
            analyst_events = fetch_upgrades_downgrades(fmp, ticker)
            ticker_events.extend(analyst_events)

        # Consolidation
        consolidated = consolidate_events(ticker, ticker_events)
        # Déduplication spéciale earnings : un seul earnings par ticker (le plus proche)
        earnings_events = [e for e in consolidated if e["type"] == "earnings"]
        if len(earnings_events) > 1:
            # Garder seulement l'earnings le plus proche (days_until min)
            best = min(earnings_events, key=lambda e: e.get("days_until", 999))
            consolidated = [e for e in consolidated if e["type"] != "earnings"] + [best]
        # Limite bruit (max 10 events par ticker, plus sévères d'abord)
        consolidated.sort(key=lambda x: ({"high": 0, "medium": 1, "low": 2}.get(x.get("severity", "low"), 2), x.get("days_until") if x.get("days_until") is not None else 999))
        consolidated = consolidated[:10]
        all_events.extend(consolidated)

        print(f"[watchman]   {ticker}: {len(consolidated)} event(s)", file=sys.stderr)

        # Auto-generation — un seul preview par ticker max
        preview_done = False
        for ev in consolidated:
            days = ev.get("days_until")
            # Preview auto pour le premier earnings ≤ 3j (un seul par ticker)
            if not preview_done and ev["type"] == "earnings" and days is not None and days <= 3:
                if generate_preview(ticker, ev):
                    previews_generated += 1
                    preview_done = True
            # Update flash pour événements déjà survenus
            if days is not None and days <= 0:
                if generate_update_for_event(ticker, ev):
                    updates_generated += 1

    # Write JSON report
    date_str = today_str()
    report = {
        "meta": {
            "date": date_str,
            "tickers_scanned": len(tickers),
            "events_total": len(all_events),
            "previews_auto": previews_generated,
            "updates_auto": updates_generated,
        },
        "events": all_events,
    }
    output_path = DATA_DIR / f"upcoming_events_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "upcoming_events_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    # Write dashboard markdown
    dashboard_md = build_dashboard(all_events)
    dashboard_path = ALERTES_DIR / "UPCOMING_EVENTS.md"
    dashboard_path.write_text(dashboard_md, encoding="utf-8")

    print(
        f"[watchman] Report → {output_path} | "
        f"Events: {len(all_events)} | "
        f"Previews auto: {previews_generated} | "
        f"Updates flash: {updates_generated} | "
        f"Dashboard → {dashboard_path}",
        file=sys.stderr
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

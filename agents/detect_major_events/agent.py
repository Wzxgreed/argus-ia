#!/usr/bin/env python3
"""
detect_major_events.py — Détection automatique d'événements majeurs nécessitant un full refresh.

Triggers d'événements majeurs :
  1. Gap prix > ±5% overnight (news majeure, earnings surprise, guidance)
  2. Volume > 3× moyenne 20j (réaction institutionnelle massive)
  3. ATR relatif > 5% (volatilité anormale)
  4. News keywords : acquisition, merger, CEO, guidance, bankruptcy, FDA, sanction, tariff
  5. Earnings surprise > 20% (FMP si disponible, sinon proxy par gap prix)
  6. Golden/Death cross (changement de tendance structurel)

Output:
  Actions/[TICKER]/[TICKER]_YYYY-MM-DD_DRAFT_refresh.md  → full re-analyse
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yfinance as yf

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"

# Seuils de déclenchement
TRIGGER_GAP_PCT = 5.0          # Gap overnight > 5%
TRIGGER_VOLUME_MULT = 3.0      # Volume > 3× moyenne 20j
TRIGGER_ATR_REL = 5.0          # ATR / close > 5%
TRIGGER_EARNINGS_SURPRISE = 20.0  # Surprise EPS > 20% (si données dispo)

# Keywords déclencheurs dans les news
NEWS_KEYWORDS = [
    "acquisition", "acquire", "merger", "merge", "takeover",
    "ceo", "chief executive", "depart", "resign", "new ceo",
    "guidance", "forecast", "outlook", "raised guidance", "lowered guidance",
    "bankruptcy", "chapter 11", "restructuring",
    "fda", "approval", "clinical trial", "phase 3",
    "sanction", "tariff", "export ban", "investigation", "antitrust",
    "partnership", "deal", "contract", "agreement", "joint venture",
    "spin-off", "divestiture", "ipo", "offering",
    "buyback", "dividend", "split",
]


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_latest() -> dict:
    """Lit le snapshot du jour (produit par fetch_prices.py)."""
    latest = DATA_DIR / "latest.json"
    if not latest.exists():
        return {}
    try:
        with open(latest, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def scan_news_keywords(ticker: str) -> list[str]:
    """Scanne les news yfinance et retourne les keywords matchés."""
    try:
        stock = yf.Ticker(ticker)
        news = stock.news or []
        matches = []
        for item in news:
            title = (item.get("title") or "").lower()
            summary = (item.get("summary") or "").lower()
            text = title + " " + summary
            for kw in NEWS_KEYWORDS:
                if kw in text and kw not in matches:
                    matches.append(kw)
        return matches
    except Exception:
        return []


def check_earnings_surprise(ticker: str) -> dict | None:
    """
    Tente de récupérer le dernier earnings surprise via FMP Stable.
    Retourne un dict avec surprise_pct ou None si indisponible.
    """
    # TODO: si FMP ajoute un endpoint stable pour earnings-surprises, l'implémenter ici
    # Pour l'instant, on utilise le gap prix comme proxy
    return None


def detect_triggers(ticker: str, snapshot: dict) -> list[dict]:
    """
    Analyse un ticker et retourne la liste des triggers déclenchés.
    Chaque trigger = {"type": str, "severity": str, "details": str}
    """
    triggers = []
    data = snapshot.get("prices", {}).get(ticker, {})
    if data.get("error"):
        return triggers

    price = data.get("price", {})
    tech = data.get("technical", {})

    # 1. Gap prix
    change_pct = price.get("change_pct")
    if change_pct is not None and abs(change_pct) >= TRIGGER_GAP_PCT:
        triggers.append({
            "type": "price_gap",
            "severity": "high" if abs(change_pct) >= 10 else "medium",
            "details": f"Gap {change_pct:+.2f}% overnight (seuil ±{TRIGGER_GAP_PCT}%)",
        })

    # 2. Volume surge
    vol = price.get("volume")
    vol_avg = price.get("volume_avg_20d")
    if vol and vol_avg and vol_avg > 0:
        mult = vol / vol_avg
        if mult >= TRIGGER_VOLUME_MULT:
            triggers.append({
                "type": "volume_surge",
                "severity": "high" if mult >= 5 else "medium",
                "details": f"Volume {mult:.1f}× moyenne 20j ({vol:,} vs {vol_avg:,})",
            })

    # 3. ATR relatif
    atr = tech.get("atr14")
    close = price.get("close")
    if atr and close and close > 0:
        atr_rel = (atr / close) * 100
        if atr_rel >= TRIGGER_ATR_REL:
            triggers.append({
                "type": "atr_spike",
                "severity": "medium",
                "details": f"ATR relatif {atr_rel:.2f}% (seuil {TRIGGER_ATR_REL}%)",
            })

    # 4. Golden/Death cross (changement de régime technique)
    golden = tech.get("golden_cross")
    prev_golden = None  # On n'a pas l'historique ici — on peut lire le dernier refresh
    # Pour le moment, on déclenche seulement si le golden_cross est présent
    # et qu'on détecte un changement macro (via proxy gap)

    # 5. News keywords
    news_matches = scan_news_keywords(ticker)
    if news_matches:
        triggers.append({
            "type": "news_keywords",
            "severity": "medium",
            "details": f"Keywords détectés : {', '.join(news_matches)}",
        })

    # 6. Earnings surprise (FMP si dispo, sinon proxy)
    earnings_surprise = check_earnings_surprise(ticker)
    if earnings_surprise:
        surprise_pct = earnings_surprise.get("surprise_pct", 0)
        if abs(surprise_pct) >= TRIGGER_EARNINGS_SURPRISE:
            triggers.append({
                "type": "earnings_surprise",
                "severity": "high",
                "details": f"Earnings surprise {surprise_pct:+.1f}% (seuil ±{TRIGGER_EARNINGS_SURPRISE}%)",
            })
    else:
        # Proxy : si earnings est aujourd'hui/hier ET gap > 5%, on suspecte un surprise
        calendar = snapshot.get("calendar", {})
        earnings_events = calendar.get("earnings", [])
        today = datetime.now(timezone.utc).date()
        for ev in earnings_events:
            if ev.get("ticker") == ticker and ev.get("event_type") == "earnings":
                try:
                    ev_date = datetime.strptime(ev["date"], "%Y-%m-%d").date()
                    if 0 <= (today - ev_date).days <= 1 and change_pct and abs(change_pct) >= TRIGGER_GAP_PCT:
                        triggers.append({
                            "type": "earnings_surprise_proxy",
                            "severity": "medium",
                            "details": f"Earnings hier/aujourd'hui + gap {change_pct:+.2f}% → possible surprise",
                        })
                except Exception:
                    pass

    return triggers


def read_previous_thesis(ticker: str) -> str:
    """Lit la thèse courante depuis INDEX.md si elle existe."""
    index_path = BASE_DIR / "Actions" / ticker / "INDEX.md"
    if not index_path.exists():
        return "Aucune thèse précédente."
    try:
        text = index_path.read_text(encoding="utf-8")
        # Cherche la section thèse courante
        if "## Thèse courante" in text:
            parts = text.split("## Thèse courante", 1)
            return parts[1].split("##", 1)[0].strip() if len(parts) > 1 else text[:500]
        return text[:800]
    except Exception:
        return "Aucune thèse précédente."


def generate_refresh_draft(ticker: str, triggers: list[dict], snapshot: dict) -> Path:
    """
    Génère un DRAFT_refresh.md avec toutes les données brutes actuelles
    et l'historique de la thèse précédente pour comparaison.
    """
    action_dir = BASE_DIR / "Actions" / ticker
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    data = snapshot.get("prices", {}).get(ticker, {})
    price = data.get("price", {})
    tech = data.get("technical", {})
    fund = data.get("fundamentals", {})
    options = data.get("options", {})
    fmp = data.get("fmp_consensus", {})
    ratios = data.get("fmp_ratios", {})
    metrics = data.get("fmp_key_metrics", {})

    previous_thesis = read_previous_thesis(ticker)

    trigger_lines = "\n".join(
        f"- **{t['type'].upper()}** ({t['severity']}) — {t['details']}" for t in triggers
    )

    content = f"""# {ticker} — FULL REFRESH (Événement Majeur)

> **Date :** {date_str}
> **Statut :** 🔴 FULL REFRESH — Thèse précédente potentiellement obsolète
> **Type :** Rafraîchissement complet (pas une simple mise à jour)

---

## 🚨 Triggers détectés

{trigger_lines}

---

## 📜 Thèse précédente (à comparer)

{previous_thesis}

---

## 1. Synthèse Exécutive (à réviser intégralement)

**Verdict rapide :** [À COMPLÉTER — Achat / Neutre / Vente / Surveiller]
**Prix cible révisé :** $XX.XX (upside/downside XX%)
**Score Opportunité révisé :** X.X/10
**Horizon :** [À COMPLÉTER]

> ⚠️ **Cette section doit expliquer si les triggers ci-dessus confirment, modifient ou invalident la thèse précédente.**

---

## 2. Bloc Prix & Technique (données actuelles)

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | ${price.get('close', 'N/A')} | Yahoo Finance |
| Change % | {price.get('change_pct', 'N/A')}% | Yahoo Finance |
| Volume | {price.get('volume', 'N/A'):,} | Yahoo Finance |
| Volume vs 20j | {round(price.get('volume',0)/price.get('volume_avg_20d',1),1) if price.get('volume_avg_20d') else 'N/A'}× | Calcul |
| RSI 14j | {tech.get('rsi14', 'N/A')} | Calcul agent |
| ATR 14j | {tech.get('atr14', 'N/A')} | Calcul agent |
| MM 50j | {tech.get('mm50', 'N/A')} | Calcul agent |
| MM 200j | {tech.get('mm200', 'N/A')} | Calcul agent |
| Golden Cross | {tech.get('golden_cross', 'N/A')} | Calcul agent |

**Niveaux clés :**
- Support : $XX.XX [À COMPLÉTER]
- Résistance : $XX.XX [À COMPLÉTER]
- Stop-loss ATR (2×) : $XX.XX [À COMPLÉTER]

**Verdict timing :** [Favorable / Neutre / Défavorable — À COMPLÉTER]

---

## 3. Bloc Fondamental (données actuelles)

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | {fund.get('market_cap', 'N/A'):,} | Yahoo Finance |
| P/E (TTM) | {fund.get('pe_ratio', 'N/A')} | Yahoo Finance |
| Forward P/E | {fund.get('forward_pe', 'N/A')} | Yahoo Finance |
| Beta | {fund.get('beta', 'N/A')} | Yahoo Finance |
| Secteur | {fund.get('sector', 'N/A')} | Yahoo Finance |
| **FMP Consensus PT** | {fmp.get('price_target_avg', 'N/A')} ({fmp.get('num_analysts', 'N/A')} analysts) | FMP Stable API |
| **FMP ROE** | {ratios.get('roe', 'N/A')} | FMP Stable API |
| **FMP Gross Margin** | {ratios.get('gross_margin', 'N/A')} | FMP Stable API |
| **FMP EV/EBITDA** | {metrics.get('ev_to_ebitda', 'N/A')} | FMP Stable API |

**Filtre Qualité (6 critères) :**
| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans ≥ 20% | [Oui/Non] | [À COMPLÉTER] |
| Profit CAGR 5 ans ≥ 20% | [Oui/Non] | [À COMPLÉTER] |
| Assets/Liabilities > 1.0 | [Oui/Non] | [À COMPLÉTER] |
| FCF positif et croissant 5 ans | [Oui/Non] | [À COMPLÉTER] |
| Avantage compétitif (moat) | [Oui/Non] | [À COMPLÉTER — l'event change-t-il le moat ?] |
| Industrie forte croissance (TAM ×5) | [Oui/Non] | [À COMPLÉTER] |
| **Score Qualité total** | X/6 | |

> ⚠️ **L'événement majeur peut avoir changé la structure fondamentale. Réévaluer chaque critère.**

---

## 4. Bloc Market Researcher (à réactualiser)

**TAM :** $XXB [À COMPLÉTER — l'event élargit-il le TAM ?]

**Peers principaux :**
| Peer | Market Cap | P/E | EV/EBITDA | Commentaire |
|------|-----------|-----|-----------|-------------|
| [Peer 1] | — | — | — | [À COMPLÉTER] |
| [Peer 2] | — | — | — | [À COMPLÉTER] |
| [Peer 3] | — | — | — | [À COMPLÉTER] |

**Position concurrentielle :** [À COMPLÉTER — l'event renforce-t-il le positionnement ?]

---

## 5. Bloc Macro (réactualisé)

**Régime macro actuel :** [Lire data/latest.json → macro.regime]
**Exposition sectorielle :**
- Sensibilité taux 10 ans : [+1% taux → -X% cours — À COMPLÉTER]
- Sensibilité pétrole : [+$10/bbl → +X% cours — À COMPLÉTER]
- Sensibilité DXY : [+5% DXY → -X% cours — À COMPLÉTER]

**Verdict Macro :** [Favorable / Neutre / Défavorable — À COMPLÉTER]

---

## 6. Bloc Géopolitique (réactualisé)

**Score Politique :** [Lire data/geo_risk_latest.json — À COMPLÉTER]
**Exposition :**
- Revenus géo : [À COMPLÉTER — l'event change-t-il l'exposition géographique ?]
- Supply chain : [À COMPLÉTER]

---

## 7. Bloc Sentiment (réactualisé)

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | {fmp.get('price_target_avg', 'N/A')} ({fmp.get('num_analysts', 'N/A')} analysts) | FMP |
| Put/Call ratio | {options.get('put_call_ratio', 'N/A')} | Yahoo |
| Max pain | {options.get('max_pain', 'N/A')} | Yahoo |

**Verdict Sentiment :** [Bullish / Neutre / Bearish — À COMPLÉTER]

---

## 8. Synthèse & Recommandation (à réécrire)

**Thèse d'investissement révisée (1 paragraphe) :**
[À COMPLÉTER — la thèse précédente est-elle toujours valide ? Qu'a changé l'événement ?]

**Catalyseurs forward :**
| Catalyst | Timeline | Probabilité | Impact |
|----------|----------|-------------|--------|
| [Catalyst 1] | QX 20XX | XX% | [À COMPLÉTER] |
| [Catalyst 2] | 20XX | XX% | [À COMPLÉTER] |

**Risques clés :**
1. [À COMPLÉTER — risque lié à l'événement détecté]
2. [À COMPLÉTER]
3. [À COMPLÉTER]

---

## ⚡ INSTRUCTION POUR L'AGENT LLM

Cet analyse est un **FULL REFRESH** déclenché par `agents/detect_major_events/agent.py`.
**Mission :**
1. Comparer cette analyse avec la thèse précédente (section 📜 ci-dessus)
2. Déterminer si l'événement majeur **confirme, modifie ou invalide** la thèse
3. Recalculer le Filtre Qualité 6 critères (l'événement peut changer le moat, le TAM, etc.)
4. Réviser le prix cible et le Score Opportunité
5. Sauvegarder le fichier complété sous `Actions/{ticker}/{ticker}_{date_str}_init.md`
6. **Mettre à jour `INDEX.md`** avec la nouvelle thèse courante et un lien vers l'ancienne
7. **Logger dans `Actions/{ticker}/REFRESH_LOG.md`** la date, les triggers, et la conclusion (confirm/modify/invalidate)
8. **Renommer le DRAFT_refresh** en `_DRAFT_refresh.md` (archive)

**Règle absolue :** utiliser EXCLUSIVEMENT les chiffres de `data/latest.json`. Ne jamais "deviner".
"""

    draft_path = action_dir / f"{ticker}_{date_str}_DRAFT_refresh.md"
    draft_path.write_text(content, encoding="utf-8")
    print(f"[detect_major_events] Generated FULL REFRESH DRAFT → {draft_path}", file=sys.stderr)
    return draft_path


def update_context_on_refresh(ticker: str, triggers: list[dict]) -> None:
    """Injecte les triggers détectés dans le CONTEXT.md du ticker."""
    action_dir = BASE_DIR / "Actions" / ticker
    context_path = action_dir / "CONTEXT.md"
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    trigger_lines = "\n".join(f"- **{t['type'].upper()}** ({t['severity']}) — {t['details']}" for t in triggers)

    if context_path.exists():
        text = context_path.read_text(encoding="utf-8")
        # Remplacer la section triggers
        if "## 🔄 Triggers détectés (full refresh)" in text:
            parts = text.split("## 🔄 Triggers détectés (full refresh)", 1)
            header = parts[0] + "## 🔄 Triggers détectés (full refresh)\n\n"
            # Jusqu'au prochain `---`
            remainder = parts[1]
            next_sep = remainder.find("\n---")
            if next_sep != -1:
                footer = remainder[next_sep:]
            else:
                footer = "\n\n---\n\n*Généré automatiquement — ne pas éditer manuellement.*\n"
            text = header + trigger_lines + "\n" + footer
        else:
            text = text.rstrip() + f"\n\n---\n\n## 🔄 Triggers détectés (full refresh)\n\n{trigger_lines}\n\n---\n\n*Généré automatiquement — ne pas éditer manuellement.*\n"
    else:
        text = f"""# CONTEXT — {ticker} — Dernière mise à jour : {date_str}

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.

---

## 🎯 Thèse active

- **Recommandation :** —
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** —
- **Horizon :** —

---

## 🔄 Triggers détectés (full refresh)

{trigger_lines}

---

*Généré automatiquement — ne pas éditer manuellement.*
"""

    context_path.write_text(text, encoding="utf-8")
    print(f"[detect_major_events] Updated {context_path}", file=sys.stderr)


def update_refresh_log(ticker: str, triggers: list[dict]) -> None:
    """Ajoute une entrée dans REFRESH_LOG.md pour tracer l'historique des refreshes."""
    action_dir = BASE_DIR / "Actions" / ticker
    log_path = action_dir / "REFRESH_LOG.md"
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    entry = f"""
## {date_str} — Full Refresh Triggered

**Triggers :**
"""
    for t in triggers:
        entry += f"- {t['type']} ({t['severity']}) : {t['details']}\n"
    entry += "\n**Conclusion :** [À compléter après analyse LLM]\n\n---\n"

    if log_path.exists():
        existing = log_path.read_text(encoding="utf-8")
        content = existing + entry
    else:
        content = f"# {ticker} — Historique des Full Refreshes\n\n" + entry

    log_path.write_text(content, encoding="utf-8")
    print(f"[detect_major_events] Updated {log_path}", file=sys.stderr)


def main():
    config = load_config()
    tickers = [t["ticker"] for t in config.get("tickers", [])]
    snapshot = load_latest()

    if not snapshot:
        print("[detect_major_events] No latest.json found. Run fetch_prices.py first.", file=sys.stderr)
        return 1

    triggered = 0
    for ticker in tickers:
        triggers = detect_triggers(ticker, snapshot)
        if not triggers:
            continue

        triggered += 1
        print(f"[detect_major_events] 🔴 {ticker}: {len(triggers)} trigger(s)", file=sys.stderr)
        for t in triggers:
            print(f"[detect_major_events]    → {t['type']} ({t['severity']}): {t['details']}", file=sys.stderr)

        # Generate refresh DRAFT
        draft_path = generate_refresh_draft(ticker, triggers, snapshot)

        # Update refresh log
        update_refresh_log(ticker, triggers)

        # Update context memory
        update_context_on_refresh(ticker, triggers)

    if triggered == 0:
        print("[detect_major_events] ✅ No major events detected.", file=sys.stderr)
    else:
        print(f"[detect_major_events] ⚡ {triggered} ticker(s) require FULL REFRESH.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

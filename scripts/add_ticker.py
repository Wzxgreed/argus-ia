#!/usr/bin/env python3
"""
add_ticker.py — Onboarding complet d'un nouveau ticker dans Argus-IA.

Usage:
    python scripts/add_ticker.py TICKER "Nom complet" "Secteur" [priority] [exchange]

Exemple:
    python scripts/add_ticker.py TSLA "Tesla Inc." "Automobile / Énergie" medium NASDAQ
    python scripts/add_ticker.py AAPL "Apple Inc." "Tech" high NASDAQ

Actions:
    1. Ajoute à config/watchlist.json
    2. Vérifie disponibilité Yahoo Finance + FMP
    3. Crée Actions/[TICKER]/ avec templates renommés
    4. Fetch un snapshot immédiat des données (prix, technique, FMP)
    5. Génère PENDING_ANALYSIS.md avec prompt prêt pour l'agent LLM
"""

import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import yfinance as yf

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
TEMPLATE_DIR = BASE_DIR / "Actions" / "_TEMPLATE_ACTION"

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def ticker_exists(config, ticker):
    return any(t["ticker"].upper() == ticker.upper() for t in config.get("tickers", []))


def verify_yahoo(ticker):
    """Vérifie que le ticker existe sur Yahoo Finance."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info or {}
        hist = stock.history(period="5d")
        return {
            "ok": hist is not None and not hist.empty,
            "name": info.get("longName") or info.get("shortName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "exchange": info.get("exchange"),
            "market_cap": info.get("marketCap"),
            "currency": info.get("currency"),
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


def add_to_watchlist(config, ticker, name, sector, priority, exchange, notes=""):
    """Ajoute le ticker à watchlist.json."""
    new_entry = {
        "ticker": ticker.upper(),
        "name": name,
        "sector": sector,
        "priority": priority,
        "exchange": exchange,
        "notes": notes,
    }
    config.setdefault("tickers", []).append(new_entry)
    save_config(config)
    return True


def create_action_folder(ticker):
    """Crée Actions/[TICKER]/ et copie les templates."""
    action_dir = BASE_DIR / "Actions" / ticker.upper()
    action_dir.mkdir(parents=True, exist_ok=True)

    if not TEMPLATE_DIR.exists():
        print(f"[add_ticker] ⚠️  Template directory not found: {TEMPLATE_DIR}", file=sys.stderr)
        return

    # Copy and rename templates
    for template_file in TEMPLATE_DIR.iterdir():
        if template_file.is_file():
            dest_name = template_file.name.replace("TICKER", ticker.upper())
            dest = action_dir / dest_name
            if not dest.exists():
                shutil.copy2(template_file, dest)
                print(f"[add_ticker]   Created {dest}", file=sys.stderr)


def fetch_snapshot(ticker):
    """Récupère un snapshot immédiat des données pour le ticker."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="6mo", interval="1d")
        info = stock.info or {}

        if hist.empty:
            return None

        last = hist.iloc[-1]
        prev = hist.iloc[-2] if len(hist) > 1 else last

        snapshot = {
            "ticker": ticker,
            "price": {
                "close": round(float(last["Close"]), 2),
                "change_pct": round((last["Close"] - prev["Close"]) / prev["Close"] * 100, 2),
                "volume": int(last["Volume"]),
            },
            "fundamentals": {
                "market_cap": info.get("marketCap"),
                "pe_ratio": info.get("trailingPE"),
                "forward_pe": info.get("forwardPE"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "beta": info.get("beta"),
            },
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
        return snapshot
    except Exception as e:
        print(f"[add_ticker] Error fetching snapshot: {e}", file=sys.stderr)
        return None


def generate_draft_init(ticker, yahoo_data, snapshot, sector, priority):
    """
    Génère un DRAFT_init.md avec tous les blocs de données pré-remplis.
    Les interprétations qualitatives sont marquées [À COMPLÉTER].
    """
    action_dir = BASE_DIR / "Actions" / ticker.upper()
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    p = snapshot["price"] if snapshot else {}
    f = snapshot["fundamentals"] if snapshot else {}

    content = f"""# {ticker.upper()} — Analyse Initiale (DRAFT)

> **Date :** {date_str}
> **Statut :** 🟡 DRAFT — données brutes pré-collectées, interprétation requise
> **Priorité :** {priority}
> **Ticker :** {ticker.upper()} | **Secteur :** {sector} | **Exchange :** {yahoo_data.get('exchange', 'N/A')}

---

## 1. Synthèse Exécutive

**Verdict rapide :** [À COMPLÉTER — Achat / Neutre / Vente / Surveiller]
**Prix cible :** $XX.XX (upside/downside XX%)
**Score Opportunité :** X.X/10 (Catalyseur X.X + Valorisation X.X + Momentum X.X)
**Horizon :** [À COMPLÉTER]

---

## 2. Bloc Prix & Technique (pré-collecté)

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | ${p.get('close', 'N/A')} | Yahoo Finance |
| Change % | {p.get('change_pct', 'N/A')}% | Yahoo Finance |
| Volume | {p.get('volume', 'N/A'):,} | Yahoo Finance |
| RSI 14j | [À COMPLÉTER — lire data/latest.json] | Calcul agent |
| ATR 14j | [À COMPLÉTER — lire data/latest.json] | Calcul agent |
| MM 50j | [À COMPLÉTER — lire data/latest.json] | Calcul agent |
| MM 200j | [À COMPLÉTER — lire data/latest.json] | Calcul agent |
| Golden Cross | [À COMPLÉTER] | Calcul agent |

**Niveaux clés :**
- Support : $XX.XX [À COMPLÉTER]
- Résistance : $XX.XX [À COMPLÉTER]
- Stop-loss ATR (2×) : $XX.XX [À COMPLÉTER]

**Verdict timing :** [Favorable / Neutre / Défavorable — À COMPLÉTER]

---

## 3. Bloc Fondamental (pré-collecté)

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | {f.get('market_cap', 'N/A'):,} | Yahoo Finance |
| P/E (TTM) | {f.get('pe_ratio', 'N/A')} | Yahoo Finance |
| Forward P/E | {f.get('forward_pe', 'N/A')} | Yahoo Finance |
| Beta | {f.get('beta', 'N/A')} | Yahoo Finance |
| Secteur | {f.get('sector', 'N/A')} | Yahoo Finance |
| Industrie | {f.get('industry', 'N/A')} | Yahoo Finance |
| **FMP Consensus PT** | [À COMPLÉTER — lire data/latest.json → fmp_consensus] | FMP Stable API |
| **FMP Analysts** | [À COMPLÉTER] | FMP Stable API |
| **FMP ROE** | [À COMPLÉTER — lire fmp_ratios] | FMP Stable API |
| **FMP Gross Margin** | [À COMPLÉTER] | FMP Stable API |
| **FMP EV/EBITDA** | [À COMPLÉTER — lire fmp_key_metrics] | FMP Stable API |

**Filtre Qualité (6 critères) :**
| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans ≥ 20% | [Oui/Non] | [À COMPLÉTER — calculer depuis statements] |
| Profit CAGR 5 ans ≥ 20% | [Oui/Non] | [À COMPLÉTER] |
| Assets/Liabilities > 1.0 | [Oui/Non] | [À COMPLÉTER — dernier bilan] |
| FCF positif et croissant 5 ans | [Oui/Non] | [À COMPLÉTER — cash-flow statement] |
| Avantage compétitif (moat) | [Oui/Non] | [À COMPLÉTER — analyse qualitative] |
| Industrie forte croissance (TAM ×5) | [Oui/Non] | [À COMPLÉTER — Market Researcher] |
| **Score Qualité total** | X/6 | |

**Verdict Filtre Qualité :** [✅ Quality Compounder / ⚠️ Quality Partielle / 🔴 Hors périmètre — À COMPLÉTER]

---

## 4. Bloc Market Researcher (pré-collecté)

**TAM (Total Addressable Market) :** $XXB [À COMPLÉTER]
**TAM ×5 sur 10 ans :** [Oui / Non — À COMPLÉTER]

**Peers principaux :**
| Peer | Market Cap | P/E | EV/EBITDA | Commentaire |
|------|-----------|-----|-----------|-------------|
| [Peer 1] | — | — | — | [À COMPLÉTER] |
| [Peer 2] | — | — | — | [À COMPLÉTER] |
| [Peer 3] | — | — | — | [À COMPLÉTER] |

**Position concurrentielle :** [À COMPLÉTER — leader/challenger/niche]
**Barrières à l'entrée :** [À COMPLÉTER]

---

## 5. Bloc Macro (pré-collecté)

**Régime macro actuel :** [Lire data/latest.json → macro.regime]
**Exposition sectorielle :**
- Sensibilité taux 10 ans : [+1% taux → -X% cours — À COMPLÉTER]
- Sensibilité pétrole : [+$10/bbl → +X% cours — À COMPLÉTER]
- Sensibilité DXY : [+5% DXY → -X% cours — À COMPLÉTER]
- Sensibilité Chine : [À COMPLÉTER]

**Verdict Macro :** [Favorable / Neutre / Défavorable — À COMPLÉTER]

---

## 6. Bloc Géopolitique (pré-collecté)

**Score Politique :** [Lire data/geo_risk_latest.json — À COMPLÉTER]
**Exposition :**
- Revenus géo : [À COMPLÉTER — % US, EU, Chine, etc.]
- Supply chain : [À COMPLÉTER]
- Macro sensibilité : [À COMPLÉTER]

**Scénarios :**
| Scénario | Probabilité | Impact | Action |
|----------|------------|--------|--------|
| Optimiste | 20% | +10% | [À COMPLÉTER] |
| Central | 55% | −2% | [À COMPLÉTER] |
| Pessimiste | 25% | −18% | [À COMPLÉTER] |

---

## 7. Bloc Sentiment (pré-collecté)

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | [À COMPLÉTER — lire fmp_consensus] | FMP |
| Upgrades/downgrades 30j | [À COMPLÉTER] | FMP |
| Put/Call ratio | [À COMPLÉTER — lire options dans latest.json] | Yahoo |
| Max pain | [À COMPLÉTER] | Yahoo |
| Volume relatif | [À COMPLÉTER] | Calcul agent |

**Verdict Sentiment :** [Bullish / Neutre / Bearish — À COMPLÉTER]

---

## 8. Bloc Quant (pré-collecté)

**Signification statistique :** [Lire data/quant_report_latest.json — À COMPLÉTER]
**Sharpe ratio (système) :** [À COMPLÉTER]
**Calibration :** [À COMPLÉTER — win rate par fourchette de score]

---

## 9. Synthèse & Recommandation

**Thèse d'investissement (1 paragraphe) :**
[À COMPLÉTER — synthèse de tous les blocs ci-dessus]

**Catalyseurs forward :**
| Catalyst | Timeline | Probabilité | Impact |
|----------|----------|-------------|--------|
| [Catalyst 1] | QX 20XX | XX% | [À COMPLÉTER] |
| [Catalyst 2] | 20XX | XX% | [À COMPLÉTER] |

**Risques clés :**
1. [À COMPLÉTER]
2. [À COMPLÉTER]
3. [À COMPLÉTER]

---

## ⚡ INSTRUCTION POUR L'AGENT LLM

Cet analyse est un **DRAFT pré-collecté** par `scripts/add_ticker.py`.
**Mission :** remplir toutes les sections marquées `[À COMPLÉTER]` en :
1. Lisant `data/latest.json` pour les données temps réel (RSI, ATR, MM, FMP, options)
2. Lisant `data/quant_report_latest.json` pour les métriques statistiques
3. Lisant `data/geo_risk_latest.json` pour l'exposition politique
4. Effectuant les recherches Market Researcher (TAM, peers, competitive landscape)
5. Calculant le Filtre Qualité 6 critères
6. Révisant le Score Opportunité

**Règle absolue :** utiliser EXCLUSIVEMENT les chiffres de `data/latest.json`. Ne jamais "deviner".

**Output final :** sauvegarder le fichier complété sous `Actions/{ticker.upper()}/{ticker.upper()}_{date_str}_init.md`
"""

    draft_path = action_dir / f"{ticker.upper()}_{date_str}_DRAFT_init.md"
    draft_path.write_text(content, encoding="utf-8")
    print(f"[add_ticker] Generated DRAFT → {draft_path}", file=sys.stderr)
    return draft_path


def generate_pending_analysis(ticker, yahoo_data, snapshot, sector, priority, draft_path):
    """Génère PENDING_ANALYSIS.md avec le chemin du DRAFT."""
    action_dir = BASE_DIR / "Actions" / ticker.upper()
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    p = snapshot["price"] if snapshot else {}
    f = snapshot["fundamentals"] if snapshot else {}

    content = f"""# {ticker.upper()} — Analyse en attente

> **Date :** {date_str}
> **Statut :** 🟡 DRAFT généré — prêt pour interprétation LLM
> **Priorité :** {priority}

---

## Fichiers disponibles

| Fichier | Statut | Description |
|---------|--------|-------------|
| `{draft_path.name}` | ✅ Prêt | DRAFT avec données brutes pré-collectées |
| `INDEX.md` | ⏳ En attente | À créer après complétion du DRAFT |
| `SUPPLY_CHAIN.md` | ⏳ En attente | À créer après analyse |
| `{ticker.upper()}_{date_str}_init.md` | ⏳ En attente | Version finale (copie du DRAFT complété) |

---

## Données pré-collectées (snapshot)

| Donnée | Valeur |
|--------|--------|
| **Cours** | ${p.get('close', 'N/A')} |
| **Change** | {p.get('change_pct', 'N/A')}% |
| **Market Cap** | {f.get('market_cap', 'N/A'):,} |
| **P/E (TTM)** | {f.get('pe_ratio', 'N/A')} |
| **Secteur** | {f.get('sector', 'N/A')} |

---

## Déclenchement automatique

**Aucune action manuelle requise.**

L'agent LLM détecte et complète automatiquement les DRAFT au démarrage de chaque session (voir Étape 0a-7 du CLAUDE.md). Le pipeline `run_morning.sh` affiche aussi un récapitulatif des DRAFT en attente à la fin de son exécution.

---

## Workflow de complétion

1. **Lire le DRAFT** (`{draft_path.name}`) — tous les blocs de données sont pré-structurés
2. **Lire `data/latest.json`** — remplir les champs techniques (RSI, ATR, MM, FMP, options)
3. **Lire `data/quant_report_latest.json`** — remplir le bloc Quant
4. **Lire `data/geo_risk_latest.json`** — remplir le bloc Géopolitique
5. **Market Researcher** — remplir TAM, peers, competitive landscape
6. **Agent Fondamental** — calculer Filtre Qualité 6 critères, DCF, valorisation
7. **Agent Technique** — interpréter RSI, niveaux, timing
8. **Agent Sentiment** — analyser consensus, options, news
9. **Copier le DRAFT complété** → `{ticker.upper()}_{date_str}_init.md`
10. **Créer `INDEX.md`** avec thèse courante
11. **Mettre à jour `WATCHLIST_SCORES.md`** et `CALENDRIER_EARNINGS.md`
12. **Supprimer le DRAFT** (ou le renommer `_DRAFT_init.md` pour archive)
"""

    path = action_dir / "PENDING_ANALYSIS.md"
    path.write_text(content, encoding="utf-8")
    print(f"[add_ticker] Generated {path}", file=sys.stderr)


def update_actualites_watchlist(ticker, name, sector, priority):
    """Ajoute le ticker dans Actualités/WATCHLIST.md."""
    watchlist_md = BASE_DIR / "Actualités" / "WATCHLIST.md"
    if not watchlist_md.exists():
        return

    text = watchlist_md.read_text(encoding="utf-8")
    line = f"\n| {ticker.upper()} | {name} | {sector} | {priority} | Ajouté le {datetime.now(timezone.utc).strftime('%Y-%m-%d')} |"

    # Find first table and append
    if "|" in text:
        # Naive append at end of first table
        lines = text.splitlines()
        # Find end of first table
        table_end = 0
        in_table = False
        for i, l in enumerate(lines):
            if l.strip().startswith("|"):
                in_table = True
                table_end = i
            elif in_table and not l.strip().startswith("|"):
                break

        lines.insert(table_end + 1, line)
        watchlist_md.write_text("\n".join(lines), encoding="utf-8")
        print(f"[add_ticker] Added to Actualités/WATCHLIST.md", file=sys.stderr)


def main():
    if len(sys.argv) < 4:
        print("Usage: python scripts/add_ticker.py TICKER 'Nom complet' 'Secteur' [priority] [exchange]", file=sys.stderr)
        print("Example: python scripts/add_ticker.py TSLA 'Tesla Inc.' 'Automobile / Énergie' medium NASDAQ", file=sys.stderr)
        sys.exit(1)

    ticker = sys.argv[1].upper()
    name = sys.argv[2]
    sector = sys.argv[3]
    priority = sys.argv[4] if len(sys.argv) > 4 else "medium"
    exchange = sys.argv[5] if len(sys.argv) > 5 else "NASDAQ"

    print(f"[add_ticker] Onboarding {ticker} — {name}", file=sys.stderr)

    # Load config
    config = load_config()

    # Check existence
    if ticker_exists(config, ticker):
        print(f"[add_ticker] ❌ {ticker} already exists in watchlist. Aborting.", file=sys.stderr)
        sys.exit(1)

    # Verify Yahoo
    yahoo_data = verify_yahoo(ticker)
    if not yahoo_data["ok"]:
        print(f"[add_ticker] ❌ Yahoo Finance does not recognize {ticker}.", file=sys.stderr)
        print(f"[add_ticker]    Error: {yahoo_data.get('error', 'Unknown')}", file=sys.stderr)
        print(f"[add_ticker]    Are you sure about the symbol?", file=sys.stderr)
        sys.exit(1)

    print(f"[add_ticker] ✅ Yahoo OK : {yahoo_data.get('name')} ({yahoo_data.get('exchange')})", file=sys.stderr)

    # Add to config
    add_to_watchlist(config, ticker, name, sector, priority, exchange,
                     notes=f"Ajouté le {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    print(f"[add_ticker] ✅ Added to config/watchlist.json", file=sys.stderr)

    # Create folder
    create_action_folder(ticker)

    # Fetch snapshot
    snapshot = fetch_snapshot(ticker)
    if snapshot:
        print(f"[add_ticker] ✅ Snapshot : ${snapshot['price']['close']} (change {snapshot['price']['change_pct']}%)", file=sys.stderr)
    else:
        print(f"[add_ticker] ⚠️  Snapshot failed", file=sys.stderr)

    # Generate DRAFT init (pre-filled with raw data)
    draft_path = generate_draft_init(ticker, yahoo_data, snapshot, sector, priority)

    # Generate pending analysis (references the DRAFT)
    generate_pending_analysis(ticker, yahoo_data, snapshot, sector, priority, draft_path)

    # Update Actualités/WATCHLIST.md
    update_actualites_watchlist(ticker, name, sector, priority)

    # Summary
    print(f"\n[add_ticker] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", file=sys.stderr)
    print(f"[add_ticker] ✅ {ticker} ONBOARDED", file=sys.stderr)
    print(f"[add_ticker] 📁 Dossier : Actions/{ticker}/", file=sys.stderr)
    print(f"[add_ticker] 📄 DRAFT    : Actions/{ticker}/{draft_path.name}", file=sys.stderr)
    print(f"[add_ticker] 📊 Données : data/latest.json (dès demain matin)", file=sys.stderr)
    print(f"[add_ticker] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", file=sys.stderr)
    print(f"[add_ticker] The DRAFT will be auto-completed by the LLM agent at next session.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

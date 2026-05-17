#!/usr/bin/env python3
"""
full_analysis.py — Agent d'analyse complète multi-étapes pour un ticker.
Exécute les protocoles des agents Argus-IA en séquence via le LLM proxy.

Usage :
  python3 scripts/full_analysis.py AAPL
"""
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
AGENTS_DIR = BASE_DIR / "agents"
ACTIONS_DIR = BASE_DIR / "Actions"

sys.path.insert(0, str(BASE_DIR / "scripts"))
from ask_llm import ask_llm


def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def load_md(path: Path) -> str:
    if path.exists():
        return path.read_text()
    return ""


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def log(msg: str):
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {msg}", flush=True)


def call_llm(prompt: str, system: str = "", model: str = "kimi-k2.6:cloud") -> str:
    """Appelle le LLM via le proxy local."""
    response = ask_llm(prompt, model=model, system=system)
    if response.startswith("[ERREUR]"):
        raise RuntimeError(response)
    return response.strip()


def load_protocols() -> dict:
    """Charge les protocoles des agents."""
    protocols = {}
    for name in ["AGENT_MACRO", "AGENT_TECHNIQUE", "AGENT_FONDAMENTAL", "AGENT_SENTIMENT", "AGENT_FLUX", "SKILL_MARKET_RESEARCHER"]:
        path = AGENTS_DIR / f"{name}.md"
        if path.exists():
            protocols[name] = path.read_text()
        else:
            log(f"⚠️ Protocole manquant : {name}.md")
            protocols[name] = ""
    return protocols


def _fmt(val, prefix: str = "", suffix: str = "", default: str = "N/A") -> str:
    """Formate une valeur numérique ou retourne default."""
    if val is None:
        return f"{prefix}{default}{suffix}"
    if isinstance(val, (int, float)):
        if isinstance(val, float) and val == int(val):
            return f"{prefix}{int(val):,}{suffix}"
        return f"{prefix}{val:,.2f}{suffix}" if isinstance(val, float) else f"{prefix}{val:,}{suffix}"
    return f"{prefix}{val}{suffix}"


def build_data_context(ticker: str, data: dict) -> str:
    """Construit le contexte de données pour les prompts."""
    price = data.get("price", {})
    tech = data.get("technical", {})
    fund = data.get("fundamentals", {})
    options = data.get("options", {})

    lines = [
        f"## DONNÉES BRUTES POUR {ticker}",
        "",
        "**Cours :**",
        f"- Close : {_fmt(price.get('close'), '$')}",
        f"- Open : {_fmt(price.get('open'), '$')}",
        f"- High : {_fmt(price.get('high'), '$')}",
        f"- Low : {_fmt(price.get('low'), '$')}",
        f"- Change % : {_fmt(price.get('change_pct'), suffix='%')}",
        f"- Volume : {_fmt(price.get('volume'))}",
        f"- Volume moyen 20j : {_fmt(price.get('volume_avg_20d'))}",
        "",
        "**Technique :**",
        f"- RSI 14j : {_fmt(tech.get('rsi14'))}",
        f"- ATR 14j : {_fmt(tech.get('atr14'), '$')}",
        f"- MM 50j : {_fmt(tech.get('mm50'), '$')}",
        f"- MM 200j : {_fmt(tech.get('mm200'))}",
        f"- Golden/Death Cross : {tech.get('golden_cross') or 'Non'}",
        "",
        "**Fondamentaux :**",
        f"- Market Cap : {_fmt(fund.get('market_cap'), '$')}",
        f"- Secteur : {fund.get('sector', 'N/A')}",
        f"- Industrie : {fund.get('industry', 'N/A')}",
        f"- P/E : {_fmt(fund.get('pe_ratio'))}",
        f"- Forward P/E : {_fmt(fund.get('forward_pe'))}",
        f"- EV/EBITDA : {_fmt(fund.get('ev_ebitda'))}",
        f"- EV/Revenue : {_fmt(fund.get('ev_revenue'))}",
        f"- P/B : {_fmt(fund.get('price_to_book'))}",
        f"- Dividend Yield : {_fmt(fund.get('dividend_yield'), suffix='%')}",
        f"- Beta : {_fmt(fund.get('beta'))}",
        f"- Short Interest : {_fmt(fund.get('short_interest_pct'), suffix='%')}",
        f"- Float : {_fmt(fund.get('shares_float'))}",
        f"- Outstanding : {_fmt(fund.get('shares_outstanding'))}",
        f"- 52W High : {_fmt(fund.get('fifty_two_week_high'), '$')}",
        f"- 52W Low : {_fmt(fund.get('fifty_two_week_low'), '$')}",
        "",
        "**Options :**",
        f"- Max Pain : {_fmt(options.get('max_pain'), '$')}",
        f"- Put/Call Ratio : {_fmt(options.get('put_call_ratio'))}",
        f"- Call OI % : {_fmt(options.get('call_oi_pct'), suffix='%')}",
    ]
    return "\n".join(lines)


def step_market_researcher(ticker: str, data_ctx: str, protocol: str) -> str:
    """Étape 1 : Market Researcher (TAM, peers, landscape)."""
    log("🌍 Étape 1/6 — Market Researcher")
    prompt = f"""{data_ctx}

## PROTOCOLE MARKET RESEARCHER
{protocol[:800]}

Ta mission : Produire le bloc **Market Researcher** pour {ticker}.
Format markdown concis (max 200 mots) avec :
- TAM et croissance du secteur
- 3-5 peers principaux avec multiples
- Positionnement concurrentiel
- Investment implications (2-3 phrases)

Réponds UNIQUEMENT avec le bloc markdown, sans introduction."""
    return call_llm(prompt, system="Tu es un analyste sectoriel senior (JPM/GS/MS style).")


def step_macro(ticker: str, data_ctx: str, protocol: str) -> str:
    """Étape 2 : Agent Macro (régime, exposition)."""
    log("🏛️ Étape 2/6 — Agent Macro")
    prompt = f"""{data_ctx}

## PROTOCOLE AGENT MACRO
{protocol[:800]}

Ta mission : Produire le bloc **Macro** pour {ticker}.
Format markdown concis (max 150 mots) avec :
- Régime macro actif et impact sur le secteur
- Exposition sectorielle et sensibilités (taux, USD, pétrole, Chine)
- Ajustement de pondération suggéré (Catalyseur/Valorisation/Momentum)

Réponds UNIQUEMENT avec le bloc markdown, sans introduction."""
    return call_llm(prompt, system="Tu es un stratège macro institutionnel.")


def step_technique(ticker: str, data_ctx: str, protocol: str) -> str:
    """Étape 3 : Agent Technique (indicateurs, niveaux, timing)."""
    log("📈 Étape 3/6 — Agent Technique")
    price = load_json(DATA_DIR / "latest.json").get("prices", {}).get(ticker, {}).get("price", {})
    tech = load_json(DATA_DIR / "latest.json").get("prices", {}).get(ticker, {}).get("technical", {})
    close = price.get("close", 0)
    atr = tech.get("atr14", 0)
    sl = round(close - 2 * atr, 2) if close and atr else "N/A"
    tp = round(close + 3 * atr, 2) if close and atr else "N/A"

    prompt = f"""{data_ctx}

## DONNÉES TECHNIQUES COMPLÉMENTAIRES
- Stop-loss suggéré (2×ATR) : ${sl}
- Take-profit suggéré (3×ATR) : ${tp}

## PROTOCOLE AGENT TECHNIQUE
{protocol[:800]}

Ta mission : Produire le bloc **Technique** pour {ticker}.
Format markdown structuré avec :
- RSI 14j, MACD, MM50/200, Golden/Death cross
- Volume relatif vs 20j
- Supports et résistances clés
- Force relative vs S&P 500 (si disponible)
- Timing verdict : Favorable / Neutre / Défavorable
- Score Momentum /10

Réponds UNIQUEMENT avec le bloc markdown."""
    return call_llm(prompt, system="Tu es un analyste technique institutionnel (CMT).")


def step_fondamental(ticker: str, data_ctx: str, protocol: str) -> str:
    """Étape 4 : Agent Fondamental (Filtre Qualité, valorisation)."""
    log("📊 Étape 4/6 — Agent Fondamental")
    prompt = f"""{data_ctx}

## PROTOCOLE AGENT FONDAMENTAL
{protocol[:800]}

Ta mission : Produire le bloc **Fondamental** pour {ticker}.
Format markdown structuré avec :

### Filtre Qualité (6 critères)
| Critère | Score | Commentaire |
|---------|-------|-------------|
| Revenue CAGR 5 ans | ?/1 | |
| Profit CAGR 5 ans | ?/1 | |
| Assets/Liabilities > 1.0 | ?/1 | |
| FCF positif croissant | ?/1 | |
| Moat structurel | ?/1 | |
| TAM ×5 / 10 ans | ?/1 | |

**Score Qualité : X/6** → [✅ Quality Compounder / ⚠️ Partielle / 🔴 Hors périmètre]

### Valorisation
- P/E, Forward P/E, EV/EBITDA, P/B
- Comparaison sectorielle
- DCF simplifié (si données disponibles)
- Score Valorisation /10

### Risques fondamentaux (3 max)

Réponds UNIQUEMENT avec le bloc markdown."""
    return call_llm(prompt, system="Tu es un analyste fondamental senior (CFA).")


def step_sentiment(ticker: str, data_ctx: str, protocol: str) -> str:
    """Étape 5 : Agent Sentiment (news, options, insiders)."""
    log("💬 Étape 5/6 — Agent Sentiment")
    prompt = f"""{data_ctx}

## PROTOCOLE AGENT SENTIMENT
{protocol[:800]}

Ta mission : Produire le bloc **Sentiment** pour {ticker}.
Format markdown structuré avec :
- Consensus analystes (upgrades/downgrades)
- Options : Max Pain, Put/Call, IV Rank
- Short interest et borrow rate
- Insider trades (si mentionné)
- News récentes et tonalité
- Score Catalyseur /10

Réponds UNIQUEMENT avec le bloc markdown."""
    return call_llm(prompt, system="Tu es un analyste sentiment et options.")


def step_flux(ticker: str, data_ctx: str, protocol: str) -> str:
    """Étape 6 : Agent Flux (institutionnels, dark pool, gamma)."""
    log("🏦 Étape 6/6 — Agent Flux")
    prompt = f"""{data_ctx}

## PROTOCOLE AGENT FLUX
{protocol[:1500]}

Ta mission : Produire le bloc **Flux Institutionnels** pour {ticker}.
Format markdown concis (max 150 mots) avec :
- 13F / accumulation-distribution
- ETF flows sectoriels
- Dark pool / block trades
- Gamma exposure / max pain
- Score ajustement Catalyseur (bonus/malus)

Réponds UNIQUEMENT avec le bloc markdown."""
    return call_llm(prompt, system="Tu es un analyste flux institutionnels.")


def compile_report(ticker: str, blocks: dict) -> str:
    """Compile tous les blocs dans le rapport final."""
    today = now_str()
    price_data = load_json(DATA_DIR / "latest.json").get("prices", {}).get(ticker, {})
    close = price_data.get("price", {}).get("close", "N/A")

    report = f"""# {ticker} — Analyse Initiale ({today})

> ⚠️ **Note :** Cette analyse a été générée automatiquement par le système multi-agents Argus-IA. Pour une analyse institutionnelle complète avec données FMP, SEC filings et transcripts, exécutez l'analyse manuelle via Claude Code avec la commande :> `Analyse {ticker}, crée le dossier Actions/{ticker}/ et sauvegarde l'analyse initiale`

---

## Résumé Exécutif
{blocks.get('summary', 'À compléter manuellement après lecture des blocs ci-dessous.')}

---

{blocks.get('market_researcher', '### Market Researcher\n*Non disponible — données insuffisantes.*')}

---

{blocks.get('macro', '### Macro\n*Non disponible — données insuffisantes.*')}

---

{blocks.get('technique', '### Technique\n*Non disponible — données insuffisantes.*')}

---

{blocks.get('fondamental', '### Fondamental\n*Non disponible — données insuffisantes.*')}

---

{blocks.get('sentiment', '### Sentiment\n*Non disponible — données insuffisantes.*')}

---

{blocks.get('flux', '### Flux Institutionnels\n*Non disponible — données insuffisantes.*')}

---

## Scoring Global
| Axe | Score | Pondération |
|-----|-------|-------------|
| Catalyseur | X/10 | 35% |
| Valorisation | X/10 | 40% |
| Momentum | X/10 | 25% |
| **Score Opportunité** | **X/10** | |

## Niveaux et Ratio R/R
- Cours actuel : ${close}
- Stop-loss : [calculé dans le bloc Technique]
- Take-profit : [calculé dans le bloc Technique]
- Ratio R/R : X:1

## Conclusion
[ACHETER / ATTENDRE / SURVEILLER / ÉVITER]

---
*Généré automatiquement par Argus-IA le {today} via multi-agents (Market Researcher → Macro → Technique → Fondamental → Sentiment → Flux)*
"""
    return report


def generate_summary(ticker: str, blocks: dict) -> str:
    """Génère le résumé exécutif à partir de tous les blocs."""
    log("📝 Compilation du résumé exécutif")
    combined = "\n\n".join([
        blocks.get("market_researcher", ""),
        blocks.get("macro", ""),
        blocks.get("technique", ""),
        blocks.get("fondamental", ""),
        blocks.get("sentiment", ""),
    ])
    prompt = f"""Tu es le rédacteur en chef d'un desk d'analyse institutionnel. À partir des blocs d'analyse suivants pour {ticker}, rédige un **résumé exécutif** de 3-4 phrases maximum qui synthétise :
1. La thèse d'investissement principale (bull/bear)
2. Le niveau de qualité de l'entreprise
3. Le timing technique
4. Le verdict global (ACHETER / ATTENDRE / SURVEILLER / ÉVITER)

---
{combined[:4000]}
---

Réponds UNIQUEMENT avec le résumé (3-4 phrases), sans titre ni formatage."""
    return call_llm(prompt, system="Tu rédiges des résumés exécutifs concis pour des rapports institutionnels.")


def run_full_analysis(ticker: str):
    """Pipeline complet d'analyse multi-agents."""
    ticker = ticker.upper()
    today = now_str()
    log(f"🚀 Lancement de l'analyse complète pour {ticker}")

    # ── Étape 0 : Chargement des données ──
    latest = load_json(DATA_DIR / "latest.json")
    ticker_data = latest.get("prices", {}).get(ticker)
    if not ticker_data:
        raise ValueError(f"Aucune donnée trouvée pour {ticker} dans data/latest.json")

    protocols = load_protocols()
    data_ctx = build_data_context(ticker, ticker_data)

    # ── Étape 1-6 : Exécution séquentielle des agents ──
    log("🔄 Lancement séquentiel des 6 agents...")
    blocks = {}
    blocks["market_researcher"] = step_market_researcher(ticker, data_ctx, protocols.get("SKILL_MARKET_RESEARCHER", ""))
    blocks["macro"] = step_macro(ticker, data_ctx, protocols.get("AGENT_MACRO", ""))
    blocks["technique"] = step_technique(ticker, data_ctx, protocols.get("AGENT_TECHNIQUE", ""))
    blocks["fondamental"] = step_fondamental(ticker, data_ctx, protocols.get("AGENT_FONDAMENTAL", ""))
    blocks["sentiment"] = step_sentiment(ticker, data_ctx, protocols.get("AGENT_SENTIMENT", ""))
    blocks["flux"] = step_flux(ticker, data_ctx, protocols.get("AGENT_FLUX", ""))

    # ── Compilation du résumé ──
    blocks["summary"] = generate_summary(ticker, blocks)

    # ── Création du rapport final ──
    report = compile_report(ticker, blocks)

    # ── Sauvegarde ──
    ticker_dir = ACTIONS_DIR / ticker
    ticker_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{ticker}_{today}_init.md"
    filepath = ticker_dir / filename
    filepath.write_text(report, encoding="utf-8")
    log(f"✅ Rapport sauvegardé : {filepath}")

    # INDEX.md
    index_path = ticker_dir / "INDEX.md"
    if not index_path.exists():
        index_path.write_text(f"""# {ticker}

## Thèse courante
{blocks['summary']}

## Historique
| Date | Fichier | Type |
|------|---------|------|
| {today} | [{filename}]({filename}) | Analyse initiale (auto) |

## Agenda
- Prochain earnings : [à compléter]

## Alertes actives
- Aucune
""", encoding="utf-8")
        log(f"✅ INDEX.md créé")
    else:
        text = index_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "| Date | Fichier | Type |" in line:
                text = text.replace(line, line + f"\n| {today} | [{filename}]({filename}) | Analyse initiale (auto) |")
                break
        index_path.write_text(text, encoding="utf-8")
        log(f"✅ INDEX.md mis à jour")

    # CONTEXT.md
    ctx_path = ticker_dir / "CONTEXT.md"
    if not ctx_path.exists():
        ctx_path.write_text(f"""# Contexte {ticker}

## Thèse active
{blocks['summary']}

## Score actuel
- Opportunité : X/10
- Valorisation : X/10
- Momentum : X/10

## Niveaux
- Cours : {ticker_data.get('price', {}).get('close', 'N/A')}
- SL : [voir rapport]
- TP : [voir rapport]

## Statut
[ACTIVE / EN SURVEILLANCE / CLOS]
""", encoding="utf-8")
        log(f"✅ CONTEXT.md créé")

    return str(filepath), report


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Analyse complète multi-agents Argus-IA")
    parser.add_argument("ticker", help="Ticker à analyser")
    args = parser.parse_args()

    try:
        path, report = run_full_analysis(args.ticker)
        log(f"\n✅ Analyse complète terminée : {path}")
        log(f"   Longueur : {len(report)} caractères")
    except Exception as e:
        log(f"\n❌ Erreur : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

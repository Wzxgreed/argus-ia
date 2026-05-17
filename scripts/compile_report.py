#!/usr/bin/env python3
"""
compile_report.py — Compile un rapport institutionnel pour un ticker
en utilisant les vrais agents Python + un seul appel LLM pour la prose.

Usage:
    python3 scripts/compile_report.py SQ
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
AGENTS_DIR = BASE_DIR / "agents"
ACTIONS_DIR = BASE_DIR / "Actions"
LOGS_DIR = BASE_DIR / "logs"

sys.path.insert(0, str(BASE_DIR / "scripts"))
from ask_llm import ask_llm


def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


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


def run_agent(name: str, timeout: int = 300) -> bool:
    """Lance un agent individuel via l'orchestrateur."""
    log(f"🔧 Lancement agent : {name}")
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{AGENTS_DIR}:{BASE_DIR / 'scripts'}:{BASE_DIR}"
    cmd = [sys.executable, str(BASE_DIR / "agents" / "orchestrator.py"), f"--agent={name}"]
    try:
        proc = subprocess.run(cmd, cwd=BASE_DIR, env=env, capture_output=True, text=True, timeout=timeout)
        ok = proc.returncode == 0
        if not ok:
            log(f"⚠️  Agent {name} exit={proc.returncode} (allow_fail possible)")
        else:
            log(f"✅ Agent {name} terminé")
        return ok
    except subprocess.TimeoutExpired:
        log(f"⏱️  Agent {name} timeout")
        return False
    except Exception as e:
        log(f"❌ Agent {name} erreur : {e}")
        return False


def run_agents_for_ticker(ticker: str) -> None:
    """Relance les agents pertinents pour mettre à jour les données du ticker."""
    # Les agents qui enrichissent les données structurées par ticker
    agents_to_run = [
        "prices",
        "macro",
        "news_fetcher",
        "data_quality_gate",
        "accounting",
        "geo",
        "crypto",
        "sector_rotation",
        "social",
        "fx",
        "event_driven",
        "watchman",
        "detect_major_events",
        "recommandation",
    ]
    for agent in agents_to_run:
        run_agent(agent, timeout=300)


def _fmt(val, prefix: str = "", suffix: str = "", default: str = "N/A") -> str:
    if val is None:
        return f"{prefix}{default}{suffix}"
    if isinstance(val, (int, float)):
        if isinstance(val, float) and val == int(val):
            return f"{prefix}{int(val):,}{suffix}"
        return f"{prefix}{val:,.2f}{suffix}" if isinstance(val, float) else f"{prefix}{val:,}{suffix}"
    return f"{prefix}{val}{suffix}"


def build_data_context(ticker: str, data: dict) -> str:
    """Construit le contexte de données brutes."""
    price = data.get("price", {})
    tech = data.get("technical", {})
    fund = data.get("fundamentals", {})
    options = data.get("options", {})
    macro = data.get("macro", {})

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
        "",
        "**Macro (snapshot) :**",
        f"- VIX : {_fmt(macro.get('vix'))}",
        f"- DXY : {_fmt(macro.get('dxy'))}",
        f"- Taux 10Y : {_fmt(macro.get('us10y'), suffix='%')}",
        f"- Pétrole (WTI) : {_fmt(macro.get('wti'), '$')}",
        f"- Or : {_fmt(macro.get('gold'), '$')}",
    ]
    return "\n".join(lines)


def load_agent_data(ticker: str) -> dict:
    """Charge les données des agents Python réels pour ce ticker."""
    result = {}

    # Recommandation (le plus important — contient scores, SL, TP, action)
    rec = load_json(DATA_DIR / "recommandations_latest.json")
    for r in rec.get("recommandations", []):
        if r.get("ticker") == ticker:
            result["recommandation"] = r
            break

    # Accounting
    acc = load_json(DATA_DIR / "accounting_risk_latest.json")
    result["accounting"] = acc.get("analysis", {}).get(ticker)

    # Geo
    geo = load_json(DATA_DIR / "geo_risk_latest.json")
    result["geo"] = geo.get("ticker_exposure", {}).get(ticker)

    # Crypto
    crypto = load_json(DATA_DIR / "crypto_correlation_latest.json")
    result["crypto"] = crypto.get("analysis", {}).get(ticker)

    # Sector rotation
    sr = load_json(DATA_DIR / "sector_rotation_latest.json")
    sector_ticker = None
    for s in sr.get("ranking", []):
        if s.get("ticker") == ticker:
            sector_ticker = s
            break
    result["sector_rotation"] = sector_ticker

    # Social
    social = load_json(DATA_DIR / "social_sentiment_latest.json")
    result["social"] = social.get("analysis", {}).get(ticker)

    # FX
    fx = load_json(DATA_DIR / "fx_exposure_latest.json")
    fx_ticker = None
    for f in fx.get("tickers", []):
        if f.get("ticker") == ticker:
            fx_ticker = f
            break
    result["fx"] = fx_ticker

    # Events
    ev = load_json(DATA_DIR / "events_latest.json")
    result["events"] = ev.get("ticker_events", {}).get(ticker, [])

    # Upcoming events
    ue = load_json(DATA_DIR / "upcoming_events_latest.json")
    result["upcoming"] = [e for e in ue.get("events", []) if e.get("ticker") == ticker]

    # Quality gate
    qg = load_json(DATA_DIR / "quality_report_latest.json")
    result["quality"] = qg.get("tickers", {}).get(ticker)

    # Quant
    quant = load_json(DATA_DIR / "quant_report_latest.json")
    result["quant"] = quant

    # Transcripts NLP
    nlp = load_json(DATA_DIR / "transcripts_NLP_latest.json")
    result["nlp"] = [t for t in nlp.get("transcripts", []) if t.get("ticker") == ticker]

    # Detect major events
    maj = load_json(DATA_DIR / "detect_major_events_latest.json")
    result["major_events"] = [e for e in maj.get("events", []) if e.get("ticker") == ticker]

    return result


def format_agent_context(ticker: str, agent_data: dict) -> str:
    """Formate les données des agents en texte structuré pour le prompt LLM."""
    lines = [f"## DONNÉES AGENTS POUR {ticker}", ""]

    # Recommandation
    rec = agent_data.get("recommandation")
    if rec:
        lines.extend([
            "**Agent Recommandation :**",
            f"- Action : {rec.get('action', 'N/A')} | Direction : {rec.get('direction', 'N/A')}",
            f"- Score Global : {rec.get('score_global_ajuste', rec.get('score_global', 'N/A'))}/100",
            f"- Score Opportunité : {rec.get('score_opportunite', 'N/A')}/10 (C:{rec.get('score_catalyseur', 'N/A')} V:{rec.get('score_valorisation', 'N/A')} M:{rec.get('score_momentum', 'N/A')})",
            f"- Timing : {rec.get('timing', 'N/A')} | Horizon : {rec.get('horizon', 'N/A')}",
            f"- Prix actuel : ${_fmt(rec.get('prix_actuel'))}",
            f"- Entrée suggérée : ${_fmt(rec.get('prix_entree_suggere'))}",
            f"- Stop-loss : ${_fmt(rec.get('stop_loss'))}",
            f"- Take-profit : ${_fmt(rec.get('take_profit'))}",
            f"- Ratio R/R : {rec.get('risque_rendement_ratio', 'N/A')}",
            f"- Sizing : {rec.get('sizing', 'N/A')}",
        ])
        if rec.get("justification"):
            lines.append("- Justification :")
            for j in rec["justification"]:
                lines.append(f"  • {j}")
        if rec.get("risques"):
            lines.append("- Risques :")
            for r in rec["risques"]:
                lines.append(f"  • {r}")
        if rec.get("alertes"):
            lines.append("- Alertes :")
            for a in rec["alertes"]:
                lines.append(f"  • {a}")
        lines.append("")

    # Accounting
    acc = agent_data.get("accounting")
    if acc:
        lines.append("**Agent Accounting (Risque comptable) :**")
        lines.append(f"- Risk Level : {acc.get('risk_level', 'N/A')}")
        if acc.get("beneish"):
            b = acc["beneish"]
            lines.append(f"  • Beneish M-Score : {b.get('m_score', 'N/A')} | Verdict : {b.get('verdict', 'N/A')}")
        if acc.get("altman"):
            a = acc["altman"]
            lines.append(f"  • Altman Z-Score : {a.get('z_score', 'N/A')} | Verdict : {a.get('verdict', 'N/A')}")
        if acc.get("piotroski"):
            p = acc["piotroski"]
            lines.append(f"  • Piotroski F-Score : {p.get('f_score', 'N/A')} | Verdict : {p.get('verdict', 'N/A')}")
        if acc.get("sloan"):
            s = acc["sloan"]
            lines.append(f"  • Sloan Ratio : {s.get('sloan_ratio', 'N/A')} | Verdict : {s.get('verdict', 'N/A')}")
        if acc.get("alerts"):
            lines.append("  • Alertes : " + ", ".join(acc["alerts"]))
        lines.append("")

    # Geo
    geo = agent_data.get("geo")
    if geo:
        lines.append("**Agent Géopolitique :**")
        lines.append(f"- Geo Risk Score : {geo.get('geo_risk_score', 'N/A')}/10 | Flag : {geo.get('flag', 'N/A')}")
        if geo.get("relevant_events"):
            for ev in geo["relevant_events"][:3]:
                lines.append(f"  • {ev.get('title', '')} — Score {ev.get('score', 'N/A')}/10")
        lines.append("")

    # Crypto
    crypto = agent_data.get("crypto")
    if crypto:
        lines.append("**Agent Crypto-Correlation :**")
        lines.append(f"- Corrélation 30j BTC : {crypto.get('correlation_30d', 'N/A')}")
        lines.append(f"- Beta BTC : {crypto.get('beta_btc', 'N/A')}")
        lines.append(f"- Divergence Score : {crypto.get('divergence_score', 'N/A')}/10")
        lines.append(f"- Verdict : {crypto.get('verdict', 'N/A')}")
        lines.append("")

    # Sector rotation
    sr = agent_data.get("sector_rotation")
    if sr:
        lines.append("**Agent Sector Rotation :**")
        lines.append(f"- RS 20j vs SPY : {sr.get('rs_20d', 'N/A')} | RS 60j : {sr.get('rs_60d', 'N/A')}")
        lines.append(f"- Momentum Score : {sr.get('momentum_score', 'N/A')}/10")
        lines.append(f"- Régime : {sr.get('regime', 'N/A')} | Alignement : {sr.get('regime_alignment', 'N/A')}")
        if sr.get("crossover"):
            lines.append(f"- Crossover : {sr['crossover']}")
        lines.append("")

    # Social
    social = agent_data.get("social")
    if social:
        lines.append("**Agent Social Sentiment :**")
        lines.append(f"- Mentions : {social.get('mention_count', 'N/A')} | Spike : {social.get('mention_spike', False)}")
        lines.append(f"- Sentiment Score : {social.get('sentiment_score', 'N/A')}/10 | Label : {social.get('sentiment_label', 'N/A')}")
        lines.append(f"- Pump Detected : {social.get('pump_detected', False)}")
        lines.append("")

    # FX
    fx = agent_data.get("fx")
    if fx:
        lines.append("**Agent FX Exposure :**")
        lines.append(f"- Exposition : {fx.get('exposure_pct', 'N/A')}% | Direction : {fx.get('direction_label', 'N/A')}")
        lines.append(f"- Impact revenus : {fx.get('impact_revenue_pct', 'N/A')}% | Impact EPS : {fx.get('impact_eps_pct', 'N/A')}%")
        lines.append(f"- FX Impact Score : {fx.get('fx_impact_score', 'N/A')}/10")
        lines.append("")

    # Events
    events = agent_data.get("events")
    if events:
        lines.append("**Agent Event-Driven :**")
        for ev in events[:5]:
            lines.append(f"- [{ev.get('type', 'N/A')}] {ev.get('description', '')} — Impact {ev.get('impact_score', 'N/A')}/10")
        lines.append("")

    # Upcoming
    upcoming = agent_data.get("upcoming")
    if upcoming:
        lines.append("**Événements à venir (Watchman) :**")
        for ev in upcoming[:5]:
            d = ev.get('days_until')
            d_str = f" (J-{d})" if d is not None else ""
            lines.append(f"- {ev.get('type', 'N/A')}{d_str} : {ev.get('details', '')}")
        lines.append("")

    # Quality gate
    qg = agent_data.get("quality")
    if qg:
        lines.append("**Data Quality Gate :**")
        lines.append(f"- Status : {qg.get('status', 'N/A')}")
        for r in qg.get("reasons", [])[:5]:
            if isinstance(r, dict):
                lines.append(f"  • [{r.get('severity', 'N/A').upper()}] {r.get('message', '')}")
            else:
                lines.append(f"  • {r}")
        lines.append("")

    # Quant
    quant = agent_data.get("quant")
    if quant:
        sig = quant.get("significance", {})
        lines.append("**Agent Quant :**")
        lines.append(f"- Significance : {sig.get('conclusion', 'N/A')} (p-value: {sig.get('p_value', 'N/A')})")
        rm = quant.get("risk_metrics", {})
        lines.append(f"- Sharpe : {rm.get('sharpe', 'N/A')} | Sortino : {rm.get('sortino', 'N/A')} | Max DD : {rm.get('max_drawdown', 'N/A')}")
        lines.append("")

    # NLP
    nlp = agent_data.get("nlp")
    if nlp:
        lines.append("**NLP Transcripts (Confiance Management) :**")
        for t in nlp[:3]:
            lines.append(f"- {t.get('quarter', 'N/A')} {t.get('year', 'N/A')} : Score Management {t.get('management_score', 'N/A')}/10 | Evasions : {t.get('evasions', 'N/A')}")
        lines.append("")

    # Major events
    maj = agent_data.get("major_events")
    if maj:
        lines.append("**Major Events Detected :**")
        for e in maj[:5]:
            lines.append(f"- [{e.get('severity', 'N/A').upper()}] {e.get('event_type', 'N/A')} : {e.get('description', '')}")
        lines.append("")

    if len(lines) == 2:
        lines.append("*Aucune donnée agent disponible pour ce ticker.*")

    return "\n".join(lines)


def compile_prompt(ticker: str, data_ctx: str, agent_ctx: str) -> str:
    """Construit le prompt unique pour le LLM."""
    return f"""Tu es le rédacteur en chef d'un desk d'analyse institutionnel (style JPM/GS/MS).
À partir des données brutes et des analyses produites par les agents IA ci-dessous,
rédige un rapport markdown complet pour **{ticker}**.

Le rapport doit suivre EXACTEMENT cette structure et ce format :

---

# {ticker} — Analyse Initiale ({now_str()})

> ⚠️ **Note :** Cette analyse a été générée par le système multi-agents Argus-IA en utilisant les agents Python réels (accounting, quant, geo, sentiment, FX, event-driven, sector rotation) + une compilation LLM unique.

---

## Résumé Exécutif
3-4 phrases maximum qui synthétisent :
1. La thèse d'investissement principale (bull/bear)
2. Le niveau de qualité de l'entreprise
3. Le timing technique
4. Le verdict global (ACHETER / ATTENDRE / SURVEILLER / ÉVITER)

---

### Market Researcher
TAM du secteur, 3-5 peers principaux avec multiples, positionnement concurrentiel, investment implications (2-3 phrases).
Si les données agents ne contiennent pas de TAM explicite, déduis du secteur/industrie dans les fondamentaux.

---

### Macro
Régime macro actif et impact sur le secteur, exposition sectorielle et sensibilités (taux, USD, pétrole, Chine).
Intègre les données de l'Agent Géopolitique et FX si disponibles.
Ajustement de pondération suggéré (Catalyseur/Valorisation/Momentum).

---

### Technique
RSI 14j, MACD, MM50/200, Golden/Death cross, volume relatif vs 20j, supports et résistances clés.
Force relative vs S&P 500 (si disponible dans sector rotation).
Timing verdict : Favorable / Neutre / Défavorable.
Score Momentum /10 (utilise le score de l'agent recommandation si présent).
Niveaux SL et TP issus de l'agent recommandation.

---

### Fondamental
Filtre Qualité (6 critères) avec score /6 et verdict [✅ Quality Compounder / ⚠️ Partielle / 🔴 Hors périmètre].
Intègre les données de l'Agent Accounting (M-Score, Z-Score, F-Score, Sloan).
Valorisation : P/E, Forward P/E, EV/EBITDA, P/B, comparaison sectorielle.
Score Valorisation /10 (utilise l'agent recommandation si présent).
Risques fondamentaux (3 max).

---

### Sentiment
Consensus analystes, options (Max Pain, Put/Call), short interest, insider trades.
Intègre l'Agent Social Sentiment (mentions Reddit, pump detection).
Intègre l'Agent Event-Driven (M&A, buybacks, guidance changes).
Score Catalyseur /10.

---

### Flux Institutionnels
13F / accumulation-distribution (si données disponibles).
ETF flows sectoriels (si disponibles).
Dark pool / block trades.
Gamma exposure / max pain (depuis les données options).
Score ajustement Catalyseur (bonus/malus).

---

## Scoring Global
| Axe | Score | Pondération |
|-----|-------|-------------|
| Catalyseur | X/10 | 35% |
| Valorisation | X/10 | 40% |
| Momentum | X/10 | 25% |
| **Score Opportunité** | **X/10** | |

Utilise les scores de l'agent recommandation si disponibles.
Si absent, évalue toi-même sur la base des données fournies.

## Niveaux et Ratio R/R
- Cours actuel : $[close]
- Stop-loss : $[SL]
- Take-profit : $[TP]
- Ratio R/R : X:1

Utilise impérativement les niveaux de l'agent recommandation s'ils existent.

## Conclusion
[ACHETER / ATTENDRE / SURVEILLER / ÉVITER]

---

**Instructions importantes :**
- Utilise EXCLUSIVEMENT les chiffres des données brutes et agents ci-dessous.
- Ne devine jamais un cours, un multiple ou une métrique.
- Si une donnée est manquante, indique [DONNÉES MANQUANTES] ou [UNSOURCED].
- Le rapport doit être concis, institutionnel, sans jargon superflu.
- Réponds UNIQUEMENT avec le rapport markdown, sans introduction ni conclusion extérieure.

---

{data_ctx}

---

{agent_ctx}

---

Rédige le rapport maintenant.
"""


def generate_summary(ticker: str, report: str) -> str:
    """Extrait un résumé exécutif du rapport généré."""
    prompt = f"""Tu es le rédacteur en chef d'un desk d'analyse institutionnel.
À partir du rapport suivant pour {ticker}, extrais un **résumé exécutif** de 3-4 phrases maximum qui synthétise :
1. La thèse d'investissement principale (bull/bear)
2. Le niveau de qualité de l'entreprise
3. Le timing technique
4. Le verdict global (ACHETER / ATTENDRE / SURVEILLER / ÉVITER)

---
{report[:6000]}
---

Réponds UNIQUEMENT avec le résumé (3-4 phrases), sans titre ni formatage."""
    return call_llm(prompt, system="Tu rédiges des résumés exécutifs concis pour des rapports institutionnels.")


def run_compile_report(ticker: str, force_agents: bool = False):
    """Pipeline complet : agents réels + compilation LLM unique."""
    ticker = ticker.upper()
    today = now_str()
    log(f"🚀 Compilation du rapport pour {ticker}")

    # ── Étape 0 : Chargement des données brutes ──
    latest = load_json(DATA_DIR / "latest.json")
    ticker_data = latest.get("prices", {}).get(ticker)
    if not ticker_data:
        raise ValueError(f"Aucune donnée trouvée pour {ticker} dans data/latest.json")

    data_ctx = build_data_context(ticker, ticker_data)

    # ── Étape 1 : Exécution des agents Python réels ──
    agent_data = load_agent_data(ticker)
    has_recommendation = agent_data.get("recommandation") is not None

    if force_agents or not has_recommendation:
        log("🔄 Agents manquants ou force_agents — relance des agents pertinents...")
        run_agents_for_ticker(ticker)
        # Recharge après exécution
        agent_data = load_agent_data(ticker)
    else:
        log("✅ Données agents déjà disponibles")

    agent_ctx = format_agent_context(ticker, agent_data)

    # ── Étape 2 : Compilation LLM unique ──
    log("🧠 Compilation LLM unique...")
    prompt = compile_prompt(ticker, data_ctx, agent_ctx)
    report = call_llm(prompt, system="Tu es un analyste institutionnel senior.")

    # ── Étape 3 : Résumé exécutif ──
    log("📝 Extraction du résumé exécutif...")
    try:
        summary = generate_summary(ticker, report)
    except Exception as e:
        log(f"⚠️  Erreur résumé : {e}")
        summary = "[Résumé non disponible — voir rapport complet]"

    # ── Étape 4 : Sauvegarde ──
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
{summary}

## Historique
| Date | Fichier | Type |
|------|---------|------|
| {today} | [{filename}]({filename}) | Analyse initiale (agents réels) |

## Agenda
- Prochain earnings : [à compléter]

## Alertes actives
- Aucune
""", encoding="utf-8")
        log("✅ INDEX.md créé")
    else:
        text = index_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "| Date | Fichier | Type |" in line:
                text = text.replace(line, line + f"\n| {today} | [{filename}]({filename}) | Analyse initiale (agents réels) |")
                break
        index_path.write_text(text, encoding="utf-8")
        log("✅ INDEX.md mis à jour")

    # CONTEXT.md
    ctx_path = ticker_dir / "CONTEXT.md"
    rec = agent_data.get("recommandation", {})
    if not ctx_path.exists():
        ctx_path.write_text(f"""# Contexte {ticker}

## Thèse active
{summary}

## Score actuel
- Opportunité : {rec.get('score_opportunite', 'N/A')}/10
- Valorisation : {rec.get('score_valorisation', 'N/A')}/10
- Momentum : {rec.get('score_momentum', 'N/A')}/10

## Niveaux
- Cours : {ticker_data.get('price', {}).get('close', 'N/A')}
- SL : {rec.get('stop_loss', '[voir rapport]')}
- TP : {rec.get('take_profit', '[voir rapport]')}

## Statut
[ACTIVE / EN SURVEILLANCE / CLOS]
""", encoding="utf-8")
        log("✅ CONTEXT.md créé")

    return str(filepath), report, agent_data


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Compilation de rapport Argus-IA (agents réels + LLM unique)")
    parser.add_argument("ticker", help="Ticker à analyser")
    parser.add_argument("--force-agents", action="store_true", help="Forcer la réexécution des agents")
    args = parser.parse_args()

    try:
        path, report, agent_data = run_compile_report(args.ticker, force_agents=args.force_agents)
        log(f"\n✅ Rapport compilé : {path}")
        log(f"   Longueur : {len(report)} caractères")
        rec = agent_data.get("recommandation")
        if rec:
            log(f"   Action : {rec.get('action')} | Score : {rec.get('score_global_ajuste', rec.get('score_global'))}/100")
    except Exception as e:
        log(f"\n❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

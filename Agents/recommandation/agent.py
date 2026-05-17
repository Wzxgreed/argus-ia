#!/usr/bin/env python3
"""
agent_recommandation.py — Agent Recommandation.

Protocol : `Agents/ORCHESTRATION.md` (scoring & pondération) + `CLAUDE.md` (tableaux de décision)

Lit tous les JSON produits par les autres agents, calcule un Score Global Composite,
et traduit en actions explicites : ACHETER / CONSERVER / ATTENDRE / RÉDUIRE / VENDRE.

Score Opportunité = (Catalyseur × A%) + (Valorisation × B%) + (Momentum × C%)
Pondération A/B/C déterminée par le régime macro actif.

Usage:
    python agents/recommandation/agent.py

Output:
    data/recommandations_YYYY-MM-DD.json  (symlink latest)
    Recommandations/YYYY-MM-DD.md           (dashboard humain)
"""

import sys
from pathlib import Path
_scripts = Path(__file__).resolve().parent.parent / 'scripts'
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
RECO_DIR = BASE_DIR / "Recommandations"
LATEST_PATH = DATA_DIR / "latest.json"


# Pondérations par régime macro (Catalyseur, Valorisation, Momentum)
REGIME_WEIGHTS = {
    "Normal":           {"catalyseur": 0.35, "valorisation": 0.40, "momentum": 0.25},
    "Risk-off":         {"catalyseur": 0.30, "valorisation": 0.45, "momentum": 0.25},
    "Risk-on/Bull":     {"catalyseur": 0.40, "valorisation": 0.30, "momentum": 0.30},
    "Pré-FOMC":         {"catalyseur": 0.35, "valorisation": 0.40, "momentum": 0.25},
    "Pré-earnings":     {"catalyseur": 0.45, "valorisation": 0.30, "momentum": 0.25},
    "Stagflation":      {"catalyseur": 0.35, "valorisation": 0.40, "momentum": 0.25},
    "Récession":        {"catalyseur": 0.25, "valorisation": 0.50, "momentum": 0.25},
    "Unknown":          {"catalyseur": 0.35, "valorisation": 0.40, "momentum": 0.25},
}


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def load_latest_json(filename: str) -> dict:
    return load_json(DATA_DIR / filename)


def get_regime_weights(macro: dict) -> dict:
    """Récupère la pondération du régime macro actif."""
    regime = macro.get("regime", {}).get("regime", "Unknown")
    return REGIME_WEIGHTS.get(regime, REGIME_WEIGHTS["Unknown"])


def compute_score_catalyseur(ticker: str, price_data: dict, all_snapshots: dict) -> float:
    """
    Score Catalyseur /10 — mesure la force des catalyseurs immédiats.
    Sources : events, earnings proche, upgrades, insider trades, news structurantes.
    """
    score = 5.0  # base neutre

    # --- Earnings proche (watchman) ---
    upcoming = all_snapshots.get("upcoming_events", {})
    events = upcoming.get("events", [])
    ticker_events = [e for e in events if e.get("ticker") == ticker]
    earnings_near = [e for e in ticker_events if e.get("type") == "earnings"]
    for ev in earnings_near:
        days = ev.get("days_until")
        if days is not None and days <= 3:
            score += 1.5
        elif days is not None and days <= 7:
            score += 0.8

    # --- Event-Driven ---
    ed = all_snapshots.get("events", {})
    te = ed.get("ticker_events", {}).get(ticker, {})
    if te:
        top_type = te.get("top_event_type", "")
        top_impact = te.get("top_event_impact_score", 0)
        if top_type == "merger" and top_impact > 0:
            score += 2.0
        elif top_type == "buyback":
            score += 1.0
        elif top_type == "activism":
            score += 1.5
        elif top_type == "guidance_change" and top_impact > 0:
            score += 1.5
        elif top_type == "guidance_change" and top_impact < 0:
            score -= 2.0

    # --- Quant (significativité des signaux) ---
    quant = all_snapshots.get("quant_report", {})
    if quant:
        p_value = quant.get("summary", {}).get("p_value", 0.05)
        if p_value < 0.05:
            score += 0.5  # Signaux statistiquement significatifs
        elif p_value > 0.20:
            score -= 1.0  # Signaux bruités

    # --- FMP consensus (upside = catalyseur latent) ---
    fmp_consensus = price_data.get("fmp_consensus", {})
    if fmp_consensus:
        pt_avg = fmp_consensus.get("price_target_avg")
        num_analysts = fmp_consensus.get("num_analysts", 0)
        close = price_data.get("price", {}).get("close", 0)
        if pt_avg and close:
            upside = (pt_avg - close) / close * 100
            if upside > 25:
                score += 1.5
            elif upside > 15:
                score += 1.0
            elif upside > 5:
                score += 0.5
            elif upside < -5:
                score -= 1.0
        if num_analysts >= 15:
            score += 0.3

    return max(0, min(10, score))


def compute_score_valorisation(ticker: str, price_data: dict, all_snapshots: dict) -> float:
    """
    Score Valorisation /10 — mesure l'attractivité des multiples.
    Sources : P/E, P/B, EV/EBITDA, FCF yield, consensus PT, filtre qualité.
    """
    score = 5.0
    fund = price_data.get("fundamentals", {})
    close = price_data.get("price", {}).get("close", 0)

    # --- Multiples fondamentaux ---
    pe = fund.get("pe_ratio")
    forward_pe = fund.get("forward_pe")
    pb = fund.get("price_to_book")
    ev_ebitda = price_data.get("fmp_key_metrics", {}).get("ev_to_ebitda")

    if pe is not None:
        if pe < 15:
            score += 1.5
        elif pe < 25:
            score += 0.5
        elif pe > 50:
            score -= 1.5
        elif pe > 40:
            score -= 0.5

    if forward_pe is not None and pe is not None:
        # Forward P/E < TTM P/E = croissance des profits attendue
        if forward_pe < pe:
            score += 0.5
        elif forward_pe > pe * 1.5:
            score -= 0.5

    if pb is not None:
        if pb < 2:
            score += 0.5
        elif pb > 10:
            score -= 0.5

    if ev_ebitda is not None:
        if ev_ebitda < 10:
            score += 0.5
        elif ev_ebitda > 25:
            score -= 0.5

    # --- FCF yield ---
    fcf_yield = price_data.get("fmp_key_metrics", {}).get("free_cash_flow_yield")
    if fcf_yield is not None:
        if fcf_yield > 0.05:
            score += 1.0
        elif fcf_yield > 0.02:
            score += 0.5
        elif fcf_yield < 0:
            score -= 1.0

    # --- Consensus PT upside ---
    fmp_consensus = price_data.get("fmp_consensus", {})
    if fmp_consensus:
        pt_avg = fmp_consensus.get("price_target_avg")
        if pt_avg and close:
            upside = (pt_avg - close) / close * 100
            if upside > 25:
                score += 1.5
            elif upside > 15:
                score += 1.0
            elif upside > 5:
                score += 0.5
            elif upside < -10:
                score -= 1.0

    # --- Filtre Qualité (accounting) ---
    accounting = all_snapshots.get("accounting_risk", {})
    analysis = accounting.get("analysis", {}).get(ticker, {})
    if analysis:
        f_score = analysis.get("piotroski", {}).get("f_score")
        if f_score is not None:
            if f_score >= 7:
                score += 1.0
            elif f_score >= 4:
                score += 0.3
            elif f_score <= 3:
                score -= 1.0
                # Plafonner si F-Score faible (règle CLAUDE.md)
                score = min(score, 5.0)

    # --- Beneish M-Score / Altman Z-Score ---
    if analysis:
        m_score = analysis.get("beneish", {}).get("m_score")
        z_score = analysis.get("altman", {}).get("z_score")
        if m_score is not None and m_score > -1.78:
            score = 2.0  # manipulation suspectée → score très faible
        if z_score is not None and z_score < 1.81:
            score = 1.0  # distress → score très faible

    return max(0, min(10, score))


def compute_score_momentum(ticker: str, price_data: dict, all_snapshots: dict) -> float:
    """
    Score Momentum /10 — mesure la force technique du cours.
    Sources : RSI, MM, change_pct, volume, ATR, golden/death cross.
    """
    score = 5.0
    technical = price_data.get("technical", {})
    price = price_data.get("price", {})

    rsi = technical.get("rsi14")
    mm50 = technical.get("mm50")
    mm200 = technical.get("mm200")
    close = price.get("close", 0)
    change_pct = price.get("change_pct", 0)
    volume = price.get("volume", 0)
    vol_avg = price.get("volume_avg_20d", 1)

    # --- RSI ---
    if rsi is not None:
        if 45 <= rsi <= 60:
            score += 1.0
        elif 60 < rsi <= 70:
            score += 0.5
        elif rsi > 70:
            score -= 1.0
        elif 30 <= rsi < 45:
            score -= 0.5
        elif rsi < 30:
            score += 0.5  # survente = possible rebound

    # --- Moyennes mobiles ---
    if close and mm50:
        if close > mm50:
            score += 1.0
        else:
            score -= 1.0

    if close and mm200 and mm200 > 0:
        if close > mm200:
            score += 0.5
        else:
            score -= 0.5

    # Golden / Death cross
    golden = technical.get("golden_cross")
    if golden is True:
        score += 0.5
    elif golden is False:
        score -= 0.5

    # --- Change % du jour ---
    if change_pct > 3:
        score += 0.5
    elif change_pct > 1:
        score += 0.3
    elif change_pct < -5:
        score -= 1.0
    elif change_pct < -3:
        score -= 0.5

    # --- Volume relatif ---
    if vol_avg > 0 and volume > vol_avg * 2:
        if change_pct > 0:
            score += 0.5
        else:
            score -= 0.5

    # --- Sector rotation ---
    sector = all_snapshots.get("sector_rotation", {})
    rankings = sector.get("rankings", [])
    ticker_rank = next((r for r in rankings if r.get("ticker") == ticker), None)
    if ticker_rank:
        rank = ticker_rank.get("rank")
        if rank is not None:
            if rank <= 3:
                score += 0.5
            elif rank >= 8:
                score -= 0.5

    return max(0, min(10, score))


def compute_score_global(ticker: str, prices_data: dict, all_snapshots: dict, macro: dict) -> dict:
    """
    Calcule le Score Global Composite pour un ticker.
    Score Opportunité = (Catalyseur × A%) + (Valorisation × B%) + (Momentum × C%)
    """
    price_data = prices_data.get(ticker, {})
    price = price_data.get("price", {})
    technical = price_data.get("technical", {})
    close = price.get("close", 0)
    atr = technical.get("atr14", 0)
    rsi = technical.get("rsi14", 50)

    # --- 1. Scores des 3 axes ---
    score_catalyseur = compute_score_catalyseur(ticker, price_data, all_snapshots)
    score_valorisation = compute_score_valorisation(ticker, price_data, all_snapshots)
    score_momentum = compute_score_momentum(ticker, price_data, all_snapshots)

    # Règle de disqualification : si un score ≤ 2 → exclure
    if score_catalyseur <= 2 or score_valorisation <= 2 or score_momentum <= 2:
        score_opportunite = min(score_catalyseur, score_valorisation, score_momentum)
    else:
        # --- 2. Pondération selon régime macro ---
        weights = get_regime_weights(macro)
        score_opportunite = (
            score_catalyseur * weights["catalyseur"]
            + score_valorisation * weights["valorisation"]
            + score_momentum * weights["momentum"]
        )

    score_opportunite = max(0, min(10, score_opportunite))

    # --- 3. Malus externes ---
    malus_accounting = 0
    malus_geo = 0
    malus_fx = 0
    malus_event = 0
    malus_social = 0
    bonus_event = 0
    bonus_buyback = 0
    bonus_sector = 0

    # Accounting
    accounting = all_snapshots.get("accounting_risk", {})
    acc_ticker = accounting.get("ticker_assessments", {}).get(ticker, {})
    if not acc_ticker:
        # Fallback sur le nouveau format
        acc_ticker = accounting.get("analysis", {}).get(ticker, {})
    if acc_ticker:
        m_score = acc_ticker.get("m_score", -5)
        z_score = acc_ticker.get("z_score", 5)
        if m_score is not None and m_score > -1.78:
            malus_accounting = 25
        elif z_score is not None and z_score < 1.81:
            malus_accounting = 25

    # Geo
    geo = all_snapshots.get("geo_risk", {})
    geo_ticker = geo.get("ticker_exposure", {}).get(ticker, {})
    if geo_ticker:
        geo_score = geo_ticker.get("geo_risk_score", 0)
        if geo_score >= 7:
            malus_geo = 15
        elif geo_score >= 4:
            malus_geo = 5

    # FX
    fx = all_snapshots.get("fx_exposure", {})
    fx_tickers = fx.get("tickers", [])
    fx_ticker = next((t for t in fx_tickers if t["ticker"] == ticker), {})
    if fx_ticker:
        fx_score = fx_ticker.get("fx_impact_score", 0)
        direction = fx_ticker.get("direction_label", "neutral")
        if fx_score >= 7 and direction == "headwind":
            malus_fx = 10
        elif fx_score >= 4 and direction == "headwind":
            malus_fx = 5

    # Event-Driven
    events = all_snapshots.get("events", {})
    event_tickers = events.get("ticker_events", {})
    event_ticker = event_tickers.get(ticker, {})
    if event_ticker:
        top_type = event_ticker.get("top_event_type", "")
        top_impact = event_ticker.get("top_event_impact_score", 0)
        if top_type == "guidance_change" and top_impact < -5:
            malus_event = 15
        elif top_type == "merger" and top_impact > 0:
            bonus_event = 15
        elif top_type == "buyback":
            bonus_buyback = 8
        elif top_type == "activism":
            bonus_event = 10

    # Social
    social = all_snapshots.get("social_sentiment", {})
    social_tickers = social.get("tickers", [])
    social_ticker = next((t for t in social_tickers if t["ticker"] == ticker), {})
    if social_ticker:
        sentiment = social_ticker.get("sentiment_score", 5)
        pump = social_ticker.get("pump_detected", False)
        if pump:
            malus_social = 10
        if sentiment < 2:
            malus_social = max(malus_social, 5)

    # --- 4. Score Global Composite ---
    score_global = (
        score_opportunite * 10
        - malus_accounting
        - malus_geo
        - malus_fx
        - malus_event
        - malus_social
        + bonus_event
        + bonus_buyback
        + bonus_sector
    )
    score_global = max(0, min(100, score_global))

    # --- 5. Timing technique ---
    timing_malus = 0
    timing_bonus = 0

    if rsi is not None:
        if rsi > 70:
            timing_malus += 15
        elif rsi < 30:
            timing_bonus += 5

    mm50 = technical.get("mm50")
    if mm50 and close:
        if close < mm50:
            timing_malus += 8
        else:
            timing_bonus += 5

    mm200 = technical.get("mm200")
    if mm200 and close and mm200 > 0:
        if close < mm200:
            timing_malus += 5

    vol = price.get("volume", 0)
    vol_avg = price.get("volume_avg_20d", 1)
    if vol_avg > 0 and vol > vol_avg * 2:
        if change_pct > 0:
            timing_bonus += 5
        else:
            timing_malus += 5

    score_global_ajuste = score_global - timing_malus + timing_bonus
    score_global_ajuste = max(0, min(100, score_global_ajuste))

    # --- 6. Détermination de l'action ---
    if score_global_ajuste >= 75:
        action = "ACHETER"
        direction = "Long"
        sizing = "Standard"
    elif score_global_ajuste >= 60:
        action = "ACHETER"
        direction = "Long"
        sizing = "Réduit"
    elif score_global_ajuste >= 50:
        action = "ATTENDRE"
        direction = "Neutre"
        sizing = "—"
    elif score_global_ajuste >= 35:
        action = "SURVEILLER"
        direction = "Neutre"
        sizing = "—"
    else:
        action = "ÉVITER"
        direction = "Neutre"
        sizing = "—"

    # Override si malus accounting majeur
    if malus_accounting >= 25:
        action = "ÉVITER"
        direction = "Neutre"

    # --- 7. Niveaux ---
    prix_entree = close if close else 0
    stop_loss = round(close - 2 * atr, 2) if close and atr else None
    take_profit = round(close + 3 * atr, 2) if close and atr else None
    rr_ratio = None
    if take_profit and stop_loss and close:
        gain = take_profit - close
        perte = close - stop_loss
        if perte > 0:
            rr_ratio = round(gain / perte, 1)

    # --- 8. Justification ---
    justification = []
    justification.append(f"Score Opportunité {score_opportunite:.1f}/10 (C:{score_catalyseur:.1f} V:{score_valorisation:.1f} M:{score_momentum:.1f})")

    if score_catalyseur >= 7:
        justification.append(f"🟢 Catalyseur fort ({score_catalyseur:.1f}/10)")
    elif score_catalyseur <= 4:
        justification.append(f"🔴 Catalyseur faible ({score_catalyseur:.1f}/10)")

    if score_valorisation >= 7:
        justification.append(f"🟢 Valorisation attractive ({score_valorisation:.1f}/10)")
    elif score_valorisation <= 4:
        justification.append(f"🔴 Valorisation défavorable ({score_valorisation:.1f}/10)")

    if score_momentum >= 7:
        justification.append(f"🟢 Momentum haussier ({score_momentum:.1f}/10)")
    elif score_momentum <= 4:
        justification.append(f"🔴 Momentum baissier ({score_momentum:.1f}/10)")

    if rsi is not None:
        if 40 <= rsi <= 60:
            justification.append(f"RSI {rsi:.0f} — zone neutre favorable")
        elif rsi > 70:
            justification.append(f"RSI {rsi:.0f} — surachat technique")
        elif rsi < 30:
            justification.append(f"RSI {rsi:.0f} — survente technique")

    if close and mm50 and close > mm50:
        justification.append("Cours au-dessus de MM50 — tendance haussière")
    elif close and mm50:
        justification.append("Cours sous MM50 — tendance baissière")

    if malus_accounting >= 25:
        justification.append("🔴 Risque accounting majeur — M-Score ou Z-Score critique")
    if malus_geo >= 10:
        justification.append("🟡 Risque géopolitique élevé")
    if malus_fx >= 5:
        justification.append("🟡 Headwind FX détecté")
    if bonus_event >= 10:
        justification.append("🟢 Événement corporate favorable détecté")
    if malus_social >= 5:
        justification.append("🟡 Signal social négatif (pump/sentiment extrême)")

    risques = []
    if event_ticker and event_ticker.get("event_count", 0) > 0:
        risques.append("Événement corporate en cours — surveillance recommandée")
    if fx_ticker and fx_ticker.get("divergence_flag") == "underperformance":
        risques.append("Divergence FX/cours — autre facteur négatif en cours")

    return {
        "ticker": ticker,
        "action": action,
        "direction": direction,
        "score_global": round(score_global, 1),
        "score_global_ajuste": round(score_global_ajuste, 1),
        "score_opportunite": round(score_opportunite, 1),
        "score_catalyseur": round(score_catalyseur, 1),
        "score_valorisation": round(score_valorisation, 1),
        "score_momentum": round(score_momentum, 1),
        "timing": "Favorable" if timing_bonus > timing_malus else "Défavorable" if timing_malus > timing_bonus else "Neutre",
        "horizon": "1–3 mois" if action == "ACHETER" else "—",
        "prix_actuel": round(close, 2) if close else None,
        "prix_entree_suggere": round(prix_entree, 2) if prix_entree else None,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "risque_rendement_ratio": rr_ratio,
        "sizing": sizing,
        "justification": justification,
        "risques": risques,
        "alertes": [],
    }


def main():
    print("[reco] Starting recommendation engine...", file=sys.stderr)

    config = load_config()
    tickers_data = config.get("tickers", [])
    latest = load_json(LATEST_PATH)

    if not latest:
        print("[reco] ERROR: No latest.json found", file=sys.stderr)
        return 1

    prices_data = latest.get("prices", {})
    macro = latest.get("macro", {})

    # Charger tous les snapshots
    all_snapshots = {
        "accounting_risk": load_latest_json("accounting_risk_latest.json"),
        "geo_risk": load_latest_json("geo_risk_latest.json"),
        "fx_exposure": load_latest_json("fx_exposure_latest.json"),
        "events": load_latest_json("events_latest.json"),
        "social_sentiment": load_latest_json("social_sentiment_latest.json"),
        "quant_report": load_latest_json("quant_report_latest.json"),
        "crypto_correlation": load_latest_json("crypto_correlation_latest.json"),
        "sector_rotation": load_latest_json("sector_rotation_latest.json"),
        "upcoming_events": load_latest_json("upcoming_events_latest.json"),
    }

    reco_count = {"acheter": 0, "conserver": 0, "attendre": 0, "surveiller": 0, "eviter": 0}
    recommandations = []

    for ticker_data in tickers_data:
        ticker = ticker_data["ticker"]
        print(f"[reco] Analyzing {ticker}...", file=sys.stderr)

        reco = compute_score_global(ticker, prices_data, all_snapshots, macro)
        recommandations.append(reco)

        action_key = reco["action"].lower().replace("é", "e")
        if action_key in reco_count:
            reco_count[action_key] += 1

        print(
            f"[reco]   {ticker}: {reco['action']} (Score Global {reco['score_global_ajuste']}/100, "
            f"Opportunité {reco['score_opportunite']}/10 — C:{reco['score_catalyseur']} V:{reco['score_valorisation']} M:{reco['score_momentum']})",
            file=sys.stderr
        )

    # Tri par score global décroissant
    recommandations.sort(key=lambda x: x["score_global_ajuste"], reverse=True)

    # Build JSON report
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    macro_data = macro.get("data", {})
    dxy = macro_data.get("dxy", {})
    vix = macro_data.get("vix", {})
    regime = macro.get("regime", {}).get("regime", "Unknown")
    weights = get_regime_weights(macro)

    report = {
        "meta": {
            "date": date_str,
            "regime_macro": regime,
            "regime_weights": {k: round(v, 2) for k, v in weights.items()},
            "dxy_trend": round(dxy.get("change_pct", 0), 2) if dxy else 0,
            "vix": round(vix.get("value", 0), 2) if vix else 0,
            "total_tickers": len(tickers_data),
            "recommandations_count": reco_count,
        },
        "recommandations": recommandations,
    }

    # Write JSON
    output_path = DATA_DIR / f"recommandations_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "recommandations_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    # Write Markdown dashboard
    reco_md = RECO_DIR / f"{date_str}.md"
    with open(reco_md, "w", encoding="utf-8") as f:
        f.write(f"# Recommandations du Jour — {date_str}\n\n")
        f.write("## Contexte macro\n")
        f.write(f"**Régime :** {report['meta']['regime_macro']} | ")
        f.write(f"**VIX :** {report['meta']['vix']} | ")
        f.write(f"**DXY :** {report['meta']['dxy_trend']}% | ")
        f.write(f"**Pondération :** Catalyseur {report['meta']['regime_weights']['catalyseur']:.0%}, ")
        f.write(f"Valorisation {report['meta']['regime_weights']['valorisation']:.0%}, ")
        f.write(f"Momentum {report['meta']['regime_weights']['momentum']:.0%}\n\n")
        f.write("---\n\n")

        # Group by action
        actions_order = ["ACHETER", "CONSERVER", "ATTENDRE", "SURVEILLER", "ÉVITER"]
        for action in actions_order:
            group = [r for r in recommandations if r["action"] == action]
            if not group:
                continue

            emoji = {"ACHETER": "🟢", "CONSERVER": "🟡", "ATTENDRE": "⚪", "SURVEILLER": "🟠", "ÉVITER": "🔴"}.get(action, "⚪")
            f.write(f"## {emoji} {action} ({len(group)})\n\n")

            for r in group:
                f.write(f"### {r['ticker']} — {action} (Score Global {r['score_global_ajuste']}/100)\n")
                f.write(f"| | |\n|---|---|\n")
                if r['prix_actuel']:
                    f.write(f"| **Prix actuel** | ${r['prix_actuel']} |\n")
                f.write(f"| **Score Opportunité** | {r['score_opportunite']}/10 (C:{r['score_catalyseur']} V:{r['score_valorisation']} M:{r['score_momentum']}) |\n")
                if r['stop_loss']:
                    f.write(f"| **Stop-loss suggéré** | ${r['stop_loss']} |\n")
                if r['take_profit']:
                    f.write(f"| **Take-profit suggéré** | ${r['take_profit']} |\n")
                if r['risque_rendement_ratio']:
                    f.write(f"| **Ratio R/R** | {r['risque_rendement_ratio']} |\n")
                if r['horizon'] != "—":
                    f.write(f"| **Horizon** | {r['horizon']} |\n")
                if r['sizing'] != "—":
                    f.write(f"| **Sizing** | {r['sizing']} |\n")
                f.write("\n")

                if r['justification']:
                    f.write("**Pourquoi :**\n")
                    for j in r['justification']:
                        f.write(f"- {j}\n")
                    f.write("\n")

                if r['risques']:
                    f.write("**Risques :**\n")
                    for risk in r['risques']:
                        f.write(f"- {risk}\n")
                    f.write("\n")

                f.write("\n")

        f.write("---\n\n")
        f.write("## Résumé\n\n")
        f.write(f"| Action | Count |\n|---|---|\n")
        for k, v in reco_count.items():
            f.write(f"| {k.capitalize()} | {v} |\n")
        f.write("\n")
        f.write("---\n\n")
        f.write("> **Avertissement :** Ces recommandations sont des outils d'analyse, pas des conseils en investissement. "
                "Le système n'effectue pas de prédictions de cours futures. Vérifiez toujours les données avant de décider.\n")

    print(
        f"[reco] Report written → {output_path} | Dashboard → {reco_md} | "
        f"Acheter: {reco_count['acheter']}, Éviter: {reco_count['eviter']}",
        file=sys.stderr
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())

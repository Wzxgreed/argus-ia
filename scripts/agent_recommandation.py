#!/usr/bin/env python3
"""
agent_recommandation.py — Agent Recommandation.

Lit tous les JSON produits par les autres agents, calcule un Score Global Composite,
et traduit en actions explicites : ACHETER / CONSERVER / ATTENDRE / RÉDUIRE / VENDRE.

Usage:
    python scripts/agent_recommandation.py

Output:
    data/recommandations_YYYY-MM-DD.json  (symlink latest)
    Recommandations/YYYY-MM-DD.md           (dashboard humain)
"""

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


def compute_score_global(ticker: str, prices_data: dict, all_snapshots: dict) -> dict:
    """
    Calcule le Score Global Composite pour un ticker.
    Retourne un dict avec score, action, niveaux, justification.
    """
    # Données de base
    price_data = prices_data.get(ticker, {})
    price = price_data.get("price", {})
    technical = price_data.get("technical", {})
    fundamentals = price_data.get("fundamentals", {})
    options = price_data.get("options", {})

    # Valeurs par défaut
    close = price.get("close", 0)
    atr = technical.get("atr14", 0)
    rsi = technical.get("rsi14", 50)
    mm50 = technical.get("mm50", close)
    mm200 = technical.get("mm200", close)
    change_pct = price.get("change_pct", 0)

    # --- 1. Score Opportunité de base (proxy depuis les données disponibles) ---
    score_opportunite = 5.0

    # Ajustement RSI
    if rsi is not None:
        if 40 <= rsi <= 60:
            score_opportunite += 1.0
        elif rsi > 70:
            score_opportunite -= 1.5
        elif rsi < 30:
            score_opportunite += 0.5  # Survente = possible rebound

    # Ajustement momentum
    if change_pct > 2:
        score_opportunite += 0.5
    elif change_pct < -5:
        score_opportunite -= 1.0

    # Ajustement FMP consensus
    fmp_consensus = price_data.get("fmp_consensus", {})
    if fmp_consensus:
        pt_avg = fmp_consensus.get("price_target_avg")
        num_analysts = fmp_consensus.get("num_analysts", 0)
        if pt_avg and close:
            upside = (pt_avg - close) / close * 100
            if upside > 20:
                score_opportunite += 1.0
            elif upside > 10:
                score_opportunite += 0.5
            elif upside < 0:
                score_opportunite -= 0.5
        if num_analysts >= 10:
            score_opportunite += 0.3

    score_opportunite = max(0, min(10, score_opportunite))

    # --- 2. Malus externes ---
    malus_accounting = 0
    malus_geo = 0
    malus_fx = 0
    malus_event = 0
    malus_social = 0
    malus_quant = 0
    bonus_event = 0
    bonus_buyback = 0
    bonus_sector = 0

    # Accounting
    accounting = all_snapshots.get("accounting_risk", {})
    acc_ticker = accounting.get("ticker_assessments", {}).get(ticker, {})
    if acc_ticker:
        m_score = acc_ticker.get("m_score", -5)
        z_score = acc_ticker.get("z_score", 5)
        if m_score > -1.78 or z_score < 1.81:
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

    # Quant
    quant = all_snapshots.get("quant_report", {})
    if quant:
        p_value = quant.get("summary", {}).get("p_value", 0.05)
        if p_value > 0.20:
            malus_quant = 15
        elif p_value > 0.10:
            malus_quant = 8

    # --- 3. Score Global Composite ---
    score_global = (
        score_opportunite * 10
        - malus_accounting
        - malus_geo
        - malus_fx
        - malus_event
        - malus_social
        - malus_quant
        + bonus_event
        + bonus_buyback
        + bonus_sector
    )
    score_global = max(0, min(100, score_global))

    # --- 4. Timing technique ---
    timing_malus = 0
    timing_bonus = 0

    if rsi is not None:
        if rsi > 70:
            timing_malus += 15
        elif rsi < 30:
            timing_bonus += 5

    if mm50 and close:
        if close < mm50:
            timing_malus += 8
        else:
            timing_bonus += 5

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

    # --- 5. Détermination de l'action ---
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

    # --- 6. Niveaux ---
    prix_entree = close if close else 0
    stop_loss = round(close - 2 * atr, 2) if close and atr else None
    take_profit = round(close + 3 * atr, 2) if close and atr else None
    rr_ratio = None
    if take_profit and stop_loss and close:
        gain = take_profit - close
        perte = close - stop_loss
        if perte > 0:
            rr_ratio = round(gain / perte, 1)

    # --- 7. Justification ---
    justification = []
    if score_opportunite >= 7:
        justification.append(f"Score Opportunité élevé ({score_opportunite:.1f}/10)")
    elif score_opportunite <= 4:
        justification.append(f"Score Opportunité faible ({score_opportunite:.1f}/10)")

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
    }

    reco_count = {"acheter": 0, "conserver": 0, "attendre": 0, "surveiller": 0, "eviter": 0}
    recommandations = []

    for ticker_data in tickers_data:
        ticker = ticker_data["ticker"]
        print(f"[reco] Analyzing {ticker}...", file=sys.stderr)

        reco = compute_score_global(ticker, prices_data, all_snapshots)
        recommandations.append(reco)

        action_key = reco["action"].lower().replace("é", "e")
        if action_key in reco_count:
            reco_count[action_key] += 1

        print(
            f"[reco]   {ticker}: {reco['action']} (Score {reco['score_global_ajuste']}/100)",
            file=sys.stderr
        )

    # Tri par score global décroissant
    recommandations.sort(key=lambda x: x["score_global_ajuste"], reverse=True)

    # Build JSON report
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    macro = latest.get("macro", {}).get("data", {})
    dxy = macro.get("dxy", {})
    vix = macro.get("vix", {})

    report = {
        "meta": {
            "date": date_str,
            "regime_macro": latest.get("macro", {}).get("regime", {}).get("regime", "Unknown"),
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
        f.write(f"**Trend :** {'Risk-on' if report['meta']['dxy_trend'] < 0 else 'Risk-off' if report['meta']['dxy_trend'] > 1 else 'Neutre'}\n\n")
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

#!/usr/bin/env python3
"""
update_context.py — Mémoire court terme par ticker (CONTEXT.md).

Génère pour chaque ticker un fichier CONTEXT.md contenant :
  • Thèse active (extraite de INDEX.md)
  • Erreurs de prédiction (SUIVI_PRIX_CIBLES.md + SUIVI_EARNINGS_PREDICTIONS.md)
  • Alertes actives (Alertes/ALERTES.md)
  • Prochains événements (Alertes/UPCOMING_EVENTS.md)
  • Contexte technique (data/latest.json)
  • Résumé de la dernière analyse

Usage:
    python agents/update_context/agent.py

Output:
    Actions/[TICKER]/CONTEXT.md pour chaque ticker de la watchlist.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"
ACTIONS_DIR = BASE_DIR / "Actions"
ALERTES_PATH = BASE_DIR / "Alertes" / "ALERTES.md"
UPCOMING_PATH = BASE_DIR / "Alertes" / "UPCOMING_EVENTS.md"
SUIVI_PRIX_PATH = ACTIONS_DIR / "SUIVI_PRIX_CIBLES.md"
SUIVI_EARNINGS_PATH = ACTIONS_DIR / "SUIVI_EARNINGS_PREDICTIONS.md"


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_latest() -> dict:
    latest = DATA_DIR / "latest.json"
    if not latest.exists():
        return {}
    try:
        target = latest.resolve()
        with open(target, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def parse_index_md(index_path: Path) -> dict:
    """Parse INDEX.md pour extraire thèse, score, prix cible, SL, statut."""
    if not index_path.exists():
        return {}
    text = index_path.read_text(encoding="utf-8")
    result = {
        "recommandation": None,
        "score": None,
        "prix_cible": None,
        "stop_loss": None,
        "statut_thesis": None,
        "horizon": None,
    }

    # Recommandation : texte après **Recommandation :**
    m = re.search(r"\*\*Recommandation\s*:\s*\*\*([^|]+)", text)
    if m:
        result["recommandation"] = m.group(1).strip()

    # Score
    m = re.search(r"\*\*Score\s*:\s*\*\*\s*([0-9.]+)/10", text)
    if m:
        result["score"] = float(m.group(1))

    # Prix cible
    m = re.search(r"\*\*Prix cible\s*:\s*\*\*\s*[$]?([0-9.,]+)", text)
    if m:
        result["prix_cible"] = m.group(1).replace(",", "").strip()

    # Stop-loss
    m = re.search(r"\*\*Stop-loss\s*:\s*\*\*\s*[$]?([0-9.,]+)", text)
    if m:
        result["stop_loss"] = m.group(1).replace(",", "").strip()

    # Statut thèse (validée/modifiée/invalide)
    for status in ["validée", "modifiée", "invalide"]:
        if status in text.lower():
            result["statut_thesis"] = status
            break

    # Horizon
    m = re.search(r"\*\*Horizon\s*:\s*\*\*\s*([^\n|]+)", text)
    if m:
        result["horizon"] = m.group(1).strip()

    return result


def get_latest_analysis(ticker_dir: Path) -> dict:
    """Retourne le fichier .md le plus récent (par date dans le nom) et son résumé."""
    md_files = [f for f in ticker_dir.iterdir() if f.suffix == ".md" and f.name != "CONTEXT.md"]
    # Filtrer ceux avec une date YYYY-MM-DD dans le nom
    dated = []
    for f in md_files:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
        if m:
            dated.append((m.group(1), f))
    if not dated:
        return {}
    dated.sort(key=lambda x: x[0], reverse=True)
    latest_date, latest_file = dated[0]

    # Extraire un résumé : première phrase de la section conclusion ou thèse
    text = latest_file.read_text(encoding="utf-8")
    summary = ""
    # Chercher une phrase après un titre "Conclusion" ou "Thèse"
    for pattern in [
        r"#{1,3}\s*Conclusion\s*\n+([^\n#.]{20,300})",
        r"#{1,3}\s*Thèse\s*\n+([^\n#.]{20,300})",
    ]:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            summary = m.group(1).strip()
            break
    if not summary:
        # Fallback : première phrase non-titre du fichier
        lines = [l.strip() for l in text.splitlines() if l.strip() and not l.strip().startswith("#")]
        if lines:
            summary = lines[0][:200]

    # Type d'analyse
    type_analyse = "init"
    if "_update." in latest_file.name:
        type_analyse = "update"
    elif "_earnings." in latest_file.name:
        type_analyse = "earnings"
    elif "_preview." in latest_file.name:
        type_analyse = "preview"
    elif "_refresh" in latest_file.name or "full refresh" in text.lower():
        type_analyse = "full refresh"

    return {
        "date": latest_date,
        "type": type_analyse,
        "file": latest_file.name,
        "summary": summary,
    }


def parse_tracking_errors(ticker: str, suivi_path: Path) -> list[dict]:
    """Parse SUIVI_PRIX_CIBLES.md ou SUIVI_EARNINGS_PREDICTIONS.md pour les Miss/Imprécis."""
    if not suivi_path.exists():
        return []
    text = suivi_path.read_text(encoding="utf-8")
    errors = []
    # Chercher les lignes de tableau contenant le ticker et un verdict négatif
    for line in text.splitlines():
        if ticker not in line:
            continue
        # Prix cibles : Miss
        if "❌ Miss" in line or "⚠️ Partiel" in line or "❌ Imprécis" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 6:
                errors.append({
                    "date": parts[1] if len(parts) > 1 else "",
                    "type": "prix cible" if "Prix cible" in suivi_path.name else "earnings",
                    "error": "Miss / Imprécis",
                    "lesson": f"Ligne: {' | '.join(parts[:6])}",
                })
    return errors


def parse_alertes(ticker: str) -> list[str]:
    """Parse Alertes/ALERTES.md pour les alertes actives du ticker."""
    if not ALERTES_PATH.exists():
        return []
    text = ALERTES_PATH.read_text(encoding="utf-8")
    alerts = []
    in_table = False
    for line in text.splitlines():
        if "| Ticker |" in line and "Type |" in line:
            in_table = True
            continue
        if in_table and line.startswith("|") and ticker in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4:
                alert_type = parts[2] if len(parts) > 2 else ""
                seuil = parts[3] if len(parts) > 3 else ""
                statut = parts[5] if len(parts) > 5 else ""
                alerts.append(f"{alert_type} — {seuil} — {statut}")
    return alerts


def parse_upcoming_events(ticker: str) -> list[dict]:
    """Parse Alertes/UPCOMING_EVENTS.md pour les événements du ticker."""
    if not UPCOMING_PATH.exists():
        return []
    text = UPCOMING_PATH.read_text(encoding="utf-8")
    events = []
    for line in text.splitlines():
        if ticker not in line:
            continue
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 5 and parts[1] == ticker:
            event_type = parts[2] if len(parts) > 2 else ""
            date_ev = parts[3] if len(parts) > 3 else ""
            detail = parts[5] if len(parts) > 5 else ""
            events.append({"type": event_type, "date": date_ev, "detail": detail})
    return events


def get_technical_context(ticker: str, latest: dict) -> dict:
    """Extrait RSI, MM, ATR, volume depuis latest.json."""
    data = latest.get("prices", {}).get(ticker, {})
    price = data.get("price", {})
    tech = data.get("technical", {})
    return {
        "rsi14": tech.get("rsi14"),
        "mm50": tech.get("mm50"),
        "mm200": tech.get("mm200"),
        "atr14": tech.get("atr14"),
        "volume_avg_20d": price.get("volume_avg_20d"),
    }


def build_context_md(ticker: str, ctx: dict) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"# CONTEXT — {ticker} — Dernière mise à jour : {today}",
        "",
        "> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.",
        "> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.",
        "",
        "---",
        "",
        "## 🎯 Thèse active",
        "",
    ]

    thesis = ctx.get("thesis", {})
    reco = thesis.get("recommandation") or "—"
    score = thesis.get("score") or "—"
    pt = thesis.get("prix_cible") or "—"
    sl = thesis.get("stop_loss") or "—"
    statut = thesis.get("statut_thesis") or "—"
    horizon = thesis.get("horizon") or "—"

    lines += [
        f"- **Recommandation :** {reco}",
        f"- **Score global :** {score}/10",
        f"- **Prix cible :** ${pt}",
        f"- **Stop-loss :** ${sl}",
        f"- **Statut thèse :** {statut}",
        f"- **Horizon :** {horizon}",
        "",
        "---",
        "",
        "## 📉 Erreurs de prédiction récentes",
        "",
    ]

    errors = ctx.get("errors", [])
    if errors:
        for e in errors[:5]:  # Max 5 erreurs
            lines.append(f"- **{e['date']}** · {e['type']} · {e['error']} · {e['lesson']}")
    else:
        lines.append("- Aucune erreur enregistrée.")

    lines += [
        "",
        "---",
        "",
        "## 🚨 Alertes actives",
        "",
    ]

    alerts = ctx.get("alertes", [])
    if alerts:
        for a in alerts:
            lines.append(f"- {a}")
    else:
        lines.append("- Aucune alerte active.")

    lines += [
        "",
        "---",
        "",
        "## 📅 Prochains événements",
        "",
    ]

    events = ctx.get("events", [])
    if events:
        for ev in events[:5]:
            lines.append(f"- **{ev['date']}** · {ev['type']} · {ev['detail']}")
    else:
        lines.append("- Aucun événement à venir.")

    lines += [
        "",
        "---",
        "",
        "## 📊 Contexte technique (dernier snapshot)",
        "",
    ]

    tech = ctx.get("technical", {})
    lines.append(f"- **RSI 14j :** {tech.get('rsi14') or '—'}")
    lines.append(f"- **MM 50j :** {tech.get('mm50') or '—'}")
    lines.append(f"- **MM 200j :** {tech.get('mm200') or '—'}")
    lines.append(f"- **ATR 14j :** {tech.get('atr14') or '—'}")
    lines.append(f"- **Volume moy. 20j :** {tech.get('volume_avg_20d') or '—'}")

    lines += [
        "",
        "---",
        "",
        "## 📝 Résumé dernière analyse",
        "",
    ]

    last = ctx.get("latest_analysis", {})
    if last:
        lines.append(f"- **Date :** {last.get('date') or '—'}")
        lines.append(f"- **Type :** {last.get('type') or '—'}")
        lines.append(f"- **Fichier :** `{last.get('file') or '—'}`")
        lines.append(f"- **Conclusion :** {last.get('summary') or '—'}")
    else:
        lines.append("- Aucune analyse enregistrée.")

    lines += [
        "",
        "---",
        "",
        "## 🔄 Triggers détectés (full refresh)",
        "",
    ]

    triggers = ctx.get("triggers", [])
    if triggers:
        for t in triggers:
            lines.append(f"- {t}")
    else:
        lines.append("- Aucun trigger récent.")

    lines += [
        "",
        "---",
        "",
        "*Généré automatiquement — ne pas éditer manuellement.*",
        "",
    ]

    return "\n".join(lines)


def main():
    config = load_config()
    tickers = [t["ticker"] for t in config.get("tickers", [])]
    latest = load_latest()

    updated = 0
    for ticker in tickers:
        ticker_dir = ACTIONS_DIR / ticker.upper()
        if not ticker_dir.exists():
            continue

        ctx = {
            "ticker": ticker,
            "thesis": parse_index_md(ticker_dir / "INDEX.md"),
            "latest_analysis": get_latest_analysis(ticker_dir),
            "errors": [],
            "alertes": parse_alertes(ticker),
            "events": parse_upcoming_events(ticker),
            "technical": get_technical_context(ticker, latest),
            "triggers": [],
        }

        # Erreurs de prix cibles + earnings
        ctx["errors"].extend(parse_tracking_errors(ticker, SUIVI_PRIX_PATH))
        ctx["errors"].extend(parse_tracking_errors(ticker, SUIVI_EARNINGS_PATH))

        # Triggers depuis REFRESH_LOG.md si présent
        refresh_log = ticker_dir / "REFRESH_LOG.md"
        if refresh_log.exists():
            text = refresh_log.read_text(encoding="utf-8")
            for line in text.splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith("|") or stripped.startswith("#") or stripped.startswith("**"):
                    continue
                if any(k in stripped for k in ("PRICE_GAP", "ATR_SPIKE", "VOLUME_SPIKE", "NEWS_KEYWORD", "EARNINGS_SURPRISE", "GOLDEN_CROSS", "DEATH_CROSS")):
                    ctx["triggers"].append(stripped.lstrip("- ").strip())

        md = build_context_md(ticker, ctx)
        (ticker_dir / "CONTEXT.md").write_text(md, encoding="utf-8")
        updated += 1

    print(f"[update_context] {updated} CONTEXT.md mis à jour.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

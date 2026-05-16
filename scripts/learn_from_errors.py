#!/usr/bin/env python3
"""
learn_from_errors.py — Boucle d'apprentissage automatique.

Chaque matin, ce script vérifie les fenêtres de suivi ouvertes, calcule les
performances réelles via yfinance, met à jour les verdicts, et extrait des
règles d'apprentissage sur les erreurs.

Intégration :
    bash scripts/run_morning.sh (étape 0b, avant fetch_prices)

Sources :
    - Opportunités/BACKTESTING.md — signaux J+5/J+20/J+60
    - Actions/SUIVI_PRIX_CIBLES.md — prix cibles J+30/J+90/J+180

Cibles :
    - Mêmes fichiers (mise à jour des verdicts)
    - Agents/APPRENTISSAGES.md (règles extraites)
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import yfinance as yf

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

BACKTESTING_PATH = BASE_DIR / "Opportunités" / "BACKTESTING.md"
SUIVI_PRIX_PATH = BASE_DIR / "Actions" / "SUIVI_PRIX_CIBLES.md"
APPRENTISSAGES_PATH = BASE_DIR / "Agents" / "APPRENTISSAGES.md"
POST_MORTEMS_DIR = BASE_DIR / "Agents" / "POST_MORTEMS"

today = datetime.now(timezone.utc).date()

# Seuils de verdict (tolerance ±2%)
HIT_THRESHOLD = 0.02
MISS_THRESHOLD = -0.02

# Fenêtres actives
HORIZONS_BT = {"J+5": 5, "J+20": 20, "J+60": 60}
HORIZONS_PC = {"J+30": 30, "J+90": 90, "J+180": 180}

# ---------------------------------------------------------------------------
# Markdown table parsing helpers (no heavy deps)
# ---------------------------------------------------------------------------


def parse_markdown_table(text: str, header_keywords: list[str]) -> list[dict]:
    """
    Parse le premier tableau markdown trouvé dont l'en-tête contient
    au moins un des mots-clés.
    Retourne une liste de dicts {col_name: value}.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if not any(kw.lower() in " ".join(cols).lower() for kw in header_keywords):
            continue
        # Ligne suivante doit être le séparateur |---|---|
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        header = cols
        rows = []
        for j in range(i + 2, len(lines)):
            row_line = lines[j].strip()
            if not row_line.startswith("|"):
                break
            cells = [c.strip() for c in row_line.split("|")[1:-1]]
            if len(cells) != len(header):
                continue
            rows.append({header[idx]: cells[idx] for idx in range(len(header))})
        return rows
    return []


def replace_table_rows(text: str, header_keywords: list[str], new_rows: list[dict]) -> str:
    """
    Remplace les lignes de données du premier tableau matching
    header_keywords par new_rows (mêmes colonnes).
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if not any(kw.lower() in " ".join(cols).lower() for kw in header_keywords):
            continue
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        header = cols
        # Trouver la fin du tableau
        end_idx = i + 2
        for j in range(i + 2, len(lines)):
            if not lines[j].strip().startswith("|"):
                end_idx = j
                break
            end_idx = j + 1
        # Construire les nouvelles lignes
        new_lines = [line, lines[i + 1]]
        for row in new_rows:
            cells = [str(row.get(col, "")).strip() for col in header]
            new_lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines[:i] + new_lines + lines[end_idx:])
    return text


# ---------------------------------------------------------------------------
# Price helpers
# ---------------------------------------------------------------------------


def get_close_on_date(ticker: str, target_date: datetime.date) -> float | None:
    """
    Récupère le cours de clôture le plus proche de target_date via yfinance.
    Retourne None si aucune donnée.
    """
    try:
        stock = yf.Ticker(ticker)
        # Prendre une fenêtre suffisante pour couvrir target_date
        start = target_date - timedelta(days=10)
        end = target_date + timedelta(days=3)
        hist = stock.history(start=start.isoformat(), end=end.isoformat())
        if hist.empty:
            return None
        # Index est timezone-aware UTC ; normaliser target_date
        for date_idx in hist.index:
            d = date_idx.tz_convert("UTC").date()
            if d == target_date:
                return round(float(hist.loc[date_idx, "Close"]), 2)
        # Si pas de match exact, prendre le dernier avant
        before = hist[hist.index.date <= target_date]
        if not before.empty:
            return round(float(before.iloc[-1]["Close"]), 2)
        return None
    except Exception as e:
        print(f"[learn] Error fetching price for {ticker} @ {target_date}: {e}", file=sys.stderr)
        return None


def parse_price(text: str) -> float | None:
    """Extrait un prix d'une chaîne comme '$84.89' ou '~$237' ou '61.20'."""
    m = re.search(r"[\$~]?\s*([0-9]+\.?[0-9]*)", text.replace(",", ""))
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


# ---------------------------------------------------------------------------
# Verdict logic
# ---------------------------------------------------------------------------


def verdict_opportunity(return_pct: float) -> tuple[str, float]:
    """Retourne (verdict, return_pct arrondi)."""
    ret = round(return_pct, 2)
    if ret >= HIT_THRESHOLD:
        return ("✅ Hit", ret)
    if ret <= MISS_THRESHOLD:
        return ("❌ Miss", ret)
    return ("⚪ Scratch", ret)


def verdict_price_target(price_target: float, reco: str, price_window: float) -> str:
    """
    Verdict spécifique aux prix cibles.
    Simplifié : comparaison directionnelle + amplitude.
    """
    reco_up = any(w in reco.lower() for w in ["achat", "buy", "overweight", "accumuler", "conserver"])
    reco_down = any(w in reco.lower() for w in ["vente", "sell", "underweight", "réduire"])
    delta = price_window - price_target
    delta_pct = delta / price_target if price_target != 0 else 0

    if reco_up and delta_pct >= 0.10:
        return "✅ Hit"
    if reco_up and delta_pct >= 0:
        return "⚠️ Partiel"
    if reco_down and delta_pct <= -0.10:
        return "✅ Hit"
    if reco_down and delta_pct <= 0:
        return "⚠️ Partiel"
    if abs(delta_pct) <= 0.05:
        return "⚪ Scratch"
    return "❌ Miss"


# ---------------------------------------------------------------------------
# Post-mortem generation
# ---------------------------------------------------------------------------


def generate_post_mortem(ticker: str, signal_date: str, score: str,
                         signal_type: str, entry_price: float, horizon: str,
                         exit_price: float, return_pct: float,
                         verdict: str) -> dict:
    """
    Génère un post-mortem structuré et une règle extraite.
    """
    pm = {
        "ticker": ticker,
        "date_signal": signal_date,
        "date_post_mortem": today.isoformat(),
        "score": score,
        "type": signal_type,
        "horizon": horizon,
        "entry_price": entry_price,
        "exit_price": exit_price,
        "return_pct": return_pct,
        "verdict": verdict,
        "rule_extracted": None,
        "confidence": "faible",
    }

    # Heuristique simple d'extraction de règle
    # À enrichir au fil du temps avec des patterns réels
    if "stagflation" in signal_type.lower() or "macro" in signal_type.lower():
        pm["rule_extracted"] = (
            "Si régime Stagflation confirmé → pénaliser Score Catalyseur de −0.5 pt "
            "sur tous les tickers cycliques, quelle que soit la qualité du catalyseur annoncé."
        )
        pm["confidence"] = "moyenne"
    elif "earnings" in signal_type.lower():
        pm["rule_extracted"] = (
            "Si le signal est basé sur un earnings beat mais que le RSI > 65 au moment du signal "
            "→ pénaliser Momentum de −0.5 pt (réaction déjà priced-in)."
        )
        pm["confidence"] = "moyenne"
    elif return_pct < -0.15:
        pm["rule_extracted"] = (
            "Si le cours chute > 15% dans les 20 jours post-signal → vérifier si un événement "
            "macro majeur (guerre, régulation, guidance cut) a été ignoré dans l'analyse initiale. "
            "Appliquer malus −1 pt Score Catalyseur si événement macro non modélisé."
        )
        pm["confidence"] = "moyenne"
    else:
        pm["rule_extracted"] = (
            "Post-mortem générique : relire l'analyse originale pour identifier la cause racine "
            "(Macro / Valorisation / Timing / Qualité bénéfices) et formuler une règle corrective."
        )
        pm["confidence"] = "faible"

    return pm


def save_post_mortem(pm: dict) -> None:
    """Écrit le post-mortem dans un fichier daté."""
    POST_MORTEMS_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{pm['ticker']}_{pm['date_signal']}_{pm['horizon']}_post_mortem.json"
    path = POST_MORTEMS_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(pm, f, indent=2, ensure_ascii=False, default=str)
    print(f"[learn] Post-mortem written → {path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# APPRENTISSAGES.md updater
# ---------------------------------------------------------------------------


def append_rule_to_apprentissages(rule_text: str, source: str, confidence: str) -> None:
    """
    Ajoute une règle dans APPRENTISSAGES.md (section Règles actives).
    Évite les doublons exacts.
    """
    if not APPRENTISSAGES_PATH.exists():
        print("[learn] APPRENTISSAGES.md not found, skipping rule append.", file=sys.stderr)
        return

    text = APPRENTISSAGES_PATH.read_text(encoding="utf-8")
    if rule_text in text:
        print("[learn] Rule already present in APPRENTISSAGES.md, skipping.", file=sys.stderr)
        return

    # Insert after "## Règles actives issues des erreurs"
    marker = "## Règles actives issues des erreurs"
    if marker not in text:
        print("[learn] Marker not found in APPRENTISSAGES.md, skipping.", file=sys.stderr)
        return

    rule_block = (
        f"\n### Règle auto — {today.isoformat()}\n"
        f"- **Règle :** {rule_text}\n"
        f"- **Source :** {source}\n"
        f"- **Confiance :** {confidence}\n"
        f"- **Commentaire :** Extrait automatiquement par `learn_from_errors.py`. "
        f"À réévaluer après 3 mois ou 10 signaux supplémentaires.\n"
    )

    idx = text.index(marker) + len(marker)
    new_text = text[:idx] + rule_block + text[idx:]
    APPRENTISSAGES_PATH.write_text(new_text, encoding="utf-8")
    print(f"[learn] Rule appended to APPRENTISSAGES.md", file=sys.stderr)


# ---------------------------------------------------------------------------
# BACKTESTING updater
# ---------------------------------------------------------------------------


def process_backtesting() -> dict:
    """
    Vérifie les fenêtres BACKTESTING, récupère les prix, calcule les verdicts.
    Retourne un rapport d'activité.
    """
    stats = {"checked": 0, "hits": 0, "misses": 0, "scratches": 0, "post_mortems": 0}

    if not BACKTESTING_PATH.exists():
        print("[learn] BACKTESTING.md not found, skipping.", file=sys.stderr)
        return stats

    text = BACKTESTING_PATH.read_text(encoding="utf-8")
    rows = parse_markdown_table(text, ["Date signal", "Ticker", "Cours signal", "J+5"])
    if not rows:
        print("[learn] No backtesting table found.", file=sys.stderr)
        return stats

    updated_rows = []
    any_change = False

    for row in rows:
        ticker = row.get("Ticker", "").strip()
        signal_date_str = row.get("Date signal", "").strip()
        entry_price = parse_price(row.get("Cours signal", ""))
        score = row.get("Score", "").strip()
        signal_type = row.get("Type signal", "").strip()

        if not ticker or not signal_date_str or entry_price is None:
            updated_rows.append(row)
            continue

        try:
            signal_date = datetime.strptime(signal_date_str, "%Y-%m-%d").date()
        except ValueError:
            updated_rows.append(row)
            continue

        # Vérifier chaque horizon
        new_row = dict(row)
        for col_horizon, delta in HORIZONS_BT.items():
            if col_horizon not in new_row:
                continue
            cell = new_row[col_horizon].strip()
            # Si déjà calculé (pas ⏳), ne pas toucher
            if not cell.startswith("⏳"):
                continue

            target_date = signal_date + timedelta(days=delta)
            # Tolérance ±2 jours
            if target_date > today + timedelta(days=2):
                continue  # trop tôt

            # Récupérer le prix au target_date
            exit_price = get_close_on_date(ticker, target_date)
            if exit_price is None:
                # Si c'est aujourd'hui et le marché est ouvert, on peut utiliser latest.json
                if target_date == today:
                    exit_price = get_latest_json_price(ticker)
                if exit_price is None:
                    continue  # données indisponibles, skip

            ret = (exit_price - entry_price) / entry_price
            verdict, ret_rounded = verdict_opportunity(ret)
            new_row[col_horizon] = f"{verdict} ({ret_rounded:+.1%})"
            stats["checked"] += 1
            if "✅ Hit" in verdict:
                stats["hits"] += 1
            elif "❌ Miss" in verdict:
                stats["misses"] += 1
                # Post-mortem sur J+20 et J+60 uniquement
                if col_horizon in ("J+20", "J+60"):
                    pm = generate_post_mortem(
                        ticker, signal_date_str, score, signal_type,
                        entry_price, col_horizon, exit_price, ret, verdict
                    )
                    save_post_mortem(pm)
                    append_rule_to_apprentissages(
                        pm["rule_extracted"],
                        f"Post-mortem {ticker} {signal_date_str} {col_horizon}",
                        pm["confidence"]
                    )
                    new_row["Post-mortem"] = f"[Post-mortem {today}]"
                    stats["post_mortems"] += 1
            else:
                stats["scratches"] += 1
            any_change = True

        updated_rows.append(new_row)

    if any_change:
        new_text = replace_table_rows(text, ["Date signal", "Ticker", "Cours signal", "J+5"], updated_rows)
        BACKTESTING_PATH.write_text(new_text, encoding="utf-8")
        print(f"[learn] BACKTESTING.md updated.", file=sys.stderr)

    return stats


# ---------------------------------------------------------------------------
# SUIVI_PRIX_CIBLES updater
# ---------------------------------------------------------------------------


def process_suivi_prix() -> dict:
    """
    Vérifie les fenêtres SUIVI_PRIX_CIBLES, calcule les verdicts.
    """
    stats = {"checked": 0, "hits": 0, "partiels": 0, "misses": 0}

    if not SUIVI_PRIX_PATH.exists():
        print("[learn] SUIVI_PRIX_CIBLES.md not found, skipping.", file=sys.stderr)
        return stats

    text = SUIVI_PRIX_PATH.read_text(encoding="utf-8")
    rows = parse_markdown_table(text, ["Date analyse", "Ticker", "Prix cible", "J+30"])
    if not rows:
        print("[learn] No price target table found.", file=sys.stderr)
        return stats

    updated_rows = []
    any_change = False

    for row in rows:
        ticker = row.get("Ticker", "").strip()
        date_str = row.get("Date analyse", "").strip()
        price_target = parse_price(row.get("Prix cible", ""))
        reco = row.get("Reco", "").strip()
        entry_price = parse_price(row.get("Cours à l'analyse", ""))

        if not ticker or not date_str or price_target is None:
            updated_rows.append(row)
            continue

        try:
            analysis_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            updated_rows.append(row)
            continue

        new_row = dict(row)
        for col_horizon, delta in HORIZONS_PC.items():
            if col_horizon not in new_row:
                continue
            cell = new_row[col_horizon].strip()
            if not cell.startswith("⏳") and not cell.startswith("202"):
                # Déjà un verdict, skip
                continue

            target_date = analysis_date + timedelta(days=delta)
            if target_date > today + timedelta(days=2):
                continue

            # Récupérer prix au target_date
            window_price = get_close_on_date(ticker, target_date)
            if window_price is None:
                if target_date == today:
                    window_price = get_latest_json_price(ticker)
                if window_price is None:
                    continue

            verdict = verdict_price_target(price_target, reco, window_price)
            new_row[col_horizon] = verdict
            new_row["Verdict final"] = verdict
            stats["checked"] += 1
            if verdict == "✅ Hit":
                stats["hits"] += 1
            elif verdict == "⚠️ Partiel":
                stats["partiels"] += 1
            elif verdict == "❌ Miss":
                stats["misses"] += 1
                # Post-mortem prix cible
                pm = generate_post_mortem(
                    ticker, date_str, "—", "Prix cible", entry_price or price_target,
                    col_horizon, window_price,
                    (window_price - (entry_price or price_target)) / (entry_price or price_target),
                    verdict
                )
                pm["rule_extracted"] = (
                    "Si prix cible rate avec une erreur > 20% → revérifier le Filtre Qualité "
                    "et les hypothèses de DCF avant prochaine émission de PT sur ce ticker."
                )
                save_post_mortem(pm)
                append_rule_to_apprentissages(
                    pm["rule_extracted"],
                    f"Post-mortem prix cible {ticker} {date_str}",
                    "moyenne"
                )
            any_change = True

        updated_rows.append(new_row)

    if any_change:
        new_text = replace_table_rows(text, ["Date analyse", "Ticker", "Prix cible", "J+30"], updated_rows)
        SUIVI_PRIX_PATH.write_text(new_text, encoding="utf-8")
        print(f"[learn] SUIVI_PRIX_CIBLES.md updated.", file=sys.stderr)

    return stats


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------


def get_latest_json_price(ticker: str) -> float | None:
    """Fallback : lit data/latest.json pour le cours du jour."""
    latest = BASE_DIR / "data" / "latest.json"
    if not latest.exists():
        return None
    try:
        data = json.loads(latest.read_text(encoding="utf-8"))
        block = data.get("prices", {}).get(ticker, {})
        return block.get("price", {}).get("close")
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print(f"[learn] Starting learning loop — {today.isoformat()}", file=sys.stderr)

    bt_stats = process_backtesting()
    pc_stats = process_suivi_prix()

    total_checked = bt_stats["checked"] + pc_stats["checked"]
    total_hits = bt_stats["hits"] + pc_stats["hits"]
    total_misses = bt_stats["misses"] + pc_stats["misses"]

    print(
        f"[learn] Done — {total_checked} windows checked | "
        f"{total_hits} hits | {total_misses} misses | "
        f"{bt_stats['post_mortems']} post-mortems generated",
        file=sys.stderr
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

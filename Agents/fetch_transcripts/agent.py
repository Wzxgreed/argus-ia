#!/usr/bin/env python3
"""
fetch_transcripts.py — NLP Transcript Analysis via FMP.

Récupère les transcripts des earnings calls via FMP, analyse le ton du management
sur 3 axes : confiance vs prudence, évasions Q&A, pivots ambigus.

Usage:
    python agents/fetch_transcripts/agent.py

Output:
    data/transcripts_NLP_YYYY-MM-DD.json
"""

import sys
from pathlib import Path
_scripts = Path(__file__).resolve().parent.parent / 'scripts'
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from fmp_client import FMPClient

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"

# ---------------------------------------------------------------------------
# NLP Keywords & Patterns
# ---------------------------------------------------------------------------

CONFIDENCE_KEYWORDS = [
    "confident", "strong momentum", "solid execution", "exceeded expectations",
    "robust demand", "clear path", "well positioned", "accelerating",
    "record", "all-time high", "strong pipeline", "excellent", "outperform",
    "surpassed", "gaining share", "expanding margins", "healthy",
    "we are confident", "very pleased", "exceptional", "remarkable",
    "outstanding", "extraordinary", "unprecedented", "transformational",
    "dominant", "leadership position", "best-in-class", "industry leading",
    "significant tailwinds", "strong visibility", "high conviction",
    "on track", "ahead of plan", "exceeded our targets", "sustainable growth",
    "reinforce", "strengthen", "deepen", "broaden", "expand", "scale",
    "optimistic", "bullish", "favorable", "encouraging", "positive",
    "forte croissance", "solide", "robuste", "excellente visibilité",
    "confiance", "satisfaction", "dépasser", "accélération", "leadership",
]

PRUDENCE_KEYWORDS = [
    "cautious", "headwinds", "challenging", "uncertain", "macro pressure",
    "monitoring closely", "softness", "deceleration", "mixed",
    "cost pressure", "margin compression", "pricing pressure", "supply chain",
    "normalizing", "cycling tough comps", "temper expectations",
    "early days", "too soon to tell", "remains to be seen", "bumpy",
    "not immune", "we are mindful", "we are watching", "notable caution",
    "geopolitical", "inflationary", "we remain cautious", "measured approach",
    "prudent", "disciplined", "manageable", "modest", "moderate",
    "volatile", "unpredictable", "fragile", "under pressure",
    "prudent", "mesuré", "précaution", "pression", "incertitude",
    "ralentissement", "normalisation", "tête de série difficile",
    "nous surveillons", "nous restons prudents", "contexte difficile",
]

AMBIGUITY_PIVOTS = [
    "restructuring", "rightsizing", "optimizing", "streamlining",
    "pivot", "strategic review", "exploring options", "evaluating alternatives",
    "transition period", "investment phase", "build-out", "ramp-up",
    "not material", "immaterial", "limited impact", "early innings",
    "longer term", "multi-year journey", "we are in the process of",
    "sequentially", "run-rate", "annualized", "exit rate", "normalized",
    "adjusted", "pro forma", "non-gaap", "excluding", "one-time",
    "realigning", "refocusing", "consolidating", "integrating",
    "strategic alternatives", "under review", "being assessed",
    "restructuration", "réorganisation", "optimisation", "période de transition",
    "phase d'investissement", "pas significatif", "impact limité",
    "début de parcours", "à long terme", "en cours de processus",
]

EVASION_PATTERNS = [
    r"(?:we\s+(?:won't|will not|cannot|can't)\s+(?:comment|discuss|speculate|disclose|provide|share|get into|go into|address|elaborate))",
    r"(?:i\s+(?:won't|will not|cannot|can't)\s+(?:comment|discuss|speculate|disclose|provide|share|get into|go into|address|elaborate))",
    r"(?:not\s+(?:something\s+we\s+(?:can|will)|(?:in\s+a\s+position\s+to)))\s+(?:comment|discuss|speculate|disclose|provide|share)",
    r"(?:we\s+(?:prefer|would\s+prefer)\s+(?:not\s+to|to\s+avoid))\s+(?:comment|discuss|speculate|disclose|provide|share)",
    r"(?:i\s+(?:don't|do\s+not)\s+(?:have|know|have\s+the)\s+(?:specifics|details|numbers|data|information|visibility))",
    r"(?:we\s+(?:don't|do\s+not)\s+(?:have|know|have\s+the)\s+(?:specifics|details|numbers|data|information|visibility))",
    r"(?:we\s+(?:will|are\s+going\s+to)\s+(?:update\s+you|get\s+back\s+to\s+you|share\s+more|provide\s+more\s+details)\s+(?:in\s+the\s+future|at\s+a\s+later\s+date|as\s+we\s+progress|when\s+appropriate))",
    r"(?:that\s+is|that's)\s+(?:not\s+(?:the\s+focus|what\s+we\s+are\s+focusing\s+on|something\s+we\s+track|a\s+priority|relevant)\s+(?:today|here|now|at\s+this\s+time))",
    r"(?:i\s+(?:think|believe)\s+(?:it\s+is|it's)\s+(?:premature|too\s+early)\s+(?:to|for\s+us\s+to))",
]


def count_keywords(text: str, keywords: list) -> int:
    """Compte les occurrences de mots-clés (case-insensitive, whole word)."""
    text_lower = text.lower()
    count = 0
    for kw in keywords:
        pattern = re.compile(r'\b' + re.escape(kw.lower()) + r'\b')
        count += len(pattern.findall(text_lower))
    return count


def count_evasions(text: str) -> int:
    """Compte les patterns d'évasions Q&A dans le texte."""
    count = 0
    for pattern in EVASION_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        count += len(matches)
    return count


def extract_guidance_statements(text: str) -> list:
    """Extrait les phrases contenant des mots de guidance."""
    guidance_words = [
        "guidance", "outlook", "forecast", "expect", "project",
        "anticipate", "target", "plan", "objective", "goal",
        "visibility", "trajectory", "momentum", "trend",
    ]
    sentences = re.split(r'(?<=[.!?])\s+', text)
    guidance_sentences = []
    for sent in sentences:
        if any(w in sent.lower() for w in guidance_words):
            guidance_sentences.append(sent.strip())
    return guidance_sentences


def classify_guidance_firmness(guidance_sentences: list) -> dict:
    """
    Classe la fermeté de la guidance : ferme / prudente / vague.
    Retourne un dict avec count par catégorie.
    """
    firm_indicators = [
        "expect", "project", "target", "guidance is", "we are confident",
        "we anticipate", "we forecast", "range of", "between",
        "we reiterate", "maintaining our", "raising our", "increasing our",
    ]
    vague_indicators = [
        "difficult to predict", "uncertain", "subject to", "depending on",
        "could be", "may be", "might", "potentially", "if conditions allow",
        "we'll see", "too early", "not ready to", "we are evaluating",
        "we are assessing", "monitoring", "early to tell", "not in a position",
    ]

    firm_count = 0
    vague_count = 0
    for sent in guidance_sentences:
        sent_lower = sent.lower()
        if any(w in sent_lower for w in firm_indicators):
            firm_count += 1
        if any(w in sent_lower for w in vague_indicators):
            vague_count += 1

    return {
        "firm": firm_count,
        "vague": vague_count,
        "total": len(guidance_sentences),
        "firmness_score": round(firm_count / max(len(guidance_sentences), 1) * 10, 2),
    }


def analyze_transcript(transcript_text: str) -> dict:
    """
    Analyse un transcript complet et retourne les métriques NLP.
    """
    text = transcript_text or ""

    # Séparation Prepared Remarks vs Q&A
    qa_split = text.lower().split("question-and-answer")
    if len(qa_split) == 1:
        qa_split = text.lower().split("q & a")
    if len(qa_split) == 1:
        qa_split = text.lower().split("questions and answers")

    prepared_remarks = qa_split[0] if qa_split else text
    qa_section = qa_split[1] if len(qa_split) > 1 else ""

    # --- Comptages ---
    conf_count = count_keywords(text, CONFIDENCE_KEYWORDS)
    prud_count = count_keywords(text, PRUDENCE_KEYWORDS)
    pivot_count = count_keywords(text, AMBIGUITY_PIVOTS)
    evasion_count = count_evasions(text)

    # --- Ratios ---
    total_words = len(text.split())
    ratio_conf_prud = round(conf_count / max(prud_count, 1), 2)
    confidence_density = round(conf_count / max(total_words, 1) * 1000, 3)
    prudence_density = round(prud_count / max(total_words, 1) * 1000, 3)

    # --- Guidance ---
    guidance_sents = extract_guidance_statements(text)
    guidance_firmness = classify_guidance_firmness(guidance_sents)

    # --- Évasions par section ---
    evasion_prepared = count_evasions(prepared_remarks)
    evasion_qa = count_evasions(qa_section)

    return {
        "total_words": total_words,
        "confidence_count": conf_count,
        "prudence_count": prud_count,
        "confidence_prudence_ratio": ratio_conf_prud,
        "confidence_density": confidence_density,
        "prudence_density": prudence_density,
        "pivots_ambiguous": pivot_count,
        "evasions_total": evasion_count,
        "evasions_prepared": evasion_prepared,
        "evasions_qa": evasion_qa,
        "guidance_sentences_count": len(guidance_sents),
        "guidance_firmness": guidance_firmness,
        "sample_guidance": guidance_sents[:3],
    }


def compute_confidence_score(current: dict, previous: dict = None) -> dict:
    """
    Calcule le Score Confiance Management /10 et son évolution vs trimestre précédent.
    """
    score = 5.0  # base neutre

    # Ratio confiance/prudence
    ratio = current.get("confidence_prudence_ratio", 1.0)
    if ratio > 2.5:
        score += 1.5
    elif ratio > 1.5:
        score += 0.5
    elif ratio < 0.7:
        score -= 1.5
    elif ratio < 1.0:
        score -= 0.5

    # Évasions (pénalité si > 5)
    evasions = current.get("evasions_total", 0)
    if evasions > 8:
        score -= 1.5
    elif evasions > 5:
        score -= 0.5
    elif evasions <= 2:
        score += 0.5

    # Pivots ambigus (pénalité si > 3)
    pivots = current.get("pivots_ambiguous", 0)
    if pivots > 5:
        score -= 1.0
    elif pivots > 3:
        score -= 0.5

    # Fermeté guidance
    firmness = current.get("guidance_firmness", {})
    firm_pct = firmness.get("firmness_score", 5)
    if firm_pct >= 7:
        score += 0.5
    elif firm_pct <= 3:
        score -= 0.5

    # Score final borné [0, 10]
    score = max(0, min(10, round(score, 1)))

    # Évolution vs précédent
    evolution = None
    if previous:
        prev_score = previous.get("confidence_score", 5.0)
        evolution = round(score - prev_score, 1)

    return {
        "score": score,
        "previous_score": previous.get("confidence_score") if previous else None,
        "evolution": evolution,
        "interpretation": (
            "Confiant / Fermeté solide" if score >= 7.5 else
            "Neutre / Prudence modérée" if score >= 5 else
            "Hésitant / Évasions nombreuses" if score >= 3 else
            "Dégradé / Signaux de faiblesse"
        ),
    }


def fetch_and_analyze_ticker(fmp: FMPClient, ticker: str) -> dict:
    """
    Récupère les transcripts des 3 derniers trimestres via FMP et analyse chacun.
    """
    # FMP : le transcript le plus récent (quarter 1, year 2026 par défaut)
    # On essaie Q1 2026, puis Q4 2025, Q3 2025, Q2 2025
    quarters_to_try = [
        {"year": 2026, "quarter": 1, "label": "Q1 FY27"},
        {"year": 2025, "quarter": 4, "label": "Q4 FY26"},
        {"year": 2025, "quarter": 3, "label": "Q3 FY26"},
        {"year": 2025, "quarter": 2, "label": "Q2 FY26"},
    ]

    transcripts_analyzed = []
    latest_analysis = None
    previous_analysis = None

    for q in quarters_to_try:
        try:
            data = fmp.get_earning_call_transcript(ticker, year=q["year"], quarter=q["quarter"])
            if isinstance(data, dict) and data.get("error"):
                reason = data.get("reason", "")
                if "402" in reason or "Restricted" in reason:
                    print(f"[fetch_transcripts] ⚠️  Plan FMP insuffisant pour transcripts (402). Skipping {ticker}.", file=sys.stderr)
                    return {
                        "ticker": ticker,
                        "transcripts_count": 0,
                        "latest_quarter": None,
                        "latest_date": None,
                        "latest_analysis": None,
                        "previous_analysis": None,
                        "all_quarters": [],
                        "note": "FMP plan insuffisant — transcripts require Enterprise+ subscription.",
                    }
                continue
            if isinstance(data, list) and len(data) > 0:
                transcript_item = data[0]
            elif isinstance(data, dict):
                transcript_item = data
            else:
                continue

            content = transcript_item.get("content", "")
            if not content or len(content) < 100:
                continue

            analysis = analyze_transcript(content)
            analysis["quarter"] = q["label"]
            analysis["year"] = q["year"]
            analysis["quarter_num"] = q["quarter"]
            analysis["date"] = transcript_item.get("date")
            analysis["symbol"] = transcript_item.get("symbol", ticker)

            # Stocker pour comparaison inter-trimestrielle plus tard
            transcripts_analyzed.append(analysis)

        except Exception as e:
            print(f"[fetch_transcripts] Error fetching {ticker} {q['label']}: {e}", file=sys.stderr)
            continue

    # Calcul des scores avec comparaison inter-trimestrielle
    if len(transcripts_analyzed) >= 1:
        # Latest = premier de la liste (le plus récent)
        latest = transcripts_analyzed[0]
        previous = transcripts_analyzed[1] if len(transcripts_analyzed) > 1 else None
        score_info = compute_confidence_score(latest, previous)
        latest["confidence_score"] = score_info["score"]
        latest["confidence_score_interpretation"] = score_info["interpretation"]
        latest["confidence_score_evolution"] = score_info.get("evolution")

    return {
        "ticker": ticker,
        "transcripts_count": len(transcripts_analyzed),
        "latest_quarter": transcripts_analyzed[0]["quarter"] if transcripts_analyzed else None,
        "latest_date": transcripts_analyzed[0]["date"] if transcripts_analyzed else None,
        "latest_analysis": transcripts_analyzed[0] if transcripts_analyzed else None,
        "previous_analysis": transcripts_analyzed[1] if len(transcripts_analyzed) > 1 else None,
        "all_quarters": [{"quarter": t["quarter"], "date": t.get("date"), "confidence_score": t.get("confidence_score")} for t in transcripts_analyzed],
    }


def main():
    fmp = FMPClient()
    if not fmp.api_key:
        print("[fetch_transcripts] FMP_API_KEY not found. Transcript analysis skipped.", file=sys.stderr)
        return 0

    config = load_config()
    tickers = [t["ticker"] for t in config["tickers"]]

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_path = DATA_DIR / f"transcripts_NLP_{date_str}.json"

    results = {
        "meta": {
            "date": date_str,
            "source": "fmp",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "tickers_requested": tickers,
            "tickers_with_transcripts": 0,
        },
        "nlp": {},
    }

    for t in tickers:
        print(f"[fetch_transcripts] Analyzing {t}...", file=sys.stderr)
        data = fetch_and_analyze_ticker(fmp, t)
        results["nlp"][t] = data
        if data.get("transcripts_count", 0) > 0:
            results["meta"]["tickers_with_transcripts"] += 1

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "transcripts_NLP_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(f"[fetch_transcripts] Written {output_path} ({results['meta']['tickers_with_transcripts']} tickers with transcripts)", file=sys.stderr)
    return 0


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    sys.exit(main())

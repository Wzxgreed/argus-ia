# 🔭 Événements à venir — Watchlist Argus-IA

> **Date :** 2026-06-28
> **Tickers scannés :** 29
> **Événements détectés :** 29

---

## 🔴 ≤ 3 jours — Action immédiate requise

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| SQ | earnings | 2026-06-29 | 1j | Earnings ... | fmp |
| TEST | earnings | 2026-06-29 | 1j | Earnings ... | fmp |
| AST | earnings | 2026-06-29 | 1j | Earnings ... | fmp |
| AXA | earnings | 2026-06-29 | 1j | Earnings ... | fmp |
| SPCX | earnings | 2026-06-29 | 1j | Earnings ... | fmp |
| QTBS | earnings | 2026-06-29 | 1j | Earnings ... | fmp |
| ASTSPACE | earnings | 2026-06-29 | 1j | Earnings ... | fmp |

---

## 🟡 ≤ 7 jours — Surveillance renforcée

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| — | — | — | — | — | — |

---

## 🟢 ≤ 30 jours — Radar

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| NOK | earnings | 2026-07-23 | 25j | Earnings date — Est EPS $0.06-$0.08, Rev $4.8B... | yfinance |
| SOFI | earnings | 2026-07-28 | 30j | Earnings date — Est EPS $0.10-$0.11, Rev $1.1B... | yfinance |
| AAL | earnings | 2026-07-23 | 25j | Earnings date — Est EPS $-0.34-$0.19, Rev $16.7B... | yfinance |

---

## ❓ Sans date précise — Détectés dans les news

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| — | — | — | — | — | — |

---

## Workflow

1. **Chaque matin** : lire cette page. Si un événement passe de 🟢 → 🟡 ou 🟡 → 🔴, préparer l'analyse.
2. **🔴 ≤ 3j** : `agent_watchman.py` génère automatiquement un `_preview.md` si c'est un earnings ou un catalyseur structurant.
3. **Post-événement** : lire `data/latest.json` + `data/transcripts_NLP_latest.json` puis générer `_earnings.md` ou `_update.md`.
4. **Nouveau CEO / Insider major / Analyste** : `agent_watchman.py` génère automatiquement un `_update.md` flash.

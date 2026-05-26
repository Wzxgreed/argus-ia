# 🔭 Événements à venir — Watchlist Argus-IA

> **Date :** 2026-05-26
> **Tickers scannés :** 26
> **Événements détectés :** 26

---

## 🔴 ≤ 3 jours — Action immédiate requise

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| IREN | earnings | 2026-05-26 | 0j | Earnings ... | fmp |
| SQ | earnings | 2026-05-26 | 0j | Earnings ... | fmp |
| TEST | earnings | 2026-05-26 | 0j | Earnings ... | fmp |
| FUBO | earnings | 2026-05-26 | 0j | Earnings ... | fmp |
| A | earnings | 2026-05-27 | 1j | Earnings date — Est EPS $1.39-$1.42, Rev $1.8B... | yfinance |
| AST | earnings | 2026-05-26 | 0j | Earnings ... | fmp |
| AXA | earnings | 2026-05-26 | 0j | Earnings ... | fmp |
| SPCX | earnings | 2026-05-26 | 0j | Earnings ... | fmp |
| QTBS | earnings | 2026-05-26 | 0j | Earnings ... | fmp |

---

## 🟡 ≤ 7 jours — Surveillance renforcée

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| — | — | — | — | — | — |

---

## 🟢 ≤ 30 jours — Radar

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| MU | earnings | 2026-06-24 | 29j | Earnings date — Est EPS $7.53-$23.00, Rev $33.6B... | yfinance |

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

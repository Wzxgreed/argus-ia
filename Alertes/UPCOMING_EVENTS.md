# 🔭 Événements à venir — Watchlist Argus-IA

> **Date :** 2026-05-17
> **Tickers scannés :** 6
> **Événements détectés :** 6

---

## 🔴 ≤ 3 jours — Action immédiate requise

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| IREN | earnings | 2026-05-17 | 0j | Earnings ... | fmp |
| NVDA | earnings | 2026-05-20 | 3j | Earnings date — Est EPS $1.69-$1.99, Rev $79.2B... | yfinance |

---

## 🟡 ≤ 7 jours — Surveillance renforcée

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| — | — | — | — | — | — |

---

## 🟢 ≤ 30 jours — Radar

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| — | — | — | — | — | — |

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

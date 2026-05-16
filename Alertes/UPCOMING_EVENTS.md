# 🔭 Événements à venir — Watchlist Argus-IA

> **Date :** 2026-05-16
> **Tickers scannés :** 6
> **Événements détectés :** 15

---

## 🔴 ≤ 3 jours — Action immédiate requise

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| IREN | earnings | 2026-05-17 | 1j | Earnings ... | fmp |

---

## 🟡 ≤ 7 jours — Surveillance renforcée

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| NVDA | earnings | 2026-05-20 | 4j | Earnings date — Est EPS $1.69-$1.99, Rev $79.2B... | yfinance |

---

## 🟢 ≤ 30 jours — Radar

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| — | — | — | — | — | — |

---

## ❓ Sans date précise — Détectés dans les news

| Ticker | Type | Date | Jours | Détail | Source |
|--------|------|------|-------|--------|--------|
| IREN | news_expansion | None | ? | News: IREN Raises $3 Billion To Fund A.I. Cloud Expansion... | yfinance_news |
| RTX | news_upcoming | None | ? | News: Nvidia Chips, Boeing Jets: Stock Traders Eye Trump in ... | yfinance_news |
| VRT | news_earnings_call | None | ? | News: Tecogen Q1 Earnings Call Highlights [event: q1 2026]... | yfinance_news |
| VRT | news_13f | None | ? | News: Leon Cooperman's Strategic Moves: Regal Rexnord Corp E... | yfinance_news |
| VRT | news_new_stake | None | ? | News: Institutional investors flocked to establish new stake... | yfinance_news |
| VRT | news_expansion | None | ? | News: VRT vs. APH: Which AI Infrastructure Stock Is the Smar... | yfinance_news |
| NVDA | news_to_report | None | ? | News: Nvidia to report Q1 earnings as chip competition grows... | yfinance_news |
| NVDA | news_bearish | None | ? | News: Forget Utility Dividends. Kevin Warsh Just Made the 30... | yfinance_news |
| AAPL | news_new_ceo | None | ? | News: Berkshire Hathaway triples Alphabet stake and invests ... | yfinance_news |

---

## Workflow

1. **Chaque matin** : lire cette page. Si un événement passe de 🟢 → 🟡 ou 🟡 → 🔴, préparer l'analyse.
2. **🔴 ≤ 3j** : `agent_watchman.py` génère automatiquement un `_preview.md` si c'est un earnings ou un catalyseur structurant.
3. **Post-événement** : lire `data/latest.json` + `data/transcripts_NLP_latest.json` puis générer `_earnings.md` ou `_update.md`.
4. **Nouveau CEO / Insider major / Analyste** : `agent_watchman.py` génère automatiquement un `_update.md` flash.

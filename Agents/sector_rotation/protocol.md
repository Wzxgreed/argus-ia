# Agent Sector Rotation — Protocole de Surveillance Sectorielle

**Script associé :** `agents/sector_rotation/agent.py`
**Output :** `data/sector_rotation_YYYY-MM-DD.json`

---

## Mission

Surveiller la rotation sectorielle via les ETFs SPDR et aligner la watchlist avec le régime macro actif.

---

## Sources

| Ticker | Secteur |
|--------|---------|
| XLK | Technology |
| XLE | Energy |
| XLF | Financials |
| XLI | Industrials |
| XLU | Utilities |
| XLV | Health Care |
| XLP | Consumer Staples |
| XLY | Consumer Discretionary |
| XLB | Materials |
| XLRE | Real Estate |
| XLC | Communication Services |
| SPY | S&P 500 (benchmark) |

---

## Signaux Calculés

### 1. Force Relative (RS) vs SPY
```
RS_20j = rendement 20j du secteur / rendement 20j du SPY
RS_60j = rendement 60j du secteur / rendement 60j du SPY
```

### 2. Crossover RS
- **Bullish crossover** : RS 20j passe au-dessus de RS 60j → momentum sectoriel en accélération
- **Bearish crossover** : RS 20j passe en dessous de RS 60j → décélération

### 3. Momentum Score /10
Normalisé par percentile du RS 20j parmi les 11 secteurs.

### 4. Alignement Régime Macro
| Régime | Secteurs privilégiés | Secteurs à éviter |
|--------|---------------------|-------------------|
| Risk-on / Bull | XLK, XLY, XLC, XLI | XLU, XLP |
| Risk-off | XLU, XLP, XLV | XLY, XLB, XLE |
| Stagflation | XLE, XLB, XLU | XLK, XLY |
| Pré-FOMC | XLF, XLI, XLV | XLE, XLRE |
| Récession | XLU, XLP, XLV | XLY, XLI, XLRE |

---

## Seuils d'Alerte

- **Rotation majeure** : ≥3 secteurs changent de quartile de RS 20j en 1 semaine
- **Divergence macro** : top 3 secteurs en RS sont dans la liste "à éviter" du régime actif → WARNING
- **Momentum extrême** : RS 20j > 2.0 (secteur très sur-acheté relativement) ou < 0.5 (très sous-performant)

---

## Output JSON

```json
{
  "ranking": [
    {"sector": "XLK", "rs20": 1.35, "rs60": 1.12, "crossover": "bullish", "momentum_score": 8.5},
    {"sector": "XLE", "rs20": 0.78, "rs60": 1.05, "crossover": "bearish", "momentum_score": 3.2}
  ],
  "top3": ["XLK", "XLC", "XLI"],
  "bottom3": ["XLU", "XLRE", "XLP"],
  "macro_alignment": "risk-on",
  "divergence_alert": false
}
```

---

## Intégration Scoring

- Top 3 secteurs → privilégier les tickers de ces secteurs (+0.5 pt Opportunité)
- Bottom 3 secteurs → pénaliser les tickers de ces secteurs (−0.5 pt Opportunité)
- Crossover détecté sur le secteur d'un ticker → mentionner dans `_update.md`

---

*Protocole lu par l'agent LLM et implémenté dans `agents/sector_rotation/agent.py`.*

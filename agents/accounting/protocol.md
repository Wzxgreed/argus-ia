# Agent Accounting — Protocole de Détection Fraude & Qualité Comptable

**Script associé :** `agents/accounting/agent.py`
**Output :** `data/accounting_risk_YYYY-MM-DD.json`

---

## Mission

Détecter la manipulation comptable et évaluer la santé financière de chaque ticker via 4 métriques institutionnelles :

1. **Beneish M-Score** — probabilité de manipulation comptable
2. **Altman Z-Score** — probabilité de faillite (distress)
3. **Piotroski F-Score** — santé financière globale (0-9)
4. **Sloan Ratio** — qualité des bénéfices (accruals vs cash-flow)

---

## Seuils & Règles Absolues

| Métrique | Seuil 🔴 | Seuil 🟡 | Seuil 🟢 |
|----------|---------|---------|---------|
| **Beneish M-Score** | > -1.78 | -2.22 à -1.78 | < -2.22 |
| **Altman Z-Score** | < 1.81 | 1.81 – 2.99 | > 2.99 |
| **Piotroski F-Score** | ≤ 3 | 4 – 6 | ≥ 7 |
| **Sloan Ratio** | > 0.10 | 0.05 – 0.10 | < 0.05 |

**Règle absolue :** si M-Score > -1.78 **OU** Z-Score < 1.81 → **EXCLURE du long** / paper trading bloqué.

---

## Méthodologie

### Beneish M-Score
Formule composite à 8 variables (DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA).  
Seuil historique de détection : **-1.78** (Enron avait ~-1.5).  
Sources : `income-statement`, `balance-sheet-statement`, `cash-flow-statement` (FMP).

### Altman Z-Score
Formule à 5 ratios (working capital, retained earnings, EBIT, market cap, sales).  
Seuils : < 1.81 = distress probable, 1.81-2.99 = grey zone, > 2.99 = safe.

### Piotroski F-Score
9 critères binaires regroupés en 3 catégories :
- Rentabilité (4 critères : ROA > 0, CFO > 0, ROA croissant, CFO > NI)
- Levier/Liquidité (3 critères : leverage ↓, current ratio ↑, pas d'émission actions)
- Efficacité (2 critères : gross margin ↑, asset turnover ↑)

### Sloan Ratio
`(Net Income − CFO) / Total Assets`  
Accruals élevés = bénéfices de faible qualité (cash non collecté).

---

## Output JSON

```json
{
  "AAPL": {
    "m_score": -2.45,
    "z_score": 4.12,
    "f_score": 7,
    "sloan_ratio": 0.03,
    "risk_level": "🟢 Faible",
    "excluded": false,
    "warnings": []
  }
}
```

---

## Intégration Scoring

- M-Score > -1.78 ou Z-Score < 1.81 → **malus −25** sur Score Global Composite
- F-Score ≤ 3 → plafonner Score Valorisation à 5/10
- Sloan Ratio > 0.10 → qualifier la qualité des bénéfices comme "faible" dans l'analyse

---

*Protocole lu par l'agent LLM et implémenté dans `agents/accounting/agent.py`.*

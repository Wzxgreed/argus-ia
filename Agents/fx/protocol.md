# Agent FX Exposure — Protocole d'Exposition aux Devises

**Script associé :** `agents/fx/agent.py`
**Output :** `data/fx_exposure_YYYY-MM-DD.json`

---

## Mission

Mesurer l'exposition de chaque ticker aux fluctuations de change (USD, EUR, JPY, CNY) et chiffrer l'impact estimé sur les revenus, les marges et la valorisation.

---

## Sources

- `data/latest.json` → macro/forex (DXY, EUR/USD, USD/JPY, USD/CNY)
- `config/watchlist.json` → secteurs (proxy d'exposition si données FMP absentes)
- `fmp_key_metrics` → revenus géographiques (si disponible)

---

## Exposition par Secteur (Proxy si FMP absent)

| Secteur | Exposition USD | Exposition EUR | Exposition CNY | Exposition JPY |
|---------|---------------|----------------|----------------|----------------|
| Technology | Élevée | Modérée | Élevée | Modérée |
| Energy | Élevée | Modérée | Élevée | Faible |
| Materials | Élevée | Modérée | Très élevée | Faible |
| Industrials | Élevée | Élevée | Modérée | Modérée |
| Consumer Discretionary | Modérée | Élevée | Élevée | Faible |
| Health Care | Faible | Élevée | Faible | Faible |
| Financials | Faible | Modérée | Faible | Faible |
| Utilities | Faible | Faible | Faible | Faible |

---

## Signaux Calculés

### 1. % Revenus Hors-USD
Si données FMP disponibles (segment reporting) :
```
pct_non_usd = 1 − (revenus_US / revenus_total)
```
Sinon : utiliser le proxy sectoriel ci-dessus.

### 2. Impact Revenus/EPS Estimé
```
impact_pct = pct_non_usd × β_fx × change_fx_20j
```
Où `β_fx` est la sensibilité historique du secteur à la devise (coefficient empirique).

### 3. Divergence Cours / Modèle FX
```
cours_implied_by_fx = cours_base × (1 + impact_pct)
divergence_pct = (cours_actuel − cours_implied) / cours_implied
```
- Divergence > 5% → [ANOMALIE FX] : le cours ne reflète pas le headwind/tailwind

### 4. Score FX Impact /10
```
score = min(10, pct_non_usd × 5 + abs(impact_pct) × 10 + trend_dxy × 2)
```
Classification :
- 0–2 : Faible / Inverse
- 3–5 : Modérée
- 6–8 : Élevée
- 9–10 : Très élevée + headwind/tailwind actif

---

## Seuils d'Alerte

- **Exposition élevée + DXY headwind + non pricé** → −1 pt Score Fondamental (EPS NTM sur-estimé)
- **Exposition élevée + DXY tailwind + non pricé** → +0.5 pt Score Valorisation
- **Divergence > 5%** → alerter [ANOMALIE FX] et chercher autre facteur explicatif

---

## Règles Absolues

- Ne jamais doubler le malus : si FX headwind ET guidance cut sur le même ticker, le malus FX s'applique une seule fois
- Si le ticker a des hedges naturels (opérations locales dans la devise étrangère), réduire l'exposition de 50%

---

## Output JSON

```json
{
  "AAPL": {
    "pct_non_usd": 0.58,
    "impact_revenus_pct": -2.1,
    "impact_eps_pct": -1.8,
    "divergence_pct": 1.2,
    "score_fx_impact": 6.5,
    "classification": "Élevée",
    "direction": "headwind",
    "adjustment": "−1 pt Score Fondamental"
  }
}
```

---

*Protocole lu par l'agent LLM et implémenté dans `agents/fx/agent.py`.*

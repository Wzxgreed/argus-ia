# Agent Event-Driven — Protocole d'Événements Corporates

**Script associé :** `agents/event_driven/agent.py`
**Output :** `data/events_YYYY-MM-DD.json` + `Alertes/EVENT_DRIVEN.md`

---

## Mission

Détecter et analyser les événements corporates structurants qui créent des catalyseurs de prix asymétriques :

- **M&A** (mergers & acquisitions)
- **Buybacks** (et leur qualité nette)
- **Activisme** (13D filings)
- **Guidance changes** (raise / cut / withdraw)
- **Spin-offs / divestitures**
- **FDA decisions** (biotech/pharma)
- **Settlements légaux**

---

## Sources

- `news` (Yahoo Finance) pour annonces publiques
- `secFilings` (8-K, 13D) pour événements réglementés
- `company` / `quote` pour contexte de valorisation

---

## Signaux Calculés

### 1. Spread M&A (arbitrage)
```
spread_pct = (prix offre − cours actuel) / cours actuel
```
- Spread > 5% + probabilité élevée de clôture → **+2 pt Catalyseur**
- Spread < 2% + risque régulatoire élevé → catalyseur faible

### 2. Buyback Net Yield
```
net_yield = (buyback_annual − stock_based_compensation_annual) / market_cap
```
- Net yield > 4% + cours sous-évalué → **+1 pt Valorisation**
- Buyback < SBC (dilution nette) → malus −0.5 pt

### 3. Activisme — Score de Succès
Pour chaque 13D filing, évaluer :
- **Track record** de l'activiste (historique des campagnes réussies)
- **Type de demande** : siège au board (probabilité succès ~60%), vente forcée (~40%), spin-off (~50%)
- **Taille de la position** (>5% = sérieux)

### 4. Guidance Changes
| Type | Impact Score Catalyseur |
|------|------------------------|
| Guidance raise > 5% | +2 pt |
| Guidance cut > 5% | −3 pt |
| Guidance withdrawn | −2.5 pt |
| Guidance inline | 0 pt |

### 5. Score Event-Driven /10
```
Score = (probabilité de réalisation × 4) +
        (asymétrie gain/perte × 3) +
        (1 / timeline en mois × 2) +
        (certaineté "déjà pricé ?" × 1)
```

---

## Seuils d'Action

- **M&A annoncé sur ticker watchlist** → ajuster Score Catalyseur +2 pt
- **Buyback net yield > 4%** → ajuster Score Valorisation +0.5 pt
- **Guidance cut > 5%** → ajuster Score Catalyseur −3 pt
- **13D filing** → générer `_update.md` flash automatique si pas déjà fait

---

## Règles Absolues

- **M&A hostile + spread > 10%** → ne pas augmenter le sizing standard (risque de deal break)
- **Guidance withdrawn + sector rotation défavorable** → double malus (−2.5 + −0.5 = −3 pt)
- **Activiste avec track record < 30%** → ne pas compter comme catalyseur positif

---

## Output JSON

```json
{
  "AAPL": {
    "events": [
      {"type": "buyback", "net_yield_pct": 3.8, "impact": "+0.5 Valorisation"},
      {"type": "guidance_raise", "magnitude_pct": 6.2, "impact": "+2 Catalyseur"}
    ],
    "score_event_driven": 6.5
  }
}
```

---

*Protocole lu par l'agent LLM et implémenté dans `agents/event_driven/agent.py`.*

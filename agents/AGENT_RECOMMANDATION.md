# Agent Recommandation

**Rôle :** Traduire la synthèse de tous les agents (Macro, Flux, Technique, Fondamental, Sentiment, FX, Event-Driven, Supply Chain, Accounting) en **actions explicites** pour chaque ticker de la watchlist. C'est le dernier maillon de la chaîne — celui qui transforme les scores en décisions.

**Déclenché par :**
- Workflow du matin — après tous les autres agents (étape finale)
- Commande manuelle : `Quelles sont les recommandations aujourd'hui ?`
- Commande manuelle : `Que faire sur [TICKER] ?`
- Changement de régime macro (Risk-off) — révision immédiate des recommandations

**Coopère avec :**
- ← **Tous les agents** : reçoit leurs scores, bonus/malus, alertes
- → **Portefeuille** : alimente `Portefeuille/POSITIONS.md` avec les entrées/sorties suggérées
- → **Paper Trading** : déclenche les ordres virtuels via `paper_trading.py`
- → **Utilisateur** : livrable final `Recommandations/YYYY-MM-DD.md`

---

## Philosophie

**Pas de prédiction de cours.** L'agent ne dit pas "AAPL sera à $210 dans 3 mois". Il dit :
- "Sur la base des données disponibles aujourd'hui, le profil risque/rendement d'AAPL est favorable"
- "Le timing technique est défavorable — attendre le retour au-dessus de MM50"
- "Un événement binaire (M&A) crée une asymétrie positive — entrée possible avec sizing réduit"

**Règle absolue :** Aucune recommandation sans que les étapes 0a (données) et 0b (mémoire) aient été exécutées. Pas de "intuition" — uniquement des scores quantifiés.

---

## Source de vérité

L'agent lit **exclusivement** les JSON produits par les autres agents. Il n'appelle jamais d'API directement.

| Fichier JSON | Agent source | Ce qu'il en extrait |
|--------------|--------------|-------------------|
| `data/latest.json` | `fetch_prices.py` | Cours, volumes, RSI, ATR, MM, FMP data |
| `data/quant_report_latest.json` | `agent_quant.py` | P-value, win rate, calibration |
| `data/geo_risk_latest.json` | `agent_geo.py` | Score Politique, scénarios |
| `data/crypto_correlation_latest.json` | `agent_crypto.py` | Beta BTC, divergence |
| `data/accounting_risk_latest.json` | `agent_accounting.py` | M-Score, Z-Score, F-Score |
| `data/sector_rotation_latest.json` | `agent_sector_rotation.py` | RS vs SPY, ranking |
| `data/social_sentiment_latest.json` | `agent_social.py` | Sentiment retail, pump |
| `data/fx_exposure_latest.json` | `agent_fx.py` | Score FX Impact, headwind/tailwind |
| `data/events_latest.json` | `agent_event_driven.py` | Event-Driven score, M&A, buybacks |
| `data/upcoming_events_latest.json` | `agent_watchman.py` | Earnings proches, insiders |
| `Actions/WATCHLIST_SCORES.md` | Agent LLM (synthèse) | Derniers scores par ticker |
| `Portefeuille/POSITIONS.md` | Utilisateur | Positions ouvertes réelles |
| `Portefeuille/PAPER_POSITIONS.json` | `paper_trading.py` | Positions paper trading |

---

## Signaux composite — Comment l'agent décide

### 1. Score Global Composite /100

```
Score Global =
  Score Opportunité (0–10)     × 10  →  0–100
  − Malus Accounting (0–30)          →  si M-Score > −1.78 ou Z-Score < 1.81
  − Malus Geo (0–20)                  →  si Score Politique ≥ 7
  − Malus FX (0–15)                   →  si FX Impact ≥ 7 + headwind
  − Malus Event (0–15)                →  si guidance cut > 5% ou 13D hostile
  − Malus Social (0–10)               →  si pump detected ou sentiment extrême < 1.5
  − Malus Quant (0–20)                →  si p-value > 0.20 (signaux non significatifs)
  + Bonus Event (0–20)                →  si M&A attractif + probabilité > 60%
  + Bonus Buyback (0–10)              →  si net buyback yield > 4%
  + Bonus Sector (0–10)               →  si ticker dans top 3 sector rotation
```

| Score Global | Signal brut | Interprétation |
|-------------|-------------|----------------|
| ≥ 80 | 🟢 Très favorable | Profil risque/rendement très attractif |
| 65–79 | 🟢 Favorable | Opportunité solide avec gestion du risque |
| 50–64 | 🟡 Neutre positif | Qualité présente mais pas de catalyseur clair |
| 35–49 | 🟡 Neutre | Ni attractif ni dangereux — pas d'action recommandée |
| 20–34 | 🟠 Prudent | Risques détectés (FX, geo, accounting) — éviter ou réduire |
| < 20 | 🔴 Défavorable | Multiple risques cumulés — éviter |

### 2. Timing technique — Filtre de confirmation

Le Score Global brut est ajusté par le timing technique. Une action peut avoir un profil fondamental excellent mais être surachetée technique (RSI > 70) ou en dessous de tous ses supports.

| Condition technique | Ajustement Score Global | Règle |
|--------------------|------------------------|-------|
| RSI 14j > 70 | −15 | Surachat technique — attendre correction |
| RSI 14j < 30 | +5 | Survente technique — possible rebond |
| Cours < MM50 ET MM200 | −10 | Tendance baissière confirmée |
| Cours > MM50 ET MM200 + Golden Cross | +10 | Tendance haussière confirmée |
| Volume > 2× moyenne 20j + cours hausse | +5 | Confirmation d'intérêt acheteur |
| Volume > 2× moyenne 20j + cours baisse | −5 | Distribution possible |
| ATR > 5% du cours | −5 | Volatilité élevée — sizing réduit |
| Force relative 90j vs S&P > 1.1 | +5 | Surperformance sectorielle |
| Force relative 90j vs S&P < 0.9 | −5 | Sous-performance sectorielle |

### 3. Détermination de l'action

L'action finale combine le Score Global ajusté + la présence ou non d'une position ouverte.

#### Cas A : Pas de position ouverte

| Score Global ajusté | Action | Direction | Horizon suggéré | Sizing |
|--------------------|--------|-----------|-----------------|--------|
| ≥ 75 | **ACHETER** | Long | 1–3 mois | Standard (1% risk / 2×ATR) |
| 60–74 | **ACHETER** avec confirmation | Long | 1–3 mois | Réduit (0.75% risk) |
| 50–59 | **ATTENDRE** | Neutre | — | — |
| 35–49 | **SURVEILLER** | Neutre | — | — |
| < 35 | **ÉVITER** | Neutre | — | — |

#### Cas B : Position ouverte en gain

| Score Global ajusté | Cours vs prix cible | Action |
|--------------------|--------------------|--------|
| ≥ 70 | Cours < prix cible − 10% | **CONSERVER** — thèse intacte |
| ≥ 70 | Cours ≥ prix cible | **PRENDRE PROFIT partiel** (25–50%) |
| 50–69 | Cours < prix cible | **CONSERVER** — surveillance renforcée |
| 50–69 | Cours ≥ prix cible | **VENDRE** — objectif atteint |
| < 50 | — | **RÉDUIRE** — dégradation du profil |
| < 35 | — | **VENDRE** — stop thèse |

#### Cas C : Position ouverte en perte

| Perte vs SL | Score Global ajusté | Action |
|-------------|--------------------|--------|
| Cours > SL | ≥ 60 | **CONSERVER** — stop non atteint, thèse intacte |
| Cours > SL | < 50 | **RÉDUIRE** — stop non atteint mais profil se dégrade |
| Cours ≤ SL | — | **VENDRE** — stop atteint, sortie mécanique |
| Cours > SL + 3 jours de baisse ≥ 5% | — | **VENDRE anticipé** — momentum très négatif |

#### Cas D : Position paper trading ouverte

L'agent lit `Portefeuille/PAPER_POSITIONS.json`. Les règles de sortie du paper trading priment :
- SL atteint (cours ≤ entrée − 2×ATR) → **CLOSE** obligatoire
- TP atteint (cours ≥ entrée + 3×ATR) → **CLOSE** ou réduction partielle
- Time stop J+60 → **CLOSE**
- Score Global < 40 → **CLOSE anticipé**

---

## Format de sortie — Recommandations du jour

### Fichier JSON : `data/recommandations_YYYY-MM-DD.json`

Structure pour consommation par le paper trading et les autres scripts.

```json
{
  "meta": {
    "date": "2026-05-16",
    "regime_macro": "Normal",
    "dxy_trend": "stable",
    "vix": 21.34,
    "total_tickers": 6,
    "recommandations_count": {
      "acheter": 2,
      "conserver": 1,
      "attendre": 1,
      "reduire": 1,
      "vendre": 1
    }
  },
  "recommandations": [
    {
      "ticker": "NVDA",
      "action": "ACHETER",
      "direction": "Long",
      "score_global": 82,
      "score_opportunite": 8.5,
      "timing": "Favorable",
      "horizon": "1–3 mois",
      "prix_entree_suggere": 185.50,
      "prix_cible": 210.00,
      "stop_loss": 179.00,
      "upside_potentiel_pct": 13.2,
      "risque_rendement_ratio": 2.1,
      "sizing": "Standard",
      "justification": [
        "Score Opportunité 8.5/10 (Catalyseur: contrat IREN, Valorisation: P/E 28 vs sector 35)",
        "RSI 54 (neutre), cours > MM50, Golden Cross confirmé",
        "FX headwind modéré (−0.3 pt) — impact limité",
        "Event-Driven: aucun événement négatif détecté",
        "Accounting: M-Score −2.1 (sain), Z-Score 4.2 (sain)",
        "Sector rotation: XLK top 1 RS vs SPY — secteur en favor"
      ],
      "risques": [
        "Earnings dans 4 jours → volatilité attendue",
        "Exposition Chine ~20% → risque géopolitique tarifaire"
      ],
      "alertes": []
    },
    {
      "ticker": "IREN",
      "action": "VENDRE",
      "direction": "Close",
      "score_global": 18,
      "score_opportunite": 3.2,
      "timing": "Défavorable",
      "horizon": "—",
      "justification": [
        "Score Opportunité 3.2/10 — Catalyseur très faible",
        "RSI en baisse, cours < MM50, pas de support proche",
        "Crypto correlation: beta BTC 2.1, BTC en baisse −5%",
        "Social sentiment: pump detected — signal de prudence",
        "FX: exposition CAD modérée, headwind léger"
      ],
      "risques": [
        "Rebond technique possible si BTC repart",
        "Volatilité extrême (ATR 10% du cours)"
      ],
      "alertes": ["Pump detecté sur Reddit — vérifier avec sources institutionnelles"]
    }
  ]
}
```

### Fichier Markdown : `Recommandations/YYYY-MM-DD.md`

Livrable humain — lu par l'utilisateur chaque matin.

```markdown
# Recommandations du Jour — 2026-05-16

## Contexte macro
**Régime :** Normal | **VIX :** 21.34 | **DXY :** stable (+0.4%) | **Tendance :** Risk-on modéré

---

## 🟢 À l'achat (2)

### NVDA — ACHETER (Score Global 82/100)
| | |
|---|---|
| **Prix actuel** | $185.50 |
| **Prix cible** | $210.00 (+13.2%) |
| **Stop-loss suggéré** | $179.00 (−3.5%) |
| **Ratio R/R** | 2.1 |
| **Horizon** | 1–3 mois |
| **Sizing** | Standard |

**Pourquoi :** Contrat IREN à $3.4B comme catalyseur immédiat. Valorisation P/E 28 vs sectoriel 35 (discount). Technique favorable : Golden Cross, RSI 54 (pas suracheté), volume en hausse. Accounting sain (M-Score −2.1, Z-Score 4.2).

**Risques :** Earnings dans 4 jours → volatilité. Exposition Chine ~20% → risque tarifaire.

---

## 🟡 Conserver (1)

### AAPL — CONSERVER (Score Global 68/100)
**Position ouverte** : Oui (entrée $178.50)
| | |
|---|---|
| **Prix actuel** | $191.00 |
| **Prix cible** | $210.00 |
| **Stop-loss** | $172.00 |
| **P&L position** | +7.0% |

**Pourquoi :** Thèse intacte. Filtre Qualité 5/6. FX headwind modéré (−0.3 pt) — pas de quoi paniquer. Attendre earnings pour réviser.

---

## 🟠 Réduire (1)

### XOM — RÉDUIRE (Score Global 32/100)
**Position ouverte** : Oui (entrée $155.00)

**Pourquoi :** Pétrole en baisse, DXY stable mais pétrole suracheté technique. FX headwind énergétique. Score Opportunité en dégradation. Ne pas vendre tout — conserver 50% et remonter SL.

---

## 🔴 À vendre / Éviter (1)

### IREN — VENDRE (Score Global 18/100)

**Pourquoi :** Score Opportunité effondré (3.2/10). BTC en baisse −5%, beta BTC 2.1 amplifie la chute. Pump detected sur Reddit — signal de prudence majeure. Pas de support technique proche.

---

## Résumé portefeuille

| | Valeur | P&L Jour |
|---|---|---|
| **Positions ouvertes** | 3 | — |
| **Actions suggérées** | ACHETER: 2, CONSERVER: 1, RÉDUIRE: 1, VENDRE: 1 | — |
| **Cash disponible** | XX% | — |

---

## Notes
- Win rate J+20 du système : 62% (20 derniers signaux)
- P-value : 0.08 (signaux significatifs)
- Prochain événement critique : NVDA earnings dans 4 jours
```

---

## Alertes automatiques de l'Agent Recommandation

| Condition | Alerte | Action |
|-----------|--------|--------|
| Score Global passe de > 70 à < 50 sur un ticker en position | 🔴 Dégradation majeure | Mettre à jour `POSITIONS.md` + suggérer réduction |
| Nouvelle entrée suggérée (Score ≥ 75) + pas de position | 🟢 Opportunité | Créer ligne dans `PAPER_TRADES.md` si paper trading actif |
| Stop-loss approche à −5% du cours | 🟡 Stop proche | Alerte dans le bulletin + surveillance renforcée |
| 3 tickers watchlist passent en 🔴 même jour | 🔴 Alerte système | Vérifier le régime macro — possible basculement Risk-off |
| Score Global > 80 mais timing RSI > 70 | 🟡 Value trap technique | Note "Attendre correction" au lieu de "Acheter" |
| Toutes les positions ouvertes en perte + VIX > 25 | 🔴 Capitulation potentielle | Suggérer hedge SPY puts |

---

## Intégration Paper Trading

L'Agent Recommandation est le **déclencheur** du paper trading. Quand une recommandation `ACHETER` est émise :

```
1. Agent Recommandation émet ACHETER NVDA
2. Si paper trading actif :
   → Calculer sizing via MODULE_SIZING (ATR, score, capital)
   → Écrire entrée dans PAPER_TRADES.md
   → Mettre à jour PAPER_POSITIONS.json
   → Définir SL = entrée − 2×ATR, TP = entrée + 3×ATR
3. Si position réelle existe déjà :
   → Mettre à jour POSITIONS.md avec la recommandation
   → Ne PAS exécuter automatiquement (l'utilisateur décide)
```

---

## Limites et avertissements

1. **Pas de prédiction.** Le système ne sait pas où le cours sera demain. Il évalue la qualité d'une opportunité à un instant T.
2. **Pas de conseil financier.** Ces recommandations sont des outils d'analyse, pas des ordres d'achat/vente. L'utilisateur garde la décision finale.
3. **Dépendance aux données.** Si `latest.json` contient des erreurs (fetch échoué, données partielles), la recommandation sera biaisée. L'agent doit toujours vérifier `validation_report.txt`.
4. **Délai.** Les recommandations sont basées sur les données du dernier pipeline. Si le marché a bougé de 5% depuis, la recommandation est obsolète.
5. **Surapprentissage.** Si les scores sont calibrés sur un régime passé qui change, les recommandations peuvent devenir contre-productives. D'où l'importance du Quant Report (p-value).

---

## Commandes rapides

| Commande | Action |
|----------|--------|
| `Quelles sont les recommandations aujourd'hui ?` | Lancer l'Agent Recommandation sur toute la watchlist |
| `Que faire sur [TICKER] ?` | Recommandation spécifique pour un ticker |
| `Mets à jour les recommandations après la news sur [TICKER]` | Recalcul après événement |
| `Quel est le ratio risque/rendement de [TICKER] ?` | Niveaux d'entrée, SL, TP |
| `Quelles positions devrais-je fermer ?` | Scan des positions ouvertes en dégradation |

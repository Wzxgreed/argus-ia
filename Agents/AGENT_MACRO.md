# Agent Macro

**Rôle :** Surveiller en continu le régime macroéconomique mondial, identifier les ruptures de tendance macro, et recalibrer dynamiquement la pondération des 3 agents (Technique, Fondamental, Sentiment) en conséquence. C'est le méta-agent qui donne le contexte dans lequel les 3 autres opèrent.

**Déclenché par :**
- Workflow du matin — s'exécute en **premier**, avant tout autre agent
- Publication d'un indicateur macro majeur (CPI, NFP, PIB, décision de banque centrale)
- Franchissement d'un seuil macro critique (VIX > 30, inversion courbe, DXY > 105...)
- Commande manuelle : `Analyse macro : quel est le régime actuel ?`

**Coopère avec :**
- → Agent Sentiment : fournit le régime macro pour calibrer le VIX et le risk-on/off
- → Agent Fondamental : ajuste la prime de risque et le WACC dans le DCF
- → Agent Technique : signale les niveaux macro qui font office de support/résistance systémiques
- → Orchestration : publie le régime actif qui détermine la pondération du score final

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `indexes` | S&P 500, NASDAQ, Russell 2000, VIX, obligations 10 ans US |
| `economics` | CPI, PCE, NFP, PIB, PMI, ISM, chômage, ventes retail, confiance consommateur |
| `forex` | DXY, EUR/USD, USD/JPY, USD/CNY — force/faiblesse du dollar |
| `commodity` | Pétrole (WTI/Brent), gaz naturel, or, cuivre (proxy croissance) |
| `news` | Fed speeches, BCE, BOJ, BOE, PBOC — signaux forward guidance |
| `calendar` | Calendrier des publications économiques à venir |

---

## Calendrier macro — Événements à surveiller

### Publications hebdomadaires
| Jour | Publication | Impact marché |
|------|------------|---------------|
| Lundi | PMI manufacturier | Modéré |
| Mercredi | ISM Services + stocks pétrole EIA | Modéré |
| Jeudi | Inscriptions chômage hebdo | Modéré |
| Vendredi | NFP (1er vendredi du mois) | **Élevé** |

### Publications mensuelles clés
| Publication | Fréquence | Impact |
|------------|-----------|--------|
| CPI (Inflation) | Mensuel | **Très élevé** |
| PCE Core | Mensuel | **Très élevé** (préféré Fed) |
| PIB (GDP) | Trimestriel | **Élevé** |
| PPI (Prix producteurs) | Mensuel | Modéré |
| Retail Sales | Mensuel | Modéré |
| Confiance consommateur (Michigan/Conference Board) | Mensuel | Modéré |
| PMI Composite (ISM + Markit) | Mensuel | Modéré |

### Événements banques centrales
| Banque | Fréquence réunions | À surveiller |
|--------|-------------------|--------------|
| **Fed (FOMC)** | 8x/an | Décision taux + dot plot + conférence Powell |
| BCE | 8x/an | Décision taux + forward guidance Lagarde |
| BOJ | 8x/an | YCC (yield curve control) + pivot potentiel |
| BOE | 8x/an | Inflation UK + récession |
| PBOC | Mensuel | Reserve ratio (RRR) + taux de repo |

> **Règle :** Dans les 48h avant une décision FOMC → passer automatiquement en régime **Pré-FOMC** (pondération spéciale, voir ci-dessous).

---

## Indicateurs de régime macro

### 1. Courbe des taux (Yield Curve)
| Configuration | Signal | Implication marchés |
|--------------|--------|---------------------|
| Taux 10Y − 2Y > +50 bps | Courbe normale | Croissance attendue, risk-on |
| Taux 10Y − 2Y entre 0 et +50 bps | Aplatissement | Ralentissement possible |
| Taux 10Y − 2Y < 0 (inversion) | Inversion | Signal récessionnaire (fiable à 12-18 mois) |
| Désinversion rapide après inversion | Recoupling | Phase la plus dangereuse historiquement |

### 2. DXY (Dollar Index)
| Niveau/Tendance | Implication |
|----------------|-------------|
| DXY en hausse forte (>1% semaine) | Pression sur commodités, EM, multinationales US |
| DXY stable (±0.5% semaine) | Neutre |
| DXY en baisse (>1% semaine) | Favorable aux commodités, EM, exportateurs US |
| DXY > 105 | Zone de stress pour les marchés émergents |
| DXY < 100 | Zone favorable à la reflation mondiale |

### 3. VIX — Régime de volatilité
| VIX | Régime | Pondération |
|-----|--------|-------------|
| < 15 | Euphorie / Complacence | Risk-on Bull |
| 15–25 | Normal | Normal |
| 25–35 | Stress / Peur | Risk-off |
| > 35 | Capitulation / Crise | Risk-off extrême |

### 4. Spreads de crédit
| Indicateur | Seuil | Signal |
|-----------|-------|--------|
| IG Credit Spread (Investment Grade) | > 150 bps | Stress financier modéré |
| HY Credit Spread (High Yield) | > 400 bps | Stress financier élevé |
| HY Credit Spread | > 700 bps | Crise de crédit — réduire exposition |
| Tendance spreads | En rétrécissement | Risk-on — favorable aux actions |

### 5. Cuivre / Or (ratio)
| Ratio Cu/Au | Signal | Interprétation |
|------------|--------|----------------|
| En hausse | Positif | Croissance attendue, appétit pour le risque |
| En baisse | Négatif | Ralentissement économique anticipé |

---

## Régimes macro et pondérations

L'Agent Macro déclare **un régime unique** en début de workflow. Ce régime détermine les pondérations utilisées par l'Orchestration.

| Régime | Conditions requises | Catalyseur | Valorisation | Momentum |
|--------|--------------------|----|----|----|
| **Normal** | VIX 15–25 · Courbe normale · Spreads HY < 400 bps | 40% | 35% | 25% |
| **Risk-on / Bull** | VIX < 15 · DXY faible · Cuivre en hausse | 40% | 25% | 35% |
| **Risk-off** | VIX 25–35 · Spreads HY > 400 bps · Courbe aplatie | 30% | 45% | 25% |
| **Risk-off extrême** | VIX > 35 · Spreads HY > 700 bps · DXY spike | 20% | 55% | 25% |
| **Pré-FOMC** | FOMC dans ≤ 48h | 50% | 30% | 20% |
| **Pré-earnings** | Earnings watchlist dans ≤ 5 jours | 50% | 30% | 20% |
| **Stagflation** | Inflation > 4% ET PIB < 1% | 30% | 40% | 30% |
| **Récession confirmée** | 2 trimestres PIB négatifs | 25% | 50% | 25% |

> **Priorité :** Si plusieurs conditions coexistent, prendre le régime le plus restrictif. Ex : Pré-FOMC + VIX > 25 → appliquer Risk-off (plus conservateur).

---

## Carte d'exposition macro par secteur

| Secteur | USD fort | Taux hausse | Pétrole hausse | Chine slow | Récession |
|---------|----------|-------------|----------------|-----------|-----------|
| Tech US (export) | ❌ −5 à −10% | ❌ −8% (duration) | ⚪ Neutre | ❌ −5% | ❌ −15% |
| Énergie | ⚪ Neutre | ⚪ Neutre | ✅ +10 à +20% | ⚪ Neutre | ❌ −10% |
| Banques US | ⚪ Neutre | ✅ +5 à +8% | ⚪ Neutre | ❌ −3% | ❌ −20% |
| Consommation discrétionnaire | ❌ −3% | ❌ −5% | ❌ −3% | ❌ −8% | ❌ −25% |
| Healthcare | ✅ +2% | ⚪ Neutre | ⚪ Neutre | ⚪ Neutre | ✅ +5% (défensif) |
| Matériaux / Mines | ❌ −8% | ⚪ Neutre | ⚪ Neutre | ❌ −10% | ❌ −15% |
| Immobilier (REIT) | ⚪ Neutre | ❌ −10% | ⚪ Neutre | ⚪ Neutre | ❌ −15% |
| Utilities | ⚪ Neutre | ❌ −8% | ✅ +3% | ⚪ Neutre | ✅ +5% (défensif) |
| Semi-conducteurs | ❌ −5% | ❌ −10% | ⚪ Neutre | ❌ −15% | ❌ −20% |
| Défense / Aéro | ✅ +3% | ⚪ Neutre | ⚪ Neutre | ✅ +5% | ⚪ Neutre |

> **Usage :** Cette carte est lue par l'Agent Fondamental pour chiffrer l'impact sectoriel sur chaque ticker de la watchlist lors du workflow du matin.

---

## Format de sortie — Bloc Macro

> Ce bloc est produit en tête de chaque bulletin et de chaque analyse `_init.md`.

```markdown
## Contexte Macro [Agent Macro — YYYY-MM-DD]

### Régime actif : [NORMAL / RISK-OFF / RISK-ON / PRÉ-FOMC / PRÉ-EARNINGS / STAGFLATION / RÉCESSION]
**Pondération active :** Catalyseur XX% · Valorisation XX% · Momentum XX%

### Indicateurs clés
| Indicateur | Valeur | Variation 1 sem. | Signal |
|-----------|--------|-----------------|--------|
| VIX | XX | +/-X | Peur / Normal / Euphorique |
| Taux 10Y US | XX% | +/-X bps | Haussier / Stable / Baissier |
| Courbe 10Y−2Y | +/-X bps | Inversion / Normale / Aplatissement |
| DXY | XXX.X | +/-X% | Fort / Neutre / Faible |
| Pétrole WTI | $XX | +/-X% | Haussier / Stable / Baissier |
| Or | $XXX | +/-X% | Risk-off / Neutre |
| Cuivre | $X.XX | +/-X% | Croissance / Ralentissement |
| HY Spread | XXX bps | +/-X bps | Sain / Stress / Crise |

### Événements macro à venir (7 jours)
| Date | Publication | Consensus | Importance |
|------|------------|-----------|-----------|
| YYYY-MM-DD | CPI US | X.X% | 🔴 Critique |
| ... | ... | ... | ... |

### Lecture macro
**Tendance dominante :** [Croissance / Ralentissement / Stagflation / Récession]
**Banques centrales :** [Hawkish / Pivot / Dovish] — [Fed] / [BCE] / [BOJ]
**Risque principal :** [Ex : Réaccélération inflation → retard pivot Fed]
**Opportunité macro :** [Ex : Détente des taux → rebond des valeurs de croissance long duration]

### Impact sur la watchlist — Alerte sectorielle
> [Ex : Hausse DXY +2% cette semaine → pression sur les multinationales tech (AAPL, MSFT). Voir carte d'exposition sectorielle.]

### HANDOFF → Agents Technique / Fondamental / Sentiment
> `Régime : [NORMAL/RISK-OFF/RISK-ON/...] | Pondération : Cat XX% · Val XX% · Mom XX% | VIX : XX | Taux 10Y : XX% | Courbe : [Normale/Aplatie/Inversée] | DXY : [Fort/Neutre/Faible] | Spreads HY : XXX bps [Sain/Stress] | Biais marché : [Risk-on/Risk-off/Indécis]`
```

---

## Alertes macro automatiques

| Condition | Alerte déclenchée | Action |
|-----------|------------------|--------|
| VIX franchit 25 à la hausse | 🟡 Alerte Risk-off | Basculer pondération Risk-off + notifier dans bulletin |
| VIX franchit 35 à la hausse | 🔴 Alerte Risk-off extrême | Revoir toutes les positions ouvertes + réviser stop-loss |
| VIX redescend sous 20 après spike | 🟢 Retour au calme | Rebascule progressivement vers pondération normale |
| Inversion courbe 10Y−2Y | 🔴 Signal récessionnaire | Mentionner dans bulletin + renforcer les défensifs |
| NFP/CPI hors consensus > 20% | 🔴 Surprise macro | Déclencher analyse d'impact sur toute la watchlist |
| DXY +2% en une semaine | 🟡 Alerte USD | Appliquer carte d'exposition sectorielle — alerter multinationales |
| HY Spread > 500 bps | 🔴 Stress crédit | Réduire exposition générale recommandée |
| FOMC dans ≤ 48h | ⚠️ Pré-FOMC | Basculer en régime Pré-FOMC automatiquement |

---

## Scoring macro pour ajustement du score Opportunité

L'Agent Macro ne produit pas de score direct mais introduit deux ajustements :

**Ajustement de pondération** (décrit ci-dessus) — modifie les poids Catalyseur/Valorisation/Momentum.

**Bonus/malus macro sur le score final :**
| Condition | Ajustement |
|-----------|-----------|
| Régime Risk-on + action dans secteur favorisé par la macro | +0.5 pt sur score final |
| Régime Risk-off + action défensive (Healthcare, Utilities, Cash) | +0.5 pt sur score final |
| Régime Risk-off + action cyclique à fort levier | −1 pt sur score final |
| Surprise macro négative majeure (CPI >> consensus) | −0.5 pt pour toutes les actions de croissance |
| Pivot banque centrale confirmé | +0.5 pt pour les actions de croissance long duration |

---

## Hedge automatique Risk-off — Protocole de couverture

> Ce protocole est déclenché **automatiquement** quand le régime bascule en Risk-off (VIX > 25) ou Risk-off extrême (VIX > 35).
> L'objectif est de proposer une couverture calibrée au portefeuille existant, sans nécessiter d'action manuelle de l'utilisateur.

### Conditions de déclenchement

| Condition | Niveau de hedge | Urgence |
|-----------|----------------|---------|
| VIX franchit 25 + régime Risk-off | Hedge partiel (20-30% exposition) | 🟡 Modérée |
| VIX franchit 35 + Risk-off extrême | Hedge fort (40-60% exposition) | 🔴 Élevée |
| Inversion courbe 10Y-2Y + données récessionnaires | Hedge défensif (rotation) | 🟡 Modérée |
| HY Spread > 500 bps | Hedge crédit | 🔴 Élevée |
| DXY +3% en 5 jours | Hedge USD (multinationales) | 🟡 Modérée |

### Calcul de la couverture recommandée

```
ÉTAPE 1 — Identifier l'exposition nette à couvrir
→ Lire Portefeuille/POSITIONS.md
→ Calculer l'exposition totale en capital déployé (hors cash)
→ Identifier les positions les plus cycliques / long duration (betas > 1.2)

ÉTAPE 2 — Choisir l'instrument de hedge selon le régime
→ Risk-off standard : SPY puts (expiration 30-60j, strike -5% à -10% OTM)
→ Risk-off extrême : SPY puts + VIX calls (expiration < 30j)
→ Récession probable : Rotation vers defensives + or
→ Stress crédit HY : Réduction positions high-beta + LQD / TLT
→ USD fort : Réduction multinationales exposées Asie / EM

ÉTAPE 3 — Calibrer la taille du hedge
→ Taille hedge = Exposition à couvrir × Pourcentage de couverture désiré
→ Pourcentage de couverture = f(niveau de stress) :
   VIX 25-30 : 20% de l'exposition cyclique
   VIX 30-35 : 35% de l'exposition cyclique
   VIX > 35   : 50% de l'exposition cyclique

→ Vérifier le delta du put : strike -5% OTM ≈ delta 0.25 → multiplier la taille par 4
   [Pour couvrir $10k d'exposition avec des puts delta 0.25 → acheter $40k notionnel de puts]

ÉTAPE 4 — Coût du hedge (sanity check)
→ Estimer le coût de la prime (% du capital couvert)
→ Si coût > 1.5% du capital total → envisager alternatives moins chères (collars, covered puts)
```

### Menu de hedges par régime

| Régime | Hedge principal | Hedge secondaire | Rotation recommandée |
|--------|---------------|-----------------|---------------------|
| Risk-off standard (VIX 25-30) | SPY puts OTM -5% (30-60j) | Position or (GLD/IAU) | Réduire cycliques de 20% |
| Risk-off extrême (VIX > 35) | SPY puts OTM -10% (30j) + VIX calls | T-bills / cash | Réduire cycliques de 40% |
| Pré-récession (courbe inversée) | TLT (obligations LT) + XLU (Utilities) | GLD + cash | Rotation vers défensives |
| Stress crédit (HY > 500 bps) | Réduire positions à levier élevé | Cash + Investment Grade | Sortir des small caps |
| USD fort (DXY > 105) | Réduire multinationales (AAPL, MSFT, CAT) | USD cash directement | Préférer pure domestic plays |

### Format dans le bulletin quand déclenché

```markdown
## ⚠️ ALERTE HEDGE — Régime Risk-off [VIX : XX]

**Régime actif :** Risk-off [standard / extrême]
**Exposition totale à couvrir :** $XXXk (XX% du portefeuille)
**Exposition cyclique prioritaire :** [TICK1] ($Xk) + [TICK2] ($Xk) = $Xk

**Hedge recommandé :**
| Instrument | Taille | Coût estimé | Protection |
|-----------|--------|------------|-----------|
| SPY Puts -5% OTM (expiration 30j) | XX contrats (~$Xk notionnel) | ~$XXX prime | Couverture XX% |
| GLD (or) | XX% du capital | — | Décorrélation |

**Coût total hedge :** ~$XXX (X.X% du capital)
**Niveau de couverture atteint :** XX% de l'exposition cyclique

**Actions immédiates recommandées :**
1. [Réduire [TICKER] de XX% si stop-loss ATR franchi]
2. [Ne pas ouvrir de nouvelles positions cycliques jusqu'à VIX < 22]
```

### Déclenchement automatique de la désactivation du hedge

```
QUAND DÉSACTIVER LE HEDGE :
→ VIX redescend sous 20 pendant 3 jours consécutifs → hedge inutile
→ Régime rebascule vers Normal ou Risk-on → fermer les puts progressivement
→ Perte sur le hedge > 80% de la prime payée → fermer (stop loss sur le hedge)

RÈGLE GÉNÉRALE :
→ Un hedge acheté pendant un spike de VIX se dévalue rapidement si le VIX redescend
→ Ne jamais maintenir un hedge coûteux dans un régime redevenu calme
→ L'objectif est la protection, pas le profit sur le hedge lui-même
```

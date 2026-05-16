# Agent Flux

**Rôle :** Tracer les flux d'argent institutionnels — qui achète, qui vend, combien, et où — pour détecter les positionnements cachés, les rotations sectorielles, et les setups à fort potentiel que les données publiques seules ne révèlent pas.

**Déclenché par :**
- Workflow du matin — s'exécute après l'Agent Macro, en parallèle avec l'Agent Sentiment
- Publication trimestrielle des 13F (45 jours après fin de trimestre)
- Détection d'un volume anormal (>2x) sur un ticker watchlist
- Commande manuelle : `Analyse flux institutionnels de [TICKER]`

**Coopère avec :**
- → Agent Technique : fournit l'explication des volumes anormaux (flux bloc, ETF rebalancing)
- → Agent Sentiment : enrichit la section Short Interest avec borrow rate et évolution
- → Agent Fondamental : signale les accumulations/distributions institutionnelles pour pondérer la thèse
- → Orchestration : bonus/malus sur le score Catalyseur si flux net significatif détecté

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `form13F` | Positions des grands fonds (hedge funds, mutual funds) — trimestriel |
| `etfAndMutualFunds` | Quels ETF détiennent le titre + pondération + flux nets |
| `quote` | Short interest, borrow rate, days to cover, volume relatif |
| `insiderTrades` | Achats/ventes d'initiés (cross-référence avec Agent Sentiment) |
| `marketPerformance` | Performance relative secteur vs marché (proxy rotation) |
| `indexes` | Flows sectoriels (tech vs value vs défensifs) |

---

## Métriques analysées

### 1. Flux 13F — Activité des grands fonds

> Les 13F sont publiés avec 45 jours de délai. Ils révèlent les positions au dernier jour du trimestre.

| Signal | Calcul | Interprétation |
|--------|--------|----------------|
| **Nouveaux entrants** | Fonds ayant initialisé une position vs trimestre précédent | Intérêt institutionnel nouveau → signal positif |
| **Sortants** | Fonds ayant liquidé leur position | Distribution institutionnelle → signal négatif |
| **Renforcements** | Fonds ayant augmenté leur position > +20% | Conviction croissante |
| **Réductions** | Fonds ayant réduit > −20% | Prise de bénéfice ou perte de conviction |
| **Concentration** | % des actions détenues par les 10 plus grands fonds | > 50% = très concentré (risque de déstabilisation) |
| **Nombre de fonds** | Total des fonds déclarés | En hausse = intérêt croissant / en baisse = abandon |

**Fonds clés à surveiller en priorité :**
- Berkshire Hathaway (Buffett) — signal de qualité long terme
- Bridgewater Associates (Dalio) — signal macro
- Tiger Global, Coatue, D1 Capital — signal growth tech
- ValueAct, Third Point — signal activiste (potentiel catalyseur)
- BlackRock, Vanguard — signal de momentum institutionnel large

### 2. Flux ETF

| Signal | Calcul | Interprétation |
|--------|--------|----------------|
| **Exposition ETF** | Nombre d'ETF détenant le titre + AUM total exposé | Proxy liquidité institutionnelle |
| **Flux ETF nets** | Souscriptions − rachats sur les ETF majeurs (7j, 30j) | Entrées nettes = demande institutionnelle |
| **Poids dans ETF sectoriels** | % du titre dans les ETF de son secteur | Titre surpondéré = soutenu / sous-pondéré = délaissé |
| **Rééquilibrage ETF** | Reconstitution des indices (S&P 500, Russell, MSCI) | Achat/vente forcé prévisible → opportunité |
| **ETF thématiques** | Présence dans ETF IA, Défense, Clean Energy, etc. | Exposition à une thèse macro sectorielle |

**ETF majeurs à surveiller par secteur :**
| Secteur | ETF de référence |
|---------|----------------|
| Tech large cap | QQQ, XLK |
| Small caps | IWM, IJR |
| Valeur financière | XLF |
| Énergie | XLE |
| Santé | XLV |
| Défense | ITA, XAR |
| IA / Semi | SOXX, SMH, BOTZ |

### 3. Short Interest — Analyse approfondie

> Complète et enrichit le signal de l'Agent Sentiment.

| Métrique | Calcul | Seuil d'alerte | Interprétation |
|----------|--------|----------------|----------------|
| **Short interest (% float)** | Shares short / Float total | > 15% | Pression vendeuse structurelle |
| **Days to cover** | Shares short / Volume moyen 20j | > 5j | Fort — potentiel squeeze |
| **Borrow rate (taux d'emprunt)** | Taux annualisé pour emprunter le titre | > 10% | Short coûteux → pression sur les shorts |
| **Évolution 4 semaines** | Δ% short interest sur 4 sem. | > +15% | Shorts en accumulation — pression baissière |
| **Évolution 4 semaines** | Δ% short interest sur 4 sem. | < −20% | Covering — potentiel short squeeze |

**Short Squeeze Setup — Conditions cumulatives :**
```
✅ Short interest > 15% float
✅ Days to cover > 7j
✅ Borrow rate > 20% (coûteux à maintenir)
✅ Catalyseur positif identifié (earnings beat, upgrade, news)
✅ Volume > 1.5x moyenne 20j
→ ALERTE SQUEEZE : majorer score Catalyseur de +2 pts
```

### 4. Dark Pool & Block Trades

> Le dark pool représente ~35-40% du volume US. Les blocs significatifs révèlent des intentions institutionnelles.

| Signal | Définition | Interprétation |
|--------|-----------|----------------|
| **Block trade** | Transaction > 10 000 actions ou > $200k d'un coup | Institutionnel en action |
| **Dark pool ratio** | Volume dark pool / Volume total | > 50% = flux caché important |
| **Accumulation bloc** | Série de blocs en l'espace de 5j | Institution qui construit une position |
| **Distribution bloc** | Blocs en vente réguliers sur 5-10j | Institution qui sort progressivement |
| **Anomalie volume intraday** | Pic de volume à des horaires inhabituels | Possiblement lié à un ordre institutionnel |

### 5. Options Gamma Exposure & Max Pain

| Métrique | Définition | Usage |
|----------|-----------|-------|
| **Max Pain** | Cours à l'expiration qui fait perdre le plus aux acheteurs d'options | Attraction gravitationnelle du cours à l'expiration |
| **Gamma exposure (GEX)** | Sensibilité du delta des market makers à une variation de cours | GEX positif = market makers stabilisent le cours / GEX négatif = amplification des mouvements |
| **Mur de calls (call wall)** | Strike avec le plus gros open interest en calls | Résistance technique forte (les MM hedgent en vendant) |
| **Mur de puts (put wall)** | Strike avec le plus gros open interest en puts | Support technique fort (les MM hedgent en achetant) |
| **IV Rank** | Rang de l'IV actuelle vs les 52 dernières semaines | IV Rank > 80 = IV très élevée, opportunité de vente de vol / < 20 = IV basse, opportunité d'achat de vol |

**Lecture opérationnelle :**
- Cours entre put wall et call wall → range probable jusqu'à expiration
- Cours franchit le call wall avec volume → les MM doivent acheter → accélération haussière
- Cours sous le put wall → les MM doivent vendre → accélération baissière
- Max pain < cours actuel → pression à la baisse jusqu'à expiration

### 6. Rotation sectorielle institutionnelle

| Signal | Calcul | Interprétation |
|--------|--------|----------------|
| **Flux sectoriels nets** | Variation des flux ETF par secteur (7j) | Identifier les secteurs en accumulation/distribution |
| **Momentum relatif sectoriel** | Performance secteur vs S&P (4 semaines) | Identifier la rotation en cours |
| **Ratio growth/value** | QQQ / IWD | En hausse → risk-on, favoriser la croissance |
| **Ratio small/large** | IWM / SPY | En hausse → appétit pour le risque, conditions financières accommodantes |

---

## Format de sortie — Bloc Flux

> Ce bloc est inséré dans les `_init.md` et les `_update.md` quand un signal de flux est détecté.

```markdown
## Analyse Flux Institutionnels [Agent Flux — YYYY-MM-DD]

### Positionnement 13F (dernier trimestre connu : QX YYYY)
| Signal | Détail | Tendance |
|--------|--------|---------|
| Fonds détenteurs | X fonds | +/-X vs trimestre précédent |
| Nouveaux entrants | X fonds (dont : ...) | 🟢 Intérêt nouveau / ⚪ Stable / 🔴 Abandon |
| Sorties notables | X fonds (dont : ...) | — |
| Renforcements significatifs | X fonds > +20% (dont : ...) | — |
| Concentration top 10 | XX% du float | Élevée / Normale / Dispersée |

**Signal 13F net :** 🟢 Accumulation institutionnelle / ⚪ Stable / 🔴 Distribution

### Flux ETF
| ETF | Poids titre | Flux nets 30j | Signal |
|-----|------------|--------------|--------|
| [ETF majeur] | X.X% | +/- $XXXm | Entrées / Sorties |
| [ETF sectoriel] | X.X% | +/- $XXXm | Entrées / Sorties |

**Flux ETF net :** 🟢 Positif / ⚪ Neutre / 🔴 Négatif

### Short Interest & Borrow
| % Float | Days to Cover | Borrow Rate | Évolution 4 sem. | Squeeze Setup |
|---------|--------------|-------------|-----------------|--------------|
| XX% | Xj | X% | +/-X% | ✅ Oui / ❌ Non |

### Options — Gamma & Max Pain
| Expiration proche | Max Pain | Call Wall | Put Wall | GEX | IV Rank |
|------------------|----------|-----------|---------|-----|---------|
| YYYY-MM-DD | $XXX | $XXX | $XXX | Positif / Négatif | XX% |

**Lecture :** Cours actuel ($XXX) [au-dessus/en-dessous/entre] le put wall ($XXX) et le call wall ($XXX).
→ [Implication sur la direction probable jusqu'à expiration]

### Dark Pool & Blocs
| Signal | Détail | Interprétation |
|--------|--------|---------------|
| Ratio dark pool | XX% | Élevé / Normal |
| Blocs détectés (5j) | X blocs (achat/vente) | Accumulation / Distribution / Neutre |

### Rotation sectorielle
| Secteur du titre | Flux nets 7j | Position vs S&P 4 sem. | Signal |
|-----------------|-------------|----------------------|--------|
| [Secteur] | +/-$XXXm | +/-X% | En faveur / Délaissé |

### Verdict Flux
**Signal dominant :** 🟢 Accumulation institutionnelle / ⚪ Neutre / 🔴 Distribution
**Point de vigilance :** [Ex : Max pain à $XXX → possible pression baissière jusqu'au XX/XX]
**Boost score :** [+X pt Catalyseur si squeeze setup confirmé / -X pt si distribution lourde]

### HANDOFF → Agent Sentiment & Synthèse
> `Flux 13F : Accumulation/Stable/Distribution | Flux ETF : Positif/Neutre/Négatif | Short : XX% float, Xj cover, X% borrow | Squeeze setup : Oui/Non | Max Pain : $XXX | GEX : Positif/Négatif | Dark pool : Accumulation/Distribution/Neutre | Rotation secteur : Favorable/Neutre/Défavorable`
```

---

## Alertes automatiques générées par cet agent

| Condition | Alerte | Action |
|-----------|--------|--------|
| Nouveau grand fonds entre au 13F (>$50M) | 🟢 Accumulation institutionnelle | Notifier dans bulletin + ajouter dans `_update.md` |
| Grand fonds sort complètement | 🔴 Distribution institutionnelle | Notifier + réviser la thèse |
| Borrow rate dépasse 30% | ⚠️ Short très coûteux | Majorer probabilité de covering |
| Short interest baisse > −20% en 2 semaines | ⚠️ Covering en cours | Alert squeeze potentiel |
| Série de blocs acheteurs sur 5j | 🟢 Accumulation bloc | Notifier dans bulletin |
| Cours franchit le call wall avec volume > 2x | 🟢 Breakout gamma | Alerte achat technique confirmé institutionnellement |
| IV Rank > 80% sans earnings imminent | ⚠️ Marché nerveux | Prudence, possible news négative non publique |
| Entrées ETF sectoriel > $500m en 1 semaine | 🟢 Rotation favorable | Identifier les bénéficiaires dans la watchlist |

---

## Scoring — Contribution au score Catalyseur

L'Agent Flux contribue via des bonus/malus sur le Score Catalyseur de l'Agent Sentiment :

| Signal | Ajustement |
|--------|-----------|
| Accumulation 13F nette (> 5 nouveaux fonds) | +1 pt Catalyseur |
| Fonds activiste détecté (ValueAct, Third Point…) | +1.5 pt Catalyseur |
| Distribution 13F nette (> 5 sorties de fonds) | −1 pt Catalyseur |
| Short squeeze setup complet (4 conditions) | +2 pts Catalyseur |
| Dark pool accumulation sur 5j | +0.5 pt Catalyseur |
| Flux ETF nets positifs > $200m sur 30j | +0.5 pt Catalyseur |
| Cours en-dessous du put wall (GEX amplificateur baissier) | −0.5 pt Catalyseur |
| Cours au-dessus du call wall (GEX amplificateur haussier) | +0.5 pt Catalyseur |

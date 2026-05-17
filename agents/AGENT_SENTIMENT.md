# Agent Sentiment

**Rôle :** Mesurer le sentiment du marché sur une action — via les news, les positions d'analystes, l'activité des insiders, les signaux de la communauté financière et les indicateurs de peur/cupidité — pour détecter les retournements et les opportunités que les fondamentaux seuls ne voient pas.

**Déclenché par :**
- Workflow du matin (bulletin) — scan global de la watchlist
- Détection d'une news impactante → analyse sentiment ciblée
- Création d'une analyse initiale (`_init.md`)
- Commande manuelle : `Analyse sentiment de [TICKER]`

**Coopère avec :**
- → Agent Technique : fournit le signal short interest pour pondérer les volumes
- → Agent Fondamental : fournit les révisions d'analystes pour recadrer les estimations
- → Opportunités : fournit le score Catalyseur Actualité (40% du score total)

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `news` | Articles financiers récents sur le ticker ou le secteur |
| `analyst` | Consensus, prix cibles, upgrades/downgrades récents |
| `insiderTrades` | Achats/ventes d'initiés (dirigeants, administrateurs) |
| `senate` | Transactions de sénateurs/membres du Congrès US |
| `commitmentOfTraders` | Positions nettes des fonds sur futures (matières premières, indices) |
| `quote` | Short interest (% float), days to cover |
| `marketPerformance` | Performance relative secteur vs marché |
| `indexes` | État des grands indices (context marché général) |

---

## Métriques analysées

### 1. Sentiment Analystes
| Signal | Source | Interprétation |
|--------|--------|----------------|
| Consensus Buy/Hold/Sell | `analyst` | > 70% Buy = très positif |
| Prix cible médian | `analyst` | vs cours actuel → upside/downside implicite |
| Upgrades récents (30j) | `analyst` | ≥ 2 upgrades = momentum positif |
| Downgrades récents (30j) | `analyst` | ≥ 2 downgrades = signal négatif |
| Révision prix cible (1 mois) | `analyst` | Hausse > 5% = confiance croissante |
| Dispersion des prix cibles | `analyst` | Fourchette étroite = consensus fort |

### 2. Activité Insiders
| Signal | Source | Interprétation |
|--------|--------|----------------|
| Achats net insiders (3 mois) | `insiderTrades` | > $500k achats = signal positif fort |
| Ventes nettes insiders (3 mois) | `insiderTrades` | > $2M ventes = signal ambigu (peut être planifié) |
| Achats CEO/CFO spécifiquement | `insiderTrades` | Achat CEO = signal très fort |
| Cluster buying | `insiderTrades` | ≥ 3 insiders achètent en même temps = signal fort |
| Ratio achats/ventes (3 mois) | `insiderTrades` | > 1 = net acheteur |

### 3. Short Interest
| Signal | Calcul | Interprétation |
|--------|--------|----------------|
| Short interest (% float) | Shares short / Float | < 5% faible, 5-15% modéré, > 15% élevé |
| Days to cover | Shares short / Volume moyen | > 5j = fort, potentiel short squeeze |
| Variation short (2 semaines) | Δ% short interest | > +10% = pression vendeuse croissante |
| Short squeeze setup | Short > 15% + Volume > 2x | Signal fort, surveiller de près |

### 4. Options Flow au niveau du titre — Analyse approfondie
| Signal | Source | Interprétation |
|--------|--------|----------------|
| Put/Call ratio individuel | `quote` options chain | < 0.7 = biais haussier · > 1.2 = peur / protection |
| IV 30j (Implied Volatility) | `quote` options | — comparé à HV 30j historique |
| IV vs HV | IV − HV | IV >> HV = peur du marché sur ce titre spécifiquement |
| **IV Rank (IVR)** | Rang IV actuelle vs 52 semaines | IVR > 80 = IV très haute (vente de vol) · IVR < 20 = IV basse (achat de vol) |
| Options flow net | Calls minus Puts $ notionnel | Flux net positif = biais institutionnel haussier |
| Expiry cliff | Options expirant dans < 7j | Position dominante → peut créer un gamma squeeze |
| **Max Pain** | Strike où les acheteurs perdent le plus | Attraction gravitationnelle du cours à l'expiration |
| **Call wall** | Strike avec plus gros OI calls | Résistance dynamique (MM hedgent en vendant) |
| **Put wall** | Strike avec plus gros OI puts | Support dynamique (MM hedgent en achetant) |
| **GEX (Gamma Exposure)** | Sensibilité delta des MM | GEX positif = marché stabilisé · GEX négatif = mouvements amplifiés |
| **Unusual options activity** | Volume options >> OI (ratio > 3×) | Achat directionnel institutionnel — surveiller l'expiration et le strike |

**Règle IV vs HV :**
- IV > HV + 10 pts → marché très nerveux, peur non résolue → attendre stabilisation OU saisir l'opportunité si fondamental solide
- IV ≈ HV → volatilité pricée normalement
- IV < HV → complacence → le marché sous-estime le risque

**Lecture Max Pain / Gamma :**
- Cours entre put wall et call wall → range probable jusqu'à expiration (les MM stabilisent)
- Cours franchit le call wall + volume > 2x → MM doivent acheter → accélération haussière (gamma squeeze)
- Cours sous le put wall → MM doivent vendre → accélération baissière
- GEX négatif = environnement de forte volatilité (mouvements amplifiés dans les 2 sens)

**Unusual Options Activity — protocole d'alerte :**
```
Si volume options > 3× OI habituel ET expiration < 30j :
→ Identifier le strike et la direction (call/put)
→ Vérifier s'il y a un événement prévu (earnings, FDA, FOMC)
→ Si pas d'événement connu → alerte "information non publique potentielle"
→ Ajouter dans le bulletin et dans le _update.md du ticker
```

### 5. Earnings Whisper & Surprise Historique
| Signal | Source | Interprétation |
|--------|--------|----------------|
| Earnings Whisper | Communauté vs consensus | Whisper > consensus = bar implicite plus élevé |
| Historique beat/miss | `earningsTranscript` / `statements` | ≥ 75% beat = management crédible |
| Surprise EPS moyenne | Δ EPS réel vs consensus | > +5% systématiquement = signal positif |
| Réaction moyenne post-earnings | % variation cours | Ampleur typique = calibrer l'anticipation |

### 6. News & Médias
| Signal | Source | Interprétation |
|--------|--------|----------------|
| Volume de news (7 jours) | `news` | Pic = événement majeur |
| Tonalité des titres | `news` | Analyser positif/négatif/neutre |
| News macro liées | `news` | Impact sectoriel ou géopolitique |
| Mention dans news geopolitiques | `news` | Exposition à un risque mondial |

### 7. Job Postings — Signal Avancé 6-12 mois

> Les offres d'emploi sont l'un des meilleurs indicateurs avancés disponibles publiquement. Une entreprise qui recrute massivement dans un domaine précis prépare quelque chose — bien avant que les résultats financiers le reflètent.

**Sources :** `news` (mentions licenciements/embauches) + `secFilings` (évolution effectifs 10-K) + `company` (taille équipes)

| Signal | Lead time | Interprétation |
|--------|-----------|----------------|
| **Recrutement massif ingénieurs IA/ML** | 6-12 mois | Produit IA en développement → avantage compétitif à venir |
| **Recrutement massif commerciaux / Sales** | 3-6 mois | Accélération de croissance anticipée en interne |
| **Suppression postes commerciaux** | 3-6 mois | Ralentissement de la demande admis en interne |
| **Recrutement R&D spécifique (ex: batteries, spatial)** | 12-24 mois | Pivot stratégique ou nouveau produit majeur |
| **Vague de licenciements (>5% effectifs)** | 1-3 mois | Restructuration, réduction coûts → marges court terme / risque morale équipes |
| **Départs massifs C-suite (CEO, CFO, CTO)** | 0-3 mois | Instabilité stratégique — signal négatif fort |
| **Recrutement head of manufacturing dans nouveau pays** | 12-18 mois | Diversification supply chain / expansion géographique |
| **Gel des embauches annoncé** | 1-6 mois | Direction prépare une période difficile |
| **Ratio R&D/Sales croissant sur recrutements** | 6-12 mois | Pivot vers innovation — positif long terme |

**Méthode de détection :**
```
1. À l'analyse initiale (_init.md) :
   → Chercher dans `news` les 6 derniers mois : "[TICKER] hiring", "[TICKER] layoffs",
     "[TICKER] recrute", "[TICKER] supprime postes"
   → Chercher dans `secFilings` (10-K) l'évolution des effectifs sur 3 ans
   → Chercher dans `company` la taille des équipes par département si disponible

2. Au bulletin du matin :
   → Surveiller les news de licenciements/embauches sur la watchlist
   → Si signal détecté → l'intégrer dans le _update.md avec le lead time estimé

3. Interprétation :
   → Ne jamais scorer seul — croiser avec les fondamentaux
   → Un recrutement massif sans revenus croissants = cash burn accéléré
   → Des licenciements ciblés sur une division = signal de pivot stratégique
```

**Format dans le Bloc Sentiment :**
```markdown
### Job Postings (signal avancé)
| Signal détecté | Ampleur | Lead time | Interprétation | Score impact |
|---------------|---------|-----------|----------------|--------------|
| [ex: +500 ingénieurs IA en 6 mois] | Fort | 6-12 mois | Produit IA imminent | +0.5 pt |
| [ex: Gel embauches annoncé] | Modéré | 1-6 mois | Prudence revenus | -0.5 pt |
```

**Bonus/malus scoring :**
- Recrutement massif dans domaine stratégique aligné avec thèse → +0.5 pt Catalyseur
- Vague licenciements > 10% effectifs → −1 pt Catalyseur
- Départs massifs C-suite → −0.5 pt Catalyseur
- Gel embauches → −0.3 pt Catalyseur

### 8. Transactions Politiques (US)
| Signal | Source | Interprétation |
|--------|--------|----------------|
| Achats sénateurs (3 mois) | `senate` | Insider view réglementaire potentiel |
| Ventes sénateurs (3 mois) | `senate` | Signal de risque réglementaire |

### 9. Contrats Gouvernementaux — Signal Avancé 12-24 mois

> Les contrats gouvernementaux sont publics, souvent massifs, et généralement sous-exploités par le marché dans les 24-48h suivant leur annonce. Particulièrement pertinent pour les secteurs **défense**, **infrastructure**, **santé**, **cloud gouvernemental**, **énergie**.

**Sources :** `secFilings` (8-K contrats matériels) + `news` (annonces SAM.gov, DoD, HHS) + `company` (part du CA gouvernemental)

#### Secteurs prioritaires à monitorer

| Secteur | Agences clés | Type de contrats | Lead time typique |
|---------|-------------|-----------------|-------------------|
| **Défense** | DoD, DARPA, NATO | IDIQ, prime contracts, R&D | 12-24 mois sur revenus |
| **Cloud/IT gouvernemental** | DoD, CIA, NSA, GSA | JWCC, JEDI successeurs | 12-36 mois sur revenus |
| **Santé** | HHS, VA, Medicare | Prestataires médicaux, IT santé | 6-18 mois |
| **Infrastructure** | DoT, DoE, Corps of Engineers | Grands travaux, énergie propre | 12-24 mois |
| **Spatial** | NASA, NRO, USSF | Contrats de lancement, satellites | 18-36 mois |

#### Protocole de détection

```
1. À l'analyse initiale (_init.md) :
   → Chercher dans `secFilings` les 8-K des 12 derniers mois avec mention "contract", "award", "DoD", "government"
   → Estimer la part du CA gouvernemental (mentionnée dans 10-K segment revenues)
   → Identifier les agences clientes et les dates de renouvellement de contrats

2. Au bulletin du matin (secteurs défense/infra/santé/cloud) :
   → Scanner `news` : "[TICKER] contract award", "[TICKER] DoD", "[TICKER] government"
   → Si contrat annoncé → estimer le montant, la durée, l'impact sur revenus

3. Évaluation d'un contrat détecté :
   → Montant / CA annuel × 100 = % de revenus additionnels
   → Durée du contrat → revenus récurrents ou one-shot
   → Nouveau client vs renouvellement (renouvellement = moins d'upside mais plus de visibilité)
```

#### Scoring des contrats gouvernementaux

| Type de contrat | Montant relatif | Impact Score |
|----------------|----------------|-------------|
| Nouveau contrat majeur (>5% CA annuel) | >5% CA | +2 pt Catalyseur |
| Renouvellement contrat clé | Maintien | +0.5 pt Catalyseur |
| Extension contrat existant (+scope) | >2% CA | +1 pt Catalyseur |
| Perte d'un contrat clé | >5% CA | −2 pt Catalyseur |
| Audit / enquête sur exécution | — | −1 pt Catalyseur |
| Gel budgétaire agence cliente | — | −0.5 pt Catalyseur |

**Format dans le Bloc Sentiment :**
```markdown
### Contrats Gouvernementaux (si secteur concerné)
| Date | Agence | Montant | Durée | Type | Impact CA estimé | Signal |
|------|--------|---------|-------|------|-----------------|--------|
| YYYY-MM-DD | DoD | $XXXm | X ans | Nouveau / Renouvellement | +X% | 🟢/🟡/🔴 |
```

### 5b. Track Record Analystes — Précision historique

> Toutes les recommandations ne se valent pas. Un upgrade de GS avec un analyste à 72% de précision vaut 3× un upgrade d'une boutique inconnue.

| Signal | Méthode | Interprétation |
|--------|---------|----------------|
| **Précision analyste (% correct)** | Historique beat/miss des prix cibles sur 12 mois | > 65% = fiable · < 45% = peu fiable |
| **Précision maison (% correct)** | Historique par banque sur le secteur | Goldman, MS, JPM souvent > 60% sur large cap |
| **Biais analyste** | Tendance systématique à surestimer/sous-estimer | Analyste toujours optimiste = ajuster cible à la baisse |
| **Révisions vs réalité** | Révisions de prix cible suivies de révisions de cours | Révision hausse suivie par d'autres = signal fort |
| **Délai de réaction** | Analyste upgrades en retard vs cours | Si upgrade après +20% = laggard, signal affaibli |

**Maisons de courtage — réputation sectorielle à noter dans INDEX.md :**
- Tech : Goldman Sachs, Wedbush, Piper Sandler
- Biotech/Pharma : SVB Securities, Cowen, Leerink
- Énergie : Tudor Pickering, Raymond James
- Banques : Wolfe Research, Evercore
- Consommation : UBS, Bernstein

**Règle de pondération :**
- Upgrade d'un analyste > 65% précision sur le secteur → ×1.5 sur le signal analyste
- Downgrade d'un analyste > 65% précision sur le secteur → ×1.5 sur le signal analyste négatif
- Note d'une maison < 45% de précision historique → ×0.5 (signal atténué)

> **Fichier de référence :** Documenter les track records découverts dans `Agents/ANALYST_TRACK_RECORD.md`

### 5c. EPS Revision Momentum — Signal Factoriel Clé

> L'accélération des révisions d'estimations à la hausse est l'un des signaux les plus documentés en factor investing. Elle prédit les surperformances avec une fiabilité élevée sur horizon 3-6 mois. C'est un signal distinct du consensus actuel : une action peut avoir 70% de Buy ET des révisions en baisse — c'est un signal de dégradation silencieuse.

**Sources :** `analyst` (estimations EPS/CA consensus + historique des révisions)

#### Métriques à calculer

| Métrique | Calcul | Interprétation |
|----------|--------|----------------|
| **Révisions 30j** | Nb analystes ayant relevé vs abaissé EPS FY1 sur 30j | Solde positif = momentum haussier |
| **Révisions 60j** | Même calcul sur 60 jours | Signal plus fiable (moins de bruit) |
| **Révisions 90j** | Même calcul sur 90 jours | Tendance structurelle |
| **EPS FY1 consensus Δ%** | (Consensus actuel − Consensus J-60) / Consensus J-60 | Variation absolue de l'estimation |
| **EPS FY2 consensus Δ%** | Même calcul sur l'année suivante | Moins sensible au trimestre en cours |
| **Vitesse de révision** | Accélération des révisions (Δ30j vs Δ60j précédents) | Accélération = signal plus fort |
| **Breadth de révision** | % d'analystes couvrant qui ont révisé en hausse | > 60% = fort consensus de révision |

#### Protocole de collecte

```
1. Via `analyst` : récupérer l'historique des estimations EPS consensus (FY1, FY2)
   → Comparer consensus J-0 vs J-30, J-60, J-90
   → Calculer le Δ% pour chaque horizon

2. Compter les révisions individuelles :
   → Nombre d'analystes ayant relevé EPS FY1 sur 30j (Révisions Hausse)
   → Nombre d'analystes ayant abaissé EPS FY1 sur 30j (Révisions Baisse)
   → Solde Net = Révisions Hausse − Révisions Baisse

3. Calculer la Vitesse :
   → Solde Net 30j vs Solde Net J-30 à J-60 (mois précédent)
   → Accélération = solde net en amélioration
   → Décélération = solde net en dégradation
```

#### Tableau de scoring EPS Revision Momentum

| Configuration | Signal | Ajustement Score |
|--------------|--------|-----------------|
| Solde net > +5 sur 30j + EPS FY1 Δ > +3% | 🚀 Révisions fortes | +1.5 pt Catalyseur |
| Solde net > +3 sur 30j + accélération | 🟢 Révisions positives | +1 pt Catalyseur |
| Solde net 0 à +2 / stable | ⚪ Neutre | 0 pt |
| Solde net négatif (−1 à −3) | 🟡 Légère dégradation | −0.5 pt Catalyseur |
| Solde net < −3 + EPS FY1 Δ < −3% | 🔴 Révisions négatives | −1 pt Catalyseur |
| Accélération baissière (dégradation qui s'amplifie) | 🔴🔴 Alerte | −1.5 pt Catalyseur |

#### Signaux composites puissants

| Combo | Interprétation |
|-------|---------------|
| Révisions fortes + Insiders acheteurs | Signal doublement confirmatoire — très fort |
| Révisions fortes + NLP confident (ratio > 2.5) | Le management confirme ce que les analystes anticipent |
| Révisions fortes + Prix cible consensus en hausse | Triple confirmation — probabilité de surperformance élevée |
| Révisions négatives + NLP prudent | Dégradation silencieuse avant profits warning — sortir ou réduire |
| Révisions négatives + Insiders vendeurs | Signal de sortie majeur |

**Format dans le Bloc Sentiment :**
```markdown
### EPS Revision Momentum
| Horizon | Révisions ↑ | Révisions ↓ | Solde Net | EPS FY1 Δ% | Vitesse | Signal |
|---------|------------|------------|-----------|-----------|---------|--------|
| 30j     | +X         | −X         | +/−X      | +/−X%     | ↑↑/↑/→/↓/↓↓ | |
| 60j     | +X         | −X         | +/−X      | +/−X%     | | |
| 90j     | +X         | −X         | +/−X      | +/−X%     | | |

**Verdict :** 🚀 Forte accélération / 🟢 Positif / ⚪ Neutre / 🟡 Légère dégradation / 🔴 Dégradation
```

---

### 6. Sentiment Marché Global (contexte)

| Indicateur | Source | Seuil d'alerte |
|------------|--------|----------------|
| VIX | `indexes` | > 25 = peur, > 35 = capitulation |
| Put/Call ratio S&P | `indexes` | > 1.2 = peur extrême, < 0.7 = euphorie |
| Performance S&P vs NASDAQ | `marketPerformance` | Rotation risk-on / risk-off |
| Fear & Greed Index (proxy) | Composite | < 25 = Extreme Fear, > 75 = Extreme Greed |

---

## Format de sortie — Bloc Sentiment

> Ce bloc est inséré dans chaque `_init.md` et `_update.md`.

```markdown
## Analyse Sentiment [Agent Sentiment — YYYY-MM-DD]

### Analystes Wall Street
| Consensus | Buy | Hold | Sell | Prix cible médian | Upside implicite |
|-----------|-----|------|------|-------------------|-----------------|
| Positif / Neutre / Négatif | XX% | XX% | XX% | $XXX | +/-XX% |

**Mouvements récents (30j) :** X upgrades / X downgrades
**Révision prix cible moyen :** +/-XX% ce mois

### Insiders
| Période | Achats | Ventes | Signal |
|---------|--------|--------|--------|
| 3 mois | $XXXk (X personnes) | $XXXk (X personnes) | 🟢 Net acheteur / 🔴 Net vendeur / ⚪ Neutre |

**Signal notable :** [ex : PDG a acheté $500k le 2026-05-03]

### Short Interest
| % Float | Days to Cover | Variation 2 sem. | Risque Squeeze |
|---------|---------------|-----------------|----------------|
| XX% | Xj | +/-X% | Oui / Non |

### Options Flow (niveau du titre)
| Put/Call ratio | IV 30j | HV 30j | IV Rank | Max Pain | Call Wall | Put Wall | GEX | Signal |
|---------------|--------|--------|---------|---------|-----------|---------|-----|--------|
| X.X | XX% | XX% | XX% | $XXX | $XXX | $XXX | Pos/Neg | Peur / Normal / Complacence |

**Unusual Options Activity :** [Oui — X calls $XXX strike exp. XX/XX · Volume Xk vs OI XXX / Non]

### Earnings Whisper (si dans < 30 jours)
| Consensus EPS | Whisper EPS | Écart | Historique beat | Réaction moy. post-earnings |
|--------------|------------|-------|----------------|----------------------------|
| $X.XX | $X.XX | +/-X% | XX% | +/-X% |

### News & Médias (7 derniers jours)
| Volume | Tonalité dominante | Événement majeur |
|--------|--------------------|-----------------|
| X articles | Positive / Neutre / Négative | ... |

### Transactions politiques (si pertinent)
- [Sénateur X] a acheté $XXXk le YYYY-MM-DD

### Contexte marché global
| VIX | Sentiment global | Phase de marché |
|-----|-----------------|-----------------|
| XX | Fear / Neutral / Greed | Risk-on / Risk-off / Indécis |

### Verdict Sentiment
**Score Catalyseur /10 :** X/10
**Sentiment dominant :** 🟢 Très positif / 🟡 Mixte / 🔴 Négatif
**Signal le plus fort :** [ex : cluster buying insiders + 3 upgrades analystes + IV/HV comprimée]
**Risque sentiment :** [ex : short interest élevé → attention aux reprises violentes / IV >> HV → gap potentiel]

### HANDOFF → Agent Fondamental & Synthèse
> `Score Catalyseur : X/10 | Sentiment : Positif/Mixte/Négatif | Short interest : XX% (Squeeze potentiel : Oui/Non) | IV vs HV : +/-X pts (Nerveux/Normal/Complacent) | Analystes : X Buy/X Hold/X Sell | Insiders : Net acheteur/vendeur/neutre | VIX : XX (Risk-on/off)`
```

---

## Cas spéciaux — Signaux à fort potentiel

### Short Squeeze Setup
**Conditions :** Short interest > 15% float + Days to cover > 7j + Catalyseur positif
**Action :** Alerter dans le bulletin + majorer le score Catalyseur de +2 pts

### Cluster Buying Insiders
**Conditions :** ≥ 3 insiders achètent dans une fenêtre de 30 jours
**Action :** Alerter immédiatement, souvent précurseur d'une hausse à 3-6 mois

### Divergence Analystes / Cours
**Conditions :** Consensus > 80% Buy mais cours en baisse de > 20%
**Action :** Signal contrarian fort — creuser le pourquoi (marché voit un risque non pricé ?)

### Capitulation (VIX > 35 + sentiment extrême négatif)
**Conditions :** VIX > 35 + news très négatives + cours sur support fort
**Action :** Opportunité contrarian — noter dans le rapport Opportunités

---

## Scoring Catalyseur pour le rapport Opportunités

| Fourchette score | Interprétation |
|-----------------|----------------|
| 9–10 | Catalyseur majeur (FDA approval, M&A, earnings beat + raise) + sentiment très positif |
| 7–8 | Bon catalyseur (upgrade, bon earnings, macro favorable) + sentiment positif |
| 5–6 | Catalyseur modéré ou sentiment mixte |
| 3–4 | Pas de catalyseur clair ou sentiment légèrement négatif |
| 1–2 | Catalyseur négatif ou sentiment très négatif |

**Calcul score :**
- Qualité du catalyseur actualité : 0–3 pts
- Consensus analystes (upgrades/downgrades + dispersion) : 0–2 pts
- Insiders (direction des transactions + cluster buying) : 0–2 pts
- Short interest (risque ou potentiel squeeze) : 0–1 pt
- Options flow (put/call ratio + IV vs HV) : 0–1 pt
- Sentiment marché global (VIX, risk-on/off) : 0–1 pt

**Bonus/malus options :**
- IV << HV + put/call < 0.7 + catalyseur positif → +0.5 pt (le marché est serein, l'opportunité est sous-radar)
- IV >> HV de > 15 pts sans catalyseur identifiable → −0.5 pt (risque de news négative non publique)

---

## Alertes automatiques générées par cet agent

| Condition | Alerte déclenchée |
|-----------|------------------|
| Upgrade ou downgrade inattendu | Notifier dans bulletin + `_update.md` |
| Achat insider > $500k | Notifier dans bulletin + section "Signaux forts" |
| Short interest dépasse 20% float | Notifier dans bulletin + surveiller pour squeeze |
| VIX dépasse 30 | Avertissement global dans le bulletin |
| Volume news × 3 en une journée | Vérifier s'il y a un événement non couvert |

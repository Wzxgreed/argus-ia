# Agent FX Exposure

**Rôle :** Mesurer l'exposition de chaque ticker aux fluctuations de change (USD, EUR, JPY, CNY) et chiffrer l'impact estimé sur les revenus, les marges et la valorisation. L'Agent Macro regarde le DXY en agrégé ; cet agent traduit le mouvement FX en impact micro par action.

**Déclenché par :**
- Workflow du matin — après l'Agent Macro (régime DXY déjà identifié)
- Création d'une analyse initiale (`_init.md`) — pour les tickers multinationaux
- Commande manuelle : `Quelle est l'exposition FX de [TICKER] ?`
- Franchissement d'un seuil DXY critique (> +2% semaine) — scan automatique de toute la watchlist

**Coopère avec :**
- → Agent Macro : reçoit le régime DXY et la tendance USD
- → Agent Fondamental : fournit l'ajustement EPS/Revenus lié au FX pour le DCF et les comps
- → Agent Sentiment : ajuste le Score Catalyseur si le FX crée un headwind/tailwind non pricé
- → Opportunités : ajuste le score Valorisation si le FX amplifie ou réduit le discount vs pairs

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `fmp_key_metrics` | Revenus géographiques (% US / Europe / Asie / Amériques) |
| `fmp_ratios` | Marges brutes/nettes, ROIC — base pour estimer l'impact marge |
| `company` | Description activité, supply chain géo, usines localisées |
| `secFilings` (10-K) | Segment revenues by geography, discussion FX risk dans Risk Factors |
| `forex` | DXY, EUR/USD, USD/JPY, USD/CNY — tendances 30j/90j/1 an |
| `earningsTranscript` | Mentions "FX headwind", "currency translation", "natural hedge" |
| `quote` | Cours localisés (ADR, listings secondaires) pour vérifier divergences |

---

## Métriques analysées

### 1. Cartographie de l'exposition FX par ticker

> Objectif : estimer le % du CA et du bénéfice exposé à chaque devise.

| Donnée | Source | Méthode de calcul |
|--------|--------|-------------------|
| **% Revenus hors-USD** | 10-K / `fmp_key_metrics` | Somme segments géo non-US / CA total |
| **Devise principale d'exposition** | 10-K Risk Factors | Mentionnée explicitement (ex : EUR, CNY, JPY, MXN) |
| **Sensibilité directionnelle** | Analyse métier | Exportateur US = bénéficie d'un USD faible · Importateur = pénalisé |
| **Natural hedge** | 10-K / Transcript | A-t-il des coûts dans la même devise que ses revenus ? (ex : production locale en Europe) |
| **Hedge comptable** | 10-K | Utilise-t-il des forwards/options ? Quelle couverture % ? |

**Classification automatique :**
```
Exposition Élevée  → > 50% revenus hors-USD + pas de natural hedge
Exposition Modérée → 20-50% revenus hors-USD + partial hedge
Exposition Faible   → < 20% revenus hors-USD ou natural hedge complet
Exposition Inverse  → Bénéficiaire d'un USD fort (ex : importateur US pur)
```

### 2. Impact estimé sur les revenus et les EPS

**Méthode de calcul simplifiée (utilisée dans `_init.md`) :**
```
Impact revenus estimé (%) = Δ devise clé vs USD (12 mois) × % revenus exposés × (1 - couverture hedge)
Impact EPS estimé (%)     = Impact revenus × operating leverage (β bénéfice ≈ 1.5× revenus)
```

| Ticker type | DXY +1% → impact revenus | DXY +1% → impact EPS | Source de vérité |
|-------------|--------------------------|----------------------|-------------------|
| Multinationale tech (AAPL, MSFT) | −2 à −4% | −3 à −6% | 10-K segment geo + guidance calls |
| Exportateur industriel (CAT, DE) | −3 à −5% | −4 à −8% | 10-K + transcript |
| Pharma / Healthcare (JNJ, LLY) | −1 à −2% | −1.5 à −3% | 10-K + hedge actif |
| Miner / Matière première (FCX) | +2 à +4% (USD denom.) | +3 à +6% | Prix matières en USD |
| Domestic pur (WMT US, UNH) | ~0% | ~0% | Pas d'exposition |
| Crypto-exposé (IREN) | Négligeable | Négligeable | Coûts en CAD, revenus en BTC |

> **Règle :** Si la donnée géographique n'est pas disponible dans `fmp_key_metrics`, marquer `[DONNÉES PARTIELLES — FX]` et utiliser l'estimation sectorielle par défaut.

### 3. Divergence FX / Cours — Détection d'anomalie

| Condition | Signal | Interprétation |
|-----------|--------|----------------|
| DXY baisse fortement (−2% semaine) + cours baisse quand même | 🔴 Anomalie | Le marché pense que l'entreprise est pénalisée au-delà du FX (concurrence, guidance cut) |
| DXY hausse fortement (+2% semaine) + cours hausse quand même | 🟢 Surperformance | La société dépasse le headwind FX — force intrinsèque |
| Cours réagit exactement comme prévu par le modèle FX | ⚪ Aligné | Le FX est le driver dominant — rien d'autre à chercher |
| Cours baisse PLUS que le modèle FX prédit | 🔴 Risque additionnel | Autre risque non pricé (guidance, concurrence, réglementaire) |
| Cours baisse MOINS que le modèle FX prédit | 🟢 Résilience | Management a hedge efficace ou natural hedge sous-estimé |

**Format de détection dans le bulletin :**
```markdown
### Divergence FX / Cours — [TICKER]
| Driver | Prédiction modèle FX | Réalité cours | Écart | Interprétation |
|--------|---------------------|--------------|-------|----------------|
| DXY −2% | +3% attendu | +1% réel | −2% | 🔴 Sous-performance — chercher autre facteur |
```

### 4. Hedge comptable et natural hedge

> Un ticker avec 60% de revenus en EUR mais 50% de coûts en EUR a une exposition NETTE de 10% — pas 60%.

| Élément | Source | Impact sur l'exposition nette |
|---------|--------|------------------------------|
| Production locale à l'étranger | 10-K / Transcript | Réduit l'exposition (coûts et revenus dans la même devise) |
| Forward contracts / options | 10-K (Note dérivés) | Réduit l'exposition à hauteur de la couverture |
| Dette en devise étrangère | Bilan | Peut créer un natural hedge inverse (ex : dette EUR vs revenus EUR) |
| Cash holdings étrangers | Bilan | Translation risk — pas d'impact P&L tant que non rapatrié |

**Règle de calcul de l'exposition nette :**
```
Exposition nette = Revenus étrangers − Coûts étrangers − Couverture hedge (% revenus)
```

### 5. Cadrage par devise — Secteurs et tickers sensibles

| Devise | Tendance DXY | Secteurs gagnants | Secteurs perdants | Tickers watchlist typiques |
|--------|-----------|-------------------|-------------------|---------------------------|
| **EUR** | DXY ↓ (EUR/USD ↑) | Exportateurs US en Europe, Tourism | Importateurs US depuis Europe, REITs EU | AAPL, MSFT, PG (ventes EU) |
| **CNY** | DXY ↓ (USD/CNY ↓) | Commodités, Miners | Tech US en Chine, Industriels | AAPL (ventes CN), NVDA (ventes CN) |
| **JPY** | DXY ↓ (USD/JPY ↓) | Automobilistes US, Importateurs US | Exportateurs Japon en US | TM, HMC (si dans watchlist) |
| **MXN / CAD** | DXY ↓ | Énergie (pétrole en USD), Agro | Manufacturiers US au Mexique | XLE, CVX |

---

## Format de sortie — Bloc FX Exposure

> Ce bloc est inséré dans chaque `_init.md` et `_update.md` pour les tickers multinationaux. Pour les domestiques purs, le bloc est optionnel (marquer "Exposition FX négligeable").

```markdown
## Exposition FX [Agent FX — YYYY-MM-DD]

### Cartographie de l'exposition
| Zone géographique | % CA | Devise | Sensibilité | Hedge / Natural hedge |
|-------------------|------|--------|-------------|----------------------|
| États-Unis | XX% | USD | — | — |
| Europe | XX% | EUR | Exportateur → baisse EUR pénalise | Forward 50% couverture |
| Asie-Pacifique | XX% | CNY/JPY | Exportateur → baisse CNY pénalise | Production locale CN (natural hedge partiel) |
| Amériques | XX% | MXN/CAD | Neutre | — |

**Exposition nette estimée :** XX% du CA (après hedge et natural hedge)
**Classification :** Exposition Élevée / Modérée / Faible / Inverse

### Impact macro actuel
| Devise | Tendance 30j | Tendance 90j | Impact revenus estimé | Impact EPS estimé |
|--------|-------------|-------------|----------------------|-------------------|
| EUR/USD | +/−X% | +/−X% | +/−X% | +/−X% |
| USD/CNY | +/−X% | +/−X% | +/−X% | +/−X% |
| DXY | +/−X% | +/−X% | — | — |

### Divergence FX / Cours
| Prédiction modèle FX | Réalité cours (7j) | Écart | Interprétation |
|---------------------|-------------------|-------|----------------|
| +X% attendu | +Y% réel | X−Y% | Aligné / Surperformance / Sous-performance |

**Signal :** [Ex : Le titre sous-performe de 3% vs le modèle FX → autre facteur négatif en cours]

### Verdict FX
**Score FX Impact /10 :** X/10 (0 = pas d'exposition, 10 = exposition massive + headwind actif)
**Direction :** 🟢 Tailwind (USD faible ou hedge efficace) / 🟡 Neutre / 🔴 Headwind (USD fort + exposition nette)
**Ajustement Score Fondamental :** +/−X% sur les estimations EPS NTM
**Ajustement Score Valorisation :** +/−X pt si le FX n'est pas pricé par le marché

### HANDOFF → Agent Fondamental & Sentiment
> `FX Impact : X/10 | Exposition nette : XX% | Headwind/Tailwind : [headwind/tailwind/neutre] | DXY trend : [hausse/baisse/stable] | Divergence cours : [oui/non] | Ajustement EPS : +/−X%`
```

---

## Alertes automatiques générées par cet agent

| Condition | Alerte déclenchée | Action |
|-----------|------------------|--------|
| DXY bouge > +/−2% en une semaine | 🟡 Alerte FX globale | Scanner toute la watchlist pour exposition élevée |
| Ticker avec exposition élevée + DXY dans la direction défavorable | 🔴 Headwind FX actif | Noter dans `_update.md` + ajuster prix cible |
| Divergence cours vs modèle FX > 5% | 🟡 Anomalie | Déclencher analyse approfondie (_update.md flash) |
| Management mentionne "FX headwind" dans transcript récent | 🟡 Signal qualitatif | Vérifier si déjà pricé par le marché |
| Hedge comptable expire dans < 90j | 🟡 Risque de rollover | Mentionner dans le bulletin si exposition élevée |
| Ticker bénéficiaire de DXY fort (importateur pur) + DXY > 105 | 🟢 Opportunité FX | Survaloriser dans le scoring |

---

## Scoring FX Impact et ajustements du Score Opportunité

L'agent produit un **Score FX Impact /10** qui est utilisé comme bonus/malus sur le Score Fondamental et le Score Valorisation.

**Calcul du Score FX Impact :**
| Facteur | Pondération | Échelle |
|---------|------------|---------|
| % revenus exposés (net, post-hedge) | 40% | 0–10 (0% = 0, >60% = 10) |
| Amplitude du mouvement FX (30j vs 90j trend) | 30% | 0–10 (stable = 0, >5% = 10) |
| Direction (headwind vs tailwind vs neutre) | 20% | Headwind = 10, Neutre = 5, Tailwind = 0 |
| Divergence cours / modèle FX | 10% | Anomalie négative = +3, Anomalie positive = −3 |

> **Règle :** Score FX Impact élevé = mauvais (exposition + headwind). Score bas = bon (peu d'exposition ou tailwind).

**Ajustements sur le Score Opportunité :**
| Condition | Ajustement | Justification |
|-----------|-----------|---------------|
| Exposition élevée + DXY headwind actif + non pricé | −1 pt Score Fondamental | EPS NTM sur-estimé par le consensus |
| Exposition élevée + DXY tailwind actif + non pricé | +0.5 pt Score Valorisation | EPS sous-estimé, upside caché |
| Divergence cours vs modèle < −5% (sous-performance) | −0.5 pt Score Catalyseur | Marché détecte un risque additionnel |
| Divergence cours vs modèle > +5% (surperformance) | +0.5 pt Score Catalyseur | Force intrinsèque malgré le FX |
| Exposition faible + DXY volatile | 0 pt | Pas d'impact significatif |

---

## Cas spéciaux — Protocoles avancés

### 1. Currency Crisis — Dépassement des seuils normaux
**Conditions :** Devise émergente (CNY, MXN, TRY, ARS) perd > 10% en 30j.
**Action :** Identifier les tickers avec exposition à cette devise → `_update.md` flash avec scénarios de stress.

### 2. Paradoxe du Yen Carry Trade Unwind
**Conditions :** USD/JPY baisse rapidement (< −3% semaine) alors que DXY stable.
**Action :** Alerter sur les tickers japonais et les hedge funds à levier. Impact indirect sur la volatilité globale.

### 3. Hedging Cost Spike
**Conditions :** Coût des forwards/options FX devient prohibitif (ex : pré-FOMC).
**Action :** Si une entreprise annonce réduire son hedge → exposition nette augmente mécaniquement → re-scorer.

### 4. Repatriation Tax / Regulatory FX
**Conditions :** Changement de réglementation sur le rapatriement de cash étranger (ex : réforme fiscale US).
**Action :** Impact sur la valorisation (cash trapped vs cash disponible) — ajuster le DCF.

---

## Intégration dans le workflow du matin

```
ÉTAPE 1 — Agent Macro produit le régime DXY et la tendance des devises
ÉTAPE 2 — Agent FX lit le régime DXY + `data/latest.json` (forex)
ÉTAPE 3 — Pour chaque ticker de la watchlist avec exposition géo connue :
         → Calculer l'exposition nette
         → Estimer l'impact revenus/EPS
         → Détecter divergence cours / modèle FX
         → Produire le Bloc FX (si exposition > Faible)
ÉTAPE 4 — Transmettre ajustements à l'Agent Fondamental (EPS) et Sentiment (Catalyseur)
```

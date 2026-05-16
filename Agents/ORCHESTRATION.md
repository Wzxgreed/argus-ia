# Orchestration des agents

Ce fichier décrit comment les agents (Macro, Flux, Supply Chain, Technique, Fondamental, Sentiment) s'articulent selon chaque type d'analyse.

---

## Vue d'ensemble

```
                    ┌─────────────────────────────┐
                    │     COMMANDE UTILISATEUR     │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  ÉTAPE 0 — MÉMOIRE (ABSOLU)  │
                    │  Lire APPRENTISSAGES.md       │
                    │  Clôturer fenêtres BACKTEST   │
                    │  + SUIVI_PRIX_CIBLES.md       │
                    │  + SUIVI_EARNINGS_PRED.md     │
                    │  Post-mortem si Miss détecté  │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                                         │
     ┌────────▼────────┐                    ┌───────────▼──────────┐
     │   AGENT MACRO   │                    │     AGENT FLUX       │
     │  (s'exécute 1er)│                    │  (en parallèle Macro)│
     │                 │                    │                      │
     │ • Régime macro  │                    │ • Flux 13F           │
     │ • Banques cent. │                    │ • Flux ETF           │
     │ • Courbe taux   │                    │ • Short / borrow     │
     │ • DXY / VIX     │                    │ • Dark pool / blocs  │
     │ • Calendrier éco│                    │ • Max pain / GEX     │
     └────────┬────────┘                    └───────────┬──────────┘
              │ Régime + Pondération                    │ Bonus/malus Catalyseur
              │                                         │
              └──────────────────┬──────────────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │   AGENT SUPPLY CHAIN      │
                    │  (scan quotidien matin)   │
                    │                           │
                    │ • Fournisseurs 🔴🟡 watchlist│
                    │ • Clients critiques        │
                    │ • Matières premières       │
                    │ • Alertes supply chain     │
                    └────────────┬──────────────┘
                                 │ Signaux avancés (1-3 trimestres)
                                 │ Bonus/malus Catalyseur
                                 │
              ┌──────────────────┼──────────────────────┐
              │                  │                       │
     ┌────────▼────────┐ ┌───────▼────────┐  ┌──────────▼───────┐
     │ AGENT FONDAMENTAL│ │ AGENT TECHNIQUE│  │ AGENT SENTIMENT  │
     │                  │ │                │  │                  │
     │ • Résultats fin. │ │ • RSI, MACD,MM │  │ • News & médias  │
     │ • Ratios & DCF   │ │ • Force relative│  │ • Analystes (TP) │
     │ • Secteur & Comps│ │ • Saisonnalité │  │ • Insiders       │
     │ • NLP transcript │ │ • Volumes      │  │ • Options flow   │
     │ • Qualité bénéf. │ │ • Supports/Rés.│  │ • Job postings   │
     └────────┬─────────┘ └───────┬────────┘  └──────────┬───────┘
              │                   │                       │
              │ Prix cible        │ Score Momentum        │ Score Catalyseur
              │ Score Val /10     │ +RS +Seasonality      │ +Track record TP
              │ +Confiance Mgmt   │                       │ +Job postings signal
              │                   │                       │
              └───────────────────┼───────────────────────┘
                                  │
                   ┌──────────────▼──────────────┐
                   │        SYNTHÈSE FINALE        │
                   │  Score Opportunité /10 :      │
                   │  (pondération du régime Macro)│
                   │  Catalyseur×XX% + Val×XX%     │
                   │  + Momentum×XX%               │
                   │  + bonus/malus Macro & Flux    │
                   │  + bonus/malus Supply Chain    │
                   └──────────────┬──────────────┘
                                  │
              ┌───────────────────┼────────────────────┐
              │                   │                    │
   ┌──────────▼───────┐ ┌────────▼────────┐ ┌─────────▼────────┐
   │  Actions/[TICK]/ │ │ Actualités/     │ │  Opportunités/   │
   │  _update.md      │ │ YYYY-MM-DD.md   │ │  YYYY-MM-DD.md   │
   │  SUPPLY_CHAIN.md │ │                 │ │                  │
   └──────────────────┘ └─────────────────┘ └──────────────────┘
                                                       │
                                           ┌───────────▼──────────┐
                                           │  BACKTESTING.md      │
                                           │  SUIVI_PRIX_CIBLES   │
                                           │  SUIVI_EARNINGS_PRED │
                                           └──────────────────────┘
```

---

## Séquence par type d'analyse

### Analyse initiale d'une action

| Ordre | Agent | Ce qu'il produit | Passe à |
|-------|-------|-----------------|---------|
| 1 | **Macro** | Régime actif + pondération + carte d'exposition sectorielle | → Tous les agents |
| 2 | **Flux** | Positionnement 13F, flux ETF, short/borrow, max pain | → Sentiment (bonus Catalyseur) |
| 3 | **Supply Chain** | Cartographie fournisseurs/clients (10-K) + scoring criticité + `SUPPLY_CHAIN.md` | → Fondamental (risques marges) + Sentiment (signaux avancés) |
| 4 | **Fondamental** | Filtre Qualité + Thèse + Valorisation + DCF + NLP transcript + prix cible | → Technique (prix cible) |
| 5 | **Technique** | Tendance + Force relative + Saisonnalité + Timing | → Sentiment (short interest) |
| 6 | **Sentiment** | Analystes (track record) + Insiders + Options flow complet + Job postings signal | → Synthèse |
| 7 | Synthèse | `_init.md` complet avec tous les blocs + sizing recommandé | → INDEX.md + SUIVI_PRIX_CIBLES.md |

---

### Bulletin du matin

| Ordre | Agent | Périmètre | Ce qu'il produit |
|-------|-------|-----------|-----------------|
| 0 | **Mémoire** | APPRENTISSAGES.md + 3 fichiers de suivi | Règles actives chargées + verdicts J+5/20/60/30/90/180 + post-mortems si Miss |
| 1 | **Macro** | Monde entier | Régime actif, pondération du jour, alertes macro, calendrier éco 7j |
| 2 | **Flux** | Watchlist | Flux ETF, dark pool, short interest evolution, gamma/max pain |
| 3 | **Supply Chain** | Watchlist (entités 🔴🟡 de chaque SUPPLY_CHAIN.md) | News du jour sur fournisseurs/clients critiques + alertes si earnings publiés |
| 4 | **Sentiment** | Monde entier | News mondiales classées, VIX, sentiment macro, unusual options |
| 5 | **Fondamental** | Tickers watchlist touchés | Révisions d'estimations si earnings ou actu majeure + NLP si transcript dispo |
| 6 | **Technique** | Tickers watchlist | Cours ouverture, variations, signaux techniques, force relative |
| 7 | Synthèse | Tous tickers scorés | Rapport Opportunités + Bulletin + `_update.md` + enregistrement BACKTESTING |

> **Étape 0 est non-négociable.** Si un post-mortem est déclenché, il est traité AVANT le workflow du jour — une erreur non comprise sera répétée.
> Le Macro passe en premier parmi les agents. Le Flux en second pour les signaux cachés. Le Supply Chain en troisième pour les signaux avancés (1-3 trimestres).

---

### Détection d'une actualité impactante

| Condition | Agents déclenchés | Livrable |
|-----------|------------------|----------|
| News macro mondiale (taux, GDP, guerre) | Sentiment → Fondamental → Technique | `_update.md` pour chaque ticker exposé |
| Earnings d'un concurrent | Fondamental → Sentiment | `_update.md` avec révision comps |
| Upgrade / Downgrade analyste | Sentiment → Technique | Note dans INDEX.md + alerte si impact > 5% |
| Volume anormal (>2x) | Technique → Sentiment | Vérification croisée : actu cachée ? insider ? |
| Franchissement d'un seuil d'alerte | Technique → tous | `_update.md` complet + notification bulletin |

---

### Filtre Qualité — Pré-étape obligatoire

> Le Filtre Qualité est exécuté **avant** le calcul du score Opportunité, dans la phase Fondamentale.
> Il conditionne le score maximal atteignable et la nature de la recommandation.

```
ORDRE D'EXÉCUTION :
1. Agent Sentiment  → Régime marché + Score Catalyseur
2. Agent Fondamental → [FILTRE QUALITÉ EN PREMIER] → Score Valorisation
3. Agent Technique  → Score Momentum
4. Synthèse         → Score final (avec pondération du régime actif)
```

### Impact du Filtre Qualité sur le score final

| Score Qualité | Label | Score Val. max | Recommandation possible |
|---------------|-------|----------------|------------------------|
| 5–6 / 6 | ✅ Quality Compounder | 10/10 | Toutes (Achat long terme, renforcement, etc.) |
| 4 / 6 | ⚠️ Quality Partielle | 8/10 | Achat avec conviction modérée · position sizing réduite |
| ≤ 3 / 6 | 🔴 Hors périmètre | 5/10 | Trade court terme uniquement · pas de position de fond |

### Règle d'affichage dans le rapport Opportunités

- **Quality Compounder** → afficher badge ✅ à côté du ticker
- **Quality Partielle** → afficher ⚠️ et préciser le(s) critère(s) manquant(s)
- **Hors périmètre** → afficher 🔴 et ajouter : *"Trade spéculatif uniquement — hors périmètre qualité long terme"*

---

## Score Opportunité — Contribution de chaque agent

```
Score Final /10 =

  Agent Sentiment  →  Score Catalyseur  × 40%
  Agent Fondamental → Score Valorisation × 35%
  Agent Technique  →  Score Momentum    × 25%
```

**Règle de seuil :** Une opportunité n'est publiée dans le rapport que si :
- Score Final ≥ 6/10 **ET**
- Aucun des 3 scores individuels n'est ≤ 2/10

**Règle Filtre Qualité :** Vérifier le Score Qualité (lu dans le Handoff Fondamental) avant publication :
- Score Qualité ≤ 3/6 → Score Valorisation plafonné à 5/10 → recalculer le score final
- Afficher le badge qualité (✅ / ⚠️ / 🔴) dans le rapport Opportunités

**Règle de conflit :** Appliquer systématiquement le protocole de la section "Gestion des conflits" avant de publier.

**Régime actif :** Lire dans le Handoff Package du Sentiment. Appliquer la pondération correspondante.

---

## Gestion des conflits entre agents

Quand les scores des 3 agents divergent, appliquer les règles suivantes avant de calculer le score final.

### Conflits fréquents et protocoles

| Conflit | Configuration | Protocole |
|---------|--------------|-----------|
| Fondamental élevé / Technique bas | Val ≥ 7 · Momentum ≤ 4 | "Value trap potentiel" — ne pas entrer maintenant. Flag dans INDEX.md : *"Attendre confirmation technique : cours doit repasser au-dessus de MM50 ou RSI > 45"* |
| Sentiment élevé / Fondamental bas | Catalyseur ≥ 7 · Valorisation ≤ 4 | "Catalyseur spéculatif" — horizon court terme uniquement. Mentionner dans le rapport Opportunités : *"Trade de sentiment, pas de thèse fondamentale solide. Dimensionner la position en conséquence."* |
| Technique élevé / Sentiment bas | Momentum ≥ 7 · Catalyseur ≤ 4 | "Breakout technique sans conviction" — volume à surveiller. Si volume > 2x ET short interest élevé → potentiel short squeeze, conserver. Sinon → prudence, risque de faux breakout. |
| Tous élevés sauf Fondamental | Val ≤ 3 | ❌ Disqualification automatique (règle du score ≤ 2 étendue à ≤ 3 si les deux autres sont ≥ 8) — risque de piège spéculatif sur action fondamentalement chère |
| Conflit mineur (écart ≤ 2 pts) | Tous dans 4–8 | Calculer normalement. Mentionner l'axe le plus faible dans la note de risque. |

### Formulation dans les fichiers en cas de conflit
> Ajouter un encadré `⚠️ CONFLIT D'AGENTS` dans le bloc Synthèse du fichier concerné, avec le protocole appliqué et la condition de résolution.

---

## Pondération dynamique selon le régime de marché

Le score final n'est pas toujours (40% / 35% / 25%). L'Agent Sentiment détermine le régime en début d'analyse via le VIX et le contexte macro.

### Régimes de pondération

| Régime | Condition | Catalyseur | Valorisation | Momentum | Logique |
|--------|-----------|------------|--------------|----------|---------|
| **Normal** | VIX 15–25, marché stable | 40% | 35% | 25% | Équilibre standard |
| **Risk-off** | VIX > 25 ou contexte macro dégradé | 30% | 45% | 25% | La qualité du bilan prime, les catalyseurs spéculatifs comptent moins |
| **Risk-on / Bull** | VIX < 15, marché euphorique | 40% | 25% | 35% | Le momentum porte plus loin, la valorisation est moins discriminante |
| **Pré-earnings** | Earnings dans ≤ 5 jours | 50% | 30% | 20% | Le catalyseur (surprise/déception earnings) domine tout |

**Règle :** L'Agent Macro annonce le régime en tête de son Handoff Package. Ce régime s'applique au calcul du score final.

> Exemple : VIX = 32 → Régime Risk-off → Score = (Catalyseur×30%) + (Valorisation×45%) + (Momentum×25%)

---

## Boucle d'apprentissage — Flux post-mortem

```
Miss détecté dans BACKTESTING.md
         │
         ▼
Lire fichier source du signal
Actions/[TICKER]/[TICKER]_YYYY-MM-DD_[type].md
         │
         ▼
Récupérer cours day-by-day + news période (`quote` + `news`)
         │
         ▼
Identifier l'événement déclencheur de la baisse
         │
         ▼
Diagnostiquer l'agent responsable de l'erreur
(Macro / Flux / Technique / Fondamental / Sentiment)
         │
         ▼
Extraire UNE règle corrective universelle
         │
         ├──► Écrire post-mortem dans Agents/APPRENTISSAGES.md
         ├──► Ajouter règle dans "Règles actives"
         ├──► Mettre à jour Track Record analyste si applicable
         └──► Mettre à jour colonne "Post-mortem" dans BACKTESTING.md
```

**Règle de non-surapprentissage :**
- 1 occurrence → règle "Faible confiance" (noter mais ne pas appliquer automatiquement)
- 2-3 occurrences → règle "Moyenne confiance" (appliquer avec malus modéré)
- 4+ occurrences cohérentes → règle "Forte confiance" (appliquer systématiquement)

---

## Flux d'informations entre agents

| Information | De | Vers | Usage |
|-------------|-----|------|-------|
| Régime macro + pondération | **Macro** | Tous | Calibrer les poids du score final |
| Carte exposition sectorielle | **Macro** | Fondamental | Chiffrer l'impact macro sur les revenus |
| Alerte macro (FOMC, CPI) | **Macro** | Sentiment | Anticiper la volatilité |
| Flux 13F + ETF | **Flux** | Sentiment | Enrichir le score Catalyseur (+/- pts) |
| Max pain + GEX | **Flux** | Technique | Niveaux de support/résistance options |
| Short interest + borrow rate | **Flux** | Technique + Sentiment | Squeeze setup + explication volumes |
| Fournisseur critique : pénurie/fermeture | **Supply Chain** | Fondamental | Réviser marges + timeline produit |
| Client critique : profits warning | **Supply Chain** | Fondamental + Sentiment | Réviser revenus forward + Score Catalyseur −1.5pt |
| Client critique : guidance en hausse | **Supply Chain** | Sentiment | Score Catalyseur +1pt |
| Nouveau client majeur (>10% CA potentiel) | **Supply Chain** | Fondamental + Sentiment | Score Catalyseur +2pt |
| Rupture géopolitique zone production | **Supply Chain** | Macro + Sentiment | Score Catalyseur −2pt |
| NLP transcript — Score Confiance Mgmt | **Fondamental** | Synthèse | ±0.5 à ±1pt sur Score Valorisation |
| Job postings signal (6-12 mois) | **Sentiment** | Fondamental | Signal avancé revenus / coûts |
| Prix cible fondamental | **Fondamental** | Technique | Calcul de l'upside technique (cours vs cible) |
| Court terme vs support | **Technique** | Fondamental | Pondérer le timing dans la thèse |
| Révisions analystes (track record) | **Sentiment** | Fondamental | Recalibrer les estimations de consensus |
| Catalyseur news | **Sentiment** | Fondamental + Technique | Déclencher une mise à jour des deux |
| Score RSI extrême | **Technique** | Sentiment | Chercher confirmation dans les flux (short squeeze ?) |
| Force relative | **Technique** | Opportunités | Signal de leader/retardataire pour le classement |
| Unusual options activity | **Sentiment** | Flux | Croiser avec dark pool pour confirmer |

---

## Commandes par agent

| Commande | Agent(s) déclenché(s) |
|----------|-----------------------|
| `Analyse technique de [TICKER]` | Technique seul |
| `Analyse fondamentale de [TICKER]` | Fondamental seul |
| `Analyse sentiment de [TICKER]` | Sentiment seul |
| `Analyse flux de [TICKER]` | Flux seul |
| `Quel est le régime macro actuel ?` | Macro seul |
| `Analyse la supply chain de [TICKER]` | Supply Chain → crée/met à jour SUPPLY_CHAIN.md |
| `Quels fournisseurs de [TICKER] ont publié des news aujourd'hui ?` | Supply Chain → `news` sur entités critiques |
| `Analyse le ton management de [TICKER] sur les derniers calls` | Fondamental (NLP transcript) |
| `Analyse les offres d'emploi de [TICKER] — signal avancé` | Sentiment (job postings) |
| `Analyse complète de [TICKER]` | Macro → Flux → Supply Chain → Fondamental → Technique → Sentiment → Synthèse |
| `Lance le bulletin du matin` | Macro → Flux → Supply Chain → Sentiment → Fondamental → Technique → Synthèse |
| `Quelles opportunités aujourd'hui ?` | Macro → Flux → Supply Chain → Sentiment → Technique → Score → Rapport |
| `[TICKER] a une news, quel impact ?` | Sentiment → Fondamental → Technique |
| `Analyse le risque de mon portefeuille` | Macro + MODULE_RISQUE_PORTEFEUILLE |
| `Quel sizing pour [TICKER] ?` | MODULE_SIZING (lit ATR du Technique + Score du Fondamental) |
| `Suivi des signaux backtesting` | BACKTESTING.md + `quote` (cours actuels) |
| `Suivi des prix cibles` | SUIVI_PRIX_CIBLES.md + `quote` (cours actuels) |
| `Suivi des prédictions earnings` | SUIVI_EARNINGS_PREDICTIONS.md + résultats réels |

---

## Modules d'analyse avancée

### Agent Supply Chain — [Agents/AGENT_SUPPLY_CHAIN.md](Agents/AGENT_SUPPLY_CHAIN.md)

Cartographie les dépendances critiques (fournisseurs + clients) pour chaque ticker et les surveille en continu. Détecte les risques **1 à 3 trimestres avant** qu'ils apparaissent dans les résultats financiers.

**Fichiers produits :** `Actions/[TICKER]/SUPPLY_CHAIN.md` (créé à l'init, mis à jour à chaque signal)

**Intégration dans le scoring :**

| Signal détecté | Ajustement Score |
|---------------|-----------------|
| Nouveau client majeur (>10% CA potentiel) | +2 pt Catalyseur |
| Client critique : guidance en forte hausse | +1 pt Catalyseur |
| Client critique mentionne ticker positivement | +1.5 pt Catalyseur |
| Client critique : profits warning | −1.5 pt Catalyseur |
| Fournisseur critique : pénurie ou fermeture usine | −2 pt Catalyseur |
| Rupture géopolitique dans zone de production critique | −2 pt Catalyseur |
| Reshoring / rapatriement production (favorable) | +1 pt Catalyseur |

---

### NLP Transcript — Intégré dans Agent Fondamental

Analyse du vocabulaire des earnings calls sur 3 trimestres pour détecter les changements de ton du management **avant** que les chiffres ne le confirment.

**Métriques clés :** Ratio Confiance/Prudence, évolutions inter-trimestrielles, évasions Q&A, formulation guidance

**Intégration dans le scoring :**

| Signal NLP | Ajustement Score |
|-----------|-----------------|
| Ratio confiance > 2.5 et en hausse vs trimestre précédent | +1 pt Valorisation |
| Ratio confiance 1.5–2.5 (neutre) | 0 pt |
| Ratio confiance < 1.5 ou en forte baisse | −0.5 pt Valorisation |
| Pivots ambigus ≥ 3 (restructuring, rightsizing…) | −1 pt Valorisation |
| Évasions Q&A ≥ 5 | −0.5 pt Valorisation |

---

### Job Postings — Intégré dans Agent Sentiment

Signal avancé **6 à 12 mois** basé sur les offres d'emploi publiées par les entreprises et leurs principaux clients/fournisseurs.

**Signaux clés :** accélération/décélération des embauches, pivots technologiques, suppressions de postes annoncées

**Intégration dans le scoring :**

| Signal Job Postings | Ajustement Score |
|--------------------|-----------------|
| Recrutement accéléré (>30% postes vs même période an-1) | +1 pt Catalyseur |
| Recrutement stable (±15%) | 0 pt |
| Forte décélération embauches (>30% en moins) | −1 pt Catalyseur |
| Plan de licenciements annoncé (>5% effectifs) | −2 pt Catalyseur |
| Nouveaux postes IA/tech stratégique > 20% des offres | +0.5 pt Catalyseur |

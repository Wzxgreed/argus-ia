# Orchestration avancée — Handoffs & Commandes prêtes à l'emploi

Ce fichier contient le format exact des Handoff Packages entre agents et les prompts prêts à l'emploi pour déclencher les workflows.

**Architecture actuelle : 6 agents**
`Macro → Flux → Supply Chain → (Fondamental + Technique + Sentiment) → Synthèse`

---

## Format Handoff Package — Standard entre agents

> Chaque agent termine son analyse en produisant un Handoff Package dans ce format exact.
> L'agent suivant LIT ce bloc **en premier**, avant de commencer son propre travail.

### Handoff Macro → Tous les agents

```
=== HANDOFF PACKAGE — AGENT MACRO → TOUS ===
Date : YYYY-MM-DD | Ticker : [TICKER ou GLOBAL]

RÉGIME ACTIF : [NORMAL / RISK-OFF / RISK-ON / PRÉ-FOMC / PRÉ-EARNINGS / STAGFLATION / RÉCESSION]
PONDÉRATION : Catalyseur XX% · Valorisation XX% · Momentum XX%
BONUS/MALUS MACRO : [ex : −1pt sur cycliques / +0.5pt sur défensives]

ENVIRONNEMENT :
- VIX : XX ([Calme <15 / Normal 15-25 / Peur 25-35 / Capitulation >35])
- Taux 10Y US : X.X% ([Montant / Stable / Baisse])
- Courbe 10Y−2Y : [Normale / Aplatie / Inversée]
- DXY : XXX ([Fort >103 / Neutre / Faible <98])
- Spreads HY : XXX bps ([Sain <350 / Stress 350-500 / Crise >500])

ALERTES MACRO DU JOUR :
- [Ex : FOMC dans 48h → basculer régime Pré-FOMC]
- [Ex : CPI +0.4% vs +0.3% attendu → réaccélération inflation → hawkish surprise]

CARTE D'EXPOSITION SECTORIELLE (sensibilités actuelles) :
- Taux +1% → Tech −X% / Utilities +X% / Banks +X%
- DXY +5% → Multinationales −X% / Domestiques +X%
- Pétrole +10% → Énergie +X% / Transport −X% / Consommation −X%
- Chine −10% → Semis −X% / Luxe −X% / Matériaux −X%
=== FIN HANDOFF MACRO ===
```

### Handoff Flux → Sentiment + Technique

```
=== HANDOFF PACKAGE — AGENT FLUX → SENTIMENT + TECHNIQUE ===
Date : YYYY-MM-DD | Ticker : [TICKER]

POSITIONNEMENT INSTITUTIONNEL (13F) :
- Nouveaux entrants : [Fonds X ($XXm) / Aucun]
- Sorties majeures : [Fonds Y (−$XXm) / Aucune]
- Renforcements : [Fonds Z (+XX% position)]
- Signal 13F : 🟢 Accumulation / ⚪ Stable / 🔴 Distribution

FLUX ETF :
- Flux nets ETF secteur (7j) : +/−$XXm
- ETF [TICKER] spécifique (si applicable) : +/−$XXm
- Signal ETF : Entrant / Sortant / Neutre

SHORT INTEREST :
- Short interest : XX% float | Days to cover : Xj | Borrow rate : XX%
- Variation 2 sem. : +/−X%
- Squeeze setup : ✅ OUI (4 conditions réunies) / ❌ NON

OPTIONS (Gamma & Max Pain) :
- Max Pain : $XXX | Call Wall : $XXX | Put Wall : $XXX
- GEX : [POSITIF stabilisant / NÉGATIF amplifiant]
- IV Rank : XX% ([Bas <30 / Normal 30-70 / Élevé >70])

BONUS/MALUS FLUX SUR SCORE CATALYSEUR :
[ex : +2pt squeeze setup / +1.5pt activist entrant / −1pt distribution 13F]
=== FIN HANDOFF FLUX ===
```

### Handoff Supply Chain → Fondamental + Sentiment

```
=== HANDOFF PACKAGE — AGENT SUPPLY CHAIN → FONDAMENTAL + SENTIMENT ===
Date : YYYY-MM-DD | Ticker : [TICKER]

SIGNAUX DU JOUR :
- [Fournisseur critique X] : [News / Earnings / Guidance] → Impact estimé : [+/-X% marges]
- [Client critique Y] : [News / Earnings / Profits warning] → Impact revenus : [+/-X%]
- Aucun signal détecté ce jour

ÉTAT DE LA SUPPLY CHAIN :
- Concentration fournisseur : Élevée / Modérée / Faible
- Risque géopolitique zones de production : [Ex : Taiwan tension Modérée]
- Tendance carnet de commandes : Croissant / Stable / Décroissant

BONUS/MALUS SUPPLY CHAIN SUR SCORE CATALYSEUR :
[ex : −1.5pt profits warning client / +1pt guidance en hausse fournisseur]

ENTITÉS À SURVEILLER CETTE SEMAINE :
- [Entité] ([TICK]) — earnings le YYYY-MM-DD
=== FIN HANDOFF SUPPLY CHAIN ===
```

### Handoff Sentiment → Fondamental + Synthèse

```
=== HANDOFF PACKAGE — AGENT SENTIMENT → FONDAMENTAL + SYNTHÈSE ===
Date : YYYY-MM-DD | Ticker : [TICKER]

SCORE CATALYSEUR : X/10
SENTIMENT DOMINANT : 🟢 Très positif / 🟡 Mixte / 🔴 Négatif

ANALYSTES :
- Consensus : XX% Buy · XX% Hold · XX% Sell | Prix cible médian : $XXX | Upside : +/-XX%
- Mouvements 30j : X upgrades / X downgrades (source fiable : Oui/Non)
- EPS Revision Momentum 30j : Solde net +X/-X | Signal : 🚀/🟢/⚪/🟡/🔴

INSIDERS :
- Net 3 mois : Acheteur $XXXk (X pers.) / Vendeur $XXXk / Neutre
- Signal notable : [ex : CEO achat $500k le DATE / Aucun]

SHORT & OPTIONS :
- Short interest : XX% float | DTC : Xj | Squeeze : Oui/Non
- IV Rank : XX% | Max Pain : $XXX | GEX : Pos/Neg
- Unusual options : [Oui — détail / Non]

JOB POSTINGS : [Signal détecté / Aucun]
CONTRATS GOV. : [Contrat détecté / Aucun]
TRANSACTIONS POLITIQUES : [Signal / Aucun]

CONTEXTE MARCHÉ :
- VIX : XX | Put/Call S&P : X.X | Fear & Greed : XX
=== FIN HANDOFF SENTIMENT ===
```

### Handoff Fondamental → Technique + Synthèse

```
=== HANDOFF PACKAGE — AGENT FONDAMENTAL → TECHNIQUE + SYNTHÈSE ===
Date : YYYY-MM-DD | Ticker : [TICKER]

FILTRE QUALITÉ : X/6 — ✅ Quality Compounder / ⚠️ Partielle / 🔴 Hors périmètre
SCORE VALORISATION : X/10 (plafonné à 5/10 si Filtre ≤ 3/6)
SCORE CONFIANCE MANAGEMENT (NLP) : X/10

PRIX CIBLE : $XXX | Méthode : [DCF / NTM Comps / LTM Comps]
UPSIDE/DOWNSIDE : +/-XX% vs cours actuel $XXX
MARGE DE SÉCURITÉ : XX%

MÉTRIQUES CLÉS :
- Revenus : $Xb (+XX% YoY) | Marge brute : XX% | EPS : $X.XX
- FCF yield : X.X% | Qualité bénéfices : ✅/⚠️/🔴 (accruals : X%)
- Dette/EBITDA : X.Xx | ROIC : XX%
- Valorisation vs pairs : Prime +XX% / Décote −XX% / Ligne (multiple retenu : XX× [LTM/NTM])

THÈSE : Haussier / Neutre / Baissier
RISQUE PRINCIPAL : [En 1 ligne]

MODÈLE PRÉDICTION EARNINGS (si preview) :
- Score composite : +X.X | Proba beat : XX% | Réaction estimée : +/-X% à +/-X%
=== FIN HANDOFF FONDAMENTAL ===
```

### Handoff Technique → Synthèse

```
=== HANDOFF PACKAGE — AGENT TECHNIQUE → SYNTHÈSE ===
Date : YYYY-MM-DD | Ticker : [TICKER]

SCORE MOMENTUM : X/10
TIMING : ✅ Favorable / ⚠️ Attendre / ❌ Défavorable

COURS & NIVEAUX :
- Cours : $XXX | ATR 14j : $X.XX | Stop ATR : $XXX (cours − 2×ATR)
- MM50 : $XXX ([Au-dessus / En dessous]) | MM200 : $XXX ([Au-dessus / En dessous])
- Tendance : Golden cross / Death cross / Neutre
- VWAP : Au-dessus / En dessous | Bollinger : Squeeze / Normal / Élargi

INDICATEURS :
- RSI 14j : XX ([Survendu <30 / Neutre / Suracheté >70])
- MACD : [Haussier / Baissier / Croisement en cours]
- Volume : ×X vs moy. 20j ([Élevé / Normal / Faible])

FORCE RELATIVE :
- RS vs S&P 500 (90j) : +/-XX% | Signal : Leader / Neutre / Retardataire
- RS vs ETF secteur (90j) : +/-XX% | Signal : Leader / Neutre / Retardataire

SAISONNALITÉ : [Favorable / Neutre / Défavorable] — [ex : Juin historiquement +2.3% pour Tech]

SUPPORTS & RÉSISTANCES :
- Support 1 : $XXX | Support 2 : $XXX
- Résistance 1 : $XXX (Call Wall) | Résistance 2 : $XXX
=== FIN HANDOFF TECHNIQUE ===
```

---

## Mode 1 — Bulletin du matin complet (6 agents)

```
Étape 0 OBLIGATOIRE :
→ Lire Agents/APPRENTISSAGES.md en entier, charger toutes les règles actives
→ Vérifier les 3 fichiers de suivi : BACKTESTING.md · SUIVI_PRIX_CIBLES.md · SUIVI_EARNINGS_PREDICTIONS.md
→ Clôturer les fenêtres échues, déclencher les post-mortems si Miss détecté

Ensuite, en suivant CLAUDE.md et Agents/ORCHESTRATION.md :

Phase 0 — Alertes : Lire ALERTES.md (simples + composites) → évaluer chaque condition
Phase 0b — Supply Chain : Scanner news sur entités 🔴🟡 de chaque SUPPLY_CHAIN.md watchlist
Phase 1 — Agent Macro : Régime actif + pondération + alertes macro → Handoff Macro
Phase 2 — Agent Flux : 13F, ETF, short, dark pool, gamma/max pain watchlist → Handoff Flux
Phase 3 — Agent Supply Chain : Signaux du jour sur fournisseurs/clients critiques → Handoff Supply Chain
Phase 4 — Agent Sentiment : News mondiales + analystes + insiders + options → Handoff Sentiment
Phase 5 — Agent Fondamental : Révisions estimations tickers impactés → Handoff Fondamental
Phase 6 — Agent Technique : Cours, ATR, force relative, saisonnalité watchlist → Handoff Technique
Phase 7 — Synthèse : Score final avec pondération du régime actif + WATCHLIST_SCORES.md
→ Créer Actualités/YYYY-MM-DD.md · _update.md nécessaires · Opportunités/YYYY-MM-DD.md
```

---

## Mode 2 — Analyse initiale complète d'une nouvelle action

```
Étape 0 : Lire APPRENTISSAGES.md → charger règles actives

En suivant Agents/ORCHESTRATION.md :

1. Agent Macro → Handoff Macro (régime + sensibilité sectorielle du ticker)
2. Agent Flux → Handoff Flux (positionnement institutionnel initial)
3. Agent Supply Chain → créer Actions/[TICKER]/SUPPLY_CHAIN.md + Handoff Supply Chain
4. Agent Fondamental (+ Market Researcher skill) :
   → Filtre Qualité 6/6 EN PREMIER
   → Valorisation DCF + Comps LTM/NTM
   → NLP transcript dernier earnings
   → Handoff Fondamental
5. Agent Technique → Handoff Technique (ATR stop-loss + force relative + saisonnalité)
6. Agent Sentiment (+ Earnings Reviewer si earnings récents) :
   → EPS Revision Momentum · Job postings · Contrats gov. · Track record analystes
   → Handoff Sentiment
7. Synthèse → Score final pondéré régime Macro

Créer dans ordre :
→ Actions/[TICKER]/[TICKER]_YYYY-MM-DD_init.md (tous les blocs)
→ Actions/[TICKER]/[TICKER]_YYYY-MM-DD_earnings.md (si trimestre récent disponible)
→ Actions/[TICKER]/INDEX.md
→ Actualités/WATCHLIST.md (ajouter ticker)
→ Actualités/CALENDRIER_EARNINGS.md (ajouter prochain earnings)
→ Alertes/ALERTES.md (ajouter seuils simples + alerte composite recommandée)
→ Actions/SUIVI_PRIX_CIBLES.md (enregistrer prix cible J+30/90/180)
→ Actions/WATCHLIST_SCORES.md (ajouter ligne ticker)
→ Actions/CORRELATIONS_WATCHLIST.md (calculer corrélations initiales)
```

---

## Mode 3 — Impact d'une actualité sur un ticker suivi

```
Étape 0 : Lire APPRENTISSAGES.md + Actions/[TICKER]/INDEX.md + TOUS les fichiers du dossier

En suivant Agents/ORCHESTRATION.md :

1. Agent Macro → régime a-t-il changé ? Handoff Macro mis à jour
2. Agent Supply Chain → cette news touche-t-elle un fournisseur ou client de [TICKER] ?
3. Agent Sentiment → impact sentiment, réaction analystes, IV vs HV post-news
4. Agent Fondamental → 3 scénarios (optimiste/central/pessimiste) + probabilités + révision prix cible
5. Agent Technique → cours tient-il les supports ? ATR recalculé → nouveau stop-loss

→ Créer Actions/[TICKER]/[TICKER]_YYYY-MM-DD_update.md
→ Mettre à jour Actions/[TICKER]/INDEX.md
→ Mettre à jour Actions/WATCHLIST_SCORES.md
→ Si position ouverte : Portefeuille/POSITIONS.md (P&L + stop révisé)
→ Vérifier CORRELATIONS_WATCHLIST.md : mouvement > 3% → analyser les corrélés
```

---

## Mode 4 — Preview pré-earnings

```
Étape 0 : Lire APPRENTISSAGES.md + SUIVI_EARNINGS_PREDICTIONS.md (calibration ticker)

En suivant Agents/AGENT_FONDAMENTAL.md (section Modèle Prédiction) :

1. Agent Macro → régime actif + pondération du moment
2. Agent Fondamental :
   → Révisions EPS J-30 (Input 1, poids 35%)
   → NLP ton management dernier call (Input 3, poids 25%)
   → Score composite + probabilité beat chiffrée
3. Agent Technique :
   → Momentum J-30 vs secteur ETF (Input 2, poids 25%)
4. Agent Sentiment :
   → IV Rank J-7 (Input 4, poids 15%)
   → EPS Revision Momentum
   → Earnings whisper vs consensus

→ Créer Actions/[TICKER]/[TICKER]_YYYY-MM-DD_preview.md
→ Enregistrer dans Actions/SUIVI_EARNINGS_PREDICTIONS.md
```

---

## Mode 5 — Revue hebdomadaire (lundi)

```
Étape 0 : Lire APPRENTISSAGES.md + clôturer toutes les fenêtres des 3 fichiers de suivi

En suivant Agents/WORKFLOW_SEMAINE.md :

Phase H1 — Portefeuille : P&L + révision stop-loss ATR + alertes positions −15%
Phase H2 — Risque : recalcul corrélations (CORRELATIONS_WATCHLIST.md) + stress tests
Phase H3 — Watchlist : scores + prix cibles + patterns récurrents (PATTERNS_HISTORIQUES.md)
Phase H4 — Calendrier : earnings 7j + alertes composites à réviser
Phase H5 — Rapport : Actualités/Semaines/[YYYY-WXX].md

→ Mettre à jour Actions/CORRELATIONS_WATCHLIST.md (matrice 30j)
→ Mettre à jour Actions/WATCHLIST_SCORES.md (historique 7j)
→ Mettre à jour Portefeuille/POSITIONS.md (stops révisés)
```

---

## Mode 6 — Agent unique ciblé

```
# Macro seul
Joue uniquement le rôle de l'Agent Macro (Agents/AGENT_MACRO.md) :
→ Quel est le régime actuel ? Quelle pondération appliquer ?
→ Y a-t-il un hedge Risk-off recommandé pour le portefeuille actuel ?
→ Produis le Handoff Macro complet.

# Flux seul
Joue uniquement le rôle de l'Agent Flux (Agents/AGENT_FLUX.md) sur [TICKER] :
→ Analyse 13F, ETF, short interest, dark pool, gamma/max pain
→ Produis le Handoff Flux complet avec bonus/malus sur le score Catalyseur.

# Supply Chain seul
Joue uniquement le rôle de l'Agent Supply Chain (Agents/AGENT_SUPPLY_CHAIN.md) sur [TICKER] :
→ Cartographie fournisseurs/clients (10-K) + scoring criticité
→ Crée ou met à jour Actions/[TICKER]/SUPPLY_CHAIN.md

# Fondamental seul
Joue uniquement le rôle de l'Agent Fondamental (Agents/AGENT_FONDAMENTAL.md) sur [TICKER] :
→ Filtre Qualité + Valorisation DCF + Comps + NLP transcript
→ Produis le Handoff Fondamental avec Score Valorisation /10.

# Technique seul
Joue uniquement le rôle de l'Agent Technique (Agents/AGENT_TECHNIQUE.md) sur [TICKER] :
→ RSI, MACD, ATR, force relative, saisonnalité, stop-loss
→ Produis le Handoff Technique avec Score Momentum /10.

# Sentiment seul
Joue uniquement le rôle de l'Agent Sentiment (Agents/AGENT_SENTIMENT.md) sur [TICKER] :
→ Analystes (track record), insiders, options, EPS revision momentum, job postings
→ Produis le Handoff Sentiment avec Score Catalyseur /10.
```

---

## Règles de passage entre agents

| Transition | Ce que l'agent suivant lit en priorité |
|-----------|---------------------------------------|
| Macro → Tous | Régime + pondération + bonus/malus macro + carte exposition |
| Flux → Sentiment + Technique | Short interest + GEX + Max Pain + bonus/malus Catalyseur |
| Supply Chain → Fondamental | Signaux fournisseurs/clients + impact marges/revenus |
| Supply Chain → Sentiment | Bonus/malus Catalyseur supply chain |
| Sentiment → Fondamental | Révisions EPS + Score Catalyseur + IV vs HV + régime |
| Fondamental → Technique | Prix cible + Score Val + Filtre Qualité + Confiance Management |
| Technique → Synthèse | Score Momentum + ATR stop + force relative + saisonnalité |

**Règle de disqualification :** score individuel ≤ 2/10 → exclure du rapport Opportunités.

**Règle de conflit :** écart entre scores ≥ 3 pts → appliquer la section "Gestion des conflits" dans ORCHESTRATION.md.

**Règle Filtre Qualité :** Score Qualité ≤ 3/6 → Score Valorisation plafonné à 5/10 avant synthèse.

---

## Fréquence recommandée

| Mode | Fréquence | Déclencheur |
|------|-----------|-------------|
| Mode 1 — Bulletin matin | Chaque jour ouvré | Manuellement ou via schedule |
| Mode 2 — Nouvelle action | À la demande | Quand tu découvres une action |
| Mode 3 — Impact actualité | Dès qu'une news sort | News ≥ modéré sur ticker watchlist |
| Mode 4 — Preview earnings | J-5 avant l'annonce | Automatique si CALENDRIER_EARNINGS.md |
| Mode 5 — Revue hebdo | Chaque lundi | Avant le bulletin du matin |
| Mode 6 — Agent ciblé | À la demande | Pour approfondir un angle spécifique |

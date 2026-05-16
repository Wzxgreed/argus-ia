# Agent Supply Chain

**Rôle :** Cartographier les dépendances critiques de chaque ticker (fournisseurs et clients clés), les surveiller en continu, et détecter les risques ou opportunités avant qu'ils apparaissent dans les résultats financiers. Un fournisseur qui publie de mauvais résultats impacte le ticker 1 à 3 trimestres plus tard — cet agent le détecte en avance.

**Déclenché par :**
- Création d'une nouvelle analyse (`_init.md`) — cartographie initiale obligatoire
- Workflow du matin — scan automatique des news sur les entités supply chain de la watchlist
- Publication de résultats par un fournisseur/client clé d'un ticker watchlist
- Commande manuelle : `Analyse la supply chain de [TICKER]`

**Coopère avec :**
- → Agent Fondamental : enrichit l'analyse des marges et des risques de coûts
- → Agent Sentiment : fournit des signaux avancés pour le Score Catalyseur
- → Agent Macro : croise avec la carte d'exposition géographique
- → Opportunités : bonus/malus sur le score si signal supply chain majeur détecté

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `secFilings` | 10-K (section "Risk Factors" + "Customers" + "Suppliers") |
| `company` | Description business, partenaires mentionnés |
| `news` | News sur les fournisseurs/clients identifiés |
| `earningsTranscript` | Mentions fournisseurs/clients dans les calls earnings |
| `statements` | Évolution des coûts des matières premières, marges brutes |
| `quote` | Cours des fournisseurs/clients cotés |

---

## Cartographie Supply Chain — Méthode

### Étape 1 — Identification des entités clés

**Fournisseurs (inputs)** — identifier depuis les 10-K :
- Fournisseurs nommés explicitement (>10% des achats → obligation de déclaration SEC)
- Matières premières critiques et leurs producteurs dominants
- Fournisseurs de composants clés (ex : pour Apple → TSMC, Samsung, Foxconn)
- Prestataires de services critiques (cloud, logistique, manufacturing)

**Clients (outputs)** — identifier depuis les 10-K :
- Clients nommés explicitement (>10% du CA → obligation de déclaration SEC)
- Secteurs/industries clientes et leurs leaders
- Canaux de distribution critiques (ex : Amazon, distributeurs)
- Partenaires OEM/white-label

**Entités de substitution** — évaluer la fragilité :
- Nombre de fournisseurs alternatifs disponibles
- Délai de substitution estimé
- Coût de switching

### Étape 2 — Scoring de criticité

| Score criticité | Critères |
|----------------|---------|
| 🔴 Critique (3) | Part > 20% des achats/CA + pas d'alternative rapide |
| 🟡 Important (2) | Part 10-20% OU alternative disponible mais coûteuse |
| 🟢 Modéré (1) | Part < 10% OU facilement substituable |

### Étape 3 — Surveillance continue

Pour chaque entité critique (score 3) ou importante (score 2) **cotée en bourse** :
- Ajouter à la liste de surveillance
- Monitorer via `news` + `quote` + `statements`
- Déclencher une alerte si résultats publiés, guidance abaissée, ou news négative majeure

---

## Format de sortie — Carte Supply Chain

> Ce bloc est créé dans `Actions/[TICKER]/SUPPLY_CHAIN.md` lors de l'analyse initiale
> et mis à jour lors des `_update.md` si une entité clé publie des données significatives.

```markdown
# [TICKER] — Carte Supply Chain

**Dernière mise à jour :** YYYY-MM-DD
**Source principale :** 10-K YYYY (section Risk Factors + Suppliers/Customers)

---

## Fournisseurs clés

| Rang | Entité | Ticker | Part estimée des achats | Criticité | Dernière news |
|------|--------|--------|------------------------|-----------|---------------|
| 1 | [Fournisseur] | [TICK] | XX% | 🔴 Critique | YYYY-MM-DD |
| 2 | [Fournisseur] | [TICK] | ~XX% | 🟡 Important | — |
| 3 | [Fournisseur] | — | ~XX% | 🟢 Modéré | — |
| 4 | [Matière première] | — | ~XX% | 🟡 Important | — |
| 5 | [Fournisseur] | [TICK] | ~XX% | 🟢 Modéré | — |

**Concentration fournisseur :** [Élevée / Modérée / Faible]
**Risque géographique fournisseurs :** [ex : 60% des composants fabriqués à Taïwan]
**Alternatives disponibles :** [ex : TSMC dominant, Samsung comme backup — délai switch : 12-18 mois]

---

## Clients clés

| Rang | Entité | Ticker | Part estimée du CA | Criticité | Dernière news |
|------|--------|--------|-------------------|-----------|---------------|
| 1 | [Client] | [TICK] | XX% | 🔴 Critique | — |
| 2 | [Client] | [TICK] | ~XX% | 🟡 Important | — |
| 3 | [Secteur client] | — | ~XX% | 🟡 Important | — |
| 4 | [Client] | [TICK] | ~XX% | 🟢 Modéré | — |
| 5 | [Client] | [TICK] | ~XX% | 🟢 Modéré | — |

**Concentration client :** [Élevée / Modérée / Faible]
**Risque de dépendance :** [ex : Apple représente 25% du CA — si Apple réduit ses commandes → impact immédiat]

---

## Risques supply chain identifiés

| Risque | Probabilité | Impact cours estimé | Signal d'alerte |
|--------|------------|--------------------|--------------||
| [ex : Crise semi-conducteurs Taïwan] | Faible | −15 à −25% | Tension géopolitique Détroit |
| [ex : Perte du client Apple] | Très faible | −20% | Apple earnings décevants |
| [ex : Hausse coût matières premières] | Modérée | −3 à −5% marge | Cuivre/lithium > seuil X |

---

## Opportunités supply chain

| Opportunité | Probabilité | Impact cours estimé | Signal déclencheur |
|-------------|------------|--------------------|--------------------|
| [ex : Rapatriement chaîne US (reshoring)] | Modérée | +5 à +10% | Politique industrielle US |
| [ex : Client [X] accélère ses commandes] | Modérée | +3 à +8% | Earnings client positifs |

---

## Historique des signaux supply chain

| Date | Entité | Événement | Impact détecté sur [TICKER] | Délai |
|------|--------|-----------|----------------------------|-------|
| — | — | — | — | — |
```

---

## Protocole de monitoring quotidien (workflow du matin)

```
PHASE 0 du bulletin du matin — SUPPLY CHAIN CHECK :
1. Pour chaque ticker de la watchlist avec une SUPPLY_CHAIN.md :
   a. Récupérer les news du jour sur toutes les entités 🔴 Critiques et 🟡 Importantes via `news`
   b. Vérifier si un fournisseur/client clé a publié ses résultats ce jour ou hier
   c. Si oui → analyser l'impact sur [TICKER] (voir protocole d'impact ci-dessous)

2. Déclencher une alerte supply chain si :
   → Fournisseur critique : guidance abaissée, pénurie annoncée, problème qualité
   → Client critique : profits warning, réduction budgets capex, churn massif
   → Rupture géopolitique dans la zone de production clé
   → Cours d'une matière première clé franchit un seuil critique

3. Si alerte déclenchée → créer un [TICKER]_YYYY-MM-DD_update.md avec la section Supply Chain
```

## Protocole d'impact — Résultats d'un fournisseur/client clé

```
QUAND UN FOURNISSEUR/CLIENT CRITIQUE PUBLIE SES RÉSULTATS :

ÉTAPE 1 — LECTURE DES RÉSULTATS
→ Récupérer les chiffres clés (revenus, marges, guidance) via `statements` ou `news`
→ Identifier les mentions explicites de [TICKER] dans le transcript (`earningsTranscript`)

ÉTAPE 2 — CALCUL DE L'IMPACT SUR [TICKER]
→ Si FOURNISSEUR critique :
   - Guidance en hausse → risque de pression sur les coûts de [TICKER] → impact marges −X%
   - Pénurie annoncée → risque de rupture d'approvisionnement → timeline produit décalée
   - Fermeture usine → risque supply critique → impact immédiat sur cours

→ Si CLIENT critique :
   - Profits warning → réduction probable des commandes → impact revenus [TICKER] −X%
   - Guidance relevée → hausse probable des commandes → impact revenus [TICKER] +X%
   - Mentionne [TICKER] positivement dans le call → signal très fort

ÉTAPE 3 — DÉLAI D'IMPACT ESTIMÉ
→ Impact immédiat (0-1 mois) : rupture d'approvisionnement confirmée, perte contrat annoncée
→ Impact à moyen terme (1-3 trimestres) : dégradation progressive des commandes
→ Impact à long terme (3-6 trimestres) : changement structurel de la chaîne

ÉTAPE 4 — MISE À JOUR
→ Créer [TICKER]_YYYY-MM-DD_update.md avec section "Signal Supply Chain"
→ Mettre à jour SUPPLY_CHAIN.md (colonne "Dernière news")
→ Mettre à jour INDEX.md
→ Si impact estimé > 3% sur le cours → ajouter dans le rapport Opportunités du jour
```

---

## Scoring — Contribution au score Catalyseur

| Signal | Ajustement |
|--------|-----------|
| Client critique publie guidance en forte hausse (+>10%) | +1 pt Catalyseur |
| Client critique mentionne explicitement le ticker positivement | +1.5 pt Catalyseur |
| Fournisseur critique annonce pénurie ou fermeture usine | −2 pts Catalyseur |
| Client critique émet un profits warning | −1.5 pt Catalyseur |
| Reshoring / rapatriement production annoncé (favorable) | +1 pt Catalyseur |
| Rupture géopolitique dans zone de production critique | −2 pts Catalyseur |
| Nouveau client majeur annoncé (>10% CA potentiel) | +2 pts Catalyseur |

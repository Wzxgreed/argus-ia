# Apprentissages — Mémoire Institutionnelle du Système

> **LECTURE OBLIGATOIRE EN TOUT PREMIER à chaque session, avant l'Agent Macro.**
> Ce fichier contient les règles corrigées issues de l'analyse des erreurs passées.
> Toutes les règles ici **surpassent** les règles par défaut des agents.

---

## Comment ce fichier fonctionne

Chaque fois qu'un signal est classé **Miss** dans `Opportunités/BACKTESTING.md`, un post-mortem est déclenché automatiquement. L'agent relit l'analyse originale, identifie la cause racine, et documente la leçon ici sous forme de règle actionnable.

Au fil du temps, ce fichier devient la mémoire des erreurs du système. Plus il est riche, plus les scores sont précis.

---

## Périmètre du système d'apprentissage

Le système apprend de **3 types d'erreurs** distincts, chacun avec son propre journal de post-mortems :

| Type d'erreur | Source | Fichier de suivi | Horizon de détection |
|--------------|--------|-----------------|---------------------|
| **Opportunités manquées** | Signaux scorés ≥ 6/10 publiés dans Opportunités/ | `Opportunités/BACKTESTING.md` | J+5, J+20, J+60 |
| **Prix cibles incorrects** | Tout `_init.md` et `_update.md` | `Actions/SUIVI_PRIX_CIBLES.md` | J+30, J+90, J+180 |
| **Prédictions earnings imprécises** | Tout `_preview.md` | `Actions/SUIVI_EARNINGS_PREDICTIONS.md` | Le jour J (après publication) |

---

## ÉTAPE 0 — Protocole de lecture au démarrage

```
À CHAQUE SESSION, AVANT TOUT :

1. Lire ce fichier en entier
2. Charger toutes les règles de la section "Règles actives issues des erreurs"
3. Appliquer ces règles en priorité sur les règles par défaut des agents
4. Si une règle ici contredit une règle dans un fichier agent → cette règle prévaut
5. Vérifier les 3 fichiers de suivi pour les fenêtres arrivant à échéance :
   → Opportunités/BACKTESTING.md (J+5, J+20, J+60)
   → Actions/SUIVI_PRIX_CIBLES.md (J+30, J+90, J+180)
   → Actions/SUIVI_EARNINGS_PREDICTIONS.md (fenêtres en attente de résultats)
6. Pour chaque fenêtre échue : récupérer le cours via `quote`, enregistrer le verdict
7. Pour chaque Miss / Imprécis détecté : déclencher le post-mortem AVANT le workflow du jour
8. Logger mentalement : "X règles d'apprentissage chargées · Y fenêtres vérifiées · Z post-mortems déclenchés"
```

---

## Règles actives issues des erreurs

> Section à enrichir au fil des post-mortems. Vide au démarrage — se remplit automatiquement.

### Ajustements de scoring

| Règle | Source | Depuis | Confiance |
|-------|--------|--------|-----------|
| — | — | — | — |

*Exemple de ce que cette section contiendra :*
> `Régime Risk-off confirmé → pénaliser Score Catalyseur de −1 pt sur tous les tickers cycliques, quelle que soit la qualité du catalyseur annoncé.` ← *issue du post-mortem du 2026-XX-XX sur [TICKER]*

---

### Patterns d'erreurs récurrents

| Pattern identifié | Fréquence | Correction appliquée |
|-------------------|-----------|----------------------|
| — | — | — |

---

### Track record analystes — corrections réelles

> Complète `Agents/ANALYST_TRACK_RECORD.md` avec les données observées sur la watchlist.

| Analyste / Maison | Ticker(s) concerné(s) | Précision observée | Biais | Règle de pondération appliquée |
|------------------|----------------------|-------------------|-------|-------------------------------|
| — | — | — | — | — |

---

### Signaux sur-scorés — blacklist temporaire

> Signaux qui se sont révélés peu fiables sur la watchlist actuelle.

| Signal | Contexte de défaillance | Pénalité appliquée | Réévaluation prévue |
|--------|------------------------|-------------------|---------------------|
| — | — | — | — |

---

### Signaux sous-scorés — bonus empiriques

> Signaux qui se sont révélés plus prédictifs que leur pondération par défaut.

| Signal | Contexte de surperformance | Bonus appliqué | Réévaluation prévue |
|--------|--------------------------|---------------|---------------------|
| — | — | — | — |

---

## Journal des post-mortems — Opportunités (BACKTESTING)

> Post-mortems sur les signaux d'opportunités scorés ≥ 6/10 qui ont été des Misses à J+20 ou J+60.

*(Voir template dans Opportunités/BACKTESTING.md — section "Template post-mortem")*

---

## Journal des post-mortems — Prix Cibles (SUIVI_PRIX_CIBLES)

> Post-mortems sur les prix cibles de `_init.md` et `_update.md` qui ont été des Misses à J+90 ou J+180.

```markdown
## Post-Mortem Prix Cible #XXX — [TICKER] — Analyse du [DATE] → Miss à J+[90/180]

**Prix cible émis :** $XXX le YYYY-MM-DD ([Achat/Neutre/Vente])
**Cours à l'émission :** $XXX | **Upside annoncé :** +/-XX%
**Cours à J+[90/180] :** $XXX (performance réelle : [+/-XX%])
**Fichier source :** Actions/[TICKER]/[TICKER]_YYYY-MM-DD_[init/update].md

### Thèse originale résumée
> [En 2-3 lignes : qu'est-ce que l'agent avait prédit et pourquoi]

### Ce qui s'est réellement passé
> [Description factuelle de la trajectoire du cours et des événements clés]

### Type d'erreur
- [ ] A) Direction incorrecte (bullish sur action qui a baissé)
- [ ] B) Amplitude incorrecte (bonne direction, prix cible trop ambitieux)
- [ ] C) Timing incorrect (thèse juste mais trop tôt)
- [ ] D) Risque non modélisé (événement non anticipé)

### Analyse détaillée
> [Qu'est-ce qui était visible dans les données au moment de l'analyse ?
>  Quel signal a été sous-pondéré ou ignoré ?]

### Règle extraite
> **NOUVELLE RÈGLE :** [...]

### Action sur le système
- [ ] Règle ajoutée dans "Règles actives"
- [ ] Paramètres DCF révisés
- [ ] Aucune action (événement isolé)

**Confiance :** Faible / Moyenne / Forte
```

---

## Journal des post-mortems — Earnings Predictions (SUIVI_EARNINGS_PREDICTIONS)

> Post-mortems sur les prédictions de réaction earnings imprécises (écart > 8% entre prédiction et réalité).

```markdown
## Post-Mortem Earnings #XXX — [TICKER] — Preview du [DATE] → Imprécis

**Earnings date :** YYYY-MM-DD
**Prédiction :** Beat → +X% / Inline → ±X% / Miss → -X% | Proba beat : XX%
**Résultat réel :** EPS surprise [+/-XX%] · Rev surprise [+/-XX%]
**Réaction prédite :** +/-X% | **Réaction réelle :** +/-X% | **Écart :** X pts
**Fichier source :** Actions/[TICKER]/[TICKER]_YYYY-MM-DD_preview.md

### Ce que l'agent avait prédit
> [Résumé de la logique de prédiction]

### Ce qui s'est réellement passé
> [Résultats + réaction du cours + éléments qui ont surpris]

### Type d'erreur
- [ ] A) Surprise mal estimée (beat/miss plus fort qu'anticipé)
- [ ] B) Barre implicite ignorée (beat sur chiffres, déception sur guidance)
- [ ] C) Réaction atypique (macro dominante ce jour-là)
- [ ] D) Mauvaise métrique clé surveillée (marché regardait ailleurs)

### Règle extraite
> **NOUVELLE RÈGLE :** [...]
> Exemple : "Pour [TICKER], pondérer la guidance à 60% dans la prédiction de réaction"

### Action sur le système
- [ ] Règle ajoutée dans "Règles actives"
- [ ] Règle de calibration ticker ajoutée dans SUIVI_EARNINGS_PREDICTIONS.md
- [ ] Aucune action (exogène)

**Confiance :** Faible / Moyenne / Forte
```

---

## Journal des post-mortems

> Un post-mortem par Miss. Format standardisé.

---

### Template post-mortem

```markdown
## Post-Mortem #XXX — [TICKER] — [DATE SIGNAL] → Miss à J+[5/20/60]

**Signal original :** Score X/10 le YYYY-MM-DD — [type de catalyseur]
**Cours au signal :** $XXX
**Cours à J+XX :** $XXX (−X% — Miss)
**Fichier source :** Actions/[TICKER]/[TICKER]_YYYY-MM-DD_[type].md

### Ce que l'agent avait prédit
> [Résumé de la thèse et du score en 3-4 lignes]

### Ce qui s'est réellement passé
> [Description factuelle de ce qui a fait chuter le cours ou invalidé la thèse]

### Cause racine (choisir 1 principale)
- [ ] **Macro ignorée** — le régime était défavorable mais le signal sectoriel a prévalu
- [ ] **Catalyst surévalué** — la news était moins impactante qu'estimé / déjà pricée
- [ ] **Analyste peu fiable** — upgrade d'une source avec faible track record
- [ ] **Force relative ignorée** — le titre sous-performait déjà son secteur
- [ ] **Timing erroné** — la thèse était juste mais l'entrée trop tôt
- [ ] **Risque non modélisé** — événement externe non anticipé (black swan)
- [ ] **Valorisation trop agressive** — hypothèses DCF non validées par les faits
- [ ] **Qualité bénéfices** — accruals ratio non vérifié, EPS gonflé
- [ ] **Short interest ignoré** — la pression vendeuse structurelle a persisté
- [ ] **Régime Risk-off** — pénalité macro non appliquée sur le cyclique
- [ ] **Autre :** _______________

### Analyse détaillée
> [3-5 paragraphes : qu'est-ce qui aurait dû alerter ? quel signal était là mais sous-pondéré ?
> Quel élément de l'analyse initiale était fondamentalement incorrect ?
> Qu'aurait fait un analyste expérimenté différemment ?]

### Règle extraite
> **NOUVELLE RÈGLE :** [Formulation précise et actionnable de la règle à appliquer à l'avenir]
> Exemple : "Si le score Momentum < 5/10 ET le régime est Risk-off → ne pas publier l'opportunité même si score global ≥ 6"

### Action sur le système
- [ ] Règle ajoutée dans "Règles actives" ci-dessus
- [ ] Analyste/maison noté dans Track record
- [ ] Pénalité ajoutée sur le type de signal si récurrence
- [ ] Aucune action requise (événement isolé / black swan)

**Confiance dans la règle extraite :** Faible (1 occurrence) / Moyenne (2-3 occurrences) / Forte (4+ occurrences)
```

---

## Statistiques d'apprentissage globales

| Métrique | Valeur |
|----------|--------|
| Post-mortems Opportunités réalisés | 0 |
| Post-mortems Prix Cibles réalisés | 0 |
| Post-mortems Earnings réalisés | 0 |
| **Total post-mortems** | **0** |
| Règles actives | 0 |
| Règles Faible confiance (1 occurrence) | 0 |
| Règles Moyenne confiance (2-3 occurrences) | 0 |
| Règles Forte confiance (4+ occurrences) | 0 |
| Règles invalidées (réévaluées) | 0 |
| Win rate opportunités J+20 (avant règles) | — |
| Win rate opportunités J+20 (après règles) | — |
| Taux réussite prix cibles J+90 | — |
| Précision prédictions earnings | — |
| Cause racine la plus fréquente | — |

---

## Processus de révision des règles

```
RÉVISION TRIMESTRIELLE (tous les 3 mois) :
1. Relire toutes les règles actives
2. Pour chaque règle, vérifier si elle a amélioré ou dégradé les scores depuis son ajout
3. Si une règle a été appliquée ≥ 5 fois et que le win rate sur ces signaux est > 65% → marquer "Validée"
4. Si une règle a été appliquée ≥ 5 fois et que le win rate est < 50% → invalider et ré-analyser
5. Documenter la révision ici avec la date

RÈGLE DE SURAPPRENTISSAGE :
→ Ne jamais appliquer une règle extraite d'un seul post-mortem de façon définitive
→ La marquer "Faible confiance" jusqu'à 3 occurrences confirmées
→ Une règle "Forte confiance" doit avoir ≥ 4 occurrences cohérentes
```

---

## Historique des révisions

| Date | Révision effectuée | Règles validées | Règles invalidées |
|------|-------------------|----------------|-------------------|
| — | — | — | — |

---

## 🎯 Calibration automatique des scores

> Cette section permet de détecter les **biais systématiques** du système de scoring — quand l'agent sur-score ou sous-score de façon répétée — et d'ajuster l'étalonnage global pour que les scores reflètent mieux la réalité.

### Principe

Un système de scoring est bien calibré si :
- Les opportunités scorées **8-9/10** gagnent ≥ 70% du temps
- Les opportunités scorées **6-7/10** gagnent ≥ 55% du temps
- Les prix cibles à **J+90** sont atteints à ±20% dans ≥ 60% des cas
- Les prédictions earnings sont précises (±3%) dans ≥ 50% des cas

Si ces seuils ne sont pas atteints → le système est **mal calibré** et doit être ajusté.

---

### Table de calibration — Opportunités (mise à jour trimestrielle)

| Tranche de score | Nb signaux | Gagnants J+20 | Win rate | Calibré ? | Ajustement |
|-----------------|-----------|--------------|----------|----------|-----------|
| 9–10 | 0 | — | — | — | — |
| 8–8.9 | 0 | — | — | — | — |
| 7–7.9 | 0 | — | — | — | — |
| 6–6.9 | 0 | — | — | — | — |

**Seuil de déclenchement d'un ajustement :** Win rate observé s'écarte > 15pts du win rate cible sur ≥ 10 signaux.

---

### Table de calibration — Prix cibles (mise à jour trimestrielle)

| Tranche d'upside annoncé | Nb prix cibles | Atteints ±20% J+90 | Taux réussite | Calibré ? |
|-------------------------|---------------|-------------------|--------------|----------|
| Upside > +30% | 0 | — | — | — |
| Upside +20-30% | 0 | — | — | — |
| Upside +10-20% | 0 | — | — | — |
| Upside < +10% | 0 | — | — | — |

---

### Table de calibration — Prédictions earnings (mise à jour à chaque saison d'earnings)

| Type de prédiction | Nb prédictions | Précision ≤ 3% | Approximatif 3-8% | Imprécis > 8% | Calibré ? |
|-------------------|---------------|---------------|------------------|--------------|----------|
| Beat | 0 | — | — | — | — |
| Inline | 0 | — | — | — | — |
| Miss | 0 | — | — | — | — |

---

### Détection de biais systématiques

```
ANALYSE TRIMESTRIELLE DES BIAIS :

1. BIAIS D'OPTIMISME (score systématiquement trop haut)
   → Symptôme : win rate J+20 < 45% sur les signaux 7-8/10
   → Diagnostic : l'agent sur-pondère les catalyseurs positifs
   → Correction : appliquer un malus de −0.5pt sur le Score Catalyseur jusqu'à réétalonnage

2. BIAIS DE PESSIMISME (score systématiquement trop bas)
   → Symptôme : les opportunités non publiées (score 5-6/10) performent mieux que les publiées
   → Diagnostic : l'agent est trop conservateur sur la pondération du Momentum
   → Correction : abaisser le seuil de publication à 5.5/10 temporairement

3. BIAIS SECTORIEL
   → Symptôme : win rate < 45% sur un secteur spécifique mais > 65% sur les autres
   → Diagnostic : les pondérations par défaut sont mal calibrées pour ce secteur
   → Correction : ajouter une règle de calibration sectorielle dans "Règles actives"

4. BIAIS TEMPOREL (régime de marché)
   → Symptôme : win rate chute significativement pendant les périodes Risk-off
   → Diagnostic : les bonus/malus macro ne sont pas suffisamment appliqués
   → Correction : renforcer le malus Macro sur les signaux Risk-off
```

---

### Ajustements de calibration actifs

| Ajustement | Motif | Depuis | Sur quel agent | Fin prévue |
|-----------|-------|--------|---------------|-----------|
| — | — | — | — | — |

---

### Protocole de calibration trimestrielle

```
TOUS LES 3 MOIS (coïncide avec la révision des règles) :

ÉTAPE 1 — Collecte des données
→ Compter tous les signaux publiés depuis 3 mois (BACKTESTING.md)
→ Compter les prix cibles émis et clôturés (SUIVI_PRIX_CIBLES.md)
→ Compter les prédictions earnings comparées aux réalités (SUIVI_EARNINGS_PREDICTIONS.md)

ÉTAPE 2 — Calcul des win rates par tranche
→ Remplir les 3 tables de calibration ci-dessus
→ Comparer avec les seuils cibles

ÉTAPE 3 — Détection des biais
→ Appliquer les 4 tests de biais décrits ci-dessus
→ Si biais détecté → formiger un ajustement et l'ajouter dans "Ajustements actifs"

ÉTAPE 4 — Réétalonnage
→ Ajouter l'ajustement dans "Règles actives" (en haut du fichier) avec la date
→ Surveiller l'effet pendant le trimestre suivant
→ Si ajustement inefficace → post-mortem dédié sur le biais

ÉTAPE 5 — Documentation
→ Logger la calibration dans "Historique des révisions"
```

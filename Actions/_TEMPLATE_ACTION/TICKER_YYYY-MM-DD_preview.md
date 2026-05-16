# [NOM ENTREPRISE] ([TICKER]) — Preview Earnings QX YYYY

**Date de publication :** YYYY-MM-DD (dans X jours)
**Analyse précédente :** [TICKER_YYYY-MM-DD_init.md](./TICKER_YYYY-MM-DD_init.md)
**Position ouverte :** Oui / Non — $XXX entrée

---

## Résumé exécutif

> En 2-3 phrases : qu'attend le marché, quel est le vrai enjeu de ces résultats, et quelle est la direction la plus probable.

**Probabilité beat consensus :** XX%
**Sensibilité du cours :** +/-X% si résultats conformes · +X% si beat · -X% si miss

---

## Consensus actuel

| Métrique | Consensus | Trimestre précédent | YoY attendu |
|----------|-----------|---------------------|-------------|
| Revenus | $Xb | $Xb | +/-XX% |
| EPS | $X.XX | $X.XX | +/-XX% |
| Marge brute | XX% | XX% | +/-X pts |
| EBITDA | $Xb | $Xb | +/-XX% |
| FCF | $Xb | $Xb | |

**Source des estimations :** [FMP consensus YYYY-MM-DD / Bloomberg / FactSet]
**Earnings date :** YYYY-MM-DD (pre-market / after-hours)

---

## Les 3–5 questions clés que le marché va poser (Catalyst Checklist)

| # | Question | Pourquoi c'est décisif | Seuil de réaction | Métrique à surveiller |
|---|----------|------------------------|-------------------|---------------------|
| 1 | [Question 1] | ... | Beat > X% / Miss < X% | Revenue vs consensus |
| 2 | [Question 2] | ... | Guidance relevée / abaissée | Forward guidance FY+1 |
| 3 | [Question 3] | ... | ... | Marges / Mix / FCF |
| 4 | [Question 4] | ... | ... | Segment spécifique |
| 5 | [Question 5] | ... | ... | Narratif stratégique |

---

## Scénarios — Bull / Base / Bear

| Scénario | Revenue | EPS | Key Driver | Stock Reaction | Probabilité |
|----------|---------|-----|------------|----------------|-------------|
| **🟢 Bull** | $Xb (+X% vs cons.) | $X.XX (+X%) | [Driver : beat large + guidance relevée + catalyseur] | +X% à +Y% | XX% |
| **🟡 Base** | $Xb (±X% cons.) | $X.XX (±X%) | [Driver : en ligne + guidance stable] | ±X% | XX% |
| **🔴 Bear** | $Xb (−X% vs cons.) | $X.XX (−X%) | [Driver : miss + guidance abaissée + inquiétude] | −X% à −Y% | XX% |

**Pour chaque scénario :**
- Qu'est-ce qui doit arriver operationnellement pour atteindre ce scénario ?
- Quel commentaire du management signalerait ce scénario ?
- Contexte historique : comment le stock a-t-il réagi sur des prints similaires ?

---

## Trading Setup — Niveaux techniques & Options

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| Cours actuel | $XXX | |
| Support clé | $XXX | |
| Résistance clé | $XXX | |
| **Implied move from options** | ±X% | [Calculé depuis options chain : (call+put most active ATM) / cours] |
| Volume moyen 20j | XXM | |
| Volume 5 derniers jours | XXM | Accumulation / Distribution / Neutre |
| Short interest | XX% float | Faible <5% / Modéré 5-15% / Élevé >15% |
| Options flow (calls/puts) | X:X | Biais haussier / baissier / neutre |
| Révisions consensus (30j) | X upgrades / X downgrades | Momentum analyst positif / négatif |

**Post-earnings levels :**
| Scénario | Cours cible post-earnings | Action technique |
|----------|--------------------------|-----------------|
| Beat + guidance relevée | $XXX (+X%) | Breakout résistance → renforcement possible |
| Inline consensus | $XXX (+/-X%) | Dans la range → conserver / attendre |
| Miss ou guidance abaissée | $XXX (−X%) | Support testé → réduire si cassé |

---

## Impact sur la thèse

**Thèse actuelle :** [copier depuis INDEX.md]

**Ce qui confirmerait la thèse :**
- ...

**Ce qui remettrait en cause la thèse :**
- ...

---

## Plan d'action post-résultats

| Résultat | Action suggérée |
|----------|----------------|
| Beat + guidance relevée | Renforcer / Conserver — prix cible révisé à $XXX |
| Inline | Conserver — thèse inchangée |
| Miss | Réduire / Couper — réévaluation thèse nécessaire |

---

## Liens

- [Retour à l'index](./INDEX.md)
- [Analyse initiale](./TICKER_YYYY-MM-DD_init.md)
- Résultats à venir : [TICKER_YYYY-MM-DD_earnings.md](./TICKER_YYYY-MM-DD_earnings.md) (à créer post-publication)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE À LA CRÉATION

> Ce bloc est rempli par l'agent immédiatement après avoir complété ce fichier.
> Ces données serviront à évaluer la précision des prédictions après la publication des résultats.

```
ACTION REQUISE après sauvegarde de ce fichier :
→ Ouvrir Actions/SUIVI_EARNINGS_PREDICTIONS.md
→ Ajouter la ligne suivante dans le journal :
| [DATE PREVIEW] | [TICKER] | [DATE EARNINGS] | $[EPS CONSENSUS] | [RECO PREVIEW] | +X% si beat | -X% si miss | XX% | — | — | — | — | — | ⏳ En attente | — |
→ Ajouter dans "Fenêtres en attente" :
| [TICKER] | [DATE PREVIEW] | [DATE EARNINGS] | Enregistré ✅ |
```

**Données à enregistrer (prédictions) :**
- Date earnings : [YYYY-MM-DD]
- EPS consensus : $[X.XX]
- Revenus consensus : $[Xb]
- Réaction prédite si **beat** : +[X]%
- Réaction prédite si **inline** : ±[X]%
- Réaction prédite si **miss** : -[X]%
- Probabilité de beat estimée : [XX]%
- Métrique clé à surveiller : [Revenus / EPS / Guidance / Marges / ...]

```
ACTION REQUISE lors de la création du _earnings.md correspondant :
→ Revenir dans SUIVI_EARNINGS_PREDICTIONS.md
→ Compléter la ligne avec les données réelles :
  - EPS réel · Surprise EPS · Revenus réels · Surprise revenus · Réaction cours effective
→ Calculer le verdict (✅ Précis / ⚠️ Approximatif / ❌ Imprécis)
→ Si ❌ Imprécis → déclencher le post-mortem earnings
```

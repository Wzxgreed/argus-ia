# Analyst Track Record

Ce fichier documente la précision historique des analystes sell-side et des maisons de courtage sur les tickers de la watchlist. Il est lu par l'Agent Sentiment pour pondérer les upgrades/downgrades selon la fiabilité de la source.

**Mise à jour :** À chaque nouveau rating analysté détecté + vérification trimestrielle des prix cibles précédents.

---

## Règle de calcul de la précision

```
Précision analyste = (Nombre de recommandations correctes) / (Total recommandations) × 100

"Correcte" = le cours a atteint le prix cible dans les 12 mois suivant la publication
  OU la direction a été bonne (Buy → cours +, Sell → cours −) sur 6 mois

Biais = Moyenne des écarts (Prix cible − Prix réalisé) :
  Positif = analyste systématiquement trop optimiste
  Négatif = analyste systématiquement trop conservateur
```

---

## Registry par maison de courtage

### Grandes banques — réputation sectorielle générale

| Maison | Points forts sectoriels | Précision estimée (général) | Note |
|--------|------------------------|---------------------------|------|
| Goldman Sachs | Tech, Banques, Macro | ~65% | Souvent précurseur de tendance |
| Morgan Stanley | Tech, Consumer | ~63% | Bons modèles de valorisation |
| JPMorgan | Toutes catégories | ~60% | Large coverage, signal dilué |
| Bank of America | Énergie, Consumer | ~58% | — |
| Wedbush | Tech, Software | ~67% | Spécialiste tech — fiable |
| Piper Sandler | Tech, Healthcare | ~62% | — |
| Evercore ISI | Banques, Industriels | ~64% | Très suivi par les institutionnels |
| Wolfe Research | Banques, Autos | ~65% | Très respecté sur les financières |
| SVB Securities | Biotech | ~60% | Spécialiste biotech |
| Cowen | Biotech, Tech | ~58% | — |
| UBS | Consommation, Luxe | ~61% | Fort sur le secteur luxe européen |
| Bernstein | Consommation | ~63% | Analyses en profondeur |

> **Important :** Ces chiffres sont des estimations générales de l'industrie. Les mettre à jour avec les données réelles observées sur la watchlist.

---

## Registry par analyste — Watchlist

> À remplir au fur et à mesure des analyses.

| Analyste | Maison | Secteur(s) | Tickers couverts sur watchlist | Précision calculée | Biais | Dernière mise à jour |
|---------|--------|-----------|-------------------------------|-------------------|-------|---------------------|
| — | — | — | — | — | — | — |

---

## Historique des recommandations suivies

> Pour chaque upgrade/downgrade détecté sur un ticker watchlist, enregistrer ici pour calcul de précision dans 12 mois.

| Date | Analyste | Maison | Ticker | Type | Prix cible annoncé | Cours au moment | Verdict à 12 mois | Correct ? |
|------|---------|--------|--------|------|-------------------|----------------|------------------|-----------|
| — | — | — | — | — | — | — | — | — |

---

## Règles de pondération actives

Ces règles sont appliquées par l'Agent Sentiment lors du scoring :

| Condition | Pondération |
|-----------|------------|
| Analyste avec précision > 65% sur ce secteur | ×1.5 sur le signal analyste |
| Analyste avec précision > 70% (rare, top tier) | ×2.0 sur le signal analyste |
| Analyste inconnu / boutique sans historique | ×0.7 (signal atténué) |
| Analyste avec précision < 45% | ×0.5 (signal fortement atténué) |
| Analyste avec biais > +20% (trop optimiste) | Ajuster prix cible à la baisse de 15% |
| Upgrade après hausse de cours > +20% | Signal affaibli — "laggard upgrade", ×0.6 |

---

## Patterns à documenter

| Pattern | Comportement observé | Action |
|---------|---------------------|--------|
| Cluster d'upgrades | ≥ 3 maisons upgradent en 1 semaine | Signal très fort — +1 pt Catalyseur |
| Upgrade contradictoire | Une maison upgrada seule à contre-courant | Creuser la thèse — souvent précurseur |
| Downgrade lors d'un creux | Analyste downgrade après −30% | Signal contrarian positif potentiel |
| Prix cible régulièrement relevé | Série de hausses progressives de PT | Tendance haussière fondamentale confirmée |

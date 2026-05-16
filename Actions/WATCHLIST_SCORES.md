# Watchlist — Scores & Radar du Jour

**Mis à jour le :** YYYY-MM-DD (chaque matin après la Phase 2 du bulletin)
**Régime macro actif :** [Normal / Risk-off / Risk-on / Pré-FOMC / Stagflation / Récession]
**Pondération du jour :** Catalyseur ×XX% · Valorisation ×XX% · Momentum ×XX%

> Ce fichier est la **vue de synthèse** de toute la watchlist. Il est mis à jour automatiquement à chaque bulletin du matin.
> Pour le détail d'un ticker, lire son `INDEX.md` et ses fichiers `_update.md`.

---

## 🏆 Tableau de bord — Scores du jour

| Ticker | Nom | 📊 Cat. | 💰 Val. | 📈 Mom. | 🎯 Score Final | Tendance | Qualité | Prochain Catalyseur | Dernière MAJ |
|--------|-----|--------|--------|--------|---------------|----------|---------|---------------------|-------------|
| | | /10 | /10 | /10 | /10 | ↑ ↓ → | ✅⚠️🔴 | | |

> **Tendance :** ↑ score en hausse vs J-1 · → stable · ↓ score en baisse
> **Qualité :** ✅ Quality Compounder · ⚠️ Quality Partielle · 🔴 Hors périmètre

---

## 🚨 Alertes actives du jour

| Ticker | Type d'alerte | Condition | Valeur actuelle | Statut |
|--------|--------------|-----------|----------------|--------|
| | Composite / Simple | | | 🔴 Déclenchée / 🟡 Proche / 🟢 OK |

---

## 📡 Radar supply chain — Signaux du jour

| Ticker watchlist | Entité impactante | Criticité | Événement | Impact estimé |
|-----------------|-------------------|-----------|-----------|---------------|
| | | 🔴/🟡 | | |

> Vide si aucun signal supply chain détecté ce jour.

---

## 📐 Révisions d'estimations — Momentum (30 derniers jours)

| Ticker | Révisions Hausse | Révisions Baisse | Solde Net | Momentum | Signal |
|--------|-----------------|-----------------|-----------|----------|--------|
| | +X | −X | +X / −X | ↑↑ / ↑ / → / ↓ / ↓↓ | |

---

## 📅 Prochains catalyseurs (30 jours)

| Date | Ticker | Événement | Impact attendu | Preview créé |
|------|--------|-----------|---------------|-------------|
| | | Earnings / FOMC / Conf. / Produit | 🔴🟡🟢 | Oui / Non |

---

## 📊 Historique des scores (7 derniers jours)

> Permet de détecter les tendances d'amélioration ou dégradation progressive.

| Ticker | J-6 | J-5 | J-4 | J-3 | J-2 | J-1 | Aujourd'hui | Tendance 7j |
|--------|-----|-----|-----|-----|-----|-----|-------------|-------------|
| | | | | | | | | ↑↑ / ↑ / → / ↓ / ↓↓ |

---

## 🔗 Corrélations watchlist — Alertes du jour

> Si un ticker bouge de >3%, les corrélés sont automatiquement vérifiés.
> Voir `Actions/CORRELATIONS_WATCHLIST.md` pour la matrice complète.

| Ticker en mouvement | Variation | Tickers corrélés impactés | Corrélation | Action recommandée |
|--------------------|-----------|--------------------------|-------------|-------------------|
| | | | >0.7 | Vérifier exposition |

---

## 📝 Notes du jour

> Observations transversales, thèmes dominants, régime macro.

*[Notes libres du bulletin du matin]*

---

## Protocole de mise à jour

```
CHAQUE MATIN — après la Phase 2 du bulletin :

1. Mettre à jour la date et le régime macro actif en en-tête
2. Pour chaque ticker watchlist :
   a. Récupérer le cours actuel via `quote`
   b. Calculer les 3 scores (ou les reprendre du _update.md si créé ce jour)
   c. Calculer le Score Final avec la pondération du jour (régime Macro)
   d. Mettre à jour la tendance (vs score J-1)
   e. Mettre à jour le prochain catalyseur
3. Scanner les alertes actives (simples et composites)
4. Insérer les signaux supply chain détectés en Phase 0b
5. Mettre à jour le momentum des révisions d'estimations
6. Décaler l'historique 7 jours (supprimer J-7, ajouter Aujourd'hui)
7. Identifier les mouvements >3% et vérifier les corrélés
```

---

## Légende des scores

| Score | Signal |
|-------|--------|
| 8–10 | 🟢 Fort — opportunité active |
| 6–7.9 | 🟡 Modéré — à surveiller |
| 4–5.9 | ⚪ Neutre |
| 2–3.9 | 🔴 Faible — éviter ou couvrir |
| 0–1.9 | 🔴🔴 Très faible — signal de sortie |

# Watchlist — Scores & Radar du Jour

**Mis à jour le :** 2026-05-17
**Régime macro actif :** Stagflation
**Pondération du jour :** Catalyseur ×35% · Valorisation ×40% · Momentum ×25%

> Ce fichier est la **vue de synthèse** de toute la watchlist. Il est mis à jour automatiquement à chaque bulletin du matin.
> Pour le détail d'un ticker, lire son `INDEX.md` et ses fichiers `_update.md`.

---

## 🏆 Tableau de bord — Scores du jour

| Ticker | Nom | 📊 Cat. | 💰 Val. | 📈 Mom. | 🎯 Score Final | Tendance | Qualité | Prochain Catalyseur | Dernière MAJ |
|--------|-----|--------|--------|--------|---------------|----------|---------|---------------------|-------------|
| NVDA | NVIDIA Corp | 7.5 | 6.0 | 6.5 | **6.7** | → | ✅ | Earnings 20 mai | 2026-05-16 |
| XOM | ExxonMobil | 5.5 | 6.5 | 7.0 | **6.3** | ↑ | ✅ | Pétrole $105 | 2026-05-16 |
| IREN | IREN Limited | 7.5 | 2.5 | 5.5 | **4.51** | ↓↓ | ⚠️ | Earnings aujourd'hui (J0) | 2026-05-17 |
| VRT | Vertiv Holdings | 5.5 | 4.5 | 5.5 | **5.1** | → | ⚠️ | — | 2026-05-16 |
| RTX | RTX Corp | 5.0 | 5.5 | 4.0 | **5.0** | ↓ | ✅ | — | 2026-05-16 |
| AAPL | Apple Inc. | 5.0 | 5.0 | 5.0 | **5.0** | → | ⚠️ | Données manquantes | 2026-05-16 |

> **Tendance :** ↑ score en hausse vs J-1 · → stable · ↓ score en baisse
> **Qualité :** ✅ Quality Compounder · ⚠️ Quality Partielle · 🔴 Hors périmètre

---

## 🚨 Alertes actives du jour

| Ticker | Type d'alerte | Condition | Valeur actuelle | Statut |
|--------|--------------|-----------|----------------|--------|
| IREN | Simple — Stop-loss | Cours < $54.20 | $52.86 (low) | 🔴 Déclenchée |
| IREN | Simple — Baisse | Cours < $54.20 | $52.94 | 🔴 Déclenchée |
| NVDA | Composite — Earnings proche | ≤ 5j | 4j | 🟡 Proche |
| IREN | Composite — Earnings immédiat | ≤ 3j | 1j | 🔴 Proche |

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
| 2026-05-17 | IREN | Earnings Q4 FY26 | 🔴 Élevé — verdict transition | 🟢 Oui (dans bulletin) |
| 2026-05-20 | NVDA | Earnings Q1 FY27 | 🔴 Élevé — barre haute | 🟡 En cours |

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
| IREN | -9.35% | NVDA (deal $3.4B) | 0.65 | 🟡 Vérifier exposition NVDA si IREN déçoit |
| XOM | +4.07% | — | — | 🟢 Isolé — pas de corrélés watchlist |
| NVDA | -4.42% | VRT (partenaire) | 0.55 | ⚪ Corrélation modérée — pas d'action |

---

## 📝 Notes du jour

**Régime Stagflation actif** — CPI 3.8%, pétrole $105+, 10Y 4.595%. Pondération du jour : Catalyseur ×35% · Valorisation ×40% · Momentum ×25%.

**Thèmes dominants :**
1. **Énergie en outperform** — WTI +4.2%, Brent +3.35%. XOM (+4.07%) profite du régime Stagflation historiquement favorable au secteur.
2. **Tech / IA pullback pré-earnings** — NVDA (-4.42%) et VRT (-1.41%) reculent avec la remontée des taux longs. NVDA offre un point d'entrée technique sur fondamentaux solides (earnings 20 mai).
3. **Infrastructure IA nervosité** — IREN gap -9.35% sans catalyseur fondamental identifiable. Nervosité pré-earnings (demain 17 mai). Thèse fondamentale ($13.1B contrats, moat électrique) intacte mais stop-loss technique dépassé ($52.86 < $54.20).
4. **Nouveau ticker watchlist** — AAPL ajouté aujourd'hui. Analyse initiale en cours, données techniques manquantes dans `latest.json` (à récupérer lors du prochain run `fetch_prices.py`).

**Alertes actives :**
- IREN : stop-loss déclenché, earnings binaire demain — surveillance obligatoire
- NVDA : earnings dans 4j — barre haute, réduire le sizing si entrée

**Prochaines étapes :**
- Attendre earnings IREN demain (17 mai) → préparer `_earnings.md`
- Préparer preview NVDA earnings (20 mai)
- Récupérer données AAPL complètes (RSI, ATR, FMP consensus, options)

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

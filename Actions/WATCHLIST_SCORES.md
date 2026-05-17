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
| IREN | IREN Limited | 7.5 | 2.5 | 5.5 | **4.51** | ↓↓ | ⚠️ | Transition BTC→HPC/IA | 2026-05-17 |
| VRT | Vertiv Holdings | 8.5 | 3.0 | 7.0 | **5.43** | → | ✅ | Earnings Q1 FY2026 | 2026-05-17 |
| NOK | Nokia Corporation | 3.0 | 2.0 | 4.5 | **2.48** | → | 🔴 | Surévaluation massive | 2026-05-17 |
| SOFI | SoFi Technologies | 6.0 | 5.0 | 3.0 | **4.85** | → | ⚠️ | Earnings Q1 FY2026 / Fed juin | 2026-05-17 |
| AAL | American Airlines | 3.5 | 4.0 | 4.5 | **3.95** | → | 🔴 | Earnings Q1 / WTI / Fed | 2026-05-17 |

> **Tendance :** ↑ score en hausse vs J-1 · → stable · ↓ score en baisse
> **Qualité :** ✅ Quality Compounder · ⚠️ Quality Partielle · 🔴 Hors périmètre

---

## 🚨 Alertes actives du jour

| Ticker | Type d'alerte | Condition | Valeur actuelle | Statut |
|--------|--------------|-----------|----------------|--------|
| IREN | Simple — Stop-loss | Cours < $54.20 | $52.86 (low) | 🔴 Déclenchée |
| IREN | Simple — Baisse | Cours < $54.20 | $52.94 | 🔴 Déclenchée |
| NOK | Simple — Stop-loss | Cours < $12.03 | $13.95 | 🟢 Active |

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
| IREN | -9.35% | VRT (data center) | 0.40 | ⚪ Faible corrélation |
| VRT | -1.41% | IREN (data center) | 0.40 | ⚪ Faible corrélation |

---

## 📝 Notes du jour

**Régime Stagflation actif** — CPI 3.8%, pétrole $105+, 10Y 4.595%. Pondération du jour : Catalyseur ×35% · Valorisation ×40% · Momentum ×25%.

**Thèmes dominants :**
1. **Reset complet — base propre pour apprentissage** — Toutes les analyses historiques ont été supprimées. Seuls IREN, VRT et NOK ont une analyse initiale complète basée sur des données réelles.
2. **Infrastructure IA / Data center** — IREN (-9.35%) et VRT (-1.41%) corrélés faiblement au secteur. IREN stop-loss dépassé ($52.86 < $54.20). VRT RSI 68.4 proche suracheté, put/call 3.41 extrêmement baissier.
3. **Value trap confirmé** — NOK (P/E 87, cours +50% vs consensus $9.26) hors périmètre qualité. Pas de position.

**Alertes actives :**
- IREN : stop-loss déclenché — surveillance obligatoire
- VRT : put/call 3.41 extrême, RSI proche suracheté — risque de correction
- NOK : surévaluation massive — éviter

**Prochaines étapes :**
- Surveiller earnings IREN (si disponibles) → préparer `_earnings.md`
- Vérifier fenêtres J+30/J+90/J+180 des prix cibles IREN ($65.86), VRT ($400), NOK ($9.26)
- Lancer le pipeline du matin pour récupérer les données actualisées

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

# TEST — Mise à jour quotidienne

> **Date :** 2026-06-08
> **Type :** Mise à jour post-session
> **Source :** data/latest.json (snapshot 10:00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-03 | 2026-06-08 | Δ |
|------------|-----------|------------|---|
| Cours close | $45.901 | $43.527 | **-5.16%** |
| Previous close | — | $45.468 | -4.27% session |
| RSI 14j | 46.74 | 41.19 | **-5.55 pts** |
| MM 50j | $43.41 | $43.54 | +$0.13 |
| Volume session | 1,700 | 5,000 | **+194%** |
| Volume vs avg 20j | 0.78× | 2.06× | — |
| Score Global | 66.0/100 | 49.0 (36.0 ajusté) | **-17.0 pts** |
| Score Opportunité | 6.1/10 | 4.9/10 | -1.2 pt |
| Score Momentum | 7.3/10 | 2.5/10 | **-4.8 pts** |
| Score Catalyseur | — | 6.5/10 | — |
| Score Valorisation | — | 5.0/10 | — |
| Verdict | ACHETER (Réduit) | **SURVEILLER** | 🔴 Changement |
| SL | $43.84 | $41.59 | Révisé |
| TP | $48.99 | $46.44 | Révisé |

**Changement majeur :** le verdict passe de **ACHETER (Réduit)** à **SURVEILLER** sur la base d'une dégradation technique sévère (momentum effondré de 7.3 à 2.5) et d'une perte de -5.2% sur 5 séances.

---

## Mise à jour technique

- **Cours :** $43.527, en repli de -4.27% sur la session et -5.16% vs le snapshot du 03/06 à $45.901.
- **Support clé :** MM50 à $43.54 — le cours clôture quasi exactement sur cette moyenne ($43.527, écart -$0.013). Franchissement à la baisse de la MM50 confirmerait un signal de distribution à moyen terme.
- **RSI 14j :** 41.19, en chute de 5.55 pts depuis le 03/06. Sortie de la zone neutre (40-60) vers la zone de survente légère (<40). Un RSI < 35 renforcerait le signal de survente.
- **Volume :** 5,000, soit 2.06× la moyenne 20j (2,430). Activité inhabituelle en hausse sur fond de baisse = signe de distribution/vente aggressive.
- **ATR 14j :** $0.97 (stable vs précédent).

**Verdict timing :** Défavorable. Cours sous pression, momentum cassé, volume de vente.

---

## Mise à jour sentiment / scores agents

Données issues de `data/recommandations_latest.json` (2026-06-08) :

| Axe | Score | Évolution |
|-----|-------|-----------|
| Catalyseur | 6.5/10 | Stable |
| Valorisation | 5.0/10 | Stable |
| Momentum | **2.5/10** | 🔴 Effondré |
| Opportunité | 4.9/10 | -1.2 pt |

- **Catalyseur stable à 6.5/10** : pas de nouvelle événement détecté.
- **Valorisation stable à 5.0/10** : sans données fondamentales (P/E, market cap absents), le score reste neutre.
- **Momentum en chute libre à 2.5/10** : le titre perd son momentum haussier. Cours sous MM50 (signal technique baissier).

**Modules agents :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-05-17) : aucun flag géopolitique pour TEST.
- `quality_report_latest.json` (2026-05-17) : TEST non scanné (données fondamentales indisponibles).
- Accounting / sector rotation / social sentiment / FX / event-driven / upcoming events : fichiers absents pour cette date.

---

## Révision des niveaux SL / TP

Calculs ATR-based (cours $43.527, ATR $0.97) :

| Niveau | Formule | Valeur |
|--------|---------|--------|
| Stop-loss | Cours - 2×ATR | $41.59 |
| Take-profit | Cours + 3×ATR | $46.44 |
| Ratio R/R | 2.91 / 1.94 | **1.5** |

**Note :** les niveaux ont été révisés à la baisse suite au repli du cours. Le SL à $41.59 correspond à -4.5% sous le cours actuel.

---

## Conclusion — Thèse modifiée

**La thèse est MODIFIÉE.** Le verdict passe de **ACHETER (Réduit)** à **SURVEILLER**.

**Raisons :**
1. **Momentum cassé** : le Score Momentum est passé de 7.3 à 2.5/10 en 5 séances, signalant une rupture de la dynamique haussière.
2. **Perte technique** : -5.16% sur 5 séances avec volume ×2 la moyenne sur baisse.
3. **Test de la MM50** : le cours est revenu exactement sur sa MM50 ($43.54). Un franchissement à la baisse ouvrirait la voie vers le support des 52 semaines à $40.27.
4. **Score Global** : chute de 66.0 à 49.0/100 (36.0 ajusté), sortie de la zone ACHETER.

**Prochaines étapes :**
- Surveiller le comportement autour de la MM50 ($43.54) dans les 24-48h.
- Si clôture sous MM50 + RSI < 35 → risque d'invalidation complète de la thèse (passage ÉVITER).
- Si rebond sur MM50 avec volume > 1.5× moyenne → possible retour en ATTENDRE.
- Earnings JOUR J le 2026-06-08 — résultats non observables dans le snapshot 10h UTC.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json, data/recommandations_latest.json*

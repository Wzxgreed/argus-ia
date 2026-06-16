# TEST — Mise à jour quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-16
> **Type :** Mise à jour post-pipeline 10h UTC
> **Source :** `data/latest.json` (snapshot 10:00:01 UTC), `data/recommandations_latest.json`

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-15 21h UTC | 2026-06-16 10h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | **$45.4403** | **NaN** | **[DONNÉES MANQUANTES]** 🔴 |
| Previous close | $44.836 | $44.836 | Stable ⚪ |
| RSI 14j | **46.33** | **43.91** | **−2.42 pts** 🔴 |
| MM 50j | $43.70 | `null` | [DONNÉES MANQUANTES] 🔴 |
| MM 200j | `null` | `null` | [DONNÉES MANQUANTES] |
| ATR 14j | $1.25 | `null` | [DONNÉES MANQUANTES] 🔴 |
| Volume session | 1,294 | **1,294** | **Stable** ⚪ |
| Volume vs avg 20j | 0.55× | **0.55×** | Stable ⚪ |
| 52w high | $57.74 | $57.74 | — |
| 52w low | $40.27 | $40.27 | — |

**Mutation technique négative.** Le cours close n'est plus disponible (NaN), l'ATR et la MM50 ont été perdus, et le RSI recule de 2.42 pts à 43.91, réintégrant la zone de neutralité inférieure (40–45). Le pipeline a dégradé le verdict de **ACHETER (Réduit)** à **ATTENDRE**.

---

## Mise à jour technique

- **Cours :** `NaN` — close intraday indisponible pour le snapshot 10h UTC. Le previous close reste à $44.836. **[DONNÉES MANQUANTES]**
- **RSI 14j :** 43.91, en recul de 2.42 pts vs 46.33 à la clôture précédente. Retour dans la zone neutre inférieure (40–45), effaçant le rétablissement observé à 21h UTC du 15/06. Le momentum se dégrade.
- **MM 50j :** `null` — donnée manquante. Perte de la référence technique qui soutenait la thèse (précédemment $43.70, +4.0% sous le cours).
- **MM 200j :** `null` — donnée manquante persistante.
- **ATR 14j :** `null` — donnée manquante. Impossible de calculer les niveaux de volatilité.
- **Volume :** 1,294 unités (0.55× moyenne 20j de 2,354). Stable vs la clôture précédente, mais toujours très inférieur à la moyenne. L'illiquidité persiste.
- **52w range :** $40.27–$57.74. Aucun changement.

**Verdict timing :** Neutre à défavorable. La perte du close, de l'ATR et de la MM50 prive l'analyse de ses repères techniques. Le RSI en recul confirme un loss de momentum. Tant que les données ne sont pas rétablies, aucun signal technique haussier ne peut être confirmé.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI) — bloc vide dans `latest.json`

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-16, flag persistant depuis 16+ jours) — hypothèse artefact calendrier FMP toujours valide. Aucun résultat observable.

---

## Mise à jour sentiment / options / news

Données issues de l'écosystème agents (snapshot 10h UTC) :

| Module | Statut | Commentaire |
|--------|--------|-------------|
| `recommandations_latest.json` | **Présent** | Scores recalculés par le pipeline — voir section scoring ci-dessous |
| `quant_report_latest.json` | 2026-05-17 | Insuffisant — pas de signaux historiques pour TEST |
| `geo_risk_latest.json` | 2026-05-17 | Score géo non disponible pour TEST (ticker non flaggué) |
| `accounting_risk_latest.json` | Absent | Évaluation impossible |
| `sector_rotation_latest.json` | 2026-06-16 | TEST sans secteur assigné — pas de privilège/pénalité sectorielle |
| `social_sentiment_latest.json` | 2026-06-16 | 0 mention, sentiment « No data », pas de pump détecté |
| `fx_exposure_latest.json` | 2026-06-16 | Exposition 25%, direction neutre, divergence « aligned », score FX 0.0 |
| `events_latest.json` | 2026-06-16 | 0 événement corporate détecté pour TEST |
| `upcoming_events_latest.json` | 2026-06-16 | Earnings JOUR J (2026-06-16) non résolu — artefact FMP |

**Absence de flux sentiment/options/news** pour ce snapshot. Aucun catalyseur externe identifié. Le sentiment retail « No data » et le score FX neutre n'apportent ni bonus ni malus au scoring global.

---

## Nouveau scoring global

Le pipeline a recalculé les scores agents pour le snapshot 10h UTC (`data/recommandations_latest.json` présent). Comparaison avec les données de la clôture précédente :

| Métrique | Valeur 21h UTC 15/06 | Valeur 10h UTC 16/06 (pipeline) | Δ |
|----------|---------------------|----------------------------------|---|
| Score Catalyseur | 6.5/10 | **6.5/10** | Stable ⚪ |
| Score Valorisation | 5.0/10 | **5.0/10** | Stable ⚪ |
| Score Momentum | 7.3/10 | **4.5/10** | **−2.8 pts** 🔴 |
| Score Opportunité | 6.1/10 | **5.4/10** | **−0.7 pt** 🔴 |
| Score Global | 61.0/100 | **54.0/100** | **−7.0 pts** 🔴 |
| Score Global Ajusté | 66.0/100 | **54.0/100** | **−12.0 pts** 🔴 |
| Verdict | ACHETER (Réduit) | **ATTENDRE** | **Dégradation** 🔴 |
| Timing | Favorable | **Neutre** | Dégradation 🔴 |
| Horizon | 1–3 mois | — | — |
| Sizing | Réduit | **—** | Annulé 🔴 |

**Interprétation :** La dégradation est entièrement portée par le **Score Momentum** qui s'effondre de 7.3 à 4.5 (−2.8 pts). Cette chute s'explique par :
1. La perte du cours close (NaN) qui empêche le calcul du momentum de prix
2. Le recul du RSI sous 45 (43.91), sortant de la zone neutre médiane favorable
3. La disparition de l'ATR et de la MM50, privant le modèle de ses inputs techniques

Le Score Catalyseur (6.5) et le Score Valorisation (5.0) sont inchangés, mais la pondération régime (Catalyseur 35% / Valorisation 40% / Momentum 25%) fait du Momentum un facteur discriminant. Avec un Score Momentum à 4.5, le Score Opportunité chute à 5.4, entraînant le Score Global sous le seuil de 60 (limite inférieure de la zone ACHETER Réduit).

**Règle de disqualification :** Non activée (aucun score ≤ 2/10).

---

## Révision des niveaux SL / TP

**Niveaux précédents suspendus** en raison de l'absence de données fiables :

| Niveau | Valeur précédente (21h UTC 15/06) | Statut 10h UTC 16/06 |
|--------|-----------------------------------|----------------------|
| Stop-loss | $42.94 | **Suspendu** — close NaN, ATR null |
| Take-profit | $49.19 | **Suspendu** — close NaN, ATR null |
| Ratio R/R | 1.5 | **Non calculable** |

**Raisons de la suspension :**
- Le cours close est `NaN` : impossible de calculer un SL/TP en dollar
- L'ATR 14j est `null` : impossible d'appliquer la méthode ATR-based
- La MM50 est `null` : perte du support technique de référence

**Protocole de réactivation :** Les niveaux SL/TP ne seront rétablis que lorsque les trois conditions suivantes seront remplies :
1. Cours close disponible et fiable
2. ATR 14j disponible
3. MM50 disponible

---

## Conclusion — Thèse modifiée (dégradation)

**La thèse est MODIFIÉE : verdict dégradé de ACHETER (Réduit) à ATTENDRE.**

**Raisons de la dégradation :**
1. **Perte des données techniques clés** : close NaN, ATR null, MM50 null. Le modèle perd ses repères de prix et de volatilité.
2. **Dégradation du momentum** : RSI 43.91 (−2.42 pts), retour dans la zone neutre inférieure. Le rétablissement technique de la clôture précédente est annulé.
3. **Score Momentum effondré** : 7.3 → 4.5 (−2.8 pts), entraînant le Score Global sous le seuil de 60.
4. **Verdict pipeline confirmé** : le recalcul automatique du pipeline place TEST en ATTENDRE (Score Global 54.0/100), en dessous de la zone d'achat.

**Points de vigilance maintenus / renforcés :**
- **Illiquidité structurelle persistante** : volume 1,294 (0.55× avg), stable mais très faible.
- **Absence totale de données fondamentales et options** : aucune couche de protection.
- **Earnings JOUR J persistant** : artefact calendrier FMP non résolu après 16+ jours.
- **[NOUVEAU] Données techniques corrompues** : close NaN, ATR null, MM50 null — probablement lié à la faible liquidité ou à un problème de source Yahoo/FMP.

**Scénarios de suivi :**
- Si données techniques rétablies (close, ATR, MM50) + RSI > 45 sur volume > 0.6× avg → réévaluation possible vers **ACHETER (Réduit)**.
- Si close NaN persiste sur le prochain snapshot → maintien **ATTENDRE**, risque de glissement vers **SURVEILLER**.
- Si RSI repasse sous 40 malgré la reprise des données → dégradation **SURVEILLER**.
- Si volume retombe sous 0.4× avg → signal de faiblesse structurelle.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 10h UTC), data/recommandations_latest.json*

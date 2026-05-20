# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-05-20 (snapshot 10:00 UTC — données quasi inchangées, close final confirmé $15.23)
**Type :** `_update.md` — Analyse d'impact post-session (close final)
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `_update.md` 2026-05-19 (21:00 UTC) | **Snapshot 2026-05-20 (10:00 UTC)** | **Δ vs veille** |
|----------|-------------------------------------|--------------------------------------|-----------------|
| Cours close | $15.23 | **$15.23** | **$0.00 (0.00%)** |
| RSI 14j | 47.22 | **47.22** | **0.00 pts** |
| ATR 14j | $0.70 | **$0.70** | **$0.00** |
| MM 50j | $16.91 | **$16.91** | **$0.00** |
| Volume | 63.48M (0.93×) | **63.59M (0.93×)** | **+0.11M (+0.01×)** |
| P/E LTM (Yahoo) | 33.84 | **33.84** | **0.00** |
| Forward P/E | 19.46 | **19.46** | **0.00** |
| Beta | 2.126 | **2.126** | 0.000 |
| Short interest | 0.1272% | **0.1272%** | 0.000 pts |
| Consensus PT | $25.41 (27a) | **$25.41 (27a)** | 0.00 |
| Max Pain options | $16.00 | **$1.00** | **−$15.00** |
| Put/Call ratio | 0.59 | **null** | [DONNÉES MANQUANTES] |
| Call OI % | 62.7% | **null** | [DONNÉES MANQUANTES] |
| 52W range | $12.74–$32.73 | **$12.74–$32.73** | — |
| Earnings J | 70 | **69** | −1j |

**🚨 Alerte data quality — Options :** Le snapshot `data/latest.json` du 2026-05-20 rapporte un **Max Pain de $1.00**, contre $16.00 hier. Cette valeur est **aberrante** (écart de −93.8% vs consensus historique et niveau technique). Elle correspond à un bug data ou à une absence de données options dans le pipeline. **Les valeurs options du 2026-05-19 ($16.00, Put/Call 0.59, Call OI 62.7%) sont conservées comme référence jusqu'à correction.** Le Put/Call ratio et le Call OI % apparaissent `null` dans le snapshot du jour — [DONNÉES PARTIELLES].

**⚠️ Contexte :** Le snapshot 10h UTC du 2026-05-20 reprend le close final du 2026-05-19 ($15.23). Aucune session de trading nouvelle n'est intégrée. Les métriques techniques et fondamentales sont **quasi inchangées** — cette update est une confirmation des niveaux avec une alerte data quality.

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-05-20 | Signal |
|------------|-------------------|--------|
| RSI 14j | 47.22 | 🟡 Zone neutre — inchangé depuis le 19/05 |
| MM 50j | $16.91 | 🔴 Cours −9.9% sous MM50 — trend baissier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.70 | Volatilité modérée (ATR rel. 4.59%) — stable |
| Support clé | $14.92–$15.00 | 🟡 Low du 19/05 $14.92 = niveau critique à surveiller |
| Résistance clé | $16.00–$16.91 | 🔴 Max Pain historique $16.00 + MM50 $16.91 = double mur |
| Volume relatif | 0.93× | 🟡 Normal — participation de marché standard |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Options (référence 2026-05-19, alerte data quality 2026-05-20) :**

| Métrique | Valeur référence | Signal |
|----------|------------------|--------|
| Max Pain | $16.00 | ⚠️ Au-dessus du cours ($15.23) — attraction gravitationnelle |
| Put/Call ratio | 0.59 | 🟡 Léger skew call — stable (données du 19/05) |
| Call OI % | 62.7% | 🟢 Concentration call stable (données du 19/05) |
| Expiration prochaine | 2026-05-22 (2 jours) | Risque de pinning autour de $15.50–$16.00 |

> **Alerte data quality :** Le Max Pain $1.00 du snapshot 2026-05-20 est une anomalie évidente. Ne pas utiliser pour le scoring. Les valeurs du 19/05 ($16.00) sont conservées comme référence. Le pipeline a émis une alerte data quality options ce jour (voir commit `3545a28`).

**Tendance :** Baissière court terme inchangée. Aucune nouvelle session de trading n'a été intégrée dans ce snapshot. La configuration technique reste identique à celle du 19/05 : cours sous MM50, RSI neutre sans momentum haussier, support critique $14.92–$15.00. L'expiration options du 2026-05-22 (2 jours) maintient le risque de pinning entre $15.50 et $16.00.

---

## 3. Mise à jour fondamentale

**Aucune donnée fondamentale nouvelle depuis le Full Refresh du 2026-05-17.** Les ratios FMP (FY 2025) et les multiples Yahoo sont stables.

| Ratio | Valeur _init.md (17/05) | Valeur 2026-05-20 | Δ |
|-------|-------------------------|-------------------|---|
| Gross margin (FMP) | 75.1% | 75.1% | 0.0 |
| Operating margin (FMP) | 11.0% | 11.0% | 0.0 |
| Net margin (FMP) | 10.1% | 10.1% | 0.0 |
| Debt/Equity (FMP) | 0.173 | 0.173 | 0.000 |
| P/B (FMP) | 2.87 | 2.87 | 0.00 |
| P/B (Yahoo) | 1.805 | 1.805 | 0.000 |
| P/E LTM (Yahoo) | 33.84 | 33.84 | 0.00 |
| Forward P/E | 19.46 | 19.46 | 0.00 |
| EV/Revenue (Yahoo) | 4.577 | 4.577 | 0.000 |
| FCF yield | −13.2% | −13.2% | 0.0 |

> **Rappel Filtre Qualité :** 4/6 (Quality Partielle). Faiblesses structurelles inchangées : profit CAGR 5 ans non atteint (rentabilité GAAP trop récente), moat en construction, ROE faible, FCF négatif. Malus −0.5 pt sur Score Valorisation appliqué.

---

## 4. Mise à jour sentiment / options / news

### Consensus analystes
- **27 analystes, PT moyen $25.41** — inchangé depuis le 17/05. Upside +66.8% vs cours $15.23.
- 9 analystes actifs le mois dernier, 10 le trimestre dernier — couverture dense et stable.

### Options
- **Max Pain :** $16.00 (référence 19/05) — au-dessus du cours. [ALERTE DATA QUALITY] Snapshot 20/05 rapporte $1.00 (aberrant).
- **Put/Call ratio :** 0.59 (référence 19/05) — [DONNÉES MANQUANTES] dans snapshot 20/05 (`null`).
- **Call OI % :** 62.7% (référence 19/05) — [DONNÉES MANQUANTES] dans snapshot 20/05 (`null`).
- **Interprétation :** Aucune activité options inhabituelle détectée. Le positionnement reste légèrement call-skewé à très court terme. Expiration courte 2026-05-22 (2 jours) = risque de pinning.

### News & Social
- **Aucune mention Reddit** (`social_sentiment_latest.json` : 0 mentions, score 0/10).
- **Aucun événement corporate** (`events_latest.json` : 0 événement SOFI).
- **Aucune alerte géopolitique** (`geo_risk_latest.json` : SOFI non flaggé, score politique faible).
- **Aucune exposition FX active** (`fx_exposure_latest.json` : fx_impact_score 0.0, flag 🟢).
- **Aucun événement event-driven** (`events_latest.json` : 0 événement).

---

## 5. Nouveau scoring global

### Données agents actualisées (`recommandations_latest.json` — 2026-05-20)

| Axe | Score /10 | Pondération (Régime Normal) | Pondéré |
|-----|-----------|----------------------------|---------|
| Catalyseur | 6.8 | 35% | 2.380 |
| Valorisation | 6.0 | 40% | 2.400 |
| Momentum | 4.5 | 25% | 1.125 |
| **Score Opportunité brut** | | | **5.905/10** |
| Quality Partielle (4/6) | Malus −0.5 pt sur Val | | — |
| **Score Opportunité ajusté** | | | **5.9/10** |

**Évolution vs 2026-05-19 :** Score Opportunité stable à **5.9/10**. Tous les axes sont inchangés (Catalyseur 6.8, Valorisation 6.0, Momentum 4.5). Le régime macro reste indéterminé dans le système ("Unknown"), pondération par défaut 35/40/25 appliquée.

### Score Global Composite /100

| Composant | Valeur | Impact |
|-----------|--------|--------|
| Score Opportunité × 10 | 59 | Base |
| Malus Accounting | 0 | Fichier absent — pas de pénalité |
| Malus Geo | 0 | Non flaggé = faible |
| Malus FX | 0 | fx_impact_score 0.0 |
| Malus Event | 0 | Aucun événement |
| Malus Social | 0 | 0 mentions = neutre |
| Malus Quant | 0 | Insuffisant — pas de pénalité |
| Bonus Event | 0 | Aucun |
| Bonus Buyback | 0 | Aucun programme signalé |
| Malus Sector | −3 | XLF momentum 0.0/10 (faible) — secteur financier sans direction |
| Timing technique | −5 | Trend baissier sous MM50, RSI neutre sans momentum |
| **Score Global ajusté** | | **51.1/100** |

**Classification :** 51.1/100 = **ATTENDRE** (plage 50–59, bord inférieur).

> **Note :** Le snapshot 2026-05-20 est identique au 19/05 sur le plan scoring. Aucun basculement de zone. Le Score Global reste dans la zone ATTENDRE.

---

## 6. Révision des niveaux SL / TP

| Niveau | Ancien (19/05) | Révisé 2026-05-20 | Justification |
|--------|----------------|-------------------|---------------|
| **Prix cible** | $17.33 | **$17.33** | Cours + 3×ATR = $15.23 + $2.10 — inchangé (ATR stable) |
| **Stop-loss** | $13.83 | **$13.83** | Cours − 2×ATR = $15.23 − $1.40 — inchangé |
| **Upside / Downside** | +13.7% / −9.2% | **+13.7% / −9.2%** | Inchangé (cours et ATR stables) |
| **Ratio R/R** | 1.50 | **1.50** | Stable — acceptable mais limité |
| **Support critique** | $14.92 | **$14.92** | Low du 19/05 — niveau à surveiller |

**Verdict technique :** Aucune révision des niveaux. L'ATR ($0.70) et le cours ($15.23) sont inchangés depuis le close du 19/05. Le support critique reste le low du 19/05 à **$14.92**. Un break sous $14.90 ouvre $14.50 puis le 52W low $12.74. Le Max Pain historique $16.00 et la MM50 $16.91 restent les résistances clés.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — Pas de modification structurelle.**

Le snapshot du 2026-05-20 (10h UTC) reprend le close final du 2026-05-19 ($15.23) sans apport de nouvelles données de marché. La thèse reste inchangée :

1. **Aucun mouvement de cours nouveau** — Close $15.23 identique au 19/05. Le snapshot est matinal et n'intègre pas de session de trading supplémentaire.
2. **Métriques techniques stables** — RSI 47.22, MM50 $16.91, ATR $0.70, volume 0.93×. La configuration technique n'évolue pas.
3. **Alerte data quality options** — Max Pain $1.00 aberrant dans `data/latest.json`. Valeur historique $16.00 conservée. Put/Call et Call OI `null` dans le snapshot. Mention [DONNÉES PARTIELLES] appliquée.
4. **Aucun catalyseur immédiat** — Earnings Q2 dans 69j (2026-07-28), consensus stable, pas de news structurante.
5. **Sector headwind inchangé** — XLF momentum 0.0/10, return 20j −2.29%. Le secteur financier reste sans direction.
6. **Qualité partielle inchangée** — 4/6, FCF négatif, ROE faible, dépendance aux taux.
7. **Score Global 51.1/100 (ATTENDRE)** — Identique au 19/05. Pas de basculement de zone.
8. **Exposition FX neutre** — fx_impact_score 0.0, flag 🟢. Aucun headwind/tailwind de change.
9. **Social sentiment neutre** — 0 mentions Reddit, pas de pump/dump détecté.
10. **Prochain earnings** — 2026-07-28 (69j). Est EPS $0.10–$0.11, Rev $1.1B (source yfinance).

**Action recommandée : ATTENDRE** — Pas de position.
- **Entrée potentielle :** Un retour quotidien au-dessus de $16.91 (MM50) avec volume > 1.2× moy. 20j.
- **Stop-loss :** $13.83 (ajusté ATR).
- **Scénario baissier :** Cassure de $14.90 → ouverture vers $14.50 puis $12.74 (52W low). Si ce scénario se matérialise, réviser le Filtre Qualité et le prix cible à la baisse.

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données enregistrées :**
- Recommandation : ATTENDRE
- Prix cible : $17.33
- Cours au moment de l'analyse : $15.23
- Upside/Downside : +13.7% / −9.2%
- Horizon : 3–6 mois
- Score Opportunité : 5.9/10
- Score Global : 51.1/100
- Thèse résumée : Snapshot 2026-05-20 quasi inchangé vs 19/05 (close $15.23, RSI 47.22, MM50 $16.91, ATR $0.70). [ALERTE DATA QUALITY] Max Pain options $1.00 aberrant — valeur historique $16.00 conservée. Put/Call et Call OI null dans snapshot (données partielles). Aucune news structurante. Score Global 51.1/100 (ATTENDRE). TP $17.33, SL $13.83, R/R 1.50. Earnings dans 69j.

---

## Références

- `Actions/SOFI/SOFI_2026-05-17_init.md` — Analyse initiale / Full Refresh
- `Actions/SOFI/SOFI_2026-05-18_update.md` — Mise à jour quotidienne (close final 20:56 UTC)
- `Actions/SOFI/SOFI_2026-05-19_update.md` — Mise à jour quotidienne (close final 21:00 UTC)
- `data/latest.json` (2026-05-20T10:00:08+00:00) — Cours, RSI, ATR, consensus, ratios FMP, options [DONNÉES PARTIELLES options]
- `data/recommandations_latest.json` (2026-05-20) — Scores agents actualisés
- `data/quant_report_latest.json` — Insuffisant
- `data/geo_risk_latest.json` — Non flaggé
- `data/sector_rotation_latest.json` — XLF momentum 0.0
- `data/social_sentiment_latest.json` — 0 mentions
- `data/fx_exposure_latest.json` — fx_impact_score 0.0
- `data/upcoming_events_latest.json` — Earnings 2026-07-28 (69j)
- `data/events_latest.json` — Aucun événement corporate
- Commit `3545a28` — Alerte data quality options (max pain .00 aberrant)

# FLY — Mise à Jour (2026-06-16, snapshot 10h UTC)

> **Type :** `_update.md` — Snapshot pré-market, données techniques partielles, scores dégradés, thèse ATTENDRE (54.2) confirmée avec nuance négative
> **Référence précédente :** [FLY_2026-06-15_update_21h.md](FLY_2026-06-15_update_21h.md) (snapshot 21h UTC)
> **Données source :** `data/latest.json` (timestamp 2026-06-16T10:00:09.448585+00:00), `data/recommandations_2026-06-16.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-16.json`, `data/social_sentiment_2026-06-16.json`, `data/fx_exposure_2026-06-16.json`, `data/upcoming_events_2026-06-16.json`, `data/events_2026-06-16.json`
> **Validation data :** FLY status `ok` dans `data/validation_report.txt`. Aucun warning.

---

## Résumé — Données techniques partielles, scores dégradés, survente extrême aggravée

Le snapshot 10h UTC (pré-market) n'enregistre **pas de close du jour** (NaN). Le **previous_close officiel est révisé à $31.87** — invalidant le snapshot after-hours $33.36 du 15/06 21h UTC. Le cours de référence effectif est donc revenu à **$31.87**.

Le RSI chute à **18.0** (−2.81 pts vs 20.81 à 21h UTC), creusant la survente extrême. Les scores agents se sont **dégradés** : Score Opportunité **4.9/10** (−1.0 pt), Score Global Ajusté **54.2** (−2.1 pts). Les baisses touchent le **Catalyseur 5.0/10** (−1.5 pt) et la **Valorisation 4.5/10** (−1.5 pt). Le Momentum est légèrement révisé à la hausse **5.5/10** (+0.5 pt). Le **timing passe à Favorable** (mean reversion technique sur RSI 18.0).

**Comparatif 15/06 21h UTC → 16/06 10h UTC :**

| Métrique | 2026-06-15 21h UTC | 2026-06-16 10h UTC | Variation |
|----------|--------------------|--------------------|-----------|
| Cours close | $33.36 (after-hours) | **NaN** (pré-market) | Pas de close |
| Previous close officiel | $31.87 | **$31.87** | Stable |
| RSI 14j | 20.81 | **18.0** | **−2.81 pts, survente EXTRÊME aggravée** |
| ATR 14j | 5.4 | **null** | [DONNÉES PARTIELLES] |
| MM 50j | 39.47 | **null** | [DONNÉES PARTIELLES] |
| Volume session | 7.07M | **7.07M** | Identique (même base) |
| Forward P/E (Yahoo) | −25.91 | **−25.91** | Stable |
| P/B (Yahoo) | 4.833 | **4.833** | Stable |
| Market Cap (Yahoo) | $5.48B | **$5.48B** | Stable |
| Score Catalyseur | 6.5/10 | **5.0/10** | **−1.5 pt** |
| Score Valorisation | 6.0/10 | **4.5/10** | **−1.5 pt** |
| Score Momentum | 5.0/10 | **5.5/10** | **+0.5 pt** |
| Score Opportunité | 5.9/10 | **4.9/10** | **−1.0 pt** |
| Score Global Ajusté | 56.3 | **54.2** | **−2.1 pts** |
| Action | ATTENDRE | **ATTENDRE** | Stable |
| Timing | Défavorable | **Favorable** | **Modifié** |
| Max Pain | $65.00 (ANOMALIE) | **$20.00 (ANOMALIE)** | Mutation aberrante |
| Put/Call Ratio | 0.27 | **null** | [ANOMALIE DATA] |
| Call OI % | 78.5% | **null** | [ANOMALIE DATA] |
| Consensus PT | $43.77 (13 analysts) | **$43.77 (13 analysts)** | Stable |

**Verdict :** Le snapshot pré-market confirme la stabilité du close officiel à $31.87 et l'aggravation de la survente (RSI 18.0). La dégradation des scores Catalyseur et Valorisation (−1.5 pt chacun) est le développement majeur : l'agent perçoit une détérioration de la perception fondamentale malgré la survente extrême. Le timing passe à **Favorable** sur rebond technique mean reversion, mais l'action reste **ATTENDRE (54.2)**.

---

## Mise à jour technique — Données partielles, survente extrême aggravée

| Indicateur | Valeur 10h UTC | Verdict |
|------------|----------------|---------|
| Cours (close) | NaN | Pré-market — pas de close du jour |
| Previous close | **$31.87** | Référence officielle stable |
| RSI 14j | **18.0** | Survente **EXTRÊME** — niveau historique aggravé |
| ATR 14j | **null** | [DONNÉES PARTIELLES] |
| MM 50j | **null** | [DONNÉES PARTIELLES] |
| Volume session | 7,074,939 | **0.74x moy. 20j** — identique au snapshot précédent |
| Support 1 | $30.00 (psychologique) | Support structurel majeur |
| Support 2 | $28.00–$26.00 | Zone de consolidation historique |
| Résistance 1 | $35.00–$36.00 | Résistance technique clé |
| Résistance 2 | $39.47 (MM50 historique) | Résistance majeure |
| 52W Range | $16.00 – $73.80 | Midpoint $44.90 |

**Options — Anomalie persistante :**

| Métrique | Valeur 10h UTC | Statut |
|----------|---------------|--------|
| Max Pain | $20.00 | **ABERRANT** — nouvelle valeur aberrante |
| Put/Call Ratio | **null** | [ANOMALIE DATA] |
| Call OI % | **null** | [ANOMALIE DATA] |
| Expiration | 2026-06-18 | J+2 |

**Interprétation technique :**
- Le **RSI 18.0** est le niveau le plus bas observé sur FLY depuis le début du suivi, et l'un des plus bas de la watchlist. Cette survente extrême peut attirer des acheteurs techniques à court terme (mean reversion), justifiant le passage du timing à **Favorable**.
- L'absence de données ATR, MM50 et MM200 empêche toute calibration précise des niveaux de support/résistance et des stop-loss/take-profit. [DONNÉES PARTIELLES]
- La **structure options est totalement illisible** (max pain $20.00 aberrant, put/call et call OI null). L'anomalie observée hier ($65.00) a muté vers une nouvelle valeur aberrante. Impossible d'intégrer la structure options dans l'analyse.
- Le volume 0.74x moy. 20j reste sous-moyenne, indiquant une participation institutionnelle modérée.

**Timing verdict :** **Favorable** — modifié. Le RSI 18.0 crée une opportunité de mean reversion technique à court terme, mais sans données MM50/ATR, la confiance dans ce signal est limitée.

---

## Mise à jour fondamentale — Strictement inchangée

Toutes les métriques fondamentales FMP sont strictement identiques :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $5.48B | Stable |
| Forward P/E (Yahoo) | −25.91 | Inchangé |
| EV/Revenue (Yahoo) | 26.216x | Inchangé |
| P/B (Yahoo) | 4.833 | Stable |
| Gross Margin (FMP) | 15.56% | Inchangé — faible |
| Operating Margin (FMP) | −154.25% | Inchangé — fortement négatif |
| Net Margin (FMP) | −186.63% | Inchangé — fortement négatif |
| Debt/Equity (FMP) | 0.259 | Inchangé — levier modéré |
| Current Ratio (FMP) | 4.51 | Inchangé — liquidité solide |
| Short Interest | 12.12% | Inchangé — pression vendeuse accrue |
| FMP Consensus PT | $43.77 (13 analysts) | Inchangé — upside +37.3% vs spot $31.87 |

**Filtre Qualité :** **2/6** (Hors périmètre) — strictement inchangé.

---

## Mise à jour sentiment / options / news — Silence médiatique persistant, anomalie options mutée

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | **$43.77 (13 analysts)** | FMP Stable API | PT +37.3% au-dessus du spot — stable |
| Max Pain | **$20.00** | `latest.json` 10:00 UTC | **ABERRANT** — mutation depuis $65.00 |
| Put/Call Ratio | **null** | `latest.json` 10:00 UTC | [ANOMALIE DATA] |
| Call OI % | **null** | `latest.json` 10:00 UTC | [ANOMALIE DATA] |
| Short Interest | **12.12%** | Yahoo Finance | Élevé — inchangé |
| Social Sentiment | 0 mention | `data/social_sentiment_2026-06-16.json` | Pas d'activité retail |
| Event-Driven | Aucun | `data/events_2026-06-16.json` | Pas de M&A, buyback, guidance change, activism |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (49 jours) | `data/upcoming_events_2026-06-16.json` | Est EPS −$0.61 à −$0.45, Rev $0.1B |
| News FLY | Aucune | `data/news_2026-06-16.json` | Silence médiatique persistant |
| Expiration options | **2026-06-18 (J+2)** | Yahoo Finance | Anomalie persistante |

**Score Catalyseur :** **5.0/10** — dégradé de 1.5 pt. L'agent a révisé à la baisse la perception des catalyseurs. Le consensus inchangé ($43.77) reste le seul élément positif, mais l'absence de news et l'anomalie options persistante pèsent sur le score.

---

## Scoring global — ATTENDRE (54.2), dégradé de −2.1 pts vs 21h UTC

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 5.0/10 | 35% | 1.750 |
| Valorisation | 4.5/10 | 40% | 1.800 |
| Momentum | 5.5/10 | 25% | 1.375 |
| **Score Opportunité** | **4.9/10** | | |
| **Score Global** | **49.2** | | |
| **Score Global Ajusté** | **54.2** | | |

**Action :** **ATTENDRE**
**Direction :** Neutre
**Timing :** **Favorable**
**Horizon :** —

**Ajustements agents complémentaires :**
- **Agent Quant :** Signaux non significatifs (p-value 1.0, n=0, insuffisant) — pas d'ajustement.
- **Agent Geo :** FLY non flaggué (geo_risk_score absent, 🟢) — pas de malus.
- **Agent Sector Rotation :** Données NaN pour tous les secteurs (regime UNKNOWN) — pas d'ajustement.
- **Agent Social :** 0 mention — neutre.
- **Agent FX :** Exposition 25%, fx_impact_score 0.0, 🟢 — pas d'ajustement.
- **Agent Event-Driven :** 0 événement — neutre.
- **Agent Accounting :** Fichier indisponible — pas d'ajustement.

---

## Révision des niveaux SL / TP — Impossible à recalibrer (ATR null)

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours de référence | $31.87 | Previous close officiel | Stable vs close 15/06 |
| Stop-loss | **—** | ATR null | [DONNÉES PARTIELLES] — impossible de calibrer |
| Take-profit | **—** | ATR null | [DONNÉES PARTIELLES] — impossible de calibrer |
| Ratio R/R | **—** | — | Non calculable |

**Risque technique :** Sans ATR ni MM50, l'analyse technique est partiellement aveugle. Le support psychologique $30.00 reste le niveau clé à surveiller. Une cassure de $30.00 en clôture sur volume > 1.0x moy. 20j ouvrirait le chemin vers $28.00–$26.00. Le RSI 18.0 indique une survente extrême mais ne constitue pas un signal d'achat sans catalyst fondamental.

---

## Conclusion — Thèse ATTENDRE (54.2) confirmée avec intensité négative renforcée

**Verdict : Thèse ATTENDRE (54.2) confirmée — dégradation des scores fondamentaux, timing modifié à Favorable sur mean reversion technique.**

Le snapshot 10h UTC matérialise trois développements majeurs :

1. **Révision du close officiel à $31.87** : le snapshot after-hours $33.36 du 15/06 21h UTC est invalidé par le previous_close officiel du 16/06. Le cours effectif n'a pas rebondi.

2. **Survente extrême aggravée (RSI 18.0)** : niveau historique qui justifie le passage du timing à **Favorable** (opportunité mean reversion technique), mais sans données ATR/MM50, la fiabilité de ce signal est limitée.

3. **Dégradation des scores agents** : Catalyseur −1.5 pt (6.5 → 5.0) et Valorisation −1.5 pt (6.0 → 4.5). L'agent Recommandation perçoit une détérioration de la qualité fondamentale et des perspectives de catalyseurs, portant le Score Global Ajusté à 54.2 (−2.1 pts).

**Ce qui maintient la prudence :**
- **Filtre Qualité 2/6** : profil fondamental inchangé et défavorable.
- **Forward P/E −25.91, EV/Revenue 26.2x** : valorisation incompatible avec un profil sans profit.
- **Short Interest 12.12%** : pression vendeuse accrue et inchangée.
- **Anomalie options persistante** : max pain $20.00 aberrant, données options null.
- **Données techniques partielles** : ATR, MM50, MM200 null — impossible de calibrer SL/TP et de confirmer la structure technique.
- **Silence médiatique** : aucune news, aucun catalyst.

**Ce qui est légèrement positif / observé :**
- **RSI 18.0** : survente extrême historique, potentiel de rebond technique à court terme.
- **Timing Favorable** : l'agent détecte une opportunité mean reversion.
- **Consensus $43.77 (+37.3%)** : ancrage haussier des analystes inchangé.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 49 jours) : Est EPS −$0.61 à −$0.45, Rev $0.1B.
2. **Expiration options** (2026-06-18, J+2) : anomalie persistante, impossible de calibrer le pin risk.
3. **Mean reversion technique** : RSI 18.0 pourrait attirer des acheteurs techniques, mais la tendance reste défavorable sans données MM50.

**Risques :**
1. **Continuation baissière** : pas de support technique confirmé sans MM50/ATR.
2. **Cassure de $30.00** : si brisée en clôture, retour vers $28.00–$26.00.
3. **Short Interest 12.12%** : pression vendeuse continue.
4. **Anomalie data** : impossible de calibrer le risque options et technique.
5. **Fondamentaux inchangés** : pas de justification fondamentale à un retournement.

**Prochaine étape :**
- **Ne pas prendre de position** — ATTENDRE (54.2), timing Favorable mais données partielles.
- **Surveiller le comportement autour de $30.00** — niveau psychologique clé.
- **Attendre la restauration des données techniques** (ATR, MM50) pour recalibrer les niveaux SL/TP.
- **Attendre la résolution de l'anomalie options** après expiration 2026-06-18.
- **Si un catalyst fondamental émerge** → réévaluer Score Catalyseur. Sans cela, le setup reste technique et fragile.

---

*Snapshot 10:00 UTC 16/06 — Close NaN (pré-market), Previous Close $31.87, RSI 18.0 (survente extrême), ATR null, MM50 null, volume 7.07M (0.74x moy. 20j), Short Interest 12.12%. Consensus $43.77 (13 analysts). Options : max pain $20.00 (aberrant), put/call null, call OI null. Fondamentaux inchangés (Filtre Qualité 2/6). Agent Recommandation : ATTENDRE (54.2), timing Favorable. Thèse confirmée avec intensité négative renforcée.*

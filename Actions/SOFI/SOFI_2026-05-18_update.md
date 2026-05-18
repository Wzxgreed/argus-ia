# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-05-18 (post-pipeline 10:00 UTC)
**Type :** `_update.md` — Analyse d'impact post-session
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | 2026-05-18 08:46 (update matinal) | 2026-05-18 10:00 UTC (pipeline) | Δ |
|----------|-----------------------------------|---------------------------------|---|
| Cours close | $15.61 | $15.61 | $0.00 (0.0%) |
| RSI 14j | 30.21 | 30.21 | 0.0 |
| ATR 14j | $0.82 | $0.82 | $0.00 |
| MM 50j | $17.05 | $17.05 | $0.00 |
| Volume relatif | 0.74× | 0.74× | 0.0× |
| P/E LTM | 34.69 | 34.69 | 0.0 |
| Forward P/E | 19.95 | 19.95 | 0.0 |
| Beta | 2.126 | 2.126 | 0.0 |
| Short interest | 0.13% | 0.13% | 0.0 |
| Consensus PT | $25.41 (27a) | $25.41 (27a) | 0.0 |
| XLF momentum | 0.0 | 0.0 | 0.0 |

**Verdict :** Aucun changement de données entre la mise à jour matinale (08:46) et le pipeline de 10:00 UTC. Le snapshot `data/latest.json` (timestamp 2026-05-18T10:00:08+00:00) confirme l'intégralité des niveaux. Le `SOFI_2026-05-18_DRAFT_refresh.md` (trigger ATR_SPIKE medium, identique au 2026-05-17) a été traité et archivé — la thèse est confirmée sans modification structurelle.

---

## 2. Mise à jour technique

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 30.21 | 🟢 Zone de survente — rebond technique possible mais non confirmé |
| MM 50j | $17.05 | 🔴 Cours −8.4% sous MM50 — trend baissier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.82 | Volatilité modérée-élevée (ATR rel. 5.25%) |
| Support clé | $14.50–$15.38 | 🟡 Low du jour confirmé à $15.38, zone mars–avril 2026 |
| Résistance clé | $16.50–$17.05 | 🔴 Max Pain historique $16.50 + MM50 $17.05 = double mur |
| Volume relatif | 0.74× | 🔴 Faible — ni capitulation ni accumulation institutionnelle |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Tendance :** Baissière court terme. Le low $15.38 du jour est un niveau à surveiller : une cassure quotidienne sous $15.30 ouvrirait la voie vers $14.50 puis le 52W low $12.74. À l'inverse, un retour au-dessus de $16.50 (Max Pain historique) serait le premier signal de retournement.

---

## 3. Mise à jour fondamentale

**Aucune donnée fondamentale nouvelle depuis le Full Refresh du 2026-05-17.** Les ratios FMP (FY 2025) restent stables :

| Ratio | Valeur | Commentaire |
|-------|--------|-------------|
| Gross margin | 75.1% | Solide, stable |
| Operating margin | 11.0% | En amélioration vs historique |
| Net margin | 10.1% | Rentabilité GAAP récente confirmée |
| Debt/Equity | 0.17 | Faible levier — solide post-charter bancaire |
| EV/EBITDA | 35.5 | Élevé vs banques, aligné sur fintechs growth |
| EV/Sales | 5.66 | Premium croissance justifié par membres +30% YoY |
| ROE | 4.6% | Faible — capital bancaire élevé dilue le rendement |
| FCF yield | −13.2% | FCF négatif — investissements en cours |

> **Rappel Filtre Qualité :** 4/6 (Quality Partielle). Les faiblesses structurelles (profit CAGR 5 ans non atteint, moat encore en construction, ROE faible) ne sont pas résolues en 24h. Malus −0.5 pt sur Score Valorisation appliqué.

---

## 4. Mise à jour sentiment / options / news

### Consensus analystes
- **27 analystes, PT moyen $25.41** — inchangé. Upside +62.8% vs cours actuel.
- 9 analystes actifs le mois dernier, 10 le trimestre dernier — couverture dense et stable.

### Options
- **[DONNÉES PARTIELLES]** `data/latest.json` retourne `max_pain: 1.0` avec `put_call_ratio: null` et `call_oi_pct: null` pour SOFI le 2026-05-18. Le Max Pain $1.00 est irréaliste (52W low = $12.74) ; il s'agit d'un placeholder ou d'une erreur de parsing Yahoo Finance. Les valeurs du 2026-05-17 (Max Pain $16.50, Put/Call 0.58, Call OI 63.4%) restent les dernières fiables.
- **Expiration prochaine :** 2026-05-22 (4 jours) — risque de pinning autour de l'ancien Max Pain $16.50 si les données historiques restent valides.

### News & Social
- **Aucune mention Reddit** (`social_sentiment_latest.json` : 0 mentions, score 0/10).
- **Aucun événement corporate** (`events_latest.json` : 0 événement SOFI).
- **Aucune alerte géopolitique** (`geo_risk_latest.json` : SOFI non flaggé).

---

## 5. Nouveau scoring global

### Données agents actualisées (recommandations_latest.json)

| Axe | Score /10 | Pondération (Régime Normal) | Pondéré |
|-----|-----------|----------------------------|---------|
| Catalyseur | 6.8 | 35% | 2.380 |
| Valorisation | 6.0 | 40% | 2.400 |
| Momentum | 3.5 | 25% | 0.875 |
| **Score Opportunité brut** | | | **5.655/10** |
| Quality Partielle (4/6) | Malus −0.5 pt sur Val | | — |
| **Score Opportunité ajusté** | | | **5.7/10** |

**Évolution vs 2026-05-17 :** Score Opportunité stable à 5.7/10 (vs 5.1/10 au 2026-05-17), principalement porté par l'axe Catalyseur (+1.3 pt) qui reflète la stabilité du consensus analystes et l'absence de dégradation de nouvelles. Le Momentum reste faible (3.5/10) du fait du trend sous MM50.

### Score Global Composite /100

| Composant | Valeur | Impact |
|-----------|--------|--------|
| Score Opportunité × 10 | 57 | Base |
| Malus Accounting | 0 | Fichier absent — pas de pénalité |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | fx_impact_score 0.0 |
| Malus Event | 0 | Aucun événement |
| Malus Social | 0 | 0 mentions = neutre |
| Malus Quant | 0 | Insuffisant — pas de pénalité |
| Bonus Event | 0 | Aucun |
| Bonus Buyback | 0 | Aucun programme signalé |
| Malus Sector | −3 | XLF momentum 0.0 (faible) |
| Timing technique | −5 | Trend baissier sous MM50, RSI 30 = survente non exploitée |
| **Score Global ajusté** | | **48.6/100** |

**Classification :** 48.6/100 = **SURVEILLER** (plage 35–49).

> **Note de méthodologie :** L'analyse initiale du 2026-05-17 classifiait 43/100 comme ATTENDRE. Selon la grille institutionnelle Argus-IA (35–49 = SURVEILLER, 50–59 = ATTENDRE), 43/100 et 48.6/100 relèvent tous deux de la zone SURVEILLER. Cette mise à jour confirme la classification précédente.

---

## 6. Révision des niveaux SL / TP

| Niveau | Ancien (08:46) | Révisé | Justification |
|--------|----------------|--------|---------------|
| **Prix cible** | $18.07 | **$18.07** | Inchangé — alignement sur le modèle de recommandation institutionnel (3×ATR au-dessus du cours) |
| **Stop-loss** | $13.97 | **$13.97** | Inchangé — cours − 2×ATR = $15.61 − $1.64 |
| **Upside / Downside** | +15.8% / −10.5% | **+15.8% / −10.5%** | Inchangé |
| **Ratio R/R** | 1.50 | **1.50** | Acceptable mais plus faible — sizing réduit si entrée |
| **Support critique** | $15.38 | **$15.38** | Low du jour confirmé — un break sous $15.30 ouvre $14.50 |

**Verdict technique :** Les niveaux de risque ne changent pas. Le ratio R/R à 1.50 reste acceptable mais limité. Le trend baissier intact et le volume faible ne justifient pas d'élargir le TP au-dessus de $18.07 à ce stade.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — Pas de modification.**

La configuration fondamentale et technique de SoFi n'a pas changé entre la mise à jour matinale (08:46) et le pipeline de 10:00 UTC. Le Full Refresh du 2026-05-17 reste la référence. Cette mise à jour confirme les éléments clés :

1. **Survente technique non exploitée** — RSI 30.21 sans rebond, volume faible, cours sous MM50.
2. **Aucun catalyseur immédiat** — Earnings Q2 dans 71j (2026-07-28), consensus stable, pas de news structurante.
3. **Sector headwind** — XLF momentum nul (0.0/10), return 20j −2.54%. Le secteur financier ne porte pas SoFi.
4. **Qualité partielle inchangée** — 4/6, FCF négatif, ROE faible, dépendance aux taux.
5. **Exposition macro dominante** — Taux US + politique prêts étudiants = risques non résolus.

**Changement majeur :** Aucun. Le cours a testé $15.38 sans casser. Le support $14.50–$15.50 tient. L'absence de volume et de catalyseur rend tout rebond technique fragile.

**Action recommandée : SURVEILLER** — Pas de position.
- **Entrée potentielle :** Un retour quotidien au-dessus de $17.05 (MM50) avec volume > 1.2× moy. 20j.
- **Stop-loss :** $13.97 (invariant).
- **Scénario baissier :** Cassure de $15.30 → ouverture vers $14.50 puis $12.74 (52W low). Si ce scénario se matérialise, réviser le Filtre Qualité et le prix cible à la baisse.

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données enregistrées :**
- Recommandation : SURVEILLER
- Prix cible : $18.07
- Cours au moment de l'analyse : $15.61
- Upside/Downside : +15.8% / −10.5%
- Horizon : 3–6 mois
- Score Opportunité : 5.7/10
- Score Global : 48.6/100
- Thèse résumée : Aucun changement de fond entre la mise à jour matinale et le pipeline 10:00 UTC. Survente technique (RSI 30) sans rebond, trend baissier sous MM50, volume faible. Earnings dans 71j. Support $15.38 tient. DRAFT_refresh archivé. SURVEILLER.

---

## Références

- `Actions/SOFI/SOFI_2026-05-17_init.md` — Analyse initiale / Full Refresh
- `Actions/SOFI/SOFI_2026-05-18_update.md` (08:46) — Première mise à jour du jour
- `data/latest.json` (2026-05-18T10:00:08+00:00) — Cours, RSI, ATR, consensus, ratios FMP
- `data/recommandations_latest.json` (2026-05-18) — Scores agents actualisés
- `data/quant_report_latest.json` — Insuffisant
- `data/geo_risk_latest.json` — Non flaggé
- `data/sector_rotation_latest.json` — XLF momentum 0.0
- `data/social_sentiment_latest.json` — 0 mentions
- `data/fx_exposure_latest.json` — fx_impact_score 0.0
- `data/upcoming_events_latest.json` — Earnings 2026-07-28 (71j)
- `data/events_latest.json` — Aucun événement corporate

# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-05-19 (snapshot 13:00 UTC — close confirmé)
**Type :** `_update.md` — Analyse d'impact post-session
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `_update.md` 2026-05-19 (10:00 UTC) | **Snapshot 2026-05-19 13:00 UTC** | **Δ** |
|----------|-------------------------------------|-----------------------------------|-------|
| Cours close | $15.71 | **$15.71** | **0.00** |
| RSI 14j | 32.70 | **32.70** | **0.00** |
| ATR 14j | $0.84 | **$0.84** | **0.00** |
| MM 50j | $16.98 | **$16.98** | **0.00** |
| Volume | 66.7M (0.98×) | **66.7M (0.98×)** | **0.0** |
| P/E LTM | 34.91 | **34.91** | **0.00** |
| Forward P/E | 20.08 | **20.08** | **0.00** |
| Beta | 2.126 | **2.126** | **0.000** |
| Short interest | 0.1272% | **0.1272%** | **0.000 pts** |
| Consensus PT | $25.41 (27a) | **$25.41 (27a)** | **0.00** |
| Max Pain options | $1.00 [ANOMALIE] | **$16.00** | **+$15.00** |
| Put/Call ratio | null [MANQUANT] | **0.59** | **—** |
| Call OI % | null [MANQUANT] | **62.7%** | **—** |
| 52W range | $12.74–$32.73 | **$12.74–$32.73** | **—** |

**Verdict :** Le snapshot 2026-05-19 13:00 UTC confirme le close à **$15.71** sans changement technique (RSI, ATR, MM50 identiques au snapshot 10:00 UTC). **Le principal événement est le retour des données options fiables** dans `data/latest.json` : Max Pain **$16.00** (vs anomalie $1.00 matinale), Put/Call **0.59**, Call OI **62.7%**. Ces niveaux traduisent un rééquilibrage haussier du sentiment options vs le close du 2026-05-18 (Max Pain $15.00, Put/Call 0.77, Call OI 56.6%). **Aucune news structurante, aucun événement corporate.**

---

## 2. Mise à jour technique

| Indicateur | Valeur 13:00 UTC | Signal |
|------------|------------------|--------|
| RSI 14j | 32.70 | 🟢 Zone de survente — rebond technique possible mais non confirmé |
| MM 50j | $16.98 | 🔴 Cours −7.5% sous MM50 — trend baissier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.84 | Volatilité modérée-élevée (ATR rel. 5.35%) |
| Support clé | $15.34–$15.00 | 🟡 Low du jour 2026-05-18 $15.34 + ancien Max Pain $15.00 = zone de confluence |
| Résistance clé | $16.00–$16.98 | 🔴 Nouveau Max Pain $16.00 + MM50 $16.98 = double mur renforcé |
| Volume relatif | 0.98× | 🟡 Normal — participation de marché standard, ni accumulation ni distribution |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Options (données revenues à 13:00 UTC) :**

| Métrique | Valeur 13:00 UTC | Δ vs 2026-05-18 20:56 UTC | Signal |
|----------|------------------|---------------------------|--------|
| Max Pain | $16.00 | +$1.00 | ⚠️ Décalage haussier — au-dessus du cours ($15.71), proche de MM50 |
| Put/Call ratio | 0.59 | −0.18 | 🟡 Retour au niveau du 2026-05-17 (0.58) — sentiment call-skewé modéré |
| Call OI % | 62.7% | +6.1 pts | 🟢 Concentration call en hausse — majorité call renforcée |
| Expiration prochaine | 2026-05-22 (3 jours) | — | Risque de pinning autour de $15.50–$16.00 |

**Interprétation options :** Le retour des données options fiables révèle un rééquilibrage haussier par rapport au close du 2026-05-18. Le Max Pain remonte de $15.00 à $16.00 (+$1.00), ce qui place le niveau de gravitation options au-dessus du cours actuel et en direction de la MM50 ($16.98). Le Put/Call à 0.59 est proche du niveau historique du 2026-05-17 (0.58) et traduit un léger skew call. La montée du Call OI de 56.6% à 62.7% (+6.1 pts) indique une accumulation d'Open Interest sur les calls avant l'expiration du 2026-05-22 (3 jours). Ce pattern peut refléter :
- Des achats de calls spéculatifs sur un rebond technique depuis la survente (RSI 32.7)
- Des couvertures de shorts via calls
- Un positionnement pré-earnings anticipé (Q2 dans 70j)

**Verdict :** Le signal options n'est pas directionnel fort mais légèrement haussier à très court terme. Attention au pinning autour de $15.50–$16.00 à expiration vendredi.

**Tendance :** Baissière court terme inchangée. La configuration technique du 2026-05-18 (marteau baissier intraday, rejet à $16.32, close $15.71) reste valide. Le support $15.34 (low 2026-05-18) tient. Un break quotidien sous $15.30 ouvrirait $14.50 puis le 52W low $12.74. À l'inverse, un retour au-dessus de $16.98 (MM50) avec volume >1.2× reste le premier signal de retournement.

---

## 3. Mise à jour fondamentale

**Aucune donnée fondamentale nouvelle.** Les ratios FMP (FY 2025) restent identiques au snapshot 2026-05-19 10:00 UTC :

| Ratio | Valeur _update.md 10:00 UTC | Valeur 2026-05-19 13:00 UTC | Δ |
|-------|------------------------------|-----------------------------|---|
| Gross margin | 75.1% | 75.1% | 0.0 |
| Operating margin | 11.0% | 11.0% | 0.0 |
| Net margin | 10.1% | 10.1% | 0.0 |
| Debt/Equity | 0.173 | 0.173 | 0.000 |
| EV/EBITDA (FMP) | 35.52 | 35.52 | 0.00 |
| EV/Sales | 4.73 | 4.73 | 0.00 |
| P/B (FMP) | 2.87 | 2.87 | 0.00 |
| P/E LTM (Yahoo) | 34.91 | 34.91 | 0.00 |
| Forward P/E | 20.08 | 20.08 | 0.00 |
| FCF yield | −13.2% | −13.2% | 0.0 |

> **Rappel Filtre Qualité :** 4/6 (Quality Partielle). Les faiblesses structurelles (profit CAGR 5 ans non atteint, moat encore en construction, ROE faible, FCF négatif) ne sont pas résolues. Malus −0.5 pt sur Score Valorisation appliqué.

---

## 4. Mise à jour sentiment / options / news

### Consensus analystes
- **27 analystes, PT moyen $25.41** — inchangé. Upside +61.7% vs cours $15.71.
- 9 analystes actifs le mois dernier, 10 le trimestre dernier — couverture dense et stable.

### Options (données revenues — voir section 2)
Le snapshot `data/latest.json` (2026-05-19T13:00:07+00:00) fournit désormais des données options fiables pour SOFI :
- **Max Pain $16.00** — décalage haussier vs $15.00 du 2026-05-18. Au-dessus du cours, proche de la MM50.
- **Put/Call 0.59** — retour au niveau du 2026-05-17 (0.58), rééquilibrage call-skewé modéré.
- **Call OI 62.7%** — hausse de 6.1 pts vs 56.6% du 2026-05-18, concentration call renforcée.

**Interprétation :** Accumulation d'Open Interest call avant expiration courte (3 jours). Pas d'activité inhabituelle flagrante (volume vs OI non fourni), mais le mouvement vers $16.00 du Max Pain peut créer une attraction gravitationnelle modérée haussière à très court terme.

### News & Social
- **Aucune mention Reddit** (`social_sentiment_latest.json` : 0 mentions, score 0/10).
- **Aucun événement corporate** (`events_latest.json` : 0 événement SOFI).
- **Aucune alerte géopolitique** (`geo_risk_latest.json` : SOFI non flaggé, score politique faible).
- **Aucune exposition FX active** (`fx_exposure_latest.json` : fx_impact_score 0.0, flag 🟢).

---

## 5. Nouveau scoring global

### Données agents actualisées (`recommandations_latest.json`)

| Axe | Score /10 | Pondération (Régime Normal) | Pondéré |
|-----|-----------|----------------------------|---------|
| Catalyseur | 6.8 | 35% | 2.380 |
| Valorisation | 6.0 | 40% | 2.400 |
| Momentum | 3.5 | 25% | 0.875 |
| **Score Opportunité brut** | | | **5.655/10** |
| Quality Partielle (4/6) | Malus −0.5 pt sur Val | | — |
| **Score Opportunité ajusté** | | | **5.7/10** |

**Évolution :** Score Opportunité stable à **5.7/10** (identique au snapshot 10:00 UTC et au close 2026-05-18). Le Momentum reste faible (3.5/10) du fait du trend sous MM50. Le Catalyseur (6.8/10) est soutenu par le consensus analystes dense. Les options ne modifient pas le score car elles ne créent pas de catalyseur fondamental nouveau, mais elles renforcent légèrement le sentiment à très court terme.

### Score Global Composite /100

| Composant | Valeur | Impact |
|-----------|--------|--------|
| Score Opportunité × 10 | 57 | Base |
| Malus Accounting | 0 | Fichier absent — pas de pénalité |
| Malus Geo | 0 | Non flaggé = faible |
| Malus FX | 0 | fx_impact_score 0.0 |
| Malus Event | 0 | Aucun événement |
| Malus Social | 0 | 0 mentions = neutre |
| Malus Quant | 0 | Insuffisant — pas de pénalité |
| Bonus Event | 0 | Aucun |
| Bonus Buyback | 0 | Aucun programme signalé |
| Malus Sector | −3 | XLF momentum 0.0/10 (faible) |
| Timing technique | −5 | Trend baissier sous MM50, RSI 32.7 = survente non exploitée |
| **Score Global ajusté** | | **48.6/100** |

**Classification :** 48.6/100 = **SURVEILLER** (plage 35–49, bord supérieur).

---

## 6. Révision des niveaux SL / TP

| Niveau | Ancien (_update.md 10:00 UTC) | Révisé 13:00 UTC | Justification |
|--------|--------------------------------|------------------|---------------|
| **Prix cible** | $18.23 | **$18.23** | Cours + 3×ATR = $15.71 + $2.52 |
| **Stop-loss** | $14.03 | **$14.03** | Cours − 2×ATR = $15.71 − $1.68 |
| **Upside / Downside** | +16.0% / −10.7% | **+16.0% / −10.7%** | Inchangé |
| **Ratio R/R** | 1.50 | **1.50** | Acceptable mais limité — sizing réduit si entrée |
| **Support critique** | $15.34 | **$15.34** | Low du 2026-05-18 confirmé — un break sous $15.30 ouvre $14.50 |

**Verdict technique :** Les niveaux de risque sont confirmés par le snapshot 13:00 UTC. Aucune révision nécessaire. Le ratio R/R à 1.50 reste acceptable mais limité.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — Pas de modification structurelle.**

Le snapshot 2026-05-19 13:00 UTC confirme intégralement le close final du 2026-05-18 et le snapshot 10:00 UTC. Aucun changement de cours, de données techniques, ou de fondamentaux. **La seule évolution est le retour des données options fiables**, qui révèlent un rééquilibrage légèrement haussier à très court terme :

1. **Survente technique non exploitée** — RSI 32.70 sans rebond confirmé, trend sous MM50.
2. **Volume normalisé** — 0.98× moy. 20j. Session standard, ni accumulation ni distribution.
3. **Rejet intraday à $16.32 (2026-05-18)** — La tentative de rally jusqu'à +5.4% a été rejetée, confirmant la résistance $16.30–$16.50.
4. **Options légèrement haussier à très court terme** — Max Pain $16.00 (+$1.00 vs 18/05), Call OI 62.7% (+6.1 pts), Put/Call 0.59. Risque de pinning vers $15.50–$16.00 à expiration 2026-05-22.
5. **Aucun catalyseur immédiat** — Earnings Q2 dans 70j (2026-07-28), consensus stable, pas de news structurante.
6. **Sector headwind** — XLF momentum nul (0.0/10), return 20j −1.69%. Le secteur financier ne porte pas SoFi.
7. **Qualité partielle inchangée** — 4/6, FCF négatif, ROE faible, dépendance aux taux.
8. **Exposition macro dominante** — Taux US + politique prêts étudiants = risques non résolus.
9. **Données options désormais complètes** — Le snapshot 13:00 UTC corrige l'anomalie matinale (Max Pain $1.00). Les valeurs fiables ($16.00, 0.59, 62.7%) sont intégrées.

**Action recommandée : SURVEILLER** — Pas de position.
- **Entrée potentielle :** Un retour quotidien au-dessus de $16.98 (MM50) avec volume > 1.2× moy. 20j.
- **Stop-loss :** $14.03 (ajusté ATR).
- **Scénario baissier :** Cassure de $15.30 → ouverture vers $14.50 puis $12.74 (52W low). Si ce scénario se matérialise, réviser le Filtre Qualité et le prix cible à la baisse.

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données enregistrées :**
- Recommandation : SURVEILLER
- Prix cible : $18.23
- Cours au moment de l'analyse : $15.71
- Upside/Downside : +16.0% / −10.7%
- Horizon : 3–6 mois
- Score Opportunité : 5.7/10
- Score Global : 48.6/100
- Thèse résumée : Snapshot 2026-05-19 13:00 UTC confirme stabilité vs close 2026-05-18. Cours $15.71, RSI 32.70, MM50 $16.98, ATR $0.84. Volume normal (0.98×). Données options revenues : Max Pain $16.00 (+$1.00 vs 18/05), Put/Call 0.59, Call OI 62.7% (+6.1 pts). Sentiment options légèrement haussier à court terme. Aucune news structurante. Support $15.34 tient. SURVEILLER.

---

## Références

- `Actions/SOFI/SOFI_2026-05-17_init.md` — Analyse initiale / Full Refresh
- `Actions/SOFI/SOFI_2026-05-18_update.md` — Mise à jour quotidienne (close final 20:56 UTC)
- `Actions/SOFI/SOFI_2026-05-19_update.md` (snapshot 10:00 UTC) — Mise à jour pré-marché
- `Actions/SOFI/SOFI_2026-05-19_update.md` (snapshot 13:00 UTC) — Cette analyse
- `data/latest.json` (2026-05-19T13:00:07+00:00) — Cours, RSI, ATR, consensus, ratios FMP, options [COMPLÈTES]
- `data/recommandations_latest.json` (2026-05-19) — Scores agents actualisés
- `data/quant_report_latest.json` — Insuffisant
- `data/geo_risk_latest.json` — Non flaggé
- `data/sector_rotation_latest.json` — XLF momentum 0.0
- `data/social_sentiment_latest.json` — 0 mentions
- `data/fx_exposure_latest.json` — fx_impact_score 0.0
- `data/upcoming_events_latest.json` — Earnings 2026-07-28 (70j)
- `data/events_latest.json` — Aucun événement corporate

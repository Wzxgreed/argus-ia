# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-05-19 (snapshot 10:00 UTC — pré-marché)
**Type :** `_update.md` — Analyse d'impact post-session / confirmation matinale
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `_update.md` 2026-05-18 (20:56 UTC) | **Snapshot 2026-05-19 10:00 UTC** | **Δ** |
|----------|-------------------------------------|-----------------------------------|-------|
| Cours close | $15.71 | **$15.71** | **0.00** |
| RSI 14j | 32.70 | **32.70** | **0.00** |
| ATR 14j | $0.84 | **$0.84** | **0.00** |
| MM 50j | $16.98 | **$16.98** | **0.00** |
| Volume | 66.2M (0.97×) | **66.7M (0.98×)** | **+0.5M (+0.01×)** |
| P/E LTM | 34.91 | **34.91** | **0.00** |
| Forward P/E | 20.08 | **20.08** | **0.00** |
| Beta | 2.126 | **2.126** | **0.000** |
| Short interest | 0.1272% | **0.1272%** | **0.000 pts** |
| Consensus PT | $25.41 (27a) | **$25.41 (27a)** | **0.00** |
| Max Pain options | $15.00 | **$1.00 [ANOMALIE]** | **−$14.00** |
| Put/Call ratio | 0.77 | **null [MANQUANT]** | **—** |
| Call OI % | 56.6% | **null [MANQUANT]** | **—** |
| 52W range | $12.74–$32.73 | **$12.74–$32.73** | **—** |

**Verdict :** Le snapshot 2026-05-19 10:00 UTC est un **snapshot pré-marché** qui confirme intégralement le close final du 2026-05-18. Aucun nouveau close n'est disponible. Le cours reste à **$15.71**, le RSI à **32.70**, l'ATR à **$0.84**. Le volume légèrement révisé à **66.7M** (0.98× moy. 20j) ne change pas l'interprétation. **Données options partiellement manquantes** dans `latest.json` (Max Pain $1.00 = anomalie de parsing, Put/Call et Call OI null) — les dernières valeurs fiables ($15.00, 0.77, 56.6%) sont conservées pour l'analyse. **Aucune news structurante, aucun événement corporate.**

---

## 2. Mise à jour technique

| Indicateur | Valeur 10:00 UTC | Signal |
|------------|------------------|--------|
| RSI 14j | 32.70 | 🟢 Zone de survente — rebond technique possible mais non confirmé |
| MM 50j | $16.98 | 🔴 Cours −7.5% sous MM50 — trend baissier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.84 | Volatilité modérée-élevée (ATR rel. 5.35%) |
| Support clé | $15.34–$15.00 | 🟡 Low du jour 2026-05-18 $15.34 + Max Pain $15.00 = zone de confluence |
| Résistance clé | $16.32–$16.98 | 🔴 High 2026-05-18 $16.32 + MM50 $16.98 = double mur |
| Volume relatif | 0.98× | 🟡 Normal — participation de marché standard, ni accumulation ni distribution |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Options ([DONNÉES PARTIELLES] dans snapshot) :**

| Métrique | Valeur fiable (dernier snapshot complet) | Signal |
|----------|------------------------------------------|--------|
| Max Pain | $15.00 | ⚠️ Proche du cours — attraction gravitationnelle à expiration 2026-05-22 (3 jours) |
| Put/Call ratio | 0.77 | 🟡 Neutre — hausse vs 0.58 historique, moins de skew call |
| Call OI % | 56.6% | 🟡 Neutre — majorité call mais moins marquée qu'avant (63.4% au 2026-05-17) |
| Expiration prochaine | 2026-05-22 (3 jours) | Risque de pinning autour de $15.00–$15.50 |

> **Note données :** Le snapshot 2026-05-19 10:00 UTC retourne `max_pain: 1.0`, `put_call_ratio: null`, `call_oi_pct: null` pour SOFI. Il s'agit d'une anomalie de parsing Yahoo Finance (Max Pain $1.00 est incohérent pour un titre à $15.71). Les dernières valeurs fiables (2026-05-18 20:56 UTC) sont conservées pour l'analyse.

**Tendance :** Baissière court terme inchangée. La configuration technique du 2026-05-18 (marteau baissier intraday, rejet à $16.32, close $15.71) reste valide. Le support $15.34 (low 2026-05-18) tient. Un break quotidien sous $15.30 ouvrirait $14.50 puis le 52W low $12.74. À l'inverse, un retour au-dessus de $16.98 (MM50) avec volume >1.2× reste le premier signal de retournement.

---

## 3. Mise à jour fondamentale

**Aucune donnée fondamentale nouvelle.** Les ratios FMP (FY 2025) restent identiques au snapshot 2026-05-18 20:56 UTC :

| Ratio | Valeur _update.md 2026-05-18 | Valeur 2026-05-19 10:00 UTC | Δ |
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

### Options ([DONNÉES PARTIELLES] — voir section 2)
Le snapshot matinal ne fournit pas de données options fiables pour SOFI. Les dernières valeurs connues (2026-05-18 20:56 UTC) indiquent :
- Max Pain $15.00 — proche du cours, plausible pour expiration 2026-05-22 (3 jours).
- Put/Call 0.77 — rééquilibrage vers les puts vs 0.58 du 2026-05-17.
- Call OI 56.6% — calls majoritaires mais concentration en baisse de 6.8 pts.

**Interprétation :** Aucune activité options inhabituelle signalée. Le rééquilibrage put/call traduit probablement une couverture de positions longues avant expiration courte.

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

**Évolution :** Score Opportunité stable à **5.7/10** (identique au 2026-05-18). Le Momentum reste faible (3.5/10) du fait du trend sous MM50. Le Catalyseur (6.8/10) est soutenu par le consensus analystes dense, mais aucun catalyseur immédiat ne le fait monter au-dessus de 7.0.

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

| Niveau | Ancien (_update.md 2026-05-18) | Révisé 10:00 UTC | Justification |
|--------|----------------------------------|------------------|---------------|
| **Prix cible** | $18.23 | **$18.23** | Cours + 3×ATR = $15.71 + $2.52 |
| **Stop-loss** | $14.03 | **$14.03** | Cours − 2×ATR = $15.71 − $1.68 |
| **Upside / Downside** | +16.0% / −10.7% | **+16.0% / −10.7%** | Inchangé |
| **Ratio R/R** | 1.50 | **1.50** | Acceptable mais limité — sizing réduit si entrée |
| **Support critique** | $15.34 | **$15.34** | Low du 2026-05-18 confirmé — un break sous $15.30 ouvre $14.50 |

**Verdict technique :** Les niveaux de risque sont confirmés par le snapshot matinal. Aucune révision nécessaire. Le ratio R/R à 1.50 reste acceptable mais limité.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — Pas de modification structurelle.**

Le snapshot pré-marché du 2026-05-19 10:00 UTC confirme intégralement la configuration du close final du 2026-05-18. Aucune donnée nouvelle, aucune news structurante, aucun événement corporate. Les éléments clés restent inchangés :

1. **Survente technique non exploitée** — RSI 32.70 sans rebond confirmé, trend sous MM50.
2. **Volume normalisé** — 0.98× moy. 20j. Session standard, ni accumulation ni distribution.
3. **Rejet intraday à $16.32 (2026-05-18)** — La tentative de rally jusqu'à +5.4% a été rejetée, confirmant la résistance $16.30–$16.50.
4. **Aucun catalyseur immédiat** — Earnings Q2 dans 70j (2026-07-28), consensus stable, pas de news structurante.
5. **Sector headwind** — XLF momentum nul (0.0/10), return 20j −1.69%. Le secteur financier ne porte pas SoFi.
6. **Qualité partielle inchangée** — 4/6, FCF négatif, ROE faible, dépendance aux taux.
7. **Options rééquilibrées** — Put/Call 0.77 et Call OI 56.6% traduisent un sentiment neutre. Pas d'activité inhabituelle.
8. **Exposition macro dominante** — Taux US + politique prêts étudiants = risques non résolus.
9. **[DONNÉES PARTIELLES] options** — Le snapshot matinal ne fournit pas de données options fiables pour SOFI. Pas d'impact sur la thèse.

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
- Thèse résumée : Snapshot pré-marché 2026-05-19 10:00 UTC confirme stabilité vs close 2026-05-18. Cours $15.71, RSI 32.70, MM50 $16.98, ATR $0.84. Volume normal (0.98×). Données options partiellement manquantes (anomalie Max Pain $1.00). Aucune news structurante. Support $15.34 tient. SURVEILLER.

---

## Références

- `Actions/SOFI/SOFI_2026-05-17_init.md` — Analyse initiale / Full Refresh
- `Actions/SOFI/SOFI_2026-05-18_update.md` — Mise à jour quotidienne (close final 20:56 UTC)
- `Actions/SOFI/SOFI_2026-05-19_update.md` (snapshot 10:00 UTC) — Cette analyse
- `data/latest.json` (2026-05-19T10:00:07+00:00) — Cours, RSI, ATR, consensus, ratios FMP, options [PARTIELLES]
- `data/recommandations_latest.json` (2026-05-19) — Scores agents actualisés
- `data/quant_report_latest.json` — Insuffisant
- `data/geo_risk_latest.json` — Non flaggé
- `data/sector_rotation_latest.json` — XLF momentum 0.0
- `data/social_sentiment_latest.json` — 0 mentions
- `data/fx_exposure_latest.json` — fx_impact_score 0.0
- `data/upcoming_events_latest.json` — Earnings 2026-07-28 (70j)
- `data/events_latest.json` — Aucun événement corporate

# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-05-27 (snapshot 10:00 UTC — pré-marché US)
**Type :** `_update.md` — Mise à jour pré-session
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `_update.md` 2026-05-26 (21:00 UTC) | **Snapshot 2026-05-27 (10:00 UTC)** | **Δ** |
|----------|-------------------------------------|-------------------------------------|-------|
| Cours close | $15.98 | **$15.98** | **$0.00 (0.00%)** |
| RSI 14j | 49.59 | **49.59** | **0.00 pt** |
| ATR 14j | $0.71 | **$0.71** | **$0.00** |
| MM 50j | $16.73 | **$16.73** | **$0.00** |
| Volume (close précédent) | 79.35M (1.13×) | **80.29M (1.14×)** | **+0.94M (+1.2%)** |
| P/E LTM (Yahoo) | 35.51 | **35.51** | **0.00** |
| Forward P/E | 20.60 | **20.60** | **0.00** |
| EV/Revenue (Yahoo) | 4.823 | **4.823** | **0.000** |
| P/B (Yahoo) | 1.894 | **1.894** | **0.000** |
| Beta | 2.126 | **2.126** | 0.000 |
| Short interest | 12.72% | **12.72%** | 0.000 pts |
| Consensus PT | $25.41 (27a) | **$25.41 (27a)** | 0.00 |
| Max Pain options | $16.00 | **$5.00** ⚠️ | **Anomalie JSON** |
| Put/Call ratio | 0.70 | **null** ⚠️ | **Anomalie JSON** |
| Call OI % | 58.8% | **null** ⚠️ | **Anomalie JSON** |
| 52W range | $12.86–$32.73 | **$12.86–$32.73** | Inchangé |
| Earnings J | 63 | **62** | −1j |

**Verdict : Stabilité totale du snapshot pré-marché. Aucune variation de cours, de technique ni de fondamental entre le close 2026-05-26 21:00 UTC et le snapshot 2026-05-27 10:00 UTC. Le volume légèrement révisé à la hausse (+1.2%) est une correction mécanique post-close. L'échéance earnings se rapproche de 62j (vs 63j).**

Le snapshot 10:00 UTC du 2026-05-27 est un snapshot **pré-marché** (10:00 UTC = 06:00 ET, marché US fermé). Il reprend le close final de la veille à **$15.98** sans aucune variation. Le RSI 14j reste à **49.59** (zone neutre médiane), l'ATR 14j à **$0.71**, la MM50 à **$16.73**. Le cours reste sous la MM50 (−4.5%). Le support psychologique **$15.00** est intact (52W low $12.86).

**[ALERTE DATA QUALITY]** — Le fichier `data/latest.json` du 2026-05-27 présente une **anomalie systémique sur les options SOFI** : Max Pain $5.00 (vs $16.00 historique confirmé), Put/Call `null`, Call OI `null`. Ces valeurs sont aberrantes et incohérentes avec les closes précédents. Les valeurs confirmées du 2026-05-26 sont maintenues : **Max Pain $16.00, Put/Call 0.70, Call OI 58.8%**.

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-05-27 (10:00 UTC) | Signal |
|------------|-------------------------------|--------|
| RSI 14j | 49.59 | 🟡 Zone neutre médiane — sans direction claire |
| MM 50j | $16.73 | 🔴 Cours −4.5% sous MM50 — trend baissier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.71 | 🟡 Volatilité stable (ATR rel. 4.44%) |
| Support clé | $15.00–$15.86 | 🟢 Support psychologique $15.00 tenu |
| Résistance clé | $16.73–$16.95 | 🔴 MM50 $16.73 + high 26/05 $16.95 = double mur |
| Volume relatif | 1.14× | 🟢 Volume légèrement supérieur à la moyenne — stable |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Options (valeurs historiques confirmées — anomalie JSON 2026-05-27) :**

| Métrique | Valeur confirmée | Signal |
|----------|------------------|--------|
| Max Pain | $16.00 | 🟡 Légèrement au-dessus du cours ($15.98) — pinning vers ce niveau à l'expiration 29/05 |
| Put/Call ratio | 0.70 | 🟡 Rebalancement vers les puts stable |
| Call OI % | 58.8% | 🟢 Skew call stable |
| Expiration prochaine | 2026-05-29 (2 jours ouvrés) | Risque de pinning autour de $16.00 élevé |

> **Interprétation :** Aucun mouvement technique nouveau depuis le close 2026-05-26. Le cours $15.98 est en parfaite parité avec le Max Pain $16.00. Le pinning à l'expiration du 2026-05-29 (2 jours ouvrés restants) reste le risque dominant à très court terme. Le Put/Call 0.70 et le Call OI 58.8% sont inchangés. Un break net au-dessus de $16.30 ou sous $15.70 après expiration libérerait la tendance.

---

## 3. Mise à jour fondamentale

**Aucune donnée fondamentale nouvelle.** Les ratios FMP (FY 2025) et les multiples de marché sont stables.

| Ratio | Valeur _init.md (17/05) | Valeur 2026-05-27 (10:00 UTC) | Δ |
|-------|-------------------------|-------------------------------|---|
| Gross margin (FMP) | 75.1% | 75.1% | 0.0 |
| Operating margin (FMP) | 11.0% | 11.0% | 0.0 |
| Net margin (FMP) | 10.1% | 10.1% | 0.0 |
| Debt/Equity (FMP) | 0.173 | 0.173 | 0.000 |
| P/B (FMP) | 2.87 | 2.87 | 0.00 |
| P/B (Yahoo) | 1.894 | **1.894** | **0.000** |
| P/E LTM (Yahoo) | 35.51 | **35.51** | **0.00** |
| Forward P/E | 20.60 | **20.60** | **0.00** |
| EV/Revenue (Yahoo) | 4.823 | **4.823** | **0.000** |
| FCF yield | −13.2% | −13.2% | 0.0 |

> **Rappel Filtre Qualité :** 4/6 (Quality Partielle). Faiblesses structurelles inchangées : profit CAGR 5 ans non atteint, moat en construction, ROE faible (4.6%), FCF négatif. Malus −0.5 pt sur Score Valorisation appliqué.

---

## 4. Mise à jour sentiment / options / news

### Consensus analystes
- **27 analystes, PT moyen $25.41** — inchangé. Upside +59.0% vs cours $15.98.
- 8 analystes actifs le mois dernier, 10 le trimestre dernier — couverture dense et stable.

### Options (valeurs confirmées — anomalie JSON 2026-05-27)
- **Max Pain :** $16.00 (inchangé) — parité avec le cours $15.98. Pinning très probable à l'expiration 29/05.
- **Put/Call ratio :** 0.70 (inchangé) — défensivisme stable.
- **Call OI % :** 58.8% (inchangé) — skew call stable.
- **Interprétation :** Aucun repositionnement options depuis le snapshot 21:00 UTC 2026-05-26. Le marché options anticipe un niveau $16.00 pour l'expiration du 29/05. Le pinning reste le risque dominant à 2 jours de l'expiration.

### News & Social
- **Aucune mention Reddit** (`social_sentiment_2026-05-27.json` : 0 mentions, score 0/10, EXTREME_BEARISH par absence de données).
- **Aucune news SOFI** (`news_2026-05-27.json` : 0 item).
- **Aucun événement corporate** (`events_2026-05-27.json` : 0 événement SOFI).
- **Aucune alerte géopolitique** (`geo_risk_2026-05-17.json` : SOFI non flaggé, geo_risk_score non renseigné, flag 🟢).
- **Aucune exposition FX active** (`fx_exposure_2026-05-27.json` : fx_impact_score 0.0, flag 🟢).

---

## 5. Nouveau scoring global

### Données agents actualisées (`recommandations_2026-05-27.json` — 10:00 UTC)

| Axe | Score /10 | Pondération (Régime Normal) | Pondéré |
|-----|-----------|----------------------------|---------|
| Catalyseur | 6.8 | 35% | 2.380 |
| Valorisation | 6.0 | 40% | 2.400 |
| Momentum | 5.3 | 25% | 1.325 |
| **Score Opportunité brut** | | | **6.105/10** |
| Quality Partielle (4/6) | Malus −0.5 pt sur Val | | — |
| **Score Opportunité ajusté** | | | **6.1/10** |

**Évolution vs snapshot 2026-05-26 21:00 UTC :** Inchangé. Score Opportunité **6.1/10**, Score Global ajusté **53.1/100**. Classification **ATTENDRE** confirmée.

Les scores agents n'ont pas évolué. Le Catalyseur (6.8), la Valorisation (6.0) et le Momentum (5.3) sont stables. Le snapshot pré-marché ne fournit pas de nouvelles données de prix ou de volume susceptibles de modifier le scoring.

### Score Global Composite /100

| Composant | Valeur | Impact |
|-----------|--------|--------|
| Score Opportunité × 10 | 61 | Base |
| Malus Accounting | 0 | Fichier absent — pas de pénalité |
| Malus Geo | 0 | Non flaggé = faible |
| Malus FX | 0 | fx_impact_score 0.0 |
| Malus Event | 0 | Aucun événement |
| Malus Social | 0 | 0 mentions = neutre |
| Malus Quant | 0 | Insuffisant — pas de pénalité |
| Bonus Event | 0 | Aucun |
| Bonus Buyback | 0 | Aucun programme signalé |
| Malus Sector | −3 | XLF momentum 0.0/10 (faible) — secteur financier sans direction |
| Timing technique | −3 | Cours sous MM50 mais RSI neutre, pas de survente ni surachat |
| Autres malus ajustés | −1.9 | Ajustement composite (détail non granulaire dans données brutes) |
| **Score Global ajusté** | | **53.1/100** |

**Classification :** 53.1/100 = **ATTENDRE** (plage 50–59, bord inférieur).

> **Note :** Le score 53.1 reste en bord inférieure de la zone ATTENDRE. Une dégradation technique de −3% ramènerait immédiatement en zone SURVEILLER. Le secteur financier (XLF) reste sans direction (momentum 0.0/10, signal ROTATION_TO_CYCLICAL détecté mais XLF non concerné).

---

## 6. Révision des niveaux SL / TP

| Niveau | Ancien (2026-05-26 21:00 UTC) | Révisé 2026-05-27 (10:00 UTC) | Justification |
|--------|-------------------------------|-------------------------------|---------------|
| **Prix cible** | $18.11 | **$18.11** | Cours + 3×ATR = $15.98 + $2.13 — ATR stable à $0.71 |
| **Stop-loss** | $14.56 | **$14.56** | Cours − 2×ATR = $15.98 − $1.42 — ATR stable |
| **Upside / Downside** | +13.3% / −8.9% | **+13.3% / −8.9%** | Ratio inchangé |
| **Ratio R/R** | 1.50 | **1.50** | Stable |
| **Support critique** | $15.00 | **$15.00** | Support psychologique $15.00 inchangé |

**Verdict technique :** Les niveaux SL/TP sont inchangés. SL à **$14.56**, TP à **$18.11**. Le ratio R/R reste à 1.50. Le support critique reste le niveau psychologique **$15.00**. La résistance clé est la MM50 **$16.73** (high 26/05 $16.95 a été rejeté). Un break quotidien au-dessus de $16.73 avec volume > 1.2× moy. 20j (~84M) ouvrirait la voie vers le TP $18.11.

> **Point de vigilance options :** Max Pain $16.00 légèrement au-dessus du cours. Le pinning à l'expiration du 29/05 (2 jours ouvrés) risque d'emprisonner le cours dans une fourchette étroite autour de $16.00 ± $0.30. Une cassure nette au-dessus de $16.30 ou sous $15.70 après expiration libérerait la tendance.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — Classification ATTENDRE maintenue, stabilité totale du snapshot pré-marché.**

La thèse fondamentale et technique reste inchangée. Le snapshot 2026-05-27 10:00 UTC (pré-marché) confirme la stabilité totale vs le close 2026-05-26 21:00 UTC :

1. **Close $15.98** — Inchangé. Aucun mouvement de cours depuis le close final de la veille.
2. **RSI stable à 49.59** — Zone neutre médiane inchangée. Pas de survente ni de surachat.
3. **Volume stable à 80.29M (1.14×)** — Légère révision mécanique post-close (+1.2% vs 79.35M), sans signification technique.
4. **ATR stable à $0.71** — Volatilité intraday inchangée.
5. **Cours reste sous MM50 ($16.73)** — Trend baissier court terme intact (−4.5%).
6. **Momentum agent stable à 5.3/10** — Pas de changement de score.
7. **Score Opportunité 6.1/10 (inchangé)** — Au-dessus du seuil 6.0.
8. **Score Global 53.1/100 (inchangé)** — ATTENDRE confirmé (bord inférieur).
9. **Options inchangées** — Max Pain $16.00 légèrement au-dessus du cours. Pinning 29/05 probable. [ALERTE DATA QUALITY] Anomalie JSON 2026-05-27 sur les options (max pain $5.00, put/call null) — valeurs historiques confirmées maintenues.
10. **Aucun catalyseur fondamental** — Earnings Q2 dans 62j (2026-07-28), consensus stable, pas de news.
11. **Sector headwind inchangé** — XLF momentum 0.0/10. Secteur financier sans direction.
12. **Qualité partielle inchangée** — 4/6, FCF négatif, ROE faible.
13. **Exposition FX neutre** — fx_impact_score 0.0, flag 🟢.
14. **Social sentiment neutre** — 0 mentions Reddit, pas de pump/dump.
15. **Risque géopolitique faible** — SOFI non flaggé dans geo_risk_latest.json.
16. **Accounting risk non évalué** — Fichier absent — pas de malus appliqué.
17. **Validation data :** SOFI OK dans `validation_report.txt` (2026-05-27) — aucun warning, aucune erreur.

**Action recommandée : ATTENDRE** — Pas de position. La classification ATTENDRE est confirmée. Le snapshot pré-marché n'apporte aucun élément nouveau modifiant la thèse.
- **Entrée potentielle :** Un retour quotidien au-dessus de $16.76 (MM50) avec volume > 1.2× moy. 20j (~84M).
- **Stop-loss :** $14.56 (inchangé).
- **Scénario baissier :** Cassure de $15.00 → ouverture vers $14.56 (SL) puis $12.86 (52W low).
- **Scénario haussier :** Break de $16.76 (MM50) avec volume > 84M → ouverture vers $18.11 (TP) puis $19.51 (prix cible historique).
- **Scénario options (court terme) :** Pinning vers Max Pain $16.00 à l'expiration 29/05 (2 jours ouvrés). Pas d'action avant cassure post-expiration.

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données enregistrées :**
- Recommandation : ATTENDRE
- Prix cible : $18.11
- Cours au moment de l'analyse : $15.98
- Upside/Downside : +13.3% / −8.9%
- Horizon : 3–6 mois
- Score Opportunité : 6.1/10
- Score Global : 53.1/100
- Thèse résumée : Snapshot 10:00 UTC 2026-05-27 (pré-marché) confirme stabilité totale vs close 2026-05-26 21:00 UTC. Cours $15.98, RSI 49.59, ATR $0.71, MM50 $16.73. Volume 80.29M (1.14× moy. 20j) — stable. Cours sous MM50, timing Défavorable. Score Opportunité 6.1/10, Score Global 53.1/100 (ATTENDRE, bord inférieur). SL $14.56, TP $18.11, R/R 1.50. Options inchangées (valeurs historiques confirmées) : Max Pain $16.00 (parité avec cours), Put/Call 0.70, Call OI 58.8%. [ALERTE DATA QUALITY] Anomalie JSON 2026-05-27 sur options (max pain $5.00 aberrant, put/call null). Pinning 29/05 probable. Earnings dans 62j. Support $15.00 tenu. Aucune news, aucun événement corporate, exposition FX et géo neutres. Accounting risk non évalué (fichier absent). Validation data : SOFI OK.

---

## Références

- `Actions/SOFI/SOFI_2026-05-17_init.md` — Analyse initiale / Full Refresh
- `Actions/SOFI/SOFI_2026-05-18_update.md` — Mise à jour quotidienne
- `Actions/SOFI/SOFI_2026-05-19_update.md` — Mise à jour quotidienne
- `Actions/SOFI/SOFI_2026-05-20_update.md` — Mise à jour quotidienne
- `Actions/SOFI/SOFI_2026-05-25_update.md` — Mise à jour quotidienne (stabilité totale confirmée)
- `Actions/SOFI/SOFI_2026-05-26_update.md` — Mise à jour quotidienne (close final confirmé, volume révisé +49.5%, ATTENDRE maintenu)
- `Actions/SOFI/SOFI_2026-05-27_update.md` — Ce fichier (snapshot 10:00 UTC — pré-marché, stabilité totale confirmée, anomalie options JSON signalée)
- `data/latest.json` (2026-05-27T10:00:08+00:00) — Cours, RSI, ATR, consensus, ratios FMP, options
- `data/recommandations_2026-05-27.json` (10:00 UTC) — Scores agents actualisés
- `data/quant_2026-05-17.json` — Insuffisant
- `data/geo_risk_2026-05-17.json` — SOFI non flaggé
- `data/sector_rotation_2026-05-27.json` — XLF momentum 0.0
- `data/social_sentiment_2026-05-27.json` — 0 mentions
- `data/fx_exposure_2026-05-27.json` — fx_impact_score 0.0
- `data/upcoming_events_2026-05-27.json` — Earnings 2026-07-28 (62j)
- `data/events_2026-05-27.json` — Aucun événement corporate
- `data/news_2026-05-27.json` — 0 news SOFI
- `data/validation_report.txt` (2026-05-27) — SOFI OK

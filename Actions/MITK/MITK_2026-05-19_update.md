# MITK — Mise à Jour Post-Pipeline (2026-05-19 13:00 UTC)

> Desk : Argus-IA | Pipeline : 13:00 UTC | Données : `data/latest.json` (2026-05-19T13:00:12Z) | Score Global Ajusté : **49.8/100** | Action : **SURVEILLER**

---

## Résumé des Changements

**Verdict : DONNÉES STABLES SUR LES MÉTRIQUES PRINCIPALES, MAIS VOLATILITÉ DES DONNÉES OPTIONS CONFIRMÉE. Cours inchangé à $14.13, RSI 50.62 stable, volume 915,700 (0.74× moyenne 20j), ATR $0.85 inchangé. Thèse SURVEILLER confirmée.**

Le snapshot 13:00 UTC confirme la stabilité des données fondamentales et techniques du snapshot 10:00 UTC :
- **Close** : $14.13 (previous close $14.26, -0.91%) — stable
- **Volume** : 915,700 — stable (0.74× moyenne 20j de 1,236,030)
- **RSI 14j** : 50.62 — stable
- **ATR 14j** : $0.85 — stable (~6.0% du spot)
- **MM50** : $14.30 — stable
- **Score Global Ajusté** : 49.8/100 — stable
- **Score Opportunité** : 5.8/10 (C:5.5 V:6.5 M:5.0) — stable

**Changement notable : volatilité des données options.** Entre le snapshot 10:00 UTC et 13:00 UTC, les données dérivées de Yahoo Finance ont basculé :
- **Max Pain** : $7.50 (10:00 UTC) → **$20.00** (13:00 UTC) — retour de l'anomalie aberrante (+41.5% au-dessus du spot)
- **Put/Call ratio** : `null` (10:00 UTC) → **0.17** (13:00 UTC)
- **Call OI %** : `null` (10:00 UTC) → **85.8%** (13:00 UTC)

Cette instabilité intrajour confirme que la liquidité options sur MITK est **insuffisante pour une lecture institutionnelle robuste**. Le Max Pain à $20.00 est mathématalement incohérent avec un spot à $14.13 et un consensus analystes à $16.00. Ces données doivent être traitées comme un artefact algorithmique de Yahoo Finance (probablement dû à un très faible open interest concentré sur des strikes éloignés).

---

## Table Comparative — Snapshot 10:00Z vs 13:00Z (2026-05-19)

| Variable | Snapshot 10:00Z | Snapshot 13:00Z | Δ (13:00 vs 10:00) |
|---|---|---|---|
| **Cours close** | $14.13 | **$14.13** | **—** |
| **Change %** | -0.91% | **-0.91%** | **—** |
| **RSI 14j** | 50.62 | **50.62** | **—** |
| **ATR 14j** | $0.85 | **$0.85** | **—** |
| **MM 50j** | $14.30 | **$14.30** | **—** |
| **Volume jour** | 915,700 | **915,700** | **—** |
| **Volume vs 20j** | 0.74× | **0.74×** | **—** |
| **Market Cap (Yahoo)** | $638.1M | **$638.1M** | — |
| **Score Global Ajusté** | 49.8/100 | **49.8/100** | — |
| **Score Opportunité** | 5.8/10 | **5.8/10** | — |
| **Score Catalyseur** | 5.5/10 | **5.5/10** | — |
| **Score Valorisation** | 6.5/10 | **6.5/10** | — |
| **Score Momentum** | 5.0/10 | **5.0/10** | — |
| **Action recommandée** | SURVEILLER | **SURVEILLER** | — |
| **Consensus PT (FMP)** | $16.00 (2 analysts) | **$16.00 (2 analysts)** | — |
| **Max Pain** | $7.50 | **$20.00** | **+$12.50 (+166.7%)** |
| **Put/Call ratio** | null | **0.17** | **[RÉAPPARU]** |
| **Call OI %** | null | **85.8%** | **[RÉAPPARU]** |
| **Prochain earnings** | 2026-08-06 (79j) | **2026-08-06 (79j)** | — |
| **Régime macro** | Unknown | **Unknown** | — |
| **XLK momentum** | 10.0 | **10.0** | — |
| **Geo risk score** | 0/10 | **0/10** | — |
| **FX impact score** | 0.0 | **0.0** | — |
| **Social sentiment** | 0 / No data | **0 / No data** | — |
| **Events corporate** | Aucun | **Aucun** | — |

**Lecture institutionnelle :** La stabilité totale des métriques principales (cours, volume, RSI, ATR, scores) confirme que la séance US du 2026-05-19 n'a pas encore ouvert au moment du snapshot 13:00 UTC (données de clôture de la veille répétées). La seule variation — les données options — est un artefact de plateforme et invalide toute analyse dérivée.

---

## 1. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| **Cours close** | $14.13 | Stable, sous MM50 |
| **Change %** | -0.91% | Inchangé vs previous close |
| **RSI (14j)** | 50.62 | Zone neutre, marginalement au-dessus de 50 |
| **ATR (14j)** | $0.85 | ~6.0% du spot |
| **MM 50j** | $14.30 | Close sous MM50 (-1.2%) |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume** | 915,700 | **0.74× moyenne 20j** — liquidité inférieure à la normale |
| **52-week range** | $8.53 – $16.48 | Spot à 85.6% du range |
| **Beta** | 0.955 | Aligné sur le marché |

**Niveaux clés (stables) :**
- Support immédiat : $13.74 (low du jour précédent)
- Support structurel : $13.00 (zone de consolidation)
- Résistance intermédiaire : $14.30 (MM50)
- Résistance majeure : $16.00 (consensus PT) / $16.48 (52w high)
- Stop-loss ATR (2×) : **$12.43** (-12.0%)
- Take-profit ATR (3×) : **$16.68** (+18.0%)
- Ratio R/R : **1.5**

**Verdict timing :** Neutre à légèrement défavorable. Le prix reste sous MM50 avec un volume inférieur à la moyenne. La configuration reste de consolidation neutre/baissière. Seule une cassure confirmée au-dessus de $14.30 (MM50) avec volume >1.0× moyenne et RSI >55 invaliderait le timing défavorable.

**Momentum sectoriel :** XLK affiche un momentum score de **10.0/10** (top sector, return 20j +12.81%, return 60j +23.92%). MITK, classé Software-Application (Technology), bénéficie indirectement de ce momentum sectoriel, mais son propre momentum individuel (5.0/10) reste faible, suggérant une sous-performance relative au secteur.

---

## 2. Mise à Jour Fondamentale (Inchangée)

Les données fondamentales n'ont pas évolué entre les snapshots.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $638.1M (Yahoo) / $446.6M (FMP) | Yahoo / FMP |
| P/E (TTM) | 41.56x (Yahoo) / 50.78x (FMP) | Yahoo / FMP |
| Forward P/E | 11.64x | Yahoo Finance |
| EV/EBITDA | 14.71x (Yahoo) / 12.15x (FMP) | Yahoo / FMP |
| P/B | 2.65x (Yahoo) / 1.86x (FMP) | Yahoo / FMP |
| Gross Margin | 85.1% | FMP |
| Operating Margin | 9.3% | FMP |
| EBITDA Margin | 20.5% | FMP |
| Net Margin | 4.9% | FMP |
| ROIC | 3.16% | FMP key metrics |
| ROE | 3.66% | FMP key metrics |
| FCF Yield | 12.1% | FMP |
| Net Debt / EBITDA | 0.03x | FMP |
| SBC / Revenue | 9.35% | FMP |

**Filtre Qualité :** 3–4 / 6 — Quality Partielle. Forward P/E attractif et FCF yield solide, mais ROIC faible et séries historiques incomplètes. Aucun changement depuis l'analyse initiale.

**Données comptables :** `data/accounting_risk_latest.json` inexistant — pas de scan comptable disponible. Pas d'alerte M-Score/Z-Score/F-Score/Sloan.

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Lecture |
|---|---|---|
| Consensus PT | $16.00 (2 analysts) | Upside +13.2%, couverture faible |
| **Max Pain** | $20.00 | 🔴 Anomalie confirmée (+41.5% au-dessus du spot) — données instables |
| **Put/Call ratio** | 0.17 | Réapparu entre 10h et 13h UTC — signal dérivé non fiable |
| **Call OI %** | 85.8% | Réapparu entre 10h et 13h UTC — lecture institutionnelle impossible |
| Short Interest | 7.32% | Modéré, pas de squeeze setup |
| Social Sentiment | 0 / No data | Sous le radar retail |
| Upgrades/Downgrades | Aucun | Silence analystes |
| News structurantes | Aucune | — |

**Verdict Sentiment :** Neutre. L'instabilité intrajour des données options (Max Pain $7.50 → $20.00 en 3 heures) confirme que la liquidité dérivée sur MITK est insuffisante pour toute analyse institutionnelle. Le positionnement call-dominated (85.8% call OI) n'est pas interprétable en raison du faible open interest global. Aucun flux de news, aucun insider trade, aucun upgrade/downgrade. MITK reste sous le radar.

---

## 4. Scoring Global — Révision

| Pilier | Score | Poids | Pondéré |
|---|---|---|---|
| **Catalyseur** | 5.5/10 | 35% | 1.925 |
| **Valorisation** | 6.5/10 | 40% | 2.600 |
| **Momentum** | 5.0/10 | 25% | 1.250 |
| **Score Opportunité** | **5.8/10** | — | **5.775** |
| **Score Global Ajusté** | **49.8/100** | — | — |

| Seuil | Action | Sizing |
|---|---|---|
| Score Global 49.8/100 | **SURVEILLER** | — |

**Explication :** Le Score Opportunité reste stable à 5.8/10 (catégorie ATTENDRE 50–59), mais les malus techniques (momentum 5.0/10, timing neutre/défavorable) et le franchissement du seuil psychologique 50 sur le score global ajusté placent MITK dans la catégorie **SURVEILLER** (35–49). La valorisation reste attractive (6.5/10), mais sans catalyseur ni volume de confirmation, l'asymétrie n'est pas activable.

**Risques additionnels (inchangés) :**
- Geo risk : 0/10 — pas d'exposition politique détectée
- FX impact : 0.0 — exposition USD, pas de divergence
- Social sentiment : 0/10 — pas de signal retail
- Events corporate : aucun

---

## 5. Révision des Niveaux SL / TP

| Niveau | Prix | Distance |
|---|---|---|
| **Stop-loss** | $12.43 | -12.0% |
| **Take-profit** | $16.68 | +18.0% |
| **Ratio R/R** | 1.5 | Seuil institutionnel non atteint (cible 1:2) |

Les niveaux sont inchangés : close stable à $14.13 et ATR stable à $0.85.

---

## 6. Calendrier & Événements (Inchangé)

| Événement | Date | Jours restants |
|---|---|---|
| **Earnings Q3 FY2026** | 2026-08-06 | **79** |
| **Expiration options** | 2026-06-18 | 30 |

**Alertes actives (révisées) :**
- 🟡 **[VOLUME SOUS MOYENNE]** 0.74× moyenne 20j — liquidité inférieure à la normale
- 🔴 **[ANOMALIE OPTIONS CONFIRMÉE]** Max Pain $20.00 (instable : $7.50 à 10:00 UTC → $20.00 à 13:00 UTC) — données dérivées non fiables
- 🟡 **[DONNÉES OPTIONS INSTABLES]** Put/Call et Call OI % réapparus entre 10h et 13h UTC — pas de signal dérivé fiable
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($638M vs $447M) et P/E — utiliser Yahoo comme primaire
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital dans les prochains filings
- 🟡 **[SCORE SOUS SEUIL 50]** Global ajusté 49.8/100 — surveillance renforcée

---

## 7. Conclusion — Thèse Confirmée (SURVEILLER)

**Verdict : THÈSE SURVEILLER CONFIRMÉE. Snapshot 13:00 UTC strictement identique au snapshot 10:00 UTC sur toutes les métriques principales. Seule instabilité = données options (Max Pain $20.00, retour de l'anomalie algorithmique), confirmant l'insuffisance de la liquidité dérivée pour une lecture institutionnelle.**

MITK reste un small-cap logiciel ($638M Yahoo) avec un profil qualité partielle (3–4/6) : Forward P/E attractif (11.64x), FCF yield solide (12.1%), mais rentabilité du capital faible (ROIC 3.16%) et couverture institutionnelle quasi nulle (2 analysts). Le volume final s'établit à 0.74× la moyenne 20j, une liquidité inférieure à la normale sans signification directionnelle.

Le secteur Technology (XLK) affiche un momentum exceptionnel (10.0/10, +12.81% sur 20j), mais MITK sous-performe son secteur avec un momentum individuel de 5.0/10, ce qui suggère une sélectivité du marché au sein du secteur tech.

Le Score Global Ajusté **49.8/100** et la recommandation **SURVEILLER** sont maintenus. Les fondamentaux n'ont pas changé. Le consensus à $16.00 offre un upside théorique de +13.2%, mais sans catalyseur ni volume confirmé, cette cible n'est pas activable.

**Recommandation :** **SURVEILLER.**

Ne pas engager de nouvelle position. Déteneurs : maintenir le SL à $12.43. Seule une cassure confirmée au-dessus de $14.30 (MM50) avec volume >1.0× moyenne et RSI >55 justifierait une révision technique. Une cassure au-dessus de $16.00–$16.48 avec volume >1.5× moyenne justifierait un passage à **ATTENDRE** puis **ACHETER** (sizing réduit). À l'inverse, une cassure sous $13.00 avec volume élevé invaliderait la thèse et justifierait un passage à **ÉVITER**.

---

*Révision post-pipeline 13:00 UTC — Données : `data/latest.json` (2026-05-19T13:00:12Z), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-05-19.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_2026-05-19.json`, `data/upcoming_events_2026-05-19.json`, `data/events_2026-05-19.json`, `data/validation_report.txt` (2026-05-19T12:06Z) — Date : 2026-05-19*

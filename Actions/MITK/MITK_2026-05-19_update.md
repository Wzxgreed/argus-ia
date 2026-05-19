# MITK — Mise à Jour Post-Pipeline (2026-05-19 10:00 UTC)

> Desk : Argus-IA | Pipeline : 10:00 UTC | Données : `data/latest.json` (2026-05-19T10:00:12Z) | Score Global Ajusté : **49.8/100** | Action : **SURVEILLER**

---

## Résumé des Changements

**Verdict : DONNÉES STABLES POST-CLOSE (SNAPSHOT 10:00 UTC 2026-05-19). Cours inchangé à $14.13, RSI 50.62 stable, volume 915,700 (0.74× moyenne 20j), ATR $0.85 inchangé. Thèse SURVEILLER confirmée — pas de basculement.**

Le snapshot 10:00 UTC confirme l'intégralité des données du snapshot 22:35 UTC du 2026-05-18 :
- **Close** : $14.13 (previous close $14.26, -0.91%) — stable
- **Volume** : 915,700 — stable (0.74× moyenne 20j de 1,236,030)
- **RSI 14j** : 50.62 — stable
- **ATR 14j** : $0.85 — stable (~6.0% du spot)
- **MM50** : $14.30 — stable
- **Score Global Ajusté** : 49.8/100 — stable
- **Score Opportunité** : 5.8/10 (C:5.5 V:6.5 M:5.0) — stable

**Correction notable :** Le **Max Pain** est révisé de **$20.00 → $7.50** (expiration 2026-06-18). L'ancienne valeur de $20.00 était une anomalie aberrante (+41.5% au-dessus du spot) qualifiée dans le précédent update. La nouvelle valeur de $7.50 résout cette anomalie mais se situe **sous le spot** (-46.9%), ce qui reflète une liquidité options extrêmement faible et un positionnement put-dominated sur les strikes proches. Les données Yahoo (`put_call_ratio`, `call_oi_pct`) sont désormais `null`, confirmant l'indisponibilité d'un signal dérivé fiable.

**Données options :** `put_call_ratio` et `call_oi_pct` passés de 0.14 / 87.4% à `null` — [DONNÉES MANQUANTES]. La liquidité options reste insuffisante pour une lecture institutionnelle.

---

## Table Comparative — Snapshot 2026-05-18 22:35Z vs 2026-05-19 10:00Z

| Variable | Snapshot 18/05 22:35Z | Snapshot 19/05 10:00Z | Δ (19/05 vs 18/05) |
|---|---|---|---|
| **Cours close** | $14.13 | **$14.13** | **—** |
| **Change %** | -0.91% | **-0.91%** | **—** |
| **RSI 14j** | 50.62 | **50.62** | **—** |
| **ATR 14j** | $0.85 | **$0.85** | **—** |
| **MM 50j** | $14.30 | **$14.30** | **—** |
| **Volume jour** | 914,696 | **915,700** | **+0.1%** |
| **Volume vs 20j** | 0.74× | **0.74×** | **—** |
| **Market Cap (Yahoo)** | $638.1M | **$638.1M** | — |
| **Score Global Ajusté** | 49.8/100 | **49.8/100** | — |
| **Score Opportunité** | 5.8/10 | **5.8/10** | — |
| **Score Catalyseur** | 5.5/10 | **5.5/10** | — |
| **Score Valorisation** | 6.5/10 | **6.5/10** | — |
| **Score Momentum** | 5.0/10 | **5.0/10** | — |
| **Action recommandée** | SURVEILLER | **SURVEILLER** | — |
| **Consensus PT (FMP)** | $16.00 (2 analysts) | **$16.00 (2 analysts)** | — |
| **Max Pain** | $20.00 | **$7.50** | **-62.5%** |
| **Put/Call ratio** | 0.14 | **null** | **[DONNÉES MANQUANTES]** |
| **Call OI %** | 87.4% | **null** | **[DONNÉES MANQUANTES]** |
| **Prochain earnings** | 2026-08-06 (80j) | **2026-08-06 (79j)** | **-1j** |
| **Régime macro** | Unknown | **Unknown** | — |
| **XLK momentum** | 10.0 | **10.0** | — |
| **Geo risk score** | 0/10 | **0/10** | — |
| **FX impact score** | 0.0 | **0.0** | — |
| **Social sentiment** | 0 / No data | **0 / No data** | — |
| **Events corporate** | Aucun | **Aucun** | — |

**Lecture institutionnelle :** La stabilité totale des données entre les deux snapshots confirme que la séance du 2026-05-18 s'est clôturée sans surprise, et que le snapshot du matin du 2026-05-19 n'apporte aucune donnée nouvelle (pipeline 10:00 UTC reprend les données de clôture de la veille pour les séances US non ouvertes). La correction du Max Pain est une résolution de l'anomalie algorithmique précédente, pas un événement de marché.

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
| **Max Pain** | $7.50 | Sous le spot (-46.9%) — liquidité options extrêmement faible, put-dominated |
| **Put/Call ratio** | null | [DONNÉES MANQUANTES] — signal dérivé indisponible |
| **Call OI %** | null | [DONNÉES MANQUANTES] |
| Short Interest | 7.32% | Modéré, pas de squeeze setup |
| Social Sentiment | 0 / No data | Sous le radar retail |
| Upgrades/Downgrades | Aucun | Silence analystes |
| News structurantes | Aucune | — |

**Verdict Sentiment :** Neutre. La résolution de l'anomalie Max Pain ($20.00 → $7.50) ne modifie pas la conclusion : la liquidité options est insuffisante pour une lecture institutionnelle robuste. Le passage de put/call et call OI à `null` confirme l'indisponibilité des données Yahoo pour ce ticker. Aucun flux de news, aucun insider trade, aucun upgrade/downgrade. MITK reste sous le radar.

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
- 🟡 **[MAX PAIN CORRIGÉ]** $7.50 (résolution anomalie $20.00) — liquidité options extrêmement faible, put-dominated
- 🟡 **[DONNÉES OPTIONS MANQUANTES]** Put/Call et Call OI % indisponibles — pas de signal dérivé fiable
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($638M vs $447M) et P/E — utiliser Yahoo comme primaire
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital dans les prochains filings
- 🟡 **[SCORE SOUS SEUIL 50]** Global ajusté 49.8/100 — surveillance renforcée

---

## 7. Conclusion — Thèse Confirmée (SURVEILLER)

**Verdict : THÈSE SURVEILLER CONFIRMÉE. Snapshot 2026-05-19 10:00 UTC strictement identique au snapshot 2026-05-18 22:35 UTC sur toutes les métriques principales. Seule correction = Max Pain révisé $7.50 (résolution de l'anomalie algorithmique $20.00).**

MITK reste un small-cap logiciel ($638M Yahoo) avec un profil qualité partielle (3–4/6) : Forward P/E attractif (11.64x), FCF yield solide (12.1%), mais rentabilité du capital faible (ROIC 3.16%) et couverture institutionnelle quasi nulle (2 analysts). La séance du 2026-05-18 a démontré la volatilité intrinsèque du titre : gap +5.08% du matin, stabilisation à -0.91% post-close. Le volume final s'établit à 0.74× la moyenne 20j, une liquidité inférieure à la normale sans signification directionnelle.

Le secteur Technology (XLK) affiche un momentum exceptionnel (10.0/10, +12.81% sur 20j), mais MITK sous-performe son secteur avec un momentum individuel de 5.0/10, ce qui suggère une sélectivité du marché au sein du secteur tech.

Le Score Global Ajusté **49.8/100** et la recommandation **SURVEILLER** sont maintenus. Les fondamentaux n'ont pas changé. Le consensus à $16.00 offre un upside théorique de +13.2%, mais sans catalyseur ni volume confirmé, cette cible n'est pas activable.

**Recommandation :** **SURVEILLER.**

Ne pas engager de nouvelle position. Déteneurs : maintenir le SL à $12.43. Seule une cassure confirmée au-dessus de $14.30 (MM50) avec volume >1.0× moyenne et RSI >55 justifierait une révision technique. Une cassure au-dessus de $16.00–$16.48 avec volume >1.5× moyenne justifierait un passage à **ATTENDRE** puis **ACHETER** (sizing réduit). À l'inverse, une cassure sous $13.00 avec volume élevé invaliderait la thèse et justifierait un passage à **ÉVITER**.

---

*Révision post-pipeline 10:00 UTC — Données : `data/latest.json` (2026-05-19T10:00:12Z), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-05-19.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_2026-05-19.json`, `data/upcoming_events_2026-05-19.json`, `data/events_2026-05-19.json`, `data/validation_report.txt` (2026-05-19T10:00Z) — Date : 2026-05-19*

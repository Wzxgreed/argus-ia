# MITK — Mise à Jour Quotidienne Révisée (2026-05-18 post-pipeline 13:00 UTC)

> Desk : Argus-IA | Pipeline : 13:00 UTC | Données : `data/latest.json` (2026-05-18T13:00:12Z) | Score Global : **51.0/100** | Action : **ATTENDRE**

---

## Résumé — Validation Post-Pipeline

**Verdict : DONNÉES DE BASE INCHANGÉES vs snapshot 10:00 UTC. OPTIONS RAFRAÎCHIES. Thèse ATTENDRE confirmée.**

Le troisième passage du pipeline (13:00 UTC) n'a détecté aucune variation de cours, de volume, de macro ou de sentiment par rapport au snapshot 10:00. Le close reste à **$14.26** (+5.08%), le RSI à **51.62**, la MM50 à **$14.31** et l'ATR à **$0.86**. Les scores agents (Catalyseur 5.5, Valorisation 6.5, Momentum 5.5 → Opportunité 5.9 → Global ajusté 51.0) sont identiques.

**Changement significatif :** les données options ont été rafraîchies par le provider. Le Max Pain passe de **$7.50** (anomalie) à **$20.00**, le Put/Call ratio est désormais disponible à **0.14**, et le Call OI représente **87.4%** de l'open interest total. Ces nouvelles données, bien que plus cohérentes, restent à manipuler avec prudence compte tenu de la faible liquidité dérivée de MITK.

---

## Table Comparative — Snapshot 10:00 UTC vs Pipeline 13:00 UTC

| Variable | Snapshot 10:00Z | Pipeline 13:00Z | Δ | Statut |
|---|---|---|---|---|
| **Cours close** | $14.26 | $14.26 | — | ✅ Inchangé |
| **Change %** | +5.08% | +5.08% | — | ✅ Inchangé |
| **RSI 14j** | 51.62 | 51.62 | — | ✅ Inchangé |
| **MM 50j** | $14.31 | $14.31 | — | ✅ Inchangé |
| **ATR 14j** | $0.86 | $0.86 | — | ✅ Inchangé |
| **Volume jour** | 1,317,800 | 1,317,800 | — | ✅ Inchangé |
| **Volume vs 20j** | 1.07× | 1.07× | — | ✅ Inchangé |
| **Consensus PT (FMP)** | $16.00 (2 analysts) | $16.00 (2 analysts) | — | ✅ Inchangé |
| **Max Pain** | $7.50 | **$20.00** | **+$12.50** | 🟢 Rafraîchi — moins aberrant |
| **Put/Call ratio** | N/A | **0.14** | **Disponible** | 🟢 Données restaurées |
| **Call OI %** | N/A | **87.4%** | **Disponible** | 🟢 Call-dominated |
| **Score Global Ajusté** | 51.0/100 | 51.0/100 | — | ✅ Inchangé |
| **Score Opportunité** | 5.9/10 | 5.9/10 | — | ✅ Inchangé |
| **Prochain earnings** | 2026-08-06 (80j) | 2026-08-06 (80j) | — | ✅ Inchangé |
| **Régime macro** | Inconnu | Inconnu | — | ⚠️ Données macro partielles |
| **XLK momentum** | 10.0 (+14.2% / 20j) | 10.0 (+14.2% / 20j) | — | ✅ Inchangé |
| **Geo risk score** | 0/10 | 0/10 | — | ✅ Inchangé |
| **FX impact score** | 0.0 | 0.0 | — | ✅ Inchangé |
| **Social sentiment** | 0 / No data | 0 / No data | — | ✅ Inchangé |
| **Events corporate** | Aucun | Aucun | — | ✅ Inchangé |

**Lecture institutionnelle :** L'absence de delta sur le spot et les volumes confirme que le gap +5.08% du matin reste un événement isolé sans suite. Le rafraîchissement des données options est technique (provider) et non lié à un flux de marché. Le Max Pain à $20.00 (+40.3% vs spot) reste éloigné mais dans la zone haussière, ce qui est plus cohérent qu'un Max Pain à -47% du spot. Le ratio Put/Call 0.14 et le Call OI 87.4% traduisent un positionnement options call-dominated, typique d'un small-cap sous le radar retail avec peu d'activité dérivée.

---

## 1. Mise à Jour Technique (Inchangée)

| Indicateur | Valeur | Lecture |
|---|---|---|
| **RSI (14j)** | 51.62 | Zone neutre |
| **ATR (14j)** | $0.86 | ~6.0% du spot |
| **MM 50j** | $14.31 | Close sous MM50 (-0.3%) |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume** | 1,317,800 | 1.07× moyenne 20j |
| **52-week range** | $8.53 – $16.48 | Spot à 86.5% du range |
| **Beta** | 0.955 | Aligné sur le marché |

**Niveaux clés (validés) :**
- Support immédiat : $13.52 (low du jour)
- Support structurel : $13.00 (zone de consolidation)
- Résistance intermédiaire : $14.68 (high du jour)
- Résistance majeure : $16.00 (consensus PT) / $16.48 (52w high)
- Stop-loss ATR (2×) : **$12.54** (-12.1%)
- Take-profit ATR (3×) : **$16.84** (+18.1%)
- Ratio R/R : **1.5**

**Verdict timing :** Défavorable. Le prix reste sous MM50 malgré le gap. Aucune confirmation de cassure ni de retrait vers support avec volume. Attendre.

---

## 2. Mise à Jour Fondamentale (Inchangée)

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $643.9M (Yahoo) / $446.6M (FMP) | Yahoo / FMP |
| P/E (TTM) | 41.94x (Yahoo) / 50.78x (FMP) | Yahoo / FMP |
| Forward P/E | 11.75x | Yahoo Finance |
| EV/EBITDA | 14.85x (Yahoo) / 12.15x (FMP) | Yahoo / FMP |
| P/B | 2.67x (Yahoo) / 1.86x (FMP) | Yahoo / FMP |
| Gross Margin | 85.1% | FMP |
| Operating Margin | 9.3% | FMP |
| EBITDA Margin | 20.5% | FMP |
| Net Margin | 4.9% | FMP |
| ROIC | 3.16% | FMP key metrics |
| ROE | 3.66% | FMP key metrics |
| FCF Yield | 12.1% | FMP |
| Net Debt / EBITDA | 0.03x | FMP |
| SBC / Revenue | 9.35% | FMP |

**Filtre Qualité :** 3–4 / 6 — Quality Partielle. Forward P/E attractif et FCF yield solide, mais ROIC faible et séries historiques incomplètes.

> **Note :** La divergence Yahoo/FMP sur le market cap ($643.9M vs $446.6M) et le P/E (41.94x vs 50.78x) persiste. Nous continuons d'utiliser Yahoo comme source primaire pour le spot et les multiples courants, FMP pour les ratios opérationnels et le consensus.

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Lecture |
|---|---|---|
| Consensus PT | $16.00 (2 analysts) | Upside +12.1%, couverture faible |
| **Max Pain** | **$20.00** | 🟡 Éloigné du spot (+40.3%) — liquidité options faible |
| **Put/Call ratio** | **0.14** | 🟢 Call-dominated (très faible activité put) |
| **Call OI %** | **87.4%** | 🟢 Positionnement options haussier |
| Short Interest | 7.32% | Modéré, pas de squeeze setup |
| Social Sentiment | 0 / No data | Sous le radar retail |
| Upgrades/Downgrades | Aucun | Silence analystes |
| News structurantes | Aucune | — |

**Verdict Sentiment :** Neutre à légèrement positif sur les options. Le rafraîchissement des données options révèle un positionnement call-dominated (Put/Call 0.14, Call OI 87.4%), ce qui est cohérent avec un titre small-cap tech en consolidation sous ses highs. Cependant, le Max Pain à $20.00 est trop éloigné pour constituer un niveau significatif. L'illiquidité globale des options (expiration proche 2026-06-18 avec peu d'open interest) invalide toute lecture dérivée institutionnelle robuste.

**Alerte options :** Le passage de Max Pain $7.50 → $20.00 entre les snapshots 10:00Z et 13:00Z est un ajustement provider, pas un mouvement de marché. Ne pas sur-interpréter.

---

## 4. Scoring Global — Révision (Inchangé)

| Pilier | Score | Poids | Pondéré |
|---|---|---|---|
| **Catalyseur** | 5.5/10 | 35% | 1.925 |
| **Valorisation** | 6.5/10 | 40% | 2.600 |
| **Momentum** | 5.5/10 | 25% | 1.375 |
| **Score Opportunité** | **5.9/10** | — | **5.900** |
| **Score Global Ajusté** | **51.0/100** | — | — |

| Seuil | Action | Sizing |
|---|---|---|
| Score Global 51.0/100 | **ATTENDRE** | — |

---

## 5. Révision des Niveaux SL / TP (Inchangée)

| Niveau | Prix | Distance |
|---|---|---|
| **Stop-loss** | $12.54 | -12.1% |
| **Take-profit** | $16.84 | +18.1% |
| **Ratio R/R** | 1.5 | Seuil institutionnel non atteint (cible 1:2) |

---

## 6. Calendrier & Événements (Inchangé)

| Événement | Date | Jours restants |
|---|---|---|
| **Earnings Q3 FY2026** | 2026-08-06 | **80** |
| **Expiration options** | 2026-06-18 | 31 |

**Alertes actives :**
- 🟡 **[MAX PAIN ÉLOIGNÉ]** $20.00 vs spot $14.26 (+40.3%) — liquidité options insuffisante
- 🟡 **[DONNÉES OPTIONS VOLATILES]** Max Pain a varié de $7.50 à $20.00 intrajour — provider data
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap / P/E — utiliser Yahoo comme primaire
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer dans les prochains filings
- 🟡 **[ILLIQUIDITÉ OPTIONS]** Faible OI, Put/Call 0.14 — pas de signal dérivé fiable

---

## 7. Conclusion — Thèse Confirmée

**Verdict : THÈSE ATTENDRE CONFIRMÉE — AUCUN CHANGEMENT DE CONTEXTE FONDAMENTAL NI TECHNIQUE ENTRE 10:00Z ET 13:00Z.**

MITK reste un small-cap logiciel ($644M Yahoo) avec un profil qualité partielle (3–4/6) : Forward P/E attractif (11.75x), FCF yield solide (12.1%), mais rentabilité du capital faible (ROIC 3.16%) et couverture institutionnelle quasi nulle (2 analysts). Le gap +5.08% du matin n'a trouvé ni catalyseur ni confirmation technique. Le titre évolue sous MM50 dans un range $13.50–$14.70.

Le rafraîchissement des données options (Max Pain $20.00, Put/Call 0.14, Call OI 87.4%) est un ajustement technique provider sans incidence sur la thèse. La faible liquidité dérivée de MITK invalide toute lecture institutionnelle basée sur le flux options.

**Recommandation :** **ATTENDRE.**

Ne pas engager de nouvelle position. Déteneurs : maintenir le SL à $12.54. Seule une cassure confirmée au-dessus de $16.00–$16.48 avec volume >1.5× moyenne et RSI >55 justifierait une révision à **ACHETER** (sizing réduit).

---

*Révision post-pipeline 13:00 UTC — Données de base inchangées vs snapshot 10:00 UTC, options rafraîchies — Sources : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/geo_risk_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json` — Date : 2026-05-18*

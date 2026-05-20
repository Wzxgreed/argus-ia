# PLTR — Mise à Jour Quotidienne (2026-05-20, snapshot 13:00 UTC)

> **Source :** `data/latest.json` (snapshot 2026-05-20 13:00 UTC) + agents sector, FX, watchman, events, social, quant, geo
> **Référence précédente :** [PLTR_2026-05-19_update.md](PLTR_2026-05-19_update.md) (close 21:00 UTC) + [PLTR_2026-05-20_update.md](PLTR_2026-05-20_update.md) (snapshot 10:00 UTC, pré-ouverture)
> **Contexte :** Snapshot officiel 13:00 UTC du pipeline. Données de cours reflètent la séance du 2026-05-20.

---

## Résumé des Changements depuis l'Update Précédent (2026-05-19 close 21:00 UTC)

| Indicateur | 19/05 close | 20/05 13:00 | Δ |
|-----------|-------------|-------------|---|
| Cours close | **$135.26** | **$135.26** | **0.00%** |
| Open / High / Low | $135.17 / $137.46 / $133.60 | **$135.17 / $137.47 / $133.60** | **High +$0.01** |
| RSI 14j | **46.36** | **46.36** | **0** |
| Volume jour | 29.65M | **29.70M** | **+0.2%** |
| Volume vs moy. 20j | −31.9% | **−31.8%** | **Compression identique** |
| ATR 14j | **5.62** | **5.62** | **0** |
| MM 50j | **143.54** | **143.54** | **0** |
| Max Pain options | $140.00 | **$140.00** | **✅ Anomalie résolue** |
| Put/Call Ratio | 0.64 | **0.61** | **−0.03** |
| Call OI % | 60.8% | **62.2%** | **+1.4 pp** |
| Score Catalyseur | 6.8/10 | **6.8/10** | **0** |
| Score Valorisation | 4.5/10 | **4.5/10** | **0** |
| Score Momentum | 5.0/10 | **5.0/10** | **0** |
| Score Opportunité | 5.4/10 | **5.4/10** | **0** |
| Score Global ajusté | 46.3/100 | **46.3/100** | **0** |
| Action | SURVEILLER | **SURVEILLER** | **→ Confirmé** |

**Verdict :** Aucun changement significatif dans les données de marché entre la clôture du 19/05 et le snapshot 13:00 UTC du 20/05. Le cours, le RSI, l'ATR, les moyennes mobiles et les volumes sont **strictement inchangés**. Les scores agents n'ont pas été révisés. **Thèse SURVEILLER confirmée sans modification.**

**Résolution anomalie data quality :** L'anomalie options signalée au snapshot 10:00 UTC (Max Pain aberrant $50.00, Put/Call et Call OI passés à `null`) est **entièrement résolue** au snapshot 13:00 UTC :
- Max Pain : $50.00 → **$140.00** (cohérent avec le spot $135.26)
- Put/Call Ratio : `null` → **0.61**
- Call OI % : `null` → **62.2%**

La structure options est modérément haussière et stable. L'expiration du 2026-05-22 est dans 2 jours — la désynchronisation observée à 10:00 UTC était probablement liée au roll des séries en approche de l'expiration.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| Cours | **$135.26** | Inchangé vs previous close (snapshot 13:00 UTC) |
| RSI 14j | **46.36** | Stable — zone neutre inférieure, sortie complète de la zone < 40 confirmée depuis le 17/05 |
| MM 50j | **143.54** | Cours **−5.8% sous MM50** — résistance dynamique inchangée |
| MM 200j | — | [DONNÉES MANQUANTES] |
| Golden/Death Cross | Non | Aucun signal de croisement |
| Volume relatif vs 20j | **−31.8%** | 29.70M vs 43.53M moy. — compression persistante |
| Fourchette 52 semaines | $118.93 / $207.52 | Positionné à 35% du range |
| ATR 14j | **$5.62** | Volatilité stable |
| Beta | **1.521** | Élevé — amplifie les rotations sectorielles |
| Timing verdict | **Défavorable** | Sous MM50 + volume sous moyenne |

**Évolution vs snapshot 19/05 close :**
- **Cours** : inchangé à $135.26. High du jour $137.47 (+1.6% intraday) sans tenir.
- **RSI** : stable à 46.36 — dynamique positive sous-jacente maintenue mais sans progression.
- **Volume** : 29.70M (−31.8% vs 20j), en ligne avec le niveau de la veille. Aucun signal de retour institutionnel.
- **MM50** : stable à 143.54 — résistance descendante inchangée.
- **Options** : **✅ Anomalie résolue** — Max Pain $140.00, Put/Call 0.61, Call OI 62.2%. Structure modérément haussière stable.

---

## Mise à Jour Fondamentale

### Données FMP Annual FY2025 (inchangées vs précédent)

| Métrique | Valeur | Contexte |
|---------|--------|----------|
| Gross Margin | 82.4% | Excellente — business model software à forte levée |
| Operating Margin | 31.6% | Rentabilité opérationnelle élevée |
| Net Margin | 36.3% | Très élevée |
| Debt/Equity | 0.031 | Bilan quasi-sans dette |
| Current Ratio | 7.11 | Liquidité exceptionnelle |
| SBC / Revenue | 15.3% | Dilution significative par stock-based comp |
| DSO | 85 jours | Cycle de conversion client modéré |
| Cash Conversion Cycle | 81.3 jours | — |
| ROIC (FMP key metrics) | 17.9% | Création de valeur confirmée |
| Consensus Price Target | $187.61 | 33 analysts — upside théorique **+38.7%** |

### Divergences Yahoo vs FMP [DONNÉES PARTIELLES]

| Métrique | Yahoo Finance | FMP Annual FY2025 | Écart |
|---------|---------------|-------------------|-------|
| Market Cap | $324.3 Md | $421.2 Md | **+30%** |
| P/E | 152.0x | 259.2x | **+70%** |
| EV/Revenue | 60.5x | 93.8x | **+55%** |
| EV/EBITDA | 156.8x | 291.6x | **+86%** |
| P/B | 43.8x | 57.0x | **+30%** |

**Interprétation :** Écart persistant entre sources, inchangé. Les multiples restent extrêmes dans les deux cas, justifiant le Score Valorisation contenu (4.5/10). Aucune nouvelle donnée fondamentale ce jour.

**Filtre Qualité (6 critères)**
- Données Agent Accounting (M-Score, Z-Score, F-Score, Sloan) : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` absent (agent skipped lors du pipeline)
- Score Qualité : `[NON ÉVALUABLE]`
- Verdict : Le Filtre Qualité ne peut pas être appliqué sans les signaux comptables agents. Cette absence est un risque méthodologique persistant à noter.

---

## Mise à Jour Sentiment / Options / News

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| News du jour | — | Aucune news PLTR détectée dans le snapshot `data/latest.json` |
| Social Sentiment (Reddit) | No data | 0 mention collectée — absence de signal retail |
| Put/Call Ratio | **0.61** | ✅ Retour à la normale — biais modéré vers les calls |
| Call OI % | **62.2%** | ✅ Retour à la normale — appétence haussière modérée |
| Short Interest | 0.03% | Négligeable — pas de setup short squeeze |
| Insider Trades | — | [DONNÉES MANQUANTES] |
| Upgrades/Downgrades | — | [DONNÉES MANQUANTES] |
| Événements Corporate | Aucun | `data/events_latest.json` vide pour PLTR |

**Catalyseur prochain :** Earnings Q2 FY2026 le **2026-08-03** (75 jours). Est. EPS $0.32–$0.40, Rev $1.8B. Pas de preview requis (> 5j).

**Notes options :** La structure options est revenue à la normale après l'anomalie du snapshot 10:00 UTC. Max Pain $140.00, Put/Call 0.61, Call OI 62.2% — configuration modérément haussière stable. L'expiration du 2026-05-22 est dans 2 jours — surveiller la cohérence des données post-expiration.

---

## Scoring Global — Révision

| Axe | Score 13:00 UTC | Score 19/05 close | Δ | Pondération (Unknown) |
|-----|----------------|-------------------|---|---------------------|
| Catalyseur | **6.8/10** | 6.8/10 | 0 | 35% |
| Valorisation | **4.5/10** | 4.5/10 | 0 | 40% |
| Momentum | **5.0/10** | 5.0/10 | 0 | 25% |
| **Score Opportunité** | **5.4/10** | **5.4/10** | **0** | — |

**Score Global brut :** 54.3/100  
**Score Global ajusté :** **46.3/100** (malus technique et structuraux)  
**Action :** **SURVEILLER**

**Explication :** Les scores agents sont strictement inchangés vs la clôture du 19/05. L'absence de nouvelles données de séance (cours inchangé, volumes identiques) ne justifie aucune révision. Le profil technique reste identique : RSI 46.36 (neutre inférieur), sous MM50 (−5.8%), volume compressé (−31.8% vs 20j). L'événement du jour est la **résolution de l'anomalie data quality des options** entre 10:00 UTC et 13:00 UTC, qui n'impacte pas le scoring global mais rétablit la fiabilité du suivi options. Pas d'entrée avant confirmation technique (franchissement MM50 à $143.54 avec volume > moyenne 20j).

---

## Niveaux et Ratio R/R

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| Cours actuel | $135.26 | — |
| Entrée suggérée | $135.26 | — |
| Stop-loss suggéré | **$124.02** | Cours − 2×ATR = $135.26 − $11.24 |
| Take-profit suggéré | **$152.12** | Cours + 3×ATR = $135.26 + $16.86 |
| Ratio R/R | **1.5** | Ratio institutionnel standard |
| Upside vers consensus PT | +38.7% | $187.61 — horizon long terme |
| Max Pain (exp. 2026-05-22) | **$140.00** | +3.5% au-dessus du spot — zone de gravitation options |

*Niveaux inchangés vs 19/05 (cours et ATR identiques).*

---

## Contexte Macro, Sectoriel & Risques

| Facteur | État | Impact PLTR |
|---------|------|-------------|
| Régime macro | Unknown (VIX/DXY/taux non alimentés) | Pas d'ajustement régime-aware applicable |
| DXY | Stable | Neutre — pas de divergence FX détectée |
| XLK (Technology) | **Top sector** — Momentum 10.0/10, RS 20j +7.78% | **Vent favorable** structurel inchangé |
| Beta 1.52 | Élevé | Amplifie les rotations sectorielles |
| Geo Risk | Score 0 | Pas d'événement géopolitique spécifique (`data/geo_risk_latest.json`) |
| Accounting Risk | [DONNÉES MANQUANTES] | `data/accounting_risk_latest.json` absent — agent skipped |
| Quant Calibration | Insuffisant | Pas assez de signaux historiques (`p_value` 1.0) — calibration en cours |
| Social Sentiment | No data | Pas de signal retail exploitable |
| FX Exposure | 55% export EUR/CNY | FX Impact Score 0.0 — neutral, divergence aligned |
| Options Data Quality | ✅ Résolue | Max Pain cohérent ($140), Put/Call 0.61, Call OI 62.2% — signaux exploitables |

---

## Conclusion — État de la Thèse

**Statut : SURVEILLER — Thèse confirmée, données de marché inchangées, anomalie options résolue.**

**Arguments confirmants :**
- Marges opérationnelles et nettes excellentes (FMP FY2025 : GM 82%, OM 32%, NM 36%)
- Bilan solide : quasi-zero dette, current ratio 7.1, ROIC 18%
- Consensus analystes actif (33 analysts, PT $187.61 = +38.7% upside)
- XLK leader sectoriel (momentum 10.0/10) — environnement favorable aux techs
- RSI 46.36, sortie complète de la zone < 40 depuis le 17/05
- ✅ Structure options revenue à la normale : Max Pain $140.00, Put/Call 0.61, Call OI 62.2%
- Aucune news négative détectée ce jour

**Arguments limitants :**
- Timing technique défavorable : sous MM50 (−5.8%), volume **−31.8% sous moyenne 20j**
- Multiples extrêmes quel que soit la source (P/E 152x–259x, EV/Revenue 60x–94x)
- Divergence data Yahoo vs FMP sur toutes les métriques de valorisation [DONNÉES PARTIELLES]
- Accounting risk non évalué (agent absent) — qualité comptable non confirmée
- Aucune news ni catalyseur immédiat avant earnings août

**Scénarios :**
1. **Optimiste (25%)** : Rebond sur support + retour du volume institutionnel → test MM50 ($144) puis consolidation
2. **Central (50%)** : Consolidation latérale $130–$145 en l'absence de catalyseur jusqu'à earnings août
3. **Pessimiste (25%)** : Compression multiple dans un environnement incertain → test du support $118.93 (52w low)

**Prochaines étapes :**
- Surveiller le franchissement de la MM50 ($143.54) avec volume supérieur à la moyenne 20j (> 44M)
- Préparer `_preview.md` si earnings approchent à ≤ 5 jours (actuellement 75j)
- Réactiver l'agent accounting dès que possible pour valider le Filtre Qualité 6 critères
- **Surveiller la cohérence des données options post-expiration 2026-05-22** — vérifier que les signaux restent stables

---

## Validation Analyste Senior — Snapshot 13:00 UTC

**Analyste :** Desk Argus-IA  
**Timestamp validation :** 2026-05-20 13:00 UTC  
**Status :** ✅ Confirmé — snapshot 13:00 UTC, données quasi inchangées vs clôture 19/05, anomalie options résolue.

| Check | Résultat |
|-------|----------|
| `data/latest.json` (13:00 UTC) | Cours $135.26, RSI 46.36, ATR 5.62, MM50 143.54, Volume 29.70M — **inchangés vs 19/05** |
| Options (13:00 UTC) | Max Pain $140.00 ✅, Put/Call 0.61, Call OI 62.2% — **anomalie 10:00 UTC résolue** |
| `data/recommandations_latest.json` | Scores inchangés : C 6.8 / V 4.5 / M 5.0 → Opp 5.4 / Global 46.3 |
| `data/geo_risk_latest.json` | Score 0, aucun ticker PLTR flaggé |
| `data/fx_exposure_latest.json` | FX Impact Score 0.0, divergence aligned, pas de headwind |
| `data/events_latest.json` | Aucun événement corporate détecté |
| `data/news_latest.json` | Aucune news PLTR dans le snapshot Yahoo |
| `data/social_sentiment_latest.json` | No data — pas de signal retail |
| `data/upcoming_events_latest.json` | Earnings Q2 FY2026 confirmé 2026-08-03 (75j) |
| `data/quant_report_latest.json` | Pas assez de signaux historiques (p-value 1.0) — calibration en cours |
| `data/sector_rotation_latest.json` | XLK top sector (momentum 10.0/10) — vent favorable inchangé |
| Accounting Risk | `data/accounting_risk_latest.json` absent — risque méthodologique persistant |
| Data Quality Alert | ✅ Résolu — Max Pain $140.00 (cohérent vs spot $135.26) |

**Conclusion validation :** Le snapshot 13:00 UTC du 2026-05-20 ne présente aucun changement significatif dans les données de marché vs la clôture du 19/05. Cours, RSI, ATR, volumes et scores agents sont identiques. L'unique événement notable est la **résolution complète de l'anomalie data quality sur les options** (Max Pain revenu de $50.00 aberrant à $140.00 cohérent, Put/Call et Call OI restaurés). La thèse **SURVEILLER** reste inchangée. Le timing d'entrée reste conditionné au franchissement de la MM50 ($143.54) avec volume > 44M. Les signaux options sont à nouveau exploitables.

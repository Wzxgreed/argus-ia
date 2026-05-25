# PLTR — Mise à Jour Quotidienne (2026-05-25, snapshot 10:00 UTC)

> **Source :** `data/latest.json` (snapshot 2026-05-25 10:00 UTC) + agents sector, FX, watchman, events, social, quant, geo
> **Référence précédente :** [PLTR_2026-05-20_update.md](PLTR_2026-05-20_update.md) (snapshot 13:00 UTC)
> **Contexte :** Snapshot officiel du pipeline matinal. Données de cours reflètent la séance du 2026-05-25.

---

## Résumé des Changements depuis l'Update Précédent (2026-05-20)

| Indicateur | 20/05 close | 25/05 10:00 | Δ |
|-----------|-------------|-------------|---|
| Cours close | **$135.26** | **$136.88** | **+1.20%** |
| Open / High / Low | — | $137.43 / $139.02 / $134.30 | High +$1.56 vs previous close |
| RSI 14j | **46.36** | **35.66** | **−10.70** |
| Volume jour | 29.70M | **27.48M** | **−7.5%** |
| Volume vs moy. 20j | −31.8% | **−32.4%** | **Compression identique** |
| ATR 14j | **5.62** | **5.35** | **−4.8%** |
| MM 50j | **143.54** | **142.64** | **−$0.90** |
| Max Pain options | $140.00 | **$140.00** | **0** |
| Put/Call Ratio | 0.61 | **0.48** | **−0.13** |
| Call OI % | 62.2% | **67.4%** | **+5.2 pp** |
| Score Catalyseur | 6.8/10 | **6.8/10** | **0** |
| Score Valorisation | 4.5/10 | **4.5/10** | **0** |
| Score Momentum | 5.0/10 | **3.5/10** | **−1.5** |
| Score Opportunité | 5.4/10 | **5.1/10** | **−0.3** |
| Score Global ajusté | 46.3/100 | **42.5/100** | **−3.8** |
| Action | SURVEILLER | **SURVEILLER** | **→ Confirmé** |

**Verdict :** Le cours progresse légèrement (+1.2%) mais le momentum technique se dégrade nettement. Le RSI chute de 10.7 pts et franchit le seuil 40 vers le bas, signalant un retour en zone de survente technique. Le volume reste compressé (−32.4%). Les options montrent un biais haussier renforcé (Put/Call 0.48, Call OI 67.4%). Le score Momentum est révisé à la baisse (−1.5 pt), entraînant une dégradation du Score Global ajusté (−3.8 pts). **Thèse SURVEILLER confirmée mais avec un timing technique plus défavorable.**

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|-----------|--------|-------------|
| Cours | **$136.88** | +1.2% vs close 20/05, mais −0.39% vs previous close 137.415 |
| RSI 14j | **35.66** | 🔴 **Entrée en zone de survente (< 40)** — dynamique baissière renforcée |
| MM 50j | **142.64** | Cours **−4.0% sous MM50** — écart réduit vs −5.8% précédent mais résistance intacte |
| MM 200j | — | [DONNÉES MANQUANTES] |
| Golden/Death Cross | Non | Aucun signal de croisement |
| Volume relatif vs 20j | **−32.4%** | 27.48M vs 40.64M moy. — compression persistante, pas de retour institutionnel |
| Fourchette 52 semaines | $118.93 / $207.52 | Positionné à 22% du range (plus bas que 35% précédent) |
| ATR 14j | **$5.35** | Volatilité en légère contraction (−4.8%) |
| Beta | **1.521** | Élevé — amplifie les rotations sectorielles |
| Timing verdict | **Défavorable** | Sous MM50 + RSI < 40 + volume sous moyenne |

**Évolution vs snapshot 20/05 :**
- **Cours** : +$1.62 (+1.2%) mais close sous l'open ($137.43) — session faible avec rejet du high à $139.02.
- **RSI** : 46.36 → **35.66** — 🔴 franchissement du seuil 40 vers le bas. Sortie de la zone neutre inférieure pour entrer en survente technique. Signal négatif.
- **Volume** : 27.48M (−32.4% vs 20j), en ligne avec le niveau de la semaine dernière. Aucun signal de retour institutionnel.
- **MM50** : 143.54 → 142.64 — résistance descendante se rapproche légèrement, mais le cours reste sous ce niveau.
- **Options** : Put/Call 0.61 → **0.48**, Call OI 62.2% → **67.4%**. Biais haussier modérément renforcé. Max Pain stable à $140.00.

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
| ROIC (FMP key metrics) | 17.9% | Création de valeur confirmée |
| Consensus Price Target | $186.15 | 34 analysts — upside théorique **+35.9%** |

### Divergences Yahoo vs FMP [DONNÉES PARTIELLES]

| Métrique | Yahoo Finance | FMP Annual FY2025 | Écart |
|---------|---------------|-------------------|-------|
| Market Cap | $328.1 Md | $421.2 Md | **+28%** |
| P/E | 153.8x | 259.2x | **+68%** |
| EV/Revenue | 61.3x | 93.8x | **+53%** |
| EV/EBITDA | 158.8x | 291.6x | **+84%** |
| P/B | 38.8x | 57.0x | **+47%** |

**Interprétation :** Écart persistant entre sources, inchangé en proportion. Les multiples restent extrêmes dans les deux cas, justifiant le Score Valorisation contenu (4.5/10). Aucune nouvelle donnée fondamentale depuis le 20/05.

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
| Put/Call Ratio | **0.48** | Biais modéré vers les calls, renforcé vs 0.61 précédent |
| Call OI % | **67.4%** | Appétence haussière modérée, en hausse de 5.2 pp |
| Short Interest | 2.77% | Faible — pas de setup short squeeze |
| Insider Trades | — | [DONNÉES MANQUANTES] |
| Upgrades/Downgrades | — | [DONNÉES MANQUANTES] |
| Événements Corporate | Aucun | `data/events_latest.json` vide pour PLTR |

**Catalyseur prochain :** Earnings Q2 FY2026 le **2026-08-03** (70 jours). Est. EPS $0.32–$0.40, Rev $1.8B. Pas de preview requis (> 5j).

**Notes options :** La structure options montre un biais haussier renforcé malgré la dégradation technique. Put/Call 0.48 (vs 0.61) et Call OI 67.4% (vs 62.2%) suggèrent que le marché options anticipe un rebond ou maintient des positions haussières. Max Pain $140.00 cohérent avec le spot $136.88 — zone de gravitation options à +2.3%.

---

## Scoring Global — Révision

| Axe | Score 25/05 | Score 20/05 | Δ | Pondération (Unknown) |
|-----|-------------|-------------|---|---------------------|
| Catalyseur | **6.8/10** | 6.8/10 | 0 | 35% |
| Valorisation | **4.5/10** | 4.5/10 | 0 | 40% |
| Momentum | **3.5/10** | 5.0/10 | **−1.5** | 25% |
| **Score Opportunité** | **5.1/10** | **5.4/10** | **−0.3** | — |

**Score Global brut :** 51.0/100  
**Score Global ajusté :** **42.5/100** (malus technique et structuraux)  
**Action :** **SURVEILLER**

**Explication :** Le score Momentum est révisé à la baisse de 1.5 pt, reflétant le franchissement du RSI sous 40 (35.66) et la persistance du volume compressé. Le cours progresse légèrement (+1.2%) mais la dynamique sous-jacente s'est dégradée. L'écart MM50 se réduit (−4.0% vs −5.8%) mais la résistance dynamique reste intacte. Les options renforcent leur biais haussier (Put/Call 0.48, Call OI 67.4%), ce qui constitue un facteur mitigant. Pas d'entrée avant confirmation technique (franchissement MM50 à $142.64 avec volume > moyenne 20j > 40M) ou rebond RSI au-dessus de 40.

---

## Niveaux et Ratio R/R

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| Cours actuel | $136.88 | — |
| Entrée suggérée | $136.88 | — |
| Stop-loss suggéré | **$126.18** | Cours − 2×ATR = $136.88 − $10.70 |
| Take-profit suggéré | **$152.93** | Cours + 3×ATR = $136.88 + $16.05 |
| Ratio R/R | **1.5** | Ratio institutionnel standard |
| Upside vers consensus PT | +35.9% | $186.15 — horizon long terme |
| Max Pain (exp. 2026-05-29) | **$140.00** | +2.3% au-dessus du spot — zone de gravitation options |

*Niveaux révisés vs 20/05 : ATR légèrement plus faible ($5.35 vs $5.62), cours légèrement plus élevé. SL/TP ajustés en conséquence.*

---

## Contexte Macro, Sectoriel & Risques

| Facteur | État | Impact PLTR |
|---------|------|-------------|
| Régime macro | Unknown (VIX/DXY/taux non alimentés) | Pas d'ajustement régime-aware applicable |
| DXY | Stable | Neutre — pas de divergence FX détectée |
| XLK (Technology) | **Top sector** — Momentum 10.0/10, RS 20j +8.15% | **Vent favorable** structurel inchangé |
| Beta 1.52 | Élevé | Amplifie les rotations sectorielles |
| Geo Risk | Score 0 | Pas d'événement géopolitique spécifique (`data/geo_risk_latest.json`) |
| Accounting Risk | [DONNÉES MANQUANTES] | `data/accounting_risk_latest.json` absent — agent skipped |
| Quant Calibration | Insuffisant | Pas assez de signaux historiques (`p_value` 1.0) — calibration en cours |
| Social Sentiment | No data | Pas de signal retail exploitable |
| FX Exposure | 55% export EUR/CNY | FX Impact Score 0.0 — neutral, divergence aligned |
| Options Data Quality | ✅ Stable | Max Pain cohérent ($140), Put/Call 0.48, Call OI 67.4% — signaux exploitables |

---

## Conclusion — État de la Thèse

**Statut : SURVEILLER — Thèse confirmée mais avec dégradation technique. Le momentum s'est affaibli (RSI 35.66 < 40) alors que le cours stagne légèrement au-dessus du précédent close.**

**Arguments confirmants :**
- Marges opérationnelles et nettes excellentes (FMP FY2025 : GM 82%, OM 32%, NM 36%)
- Bilan solide : quasi-zero dette, current ratio 7.1, ROIC 18%
- Consensus analystes actif (34 analysts, PT $186.15 = +35.9% upside)
- XLK leader sectoriel (momentum 10.0/10) — environnement favorable aux techs
- Options renforçant leur biais haussier : Put/Call 0.48, Call OI 67.4%
- Aucune news négative détectée ce jour

**Arguments limitants :**
- 🔴 **RSI 35.66 — retour en zone de survente technique (< 40)**
- Timing technique défavorable : sous MM50 (−4.0%), volume **−32.4% sous moyenne 20j**
- Multiples extrêmes quel que soit la source (P/E 154x–259x, EV/Revenue 61x–94x)
- Divergence data Yahoo vs FMP sur toutes les métriques de valorisation [DONNÉES PARTIELLES]
- Accounting risk non évalué (agent absent) — qualité comptable non confirmée
- Aucune news ni catalyseur immédiat avant earnings août

**Scénarios :**
1. **Optimiste (20%)** : Rebond technique sur support $134–$135 + retour du volume institutionnel → test MM50 ($142.64) puis consolidation
2. **Central (55%)** : Consolidation latérale $130–$142 en l'absence de catalyseur jusqu'à earnings août, RSI oscillant 30–45
3. **Pessimiste (25%)** : Rupture du support $134 sous volume → test du support majeur $118.93 (52w low)

**Prochaines étapes :**
- Surveiller le franchissement du RSI au-dessus de 40 — signal de sortie de survente
- Surveiller le franchissement de la MM50 ($142.64) avec volume supérieur à la moyenne 20j (> 40M)
- Préparer `_preview.md` si earnings approchent à ≤ 5 jours (actuellement 70j)
- Réactiver l'agent accounting dès que possible pour valider le Filtre Qualité 6 critères
- Surveiller la cohérence des données options post-expiration 2026-05-29

---

## Validation Analyste Senior — Snapshot 10:00 UTC

**Analyste :** Desk Argus-IA  
**Timestamp validation :** 2026-05-25 10:00 UTC  
**Status :** ✅ Confirmé — snapshot 10:00 UTC, données actualisées avec dégradation technique significative (RSI < 40).

| Check | Résultat |
|-------|----------|
| `data/latest.json` (10:00 UTC) | Cours $136.88, RSI 35.66, ATR 5.35, MM50 142.64, Volume 27.48M — **RSI franchi < 40** |
| Options (10:00 UTC) | Max Pain $140.00 ✅, Put/Call 0.48, Call OI 67.4% — **biais haussier renforcé** |
| `data/recommandations_latest.json` | Scores révisés : C 6.8 / V 4.5 / M **3.5** → Opp **5.1** / Global **42.5** |
| `data/geo_risk_latest.json` | Score 0, aucun ticker PLTR flaggé |
| `data/fx_exposure_latest.json` | FX Impact Score 0.0, divergence aligned, pas de headwind |
| `data/events_latest.json` | Aucun événement corporate détecté |
| `data/news_latest.json` | Aucune news PLTR dans le snapshot Yahoo |
| `data/social_sentiment_latest.json` | No data — pas de signal retail |
| `data/upcoming_events_latest.json` | Earnings Q2 FY2026 confirmé 2026-08-03 (70j) |
| `data/quant_report_latest.json` | Pas assez de signaux historiques (p-value 1.0) — calibration en cours |
| `data/sector_rotation_latest.json` | XLK top sector (momentum 10.0/10) — vent favorable inchangé |
| Accounting Risk | `data/accounting_risk_latest.json` absent — risque méthodologique persistant |
| Data Quality Alert | ✅ Stable — Max Pain $140.00 (cohérent vs spot $136.88) |

**Conclusion validation :** Le snapshot 10:00 UTC du 2026-05-25 montre une **dégradation technique significative** malgré un cours légèrement supérieur (+1.2%). Le RSI a franchi le seuil 40 vers le bas (35.66), signalant un retour en zone de survente. Le volume reste compressé (−32.4%). Le score Momentum est révisé à la baisse (−1.5 pt → 3.5/10), entraînant une dégradation du Score Global ajusté (−3.8 pts → 42.5/100). La structure options, elle, renforce son biais haussier (Put/Call 0.48, Call OI 67.4%), ce qui constitue un facteur mitigant. La thèse **SURVEILLER** reste inchangée mais le timing d'entrée est davantage conditionné à un rebond RSI au-dessus de 40 et au franchissement de la MM50 ($142.64) avec volume > 40M.

# CTMX — Mise à Jour — Snapshot 2026-06-16 10h UTC

> **Société :** CytomX Therapeutics, Inc.
> **Secteur :** Healthcare / Biotechnology — Probody therapeutics
> **Exchange :** NASDAQ
> **Date :** 2026-06-16
> **Snapshot :** 10:00 UTC (pré-ouverture US)
> **Analyste :** Desk Argus-IA

---

## Résumé Exécutif

**Stabilité mécanique totale** vs snapshot 21h UTC 2026-06-15. Le **close reste à $3.04** sur le snapshot 10h UTC, avec l'ensemble des données techniques inchangées : RSI 25.93, ATR $0.18, MM50 $3.90, volume 0.87× moyenne 20j. Aucune mutation de cours, de momentum ou de structure n'est détectée sur ce snapshot pré-ouverture.

**Anomalie options JSON 6e occurrence** détectée et traitée : max pain $6.00 (aberrant, conservé à $4.00), put/call ratio 0.0 (aberrant, conservé à 0.14), call OI 100.0% (aberrant, conservé à 87.8%). L'expiration demain (2026-06-18) maintient le pin risk haussier vers $4.00.

**DRAFT_refresh classé faux positif** : le trigger `ATR_SPIKE` (5.92%) a été déclenché par `agents/detect_major_events/agent.py` mais l'ATR n'a pas muté ($0.18 stable vs snapshot précédent). Aucun événement majeur ne confirme, modifie ou invalide la thèse.

Le **Score Global Ajusté reste à 55.0/100** et le **Score Opportunité à 5.8/10** (C:6.5 V:6.0 M:4.5). La recommandation reste **ATTENDRE**. Le timing reste **Défavorable**.

---

## Changements depuis l'Analyse Précédente (Snapshot 2026-06-15 21h UTC)

### 1. Technique — Stabilité totale

| Indicateur | 15/06 21h UTC | 16/06 10h UTC | Signal |
|---|---|---|---|
| Cours close | **$3.04** | **$3.04** | **Inchangé** |
| Previous close | $3.01 | **$3.01** | — |
| Open / High / Low | 3.05 / 3.13 / 2.98 | **3.05 / 3.13 / 2.98** | Inchangé |
| Volume | 2,921,174 | **2,921,200** | **Stable** (diff. < 0.001%) |
| Volume rel. 20j | 0.87× | **0.87×** | **Inchangé** |
| RSI 14j | 25.93 | **25.93** | **Inchangé** — survente extrême persistante |
| ATR 14j | $0.18 | **$0.18** | **Inchangé** |
| MM 50j | $3.90 | **$3.90** | **Stable** |
| MM 200j | null | **null** | [DONNÉES PARTIELLES] |
| Short Interest | 14.97% | **14.97%** | **Stable** |
| 52W High / Low | $8.21 / $1.72 | **$8.21 / $1.72** | — |

**Verdict technique :** Aucune mutation technique. Le snapshot 10h UTC du 16/06 reproduit mécaniquement les données du close 21h UTC du 15/06 (pré-ouverture US). Le RSI à 25.93 reste en survente extrême. L'écart MM50 est stable à **−22.1%**. Le support $2.98 (low) n'a pas été retesté. Le timing reste **Défavorable** — position sous MM50 et tendance baissière persistante.

### 2. Options — Anomalie JSON 6e occurrence, valeurs opérationnelles conservées

| Indicateur | 15/06 21h UTC | 16/06 10h UTC (JSON brut) | Valeur conservée | Signal |
|---|---|---|---|---|
| Max Pain | $4.00 | **$6.00** | **$4.00** | Anomalie JSON 6e occurrence — valeur aberrante rejetée |
| Put/Call Ratio | 0.14 | **0.00** | **0.14** | Anomalie JSON — cohérence interne rejetée |
| Call OI % | 87.8% | **100.0%** | **87.8%** | Anomalie JSON — cohérence interne rejetée |
| Expiration proche | 2026-06-18 | **2026-06-18** | **Demain** (~1 jour) | Inchangé |

**Verdict options :** La structure options reste **très haussière** sur la base des valeurs opérationnelles conservées ($4.00 / 0.14 / 87.8%). L'anomalie JSON récurrente (max pain aberrant, put/call nul, call OI 100%) est un artefact de parsing sans impact sur l'interprétation. Le spot à $3.04 est sous le max pain $4.00 avec expiration demain — le pin risk haussier reste actif.

### 3. Fondamental — Aucun changement

Données FMP FY2025 inchangées. Pas de nouveau filing SEC, pas de guidance update, pas de nouvelles collaborations annoncées.

| Métrique | Valeur | Statut |
|----------|--------|--------|
| Market Cap (Yahoo) | **$661.8M** | Stable |
| Market Cap (FMP) | $587.6M | — |
| EV/Revenue | 8.946 (Yahoo) / 7.60 (FMP) | Élevé pour biotech pré-commercial |
| Forward P/E | −6.26 | Pertes attendues |
| Short Interest | **14.97%** | Stable |
| Current Ratio | 3.09 | Trésorerie confortable |
| Cash / Working Capital | $97.3M / $97.3M | Runway ~2–3 ans |
| Filtre Qualité | **2/6** | Hors périmètre (inchangé) |

**Consensus Analystes (FMP) :**
- Price target moyen : **$9.05** (+198% upside vs $3.04)
- Nombre d'analystes : **11** (1 ce mois, 4 ce trimestre)
- Sources : TheFly, StreetInsider, Benzinga

### 4. Sentiment / News / Social

| Indicateur | 15/06 21h UTC | 16/06 10h UTC | Signal |
|---|---|---|---|
| News pipeline | Aucune | **Aucune** | — |
| Social Sentiment | 0/10 | **0/10** | Aucun intérêt retail |
| Pump detection | Non | **Non** | — |

**Verdict sentiment :** Neutre à baissier. Aucune news, aucun intérêt retail. Le consensus analystes reste le seul soutien haussier structurel (PT +198%). Le short interest stable à 14.97% maintient le potentiel de short squeeze, mais aucun catalyseur déclencheur n'est visible.

---

## Contexte Sectoriel & Macro

| Facteur | Impact | Détail |
|---------|--------|--------|
| **XLV (Healthcare)** | Défensif | `data/sector_rotation_latest.json` (2026-06-16) : régime UNKNOWN, données RS non exploitables (NaN). XLV momentum_score 10.0 (artefact — pas de donnée réelle). |
| **Biotech spécifique** | Risque élevé | Sous-secteur biotech early-stage reste pénalisé. Pas de rotation sectorielle détectée. |
| **DXY / FX** | Neutre | `data/fx_exposure_latest.json` (2026-06-16) : CTMX exposure ~55% EUR/CNY, FX Impact Score **0.0** — aucun headwind/tailwind. |
| **Geo risk** | Non flaggé | `data/geo_risk_latest.json` (2026-05-17) : CTMX non présent, aucun risque géo détecté. |
| **Accounting risk** | Scan indisponible | `data/accounting_risk_latest.json` absent — pas de M-Score/Z-Score. |
| **Event-driven** | Aucun | `data/events_latest.json` (2026-06-16) : 0 événement corporate détecté pour CTMX. |
| **Earnings** | J+51 | Earnings confirmé le **2026-08-06** (Est EPS $−0.13 à $−0.07, Rev $0.0B). Pas de preview requis. |
| **Quant** | Calibration en cours | `data/quant_report_latest.json` (2026-05-17) : 0 signaux, p-value null — pas assez d'historique. |
| **Social Sentiment** | Aucun | `data/social_sentiment_latest.json` (2026-06-16) : CTMX 0 mentions, sentiment 0/10, pump non détecté. |
| **Validation** | OK | `data/validation_report.txt` (2026-06-16) : 0 CRITICAL, CTMX non concerné par les 5 errors / 2 warnings. |

---

## Scoring Global (Agents)

| Axe | Score | Pondération Régime Normal | Contribution | Justification |
|-----|-------|---------------------------|------------|---------------|
| Catalyseur | **6.5/10** | 35% | 2.28 | Pipeline Probody + partenariats majeurs. Structure options très haussière (call OI 87.8%) avec expiration demain — pin risk haussier. Volume normalisé (0.87×). |
| Valorisation | **6.0/10** | 40% | 2.40 | Biotech pré-profit, PT consensus +198% offre upside asymétrique. Plafonné par Filtre Qualité 2/6. |
| Momentum | **4.5/10** | 25% | 1.13 | RSI 25.93 survente extrême. Volume normalisé 0.87×, mais cours sous MM50 ($3.90, écart −22.1%) et tendance baissière persistante. |
| **Score Opportunité** | **5.8/10** | — | — | **Inchangé** vs snapshot 21h UTC 15/06 |
| **Malus** | | | −3.0 | Biotech pre-revenue + pertes (Filtre Qualité ≤ 3/6) |
| **Bonus** | | | +0.0 | Aucun bonus détecté |
| **Score Global** | **58.0/100** | | | Inchangé vs snapshot 21h UTC 15/06 |
| **Score Global Ajusté** | **55.0/100** | | | **Inchangé** — reste au-dessus du seuil institutionnel (50) |

**Action recommandée :** **ATTENDRE** *(inchangée)*
**Timing :** Défavorable *(inchangé)*
**Sizing :** — (pas de position recommandée)

**Note de fiabilité :** Score Global Ajusté 55.0/100 — au-dessus du seuil institutionnel. Aucune mutation technique ou fondamentale depuis le snapshot précédent. L'expiration options demain (2026-06-18) reste le catalyseur technique court terme le plus proche. Le DRAFT_refresh est un faux positif — pas de réécriture de thèse nécessaire.

---

## Révision des Niveaux SL / TP

Aucune révision nécessaire. SL/TP conservés sur base ATR $0.18 et close $3.04.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix de référence | **$3.04** | Close 2026-06-16 10h UTC |
| Stop-loss suggéré | **$2.68** | Cours ref − 2×ATR ($3.04 − $0.36) — aligné avec agent Recommandation |
| Take-profit technique | **$3.58** | Cours ref + 3×ATR ($3.04 + $0.54) — aligné avec agent Recommandation |
| Take-profit consensus | **$9.05** | Price target moyen analystes |
| Ratio R/R (technique) | **1.5** | $0.54 / $0.36 — aligné avec agent Recommandation |
| Ratio R/R (consensus) | **15.9** | $6.01 / $0.38 |
| Ratio R/R (max pain) | **2.7** | $0.96 / $0.36 | $4.00 max pain vs close $3.04 |

---

## Conclusion — Snapshot 10h UTC

**Thèse : NON ÉTABLIE — PROFIL SPÉCULATIF BIOTECH — ATTENDRE (INCHANGÉE)**

Le snapshot 10h UTC du 2026-06-16 enregistre une **stabilité mécanique totale** vs le snapshot 21h UTC du 15/06. Le **close reste à $3.04**, le **RSI à 25.93** (survente extrême), l'**ATR à $0.18**, la **MM50 à $3.90** (écart −22.1%) et le **volume à 0.87×** moyenne 20j. Aucune mutation de cours, de momentum ou de structure n'est détectée.

**Le développement clé est l'absence de changement** — le marché est en standby pré-ouverture US. La **structure options très haussière** (put/call 0.14, call OI 87.8%, max pain $4.00) avec expiration demain (2026-06-18) reste le catalyseur technique dominant. Le pin risk haussier vers $4.00 persiste.

Le **Score Global Ajusté reste à 55.0/100** et le **Score Opportunité à 5.8/10**. La recommandation reste **ATTENDRE**. Le timing reste **Défavorable** (inchangé) en raison de la position sous MM50 et de la tendance baissière persistante.

**Ce qui a changé depuis le snapshot 2026-06-15 21h UTC :**
- 🟡 Cours : **$3.04** (inchangé)
- 🟡 Volume : **0.87×** (inchangé)
- 🟡 RSI : **25.93** (inchangé, survente extrême persistante)
- 🟡 ATR : **$0.18** (inchangé)
- 🟡 MM50 : **$3.90** (stable)
- 🟢 Options : **anomalie JSON 6e occurrence traitée** (valeurs opérationnelles conservées : max pain $4.00, put/call 0.14, call OI 87.8%)
- 🟡 Short interest : **14.97%** (stable)
- 🟡 Timing : **Défavorable** (inchangé)
- 🟡 SL/TP : conservés **$2.68 / $3.58**
- 🟡 DRAFT_refresh : **classé faux positif** (ATR_SPIKE sans mutation — données identiques close 21h UTC 15/06)
- ❌ Aucune news majeure

---

## Mise à jour snapshot 17:00 UTC — Post-session US

---

## Résumé Exécutif — Snapshot 17h UTC

**Close à $2.93** (−3.62% vs previous_close $3.04) sur le snapshot 17h UTC. Le **RSI s'effondre à 17.16** (−8.77 pts vs snapshot 10h UTC), atteignant une **survente extrême historique** sur la période de suivi. L'**ATR 14j se rétracte légèrement à $0.17** (−$0.01) et la **MM50 glisse à $3.87** (−$0.03). Le **volume retombe à 0.73×** moyenne 20j (2.45M vs 3.34M) — **retour à l'anémie** après la normalisation de 0.87× observée au snapshot 10h UTC.

Le **support $2.98 est cassé** (low du jour $2.865) — premier break sous ce niveau depuis le test du 15/06. Le cours a ouvert à $3.03, testé $3.05 (high) puis dégringolé jusqu'à $2.865 avant de clôturer à $2.93. C'est une **distribution vendeuse** en fin de séance sans récupération.

La **structure options reste très haussière** — max pain $4.00 (cohérent), put/call ratio **0.14**, call OI **87.8%**, expiration **demain** (2026-06-18). Pas d'anomalie JSON sur ce snapshot — données propres. Le spot $2.93 reste très sous le max pain $4.00, maintenant la pression technique haussière (pin risk) mais avec un momentum réel qui s'inverse à la baisse.

Le **Score Global Ajusté remonte marginalement à 55.8/100** (+0.8 pt, `data/recommandations_latest.json`) et le **Score Opportunité à 5.9/10** (C:6.5 V:6.5 M:4.0). Le momentum est dégradé (−0.5 pt) mais la valorisation est réévaluée à la hausse (+0.5 pt) sur le cours plus faible. La recommandation reste **ATTENDRE**. Le timing reste **Défavorable**.

---

## Changements depuis l'Analyse Précédente (Snapshot 2026-06-16 10h UTC)

### 1. Technique — Distribution baissière, support cassé, RSI en survente extrême

| Indicateur | 16/06 10h UTC | 16/06 17h UTC | Signal |
|---|---|---|---|
| Cours close | **$3.04** | **$2.93** | **−3.62%** |
| Previous close | $3.01 | **$3.04** | — |
| Open / High / Low | 3.05 / 3.13 / 2.98 | **3.03 / 3.05 / 2.865** | Low $2.865 (support $2.98 cassé) |
| Volume | 2,921,200 | **2,446,956** | **−16.2%** |
| Volume rel. 20j | 0.87× | **0.73×** | **Anémie revenant** |
| RSI 14j | 25.93 | **17.16** | **−8.77 pts** — survente extrême historique |
| ATR 14j | $0.18 | **$0.17** | **−$0.01** — volatilité légèrement en contraction |
| MM 50j | $3.90 | **$3.87** | **Glissement baissier** |
| MM 200j | null | **null** | [DONNÉES PARTIELLES] |
| Short Interest | 14.97% | **14.97%** | **Stable** |
| 52W High / Low | $8.21 / $1.72 | **$8.21 / $1.72** | — |

**Verdict technique :** Le mouvement de −3.62% à $2.93 est une **distribution vendeuse** confirmée par le break du support $2.98 (low $2.865). Le RSI à 17.16 est une survente extrême rare — le plus bas observé sur la période de suivi Argus-IA (précédent plancher : 23.02 le 2026-06-10). Cela indique un épuisement vendeur potentiel, mais le manque de volume (0.73×) suggère que l'achat n'est pas non plus au rendez-vous. L'écart MM50 s'aggrave à **−24.3%** (vs −22.1%). La MM50 glisse à $3.87, confirmant la tendance baissière. Le timing reste **Défavorable** — la survente RSI n'est pas suffisante pour compenser la position sous MM50 et le break de support.

### 2. Options — Structure très haussière inchangée, données propres

| Indicateur | 16/06 10h UTC | 16/06 17h UTC | Signal |
|---|---|---|---|
| Max Pain | $4.00 (conservé) | **$4.00** | **Stable** — cohérent, pas d'anomalie |
| Put/Call Ratio | 0.14 (conservé) | **0.14** | **Stable** — très haussier |
| Call OI % | 87.8% (conservé) | **87.8%** | **Stable** — dominance calls |
| Expiration proche | 2026-06-18 | **2026-06-18** | **Demain** (~1 jour) |

**Verdict options :** La structure options reste **très haussière** et inchangée. Le spot à $2.93 est désormais **$1.07 sous le max pain $4.00** avec expiration demain. La combinaison put/call 0.14 + call OI 87.8% + spot sous max pain crée une pression technique haussière maximale (pin risk). Cependant, le momentum réel du jour (−3.62%, volume faible) va à l'encontre de ce signal options. Le pin risk reste le catalyseur technique dominant mais il est maintenant en conflit avec la distribution vendeuse observée.

### 3. Fondamental — Aucun changement

Données FMP FY2025 inchangées. Pas de nouveau filing SEC, pas de guidance update, pas de nouvelles collaborations annoncées.

| Métrique | Valeur | Statut |
|----------|--------|--------|
| Market Cap (Yahoo) | **$637.9M** | Rétracté avec le cours (−3.6%) |
| Market Cap (FMP) | $587.6M | — |
| EV/Revenue | 8.946 (Yahoo) / 7.60 (FMP) | Élevé pour biotech pré-commercial |
| Forward P/E | −6.03 | Pertes attendues |
| Short Interest | **14.97%** | Stable |
| Current Ratio | 3.09 | Trésorerie confortable |
| Cash / Working Capital | $97.3M / $97.3M | Runway ~2–3 ans |
| Filtre Qualité | **2/6** | Hors périmètre (inchangé) |

**Consensus Analystes (FMP) :**
- Price target moyen : **$9.05** (+209% upside vs $2.93)
- Nombre d'analystes : **11** (1 ce mois, 4 ce trimestre)
- Sources : TheFly, StreetInsider, Benzinga

### 4. Sentiment / News / Social

| Indicateur | 16/06 10h UTC | 16/06 17h UTC | Signal |
|---|---|---|---|
| News pipeline | Aucune | **Aucune** | — |
| Social Sentiment | 0/10 | **0/10** | Aucun intérêt retail |
| Pump detection | Non | **Non** | — |

**Verdict sentiment :** Neutre à baissier. Aucune news, aucun intérêt retail. Le consensus analystes reste le seul soutien haussier structurel (PT +209%). Le short interest stable à 14.97% maintient le potentiel de short squeeze, mais aucun catalyseur déclencheur n'est visible. Le mouvement de −3.62% sans news suggère soit un stop-loss institutionnel déclenché, soit un arbitrage pre-expiration options.

---

## Contexte Sectoriel & Macro — Actualisé 17h UTC

| Facteur | Impact | Détail |
|---------|--------|--------|
| **XLV (Healthcare)** | Défensif sous-performant | `data/sector_rotation_latest.json` (2026-06-16) : XLV momentum_score **3.55** (rang 6e/11, corrigé vs 10.0 artefact matinal), return_20d +5.63% vs SPY +1.79% — surperformance relative mais momentum modéré. Healthcare reste un secteur défensif sous-performant sur 60j (RS −9.37%). |
| **Biotech spécifique** | Risque élevé | Sous-secteur biotech early-stage reste pénalisé. Rotation vers la tech (XLK momentum 10.0) continue de drainer les flux. |
| **Rotation sectorielle** | `NEUTRAL` | Signal macro du jour : régime UNKNOWN, top3 = XLK / XLF / XLB, bottom3 = XLE / XLU / XLC. Healthcare neutre. |
| **DXY / FX** | Neutre | `data/fx_exposure_latest.json` (2026-06-16) : CTMX exposure ~55% EUR/CNY, FX Impact Score **0.0** — aucun headwind/tailwind. |
| **Geo risk** | Non flaggé | `data/geo_risk_latest.json` (2026-05-17) : CTMX non présent, aucun risque géo détecté. |
| **Accounting risk** | Scan indisponible | `data/accounting_risk_latest.json` absent — pas de M-Score/Z-Score. |
| **Event-driven** | Aucun | `data/events_latest.json` (2026-06-16) : 0 événement corporate détecté pour CTMX. |
| **Earnings** | J+51 | Earnings confirmé le **2026-08-06** (Est EPS $−0.13 à $−0.07, Rev $0.0B). Pas de preview requis. |
| **Quant** | Calibration en cours | `data/quant_report_latest.json` (2026-05-17) : 0 signaux, p-value null — pas assez d'historique. |
| **Social Sentiment** | Aucun | `data/social_sentiment_latest.json` (2026-06-16) : CTMX 0 mentions, sentiment 0/10, pump non détecté. |
| **Upcoming Events** | J+1 | `data/upcoming_events_latest.json` (2026-06-16) : expiration options **2026-06-18** (J+1). Pas d'autre événement structurant. |

---

## Scoring Global (Agents) — Actualisé 17h UTC

| Axe | Score | Pondération Régime Normal | Contribution | Justification |
|-----|-------|---------------------------|------------|---------------|
| Catalyseur | **6.5/10** | 35% | 2.28 | Pipeline Probody + partenariats majeurs. Structure options très haussière (call OI 87.8%) avec expiration demain — pin risk haussier. Volume faible (0.73×) atténue la crédibilité. |
| Valorisation | **6.5/10** | 40% | 2.60 | Biotech pré-profit, PT consensus +209% offre upside asymétrique accru sur le cours plus faible. Plafonné par Filtre Qualité 2/6. |
| Momentum | **4.0/10** | 25% | 1.00 | RSI 17.16 survente extrême historique (signal d'épuisement). Volume anémique 0.73×. Cours sous MM50 ($3.87, écart −24.3%), support $2.98 cassé. |
| **Score Opportunité** | **5.9/10** | — | — | **+0.1 pt** vs snapshot 10h UTC (valorisation ↑, momentum ↓) |
| **Malus** | | | −3.0 | Biotech pre-revenue + pertes (Filtre Qualité ≤ 3/6) |
| **Bonus** | | | +0.0 | Aucun bonus détecté |
| **Score Global** | **58.8/100** | | | +0.8 pt vs snapshot 10h UTC |
| **Score Global Ajusté** | **55.8/100** | | | **+0.8 pt** — reste au-dessus du seuil institutionnel (50) |

**Action recommandée :** **ATTENDRE** *(inchangée)*
**Timing :** Défavorable *(inchangé)*
**Sizing :** — (pas de position recommandée)

**Note de fiabilité :** Score Global Ajusté 55.8/100 — au-dessus du seuil institutionnel mais stable. Le développement clé de la session US est la **distribution vendeuse de −3.62% avec break du support $2.98** et RSI à 17.16 (survente extrême historique). La structure options très haussière (put/call 0.14, call OI 87.8%) avec expiration demain reste le catalyseur technique dominant, mais elle est maintenant en conflit avec le momentum baissier réel. Le faible volume (0.73×) indique une absence de conviction des deux côtés — ni vente paniquée, ni achat opportuniste.

---

## Révision des Niveaux SL / TP — Actualisée 17h UTC

SL/TP recalculés sur base ATR $0.17 et close $2.93.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix de référence | **$2.93** | Close 2026-06-16 17h UTC |
| Stop-loss suggéré | **$2.59** | Cours ref − 2×ATR ($2.93 − $0.34) — aligné avec agent Recommandation |
| Take-profit technique | **$3.44** | Cours ref + 3×ATR ($2.93 + $0.51) — aligné avec agent Recommandation |
| Take-profit consensus | **$9.05** | Price target moyen analystes |
| Ratio R/R (technique) | **1.5** | $0.51 / $0.34 — aligné avec agent Recommandation |
| Ratio R/R (consensus) | **16.9** | $6.12 / $0.34 |
| Ratio R/R (max pain) | **3.1** | $1.07 / $0.34 | $4.00 max pain vs close $2.93 |

**Attention :** Le ratio R/R consensus reste trompeur pour une biotech pré-revenue. Le risque de gap-down en cas d'échec clinique peut dépasser 50%. Le support $2.98 a été cassé (low $2.865) — le nouveau support immédiat est $2.86 (low du jour). La structure options haussière (expiration demain) crée un catalyseur technique court terme vers $4.00 (max pain), mais le momentum baissier de la session US va à l'encontre de ce signal. Si le cours clôture demain au-dessus de $3.00 avec volume > 0.8× moyenne, cela confirmerait un rebond technique. Un clôture sous $2.86 avec volume > 0.8× activerait la dégradation vers SURVEILLER.

---

## Conclusion — Snapshot 17h UTC

**Thèse : NON ÉTABLIE — PROFIL SPÉCULATIF BIOTECH — ATTENDRE (INCHANGÉE)**

Le snapshot 17h UTC du 2026-06-16 enregistre un **close à $2.93** (−3.62% vs snapshot 10h UTC) avec des données techniques **dégradées**. Le **RSI s'effondre à 17.16** (−8.77 pts), atteignant une survente extrême historique. L'**ATR se rétracte légèrement à $0.17** et la **MM50 glisse à $3.87** (écart −24.3%). Le **volume retombe à 0.73×** moyenne 20j — **retour à l'anémie** après la normalisation de 0.87× observée au snapshot 10h UTC. Le **support $2.98 est cassé** (low $2.865) — première cassure depuis le test du 15/06.

**Le développement clé de la session US est la distribution vendeuse de −3.62% avec break du support $2.98**, invalidant le signal de consolidation du snapshot 10h UTC. Le RSI 17.16 est un signal d'épuisement vendeur rare, mais le volume faible (0.73×) indique une absence de conviction des deux côtés. La **structure options reste très haussière** (put/call 0.14, call OI 87.8%, max pain $4.00) avec expiration demain (2026-06-18) — le pin risk haussier persiste mais est maintenant en conflit avec le momentum baissier.

Le **Score Global Ajusté remonte marginalement à 55.8/100** (+0.8 pt) et le **Score Opportunité à 5.9/10** (+0.1 pt). La hausse du score est mécanique — la valorisation s'améliore sur un cours plus faible (+209% upside), compensant la dégradation du momentum. La recommandation reste **ATTENDRE**. Le timing reste **Défavorable** (inchangé) en raison de la position sous MM50, du break de support et de la tendance baissière persistante.

**Ce qui a changé depuis le snapshot 2026-06-16 10h UTC :**
- 🔴 Cours : **$2.93** (−3.62%)
- 🔴 Volume : **0.73×** (anémie revenant vs 0.87×)
- 🔴 RSI : **17.16** (−8.77 pts, survente extrême historique — nouveau plancher)
- 🟡 ATR : **$0.17** (−$0.01, volatilité en contraction)
- 🔴 MM50 : **$3.87** (glissement baissier −$0.03, écart −24.3%)
- 🔴 Support : **$2.98 cassé** (low $2.865 — distribution vendeuse)
- 🟢 Options : **structure très haussière inchangée** (max pain $4.00, put/call 0.14, call OI 87.8%), **pas d'anomalie JSON**
- 🟡 Short interest : **14.97%** (stable)
- 🟡 Scores : Global Ajusté **55.8/100** (+0.8 pt), Opportunité **5.9/10** (+0.1 pt), Valorisation **6.5/10** (+0.5 pt), Momentum **4.0/10** (−0.5 pt)
- 🟡 SL/TP : révisés **$2.59 / $3.44** (−$0.09 / −$0.14 mécaniquement)
- 🔴 Timing : **Défavorable** (inchangé mais renforcé par le break de support)
- ❌ Aucune news majeure — mouvement purement technique / pre-expiration

**Conditions de passage à ACHETER :**
1. Consolidation au-dessus de $3.00 avec volume > 0.8× moyenne (recapture du support)
2. Clôture au-dessus du max pain $4.00 post-expiration (2026-06-18)
3. Data readout positif CX-2029 ou CX-904 (catalyseur clinique majeur)
4. Nouveau partenariat avec upfront significatif (> $100M)

**Conditions de passage à SURVEILLER (dégradation) :**
1. Clôture sous $2.86 avec volume > 0.8× moyenne (nouveau support cassé)
2. Volume s'effondrant sous 0.4× moyenne sur rebond (pas de conviction)
3. Break sous $2.80 avec volume > 0.8× moyenne

**Conditions de passage à ÉVITER :**
1. Échec clinique majeur (stop essai)
2. Dilution capitale > 20% sans catalyseur
3. Perte d'un partenariat stratégique (AbbVie/BMS)

**Alertes actives :**
- 🔴 Cours $2.93 — −3.62% vs 10h UTC, high $3.05, low $2.865 (support $2.98 cassé)
- 🔴 Volume 0.73× — retour à l'anémie, pas de conviction achat ni vente
- 🔴 RSI 17.16 — survente extrême historique, épuisement vendeur potentiel
- 🔴 Support $2.98 **CASSÉ** — nouveau support $2.86 (low du jour)
- 🟢 Short interest 14.97% — stable, potentiel short squeeze si catalyseur
- 🔴 Cours sous MM50 ($3.87) avec écart −24.3%
- 🟡 Score Global Ajusté 55.8/100 — au-dessus du seuil institutionnel mais stable
- 🟡 Recommandation ATTENDRE — zone de risque technique accru
- 🟢 Options — **structure très haussière** (max pain $4.00, put/call 0.14, call OI 87.8%), expiration demain
- [WARNING] Données MM200 manquantes
- [WARNING] Biotech pré-revenue — scoring standard peu fiable
- [INFO] Earnings confirmé le 2026-08-06 (J+51) — Est EPS $−0.13 à $−0.07
- [INFO] Expiration options **demain** (2026-06-18) — volatilité potentielle, pin risk vers $4.00 vs spot $2.93

---

*Rapport généré automatiquement — snapshot 2026-06-16 17:00 UTC.*
*Analyse précédente : `CTMX_2026-06-16_update.md` (snapshot 10h UTC) — close $3.04, ATTENDRE.*

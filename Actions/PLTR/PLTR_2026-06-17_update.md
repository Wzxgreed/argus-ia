# PLTR — Mise à Jour Quotidienne (2026-06-17, snapshot 10h UTC)

> **Source :** `data/2026-06-17.json` (snapshot 2026-06-17T10:00:10Z) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [PLTR_2026-06-16_17-00_update.md](PLTR_2026-06-16_17-00_update.md) (snapshot 16/06 17h UTC)
> **Contexte :** Snapshot pré-séance US mercredi 17/06, 10h UTC. **Amélioration technique nette** : cours +1.70% vs close 16/06, volume recovery +78.7%, RSI franchit 50, écart MM50 réduit de −5.75% à −4.19%.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-16 17h UTC)

| Indicateur | Snapshot 16/06 17h UTC | Snapshot 17/06 10h UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours référence | $131.02 | **$133.25** | **+1.70%** — rebond technique |
| RSI 14j | 49.00 | **50.51** | **+1.51 pt** — franchissement zone 50 |
| Volume (close référence) | 16.96M | **30.31M** | **🟢 +78.7% — recovery majeur** |
| Volume vs 20j | 0.45× | **0.78×** | 🟢 **Normalisation en cours** |
| Short Interest | 3.23% | **3.23%** | = — inchangé |
| MM 50j | 139.02 | **139.07** | = — quasi-inchangée (+$0.05) |
| ATR 14j | 7.71 | **7.71** | = — stable |
| Consensus FMP PT | $187.47 (34 analystes) | **$187.47 (34 analystes)** | = — inchangé |
| Options Max Pain | $140.00 | **$140.00** | = — opérationnel (anomalie JSON détectée et traitée) |
| Options Put/Call | 0.68 | **0.68** | = — opérationnel (conservé) |
| Options Call OI % | 59.5% | **59.5%** | = — opérationnel (conservé) |
| Score Opportunité (calculé) | 5.4/10 | **5.6/10** | 🟢 **+0.2 pt** |
| Score Global (calculé) | 54.3/100 | **56.0/100** | 🟢 **+1.7 pt** |
| Score Global ajusté (calculé) | 46.3/100 | **48.0/100** | 🟢 **+1.7 pt** |
| Recommandation | SURVEILLER | **SURVEILLER** | = — maintenu |
| Timing | Défavorable | **Défavorable** | = — maintenu, mais nuance améliorée |
| Stop-loss suggéré | $115.60 | **$117.83** | 🟢 Révisé à la hausse (cours +1.70%) |
| Take-profit suggéré | $154.15 | **$156.38** | 🟢 Révisé à la hausse (cours +1.70%) |
| Cours vs MM50 | −5.75% | **−4.19%** | 🟢 **Écart réduit** |

**Verdict :** Le snapshot 10h UTC du 17/06 enregistre une **amélioration technique nette** par rapport au snapshot 17h UTC du 16/06. Le cours rebondit de +1.70% à $133.25, le volume récupère fortement à **30.31M (0.78× moyenne)** vs le collapse historique de 16.96M (0.45×), et le RSI franchit la zone 50 à **50.51** (+1.51 pt). L'écart sous la MM50 se réduit de −5.75% à **−4.19%**. Le consensus FMP, les fondamentaux FY2025 et la structure options (opérationnelle) sont strictement inchangés. Les scores calculés sont légèrement révisés à la hausse (Opportunité 5.6/10, Global ajusté 48.0/100). La recommandation **SURVEILLER** et le timing **Défavorable** sont maintenus, avec une **nuance technique nettement améliorée**.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (close référence) | $133.25 | +1.70% vs previous close $131.02 (16/06 17h) ; −1.08% vs previous close officiel $134.71 |
| Open | $134.59 | — |
| High | $134.59 | — |
| Low | $129.62 | — |
| RSI 14j | 50.51 | 🟡 Neutre-haussier — franchissement zone 50 |
| Volume 20j | 38,770,520 | 🟢 30.31M = **0.78× moyenne — recovery majeur** |
| 52W Range | $122.68–$207.52 | Cours à 8.6% du 52W low, 35.8% sous le 52W high |
| Short Interest | 3.23% | 🟡 Modéré — inchangé |
| MM 50j | 139.07 | 🔴 Cours −4.19% sous MM50 — cassure maintenue mais écart réduit |
| ATR 14j | 7.71 | 🟡 Stable — inchangé |

**Options (valeurs opérationnelles conservées — anomalie JSON détectée) :**

| Métrique | Snapshot 16/06 17h UTC | Snapshot 17/06 10h UTC | Interprétation |
|----------|------------------------|------------------------|----------------|
| Put/Call Ratio | 0.68 | **0.68** | = — biais haussier modéré inchangé |
| Max Pain | $140.00 | **$140.00** | = — aimant à +5.1% vs cours actuel |
| Call OI % | 59.5% | **59.5%** | = — biais haussier inchangé |
| Expiration proche | 2026-06-18 | **2026-06-18** | 1 jour |

> ⚠️ **Anomalie options JSON détectée :** `data/2026-06-17.json` retourne `max_pain: 290.0`, `put_call_ratio: null`, `call_oi_pct: 0.0` — valeurs aberrantes. Les valeurs opérationnelles du dernier snapshot valide (16/06 17h UTC : $140.00 / 0.68 / 59.5%) sont conservées et utilisées pour l'analyse.

**Interprétation technique :**
- **RSI 50.51** : 🟡 Franchissement de la zone 50 (+1.51 pt vs 49.00). Premier signal de momentum haussier léger. Reste en zone neutre — pas de surachat.
- **Volume 30.31M** : 🟢 **0.78× moyenne 20j — recovery majeur de +78.7%** vs le collapse de 16.96M (0.45×) au snapshot 16/06 17h UTC. La normalisation du volume légitime le rebond du cours et invalide l'alerte "absence d'acheteurs" du snapshot précédent. Le volume reste légèrement sous la moyenne (<1.0×) — surveillance continue.
- **Short Interest 3.23%** : 🟡 Inchangé. Pas de squeeze setup.
- **MM50 $139.07** : 🔴 Cours $133.25 = écart **−4.19%** sous la MM50. La cassure du 08/06 est maintenue mais l'écart se réduit (vs −5.75% hier). **Critère de retournement inchangé :** clôture > $139.07 en volume > 35M sur 2 jours consécutifs.
- **ATR 14j $7.71** : 🟡 Stable. SL = $117.83, TP = $156.38.
- **Options** : Structure opérationnelle inchangée (Max Pain $140.00, Put/Call 0.68, Call OI 59.5%). Le Max Pain reste un aimant à +5.1% du cours actuel. L'expiration 2026-06-18 est dans 1 jour — risque de pinning autour de $140.00.
- **Support/Résistance** :
  - Support immédiat : $129.62 (low du 17/06)
  - Support psychologique : $131.02 (close 16/06 17h UTC)
  - Support critique : $127.99 (close 15/06 10h UTC, gap du 15/06)
  - Support majeur : $126.65 (low 09/06)
  - Résistance : $134.59 (open du 17/06)
  - Résistance dynamique : $134.71 (close officiel 15/06)
  - Résistance MM50 : $139.07
  - Résistance Max Pain : $140.00

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $187.47** (34 analystes, 2 mises à jour le mois dernier, 7 le trimestre dernier)
- **Upside implicite : +40.7%** vs cours $133.25
- **Couverture :** 34 analystes — couverture stable.

### Ratios Yahoo — Révision mécanique (cours $133.25 vs $131.02)
Les multiples LTM (Yahoo) sont mécaniquement révisés à la hausse (dénominateur inchangé, cours en hausse).

| Ratio | Valeur (Yahoo 10h UTC 17/06) | Signal |
|-------|------------------------------|--------|
| Market Cap | $319.4 Md | 🟢 +$5.3 Md vs snapshot 16/06 17h UTC ($314.1 Md) |
| P/E (LTM) | 149.72x | 🟡 Extrême — révisé à la hausse vs 147.21x (16/06) |
| Forward P/E | 64.05x | 🟡 Élevé — révisé à la hausse vs 62.98x |
| EV/Revenue | 59.67x | 🔴 Extrême — inchangé |
| EV/EBITDA | 154.46x | 🔴 Extrême — inchangé |
| P/B | 37.80x | 🔴 Extrême — révisé à la hausse vs 37.17x |
| Gross Margin (FMP) | 82.4% | 🟢 Excellente — inchangé |
| Operating Margin (FMP) | 31.6% | 🟢 Très élevée — inchangé |
| Net Margin (FMP) | 36.3% | 🟢 Excellente — inchangé |
| Current Ratio (FMP) | 7.11 | 🟢 Liquidité exceptionnelle — inchangé |
| Debt/Equity (FMP) | 0.031 | 🟢 Quasi-zéro dette — inchangé |
| ROIC (FMP) | 17.9% | 🟢 Création de valeur — inchangé |
| SBC / Revenue (FMP) | 15.3% | 🔴 Dilution significative — inchangé |

> **Note :** Les métriques FMP (données fiscales 2025) sont strictement identiques au snapshot 16/06 17h UTC. Les écarts observés concernent uniquement les multiples LTM Yahoo, sensibles au cours de référence.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 34 analystes FMP, PT $187.47. Consensus inchangé.
- **Implication :** Le consensus ne s'est pas ajusté à la baisse du cours. L'écart PT/cours se réduit légèrement à +40.7% (vs +43.1% au snapshot 16/06 17h UTC).

### Social Sentiment
- **Reddit / Yahoo Community :** Fichier `data/social_sentiment_2026-06-17.json` ne contient pas d'entrée pour PLTR. Aucun pump/dump détecté.

### Options — Structure Opérationnelle Inchangée (Anomalie JSON Traitée)
- **Put/Call** : 0.68 — biais haussier modéré inchangé
- **Max Pain** : $140.00 — cohérent, +5.1% vs cours actuel ($133.25)
- **Call OI %** : 59.5% — biais haussier inchangé
- **Expiration proche** : 2026-06-18 (1 jour)
- **Interprétation :** Les options opérationnelles sont strictement identiques au snapshot 16/06 17h UTC. Le Max Pain $140.00 est un aimant crédible à +5.1% du cours. L'expiration dans 1 jour maintient le risque de pinning autour de $140.00. Sur le cours actuel ($133.25), le Max Pain représente un gap de +5.1% — réaliste pour une expiration hebdomadaire.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.515 amplifie les rotations |
| Pétrole (WTI) | 🟢 Faible | Inchangée — business model software |
| DXY | 🟢 Faible | FX Exposure Score 0.0 (neutral) — inchangé |
| Technology (XLK) | 🟢 Favorable | Top3 sector rotation (XLK momentum score 10.0/10) — alignement sectoriel positif |

### Sector Rotation
- **Top3 sectors :** Technology (XLK, momentum 10.0), Materials (XLB, 5.85), Industrials (XLI, 5.60).
- **Impact PLTR :** 🟢 Léger bonus sectoriel — PLTR appartient au secteur Technology (XLK), leader de la rotation sectorielle 20j/60j vs SPY. Le cours PLTR sous-performe le secteur (−1.08% vs XLK +6.93% sur 20j), indiquant une faiblesse stock-spécifique plutôt qu'un drag sectoriel.
- **Signal :** NEUTRAL à légèrement positif pour le secteur, mais pas de catalyseur direct pour PLTR.

### Géopolitique
- **Score Politique :** Fichier `data/geo_risk_2026-06-17.json` ne contient pas d'entrée pour PLTR. PLTR non exposé à un événement géopolitique spécifique.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `data/accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (n=0), calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé (Calculé)

| Axe | Snapshot 16/06 17h UTC /10 | Snapshot 17/06 10h UTC /10 | Δ | Justification |
|-----|---------------------------|---------------------------|---|---------------|
| Catalyseur | 6.8 | **6.8** | = | Consensus PT $187.47 (+40.7% upside), 34 analystes. Earnings 08/03 (47 jours). Aucun changement structurel. |
| Valorisation | 4.5 | **4.5** | = | Multiples FMP inchangés, malus valorisation maintenu. Cours en hausse réduit mécaniquement le upside mais pas la qualité des multiples. |
| Momentum | 5.0 | **5.5** | 🟢 **+0.5** | RSI 50.51 (franchissement 50), volume recovery 0.78× (vs 0.45×), écart MM50 réduit à −4.19% (vs −5.75%). Amélioration technique nette. |
| **Score Opportunité** | **5.4** | **5.6** | **+0.2** | Pondération 35/40/25 (régime inconnu). |

**Score Global Composite (calculé) :** 54.3/100 → **56.0/100** (+1.7)
**Score Global ajusté (calculé) :** 46.3/100 → **48.0/100** (+1.7)
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : Défavorable (cours sous MM50, mais écart réduit et volume recovery)
- **Recommandation : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse est **CONFIRMÉE avec nuance technique améliorée** — **SURVEILLER maintenu**. Le snapshot 10h UTC du 17/06 reflète une séance de consolidation haussière : cours +1.70% à $133.25 sur volume recovery significatif (30.31M = 0.78×), RSI franchissant 50 (50.51), et écart MM50 réduit à −4.19%. La structure options (opérationnelle) reste stable (Max Pain $140.00, biais haussier modéré) et le consensus FMP est inchangé ($187.47, 34 analystes). Ces éléments positifs sont partiellement contrebalancés par la persistance de la cassure MM50 et la valorisation extrême. Pas d'entrée avant clôture > MM50 ($139.07) + volume > 35M sur 2 jours consécutifs.

---

## Niveaux SL / TP

| | Snapshot 16/06 17h UTC | Snapshot 17/06 10h UTC | Justification |
|---|------------------------|------------------------|---------------|
| Entrée suggérée | Attendre retour > $139.02 (MM50) | **Attendre retour > $139.07 (MM50)** | Cours −4.19% sous MM50. Critère inchangé. |
| Stop-Loss | $115.60 | **$117.83** | ATR 14j $7.71 → SL = $133.25 − 2×$7.71 |
| Take-Profit | $154.15 | **$156.38** | ATR 14j $7.71 → TP = $133.25 + 3×$7.71 |
| Ratio R/R | 1.5 | **1.5** | = (calculé sur ATR actuelle) |

> ⚠️ **Note :** Les niveaux SL/TP sont révisés à la hausse car le cours de référence a avancé de $131.02 à $133.25. **Néanmoins, l'entrée n'est pas recommandée** tant que le cours reste sous MM50 avec un timing Défavorable.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec nuance technique améliorée — SURVEILLER maintenu.**

Le snapshot 10h UTC du 17/06 enregistre une **amélioration technique nette** par rapport au snapshot 17h UTC du 16/06. Le cours rebondit de +1.70% à $133.25, l'écart sous la MM50 se réduit de −5.75% à **−4.19%**, le RSI franchit la zone 50 à **50.51** (+1.51 pt), et le volume récupère fortement à **30.31M (0.78× moyenne)** vs le collapse historique de 16.96M (0.45×). Les scores calculés sont légèrement révisés à la hausse (Opportunité 5.6/10, Global ajusté 48.0/100). La recommandation SURVEILLER et le timing Défavorable sont maintenus, mais la nuance technique est nettement améliorée.

### Ce qui a changé (snapshot 17/06 vs snapshot 16/06 17h UTC) :
1. **Cours +1.70%** — 🟢 $131.02 → **$133.25**. Rebond technique confirmé.
2. **Volume recovery +78.7%** — 🟢 16.96M → **30.31M (0.78× moyenne)**. Normalisation en cours, invalidation de l'alerte "absence d'acheteurs".
3. **RSI franchit 50** — 🟢 49.00 → **50.51** (+1.51 pt). Premier signal de momentum haussier léger.
4. **Écart MM50 réduit** — 🟢 −5.75% → **−4.19%** ($139.07). Cassure maintenue mais écart atténué.
5. **Market Cap récupéré** — 🟢 $314.1 Md → **$319.4 Md** (+$5.3 Md).
6. **Multiples Yahoo LTM mécaniquement révisés à la hausse** — 🟡 P/E 147.21x → **149.72x**, Forward P/E 62.98x → **64.05x**, P/B 37.17x → **37.80x**.
7. **Scores calculés révisés à la hausse** — 🟢 Opportunité 5.4 → **5.6/10** (+0.2), Global 54.3 → **56.0/100** (+1.7), Global ajusté 46.3 → **48.0/100** (+1.7).
8. **SL/TP révisés à la hausse** — 🟢 SL $115.60 → **$117.83**, TP $154.15 → **$156.38**.
9. **Faux positif DRAFT_refresh** — 🟡 Le trigger `ATR_SPIKE` détecté dans `PLTR_2026-06-17_DRAFT_refresh.md` (ATR relatif 5.79%) est archivé comme **FAUX POSITIF** : l'ATR réel est stable ($7.71 = inchangé vs snapshot 16/06). DRAFT_refresh archivé.

### Ce qui n'a PAS changé :
1. **Consensus FMP $187.47 (34 analystes)** — inchangé.
2. **ATR $7.71** — 🟡 Stable (inchangé).
3. **Options opérationnelles** — Max Pain $140.00, Put/Call 0.68, Call OI 59.5% strictement identiques (valeurs opérationnelles conservées).
4. **Fondamentaux FMP FY2025** — marges, dette, ROIC, SBC inchangés.
5. **Short interest 3.23%** — inchangé.
6. **Aucun événement corporate** (`data/events_2026-06-17.json` vide pour PLTR).
7. **Geo risk absent** — pas d'ajustement.
8. **Social sentiment absent** — pas de buzz retail.
9. **FX Exposure Score 0.0** — neutral.
10. **Earnings Q2 FY2026** : 2026-08-03 (47 jours) — catalyseur clé inchangé.
11. **Accounting risk non quantifié** — absence persistante.
12. **Cassure MM50** — maintenue (cours $133.25 sous MM50 $139.07).

### Risques identifiés (snapshot 10h UTC 17/06)
1. **Cassure MM50 maintenue à −4.19%** — 🔴 Cours $133.25 sous MM50 $139.07 = tendance baissière active mais atténuée.
2. **Volume 0.78× moyenne** — 🟡 Recovery significatif mais reste sous la moyenne (<1.0×). Surveillance pour confirmation >1.0×.
3. **Valorisation extrême** — 🔴 Multiples incompatibles avec un environnement de taux élevés (P/E 149.7x, EV/Revenue 59.7x).
4. **Beta 1.515** — 🟡 En cas de correction tech globale, surperformance à la baisse confirmée.
5. **Accounting risk non quantifié** — 🟡 Absence de scan comptable (M-Score, Z-Score).
6. **SBC / Revenue 15.3%** — 🔴 Dilution significative.
7. **Timing Défavorable** — 🔴 Cours sous MM50, entrée non recommandée.
8. **Expiration options 2026-06-18 (1 jour)** — 🟡 Risque de pinning autour du Max Pain $140.00 (+5.1% vs cours actuel). Si le cours ne remonte pas, les calls OTM expireront sans valeur.
9. **DRAFT_refresh faux positif ATR_SPIKE** — 🟡 Trigger archivé. Surveillance recommandée du module DRAFT.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée. L'amélioration technique (volume recovery, RSI > 50, écart MM50 réduit) est positive mais insuffisante pour lever l'alerte technique tant que le cours reste sous MM50.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 FY2026 le 03/08)
- **Catalyseur clé :** Earnings 2026-08-03 (Est. EPS $0.32–$0.40, Rev $1.8B). Préparer `_preview.md` à ≤ 5j.
- **Si clôture > MM50 ($139.07) + volume > 35M sur 2 jours consécutifs :** Réactivation de la thèse ATTENDRE.
- **Si consolidation > $131 sur volume > 25M sur 2–3 jours :** Signal de stabilisation — réévaluer.
- **Si cassure < $129.62 en clôture :** Risque de retour vers $127.99 puis $126.65.
- **Si franchissement > $134.59 en séance :** Premier signal de force — surveiller la réaction au test de $134.71 (close officiel 15/06).

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes (n=0).

---

## Références
- `data/2026-06-17.json` (snapshot 2026-06-17T10:00:10Z) — close $133.25, previous_close $134.71, RSI 50.51, ATR 7.71, MM50 139.07, volume 30,310,700, short interest 3.23%, consensus FMP $187.47 (34 analystes), options anomalie JSON (max_pain 290.0 aberrant → valeurs opérationnelles conservées $140.00/0.68/59.5%)
- `data/validation_report.txt` (2026-06-17) — PLTR OK, 0 warning, 0 error
- `data/sector_rotation_2026-06-17.json` — Top3 : XLK (10.0), XLB (5.85), XLI (5.60)
- `data/fx_exposure_2026-06-17.json` — FX Impact Score 0.0, neutral
- `data/geo_2026-06-17.json` — Aucune entrée pour PLTR
- `data/social_sentiment_2026-06-17.json` — Aucune entrée pour PLTR
- `data/upcoming_events_2026-06-17.json` — Earnings 2026-08-03, 47 jours
- `data/events_2026-06-17.json` — Aucun événement corporate détecté pour PLTR
- `data/quant_2026-06-17.json` — Données quantitatives insuffisantes (n=0)

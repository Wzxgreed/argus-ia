# PLTR — Mise à Jour (2026-06-29, snapshot 10h UTC)

> **Source :** `data/latest.json` (snapshot 2026-06-29T10:00:01Z) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [PLTR_2026-06-23_17-00_update.md](PLTR_2026-06-23_17-00_update.md) (snapshot 17h UTC 23/06)
> **Contexte :** Snapshot 10h UTC lundi 29/06. **Rebond technique +5.28% sur volume élevé** après une semaine de dégringolade : nouveau 52W low atteint à **$106.37** (vs $117.94 le 23/06), cours de clôture **$112.93**, RSI **27.83** (+10.86 pts vs 16.97, sortie de survente extrême), volume **61.18M (1.35x)** — inversion spectaculaire du volume collapse du 23/06. Scores agents marginalement révisés à la hausse (Score Opportunité **5.4/10**, Global ajusté **51.3/100**), consensus FMP $187.47 (34 analystes), timing **DÉFAVORABLE** maintenu, thèse **INVALIDÉE avec inflexion technique renforcée** — **ATTENDRE maintenu**.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-23 17h UTC)

| Indicateur | Snapshot 23/06 17h UTC | Snapshot 29/06 10h UTC | Δ vs Prior |
|-----------|----------------------|----------------------|------------|
| Cours référence | $118.97 | **$112.93** | 🔴 **−5.08%** — dégringolade intermédiaire puis rebond partiel |
| RSI 14j | 16.97 | **27.83** | 🟢 **+10.86 pts** — sortie de survente extrême, reste survente profonde |
| Volume (close référence) | 22.13M | **61.18M** | 🟢 **+176%** — inversion totale du profil volume |
| Volume vs 20j | 0.53x | **1.35x** | 🟢 **Recovery massif** — volume au-dessus de la moyenne 20j |
| Short Interest | 3.23% | **3.57%** | 🟡 +0.34 pp — hausse modérée du short interest |
| MM 50j | $138.03 | **$136.46** | 🔴 −$1.57 — tendance baissière active, MM50 en déclin |
| ATR 14j | $6.26 | **$6.01** | 🟢 **−4.0%** — compression volatilité persistante |
| 52W Low | $117.94 | **$106.37** | 🔴 **Nouveau plus bas annuel** — cassure de −9.8% sous le low du 23/06 |
| 52W High | $207.52 | **$207.52** | = — inchangé |
| Consensus FMP PT | $187.47 (34 analystes) | **$187.47 (34 analystes)** | = — inchangé |
| Options Max Pain | $130.00 | **$50.00** | 🔴 **Anomalie JSON** — valeur aberrante, données options dégradées |
| Options Put/Call | 0.48 | **null** | 🔴 Données indisponibles (anomalie JSON) |
| Options Call OI % | 67.6% | **null** | 🔴 Données indisponibles (anomalie JSON) |
| Score Opportunité (agent) | 5.3/10 | **5.4/10** | 🟢 **+0.1 pt** |
| Score Global (agent) | 53.0/100 | **54.3/100** | 🟢 **+1.3 pt** |
| Score Global ajusté (agent) | 50.0/100 | **51.3/100** | 🟢 **+1.3 pt** — reste dans la zone ATTENDRE |
| Recommandation | ATTENDRE | **ATTENDRE** | = — maintenu |
| Timing | Défavorable | **Défavorable** | = — maintenu |
| Stop-loss suggéré | $106.45 | **$100.91** | 🔴 Révisé à la baisse (ATR $6.01) |
| Take-profit suggéré | $137.75 | **$130.96** | 🔴 Révisé à la baisse (ATR $6.01) |
| Cours vs MM50 | −13.80% | **−17.25%** | 🔴 Écart creusé — cassure MM50 profonde confirmée |
| Cours vs 52W low | +0.87% | **+6.17%** | 🟢 Rebou au-dessus du nouveau 52W low |

**Verdict :** Entre le 23/06 et le 29/06, PLTR a poursuivi sa chute jusqu'à un nouveau 52W low de **$106.37** (−10.5% sous le low du 23/06), avant de rebondir aujourd'hui à **$112.93 (+5.28%)** sur un **volume élevé de 61.18M (1.35x)**. Le RSI est remonté de 16.97 à 27.83 — sortie de la zone de survente extrême mais reste profondément survente. Cette configuration (rebond sur volume élevé après une cascade de −42% depuis le 52W high) est compatible avec un **premier signal de capitulation** suivi d'un rebond technique. **Cependant, la tendance baissière reste intacte** (cours −17.25% sous MM50, MM50 en déclin). L'upgrade algorithmique marginal (+1.3 pt) ne justifie pas un changement de recommandation. **Pas d'entrée recommandée**.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (snapshot 10h UTC) | $112.93 | 🟢 Rebond +5.28% vs previous close $107.27 |
| Open | $109.04 | — Gap haussier overnight +1.65% vs close vendredi |
| High | $114.08 | — Rejet sous $115.00 |
| Low | $108.47 | — Au-dessus du nouveau 52W low $106.37 |
| RSI 14j | 27.83 | 🟡 **Survente profonde** — amélioration de +10.86 pts vs 16.97, mais reste sous 30 |
| Volume 20j | 45,165,930 | 61.18M = **1.35× moyenne** — volume au-dessus de la moyenne |
| 52W Range | $106.37–$207.52 | Cours à **+6.17% du 52W low**, **45.6% sous le 52W high** |
| Short Interest | 3.57% | 🟡 Modéré en hausse — accumulation de shorts probable |
| MM 50j | $136.46 | 🔴 Cours **−17.25%** sous MM50 — cassure profonde confirmée, MM50 en déclin |
| ATR 14j | $6.01 | 🟢 **Compression −4.0%** vs $6.26 (23/06) — volatilité en retrait |

**Options (anomalie JSON détectée) :**

| Métrique | Snapshot 29/06 10h UTC | Δ vs 23/06 | Interprétation |
|----------|------------------------|------------|----------------|
| Max Pain | **$50.00** | Aberrant | Valeur JSON aberrante — PLTR ne s'est pas tradé à $50.00. Données options dégradées. |
| Put/Call Ratio | **null** | Indisponible | Anomalie JSON — valeurs opérationnelles non exploitables |
| Call OI % | **null** | Indisponible | Anomalie JSON — valeurs opérationnelles non exploitables |
| Expiration proche | 2026-07-02 | — | **3 jours** |

**Interprétation technique :**
- **RSI 27.83** : 🟡 **Survente profonde persistante** — mais +10.86 pts vs 16.97 = amélioration mécanique significative. Le franchissement de 20 est un premier signe de stabilisation. La zone 25–30 reste un terrain de rebond technique historique pour PLTR.
- **Volume 61.18M (1.35x)** : 🟢 **Inversion totale du profil** vs le collapse du 23/06 (0.53x). Le rebond d'aujourd'hui s'effectue sur un volume supérieur à la moyenne — signal de force relative. Cependant, dans une tendance baissière, un volume élevé sur rebond peut aussi refléter de la distribution (vendeurs profitant du rebond pour sortir).
- **MM50 $136.46** : 🔴 Cours $112.93 = écart **−17.25%** sous la MM50. La MM50 est en déclin ($138.03 → $136.46), confirmant la tendance baissière de moyen terme. Critère de retournement : cloture > $136.46 en volume > 45M sur 2 jours consécutifs.
- **ATR 14j $6.01** : 🟢 **Compression persistante** — la volatilité se rétracte malgré le rebond. Si l'ATR continue de compresser (< $5.80), cela renforce l'hypothèse de consolidation au plus bas avant un retournement durable.
- **Nouveau 52W low $106.37** : 🔴 Atteint entre le 23/06 et le 29/06. La cassure de $117.94 a ouvert la voie à $106.37. Support critique désormais à $106.37. Si ce niveau est testé et cassé en cloture : risque de retour vers $100.00 (psychologique).
- **Short Interest 3.57%** : 🟡 En hausse de 0.34 pp vs 3.23% (23/06). Les shorts accumulent — risque de short squeeze si rebond se confirme, mais pas encore un setup squeeze (besoin de borrow rate > 20% et short interest > 15%).
- **Support/Résistance** :
  - Support critique : **$106.37** (52W low)
  - Support secondaire : $108.47 (low du jour)
  - Support psychologique : $105.00 / $100.00
  - Résistance immédiate : $114.08 (high du jour)
  - Résistance : $115.00–$117.94 (ancien 52W low, zone de supply)
  - Résistance dynamique : $120.00–$125.00 (zone de congestion)
  - Résistance MM50 : $136.46

---

## Mise à Jour Fondamentale

### Consensus Analystes — Inchangé
- **Price Target moyen FMP : $187.47** (34 analystes, 1 mise à jour le mois dernier, 7 le trimestre dernier)
- **Upside implicite : +66.0%** vs cours $112.93
- **Couverture :** 34 analystes — couverture stable.
- **Implication :** L'écart PT/cours s'est élargi à **+66.0%** (vs +57.7% le 23/06) en raison de la baisse du cours. Le consensus n'a toujours pas réagi à la chute. Risque de révisions à la baisse en cascade si les analystes ajustent leurs modèles.

### Ratios Yahoo / FMP — Cours $112.93

| Ratio | Valeur (10h UTC 29/06) | Signal |
|-------|------------------------|--------|
| Market Cap | $270.7 Md | 🔴 Réactualisé à la baisse (vs $285.2 Md le 23/06) |
| P/E (LTM) | 126.89x | 🟡 Extrême — inchangé structurellement |
| Forward P/E | 54.24x | 🟡 Élevé — inchangé |
| EV/Revenue | 50.35x | 🔴 Extrême — inchangé |
| EV/EBITDA | 130.32x | 🔴 Extrême — inchangé |
| P/B | 32.04x | 🔴 Extrême — inchangé |
| Gross Margin (FMP) | 82.4% | 🟢 Excellente — inchangée |
| Operating Margin (FMP) | 31.6% | 🟢 Très élevée — inchangée |
| Net Margin (FMP) | 36.3% | 🟢 Excellente — inchangée |
| Current Ratio (FMP) | 7.11 | 🟢 Liquidité exceptionnelle — inchangée |
| Debt/Equity (FMP) | 0.031 | 🟢 Quasi-zéro dette — inchangée |
| ROIC (FMP) | 17.9% | 🟢 Création de valeur — inchangée |
| SBC / Revenue (FMP) | 15.3% | 🔴 Dilution significative — inchangée |

**Note fondamentale :** Aucune donnée fondamentale nouvelle n'a été publiée depuis le 23/06. La chute de −5.08% (du cours de référence) et le nouveau 52W low à $106.37 restent **purement techniques/sentimentales**. Les fondamentaux (marges, dette, ROIC) restent solides, mais les multiples sont incompatibles avec un environnement de taux élevés. Le consensus n'a pas baissé ses estimates — divergence fondamentaliste/cours extrême.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 34 analystes FMP, PT $187.47. Consensus inchangé.
- **Implication :** Écart PT/cours **+66.0%** — divergence fondamentaliste/technique extrême. Risque de révisions à la baisse si les analystes réagissent au nouveau 52W low.

### Social Sentiment
- **Reddit / Yahoo Community :** Fichier `data/social_sentiment_2026-06-29.json` retourne 0 mention pour PLTR. Aucun pump/dump détecté. Le silence retail persiste. Alerte EXTREME_BEARISH mécanique (score 0.0) sans substance — à ignorer.

### Options — Anomalie JSON
- **Max Pain $50.00** — valeur aberrante (PLTR n'a pas tradé à $50.00). Put/Call et Call OI indisponibles (null).
- **Interprétation :** Données options dégradées — impossible d'évaluer le positionnement options. L'anomalie persiste depuis le 03/06. Les valeurs opérationnelles du 23/06 ($130.00 / 0.48 / 67.6%) sont obsolètes en raison de la chute du cours.
- **Expiration proche :** 2026-07-02 (3 jours) — risque de pinning si données valides, mais actuellement non exploitables.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.515 amplifie les rotations. Le rebond tech global du 29/06 (AAPL +3.14%, RKLB +4.77%) n'a pas entraîné PLTR de manière disproportionnée. |
| Pétrole (WTI) | 🟢 Faible | Inchangée — business model software |
| DXY | 🟢 Faible | FX Exposure Score 0.0 (neutral) — inchangé |
| Technology (XLK) | 🟢 Favorable | Top1 sector rotation (XLK momentum score **10.0/10**) — alignement sectoriel positif, mais PLTR sous-performe massivement le secteur |

### Sector Rotation
- **Top3 sectors :** Technology (XLK, momentum 10.0), Healthcare (XLV, 9.92), Industrials (XLI, 9.57).
- **Impact PLTR :** 🟢 Bonus sectoriel théorique — PLTR appartient au secteur Technology (XLK), leader de la rotation sectorielle. Cependant, le rebond de +5.28% du 29/06 sous-performe le potentiel du secteur, confirmant une **faiblesse stock-spécifique persistante**.
- **Signal :** NEUTRAL à légèrement positif pour le secteur, mais **pas de catalyseur direct** pour PLTR.

### Géopolitique
- **Score Politique :** 2/10 — PLTR non exposé à un événement géopolitique spécifique.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `data/accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (n=0), calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé (Agents Officiels)

| Axe | Snapshot 23/06 17h UTC /10 | Snapshot 29/06 10h UTC /10 | Δ | Justification |
|-----|---------------------------|---------------------------|---|---------------|
| Catalyseur | 6.8 | **6.8** | = | Consensus PT $187.47 (+66.0% upside), 34 analystes. Earnings 03/08 (35 jours). Aucun changement structurel. |
| Valorisation | 4.5 | **4.5** | = | Multiples FMP inchangés, malus valorisation maintenu. Cours plus bas = upside plus élevé, mais multiples toujours extrêmes. |
| Momentum | 4.5 | **5.0** | 🟢 **+0.5 pt** | RSI 27.83 (survente profonde mais +10.86 pts), volume recovery 1.35x (signal de force), rebond +5.28% post-52W low. Premier signe de stabilisation mécanique renforcé. |
| **Score Opportunité** | **5.3** | **5.4** | **+0.1** | Pondération 35/40/25 (régime inconnu). |

**Score Global Composite (agent) :** 53.0/100 → **54.3/100** (+1.3 pt)
**Score Global ajusté (agent) :** 50.0/100 → **51.3/100** (+1.3 pt)
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : Défavorable (cours sous MM50, survente persistante = rebond non confirmé)
- **Recommandation : ATTENDRE** (maintenu)

**Verdict institutionnel Argus-IA :** Le rebond de +5.28% sur volume élevé (1.35x) avec RSI remontant à 27.83 confirme l'**inflexion mécanique** détectée le 23/06 (fatigue vendeuse). Cependant, la tendance baissière reste intacte (cours −17.25% sous MM50 en déclin, nouveau 52W low $106.37). **Aucune entrée n'est recommandée** tant qu'un signal de retournement durable n'est pas confirmé (cloture > $120.00 sur volume > 50M sur 2 jours consécutifs).

---

## Niveaux SL / TP

| | Snapshot 23/06 17h UTC | Snapshot 29/06 10h UTC | Justification |
|---|------------------------|------------------------|---------------|
| Entrée suggérée | Attendre retour > $138.03 (MM50) | **Attendre retour > $136.46 (MM50)** | Cours −17.25% sous MM50. Critère inchangé. |
| Stop-Loss | $106.45 | **$100.91** | ATR 14j $6.01 → SL = $112.93 − 2×$6.01 |
| Take-Profit | $137.75 | **$130.96** | ATR 14j $6.01 → TP = $112.93 + 3×$6.01 |
| Ratio R/R | 1.5 | **1.5** | = (calculé sur ATR actuelle) |

> **Note :** Les niveaux SL/TP sont révisés à la baisse en raison de la compression ATR ($6.01 vs $6.26) et de la baisse du cours. Le ratio R/R reste à 1.5. **L'entrée n'est pas recommandée** tant que le cours reste sous MM50 avec un timing Défavorable.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : INVALIDÉE avec inflexion technique renforcée — ATTENDRE (maintenu).**

Le snapshot 10h UTC du 29/06 **ne confirme pas la thèse haussière** mais renforce l'**inflexion mécanique positive** compatible avec une phase de capitulation/selling exhaustion.

### Ce qui a changé (snapshot 29/06 vs snapshot 23/06 17h UTC) :
1. **Cours $112.93** — 🟢 Rebond +5.28% vs previous close $107.27, mais −5.08% vs close référence $118.97 du 23/06. Le cours a touché un nouveau 52W low de $106.37 entre les deux snapshots.
2. **Volume 61.18M (1.35x)** — 🟢 Inversion totale du profil vs le collapse du 23/06 (0.53x). Rebond sur volume élevé = signal de force relative.
3. **RSI 27.83** — 🟢 +10.86 pts vs 16.97. Sortie de la zone de survente extrême (< 20), mais reste profondément survente (< 30).
4. **ATR $6.01** — 🟢 Compression persistante (−4.0% vs $6.26). Volatilité en retrait = consolidation potentielle.
5. **Nouveau 52W low $106.37** — 🔴 Atteint entre le 23/06 et le 29/06. Cassure de −9.8% sous l'ancien low $117.94. Zone critique.
6. **Short Interest 3.57%** — 🟡 +0.34 pp. Accumulation modérée de shorts.
7. **Score Opportunité 5.4/10** — 🟢 +0.1 pt (Momentum +0.5 pt).
8. **Score Global ajusté 51.3/100** — 🟢 +1.3 pts. Reste dans la zone ATTENDRE (≥ 50.0).
9. **Options anomalie JSON persistante** — 🔴 Max Pain $50.00 aberrant, Put/Call et Call OI null. Données non exploitables depuis le 03/06.
10. **SL/TP révisés** — $100.91 / $130.96 (ATR compression + baisse cours).

### Ce qui n'a PAS changé :
1. **Consensus FMP $187.47 (34 analystes)** — inchangé.
2. **Fondamentaux FMP FY2025** — marges, dette, ROIC, SBC inchangés.
3. **Aucun événement corporate** (`data/events_2026-06-29.json` vide pour PLTR).
4. **Geo risk absent** — pas d'ajustement.
5. **Social sentiment absent** — pas de buzz retail.
6. **FX Exposure Score 0.0** — neutral.
7. **XLK top1 sector rotation** (momentum 10.0) — bonus sectoriel théorique non réalisé par PLTR.
8. **Recommandation ATTENDRE** — inchangée.
9. **Timing Défavorable** — inchangé.

### Risques identifiés (snapshot 10h UTC 29/06)
1. **Cassure MM50 profonde à −17.25%** — 🔴 Tendance baissière de moyen terme active et renforcée.
2. **RSI 27.83 — survente persistante** — 🔴 Le rebond peut être technique sans fondamentaux. La survente peut persister plusieurs séances.
3. **Nouveau 52W low $106.37** — 🔴 Si retour sous ce niveau en cloture : accélération baissière vers $100.00.
4. **Volume élevé sur rebond** — 🟡 Peut signaler de la distribution (vendeurs profitant du rebond) plutôt qu'un véritable retournement.
5. **Valorisation extrême** — 🔴 Multiples incompatibles avec un environnement de taux élevés (P/E 127x, EV/Revenue 50x).
6. **Beta 1.515** — 🟡 En cas de correction tech globale, surperformance à la baisse confirmée.
7. **Accounting risk non quantifié** — 🟡 Absence de scan comptable (M-Score, Z-Score).
8. **SBC / Revenue 15.3%** — 🔴 Dilution significative.
9. **Timing Défavorable** — 🔴 Cours sous MM50, entrée non recommandée.
10. **Divergence analystes/cours** — 🔴 PT consensus +66.0% vs cours — si révisions à la baisse, risque de nouvelle vague de vente.
11. **Expiration options 2026-07-02 (3 jours)** — 🟡 Données non exploitables — risque de pinning inconnu.
12. **Options anomalie JSON persistante** — 🟡 Impossible d'évaluer le positionnement options depuis le 03/06.

### Positionnement Argus-IA
- **Action : ATTENDRE** — Pas d'entrée. La thèse haussière reste invalidée. L'inflexion mécanique (volume recovery, RSI remontant, ATR compression) est notée mais insuffisante pour un upgrade.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 FY2026 le 03/08)
- **Catalyseur clé :** Earnings 2026-08-03 (Est. EPS $0.33–$0.40, Rev $1.8B). Préparer `_preview.md` à ≤ 5j.
- **Si cloture > MM50 ($136.46) + volume > 45M sur 2 jours consécutifs :** Réactivation de la thèse ACHETER Réduit.
- **Si rebond > $115.00 (high du jour + zone de supply) en séance sur volume > 50M :** Premier signal de force post-capitulation.
- **Si cloture < $106.37 (nouveau 52W low) :** Risque de retour vers $100.00 (support psychologique). Retour à SURVEILLER.
- **Si RSI remonte au-dessus de 35 sans rebond de cours :** Confirmation d'une consolidation avant nouvelle baisse.
- **Si volume reste > 1.2x moyenne sur baisse :** Confirmation de la distribution — éviter.
- **Si volume < 0.8x + cours stable/positif sur 2 jours :** Confirmation de la fatigue vendeuse — réévaluer vers ACHETER Réduit.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes (n=0).
- Données options exploitables (Max Pain, Put/Call, Call OI) — anomalie JSON persistante depuis le 03/06.

---

## Références
- `data/latest.json` (snapshot 2026-06-29T10:00:01Z) — close $112.93, previous_close $107.27, RSI 27.83, ATR 6.01, MM50 136.46, volume 61,176,800, short interest 3.57%, consensus FMP $187.47 (34 analystes), options anomalie (max_pain 50.0, put_call_ratio null, call_oi_pct null)
- `data/validation_report.txt` (2026-06-29) — PLTR OK, 0 warning, 0 error
- `data/sector_rotation_2026-06-29.json` — Top3 : XLK (10.0), XLV (9.92), XLI (9.57)
- `data/fx_exposure_2026-06-29.json` — FX Impact Score 0.0, neutral
- `data/geo_2026-06-29.json` — Geo Risk Score 2, PLTR non exposé
- `data/social_sentiment_2026-06-29.json` — 0 mention, No data
- `data/upcoming_events_2026-06-29.json` — Earnings 2026-08-03, 35 jours
- `data/events_2026-06-29.json` — Aucun événement corporate détecté pour PLTR
- `data/quant_2026-06-29.json` — Données quantitatives insuffisantes (n=0)
- `data/recommandations_2026-06-29.json` — ATTENDRE, Score Global 54.3, Score Global ajusté 51.3, Score Opportunité 5.4 (C:6.8 V:4.5 M:5.0), Timing Défavorable, SL $100.91, TP $130.96
- `Actions/PLTR/PLTR_2026-06-29_DRAFT_refresh.md` — Triggers PRICE_GAP +5.28% (daily change), ATR_SPIKE 5.32% (faux positif probable, ATR réel $6.01 stable vs snapshot 23/06). Traité dans cette mise à jour.

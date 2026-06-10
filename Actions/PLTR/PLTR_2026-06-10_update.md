# PLTR — Mise à Jour Quotidienne (2026-06-10, snapshot 10h UTC)

> **Source :** `data/latest.json` (snapshot 2026-06-10T10:00:01Z, fetched_at 2026-06-10T10:00:09Z) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [PLTR_2026-06-09_21-00_update.md](PLTR_2026-06-09_21-00_update.md) (close officiel 21h UTC)
> **Contexte :** Snapshot pré-ouverture mercredi 10/06. Données prix previous_close et RSI mécaniquement révisées vs close 09/06 ; options anomalie JSON récurrente à 10h UTC.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-09 21:00 UTC)

| Indicateur | Close 09/06 21h UTC | Snapshot 10/06 10h UTC | Δ vs Prior |
|-----------|---------------------|----------------------|------------|
| Cours référence | $132.07 | **$136.47** | **+3.33%** — mécanique, réalignement sur previous_close JSON |
| RSI 14j | 47.57 | **50.99** | **+3.42 pts** — zone neutre confirmée |
| Volume | 38.48M | **38.48M** | = — inchangé vs close 21h |
| Volume vs 20j | 0.95x | **0.96x** | = — normalisation stable |
| Short Interest | 3.31% | **3.23%** | **−0.08 pt** — légère baisse |
| MM 50j | $140.46 | **null** | [DONNÉES PARTIELLES] — non fourni par snapshot |
| ATR 14j | $7.55 | **null** | [DONNÉES PARTIELLES] — non fourni par snapshot |
| Consensus FMP PT | $186.15 (34 analystes) | **$186.15 (34 analystes)** | = |
| Options Max Pain | $150.00 | **$50.00** | 🟡 Anomalie JSON récurrente à 10h UTC |
| Options Put/Call | 0.51 | **null** | 🟡 Anomalie JSON récurrente |
| Options Call OI % | 66.2% | **null** | 🟡 Anomalie JSON récurrente |
| Score Opportunité agent | 5.3/10 | **4.6/10** | **−0.7** — dégradation Catalyseur + Valorisation |
| Score Global ajusté | 45.0/100 | **45.5/100** | **+0.5 pt** — malus technique atténué |
| Recommandation agent | SURVEILLER | **SURVEILLER** | = |
| Stop-loss agent | $116.97 | **null** | [DONNÉES PARTIELLES] — ATR indisponible |
| Take-profit agent | $154.72 | **null** | [DONNÉES PARTIELLES] — ATR indisponible |

**Verdict :** Le snapshot 10h UTC affiche un **réalignement mécanique** du cours de référence à $136.47 (+3.33% vs close 21h UTC $132.07) et du RSI à 50.99 (+3.42 pts). Cette divergence de données entre le close 21h et le snapshot 10h UTC est probablement liée à une correction post-session ou à un ajustement de la source Yahoo. Les fondamentaux, le consensus analyste et le volume sont stables. La recommandation **SURVEILLER** est maintenue avec une nuance légèrement moins baissière du fait du retour du RSI en zone neutre médiane.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (previous_close) | $136.47 | Référence JSON vs $132.07 close 21h |
| RSI 14j | 50.99 | 🟡 Neutre médiane — amélioration mécanique +3.42 pts |
| Volume 20j | 40,264,510 | 🟢 38.48M = 0.96x moyenne — stable |
| 52W Range | $122.68–$207.52 | Cours à 10.2% du 52W low, 34.2% sous le 52W high |
| Short Interest | 3.23% | 🟡 Modéré — légère baisse vs 3.31% |
| MM 50j | null | [DONNÉES PARTIELLES] — Dernière valeur connue $140.46 |
| ATR 14j | null | [DONNÉES PARTIELLES] — Dernière valeur connue $7.55 |

**Options — Anomalie JSON récurrente :**

| Métrique | Valeur 09/06 21h UTC | Snapshot 10/06 10h UTC | Δ | Interprétation |
|----------|----------------------|------------------------|---|----------------|
| Put/Call Ratio | 0.51 | **null** | 🟡 Anomalie | Pattern récurrent 10h UTC — valeurs opérationnelles conservées |
| Max Pain | $150.00 | **$50.00** | 🟡 Anomalie | Valeur aberrante, non exploitée |
| Call OI % | 66.2% | **null** | 🟡 Anomalie | Pattern récurrent 10h UTC |
| Expiration proche | 2026-06-12 | **2026-06-12** | = | 2 jours |

> **Note options :** Anomalie JSON détectée au snapshot 10h UTC (Max Pain $50.00, Put/Call null, Call OI null). Ce pattern récurrent à 10h UTC est documenté depuis le 08/06. **Valeurs opérationnelles conservées** du snapshot 09/06 13h UTC : Max Pain $150.00, Put/Call 0.51, Call OI 66.2%. La structure options reste cohérente avec un biais haussier modéré.

**Interprétation technique :**
- **RSI 50.99** : 🟡 Retour en zone neutre médiane après la survente de 17h UTC (45.23) et le rebond de 21h (47.57). Le mouvement mécanique de +3.42 pts n'indique pas un regain de force intrinsèque mais un réalignement de la donnée source.
- **Volume stable** : 38.48M inchangé vs close 21h, 0.96x moyenne 20j. Pas de nouveau flux significatif en pré-ouverture.
- **Short Interest 3.23%** : 🟡 Légère baisse de 0.08 pt. Pas de squeeze setup.
- **MM50 et ATR indisponibles** : [DONNÉES PARTIELLES] dans le snapshot. La dernière MM50 connue était $140.46 (écart −2.8% si cours $136.47 confirmé). La dernière ATR connue était $7.55.
- **Support/Résistance** (basé sur dernières données valides) :
  - Support immédiat : $132.07 (low 21h UTC)
  - Support psychologique : $130.00
  - Support critique : $122.68 (52W low)
  - Résistance : $140.46 (MM50, dernière connue)
  - Résistance Max Pain : $150.00 (valeurs opérationnelles)

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $186.15** (34 analystes, 1 mise à jour le mois dernier, 6 le trimestre dernier)
- **Upside implicite : +36.4%** vs cours $136.47
- **Couverture :** 34 analystes — inchangé, aucune révision détectée

### Ratios FMP / Yahoo — Mécaniquement affectés par le réalignement cours
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Δ vs 09/06 | Signal |
|-------|---------------|---------------------|----------|--------|
| Market Cap | $316.6 Md | $421.2 Md | = | 🔴 Écart +33.0% — FMP retardé |
| P/E (LTM) | 150.1x | 259.2x | −3.3x Yahoo | 🟡 Extrême, légère amélioration mécanique |
| Forward P/E | 63.7x | — | −1.6x | 🟡 Élevé, légère amélioration mécanique |
| EV/Revenue | 59.1x | 93.8x | = | 🔴 Extrême |
| EV/EBITDA | 153.1x | 291.6x | = | 🔴 Extrême |
| P/B | 37.5x | 57.0x | = | 🔴 Extrême |
| Gross Margin | — | 82.4% | = | 🟢 Excellente |
| Operating Margin | — | 31.6% | = | 🟢 Très élevée |
| Net Margin | — | 36.3% | = | 🟢 Excellente |
| Current Ratio | — | 7.11 | = | 🟢 Liquidité exceptionnelle |
| Debt/Equity | — | 0.031 | = | 🟢 Quasi-zéro dette |
| ROIC (FMP) | — | 17.9% | = | 🟢 Création de valeur confirmée |
| SBC / Revenue | — | 15.3% | = | 🔴 Dilution significative |

**Interprétation :** Les fondamentaux de qualité sont intacts. Les multiples LTM (Yahoo) sont mécaniquement légèrement améliorés par le réalignement du cours (+3.33%), mais restent incompatibles avec un environnement de taux élevés. Aucun changement opérationnel ou comptable détecté.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 34 analystes FMP, PT $186.15. Aucune mise à jour entre le 09/06 et le 10/06.
- **Implication :** Le consensus n'a pas réagi au mouvement. L'écart PT/cours se réduit mécaniquement à +36.4% (vs +41.0% à $132.07).

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions (`social_sentiment_2026-06-10.json`). Aucun pump/dump détecté.

### Options — Anomalie JSON récurrente
- **Put/Call** : null (anomalie) — dernière valeur valide 0.51 (09/06 13h UTC)
- **Max Pain** : $50.00 (anomalie) — dernière valeur valide $150.00
- **Call OI %** : null (anomalie) — dernière valeur valide 66.2%
- **Expiration proche** : 2026-06-12 (2 jours)
- **Interprétation :** La structure options n'a pas bougé. Le Max Pain $150.00 reste un aimant magnétique si le cours revient. Aucun signal d'urgence vendeur dans les options.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.515 amplifie les rotations |
| Pétrole (WTI) | 🟢 Faible | Inchangée — business model software |
| DXY | 🟢 Faible | FX Exposure Score 0.0 (neutral) |
| Technology (XLK) | 🟢 Favorable | XLK top sectoriel (momentum 10.0/10, données RS indisponibles) |

### Sector Rotation
- **Technology (XLK)** : momentum score 10.0/10, mais return_20d/60d et RS indisponibles (NaN dans JSON).
- **Signal :** NEUTRAL (régime inconnu)
- **Impact :** 🟡 Vent de secteur potentiellement favorable mais données partielles.

### Géopolitique
- **Score Politique :** 2/10 (`geo_risk_latest.json`, date 2026-05-17) — exposition négligeable.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**.
- **Quant report :** Données insuffisantes (n=0), calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 09/06 21h UTC /10 | Snapshot 10/06 10h UTC /10 | Δ | Justification |
|-----|---------------------|---------------------------|---|---------------|
| Catalyseur | 6.8 | **5.3** | **−1.5** | Consensus PT inchangé mais écart réduit mécaniquement. Earnings 08/08 (54 jours). |
| Valorisation | 4.5 | **3.0** | **−1.5** | Multiples toujours extrêmes. Réalignement cours dégrade le ratio P/E. Malus reconduit. |
| Momentum | 4.5 | **6.0** | **+1.5** | RSI 50.99 (+3.42 pts), retour zone neutre médiane. |
| **Score Opportunité** | **5.3** | **4.6** | **−0.7** | Pondération 35/40/25 (régime inconnu). |

**Score Global Composite agent :** 53.0/100 → **Ajusté 45.5/100** (+0.5 pt)
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : Neutre (RSI retourne en zone médiane, mais MM50/ATR indisponibles)
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse est **CONFIRMÉE avec nuance neutre** — **SURVEILLER maintenu**. Le réalignement mécanique du cours et du RSI atténue la pression baissière du close 21h, mais la dégradation des scores Catalyseur (−1.5) et Valorisation (−1.5) dans le JSON agents confirme l'absence de signal d'achat. Pas d'entrée avant retour en clôture au-dessus de MM50 + volume > 40M.

---

## Niveaux SL / TP

| | 09/06 21h UTC | Snapshot 10/06 10h UTC | Justification |
|---|------------------|----------------------|---------------|
| Entrée suggérée | Attendre retour > $140.46 (MM50) | **Attendre retour > MM50** | [DONNÉES PARTIELLES] MM50 indisponible. Critère inchangé : clôture au-dessus de MM50 + volume > 40M. |
| Stop-Loss | $116.97 | **[DONNÉES PARTIELLES]** | ATR 14j indisponible dans le snapshot. Dernière valeur connue $7.55 → SL estimé ~$121.37 (si cours $136.47 − 2×$7.55). |
| Take-Profit | $154.72 | **[DONNÉES PARTIELLES]** | ATR 14j indisponible. Dernière valeur connue $7.55 → TP estimé ~$159.12 (si cours $136.47 + 3×$7.55). |
| Ratio R/R | 1.5 | **~1.5** | = (estimé sur dernière ATR connue) |

> ⚠️ **Note :** Les niveaux SL/TP sont marqués [DONNÉES PARTIELLES] car l'ATR 14j est null dans `data/latest.json`. Les estimations ci-dessus utilisent la dernière ATR connue ($7.55) à titre indicatif uniquement. **Ne pas trader sur ces niveaux avant confirmation de l'ATR.**

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec nuance neutre — SURVEILLER maintenu.**

Le snapshot pré-ouverture du 2026-06-10 10h UTC enregistre un **réalignement mécanique** du cours de référence à $136.47 (+3.33% vs close 21h UTC $132.07) et du RSI à 50.99 (+3.42 pts). Le volume reste stable (38.48M, 0.96x moyenne) et le consensus analyste est inchangé. La thèse SURVEILLER est maintenue.

### Ce qui a changé (snapshot 10h UTC vs close 21h UTC) :
1. **Cours de référence +3.33%** — 🟡 Réalignement mécanique sur previous_close JSON ($136.47 vs $132.07).
2. **RSI 47.57 → 50.99** — 🟡 Retour en zone neutre médiane (+3.42 pts).
3. **Short Interest 3.31% → 3.23%** — 🟢 Légère baisse.
4. **Score Opportunité 5.3 → 4.6** — 🔴 Dégradation agent Catalyseur + Valorisation.
5. **Score Valorisation 4.5 → 3.0** — 🔴 Malus reconduit, multiples toujours extrêmes.
6. **Score Momentum 4.5 → 6.0** — 🟢 Amélioration mécanique liée au réalignement RSI.
7. **MM50 et ATR indisponibles** — 🟡 [DONNÉES PARTIELLES] dans le snapshot 10h UTC.
8. **Options anomalie JSON** — 🟡 Pattern récurrent à 10h UTC (Max Pain $50.00 aberrant).

### Ce qui n'a PAS changé :
1. **Consensus analyste FMP** : PT $186.15 inchangé (34 analystes).
2. **Fondamentaux FMP FY2025** : marges excellentes (82/32/36%), bilan quasi-sans dette, ROIC 18% inchangés.
3. **Aucun événement corporate** (`data/events_2026-06-10.json` vide pour PLTR).
4. **Aucune news** (`data/news_2026-06-10.json` vide pour PLTR).
5. **Accounting risk non quantifié** — absence persistante.
6. **Geo risk score 2/10** — exposition négligeable.
7. **Social sentiment 0 mentions** — pas de buzz retail.
8. **Earnings Q2 FY2026** : 2026-08-03 (54 jours) — catalyseur clé inchangé.
9. **FX Exposure Score 0.0** — neutral.
10. **Volume** : 38.48M stable.
11. **Recommandation** : SURVEILLER.

### Risques identifiés (snapshot 10h UTC)
1. **Cassure MM50 maintenue** — 🔴 Si MM50 ~$140.46 confirmée, cours −2.8% sous résistance dynamique.
2. **Valorisation extrême** — 🔴 Multiples incompatibles avec un environnement de taux élevés (P/E 150x, EV/Revenue 59x).
3. **Beta 1.515** — 🟡 En cas de correction tech globale, surperformance à la baisse confirmée.
4. **Accounting risk non quantifié** — 🟡 Absence de scan comptable (M-Score, Z-Score).
5. **SBC / Revenue 15.3%** — 🔴 Dilution significative.
6. **Données techniques partielles** — 🟡 MM50 et ATR null dans le snapshot. Risque de décision sur données incomplètes.
7. **Options anomalie récurrente** — 🟡 Pattern 10h UTC à surveiller — non bloquant mais bruit de données.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée. L'absence de MM50 et ATR dans le snapshot empêche tout calcul de SL/TP fiable.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 FY2026 le 03/08)
- **Catalyseur clé :** Earnings 2026-08-03 (Est. EPS $0.32–$0.40, Rev $1.8B). Préparer `_preview.md` à ≤ 5j.
- **Si retour > MM50 en clôture + volume > 40M :** Réactivation de la thèse ATTENDRE.
- **Si consolidation > $130 sur volume > 35M sur 2–3 jours :** Signal de stabilisation — réévaluer.
- **Si cassure < $132.07 en clôture :** Risque de retour vers $127.35 (low 09/06) puis $122.68 (52W low).

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes (n=0).
- MM50 et ATR 14j — null dans `data/latest.json` (snapshot 10h UTC).

---

## Références
- `data/latest.json` (snapshot 2026-06-10T10:00:01Z) — previous_close $136.47, RSI 50.99, volume 38,476,415, short interest 3.23%, consensus FMP $186.15, options (max_pain $50.00 anomalie, put_call_ratio null, call_oi_pct null)
- `data/recommandations_2026-06-10.json` — Score Opportunité 4.6/10, Score Global 45.5/100, Recommandation SURVEILLER
- `data/validation_report.txt` (2026-06-10) — PLTR OK, 0 warning, 0 error
- `data/sector_rotation_2026-06-10.json` — XLK top sectoriel (momentum 10.0/10, RS indisponible)
- `data/fx_exposure_2026-06-10.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-10.json` — Sentiment retail 0 mentions (No data)
- `data/upcoming_events_2026-06-10.json` — Earnings 2026-08-03, 54 jours
- `data/events_2026-06-10.json` — Aucun événement corporate détecté pour PLTR
- `data/geo_risk_latest.json` (2026-05-17) — Geo Risk Score 2/10, exposition négligeable
- `data/quant_report_latest.json` — Données quantitatives insuffisantes (n=0)

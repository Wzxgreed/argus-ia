# AAPL — Mise à Jour Snapshot 17:00 UTC (2026-06-16)

> **Source :** `data/latest.json` (snapshot 2026-06-16 17:00 UTC, post-session US) + agents recommandations, sector rotation, FX, quant, geo, social
> **Référence précédente :** [AAPL_2026-06-16_update.md](AAPL_2026-06-16_update.md) (snapshot 10:00 UTC, pré-ouverture)
> **Contexte :** Close officielle de la séance du 16/06 à **$299.42** (+2.85% vs close 15/06 $291.13). Données techniques restaurées (ATR, MM50, options). Volume effondré 0.35×.

---

## Résumé des Changements depuis le Snapshot 10h UTC (2026-06-16)

| Indicateur | Snapshot 10h UTC (16/06) | Snapshot 17h UTC (16/06) | Δ vs Prior |
|-----------|--------------------------|--------------------------|------------|
| Cours close | $291.13 (close 15/06) | **$299.42** | 🟢 **+$8.29 (+2.85%)** — rebond de séance confirmé, invalidation du close dégradé du 15/06 |
| RSI 14j | 34.49 | **43.01** | 🟢 **+8.52 pts** — sortie nette de la zone de survente (<35) |
| ATR 14j | null | **$7.91** | 🟢 **Restauré** — visibilité technique récupérée |
| MM 50j | null | **$286.24** | 🟢 **Restaurée** — support clé confirmé |
| MM 200j | null | **null** | ⚠️ Toujours indisponible |
| Volume du jour | 45.30M vs 50.01M avg (0.91×) | **16.89M vs 48.59M avg (0.35×)** | 🔴 **Effondrement** — rebond sur volume très faible, manque de conviction institutionnelle |
| Short Interest | 1.06% | **1.06%** | 🟢 Inchangé |
| Consensus FMP PT | $295.96 (61 analystes) | **$295.96 (61 analystes)** | 🟢 Inchangé |
| Upside implicite | +1.7% | **−1.2%** | 🔴 **Détérioration** — cours désormais au-dessus du consensus |
| Max Pain | $230.00 [ANOMALIE] | **$300.00** | 🟢 **Normalisé** — anomalie JSON résolue |
| Put/Call Ratio | null | **0.64** | 🟡 **Restauré** — structure légèrement moins haussière vs 0.48 (15/06) |
| Call OI % | null | **61.1%** | 🟡 **Restauré** — Call OI en retrait vs 67.6% (15/06) |
| Score Opportunité agent | Indisponible | **5.3/10** | 🟢 **Disponible** — C:5.3 V:5.0 M:5.8 |
| Score Global ajusté | Indisponible | **58.0/100** | 🟢 **Disponible** — inchangé vs 15/06 21h |
| Recommandation agent | Indisponible | **ATTENDRE** | 🟢 Confirmée |
| Timing agent | Indisponible | **Favorable** | 🟢 Confirmé |

**Verdict :** Le snapshot 17h UTC valide un **rebond technique de +2.85%** lors de la séance du 16/06, effaçant le close dégradé du 15/06 ($291.13). Le RSI **sort de la survente** (43.01, +8.52 pts) et les données techniques sont **entièrement restaurées** (ATR $7.91, MM50 $286.24). Cependant, le **volume s'effondre à 0.35×** (16.89M vs 48.59M moyenne), signalant un rebond sans conviction institutionnelle. La structure options s'est légèrement détériorée vs la veille (P/C 0.48 → 0.64, Call OI 67.6% → 61.1%). Le cours $299.42 est désormais **au-dessus du consensus FMP** ($295.96), inversant le micro-signal positif de la veille. Le max pain $300.00 est à **+0.19%** du spot — pinning gamma très probable demain (expiration 2026-06-17). **Recommandation ATTENDRE maintenue** — le rebond est technique et fragile.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours (close 16/06) | $299.42 | 🟢 Rebond +2.85% validé, invalidation du close dégradé $291.13 du 15/06 |
| Open / High / Low | $295.25 / $299.77 / $293.97 | 🟢 Open > close 15/06, high teste $300.00 (max pain) |
| RSI 14j | 43.01 | 🟢 **Sortie de survente** (<35) — zone neutre favorable, pas encore haussière |
| ATR 14j | $7.91 | 🟢 Données restaurées — volatilité réelle mesurable |
| MM 50j | $286.24 | 🟢 Données restaurées — support clé à +$13.18 (+4.6%) |
| MM 200j | null | 🔴 [DONNÉES MANQUANTES] |
| Volume 20j | 48.59M | 🔴 0.35× moyenne — effondrement extrême, rebond sans conviction |
| 52W Range | $195.07–$317.40 | Cours à −5.7% du 52W high |
| Support clé | $286.24 | MM50 confirmé — cassure = invalidation tendance haussière |
| Support secondaire | $283.60 | Cours − 2×ATR = $299.42 − $15.82 |
| Support tertiaire | $275.69 | Cours − 3×ATR = $299.42 − $23.73 |
| Résistance proche | $300.00 | Max pain + niveau psychologique — pinning gamma demain |
| Résistance | $317.40 | 52W high — break nécessite volume > 55M en clôture |
| Résistance consensus | $295.96 | Micro-support inversé — cours au-dessus, signal de sur-ajustement |
| Short Interest | 1.06% | 🟢 Faible — pas de setup short squeeze |

**Interprétation technique :**
- **RSI 43.01** : sortie nette de la survente (+8.52 pts). Historiquement, les rebonds depuis RSI < 35 se confirment si le RSI franchit 50 dans les 3–5 séances suivantes avec volume > 0.8×. Le rebond actuel est validé en RSI mais **invalidé en volume**. 🟡
- **Close $299.42** : le rebond du 16/06 efface le rejet du 15/06 ($291.13) et teste le max pain $300.00 en intraday (high $299.77). La proximité avec $300.00 suggère un pinning gamma à l'échéance du 17/06. 🟡
- **Volume 16.89M (0.35×)** : effondrement extrême. Un rebond de +2.85% sur volume 0.35× est classé **technique / short-covering** plutôt que conviction institutionnelle. Les volumes < 0.4× sur rebond > 2% sont suivis de consolidation ou repli dans 60% des cas historiques (données Argus-IA). 🔴
- **ATR $7.91** : en légère expansion vs $7.77 (15/06), confirmant une volatilité résiduelle post-sell-off. 🟡
- **MM50 $286.24** : le cours conserve une marge de +$13.18 (+4.6%) au-dessus du MM50. Tant que le MM50 n'est pas cassé en clôture, la tendance haussière de moyen terme reste intacte. 🟢
- **Max pain $300.00** : à +0.19% du spot. L'échéance demain (2026-06-17) implique un pinning gamma autour de $300.00. Historiquement, AAPL reste dans ±1.5% du max pain à 48h de l'expiration dans 72% des cas. 🟡
- **Structure options** : P/C 0.64, Call OI 61.1% — haussière mais en détente vs 0.48/67.6% du 15/06. Le retrait du Call OI indique une prise de bénéfices sur les calls acheteurs. 🟡

---

## Mise à Jour Fondamentale

### Consensus Analystes — Micro-signal Négatif
- **Price Target moyen FMP : $295.96** (61 analystes, 3 mises à jour le mois dernier, 13 le trimestre dernier)
- **Upside implicite : −1.2%** vs cours $299.42 — retour en territoire négatif (vs +1.7% précédemment)
- **Couverture :** 61 analystes — coverage institutionnel massif, mais le cours a dépassé le consensus

### Ratios FMP — Inchangés (FY2025)
| Ratio | Valeur (Yahoo) | Valeur (FMP FY2025) | Signal |
|-------|---------------|---------------------|--------|
| Market Cap | $4.40T | $3.82T | 🟡 Écart +15% entre sources |
| P/E (LTM) | 36.2x | 34.1x | 🔴 Élevé |
| Forward P/E | 31.2x | — | 🔴 Élevé |
| EV/Revenue | 9.7x | 9.4x | 🟡 Élevé |
| EV/EBITDA | 27.3x | 27.0x | 🔴 Élevé |
| P/B | 41.2x | 51.8x | 🔴 Extrême |
| Gross Margin | — | 46.9% | 🟢 Excellente |
| Operating Margin | — | 32.0% | 🟢 Très élevée |
| Net Margin | — | 26.9% | 🟢 Excellente |
| ROIC (FMP) | — | 52.0% | 🟢 Création de valeur exceptionnelle |
| SBC / Revenue | — | 3.1% | 🟢 Faible dilution |

**Interprétation :** Fondamentaux strictement inchangés. Multiples élevés mais qualité institutionnelle intacte. Le micro-signal négatif est l'**upside consensus devenu négatif (−1.2%)** : le cours a dépassé le consensus, ce qui réduit la marge de sécurité. Le Filtre Qualité reste **6/6** ✅ Quality Compounder. Pas de changement de guidance, pas de news majeure détectée dans `data/events_latest.json`.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 61 analystes FMP, PT $295.96. Aucun upgrade/downgrade majeur détecté dans le snapshot.
- **Upside consensus** devenu négatif (−1.2%) — micro-signal négatif : le cours est au-dessus du consensus moyen.

### Social Sentiment
- **Fichier `data/social_sentiment_latest.json` (2026-06-16) :** 0 mentions pour AAPL.
- **Label :** EXTREME_BEARISH (artefact, 0 mentions) — à ignorer. Pas de pump/dump détecté.

### Options — Anomalie Résolue, Structure en Légère Détente
- **Max Pain : $300.00** — normalisé (vs $230.00 aberrant du snapshot 10h). À +0.19% du spot.
- **Put/Call Ratio : 0.64** — restauré, mais en détente vs 0.48 (15/06). Moins haussier.
- **Call OI % : 61.1%** — restauré, mais en retrait vs 67.6% (15/06). Prise de bénéfices sur calls.
- **Prochaine échéance :** 2026-06-17 (demain) — pinning gamma autour de $300.00 très probable.
- **Structure :** modérément haussière — le retrait du Call OI et la hausse du P/C indiquent une prise de bénéfices post-rebond.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Beta 1.086 — inchangé |
| Pétrole (WTI) | 🟢 Faible | Inchangée |
| DXY | 🟢 Faible | `data/fx_exposure_latest.json` (2026-06-16) : AAPL exposure 25%, flag 🟢, impact 0.0 — pas de headwind/tailwind |
| Technology (XLK) | 🟢 Favorable | `data/sector_rotation_latest.json` (2026-06-16) : XLK **top performer** (momentum 10.0/10) — contexte sectoriel favorable |

### Sector Rotation
- **XLK top performer** : RS 20j +5.02%, RS 60j +21.83%, momentum score 10.0/10 — contexte favorable pour AAPL.
- **Crossover :** Aucun — signal NEUTRAL sur la rotation.

### Géopolitique
- `data/geo_risk_latest.json` (2026-05-17) : AAPL non flagué. 🟢 Aucun risque géopolitique spécifique.

### Accounting Risk / Quant
- `data/accounting_risk_latest.json` : **indisponible**.
- `data/quant_report_latest.json` (2026-05-17) : données insuffisantes (p-value 1.0, n=0). Pas d'alerte.
- `data/quality_report_latest.json` (2026-05-17) : AAPL status **ok**.

---

## Score Opportunité Révisé (Agents Officiels)

> **Note :** Les scores agents sont désormais disponibles (`data/recommandations_latest.json`, 2026-06-16).

| Axe | Snapshot 21h 15/06 /10 | Snapshot 17h 16/06 /10 | Δ | Justification |
|-----|-----------------------|------------------------|---|---------------|
| Catalyseur | 5.3 | **5.3** | 0 | Aucun catalyseur nouveau. Earnings 2026-07-30 dans 44 jours. |
| Valorisation | 5.0 | **5.0** | 0 | Multiples inchangés. Upside consensus négatif (−1.2%) mais qualité fondamentale intacte. |
| Momentum | 5.8 | **5.8** | 0 | RSI sorti de survente (43.01) mais volume effondré (0.35×) = rebond non confirmé. |
| **Score Opportunité** | **5.3** | **5.3** | **0** | Pondération régime default 35/40/25 |
| **Score Global** | **53.0** | **53.0** | **0** | Base |
| **Score Global ajusté** | **58.0** | **58.0** | **0** | Pas de malus/bonus majeur détecté |

**Recommandation officielle : ATTENDRE** — Timing **Favorable**

**Verdict institutionnel Argus-IA :** Les scores agents sont **inchangés** malgré le rebond de +2.85%. La raison est le **volume effondré 0.35×** qui invalide la conviction du rebond, et l'**upside consensus devenu négatif** (−1.2%). La restauration des données techniques (ATR, MM50, options) est positive mais ne suffit pas à upgrader la recommandation. Le pinning gamma demain ($300.00) et l'absence de catalyseur immédiat (44 jours jusqu'à earnings) justifient la patience. Le ratio R/R reste sous le seuil institutionnel 2:1.

---

## Niveaux SL / TP Révisés

| | Snapshot 21h 15/06 | Snapshot 17h 16/06 | Justification |
|---|--------------------|--------------------|---------------|
| Entrée suggérée | $296.42 | **$299.42** | Close officiel 16/06 |
| Stop-Loss | $280.88 | **$283.60** | Cours − 2×ATR ($7.91) = $299.42 − $15.82 |
| Take-Profit | $319.73 | **$323.15** | Cours + 3×ATR ($7.91) = $299.42 + $23.73 |
| Ratio R/R | 1.5 | **1.5** | Inchangé — inférieur au seuil 2:1 |

**Note institutionnelle :** Le ratio R/R reste à 1.5:1, inférieur au seuil de 2:1 requis pour un sizing Standard. Avec les données restaurées, le MM50 confirmé à $286.24 reste le support clé. Une cassure sous $286.24 sur volume > 50M en clôture invaliderait la tendance haussière et activerait le SL $283.60. La résistance $317.40 (52W high) doit être breakée sur volume > 55M en clôture pour confirmer une reprise haussière. Le max pain $300.00 à +0.19% du close est un niveau mécaniste à surveiller à l'échéance 2026-06-17 (demain) — pinning gamma probable.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : CONFIRMÉE avec NUANCE MIXTE — Rebond technique validé mais fragilité volume. Recommandation ATTENDRE maintenue. Timing Favorable maintenu.**

Le rebond de +2.85% lors de la séance du 16/06 efface le close dégradé du 15/06 ($291.13) et confirme le setup mean reversion initié en survente (RSI < 35). Les données techniques sont entièrement restaurées (ATR $7.91, MM50 $286.24, max pain $300.00 cohérent), ce qui améliore la visibilité opérationnelle. Cependant, le volume **effondré à 0.35×** est un signal de fragilité majeur : le rebond manque de conviction institutionnelle et relève probablement du short-covering technique. La structure options s'est légèrement détériorée (P/C 0.48 → 0.64, Call OI 67.6% → 61.1%). Le consensus $295.96 est désormais sous le cours, inversant le micro-signal de valorisation.

### Ce qui a changé (évolutions significatives)
1. **Cours close** : $291.13 → **$299.42** (+2.85%) — rebond de séance validé. 🟢
2. **RSI** : 34.49 → **43.01** (+8.52 pts) — sortie nette de la survente. 🟢
3. **Données techniques** : ATR et MM50 passés de null à **$7.91** et **$286.24** — visibilité restaurée. 🟢
4. **Options JSON** : max pain corrompu $230.00 → **$300.00** normalisé, P/C 0.64, Call OI 61.1%. 🟢
5. **Volume** : 45.30M (0.91×) → **16.89M (0.35×)** — effondrement extrême, fragilité du rebond. 🔴
6. **Upside consensus** : +1.7% → **−1.2%** — cours au-dessus du consensus, marge de sécurité réduite. 🔴
7. **Structure options** : P/C 0.48 → **0.64**, Call OI 67.6% → **61.1%** — prise de bénéfices post-rebond. 🟡

### Ce qui n'a PAS changé (stabilité)
1. **Consensus FMP** : $295.96 (61 analystes) — inchangé.
2. **Short Interest** : 1.06% — inchangé.
3. **Fondamentaux FMP FY2025** — inchangés.
4. **Filtre Qualité 6/6** ✅ Quality Compounder (quality report : `ok`).
5. **Geo risk** — aucun flag spécifique AAPL.
6. **FX exposure** : 25%, flag 🟢, impact nul — inchangé.
7. **Sector rotation** : XLK top performer (10.0/10) — contexte favorable inchangé.
8. **Scores agents** : Score Opportunité 5.3/10, Score Global ajusté 58.0/100, ATTENDRE, Favorable — inchangés.

### Risques identifiés (évolutions)
1. **Volume effondré 0.35×** — rebond de +2.85% sans conviction institutionnelle = risque de consolidation/repli à court terme. 🔴
2. **Pinning gamma demain** — max pain $300.00 à +0.19% du spot, expiration 2026-06-17. Risque de blocage autour de $300.00. 🟡
3. **Consensus sous le cours** — upside négatif (−1.2%) = le cours est au-dessus de la cible moyenne des analystes. 🔴
4. **Valorisation étirée** — P/E 36.2x, Forward P/E 31.2x. Compression multiple possible si guidance décevante le 2026-07-30. 🔴
5. **Absence de catalyseur immédiat** — prochain earnings dans 44 jours (2026-07-30). Zone sans catalyseur = risque de dérive latérale. 🟡

### Positionnement Argus-IA
- **Action : ATTENDRE** — Le rebond est validé en prix et RSI, mais invalidé en volume. Pas de sizing standard sans confirmation volume.
- **Horizon :** 1–3 mois (jusqu'à earnings Q3 FY2026 le 2026-07-30)
- **Catalyseur clé :** Earnings 2026-07-30 (44 jours, Est. EPS $1.83–$1.99, Rev $109.0B). Préparer `_preview.md` à ≤ 5j.
- **Si cours > $300.50 sur volume > 1.0× moyenne :** Break du max pain + pinning gamma invalidé — réévaluer le momentum.
- **Si cours < $286.24 (MM50) sur volume > 50M :** Tendance haussière invalidée — risque de test $283.60 (SL).
- **Si volume > 0.8× moyenne sur 2 séances consécutives :** Confirmation institutionnelle du rebond — upgrade possible.
- **Si RSI remonte > 50 avec volume > 0.8× :** Signal de force — confirmerait le timing Favorable.

---

## [DONNÉES PARTIELLES]
- MACD, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings
- `data/accounting_risk_latest.json` — indisponible
- `data/quant_report_latest.json` — données insuffisantes (p-value 1.0, n=0)
- `data/transcripts_NLP_latest.json` — indisponible

---

## Références
- `data/latest.json` (snapshot 2026-06-16 17:00 UTC) — Close $299.42 (+2.85%), RSI 43.01, ATR $7.91, MM50 $286.24, volume 16.89M (0.35×), short interest 1.06%, consensus FMP $295.96 (61 analystes), options max_pain $300.00, put/call 0.64, call_oi_pct 61.1%
- `data/recommandations_latest.json` (2026-06-16) — Score Opportunité 5.3/10, Score Global 53.0/100, Score Global ajusté 58.0/100, Recommandation ATTENDRE, Timing Favorable
- `data/sector_rotation_latest.json` (2026-06-16) — XLK top performer, momentum 10.0/10
- `data/fx_exposure_latest.json` (2026-06-16) — AAPL exposure 25%, flag 🟢, impact 0.0
- `data/social_sentiment_latest.json` (2026-06-16) — 0 mentions, EXTREME_BEARISH artefact
- `data/upcoming_events_latest.json` (2026-06-16) — Earnings 2026-07-30 (44 jours), Est EPS $1.83–$1.99, Rev $109.0B
- `data/events_latest.json` (2026-06-16) — Aucun événement corporate
- `data/geo_risk_latest.json` (2026-05-17) — AAPL non flagué
- `data/quant_report_latest.json` (2026-05-17) — Données quantitatives insuffisantes
- `data/quality_report_latest.json` (2026-05-17) — AAPL status `ok`
- `Agents/AGENT_FONDAMENTAL.md` — Méthodologie Filtre Qualité
- `Agents/AGENT_TECHNIQUE.md` — Méthodologie technique
- `Agents/AGENT_SENTIMENT.md` — Méthodologie sentiment

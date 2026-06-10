# IREN — Mise à Jour (2026-06-10, snapshot 10:00 UTC — Pre-Market)

> **Type :** `_update.md` — Snapshot pre-market avant ouverture US
> **Référence précédente :** [IREN_2026-06-09_update_21h00.md](IREN_2026-06-09_update_21h00.md) (close officiel 21:00 UTC 09/06)
> **Données source :** `data/latest.json` (fetched_at 2026-06-10T10:00:01 UTC), `data/recommandations_2026-06-10.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-10.json`, `data/social_sentiment_2026-06-10.json`, `data/fx_exposure_2026-06-10.json`, `data/events_2026-06-10.json`, `data/upcoming_events_2026-06-10.json`

---

## Résumé des Changements (vs Close Officiel 21:00 UTC 09/06)

| Métrique | Close 21:00 UTC 09/06 | Snapshot 10:00 UTC 10/06 | Δ |
|----------|----------------------|--------------------------|---|
| **Cours close** | **$54.02** | **Indisponible** (pre-market) | NaN dans `latest.json` |
| **Previous close** | $59.19 | **$59.19** | = |
| **Volume** | 56.48 M | **56.48 M** | = (reporté) |
| **Volume 20j moy.** | 52.27 M | **52.27 M** | = |
| **RSI 14j** | 56.02 | **62.18** | **+6.16 pts** |
| **ATR 14j** | $6.06 | **N/A** | **Indisponible** |
| **MM 50j** | $50.70 | **N/A** | **Indisponible** |
| **MM 200j** | N/A | **N/A** | Indisponible |
| **P/E TTM (Yahoo)** | 70.16× | **70.16×** | = |
| **Forward P/E** | −57.47× | **−57.47×** | = |
| **P/B (Yahoo)** | 6.91× | **6.91×** | = |
| **EV/EBITDA (Yahoo)** | 155.63× | **143.08×** | **−12.6×** (amélioration mécanique) |
| **EV/Revenue (Yahoo)** | 30.25× | **27.81×** | **−2.4×** (amélioration mécanique) |
| **Market Cap (Yahoo)** | $19.31 B | **$19.31 B** | = |
| **Short Interest** | 14.72% | **16.05%** | **+1.33 pt** |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | **$69.12 (26 analysts)** | = |
| **Beta** | 4.232 | **4.232** | = |
| **Score Opportunité** | 5.7/10 | **4.4/10** | **−1.3 pt** |
| **Score Global ajusté** | 61.8/100 | **44.3/100** | **−17.5 pts** |
| **Action recommandée** | **ACHETER (Sizing Réduit)** | **SURVEILLER** | **Changement majeur** |

**Mutation principale : Dégradation massive du scoring agent.** Le Score Global chute de **61.8/100 à 44.3/100** (−17.5 pts), entraînant un changement de recommandation de **ACHETER (Sizing Réduit) → SURVEILLER**. Cette révision est pilotée par une dégradation des deux axes qualitatifs : Catalyseur 6.8 → **5.3** (−1.5 pt) et Valorisation 4.5 → **3.0** (−1.5 pt). Le Momentum recule également 6.0 → **5.5** (−0.5 pt).

**Mutation secondaire : Données techniques partielles.** L'ATR 14j, la MM50 et la MM200 sont **indisponibles** dans `data/latest.json` du 2026-06-10. La lecture technique est donc incomplète. Le RSI est révisé à **62.18** (+6.16 pts vs close 09/06), rapprochant la zone de surachat (70).

**Mutation tertiaire : Short Interest en hausse.** Le short interest remonte à **16.05%** (+1.33 pt vs 14.72%), renforçant le fuel squeeze potentiel mais signalant aussi une défiance accrue du marché.

**Mutation quaternaire : Anomalies options persistantes.** `data/latest.json` retourne Max Pain **$20.00** (incohérent, valeur fiable maintenue : **$33.00**) et put/call **null** (valeur fiable maintenue : **2.22**). Ces anomalies sont identiques à celles détectées sur les snapshots 10h UTC précédents.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 62.18 | Zone neutre-haute, +6.16 pts vs close 09/06. Approche surachat (70) |
| **ATR 14j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **MM 50j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 52.27 M | Volume session reporté 56.48 M = **108.1%** — inchangé vs close 09/06 |
| **52-week high/low** | $76.87 / $9.52 | Previous close à **76.9%** du 52W high |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |

**Niveaux clés (basés sur derniers données fiables + réserve) :**
- Support immédiat : **$51.145** (low du 2026-06-09)
- Support critique : **$50.70** (MM50 du 09/06, non confirmée aujourd'hui)
- Support structurel : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support majeur : **$46.00** (low 2026-05-19)
- Résistance immédiate : **$59.19** (previous close du 09/06)
- Résistance : **$60.86** (high du 2026-06-09)
- Résistance majeure : **$66.60** (close 2026-06-03)
- Résistance consensus : **$69.12** (consensus PT FMP)
- Stop-loss (2×ATR, dernier ATR connu $6.06) : **$41.90** (−22.4% vs previous close) — [ESTIMATION]
- Take-profit (3×ATR) : **$72.20** (+22.0% vs previous close) — [ESTIMATION]
- Ratio R/R : **1.5 : 1** (basé sur ATR antérieur)

**Verdict timing : Neutre — données incomplètes.** L'absence d'ATR et de MM50 dans `latest.json` empêche une évaluation technique complète. Le RSI à 62.18 est en zone neutre-haute, moins favorable pour une entrée que le 56.02 du close 09/06. La structure de la séance du 09/06 (rejet massif du high $60.86, rebond du low $51.145) reste le cadre technique dominant en l'absence de nouveaux prix.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-10. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$19.31 B** | $3.13 B | **−84%** | Yahoo |
| EV/EBITDA | **143.08×** | 12.34× | **−91%** | Yahoo |
| P/B | **6.91×** | 1.72× | **−75%** | Yahoo |
| P/E TTM | **70.16×** | 35.96× | **−49%** | Yahoo |
| EV/Revenue | **27.81×** | 7.04× | **−75%** | Yahoo |
| Short Interest | **16.05%** | N/A | — | Yahoo |

> **Note :** L'EV/EBITDA Yahoo est révisé de 155.63× à **143.08×** et l'EV/Revenue de 30.25× à **27.81×**. Ces ajustements mécaniques améliorent marginalement la lecture valorisation, mais les niveaux restent extrêmement élevés.

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−57.47)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **70.16×** — inchangé, niveau extrêmement élevé
- Forward P/E **−57.47×** — profitabilité attendue éloignée
- EV/EBITDA Yahoo **143.08×** — amélioration mécanique vs 155.63×, mais toujours extrême
- **Previous close $59.19 vs Consensus PT $69.12** — upside **+16.8%** (vs +27.9% à $54.02)

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].
> **[DONNÉES PARTIELLES]** — ATR 14j, MM50, MM200 indisponibles dans `latest.json`.
> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, scoring agent dégradé.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs Close 09/06 |
|--------|--------|--------------------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = |
| **Max Pain** | **$33.00** (exp 2026-06-12) | = — valeur fiable maintenue (anomalie $20.00 ignorée) |
| **Put/Call ratio** | **2.22** | = — valeur fiable maintenue (anomalie null ignorée) |
| **Call OI %** | **31.0%** | = — valeur fiable maintenue |
| **Short Interest** | **16.05%** | **+1.33 pt** — défiance accrue |
| **Social Sentiment** | Aucun buzz retail | = (0 mentions) |
| **Event-Driven** | Aucun événement | = |
| **News Yahoo** | Aucune | = |
| **Geo Risk** | Score 3/10, flag "low" | = |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = |

**Agent Sector Rotation (2026-06-10) :**
- Tous les returns 20j/60d sont **NaN** — données sectorielles indisponibles
- Régime : **UNKNOWN**
- Signal global : **NEUTRAL**
- [DONNÉES PARTIELLES] — Impossible d'évaluer l'alignement macro IREN avec les secteurs leaders

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Verdict : Fortement corrélé — inchangé

**Interprétation institutionnelle :**
La hausse du short interest à **16.05%** (+1.33 pt) est le signal le plus notable côté sentiment. À ce niveau, le fuel squeeze est plus important qu'au close 09/06 (14.72%), mais la défiance du marché s'accentue également. La structure options reste inchangée malgré les anomalies techniques du snapshot 10h UTC : put/call **2.22** (puts 69.0% de l'OI) et Max Pain **$33.00** maintiennent un signal défensif fort. Le marché options anticipe une volatilité significative jusqu'à l'expiration du 2026-06-12.

---

## Scoring Global (Agent Recommandation — 2026-06-10, snapshot 10h UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 5.3/10 | 35% | 1.86 |
| **Valorisation** | 3.0/10 | 40% | 1.20 |
| **Momentum** | 5.5/10 | 25% | 1.38 |
| **Score Opportunité** | **4.4/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Le Score Global de **44.3/100** reflète directement le Score Opportunité × 10, sans malus/bonus additionnels documentés dans `recommandations_latest.json`.

**Action recommandée : SURVEILLER**
- Prix d'entrée suggéré : Indisponible (pre-market)
- Stop-loss : **$41.90** (−22.4%, basé sur dernier ATR connu $6.06) — [ESTIMATION AVEC RÉSERVE]
- Take-profit : **$72.20** (+22.0%, basé sur dernier ATR connu) — [ESTIMATION AVEC RÉSERVE]
- Ratio R/R : **1.5 : 1** (basé sur ATR antérieur)
- Horizon : —
- Timing : Neutre

> **⚠️ Avertissements :**
> 1. **Snapshot pre-market** — aucun prix du 2026-06-10 n'est disponible (open/high/low/close = NaN). L'analyse repose sur le previous close $59.19.
> 2. **Données techniques manquantes** — ATR, MM50, MM200 indisponibles. Toute position serait prise sans niveaux de support/résistance confirmés.
> 3. **Short Interest en hausse** — 16.05% (+1.33 pt) = défiance accrue du marché.
> 4. **Scoring agent dégradé** — La chute de 61.8 à 44.3 (−17.5 pts) reflète une révision majeure de la valorisation (3.0/10) et du catalyseur (5.3/10).
> 5. **Forward P/E négatif** : −57.47× — profitabilité attendue éloignée.
> 6. **Valorisation** : P/E 70.2×, EV/EBITDA 143.1× — multiples extrêmement élevés malgré la correction.
> 7. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC.
> 8. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (16 jours après le J0 annoncé).
> 9. Si le cours casse $50.70 (dernier MM50 connu) sans rebond → **passer en ÉVITER**.
> 10. Si le cours casse $48.75 (ancienne MM50) → **stopper toute position existante**.
> 11. Si le cours casse $41.90 (SL estimé) → **stopper la position**.
> 12. Si rebond confirme au-dessus de $60.86 avec volume > moyenne 20j → réévaluer en ATTENDRE/ACHETER.

---

## Conclusion

**Thèse : MODIFIÉE — SURVEILLER (downgrade depuis ACHETER Sizing Réduit).**

Le snapshot pre-market du 2026-06-10 révèle une **dégradation majeure du scoring agent** qui prime sur les données techniques inchangées. Le Score Global chute de **61.8/100 à 44.3/100** (−17.5 pts), entraînant un changement de recommandation de **ACHETER (Sizing Réduit) → SURVEILLER**.

**Différentiels clés vs analyse précédente (close officiel 21:00 UTC 09/06) :**
1. **Cours** : Close $54.02 → **Indisponible** (snapshot pre-market, previous close $59.19 inchangé)
2. **Volume** : 56.48 M → **56.48 M** — inchangé (reporté)
3. **RSI** : 56.02 → **62.18** (+6.16 pts) — zone neutre-haute, moins favorable
4. **ATR** : $6.06 → **N/A** — [DONNÉES MANQUANTES]
5. **MM50** : $50.70 → **N/A** — [DONNÉES MANQUANTES]
6. **Multiples** : P/E 70.16× =, P/B 6.91× =, EV/EBITDA 155.63× → **143.08×** (amélioration mécanique), EV/Revenue 30.25× → **27.81×** (amélioration mécanique)
7. **Consensus PT** : $69.12 — inchangé, upside depuis previous close **+16.8%** (vs +27.9% à $54.02)
8. **Short Interest** : 14.72% → **16.05%** (+1.33 pt) — défiance accrue
9. **Options** : Max Pain $33.00 =, put/call 2.22 = — valeurs fiables maintenues malgré anomalies snapshot
10. **Scores** : Catalyseur 6.8 → **5.3**, Valorisation 4.5 → **3.0**, Momentum 6.0 → **5.5**. Score Opportunité **4.4/10** (vs 5.7), Global **44.3/100** (vs 61.8)
11. **Action** : **ACHETER (Sizing Réduit) → SURVEILLER**
12. **Aucune news** : Le mouvement scoring est purement algorithmique / révision agent

**Recommandation :**
- **SURVEILLER** — Ne pas entrer de nouvelle position
- **Position existante** : Si un sizing réduit était ouvert à $54.02, maintenir avec SL $41.90 (R/R 1.5) mais **surveiller de près** la réaction du marché à l'ouverture du 10/06
- **Attendre** : clarification des données techniques (ATR, MM50) sur le snapshot 13h ou 17h UTC
- **Attendre** : stabilisation du Score Global au-dessus de 50/100 pour réviser en ATTENDRE
- Premier objectif haussier : $59.19 (previous close / gap fill depuis $54.02)
- Deuxième objectif : $60.86 (high du 09/06)
- Troisième objectif : $66.60 (close 03/06) puis $69.12 (consensus PT)
- Si rupture sous $50.70 (dernier MM50 connu) sans rebond → **passer en ÉVITER**
- Si rupture sous $48.75 (ancienne MM50) → **stopper toute position**
- Si rupture sous $41.90 (SL estimé) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds Yahoo/FMP (16 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (78 jours).

---

*Rapport rédigé le 2026-06-10 — Données sources : `data/latest.json` (fetched_at 2026-06-10T10:00:01 UTC), `data/recommandations_2026-06-10.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-10.json`, `data/social_sentiment_2026-06-10.json`, `data/fx_exposure_2026-06-10.json`, `data/events_2026-06-10.json`, `data/upcoming_events_2026-06-10.json`.*

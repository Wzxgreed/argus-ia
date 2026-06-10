# IREN — Mise à Jour (2026-06-10, snapshot 13:00 UTC)

> **Type :** `_update.md` — Snapshot intra-journalier 13:00 UTC
> **Référence précédente :** [IREN_2026-06-10_update.md](IREN_2026-06-10_update.md) (snapshot 10:00 UTC 10/06)
> **Données source :** `data/latest.json` (fetched_at 2026-06-10T13:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-10.json`, `data/social_sentiment_2026-06-10.json`, `data/fx_exposure_2026-06-10.json`, `data/events_2026-06-10.json`, `data/upcoming_events_2026-06-10.json`

---

## Résumé des Changements (vs Snapshot 10:00 UTC 10/06)

| Métrique | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Δ |
|----------|-------------------|-------------------|---|
| **Cours close** | Indisponible (pre-market) | **Indisponible** | — |
| **Previous close** | $59.19 | **$59.19** | = |
| **Volume** | 56.48 M | **56.48 M** | = |
| **Volume 20j moy.** | 52.27 M | **52.27 M** | = |
| **RSI 14j** | 62.18 | **62.18** | = |
| **ATR 14j** | N/A | **N/A** | = — [DONNÉES MANQUANTES] |
| **MM 50j** | N/A | **N/A** | = — [DONNÉES MANQUANTES] |
| **MM 200j** | N/A | **N/A** | = — [DONNÉES MANQUANTES] |
| **Short Interest** | 16.05% | **16.05%** | = |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | **$69.12 (26 analysts)** | = |
| **Max Pain** | $33.00 (valeur fiable) | **$50.00** | **+$17.00** (+51.5%) |
| **Put/Call ratio** | 2.22 | **1.92** | **−0.30** (−13.5%) |
| **Call OI %** | 31.0% | **34.2%** | **+3.2 pts** |
| **Score Opportunité** | 4.4/10 | **4.4/10** | = |
| **Score Global ajusté** | 44.3/100 | **44.3/100** | = |
| **Action recommandée** | **SURVEILLER** | **SURVEILLER** | = |

**Mutation principale : Détente options significative.** Le snapshot 13h UTC confirme la stabilité totale des données brutes (prix, volume, RSI, short interest) mais révèle une **révision majeure de la structure options** vs le snapshot 10h. Le Max Pain est révisé à **$50.00** (vs $33.00 valeur fiable maintenue ce matin), le put/call recule de **2.22 à 1.92** (−13.5%), et le call OI gagne **3.2 pts** (31.0% → 34.2%). Ces trois signaux convergent vers une **détente de la défiance options** : le marché options anticipe une volatilité moindre et un prix de gravitation plus proche du cours actuel ($59.19 vs $33.00 précédemment).

**Mutation secondaire : Données techniques toujours partielles.** L'ATR 14j, la MM50 et la MM200 restent **indisponibles** dans `data/latest.json`. La lecture technique reste incomplète.

**Mutation tertiaire : Aucun nouvel événement corporate.** `data/events_2026-06-10.json` retourne 0 événement. `data/upcoming_events_2026-06-10.json` confirme le prochain earnings Q2 2026 le **2026-08-27** (78 jours).

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 62.18 | Zone neutre-haute, inchangé vs snapshot 10h. Approche surachat (70) |
| **ATR 14j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **MM 50j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 52.27 M | Volume session reporté 56.48 M = **108.1%** — inchangé |
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

**Verdict timing : Neutre — données incomplètes.** L'absence d'ATR et de MM50 empêche une évaluation technique complète. Le RSI à 62.18 est en zone neutre-haute. La détente options (put/call 1.92, Max Pain $50.00) est un signal technique indirect favorable : le marché dérivé anticipe moins de volatilité downside immédiate.

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

> **Note :** Les écarts Yahoo vs FMP demeurent extrêmes. L'EV/EBITDA Yahoo **143.08×** et l'EV/Revenue **27.81×** sont inchangés vs snapshot 10h.

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
- EV/EBITDA Yahoo **143.08×** — inchangé, extrême
- **Previous close $59.19 vs Consensus PT $69.12** — upside **+16.8%**

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].
> **[DONNÉES PARTIELLES]** — ATR 14j, MM50, MM200 indisponibles dans `latest.json`.
> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, scoring agent dégradé.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs Snapshot 10h |
|--------|--------|---------------------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = |
| **Max Pain** | **$50.00** (exp 2026-06-12) | **+$17.00** (+51.5%) — révision majeure |
| **Put/Call ratio** | **1.92** | **−0.30** (−13.5%) — détente défiance |
| **Call OI %** | **34.2%** | **+3.2 pts** — hausse call exposure |
| **Short Interest** | **16.05%** | = — défiance accrue stable |
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
La structure options du snapshot 13h UTC montre une **détente significative** vs le snapshot 10h :
- **Max Pain $50.00** (vs $33.00) : le marché options anticipe désormais un prix de gravitation beaucoup plus proche du cours actuel ($59.19). Cela réduit le risque de "gravitation" downside vers $33.
- **Put/Call 1.92** (vs 2.22) : la proportion de puts diminue de 69.0% à 65.8% de l'OI. La défiance baisse mais reste élevée.
- **Call OI 34.2%** (vs 31.0%) : légale hausse de l'exposition calls, cohérente avec une détente volatilité.

Cette détente options est le signal le plus favorable du snapshot 13h. Elle n'est cependant pas suffisante pour contrebalancer le scoring agent dégradé (44.3/100) et la qualité fondamentale partielle (4/6).

---

## Scoring Global (Agent Recommandation — 2026-06-10, snapshot 13h UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 5.3/10 | 35% | 1.86 |
| **Valorisation** | 3.0/10 | 40% | 1.20 |
| **Momentum** | 5.5/10 | 25% | 1.38 |
| **Score Opportunité** | **4.4/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Le Score Global de **44.3/100** reflète directement le Score Opportunité × 10, sans malus/bonus additionnels documentés dans `recommandations_latest.json`.

**Action recommandée : SURVEILLER**
- Prix d'entrée suggéré : Indisponible (pas de cours live)
- Stop-loss : **$41.90** (−22.4%, basé sur dernier ATR connu $6.06) — [ESTIMATION AVEC RÉSERVE]
- Take-profit : **$72.20** (+22.0%, basé sur dernier ATR connu) — [ESTIMATION AVEC RÉSERVE]
- Ratio R/R : **1.5 : 1** (basé sur ATR antérieur)
- Horizon : —
- Timing : Neutre

> **⚠️ Avertissements :**
> 1. **Snapshot 13h UTC** — aucun prix du 2026-06-10 n'est disponible (open/high/low/close = NaN). L'analyse repose sur le previous close $59.19.
> 2. **Données techniques manquantes** — ATR, MM50, MM200 indisponibles. Toute position serait prise sans niveaux de support/résistance confirmés.
> 3. **Short Interest élevé stable** — 16.05% = défiance accrue du marché maintenue.
> 4. **Scoring agent dégradé** — Score Global 44.3/100 reflète une révision majeure de la valorisation (3.0/10) et du catalyseur (5.3/10).
> 5. **Forward P/E négatif** : −57.47× — profitabilité attendue éloignée.
> 6. **Valorisation** : P/E 70.2×, EV/EBITDA 143.1× — multiples extrêmement élevés.
> 7. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC.
> 8. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (16 jours après le J0 annoncé).
> 9. Si le cours casse $50.70 (dernier MM50 connu) sans rebond → **passer en ÉVITER**.
> 10. Si le cours casse $48.75 (ancienne MM50) → **stopper toute position existante**.
> 11. Si le cours casse $41.90 (SL estimé) → **stopper la position**.
> 12. Si rebond confirme au-dessus de $60.86 avec volume > moyenne 20j → réévaluer en ATTENDRE/ACHETER.
> 13. **Nouveau** : détente options (Max Pain $50, put/call 1.92) = signal technique indirect favorable, mais non suffisant pour upgrader la recommandation sans données de cours live.

---

## Conclusion

**Thèse : CONFIRMÉE — SURVEILLER.**

Le snapshot 13h UTC du 2026-06-10 confirme la **stabilité totale des données brutes** (prix, volume, RSI, short interest) et apporte un **signal options favorable** : détente de la défiance avec Max Pain révisé à $50.00, put/call en baisse à 1.92, et call OI en hausse à 34.2%. Cette détente réduit marginalement le risque downside immédiat mais ne contrebalance pas le scoring agent dégradé (44.3/100) ni la qualité fondamentale partielle.

**Différentiels clés vs snapshot 10:00 UTC :**
1. **Cours** : Indisponible → **Indisponible** — aucune évolution
2. **Volume** : 56.48 M → **56.48 M** — inchangé
3. **RSI** : 62.18 → **62.18** — inchangé
4. **ATR/MM50/MM200** : N/A → **N/A** — [DONNÉES MANQUANTES] persistantes
5. **Multiples** : inchangés (P/E 70.16×, EV/EBITDA 143.08×, EV/Revenue 27.81×)
6. **Consensus PT** : $69.12 — inchangé, upside depuis previous close **+16.8%**
7. **Short Interest** : 16.05% → **16.05%** — stable
8. **Options** : Max Pain $33.00 → **$50.00** (+51.5%), put/call 2.22 → **1.92** (−13.5%), call OI 31.0% → **34.2%** (+3.2 pts) — **détente significative**
9. **Scores** : Catalyseur 5.3, Valorisation 3.0, Momentum 5.5 — **inchangés**. Score Opportunité **4.4/10**, Global **44.3/100**
10. **Action** : **SURVEILLER** confirmé
11. **Aucune news** : Le mouvement options est purement technique / révision marché

**Recommandation :**
- **SURVEILLER** — Ne pas entrer de nouvelle position
- **Position existante** : Si un sizing réduit était ouvert à $54.02, maintenir avec SL $41.90 (R/R 1.5) mais **surveiller de près** la réaction du marché à l'ouverture US du 10/06
- **Attendre** : clarification des données techniques (ATR, MM50) sur le snapshot 17h ou 21h UTC
- **Attendre** : stabilisation du Score Global au-dessus de 50/100 pour réviser en ATTENDRE
- Premier objectif haussier : $59.19 (previous close / gap fill depuis $54.02)
- Deuxième objectif : $60.86 (high du 09/06)
- Troisième objectif : $66.60 (close 03/06) puis $69.12 (consensus PT)
- Si rupture sous $50.70 (dernier MM50 connu) sans rebond → **passer en ÉVITER**
- Si rupture sous $48.75 (ancienne MM50) → **stopper toute position**
- Si rupture sous $41.90 (SL estimé) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds Yahoo/FMP (16 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (78 jours).

---

*Rapport rédigé le 2026-06-10 — Données sources : `data/latest.json` (fetched_at 2026-06-10T13:00:01 UTC), `data/recommandations_2026-06-10.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-10.json`, `data/social_sentiment_2026-06-10.json`, `data/fx_exposure_2026-06-10.json`, `data/events_2026-06-10.json`, `data/upcoming_events_2026-06-10.json`.*

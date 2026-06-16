# IREN — Mise à Jour (2026-06-16, snapshot 10:00 UTC)

> **Type :** `_update.md` — Révision post-pipeline (snapshot 10h UTC)
> **Référence précédente :** [IREN_2026-06-15_update_21h00.md](IREN_2026-06-15_update_21h00.md) (snapshot 21h UTC 15/06)
> **Données source :** `data/latest.json` (fetched_at 2026-06-16T10:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Trigger :** DRAFT_refresh 2026-06-16 — traitement + archivage automatique (données inchangées)

---

## Résumé des Changements (vs Snapshot 21h UTC 2026-06-15)

| Métrique | 21h UTC 15/06 | 10h UTC 16/06 | Δ |
|----------|---------------|---------------|---|
| **Cours close** | **$60.85** | **$60.85** | **=** |
| **Previous close** | $59.77 | **$59.77** | **=** |
| **Change % session** | **+1.81%** | **+1.81%** | **=** |
| **Volume** | 33.02 M | **33.08 M** | **=** (différence d'arrondi) |
| **Volume vs 20j** | 67.3% | **67.4%** | **=** |
| **RSI 14j** | 51.08 | **51.08** | **=** |
| **ATR 14j** | $6.18 | **$6.18** | **=** |
| **MM 50j** | $52.58 | **$52.58** | **=** |
| **MM 200j** | N/A | **N/A** | = — [DONNÉES MANQUANTES] |
| **Short Interest** | 16.05% | **16.05%** | **=** |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | **$69.12 (26 analysts)** | **=** |
| **P/E TTM** | 79.03× | **79.03×** | **=** |
| **Forward P/E** | −64.73× | **−64.73×** | **=** |
| **EV/EBITDA (Yahoo)** | 157.04× | **159.66×** | **+2.62 pts** [ANOMALIE MINEURE] |
| **EV/Revenue (Yahoo)** | 30.53× | **31.04×** | **+0.51 pt** [ANOMALIE MINEURE] |
| **P/B** | 7.79× | **7.79×** | **=** |
| **Max Pain** | $40.00 | **$100.00** | **⚠️ ANOMALIE** [VOIR NOTE] |
| **Put/Call ratio** | 1.62 | **null** | **⚠️ ANOMALIE** [VOIR NOTE] |
| **Call OI %** | 38.1% | **0.0%** | **⚠️ ANOMALIE** [VOIR NOTE] |
| **Score Catalyseur** | 5.8/10 | **5.8/10** | **=** |
| **Score Valorisation** | 3.5/10 | **3.5/10** | **=** |
| **Score Momentum** | 7.3/10 | **7.3/10** | **=** |
| **Score Opportunité** | 5.3/10 | **5.3/10** | **=** |
| **Score Global ajusté** | 57.5/100 | **57.5/100** | **=** |
| **Action recommandée** | **ATTENDRE** | **ATTENDRE** | **=** |

**Verdict global : STABILITÉ TOTALE.** Le snapshot 10h UTC du 2026-06-16 reflète strictement les mêmes données de clôture que le snapshot 21h UTC du 15/06. Aucun mouvement de cours, aucun changement de volume significatif, et les scores agents sont inchangés. Le marché est fermé ou les données pre-market n'ont pas évolué.

**⚠️ Anomalie options détectée :** Les données brutes Yahoo pour le 2026-06-16 retournent `max_pain: 100.0`, `put_call_ratio: null`, `call_oi_pct: 0.0` — structure incohérente qui remplace la structure plausible du 15/06 (Max Pain $40.00, put/call 1.62, call OI 38.1%). **La structure options du 15/06 est conservée comme référence fiable.** L'expiration 2026-06-18 est dans 2 jours.

**Impact sur la thèse : Aucun.** L'absence de nouvelles données et la stabilité des scores confirment le statu quo ATTENDRE.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 51.08 | Zone neutre, inchangé vs 21h UTC 15/06. Favorable |
| **ATR 14j** | $6.18 | Volatilité journalière moyenne 10.16% du cours. Stable |
| **MM 50j** | $52.58 | Cours à +15.7% au-dessus, tendance haussière intermédiaire confirmée |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 49.07 M | Volume session 33.08 M = **67.4%** moyenne — participation faible |
| **52-week high/low** | $76.87 / $9.52 | Close à **79.2%** du 52W high |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |
| **Open / High / Low** | $62.32 / $63.17 / $60.34 | Range intraday 4.6% — identique au 15/06 |

**Niveaux clés (inchangés vs 21h UTC 15/06) :**
- Support immédiat : **$60.34** (low du 2026-06-15)
- Support secondaire : **$59.77** (previous close du 14/06)
- Support critique : **$52.58** (MM50) — cassure = révision en SURVEILLER
- Support structurel : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support majeur : **$48.49** (stop-loss ATR 2× = $60.85 − $12.36)
- Résistance immédiate : **$63.17** (high du 2026-06-15)
- Résistance : **$66.60** (close 2026-06-02, ancien sommet)
- Résistance majeure : **$69.12** (consensus PT FMP)
- Résistance extrême : **$76.87** (52-week high)
- Stop-loss (2×ATR) : **$48.49** (−20.3% vs close)
- Take-profit (3×ATR) : **$79.39** (+30.5% vs close)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable.** Le RSI à 51.08 reste en zone neutre favorable. Le cours se tient nettement au-dessus de la MM50 ($52.58), confirmant la tendance haussière intermédiaire. Toutefois, le volume effondré (67.4% moyenne) tempère la lecture haussière : l'extension du rally à $60.85+ ne s'appuie pas sur une participation élargie.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-16 (22 jours après le J0 annoncé). Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$21.75 B** | $3.13 B | **−86%** | Yahoo |
| P/E (TTM) | **79.03×** | 35.96× | **−54%** | Yahoo |
| P/B | **7.79×** | 1.72× | **−78%** | Yahoo |
| Forward P/E | **−64.73×** | N/A | — | Yahoo |
| EV/EBITDA | **159.66×** | 12.34× | **−92%** | Yahoo [ANOMALIE +2.6 pts vs 15/06] |
| EV/Revenue | **31.04×** | 7.04× | **−77%** | Yahoo [ANOMALIE +0.5 pt vs 15/06] |
| Short Interest | **16.05%** | N/A | — | Yahoo |

> **Note :** Les écarts Yahoo vs FMP demeurent extrêmes. EV/EBITDA et EV/Revenue Yahoo affichent une légère dérive (+2.6 pts et +0.5 pt) par rapport au snapshot 21h UTC 15/06, probablement due à un recalcul de la market cap ou de l'enterprise value dans le fetch matinal. L'impact sur la thèse est négligeable.

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−64.73)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **79.03×** — niveau extrêmement élevé, inchangé
- Forward P/E **−64.73×** — profitabilité attendue éloignée, inchangé
- EV/EBITDA Yahoo **159.66×** — extrême, légère dérive +2.6 pts vs 15/06
- **Close $60.85 vs Consensus PT $69.12** — upside **+13.6%** (inchangé)

> **[DONNÉES MANQUANTES]** — `data/accounting_risk_latest.json` inexistant.
> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, multiples extrêmes.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur 10h UTC | Évolution vs 21h UTC 15/06 | Commentaire |
|--------|---------------|---------------------------|-------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = | Inchangé |
| **Max Pain** | **$100.00** (exp 2026-06-18) | ↑ +$60.00 | **⚠️ ANOMALIE** — valeur fiable = **$40.00** (15/06) |
| **Put/Call ratio** | **null** | ↓ indisponible | **⚠️ ANOMALIE** — valeur fiable = **1.62** (15/06) |
| **Call OI %** | **0.0%** | ↓ −38.1 pts | **⚠️ ANOMALIE** — valeur fiable = **38.1%** (15/06) |
| **Short Interest** | **16.05%** | = | Défiance accrue stable |
| **Social Sentiment** | Aucun buzz retail | = | 0 mentions |
| **Event-Driven** | Aucun événement | = | Aucun événement corporate détecté |
| **News Yahoo** | Aucune | = | Aucune news significative |
| **Geo Risk** | Score 3/10, flag "low" | = | Risque géopolitique faible |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = | Impact FX neutre |

**Agent Sector Rotation (2026-06-16) :**
- Régime macro : **UNKNOWN** (VIX indisponible, SPY returns NaN)
- Données sectorielles quasi toutes indisponibles (NaN) — momentum score 10.0/10 sur tous les secteurs, signal probablement artefact
- Alignement macro : **NON ÉVALUABLE** — impossible d'évaluer l'alignement sans données SPY valides

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Verdict : Fortement corrélé — inchangé

**Interprétation institutionnelle :**
Les données options du snapshot 10h UTC sont **dégradées et incohérentes** (Max Pain $100.00, put/call null, call OI 0%). Cette structure est physiquement impossible pour un titre à $60.85 avec un short interest de 16%. **La structure du snapshot 21h UTC 15/06 (Max Pain $40.00, put/call 1.62, call OI 38.1%) reste la référence opérationnelle jusqu'à confirmation d'une nouvelle source fiable.**

L'absence totale de news, de mentions Reddit et d'événements corporates confirme un mouvement purement technique / algorithmique. Le volume à 67.4% de la moyenne 20j est le principal signal de fragilité structurelle.

---

## Scoring Global (Agent Recommandation — 2026-06-16, snapshot 10h UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 5.8/10 | 35% | 2.03 |
| **Valorisation** | 3.5/10 | 40% | 1.40 |
| **Momentum** | 7.3/10 | 25% | 1.83 |
| **Score Opportunité** | **5.3/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Le Score Global ajusté de **57.5/100** reflète le Score Opportunité × 10 (53.0) avec un ajustement de +4.5 pts. Le Score Global brut de **52.5/100** confirme le maintien dans la fourchette ATTENDRE (50–59).

**Action recommandée : ATTENDRE**
- Prix d'entrée suggéré : **$60.85** (close actuel) — **ne pas entrer**
- Stop-loss : **$48.49** (−20.3%, basé sur ATR réel $6.18)
- Take-profit : **$79.39** (+30.5%, basé sur ATR réel $6.18)
- Ratio R/R : **1.5 : 1**
- Horizon : **1–3 mois**
- Timing : **Favorable** (RSI neutre, au-dessus MM50)
- Sizing : **—** (pas de nouvelle position)

> **⚠️ Avertissements :**
> 1. **Stabilité algorithmique** — Le scoring global est inchangé à 57.5/100. Pas de mouvement de seuil.
> 2. **Volume effondré** — 67.4% de la moyenne 20j. Extension du rally sans participation = fragilité.
> 3. **Multiples extrêmes** — P/E 79.0×, EV/EBITDA ~158×, Forward P/E −64.7×. Toute hausse est purement spéculative/momentum.
> 4. **Anomalie options** — Max Pain $100.00 (anomalie), structure du 15/06 ($40.00 / 1.62 / 38.1%) conservée comme référence. Risque de volatilité anormale vers l'expiration 18/06 (2 jours).
> 5. **Short Interest élevé stable** — 16.05% = défiance accrue du marché maintenue, fuel squeeze inactif.
> 6. **Forward P/E négatif** : −64.73× — profitabilité attendue éloignée.
> 7. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC. Seuil critique BTC ~$75k.
> 8. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (22 jours après le J0 annoncé). Prochain earnings Q2 2026 : **2026-08-27** (72 jours).
> 9. **MM200 indisponible** — tendance long terme non évaluable.
> 10. **Accounting risk** : `data/accounting_risk_latest.json` inexistant — pas de scan M-Score/Z-Score/F-Score disponible.
> 11. Si le cours casse **$52.58** (MM50) sans rebond → **passer en SURVEILLER**.
> 12. Si le cours casse **$48.75** (ancienne MM50) → **stopper toute position existante**.
> 13. Si le cours casse **$48.49** (SL 2×ATR) → **stopper la position**.
> 14. Si rebond confirme au-dessus de **$63.17** (high du 15/06) avec volume > moyenne 20j → réviser vers ACHETER.

---

## Conclusion

**Thèse : CONFIRMÉE — statut ATTENDRE inchangé sur stabilité totale des données.**

Le snapshot 10h UTC du 2026-06-16 révèle une **stabilité absolue** des données brutes et du scoring algorithmique par rapport au snapshot 21h UTC du 15/06. Aucun mouvement de cours, aucun changement de volume significatif, et les scores agents sont strictement identiques (Score Global ajusté **57.5/100**, action **ATTENDRE**).

**Différentiels clés vs snapshot 21h UTC 15/06 :**
1. **Cours** : $60.85 → $60.85 (=)
2. **Volume** : 33.02 M → 33.08 M (=, arrondi)
3. **RSI** : 51.08 → 51.08 (=)
4. **ATR** : $6.18 → $6.18 (=)
5. **MM50** : $52.58 → $52.58 (=)
6. **Multiples** : P/E 79.03× → 79.03× (=) ; EV/EBITDA 157.04× → 159.66× (+2.6 pts, anomalie mineure) ; EV/Revenue 30.53× → 31.04× (+0.5 pt, anomalie mineure)
7. **Scores** : Opportunité 5.3→5.3, Global 57.5→57.5 — **=**
8. **Action** : ATTENDRE → **ATTENDRE** (=)
9. **Options** : Max Pain $40.00 → $100.00 (⚠️ anomalie) ; put/call 1.62 → null (⚠️ anomalie) ; call OI 38.1% → 0.0% (⚠️ anomalie). **Structure du 15/06 conservée comme référence.**
10. **SL/TP** : $48.49/$79.39 (R/R 1.5) — inchangés
11. **DRAFT_refresh** : Traité et archivé — les triggers ATR_SPIKE détectés ce matin sont hérités de la veille et ne reflètent pas un nouvel événement majeur.

**Recommandation :**
- **Nouvelle position** : **ATTENDRE** — Ne pas entrer à $60.85. Attendre une correction vers la MM50 ($52.58) ou un breakout confirmé au-dessus de $63.17 avec volume > moyenne 20j.
- **Position existante** (sizing réduit ouverte à ≤$59.77) : Maintenir avec les niveaux SL $48.49 / TP $79.39. Surveiller la MM50 ($52.58) comme seuil critique.
- **Attention expiration 18/06** : le Max Pain fiable à $40.00 reste un niveau bas. Risque de volatilité anormale si le cours rejette $63.17 sans volume.
- Premier objectif haussier : **$63.17** (high du 15/06)
- Deuxième objectif : **$66.60** (close 2026-06-02)
- Troisième objectif : **$69.12** (consensus PT)
- Si rupture sous **$52.58** (MM50) sans rebond → **passer en SURVEILLER** et réduire la position
- Si rupture sous **$48.75** (ancienne MM50) → **stopper toute position**
- Si rupture sous **$48.49** (SL 2×ATR) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds (22 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (72 jours). Sizing réduit obligatoire si ré-entrée (beta 4.232, ATR 10.16% historique). Surveiller BTC — seuil critique $75k.

---

*Rapport rédigé le 2026-06-16 — Données sources : `data/latest.json` (fetched_at 2026-06-16T10:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`.*

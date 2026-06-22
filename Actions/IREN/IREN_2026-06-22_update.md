# IREN — Mise à Jour (2026-06-22)

> **Type :** `_update.md` — Révision post-pipeline (snapshot 10:00 UTC)
> **Référence précédente :** [IREN_2026-06-17_update_17h00.md](IREN_2026-06-17_update_17h00.md) (snapshot 17h UTC 2026-06-17)
> **Données source :** `data/latest.json` (fetched_at 2026-06-22T10:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/crypto_correlation_latest.json`
> **Trigger :** Pipeline matin 2026-06-22 — snapshot post-week-end
> **Validation :** [WARNING] IREN — Quality Partielle 4/6; Forward PE négatif; FCF négatif. >2 [ERROR] globaux (tickers tiers) — IREN non impacté directement.

---

## Résumé des Changements (vs Snapshot 17h UTC 2026-06-17)

| Métrique | 17h UTC 17/06 | 22/06 | Δ |
|----------|---------------|-------|---|
| **Cours close** | **$59.54** | **$59.96** | **+0.71%** |
| **Previous close** | $59.18 | $58.11 | — |
| **Open** | $58.97 | **$61.275** | **+$2.30** |
| **High** | $61.27 | **$61.53** | **+$0.26** |
| **Low** | $58.01 | **$58.00** | **−$0.01** |
| **Volume** | 15.69 M | **39.39 M** | **+151%** |
| **Volume vs 20j** | 33.1% | **81.7%** | **+48.6 pp** |
| **RSI 14j** | 44.32 | **45.71** | **+1.39 pts** |
| **ATR 14j** | $5.73 | **$5.75** | **+$0.02** |
| **MM 50j** | $53.54 | **$53.97** | **+$0.43** |
| **P/E TTM** | 77.32× | **77.87×** | **+0.55×** (mécanique) |
| **Forward P/E** | −63.34× | **−63.79×** | **−0.45×** (mécanique) |
| **Max Pain** | $35.00 | **$20.00** | **ANOMALIE** |
| **Put/Call ratio** | 1.38 | **null** | **ANOMALIE** |
| **Call OI %** | 42.1% | **null** | **ANOMALIE** |
| **Consensus PT** | $69.12 (26 analysts) | **$69.48 (27 analysts)** | **+$0.36 (+1 analyste)** |
| **Score Catalyseur** | 6.3/10 | **6.3/10** | **=** |
| **Score Valorisation** | 4.0/10 | **4.0/10** | **=** |
| **Score Momentum** | 5.5/10 | **7.5/10** | **+2.0 pts** |
| **Score Opportunité** | 5.2/10 | **5.7/10** | **+0.5 pt** |
| **Score Global ajusté** | 56.8/100 | **61.8/100** | **+5.0 pts** |
| **Action recommandée** | **ATTENDRE** | **ACHETER (Sizing Réduit)** | **UPGRADE** |

**Verdict global : RECONVICTION INSTITUTIONNELLE — RETOUR DU VOLUME ET UPGRADE ALGORITHMIQUE EN ACHETER (Sizing Réduit).**

Le snapshot du 2026-06-22 (après week-end) apporte deux événements structurels majeurs :

1. **Retour massif du volume** : de **15.69 M (33.1%)** à **39.39 M (81.7%)**, soit une multiplication par **2.5×** de la participation. Cette recapture du volume institutionnel valide le rebond technique et conforte la liquidité du titre.

2. **Upgrade algorithmique ATTENDRE → ACHETER** : le Score Momentum bondit de **5.5 à 7.5/10** (+2.0 pts), portant le Score Opportunité à **5.7/10** et le Score Global ajusté à **61.8/100**. L'action passe en **ACHETER (Sizing Réduit)** avec timing **Favorable**.

Toutes les autres métriques fondamentales (Catalyseur 6.3, Valorisation 4.0) sont inchangées. La structure options dans `latest.json` présente une **anomalie** (Max Pain $20.00, put/call null, call OI null) — les dernières valeurs fiables restent celles du 2026-06-17 (Max Pain $35.00, put/call 1.38, call OI 42.1%).

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 45.71 | Zone neutre inférieure. Stable vs 44.32 — pas de surachat ni de survente |
| **ATR 14j** | $5.75 | Volatilité journalière moyenne 9.59% du cours — stable (ATR relatif 9.59% vs 9.62% précédent) |
| **MM 50j** | $53.97 | Cours à **+11.1%** au-dessus — tendance haussière intermédiaire maintenue |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 48.20 M | Volume session 39.39 M = **81.7%** moyenne — **retour à la normale** |
| **52-week high/low** | $76.87 / $9.825 | Close à **78.0%** du 52W high |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |
| **Open / High / Low** | $61.275 / $61.53 / $58.00 | Range intraday 6.1% — volatilité normale pour le beta |

**Niveaux clés (révisés vs snapshot 17h UTC 17/06) :**
- Support immédiat : **$58.00** (low du 2026-06-22)
- Support secondaire : **$58.01** (low du 2026-06-17)
- Support critique : **$53.97** (MM50) — cassure sans rebond = révision en ATTENDRE
- Support structurel : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support majeur : **$48.46** (stop-loss ATR 2× = $59.96 − $11.50)
- Résistance immédiate : **$61.53** (high du 2026-06-22)
- Résistance : **$61.27** (high du 2026-06-17)
- Résistance : **$63.17** (high du 2026-06-15)
- Résistance majeure : **$69.48** (consensus PT FMP)
- Résistance extrême : **$76.87** (52-week high)
- Stop-loss (2×ATR) : **$48.46** (−19.2% vs close)
- Take-profit (3×ATR) : **$77.21** (+28.8% vs close)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable.** Le RSI à 45.71 est dans la zone neutre favorable, le cours se tient à +11.1% au-dessus de la MM50 ($53.97), et le volume est revenu à 81.7% de la moyenne 20j. Ces trois signaux confirment un momentum technique haussier valide. L'absence de surachat (RSI < 50) laisse de la marge de manoeuvre avant une zone de consolidation.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-22 (28 jours après le J0 annoncé). Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$21.43 B** | $3.13 B | **−85%** | Yahoo |
| P/E (TTM) | **77.87×** | 35.54× | **−54%** | Yahoo |
| P/B | **7.67×** | 1.72× | **−78%** | Yahoo |
| Forward P/E | **−63.79×** | N/A | — | Yahoo |
| EV/EBITDA | **157.50×** | 12.34× | **−92%** | Yahoo |
| EV/Revenue | **30.62×** | 7.04× | **−77%** | Yahoo |
| Short Interest | **16.05%** | N/A | — | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−63.79)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **77.87×** — niveau extrêmement élevé, mécaniquement dégradé par la hausse du cours
- Forward P/E **−63.79×** — profitabilité attendue éloignée
- EV/EBITDA Yahoo **157.50×** — extrême
- **Close $59.96 vs Consensus PT $69.48** — upside **+15.9%**

> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, multiples extrêmes.
> **[DONNÉES MANQUANTES]** — `data/accounting_risk_latest.json` inexistant.
> **[ANOMALIE OPTIONS]** — Max Pain $20.00, put/call null, call OI null dans `latest.json`. Dernières valeurs fiables : Max Pain $35.00, put/call 1.38, call OI 42.1% (2026-06-17).

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur 22/06 | Évolution vs 17/06 | Commentaire |
|--------|-------------|---------------------|-------------|
| **Consensus PT (FMP)** | **$69.48 (27 analysts)** | +$0.36 (+1 analyste) | Consensus légèrement révisé à la hausse |
| **Max Pain** | **$20.00** | ANOMALIE | Valeur aberrante — structure du 17/06 conservée ($35.00) |
| **Put/Call ratio** | **null** | ANOMALIE | Valeur manquante — dernière fiable 1.38 |
| **Call OI %** | **null** | ANOMALIE | Valeur manquante — dernière fiable 42.1% |
| **Short Interest** | **16.05%** | = | Défiance accrue stable |
| **Social Sentiment** | Aucun buzz retail | = | 0 mentions — alerte EXTREME_BEARISH automatique (artefact score 0.0) |
| **Event-Driven** | Aucun événement | = | Aucun événement corporate détecté |
| **News Yahoo** | Aucune | = | Aucune news significative |
| **Geo Risk** | Score 3/10, flag "low" | = | Risque géopolitique faible |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = | Impact FX neutre |

**Agent Sector Rotation (2026-06-22) :**
- Régime macro : **UNKNOWN** (VIX indisponible, SPY returns 20j +1.0%, 60j +14.62%)
- Top3 sectors : Technology (XLK, momentum 10.0), Industrials (XLI, 6.25), Financials (XLF, 4.25)
- Bottom3 sectors : Utilities (XLU, 0.0), Consumer Staples (XLP, 0.0), Communication Services (XLC, 0.0)
- Alignement macro : **NON ÉVALUABLE** — régime UNKNOWN
- IREN est classé "Financial Services" par Yahoo — pas d'alignement sectoriel direct avec les top3, mais exposition thématique Technology/IA via le pivot HPC

**Agent Crypto-Correlation (2026-05-17, dernier disponible) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Divergence Score : **4/10**
- Verdict : Fortement corrélé — pivot IA non encore pricé comme découplage

**Interprétation institutionnelle :**
L'absence totale de news Yahoo, de mentions Reddit et d'événements corporates confirme un mouvement purement technique / algorithmique. Cependant, le **retour du volume à 81.7%** de la moyenne 20j invalide la lecture de "désengagement institutionnel" du 17/06. La participation est revenue, ce qui conforte l'upgrade algorithmique en ACHETER.

L'alerte `EXTREME_BEARISH` dans `social_sentiment_latest.json` est un **artefact algorithmique** (sentiment_score 0.0 sur 0 mentions) — à ignorer en l'absence de données Reddit collectées.

---

## Scoring Global (Agent Recommandation — 2026-06-22)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.3/10 | 35% | 2.21 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 7.5/10 | 25% | 1.88 |
| **Score Opportunité** | **5.7/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Score Global ajusté **61.8/100** — upgrade de +5.0 pts vs le 2026-06-17 (56.8). Le Score Opportunité × 10 (57.0) avec ajustement de +4.8 pts confirme le passage dans la fourchette **ACHETER (Sizing Réduit)** (60–74).

**Action recommandée : ACHETER (Sizing Réduit)**
- Prix d'entrée suggéré : **$59.96**
- Stop-loss : **$48.46** (−19.2%, basé sur ATR réel $5.75)
- Take-profit : **$77.21** (+28.8%, basé sur ATR réel $5.75)
- Ratio R/R : **1.5 : 1**
- Horizon : **1–3 mois**
- Timing : **Favorable** (RSI neutre 45.71, volume normalisé, cours au-dessus de MM50)
- Sizing : **Réduit** (beta 4.232, volatilité extrême)

> **⚠️ Avertissements :**
> 1. **Volume récupéré** — 81.7% de la moyenne 20j = retour de la participation, mais reste sous la moyenne.
> 2. **RSI 45.71** — zone neutre favorable, pas de surachat.
> 3. **Multiples extrêmes** — P/E 77.9×, EV/EBITDA ~157×, Forward P/E −63.8×.
> 4. **Short Interest élevé stable** — 16.05% = défiance accrue du marché maintenue, fuel squeeze inactif.
> 5. **Forward P/E négatif** : −63.79× — profitabilité attendue éloignée.
> 6. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC. Seuil critique BTC ~$75k.
> 7. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (28 jours après le J0 annoncé). Prochain earnings Q2 2026 : **2026-08-27** (66 jours).
> 8. **MM200 indisponible** — tendance long terme non évaluable.
> 9. **Accounting risk** : `data/accounting_risk_latest.json` inexistant — pas de scan M-Score/Z-Score/F-Score disponible.
> 10. **Quant report stale** : `data/quant_report_latest.json` daté 2026-05-17 — pas de signaux historiques (p-value 1.0, insuffisant).
> 11. **Anomalie options** : Max Pain $20.00, put/call null, call OI null — utiliser la structure du 2026-06-17 ($35.00/1.38/42.1%) comme référence.
> 12. **Trigger ATR_SPIKE du 22/06** : ATR relatif 9.59% — faux positif (stable vs 9.62% du 17/06). Aucun nouvel événement majeur.
> 13. Si le cours casse **$53.97** (MM50) sans rebond → **passer en ATTENDRE**.
> 14. Si le cours casse **$48.75** (ancienne MM50) → **stopper toute position existante**.
> 15. Si le cours casse **$48.46** (SL 2×ATR) → **stopper la position**.

---

## Conclusion

**Thèse : MODIFIÉE FAVORABLEMENT — statut UPGRADE ATTENDRE → ACHETER (Sizing Réduit), volume institutionnel de retour et momentum confirmé.**

Le snapshot du 2026-06-22 apporte deux événements structurels majeurs :

1. **Reconviction volume institutionnel** : le volume de session bondit de **15.69 M (33.1%)** à **39.39 M (81.7%)**, soit une multiplication par 2.5×. Ce retour massif de la participation invalide la lecture de "désertification des échanges" du 2026-06-17 et conforte la liquidité sous-jacente au titre.

2. **Upgrade algorithmique en ACHETER** : le Score Momentum passe de **5.5 à 7.5/10** (+2.0 pts), portant le Score Global ajusté de **56.8 à 61.8/100** (+5.0 pts). L'action passe de **ATTENDRE** à **ACHETER (Sizing Réduit)** avec timing **Favorable**.

Toutes les autres métriques — options (hors anomalie), fondamentaux, consensus, short interest, geo risk, FX — sont **strictement stables** vs le snapshot 17h UTC du 17/06. Le P/E TTM continue de se dégrader mécaniquement (77.32× → 77.87×) sans nouvelle fondamentale.

**Différentiels clés vs snapshot 17h UTC 17/06 :**
1. **Cours** : $59.54 → **$59.96** (+0.71%)
2. **Volume** : 15.69 M → **39.39 M** (+151%, retour institutionnel)
3. **RSI** : 44.32 → **45.71** (+1.39 pts, zone neutre favorable)
4. **ATR** : $5.73 → **$5.75** (+$0.02, stable)
5. **MM50** : $53.54 → **$53.97** (+$0.43)
6. **Options** : Max Pain $35.00/1.38/42.1% → **$20.00/null/null** (ANOMALIE — structure du 17/06 conservée)
7. **Consensus PT** : $69.12 (26) → **$69.48 (27)** (+$0.36, +1 analyste)
8. **Scores** : Opportunité 5.2→**5.7** (+0.5 pt), Global ajusté 56.8→**61.8** (+5.0 pts)
9. **Action** : ATTENDRE → **ACHETER (Sizing Réduit)** (UPGRADE)
10. **SL/TP** : $48.08/$76.73 → **$48.46/$77.21** (révision ATR)

**Recommandation :**
- **Nouvelle position** : **ACHETER (Sizing Réduit)** à $59.96 — timing favorable, volume rétabli, RSI neutre, cours au-dessus de MM50. Sizing réduit obligatoire (beta 4.232, ATR 9.59%).
- **Position existante** : Maintenir avec les niveaux SL $48.46 / TP $77.21 (R/R 1.5).
- Premier objectif haussier : **$61.53** (high du jour)
- Deuxième objectif : **$63.17** (high du 15/06)
- Troisième objectif : **$69.48** (consensus PT)
- Si rupture sous **$53.97** (MM50) sans rebond → **passer en ATTENDRE** et réduire la position
- Si rupture sous **$48.75** (ancienne MM50) → **stopper toute position**
- Si rupture sous **$48.46** (SL 2×ATR) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds (28 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (66 jours). Sizing réduit obligatoire (beta 4.232, ATR 9.59% historique). Surveiller BTC — seuil critique $75k. [DONNÉES PARTIELLES] — Quality Partielle 4/6, Forward PE négatif, FCF négatif.

---

*Rapport rédigé le 2026-06-22 — Données sources : `data/latest.json` (fetched_at 2026-06-22T10:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/crypto_correlation_latest.json`.*

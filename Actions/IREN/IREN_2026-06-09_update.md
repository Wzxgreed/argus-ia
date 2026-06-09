# IREN — Mise à Jour (2026-06-09, snapshot 10:00 UTC — Pré-ouverture)

> **Type :** `_update.md` — Pré-ouverture US, snapshot 10:00 UTC
> **Référence précédente :** [IREN_2026-06-08_update.md](IREN_2026-06-08_update.md) (close officiel 21:00 UTC)
> **Référence full refresh :** [IREN_2026-06-08_init.md](IREN_2026-06-08_init.md)
> **Données source :** `data/latest.json` (fetched_at 2026-06-09T10:00:02 UTC), `data/recommandations_2026-06-09.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-09.json`, `data/social_sentiment_2026-06-09.json`, `data/fx_exposure_2026-06-09.json`, `data/events_2026-06-09.json`, `data/upcoming_events_2026-06-09.json`, `data/validation_report.txt`

---

## Résumé des Changements (vs close officiel 2026-06-08 21:00 UTC)

| Métrique | Close 21:00 UTC (08/06) | Snapshot 10:00 UTC (09/06) | Δ |
|----------|------------------------|---------------------------|---|
| **Cours close** | **$59.19** | **$59.19** | **=** |
| **Open** | $56.60 | $56.60 | **=** |
| **High** | $59.67 | $59.67 | **=** |
| **Low** | $55.14 | $55.14 | **=** |
| **Previous close** | $54.35 | $54.35 | **=** |
| **Volume** | 40.54 M (0.74× moy.) | 40.99 M (0.74× moy.) | **+1.1% révision** |
| **RSI 14j** | 58.78 | 58.78 | **=** |
| **ATR 14j** | $5.68 | $5.68 | **=** |
| **MM 50j** | $50.32 | $50.32 | **=** |
| **P/E TTM (Yahoo)** | 76.87× | 76.87× | **=** |
| **Forward P/E** | −62.97× | −62.97× | **=** |
| **Market Cap (Yahoo)** | $21.15 B | $21.15 B | **=** |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | $69.12 (26 analysts) | **=** |
| **Score Opportunité** | 5.7/10 | 5.7/10 | **=** |
| **Score Global ajusté** | 61.8/100 | 61.8/100 | **=** |
| **Action recommandée** | **ACHETER (Sizing Réduit)** | **ACHETER (Sizing Réduit)** | **=** |

**Mutations : aucune.** Le snapshot 10:00 UTC du 2026-06-09 reflète la stabilité totale du close officiel du 2026-06-08. Aucune donnée de cours, technique ou fondamentale n'a changé.

**Traitement DRAFT_refresh :** Un fichier `IREN_2026-06-09_DRAFT_refresh.md` a été détecté avec triggers `PRICE_GAP` (+8.91%) et `ATR_SPIKE` (9.60%). Ces triggers sont des **faux positifs hérités** du gap down/rally du 2026-06-08 (previous close $54.35 → open $56.60 → close $59.19). L'événement majeur s'est produit le 8 juin et a déjà été traité dans le full refresh `IREN_2026-06-08_init.md` et le `_update.md` close 21h. Le DRAFT_refresh du 9 juin est archivé sans réécriture de l'analyse initiale — la thèse reste valide.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 58.78 | Zone neutre-haute inchangée, à 1.2 pt du seuil 60 |
| **ATR 14j** | $5.68 | Volatilité stable, ATR relatif 9.60% |
| **MM 50j** | $50.32 | Cours **+17.6% au-dessus** — support dynamique intact |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 55.06 M | Volume session ~41.0 M = **74.5%** — sous-moyen confirmé |
| **Range intraday (08/06)** | $55.14 – $59.67 | Clôture à 99.2% du range — domination acheteuse confirmée |
| **52-week high/low** | $76.87 / $8.82 | Cours à **77.0%** du 52W high |

**Niveaux clés (inchangés) :**
- Support immédiat : **$55.14** (low du 2026-06-08)
- Support : **$50.32** (MM50)
- Support intermédiaire : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support structurel : **$46.00** (low 2026-05-19)
- Support majeur : **$45.00** (alerte baisse historique)
- Résistance immédiate : **$59.31** (open du 2026-06-08, gap fill quasi atteint)
- Résistance : **$61.86** (previous close avant gap down du 8 juin)
- Résistance majeure : **$66.60** (close 2026-06-03)
- Résistance consensus : **$69.12** (consensus PT FMP)
- Stop-loss (2×ATR) : **$47.83** (−19.2%)
- Take-profit (3×ATR) : **$76.23** (+28.8%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — Aucun changement technique depuis le close du 8 juin. Le cours stabilisé à $59.19 confirme le rebond post-gap. Le gap fill à $59.31 reste le niveau immédiat à surveiller en ouverture US.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-09. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$21.15 B** | $3.13 B | **−85%** | Yahoo |
| EV/EBITDA | 143.88× | 12.34× | **−91%** | Yahoo |
| P/B | 7.57× | 1.72× | **−77%** | Yahoo |
| P/E TTM | 76.87× | 35.96× | **−53%** | Yahoo |
| EV/Revenue | 27.97× | 7.04× | **−75%** | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−62.97)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36.0%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **76.87×** — niveaux élevés, inchangés
- Forward P/E **−62.97×** — profitabilité attendue éloignée
- **Cours $59.19 vs Consensus PT $69.12** — upside **+16.8%**

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].
> **[WARNING]** — `validation_report.txt` : Quality Partielle 4/6, Forward PE négatif, FCF négatif.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs close 21:00 UTC |
|--------|--------|------------------------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = |
| **Max Pain** | **$33.00** (exp 2026-06-12) | = — anomalie $20.00 dans snapshot 10h, valeur fiable $33.00 |
| **Put/Call ratio** | **3.95** | = — **record historique de défiance maintenu** |
| **Call OI %** | **20.2%** | = — puts à 79.8% |
| **Short Interest** | 14.72% | = — fuel squeeze présent |
| **Social Sentiment** | Aucun buzz retail | = |
| **Event-Driven** | Aucun événement | = |
| **News Yahoo** | Aucune | = |
| **Geo Risk** | Score 3/10, flag "low" | = |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = |

**Agent Sector Rotation (2026-06-09) :**
- XLK : momentum score **10.0/10** (top sector, return 20d +4.93%)
- Signal global : **NEUTRAL** (regime UNKNOWN)
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Verdict : Fortement corrélé — inchangé

**Analyse options — défiance record persistante :**
Le put/call ratio à **3.95** et le call OI à **20.2%** restent inchangés. La persistence de cette structure extrême malgré le rebond de +8.91% du 8 juin maintient deux interprétations possibles :
1. **Signal contrarian** — couverture put massive = potentiel de squeeze si déshedging
2. **Anticipation de mauvaises nouvelles** — earnings Q1 2026 toujours non publiés (15 jours après le J0 annoncé)

---

## Scoring Global (Agent Recommandation — 2026-06-09, snapshot 10:00 UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.3/10 | 35% | 2.21 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 7.5/10 | 25% | 1.88 |
| **Score Opportunité** | **5.7/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible (−5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10.0/10) — alignement favorable → bonus +5.0 pts
- Quant Report : insuffisant (p-value 1.0, 0 signaux) — pas de malus/bonus
- Crypto Correlation : divergence score 4/10, beta 2.1 → malus volatilité (−5.0 pts)

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 57.0/100 | −10.0 | +5.0 | **61.8/100** |

**Action recommandée : ACHETER (Sizing Réduit)**
- Prix d'entrée suggéré : $59.19
- Stop-loss : $47.83 (−19.2%)
- Take-profit : $76.23 (+28.8%)
- Ratio R/R : 1.5 : 1
- Horizon : 1–3 mois
- Timing : Favorable

> **⚠️ Avertissements :**
> 1. Recommandation basée sur des données **pre-earnings Q1 2026** (résultats toujours non intégrés dans les feeds Yahoo/FMP, 15 jours après le J0 annoncé).
> 2. **Sizing réduit obligatoire** — Beta 4.232 et ATR 9.60% imposent max 5% du portefeuille.
> 3. **Volume sous-moyen** — 0.74× moyenne 20j = participation institutionnelle modérée.
> 4. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC. Surveiller $75k comme seuil critique.
> 5. **Forward P/E négatif** : −62.97× — profitabilité attendue éloignée.
> 6. **Valorisation** : P/E 76.9×, EV/EBITDA 143.9× — multiples élevés.
> 7. **Défiance options record** : put/call 3.95, puts 79.8% — le marché s'hedge massivement malgré le rebond.
> 8. Si cours casse $50.32 (MM50) sans rebond → réviser la position.
> 9. Si cours casse $46.00 (low 19/05) → **passer en SURVEILLER**.
> 10. Si cours casse $47.83 (SL) → **stopper la position**.
> 11. Si gap fill $59.31 avec volume confirmé > moyenne 20j → momentum haussier retrouvé.
> 12. Si structure options se détend (put/call < 2.5) avec rebond du cours → signal haussier additionnel.

---

## Conclusion

**Thèse : CONFIRMÉE — ACHETER (Sizing Réduit) maintenu.**

Le snapshot pré-ouverture du 2026-06-09 confirme la **stabilité totale** des données vs le close officiel du 2026-06-08. Aucune mutation technique, fondamentale ou sentimentale n'est détectée. Le cours stabilisé à $59.19 valide le rebond post-gap du 8 juin.

**Traitement du DRAFT_refresh :**
Le fichier `IREN_2026-06-09_DRAFT_refresh.md` détecté à 10h UTC est un **faux positif**. Les triggers `PRICE_GAP` (+8.91%) et `ATR_SPIKE` (9.60%) correspondent au mouvement du 2026-06-08, déjà pleinement analysé dans le full refresh `IREN_2026-06-08_init.md` et le `_update.md` close 21h. Aucun nouvel événement majeur n'a eu lieu entre le close 21h UTC du 8 juin et le snapshot 10h UTC du 9 juin.

**Différentiels clés vs analyse précédente (close 21:00 UTC 08/06) :**
1. **Cours** : $59.19 → $59.19 — stabilité totale
2. **Volume** : 40.54 M → 40.99 M (+1.1% révision) — toujours 0.74× moyenne
3. **RSI** : 58.78 → 58.78 — inchangé
4. **MM50** : $50.32 → $50.32 — inchangé
5. **Multiples** : P/E 76.87×, Forward P/E −62.97× — inchangés
6. **Consensus PT** : $69.12 — inchangé
7. **Options** : Max Pain $33.00, put/call 3.95, call OI 20.2% — inchangés (anomalie $20.00 dans snapshot 10h, valeur fiable $33.00)
8. **Scores** : Catalyseur 6.3, Valorisation 4.0, Momentum 7.5 — Score Opportunité 5.7/10, Global 61.8/100
9. **Niveaux** : SL $47.83, TP $76.23 — inchangés
10. **Aucune news** : Le calme pré-séance maintient la configuration technique du 8 juin

**Recommandation :**
- **Entrer** à $59.19 avec SL $47.83 / TP $76.23 (R/R 1.5)
- **Sizing réduit** — max 5% du portefeuille (beta 4.232, ATR 9.60%)
- Surveiller l'ouverture US du 9 juin — si le cours comble le gap $59.31 avec volume > moyenne 20j → confirmation haussière
- Premier objectif : $61.86 (previous close avant gap down)
- Deuxième objectif : $66.60 (close 03/06) puis $69.12 (consensus PT)
- **DRAFT_refresh archivé** — faux positif, pas de réécriture nécessaire
- Si rupture sous $50.32 (MM50) → réviser la position
- Si rupture sous $46.00 (low 19/05) → **passer en SURVEILLER**
- Si rupture sous $47.83 (SL) → **stopper la position**

---

*Rapport rédigé le 2026-06-09 — Données sources : `data/latest.json` (fetched_at 2026-06-09T10:00:02 UTC), `data/recommandations_2026-06-09.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_2026-06-09.json`, `data/social_sentiment_2026-06-09.json`, `data/fx_exposure_2026-06-09.json`, `data/events_2026-06-09.json`, `data/upcoming_events_2026-06-09.json`, `data/validation_report.txt`.*

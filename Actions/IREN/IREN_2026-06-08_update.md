# IREN — Mise à Jour (2026-06-08, snapshot 21:00 UTC — Close Officiel)

> **Type :** `_update.md` — Close officiel post-session, snapshot 21:00 UTC
> **Référence précédente :** [IREN_2026-06-08_update.md](IREN_2026-06-08_update.md) (snapshot 17:00 UTC)
> **Référence full refresh :** [IREN_2026-06-08_init.md](IREN_2026-06-08_init.md)
> **Données source :** `data/latest.json` (fetched_at 2026-06-08T21:00:01 UTC), `data/recommandations_2026-06-08.json`, `data/quant_2026-06-08.json`, `data/sector_rotation_2026-06-08.json`, `data/social_sentiment_2026-06-08.json`, `data/fx_exposure_2026-06-08.json`, `data/events_2026-06-08.json`, `data/upcoming_events_2026-06-08.json`, `data/crypto_correlation_latest.json`, `data/validation_report.txt`

---

## Résumé des Changements (vs snapshot 17:00 UTC)

| Métrique | Snapshot 17:00 UTC | Close officiel 21:00 UTC | Δ |
|----------|-------------------|-------------------------|---|
| **Cours close** | **$58.525** | **$59.19** | **+1.13%** |
| **Open** | $56.435 | $56.60 | **+0.29%** |
| **High** | $58.99 | $59.67 | **+1.15%** |
| **Low** | $55.14 | $55.14 | **=** |
| **Previous close** | $54.35 | $54.35 | **=** |
| **Volume** | 22.43 M (0.41× moy.) | **40.54 M (0.74× moy.)** | **+80.7% révision** |
| **RSI 14j** | 58.22 | **58.78** | **+0.56 pt** |
| **ATR 14j** | $5.63 | $5.68 | **+$0.05** |
| **MM 50j** | $50.31 | $50.32 | **+$0.01** |
| **P/E TTM (Yahoo)** | 76.01× | **76.87×** | **+0.86 pt** |
| **Forward P/E** | −62.26× | **−62.97×** | **Détérioration marginale** |
| **Market Cap (Yahoo)** | $20.92 B | **$21.15 B** | **+$0.23 B** |
| **Consensus PT (FMP)** | $69.12 (26 analysts) | $69.12 (26 analysts) | **=** |
| **Max Pain** | $33.00 (exp 2026-06-12) | $33.00 | **=** |
| **Put/Call ratio** | 3.95 | 3.95 | **= — record maintenu** |
| **Call OI %** | 20.2% | 20.2% | **= — puts 79.8%** |
| **Score Opportunité** | 5.7/10 | 5.7/10 | **=** |
| **Score Global ajusté** | 61.8/100 | 61.8/100 | **=** |
| **Action recommandée** | **ACHETER (Sizing Réduit)** | **ACHETER (Sizing Réduit)** | **=** |

**Mutations significatives :**
1. **Close officiel à $59.19 (+1.13% vs 17h, +8.91% vs previous close)** — La clôture se rapproche du high intraday ($59.67) et efface quasiment intégralement le gap down matinal ($59.31 open). Le corps de la bougie est haussier avec clôture proche du sommet, signalant une force acheteuse en fin de séance.
2. **Volume révisé à 40.54 M = 0.74× moyenne 20j** — Le snapshot 17h sous-estimait le volume à 22.43 M (0.41×). Le close final montre un volume de session de 40.54 M, soit 73.7% de la moyenne 20j (55.03 M). Ce volume reste sous la moyenne mais n'est plus « effondré ». La distribution matinale (63.89 M au snapshot 10h) a été partiellement compensée par une activité en fin de séance non capturée dans le snapshot 17h.
3. **RSI 58.78** — Zone neutre-haute stable, à 1.2 pt du seuil de surachat (60). Le momentum reste favorable sans excès.
4. **MM50 remontée à $50.32** — Support dynamique intact, cours désormais **+17.6% au-dessus**.
5. **Multiples mécaniquement dégradés** — P/E TTM 76.87× (+0.86 pt), Forward P/E −62.97× (détérioration marginale). La valorisation reste exigeante.
6. **Structure options inchangée** — Put/call 3.95 record, call OI 20.2%. La défiance massive du marché persiste malgré le rebond de +8.91% sur la session. Persistence remarquable : le marché des options ne déshedge pas.
7. **Validation Report** — [WARNING] IREN : Quality Partielle 4/6, Forward PE négatif, FCF négatif. Pas d'[ERROR] critique.
8. **Aucune news spécifique** détectée pour IREN dans `data/news_2026-06-08.json`.
9. **Sector Rotation** inchangé : XLK top momentum (10.0/10), signal global NEUTRAL.
10. **FX Exposure** inchangé : Score 0/10, exposition CAD 15%, neutre.
11. **Social Sentiment** : 0 mention, score 0/10, aucun buzz retail.
12. **Event-Driven** : `data/events_2026-06-08.json` vide — aucun événement corporate.
13. **Geo Risk** : Score 3/10, flag "low" — inchangé.
14. **Crypto Correlation** (2026-05-17) : corrélation 30j 0.82, beta BTC 2.1, divergence score 4/10 — inchangé.
15. **Quant Report** : `data/quant_report_latest.json` date du 2026-05-17 — insuffisant (p-value 1.0, 0 signaux). Pas de malus/bonus.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 58.78 | Zone neutre-haute (+0.6 pt vs 17h), à 1.2 pt du surachat 60 |
| **ATR 14j** | $5.68 | Volatilité stable, ATR relatif 9.60% |
| **MM 50j** | $50.32 | Cours **+17.6% au-dessus** — support dynamique renforcé |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 55.03 M | Volume session 40.54 M = **73.7%** — sous-moyen mais révisé à la hausse |
| **Range intraday** | $55.14 – $59.67 | Range de 8.2%, clôture à 99.2% du range (proche du high) |
| **52-week high/low** | $76.87 / $8.82 | Cours à **77.0%** du 52W high |

**Niveaux clés (révisés au close) :**
- Support immédiat : **$55.14** (low du 2026-06-08)
- Support : **$50.32** (MM50)
- Support intermédiaire : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support structurel : **$46.00** (low 2026-05-19)
- Support majeur : **$45.00** (alerte baisse historique)
- Résistance immédiate : **$59.31** (open du 2026-06-08, gap fill quasiment atteint)
- Résistance : **$61.86** (previous close avant gap down)
- Résistance majeure : **$66.60** (close 2026-06-03)
- Résistance consensus : **$69.12** (consensus PT FMP)
- Stop-loss (2×ATR) : **$47.83** (−19.2%)
- Take-profit (3×ATR) : **$76.23** (+28.8%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — Le close à $59.19 confirme la solidité du rebond post-gap. Le cours a quasi comblé le gap ($59.31) et clôture à proximité immédiate du high intraday. Le volume révisé (0.74× moyenne) atténue le signal de faiblesse du snapshot 17h (0.41×) mais reste insuffisant pour une conviction institutionnelle forte. Le RSI à 58.78 reste dans une zone neutre favorable sans excès.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** n'est intégré dans les sources Yahoo/FMP au snapshot 21:00 UTC. Les métriques FMP restent au FY 2025 (clos 2025-06-30).

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

**Valorisation (mécaniquement dégradée par la hausse) :**
- P/E TTM Yahoo **76.87×** (+0.86 pt vs 17h) — niveaux élevés
- EV/EBITDA Yahoo **143.88×** — inchangé (extrême)
- Forward P/E **−62.97×** — détérioration marginale vs −62.26×
- P/B Yahoo **7.57×** (+0.08 pt)
- **Cours $59.19 vs Consensus PT $69.12** — upside **+16.8%** (vs +18.1% à 17h)

> **[DONNÉES PARTIELLES]** — `data/accounting_risk_latest.json` inexistant — [DONNÉES MANQUANTES].
> **[WARNING]** — `validation_report.txt` : Quality Partielle 4/6, Forward PE négatif, FCF négatif.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution vs 17:00 UTC |
|--------|--------|------------------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = |
| **Max Pain** | **$33.00** (exp 2026-06-12) | = |
| **Put/Call ratio** | **3.95** | = — **record historique de défiance maintenu** |
| **Call OI %** | **20.2%** | = — puts à 79.8% |
| **Short Interest** | 14.72% | = — fuel squeeze présent |
| **Social Sentiment** | Aucun buzz retail | = |
| **Event-Driven** | Aucun événement | = |
| **News Yahoo** | Aucune | = |
| **Geo Risk** | Score 3/10, flag "low" | = |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = |

**Agent Sector Rotation (2026-06-08) :**
- XLK : momentum score **10.0/10** (top sector, return 20d +4.93%)
- Signal global : **NEUTRAL** (regime UNKNOWN)
- Alignement macro favorable pour IREN (exposition Tech/IA)

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Verdict : Fortement corrélé — le pivot IA n'est pas encore pricé comme découplage BTC

**Analyse options — défiance record persistante :**
Le put/call ratio à **3.95** et le call OI à **20.2%** restent inchangés malgré le rebond de +8.91% sur la session. La persistence est remarquable : le marché des options ne déshedge pas alors que le cours remonte et quasi-comble le gap. Deux interprétations :
1. **Signal contrarian renforcé** — Les institutions maintiennent leur couverture put massive, créant un potentiel de squeeze technique si le cours continue de monter au-delà du gap fill.
2. **Anticipation d'un mauvais catalyseur** — La maintenance de puts dominants (79.8%) malgré le rebond peut refléter une attente de nouvelles négatives (earnings Q1 2026 toujours non publiés après 14 jours du J0 annoncé).

Le **Max Pain $33.00** (exp 2026-06-12) représente un niveau de −44.3% vs cours actuel — tail risk significatif.

---

## Scoring Global (Agent Recommandation — 2026-06-08, close officiel 21:00 UTC)

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
> 1. La recommandation reste basée sur des données **pre-earnings Q1 2026** (résultats toujours non intégrés dans les feeds Yahoo/FMP au 2026-06-08).
> 2. **Sizing réduit obligatoire** — Beta 4.232 et ATR 9.60% imposent une taille de position limitée (max 5% du portefeuille).
> 3. **Volume sous-moyen** — 0.74× moyenne 20j = participation institutionnelle modérée. Le gap fill à $59.31 n'a pas été validé par un volume supérieur à la moyenne.
> 4. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC. Surveiller $75k comme seuil critique.
> 5. **Forward P/E négatif** : −62.97× — profitabilité attendue éloignée.
> 6. **Valorisation** : P/E 76.9×, EV/EBITDA 143.9× — multiples élevés.
> 7. **Consensus PT $69.12** — upside +16.8% (vs +18.1% à 17h) se réduit mécaniquement avec la hausse.
> 8. **Défiance options record** : put/call 3.95, puts 79.8% — le marché s'hedge massivement malgré le rebond. Signal contrarian renforcé ou anticipation de mauvaises nouvelles.
> 9. Si cours casse $50.32 (MM50) sans rebond → signe de faiblesse.
> 10. Si cours casse $46.00 (low 19/05) → **passer en SURVEILLER**.
> 11. Si cours casse $47.83 (SL) → **stopper la position**.
> 12. Si gap fill $59.31 avec volume confirmé > moyenne 20j → momentum haussier retrouvé.
> 13. Si structure options se détend (put/call < 2.5) avec rebond du cours → signal haussier additionnel.

---

## Conclusion

**Thèse : CONFIRMÉE — ACHETER (Sizing Réduit) maintenu.**

Le close officiel à $59.19 confirme le rebond technique entamé après le gap down du matin. La clôture proche du high intraday ($59.67) et le quasi-comblement du gap ($59.31 open) signalent une force acheteuse en fin de séance. Le volume de session finalisé à 40.54 M (0.74× moyenne) corrige à la hausse l'impression de volume "effondré" du snapshot 17h (22.43 M), mais reste sous la moyenne 20j — le rebond n'est pas encore validé par une participation institutionnelle massive.

**Impact du rebond :**
- **Positif** : Le rejet du low $55.14 se confirme. Le cours clôture à 99.2% du range intraday, signalant une domination acheteuse en fin de séance. Le gap down matinal est quasi comblé.
- **Négatif** : Le volume reste sous la moyenne (0.74×) malgré la révision à la hausse. La valorisation se dégrade mécaniquement (P/E 76.9×, upside consensus réduit à +16.8%).
- **Neutre/Contrarian** : La structure options reste à des niveaux de défiance record (put/call 3.95, puts 79.8%) malgré le rebond de +8.91%. Cette persistence est soit un signal contrarian fort (squeeze potentiel), soit une anticipation de mauvaises nouvelles (earnings Q1 non publiés).

**Différentiels clés vs analyse précédente (snapshot 17:00 UTC) :**
1. **Cours +1.13%** : $58.525 → $59.19 — rebond technique confirmé et consolidé
2. **Volume révisé +80.7%** : 22.43 M → 40.54 M (0.74× moyenne) — correction importante du snapshot 17h, mais toujours sous-moyen
3. **RSI +0.6 pt** : 58.22 → 58.78 — momentum stable en zone neutre-haute
4. **MM50 remontée** : $50.31 → $50.32 — support dynamique intact
5. **Multiples dégradés** : P/E 76.0× → 76.9×, Forward P/E −62.26× → −62.97×
6. **Upside consensus réduit** : +18.1% → +16.8% (mécanique avec la hausse du cours)
7. **Options inchangées** : Max Pain $33.00, put/call 3.95 record, call OI 20.2% — défiance persistante
8. **Scores inchangés** : Catalyseur 6.3, Valorisation 4.0, Momentum 7.5 — Score Opportunité 5.7/10, Global 61.8/100
9. **Niveaux révisés** : SL $47.27 → $47.83, TP $75.41 → $76.23 (ATR +$0.05, base prix +$0.67)
10. **Aucune news** : Le rebond est purement technique/correlé BTC

**Recommandation :**
- **Entrer** à $59.19 avec SL $47.83 / TP $76.23 (R/R 1.5)
- **Sizing réduit** — max 5% du portefeuille (beta 4.232, ATR 9.60%)
- Surveiller BTC ($78,143) — seuil critique $75k
- Premier objectif : gap fill confirmé $59.31 (déjà atteint en intraday, clôture $59.19)
- Deuxième objectif : $61.86 (previous close avant gap down)
- Troisième objectif : $66.60 (close 03/06) puis $69.12 (consensus PT)
- **Nouveau** : Surveiller la structure options — si put/call diminue vers 2.0–2.5 avec rebond du cours, cela indiquerait un déshedging favorable
- Si rupture sous $50.32 (MM50) → réviser la position
- Si rupture sous $46.00 (low 19/05) → **passer en SURVEILLER**
- Si rupture sous $47.83 (SL) → **stopper la position**

---

*Rapport rédigé le 2026-06-08 — Données sources : `data/latest.json` (fetched_at 2026-06-08T21:00:01 UTC), `data/recommandations_2026-06-08.json`, `data/quant_2026-06-08.json`, `data/sector_rotation_2026-06-08.json`, `data/social_sentiment_2026-06-08.json`, `data/fx_exposure_2026-06-08.json`, `data/events_2026-06-08.json`, `data/upcoming_events_2026-06-08.json`, `data/crypto_correlation_latest.json`, `data/validation_report.txt`.*

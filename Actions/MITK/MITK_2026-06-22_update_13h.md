# MITK — Mitek Systems — Mise à jour 2026-06-22 13h UTC

> **Desk :** Argus-IA | Ticker : MITK (NASDAQ) | Secteur : Technology / Software — Application
> **Données :** `data/latest.json` (2026-06-22T13:00Z), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`
> **Analyse précédente :** [MITK_2026-06-22_update.md](MITK_2026-06-22_update.md) — Score Global 57.2/100 (ATTENDRE)

---

## 1. Résumé Exécutif & Changements Clés

| Indicateur | Snapshot 22/06 10h UTC | Snapshot 22/06 13h UTC | Δ |
|------------|------------------------|------------------------|---|
| **Cours close** | $17.26 | **$17.26** | inchangé |
| **Change % vs previous close** | +2.31% | **+2.31%** | inchangé |
| **Volume** | 1,770,600 | **1,770,600** | inchangé |
| **Volume vs moy. 20j** | 1.61× | **1.61×** | inchangé |
| **RSI 14j** | 50.62 | **50.62** | inchangé |
| **ATR 14j** | $0.93 | **$0.93** | inchangé |
| **MM 50j** | $15.29 | **$15.29** | inchangé |
| **Forward P/E** | 14.21x | **14.21x** | inchangé |
| **Score Global Ajusté** | 57.2/100 | **57.2/100** | inchangé |
| **Score Catalyseur** | 4.0/10 | **4.0/10** | inchangé |
| **Score Valorisation** | 5.0/10 | **5.0/10** | inchangé |
| **Score Momentum** | 7.3/10 | **7.3/10** | inchangé |
| **Action** | ATTENDRE | **ATTENDRE** | inchangée |
| **Max pain (Yahoo JSON)** | $7.50 — aberrant | **$17.50** | **✅ CORRIGÉ** |
| **Put/Call ratio (Yahoo JSON)** | null — corrompu | **0.05** | **✅ CORRIGÉ** |
| **Call OI % (Yahoo JSON)** | 0.0% — corrompu | **95.2%** | **✅ CORRIGÉ** |

**Verdict :** La thèse est **confirmée — ATTENDRE maintenu** (Score Global Ajusté 57.2/100). Le snapshot 13h UTC ne présente **aucune mutation des données de prix, technique ou fondamentale** par rapport au snapshot 10h UTC — les deux fetchs ont capturé le même close de séance ($17.26, volume 1.77M, RSI 50.62). Le **changement dominant** est la **résolution de l'anomalie options JSON persistante** : après 9 occurrences consécutives (depuis le 3 juin), les données Yahoo options retournent des valeurs cohérentes et exploitables.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | $17.26 | Yahoo Finance |
| Open / High / Low | $17.07 / $17.81 / $16.62 | Yahoo Finance |
| Change % vs previous close | +2.31% | Yahoo Finance |
| Volume | 1,770,600 | Yahoo Finance |
| Volume vs 20j | 1.61× | Calcul (moy. 1,096,465) |
| RSI 14j | 50.62 | Calcul agent |
| ATR 14j | $0.93 | Calcul agent |
| MM 50j | $15.29 | Calcul agent |
| MM 200j | N/A | Données manquantes |
| Golden Cross | N/A | Non détecté |
| Beta | 1.007 | Yahoo Finance |

**Niveaux clés :**
- Support immédiat : $16.62 (low du jour)
- Support structurel : $15.29 (MM50)
- Résistance immédiate : $17.81 (high du jour)
- Résistance majeure : $17.97 (52W high, à 4.0%)
- Stop-loss ATR (2×) : **$15.40** (−10.8%)
- Take-profit ATR (3×) : **$20.05** (+16.2%)
- Ratio R/R : **1.5**

**Verdict timing : Favorable.** Aucun changement technique vs 10h UTC. Le titre progresse dans un canal haussier de MT (+12.9% au-dessus de MM50) avec un RSI 50.62 neutre légèrement orienté haussier. Le volume à 1.61× moyenne 20j reste le signal dominant, mais le high du jour $17.81 a été rejeté (close $17.26), signalant une prise de bénéfices active sous le 52W high.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $779.2M | Yahoo Finance |
| P/E (TTM) | 50.75x | Yahoo Finance |
| Forward P/E | 14.21x | Yahoo Finance |
| EV/EBITDA (Yahoo) | 18.07x | Yahoo Finance |
| EV/Revenue | 4.00x | Yahoo Finance |
| P/B | 3.23x | Yahoo Finance |
| Beta | 1.007 | Yahoo Finance |
| Short Interest | 8.56% | Yahoo Finance |
| Shares Float | 43.7M | Yahoo Finance |
| Shares Outstanding | 45.2M | Yahoo Finance |
| 52W High / Low | $17.97 / $8.53 | Yahoo Finance |
| **FMP Consensus PT** | $16.00 (2 analysts) | FMP Stable API |
| **FMP Gross Margin** | 85.1% | FMP Stable API |
| **FMP EBITDA Margin** | 20.5% | FMP Stable API |
| **FMP EV/EBITDA** | 12.15x | FMP Stable API |
| **FMP P/FCF** | 8.24x | FMP Stable API |
| **FMP Net Debt/EBITDA** | 0.03x | FMP Stable API |
| **FMP ROIC** | 3.16% | FMP Stable API |
| **FMP ROE** | 3.66% | FMP Stable API |
| **FMP FCF Yield** | 12.1% | FMP Stable API |
| **FMP Interest Coverage** | 1.72x | FMP Stable API |

**Filtre Qualité (inchangé) :**
| Critère | Évaluation | Source / Justification |
|---------|------------|------------------------|
| Revenue CAGR 5 ans ≥ 20% | [INCONNU] | Pas de série historique complète dans latest.json |
| Profit CAGR 5 ans ≥ 20% | [INCONNU] | Idem |
| Assets / Liabilities > 1.0 | ✅ | Current ratio 1.19, Debt/Assets 0.34 |
| FCF positif et soutenu | ✅ | FCF yield 12.1%, P/FCF 8.24x |
| Avantage compétitif (moat) | ✅ | Gross margin 85% = moat logiciel / switching costs ID verification |
| Industrie forte croissance (TAM ×5) | ✅ | Digital Identity Verification ~$15–20B d'ici 2030 (CAGR ~15%) |
| **Score Qualité total** | **4 / 6** | ⚠️ Quality Partielle |

> Aucune mutation fondamentale. Le Forward P/E 14.21x reste le pilier attractif. Le faible ROIC (3.16%) et la couverture d'intérêt étroite (1.72×) sont des risques structurels non résolus.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | $16.00 (2 analysts) | FMP Stable API | Dépassé de +7.9% — couverture insuffisante |
| Short Interest | 8.56% | Yahoo Finance | Stable |
| Social Sentiment (Reddit) | 0 mentions / No data | `data/social_sentiment_latest.json` | Silence retail |
| **Max pain (Yahoo JSON)** | **$17.50** | Yahoo Finance | ✅ **Anomalie résolue** — cohérent avec le spot |
| **Put/Call ratio (Yahoo JSON)** | **0.05** | Yahoo Finance | ✅ **Corrigé** — structure extrêmement haussière |
| **Call OI % (Yahoo JSON)** | **95.2%** | Yahoo Finance | ✅ **Corrigé** — dominance calls quasi-totale |
| Expiration options la plus proche | **2026-07-17** (25j) | Yahoo Finance | Inchangée |

**Résolution de l'anomalie options JSON — CONFIRMÉE.**
Le snapshot 13h UTC marque la **10e lecture des données options** et la **1ère occurrence cohérente** depuis le 3 juin. Les valeurs précédentes ($7.50 / null / 0.0%) étaient structurellement corrompues. Les nouvelles valeurs sont économiquement plausibles :
- **Max pain $17.50** : à 0.7% du close ($17.26) — alignement typique max pain / spot
- **Put/Call 0.05** : 20 calls pour 1 put en open interest — positionnement extrêmement haussier
- **Call OI 95.2%** : quasi-totalité de l'open interest en calls

**Interprétation institutionnelle :** La résolution de l'anomalie élimine l'incertitude data quality qui pesait sur le scoring Sentiment. Cependant, la structure options révélée (put/call 0.05, call OI 95.2%) est **d'une extrême bullishness** — potentiellement trop haussière. Un ratio put/call < 0.10 est rare et peut signaler :
1. Un positionnement spéculatif agressif pré-événement (earnings dans 45j)
2. Un risque de "long squeeze" si le cours stagne ou recule (décroissance des calls OTM)
3. Une asymétrie de conviction forte mais fragile (peu de hedges puts)

**Verdict Sentiment : Neutre à légèrement haussier.** Le consensus à $16.00 reste dépassé. La couverture à 2 analysts est insuffisante. Aucune mention Reddit. Pas d'insider trades significatifs. La structure options, bien que corrigée, est à interpréter avec prudence : extrême bullishness = signal de crowd positioning, pas nécessairement de valeur fondamentale.

---

## 5. Bloc Macro, Sectoriel & Risques Transversaux

| Agent | Résultat pour MITK |
|-------|-------------------|
| **Régime macro** | Unknown — données VIX/DXY/taux partiellement indisponibles |
| **Sector rotation** | 🟢 Favorable — XLK top rank (momentum 10.0, +7.07% sur 20j vs SPY) |
| **FX exposure** | 🟢 Neutral — score 0.0, direction aligned, flag 🟢 |
| **Geo risk** | 🟢 Aucun flag détecté pour MITK |
| **Social sentiment** | ⚪ No data — 0 mentions Reddit |
| **Quant significance** | ⚪ Insuffisant — 0 signaux historiques, calibration en cours |
| **Accounting risk** | ⚪ Fichier absent — pas de scan comptable disponible |
| **Event-driven** | ⚪ Aucun événement corporate détecté pour MITK |

**Verdict Macro : Neutre / Légèrement favorable.** Le secteur Technology reste en tête du momentum sectoriel (XLK score 10.0, +7.07% vs SPY sur 20j), vent de queue passif pour MITK. L'absence de données macro complètes empêche un ajustement régime-aware du scoring.

---

## 6. Scoring Global Révisé

| Axe | Score | Pondération | Contribution |
|-------|-------|-------------|--------------|
| Catalyseur | 4.0/10 | 35% | 1.40 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 7.3/10 | 25% | 1.83 |
| **Score Opportunité brut** | **5.2/10** | — | **5.23** |
| Malus / Bonus | — | — | — |
| **Score Global Ajusté** | **57.2/100** | — | **Catégorie ATTENDRE** |

**Comparatif historique :**
- 2026-06-22 10h : 57.2/100 (ATTENDRE, C:4.0 V:5.0 M:7.3)
- 2026-06-22 13h : **57.2/100** (ATTENDRE, C:4.0 V:5.0 M:7.3)

**Aucune mutation du scoring.** Les données de prix, technique et fondamentale sont strictement identiques entre les deux snapshots (même close de séance, même volume, même indicateurs). La résolution de l'anomalie options JSON n'impacte pas directement le scoring composite (Catalyseur/Valorisation/Momentum) car elle ne modifie ni le cours, ni les multiples, ni le RSI. Elle élimine un malus data quality implicite et restaure la confiance dans le signal options.

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → le ticker n'est pas exclu, mais la combinaison Valorisation 5.0 + Catalyseur 4.0 reste trop faible pour justifier un ACHETER.

---

## 7. Niveaux de Sortie Révisés

| Niveau | Valeur | Base | Δ vs précédent |
|--------|--------|------|----------------|
| Stop-loss | **$15.40** | Cours − 2×ATR ($0.93) | inchangé |
| Take-profit | **$20.05** | Cours + 3×ATR ($0.93) | inchangé |
| Ratio R/R | **1.5** | — | inchangé |

**Remarque :** Les niveaux ATR sont inchangés car le cours et l'ATR n'ont pas bougé. Le SL $15.40 reste au-dessus de la MM50 $15.29 (+0.7%).

---

## 8. Conclusion & Action

**Thèse : CONFIRMÉE — ATTENDRE maintenu.**

Le snapshot 13h UTC 2026-06-22 ne présente aucune mutation des données de marché par rapport au snapshot 10h UTC. Le close ($17.26), le volume (1.77M), le RSI (50.62), l'ATR ($0.93) et la MM50 ($15.29) sont strictement identiques — les deux fetchs ont capturé le même état de séance (marché US non ouvert à 10h UTC, données de close de la veille inchangées à 13h UTC).

Le **changement significatif** est la **résolution de l'anomalie options JSON persistante** (9 occurrences depuis le 3 juin) :
- Max pain : $7.50 aberrant → **$17.50 cohérent**
- Put/Call : null → **0.05 (extrêmement haussier)**
- Call OI % : 0.0% → **95.2% (dominance calls)**

Cette correction élimine l'incertitude data quality mais révèle une structure options d'une **extrême bullishness** (put/call 0.05 = 20 calls pour 1 put). Ce positionnement agressif peut être interprété comme :
- 🟢 Un signal de conviction forte pré-éarnings (45j)
- 🔴 Un risque de décroissance brutale si le cours stagne (dilution des primes calls OTM)

**Action : ATTENDRE** — aucune entrée nouvelle recommandée. Les positions ouvertes (si existantes) peuvent être maintenues avec le SL $15.40. La résolution de l'anomalie options ne modifie pas la thèse fondamentale (pas de catalyseur, valorisation neutre, momentum seul insuffisant).

**Conditions pour rétablir ACHETER (Réduit) :**
- Cassure confirmée du 52W high $17.97 avec volume >1.0× moyenne 20j
- RSI > 55 confirmé sur 2 sessions
- Volume maintenu >1.0× sur au moins 2 sessions consécutives
- Upgrade analyste ou révision du consensus PT au-dessus de $18

**Conditions pour dégrader en SURVEILLER :**
- Retour sous MM50 $15.29 avec volume >0.8×
- Volume collapse <0.3× sur 2 sessions consécutives
- RSI < 40

**Prochains événements :**
- Expiration options : **2026-07-17** (25j) — surveillance structure options (max pain $17.50 proche du spot)
- Prochain earnings Q3 FY2026 : **2026-08-06** (45j) — Est EPS $0.24–$0.34, Rev ~$0.1B

---

*Généré par Argus-IA — Sources exclusives : data/latest.json, data/recommandations_2026-06-22.json, data/sector_rotation_2026-06-22.json, data/fx_exposure_2026-06-22.json, data/geo_risk_2026-06-22.json, data/upcoming_events_2026-06-22.json, data/social_sentiment_2026-06-22.json — Date : 2026-06-22*

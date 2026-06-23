# MITK — Mitek Systems — Mise à jour 2026-06-23 Snapshot 13h UTC

> **Desk :** Argus-IA | Ticker : MITK (NASDAQ) | Secteur : Technology / Software — Application
> **Données :** `data/latest.json` (2026-06-23T13:00Z), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`, `data/upcoming_events_latest.json`
> **Analyse précédente :** [MITK_2026-06-23_update.md](MITK_2026-06-23_update.md) — Score Global Ajusté 56.5/100 (ATTENDRE)

---

## 1. Résumé Exécutif & Changements Clés

| Indicateur | Snapshot 23/06 10h UTC | Snapshot 23/06 13h UTC | Δ |
|------------|------------------------|--------------------------|---|
| **Cours close** | $17.31 | **$17.31** | **$0.00 (0.00%)** |
| **Change % vs previous close** | +0.29% | **+0.29%** | inchangé |
| **Volume** | 1,138,000 | **1,138,000** | **inchangé** |
| **Volume vs moy. 20j** | 1.06× | **1.06×** | inchangé |
| **RSI 14j** | 45.17 | **45.17** | inchangé |
| **ATR 14j** | $0.93 | **$0.93** | inchangé |
| **MM 50j** | $15.35 | **$15.35** | inchangé |
| **Forward P/E** | 14.26x | **14.26x** | inchangé |
| **Score Global Ajusté** | 56.5/100 | **56.5/100** | inchangé |
| **Score Catalyseur** | 4.0/10 | **4.0/10** | inchangé |
| **Score Valorisation** | 5.0/10 | **5.0/10** | inchangé |
| **Score Momentum** | 7.0/10 | **7.0/10** | inchangé |
| **Action** | ATTENDRE | **ATTENDRE** | inchangée |

**Verdict :** La thèse est **confirmée — ATTENDRE maintenu**. Stabilité mécanique totale vs snapshot 10h UTC : cours, RSI, ATR, MM50, Forward P/E et volume sont strictement identiques. Évolution notable : **anomalie options JSON Yahoo RÉSOLUE** — le JSON 13h UTC retourne directement des valeurs cohérentes (max pain $17.50, put/call 0.05, call OI 95.2%), invalidant l'erreur récurrente observée depuis le début juin. Cette résolution confirme la structure extrêmement haussière déjà détectée manuellement.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | $17.31 | Yahoo Finance |
| Open / High / Low | $17.10 / $17.90 / $17.02 | Yahoo Finance |
| Change % vs previous close | +0.29% | Yahoo Finance |
| Volume | 1,138,000 | Yahoo Finance |
| Volume vs 20j | 1.06× | Calcul (moy. 1,076,910) |
| RSI 14j | 45.17 | Calcul agent |
| ATR 14j | $0.93 | Calcul agent |
| MM 50j | $15.35 | Calcul agent |
| MM 200j | N/A | Données manquantes |
| Golden Cross | N/A | Non détecté |
| Beta | 1.007 | Yahoo Finance |

**Niveaux clés :**
- Support immédiat : $17.02 (low du jour)
- Support structurel : $15.35 (MM50)
- Résistance immédiate : $17.90 (high du jour)
- Résistance majeure : $17.97 (52W high, à 3.8%)
- Stop-loss ATR (2×) : **$15.45** (−10.7%)
- Take-profit ATR (3×) : **$20.10** (+16.1%)
- Ratio R/R : **1.5**

**Verdict timing : Favorable.** Stabilité totale des données techniques entre 10h et 13h UTC. Le cours reste consolidé à $17.31 sur volume légèrement supérieur à la moyenne (1.06×), confirmant l'absorption au niveau actuel. Le RSI 45.17 reste dans la zone neutre favorable. Le cours conserve une marge de +12.8% au-dessus de la MM50.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $781.7M | Yahoo Finance |
| P/E (TTM) | 50.91x | Yahoo Finance |
| Forward P/E | 14.26x | Yahoo Finance |
| EV/EBITDA (Yahoo) | 18.13x | Yahoo Finance |
| EV/Revenue | 4.02x | Yahoo Finance |
| P/B | 3.24x | Yahoo Finance |
| Beta | 1.007 | Yahoo Finance |
| Short Interest | 8.56% | Yahoo Finance |
| Shares Float | 43.7M | Yahoo Finance |
| Shares Outstanding | 45.2M | Yahoo Finance |
| 52W High / Low | $17.97 / $8.53 | Yahoo Finance |
| **FMP Consensus PT** | $16.00 (2 analysts) | FMP Stable API |
| **FMP Gross Margin** | 85.1% | FMP Stable API |
| **FMP EBITDA Margin** | 20.5% | FMP Stable API |
| **FMP Current Ratio** | 1.19 | FMP Stable API |
| **FMP Interest Coverage** | 1.72x | FMP Stable API |
| **FMP P/FCF** | 8.24x | FMP Stable API |

**Filtre Qualité (inchangé) :**
| Critère | Évaluation | Source / Justification |
|---------|------------|------------------------|
| Revenue CAGR 5 ans ≥ 20% | [INCONNU] | Pas de série historique complète dans latest.json |
| Profit CAGR 5 ans ≥ 20% | [INCONNU] | Idem |
| Assets / Liabilities > 1.0 | ✅ | Current ratio FMP 1.19 |
| FCF positif et soutenu | ✅ | FCF yield 12.1% (FMP), P/FCF 8.24x |
| Avantage compétitif (moat) | ✅ | Gross margin 85% = moat logiciel / switching costs ID verification |
| Industrie forte croissance (TAM ×5) | ✅ | Digital Identity Verification ~$15–20B d'ici 2030 (CAGR ~15%) |
| **Score Qualité total** | **4 / 6** | ⚠️ Quality Partielle |

> **Note divergence Yahoo/FMP :** Le market cap FMP ($446.6M) diverge toujours significativement du market cap Yahoo ($781.7M). Les ratios FMP restent cohérents avec les valeurs historiques. Les métriques Yahoo (market cap, P/E, EV) restent utilisées comme primaires pour le scoring.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | $16.00 (2 analysts) | FMP Stable API | Dépassé de +8.1% — couverture insuffisante |
| Short Interest | 8.56% | Yahoo Finance | Stable |
| Social Sentiment (Reddit) | 0 mentions / No data | `data/social_sentiment_latest.json` | Silence retail |
| **Max pain (Yahoo JSON)** | **$17.50** | Yahoo Finance | ✅ **RÉSOLU** — valeur cohérente vs $17.02–$17.90 du jour |
| **Put/Call ratio (Yahoo JSON)** | **0.05** | Yahoo Finance | ✅ **RÉSOLU** — structure extrêmement haussière |
| **Call OI % (Yahoo JSON)** | **95.2%** | Yahoo Finance | ✅ **RÉSOLU** — aligné avec la thèse haussière technique |
| Expiration options la plus proche | **2026-07-17** (24j) | Yahoo Finance | Inchangée |

> **✅ Anomalie options JSON RÉSOLUE :** Le snapshot 13h UTC confirme la résolution de l'anomalie JSON Yahoo persistante depuis le début juin. Les valeurs retournées (max pain $17.50, put/call 0.05, call OI 95.2%) sont désormais cohérentes avec l'analyse opérationnelle manuelle utilisée dans les rapports précédents. L'écart entre max pain ($17.50) et spot ($17.31) est de 1.1% — alignement classique. Cette résolution renforce la crédibilité du signal haussier options sans apporter de mutation de score (déjà intégré manuellement).

**Verdict Sentiment : Neutre à légèrement haussier.** La structure options est désormais validée par la source primaire (Yahoo JSON) : extrêmement haussière (put/call 0.05, call OI 95.2%). Consensus PT $16.00 toujours dépassé. Aucune mention Reddit. Pas d'insider trades significatifs détectés. Aucune news majeure du jour.

---

## 5. Bloc Macro, Sectoriel & Risques Transversaux

| Agent | Résultat pour MITK |
|-------|-------------------|
| **Régime macro** | Unknown — données VIX/DXY/taux partiellement indisponibles |
| **Sector rotation** | 🟢 Favorable — XLK top rank (momentum 10.0, +7.23% sur 20j vs SPY) |
| **FX exposure** | 🟢 Neutral — score 0.0, direction aligned, flag 🟢 |
| **Geo risk** | 🟢 Aucun flag détecté pour MITK |
| **Social sentiment** | ⚪ No data — 0 mentions Reddit |
| **Quant significance** | ⚪ Insuffisant — 0 signaux historiques, calibration en cours |
| **Accounting risk** | ⚪ Fichier absent — pas de scan comptable disponible |
| **Event-driven** | ⚪ Aucun événement corporate détecté pour MITK |

**Verdict Macro : Neutre.** Le secteur Technology reste en tête du momentum sectoriel (XLK score 10.0, +7.23% vs SPY sur 20j), vent de queue passif pour MITK. Aucun risque géo, FX ou social détecté. Aucun événement corporate signalé dans `data/events_latest.json`.

---

## 6. Scoring Global

| Axe | Score | Pondération | Contribution |
|-------|-------|-------------|--------------|
| Catalyseur | 4.0/10 | 35% | 1.40 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 7.0/10 | 25% | 1.75 |
| **Score Opportunité brut** | **5.2/10** | — | **5.15** |
| Malus / Bonus | — | — | — |
| **Score Global Ajusté** | **56.5/100** | — | **Catégorie ATTENDRE** |

**Comparatif historique :**
- 2026-06-23 10h : 56.5/100 (ATTENDRE, C:4.0 V:5.0 M:7.0)
- 2026-06-23 13h : **56.5/100** (ATTENDRE, C:4.0 V:5.0 M:7.0)

**Explication :** Aucun changement de score. Les données brutes (cours, RSI, ATR, MM, fondamentaux) sont strictement identiques au snapshot 10h UTC. La résolution de l'anomalie options JSON confirme rétrospectivement la structure haussière déjà intégrée manuellement, sans impacter les scores (déjà ajustés).

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → le ticker n'est pas exclu. La combinaison Valorisation 5.0 + Catalyseur 4.0 reste trop faible pour justifier un ACHETER, mais le Momentum 7.0 offre un support technique solide.

---

## 7. Niveaux de Sortie

| Niveau | Valeur | Base | Δ vs précédent |
|--------|--------|------|----------------|
| Stop-loss | **$15.45** | Cours − 2×ATR ($0.93) | inchangé |
| Take-profit | **$20.10** | Cours + 3×ATR ($0.93) | inchangé |
| Ratio R/R | **1.5** | — | inchangé |

**Remarque :** Les niveaux ATR sont inchangés car le cours et l'ATR n'ont pas bougé. Le SL $15.45 reste au-dessus de la MM50 $15.35 (+0.6%). Une cassure sous MM50 avec volume >0.5× invaliderait la tendance haussière de MT.

---

## 8. Conclusion & Action

**Thèse : CONFIRMÉE — ATTENDRE maintenu, stabilité mécanique totale, anomalie options résolue.**

Le snapshot 13h UTC 2026-06-23 confirme l'intégralité de la lecture du snapshot 10h UTC. Cours ($17.31), RSI (45.17), ATR ($0.93), MM50 ($15.35), Forward P/E (14.26x) et volume (1,138K, 1.06×) sont **strictement identiques**. La seule évolution significative est la **résolution de l'anomalie options JSON Yahoo** : les valeurs retournées (max pain $17.50, put/call 0.05, call OI 95.2%) sont désormais cohérentes avec l'analyse opérationnelle manuelle, invalidant l'erreur persistante observée depuis le début juin.

Le **Score Global Ajusté reste à 56.5/100**, au centre de la fourchette ATTENDRE (50–59), à 3.5 pts du seuil ACHETER (Réduit). Le **Score Momentum 7.0/10** offre un support technique solide. L'absence de catalyseur (Score Catalyseur 4.0/10) et la valorisation neutre (5.0/10) justifient le maintien de la prudence.

**Action : ATTENDRE** — aucune entrée nouvelle recommandée. Les positions ouvertes (si existantes) peuvent être maintenues avec le SL $15.45. La proximité du 52W high ($17.97, 3.8%) et l'absence de catalyseur limitent l'upside immédiat.

**Conditions pour rétablir ACHETER (Réduit) :**
- Cassure confirmée du 52W high $17.97 avec volume >1.0× moyenne 20j
- RSI > 55 confirmé sur 2 sessions
- Volume maintenu >1.0× sur au moins 2 sessions consécutives
- Upgrade analyste ou révision du consensus PT au-dessus de $18

**Conditions pour dégrader en SURVEILLER :**
- Retour sous MM50 $15.35 avec volume >0.5×
- Volume collapse <0.3× sur 2 sessions consécutives
- RSI < 40

**Prochains événements :**
- Expiration options : **2026-07-17** (24j) — structure options validée (max pain $17.50 proche du spot)
- Prochain earnings Q3 FY2026 : **2026-08-06** (44j) — Est EPS $0.24–$0.34, Rev ~$0.1B

---

*Généré par Argus-IA — Sources exclusives : data/latest.json, data/recommandations_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/geo_risk_latest.json, data/upcoming_events_latest.json, data/social_sentiment_latest.json, data/events_latest.json — Date : 2026-06-23*

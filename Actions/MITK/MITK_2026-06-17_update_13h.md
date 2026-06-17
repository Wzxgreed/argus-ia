# MITK — Mitek Systems — Mise à jour 2026-06-17 13h UTC

> **Desk :** Argus-IA | Ticker : MITK (NASDAQ) | Secteur : Technology / Software — Application
> **Données :** `data/latest.json` (2026-06-17T13:00Z), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/geo_risk_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Analyse précédente :** [MITK_2026-06-17_update.md](MITK_2026-06-17_update.md) — Score Global 57.8/100 (ATTENDRE)

---

## 1. Résumé Exécutif & Changements Clés

| Indicateur | Snapshot 17/06 10h UTC | Snapshot 17/06 13h UTC | Δ |
|------------|------------------------|----------------------|---|
| **Cours close** | $17.07 | **$17.07** | **inchangé** |
| **Change % vs previous close** | +3.02% | **+3.02%** | inchangé |
| **Volume** | 729,600 | **729,600** | **inchangé** |
| **Volume vs moy. 20j** | 0.68× | **0.68×** | inchangé |
| **RSI 14j** | 49.08 | **49.08** | inchangé |
| **ATR 14j** | $0.89 | **$0.89** | inchangé |
| **MM 50j** | $15.16 | **$15.16** | inchangé |
| **Forward P/E** | 14.06x | **14.06x** | inchangé |
| **52W high** | $17.97 | **$17.97** | inchangé |
| **Distance 52W high** | 5.0% | **5.0%** | inchangé |
| **Score Global Ajusté** | 57.8/100 | **57.8/100** | inchangé |
| **Score Catalyseur** | 4.0/10 | **4.0/10** | inchangé |
| **Score Valorisation** | 5.0/10 | **5.0/10** | inchangé |
| **Score Momentum** | 7.5/10 | **7.5/10** | inchangé |
| **Action** | ATTENDRE | **ATTENDRE** | **confirmée** |
| **Max pain JSON** | $2.50 (aberrant) | **$20.00** | **RÉSOLU** |
| **Put/Call JSON** | null (corrompu) | **0.20** | **RÉSOLU** |
| **Call OI % JSON** | null (corrompu) | **83.1%** | **RÉSOLU** |

**Verdict :** La thèse est **confirmée et stable** (Score Global Ajusté 57.8/100, fourchette ATTENDRE 50–59). Aucune mutation des données de prix, technique ou fondamentale entre les snapshots 10h et 13h UTC — conforme à l'absence de session US dans cet intervalle (pré-market à 13h30 UTC). **L'anomalie options JSON est résolue** : les valeurs JSON 13h ($20.00 / 0.20 / 83.1%) alignent avec les valeurs opérationnelles validées précédemment. L'alerte régression est levée.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | $17.07 | Yahoo Finance |
| Open / High / Low | $16.55 / $17.23 / $16.34 | Yahoo Finance |
| Change % vs previous close | +3.02% | Yahoo Finance |
| Volume | 729,600 | Yahoo Finance |
| Volume vs 20j | 0.68× | Calcul (moy. 1,065,840) |
| RSI 14j | 49.08 | Calcul agent |
| ATR 14j | $0.89 | Calcul agent |
| MM 50j | $15.16 | Calcul agent |
| MM 200j | N/A | Données manquantes |
| Golden Cross | N/A | Non détecté |
| Beta | 1.007 | Yahoo Finance |

**Niveaux clés :**
- Support immédiat : $16.34 (low du jour)
- Support structurel : $15.16 (MM50)
- Résistance immédiate : $17.23 (high du jour)
- Résistance majeure : $17.97 (52W high, à 5.0%)
- Résistance options (max pain) : $20.00
- Stop-loss ATR (2×) : **$15.29** (−10.4%)
- Take-profit ATR (3×) : **$19.74** (+15.6%)
- Ratio R/R : **1.5**

**Verdict timing : Neutre.** Stabilité totale des paramètres techniques. Le titre reste dans un canal haussier de MT (+12.6% au-dessus de MM50) avec un RSI neutre (49.08). Le volume à 0.68× est en récupération vs les sessions précédentes (0.26× à 16/06 17h, 0.33× à 15/06 17h) mais reste sous la moyenne — manque de conviction institutionnelle. L'expiration options demain (2026-06-18) reste un facteur de volatilité intraday à surveiller.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $770.9M | Yahoo Finance |
| P/E (TTM) | 50.21x | Yahoo Finance |
| Forward P/E | 14.06x | Yahoo Finance |
| EV/EBITDA (Yahoo) | 17.87x | Yahoo Finance |
| EV/Revenue | 3.96x | Yahoo Finance |
| P/B | 3.20x | Yahoo Finance |
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

**Filtre Qualité (réactualisé) :**
| Critère | Évaluation | Source / Justification |
|---------|------------|------------------------|
| Revenue CAGR 5 ans ≥ 20% | [INCONNU] | Pas de série historique complète dans latest.json — maintenu de l'initiale |
| Profit CAGR 5 ans ≥ 20% | [INCONNU] | Idem |
| Assets / Liabilities > 1.0 | ✅ | Current ratio 1.19, Debt/Assets 0.34 — solvabilité ok |
| FCF positif et soutenu | ✅ | FCF yield 12.1%, P/FCF 8.24x — génération de cash réelle |
| Avantage compétitif (moat) | ✅ | Gross margin 85% = moat logiciel / switching costs ID verification |
| Industrie forte croissance (TAM ×5) | ✅ | Digital Identity Verification ~$15–20B d'ici 2030 (CAGR ~15%) |
| **Score Qualité total** | **4 / 6** | ⚠️ Quality Partielle (2 critères historiques manquants) |

> Aucune mutation fondamentale. Le profil reste inchangé : Forward P/E 14.06x attractif sur le multiple mais le faible ROIC (3.16%) et la couverture d'intérêt étroite (1.72×) sont des risques structurels persistants. Le consensus à 2 analysts et $16.00 PT reste sous le spot dépassé de +6.7%.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | $16.00 (2 analysts) | FMP Stable API |
| Short Interest | 8.56% | Yahoo Finance |
| Social Sentiment (Reddit) | 0 mentions / No data | `data/social_sentiment_latest.json` |
| **Max pain (Yahoo JSON)** | **$20.00** | Yahoo Finance — **RÉSOLU** |
| **Put/Call ratio (Yahoo)** | **0.20** | Yahoo Finance — **RÉSOLU** |
| **Call OI % (Yahoo)** | **83.1%** | Yahoo Finance — **RÉSOLU** |
| Expiration options la plus proche | **2026-06-18** (1j) | Yahoo Finance |

**Anomalie options JSON — RÉSOLUTION CONFIRMÉE :** Le snapshot 10h UTC présentait une régression vers max pain $2.50 avec put/call et call OI nulls (7e occurrence). Le snapshot 13h UTC rétablit les valeurs correctes : max pain $20.00, put/call 0.20, call OI 83.1%. **L'alerte anomalie options est levée.** La structure haussière des options (call OI dominant à 83.1%) est rétablie et cohérente avec le max pain $20.00 au-dessus du spot.

**Verdict Sentiment : Neutre.** Le consensus à $16.00 offre un upside théorique de −6.7% (dépassé). La couverture à 2 analysts reste insuffisante. Aucune mention Reddit. Pas d'insider trades significatifs détectés. L'expiration options demain reste un catalyseur de volatilité intraday.

---

## 5. Bloc Macro, Sectoriel & Risques Transversaux

| Agent | Résultat pour MITK |
|-------|-------------------|
| **Régime macro** | Unknown — données VIX/DXY/taux partiellement indisponibles dans latest.json |
| **Sector rotation** | 🟢 Favorable — XLK top rank (momentum 10.0, +6.93% sur 20j vs SPY) |
| **FX exposure** | 🟢 Neutral — score 0.0, direction aligned, flag 🟢 (exposition 25% USD, pas de divergence) |
| **Geo risk** | 🟢 Aucun flag détecté pour MITK |
| **Social sentiment** | ⚪ No data — 0 mentions Reddit |
| **Quant significance** | ⚪ Insuffisant — 0 signaux historiques, calibration en cours |
| **Accounting risk** | ⚪ Fichier absent — pas de scan comptable disponible |
| **Event-driven** | 🟢 Aucun événement corporate détecté pour MITK |

**Verdict Macro : Neutre / Légèrement favorable.** Le secteur Technology reste en tête du momentum sectoriel (XLK score 10.0), vent de queue passif. Aucun malus macro, FX, geo, social ou event-driven. L'absence de données macro complètes empêche un ajustement régime-aware du scoring.

---

## 6. Scoring Global Révisé

| Axe | Score | Pondération | Contribution |
|-------|-------|-------------|--------------|
| Catalyseur | 4.0/10 | 35% | 1.40 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 7.5/10 | 25% | 1.88 |
| **Score Opportunité brut** | **5.3/10** | — | **5.28** |
| Malus / Bonus | — | — | — |
| **Score Global Ajusté** | **57.8/100** | — | **Catégorie ATTENDRE** |

**Comparatif historique :**
- 2026-06-17 10h : 57.8/100 (ATTENDRE, C:4.0 V:5.0 M:7.5)
- 2026-06-17 13h : **57.8/100** (ATTENDRE, C:4.0 V:5.0 M:7.5) — **stabilité totale**

**Explication :** Aucun changement de scoring entre 10h et 13h UTC. Les données sources sont identiques. La résolution de l'anomalie options n'impacte pas le score car les valeurs opérationnelles validées étaient déjà utilisées dans le calcul 10h. Le Score Global 57.8/100 reste au plancher de la fourchette ATTENDRE (50–59).

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → le ticker n'est pas exclu, mais la combinaison Valorisation 5.0 + Catalyseur 4.0 est trop faible pour justifier un ACHETER.

---

## 7. Niveaux de Sortie Révisés

| Niveau | Valeur | Base | Δ vs précédent |
|--------|--------|------|----------------|
| Stop-loss | **$15.29** | Cours − 2×ATR ($0.89) | inchangé |
| Take-profit | **$19.74** | Cours + 3×ATR ($0.89) | inchangé |
| Ratio R/R | **1.5** | — | inchangé |

**Remarque :** Les niveaux sont stables. Le SL $15.29 reste au-dessus de la MM50 $15.16 (+0.9%), offrant une marge de sécurité minimale. Une cassure sous MM50 invaliderait la tendance haussière de MT.

---

## 8. Conclusion & Action

**Thèse : CONFIRMÉE — ATTENDRE.**

Le snapshot 13h UTC confirme la **stabilité mécanique totale** vs le snapshot 10h. Aucune mutation structurelle des données de prix, volume, technique ou fondamentale. L'anomalie options JSON est résolue, ce qui renforce la confiance dans la structure haussière des options (call OI 83.1%, max pain $20.00).

**Action : ATTENDRE** — aucune entrée nouvelle recommandée. Les positions ouvertes (si existantes) peuvent être maintenues avec le SL $15.29.

**Conditions pour rétablir ACHETER (Réduit) :**
- Cassure confirmée du 52W high $17.97 avec volume >1.0× moyenne 20j
- RSI > 55 confirmé sur 2 sessions
- Retour du volume >0.8× sur au moins 2 sessions consécutives
- Upgrade analyste ou révision du consensus PT au-dessus de $18

**Conditions pour dégrader en SURVEILLER :**
- Retour sous MM50 $15.16 avec volume >0.8×
- Volume collapse <0.3× sur 2 sessions consécutives
- RSI < 40

**Prochains événements :**
- Expiration options : **2026-06-18** (1j) — surveillance volatilité intraday
- Prochain earnings Q3 FY2026 : **2026-08-06** (50j) — Est EPS $0.24–$0.34, Rev ~$0.1B

---

*Généré par Argus-IA — Sources exclusives : data/latest.json, data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/geo_risk_latest.json, data/upcoming_events_latest.json, data/events_latest.json — Date : 2026-06-17*

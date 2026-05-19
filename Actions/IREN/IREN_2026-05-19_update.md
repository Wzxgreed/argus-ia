# IREN — Mise à Jour Quotidienne (2026-05-19, snapshot 13:00 UTC)

> **Type :** `_update.md` — Révision post-midi (correction données options)
> **Référence précédente :** [IREN_2026-05-19_update.md](IREN_2026-05-19_update.md) (rev. 10:00 UTC)
> **Données source :** `data/latest.json` (timestamp 2026-05-19T13:00:06.782944+00:00), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`

---

## Résumé des Changements

| Métrique | 2026-05-19 10:00 | 2026-05-19 13:00 | Δ |
|----------|------------------|------------------|---|
| **Cours close** | $50.46 | **$50.46** | **—** |
| **Previous close** | $52.94 | **$52.94** | **—** |
| **Volume** | 42.87 M | **42.87 M** | **—** |
| **RSI 14j** | 56.24 | **56.24** | **—** |
| **ATR 14j** | $5.48 | **$5.48** | **—** |
| **MM 50j** | $45.00 | **$45.00** | **—** |
| **P/E TTM** | 65.53× | **65.53×** | **—** |
| **Forward P/E** | −37.52× | **−37.52×** | **—** |
| **EV/EBITDA (Yahoo)** | 134.43× | **134.43×** | **—** |
| **Beta** | 4.18 | **4.18** | **—** |
| **Short Interest** | 0.17% | **0.17%** | **—** |
| **Max Pain** | $20.00 | **$33.00** | **+65.0%** |
| **Put/Call ratio** | N/A | **1.28** | **Nouveau** |
| **Call OI %** | N/A | **43.8%** | **Nouveau** |
| **BTC-USD** | $78,144 | **$78,144** | **—** |
| **Score Opportunité** | 6.3/10 | **6.3/10** | **—** |
| **Score Global ajusté** | 68.3/100 | **68.3/100** | **—** |

**Verdict :** Données brutes strictement inchangées vs snapshot matinal. **Correction majeure sur les données options :** le Max Pain relevé dans `data/latest.json` (13:00 UTC) est **$33.00** (et non $20.00). Le tail risk de queue revient de −60.4% à **−34.6%**, cohérent avec le niveau observé ces derniers jours. Le put/call ratio (1.28) et le call OI % (43.8%) sont désormais disponibles et intégrés. **Aucun flux post-earnings Q1 2026** n'est encore intégré dans les sources Yahoo/FMP au snapshot 13:00 UTC. L'earnings reste l'événement clé du jour (days_until = 0).

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 56.24 | Zone neutre, résilience relative — pas de survente |
| **ATR 14j** | $5.48 | Volatilité élevée stable (beta 4.18) |
| **MM 50j** | $45.00 | Cours **+12.1% au-dessus** — tendance haussière intacte |
| **MM 200j** | N/A | Non disponible |
| **Volume 20j moy.** | 52.79 M | Volume du jour 42.87 M = **81.2%** du moyen — participation stable |
| **Range intraday (veille)** | $48.48 – $53.11 | Low $48.48 défendu, résistance à l'open $53.08 |
| **52-week high/low** | $76.87 / $8.27 | Cours à **65.6%** du 52W high |

**Niveaux clés (inchangés) :**
- Support immédiat : $48.48 (low du 2026-05-18)
- Support structurel : $45.00 (psychologique + MM50)
- Résistance : $52.94 (previous close) puis $53.08 (open)
- Stop-loss (2×ATR) : **$39.50** (−21.7%)
- Take-profit (3×ATR) : **$66.90** (+32.6%)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable** — La structure technique est intacte. Tant que le cours se maintient au-dessus de $48.48 (support immédiat) et de $45.00 (MM50), la tendance haussière n'est pas remise en cause. Le Max Pain corrigé à $33.00 représente un niveau de risque de queue à −34.6%, toujours en-dessous du SL ($39.50) mais moins extrême que le niveau $20.00 précédemment rapporté.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux fondamental** depuis le snapshot 10:00 UTC. Les données FMP restent au FY 2025 (clos 2025-06-30). L'earnings Q1 2026 n'est toujours pas intégré dans Yahoo/FMP au snapshot 13:00 UTC du 2026-05-19.

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $18.03 B | $3.13 B | **−83%** | Yahoo |
| **EV/EBITDA** | 134.43× | 17.48× | **−87%** | Yahoo |
| **P/B** | 6.67× | 1.72× | **−74%** | Yahoo |
| **P/E TTM** | 65.53× | 35.96× | **−45%** | Yahoo |
| **EV/Sales** | 26.13× | 7.04× | **−73%** | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif
- ❌ FCF négatif (price_to_fcf = −2.77)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29)
- ✅ Gross Margin 68.3%
- ✅ EBITDA Margin 40.3%
- ⚠️ Moat / TAM : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé

> **⚠️ Points de vigilance earnings (Q1 2026, FY Q3) — toujours en attente :**
> 1. Guidance HPC/IA : % du CA guide issu du contrat NVIDIA ?
> 2. Marges HPC vs legacy mining — Operating Margin 3.5% doit s'améliorer
> 3. FCF : sur le chemin du positif ?
> 4. Dette / renégociation sous taux 10Y ~4.6%
> 5. ROIC : le pivot IA doit montrer une amélioration

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution |
|--------|--------|-----------|
| **Consensus PT (FMP)** | $65.86 (21 analysts) | Inchangé |
| **Max Pain** | $33.00 | **Corrigé** — tail risk −34.6% (vs −60.4% rapporté à 10:00 UTC) |
| **Put/Call ratio** | 1.28 | **Nouveau** — légèrement puts-dominated (>1.0 = bearish tilt modéré) |
| **Call OI %** | 43.8% | **Nouveau** — puts majoritaires (56.2% put OI implicite) |
| **Short Interest** | 0.17% | Très faible — pas de short squeeze setup |
| **Social Sentiment** | 0 mention, Score 0/10 | Aucun buzz Reddit/Yahoo |
| **Event-Driven** | Aucun événement | `data/events_latest.json` vide pour IREN |
| **News Yahoo** | Aucune | `data/news_latest.json` vide pour IREN |

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Divergence Score : **4/10**
- Premium vs NAV estimé : **+12%**
- Verdict : *Fortement corrélé — pivot IA non encore pricé*

**Commentaire :** L'absence de mentions sociales, de news et de flux institutionnels confirme que le mouvement reste technique/institutionnel. Le put/call ratio à 1.28 révèle une légère défiance des options traders (puts en excès), cohérent avec l'attentisme pré-earnings. Le Max Pain corrigé à $33.00 est un ancrage de risque de queue plus réaliste que le niveau $20.00 précédemment lu. Aucun upgrade/downgrade ni insider trade significatif détecté.

---

## Scoring Global (Agent Recommandation — 2026-05-19, snapshot 13:00 UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 8.3/10 | 35% | 2.91 |
| **Valorisation** | 4.5/10 | 40% | 1.80 |
| **Momentum** | 6.5/10 | 25% | 1.63 |
| **Score Opportunité** | **6.3/10** | | |

**Malus/Bonus appliqués :**
- Geo Risk Score 3/10 → malus faible (−5.0 pts)
- FX Impact Score 0/10 → neutre
- Accounting Risk : données manquantes (M-Score, Z-Score non disponibles) — [DONNÉES MANQUANTES]
- Event-Driven : aucun malus/bonus
- Social Sentiment : 0 → pas de malus/bonus
- Sector Rotation : XLK top momentum (10/10), XLE bullish — IREN exposé Technology/IA Infrastructure, alignement favorable → **bonus +10.0 pts**

| Score brut | Malus | Bonus | **Score Global ajusté** |
|------------|-------|-------|------------------------|
| 63.3/100 | −5.0 | +10.0 | **68.3/100** |

**Action recommandée : ACHETER — Sizing Réduit**
- Prix d'entrée suggéré : $50.46
- Stop-loss : $39.50 (−21.7%)
- Take-profit : $66.90 (+32.6%)
- Ratio R/R : 1.5 : 1
- Horizon : 1–3 mois
- Timing : Favorable

> **⚠️ Avertissement :** La recommandation reste basée sur des données **pre-earnings**. L'annonce du Q1 2026, attendue aujourd'hui (2026-05-19), peut modifier radicalement le score. Le sizing réduit est impératif (beta 4.18, corrélation BTC 0.82). Attendre la publication des résultats avant toute nouvelle entrée significative.

---

## Scénarios Post-Earnings (Inchangés)

| Scénario | Conditions | Impact cours estimé | Action |
|----------|------------|---------------------|--------|
| **Optimiste (25%)** | Beat revenue + guidance HPC forte + FCF positif + ROIC > 5% | +15–25% → $58–$63 | **Renforcer** — pivot IA validé |
| **Central (50%)** | Inline + guidance inchangée + FCF stable | ±5% → $48–$53 | **Conserver** — thèse inchangée |
| **Pessimiste (25%)** | Miss + compression marges + guidance cut + ROIC stagnant | −15–25% → $38–$43 | **Réduire** — revalorisation nécessaire |

**Prix cible :** $65.86 (consensus FMP, 21 analysts) — **inchangé en l'absence de nouveaux résultats.**

---

## Conclusion

**Thèse : CONFIRMÉE — Correction Max Pain, données options complétées, structure inchangée**

La structure technique et fondamentale d'IREN est **strictement inchangée** entre les snapshots 10:00 UTC et 13:00 UTC du 2026-05-19. Le cours reste à $50.46 (close de la veille, marché US ouvert mais pas de nouvelle clôture intégrée). Les deux corrections majeures de ce snapshot sont :
1. **Max Pain corrigé à $33.00** (vs $20.00 rapporté à 10:00 UTC) — le tail risk de queue revient à −34.6%, plus cohérent avec l'historique récent
2. **Put/Call ratio (1.28) et Call OI % (43.8%)** désormais disponibles — léger excès de puts, cohérent avec l'attentisme pré-earnings

**Points clés :**
1. **Cours stable** à $50.46 — close inchangé (marché ouvert, pas de nouveau close intégré)
2. **Volume stable** (81% du moyen) — participation inchangée
3. **Earnings J0** — résultats Q1 2026 attendus aujourd'hui, non encore intégrés dans FMP/Yahoo
4. **Max Pain corrigé $33.00** — tail risk −34.6%, au-dessus du SL $39.50 mais sans incidence sur la recommandation
5. **Score Opportunité 6.3/10** — inchangé (Catalyseur 8.3 compense Valorisation 4.5)
6. **Score Global ajusté 68.3/100** — inchangé (bonus sectoriel XLK top momentum)
7. **Filtre Qualité 4/6** inchangé — Quality Partielle, FCF négatif persistant
8. **Proxy BTC intact** — corrélation 0.82, beta 2.1, divergence score 4/10
9. **Sector rotation** : XLK top momentum (10/10) — contexte macro favorable au secteur
10. **Options** : put/call 1.28, call OI 43.8% — défiance modérée des options traders pré-earnings

**Récommandation :** Maintenir **ACHETER à sizing réduit** avec SL $39.50 / TP $66.90, **MAIS** :
- **Ne pas renforcer** avant les résultats Q1 2026
- Si le cours casse $48.48 sans rebond → réduire l'exposition
- Si earnings beat + guidance HPC forte → le catalyseur pourrait justifier un relèvement du score Valorisation
- La MM50 à $45 est le niveau ultime de défense : si cassée, passer en ATTENDRE
- Le Max Pain à $33.00 est un niveau de risque de queue à surveiller si guidance cut sévère (bien que supérieur au SL)

---

*Rapport généré le 2026-05-19 — Données sources : data/latest.json (13:00 UTC), data/recommandations_latest.json, data/crypto_correlation_latest.json, data/geo_risk_latest.json, data/fx_exposure_latest.json, data/social_sentiment_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/sector_rotation_latest.json*

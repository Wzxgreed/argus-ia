# IREN — Mise à Jour Quotidienne (2026-05-19, snapshot 10:00 UTC)

> **Type :** `_update.md` — Mise à jour matinale post-pipeline (snapshot 10:00 UTC)
> **Référence précédente :** [IREN_2026-05-18_update.md](IREN_2026-05-18_update.md) (rev. 22:35 UTC)
> **Données source :** `data/latest.json` (timestamp 2026-05-19T10:00:06.624603+00:00), `data/recommandations_latest.json`

---

## Résumé des Changements

| Métrique | 2026-05-18 22:35 | 2026-05-19 10:00 | Δ |
|----------|------------------|------------------|---|
| **Cours close** | $50.46 | **$50.46** | **—** |
| **Previous close** | $52.94 | **$52.94** | **—** |
| **Volume** | 42.39 M | **42.87 M** | **+0.9%** |
| **RSI 14j** | 56.24 | **56.24** | **—** |
| **ATR 14j** | $5.48 | **$5.48** | **—** |
| **MM 50j** | $45.00 | **$45.00** | **—** |
| **P/E TTM** | 65.53× | **65.53×** | **—** |
| **Forward P/E** | −37.52× | **−37.52×** | **—** |
| **EV/EBITDA (Yahoo)** | 140.45× | **134.43×** | **−4.3%** |
| **P/B (Yahoo)** | 6.67× | **6.67×** | **—** |
| **Beta** | 4.18 | **4.18** | **—** |
| **Short Interest** | 0.17% | **0.17%** | **—** |
| **Max Pain** | $33.00 | **$20.00** | **−39.4%** |
| **Put/Call ratio** | 1.55 | **N/A** | **Données manquantes** |
| **BTC-USD** | $78,144 | **$78,144** | **—** |
| **Score Opportunité** | 6.3/10 | **6.3/10** | **—** |
| **Score Global ajusté** | 68.3/100 | **68.3/100** | **—** |

**Verdict :** Données brutes quasi-stables entre le close du 2026-05-18 et le snapshot matinal du 2026-05-19. Le close de $50.46 est inchangé (marché US fermé au moment du fetch 10:00 UTC). **Le Max Pain a chuté de $33.00 à $20.00 (−39.4%)**, réduisant le tail risk de −34.6% à −60.4% — ce niveau est désormais bien en-dessous du stop-loss suggéré. **L'earnings Q1 2026 reste l'événement clé du jour** (days_until = 0 dans `upcoming_events_latest.json`). Aucun nouveau flux post-earnings n'est encore intégré. La thèse est **confirmée** avec réserve earnings inchangée.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 56.24 | Zone neutre, résilience relative — pas de survente malgré le gap |
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

**Verdict timing : Favorable** — La structure technique est intacte. Tant que le cours se maintient au-dessus de $48.48 (support immédiat) et de $45.00 (MM50), la tendance haussière n'est pas remise en cause. Le Max Pain à $20.00 est désormais un niveau de risque de queue bien en-dessous du SL ($39.50), ce qui renforce la cohérence du setup technique.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux fondamental** depuis le snapshot 22:35 du 2026-05-18. Les données FMP restent au FY 2025 (clos 2025-06-30). L'earnings Q1 2026 n'est toujours pas intégré dans Yahoo/FMP au snapshot 10:00 UTC du 2026-05-19.

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| **Market Cap** | $18.03 B | $3.13 B | **−83%** | Yahoo |
| **EV/EBITDA** | 134.43× | 17.48× | **−87%** | Yahoo |
| **P/B** | 6.67× | 1.72× | **−74%** | Yahoo |
| **P/E TTM** | 65.53× | 35.96× | **−45%** | Yahoo |
| **EV/Sales** | 26.13× | 7.04× | **−73%** | Yahoo |

**Métriques fondamentales retenues (source Yahoo, cross-check FMP) :**

| Métrique | Valeur | Signal |
|----------|--------|--------|
| **Market Cap** | $18.03 B | Inchangé |
| **P/E TTM** | 65.53× | Très élevé — prime IA/mining |
| **Forward P/E** | −37.52× | Négatif — pas de profitabilité forward |
| **EV/EBITDA** | 134.43× | Extrême — prix du pivot IA inclus |
| **P/B** | 6.67× | Élevé |
| **Gross Margin** | 68.3% | Bon |
| **EBITDA Margin** | 40.3% | Bon |
| **Operating Margin** | 3.46% | Faible |
| **Net Margin** | 17.4% | Rentable au net sur FY 2025 |
| **Debt/Equity** | 53.1% | Modéré |
| **Interest Coverage** | 1.57× | Faible |
| **FCF Yield** | −36.0% | Cash burn confirmé |
| **ROIC (FMP)** | 0.58% | Très faible |
| **ROE (FMP)** | 4.78% | Faible |
| **Net Debt/EBITDA (FMP)** | 1.98× | Modéré |

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
| **Max Pain** | $20.00 | **−39.4%** — tail risk désormais à −60.4% vs close |
| **Put/Call ratio** | N/A | Données manquantes dans le snapshot |
| **Call OI %** | N/A | Données manquantes |
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

**Commentaire :** L'absence de mentions sociales, de news et de flux institutionnels confirme que le mouvement reste technique/institutionnel. Le max pain à $20.00 est un ancrage de risque de queue désormais très éloigné du cours, ce qui peut refléter une compression de la volatilité implicite des options à très court terme (expiration 2026-05-22) ou un repositionnement des options puts vers des strikes plus bas. Aucun upgrade/downgrade ni insider trade significatif détecté.

---

## Scoring Global (Agent Recommandation — 2026-05-19, snapshot 10:00 UTC)

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
| **Pessimiste (25%)** | Miss + compression marges + guidance cut + ROIC stagnant | −15–25% → $38–$43 (−60% tail risk vers max pain $20) | **Réduire** — revalorisation nécessaire |

**Prix cible :** $65.86 (consensus FMP, 21 analysts) — **inchangé en l'absence de nouveaux résultats.**

---

## Gestion des DRAFT_refresh

| DRAFT | Trigger | Conclusion | Statut |
|-------|---------|------------|--------|
| `_DRAFT_refresh_2026-05-18` | ATR_SPIKE 10.86% | **Confirm** — faux positif de volatilité résiduelle | Archivé |
| `IREN_2026-05-19_DRAFT_refresh.md` | ATR_SPIKE 10.86% | **Confirm** — données strictement inchangées vs snapshot 22:35 UTC du 2026-05-18, aucun nouveau flux post-earnings intégré | Traité dans ce _update.md |

**Log REFRESH_LOG.md :** mise à jour avec conclusion confirm pour les entrées du 2026-05-19.

---

## Conclusion

**Thèse : CONFIRMÉE — données stables, DRAFT_refresh traité, Max Pain révisé à la baisse**

La structure technique d'IREN est **intacte** au-dessus de la MM50 à $45.00. Le snapshot matinal du 2026-05-19 confirme la stabilité totale des niveaux établis hier soir (close $50.46, RSI 56.24, ATR $5.48). Le DRAFT_refresh déclenché par ATR_SPIKE (10.86%) a été analysé, conclu comme un faux positif de volatilité résiduelle (données inchangées), et traité. Aucun nouveau flux fondamental, institutionnel, optionnel ou social n'est survenu dans l'intervalle.

**Points clés :**
1. **Cours stable** à $50.46 — close identique au snapshot précédent (marché fermé au fetch 10:00 UTC)
2. **Volume stable** (81% du moyen) — participation inchangée
3. **Earnings J0** — résultats Q1 2026 attendus aujourd'hui, non encore intégrés dans FMP/Yahoo
4. **Max Pain révisé à $20.00** (−39.4%) — tail risk de queue désormais bien en-dessous du SL ($39.50)
5. **Score Opportunité 6.3/10** — inchangé (Catalyseur 8.3 compense Valorisation 4.5)
6. **Score Global ajusté 68.3/100** — inchangé (bonus sectoriel XLK top momentum)
7. **Filtre Qualité 4/6** inchangé — Quality Partielle, FCF négatif persistant
8. **Proxy BTC intact** — corrélation 0.82, beta 2.1, divergence score 4/10
9. **Sector rotation** : XLK top momentum (10/10) — contexte macro favorable au secteur
10. **DRAFT_refresh traité** — ATR_SPIKE archivé comme faux positif de volatilité résiduelle

**Récommandation :** Maintenir **ACHETER à sizing réduit** avec SL $39.50 / TP $66.90, **MAIS** :
- **Ne pas renforcer** avant les résultats Q1 2026
- Si le cours casse $48.48 sans rebond → réduire l'exposition
- Si earnings beat + guidance HPC forte → le catalyseur pourrait justifier un relèvement du score Valorisation
- La MM50 à $45 est le niveau ultime de défense : si cassée, passer en ATTENDRE
- Le Max Pain à $20.00 est un niveau de risque de queue extrême — à surveiller si guidance cut sévère

---

*Rapport généré le 2026-05-19 — Données sources : data/latest.json, data/recommandations_latest.json, data/crypto_correlation_latest.json, data/geo_risk_latest.json, data/fx_exposure_latest.json, data/social_sentiment_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/sector_rotation_latest.json*

# SOFI — Mise à jour quotidienne

> **Date :** 2026-06-22 (snapshot 10:00 UTC — close final confirmé)
> **Type :** Mise à jour standard
> **Trigger :** Aucun — DRAFT_refresh 22/06 archivé comme faux positif ATR_SPIKE (même motif que 15–17/06, ATR absolu stable $1.01)

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | 2026-06-22 | 2026-06-17 (close) | Δ |
|----------|-----------|---------------------|---|
| Cours close | **$17.91** | $17.71 | **+1.13%** |
| RSI 14j | **48.0** | 58.54 | **−10.54 pts** |
| ATR 14j | **$1.01** | $1.07 | **−5.6%** |
| MM 50j | **$16.94** | $16.89 | +$0.05 |
| Écart MM50 | **+5.72%** | +4.85% | +87 bps |
| Volume | **80.96M** | 105.31M | **−23.1%** |
| Volume vs 20j | **1.0×** | 1.38× | −0.38× |
| Forward P/E | **21.94** | 21.69 | +1.2% |
| Short interest | **14.71%** | 14.71% | stable |

**Verdict global :** Consolidation technique saine. Le RSI normalise après l'excès de surachat du 01/06 (RSI 69.63) et revient dans la zone neutre favorable (48). Le volume retombe à la moyenne 20j (1.0×) après le pic confirmatoire du 17/06 (1.38×) — profil de consolidation post-breakout, non de distribution. Le reclaim MM50 se renforce (+5.72% écart). Aucune news structurante. **Thèse confirmée avec vigilance.**

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | $17.91 | Yahoo Finance |
| Open / High / Low | $17.825 / $17.99 / $17.265 | Yahoo Finance |
| Change % | +2.81% | Yahoo Finance |
| Volume | 80,961,100 | Yahoo Finance |
| Volume vs 20j | 1.0× (moy. 80,795,830) | Calcul agent |
| RSI 14j | 48.0 | Calcul agent |
| ATR 14j | $1.01 | Calcul agent |
| MM 50j | $16.94 | Calcul agent |
| MM 200j | — | Calcul agent |
| Golden Cross | — | Calcul agent |
| Beta | 2.152 | Yahoo Finance |

**Niveaux clés :**
- Support immédiat : $17.00 (psychologique + ancien gap 01/06)
- Support secondaire : $16.94 (MM50)
- Résistance : $18.58 (high 01/06)
- Stop-loss ATR (2×) : **$15.89** (cours − 2×ATR)
- Take-profit ATR (3×) : **$20.94** (cours + 3×ATR)

**Verdict timing :** Favorable — cours au-dessus de MM50 avec écart confortable (+5.72%), RSI 48 en zone neutre (ni surachat ni survente), ATR en compression ($1.01) indiquant une volatilité décroissante post-breakout. Structure de consolidation saine.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $22.97B | Yahoo Finance |
| P/E (TTM) | 39.8 | Yahoo Finance |
| Forward P/E | 21.94 | Yahoo Finance |
| EV/Revenue | 5.456 | Yahoo Finance |
| P/B | 2.12 | Yahoo Finance |
| FMP Consensus PT | $25.41 (27 analysts) | FMP Stable API |
| FMP Gross Margin | 75.1% | FMP Stable API |
| FMP EV/EBITDA | 35.68 | FMP Stable API |
| FMP Debt/Equity | 0.184 | FMP Stable API |

**Filtre Qualité (inchangé vs 17/06) :**
- Revenue CAGR 5 ans ≥ 20% : ✅ (croissance historique fintech lending + banking)
- Profit CAGR 5 ans ≥ 20% : ⚠️ (transition récente à la rentabilité, trajectoire positive)
- Assets/Liabilities > 1.0 : ✅ (FMP current ratio 0.24 — [DONNÉES PARTIELLES] bilan spécifique banque)
- FCF positif et croissant 5 ans : ⚠️ (FCF yield négatif −13.2%, capex/to revenue 5.1%)
- Avantage compétitif (moat) : ✅ (charter bancaire 2022 = barrière réglementaire modérée)
- Industrie forte croissance (TAM ×5) : ✅ (fintech banking + lending + investing, TAM >$500B)

**Score Qualité total : 4/6** (Quality Partielle) — inchangé. Aucun événement majeur ne modifie la structure fondamentale.

---

## 4. Bloc Sentiment / Options / News

| Signal | Valeur | Source | Δ vs 17/06 |
|--------|--------|--------|------------|
| Consensus analystes (FMP) | $25.41 (27 analysts) | FMP | inchangé |
| Put/Call ratio | 0.42 | Historique 17/06 | [ALERTE DATA QUALITY] null dans latest.json |
| Max pain | $17.00 | Historique 17/06 | [ALERTE DATA QUALITY] $5.00 aberrant dans latest.json |
| Call OI % | 70.6% | Historique 17/06 | [ALERTE DATA QUALITY] null dans latest.json |
| Short interest | 14.71% | Yahoo Finance | stable |

**Verdict Sentiment :** Neutre légèrement haussier — consensus PT $25.41 (+41.9% upside vs $17.91) inchangé. Short interest 14.71% maintenu = setup asymétrique squeeze/pression vendeuse intact. Options : repositionnement haussier conservé (Call OI 70.6%, Put/Call 0.42) — valeurs historiques utilisées car données latest.json corrompues.

**News & Événements :**
- Aucune news structurante détectée ce jour.
- Aucun événement corporate (M&A, buyback, guidance, activism) — `data/events_latest.json` : 0 événements.
- Earnings Q2 FY2026 : **2026-07-28** (dans **36 jours**) — estimates EPS $0.10–$0.11, Rev $1.1B (source : yfinance).

---

## 5. Scoring global

| Score | 2026-06-22 | 2026-06-17 | Δ |
|-------|-----------|------------|---|
| Score Opportunité | **6.4/10** | 6.5/10 | −0.1 pt |
| Score Catalyseur | **6.8/10** | 6.8/10 | stable |
| Score Valorisation | **5.5/10** | 5.5/10 | stable |
| Score Momentum | **7.3/10** | 7.5/10 | −0.2 pt |
| Score Global | **64.0/100** | 69.5/100 | −5.5 pts |
| Score Global ajusté | **69.0/100** | 69.5/100 | −0.5 pt |
| Action | **ACHETER (Réduit)** | ACHETER (Réduit) | inchangé |
| Timing | **Favorable** | Favorable | inchangé |

**Source :** `data/recommandations_latest.json` (pipeline 2026-06-22).

**Note sur le delta :** La légère baisse du Score Global (−5.5 pts brut, −0.5 pt ajusté) reflète principalement la normalisation du momentum (RSI 48.0 vs 58.54) et la compression du volume (1.0× vs 1.38×). Le reclassement n'est pas remis en cause — le score ajusté 69.0 reste dans la fourchette ACHETER (60–74).

---

## 6. Niveaux révisés

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix d'entrée suggéré | $17.91 | Cours actuel |
| Stop-loss | **$15.89** | Cours − 2×ATR ($1.01) |
| Take-profit | **$20.94** | Cours + 3×ATR ($1.01) |
| Ratio R/R | **1.5×** | (TP − Cours) / (Cours − SL) |
| Sizing | **Réduit** | Score Global 60–74 |

**Comparaison SL/TP vs 17/06 :**
- SL : $15.89 (vs $15.57) — révisé à la hausse car ATR $1.01 < $1.07 précédent, mais cours plus haut
- TP : $20.94 (vs $20.92) — quasi inchangé
- Ratio R/R : 1.5× stable

---

## 7. Bloc Macro & Sectoriel

**Régime macro :** Unknown (`data/latest.json` — régime non déterminé ce jour).

**Sectoriel (Sector Rotation) :**
- XLF (Financials) : #3/11 sectors, momentum score **4.25/10** — vent de poupe modéré, pas de rotation défavorable détectée.
- SOFI classé Financial Services / Credit Services — alignement sectoriel neutre.

**Exposition FX :**
- `data/fx_exposure_latest.json` : exposition 55%, direction export, primary EUR/CNY.
- FX Impact Score : 0.0 (neutre), divergence flag : aligned, flag 🟢.
- Aucun headwind/tailwind FX détecté.

**Géopolitique :**
- `data/geo_risk_latest.json` (2026-05-17) : SOFI non flaggé — score politique non applicable (activité domestique US).

---

## 8. Bloc Quant & Risques

**Quant :**
- `data/quant_report_latest.json` (2026-05-17) : 0 signaux historiques — calibration insuffisante.
- p-value : 1.0 (non significatif). Aucune alerte de calibration.

**Accounting :**
- `data/accounting_risk_latest.json` : fichier absent — non évalué.

**Social Sentiment :**
- `data/social_sentiment_latest.json` : 0 mentions Reddit, sentiment score 0.0 (No data), pump detected : false.

---

## 9. Conclusion — Thèse confirmée avec vigilance

**La thèse est confirmée.** Le reclaim MM50 initié le 15/06 et renforcé le 16/06 reste valide avec un écart de +5.72%. Le RSI normalise mécaniquement à 48.0 (sortie de la zone de surachat 58–69) — ce n'est pas un signal baissier mais un retour à une zone technique saine. L'ATR se compresse à $1.01, typique d'une phase de consolidation post-breakout.

**Point de vigilance :** Le volume est retombé à 1.0× (80.96M) après le pic confirmatoire du 17/06 (1.38×). Cette normalisation n'est pas inquiétante en soi (consolidation classique), mais un volume <0.7× sur 2–3 sessions consécutives justifierait une révision du timing.

**Catalyseurs forward :**
| Catalyst | Timeline | Probabilité | Impact |
|----------|----------|-------------|--------|
| Earnings Q2 FY2026 | 28 juillet 2026 (36j) | Haute | EPS $0.10–$0.11, Rev $1.1B — catalyseur majeur |
| Décision Fed (taux) | Juin–Juillet 2026 | Moyenne | Impact direct sur NIM et lending |
| Short squeeze setup | Continu | Moyenne | SI 14.71% = setup asymétrique |

**Risques clés :**
1. **Volume faible prolongé** — <0.7× sur 2+ sessions = distribution suspecte, révision timing.
2. **Retour sous MM50** — un close sous $16.94 invaliderait le breakout et justifierait un reclassement ATTENDRE.
3. **Earnings Q2** — 36j. Si guidance cut ou miss EPS, risque de gap baissier important (beta 2.152).
4. **Dépendance taux / prêts étudiants** — risque macro structurel non résolu.

---

*Généré automatiquement — données source : `data/latest.json` (2026-06-22T10:00 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/social_sentiment_latest.json`.*

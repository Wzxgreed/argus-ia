# NOK — Mise à Jour (2026-05-18)

## Résumé des Changements depuis l'Analyse Précédente (2026-05-17)

| Indicateur | 2026-05-17 | 2026-05-18 | Variation | Signal |
|-----------|------------|------------|-----------|--------|
| Cours close | $13.95 | $13.95 | 0.00 % | Stable jour-sur-jour |
| Change intraday | — | −3.53 % | — | Retour au close précédent ($14.46 → $13.95) |
| RSI 14j | 68.40 | 68.40 | 0.0 pt | Proche surachat, inchangé |
| ATR 14j | $0.96 | $0.96 | $0.00 | Volatilité inchangée |
| Volume relatif | 0.87× | 0.87× | 0.0× | Liquidité réduite |
| MM 50j | $10.17 | $10.17 | $0.00 | Support intact |
| Premium vs consensus $9.26 | +50.5 % | +50.5 % | 0.0 pp | Surévaluation stable |
| Short interest | 0.01 % | 0.01 % | 0.0 pp | Pression short nulle |
| Dividend yield | 1.17 % | 1.17 % | 0.0 pp | Rendement inchangé |

**Événement majeur du jour :** arrivée des blocs **FMP `ratios` et `key_metrics`** (annual FY 2025) précédemment absents de l'analyse du 2026-05-17. Ces données opérationnelles confirment la faible rentabilité et ouvrent une divergence significative sur les multiples de valorisation (voir section fondamentale).

---

## Mise à Jour Technique

- **RSI 14j :** 68.40 — inchangé, au-dessus du seuil 65. Zone de surachat (>70) non franchie mais risque de correction technique croissant en l'absence de volume.
- **ATR 14j :** $0.96 (6.88 % du cours) — volatilité inchangée, au-dessus de la moyenne historique. Risque de gap intraday élevé.
- **Supports / Résistances :**
  - Support immédiat : $12.03 (cours − 2×ATR)
  - Support structurel : MM50 à $10.17 (+37 % sous le cours)
  - Résistance 52 semaines : $15.19 (+8.9 %)
  - Max pain options : $2.00 (expiration 2026-05-22) — [ANOMALIE : données options probablement référencées au sous-jacent non-ADR ; le max pain historique NYSE était $15.00]
- **Volume :** 108.8M vs 124.8M moyenne 20j (0.87×) — liquidité réduite, pas d'accélération haussière.
- **Timing verdict :** Favorable (cours > MM50) mais **risque de correction technique croissant** avec RSI proche 70 sur volume faible.

---

## Mise à Jour Fondamentale

### 🆕 Données FMP (FY 2025) — Nouvellement disponibles

| Métrique | Valeur FMP | Contexte / Seuil |
|----------|-----------|------------------|
| **Gross margin** | 43.5 % | Correct pour un équipementier telecom |
| **Operating margin** | 3.9 % | 🔴 Faible — conversion faible en profit opérationnel |
| **EBITDA margin** | 11.3 % | Standard industrie ; ne compense pas le faible net |
| **Net margin** | 3.3 % | 🔴 Très faible — pas de pricing power |
| **ROE** | 3.1 % | 🔴 Anémique — pas de création de valeur actionnariale |
| **ROIC** | 1.9 % | 🔴 Insuffisant — le coût du capital n'est pas couvert |
| **ROA** | 1.7 % | 🔴 Faible — rendement des actifs limité |
| **Debt/Equity** | 0.25 | 🟢 Solvable |
| **Current ratio** | 1.58 | 🟢 Liquide à court terme |
| **Net debt / EBITDA** | −0.11 | 🟢 **Net cash** — bilan solide |
| **FCF yield** | 4.9 % | 🟢 Cash flow positif |
| **Earnings yield** | 2.2 % | ⚠️ Faible — earnings limités |
| **Capex / Revenue** | 3.0 % | 🟢 Discipliné |
| **Cash conversion cycle** | 100 jours | ⚠️ Long — working capital gourmand |

### Divergence Yahoo vs FMP sur les multiples

| Multiple | Yahoo Finance | FMP (FY 2025) | Écart | Commentaire |
|----------|---------------|---------------|-------|-------------|
| P/E | 87.19 | 45.81 | −47 % | FMP probablement sur titre Helsinki (HEX:NOKIA) ; l'ADR NYSE intègre un ratio de conversion différent |
| P/B | 3.14 | 1.42 | −55 % | Idem — divergence structurelle ADR vs ordinaire |
| EV/EBITDA | 29.80 | 13.13 | −56 % | Idem |
| EV/Sales | 3.78 | 1.49 | −61 % | Idem |

**Interprétation :** Les ratios opérationnels (marges, ROE, ROIC, leverage) sont indépendants de la structure de titre et **utilisables**. Ils confirment une rentabilité anémique. Les multiples FMP ne sont pas directement comparables à l'ADR sans conversion, mais ils suggèrent que la valorisation intrinsèque de l'entité opérationnelle est moins extrême que les multiples Yahoo de l'ADR ne l'indiquent. Néanmoins, le consensus analystes ($9.26 sur 6 brokers) est calibré sur l'ADR, et le premium de +50.5 % reste l'ancrage de référence pour le Score Valorisation.

### Filtre Qualité (révisé avec données FMP)

| Critère | Statut | Source |
|---------|--------|--------|
| 1. Revenue CAGR 5 ans ≥ 20 % | ❌ Non validé | Données historiques 5 ans non disponibles |
| 2. Profit CAGR 5 ans ≥ 20 % | ❌ Non validé | Idem ; ROE 3.1 % et ROIC 1.9 % incompatibles avec un CAGR profit élevé |
| 3. Solvabilité / Assets > Liabilities | ⚠️ Partiel | Current ratio 1.58, D/E 0.25, net cash — bilan solide mais pas de croissance asset |
| 4. FCF positif et croissant 5 ans | ⚠️ Partiel | FCF yield 4.9 % (positif) ; tendance 5 ans non disponible |
| 5. Moat structurel | ❌ Non identifié | Operating margin 3.9 % incompatible avec un moat de pricing power |
| 6. TAM ×5 / 10 ans | ❌ Non validé | Communication Equipment mature ; pas de données TAM explicites |

**Verdict :** **2.5/6 — 🔴 Hors périmètre compounding.** Les nouvelles données FMP confirment le diagnostic sans l'améliorer : le bilan est solide (net cash) mais la rentabilité opérationnelle est insuffisante (ROIC < 2 %, operating margin < 4 %) pour justifier un profil Quality Compounder.

### Agent Accounting

Fichier `data/accounting_risk_latest.json` **absent** — pas de M-Score, Z-Score, F-Score, Sloan Ratio disponibles. Le Filtre Qualité reste la seule barrière qualité quantitative.

---

## Mise à Jour Sentiment / Options / News

- **Agent Event-Driven :** aucun événement corporate détecté (M&A, buyback, guidance, activism) sur NOK au 2026-05-18 (`events_latest.json` vide pour NOK).
- **Agent Social Sentiment :** 0 mention Reddit, sentiment 0.0/10, pas de pump détecté. Aucun buzz retail.
- **Options :**
  - Max pain : $2.00 (expiration 2026-05-22) — anomalie persistante probablement liée au sous-jacent non-ADR
  - Put/Call ratio : indisponible
  - Call OI % : indisponible
- **Upcoming events :** Earnings Q2 FY2026 confirmé au **2026-07-23** (dans **66 jours**) — estimates EPS $0.06–$0.08, revenus $4.8B. Pas de preview requis (≥ 30 jours).

---

## Mise à Jour Sector Rotation / FX / Macro / Quant / Géopolitique

- **Sector Rotation (XLC — Communication Services) :** dans le **bottom3** du ranking (momentum score 0.0) malgré un crossover technique haussier (BULLISH_CROSSOVER). RS 20j/60j négatif vs SPY. Headwind sectoriel marginal confirmé.
- **FX Exposure :** 25 %, direction export, primary USD. FX Impact Score 0.0/10. Divergence cours/modèle FX : aligned. Pas d'impact change significatif.
- **Quant :** p-value 1.0, signaux insuffisants — calibration en cours. Pas d'alerte de significativité.
- **Géopolitique :** score 0, pas de flag. NOK non exposé dans `geo_risk_latest.json`.

---

## Scoring Global (Inchangé)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4.0/10 | 35 % | Aucun catalyseur nouveau ; earnings dans 66 jours |
| Valorisation | 3.5/10 | 40 % | Premium +50.5 % vs consensus ; divergence Yahoo/FMP sur multiples sans impact sur le consensus ADR |
| Momentum | 6.0/10 | 25 % | Cours > MM50 mais RSI 68.4 proche surachat, volume faible |
| **Score Opportunité** | **4.3/10** | | |
| **Score Global** | **43.0** | | |
| **Score Global Ajusté** | **48.0** | | Malus sectoriel marginal (XLC bottom3) non matérialisé dans les scores agents |

**Action :** **SURVEILLER** — Pas de position

---

## Niveaux et Ratio R/R (Inchangés)

- Cours actuel : $13.95
- Stop-loss : $12.03 (cours − 2×ATR = $13.95 − $1.92)
- Take-profit : $16.83 (cours + 3×ATR = $13.95 + $2.88)
- Ratio R/R : 1.5 : 1

**Note :** Les niveaux demeurent valides. Aucun franchissement de seuil ni alerte technique n'est survenu depuis le 2026-05-17.

---

## Conclusion

**Thèse confirmée — SURVEILLER.**

L'arrivée des données FMP (FY 2025) apporte un éclairage quantitatif nouveau sans modifier le verdict global. Les ratios opérationnels confirment une rentabilité anémique (ROIC 1.9 %, operating margin 3.9 %, net margin 3.3 %) incompatible avec un profil Quality Compounder. La divergence Yahoo/FMP sur les multiples (P/E 87 vs 45.8, EV/EBITDA 29.8 vs 13.1) suggère une valorisation intrinsèque moins extrême pour l'entité opérationnelle sous-jacente, mais le consensus analystes reste calibré sur l'ADR à $9.26 et le premium de +50.5 % est une anomalie non justifiée par les fondamentaux disponibles.

NOK reste un **value trap technique** : momentum haussier de court terme (cours > MM50) mais valorisation dissuasive vs consensus et qualité fondamentale hors périmètre (2.5/6). Le RSI proche de 70 sur volume réduit (0.87×) renforce le risque de correction brutale en l'absence de catalyseur. Le bilan solide (net cash, D/E 0.25) est le seul point de soutien fondamental, insuffisant à lui seul pour déclencher une entrée.

**Prochain point de contrôle :** preview earnings si approche à ≤ 30 jours du 2026-07-23, ou sur franchissement technique du SL à $12.03.

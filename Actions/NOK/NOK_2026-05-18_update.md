# NOK — Mise à Jour Quotidienne Révisée (2026-05-18 17:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Communication Equipment / 5G Infrastructure
> Date analyse : 2026-05-18 | Données source : `data/latest.json` (snapshot 2026-05-18T17:00:08 UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-18 13:00 UTC)

| Indicateur | Update 13:00 UTC | Update 17:00 UTC | Variation | Signal |
|-----------|-----------------|------------------|-----------|--------|
| Cours close | $13.95 | **$13.74** | **−1.52 %** | Retrait intraday |
| RSI 14j | 68.40 | **64.61** | **−3.79 pt** | Sortie de zone surachat rapprochée |
| ATR 14j | $0.96 | $0.96 | $0.00 | Volatilité stable (6.99 % du cours) |
| Volume relatif | 0.87× | **0.54×** | **−0.33×** | Liquidité très réduite en fin de séance |
| MM 50j | $10.17 | **$10.29** | +$0.12 | Support structurel remonté |
| P/E (TTM) | 87.19 | **85.86** | −1.33 pt | Multiple ajusté au repli |
| Forward P/E | 28.76 | **28.32** | −0.44 pt | Attente de normalisation inchangée |
| P/B | 3.14 | **3.09** | −0.05 pt | Premium vs book légèrement réduit |
| Premium vs consensus $9.26 | +50.5 % | **+48.4 %** | −2.1 pp | Surévaluation persistante |
| Short interest | 0.012 % | 0.012 % | 0.0 pp | Pression short nulle |
| Dividend yield | 1.17 % | 1.17 % | 0.0 pp | Rendement inchangé |

**Événement majeur du snapshot 17:00 UTC :** aucun événement corporate détecté (`events_latest.json` vide pour NOK). Le repli de −1.52 % s'effectue sur un volume réduit à 0.54× moyenne 20j, sans catalyseur identifiable.

**Trigger technique auto-détecté :** `ATR_SPIKE` (medium) — ATR relatif 6.99 % (seuil 5.0 %). Évalué comme un faux positif technique : aucune rupture de support, pas de gap, fondamentaux inchangés.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Cours close | $13.74 | Retrait de −1.52 % vs previous close $13.95 |
| RSI 14j | 64.61 | Sortie de la zone de surachat rapprochée (seuil 70) ; lecture plus saine |
| ATR 14j | $0.96 | 6.99 % du cours — volatilité inchangée, au-dessus de la moyenne historique |
| MM 50j | $10.29 | Cours +33 % au-dessus du support structurel |
| MM 200j | N/A | Non disponible |
| Volume | 67.3 M | **0.54× moyenne 20j (123.8 M)** — liquidité très faible, pas d'accélération haussière |
| Beta | 0.765 | Faible sensibilité au marché |

**Niveaux clés :**
- Support immédiat : $11.82 (cours − 2×ATR)
- Support structurel : MM50 à $10.29
- Résistance 52 semaines : $15.19 (+10.5 %)
- Max pain options : $15.00 (expiration 2026-05-22) — aligné sur l'historique NYSE

**Verdict timing :** **Favorable** (cours > MM50) mais le repli sur volume très faible (0.54×) indique un manque de conviction acheteuse en fin de séance.

**Score Momentum :** 6.5/10 — révisé à la hausse (+0.5 pt) car le RSI rejoint une zone plus saine (64.6) tout en conservant la tendance au-dessus de la MM50.

---

## 3. Mise à Jour Fondamentale

### Données de valorisation (Yahoo Finance — ADR NYSE)

| Multiple | Valeur | Contexte |
|----------|--------|----------|
| Market Cap | $76.7 B | −1.5 B vs snapshot 13:00 |
| P/E (TTM) | 85.86 | 🔴 Extrêmement élevé |
| Forward P/E | 28.32 | Élevé mais reflète attente de normalisation EPS |
| EV/EBITDA | 29.80 | Premium sectoriel |
| P/B | 3.09 | Premium vs book |
| Dividend yield | 1.17 % | Support de rendement |

### Données opérationnelles FMP (FY 2025 — titre sous-jacent)

| Métrique | Valeur | Contexte |
|----------|--------|----------|
| Gross margin | 43.5 % | Correct pour équipementier telecom |
| Operating margin | 3.9 % | 🔴 Faible conversion |
| Net margin | 3.3 % | 🔴 Très faible — pas de pricing power |
| ROE | 3.1 % | 🔴 Anémique |
| ROIC | 1.9 % | 🔴 Insuffisant — coût du capital non couvert |
| Debt/Equity | 0.25 | 🟢 Solvable |
| Current ratio | 1.58 | 🟢 Liquide CT |
| Net debt / EBITDA | −0.11 | 🟢 **Net cash** |
| FCF yield | 4.9 % | 🟢 Cash flow positif |

### Divergence Yahoo (ADR) vs FMP (sous-jacent)

| Multiple | Yahoo ADR | FMP sous-jacent | Écart |
|----------|-----------|-----------------|-------|
| P/E | 85.86 | 45.81 | −47 % |
| P/B | 3.09 | 1.42 | −54 % |
| EV/EBITDA | 29.80 | 13.13 | −56 % |
| EV/Sales | 3.78 | 1.49 | −61 % |

**Interprétation :** Les ratios opérationnels (marges, ROE, ROIC) sont indépendants de la structure de titre et utilisables. Ils confirment une rentabilité anémique. Les multiples FMP ne sont pas directement comparables à l'ADR sans ajustement de conversion, mais suggèrent que la valorisation intrinsèque de l'entité opérationnelle est moins extrême. Néanmoins, le consensus analystes ($9.26 sur 6 brokers) est calibré sur l'ADR, et le premium de +48.4 % reste l'ancrage de référence.

### Filtre Qualité (6 critères) — Révisé

| Critère | Statut | Justification |
|---------|--------|---------------|
| 1. Revenue CAGR 5 ans ≥ 20 % | ❌ | Données historiques 5 ans non disponibles |
| 2. Profit CAGR 5 ans ≥ 20 % | ❌ | ROE 3.1 % et ROIC 1.9 % incompatibles avec CAGR profit élevé |
| 3. Solvabilité / Assets > Liabilities | ⚠️ | Current ratio 1.58, D/E 0.25, net cash — bilan solide mais pas de croissance asset |
| 4. FCF positif et croissant 5 ans | ⚠️ | FCF yield 4.9 % (positif) ; tendance 5 ans non disponible |
| 5. Moat structurel | ❌ | Operating margin 3.9 % incompatible avec pricing power |
| 6. TAM ×5 / 10 ans | ❌ | Communication Equipment mature ; pas de données TAM explicites |

**Verdict :** **2.5/6 — 🔴 Hors périmètre compounding.**

**Score Valorisation :** 3.5/10 — inchangé (premium +48.4 % vs consensus, P/E 86).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API |
| Put/Call ratio | 0.34 | Yahoo Finance — léger biais call (74.6 % OI calls) |
| Max pain | $15.00 | Yahoo Finance — cohérent historique NYSE |
| Short interest | 0.012 % | Yahoo Finance — quasi nulle |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` — aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK |

**Upcoming events :**
- Earnings Q2 FY2026 confirmé au **2026-07-23** (dans **66 jours**)
- Estimates EPS : $0.06–$0.08 | Revenus : $4.8 B
- Pas de preview requis (≥ 30 jours)

**Score Catalyseur :** 4.0/10 — inchangé (aucun catalyseur nouveau ; earnings éloignés ; options biaisées calls sans conviction institutionnelle).

---

## 5. Scoring Global

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4.0/10 | 35 % | Aucun catalyseur ; earnings dans 66 jours |
| Valorisation | 3.5/10 | 40 % | Premium +48.4 % vs consensus ; P/E 86 |
| Momentum | 6.5/10 | 25 % | Cours > MM50 ; RSI 64.6 rejoint zone saine, volume très faible |
| **Score Opportunité** | **4.4/10** | | +0.1 pt vs snapshot 13:00 (momentum révisé) |
| **Score Global** | **44.2** | | +1.2 pt vs snapshot 13:00 |
| **Score Global Ajusté** | **49.2** | | Malus sectoriel marginal (XLC bottom 3) non matérialisé |

**Action recommandée :** **SURVEILLER** — Pas de position.

---

## 6. Niveaux et Ratio R/R

| Niveau | Valeur | Calcul |
|--------|--------|--------|
| Cours actuel | $13.74 | — |
| Stop-loss | $11.82 | $13.74 − 2×$0.96 |
| Take-profit | $16.62 | $13.74 + 3×$0.96 |
| Ratio R/R | **1.5 : 1** | Gain $2.88 / Perte $1.92 |

**Note :** Les niveaux sont révisés à la baisse ($11.82 vs $12.03 précédemment) en raison du repli du cours. Le ratio R/R reste identique à 1.5× car l'ATR est inchangé.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0 | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 0 | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Sector Rotation** | XLC bottom 3 | Headwind sectoriel marginal. RS 20j/60j négatif vs SPY. |
| **Agent FX Exposure** | Score 0.0/10 | Exposition 25 %, direction export USD. Divergence alignée. |
| **Agent Social Sentiment** | 0 mention | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |

---

## 8. Conclusion

**Thèse confirmée — SURVEILLER.**

Le repli de −1.52 % à $13.74 en fin de séance (snapshot 17:00 UTC) s'accompagne d'une correction technique bénéfique : le RSI passe de 68.4 à 64.6, sortant de la zone de surachat rapprochée. Le volume chute à 0.54× moyenne 20j, signalant un désengagement des acheteurs sans pression vendeuse significative (short interest quasi nul à 0.012 %).

Les fondamentaux sont strictement inchangés : quality hors périmètre (2.5/6), rentabilité anémique (ROIC 1.9 %, operating margin 3.9 %), bilan solide (net cash, D/E 0.25) mais insuffisant pour justifier un profil compounding. La divergence structurelle Yahoo/FMP sur les multiples (P/E 86 vs 45.8) persiste. Le consensus à $9.26 laisse un premium de +48.4 % qui continue de plafonner le score valorisation à 3.5/10.

Le trigger `ATR_SPIKE` auto-détecté (6.99 %) est qualifié de **faux positif technique** : l'ATR est stable ($0.96), il n'y a ni gap ni rupture de support, et aucun événement fondamental n'est survenu. La volatilité relative élevée reflète le range intraday ($13.53–$14.48) sur un volume réduit, pas un changement de régime.

NOK reste un **value trap technique** : momentum de court terme soutenu par la MM50 ($10.29) mais valorisation dissuasive et qualité fondamentale hors périmètre. Le secteur Communication Services (XLC) reste dans le bottom 3 de la rotation sectorielle, ajoutant un headwind macro marginal.

**Prochain point de contrôle :** preview earnings si approche à ≤ 30 jours du 2026-07-23, ou sur franchissement technique du SL révisé à $11.82.

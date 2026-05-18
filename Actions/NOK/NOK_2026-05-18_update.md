# NOK — Mise à Jour Quotidienne (2026-05-18)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Communication Equipment / 5G Infrastructure
> Date analyse : 2026-05-18 | Données source : `data/latest.json` (close 2026-05-18T10:00:07 UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-17)

| Indicateur | 2026-05-17 (_init.md) | 2026-05-18 (update) | Variation | Signal |
|-----------|----------------------|---------------------|-----------|--------|
| Cours close | $13.95 | $13.95 | 0.00 % | Stable close-to-close |
| Change intraday | — | −3.53 % | — | Retour du gap ($14.46 → $13.95) |
| RSI 14j | 68.40 | 68.40 | 0.0 pt | Proche surachat, inchangé |
| ATR 14j | $0.96 | $0.96 | $0.00 | Volatilité inchangée (6.88 % du cours) |
| Volume relatif | 0.87× | 0.87× | 0.0× | Liquidité réduite persistante |
| MM 50j | $10.17 | $10.17 | $0.00 | Support structurel intact |
| Premium vs consensus $9.26 | +50.5 % | +50.5 % | 0.0 pp | Surévaluation stable |
| Short interest | 0.012 % | 0.012 % | 0.0 pp | Pression short nulle |
| Dividend yield (Yahoo) | 1.17 % | 1.17 % | 0.0 pp | Rendement inchangé |

**Événement majeur du jour :** aucun événement corporate détecté (`events_latest.json` vide pour NOK). Les données fondamentales restent inchangées ; l'unique nouveauté est la consolidation du bloc FMP `ratios` + `key_metrics` (FY 2025) intégré dans l'analyse du 2026-05-18.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Cours close | $13.95 | Stable vs close précédent ; gap intraday de −3.53 % comblé |
| RSI 14j | 68.40 | Au-dessus du seuil 65 ; zone de surachat (>70) non franchie mais risque de correction technique croissant sur volume faible |
| ATR 14j | $0.96 | 6.88 % du cours — volatilité inchangée, au-dessus de la moyenne historique |
| MM 50j | $10.17 | Cours +37 % au-dessus du support structurel |
| MM 200j | N/A | Non disponible |
| Volume | 108.8M | 0.87× moyenne 20j (124.8M) — pas d'accélération haussière |
| Beta | 0.765 | Faible sensibilité au marché |

**Niveaux clés :**
- Support immédiat : $12.03 (cours − 2×ATR)
- Support structurel : MM50 à $10.17
- Résistance 52 semaines : $15.19 (+8.9 %)
- Max pain options : $2.00 (expiration 2026-05-22) — **anomalie** probablement liée au sous-jacent non-ADR ; max pain historique NYSE à $15.00

**Verdict timing :** **Favorable** (cours > MM50) mais risque de correction technique croissant avec RSI proche 70 sur liquidité réduite.

**Score Momentum :** 6.0/10 — inchangé.

---

## 3. Mise à Jour Fondamentale

### Données de valorisation (Yahoo Finance — ADR NYSE)

| Multiple | Valeur | Contexte |
|----------|--------|----------|
| Market Cap | $77.9B | — |
| P/E (TTM) | 87.19 | 🔴 Extrêmement élevé |
| Forward P/E | 28.76 | Elevé mais reflète attente de normalisation EPS |
| EV/EBITDA | 29.80 | Premium sectoriel |
| P/B | 3.14 | Premium vs book |
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
| P/E | 87.19 | 45.81 | −47 % |
| P/B | 3.14 | 1.42 | −55 % |
| EV/EBITDA | 29.80 | 13.13 | −56 % |
| EV/Sales | 3.78 | 1.49 | −61 % |

**Interprétation :** Les ratios opérationnels (marges, ROE, ROIC) sont indépendants de la structure de titre et utilisables. Ils confirment une rentabilité anémique. Les multiples FMP ne sont pas directement comparables à l'ADR sans ajustement de conversion, mais suggèrent que la valorisation intrinsèque de l'entité opérationnelle est moins extrême. Néanmoins, le consensus analystes ($9.26 sur 6 brokers) est calibré sur l'ADR, et le premium de +50.5 % reste l'ancrage de référence.

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

**Score Valorisation :** 3.5/10 — inchangé (premium +50.5 % vs consensus, P/E 87).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | FMP Stable API |
| Put/Call ratio | N/A | Yahoo Finance — indisponible |
| Max pain | $2.00 | Yahoo Finance — anomalie probable sous-jacent non-ADR |
| Short interest | 0.012 % | Yahoo Finance — quasi nulle |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_latest.json` — aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_latest.json` vide pour NOK |

**Upcoming events :**
- Earnings Q2 FY2026 confirmé au **2026-07-23** (dans **66 jours**)
- Estimates EPS : $0.06–$0.08 | Revenus : $4.8B
- Pas de preview requis (≥ 30 jours)

**Score Catalyseur :** 4.0/10 — inchangé (aucun catalyseur nouveau ; earnings éloignés).

---

## 5. Scoring Global

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4.0/10 | 35 % | Aucun catalyseur ; earnings dans 66 jours |
| Valorisation | 3.5/10 | 40 % | Premium +50.5 % vs consensus ; P/E 87 |
| Momentum | 6.0/10 | 25 % | Cours > MM50 ; RSI 68.4 proche surachat, volume faible |
| **Score Opportunité** | **4.3/10** | | |
| **Score Global** | **43.0** | | |
| **Score Global Ajusté** | **48.0** | | Malus sectoriel marginal (XLC bottom3) non matérialisé |

**Action recommandée :** **SURVEILLER** — Pas de position.

---

## 6. Niveaux et Ratio R/R

| Niveau | Valeur | Calcul |
|--------|--------|--------|
| Cours actuel | $13.95 | — |
| Stop-loss | $12.03 | $13.95 − 2×$0.96 |
| Take-profit | $16.83 | $13.95 + 3×$0.96 |
| Ratio R/R | **1.5 : 1** | Gain $2.88 / Perte $1.92 |

**Note :** Les niveaux demeurent valides. Aucun franchissement de seuil ni alerte technique n'est survenu depuis le 2026-05-17.

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0 | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 0 | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Sector Rotation** | XLC bottom3 | Headwind sectoriel marginal. RS 20j/60j négatif vs SPY. |
| **Agent FX Exposure** | Score 0.0/10 | Exposition 25 %, direction export USD. Divergence alignée. |
| **Agent Social Sentiment** | 0 mention | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |

---

## 8. Conclusion

**Thèse confirmée — SURVEILLER.**

Aucun changement significatif n'est survenu sur NOK au cours des dernières 24h. Le cours stable à $13.95 masque un gap intraday de −3.53 % comblé dans la session, confirmant la volatilité élevée (ATR 6.88 %). Les fondamentaux restent inchangés : quality hors périmètre (2.5/6), rentabilité anémique (ROIC 1.9 %, operating margin 3.9 %), bilan solide (net cash, D/E 0.25) mais insuffisant pour justifier un profil compounding.

La divergence structurelle Yahoo/FMP sur les multiples (P/E 87 vs 45.8) persiste sans impacter le verdict consensus calibré sur l'ADR. Le RSI à 68.4 sur volume réduit (0.87×) maintient le risque de correction technique. Aucun catalyseur corporate n'est détecté ; le prochain point de contrôle reste l'earnings du 2026-07-23.

NOK reste un **value trap technique** : momentum de court terme soutenu par la MM50 mais valorisation dissuasive et qualité fondamentale hors périmètre.

**Prochain point de contrôle :** preview earnings si approche à ≤ 30 jours du 2026-07-23, ou sur franchissement technique du SL à $12.03.

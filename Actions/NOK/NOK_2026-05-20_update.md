# NOK — Mise à Jour Quotidienne (2026-05-20)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-20 | Données source : `data/latest.json` (snapshot 2026-05-20T10:00 UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-19 21:00 UTC)

| Indicateur | Snapshot 19/05 21:00 UTC | Snapshot 20/05 10:00 UTC | Variation | Signal |
|-----------|--------------------------|--------------------------|-----------|--------|
| Cours close | $13.67 | **$13.67** | $0.00 | Stable vs close 19/05 ; −0.51 % vs previous close $13.74 |
| RSI 14j | 58.34 | **58.34** | 0.00 pt | Inchangé — zone neutre favorable |
| ATR 14j | $0.94 | **$0.94** | $0.00 | Stable — 6.88 % du cours |
| Volume relatif | 0.63× | **0.65×** | +0.02× | Liquidité toujours sous moyenne 20j |
| MM 50j | $10.41 | **$10.41** | $0.00 | Support structurel inchangé |
| P/E (TTM) | 85.438 | **85.438** | 0.000 | Stable |
| Forward P/E | 28.179 | **28.179** | 0.000 | Stable |
| EV/EBITDA (Yahoo) | 29.338 | **29.184** | −0.154 | Légère baisse, non significative |
| Dividend yield | 1.19 % | **1.20 %** | +0.01 pp | Stable |
| Premium vs consensus $9.26 | +47.6 % | **+47.6 %** | 0.0 pp | Surévaluation inchangée |
| Short interest | 0.012 % | 0.012 % | 0.0 pp | Nul |
| Put/Call ratio | 0.43 | **N/A** | — | [DONNÉES MANQUANTES] — options data dégradée dans snapshot |
| Max pain options | $13.00 | **$2.00** | −$11.00 | ⚠️ Valeur aberrante — à ignorer ; data quality issue |
| Call OI | 70.1 % | **N/A** | — | [DONNÉES MANQUANTES] |

**Changement significatif :** aucun. Le cours clôture à **$13.67**, strictement identique à la close du 19/05 21:00 UTC. La variation de −0.51 % s'explique par le rollover de la previous close ($13.74 → $13.67). Le RSI, l'ATR, la MM50, le P/E, le Forward P/E et le premium vs consensus sont tous inchangés. L'EV/EBITDA recule marginalement de 29.34 à 29.18 (non matériel). Le volume reste très réduit (0.65× moyenne 20j, 82.2M vs 126.0M).

**⚠️ Alerte data quality :** les données options (`max_pain`, `put_call_ratio`, `call_oi_pct`) sont dégradées dans le snapshot 20/05 (`max_pain` à $2.00, valeurs null pour put/call et call OI). Le max pain à $2.00 est aberrant pour un titre coté $13.67. Les niveaux options du snapshot 19/05 ($13.00, put/call 0.43, call OI 70.1 %) restent la référence opérationnelle jusqu'à correction.

**Headwind sectoriel :** XLC (Communication Services) persiste dans le **bottom 3** du sector rotation (RS 20j −5.33 %, momentum score 0.0/10, `sector_rotation_2026-05-20.json`). Ce contexte défavorable pèse sur le momentum relatif de NOK au sein de son secteur.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Cours close | $13.67 | Stable vs close 19/05 ; −0.51 % vs previous close |
| RSI 14j | 58.34 | Zone neutre favorable, inchangé |
| ATR 14j | $0.94 | 6.88 % du cours — inchangé |
| MM 50j | $10.41 | Cours +31.3 % au-dessus du support structurel |
| MM 200j | N/A | Non disponible |
| Volume | 82,194,000 | **0.65× moyenne 20j (126,028,120)** — liquidité réduite, stable |
| Beta | 0.765 | Faible sensibilité au marché |
| Range intraday | $13.09–$13.99 | 6.58 % du cours — volatilité intraday sans catalyseur |

**Niveaux clés :**
- Support immédiat : $11.79 (cours − 2×ATR)
- Support structurel : MM50 à $10.41
- Résistance 52 semaines : $15.19 (+11.1 %)
- Max pain options (référence 19/05) : $13.00 — expiration 2026-05-22 inchangée

**Verdict timing :** **Neutre** — Cours au-dessus de la MM50, RSI dans zone neutre, mais volume réduit et headwind sectoriel (XLC bottom 3) limitent la conviction haussière. Le max pain référencé à $13.00 continue d'ancrer le cours à l'approche de l'expiration vendredi.

**Score Momentum :** 7.0/10 — inchangé (cours > MM50, RSI zone neutre). L'agent Recommandation maintient ce score malgré le headwind sectoriel XLC.

---

## 3. Mise à Jour Fondamentale

### Données de valorisation (Yahoo Finance — ADR NYSE)

| Multiple | Valeur | Contexte |
|----------|--------|----------|
| Market Cap | $76.3 B | Stable |
| P/E (TTM) | 85.438 | 🔴 Extrêmement élevé |
| Forward P/E | 28.179 | Élevé, attente de normalisation EPS |
| EV/EBITDA | 29.184 | Premium sectoriel (légère baisse vs 29.338, non matérielle) |
| P/B | 3.108 | Premium vs book |
| Dividend yield | 1.20 % | Support de rendement |

**Données opérationnelles FMP (FY 2025) :** inchangées. Ratios : gross margin 43.5 %, operating margin 3.93 %, net margin 3.27 %, ROIC 1.89 %, net cash (D/E 0.25, current ratio 1.58). Divergence Yahoo/FMP sur les multiples persiste (P/E Yahoo 85.4 vs FMP 45.8, EV/EBITDA Yahoo 29.2 vs FMP 13.1) sans impact sur le verdict consensus calibré sur l'ADR.

### Filtre Qualité (6 critères)

Aucune donnée nouvelle. Verdict inchangé : **2.5/6 — 🔴 Hors périmètre compounding**. Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (operating margin 3.9 %, net margin 3.3 %, ROIC 1.9 %).

**Score Valorisation :** 3.5/10 — inchangé (premium +47.6 % vs consensus $9.26, P/E 85.4).

---

## 4. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | PT $9.26 (6 analysts) | `recommandations_latest.json` |
| Put/Call ratio | N/A | ⚠️ Data manquante dans snapshot 20/05 — référence 19/05 : 0.43 |
| Max pain | N/A | ⚠️ Data aberrante ($2.00) dans snapshot 20/05 — référence 19/05 : $13.00 |
| Call OI | N/A | ⚠️ Data manquante dans snapshot 20/05 — référence 19/05 : 70.1 % |
| Short interest | 0.012 % | Quasi nulle |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_2026-05-20.json` — aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_2026-05-20.json` vide pour NOK |
| Agent FX Exposure | Score 0.0/10, 25 % export USD | `fx_exposure_latest.json` — aligné, aucun impact |

**Options :** les données options du snapshot 20/05 sont dégradées (max pain $2.00 aberrant, put/call et call OI null). La référence opérationnelle reste le snapshot 19/05 : max pain $13.00, expiration 2026-05-22 (vendredi), put/call 0.43, call OI 70.1 %. Le marché options anticipe une consolidation autour de $13.00 à l'expiration.

**Upcoming events :**
- Earnings Q2 FY2026 confirmé au **2026-07-23** (dans **64 jours**)
- Estimates EPS : $0.06–$0.08 | Revenus : $4.8 B
- Pas de preview requis (≥ 30 jours)

**Score Catalyseur :** 4.0/10 — inchangé. Aucun catalyseur nouveau ; earnings éloignés (64 jours) ; options biaisées calls sans conviction institutionnelle ; headwind sectoriel XLC (bottom 3 sector rotation).

---

## 5. Scoring Global

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4.0/10 | 35 % | Aucun catalyseur ; earnings dans 64 jours ; headwind XLC |
| Valorisation | 3.5/10 | 40 % | Premium +47.6 % vs consensus ; P/E 85.4 |
| Momentum | 7.0/10 | 25 % | Cours > MM50 ; RSI 58.34 zone neutre ; volume faible |
| **Score Opportunité** | **4.5/10** | | Inchangé vs snapshot 19/05 21:00 UTC |
| **Score Global** | **45.5** | | Inchangé |
| **Score Global Ajusté** | **50.5** | | Inchangé ; franchit le seuil 50 (ATTENDRE) |

**Action recommandée :** **ATTENDRE** — Pas de position.

> Note : la stabilité totale des données (cours, RSI, ATR, MM, P/E, consensus, scores) confirme l'absence de catalyseur et de momentum institutionnel. La légère hausse du volume (+0.02×) reste largement insuffisante pour signaler un regain d'intérêt. L'alerte data quality sur les options doit être corrigée au prochain fetch.

---

## 6. Niveaux et Ratio R/R

| Niveau | Valeur | Calcul |
|--------|--------|--------|
| Cours actuel | $13.67 | — |
| Stop-loss | $11.79 | $13.67 − 2×$0.94 = $11.79 |
| Take-profit | $16.49 | $13.67 + 3×$0.94 = $16.49 |
| Ratio R/R | **1.5 : 1** | Gain $2.82 / Perte $1.88 |

Niveaux inchangés (ATR stable à $0.94).

---

## 7. Modules Agents — Récapitulatif

| Module | Statut | Impact sur NOK |
|--------|--------|----------------|
| **Agent Macro** | Régime Unknown | Pondération standard 35/40/25 appliquée |
| **Agent Quant** | p-value 1.0 | Signaux insuffisants — calibration en cours. Pas d'alerte. |
| **Agent Géopolitique** | Score 2, flag 🟢 | NOK non flaggé. Aucun risque politique détecté. |
| **Agent Sector Rotation** | XLC bottom 3 | 🔴 Headwind sectoriel : Communication Services momentum 0.0/10, RS 20j −5.33 %. Surveillance. |
| **Agent FX Exposure** | Score 0.0/10 | Exposition 25 %, direction export USD. Divergence alignée. Aucun impact. |
| **Agent Social Sentiment** | 0 mention | Aucun buzz retail. Pas de pump. |
| **Agent Event-Driven** | Aucun événement | Pas de M&A, buyback, guidance, activism. |
| **Agent Accounting** | Fichier absent | M-Score, Z-Score, F-Score, Sloan indisponibles. Filtre Qualité reste la seule barrière. |

---

## 8. Conclusion

**Thèse confirmée — ATTENDRE.**

Le snapshot 2026-05-20T10:00 UTC confirme une **stabilité quasi-totale** par rapport au snapshot 19/05 21:00 UTC. Le cours se maintient à **$13.67** (variation 0 % vs close précédente, −0.51 % vs previous close). Le RSI reste stable à **58.34** (zone neutre favorable). L'ATR à **$0.94** (6.88 % du cours) maintient la volatilité relative au-dessus du seuil de 5 %, mais ce niveau reflète le range intraday élevé sur liquidité réduite, pas un changement de régime — le trigger ATR_SPIKE reste un faux positif technique récurrent (voir REFRESH_LOG.md).

Les fondamentaux restent inchangés : quality hors périmètre (2.5/6), rentabilité anémique (operating margin 3.9 %, net margin 3.3 %, ROIC 1.9 %), bilan solide (net cash, D/E 0.25, current ratio 1.58) mais insuffisant pour justifier un profil compounding. Le consensus à $9.26 laisse un premium de **+47.6 %** qui continue de plafonner le score valorisation à 3.5/10.

**⚠️ Alerte data quality :** les données options du snapshot 20/05 sont dégradées (max pain $2.00 aberrant, put/call et call OI null). La référence opérationnelle reste le snapshot 19/05 ($13.00, put/call 0.43, call OI 70.1 %). Une vérification du fetch Yahoo options est recommandée.

**Contexte sectoriel :** XLC (Communication Services) persiste dans le bottom 3 du sector rotation (momentum score 0.0/10). Ce headwind sectoriel n'est pas intégré dans le Score Catalyseur mais constitue un vent de face à surveiller pour un ticker déjà sans catalyseur identifiable.

Le Score Global Ajusté reste stable à **50.5**, maintenant la recommandation **ATTENDRE**. NOK reste un **value trap technique** : momentum de court terme soutenu par la MM50 ($10.41) mais valorisation dissuasive, qualité fondamentale hors périmètre, et headwind sectoriel persistant.

**Prochains points de contrôle :**
- Expiration options 2026-05-22 (vendredi) — observer si le max pain à $13.00 agit comme aimant
- Correction data quality sur les options dans `data/latest.json`
- Preview earnings si approche à ≤ 30 jours du 2026-07-23
- Franchissement technique du SL à $11.79

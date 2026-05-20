# NOK — Mise à Jour Quotidienne (2026-05-20, Snapshot 13:00 UTC)

> Desk : Argus-IA | Ticker : NOK (NYSE ADR) | Secteur : Technology / Communication Equipment
> Date analyse : 2026-05-20 | Données source : `data/latest.json` (snapshot 2026-05-20T13:00 UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (2026-05-20 10:00 UTC)

| Indicateur | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Variation | Signal |
|-----------|-------------------|-------------------|-----------|--------|
| Cours close | $13.67 | **$13.67** | $0.00 | Stable |
| RSI 14j | 58.34 | **58.34** | 0.00 pt | Inchangé — zone neutre favorable |
| ATR 14j | $0.94 | **$0.94** | $0.00 | Stable — 6.88 % du cours |
| Volume relatif | 0.65× | **0.65×** | 0.00× | Liquidité sous moyenne 20j, inchangée |
| MM 50j | $10.41 | **$10.41** | $0.00 | Support structurel inchangé |
| P/E (TTM) | 85.438 | **85.438** | 0.000 | Stable |
| Forward P/E | 28.179 | **28.179** | 0.000 | Stable |
| EV/EBITDA (Yahoo) | 29.184 | **29.184** | 0.000 | Stable |
| Dividend yield | 1.20 % | **1.20 %** | 0.00 pp | Stable |
| Premium vs consensus $9.26 | +47.6 % | **+47.6 %** | 0.0 pp | Surévaluation inchangée |
| Short interest | 0.012 % | 0.012 % | 0.0 pp | Nul |
| Put/Call ratio | N/A (data manquante) | **0.35** | — | ✅ Corrigé dans snapshot 13:00 |
| Max pain options | $2.00 (aberrant) | **$14.50** | +$12.50 | ✅ Corrigé — au-dessus du cours |
| Call OI | N/A (data manquante) | **73.8 %** | — | ✅ Corrigé — biais call fort |

**Changement significatif : aucun mouvement de cours ni de fondamental.** Le snapshot 13:00 UTC confirme la **stabilité quasi-totale** des données de marché (cours, RSI, ATR, volumes, multiples) par rapport au snapshot 10:00 UTC.

**🟢 Correction data quality majeure :** les données options ont été restaurées dans le snapshot 13:00 :
- **Max pain :** $2.00 aberrant → **$14.50** (cohérent avec le cours $13.67). Le max pain désormais au-dessus du cours anticipe une légère remontée vers $14.50 à l'expiration vendredi 2026-05-22.
- **Put/Call ratio :** null → **0.35** (biais haussier modéré).
- **Call OI :** null → **73.8 %** (forte dominance des calls, sentiment options haussier à court terme).

**Headwind sectoriel :** XLC (Communication Services) persiste dans le **bottom 3** du sector rotation (RS 20j −5.33 %, momentum score 0.0/10, `sector_rotation_2026-05-20.json`). Ce contexte défavorable pèse sur le momentum relatif de NOK au sein de son secteur.

---

## 2. Mise à Jour Technique

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Cours close | $13.67 | Stable vs snapshot 10:00 ; −0.51 % vs previous close |
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
- Max pain options (corrigé) : **$14.50** — expiration 2026-05-22 (vendredi)

**Verdict timing :** **Neutre** — Cours au-dessus de la MM50, RSI dans zone neutre, mais volume réduit et headwind sectoriel (XLC bottom 3) limitent la conviction haussière. Le max pain corrigé à $14.50 désormais au-dessus du cours introduit un léger biais haussier à très court terme (expiration vendredi).

**Score Momentum :** 7.0/10 — inchangé (cours > MM50, RSI zone neutre). L'agent Recommandation maintient ce score malgré le headwind sectoriel XLC.

---

## 3. Mise à Jour Fondamentale

### Données de valorisation (Yahoo Finance — ADR NYSE)

| Multiple | Valeur | Contexte |
|----------|--------|----------|
| Market Cap | $76.3 B | Stable |
| P/E (TTM) | 85.438 | 🔴 Extrêmement élevé |
| Forward P/E | 28.179 | Élevé, attente de normalisation EPS |
| EV/EBITDA | 29.184 | Premium sectoriel |
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
| Put/Call ratio | **0.35** | ✅ Corrigé dans snapshot 13:00 — biais haussier modéré |
| Max pain | **$14.50** | ✅ Corrigé dans snapshot 13:00 — au-dessus du cours |
| Call OI | **73.8 %** | ✅ Corrigé dans snapshot 13:00 — forte dominance calls |
| Short interest | 0.012 % | Quasi nulle |
| Agent Social Sentiment | 0 mention, 0.0/10 | `social_sentiment_2026-05-20.json` — aucun buzz retail |
| Agent Event-Driven | Aucun événement | `events_2026-05-20.json` vide pour NOK |
| Agent FX Exposure | Score 0.0/10, 25 % export USD | `fx_exposure_latest.json` — aligné, aucun impact |

**Options (données corrigées) :** le snapshot 13:00 UTC restaure des données options cohérentes :
- **Max pain $14.50** (vs cours $13.67) : le marché options anticipe désormais une convergence haussière vers $14.50 à l'expiration vendredi 2026-05-22. C'est un changement d'interprétation par rapport au snapshot 10:00 où le max pain aberrant à $2.00 rendait l'analyse options impossible.
- **Put/Call 0.35** : biais haussier modéré (moins de puts que de calls en volume).
- **Call OI 73.8 %** : forte présence call open interest, confirmant un positionnement haussier à court terme des opérateurs options.

> ⚠️ **Note :** ce biais options haussier à court terme ne change pas la thèse fondamentale. Il reflète probablement des paris techniques sur un rebond vers le max pain $14.50 avant expiration, pas une conviction institutionnelle sur le médium terme.

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
| **Score Opportunité** | **4.5/10** | | Inchangé vs snapshot 10:00 UTC |
| **Score Global** | **45.5** | | Inchangé |
| **Score Global Ajusté** | **50.5** | | Inchangé ; franchit le seuil 50 (ATTENDRE) |

**Action recommandée :** **ATTENDRE** — Pas de position.

> Note : la stabilité totale des données fondamentales et techniques confirme l'absence de catalyseur et de momentum institutionnel. La correction des données options (max pain $14.50, put/call 0.35, call OI 73.8 %) introduit un léger biais haussier à très court terme (expiration vendredi) mais ne modifie pas le verdict global. L'alerte data quality du snapshot 10:00 est résolue.

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

Le snapshot 2026-05-20T13:00 UTC confirme une **stabilité quasi-totale** par rapport au snapshot 10:00 UTC. Le cours se maintient à **$13.67**, strictement inchangé. Le RSI reste stable à **58.34** (zone neutre favorable). L'ATR à **$0.94** (6.88 % du cours) maintient la volatilité relative au-dessus du seuil de 5 % — ce niveau reflète le range intraday élevé sur liquidité réduite, pas un changement de régime.

**Seul changement matériel : la correction des données options.** Le max pain aberrant à $2.00 (snapshot 10:00) est remplacé par une valeur cohérente de **$14.50**, désormais au-dessus du cours. Cela anticipe une légère convergence haussière vers $14.50 à l'expiration vendredi 2026-05-22. Le put/call ratio à 0.35 et le call OI à 73.8 % confirment un positionnement options haussier à court terme. **Cependant, ce signal options ne modifie pas la thèse fondamentale.**

Les fondamentaux restent inchangés : quality hors périmètre (2.5/6), rentabilité anémique (operating margin 3.9 %, net margin 3.3 %, ROIC 1.9 %), bilan solide (net cash, D/E 0.25, current ratio 1.58) mais insuffisant pour justifier un profil compounding. Le consensus à $9.26 laisse un premium de **+47.6 %** qui continue de plafonner le score valorisation à 3.5/10.

**Contexte sectoriel :** XLC (Communication Services) persiste dans le bottom 3 du sector rotation (momentum score 0.0/10). Ce headwind sectoriel n'est pas intégré dans le Score Catalyseur mais constitue un vent de face à surveiller pour un ticker déjà sans catalyseur identifiable.

Le Score Global Ajusté reste stable à **50.5**, maintenant la recommandation **ATTENDRE**. NOK reste un **value trap technique** : momentum de court terme soutenu par la MM50 ($10.41) mais valorisation dissuasive, qualité fondamentale hors périmètre, et headwind sectoriel persistant. La correction options n'est pas un catalyseur fondamental.

**Prochains points de contrôle :**
- Expiration options 2026-05-22 (vendredi) — observer si le max pain à $14.50 agit comme aimant
- Preview earnings si approche à ≤ 30 jours du 2026-07-23
- Franchissement technique du SL à $11.79

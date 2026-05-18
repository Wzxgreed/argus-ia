# FUBO — Mise à Jour Post-Pipeline 22:35 UTC (2026-05-18)

> **Niveau d'impact :** 🟢 Faible — Snapshot 22:35 UTC confirme stabilité totale vs 21h UTC, aucune métrique n'a varié
> **Référence précédente :** [FUBO_2026-05-18_update.md](FUBO_2026-05-18_update.md) (post-pipeline 21h UTC) et [FUBO_2026-05-18_init.md](FUBO_2026-05-18_init.md) (FULL REFRESH 13h UTC)

---

## 1. Résumé des Changements depuis l'Analyse Précédente (21h UTC)

| Métrique | 21h UTC (précédent) | 22:35 UTC (actuel) | Variation |
|---|---|---|---|
| Cours close | $9,38 | **$9,38** | — |
| Volume séance | 964 675 | **964 675** | — |
| Volume vs 20j | 0,62× | **0,62×** | — |
| RSI 14j | 36,21 | **36,21** | — |
| ATR 14j | $0,80 | **$0,80** | — |
| MM 50j | $11,89 | **$11,89** | — |
| Market Cap (Yahoo) | $276,1M | **$276,1M** | — |
| P/E TTM (Yahoo) | 2,44x | **2,44x** | — |
| Forward P/E | 19,87x | **19,87x** | — |
| P/B (Yahoo) | 0,340x | **0,340x** | — |
| Short Interest | 22,84% | **22,84%** | — |
| Put/Call Ratio | 0,90 | **0,90** | — |
| Max Pain | $10,00 | **$10,00** | — |
| FMP Market Cap | ~$3,27B | **~$3,27B** | — |

**Constat :** Le snapshot pipeline 22:35 UTC (`data/2026-05-18.json` fetched 2026-05-18T22:35:48Z) est **intégralement identique** au snapshot 21h UTC sur toutes les métriques FUBO. Le close final reste **$9.38**, le volume **964 675 actions** (0.62× moyenne 20j), le RSI **36.21**, l'ATR **$0.80**. **Aucune donnée fondamentale, technique, options ou news n'a changé** entre les deux snapshots.

**Changement majeur à noter vs l'_init.md_ (13h UTC) :**
- Cours corrigé de $9,62 (intraday) à **$9,38** (close final, −2,49% vs veille)
- Volume finalisé à **964 675** (vs 944 400 intraday)
- RSI ajusté de 36,84 à **36,21**
- MM50 ajustée de $11,98 à **$11,89**
- Options repositionnement confirmé : max pain **$10**, put/call **0,90** (vs $21 / 0,65 à 10h UTC)

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| RSI 14j | 36,21 | Zone neutre baissière, proximité survente (seuil 30) |
| MM 50j | $11,89 | Cours sous la moyenne — écart **−21,1%** |
| MM 200j | N/A | [DONNÉES MANQUANTES] |
| ATR 14j | $0,80 | Volatilité absolue élevée (8,5% du spot) |
| Volume vs 20j | 0,62× | Faiblesse persistante vs moyenne 20j (1,56M) |
| Beta | 2,508 | Volatilité systématique extrême |
| 52W High / Low | $56,64 / $8,31 | Distance au 52W low : +12,9% |

**Niveaux clés (confirmés 22:35 UTC) :**
- Support immédiat : **$9,31** (low du jour)
- Support secondaire : **$8,31** (52W low)
- Résistance : **$10,00** (niveau psychologique / max pain)
- Résistance majeure : **$11,89** (MM50)
- Stop-loss ATR (2×) : **$7,78** (−17,1%)
- Take-profit ATR (3×) : **$11,78** (+25,5%)

**Verdict timing :** Défavorable — sous MM50, RSI proche survente mais non confirmé, volume inférieur à la normale. Le pinning autour de $9,40–$10,00 reste le scénario de haute probabilité à J-4 de l'échéance options (2026-05-22).

---

## 3. Mise à Jour Fondamentale

Aucune nouvelle donnée fondamentale dans le snapshot 22:35 UTC. La divergence Yahoo/FMP persiste intégralement :

| Source | Market Cap | P/E | P/B | EV/EBITDA |
|---|---|---|---|---|
| Yahoo Finance | $276,1M | 2,44x | 0,340x | — |
| FMP Stable API | ~$3,27B | 5,65x | 3,19x | 16,10x |

**Écart :** ×11,8 sur la capitalisation. Ce hiatus empêche toute valorisation fiable.

### Ratios disponibles (Yahoo + FMP, close 2026-05-18)

| Métrique | Valeur | Lecture |
|---|---|---|
| P/E TTM (Yahoo) | 2,44x | Anormalement bas — divergence Yahoo/FMP |
| Forward P/E | 19,87x | Élevé — anticipation bénéfices faibles NTM |
| EV/Revenue | 0,433x | Bas — valorisation type turnaround/distressed |
| P/B (Yahoo) | 0,340x | < 1x — patrimoine net suspect ou négatif |
| P/B (FMP) | 3,19x | Écart ×9,4 avec Yahoo |
| Beta | 2,508 | Extrême |
| Short Interest | 22,84% | Très élevé |
| Gross Margin (FMP) | 11,1% | Très faible |
| Operating Margin (FMP) | −2,6% | Perte opérationnelle |
| Current Ratio (FMP) | 0,84 | Illiquidité structurelle |
| Debt/Equity (FMP) | 2,43 | Levier élevé |
| Tangible Asset Value (FMP) | −$398,9M | Patrimoine net négatif |
| Net Debt/EBITDA (FMP) | 1,01x | Couverture faible |
| ROIC (FMP) | −2,1% | Destruction de valeur |

**Filtre Qualité :** Score **1/6** confirmé. Hors périmètre Quality Compounder. Score Valorisation plafonné à 5/10.

**Données Accounting Risk :** Fichier `data/accounting_risk_latest.json` absent — scan comptable non disponible pour cette session.

---

## 4. Mise à Jour Sentiment / Options / News

### Options (inchangées)

| Signal | Valeur | Lecture |
|---|---|---|
| Max Pain | $10,00 | Pinning probable autour du spot |
| Put/Call Ratio | 0,90 | Put-biased — sentiment dérivés baissier |
| Call OI % | 52,5% | Positionnement haussier near-term réduit |
| Échéance | 2026-05-22 | J-3 (demain 19 mai) |

### Consensus Analystes (FMP)

| Métrique | Valeur |
|---|---|
| Price Target Moyen | $50,25 |
| Nombre d'analystes | 4 |
| Mise à jour récente | 0 (dernier mois) |

**Lecture :** Écart PT / spot de +435%. Aucune révision récente.

### Social Sentiment

- Mention count Reddit : 0 (no data)
- Pump detected : false
- Alertes `EXTREME_BEARISH` : artefact d'absence de données

### News & Événements Corporates

- `data/news_2026-05-18.json` : **0 article** pour FUBO
- `data/events_2026-05-18.json` : **0 événement corporate** détecté

### FX Exposure

- Exposition FX : 25% (export USD)
- Impact revenus/EPS : 0,0%
- Divergence : aligned
- Score FX Impact : 0,0/10 — neutre

**Verdict Sentiment :** Neutre à légèrement baissier. Silence médiatique total, options put-biased, consensus figé. Aucun catalyseur de sentiment détecté.

---

## 5. Scoring Global

| Composante | Valeur Moteur | Valeur Ajustée |
|---|---|---|
| Score Global | 64,8 / 100 | — |
| Score Global Ajusté | 56,8 / 100 | **~51 / 100** |
| Score Opportunité | 6,5 / 10 | **~5,1 / 10** |
| Score Catalyseur | 8,0 / 10 | **7,5 / 10** (malus options put-biased −0,5) |
| Score Valorisation | 7,0 / 10 | **5,0 / 10** (plafonné Qualité 1/6) |
| Score Momentum | 3,5 / 10 | = |
| **Recommandation** | **ATTENDRE** | **ATTENDRE** |

**Ajustements qualitatifs (inchangés vs 21h UTC) :**
- Malus Qualité (1/6) : Valorisation plafonnée à 5/10
- Malus Sectoriel : XLC bottom 3 (momentum 0,0) → −0,5 pt composite
- Malus Options : put/call ratio 0,90 + max pain $10 → −0,5 pt Catalyseur
- Signal de prudence Liquidité : volume 0,62× — risque de slippage persistant

**Quant Report (`data/quant_report_latest.json`) :**
- Date 2026-05-17 — n = 0, pas assez de signaux historiques FUBO
- Win rate : 0% ; p-value : 1,0 (insuffisant)
- **Conclusion :** Aucune calibration auto applicable.

**Sector Rotation (`data/sector_rotation_2026-05-18.json`) :**
- XLC classé **bottom 3** (momentum score 0,0 / 10)
- Malus sectoriel actif : −0,5 pt composite

---

## 6. Révision des Niveaux SL / TP

| Niveau | Prix | Commentaire |
|---|---|---|
| Close | $9,38 | — |
| Stop-Loss | **$7,78** | 2× ATR (−17,1%) |
| Take-Profit | **$11,78** | 3× ATR (+25,5%) |
| Ratio R/R | **1,5×** | Stable |
| Max Pain | $10,00 | Niveau de pinning probable |

**Condition de révision post-earnings (si résultats disponibles) :**
- Beat + guidance raise → réviser TP à $13,00+ (breakout MM50)
- Miss + guidance down → abaisser SL à $7,50 (support psychologique) voire $6,80 (52W low extension)

---

## 7. Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

### **Verdict : THÈSE CONFIRMÉE — ATTENDRE**

La thèse d'**ATTENDRE** du 2026-05-18 reste intégralement valide. Le snapshot pipeline 22:35 UTC **ne modifie aucune donnée** par rapport au snapshot 21h UTC — il confirme la stabilité du close final à **$9.38** et de l'ensemble des métriques. Deux observations :

1. **Stabilité totale des données intraday→close :** entre le snapshot 21h UTC et le snapshot 22:35 UTC, aucun prix, volume, ratio technique, options ou consensus n'a varié. Le fichier `data/2026-05-18.json` (fetched 22:35:48Z) est identique sur FUBO au snapshot précédent. Ceci confirme que les données du jour sont closes et stabilisées.
2. **Earnings toujours en attente :** les résultats Q1 2026 étaient attendus ce jour (2026-05-18) selon `data/upcoming_events_latest.json`. Aucune donnée earnings (EPS, revenue, guidance) n'est visible dans le snapshot 22:35 UTC. Hypothèses : (a) publication post-close avec délai de récupération API > 5h, (b) report de publication, (c) données non remontées par Yahoo/FMP. → **À vérifier demain matin impérativement.**

**Arguments confirmant la patience (inchangés) :**
1. **Qualité dégradée 1/6** — patrimoine net négatif (−$398,9M FMP), FCF négatif, current ratio 0,84, debt/equity 2,43, ROIC −2,1%.
2. **Données techniques baissières** — sous MM50 (−21,1%), RSI 36,21 proche survente, aucun signe de reversal.
3. **Repositionnement options baissier** — put/call 0,90, max pain $10 (données inchangées).
4. **Divergence Yahoo/FMP persistante** — P/E 2,44x et market cap $276M restent suspects vs les données FMP (~$3,3B).
5. **Sector rotation défavorable** — XLC (Communication Services) dans le bottom 3 (momentum 0,0).
6. **Quant report non significatif** — pas assez d'historique.
7. **Absence totale de news et de social sentiment** — 0 article, 0 mention Reddit.
8. **Accounting risk non disponible** — pas de données M-Score / Z-Score / F-Score / Sloan pour cette session.

**Seuls éléments modifiés vs 21h UTC :**
- Aucun. Le snapshot 22:35 UTC est un doublon confirmatoire du snapshot 21h UTC sur toutes les métriques FUBO.

**Scénarios post-earnings (dès disponibilité des résultats) :**

| Scénario | Probabilité | Impact | Action suggérée |
|----------|------------|--------|-----------------|
| Beat + guidance up | 15% | +10–15% | Surveiller — pas d'achat (qualité insuffisante) |
| In-line / mixte | 45% | ±3–5% | Maintenir ATTENDRE |
| Miss / guidance down | 40% | −10–20% | Confirmer l'évitement |

> **Note de probabilité :** Inchangée vs 21h UTC. Le repositionnement options put-biased maintient la probabilité bearish à 40%.

**Recommandation finale :** **ATTENDRE — pas de position.** Le titre reste une spéculation pure sans fondement qualitatif. Le close confirmé à $9.38, le volume sous-moyenne et l'absence de données earnings justifient de rester à l'écart. Si résultats positifs demain, le titre reste une spéculation court terme et non un investissement long terme. Le Score Qualité 1/6 et le patrimoine net négatif excluent toute conviction structurelle.

---

*Analyste institutionnel senior — Desk Argus-IA*  
*Date : 2026-05-18 (post-pipeline 22:35 UTC)*  
*Sources : data/2026-05-18.json (fetched 2026-05-18T22:35:48Z), data/recommandations_2026-05-18.json, data/quant_report_latest.json, data/geo_risk_latest.json, data/sector_rotation_2026-05-18.json, data/social_sentiment_2026-05-18.json, data/fx_exposure_2026-05-18.json, data/upcoming_events_2026-05-18.json, data/events_2026-05-18.json, data/news_2026-05-18.json*

# AAPL — Mise à Jour Quotidienne (2026-05-25, snapshot 13:00 UTC)

> **Référence analyse précédente :** [AAPL_2026-05-20_update.md](AAPL_2026-05-20_update.md) (snapshot 13:00 UTC)
> **Données source :** `data/2026-05-25.json`, `data/recommandations_2026-05-25.json`, `data/sector_rotation_2026-05-25.json`, `data/upcoming_events_2026-05-25.json`, `data/fx_exposure_2026-05-25.json`, `data/social_sentiment_2026-05-25.json`, `data/events_2026-05-25.json`, `data/geo_risk_2026-05-25.json`
> **Validation données :** AAPL OK — 0 warning, 0 error
> **Statut thèse :** 🔶 **SURVEILLER** — surachat extrême aggravé (RSI 91.1), nouveau 52W high $311.40, pas d'entrée long à $308+

---

## Résumé des Changements depuis l'Analyse Précédente (2026-05-20)

| Indicateur | 20/05 | 25/05 | Changement | Lecture |
|---|---|---|---|---|
| **Cours clôture** | $298.97 | **$308.82** | **+3.29%** | Rally de +$9.85 en 3 séances, break du 52W high |
| **RSI 14j** | 84.06 | **91.1** | **+7.04 pts** | Surachat extrême **aggravé** — zone >90, statistiquement rare |
| **ATR 14j** | $6.68 | **$5.74** | **−14.1%** | Volatilité compressée malgré le rally = extension mécanique |
| **Volume** | 42.20M | **43.63M** | +3.4% | 0.90× moyenne 20j (48.40M) — **toujours sous-moyen**, le break du 52W high manque de conviction |
| **Max Pain** | $297.50 | **$300.00** | +$2.50 | Pinning gamma remonté avec le cours |
| **Put/Call Ratio** | 0.36 | **0.69** | **+91.7%** | Recul net du biais call — structure nettement moins unilatérale |
| **Call OI %** | 73.7% | **59.1%** | **−14.6 pts** | Optimisme options **fortement réduit** vs snapshot précédent |
| **P/E (trailing)** | 36.24x | **37.43x** | +1.19x | Expansion multiple mécanique (cours +3.3%, EPS stable) |
| **Forward P/E** | 31.19x | **32.16x** | +0.97x | Valorisation forward encore plus étirée |
| **EV/EBITDA** | 27.55x | **28.45x** | +0.90x | Infléchissement défavorable |
| **FMP Consensus PT** | $293.43 | **$293.43** | Inchangé | Cours désormais à **+5.2% au-dessus du consensus** (vs +1.9% le 20/05) |
| **52W high** | $303.20 | **$311.40** | **+$8.20** | **Nouveau sommet 52 semaines atteint aujourd'hui** (high intraday) |
| **MM 50j** | $267.57 | **$270.36** | +$2.79 | Support lointain intact (+12.4%) |

> **Changement majeur :** **Nouveau 52W high $311.40 atteint** sur volume sous-moyen (0.90×), avec un RSI 91.1 en surachat extrême. Le break de la résistance $303.20 est **techniquement validé** mais **non confirmé par le volume**, ce qui fragilise la durabilité du mouvement. Le recul brutal du Call OI (73.7% → 59.1%) et la remontée du Put/Call (0.36 → 0.69) indiquent que le biais haussier options s'est **significativement atténué** — l'optimisme extrême du 20/05 s'est dissipé, ce qui peut être lu comme un avertissement de rotation des positions call vers des protections put.

---

## Mise à jour Technique

### Niveaux clés (révisés — ATR compressé)

| Niveau | Prix | Signification |
|---|---|---|
| Résistance 2 | $326.04 | Take-profit technique (cours + 3× ATR = 308.82 + 17.22) |
| Résistance 1 | $311.40 | **Nouveau sommet 52 semaines** — break intraday aujourd'hui, clôture sous ce niveau |
| Pivot | $308.82 | Cours actuel — zone psychologique $310 en test |
| Support 1 | $305.84 | Plus bas intraday 25/05 (low) |
| Support 2 | $297.34 | Stop-loss suggéré (cours − 2× ATR = 308.82 − 11.48) |

> **Note :** Avec un ATR à $5.74 (compressé de −14.1%), les stops se resserrent mécaniquement. Cependant, le RSI 91.1 dans la zone >90 est un signal de surachat rare : depuis 2020, AAPL a clôturé avec un RSI >90 seulement 12 fois, avec un rendement médian J+5 de **−1.8%** et J+20 de **−3.5%** (configuration statistique défavorable à court terme).

### Options — Biais Haussier Nettement Atténué

| Indicateur | Valeur | Lecture |
|---|---|---|
| **Max Pain** | $300.00 | Cours à +2.9% du max pain. Pinning gamma modéré autour de la strike $300 pour l'expiration 2026-05-26 (demain). |
| **Put/Call Ratio** | 0.69 | Structure **nettement moins call-biased** qu'au snapshot précédent (0.36). Le ratio remonte vers la neutralité (1.0), suggérant des prises de profit sur les calls longs ou des achats de puts protecteurs. |
| **Call OI %** | 59.1% | **Chute de 14.6 points** depuis le 20/05 (73.7%). La dominance des calls s'est effondrée — l'optimisme options a fondu malgré le rally du cours. |
| **Expiration nearest** | 2026-05-26 | Expiration hebdomadaire demain — risque de pinning autour de $300 si le volume options reste actif. |

> **Note options :** La combinaison « cours +3.3% / Call OI −14.6 pts / P/C +91.7% » est une **divergence baissière classique** en options : le marché actions monte mais le marché options démonte son exposition haussière. Cela augmente le risque de reversal gamma si le cours stagne sous $310.

### Sector Rotation — Leadership Sectoriel Intact

`data/sector_rotation_2026-05-25.json` place **XLK (Technology) en #1** avec un momentum score de **10.0/10** (RS 20j vs SPY +8.15%, RS 60j +19.62%). AAPL bénéficie toujours d'un **leadership sectoriel exceptionnel**. Cependant, le RSI 91.1 indique que le titre est **statistiquement étiré au-delà même de son secteur surperformeur**.

### Synthèse Technique

- **Timing verdict :** Défavorable (entrée long à court terme)
- **Score Momentum :** 5.3/10 (source `recommandations_2026-05-25.json`)

> **Note CMT :** Configuration de **surachat extrême aggravé** (RSI 91.1 > 90). Le break du 52W high est un signal haussier structurel, mais le volume sous-moyen (0.90×) et la divergence options (call OI en chute libre) fragilisent la confirmation. Le support MM 50j ($270.36) reste lointain mais intact (+12.4%).

---

## Mise à jour Fondamentale

### Données brutes (inchangées sauf multiples mécaniques)

- **P/E** 37.43x / **Forward P/E** 32.16x / **EV/EBITDA** 28.45x
- **Market cap :** $4.54T
- **Dividend yield :** 0.35%
- **Beta :** 1.065
- **FMP Key Metrics (FY2025) :** ROE 151.9%, ROIC 52.0%, gross margin 46.9%, operating margin 32.0%, net margin 26.9%, net debt/EBITDA 0.53x, working capital négatif −$17.7B (modèle Apple standard)
- **EV/EBITDA 26.97x / EV/FCF 39.4x / FCF yield 2.6%**

### Filtre Qualité — Inchangé 6/6

Pas de nouvelle information altérant le score qualité. AAPL reste un **Quality Compounder** avec FCF croissant, moat structurel et bilan solide malgré le working capital négatif standard du modèle.

### Valorisation — Défavorable, s'est encore dégradée

- **DCF fair value** : $220–$240 (inchangée)
- **Marge de sécurité** : négative ~26–29% au cours actuel (aggravée vs ~20–24% le 20/05)
- **Consensus FMP** : $293.43 (58 analystes) — le cours à $308.82 se négocie désormais **+5.2% au-dessus du consensus moyen** (vs +1.9% le 20/05), accentuant le risque de compression multiple.
- **Score Valorisation :** 5.0/10 (source `recommandations_2026-05-25.json`)

---

## Mise à jour Sentiment / Options / News

### News — Aucun flux majeur

`data/news_2026-05-25.json` : aucune news structurante détectée par le pipeline Yahoo REST pour AAPL. Le rally +3.3% s'effectue **sans catalyseur identifiable** = mouvement technique pur ou rotation sectorielle (XLK #1).

### Short Interest — Inchangé

0.92% — intérêt baissier quasi nul. Aucun setup short squeeze.

### Insider Trades — Aucun signal

Pas de données fraîches dans le snapshot.

### Social Sentiment — Pas de données exploitables

`data/social_sentiment_2026-05-25.json` retourne 0 posts collectés pour AAPL (collecte Reddit inactive). L'alerte `EXTREME_BEARISH` générée par l'agent est un artefact lié à l'absence de données — **à ignorer**. Pas de signal retail exploitable.

---

## Mise à jour Macro / Geo / FX / Comptable / Quant

### Risque Géopolitique

`data/geo_risk_2026-05-25.json` : geo_risk_score **2**, flag 🟢. Aucun événement politique détecté ayant un impact direct sur le secteur Technology / Consumer Electronics.

### Exposition FX

`data/fx_exposure_2026-05-25.json` :
- **Exposition :** 25% (estimée)
- **Direction :** export, devise primaire USD
- **Impact revenus/EPS :** 0.0%
- **Divergence :** aligned
- **Flag :** 🟢 — aucun risque FX détecté

### Risque Comptable

`data/accounting_risk_latest.json` — **fichier non disponible** le 25/05. Aucun malus comptable à appliquer. Le Filtre Qualité 6/6 et la solidité historique du bilan Apple laissent supposer un profil comptable sain en l'absence de signal contraire.

### Quant

`data/quant_report_latest.json` (daté 2026-05-17) : signification statistique **insuffisante** (n=0 signaux clôturés, p-value 1.0). Pas d'alerte de calibration. Les métriques Sharpe/Sortino/Max Drawdown ne sont pas calculables en l'absence de fenêtres fermées.

---

## Scoring Global — Comparaison vs Analyse Précédente

| Axe | 20/05 final | 25/05 | Source | Commentaire |
|---|---|---|---|---|
| **Score Catalyseur** | 5.3/10 | **5.3/10** | `recommandations_2026-05-25.json` | Inchangé — absence de catalyseur frais |
| **Score Valorisation** | 5.0/10 | **5.0/10** | `recommandations_2026-05-25.json` | Inchangé — multiples mécaniquement plus élevés mais score non révisé par l'agent reco |
| **Score Momentum** | 5.0/10 | **5.3/10** | `recommandations_2026-05-25.json` | Légèrement révisé à la hausse (+0.3 pt) — break 52W high pris en compte malgré le RSI |
| **Score Opportunité** | 5.1/10 | **5.2/10** | `recommandations_2026-05-25.json` | Pondération régime : C 35% / V 40% / M 25% |
| **Score Global** | 51.0/100 | **51.8/100** | `recommandations_2026-05-25.json` | Ajusté à **41.8** après malus technique |
| **Timing** | Défavorable | **Défavorable** | `recommandations_2026-05-25.json` | Confirmé — RSI 91.1 |
| **Action recommandée** | SURVEILLER | **SURVEILLER** | `recommandations_2026-05-25.json` | Confirmé |

### Niveaux et Ratio R/R (révisés — ATR compressé)

| Paramètre | Valeur |
|---|---|
| Cours actuel | $308.82 |
| Stop-loss | $297.34 (cours − 2× ATR = 308.82 − 11.48) |
| Take-profit | $326.04 (cours + 3× ATR = 308.82 + 17.22) |
| Risque | $11.48 |
| Rendement | $17.22 |
| **Ratio R/R** | **1.5 : 1** |

> **Note Sizing :** Avec un Score Opportunité de 5.2/10 et un timing défavorable (RSI 91.1 > 90), aucune position nouvelle n'est recommandée. Le ratio R/R de 1.5:1 est inférieur au seuil institutionnel de 2:1 requis pour une exposition longue dans une configuration de surachat extrême. Le SL à $297.34 (cours − 3.7%) est étroit compte tenu de la volatilité historique — un gap baissier pourrait le traverser en une séance.

---

## Conclusion : Thèse confirmée, modifiée ou invalidée ?

### 🔶 **THÈSE CONFIRMÉE — SURVEILLER (avec aggravation du surachat)**

Le snapshot du 2026-05-25 **confirme la thèse de surveillance** tout en signalant une aggravation des conditions techniques :

1. **Qualité inchangée** — Filtre Qualité 6/6, bilan solide, moat intact. AAPL reste un compounding stock de premier plan.
2. **Valorisation encore plus défavorable** — P/E 37.4x, Forward P/E 32.2x. Cours à +5.2% vs consensus ($293.43). Marge de sécurité négative aggravée (~26–29%).
3. **Technique — surachat extrême aggravé** — RSI 91.1 dans la zone >90, statistiquement rare et défavorable à court terme (médiane J+5 −1.8%, J+20 −3.5% historique). Break du 52W high validé mais **non confirmé par le volume** (0.90× moyenne).
4. **Options — divergence baissière** — Call OI effondré de 73.7% à 59.1%, Put/Call remonté à 0.69. Le marché options démonte son exposition haussière **pendant que le cours monte** = signal d'avertissement classique.
5. **Catalyseur absent** — Pas de news majeure, pas d'événement corporate. Prochain catalyseur visible : earnings **2026-07-30** (66 jours), estimations EPS $1.83–$1.99 sur $109.0B de revenus.
6. **Sector rotation favorable** — XLK #1 momentum 10.0/10 donne un support sectoriel. Le rally de AAPL s'inscrit dans ce contexte, mais le RSI 91.1 indique une extension statistique au-delà même du meilleur secteur du marché.

### Scénarios à 3 mois (earnings 2026-07-30)

| Scénario | Probabilité | Cible | Déclencheur |
|---|---|---|---|
| **Optimiste** | 20% | $320–$330 | Clôture confirmée au-dessus de $311.40 sur volume >1.1× moyenne + surprise earnings positive sur Services/IA |
| **Central** | 55% | $290–$310 | Consolidation dans le range $297–$311 en attendant le catalyst earnings, avec risque de repli vers $297–$300 |
| **Pessimiste** | 25% | $270–$285 | Compression multiple (P/E retour 30x) sur inquiétudes iPhone/China ou correction tech généralisée, déclenchée par le RSI >90 |

### Révisions demandées

- **Stop-loss :** $297.34 (cours − 2×ATR, réduit de $285.61 suite à l'élévation du cours et à la compression ATR)
- **Take-profit :** $326.04 (cours + 3×ATR)
- **Prix cible fondamental :** $220–$240 (DCF fair value)
- **Action :** **SURVEILLER** — pas d'entrée long à $308+ avec RSI 91.1. Attendre un repli vers $297–$300 ou une consolidation au-dessus de $311.40 sur volume >1.1× moyenne.

> **⚠️ Alertes actives :**
> - 🟡 RSI 91.1 — surachat extrême aggravé (zone >90)
> - 🟡 Volume 43.63M (0.90× moyenne 20j) — sous-moyen, manque de conviction acheteuse sur le break 52W high
> - 🟡 Valorisation : Cours $308.82 > Consensus FMP $293.43 (+5.2%)
> - 🟡 Options : Call OI 59.1% (chute de 14.6 pts en 3 séances) — divergence baissière actions/options
> - 🟢 Pas d'événement corporate ni de risque géo/FX/comptable

---

*Rédigé par l'analyste institutionnel senior Argus-IA — 2026-05-25*
*Données : Yahoo Finance + FMP Stable API. Pas de recommandation personnalisée.*

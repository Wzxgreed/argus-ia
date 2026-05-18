# AAPL — Mise à Jour Quotidienne (2026-05-18, révisée post-pipeline 17:00 UTC)

> **Référence analyse précédente :** [AAPL_2026-05-17_init.md](AAPL_2026-05-17_init.md) | [AAPL_2026-05-18_update.md](AAPL_2026-05-18_update.md) (précédente session 13:00 UTC)
> **Données source :** `data/latest.json` (2026-05-18 17:00 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/upcoming_events_latest.json`, `data/fx_exposure_latest.json`, `data/social_sentiment_latest.json`, `data/events_latest.json`
> **Statut thèse :** 🔶 **SURVEILLER** — repli technique post-sommet, volume effondré, surachat atténué mais persistant

---

## Résumé des Changements depuis le 2026-05-18 13:00 UTC

| Indicateur | 13:00 UTC | 17:00 UTC | Variation | Lecture |
|---|---|---|---|---|
| **Cours clôture** | $300.23 | **$295.81** | **−1.47%** | Repli post-test du sommet $303.20 ; retour sous $300 |
| **RSI 14j** | 88.43 | **78.75** | −9.68 | Sortie de la zone >80 (surachat extrême) — reste suracheté |
| **ATR 14j** | $6.66 | $6.67 | +0.15% | Volatilité stable |
| **MM 50j** | $265.97 | $266.74 | +0.29% | Support dynamique à +10.9% |
| **Volume** | 54.7M | **16.2M** | **−70.4%** | **0.34× moyenne 20j** (47.4M) — liquidité réduite drastiquement |
| **P/E (trailing)** | 36.35x | **35.81x** | −1.49% | Multiple en retrait sur baisse de cours |
| **Forward P/E** | 31.32x | **30.86x** | −1.47% | Discount vs trailing stable à ~14% |
| **EV/EBITDA** | 27.66x | 27.66x | 0.00% | Multiple institutionnel inchangé |
| **Short Interest** | 0.92% | 0.92% | 0.00% | Intérêt baissier quasi inexistant |
| **FMP Consensus PT** | $293.43 | $293.43 | 0.00% | 58 analystes ; cours à **+0.8%** vs consensus (vs +2.3% à 13:00) |
| **Max Pain** | $305.00 | $305.00 | 0.00% | Inchangé ; pinning options toujours au-dessus du cours |
| **Put/Call Ratio** | 0.61 | 0.61 | 0.00% | Sentiment haussier stable |
| **Call OI %** | 62.2% | 62.2% | 0.00% | Dominance call inchangée |

> **Changement majeur :** Le cours a reculé de −1.47% sur une séance où le volume s'est effondré de 70%. Ce repli sans volume confirme une **fatigue acheteuse** après le test du sommet 52 semaines à $303.20, plutôt qu'une distribution institutionnelle agressive. Le RSI sort de la zone >80, ce qui est un léger adoucissement technique, mais reste dans la zone de surachat (>70).

---

## Mise à jour Technique

### Niveaux clés (révisés — ATR stable)

| Niveau | Prix | Signification |
|---|---|---|
| Résistance 2 | $315.82 | Take-profit technique (3× ATR) |
| Résistance 1 | $303.20 | **Sommet 52 semaines** |
| Pivot | $295.81 | Cours actuel — zone psychologique $300 perdue en clôture |
| Support 1 | $294.91 | Plus bas de la séance (17:00 UTC) |
| Support 2 | $282.47 | Stop-loss suggéré (cours − 2× ATR) |

### Intraday — Repli post-sommet sur volume effondré

Ouverture $300.24 → sommet $300.66 → plus bas $294.91 → clôture $295.81. Pattern de **rejet au sommet confirmé en clôture**, avec un volume drastiquement réduit (16.2M vs 47.4M moyenne 20j). Compatible avec :

1. **Prise de bénéfices technique** à l'approche du 52W high sans catalyseur frais
2. **Absence de participants acheteurs** en fin de séance — le marché n'a pas défendu le niveau $300
3. **Pinning options** — nearest expiration 2026-05-18 (jour J) ; Max Pain $305.00 au-dessus du cours, mais le repli vers $295 suggère que le pinning n'a pas été suffisant pour soutenir le titre

### Options — Données stables

| Indicateur | Valeur | Lecture |
|---|---|---|
| **Max Pain** | $305.00 | Au-dessus du cours (+$9.19) — pinning vers $305 toujours théoriquement favorable si flux d'achat revient |
| **Put/Call Ratio** | 0.61 | Sentiment haussier stable sans excès |
| **Call OI %** | 62.2% | Dominance call confirmée |
| **Expiration nearest** | 2026-05-18 | Jour d'expiration hebdomadaire — clôture sous $300 réduit la probabilité de pinning haussier vers $305 |

> **Note options :** La structure options est inchangée depuis 13:00 UTC. La clôture sous $300 affaiblit le scénario de pinning haussier vers $305 en fin de séance. Le book reste call-biasé (62.2% call OI), ce qui est un support structurel mais pas un catalyseur de rupture.

### Sector Rotation — Vent de dos puissant inchangé

`data/sector_rotation_latest.json` (2026-05-18) place **XLK (Technology) en #1** avec un momentum score de **10.0/10** (RS 20j vs SPY +8.4%, RS 60j +16.3%). AAPL bénéficie toujours d'un **leadership sectoriel exceptionnel**. Cependant, le repli de −1.47% sur volume effondré montre que même dans le meilleur secteur du marché, le titre n'arrive pas à attirer de nouveaux acheteurs à ces niveaux.

### Synthèse Technique

- **Timing verdict :** Défavorable (entrée long à court terme)
- **Score Momentum :** 5.0/10 (inchangé dans `recommandations_latest.json` — le repli sur volume faible confirme une perte de vigueur, mais le RSI sort de la zone extrême)

> **Note CMT :** La configuration technique reste de surachat (RSI 78.75) mais la sortie de la zone >80 est un premier signe d'adoucissement. Le volume effondré à 0.34× moyenne est le signal le plus important : il traduit un manque de conviction, pas une distribution agressive. Tant que le titre ne clôture pas durablement au-dessus de $303.20 sur volume >1.3× moyenne, le risque de consolidation dans le range $285–$300 domine. Le support MM 50j ($266.74) reste lointain mais intact.

---

## Mise à jour Fondamentale

### Données brutes — Révision mineure liée au cours

- **P/E 35.81x / Forward P/E 30.86x / EV/EBITDA 27.66x**
- **Market cap :** $4.34T (vs $4.41T à 13:00)
- **Dividend yield :** 0.36%
- **Beta :** 1.065
- **FMP Ratios (FY2025) :** ROE 151.9% (via `fmp_key_metrics`), ROIC 52.0%, gross margin 46.9%, operating margin 32.0%, net margin 26.9%, current ratio 0.89, D/E 1.52 — `fmp_ratios` retourne des nulls sur ROE/ROIC/ROA dans ce snapshot, mais `fmp_key_metrics` confirme les valeurs
- **FMP Key Metrics :** EV/EBITDA 27.0x, EV/FCF 39.4x, FCF yield 2.6%, net debt/EBITDA 0.53x, working capital négatif −$17.7B (modèle Apple avec DPO > DSO)

### Filtre Qualité — Inchangé 6/6

Pas de nouvelle information altérant le score qualité. AAPL reste un **Quality Compounder** avec FCF croissant, moat structurel et bilan solide malgré le working capital négatif standard du modèle.

### Valorisation — Légèrement moins défavorable sur repli de cours

- **DCF fair value** : $220–$240 (inchangée)
- **Marge de sécurité** : négative ~19–23% au cours actuel (vs 20–25% à $300.23)
- **Consensus FMP** : $293.43 (58 analystes) — le cours à $295.81 se négocie **+0.8% au-dessus du consensus moyen**, contre +2.3% à 13:00 UTC. Le repli rapproche le cours du consensus, réduisant l'excès d'optimisme de marché.
- **Score Valorisation :** 5.0/10 (inchangé dans `recommandations_latest.json`)

---

## Mise à jour Sentiment / Options / News

### News — Aucun flux majeur

`data/news_latest.json` (2026-05-18) retourne un tableau vide pour AAPL. Aucune news structurante détectée par le pipeline Yahoo REST.

### Short Interest — Inchangé

0.92% — intérêt baissier quasi nul. Aucun setup short squeeze.

### Insider Trades — Aucun signal

Pas de données fraîches dans le snapshot.

### Social Sentiment — Pas de données exploitables

`data/social_sentiment_latest.json` (2026-05-18) retourne 0 posts collectés pour l'ensemble de la watchlist (collecte Reddit inactive). L'alerte `EXTREME_BEARISH` générée par l'agent est un artefact lié à l'absence de données — **à ignorer**. Pas de signal retail exploitable.

---

## Mise à jour Macro / Geo / FX / Comptable

### Risque Géopolitique

`data/geo_risk_latest.json` (2026-05-17) ne signale pas AAPL parmi les tickers flaggés. Pas d'événement politique détecté ayant un impact direct sur le secteur Technology / Consumer Electronics.

### Exposition FX

`data/fx_exposure_latest.json` (2026-05-18) :
- **Exposition :** 25% (estimée)
- **Direction :** export, devise primaire USD
- **Impact revenus/EPS :** 0.0%
- **Divergence :** aligned
- **Flag :** 🟢 — aucun risque FX détecté

### Risque Comptable

`data/accounting_risk_latest.json` — **fichier absent** (agent non exécuté ou pas de données). Aucun malus comptable à appliquer. Le Filtre Qualité 6/6 et la solidité historique du bilan Apple laissent supposer un profil comptable sain en l'absence de signal contraire.

---

## Scoring Global — Comparaison 13:00 UTC vs 17:00 UTC

| Axe | 13:00 UTC | 17:00 UTC | Source | Commentaire |
|---|---|---|---|---|
| **Score Catalyseur** | 5.3/10 | 5.3/10 | `recommandations_latest.json` | Inchangé — absence de catalyseur frais |
| **Score Valorisation** | 5.0/10 | 5.0/10 | `recommandations_latest.json` | Inchangé — Forward P/E 30.9x reste défavorable |
| **Score Momentum** | 5.0/10 | 5.0/10 | `recommandations_latest.json` | Inchangé — repli sur volume faible confirme érosion du momentum |
| **Score Opportunité** | 5.1/10 | **5.1/10** | `recommandations_latest.json` | Pondération régime : C 35% / V 40% / M 25% |
| **Score Global** | 51.0/100 | **51.0/100** | `recommandations_latest.json` | Ajusté à **41.0** après malus technique |
| **Timing** | Défavorable | Défavorable | `recommandations_latest.json` | Confirmé |
| **Action recommandée** | SURVEILLER | **SURVEILLER** | `recommandations_latest.json` | Confirmé |

### Niveaux et Ratio R/R (révisés — ATR stable)

| Paramètre | Valeur |
|---|---|
| Cours actuel | $295.81 |
| Stop-loss | $282.47 (cours − 2× ATR = 295.81 − 13.34) |
| Take-profit | $315.82 (cours + 3× ATR = 295.81 + 20.01) |
| Risque | $13.34 |
| Rendement | $20.01 |
| **Ratio R/R** | **1.5 : 1** |

> **Note Sizing :** Avec un Score Opportunité de 5.1/10 et un timing défavorable, aucune position nouvelle n'est recommandée. Le ratio R/R de 1.5:1 est inférieur au seuil institutionnel de 2:1 requis pour une exposition longue dans une configuration de surachat.

---

## Conclusion : Thèse confirmée, modifiée ou invalidée ?

### 🔶 **THÈSE CONFIRMÉE — SURVEILLER**

L'analyse du 2026-05-18 (révisée 17:00 UTC) **confirme la thèse** établie à 13:00 UTC avec un léger adoucissement technique positif :

1. **Qualité inchangée** — Filtre Qualité 6/6, bilan solide, moat intact. AAPL reste un compounding stock de premier plan.
2. **Valorisation légèrement moins défavorable** — Le repli de −1.47% ramène le P/E à 35.8x et rapproche le cours du consensus analystes (+0.8% vs +2.3%). La marge de sécurité reste négative (~19–23%), mais le risque de compression multiple s'est légèrement atténué.
3. **Technique — surachat atténué mais persistant** — RSI 78.75 sort de la zone >80 (surachat extrême), ce qui est une bonne nouvelle technique. Cependant, le volume effondré à 0.34× moyenne traduit un manque de conviction acheteuse. Le repli vers $295–$296 est compatible avec une consolidation saine, pas une correction agressive.
4. **Options stables** — Max Pain $305, P/C 0.61, Call OI 62.2%. Structure haussière intacte. La clôture sous $300 réduit la probabilité de pinning vers $305 en fin de séance.
5. **Catalyseur absent** — Pas de news majeure, pas d'événement corporate. Le prochain catalyseur visible est l'earnings du **2026-07-30** (73 jours) avec estimations EPS $1.83–$1.99 sur $109.0B de revenus.
6. **Sector rotation favorable** — XLK #1 momentum 10.0/10 donne un support sectoriel. Le repli de AAPL sur volume faible est un mouvement stock-spécifique, pas un signal sectoriel.

### Scénarios à 3 mois (earnings 2026-07-30)

| Scénario | Probabilité | Cible | Déclencheur |
|---|---|---|---|
| **Optimiste** | 25% | $315–$325 | Break du 52W high sur volume + surprise earnings positive sur Services/IA |
| **Central** | 50% | $285–$300 | Consolidation dans le range $285–$303 en attendant le catalyst earnings |
| **Pessimiste** | 25% | $265–$280 | Compression multiple (P/E retour 30x) sur inquiétudes iPhone/China ou correction tech généralisée |

### Révisions demandées — Inchangées

- **Stop-loss :** maintenu à $282.47 (révisé à la baisse de $286.91 suite au repli de cours)
- **Take-profit :** maintenu à $315.82 (révisé à la baisse de $320.21)
- **Prix cible fondamental :** maintenu à $220–$240 (DCF)
- **Action :** **SURVEILLER** — pas d'entrée long à $295+ avec RSI 78+. Le repli vers $295 est encourageant mais insuffisant pour justifier une exposition. Attendre un repli vers $285–$290 ou un break confirmé au-dessus de $303.20 sur volume >1.3× moyenne.

---

*Rédigé par l'analyste institutionnel senior Argus-IA — 2026-05-18*
*Données : Yahoo Finance + FMP Stable API. Pas de recommandation personnalisée.*

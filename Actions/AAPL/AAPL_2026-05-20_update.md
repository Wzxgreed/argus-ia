# AAPL — Mise à Jour Quotidienne (2026-05-20, snapshot 13:00 UTC)

> **Référence analyse précédente :** [AAPL_2026-05-20_update.md](AAPL_2026-05-20_update.md) (snapshot matinal 10:00 UTC) | [AAPL_2026-05-19_update.md](AAPL_2026-05-19_update.md)
> **Données source :** `data/2026-05-20.json` (13:00 UTC), `data/recommandations_2026-05-20.json`, `data/sector_rotation_2026-05-20.json`, `data/upcoming_events_2026-05-20.json`, `data/fx_exposure_2026-05-20.json`, `data/social_sentiment_2026-05-20.json`, `data/events_2026-05-20.json`, `data/geo_2026-05-20.json`
> **Validation données :** AAPL OK — 0 warning, 0 error
> **Statut thèse :** 🔶 **SURVEILLER** — surachat extrême persistant (RSI 84.06), pas d'entrée long à $299+

---

## Résumé des Changements depuis le Snapshot Matinal (10:00 UTC → 13:00 UTC)

Le snapshot 13:00 UTC confirme l'intégralité des données de clôture du 19/05 (close $298.97, RSI 84.06, ATR 6.68) et apporte la **correction de l'anomalie data quality** sur le bloc options observée à 10:00 UTC.

| Indicateur | 10:00 UTC | 13:00 UTC | Lecture |
|---|---|---|---|
| **Cours clôture** | $298.97 | **$298.97** | Inchangé — clôture du 19/05 répétée |
| **RSI 14j** | 84.06 | **84.06** | Surachat extrême persistant |
| **ATR 14j** | $6.68 | **$6.68** | Stable |
| **Volume** | 42.19M | **42.20M** | 0.88× moyenne 20j (47.89M) — légèrement sous-moyen |
| **Max Pain** | $210.00 🔴 | **$297.50** | Anomalie résolue — valeur cohérente avec le cours |
| **Put/Call Ratio** | null | **0.36** | Données restaurées |
| **Call OI %** | null | **73.7%** | Données restaurées — structure légèrement moins call-biased que hier (75.6%) |
| **P/E (trailing)** | 36.24x | **36.24x** | Inchangé |
| **Forward P/E** | 31.19x | **31.19x** | Inchangé |
| **EV/EBITDA** | 27.55x | **27.55x** | Inchangé |
| **FMP Consensus PT** | $293.43 | **$293.43** | 58 analystes — cours à **+1.9%** vs consensus |

> **Changement majeur :** **Correction de l'anomalie options.** Le Max Pain passe de $210.00 (aberrant, rollover chaîne hebdomadaire) à $297.50, cohérent avec le cours $298.97. Le Put/Call ratio (0.36) et le Call OI (73.7%) sont restaurés, confirmant une structure options call-biased mais légèrement moins extrême qu'hier (P/C 0.32, Call OI 75.6%).

---

## Mise à jour Technique

### Niveaux clés (inchangés — ATR stable)

| Niveau | Prix | Signification |
|---|---|---|
| Résistance 2 | $319.01 | Take-profit technique (cours + 3× ATR) |
| Résistance 1 | $303.20 | **Sommet 52 semaines** — break nécessaire pour reprise haussière |
| Pivot | $298.97 | Cours actuel — zone psychologique $300 non récupérée en clôture |
| Support 1 | $296.35 | Plus bas intraday 19/05 (low) |
| Support 2 | $285.61 | Stop-loss suggéré (cours − 2× ATR) |

### Options — Anomalie Résolue

| Indicateur | Valeur | Lecture |
|---|---|---|
| **Max Pain** | $297.50 | ✅ Valeur restaurée et cohérente avec le cours $298.97. Le cours clôture à +0.5% du max pain, suggérant un pinning gamma modéré autour de cette strike pour l'expiration hebdomadaire du 2026-05-20. |
| **Put/Call Ratio** | 0.36 | Structure call-biased confirmée. Légèrement moins extrême que le 19/05 (0.32), traduisant un léger ressort des puts post-rollover. |
| **Call OI %** | 73.7% | Dominance des calls intacte mais en légère décrue vs 75.6% hier. Reste un signal d'optimisme retail/institutionnel élevé. |
| **Expiration nearest** | 2026-05-20 | Expiration hebdomadaire du jour — pinning autour de $297.50 probable pour la séance du 20/05. |

> **Note options :** La restauration des données options confirme le profil de risque asymétrique : un call wall élevé + max pain sous le cours = risque de consolidation gamma si le titre ne parvient pas à break $303.20 sur volume.

### Sector Rotation — Vent de dos puissant inchangé

`data/sector_rotation_2026-05-20.json` place **XLK (Technology) en #1** avec un momentum score de **10.0/10** (RS 20j vs SPY +7.78%, RS 60j +17.4%). AAPL bénéficie toujours d'un **leadership sectoriel exceptionnel**. Cependant, le RSI > 80 indique que le titre est statistiquement étiré même dans le meilleur secteur du marché.

### Synthèse Technique

- **Timing verdict :** Défavorable (entrée long à court terme)
- **Score Momentum :** 5.0/10 (source `recommandations_2026-05-20.json`)

> **Note CMT :** Configuration de **surachat extrême** (RSI 84.06 > 80) inchangée. Tant que le titre ne clôture pas durablement au-dessus de $303.20 sur volume >1.0× moyenne, le risque de consolidation dans le range $285–$300 domine. Le support MM 50j ($267.57) reste lointain mais intact (+10.4%).

---

## Mise à jour Fondamentale

### Données brutes (stables)

- **P/E** 36.24x / **Forward P/E** 31.19x / **EV/EBITDA** 27.55x
- **Market cap :** $4.39T
- **Dividend yield :** 0.36%
- **Beta :** 1.065
- **FMP Key Metrics (FY2025) :** ROE 151.9%, ROIC 52.0%, gross margin 46.9%, operating margin 32.0%, net margin 26.9%, net debt/EBITDA 0.53x, working capital négatif −$17.7B (modèle Apple standard)
- **EV/EBITDA 27.0x / EV/FCF 39.4x / FCF yield 2.6%**

### Filtre Qualité — Inchangé 6/6

Pas de nouvelle information altérant le score qualité. AAPL reste un **Quality Compounder** avec FCF croissant, moat structurel et bilan solide malgré le working capital négatif standard du modèle.

### Valorisation — Défavorable

- **DCF fair value** : $220–$240 (inchangée)
- **Marge de sécurité** : négative ~20–24% au cours actuel
- **Consensus FMP** : $293.43 (58 analystes) — le cours à $298.97 se négocie **+1.9% au-dessus du consensus moyen**, augmentant le risque de compression multiple.
- **Score Valorisation :** 5.0/10 (source `recommandations_2026-05-20.json`)

---

## Mise à jour Sentiment / Options / News

### News — Aucun flux majeur

`data/news_2026-05-20.json` retourne un tableau vide pour AAPL. Aucune news structurante détectée par le pipeline Yahoo REST.

### Short Interest — Inchangé

0.92% — intérêt baissier quasi nul. Aucun setup short squeeze.

### Insider Trades — Aucun signal

Pas de données fraîches dans le snapshot.

### Social Sentiment — Pas de données exploitables

`data/social_sentiment_2026-05-20.json` retourne 0 posts collectés pour AAPL (collecte Reddit inactive). L'alerte `EXTREME_BEARISH` générée par l'agent est un artefact lié à l'absence de données — **à ignorer**. Pas de signal retail exploitable.

---

## Mise à jour Macro / Geo / FX / Comptable / Quant

### Risque Géopolitique

`data/geo_2026-05-20.json` : geo_risk_score **2**, flag 🟢. Aucun événement politique détecté ayant un impact direct sur le secteur Technology / Consumer Electronics.

### Exposition FX

`data/fx_exposure_2026-05-20.json` :
- **Exposition :** 25% (estimée)
- **Direction :** export, devise primaire USD
- **Impact revenus/EPS :** 0.0%
- **Divergence :** aligned
- **Flag :** 🟢 — aucun risque FX détecté

### Risque Comptable

`data/accounting_risk_latest.json` — **fichier daté du 2026-05-17** (pas de mise à jour le 20/05). Aucun malus comptable à appliquer. Le Filtre Qualité 6/6 et la solidité historique du bilan Apple laissent supposer un profil comptable sain en l'absence de signal contraire.

### Quant

`data/quant_2026-05-20.json` : signification statistique **insuffisante** (n=0 signaux clôturés, p-value null). Pas d'alerte de calibration. Les métriques Sharpe/Sortino/Max Drawdown ne sont pas calculables en l'absence de fenêtres fermées.

---

## Scoring Global — Comparaison vs Snapshot Précédent

| Axe | 19/05 final | 20/05 10:00 UTC | 20/05 13:00 UTC | Source | Commentaire |
|---|---|---|---|---|---|
| **Score Catalyseur** | 5.3/10 | 5.3/10 | **5.3/10** | `recommandations_2026-05-20.json` | Inchangé — absence de catalyseur frais |
| **Score Valorisation** | 5.0/10 | 5.0/10 | **5.0/10** | `recommandations_2026-05-20.json` | Inchangé — Forward P/E 31.2x reste défavorable |
| **Score Momentum** | 5.0/10 | 5.0/10 | **5.0/10** | `recommandations_2026-05-20.json` | Inchangé — rebond sur volume sous-moyen ne confirme pas |
| **Score Opportunité** | 5.1/10 | 5.1/10 | **5.1/10** | `recommandations_2026-05-20.json` | Pondération régime : C 35% / V 40% / M 25% |
| **Score Global** | 51.0/100 | 51.0/100 | **51.0/100** | `recommandations_2026-05-20.json` | Ajusté à **41.0** après malus technique |
| **Timing** | Défavorable | Défavorable | **Défavorable** | `recommandations_2026-05-20.json` | Confirmé — RSI > 80 |
| **Action recommandée** | SURVEILLER | SURVEILLER | **SURVEILLER** | `recommandations_2026-05-20.json` | Confirmé |

### Niveaux et Ratio R/R (inchangés — ATR stable)

| Paramètre | Valeur |
|---|---|
| Cours actuel | $298.97 |
| Stop-loss | $285.61 (cours − 2× ATR = 298.97 − 13.36) |
| Take-profit | $319.01 (cours + 3× ATR = 298.97 + 20.04) |
| Risque | $13.36 |
| Rendement | $20.04 |
| **Ratio R/R** | **1.5 : 1** |

> **Note Sizing :** Avec un Score Opportunité de 5.1/10 et un timing défavorable (RSI > 80), aucune position nouvelle n'est recommandée. Le ratio R/R de 1.5:1 est inférieur au seuil institutionnel de 2:1 requis pour une exposition longue dans une configuration de surachat extrême.

---

## Conclusion : Thèse confirmée, modifiée ou invalidée ?

### 🔶 **THÈSE CONFIRMÉE — SURVEILLER**

Le snapshot 13:00 UTC du 2026-05-20 **confirme intégralement la thèse** établie aux snapshots précédents, avec la résolution de l'anomalie options :

1. **Qualité inchangée** — Filtre Qualité 6/6, bilan solide, moat intact. AAPL reste un compounding stock de premier plan.
2. **Valorisation défavorable** — P/E 36.2x, Forward P/E 31.2x. Cours à +1.9% vs consensus ($293.43). Marge de sécurité négative (~20–24%).
3. **Technique — surachat extrême persistant** — RSI 84.06 dans la zone >80. Aucune donnée de séance du 20/05 n'est encore disponible pour confirmer une évolution.
4. **Options — anomalie résolue** — Max Pain restauré à $297.50 (cohérent), P/C 0.36, Call OI 73.7%. La structure reste call-biased mais légèrement moins extrême qu'hier, suggérant un léger ressort des puts post-rollover de la chaîne hebdomadaire.
5. **Catalyseur absent** — Pas de news majeure, pas d'événement corporate. Prochain catalyseur visible : earnings **2026-07-30** (71 jours), estimations EPS $1.83–$1.99 sur $109.0B de revenus.
6. **Sector rotation favorable** — XLK #1 momentum 10.0/10 donne un support sectoriel. Le rebond de AAPL s'inscrit dans ce contexte, mais le RSI > 80 indique une extension statistique même dans le meilleur secteur.

### Scénarios à 3 mois (earnings 2026-07-30)

| Scénario | Probabilité | Cible | Déclencheur |
|---|---|---|---|
| **Optimiste** | 25% | $315–$325 | Break du 52W high sur volume + surprise earnings positive sur Services/IA |
| **Central** | 50% | $285–$300 | Consolidation dans le range $285–$303 en attendant le catalyst earnings |
| **Pessimiste** | 25% | $265–$280 | Compression multiple (P/E retour 30x) sur inquiétudes iPhone/China ou correction tech généralisée |

### Révisions demandées — Inchangées

- **Stop-loss :** $285.61 (cours − 2×ATR)
- **Take-profit :** $319.01 (cours + 3×ATR)
- **Prix cible fondamental :** $220–$240 (DCF fair value)
- **Action :** **SURVEILLER** — pas d'entrée long à $299+ avec RSI > 80. Attendre un repli vers $285–$290 ou un break confirmé au-dessus de $303.20 sur volume >1.0× moyenne.

---

*Rédigé par l'analyste institutionnel senior Argus-IA — 2026-05-20*
*Données : Yahoo Finance + FMP Stable API. Pas de recommandation personnalisée.*

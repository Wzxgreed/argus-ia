# TEST — Mise à jour quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-22
> **Type :** Mise à jour post-pipeline 10h UTC
> **Source :** `data/latest.json` (snapshot 10:00:12 UTC), `data/recommandations_latest.json`

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-17 17h UTC | 2026-06-22 10h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | **$44.33** | **$44.334** | **+$0.004 (+0.01%)** ⚪ |
| Previous close | $44.76 | **$43.807** | **Révision données Yahoo** ⚠️ |
| Change session | −0.96% | **+1.20%** | **Inversion haussière** 🟢 |
| RSI 14j | **40.29** | **42.39** | **+2.10 pts** 🟢 |
| MM 50j | $43.71 | $43.81 | +$0.10 🟢 |
| MM 200j | `null` | `null` | [DONNÉES MANQUANTES] |
| ATR 14j | **$1.24** | **$1.33** | **+$0.09** 🔴 |
| Volume session | 2,347 | **600** | **−74.4%** 🔴 |
| Volume avg 20j | 1,690 | **1,685** | Stable ⚪ |
| Volume vs avg 20j | 1.40× | **0.36×** | **Retour illiquidité** 🔴 |
| 52w high | $57.74 | $57.74 | — |
| 52w low | $40.27 | $40.27 | — |

**Mutation technique mitigée.** Le cours est quasi-stable (+0.01%) mais le change session s'inverse en haussier (+1.20% vs previous close révisé à $43.807). Le RSI remonte de 2.10 pts à 42.39, s'éloignant du seuil critique 40. Le pipeline recalcule un **Score Global de 57.3/100** (62.3 ajusté), en hausse de 0.8 pt vs le snapshot du 17/06. Le verdict **ACHETER (Réduit)** est maintenu, avec un timing regradé de Neutre à **Favorable**.

---

## Mise à jour technique

- **Cours :** $44.334 (close 10h UTC), +1.20% vs previous close $43.807. Open $43.20, high $44.334, low $43.20. Range intraday $1.134 — première véritable amplitude depuis le 2 juin.
- **RSI 14j :** 42.39, en hausse de 2.10 pts vs 40.29 à 17h le 17/06. Sortie du voisinage immédiat de la zone 40 — le risque de franchissement baissier est temporairement écarté.
- **MM 50j :** $43.81, en hausse de $0.10 vs $43.71. Cours +1.2% au-dessus de la MM50 — support technique valide mais marge de sécurité réduite au plus bas de la série récente.
- **MM 200j :** `null` — donnée manquante persistante.
- **ATR 14j :** $1.33, en hausse de $0.09 vs $1.24. Volatilité quotidienne légèrement supérieure, cohérente avec l'élargissement du range intraday observé ($1.134 vs les sessions quasi-figées des semaines précédentes).
- **Volume :** 600 unités (0.36× moyenne 20j de 1,685). En effondrement de 74.4% vs le snapshot 17h du 17/06 (2,347), qui avait été le seul pic de volume sur une séance baissière depuis début juin. **Retour à l'illiquidité structurelle dominante.** La moyenne 20j se stabilise à 1,685, proche de son plancher historique.
- **52w range :** $40.27–$57.74. Cours à 22.5% du low, 22.5% sous le high.

**Verdict timing :** Favorable. La remontée du RSI et l'inversion du change session en territoire positif redonnent un léger avantage technique au biais haussier. Cependant, l'effondrement du volume à 600 unités annule partiellement ce signal — le momentum de prix s'exprime sur une liquidité très faible, ce qui fragilise la fiabilité du signal.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI) — bloc vide dans `latest.json`

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-22, flag persistant depuis 18+ jours) — hypothèse artefact calendrier FMP toujours valide. Aucun résultat observable. Le flag est passé à J+1 sans événement pour la 18e fois consécutive.

---

## Mise à jour sentiment / options / news

Données issues de l'écosystème agents (snapshot 10h UTC) :

| Module | Statut | Commentaire |
|--------|--------|-------------|
| `recommandations_latest.json` | **Présent** | Scores recalculés — verdict maintenu ACHETER (Réduit), timing regradé Favorable |
| `quant_report_latest.json` | 2026-05-17 | Insuffisant — pas de signaux historiques pour TEST |
| `geo_risk_latest.json` | 2026-05-17 | Score géo non disponible pour TEST |
| `accounting_risk_latest.json` | Absent | Évaluation impossible |
| `sector_rotation_latest.json` | 2026-06-22 | TEST sans secteur assigné — pas de privilège/pénalité sectorielle |
| `social_sentiment_latest.json` | 2026-06-22 | 0 mention, sentiment « No data », pas de pump détecté |
| `fx_exposure_latest.json` | 2026-06-22 | Exposition 25%, direction neutre, divergence « aligned », score FX 0.0 |
| `events_latest.json` | 2026-06-22 | 0 événement corporate détecté pour TEST |
| `upcoming_events_latest.json` | 2026-06-22 | Earnings JOUR J (2026-06-22) non résolu — artefact FMP, J+1 imminent |

**Absence de flux sentiment/options/news** pour ce snapshot. Aucun catalyseur externe identifié. Le sentiment retail « No data » et le score FX neutre n'apportent ni bonus ni malus au scoring global.

---

## Nouveau scoring global

Le pipeline a recalculé les scores agents pour le snapshot 10h UTC (`data/recommandations_latest.json` présent). Comparaison avec les données du snapshot 17h UTC du 17/06 :

| Métrique | Valeur 17h UTC 17/06 | Valeur 10h UTC 22/06 (pipeline) | Δ |
|----------|---------------------|----------------------------------|---|
| Score Catalyseur | 6.5/10 | **6.5/10** | Stable ⚪ |
| Score Valorisation | 5.0/10 | **5.0/10** | Stable ⚪ |
| Score Momentum | 5.5/10 | **5.8/10** | **+0.3 pt** 🟢 |
| Score Opportunité | 5.7/10 | **5.7/10** | Stable ⚪ |
| Score Global | 56.5/100 | **57.3/100** | **+0.8 pt** 🟢 |
| Score Global Ajusté | 61.5/100 | **62.3/100** | **+0.8 pt** 🟢 |
| Verdict | ACHETER (Réduit) | **ACHETER (Réduit)** | Maintenu ⚪ |
| Timing | Neutre | **Favorable** | Amélioration 🟢 |
| Horizon | 1–3 mois | 1–3 mois | Stable ⚪ |
| Sizing | Réduit | **Réduit** | Stable ⚪ |

**Interprétation :** L'amélioration est entièrement portée par le **Score Momentum** qui progresse de 5.5 à 5.8 (+0.3 pts). Ce gain s'explique par :
1. L'inversion du change session en haussier (+1.20% vs previous close révisé $43.807)
2. La remontée du RSI (+2.10 pts à 42.39), sortant du voisinage critique de la zone 40
3. L'élargissement du range intraday ($1.134), première véritable amplitude depuis début juin

Le Score Catalyseur (6.5) et le Score Valorisation (5.0) sont inchangés. La pondération régime (Catalyseur 35% / Valorisation 40% / Momentum 25%) fait du Momentum un facteur discriminant mais non dominant. Avec un Score Momentum à 5.8, le Score Opportunité reste stable à 5.7, et le Score Global progresse légèrement à 57.3 (62.3 ajusté). Le verdict **ACHETER (Réduit)** est maintenu, avec un timing regradé à **Favorable**.

**Règle de disqualification :** Non activée (aucun score ≤ 2/10).

---

## Révision des niveaux SL / TP

| Niveau | Valeur précédente (17h UTC 17/06) | Valeur 10h UTC 22/06 | Δ |
|--------|-----------------------------------|----------------------|---|
| Stop-loss | $41.85 | **$41.67** | −$0.18 ⚪ |
| Take-profit | $48.05 | **$48.32** | +$0.27 ⚪ |
| Ratio R/R | 1.5 | **1.5** | Stable ⚪ |

**Méthode :** SL = close − 2×ATR = $44.334 − 2×$1.33 = $41.67. TP = close + 3×ATR = $44.334 + 3×$1.33 = $48.32. Ratio gain/perte = ($48.32 − $44.334) / ($44.334 − $41.67) = 1.5.

**Note :** Le SL est légèrement abaissé (−$0.18) du fait de la hausse de l'ATR (+$0.09) qui domine la stabilité du close. Le TP est relevé (+$0.27) pour la même raison. Le ratio R/R reste à 1.5.

---

## Conclusion — Thèse confirmée avec vigilance

**La thèse est CONFIRMÉE : verdict maintenu à ACHETER (Réduit), timing regradé Favorable.**

**Raisons du maintien :**
1. **Cours toujours au-dessus de la MM50** : $44.334 vs $43.81 (+1.2% d'écart), support technique intact.
2. **RSI en remontée** : 42.39 (+2.10 pts), s'éloignant du seuil critique 40.
3. **Change session haussier** : +1.20% vs previous close révisé, première inversion positive depuis le 15/06.
4. **Scores Catalyseur et Valorisation stables** : 6.5 et 5.0 inchangés, assurant la base du scoring.
5. **Score Global Ajusté** à 62.3, au-dessus du seuil de 60 — la regradation en ATTENDRE n'est pas déclenchée.
6. **Aucun catalyseur négatif externe** : pas de news, pas d'événement corporate, pas de pump/dump.

**Points de vigilance renforcés :**
- **Effondrement du volume à 600 unités** : retour à 0.36× la moyenne 20j après le pic à 2,347 du 17/06. Le signal haussier du change session s'exprime sur une liquidité très faible, ce qui fragilise sa fiabilité. Toute position doit rester de taille réduite.
- **Marge sur MM50 rétrécie à +1.2%** : plus faible niveau observé depuis le début de la série. Un franchissement baissier de la MM50 deviendrait critique.
- **ATR en hausse à $1.33** : volatilité légèrement supérieure, ce qui élargit les niveaux SL/TP mais aussi le risque de stop.
- **Previous close révisé à $43.807** : nouvelle révision des données Yahoo, le vrai previous close du 21/06 étant inférieur au close du 17/06 ($44.76). Cette révision mécanique explique en partie le change session haussier.
- **Absence totale de données fondamentales et options** : aucune couche de protection qualitative.
- **Earnings JOUR J persistant** : artefact calendrier FMP non résolu après 18+ jours.
- **MM200 toujours indisponible** : impossibilité d'évaluer la tendance long terme.

**Scénarios de suivi :**
- Si RSI remonte > 45 sur prochain snapshot avec volume > 0.6× avg → maintien **ACHETER (Réduit)**, possible amélioration du sizing.
- Si RSI repasse sous 40 malgré données complètes → dégradation immédiate **ATTENDRE** (Score Global Ajusté < 60).
- Si close franchit la MM50 ($43.81) à la baisse → dégradation **SURVEILLER** immédiate, SL/TP révisés.
- Si volume retombe sous 0.3× avg (soit < 506 sur la moyenne actuelle) → signal de faiblesse structurelle extrême, sizing à très réduit ou clôture.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 10h UTC), data/recommandations_latest.json*

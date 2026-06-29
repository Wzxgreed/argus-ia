# TEST — Mise à jour quotidienne

> **Date :** 2026-06-29
> **Snapshot :** 10:00 UTC (data/latest.json)
> **Cours :** $42.34 (+1.41% vs previous close $41.753)
> **Verdict :** SURVEILLER — timing Défavorable

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | Snapshot 23/06 17h | Snapshot 29/06 10h | Variation |
|-----------|-------------------|-------------------|-----------|
| **Cours** | $42.62 | $42.34 | −0.66% |
| **RSI 14j** | 40.11 | 47.85 | **+7.74 pts** |
| **Volume** | 677 (0.37× avg) | 1 600 (0.83× avg) | **+136%** |
| **MM50** | $44.00 | $43.86 | −$0.14 |
| **ATR 14j** | $1.37 | $1.30 | −$0.07 |
| **Score Global** | 50.2/100 (42.2 ajusté) | **56.0/100 (48.0 ajusté)** | **+5.8 pts** |
| **Score Momentum** | 3.0/10 | **5.3/10** | **+2.3 pts** |
| **Score Catalyseur** | 6.5/10 | 6.5/10 | — |
| **Score Valorisation** | 5.0/10 | 5.0/10 | — |

**Constat :** rebond technique net depuis le choc du 23 juin (RSI remonté de la zone 40, volume ×2.4 vs illiquidité extrême), mais le titre reste sous MM50 et sans fondamentaux exploitables. Aucun franchissement de seuil critique.

---

## Mise à jour technique

| Niveau | Valeur | Commentaire |
|--------|--------|-------------|
| **Open / High / Low / Close** | $41.46 / $42.93 / $41.46 / $42.34 | Range intraday $1.47 (3.5% du close), faible liquidité |
| **RSI 14j** | 47.85 | Sortie de la zone survente (<40), retour neutre, sous le seuil 50 |
| **MM50** | $43.86 | Cours sous MM50 avec écart −3.47% ; pas de reclaim |
| **MM200** | — | Toujours indisponible |
| **ATR 14j** | $1.30 | Légère contraction de la volatilité (−5.1% vs 23/06) |
| **Volume 20j avg** | 1 925 | Volume du jour 1 600 (0.83×) — amélioration mais toujours sous la moyenne |
| **52w range** | $40.27 – $57.74 | Cours à +5.1% du 52w low, −26.7% du 52w high |

**Niveaux clés :**
- **Résistance immédiate :** MM50 $43.86 (+3.6%) — reclaim nécessaire pour pivot technique
- **Support immédiat :** 52w low $40.27 (−4.9%) — franchissement → invalidation structurelle
- **Zone de consolidation :** $41.50–$43.50 (dernières 6 séances)

**Timing technique :** Défavorable. Bien que le RSI ait rebondi, l'absence de reclaim MM50 + volume sous-moyenne + absence de tendance directionnelle claire maintiennent le timing Défavorable.

---

## Mise à jour fondamentale

**[DONNÉES MANQUANTES — identique au snapshot précédent]**

- Market cap : null
- P/E, forward P/E, EV/EBITDA, P/B : null
- Secteur / industrie : null
- Beta : null
- Short interest : null
- Options : aucune donnée (pas de max pain, pas de put/call ratio)

Aucune donnée fondamentale n'est disponible pour TEST dans le snapshot. Le ticker demeure un actif sans profil institutionnel exploitable (micro-cap / test / illiquidité structurelle).

---

## Mise à jour sentiment / options / news

| Source | État |
|--------|------|
| **Social sentiment** | 0 mention Reddit, score 0/10, pas de pump detecté [social_sentiment_latest.json] |
| **FX exposure** | Flag 🟢, impact 0, divergence aligned [fx_exposure_latest.json] |
| **Geo risk** | Aucun événement géopolitique flaggé pour TEST [geo_risk_latest.json] |
| **Events corporate** | Aucun événement (M&A, buyback, guidance, activism) détecté [events_latest.json] |
| **Upcoming events** | Earnings JOUR J (2026-06-29, source FMP) — **artefact persistant** depuis >20 jours, non résolu |
| **Accounting** | Fichier accounting_risk_latest.json inexistant |

**Alertes composites :** aucune alerte déclenchée sur TEST.

---

## Nouveau scoring global

| Score | Valeur | Évolution vs 23/06 |
|-------|--------|-------------------|
| **Score Opportunité** | 5.6/10 | +0.6 pt |
| **— Catalyseur** | 6.5/10 | — |
| **— Valorisation** | 5.0/10 | — |
| **— Momentum** | 5.3/10 | **+2.3 pts** |
| **Score Global** | 56.0/100 | +5.8 pts |
| **Score Global ajusté** | 48.0/100 | +5.8 pts |

**Pondération appliquée :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime Unknown).

**Justification du scoring (recommandations_latest.json) :**
- RSI 48 — zone neutre favorable
- Cours sous MM50 — tendance baissière
- Pas de malus accounting (données indisponibles)
- Pas de malus geo, FX, event, social

Le rebond du RSI et la normalisation du volume justifient la remontée du Score Momentum (3.0 → 5.3), mais le cours sous MM50 et l'absence de catalyseur empêchent tout franchissement du seuil ATTENDRE (≥60).

---

## Révision des niveaux SL / TP

| Niveau | Valeur précédente (23/06) | Valeur révisée | Justification |
|--------|--------------------------|----------------|---------------|
| **Stop-loss** | $39.88 | **$39.74** | Cours − 2×ATR = $42.34 − $2.60 |
| **Take-profit** | $46.73 | **$46.24** | Cours + 3×ATR = $42.34 + $3.90 |
| **Ratio R/R** | 1.5 | **1.5** | Maintien méthodologique |

**Note :** les niveaux sont recalculés strictement sur la base du cours et de l'ATR du snapshot. Le SL reste proche du 52w low ($40.27) ; un franchissement de ce niveau invaliderait la structure technique et justifierait une révision immédiate du verdict vers ÉVITER.

---

## Conclusion

### Thèse : CONFIRMÉE — SURVEILLER, timing Défavorable

Le rebond technique observé depuis le 23 juin est réel mais fragile :
- ✅ RSI remonté de 40.11 à 47.85 (sortie de la zone survente)
- ✅ Volume normalisé (1 600 vs 677, ×2.4) — mais toujours sous la moyenne 20j
- ❌ Cours sous MM50 ($43.86, écart −3.47%) — pas de reclaim
- ❌ Aucune donnée fondamentale ni optionnelle
- ❌ Earnings JOUR J persistant : artefact calendrier FMP non résolu

**Scénarios et probabilités :**

| Scénario | Probabilité | Trigger | Action |
|----------|------------|---------|--------|
| Reclaim MM50 + volume >1.5× avg + RSI >50 | 25% | Close > $43.86 | Réviser vers ATTENDRE |
| Consolidation latérale $41.50–$43.50 | 50% | Aucun trigger | Maintenir SURVEILLER |
| Franchissement 52w low ($40.27) | 25% | Close < $40.27 | Dégrader vers ÉVITER |

**Points de vigilance :**
1. Liquidité extrêmement faible (volume 20j ~1 925) — tout ordre peut déplacer le cours de manière disproportionnée
2. Absence totale de données fondamentales — impossible d'établir une valorisation institutionnelle
3. Earnings JOUR J non résolu depuis >20 jours — risque d'artefact FMP à surveiller
4. Cours à +5.1% du 52w low — marge de sécurité réduite

**Verdict final :** SURVEILLER. Pas de mutation suffisante pour modifier la thèse. Attendre un reclaim de la MM50 avec volume confirmatoire pour envisager une regradation.

---

*Rapport généré à partir des données data/latest.json et data/recommandations_latest.json du 2026-06-29. Tous les chiffres sont sourcés exclusivement des fichiers JSON du pipeline.*

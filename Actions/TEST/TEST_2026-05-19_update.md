# TEST — Mise à Jour Quotidienne (2026-05-19)

> **Date :** 2026-05-19
> **Heure snapshot :** 10:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-19T10:00:11 UTC), `data/recommandations_2026-05-19.json`
> **Type :** Snapshot post-pipeline matin — données vs close 2026-05-18

---

## Résumé des Changements

| Métrique | 2026-05-18 22:35 UTC | 2026-05-19 10:00 UTC | Delta |
|----------|----------------------|----------------------|-------|
| Cours | $44.94 | **$44.94** | **Inchangé** |
| RSI 14j | 58.88 | **58.87** | −0.01 |
| ATR 14j | $1.10 | **$1.16** | **+$0.06 (+5.5%)** |
| MM 50j | $43.55 | $43.55 | Inchangé |
| Volume | 2,394 (2.04×) | **14,300 (8.08×)** | **+497%** |
| Score Opportunité (agent) | 5.9/10 | **5.9/10** | Inchangé |
| Score Global (agent) | 59.0/100 | **59.0/100** | Inchangé |
| Verdict agent reco | ATTENDRE | **ATTENDRE** | Confirmé |

**Événement majeur :** Volume multiplié par près de 6× vs snapshot précédent (14,300 vs 2,394) et dépassant 8× la moyenne 20j (1,770). Cours inchangé à $44.94, ce qui indique un échange de mains important sans directionnalité nette. Aucun résultat post-earnings observable à 10:00 UTC bien que le calendrier FMP indique un earnings le 2026-05-19 (JOUR J).

---

## Mise à Jour Technique

- **Cours :** $44.935 (open $45.92 / high $45.92 / low $44.85 / previous close $46.144)
- **Variation :** −2.62% vs veille
- **RSI 14j :** 58.87 — zone neutre avec léger avantage acheteur
- **ATR 14j :** $1.16 — volatilité en légère expansion (+5.5% vs snapshot précédent)
- **MM 50j :** $43.55 — support dynamique intact, marge de sécurité +3.19%
- **MM 200j :** N/A
- **Volume relatif :** 8.08× moyenne 20j (14,300 vs 1,770) — **spike de volume significatif**
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette

**Correction de données vs analyse précédente :** Le snapshot précédent (22:35 UTC 2026-05-18) mentionnait un high $46.566 et low $46.144 — valeurs incohérentes avec le cours de clôture $44.94. Le snapshot 10:00 UTC corrige : high $45.92 (même que l'open), low $44.85. Pas de cassure du low précédent.

**Verdict timing :** Neutre. Le spike de volume à 8× la moyenne sans mouvement directionnel suggère soit une absorption de liquidité, soit un rééquilibrage de position pré-earnings. Le maintien au-dessus de MM50 ($43.55) préserve la tendance haussière de court terme, mais le close proche du low intraday ($44.85) et sous l'open ($45.92) reflète une faiblesse de clôture persistante.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 10:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — toujours 🔴 Hors périmètre
- **Sector / Industry :** null / null — TAM et comps indérivables
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant

**Impact earnings du jour :** Aucun résultat post-earnings injecté dans les snapshots Yahoo/FMP à 10:00 UTC. La baisse de −2.62% sur la séance reste sans catalyseur fondamental identifié. Earnings JOUR J (2026-05-19) — résultats potentiellement publiés en dehors des horaires de marché US.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail détectée |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles dans `latest.json` |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism (`data/events_2026-05-19.json`) |
| **Geo Risk** | Non flaggé | Score politique non spécifique pour TEST (geo_risk ne liste que IREN) |
| **FX Exposure** | Exposition 25%, impact 0% | DXY neutre, divergence alignée (`data/fx_exposure_2026-05-19.json`) |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-19 | JOUR J — résultats non observables à 10:00 UTC |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté.

---

## Scoring Global (Agent Recommandation)

Scores inchangés vs snapshot 22:35 UTC 2026-05-18 :

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 6.5/10 | 25% | 1.63 |
| **Score Opportunité** | **5.9/10** | — | **5.91** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (p-value insuffisante, n = 0) |
| Bonus / Timing | 0 | Timing neutre |
| **Score Global ajusté** | **59.0/100** | **ATTENDRE** |

**Proximité du seuil :** À 59.0/100, TEST reste à 1 point du seuil ACHETER réduit (60–74). Une confirmation technique (close > $46.00 avec volume soutenu) pourrait franchir ce seuil. Le spike de volume à 8× sans directionnalité ne constitue pas en soi un signal d'entrée.

---

## Niveaux et Ratio R/R

Niveaux ajustés de l'Agent Recommandation (snapshot $44.94, ATR $1.16) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.94 | Snapshot 10:00 UTC |
| Stop-loss suggéré (2×ATR) | **$42.62** | −5.16% sous le cours |
| Take-profit suggéré (3×ATR) | **$48.41** | +7.72% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Révision des niveaux vs analyse précédente :**
- SL ajusté de $42.74 à **$42.62** (−$0.12, élargi suite à l'expansion ATR)
- TP ajusté de $48.24 à **$48.41** (+$0.17)

**Niveaux techniques complémentaires :**
- Support MM50 : $43.55 (−3.09%) — cassure = signal baissier de court terme
- Support 52W low : $40.27 (−10.39%)
- Résistance previous close : $46.144 (+2.68%)
- Résistance 52W high : $57.74 (+28.48%)

**Note :** Le stop-loss à $42.62 se situe sous MM50 ($43.55). Une cassure de MM50 ne déclencherait pas encore le SL mais constituerait un signal de prudence anticipé.

---

## Conclusion

**Verdict : ATTENDRE — Thèse INACTIVE, confirmée sans changement de configuration fondamentale.**

Le snapshot 10:00 UTC 2026-05-19 confirme la stabilité du cours à $44.94 avec deux éléments techniques notables :
- **Spike de volume à 8.08× la moyenne 20j** (14,300 vs 1,770) — le plus élevé observé sur les derniers snapshots
- **Expansion ATR à $1.16** (+5.5%) — volatilité en légère hausse

Cependant, l'absence de directionnalité malgré le volume élevé (cours inchangé, close sous l'open) ne confirme pas un catalyseur d'entrée. Le spike pourrait refléter un repositionnement pré-earnings (JOUR J).

**Trois facteurs bloquants restent intacts :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle insuffisante** — volume moyen 20j < 2K actions malgré le spike ponctuel
3. **Opacité fondamentale totale** — aucune donnée sectorielle, comptable ou de gouvernance

**Action recommandée :** Maintenir l'attente. La configuration technique est stable mais n'offre pas de catalyseur d'entrée. Surveiller :
- La tenue de MM50 ($43.55)
- Un retour au-dessus de $46.00 (previous close) avec volume soutenu pour envisager une révision vers ACHETER réduit
- Les résultats post-earnings (JOUR J) — si publiés hors séance

**Niveau de confiance :** Très faible — l'analyse repose sur des proxies et des valeurs par défaut.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 10:00 UTC. Données : `data/latest.json`, `data/recommandations_2026-05-19.json`.*

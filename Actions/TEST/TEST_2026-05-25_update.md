# TEST — Mise à Jour Quotidienne (2026-05-25)

> **Date :** 2026-05-25
> **Heure snapshot :** 10:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-25T10:00:11 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`
> **Type :** Mise à jour quotidienne — snapshot 10:00 UTC vs analyse précédente (2026-05-20)

---

## Résumé des Changements

| Métrique | 2026-05-20 (13:00 UTC) | 2026-05-25 (10:00 UTC) | Delta |
|----------|------------------------|------------------------|-------|
| Cours close | $44.185 | **$46.339** | **+4.87%** |
| Previous close | $44.713 | $45.628 | — |
| Variation vs previous close | −1.18% | **+1.56%** | +2.74 pts |
| RSI 14j | 57.46 | **59.86** | **+2.40 pts** |
| ATR 14j | $1.25 | **$1.31** | **+4.8%** |
| MM 50j | $43.33 | **$43.41** | **+0.18%** |
| Volume | 2,500 (1.34× avg) | **500 (0.27× avg)** | **−80%** |
| Position vs MM50 | +1.85% | **+6.75%** | **+4.90 pts** |
| Score Opportunité (agent) | 6.0/10 | **6.1/10** | +0.1 pt |
| Score Global (agent) | 65.2/100 | **66.0/100** | +0.8 pt |
| Verdict agent reco | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| Timing | Favorable | **Favorable** | Confirmé |

**Observations clés :**
- **Cours en hausse de +4.87%** sur 5 séances, porté par un rebond technique sur volume très faible (500 vs 2,500 précédemment).
- **RSI approche 60** (59.86) — zone neutre favorable, pas de surachat.
- **Volume effondré à 0.27× la moyenne 20j** — 500 actions vs 1,880 de moyenne. La hausse du cours n'est pas confirmée par un flux acheteur robuste.
- **Earnings JOUR J** (2026-05-25) — flaggé dans `upcoming_events_latest.json` avec `days_until: 0`. Aucun résultat post-earnings n'est injecté dans `latest.json` à 10:00 UTC. L'événement reste non observable.
- **Score Global inchangé** dans la zone ACHETER réduit (60–74).

---

## Mise à Jour Technique

- **Cours :** $46.339 (open $46.21 / high $46.46 / low $46.21 / previous close $45.628)
- **Variation session :** +1.56% vs previous close
- **Range intraday :** $46.21–$46.46 (0.54%) — range très étroit, illiquide
- **RSI 14j :** 59.86 — zone neutre favorable, proche de 60. +2.40 pts depuis le 20/05.
- **ATR 14j :** $1.31 — volatilité légèrement en expansion (+4.8%)
- **MM 50j :** $43.41 — cours maintenu à +6.75% au-dessus
- **MM 200j :** N/A
- **Volume relatif :** 0.27× moyenne 20j (500 vs 1,880) — **attention : liquidité quasi-nulle**
- **52W range :** [$40.27, $57.74] — positionnement à +15.1% du 52W low, −19.8% du 52W high

**Verdict timing :** Favorable. La configuration technique reste intacte : cours au-dessus de la MM50, RSI dans la zone neutre favorable proche de 60. Cependant, le volume effondré (0.27× moyenne) invalide partiellement le signal haussier. Un mouvement de +4.87% sur 5 séances sans volume de confirmation est fragile et expose au risque de repli rapide si un ordre de taille intervient.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 2026-05-25 :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Agent Quant :** 0 signal historique — calibration insuffisante (p-value 1.0)
- **Validation données :** TEST non listé dans les [ERROR] ni [WARNING] du rapport de validation (22/25 OK)

**Earnings JOUR J (2026-05-25) :** `data/upcoming_events_latest.json` flague un earnings pour TEST avec `days_until: 0`. Aucun résultat post-earnings n'est injecté dans `latest.json` à 10:00 UTC. L'événement earnings (source FMP) reste non observable. Le mouvement intraday (+1.56% vs previous close, range 0.54%) est purement technique / microstructurel sur faible liquidité.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail (inchangé) |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles (`options: {}`) |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism |
| **Geo Risk** | Non flaggé | Score politique non spécifique pour TEST |
| **FX Exposure** | Exposition 25%, impact 0%, divergence alignée | DXY neutre, pas de headwind/tailwind |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-25 — days_until 0 | JOUR J — résultats toujours non observables |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation purement technique.

---

## Scoring Global (Agent Recommandation)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 7.3/10 | 25% | 1.83 |
| **Score Opportunité** | **6.1/10** | — | **6.11** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (n = 0) |
| Bonus / Timing | +5.2 | Cours au-dessus MM50 + timing Favorable |
| **Score Global ajusté** | **66.0/100** | **ACHETER (Réduit)** |

**Proximité des seuils :** À 66.0/100, TEST reste dans la zone ACHETER réduit (60–74). Le Score Opportunité à 6.1/10 franchit le seuil d'entrée minimal. Le momentum à 7.3/10 reste le pilier haussier du scoring. Aucun changement de direction depuis le 20/05.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 2026-05-25 (cours $46.34, ATR $1.31) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $46.34 | Snapshot 10:00 UTC |
| Stop-loss suggéré (2×ATR) | **$43.72** | −5.65% sous le cours |
| Take-profit suggéré (3×ATR) | **$50.27** | +8.48% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.41 (−6.22%) — support dynamique, remonté de $43.33
- **Support gap / low 20/05 :** $43.16 (−6.86%) — non cassé
- **Résistance 52W high :** $57.74 (+24.60%) — objectif théorique
- **Support 52W low :** $40.27 (−13.09%) — dernier niveau de défense

**Révision des niveaux :** Le stop-loss remonte de $41.69 à $43.72 suite à la hausse du cours et à la légère expansion de l'ATR ($1.25 → $1.31). Le take-profit remonte de $47.94 à $50.27. Le ratio R/R reste à 1.5.

**Attention :** Avec un volume de 500 actions, le slippage sur un stop-loss serait extrême. Les niveaux suggérés par l'agent sont théoriques ; en pratique, une exécution à $43.72 pourrait ne pas être réalisable sans impact de marché significatif.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse CONFIRMÉE avec prudence accrue sur le volume.**

Le snapshot 2026-05-25 confirme la trajectoire haussière technique amorcée le 20/05, mais avec un signal de fragilité majeur :
- **Cours en hausse** à $46.34 (+4.87% sur 5 séances) — rebond technique confirmé
- **RSI stable** à 59.86 — momentum haussier intact, pas de surachat
- **MM50 remontée** à $43.41 — cours à +6.75% au-dessus, écart de sécurité accru
- **Volume effondré** à 500 (0.27× moyenne 20j) — **⚠️ signal de fragilité critique**

**Trois facteurs de prudence renforcés :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurellement faible** — volume moyen 20j < 2K actions, aujourd'hui à 0.27×. Le risque de slippage et de mouvement artificiel est maximal.
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils tolérants au risque. Le timing Favorable et le maintien au-dessus de la MM50 offrent un setup technique court terme, mais le volume effondré invalide la conviction.
- **Seuil de confirmation :** Clôture au-dessus de $46.46 (high du jour) avec volume > 1,500 (retour au-dessus de la moyenne 20j)
- **Seuil d'invalidation :** Retour sous $43.41 (MM50) en clôture → revenir SURVEILLER. Cassure de $43.16 (low du 20/05) → ÉVITER
- **Sizing :** Réduit (max 3% du capital) en raison de la liquidité quasi-nulle et de l'absence de fondamentaux

**Earnings JOUR J** : Les résultats restent non observables à 10:00 UTC. Sur publication post-marché, générer immédiatement un `_earnings.md` flash si les données FMP/Yahoo sont injectées. À ce stade, l'absence de données earnings 5 jours après le premier flag JOUR J (2026-05-20) suggère soit un retard de reporting, soit une erreur de calendrier FMP.

**Niveau de confiance :** Faible — l'analyse repose sur des proxies et des valeurs par défaut. La volatilité sur faible liquidité amplifie le risque de faux signaux. Le rebond technique est validé mais **extrêmement fragile** en l'absence de volume. Toute position doit être traitée comme un trade spéculatif de très courte durée avec stop-loss mental strict.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 10:00 UTC. Données : `data/latest.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`.*

# TEST — Mise à Jour Quotidienne (2026-05-26) — Snapshot 17:00 UTC

> **Date :** 2026-05-26
> **Heure snapshot :** 17:00 UTC
> **Sources :** `data/2026-05-26.json` (fetched_at 2026-05-26T17:00:02 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`
> **Type :** Mise à jour post-session — mutation détectée vs snapshot 13:00 UTC

---

## Résumé des Changements

| Métrique | 2026-05-26 (13:00 UTC) | 2026-05-26 (17:00 UTC) | Delta |
|----------|------------------------|------------------------|-------|
| Cours close | $46.339 | **$46.845** | **+1.09%** |
| Previous close | $45.628 | $46.339 | — |
| Variation vs previous close | +1.56% | **+1.09%** | — |
| RSI 14j | 59.86 | **62.02** | **+2.16 pts** |
| ATR 14j | $1.31 | **$1.32** | **+$0.01** |
| MM 50j | $43.41 | **$43.48** | **+$0.07** |
| Volume | 500 (0.27× avg) | **930 (0.49× avg)** | **+86%** |
| Position vs MM50 | +6.75% | **+7.74%** | **+0.99 pt** |
| Score Opportunité (agent) | 6.1/10 | **6.0/10** | **−0.1 pt** |
| Score Global (agent) | 66.0/100 | **64.8/100** | **−1.2 pt** |
| Verdict agent reco | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| Timing | Favorable | **Favorable** | Confirmé |

**Observations clés :**
- **Mutation détectée après 14 snapshots consécutifs stables.** Le cours a gagné +$0.506 (+1.09%) entre 13:00 UTC et 17:00 UTC, rompant la séquence de stabilité absolue depuis le 2026-05-20. Le volume a doublé (500 → 930) mais reste à 0.49× la moyenne 20j.
- **RSI franchit 60** (59.86 → 62.02) — entrée dans la zone momentum haussier confirmée. Le précédent update (13:00 UTC) notait une proximité avec 60 ; ce seuil est désormais franchi.
- **Score Global légèrement révisé à la baisse** (66.0 → 64.8) malgré la hausse du cours, en raison d'une révision du score Momentum par l'agent Recommandation (7.3 → 6.8). L'ajustement reste dans la zone ACHETER réduit (60–74).
- **Volume relatif 0.49×** — amélioration mais toujours très en dessous de la moyenne 20j. La liquidité reste le principal risque structurel.
- **Earnings JOUR J (2026-05-26)** — flaggé dans `upcoming_events_latest.json` avec `days_until: 0`. Aucun résultat post-earnings n'est injecté dans `data/2026-05-26.json` à 17:00 UTC. Après **8 jours de flag JOUR J** (depuis le 2026-05-19 selon certains snapshots, ou 2026-05-20 selon d'autres), l'hypothèse d'un ticker de test sans reporting réel est la plus probable.
- **Rapport de validation :** 22/26 tickers OK. TEST non listé dans les [ERROR] ni [WARNING] — données considérées stables.

---

## Mise à Jour Technique

- **Cours :** $46.845 (open $46.625 / high $47.20 / low $46.625 / previous close $46.339)
- **Variation session :** +1.09% vs previous close
- **Range intraday :** $46.625–$47.20 (1.23%) — range élargi vs 13:00 UTC ($46.21–$46.46 = 0.54%)
- **RSI 14j :** 62.02 — franchissement de 60, zone momentum haussier confirmée. Évolution +2.16 pts vs 13:00 UTC.
- **ATR 14j :** $1.32 — volatilité quasi inchangée (+$0.01)
- **MM 50j :** $43.48 — cours à +7.74% au-dessus (vs +6.75% à 13:00 UTC)
- **MM 200j :** N/A
- **Volume relatif :** 0.49× moyenne 20j (930 vs 1,881) — amélioration mais toujours sous la moyenne
- **52W range :** [$40.27, $57.74] — positionnement à +16.3% du 52W low, −18.9% du 52W high

**Verdict timing :** Favorable. La configuration technique s'améliore : cours au-dessus de la MM50 avec écart accru (+7.74%), RSI au-dessus de 60 confirmant le momentum haussier. Le high du jour à $47.20 marque un nouveau niveau de résistance intraday. Le volume, bien que doublé, reste insuffisant pour valider un mouvement institutionnel. Le risque de slippage persiste.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 2026-05-26 17:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Agent Quant :** 0 signal historique — calibration insuffisante (p-value 1.0)
- **Validation données :** TEST non listé dans les [ERROR] ni [WARNING] du rapport de validation (22/26 OK)

**Earnings JOUR J (2026-05-26) :** `data/upcoming_events_latest.json` flague un earnings pour TEST avec `days_until: 0`. Aucun résultat post-earnings n'est injecté dans `data/2026-05-26.json` à 17:00 UTC. Après **8 jours de flag JOUR J**, l'hypothèse d'un retard de reporting, d'une erreur de calendrier FMP ou d'un ticker de test sans publication réelle se conforte fortement.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail (inchangé) |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles (`options: {}`) |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism |
| **Geo Risk** | Non flaggé | Pas d'événement spécifique pour TEST dans `geo_risk_latest.json` |
| **FX Exposure** | Exposition 25%, impact 0%, divergence alignée | DXY neutre, pas de headwind/tailwind |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-26 — days_until 0 | JOUR J — résultats toujours non observables à 17:00 UTC |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation purement technique. La mutation de cours à 17:00 UTC n'est accompagnée d'aucune information fondamentale ou sentimentale nouvelle.

---

## Scoring Global (Agent Recommandation)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 6.8/10 | 25% | 1.70 |
| **Score Opportunité** | **6.0/10** | — | **5.98** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (n = 0) |
| Bonus / Timing | +5.2 | Cours au-dessus MM50 + timing Favorable |
| **Score Global ajusté** | **64.8/100** | **ACHETER (Réduit)** |

**Proximité des seuils :** À 64.8/100, TEST reste dans la zone ACHETER réduit (60–74). Le Score Opportunité à 6.0/10 franchit le seuil d'entrée minimal. Le momentum à 6.8/10 reste le pilier haussier du scoring, bien que révisé à la baisse de 7.3 à 6.8 par l'agent Recommandation. Le Score Global ajusté recule légèrement (−1.2 pt) suite à cette révision de momentum, mais la direction reste intacte.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 2026-05-26 17:00 UTC (cours $46.845, ATR $1.32) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $46.85 | Snapshot 17:00 UTC |
| Stop-loss suggéré (2×ATR) | **$44.20** | −5.65% sous le cours |
| Take-profit suggéré (3×ATR) | **$50.80** | +8.44% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.48 (−7.18%) — support dynamique, légèrement remonté
- **Support gap / low 20/05 :** $43.16 (−7.87%) — non cassé
- **Résistance intraday :** $47.20 (+0.76%) — high du jour
- **Résistance 52W high :** $57.74 (+23.26%) — objectif théorique
- **Support 52W low :** $40.27 (−14.04%) — dernier niveau de défense

**Révision des niveaux :** Le stop-loss remonte légèrement à $44.20 (vs $43.72 à 13:00 UTC) du fait de la hausse du cours et de l'ATR. Le take-profit à $50.80 reste inchangé en niveau absolu mais se rapproche relativement. Le ratio R/R reste à 1.5.

**Attention :** Avec un volume de 930 actions (moyenne 20j à 1,881), le slippage sur un stop-loss reste élevé. Les niveaux suggérés par l'agent sont théoriques ; en pratique, une exécution à $44.20 pourrait ne pas être réalisable sans impact de marché significatif.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse CONFIRMÉE, première mutation de données après 14 snapshots stables.**

Le snapshot 17:00 UTC rompt la séquence de stabilité absolue observée depuis le 2026-05-20. Les données techniques s'améliorent marginalement :
- **Cours gagne +1.09%** à $46.845 (vs $46.339 à 13:00 UTC)
- **RSI franchit 60** à 62.02 — momentum haussier confirmé, zone neutre favorable dépassée
- **MM50 remonte à $43.48** — cours à +7.74% au-dessus, écart de sécurité accru
- **Volume double à 930** (0.49× moyenne 20j) — amélioration mais toujours insuffisante
- **Range intraday élargi** à 1.23% ($46.625–$47.20) vs 0.54% à 13:00 UTC — signe d'un peu d'activité
- **Score Global légèrement révisé à la baisse** à 64.8/100 (−1.2 pt) — reste dans la zone ACHETER réduit

**Trois facteurs de prudence renforcés :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurellement faible** — volume moyen 20j < 2K actions, aujourd'hui à 0.49×. Le risque de slippage et de mouvement artificiel reste maximal.
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste
4. **Earnings JOUR J non observable** — après **8 jours de flag**, aucun résultat n'a été publié ou injecté. L'hypothèse d'un ticker de test sans reporting réel est désormais la conclusion la plus probable.

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils tolérants au risque. Le franchissement du RSI au-dessus de 60 et le maintien au-dessus de la MM50 renforcent le setup technique court terme, mais le volume faible et l'opacité fondamentale invalident la conviction.
- **Seuil de confirmation :** Clôture au-dessus de $47.20 (high du jour) avec volume > 1,500 (retour au-dessus de la moyenne 20j)
- **Seuil d'invalidation :** Retour sous $43.48 (MM50) en clôture → revenir SURVEILLER. Cassure de $43.16 (low du 20/05) → ÉVITER
- **Sizing :** Réduit (max 3% du capital) en raison de la liquidité quasi-nulle et de l'absence de fondamentaux

**Niveau de confiance :** Faible — l'analyse repose sur des proxies et des valeurs par défaut. La mutation de cours à 17:00 UTC n'est pas accompagnée d'aucune information fondamentale ou sentimentale, ce qui suggère un mouvement technique ou microstructurel sur très faible liquidité. Toute position doit être traitée comme un trade spéculatif de très courte durée avec stop-loss mental strict.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 17:00 UTC. Données : `data/2026-05-26.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`.*

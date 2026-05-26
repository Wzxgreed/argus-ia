# TEST — Mise à Jour Quotidienne (2026-05-26) — Snapshot 21:00 UTC

> **Date :** 2026-05-26
> **Heure snapshot :** 21:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-26T21:00:02 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`
> **Type :** Mise à jour post-session — deuxième mutation détectée vs snapshot 17:00 UTC

---

## Résumé des Changements

| Métrique | 2026-05-26 (17:00 UTC) | 2026-05-26 (21:00 UTC) | Delta |
|----------|------------------------|------------------------|-------|
| Cours close | $46.845 | **$47.153** | **+0.66%** |
| Previous close | $46.339 | $46.339 | — |
| Variation vs previous close | +1.09% | **+1.76%** | **+0.67 pt** |
| RSI 14j | 62.02 | **62.86** | **+0.84 pt** |
| ATR 14j | $1.32 | **$1.32** | Inchangé |
| MM 50j | $43.48 | **$43.48** | Inchangée |
| Volume | 930 (0.49× avg) | **1,160 (0.61× avg)** | **+24.7%** |
| Position vs MM50 | +7.74% | **+8.40%** | **+0.66 pt** |
| Score Opportunité (agent) | 6.0/10 | **6.0/10** | Confirmé |
| Score Global (agent) | 64.8/100 | **64.8/100** | Confirmé |
| Verdict agent reco | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| Timing | Favorable | **Favorable** | Confirmé |

**Observations clés :**
- **Deuxième mutation consécutive dans la même session.** Après la première mutation à 17:00 UTC (rupture de 14 snapshots stables), le cours poursuit sa remontée à 21:00 UTC avec +$0.308 (+0.66%) supplémentaires. Le gain total sur la session atteint +$0.814 (+1.76% vs previous close).
- **RSI continue de grimper** (62.02 → 62.86) — consolidation dans la zone momentum haussier au-dessus de 60. Pas de surachat (seuil 70 non approché).
- **Volume en légère accélération** (930 → 1,160) — +24.7% vs 17:00 UTC mais toujours à 0.61× la moyenne 20j (1,893). La liquidité reste structurellement faible.
- **High du jour révisé à $47.2085** — nouveau niveau de résistance intraday établi, légèrement supérieur au high de 17:00 UTC ($47.20).
- **Score Global inchangé à 64.8/100** — l'agent Recommandation maintient le verdict ACHETER (Réduit) avec un timing Favorable. Aucun ajustement de malus/bonus détecté entre les deux snapshots.
- **Earnings JOUR J (2026-05-26)** — flaggé dans `upcoming_events_latest.json` avec `days_until: 0`. Après **9 jours de flag JOUR J** (depuis le 2026-05-19), aucun résultat post-earnings n'a été injecté dans `data/latest.json` à 21:00 UTC. L'hypothèse d'un ticker de test sans reporting réel reste la conclusion dominante.
- **Rapport de validation :** 23/26 tickers OK. TEST non listé dans les [ERROR] ni [WARNING] — données considérées stables.

---

## Mise à Jour Technique

- **Cours :** $47.153 (open $46.625 / high $47.2085 / low $46.625 / previous close $46.339)
- **Variation session :** +1.76% vs previous close
- **Range intraday :** $46.625–$47.2085 (1.25%) — range quasi identique à 17:00 UTC (1.23%), le high étant légèrement repoussé
- **RSI 14j :** 62.86 — consolidation au-dessus de 60, zone momentum haussier maintenue. Évolution +0.84 pt vs 17:00 UTC.
- **ATR 14j :** $1.32 — volatilité inchangée
- **MM 50j :** $43.48 — cours à +8.40% au-dessus (vs +7.74% à 17:00 UTC)
- **MM 200j :** N/A
- **Volume relatif :** 0.61× moyenne 20j (1,160 vs 1,893) — amélioration mais toujours sous la moyenne
- **52W range :** [$40.27, $57.74] — positionnement à +16.9% du 52W low, −18.3% du 52W high

**Verdict timing :** Favorable. La configuration technique s'améliore marginalement : cours au-dessus de la MM50 avec écart accru (+8.40%), RSI consolidé au-dessus de 60. Le high du jour à $47.2085 marque un niveau de résistance à surveiller. Le volume reste le point d'attention majeur : 1,160 actions sur la session ne valident pas un mouvement institutionnel. Le risque de slippage persiste.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 2026-05-26 21:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Agent Quant :** 0 signal historique — calibration insuffisante (p-value 1.0)
- **Validation données :** TEST non listé dans les [ERROR] ni [WARNING] du rapport de validation (23/26 OK)

**Earnings JOUR J (2026-05-26) :** `data/upcoming_events_latest.json` flague un earnings pour TEST avec `days_until: 0`. Aucun résultat post-earnings n'est injecté dans `data/latest.json` à 21:00 UTC. Après **9 jours de flag JOUR J**, l'hypothèse d'un retard de reporting, d'une erreur de calendrier FMP ou d'un ticker de test sans publication réelle se conforte fortement.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail (inchangé) |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles (`options: {}`) |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism (`events_latest.json` vide) |
| **Geo Risk** | Non flaggé | Pas d'événement spécifique pour TEST dans `geo_risk_latest.json` (date 2026-05-17) |
| **FX Exposure** | Exposition 25%, impact 0%, divergence alignée | DXY neutre, pas de headwind/tailwind (flag 🟢) |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-26 — days_until 0 | JOUR J — résultats toujours non observables à 21:00 UTC |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation purement technique. La mutation de cours à 21:00 UTC n'est accompagnée d'aucune information fondamentale ou sentimentale nouvelle.

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

**Proximité des seuils :** À 64.8/100, TEST reste dans la zone ACHETER réduit (60–74). Le Score Opportunité à 6.0/10 franchit le seuil d'entrée minimal. Le momentum à 6.8/10 reste le pilier haussier du scoring. Aucune révision de score détectée entre 17:00 UTC et 21:00 UTC — l'agent Recommandation maintient sa configuration.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 2026-05-26 21:00 UTC (cours $47.15, ATR $1.32) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $47.15 | Snapshot 21:00 UTC |
| Stop-loss suggéré (2×ATR) | **$44.51** | −5.60% sous le cours |
| Take-profit suggéré (3×ATR) | **$51.11** | +8.40% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.48 (−7.78%) — support dynamique, inchangé
- **Support gap / low 20/05 :** $43.16 (−8.46%) — non cassé
- **Résistance intraday :** $47.21 (+0.12%) — high du jour à $47.2085, testé à 21:00 UTC
- **Résistance 52W high :** $57.74 (+22.5%) — objectif théorique
- **Support 52W low :** $40.27 (−14.6%) — dernier niveau de défense

**Révision des niveaux :** Le stop-loss remonte légèrement à $44.51 (vs $44.20 à 17:00 UTC) du fait de la hausse du cours. Le take-profit à $51.11 suit la même logique (vs $50.80 à 17:00 UTC). Le ratio R/R reste à 1.5.

**Attention :** Avec un volume de 1,160 actions (moyenne 20j à 1,893), le slippage sur un stop-loss reste élevé. Les niveaux suggérés par l'agent sont théoriques ; en pratique, une exécution à $44.51 pourrait ne pas être réalisable sans impact de marché significatif.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse CONFIRMÉE, deuxième mutation consécutive dans la session.**

Le snapshot 21:00 UTC confirme la mutation amorcée à 17:00 UTC. Les données techniques s'améliorent marginalement :
- **Cours gagne +0.66%** supplémentaires à $47.15 (vs $46.845 à 17:00 UTC), soit +1.76% sur la session complète
- **RSI consolidé à 62.86** — momentum haussier maintenu au-dessus de 60
- **MM50 inchangée à $43.48** — cours à +8.40% au-dessus, écart de sécurité accru
- **Volume à 1,160** (0.61× moyenne 20j) — amélioration mais toujours insuffisante pour valider un flux institutionnel
- **Range intraday stable** à 1.25% ($46.625–$47.2085) — le high a été légèrement repoussé
- **Score Global inchangé à 64.8/100** — verdict ACHETER (Réduit) confirmé, timing Favorable

**Trois facteurs de prudence renforcés :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurellement faible** — volume moyen 20j < 2K actions, aujourd'hui à 0.61×. Le risque de slippage et de mouvement artificiel reste maximal.
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste
4. **Earnings JOUR J non observable** — après **9 jours de flag**, aucun résultat n'a été publié ou injecté. L'hypothèse d'un ticker de test sans reporting réel est désormais la conclusion la plus probable.

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils tolérants au risque. Le franchissement du RSI au-dessus de 60 et le maintien au-dessus de la MM50 renforcent le setup technique court terme, mais le volume faible et l'opacité fondamentale invalident la conviction.
- **Seuil de confirmation :** Clôture au-dessus de $47.21 (high du jour) avec volume > 1,500 (retour au-dessus de la moyenne 20j)
- **Seuil d'invalidation :** Retour sous $43.48 (MM50) en clôture → revenir SURVEILLER. Cassure de $43.16 (low du 20/05) → ÉVITER
- **Sizing :** Réduit (max 3% du capital) en raison de la liquidité quasi-nulle et de l'absence de fondamentaux

**Niveau de confiance :** Faible — l'analyse repose sur des proxies et des valeurs par défaut. La mutation de cours à 21:00 UTC n'est pas accompagnée d'aucune information fondamentale ou sentimentale, ce qui suggère un mouvement technique ou microstructurel sur très faible liquidité. Toute position doit être traitée comme un trade spéculatif de très courte durée avec stop-loss mental strict.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 21:00 UTC. Données : `data/2026-05-26.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`.*

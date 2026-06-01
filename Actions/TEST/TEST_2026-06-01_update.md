# TEST — Mise à Jour Quotidienne (2026-06-01) — Snapshot 17:00 UTC

> **Date :** 2026-06-01
> **Heure snapshot :** 17:00 UTC
> **Sources :** `data/2026-06-01.json` (fetched_at 2026-06-01T17:00:01 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`
> **Type :** Mise à jour post-session — snapshot 17:00 UTC vs 13:00 UTC

---

## Résumé des Changements

| Métrique | 2026-06-01 (13:00 UTC) | 2026-06-01 (17:00 UTC) | Delta |
|----------|------------------------|------------------------|-------|
| Cours close | $47.236 | **$46.03** | **−2.55%** |
| Previous close | $47.747 | $47.236 | — |
| Variation vs previous close | −1.07% | **−2.55%** | **−148 bps** |
| RSI 14j | 53.42 | **41.06** | **−12.36 pts** |
| ATR 14j | $1.20 | **$1.08** | **−$0.12** |
| MM 50j | $43.49 | **$43.55** | **+$0.06** |
| Volume session | 400 (0.21× avg) | **2,810 (1.42× avg)** | **+2,410 (+602.5%)** |
| Volume moy. 20j | 1,860 | **1,985** | **+125** |
| Position vs MM50 | +8.60% | **+5.69%** | **−291 bps** |
| Score Opportunité (agent) | 6.0/10 | **5.7/10** | **−0.3** |
| Score Momentum (agent) | 7.0/10 | **5.5/10** | **−1.5** |
| Score Global ajusté (agent) | 65.2/100 | **61.5/100** | **−3.7** |
| Verdict agent reco | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé à la marge |
| Timing | Favorable | **Favorable** | Confirmé |

**Observations clés :**
- **Mutation technique majeure entre 13:00 UTC et 17:00 UTC** — cours en baisse de 2.55%, RSI en chute de 12.36 pts sous le seuil 50, momentum en net recul.
- **RSI à 41.06** — sortie de la zone neutre favorable pour entrer dans la zone baissière (momentum négatif). Seuil 50 franchi à la baisse pour la première fois depuis le snapshot 10:00 UTC du 26/05 (RSI 62.02).
- **Volume en explosion relative ×7** (400 → 2,810) mais reste marginal vs moyenne 20j à 1,985 (1.42×). L'augmentation du volume accompagne la baisse du cours, ce qui est un signal de distribution faible mais réel.
- **Score Global ajusté en baisse de 3.7 pts** à 61.5/100 — verdict ACHETER (Réduit) maintenu mais le ticker se rapproche dangereusement du seuil ATTENDRE (60).
- **Earnings JOUR J (2026-06-01)** — `upcoming_events_latest.json` maintient `days_until: 0`. Après **15 jours cumulés de flag JOUR J**, aucun résultat post-earnings n'est observable. L'hypothèse d'un ticker de test sans reporting réel reste la conclusion dominante.
- **Rapport de validation :** 24/28 tickers OK, 4 KO, 2 warnings. TEST absent des anomalies — données stables.

---

## Mise à Jour Technique

- **Cours :** $46.03 (open $46.25 / high $46.54 / low $46.0099 / previous close $47.236)
- **Variation session :** −2.55% vs previous close
- **Range intraday :** $46.0099–$46.54 (1.15%) — range légèrement élargi vs 13:00 UTC (0.18%)
- **RSI 14j :** 41.06 — **franchissement du seuil 50 à la baisse**, passage en zone de momentum négatif
- **ATR 14j :** $1.08 — contraction de 10% vs 13:00 UTC, volatilité en légère compression malgré la baisse du cours
- **MM 50j :** $43.55 — cours à +5.69% au-dessus, écart de sécurité réduit de 291 bps
- **MM 200j :** N/A
- **Volume relatif :** 1.42× moyenne 20j (2,810 vs 1,985) — retour au-dessus de la moyenne après 4 jours d'effondrement
- **52W range :** [$40.27, $57.74] — positionnement à +14.3% du 52W low, −20.3% du 52W high

**Verdict timing :** Favorable. Configuration technique dégradée mais pas invalidée : cours reste au-dessus de la MM50 avec écart de +5.69%, RSI dans la zone baissière (41.06) indiquant un momentum négatif court terme. L'augmentation du volume sur baisse de cours est un signal de faiblesse à surveiller. Le risque de slippage reste élevé malgré l'amélioration du volume.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 2026-06-01 17:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Agent Quant :** 0 signal historique — calibration insuffisante (p-value 1.0, date 2026-05-17)
- **Validation données :** TEST absent des [ERROR] et [WARNING] du rapport de validation

**Earnings JOUR J (2026-06-01) :** `data/upcoming_events_latest.json` maintient le flag `days_until: 0` pour TEST. Après **15 jours cumulés de flag JOUR J**, aucun résultat post-earnings n'est observable. La probabilité d'un retard de reporting, d'une erreur de calendrier FMP ou d'un ticker de test sans publication réelle reste maximale.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail (inchangé) |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles (`options: {}`) |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism (`events_latest.json`) |
| **Geo Risk** | Non flaggé | Pas d'événement spécifique pour TEST (`geo_risk_latest.json` date 2026-05-17) |
| **FX Exposure** | Exposition 25%, impact 0%, divergence alignée | DXY neutre, pas de headwind/tailwind (flag 🟢) |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-06-01 — days_until 0 | JOUR J — résultats non observables à 17:00 UTC |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |
| **Sector Rotation** | Régime UNKNOWN, signal ROTATION_TO_CYCLICAL | XLK leader (momentum 10.0) — pas d'impact direct sur TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation purement technique. Le volume en hausse sur baisse de cours est le seul signal nouveau du snapshot 17h.

---

## Scoring Global (Agent Recommandation)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 5.5/10 | 25% | 1.38 |
| **Score Opportunité** | **5.7/10** | — | **5.65** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (n = 0) |
| Bonus / Timing | +5.0 | Cours au-dessus MM50 + timing Favorable |
| **Score Global ajusté** | **61.5/100** | **ACHETER (Réduit)** |

**Proximité des seuils :** À 61.5/100, TEST reste dans la zone ACHETER réduit (60–74) mais se rapproche du seuil inférieur. Le Score Opportunité à 5.7/10 franchit encore le seuil d'entrée minimal. Le momentum à 5.5/10 a perdu son statut de pilier haussier. Aucun malus additionnel n'est activé. **Attention :** une baisse supplémentaire de 1.5 pt du Score Global placerait TEST en zone ATTENDRE.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 2026-06-01 17:00 UTC (cours $46.03, ATR $1.08) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $46.03 | Snapshot 17:00 UTC |
| Stop-loss suggéré (2×ATR) | **$43.87** | −4.69% sous le cours |
| Take-profit suggéré (3×ATR) | **$49.27** | +6.99% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.55 (−5.39%) — support dynamique, premier niveau de défense
- **Support gap / low 20/05 :** $43.16 (−6.24%) — second niveau de défense
- **Résistance intraday :** $46.54 (+1.11%) — high de la session 01/06
- **Résistance 52W high :** $57.74 (+25.4%) — objectif théorique
- **Support 52W low :** $40.27 (−12.5%) — dernier niveau de défense

**Révision des niveaux :** SL abaissé de $44.84 à $43.87 (−$0.97) compte tenu de la baisse du cours et de la contraction de l'ATR. TP abaissé de $50.84 à $49.27 (−$1.57). Le ratio R/R reste à 1.5. Le niveau SL est désormais très proche de la MM50 ($43.55), ce qui réduit la marge de manœuvre.

**Attention :** Avec un volume de 2,810 actions (moyenne 20j à 1,985), la liquidité reste faible malgré l'amélioration relative. Le slippage sur un stop-loss à $43.87 reste significatif. Les niveaux suggérés par l'agent sont théoriques ; en pratique, une exécution à $43.87 pourrait ne pas être réalisable sans impact de marché.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse MODIFIÉE, dégradation technique confirmée.**

Le snapshot 17:00 UTC du 2026-06-01 révèle une mutation technique notable par rapport au snapshot 13:00 UTC :
- **Cours en baisse de 2.55%** à $46.03 — perte de −$1.21 vs le close 13h
- **RSI en chute de 12.36 pts à 41.06** — franchissement du seuil 50 à la baisse, passage en zone de momentum négatif
- **Score Momentum en recul de 1.5 pt** à 5.5/10 — perte du statut de pilier haussier
- **Score Global ajusté en baisse de 3.7 pts** à 61.5/100 — verdict maintenu mais à la marge
- **Volume ×7** (400 → 2,810) accompagnant la baisse — signal de faiblesse
- **Position vs MM50 réduite** à +5.69% (vs +8.60% à 13h) — marge de sécurité technique rétrécie

**Trois facteurs de prudence renforcés :**
1. **Franchissement RSI 50 à la baisse** — momentum négatif court terme activé. Le retour sous 40 amplifierait la pression vendeuse.
2. **Liquidité marginale** — volume à 2,810 (1.42× moyenne 20j) reste extrêmement faible. Le risque de slippage et de mouvement artificiel reste élevé.
3. **Proximité du seuil ATTENDRE** — à 61.5/100, TEST n'est qu'à 1.5 pt de la zone ATTENDRE (50–59). Une mutation négative additionnelle invaliderait le verdict ACHETER.

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils très tolérants au risque. Le maintien au-dessus de la MM50 et le verdict agent confirment le setup, mais la dégradation du momentum et le franchissement RSI 50 réduisent fortement la conviction.
- **Seuil de confirmation :** Clôture au-dessus de $46.54 (high de la session 01/06) avec volume > 3,000 et RSI > 45
- **Seuil d'invalidation :** Retour sous $43.55 (MM50) en clôture → revenir ATTENDRE. Cassure de $43.16 (low du 20/05) → SURVEILLER
- **Sizing :** Réduit (max 2% du capital) en raison de la liquidité faible et de la dégradation technique

**Niveau de confiance :** Très faible — l'analyse repose sur des proxies et des valeurs par défaut. La chute du RSI sous 50, la baisse de 2.55% et le volume faible sur baisse invalident toute conviction technique. Toute position doit être traitée comme un trade spéculatif de très courte durée avec stop-loss mental strict. La thèse reste maintenue uniquement par le maintien au-dessus de la MM50 et le verdict agent à la marge.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 17:00 UTC. Données : `data/2026-06-01.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`.*

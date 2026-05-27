# TEST — Mise à Jour Quotidienne (2026-05-27) — Snapshot 17:00 UTC

> **Date :** 2026-05-27
> **Heure snapshot :** 17:00 UTC (post-session)
> **Sources :** `data/latest.json` (fetched_at 2026-05-27T17:00:11 UTC), `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`
> **Type :** Mutation détectée — fin de la séquence de 15 snapshots sans mutation

---

## Résumé des Changements

| Métrique | 2026-05-27 (13:00 UTC) | 2026-05-27 (17:00 UTC) | Delta |
|----------|------------------------|------------------------|-------|
| Cours close | $47.153 | **$47.525** | **+0.79%** |
| Previous close | $46.339 | $47.153 | — |
| Variation vs previous close | +1.76% | **+0.79%** | — |
| RSI 14j | 62.86 | **62.24** | **−0.62** |
| ATR 14j | $1.32 | **$1.31** | **−$0.01** |
| MM 50j | $43.48 | **$43.55** | **+$0.07** |
| Volume session | 1,200 (0.63× avg) | **1,356 (0.71× avg)** | **+13.0%** |
| Position vs MM50 | +8.40% | **+9.13%** | **+73 bps** |
| Score Opportunité (agent) | 6.0/10 | **5.9/10** | **−0.1** |
| Score Momentum (agent) | 6.8/10 | **6.5/10** | **−0.3** |
| Score Global ajusté (agent) | 64.8/100 | **64.0/100** | **−0.8** |
| Verdict agent reco | ACHETER (Réduit) | **ACHETER (Réduit)** | Confirmé |
| Timing | Favorable | **Favorable** | Confirmé |

**Observations clés :**
- **Première mutation après 15 snapshots consécutifs de stabilité.** Le cours a progressé de +0.79% entre 13:00 UTC et 17:00 UTC, clôturant à $47.525. C'est la première variation de prix observée sur TEST depuis la session du 26/05.
- **RSI en léger recul à 62.24** (−0.62) — consolidation dans la zone momentum haussier au-dessus de 60. Le seuil de surachat (70) n'est pas approché.
- **Volume en hausse de 13%** à 1,356 actions (0.71× moyenne 20j à 1,922) — reste structurellement faible, mais la progression du volume accompagne timidement la hausse du cours.
- **Score Global ajusté en recul de 0.8 pt à 64.0/100** — verdict ACHETER (Réduit) maintenu, timing Favorable. La légère détente du momentum (−0.3 pt) explique la quasi-totalité du recul.
- **Earnings JOUR J (2026-05-27)** — `upcoming_events_latest.json` maintient le flag `days_until: 0`. Après **12 jours de flag JOUR J** (depuis le 2026-05-19), aucun résultat post-earnings n'a été injecté dans `data/latest.json`. L'hypothèse d'un ticker de test sans reporting réel reste la conclusion dominante.
- **Rapport de validation :** 23/26 tickers OK, 3 tickers KO. TEST n'est listé dans aucune anomalie — données stables.

---

## Mise à Jour Technique

- **Cours :** $47.525 (open $47.36 / high $47.6401 / low $47.4299 / previous close $47.153)
- **Variation session :** +0.79% vs previous close
- **Range intraday :** $47.36–$47.64 (0.59%)
- **RSI 14j :** 62.24 — consolidation au-dessus de 60, momentum haussier maintenu
- **ATR 14j :** $1.31 — volatilité inchangée, quasi-figée
- **MM 50j :** $43.55 — cours à +9.13% au-dessus, écart de sécurité en expansion
- **MM 200j :** N/A
- **Volume relatif :** 0.71× moyenne 20j (1,356 vs 1,922) — profil de liquidité toujours très faible, mais en légère amélioration vs 13:00 UTC
- **52W range :** [$40.27, $57.74] — positionnement à +17.9% du 52W low, −17.7% du 52W high

**Verdict timing :** Favorable. Configuration technique inchangée : cours au-dessus de la MM50 avec écart de +9.13%, RSI consolidé au-dessus de 60. Le high intraday à $47.64 constitue le nouveau niveau de résistance immédiat. Le volume reste faible (1,356 actions) et invalide la confirmation d'un mouvement institutionnel. Le risque de slippage persiste.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 2026-05-27 17:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Agent Quant :** 0 signal historique — calibration insuffisante (p-value 1.0, date 2026-05-17)
- **Validation données :** TEST absent des [ERROR] et [WARNING] du rapport de validation

**Earnings JOUR J (2026-05-27) :** `data/upcoming_events_latest.json` maintient le flag `days_until: 0` pour TEST. Après **12 jours de flag JOUR J**, aucun résultat post-earnings n'est observable. La probabilité d'un retard de reporting, d'une erreur de calendrier FMP ou d'un ticker de test sans publication réelle reste maximale.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail (inchangé) |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles (`options: {}`) |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism |
| **Geo Risk** | Non flaggé | Pas d'événement spécifique pour TEST (`geo_risk_latest.json` date 2026-05-17) |
| **FX Exposure** | Exposition 25%, impact 0%, divergence alignée | DXY neutre, pas de headwind/tailwind (flag 🟢) |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-27 — days_until 0 | JOUR J — résultats toujours non observables à 17:00 UTC |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |
| **Sector Rotation** | Régime UNKNOWN, signal NEUTRAL | XLK leader (momentum 10.0), XLY deuxième — pas d'impact direct sur TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation purement technique. Le snapshot 17:00 UTC n'apporte aucune information fondamentale ou sentimentale nouvelle.

---

## Scoring Global (Agent Recommandation)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 6.5/10 | 25% | 1.63 |
| **Score Opportunité** | **5.9/10** | — | **5.90** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (n = 0) |
| Bonus / Timing | +5.2 | Cours au-dessus MM50 + timing Favorable |
| **Score Global ajusté** | **64.0/100** | **ACHETER (Réduit)** |

**Proximité des seuils :** À 64.0/100, TEST reste dans la zone ACHETER réduit (60–74). Le Score Opportunité à 5.9/10 franchit le seuil d'entrée minimal. Le momentum à 6.5/10 reste le pilier haussier du scoring, malgré un recul de 0.3 pt lié à la légère détente du RSI. Aucun malus additionnel n'est activé.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 2026-05-27 17:00 UTC (cours $47.525, ATR $1.31) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $47.525 | Snapshot 17:00 UTC |
| Stop-loss suggéré (2×ATR) | **$44.91** | −5.50% sous le cours |
| Take-profit suggéré (3×ATR) | **$51.45** | +8.26% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Support MM50 :** $43.55 (−8.36%) — support dynamique, en légère remontée
- **Support gap / low 20/05 :** $43.16 (−9.18%) — non cassé
- **Résistance intraday :** $47.64 (+0.24%) — high de la session 27/05 à $47.6401
- **Résistance 52W high :** $57.74 (+21.5%) — objectif théorique
- **Support 52W low :** $40.27 (−15.3%) — dernier niveau de défense

**Révision des niveaux :** Le SL remonte de $44.51 à $44.91 (+$0.40) et le TP de $51.11 à $51.45 (+$0.34) en raison de la hausse du cours et de la légère baisse de l'ATR. Le ratio R/R reste à 1.5.

**Attention :** Avec un volume de 1,356 actions (moyenne 20j à 1,922), le slippage sur un stop-loss reste élevé. Les niveaux suggérés par l'agent sont théoriques ; en pratique, une exécution à $44.91 pourrait ne pas être réalisable sans impact de marché significatif.

---

## Conclusion

**Verdict : ACHETER (Réduit) — Thèse CONFIRMÉE, première mutation détectée après 15 snapshots de stabilité.**

Le snapshot 17:00 UTC du 2026-05-27 met fin à la séquence de 15 snapshots consécutifs sans mutation observée depuis la session du 26/05. Les données techniques évoluent modestement :
- **Cours en hausse de +0.79% à $47.525** — première variation de prix observée depuis 15 snapshots
- **RSI en recul à 62.24** (−0.62) — consolidation au-dessus de 60, momentum haussier intact
- **MM50 remontée à $43.55** (+$0.07) — cours à +9.13% au-dessus, écart de sécurité en expansion
- **Volume à 1,356** (0.71× moyenne 20j) — légère hausse de 13% vs 13:00 UTC, mais profil de liquidité toujours insuffisant pour valider un flux institutionnel
- **Score Global ajusté à 64.0/100** (−0.8 pt) — verdict ACHETER (Réduit) maintenu, timing Favorable

**Quatre facteurs de prudence renforcés :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurellement faible** — volume moyen 20j < 2K actions. Le risque de slippage et de mouvement artificiel reste maximal.
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste
4. **Earnings JOUR J non observable** — après **12 jours de flag**, aucun résultat n'a été publié ou injecté. L'hypothèse d'un ticker de test sans reporting réel est désormais la conclusion quasi-certaine.

**Action recommandée :**
- **ACHETER (Réduit)** uniquement pour les profils tolérants au risque. Le franchissement du RSI au-dessus de 60 et le maintien au-dessus de la MM50 renforcent le setup technique court terme, mais le volume faible et l'opacité fondamentale invalident la conviction.
- **Seuil de confirmation :** Clôture au-dessus de $47.64 (high de la session 27/05) avec volume > 1,900 (retour au-dessus de la moyenne 20j)
- **Seuil d'invalidation :** Retour sous $43.55 (MM50) en clôture → revenir SURVEILLER. Cassure de $43.16 (low du 20/05) → ÉVITER
- **Sizing :** Réduit (max 3% du capital) en raison de la liquidité quasi-nulle et de l'absence de fondamentaux

**Niveau de confiance :** Faible — l'analyse repose sur des proxies et des valeurs par défaut. La mutation détectée à 17:00 UTC (cours +0.79%, volume +13%) est timide et n'est pas accompagnée d'aucune information fondamentale ou sentimentale nouvelle, ce qui confirme le caractère technique ou microstructurel du mouvement sur très faible liquidité. Toute position doit être traitée comme un trade spéculatif de très courte durée avec stop-loss mental strict.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 17:00 UTC. Données : `data/2026-05-27.json`, `data/recommandations_latest.json`, `data/upcoming_events_latest.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/events_latest.json`.*

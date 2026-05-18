# TEST — Mise à Jour Quotidienne (2026-05-18)

> **Date :** 2026-05-18
> **Heure snapshot :** 17:00 UTC
> **Sources :** `data/2026-05-18.json` (fetched_at 2026-05-18T17:00:11 UTC), `data/recommandations_2026-05-18.json`, `data/upcoming_events_2026-05-18.json`, `data/geo_2026-05-18.json`, `data/fx_exposure_2026-05-18.json`, `data/social_sentiment_2026-05-18.json`, `data/sector_rotation_2026-05-18.json`, `data/quant_2026-05-18.json`, `data/events_2026-05-18.json`
> **Type :** Révision post-pipeline 17:00 UTC — détérioration technique avec volume anormal

---

## Résumé des Changements

| Métrique | 2026-05-18 13:00 UTC | 2026-05-18 17:00 UTC | Delta |
|----------|----------------------|----------------------|-------|
| Cours | $46.14 | **$44.85** | **-2.80%** |
| RSI 14j | 64.16 | **58.47** | **-5.69 pts** |
| ATR 14j | $1.09 | **$1.16** | **+6.4%** |
| MM 50j | $43.54 | $43.55 | +$0.01 |
| Volume | 2,400 (2.22×) | **8,587 (5.79×)** | **+258% absolu** |
| Score Opportunité | 5.7/10 | **5.5/10** | **-0.2 pt** |
| Score Global | 56.5/100 | **54.5/100** | **-2.0 pts** |
| Verdict agent reco | ATTENDRE | **ATTENDRE** | Confirmé |

**Événement majeur :** Aucun événement corporate détecté dans `data/events_latest.json` (0 événement). Earnings JOUR J (2026-05-18) toujours sans résultats post-earnings observables à 17:00 UTC. La baisse de -2.80% sur volume 5.79× la moyenne 20j n'est pas liée à un catalyseur fondamental identifiable dans les flux.

---

## Mise à Jour Technique

Configuration technique détériorée vs snapshot 13:00 UTC :
- **Cours :** $44.85 (open $45.92 / high $45.92 / low $44.85 / previous close $46.144)
- **Variation :** -2.80% — séance de distribution avec open = high et close = low, zero intraday recovery
- **RSI 14j :** 58.47 — retrait du territoire haussier modéré (64.16) vers neutre, conservation d'un léger avantage acheteur
- **ATR 14j :** $1.16 — volatilité en expansion (+6.4% vs 13:00 UTC)
- **MM 50j :** $43.55 — cours supérieur (+2.98%), support dynamique intact mais marge de sécurité réduite
- **MM 200j :** N/A
- **Volume relatif :** 5.79× moyenne 20j (8,587 vs 1,484) — spike de distribution massif sur micro-cap
- **52W range :** [$40.27, $57.74] — repositionnement vers le bas de la fourchette

**Verdict timing :** Défavorable. La séance présente un profil de vente contrôlée : open = high ($45.92), puis descente continue jusqu'à close = low ($44.85), sans aucune reprise intraday. Ce pattern sur volume 5.79× la normale sur un act illiquide traduit un déséquilibre offre/demande nettement vendeur. Le maintien au-dessus de MM50 ($43.55) empêche un basculement baissier structuré, mais la marge de sécurité est réduite à 2.98% (vs 5.97% à 13:00 UTC). Une cassure sous MM50 avec ce type de volume confirmerait un retournement de court terme.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle n'est disponible dans le snapshot 17:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — toujours 🔴 Hors périmètre
- **Sector / Industry :** null / null — impossible de dériver un TAM ou des comps
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** [DONNÉES MANQUANTES] — rapport `data/accounting_risk_latest.json` inexistant

**Impact earnings du jour :** Aucun résultat post-earnings injecté dans les snapshots Yahoo/FMP à 17:00 UTC. Le calendrier FMP indiquait un earnings le 2026-05-18, mais l'absence de données fondamentales actualisées suggère soit un retard de publication, soit une société non couverte par les bases de données institutionnelles. La baisse de -2.80% sur volume massif pourrait refléter une anticipation négative ou une déception liée à un manque de visibilité, mais sans données vérifiables, tout chiffrage reste spéculatif.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail détectée (5 subreddits scannés, 0 posts collectés) |
| **Options** | [DONNÉES MANQUANTES] | Bloc vide dans `latest.json` — max pain, GEX, IV Rank indisponibles |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism dans `data/events_latest.json` |
| **Geo Risk** | Non flaggé | Score politique 2/10 (`data/geo_2026-05-18.json`) — aucune exposition cartographiée, flag 🟢 |
| **FX Exposure** | [NON ANALYSÉ] | TEST absent du rapport `data/fx_exposure_2026-05-18.json` |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target, pas d'upgrades/downgrades dans `data/recommandations_2026-05-18.json` |
| **Upcoming Events** | [NON LISTÉ] | TEST absent du rapport `data/upcoming_events_2026-05-18.json` (earnings JOUR J non confirmé post-close) |

Aucun flux institutionnel, insider trade ou unusual options activity n'est rapporté. Le volume anormal de 8,587 actions (vs moyenne 1,484) n'est pas expliqué par un catalyseur identifié dans les agents.

---

## Scoring Global (Agent Recommandation)

L'Agent Recommandation ne produit pas de score spécifique pour TEST (`data/recommandations_latest.json` liste 14 tickers, TEST est exclu). Le scoring ci-dessous est une attribution mécanique actualisée avec les nouvelles données techniques :

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 5.0/10 | 25% | 1.25 |
| **Score Opportunité** | **5.5/10** | — | **5.53** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé (score 2/10) |
| Malus FX | 0 | Non analysé |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (p-value insuffisante, `data/quant_2026-05-18.json` n=0) |
| Bonus / Timing | 0 | Timing défavorable (volume de distribution, close au plus bas) |
| **Score Global ajusté** | **54.5/100** | **ATTENDRE** |

**Comparaison vs précédent :** Le score global passe de 56.5 à 54.5 (-2.0 pts) sous l'effet de la détérioration technique : retrait du RSI (-5.69 pts), expansion de l'ATR (+6.4%), et surtout un volume de distribution massif (5.79×) sur séance baissière avec close au plus bas. Le momentum ajusté passe de 5.5 à 5.0/10. L'attribution reste un artefact heuristique en l'absence de données fondamentales et comptables.

---

## Niveaux et Ratio R/R

Niveaux révisés (ATR +6.4%, cours -2.80%) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.85 | — |
| Stop-loss (2× ATR) | $42.53 | Révisé vs $43.96 (13:00 UTC) |
| Stop-loss serré (1.5× ATR) | $43.11 | Révisé vs $44.51 (13:00 UTC) |
| Take-profit (3× ATR) | $48.33 | Révisé vs $49.41 (13:00 UTC) |
| Ratio R/R | 1.5 | Inchangé (3×ATR / 2×ATR) |

**Attention :** Le niveau de stop-loss serré (1.5× ATR = $43.11) est désormais très proche de la MM50 ($43.55). Une cassure combinée de ces deux niveaux amplifierait le risque de continuation baissière.

---

## Conclusion

**Verdict : ATTENDRE — Thèse INACTIVE, modifiée vers la prudence.**

La configuration technique s'est détériorée entre 13:00 UTC et 17:00 UTC :
- Baisse de -2.80% sur un volume 5.79× la moyenne 20j (vs 2.22× à 13:00 UTC)
- Structure de séance vendeuse : open = high, close = low, zero reprise intraday
- RSI en retrait de 64.16 à 58.47, momentum haussier affaibli
- Marge au-dessus de MM50 réduite de 5.97% à 2.98%

**Trois facteurs bloquants restent intacts :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle insuffisante** — volume moyen 20j < 2K actions, incompatible avec un sizing institutionnel malgré le spike ponctuel de 8,587
3. **Opacité fondamentale totale** — aucune donnée sectorielle, comptable ou de gouvernance

**Action recommandée :** Maintenir l'attente. Le spike de volume baissier sans catalyseur identifié est un signal de prudence. Sans données post-earnings ou fondamentales nouvelles, TEST reste hors périmètre institutionnel. Surveiller la tenue de MM50 ($43.55) — une cassure sous ce niveau avec volume élevé invaliderait toute thèse constructive de court terme.

**Niveau de confiance :** Très faible — l'analyse repose sur des proxies et des valeurs par défaut. Aucune donnée post-earnings observable à 17:00 UTC.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 17:00 UTC. Données : `data/2026-05-18.json`.*

# TEST — Mise à Jour Quotidienne (2026-05-18)

> **Date :** 2026-05-18
> **Heure snapshot :** 22:35 UTC
> **Sources :** `data/2026-05-18.json` (fetched_at 2026-05-18T22:35:56 UTC), `data/recommandations_2026-05-18.json`
> **Type :** Confirmation post-pipeline 22:35 UTC — snapshot final vs 21:23 UTC

---

## Résumé des Changements

| Métrique | 2026-05-18 21:23 UTC | 2026-05-18 22:35 UTC | Delta |
|----------|----------------------|----------------------|-------|
| Cours | $44.94 | **$44.94** | **Inchangé** |
| RSI 14j | 58.88 | **58.88** | Inchangé |
| ATR 14j | $1.10 | **$1.10** | Inchangé |
| MM 50j | $43.55 | $43.55 | Inchangé |
| Volume | 2,394 (2.04×) | **2,394 (2.04×)** | Inchangé |
| Score Opportunité (agent) | 5.9/10 | **5.9/10** | Inchangé |
| Score Global (agent) | 59.0/100 | **59.0/100** | Inchangé |
| Verdict agent reco | ATTENDRE | **ATTENDRE** | Confirmé |

**Événement majeur :** Aucun. Le snapshot 22:35 UTC confirme l'absence de changement vs 21:23 UTC. Cours inchangé à $44.94, volume et indicateurs techniques figés. Aucun résultat post-earnings n'est observable à 22:35 UTC bien que le calendrier FMP indique un earnings le 2026-05-18.

---

## Mise à Jour Technique

Configuration technique inchangée vs snapshot 21:23 UTC :
- **Cours :** $44.94 (open $45.92 / high $46.566 / low $46.144 / previous close $46.144)
- **Variation :** −2.62% vs veille
- **RSI 14j :** 58.88 — zone neutre avec léger avantage acheteur
- **ATR 14j :** $1.10 — volatilité contractée
- **MM 50j :** $43.55 — support dynamique intact, marge de sécurité +3.19%
- **MM 200j :** N/A
- **Volume relatif :** 2.04× moyenne 20j (2,394 vs 1,174) — profil normalisé post-spike de 17h
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette

**Verdict timing :** Neutre. Aucun mouvement technique significatif entre 21:23 et 22:35 UTC. La structure de séance reste identique : tentative de reprise intraday repoussée au high $46.566, clôture proche du low reflétant une faiblesse de clôture. Le maintien au-dessus de MM50 préserve la tendance haussière de court terme.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 22:35 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — toujours 🔴 Hors périmètre
- **Sector / Industry :** null / null — TAM et comps indérivables
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant

**Impact earnings du jour :** Aucun résultat post-earnings injecté dans les snapshots Yahoo/FMP à 22:35 UTC. La baisse de −2.62% sur la séance reste sans catalyseur fondamental identifié.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail détectée |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles dans `latest.json` |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism (`data/events_2026-05-18.json`) |
| **Geo Risk** | Non flaggé | Score politique 2/10 (`data/geo_2026-05-18.json`) — 🟢 |
| **FX Exposure** | Exposition 25%, impact 0% | DXY neutre, divergence alignée (`data/fx_exposure_2026-05-18.json`) |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-18 | JOUR J — résultats non observables à 22:35 UTC |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté.

---

## Scoring Global (Agent Recommandation)

Scores inchangés vs snapshot 21:23 UTC :

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 6.5/10 | 25% | 1.63 |
| **Score Opportunité** | **5.9/10** | — | **5.91** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé (score 2/10) |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (p-value insuffisante, n = 0) |
| Bonus / Timing | 0 | Timing neutre |
| **Score Global ajusté** | **59.0/100** | **ATTENDRE** |

**Proximité du seuil :** À 59.0/100, TEST reste à 1 point du seuil ACHETER réduit (60–74). Une confirmation technique (close > $46.00 avec volume soutenu) pourrait franchir ce seuil.

---

## Niveaux et Ratio R/R

Niveaux ajustés de l'Agent Recommandation (snapshot $44.94, ATR $1.10) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.94 | Snapshot 22:35 UTC |
| Stop-loss suggéré (2×ATR) | **$42.74** | −4.90% sous le cours |
| Take-profit suggéré (3×ATR) | **$48.24** | +7.34% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques complémentaires :**
- Support MM50 : $43.55 (−3.09%) — cassure = signal baissier de court terme
- Support 52W low : $40.27 (−10.39%)
- Résistance previous close : $46.144 (+2.68%)
- Résistance 52W high : $57.74 (+28.48%)

**Note :** Le stop-loss à $42.74 se situe sous MM50 ($43.55). Une cassure de MM50 ne déclencherait pas encore le SL mais constituerait un signal de prudence anticipé.

---

## Conclusion

**Verdict : ATTENDRE — Thèse INACTIVE, confirmée sans changement de configuration.**

Le snapshot 22:35 UTC confirme la stabilité observée à 21:23 UTC :
- Cours inchangé à $44.94 (−2.62% vs veille)
- Volume normalisé à 2.04× moyenne 20j
- RSI 58.88 neutre, ATR $1.10 contracté
- Score agent stable à 59.0/100 (ATTENDRE)

**Trois facteurs bloquants restent intacts :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle insuffisante** — volume moyen 20j < 2K actions
3. **Opacité fondamentale totale** — aucune donnée sectorielle, comptable ou de gouvernance

**Action recommandée :** Maintenir l'attente. La configuration technique est stable mais n'offre pas de catalyseur d'entrée. Surveiller la tenue de MM50 ($43.55) et un retour au-dessus de $46.00 (previous close) avec volume soutenu pour envisager une révision vers ACHETER réduit. Aucun résultat post-earnings observable à 22:35 UTC malgré la date earnings FMP.

**Niveau de confiance :** Très faible — l'analyse repose sur des proxies et des valeurs par défaut.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 22:35 UTC. Données : `data/2026-05-18.json`, `data/recommandations_2026-05-18.json`.*

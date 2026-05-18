# TEST — Mise à Jour Quotidienne (2026-05-18)

> **Date :** 2026-05-18
> **Heure snapshot :** 20:34 UTC
> **Sources :** `data/2026-05-18.json` (fetched_at 2026-05-18T20:34:17 UTC), `data/recommandations_2026-05-18.json`
> **Type :** Révision post-pipeline 20:34 UTC — stabilisation après le spike de distribution de 17h

---

## Résumé des Changements

| Métrique | 2026-05-18 17:00 UTC | 2026-05-18 20:34 UTC | Delta |
|----------|----------------------|----------------------|-------|
| Cours | $44.85 | **$44.94** | **+0.20%** |
| RSI 14j | 58.47 | **58.88** | **+0.41 pt** |
| ATR 14j | $1.16 | **$1.10** | **−5.2%** |
| MM 50j | $43.55 | $43.55 | Inchangé |
| Volume | 8,587 (5.79×) | **2,394 (2.04×)** | **−72.1%** |
| Score Opportunité (agent) | — | **5.9/10** | — |
| Score Global (agent) | 54.5/100 (heuristique) | **59.0/100** | **+4.5 pts** |
| Verdict agent reco | ATTENDRE | **ATTENDRE** | Confirmé |

**Événement majeur :** Aucun événement corporate détecté (`data/events_latest.json` = 0). Le spike de volume de 17h (8,587 actions, 5.79× moyenne) s'est complètement dissipé en fin de séance. Le cours s'est stabilisé à $44.94, en repli de −2.62% vs clôture précédente ($46.144) mais quasiment inchangé vs le snapshot 17h UTC. Aucun résultat post-earnings n'est observable à 20:34 UTC.

---

## Mise à Jour Technique

Configuration technique stabilisée vs snapshot 17:00 UTC :
- **Cours :** $44.94 (open $45.92 / high $46.566 / low $46.144 / previous close $46.144)
- **Variation :** −2.62% vs veille — repli limité dans la fourchette intraday
- **RSI 14j :** 58.88 — légère remontée vs 58.47, zone neutre avec un léger avantage acheteur conservé
- **ATR 14j :** $1.10 — volatilité en contraction (−5.2% vs 17h), retour à des niveaux plus sains
- **MM 50j :** $43.55 — support dynamique intact, marge de sécurité +3.19%
- **MM 200j :** N/A
- **Volume relatif :** 2.04× moyenne 20j (2,394 vs 1,174) — retour à un profil de liquidité normal après le spike de 17h
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette

**Verdict timing :** Neutre. La dissipation du volume anormal et la stabilisation du cours à $44.94 éteignent le signal de distribution observé à 17h. La structure de séance (high $46.566) montre une tentative de reprise intraday repoussée, mais la clôture proche du plus bas de la séance reflète une faiblesse de clôture. Le maintien au-dessus de MM50 ($43.55) préserve la tendance haussière de court terme. La contraction de l'ATR à $1.10 améliore le ratio risque/rendement des niveaux suggérés.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle n'est disponible dans le snapshot 20:34 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — toujours 🔴 Hors périmètre
- **Sector / Industry :** null / null — impossible de dériver un TAM ou des comps
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** [DONNÉES MANQUANTES] — rapport `data/accounting_risk_latest.json` inexistant

**Impact earnings du jour :** Aucun résultat post-earnings injecté dans les snapshots Yahoo/FMP à 20:34 UTC. Le calendrier FMP indiquait un earnings le 2026-05-18, mais l'absence de données fondamentales actualisées suggère soit un retard de publication, soit une société non couverte par les bases institutionnelles. La baisse de −2.62% sur la séance reste sans catalyseur fondamental identifié.

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
| **Upcoming Events** | [NON LISTÉ] | TEST absent du rapport `data/upcoming_events_2026-05-18.json` |

Aucun flux institutionnel, insider trade ou unusual options activity n'est rapporté. Le volume anormal de 17h n'a pas laissé de trace en fin de séance.

---

## Scoring Global (Agent Recommandation)

L'Agent Recommandation intègre TEST dans son rapport avec les scores suivants :

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
| Malus FX | 0 | Non analysé |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (p-value insuffisante, `data/quant_2026-05-18.json` n = 0) |
| Bonus / Timing | 0 | Timing neutre (stabilisation post-spike) |
| **Score Global ajusté** | **59.0/100** | **ATTENDRE** |

**Comparaison vs précédent :** Le score global passe de 54.5 (attribution heuristique 17h) à 59.0 (score agent 20:34), soit +4.5 pts. Cette amélioration reflète la stabilisation technique : le momentum remonte à 6.5/10 (vs 5.0/10 estimé à 17h), porté par la dissipation du volume de distribution et la conservation du RSI dans la zone neutre favorable. Le catalyseur reste stable à 6.5/10. La valorisation est inchangée à 5.0/10, pénalisée par l'absence totale de données fondamentales.

**Proximité du seuil :** À 59.0/100, TEST se situe à 1 point du seuil ACHETER réduit (60–74). Une confirmation technique supplémentaire (close > $46.00 avec volume soutenu) pourrait franchir ce seuil.

---

## Niveaux et Ratio R/R

Niveaux de l'Agent Recommandation (appliqués au cours snapshot $44.94) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.94 | Snapshot 20:34 UTC |
| Stop-loss suggéré (agent) | $42.81 | −4.74% sous le cours |
| Take-profit suggéré (agent) | $48.61 | +8.17% au-dessus du cours |
| Ratio R/R | 1.5 | Inchangé (agent) |
| R/R recalculé | 1.72 | Avec SL $42.81, TP $48.61, prix $44.94 |

**Niveaux techniques complémentaires :**
- Support MM50 : $43.55 (−3.09%) — cassure = signal baissier de court terme
- Support 52W low : $40.27 (−10.39%)
- Résistance previous close : $46.144 (+2.68%)
- Résistance 52W high : $57.74 (+28.48%)

**Attention :** Le niveau de stop-loss suggéré ($42.81) se situe sous MM50 ($43.55). Une cassure de MM50 ne déclencherait pas encore le SL, mais constituerait un signal de prudence.

---

## Conclusion

**Verdict : ATTENDRE — Thèse INACTIVE, confirmée avec une légère amélioration du score.**

La configuration technique s'est stabilisée entre 17:00 UTC et 20:34 UTC :
- Cours stable à $44.94 (+0.20% vs 17h, −2.62% vs veille)
- Retour du volume à un profil normal (2.04× moyenne vs 5.79× à 17h)
- RSI inchangé en zone neutre (58.88)
- ATR en contraction ($1.10), améliorant la qualité des niveaux
- Score agent : 59.0/100 (ATTENDRE), à 1 point du seuil ACHETER réduit

**Trois facteurs bloquants restent intacts :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle insuffisante** — volume moyen 20j < 2K actions, incompatible avec un sizing institutionnel
3. **Opacité fondamentale totale** — aucune donnée sectorielle, comptable ou de gouvernance

**Action recommandée :** Maintenir l'attente. La stabilisation post-spike est rassurante mais n'offre pas de catalyseur d'entrée. Le score à 59.0/100 montre une amélioration marginale mais insuffisante pour justifier une position. Surveiller la tenue de MM50 ($43.55) et un potentiel retour au-dessus de $46.00 (previous close) avec volume soutenu pour envisager une révision vers ACHETER réduit.

**Niveau de confiance :** Très faible — l'analyse repose sur des proxies et des valeurs par défaut. Aucune donnée post-earnings observable à 20:34 UTC.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 20:34 UTC. Données : `data/2026-05-18.json`, `data/recommandations_2026-05-18.json`.*

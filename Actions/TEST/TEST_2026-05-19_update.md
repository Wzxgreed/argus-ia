# TEST — Mise à Jour Post-Opening (2026-05-19)

> **Date :** 2026-05-19
> **Heure snapshot :** 13:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-19T13:00:10 UTC), `data/recommandations_2026-05-19.json`
> **Type :** Confirmation post-pipeline — snapshot vs close 2026-05-18

---

## Résumé des Changements

| Métrique | Snapshot 10:00 UTC | Snapshot 13:00 UTC | Delta |
|----------|-------------------|-------------------|-------|
| Cours | $44.935 | **$44.935** | **Inchangé** |
| RSI 14j | 58.87 | **58.87** | Inchangé |
| ATR 14j | $1.16 | **$1.16** | Inchangé |
| MM 50j | $43.55 | **$43.55** | Inchangé |
| Volume | 14,300 (8.08×) | **14,300 (8.08×)** | Inchangé |
| Score Opportunité (agent) | 5.9/10 | **5.9/10** | Inchangé |
| Score Global (agent) | 59.0/100 | **59.0/100** | Inchangé |
| Verdict agent reco | ATTENDRE | **ATTENDRE** | Confirmé |

**Événement :** Aucune variation technique, de volume ni de prix entre les deux snapshots intra-journaliers (10:00 → 13:00 UTC). Le cours reste figé à $44.935 avec un volume anormalement élevé à 8.08× la moyenne 20j — configuration atypique suggérant soit une suspension de cotation, soit un marché illiquide sans transactions post-opening. Earnings JOUR J (2026-05-19) — résultats toujours non injectés dans les snapshots à 13:00 UTC.

---

## Mise à Jour Technique

- **Cours :** $44.935 (open $45.92 / high $45.92 / low $44.85 / previous close $46.144)
- **Variation :** −2.62% vs veille
- **RSI 14j :** 58.87 — zone neutre, momentum ni suracheté ni survendu
- **ATR 14j :** $1.16 — volatilité inchangée
- **MM 50j :** $43.55 — support dynamique intact, marge de sécurité +3.19%
- **MM 200j :** N/A
- **Volume relatif :** 8.08× moyenne 20j (14,300 vs 1,770) — **spike de volume figé**
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette

**Verdict timing :** Neutre. L'absence totale de mouvement entre 10h et 13h UTC sur un titre affichant un volume 8× la normale est anormale. Hypothèses : (i) cotation suspendue ou limitée post-opening, (ii) marché OTC sans contrepartie, (iii) aucun ordre exécuté entre les deux snapshots malgré le volume initial. Le maintien au-dessus de MM50 préserve la tendance haussière de court terme.

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 13:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre
- **Sector / Industry :** null / null — TAM et comps indérivables
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant

**Impact earnings du jour :** Aucun résultat post-earnings injecté dans les snapshots Yahoo/FMP à 13:00 UTC. La baisse de −2.62% reste sans catalyseur fondamental identifié. Earnings JOUR J (2026-05-19) — résultats potentiellement publiés en dehors des horaires de marché US ou non encore propagés dans les flux de données.

---

## Mise à Jour Sentiment / Options / News

| Agent | Valeur TEST | Note |
|-------|-------------|------|
| **Social Sentiment** | 0 mentions, score 0/10, pas de pump | Aucune discussion retail détectée |
| **Options** | [DONNÉES MANQUANTES] | Max pain, GEX, IV Rank indisponibles dans `latest.json` |
| **Event-Driven** | 0 événement corporate | Aucun M&A, buyback, guidance change, activism (`data/events_latest.json`) |
| **Geo Risk** | Non flaggé | Score politique non spécifique pour TEST |
| **FX Exposure** | Exposition 25%, impact 0% | DXY neutre, divergence alignée (`data/fx_exposure_latest.json`) |
| **Consensus analystes** | [DONNÉES MANQUANTES] | Pas de price target ni upgrades/downgrades |
| **Upcoming Events** | Earnings 2026-05-19 | JOUR J — résultats non observables à 13:00 UTC |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté.

---

## Scoring Global (Agent Recommandation)

Scores inchangés vs snapshot 10:00 UTC :

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

**Proximité du seuil :** À 59.0/100, TEST reste à 1 point du seuil ACHETER réduit (60–74). La configuration technique stable mais inactive ne fournit pas de catalyseur d'entrée.

---

## Niveaux et Ratio R/R

Niveaux confirmés de l'Agent Recommandation (snapshot $44.94, ATR $1.16) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $44.94 | Snapshot 13:00 UTC |
| Stop-loss suggéré (2×ATR) | **$42.62** | −5.16% sous le cours |
| Take-profit suggéré (3×ATR) | **$48.41** | +7.72% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques complémentaires :**
- Support MM50 : $43.55 (−3.09%) — cassure = signal baissier de court terme
- Support 52W low : $40.27 (−10.39%)
- Résistance previous close : $46.144 (+2.68%)
- Résistance 52W high : $57.74 (+28.48%)

**Note :** Le stop-loss à $42.62 se situe sous MM50 ($43.55). Une cassure de MM50 ne déclencherait pas encore le SL mais constituerait un signal de prudence anticipé.

---

## Conclusion

**Verdict : ATTENDRE — Thèse INACTIVE, confirmée sans changement de configuration entre 10:00 et 13:00 UTC.**

Le snapshot 13:00 UTC 2026-05-19 confirme la parfaite stabilité des données techniques pour TEST :
- **Cours inchangé à $44.94** entre les deux snapshots intra-journaliers
- **Volume figé à 14,300** (8.08× moyenne 20j) — anomalie de liquidité
- **RSI 58.87 et ATR $1.16 inchangés**

L'absence de mouvement malgré un volume anormalement élevé suggère une cotation suspendue, limitée ou un marché sans contrepartie. Aucun catalyseur d'entrée n'est identifiable.

**Trois facteurs bloquants restent intacts :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Liquidité structurelle insuffisante** — volume moyen 20j < 2K actions
3. **Opacité fondamentale totale** — aucune donnée sectorielle, comptable ou de gouvernance

**Action recommandée :** Maintenir l'attente. La configuration technique est stable mais n'offre pas de catalyseur d'entrée. Surveiller :
- La tenue de MM50 ($43.55)
- Un retour au-dessus de $46.00 (previous close) avec volume soutenu
- Les résultats post-earnings (JOUR J) — si publiés hors séance

**Niveau de confiance :** Très faible — l'analyse repose sur des proxies et des valeurs par défaut.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 13:00 UTC. Données : `data/latest.json`, `data/recommandations_2026-05-19.json`.*

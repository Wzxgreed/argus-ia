# TEST — Mise à Jour Post-Session (2026-05-19)

> **Date :** 2026-05-19
> **Heure snapshot :** 17:00 UTC
> **Sources :** `data/latest.json` (fetched_at 2026-05-19T17:00:01 UTC), `data/recommandations_latest.json`
> **Type :** Mise à jour post-session — snapshot 17:00 UTC vs snapshot 13:00 UTC

---

## Résumé des Changements

| Métrique | Snapshot 13:00 UTC | Snapshot 17:00 UTC | Delta |
|----------|-------------------|-------------------|-------|
| Cours | $44.935 | **$43.395** | **−3.43%** |
| RSI 14j | 58.87 | **53.18** | **−5.69 pts** |
| ATR 14j | $1.16 | **$1.27** | +9.48% |
| MM 50j | $43.55 | **$43.53** | −0.05% |
| Volume | 14,300 (8.08×) | **1,597 (0.88×)** | **Normalisé — retour sous moyenne 20j** |
| Position vs MM50 | Au-dessus (+3.19%) | **En-dessous (−0.31%)** | **Signal baissier** |
| Score Opportunité (agent) | 5.9/10 | **5.4/10** | **−0.5 pt** |
| Score Global (agent) | 59.0/100 | **46.0/100** | **−13.0 pts** |
| Verdict agent reco | ATTENDRE | **SURVEILLER** | **Dégradé** |

**Événement majeur :** Cassure de la MM50 ($43.53) en fin de séance avec un gap-down de −3.04% à l'ouverture ($43.57 vs previous close $44.935). Le volume a totalement normalisé après le spike anormal du milieu de journée. L'Agent Recommandation a dégradé le verdict de **ATTENDRE → SURVEILLER** et le timing de **Neutre → Défavorable**. Earnings JOUR J — résultats toujours non observables dans les flux de données.

---

## Mise à Jour Technique

- **Cours :** $43.395 (open $43.57 / high $43.57 / low $43.16 / previous close $44.935)
- **Variation session :** −3.43% vs previous close
- **Variation cumulée :** −5.96% vs close 2026-05-18 ($46.144) — **deux sessions de baisse consécutives**
- **RSI 14j :** 53.18 — zone neutre, en retrait depuis 58.87, momentum refroidissant
- **ATR 14j :** $1.27 — volatilité en légère hausse (+9.5%) sur le mouvement d'après-midi
- **MM 50j :** $43.53 — **cassure en clôture** (cours −0.31% sous la MM50)
- **MM 200j :** N/A
- **Volume relatif :** 0.88× moyenne 20j (1,597 vs 1,814) — **retour à une liquidité normale après l'anomalie de 14,300 en début de séance**
- **52W range :** [$40.27, $57.74] — positionnement dans le bas de la fourchette, proche du support 52W low à +7.7%

**Verdict timing :** Défavorable. La cassure sous MM50 en clôture est un signal baissier de court terme. Le gap-down à l'ouverture a bloqué tout rebound intraday (high = open = $43.57, aucun plus haut de la journée). Configuration d'engulfing baissier : le cours a ouvert au plus haut et clôturé au plus bas de la fourchette intraday ($43.16–$43.57).

---

## Mise à Jour Fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 17:00 UTC :
- **Filtre Qualité (6 critères) :** 0/6 — 🔴 Hors périmètre (inchangé)
- **Sector / Industry :** null / null — TAM et comps indisponibles
- **P/E, Forward P/E, EV/EBITDA, P/B, Beta, Dividend Yield :** [DONNÉES MANQUANTES]
- **Short Interest, Float, Outstanding :** [DONNÉES MANQUANTES]
- **Agent Accounting :** rapport `data/accounting_risk_latest.json` inexistant
- **Validation données :** TEST non listé dans les [ERROR] ni [WARNING] du rapport de validation (22/25 OK)

**Impact earnings du jour :** Aucun résultat post-earnings injecté dans `latest.json` à 17:00 UTC. L'événement earnings (source FMP) reste non observable. La baisse de −3.43% en session pourrait refléter :
(i) anticipation négative pré-earnings, (ii) propagation tardive d'une news non capturée par Yahoo, ou (iii) mouvement technique sur faible liquidité. Aucune source institutionnelle ne confirme de catalyseur fondamental.

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
| **Upcoming Events** | Earnings 2026-05-19 — days_until 0 | JOUR J — résultats toujours non observables |
| **News Yahoo** | 0 article | Aucune news collectée pour TEST |

Aucun flux institutionnel, insider trade ou unusual options activity rapporté. L'absence totale de couverture analyste et de discussion retail rend l'interprétation du mouvement purement technique.

---

## Scoring Global (Agent Recommandation)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|--------------|
| Catalyseur | 6.5/10 | 35% | 2.28 |
| Valorisation | 5.0/10 | 40% | 2.00 |
| Momentum | 4.5/10 | 25% | 1.13 |
| **Score Opportunité** | **5.4/10** | — | **5.40** |

| Ajustement | Valeur | Note |
|-----------|--------|------|
| Malus Accounting | 0 | Pas de rapport |
| Malus Geo | 0 | Non flaggé |
| Malus FX | 0 | Impact nul |
| Malus Social | 0 | Sentiment neutre |
| Malus Quant | 0 | Pas de signal (n = 0) |
| Malus Timing | −8.0 | Cassure MM50 + gap-down + timing Défavorable |
| **Score Global ajusté** | **46.0/100** | **SURVEILLER** |

**Proximité des seuils :** À 46.0/100, TEST est passé sous le seuil ATTENDRE (50–59) et se situe dans la zone SURVEILLER (35–49). Le déclassement de 13 points est entièrement expliqué par la dégradation technique (cassure MM50, gap-down, momentum en retrait). Le Score Opportunité à 5.4/10 est inchangé dans sa structure (mêmes contributions C/V/M que le snapshot 10:00), mais le timing technique a basculé en négatif.

---

## Niveaux et Ratio R/R

Niveaux recalculés sur le snapshot 17:00 UTC (cours $43.40, ATR $1.27) :

| Niveau | Valeur | Note |
|--------|--------|------|
| Cours actuel | $43.40 | Snapshot 17:00 UTC |
| Stop-loss suggéré (2×ATR) | **$40.86** | −5.86% sous le cours |
| Take-profit suggéré (3×ATR) | **$47.21** | +8.78% au-dessus du cours |
| Ratio R/R | **1.5** | Standard agent |

**Niveaux techniques clés :**
- **Résistance MM50 :** $43.53 (+0.30%) — ancien support devenu résistance immédiate
- **Résistance gap :** $44.93 (+3.54%) — previous close, seuil de combler le gap-down
- **Résistance 52W high :** $57.74 (+33.04%)
- **Support 52W low :** $40.27 (−7.21%) — dernier niveau de défense avant zone de danger
- **Support psychologique :** $40.00 (−7.83%)

**Note :** Le stop-loss à $40.86 se situe juste au-dessus du 52W low ($40.27). Une cassure simultanée du SL et du 52W low confirmerait une tendance baissière de moyen terme.

---

## Conclusion

**Verdict : SURVEILLER — Thèse DÉGRADÉE de ATTENDRE → SURVEILLER suite à la cassure technique de la MM50.**

Le snapshot 17:00 UTC révèle une dégradation technique significative par rapport au snapshot 13:00 UTC :
- **Gap-down de −3.04%** à l'ouverture ($43.57 vs previous close $44.935)
- **Cassure de la MM50** en clôture ($43.40 vs MM50 $43.53) — signal baissier de court terme
- **RSI en retrait** de 58.87 à 53.18 — momentum haussier en refroidissement
- **Volume normalisé** à 1,597 (sous moyenne 20j) — le spike anormal de 14,300 était un artefact sans soutien institutionnel

**Trois facteurs bloquants renforcés :**
1. **Filtre Qualité 0/6** — aucun critère qualité vérifiable
2. **Timing technique Défavorable** — sous MM50, gap-down non comblé, aucun plus haut intraday
3. **Opacité fondamentale totale** — absence de données sectorielles, comptables, de gouvernance et de couverture analyste

**Action recommandée :**
- **Maintenir SURVEILLER.** Aucune entrée n'est justifiée tant que le cours ne regagne pas la MM50 ($43.53) avec volume supérieur à la moyenne 20j.
- **Seuil de réévaluation :** Retour au-dessus de $44.93 (previous close / combler le gap) + volume > 2,500
- **Seuil d'alerte baissière :** Cassure de $42.00 (niveau psychologique intermédiaire) ou retour sous $40.27 (52W low)

**Earnings JOUR J** : Les résultats restent non observables à 17:00 UTC. Sur publication post-marché ou demain, générer immédiatement un `_earnings.md` flash si les données FMP/Yahoo sont injectées.

**Niveau de confiance :** Très faible — l'analyse repose sur des proxies et des valeurs par défaut. La volatilité sur faible liquidité amplifie le risque de faux signaux.

---

*Généré automatiquement par le pipeline Argus-IA — snapshot 17:00 UTC. Données : `data/latest.json`, `data/recommandations_latest.json`, `data/validation_report.txt`.*

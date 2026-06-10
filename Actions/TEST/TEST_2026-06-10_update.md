# TEST — Mise à jour quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-10
> **Type :** Mise à jour post-pipeline matin
> **Source :** data/latest.json (snapshot 10:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-09 21h UTC | 2026-06-10 10h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | $43.87 | **NaN** | **[DONNÉES MANQUANTES]** 🔴 |
| Previous close | $45.35 | $45.35 | — |
| RSI 14j | 50.48 | **57.17** | **+6.69 pts** 🟢 |
| MM 50j | $43.67 | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| MM 200j | — | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| ATR 14j | $1.07 | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| Volume session | 1,570 | **1,570** | Stable |
| Volume vs avg 20j | 0.64× | **0.64×** | Stable |
| Score Global | 59.0 (64.0 ajusté) | **57.8** | **−1.2 pts** 🔴 |
| Score Global Ajusté | 64.0 | **57.8** | **−6.2 pts** 🔴 |
| Score Opportunité | 5.9/10 | **5.8/10** | **−0.1 pt** 🔴 |
| Score Momentum | 6.5/10 | **6.0/10** | **−0.5 pt** 🔴 |
| Verdict | ACHETER (Réduit) | **ATTENDRE** | **Dégradation** 🔴 |
| SL | $41.73 | **null** | **[DONNÉES MANQUANTES]** |
| TP | $47.08 | **null** | **[DONNÉES MANQUANTES]** |

**Données techniques partielles.** Le snapshot 10h UTC du 2026-06-10 ne fournit pas de cours de clôture pour TEST (champ `close` = NaN). Le `previous_close` est maintenu à $45.35. Le RSI remonte de 6.69 pts à 57.17, confirmant un momentum neutre-haussier, mais les données de moyennes mobiles (MM50, MM200) et de volatilité (ATR14) sont absentes (`null`). L'agent de recommandations a dégradé le verdict de **ACHETER (Réduit)** à **ATTENDRE**, malgré la hausse du RSI, probablement en raison de l'indisponibilité des niveaux techniques et de la persistance du flag earnings JOUR J non résolu.

---

## Mise à jour technique

- **Cours :** NaN — pas de donnée de clôture disponible dans le snapshot. Previous close : $45.35.
- **RSI 14j :** 57.17, en hausse de 6.69 pts vs snapshot 21h UTC du 09/06. Franchissement du seuil de 55 — momentum neutre-haussier renforcé.
- **MM 50j / MM 200j :** `null` — données manquantes. Impossible d'évaluer le positionnement par rapport aux moyennes mobiles.
- **ATR 14j :** `null` — données manquantes. Impossible de calculer les niveaux de stop-loss/take-profit via la méthode ATR.
- **Volume :** 1,570 unités (0.64× moyenne 20j de 2,463). Volume inchangé vs close 09/06, toujours très contraint.
- **Range 52 semaines :** $40.27–$57.74. Sans cours actuel, impossible de situer le niveau relatif.

**Verdict timing :** Neutre. Le RSI remonte favorablement, mais l'absence de cours, de MM50 et d'ATR rend toute évaluation de timing non fiable. [DONNÉES PARTIELLES]

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle dans le snapshot 10h UTC. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-10, source FMP, `days_until = 0`) — le flag persiste pour la 10e+ journée consécutive sans résolution. L'hypothèse d'un artefact de calendrier FMP est désormais la plus probable. Aucun résultat observable.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-10, snapshot 10h UTC) :

| Axe | Score 09/06 21h | Score 10/06 10h | Δ |
|-----|----------------|----------------|---|
| Catalyseur | 6.5/10 | 6.5/10 | Stable |
| Valorisation | 5.0/10 | 5.0/10 | Stable |
| Momentum | 6.5/10 | **6.0/10** | **−0.5 pt** 🔴 |
| Opportunité | 5.9/10 | **5.8/10** | **−0.1 pt** 🔴 |

**Modules agents (snapshot 10h UTC) :**
- `quant_report_latest.json` (2026-05-17) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-05-17) : aucun flag géopolitique pour TEST.
- `accounting_risk_latest.json` (2026-06-10) : fichier absent.
- `sector_rotation_latest.json` (2026-06-10) : régime UNKNOWN, signal NEUTRAL. TEST sans secteur assigné.
- `social_sentiment_latest.json` (2026-06-10) : 0 mention, sentiment « No data », pas de pump.
- `fx_exposure_latest.json` (2026-06-10) : exposition FX 25%, impact score 0.0, divergence aligned.
- `events_latest.json` (2026-06-10) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-10) : earnings JOUR J (2026-06-10, source FMP, days_until = 0) — toujours non résolu.

---

## Nouveau scoring global

| Métrique | Valeur |
|----------|--------|
| Score Opportunité | 5.8/10 |
| Score Catalyseur | 6.5/10 |
| Score Valorisation | 5.0/10 |
| Score Momentum | 6.0/10 |
| Score Global | 57.8/100 |
| Score Global Ajusté | 57.8/100 |
| Verdict | **ATTENDRE** |
| Timing | Neutre |
| Horizon | — |

Le Score Global est passé de 59.0 à **57.8/100**, sortant de la fourchette **ACHETER (Réduit)** (60–74) pour revenir en **ATTENDRE** (50–59). La dégradation est portée par la baisse du Score Momentum (−0.5 pt, de 6.5 à 6.0), malgré une hausse du RSI, probablement due à l'indisponibilité des données de cours et de volatilité dans le snapshot. La règle de disqualification n'est pas activée (aucun score ≤ 2/10).

---

## Révision des niveaux SL / TP

**Révision impossible** — l'ATR 14j est `null` et le cours close est `NaN` dans le snapshot 10h UTC. Les niveaux antérieurs ($41.73 / $47.08, basés sur un cours de $43.87 et un ATR de $1.07) ne peuvent pas être recalculés ni validés sans données fraîches.

| Niveau | Ancien (09/06 21h) | Nouveau (10/06 10h) | Statut |
|--------|-------------------|--------------------|--------|
| Stop-loss | $41.73 | **null** | [DONNÉES MANQUANTES] |
| Take-profit | $47.08 | **null** | [DONNÉES MANQUANTES] |
| Ratio R/R | 1.5 | **null** | [DONNÉES MANQUANTES] |

---

## Conclusion — Thèse dégradée

**La thèse est DÉGRADÉE : passage ACHETER (Réduit) → ATTENDRE.**

**Raisons de la dégradation :**
1. **Données techniques partielles** : le snapshot ne fournit ni cours de clôture, ni ATR, ni moyennes mobiles. L'impossibilité de positionner le ticker techniquement invalide le signal de reclaim de MM50 observé hier.
2. **Dégradation mécanique des scores** : Score Momentum −0.5 pt, Score Global −1.2 pt. L'agent reco a automatiquement reclassé le verdict en ATTENDRE.
3. **Earnings JOUR J persistant** : le flag FMP (2026-06-10, days_until = 0) n'a toujours pas été résolu après plus de 10 jours de survenance. Risque d'artefact élevé, mais l'incertitude technique prime.

**Points de vigilance :**
- **Illiquidité extrême** : volume 1,570 (0.64× moyenne 20j). Sur un ticker microstructure aussi fine, tout signal technique est fragile.
- **Absence de données fondamentales** : impossible d'établir une thèse qualitative. TEST reste un ticker de test / cohérence flux.
- **RSI 57.17** : si le cours était confirmé au-dessus de la MM50 (lorsque disponible), le momentum serait favorable. Toutefois, sans prix ni ATR, cette lecture reste speculative.
- Si retour des données avec cours < MM50 sur volume > moyenne → maintien **ATTENDRE** voire **SURVEILLER**.
- Si retour des données avec cours confirmé au-dessus des mobiles et volume > 1.0× avg → regradation possible **ACHETER (Réduit)**.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 10h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*

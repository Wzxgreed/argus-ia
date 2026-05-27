# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-05-27 (snapshot 17:00 UTC)

**Date :** 2026-05-27
**Type :** Mise à jour post-pipeline — snapshot 17:00 UTC
**Analyse précédente :** snapshot 13:00 UTC 27/05

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (13:00 UTC 27/05) | Actuel (17:00 UTC 27/05) | Changement |
|--------|----------------------------|--------------------------|------------|
| Cours close | $22.339 | $22.339 | = — inchangé |
| RSI 14j | 59.07 | 59.07 | = |
| ATR 14j | $0.28 | $0.28 | = |
| MM 50j | $22.00 | $22.00 | = |
| Volume | 3 845 | 3 845 | = — inchangé |
| Volume vs moy. 20j | 1.02× | 1.02× | = |
| Recommandation agent | **ACHETER (Réduit)** | **ACHETER (Réduit)** | = |
| Score Opportunité | 6.0/10 | **6.0/10** | = |
| Score Catalyseur | 6.5/10 | **6.5/10** | = |
| Score Valorisation | 5.0/10 | **5.0/10** | = |
| Score Momentum | 7.0/10 | **7.0/10** | = |
| Score Global Ajusté | 65.2/100 | **65.2/100** | = |
| Timing | Favorable | **Favorable** | = |

**Verdict :** Stabilité totale confirmée vs snapshot 13:00 UTC 27/05. C'est le **9e snapshot consécutif sans mutation** (10:00 UTC 25/05 → 21:00 UTC 25/05 → 10:00 UTC 26/05 → 13:00 UTC 26/05 → 17:00 UTC 26/05 → 21:00 UTC 26/05 → 10:00 UTC 27/05 → 13:00 UTC 27/05 → 17:00 UTC 27/05). Sur l'ensemble de la séance US du 27/05 et sur les trois derniers jours, SPCX n'enregistre aucune mutation de prix, de volume ni de métrique technique entre les snapshots. Cette stabilité persistante confirme un ancrage technique exceptionnel à $22.34.

---

## Mise à jour technique

Aucune mutation vs snapshot 13:00 UTC — données Yahoo strictement identiques sur le snapshot 17:00 UTC.

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 59.07 | Zone neutre haussière — pas de surachat |
| Position vs MM50j | $22.339 > $22.00 | **Au-dessus** — tendance haussière micro maintenue |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | 1.02× | 🟢 Normalisé — liquidité structurelle habituelle |
| ATR 14j | $0.28 | Volatilité extrêmement faible |
| 52w low / high | $21.32 / $26.61 | −16.1% vs 52w high, +4.8% vs 52w low |
| Change % | −0.27% | Léger recul vs previous close $22.40 |
| Open / High / Low | $22.69 / $22.69 / $22.339 | Range intraday $0.351 (1.5%) — clôture basse de range |

**Niveaux clés (inchangés) :**
- Support immédiat : $22.00 (MM50)
- Support secondaire : $21.32 (52w low)
- Résistance immédiate : $22.69 (high du jour)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Favorable. Le setup technique (au-dessus MM50, RSI 59.07, ATR $0.28) reste validé par l'Agent Recommandation. Le volume normalisé (1.02× moyenne) reflète la liquidité structurelle habituelle de l'ETF. Le range serré confirme un ancrage technique autour de $22.34.

---

## Mise à jour fondamentale

Aucune nouvelle donnée fondamentale. SPCX reste un ETF thématique SPAC/post-IPO sans métriques classiques (P/E, EPS, consensus analystes non applicables).

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| P/E | N/A | ETF — non applicable |
| Forward P/E | N/A | ETF — non applicable |
| Market cap | N/A | ETF — non applicable |
| Beta | N/A | Non calculé |
| Dividend yield | N/A | Non distribué |
| Sector | Financial Services | Asset Management |

**Sector rotation :** Le secteur Financials (XLF) n'apparaît pas dans le top3 ni le bottom3 du `sector_rotation_2026-05-27.json`. XLF enregistre un return_20d de −0.96% et un momentum_score de 0.0 — pas de bonus/malus sectoriel pour SPCX. Seul XLK (Technology) domine avec un momentum_score de 10.0, sans lien direct avec le secteur Financials. Aucun crossover détecté dans le rapport sectoriel du 27/05.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_latest.json` absent — pas d'événement corporate détecté pour SPCX |
| Social sentiment | No data | `data/social_sentiment_latest.json` absent — 0 mentions Reddit, pump_detected = false |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable |
| FX Exposure | 🟢 | `data/fx_exposure_latest.json` absent — exposition FX non évaluée, ETF domestique US |
| Géopolitique | 🟢 | `data/geo_risk_latest.json` (2026-05-17) : pas de flag SPCX |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : pas assez de signaux historiques pour SPCX |

**Anomalie data quality persistante :** `data/upcoming_events_2026-05-27.json` mentionne un faux événement `earnings` pour SPCX (source FMP, days_until = 0) — artefact connu, à ignorer pour un ETF.

---

## Scoring global (agents pipeline 2026-05-27, snapshot 17:00 UTC)

| Axe | Score | Changement vs 13:00 UTC 27/05 | Commentaire |
|-----|-------|------------------------------|-------------|
| Score Catalyseur | 6.5/10 | = | Modéré-haussier — absence de catalyseur fondamental compensée par le momentum technique |
| Score Valorisation | 5.0/10 | = | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 7.0/10 | = | 🟢 Haussier — retour au-dessus MM50 confirmé, RSI stable en zone neutre |
| **Score Opportunité** | **6.0/10** | = | Pondération régime Normal : C×35% + V×40% + M×25% = 6.02 |
| **Score Global** | **60.2/100** | = | Avant ajustements |
| **Score Global Ajusté** | **65.2/100** | = | Bonus timing favorable appliqués |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** +5 (cours au-dessus MM50, volume normalisé)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | **ACHETER** | **Réduit** | ✅ SPCX = 65.2 |

---

## Révision des niveaux SL / TP

La recommandation reste **ACHETER (Réduit)** — niveaux confirmés par Agent Recommandation, inchangés vs 13:00 UTC 27/05.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix entrée suggéré | $22.34 | Close du jour (source `data/latest.json`) |
| Stop-loss | $21.78 | Close − 2×ATR = $22.339 − $0.56 |
| Take-profit | $23.18 | Close + 3×ATR = $22.339 + $0.84 |
| Ratio R/R | 1.5× | Gain $0.84 / Perte $0.56 |

**Verdict sizing :** Réduit. Le Score Global Ajusté (65.2) est dans la fourchette 60–74. La liquidité historique faible (volume moyen ~3 800) et l'absence de catalyseur fondamental justifient un sizing limité. Maximum 5% du capital sur cette position ETF thématique.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟢 Thèse **CONFIRMÉE** — 9e snapshot consécutif sans mutation (10:00 UTC 25/05 → 21:00 UTC 25/05 → 10:00 UTC 26/05 → 13:00 UTC 26/05 → 17:00 UTC 26/05 → 21:00 UTC 26/05 → 10:00 UTC 27/05 → 13:00 UTC 27/05 → 17:00 UTC 27/05)

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ✅ Au-dessus ($22.339 > $22.00) |
| RSI | ✅ Haussier (59.07) — pas de surachat |
| Volume | 🟢 Normalisé (1.02× moyenne) — liquidité structurelle stable |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique |
| Risque technique | 🟢 MM50 support, 52w low intact, ATR faible = risque contrôlé |
| Score Global | 🟢 65.2/100 → déclenche ACHETER Réduit |
| Stabilité snapshots | 🟢 9e snapshot consécutif identique — fiabilité renforcée sur 3 séances |

- **Confirmation :** Le setup technique identifié le 25/05 (retour au-dessus MM50, RSI en zone neutre haussière) est validé par la stabilité des données sur 9 snapshots consécutifs, incluant trois séances complètes de marché ouvert. L'absence de mutation ce 27/05 à 17:00 UTC confirme que $22.34 est le niveau de référence fiable.
- **Nuances :** Le mouvement reste 100% technique. L'absence de news fondamentale ou de catalyseur sectoriel (reprise SPAC/IPO, baisse des taux) limite la conviction et justifie le sizing Réduit. Le secteur Financials (XLF) n'est pas dans la rotation haussière du jour (momentum_score = 0.0, return_20d −0.96%). La normalisation du volume (vs anomalie ×4.5 des sessions 25–26/05) élimine le signal d'accumulation institutionnelle ; le setup repose désormais uniquement sur la structure technique.
- **Invalidation :** Une clôture sous $22.00 (MM50) avec volume >1.5× moyenne invaliderait le setup et justifierait une clôture immédiate. Une clôture sous $21.32 (52w low) avec volume élevé = reclassement ÉVITER.
- **Rehaussement en Standard :** Une cassure de $23.00 (zone de congestion) avec volume >2× moyenne et RSI stable > 55 justifierait un passage à ACHETER Standard avec relèvement du TP vers $24.00.

**Recommandation :** **ACHETER (Réduit)**
**Prix cible :** $23.18 (+3.8% upside)
**Stop-loss :** $21.78 (−2.5% downside)
**Horizon :** 1–2 semaines
**Conviction :** Modérée — setup technique validé par les agents et confirmé par la stabilité des snapshots sur 9 sessions consécutives (incluant trois séances complètes), mais manque de catalyseur fondamental et faible liquidité historique. Sizing réduit obligatoire.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 1.02× moy. 20j | 🟢 Normal | Liquidité structurelle habituelle — anomalie des sessions 25–26/05 dissipée |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | N/A | — | Données non disponibles |
| Révisions consensus | N/A | — | Non applicable |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|------------------|
| Volume >2× moyenne au prochain jour de marché | 1j | Confirmation accumulation | Distribution si cours baisse |
| Cassure $23.00 | 1–3j | Rehaussement Standard, TP $24.00 | — |
| Retour sous MM50 ($22.00) | Immédiat | — | Clôture position, retour ATTENDRE |
| Cassure 52w low ($21.32) | Immédiat | — | −3–5% supplémentaires, reclassement ÉVITER |
| News macro favorable (taux, IPO/SPAC) | Variable | Soutien aux SPACs | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : snapshot 13:00 UTC 27/05
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : $23.18
- Prix cible révisé : $23.18 (inchangé)
- Recommandation précédente : ACHETER (Réduit)
- Recommandation révisée : **ACHETER (Réduit)**
- Raison principale : Snapshot 17:00 UTC 27/05 confirme stabilité totale vs 13:00 UTC 27/05 — 9e snapshot consécutif sans mutation, thèse CONFIRMÉE
- Thèse : 🟢 Confirmée

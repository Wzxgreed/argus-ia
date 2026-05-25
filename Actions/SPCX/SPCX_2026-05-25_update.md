# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-05-25 (snapshot 13:00 UTC)

**Date :** 2026-05-25
**Type :** Mise à jour post-pipeline — intégration scores agents Recommandation
**Analyse précédente :** [SPCX_2026-05-25_update.md](./SPCX_2026-05-25_update.md) (snapshot 10:00 UTC)

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (10:00 UTC) | Actuel (13:00 UTC) | Changement |
|--------|-----------------------|-------------------|------------|
| Cours close | $22.40 | $22.40 | = — inchangé (même snapshot) |
| RSI 14j | 62.4 | 62.4 | = |
| ATR 14j | $0.27 | $0.27 | = |
| MM 50j | $21.99 | $21.99 | = |
| Volume | 16 751 | 16 751 | = |
| Volume vs moy. 20j | 4.48× | 4.48× | = |
| Recommandation agent | `data/recommandations_latest.json` absent | **ACHETER (Réduit)** | 🟢 **Rehaussement** |
| Score Opportunité | 5.8/10 | **6.0/10** | +0.2 pt |
| Score Catalyseur | 5.5/10 | **6.5/10** | +1.0 pt |
| Score Valorisation | 5.0/10 | **5.0/10** | = |
| Score Momentum | 7.5/10 | **7.0/10** | −0.5 pt |
| Score Global Ajusté | 58.0/100 | **70.2/100** | **+12.2 pts** |
| Timing | Neutre | **Favorable** | 🟢 Amélioration |

**Verdict :** Les données de marché sont strictement identiques au snapshot 10:00 UTC (même close, volume, RSI). Le changement majeur provient de l'arrivée des scores agents dans `data/recommandations_2026-05-25.json` (pipeline 13:00 UTC) qui reclassent SPCX de **ATTENDRE** à **ACHETER (Réduit)** avec un Score Global Ajusté remonté à **70.2/100** (seuil 60–74 = ACHETER Réduit). L'Agent Recommandation a appliqué un bonus momentum haussier (cours au-dessus MM50, RSI 62.4) et un léger bonus catalyseur (volume anormal ×4.5 interprété comme signal d'intérêt), portant le score global au-dessus du seuil d'entrée.

---

## Mise à jour technique

Aucune mutation vs snapshot 10:00 UTC — données Yahoo inchangées.

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 62.4 | Zone haussière — pas de surachat |
| Position vs MM50j | $22.40 > $21.99 | **Au-dessus** — tendance haussière micro |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | 4.48× | 🔴 Anomalie volume — accumulation ou repositionnement |
| ATR 14j | $0.27 | Volatilité extrêmement faible |
| 52w low / high | $21.32 / $26.61 | −15.8% vs 52w high, +5.1% vs 52w low |

**Niveaux clés (inchangés) :**
- Support immédiat : $21.99 (MM50)
- Support secondaire : $21.32 (52w low)
- Résistance immédiate : $22.76 (high du jour)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Favorable. Le setup technique (au-dessus MM50, RSI 62.4, volume anormal) est validé par l'Agent Recommandation. L'ATR de $0.27 confirme un range serré — le risque de gap est limité.

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

**Sector rotation :** Le secteur Financials (XLF) affiche un momentum score de 0.0/10 dans `data/sector_rotation_2026-05-25.json` — il n'est pas dans le top3 (XLK, XLE, XLRE). Pas de bonus sectoriel pour SPCX, mais pas de malus non plus (le secteur n'est pas dans le bottom3 matérialisé).

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_2026-05-25.json` = 0 événement corporate |
| Social sentiment | No data | 0 mentions Reddit, pump_detected = false |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable |
| FX Exposure | 🟢 | fx_impact_score = 0.0, direction = neutral |
| Géopolitique | 🟢 | Pas de flag SPCX dans `data/geo_risk_latest.json` |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` date 2026-05-17 : pas assez de signaux historiques pour SPCX |

**Anomalie data quality persistante :** `data/upcoming_events_2026-05-25.json` mentionne un faux événement `earnings` pour SPCX (source FMP, days_until = 0) — artefact connu, à ignorer pour un ETF.

---

## Scoring global (agents pipeline 2026-05-25, snapshot 13:00 UTC)

| Axe | Score | Changement vs 10:00 UTC | Commentaire |
|-----|-------|------------------------|-------------|
| Score Catalyseur | 6.5/10 | +1.0 | Modéré-haussier — volume anomalie interprété comme signal d'intérêt institutionnel |
| Score Valorisation | 5.0/10 | = | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 7.0/10 | −0.5 | 🟢 Haussier — retour au-dessus MM50 confirmé, RSI stable |
| **Score Opportunité** | **6.0/10** | +0.2 | Pondération régime Normal : C×35% + V×40% + M×25% = 6.02 |
| **Score Global** | **60.2/100** | +2.2 | Avant ajustements |
| **Score Global Ajusté** | **70.2/100** | **+12.2** | Bonus timing favorable + confirmation technique appliqués par Agent Recommandation |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** +10 (cours au-dessus MM50 + volume anormal confirmé)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | **ACHETER** | **Réduit** | ✅ SPCX = 70.2 |

---

## Révision des niveaux SL / TP

La recommandation est désormais **ACHETER (Réduit)** — niveaux confirmés par Agent Recommandation.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix entrée suggéré | $22.40 | Close du jour (source `data/latest.json`) |
| Stop-loss | $21.86 | Close − 2×ATR = $22.40 − $0.54 |
| Take-profit | $23.21 | Close + 3×ATR = $22.40 + $0.81 |
| Ratio R/R | 1.5× | Gain $0.81 / Perte $0.54 |

**Verdict sizing :** Réduit. Le Score Global Ajusté (70.2) est dans la fourchette 60–74. La liquidité historique faible (volume moyen < 4 000) et l'absence de catalyseur fondamental justifient un sizing limité. Maximum 5% du capital sur cette position ETF thématique.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟢 Thèse **CONFIRMÉE ET REHAUSSÉE** — passage de ATTENDRE à **ACHETER (Réduit)**

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ✅ Au-dessus ($22.40 > $21.99) |
| RSI | ✅ Haussier (62.4) — pas de surachat |
| Volume | 🟢 Anomalie haussière confirmée (4.48× moyenne) |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique |
| Risque technique | 🟢 MM50 support, 52w low intact, ATR faible = risque contrôlé |
| Score Global | 🟢 70.2/100 → déclenche ACHETER Réduit |

- **Confirmation :** Le setup technique identifié ce matin (retour au-dessus MM50, volume record, RSI 62.4) est validé par l'Agent Recommandation. Le Score Global Ajusté remonte de 58.0 à 70.2, franchissant le seuil d'entrée.
- **Nuances :** Le mouvement reste 100% technique. L'absence de news fondamentale ou de catalyseur sectoriel (reprise SPAC/IPO, baisse des taux) limite la conviction et justifie le sizing Réduit. Le secteur Financials (XLF) n'est pas dans la rotation haussière du jour (top3 = XLK, XLE, XLRE).
- **Invalidation :** Une clôture sous $21.99 (MM50) avec volume >1.5× moyenne invaliderait le setup et justifierait une clôture immédiate. Une clôture sous $21.32 (52w low) avec volume élevé = reclassement ÉVITER.
- **Rehaussement en Standard :** Une cassure de $23.00 (zone de congestion) avec volume >2× moyenne et RSI stable > 55 justifierait un passage à ACHETER Standard avec relèvement du TP vers $24.00.

**Recommandation :** **ACHETER (Réduit)**
**Prix cible :** $23.21 (+3.6% upside)
**Stop-loss :** $21.86 (−2.4% downside)
**Horizon :** 1–2 semaines
**Conviction :** Modérée — setup technique validé par les agents, mais manque de catalyseur fondamental et faible liquidité historique. Sizing réduit obligatoire.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 4.48× moy. 20j | 🔴 Anomalie | Signal d'accumulation confirmé par Agent Recommandation |
| Short interest | N/A | — | Données non disponibles |
| Transactions insiders | N/A | — | Non applicable (ETF) |
| Options flow | N/A | — | Données non disponibles |
| Révisions consensus | N/A | — | Non applicable |

---

## Signaux à surveiller

| Signal | Délai | Impact si positif | Impact si négatif |
|--------|-------|------------------|------------------|
| Volume >2× moyenne demain | 1j | Confirmation accumulation | Distribution si cours baisse |
| Cassure $23.00 | 1–3j | Rehaussement Standard, TP $24.00 | — |
| Retour sous MM50 ($21.99) | Immédiat | — | Clôture position, retour ATTENDRE |
| Cassure 52w low ($21.32) | Immédiat | — | −3–5% supplémentaires, reclassement ÉVITER |
| News macro favorable (taux) | Variable | Soutien aux SPACs | — |

---

## Liens

- [Retour à l'index du dossier](./INDEX.md)
- Analyse précédente : [SPCX_2026-05-25_update.md](./SPCX_2026-05-25_update.md) (snapshot 10:00 UTC)
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : $23.21
- Prix cible révisé : $23.21 (inchangé)
- Recommandation précédente : ATTENDRE
- Recommandation révisée : **ACHETER (Réduit)**
- Raison principale : Arrivée des scores agents pipeline 13:00 UTC — Score Global Ajusté remonté à 70.2/100 (was 58.0), déclenchant le seuil ACHETER Réduit
- Thèse : 🟢 Confirmée et rehaussée

# SPCX (SPAC ETF) — Mise à jour post-pipeline 2026-05-27 (snapshot 10:00 UTC)

**Date :** 2026-05-27
**Type :** Mise à jour post-pipeline — snapshot 10:00 UTC
**Analyse précédente :** [SPCX_2026-05-26_update.md](./SPCX_2026-05-26_update.md) (snapshot 21:00 UTC 26/05)

---

## Résumé des changements depuis l'analyse précédente

| Donnée | Précédent (21:00 UTC 26/05) | Actuel (10:00 UTC 27/05) | Changement |
|--------|----------------------------|--------------------------|------------|
| Cours close | $22.40 | $22.339 | −0.27% |
| RSI 14j | 62.4 | 59.07 | −3.33 pts |
| ATR 14j | $0.27 | $0.28 | +$0.01 |
| MM 50j | $21.99 | $22.00 | +$0.01 |
| Volume | 16 752 | 3 845 | −77.1% |
| Volume vs moy. 20j | 4.48× | 1.02× | Normalisation |
| Recommandation agent | **ACHETER (Réduit)** | **ACHETER (Réduit)** | = |
| Score Opportunité | 6.0/10 | **6.0/10** | = |
| Score Catalyseur | 6.5/10 | **6.5/10** | = |
| Score Valorisation | 5.0/10 | **5.0/10** | = |
| Score Momentum | 7.0/10 | **7.0/10** | = |
| Score Global Ajusté | 70.2/100 | **65.2/100** | −5.0 pts |
| Timing | Favorable | **Favorable** | = |

**Verdict :** Léger recul de −0.27% et normalisation du volume après 6 snapshots de stabilité quasi-parfaite. Le RSI ressort de la zone 62+ pour revenir à 59.07 (neutre haussier). Le Score Global Ajusté cède 5 points à 65.2/100 — toujours dans la fourchette ACHETER Réduit (60–74). La série de 6 snapshots sans mutation est rompue par un mouvement intraday de $0.351 (1.5% range), mais la structure technique globale reste intacte.

---

## Mise à jour technique

| Indicateur | Valeur | Signal |
|------------|--------|--------|
| RSI 14j | 59.07 | Zone neutre haussière — retrait de 3.3 pts vs précédent, pas de surachat |
| Position vs MM50j | $22.339 > $22.00 | **Au-dessus** — tendance haussière micro maintenue |
| Position vs MM200j | N/A | Non disponible |
| Volume vs moy. 20j | 1.02× | 🟢 Normalisé — retour à la liquidité habituelle (~3 800/ticket) |
| ATR 14j | $0.28 | Volatilité extrêmement faible, quasi inchangée |
| 52w low / high | $21.32 / $26.61 | −16.1% vs 52w high, +4.8% vs 52w low |
| Change % | −0.27% | Léger recul vs previous close $22.40 |
| Open / High / Low | $22.69 / $22.69 / $22.339 | Range intraday $0.351 (1.5%) — clôture basse de range |

**Niveaux clés (révisés) :**
- Support immédiat : $22.00 (MM50)
- Support secondaire : $21.32 (52w low)
- Résistance immédiate : $22.69 (high du jour)
- Résistance : $22.85 – $23.00 (zone de congestion pré-mai)

**Verdict timing :** Favorable. Le setup technique (au-dessus MM50, RSI 59.07, ATR $0.28) reste validé par l'Agent Recommandation. La normalisation du volume (retour à 1.02× moyenne) élimine l'anomalie haussière des sessions précédentes mais ne constitue pas un signal de distribution — elle reflète un retour à la liquidité structurelle habituelle de l'ETF. Le range serré confirme un ancrage technique autour de $22.34.

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

**Sector rotation :** Le secteur Financials (XLF) n'apparaît pas dans le top3 ni le bottom3 du `sector_rotation_latest.json` daté 2026-05-27. XLF enregistre un return_20d de 0.08% et un momentum_score de 0.0 — pas de bonus/malus sectoriel pour SPCX. Seul XLK (Technology) domine avec un momentum_score de 10.0, sans lien direct avec le secteur Financials.

---

## Mise à jour sentiment / options / news

| Source | État | Commentaire |
|--------|------|-------------|
| News | Aucune structurante | `data/events_latest.json` (2026-05-27) = 0 événement corporate pour SPCX |
| Social sentiment | No data | 0 mentions Reddit, pump_detected = false |
| Options | Non disponible | Bloc options vide dans `data/latest.json` |
| Short interest | N/A | Données non fournies par yfinance pour cet ETF |
| Analyst consensus | N/A | Non applicable |
| FX Exposure | 🟢 | fx_impact_score = 0.0, direction = neutral, divergence_flag = aligned |
| Géopolitique | 🟢 | Pas de flag SPCX dans `data/geo_risk_latest.json` (2026-05-17) |
| Accounting | N/A | `data/accounting_risk_latest.json` absent — ETF non concerné |
| Quant | N/A | `data/quant_report_latest.json` (2026-05-17) : pas assez de signaux historiques pour SPCX |

**Anomalie data quality persistante :** `data/upcoming_events_latest.json` (2026-05-27) mentionne un faux événement `earnings` pour SPCX (source FMP, days_until = 0) — artefact connu, à ignorer pour un ETF.

---

## Scoring global (agents pipeline 2026-05-27, snapshot 10:00 UTC)

| Axe | Score | Changement vs 21:00 UTC 26/05 | Commentaire |
|-----|-------|------------------------------|-------------|
| Score Catalyseur | 6.5/10 | = | Modéré-haussier — absence de catalyseur fondamental compensée par le momentum technique |
| Score Valorisation | 5.0/10 | = | Neutre — décote vs 52w high mais pas de valeur intrinsèque mesurable |
| Score Momentum | 7.0/10 | = | 🟢 Haussier — retour au-dessus MM50 confirmé, RSI stable en zone neutre |
| **Score Opportunité** | **6.0/10** | = | Pondération régime Normal : C×35% + V×40% + M×25% = 6.02 |
| **Score Global** | **60.2/100** | = | Avant ajustements |
| **Score Global Ajusté** | **65.2/100** | −5.0 pts | Bonus timing favorable appliqués, mais réduit vs 70.2 suite à normalisation du volume |

**Malus / Bonus appliqués (par Agent Recommandation) :**
- Accounting : 0 (ETF non concerné)
- Geo : 0 (pas de flag)
- FX : 0 (neutre)
- Event : 0 (aucun événement corporate réel)
- Social : 0 (pas de données)
- Quant : 0 (pas assez d'historique)
- **Timing technique :** +5 (cours au-dessus MM50 mais volume normalisé — anomalie haussière dissipée)

**Règle de disqualification :** Aucun score individuel ≤ 2/10 → ticker conservé.

| Seuil | Action | Sizing | Condition |
|-------|--------|--------|-----------|
| ≥ 75 | ACHETER | Standard | — |
| 60–74 | **ACHETER** | **Réduit** | ✅ SPCX = 65.2 |

---

## Révision des niveaux SL / TP

La recommandation reste **ACHETER (Réduit)** — niveaux confirmés par Agent Recommandation, révisés suite au nouveau close et à l'ATR $0.28.

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix entrée suggéré | $22.34 | Close du jour (source `data/latest.json`) |
| Stop-loss | $21.78 | Close − 2×ATR = $22.339 − $0.56 |
| Take-profit | $23.18 | Close + 3×ATR = $22.339 + $0.84 |
| Ratio R/R | 1.5× | Gain $0.84 / Perte $0.56 |

**Verdict sizing :** Réduit. Le Score Global Ajusté (65.2) est dans la fourchette 60–74. La liquidité historique faible (volume moyen ~3 800) et l'absence de catalyseur fondamental justifient un sizing limité. Maximum 5% du capital sur cette position ETF thématique.

---

## Conclusion : thèse confirmée, modifiée ou invalidée ?

**Verdict :** 🟢 Thèse **CONFIRMÉE avec nuance** — 7e snapshot consécutif de stabilité globale, mais première micro-mutation (−0.27%, volume normalisé, RSI −3.3 pts).

| Critère | Évaluation |
|---------|------------|
| Cours vs MM50 | ✅ Au-dessus ($22.339 > $22.00) |
| RSI | ✅ Haussier (59.07) — pas de surachat, retrait sain |
| Volume | 🟡 Normalisé (1.02× moyenne) — anomalie haussière dissipée, ni accumulation ni distribution |
| Catalyseur | 🟡 Aucun fondamental — signal purement technique |
| Risque technique | 🟢 MM50 support, 52w low intact, ATR faible = risque contrôlé |
| Score Global | 🟢 65.2/100 → déclenche ACHETER Réduit |
| Stabilité snapshots | 🟢 7e snapshot avec cours dans la fourchette $22.30–$22.40 — ancrage technique fiable |

- **Confirmation :** Le setup technique identifié le 25/05 reste validé. La micro-baisse de −0.27% et le retrait du RSI à 59.07 sont cohérents avec une consolidation saine après plusieurs sessions de stabilité absolue. La normalisation du volume n'est pas interprétée comme un signal de sortie — elle reflète le retour à la liquidité structurelle de l'ETF.
- **Nuances :** Le Score Global Ajusté recule de 5 points (70.2 → 65.2) suite à la normalisation du volume. La conviction technique est légèrement atténuée : l'anomalie volume ×4.5 qui renforçait le signal d'accumulation institutionnelle a disparu. Le mouvement reste 100% technique. Le secteur Financials (XLF) n'est pas dans la rotation haussière du jour (momentum_score = 0.0).
- **Invalidation :** Une clôture sous $22.00 (MM50) avec volume >1.5× moyenne invaliderait le setup et justifierait une clôture immédiate. Une clôture sous $21.32 (52w low) avec volume élevé = reclassement ÉVITER.
- **Rehaussement en Standard :** Une cassure de $23.00 (zone de congestion) avec volume >2× moyenne et RSI stable > 55 justifierait un passage à ACHETER Standard avec relèvement du TP vers $24.00.

**Recommandation :** **ACHETER (Réduit)**
**Prix cible :** $23.18 (+3.8% upside)
**Stop-loss :** $21.78 (−2.5% downside)
**Horizon :** 1–2 semaines
**Conviction :** Modérée — setup technique validé par les agents (Score Global Ajusté 65.2), mais normalisation du volume réduit légèrement la conviction vs les sessions précédentes. Absence de catalyseur fondamental et faible liquidité historique. Sizing réduit obligatoire.

---

## Radar activité inhabituelle

| Signal | Valeur actuelle | vs Normal | Interprétation |
|--------|----------------|-----------|----------------|
| Volume journalier | 1.02× moy. 20j | 🟢 Normal | Retour à la liquidité structurelle habituelle — anomalie des 6 snapshots précédents dissipée |
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
- Analyse précédente : [SPCX_2026-05-26_update.md](./SPCX_2026-05-26_update.md) (snapshot 21:00 UTC 26/05)
- Alertes actives : [Alertes/ALERTES.md](../../Alertes/ALERTES.md)

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données à enregistrer :**
- Prix cible précédent : $23.21
- Prix cible révisé : $23.18 (−$0.03, ajusté ATR)
- Recommandation précédente : ACHETER (Réduit)
- Recommandation révisée : **ACHETER (Réduit)**
- Raison principale : Snapshot 10:00 UTC 27/05 — micro-recul −0.27%, volume normalisé, RSI 59.07, Score Global Ajusté 65.2 (−5 pts), thèse CONFIRMÉE avec nuance
- Thèse : 🟢 Confirmée avec nuance

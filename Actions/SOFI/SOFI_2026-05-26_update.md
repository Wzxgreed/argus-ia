# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-05-26 (snapshot 10:00 UTC — stabilité confirmée vs 2026-05-25 21:00 UTC)
**Type :** `_update.md` — Mise à jour pré-ouverture (marché US non ouvert à 10:00 UTC)
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `_update.md` 2026-05-25 (21:00 UTC) | **Snapshot 2026-05-26 (10:00 UTC)** | **Δ** |
|----------|-------------------------------------|-------------------------------------|-------|
| Cours close | $15.62 | **$15.62** | **$0.00 (0.00%)** |
| RSI 14j | 43.83 | **43.83** | **0.00** |
| ATR 14j | $0.64 | **$0.64** | **$0.00** |
| MM 50j | $16.76 | **$16.76** | **$0.00** |
| Volume | 57.91M (0.84×) | **57.91M (0.84×)** | **0** |
| P/E LTM (Yahoo) | 34.71 | **34.71** | **0.00** |
| Forward P/E | 19.96 | **19.96** | **0.00** |
| Beta | 2.126 | **2.126** | 0.000 |
| Short interest | 0.1272% | **0.1272%** | 0.000 pts |
| Consensus PT | $25.41 (27a) | **$25.41 (27a)** | 0.00 |
| Max Pain options (historique) | $15.00 | **$15.00** | **$0.00** |
| Put/Call ratio (historique) | 0.75 | **0.75** | **0.00** |
| Call OI % (historique) | 57.2% | **57.2%** | **0.0 pts** |
| 52W range | $12.86–$32.73 | **$12.86–$32.73** | Inchangé |
| Earnings J | 64 | **63** | −1j |

**Verdict : Stabilité totale.** Le snapshot 10:00 UTC du 2026-05-26 confirme l'intégralité des données du snapshot 21:00 UTC du 2026-05-25. Le marché américain était fermé le 2026-05-25 (Memorial Day) et le snapshot 10:00 UTC est pré-ouverture (marché US ouvre à 13:30 UTC). Aucune transaction significative n'a altéré les niveaux techniques, fondamentaux ou options de SOFI.

**[ALERTE DATA QUALITY]** `data/latest.json` (2026-05-26) contient une anomalie systémique sur les données options : Max Pain affiché à $5.00 (aberrant vs historique $15.00), Put/Call ratio `null`, Call OI % `null`. Cette anomalie affecte l'ensemble des tickers du snapshot (confirmé par le commit VRT du jour : « anomalie options JSON détectée (put/call null, max pain 05) — valeurs confirmées 25/05 maintenues »). Les valeurs confirmées du 2026-05-25 sont maintenues pour l'interprétation : Max Pain $15.00, Put/Call 0.75, Call OI 57.2%.

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-05-26 (10:00 UTC) | Signal |
|------------|-------------------------------|--------|
| RSI 14j | 43.83 | 🟡 Zone neutre — inchangé |
| MM 50j | $16.76 | 🔴 Cours −6.8% sous MM50 — trend baissier court terme intact |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.64 | 🟢 Volatilité en compression (ATR rel. 4.10%) — range rétréci |
| Support clé | $15.00–$15.36 | 🟡 Support psychologique $15.00 inchangé |
| Résistance clé | $16.00–$16.76 | 🔴 Max Pain $15.00 + MM50 $16.76 = double mur inchangé |
| Volume relatif | 0.84× | 🟡 En retrait — pré-ouverture, volume de la dernière session (2026-05-23) |
| Beta | 2.126 | ⚠️ Volatilité extrême — sizing réduit obligatoire |

**Options (valeurs confirmées 2026-05-25 — anomalie JSON du jour) :**

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Max Pain | $15.00 | ⚠️ Sous le cours ($15.62) — attraction gravitationnelle marginale vers le bas |
| Put/Call ratio | 0.75 | 🔴 Rebalancement net vers les puts (stable) |
| Call OI % | 57.2% | 🟡 Skew call réduit (stable) |
| Expiration prochaine | 2026-05-29 (3 jours) | Risque de pinning autour de $15.00–$15.50 inchangé |

> **Interprétation :** La configuration technique est figée à la clôture du 23/05 (dernière session avant le weekend de Memorial Day). Les niveaux restent identiques : cours sous MM50, RSI neutre sans momentum haussier, support psychologique $15.00 tenu. L'expiration options du 2026-05-29 (3 jours ouvrés) approche — le pinning vers Max Pain $15.00 reste le risque dominant à très court terme.

---

## 3. Mise à jour fondamentale

**Aucune donnée fondamentale nouvelle.** Les ratios FMP (FY 2025) sont stables.

| Ratio | Valeur _init.md (17/05) | Valeur 2026-05-26 (10:00 UTC) | Δ |
|-------|-------------------------|-------------------------------|---|
| Gross margin (FMP) | 75.1% | 75.1% | 0.0 |
| Operating margin (FMP) | 11.0% | 11.0% | 0.0 |
| Net margin (FMP) | 10.1% | 10.1% | 0.0 |
| Debt/Equity (FMP) | 0.173 | 0.173 | 0.000 |
| P/B (FMP) | 2.87 | 2.87 | 0.00 |
| P/B (Yahoo) | 1.851 | **1.851** | **0.000** |
| P/E LTM (Yahoo) | 34.71 | **34.71** | **0.00** |
| Forward P/E | 19.96 | **19.96** | **0.00** |
| EV/Revenue (Yahoo) | 4.705 | **4.705** | **0.000** |
| FCF yield | −13.2% | −13.2% | 0.0 |

> **Note :** Marché fermé le 25/05 + snapshot pré-ouverture le 26/05 = aucun mouvement de multiples. Les fondamentaux sous-jacents sont inchangés.

> **Rappel Filtre Qualité :** 4/6 (Quality Partielle). Faiblesses structurelles inchangées : profit CAGR 5 ans non atteint (rentabilité GAAP trop récente), moat en construction, ROE faible, FCF négatif. Malus −0.5 pt sur Score Valorisation appliqué.

---

## 4. Mise à jour sentiment / options / news

### Consensus analystes
- **27 analystes, PT moyen $25.41** — inchangé. Upside +62.7% vs cours $15.62.
- 8 analystes actifs le mois dernier, 10 le trimestre dernier — couverture dense et stable.

### Options (valeurs confirmées 2026-05-25)
- **Max Pain :** $15.00 (inchangé) — légèrement sous le cours.
- **Put/Call ratio :** 0.75 — stable. Signal défensif à très court terme inchangé.
- **Call OI % :** 57.2% — stable.
- **Interprétation :** Aucun repositionnement options n'a eu lieu (marché fermé 25/05, snapshot pré-ouverture 26/05). Le risque de pinning vers $15.00 à l'expiration du 2026-05-29 persiste.

### News & Social
- **Aucune mention Reddit** (`social_sentiment_latest.json` : 0 mentions, score 0/10).
- **Aucune news SOFI** (`news_2026-05-26.json` : 0 item).
- **Aucun événement corporate** (`events_latest.json` : 0 événement SOFI).
- **Aucune alerte géopolitique** (`geo_risk_latest.json` : SOFI non flaggé, non exposé).
- **Aucune exposition FX active** (`fx_exposure_latest.json` : fx_impact_score 0.0, flag 🟢).
- **Aucun événement event-driven** (`events_latest.json` : 0 événement).

---

## 5. Nouveau scoring global

### Données agents actualisées (`recommandations_latest.json` — 2026-05-26 10:00 UTC)

| Axe | Score /10 | Pondération (Régime Normal) | Pondéré |
|-----|-----------|----------------------------|---------|
| Catalyseur | 6.8 | 35% | 2.380 |
| Valorisation | 6.0 | 40% | 2.400 |
| Momentum | 3.5 | 25% | 0.875 |
| **Score Opportunité brut** | | | **5.655/10** |
| Quality Partielle (4/6) | Malus −0.5 pt sur Val | | — |
| **Score Opportunité ajusté** | | | **5.7/10** |

**Évolution vs snapshot 2026-05-25 21:00 UTC :** Inchangé. Score Opportunité **5.7/10**, Score Global **48.6/100 (SURVEILLER)**. Le régime macro reste indéterminé dans le système ("Unknown"), pondération par défaut 35/40/25 appliquée.

### Score Global Composite /100

| Composant | Valeur | Impact |
|-----------|--------|--------|
| Score Opportunité × 10 | 57 | Base |
| Malus Accounting | 0 | Fichier absent — pas de pénalité |
| Malus Geo | 0 | SOFI non flaggé, non exposé = faible |
| Malus FX | 0 | fx_impact_score 0.0 |
| Malus Event | 0 | Aucun événement |
| Malus Social | 0 | 0 mentions = neutre |
| Malus Quant | 0 | Insuffisant — pas de pénalité |
| Bonus Event | 0 | Aucun |
| Bonus Buyback | 0 | Aucun programme signalé |
| Malus Sector | −3 | XLF momentum 0.0/10 (faible) — secteur financier sans direction |
| Timing technique | −5 | Trend baissier sous MM50, RSI neutre sans momentum, volatilité compressée |
| **Score Global ajusté** | | **48.6/100** |

**Classification :** 48.6/100 = **SURVEILLER** (plage 35–49, bord supérieur).

> **Note :** Aucun changement de score entre le snapshot 2026-05-25 21:00 UTC et le snapshot 2026-05-26 10:00 UTC. La classification SURVEILLER est confirmée.

---

## 6. Révision des niveaux SL / TP

| Niveau | Ancien (2026-05-25 21:00 UTC) | Révisé 2026-05-26 (10:00 UTC) | Justification |
|--------|-------------------------------|-------------------------------|---------------|
| **Prix cible** | $17.54 | **$17.54** | Cours + 3×ATR = $15.62 + $1.92 — ATR compressé à $0.64, inchangé |
| **Stop-loss** | $14.34 | **$14.34** | Cours − 2×ATR = $15.62 − $1.28 — ATR compressé, inchangé |
| **Upside / Downside** | +12.3% / −8.2% | **+12.3% / −8.2%** | Ratio inchangé, fourchette resserrée stable |
| **Ratio R/R** | 1.50 | **1.50** | Stable — acceptable mais limité |
| **Support critique** | $15.00 | **$15.00** | Support psychologique $15.00 inchangé |

**Verdict technique :** Les niveaux SL/TP restent inchangés. L'ATR compressé à $0.64 resserre la fourchette de risque : SL à **$14.34**, TP à **$17.54**. Le ratio R/R reste à 1.50. Le support critique est le niveau psychologique **$15.00**. Un break sous $15.00 ouvre $14.34 (SL) puis le 52W low $12.86. La MM50 $16.76 et la zone $16.00 restent les résistances clés.

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**Verdict : THÈSE CONFIRMÉE — Aucune mutation (marché fermé Memorial Day, snapshot pré-ouverture 2026-05-26).**

La thèse fondamentale et technique reste inchangée entre le snapshot 2026-05-25 21:00 UTC et le snapshot 2026-05-26 10:00 UTC :

1. **Cours stable à $15.62** — Marché fermé 25/05, snapshot pré-ouverture 26/05, aucun nouveau flux de prix.
2. **Compression volatilité maintenue** — ATR $0.64 inchangé. Range probable $15.00–$15.75 à court terme.
3. **Momentum dégradé mais stable** — RSI 43.83, Momentum score agent 3.5/10. Pas de survente mais pas de momentum haussier.
4. **Signal options défensif inchangé** — Put/Call 0.75, Call OI % 57.2%. Risque de pinning vers $15.00 à l'expiration du 29/05 (3 jours ouvrés).
5. **Aucun catalyseur immédiat** — Earnings Q2 dans 63j (2026-07-28), consensus stable, pas de news structurante.
6. **Sector headwind inchangé** — XLF momentum 0.0/10. Le secteur financier reste sans direction.
7. **Qualité partielle inchangée** — 4/6, FCF négatif, ROE faible, dépendance aux taux.
8. **Score Global 48.6/100 (SURVEILLER)** — Confirmé stable.
9. **Exposition FX neutre** — fx_impact_score 0.0, flag 🟢.
10. **Social sentiment neutre** — 0 mentions Reddit, pas de pump/dump détecté.
11. **Risque géopolitique faible** — SOFI non flaggé dans `geo_risk_latest.json`.
12. **Accounting risk non évalué** — Fichier `accounting_risk_latest.json` absent — pas de malus appliqué.
13. **Validation data :** SOFI OK dans `validation_report.txt` (2026-05-26) — aucun warning, aucune erreur.

**Action recommandée : SURVEILLER** — Pas de position.
- **Entrée potentielle :** Un retour quotidien au-dessus de $16.76 (MM50) avec volume > 1.2× moy. 20j.
- **Stop-loss :** $14.34 (ajusté ATR compressé).
- **Scénario baissier :** Cassure de $15.00 → ouverture vers $14.34 (SL) puis $12.86 (52W low).
- **Scénario haussier :** Break de $16.76 (MM50) avec volume > 80M → ouverture vers $17.54 (TP) puis $19.51 (prix cible historique).

---

## ⚙️ Enregistrement automatique — OBLIGATOIRE

**Données enregistrées :**
- Recommandation : SURVEILLER
- Prix cible : $17.54
- Cours au moment de l'analyse : $15.62
- Upside/Downside : +12.3% / −8.2%
- Horizon : 3–6 mois
- Score Opportunité : 5.7/10
- Score Global : 48.6/100
- Thèse résumée : Snapshot 10:00 UTC 2026-05-26 confirme stabilité totale vs 21:00 UTC 2026-05-25 (marché fermé Memorial Day + snapshot pré-ouverture). Cours $15.62, RSI 43.83, MM50 $16.76, ATR $0.64. [ALERTE DATA QUALITY] Options JSON anomalie (max pain $5.00, put/call null, call_oi null) — valeurs confirmées 25/05 maintenues : Max Pain $15.00, Put/Call 0.75, Call OI 57.2%. Score Global 48.6/100 (SURVEILLER). TP $17.54, SL $14.34, R/R 1.50. Earnings dans 63j. Support critique $15.00. Aucune news, aucun événement corporate, exposition FX et géo neutres. Accounting risk non évalué (fichier absent). Validation data : SOFI OK.

---

## Références

- `Actions/SOFI/SOFI_2026-05-17_init.md` — Analyse initiale / Full Refresh
- `Actions/SOFI/SOFI_2026-05-18_update.md` — Mise à jour quotidienne
- `Actions/SOFI/SOFI_2026-05-19_update.md` — Mise à jour quotidienne
- `Actions/SOFI/SOFI_2026-05-20_update.md` — Mise à jour quotidienne
- `Actions/SOFI/SOFI_2026-05-25_update.md` — Mise à jour quotidienne (snapshot 21:00 UTC — stabilité totale confirmée)
- `Actions/SOFI/SOFI_2026-05-26_update.md` — Ce fichier (snapshot 10:00 UTC — stabilité confirmée vs 25/05)
- `data/latest.json` (2026-05-26T10:00:08+00:00) — Cours, RSI, ATR, consensus, ratios FMP, options
- `data/recommandations_latest.json` (2026-05-26) — Scores agents actualisés
- `data/quant_report_latest.json` — Insuffisant
- `data/geo_risk_latest.json` — SOFI non flaggé
- `data/sector_rotation_latest.json` — XLF momentum 0.0
- `data/social_sentiment_latest.json` — 0 mentions
- `data/fx_exposure_latest.json` — fx_impact_score 0.0
- `data/upcoming_events_latest.json` — Earnings 2026-07-28 (63j)
- `data/events_latest.json` — Aucun événement corporate
- `data/news_2026-05-26.json` — 0 news SOFI
- `data/validation_report.txt` (2026-05-26) — SOFI OK

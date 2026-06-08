# NOK — Mise à jour quotidienne (Snapshot 21:00 UTC)

> **Date :** 2026-06-08
> **Type :** Update — révision post-session US + consolidation données
> **Fichier précédent :** [NOK_2026-06-08_update.md](./NOK_2026-06-08_update.md) (snapshot 17:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-08 17:00 UTC | 2026-06-08 21:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Cours close** | $14.775 | **$14.59** | −1.25% (révision) |
| **Change vs previous close** | +2.75% | **+1.46%** | −1.29 pt |
| **RSI 14j** | 55.47 | **54.58** | −0.89 pt |
| **Volume session** | 76.2M (0.61×) | **102.4M (0.82×)** | +34.4% révisé |
| **ATR 14j** | $1.13 | **$1.11** | −$0.02 |
| **MM 50j** | $12.16 | **$12.29** | +$0.13 |
| **Max pain options** | $15.00 | **$15.00** | — |
| **Put/Call ratio** | 1.00 | **1.00** | — |
| **Call OI %** | 49.9% | **49.9%** | — |
| **Score Global ajusté** | 51.2 — ATTENDRE | **51.2 — ATTENDRE** | — |
| **Recommandation** | ATTENDRE | **ATTENDRE** | Confirmé |

**Verdict :** Le close est révisé à la baisse à **$14.59** (+1.46% vs previous close $14.38) dans le snapshot 21:00 UTC. Le volume est simultanément révisé à la hausse à **102.4M** (0.82× moy. 20j), corrigeant l'impression de participation faible du snapshot 17h. Le RSI reste dans le haut de la zone neutre (**54.58**). Les données options, fondamentales et scores agents sont **strictement inchangées**. Le **Score Global ajusté** reste à **51.2/100** (zone ATTENDRE). Aucun événement corporate (`events_latest.json` vide pour NOK). Aucune mutation fondamentale.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Open | $14.86 | Yahoo Finance |
| High | $15.06 | Yahoo Finance |
| Low | $14.445 | Yahoo Finance |
| Close | **$14.59** | Yahoo Finance |
| Change vs previous close | **+1.46%** | Yahoo Finance |
| Volume | 102,427,836 | Yahoo Finance |
| Volume vs moy. 20j | **0.82×** | Calcul (125.5M) |
| RSI 14j | **54.58** | Calcul agent |
| ATR 14j | **$1.11** | Calcul agent |
| MM 50j | **$12.29** | Calcul agent |
| MM 200j | — | N/A |

**Niveaux clés révisés :**
- Support immédiat : **$14.445** (low du jour)
- Support structurel : **$12.29** (MM50)
- Résistance : **$15.00** (max pain options) / **$15.06** (high du jour)
- Résistance gap : **$15.47** (base du gap haussier du 25/05, non comblé)
- Stop-loss ATR (2×) : **$12.37** ($14.59 − $2.22)
- Take-profit ATR (3×) : **$17.92** ($14.59 + $3.33)
- Ratio R/R : **1.5×**

**Verdict timing :** Favorable — Le cours clôture au-dessus du previous close (+1.46%) et bien au-dessus de la MM50 (+18.7%). Le RSI à 54.58 confirme une zone neutre constructive, loin du surachat. Le volume révisé à 0.82× moyenne 20j est proche de la normalité : ni accumulation agressive, ni distribution paniquée. La proximité du max pain ($15.00, expiration 2026-06-12 dans 4 jours) maintient un overhang technique modéré (cours −2.7% sous le pin).

---

## 3. Bloc Fondamental

Inchangé vs snapshot 17:00 UTC. Voir [NOK_2026-05-17_init.md](./NOK_2026-05-17_init.md) pour le détail complet.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $81.4B | Yahoo Finance |
| P/E (TTM) | 91.19 | Yahoo Finance |
| Forward P/E | 29.97 | Yahoo Finance |
| EV/EBITDA | 30.75 | Yahoo Finance |
| P/B | 3.32 | Yahoo Finance |
| Beta | 0.781 | Yahoo Finance |
| Dividend Yield | 1.14% | Yahoo Finance |
| Short Interest | 1.08% | Yahoo Finance |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé). Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).

> **[DONNÉES PARTIELLES]** : `validation_report.txt` du 2026-06-08 signale un warning qualité sur NOK (P/E élevé, premium vs consensus). Le premium vs consensus $10.8 est de **+35.1%** (vs +36.8% à 17:00 UTC, vs +33.1% à 13:00 UTC).

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API |
| Max pain options | **$15.00** | Yahoo Finance |
| Put/Call ratio | **1.00** | Yahoo Finance |
| Call OI % | **49.9%** | Yahoo Finance |
| Expiration nearest | **2026-06-12** | Yahoo Finance |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_latest.json` |

**Structure options :**
- Max pain $15.00 inchangé. Cours $14.59 < max pain (−2.7%) — pression baissière au pin modérée, atténuée vs snapshot 13h (−4.1%).
- Put/call 1.00 et call OI 49.9% inchangés — structure neutre, sans domination call ou put.
- Expiration dans 4 jours (2026-06-12). Risque de pin vers $15.00 persiste si le cours ne parvient pas à s'en éloigner.

**News / Événements :**
- `events_latest.json` : **0 événement** corporate pour NOK
- Aucune mention Reddit, aucun pump/dump détecté
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_latest.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (momentum score 0.0, RS20d −5.22% vs SPY). Malus structurel pour NOK.
- **Exposition FX :** 25% revenus hors-USD, impact neutre (`fx_exposure_latest.json` : fx_impact_score 0.0, flag 🟢)
- **Géopolitique :** Score politique 0/10, non exposé (`geo_risk_latest.json` : aucun ticker flaggé pour NOK)
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_latest.json` (2026-06-08)

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.6/10** | C:4.0 V:3.5 M:7.3 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 91.2, premium consensus +35% |
| **Score Momentum** | 7.3/10 | 🟢 Tendance haussière structurelle intacte (+18.7% vs MM50) |
| **Score Global ajusté** | **51.2/100** | **ATTENDRE** (seuil 50–59) |
| **Timing technique** | Favorable | RSI neutre, cours au-dessus MM50, rebond sur support |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 03/06 : Score Global 31.8 — ÉVITER
- Le 08/06 10:00 : Score Global 48.0 — SURVEILLER
- Le 08/06 13:00 : Score Global 48.0 — SURVEILLER
- Le 08/06 17:00 : Score Global 51.2 — ATTENDRE
- Le 08/06 21:00 : Score Global **51.2** — **ATTENDRE** (confirmé)

Le scoring est **stable** après la révision de close. Le Score Momentum 7.3/10 compense les faiblesses fondamentales (Catalyseur 4.0, Valorisation 3.5) pour maintenir l'action dans la zone ATTENDRE. Le Filtre Qualité 2.5/6 maintient le plafond sur la valorisation.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (17:00) | Valeur révisée (21:00) | Justification |
|--------|---------------------------|------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé |
| **Stop-loss** | $12.56 | **$12.37** | Cours − 2×ATR |
| **Take-profit** | $18.11 | **$17.92** | Cours + 3×ATR |
| **Upside / Downside** | −26.9% / −14.9% | **−26.9%** / **−15.2%** | Révisé |
| **Ratio R/R** | 1.5× | **1.5×** | Stable |
| **Sizing** | — | **—** | Pas de position |

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 20% | Test $15.47 (base du gap) | Rebond confirmé sur volume, cassure du max pain $15.00. Nécessite catalyseur (contrat 5G, upgrade) |
| **Central** | 55% | Range $14.40–$15.00 | Consolidation autour de $14.60. Pin options $15.00 capte le cours jusqu'à expiration 12/06. MM50 ($12.29) comme ancre technique si dérive |
| **Pessimiste** | 25% | Cassure $14.445 → test $13.50 | Distribution continue, retour vers les fondamentaux (consensus $10.8). Volume normalisé = absence de conviction achat institutionnelle |

---

## 9. Conclusion — Thèse confirmée

**Verdict :** La thèse **ATTENDRE** est **confirmée** après la révision de close à $14.59.

**Ce qui a changé :**
1. **Cours révisé à $14.59** (−1.25% vs $14.775 à 17:00 UTC, mais +1.46% vs previous close $14.38). La session reste positive, avec un high à $15.06 testé puis rejeté.
2. **Volume révisé à 102.4M** (0.82× moy. 20j), corrigeant l'impression de participation faible du snapshot 17h (76.2M, 0.61×). La révision à la hausse indique une participation proche de la normale — ni euphorie, ni panique.
3. **RSI légèrement révisé à la baisse** à 54.58 (−0.89 pt), toujours dans la zone neutre constructive.
4. **Niveaux SL/TP révisés à la baisse** ($12.37 / $17.92) compte tenu du nouveau close et de l'ATR stable.

**Ce qui n'a pas changé :**
- Filtre Qualité hors périmètre (2.5/6) — pas de changement qualitatif.
- Aucun catalyseur fondamental détecté.
- Consensus analystes $10.8 (7 analysts) — premium persistant +35.1%.
- XLC bottom 3 du sector rotation.
- Options inchangées (max pain $15.00, put/call 1.00, expiration 12/06 dans 4 jours).
- Aucun événement corporate, aucune news structurante.
- Score Global ajusté 51.2/100 — ATTENDRE.

**Recommandation révisée :** **ATTENDRE** — Pas de position. Le résumé de la session est un rebond technique modeste (+1.46%) sur volume normalisé, sans catalyseur fondamental. La proximité du max pain ($15.00, expiration dans 4 jours) crée un overhang technique qui limite l'upside. Une entrée reste exclue sans :
- Test et rebond sur la MM50 ($12.29) avec volume > moyenne
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel ou corporate

**Prochain point de contrôle :** Earnings Q2 FY2026 le **2026-07-23** (dans 45 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 21:00 UTC), `data/recommandations_latest.json`, et fichiers JSON agents.*

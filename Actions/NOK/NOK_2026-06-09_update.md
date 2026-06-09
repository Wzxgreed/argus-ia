# NOK — Mise à jour quotidienne (Snapshot 13:00 UTC)

> **Date :** 2026-06-09
> **Type :** Update — stabilité prix/volume, correction données options
> **Fichier précédent :** [NOK_2026-06-09_update.md](./NOK_2026-06-09_update.md) (snapshot 10:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-09 10:00 UTC | 2026-06-09 13:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Cours close** | $14.59 | **$14.59** | — |
| **Change vs previous close** | +1.46% | **+1.46%** | — |
| **RSI 14j** | 54.58 | **54.58** | — |
| **Volume session** | 102.6M (0.82×) | **102.6M (0.82×)** | — |
| **ATR 14j** | $1.11 | **$1.11** | — |
| **MM 50j** | $12.29 | **$12.29** | — |
| **Max pain options** | $15.00 (opérationnel) | **$15.00** | ✅ Corrigé dans `latest.json` |
| **Put/Call ratio** | 1.00 (opérationnel) | **0.78** | 🟢 Amélioration (call-biased) |
| **Call OI %** | 49.9% (opérationnel) | **56.2%** | 🟢 Call-dominated confirmé |
| **Score Global ajusté** | 51.2 — ATTENDRE | **51.2 — ATTENDRE** | — |
| **Recommandation** | ATTENDRE | **ATTENDRE** | Confirmé |

**Verdict :** Le snapshot 13:00 UTC du 2026-06-09 reproduit **intégralement** le close officiel du 2026-06-08 21:00 UTC sur toutes les métriques prix, volume, technique et fondamentale. La seule mutation est la **correction des données options** dans `data/latest.json` (anomalie $3.00 du snapshot 10h résolue). Le **Score Global ajusté** reste à **51.2/100** (zone ATTENDRE). Aucun événement corporate (`events_latest.json` vide pour NOK). Aucune news structurante.

**DRAFT_refresh traité :** Trigger `ATR_SPIKE` (7.61%) archivé comme **faux positit technique** — l'ATR $1.11 est stable depuis le gap du 08/06, le ratio ATR/cours reflète un range consolidé, pas un changement de régime.

> **[DONNÉES PARTIELLES]** : `validation_report.txt` du 2026-06-09 signale un warning qualité sur NOK (P/E élevé, premium vs consensus). Ce warning est inchangé depuis le 2026-05-17.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Open | $14.86 | Yahoo Finance |
| High | $15.06 | Yahoo Finance |
| Low | $14.45 | Yahoo Finance |
| Close | **$14.59** | Yahoo Finance |
| Change vs previous close | **+1.46%** | Yahoo Finance |
| Volume | 102,565,500 | Yahoo Finance |
| Volume vs moy. 20j | **0.82×** | Calcul (125.6M) |
| RSI 14j | **54.58** | Calcul agent |
| ATR 14j | **$1.11** | Calcul agent |
| MM 50j | **$12.29** | Calcul agent |
| MM 200j | — | N/A |

**Niveaux clés inchangés :**
- Support immédiat : **$14.45** (low du jour)
- Support structurel : **$12.29** (MM50)
- Résistance : **$15.00** (max pain options) / **$15.06** (high du jour)
- Résistance gap : **$15.47** (base du gap haussier du 25/05, non comblé)
- Stop-loss ATR (2×) : **$12.37** ($14.59 − $2.22)
- Take-profit ATR (3×) : **$17.92** ($14.59 + $3.33)
- Ratio R/R : **1.5×**

**Verdict timing :** Favorable — Le cours reste au-dessus du previous close (+1.46%) et bien au-dessus de la MM50 (+18.7%). Le RSI à 54.58 confirme une zone neutre constructive. Le volume stable à 0.82× moyenne 20j reflète une participation normale. La proximité du max pain ($15.00, expiration 2026-06-12 dans 3 jours) maintient un overhang technique modéré (cours −2.7% sous le pin).

---

## 3. Bloc Fondamental

Inchangé vs snapshot 2026-06-08 21:00 UTC. Voir [NOK_2026-05-17_init.md](./NOK_2026-05-17_init.md) pour le détail complet.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $81.4B | Yahoo Finance |
| P/E (TTM) | 91.19 | Yahoo Finance |
| Forward P/E | 29.97 | Yahoo Finance |
| EV/EBITDA | 31.21 | Yahoo Finance |
| P/B | 3.32 | Yahoo Finance |
| Beta | 0.781 | Yahoo Finance |
| Dividend Yield | 1.12% | Yahoo Finance |
| Short Interest | 1.08% | Yahoo Finance |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé). Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 91.19 vs P/E FMP 45.81. Cette divergence ne modifie pas le verdict consensus calibré sur l'ADR.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API |
| Max pain options | **$15.00** | `data/latest.json` (✅ corrigé) |
| Put/Call ratio | **0.78** | `data/latest.json` |
| Call OI % | **56.2%** | `data/latest.json` |
| Expiration nearest | **2026-06-12** | Yahoo Finance |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_latest.json` |

✅ **Anomalie options résolue dans `data/latest.json` :** Le snapshot 13:00 UTC corrige l'anomalie du snapshot 10:00 (max pain $3.00 aberrant, put/call et call OI null). Les valeurs actuelles sont :
- Max pain **$15.00** — aligné avec les valeurs opérationnelles précédentes
- Put/call **0.78** — structure légèrement call-biased (vs 1.00 équilibré précédemment)
- Call OI **56.2%** — call-dominated confirmé (vs 49.9% précédemment)

**Structure options (mise à jour) :**
- Max pain $15.00 inchangé. Cours $14.59 < max pain (−2.7%) — pression baissière au pin modérée persiste.
- Put/call 0.78 — amélioration vs 1.00 précédent : les puts sont moins dominants, signal légèrement bullish.
- Call OI 56.2% — confirmation de la domination call, structure plus constructive qu'estimé à 10h.
- Expiration dans 3 jours (2026-06-12). Risque de pin vers $15.00 persiste mais légèrement atténué par la structure call-biased.

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

**Source :** `data/recommandations_latest.json` (2026-06-09 13:00 UTC)

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.6/10** | C:4.0 V:3.5 M:7.3 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 91.2, premium consensus +35% |
| **Score Momentum** | 7.3/10 | 🟢 Tendance haussière structurelle intacte (+18.7% vs MM50) |
| **Score Global ajusté** | **51.2/100** | **ATTENDRE** (seuil 50–59) |
| **Timing technique** | Favorable | RSI neutre, cours au-dessus MM50 |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 03/06 : Score Global 31.8 — ÉVITER
- Le 08/06 10:00 : Score Global 48.0 — SURVEILLER
- Le 08/06 21:00 : Score Global 51.2 — ATTENDRE
- Le 09/06 10:00 : Score Global **51.2** — **ATTENDRE**
- Le 09/06 13:00 : Score Global **51.2** — **ATTENDRE** (confirmé)

Le scoring est **stable**. Le Score Momentum 7.3/10 compense les faiblesses fondamentales (Catalyseur 4.0, Valorisation 3.5) pour maintenir l'action dans la zone ATTENDRE. Le Filtre Qualité 2.5/6 maintient le plafond sur la valorisation. La correction des données options (put/call 0.78, call OI 56.2%) ne modifie pas le scoring global.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (10:00 UTC) | Valeur actuelle (13:00 UTC) | Justification |
|--------|-------------------------------|----------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé |
| **Stop-loss** | $12.37 | **$12.37** | Cours − 2×ATR (inchangé) |
| **Take-profit** | $17.92 | **$17.92** | Cours + 3×ATR (inchangé) |
| **Upside / Downside** | −26.9% / −15.2% | **−26.9%** / **−15.2%** | Inchangé |
| **Ratio R/R** | 1.5× | **1.5×** | Stable |
| **Sizing** | — | **—** | Pas de position |

---

## 8. Scénarios & Probabilités

Inchangés vs 2026-06-09 10:00 UTC.

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 20% | Test $15.47 (base du gap) | Rebond confirmé sur volume, cassure du max pain $15.00. Nécessite catalyseur (contrat 5G, upgrade) |
| **Central** | 55% | Range $14.40–$15.00 | Consolidation autour de $14.60. Pin options $15.00 capte le cours jusqu'à expiration 12/06. MM50 ($12.29) comme ancre technique si dérive |
| **Pessimiste** | 25% | Cassure $14.45 → test $13.50 | Distribution continue, retour vers les fondamentaux (consensus $10.8). Volume normalisé = absence de conviction achat institutionnelle |

---

## 9. Conclusion — Thèse confirmée

**Verdict :** La thèse **ATTENDRE** est **confirmée** avec stabilité totale des données prix/volume/technique.

**Ce qui a changé :**
- **Options corrigées** dans `data/latest.json` : anomalie $3.00 du snapshot 10h résolue. Put/call 0.78 (vs 1.00 opérationnel), call OI 56.2% (vs 49.9% opérationnel) — structure légèrement plus call-biased, signal modérément plus constructif sans changer le verdict global.
- **DRAFT_refresh archivé** : trigger ATR_SPIKE (7.61%) traité comme faux positit technique.

**Ce qui n'a pas changé :**
- Cours stable à $14.59 (+1.46% vs previous close).
- Volume stable à 102.6M (0.82× moyenne 20j).
- RSI 54.58, ATR $1.11, MM50 $12.29 — tous inchangés.
- Filtre Qualité hors périmètre (2.5/6) — pas de changement qualitatif.
- Aucun catalyseur fondamental détecté.
- Consensus analystes $10.8 (7 analysts) — premium persistant +35.1%.
- XLC bottom 3 du sector rotation.
- Aucun événement corporate, aucune news structurante.
- Score Global ajusté 51.2/100 — ATTENDRE.

**Recommandation révisée :** **ATTENDRE** — Pas de position. L'absence de mutation entre le snapshot 10h et 13h confirme la consolidation sans direction claire. La correction des données options (structure call-biased 56.2%) atténue légèrement le risque de pin mais ne modifie pas l'overhang technique. Une entrée reste exclue sans :
- Test et rebond sur la MM50 ($12.29) avec volume > moyenne
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel ou corporate

**Prochain point de contrôle :** Earnings Q2 FY2026 le **2026-07-23** (dans 44 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-09 13:00 UTC), `data/recommandations_latest.json`, et fichiers JSON agents.*

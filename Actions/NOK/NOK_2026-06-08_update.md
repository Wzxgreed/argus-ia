# NOK — Mise à jour quotidienne (Snapshot 17:00 UTC)

> **Date :** 2026-06-08
> **Type :** Update — révision technique post-session US
> **Fichier précédent :** [NOK_2026-06-08_update.md](./NOK_2026-06-08_update.md) (snapshot 13:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-08 13:00 UTC | 2026-06-08 17:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Cours close** | $14.38 | **$14.775** | +2.75% |
| **RSI 14j** | 52.32 | **55.47** | +3.15 |
| **Volume session** | 183.6M (1.47×) | **76.2M (0.61×)** | Révisé |
| **ATR 14j** | $1.13 | **$1.11** | −$0.02 |
| **MM 50j** | $12.16 | **$12.29** | +$0.13 |
| **Max pain options** | $15.00 | **$15.00** | — |
| **Put/Call ratio** | 1.00 | **1.00** | — |
| **Call OI %** | 49.9% | **49.9%** | — |
| **Score Global ajusté** | 48.0 — SURVEILLER | **51.2 — ATTENDRE** | +3.2 |
| **Recommandation** | SURVEILLER | **ATTENDRE** | Upgrade mécanique |

**Verdict :** Le cours rebondit de +2.75% en fin de session US, portant le close à **$14.775** et ramenant le RSI dans le haut de la zone neutre (55.47). Le volume est révisé à la baisse dans `latest.json` (76.2M, 0.61× moy. 20j), signalant une participation institutionnelle modérée sur ce rebond. Les données options restent inchangées (max pain $15.00, put/call 1.00, expiration 2026-06-12). Le **Score Global ajusté** passe à **51.2/100**, franchissant le seuil ATTENDRE (50–59), ce qui constitue un upgrade mécanique post-rebond. Aucun événement corporate (`events_latest.json` vide pour NOK). Aucune mutation fondamentale.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Open | $14.86 | Yahoo Finance |
| High | $15.06 | Yahoo Finance |
| Low | $14.445 | Yahoo Finance |
| Close | **$14.775** | Yahoo Finance |
| Change vs previous close | **+2.75%** | Yahoo Finance |
| Volume | 76,155,361 | Yahoo Finance |
| Volume vs moy. 20j | **0.61×** | Calcul (124.2M) |
| RSI 14j | **55.47** | Calcul agent |
| ATR 14j | **$1.11** | Calcul agent |
| MM 50j | **$12.29** | Calcul agent |
| MM 200j | — | N/A |

**Niveaux clés révisés :**
- Support immédiat : **$14.445** (low du jour)
- Support structurel : **$12.29** (MM50)
- Résistance : **$15.00** (max pain options) / **$15.06** (high du jour)
- Résistance gap : **$15.47** (base du gap haussier du 25/05, non comblé)
- Stop-loss ATR (2×) : **$12.56** ($14.775 − $2.22)
- Take-profit ATR (3×) : **$18.11** ($14.775 + $3.33)
- Ratio R/R : **1.5×**

**Verdict timing :** Favorable — Le rebond de +2.75% confirme un soutien au-dessus du low intraday ($14.445). Le cours reste sous le max pain ($15.00, −1.5%), maintenant une pression baissière à l'expiration du 12/06. Le RSI à 55.47 indique une zone neutre constructive, loin du surachat. Cependant, le volume révisé à 0.61× moyenne 20j questionne la robustesse de ce rebond (participation faible).

---

## 3. Bloc Fondamental

Inchangé vs snapshot 13:00 UTC. Voir [NOK_2026-05-17_init.md](./NOK_2026-05-17_init.md) pour le détail complet.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $82.5B | Yahoo Finance |
| P/E (TTM) | 92.34 | Yahoo Finance |
| Forward P/E | 30.35 | Yahoo Finance |
| EV/EBITDA | 30.75 | Yahoo Finance |
| P/B | 3.36 | Yahoo Finance |
| Beta | 0.781 | Yahoo Finance |
| Dividend Yield | 1.14% | Yahoo Finance |
| Short Interest | 1.08% | Yahoo Finance |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé). Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).

> **[DONNÉES PARTIELLES]** : `validation_report.txt` du 2026-06-08 signale un warning qualité sur NOK (P/E élevé, premium vs consensus). Le premium vs consensus $10.8 est désormais de **+36.8%** (vs +33.1% à 13:00 UTC).

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
- Max pain $15.00 inchangé. Cours $14.775 < max pain (−1.5%) — la pression baissière au pin est atténuée par rapport au snapshot 13:00 UTC (−4.1%) mais persiste.
- Put/call 1.00 et call OI 49.9% inchangés — structure neutre, sans domination call ou put.
- Expiration dans 4 jours (2026-06-12). Risque de pin vers $15.00 si le cours ne parvient pas à s'en éloigner.

**News / Événements :**
- `events_latest.json` : **0 événement** corporate pour NOK
- Aucune mention Reddit, aucun pump/dump détecté
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_latest.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (momentum score 0.0, RS20d −5.68% vs SPY). Malus structurel pour NOK.
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
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 92.3, premium consensus +37% |
| **Score Momentum** | 7.3/10 | 🟢 Tendance haussière structurelle intacte (+20.3% vs MM50) |
| **Score Global ajusté** | **51.2/100** | **ATTENDRE** (seuil 50–59) |
| **Timing technique** | Favorable | RSI neutre, cours au-dessus MM50, rebond sur support |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 03/06 : Score Global 31.8 — ÉVITER
- Le 08/06 10:00 : Score Global 48.0 — SURVEILLER
- Le 08/06 13:00 : Score Global 48.0 — SURVEILLER
- Le 08/06 17:00 : Score Global **51.2** — **ATTENDRE** (+3.2 pts, upgrade mécanique post-rebond)

L'upgrade de SURVEILLER → ATTENDRE est **mécanique** (post-rebond +2.75% qui booste le Score Momentum de 6.0 à 7.3). Les scores fondamentaux (Catalyseur 4.0, Valorisation 3.5) restent dans la zone de faiblesse relative. Le Filtre Qualité 2.5/6 maintient le plafond sur la valorisation.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (13:00) | Valeur révisée (17:00) | Justification |
|--------|---------------------------|------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé |
| **Stop-loss** | $12.12 | **$12.56** | Cours − 2×ATR |
| **Take-profit** | $17.77 | **$18.11** | Cours + 3×ATR |
| **Upside / Downside** | −24.9% / −15.7% | **−26.9%** / **−14.9%** | Révisé |
| **Ratio R/R** | 1.5× | **1.5×** | Stable |
| **Sizing** | — | **—** | Pas de position |

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 20% | Test $15.47 (base du gap) | Rebond confirmé sur volume, cassure du max pain $15.00. Nécessite catalyseur (contrat 5G, upgrade) |
| **Central** | 55% | Range $14.40–$15.00 | Consolidation autour de $14.75. Pin options $15.00 capte le cours jusqu'à expiration 12/06. MM50 ($12.29) comme ancre technique si dérive |
| **Pessimiste** | 25% | Cassure $14.445 → test $13.50 | Distribution continue, retour vers les fondamentaux (consensus $10.8). Volume faible sur le rebond = absence de conviction |

---

## 9. Conclusion — Thèse modifiée (upgrade mécanique)

**Verdict :** La thèse précédente (« SURVEILLER — value trap, surchauffe dissipée mais pas d'opportunité d'achat ») est **modifiée** en **ATTENDRE** après le rebond de +2.75%.

**Ce qui a changé :**
1. **Cours rebondit à $14.775** (+2.75% vs $14.38 à 13:00 UTC). Le low $14.445 n'a pas été cassé, confirmant un soutien technique immédiat.
2. **Score Momentum boosté** de 6.0 à 7.3/10 (mécanique post-rebond), entraînant le Score Global ajusté de 48.0 à 51.2/100 et l'upgrade SURVEILLER → ATTENDRE.
3. **Volume révisé à 0.61× moyenne 20j** (76.2M vs 183.6M au snapshot 13:00 UTC). Ce révision à la baisse atténue la conviction sur le rebond.
4. **Niveaux SL/TP révisés** à la hausse ($12.56 / $18.11) compte tenu du nouveau close et de l'ATR stable.

**Ce qui n'a pas changé :**
- Filtre Qualité hors périmètre (2.5/6) — pas de changement qualitatif.
- Aucun catalyseur fondamental détecté.
- Consensus analystes $10.8 (7 analysts) — premium persistant +36.8%.
- XLC bottom 3 du sector rotation.
- Options inchangées (max pain $15.00, put/call 1.00, expiration 12/06).
- Aucun événement corporate, aucune news structurante.

**Recommandation révisée :** **ATTENDRE** — Pas de position. Le rebond de +2.75% est mécaniquement positif mais le volume révisé à la baisse (0.61×) et l'absence de catalyseur fondamental maintiennent l'exclusion d'entrée. La proximité du max pain ($15.00, expiration dans 4 jours) crée un overhang technique. Une entrée reste exclue sans :
- Test et rebond sur la MM50 ($12.29) avec volume > moyenne
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel ou corporate

**Prochain point de contrôle :** Earnings Q2 FY2026 le **2026-07-23** (dans 45 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 17:00 UTC), `data/recommandations_latest.json`, et fichiers JSON agents.*

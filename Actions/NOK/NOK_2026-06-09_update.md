# NOK — Mise à jour quotidienne (Snapshot 17:00 UTC)

> **Date :** 2026-06-09
> **Type :** Update — gap baissier -7.98%, passage SURVEILLER, correction post-surchauffe
> **Fichier précédent :** [NOK_2026-06-09_update.md](./NOK_2026-06-09_update.md) (snapshot 13:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-09 13:00 UTC | 2026-06-09 17:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Cours close** | $14.59 | **$13.425** | **-7.98%** 🔴 |
| **Change vs previous close** | +1.46% | **-7.98%** | **-9.44 pts** |
| **RSI 14j** | 54.58 | **48.82** | **-5.76 pts** |
| **Volume session** | 102.6M (0.82×) | **141.5M (1.13×)** | **+38.0%** |
| **ATR 14j** | $1.11 | **$1.15** | **+$0.04** |
| **MM 50j** | $12.29 | **$12.40** | +$0.11 |
| **Max pain options** | $15.00 | **$15.00** | — |
| **Put/Call ratio** | 0.78 | **0.78** | — |
| **Call OI %** | 56.2% | **56.2%** | — |
| **Score Global ajusté** | 51.2 — ATTENDRE | **48.0 — SURVEILLER** | **-3.2 pts** 🔴 |
| **Recommandation** | ATTENDRE | **SURVEILLER** | **Rétrogradé** |

**Verdict :** Le snapshot 17:00 UTC enregistre un **gap baissier de -7.98%** sans catalyseur identifié. Aucune news structurante (`news_2026-06-09.json` vide pour NOK), aucun événement corporate (`events_2026-06-09.json` vide). La baisse s'inscrit dans la **correction post-surchauffe** des semaines précédentes (cours avait doublé depuis début mai sans fondamental). Le passage de **ATTENDRE à SURVEILLER** est mécanique : le score global ajusté recule de 51.2 à **48.0/100** (seuil 35–49). Le volume en hausse de 38% à 1.13× la moyenne 20j confirme une participation vendeuse réelle, pas un gap sur volume anémique.

**DRAFT_refresh traité :** Triggers `PRICE_GAP` (-7.98%) et `ATR_SPIKE` (8.57%) **confirmés** — non faux positifs. Le gap est accompagné de volume supérieur à la moyenne et d'une cassure du niveau d'ouverture du jour. Archivé.

> **[DONNÉES PARTIELLES]** : `validation_report.txt` du 2026-06-09 signale un warning qualité sur NOK (Quality hors périmètre 2–2.5/6 ; P/E 87.19 très élevé ; cours +50% vs consensus). Ce warning est inchangé depuis le 2026-05-17. Le P/E Yahoo mécanique descend à **83.91** avec le cours $13.425.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Open | $14.58 | Yahoo Finance |
| High | $14.62 | Yahoo Finance |
| Low | **$13.18** | Yahoo Finance |
| Close | **$13.425** | Yahoo Finance |
| Change vs previous close | **-7.98%** | Yahoo Finance |
| Volume | 141,527,661 | Yahoo Finance |
| Volume vs moy. 20j | **1.13×** | Calcul (125.5M) |
| RSI 14j | **48.82** | Calcul agent |
| ATR 14j | **$1.15** | Calcul agent |
| MM 50j | **$12.40** | Calcul agent |
| MM 200j | — | N/A |

**Niveaux clés révisés :**
- Support immédiat : **$13.18** (low du jour)
- Support structurel : **$12.40** (MM50)
- Résistance : **$14.58** (open du jour) / **$14.59** (previous close)
- Résistance gap : **$15.47** (base du gap haussier du 25/05, non comblé)
- Max pain options : **$15.00** (expiration 2026-06-12 dans 3 jours)
- Stop-loss ATR (2×) : **$11.12** ($13.425 − $2.30)
- Take-profit ATR (3×) : **$16.88** ($13.425 + $3.45)
- Ratio R/R : **1.5×**

**Verdict timing :** Défavorable — Le gap baissier de -7.98% avec volume supérieur à la moyenne rompt la consolidation des deux derniers jours ($14.59). Le RSI retourne sous les 50 (48.82), sortant la zone neutre constructive. Le cours se situe désormais à **-10.5% sous le max pain** ($15.00), ce qui élimine le pin risk à la baisse mais reflète un déséquilibre vendeur. Le niveau critique à surveiller est la MM50 à $12.40 : une cassure sous ce niveau avec volume ouvrirait la voie vers le consensus $10.8.

---

## 3. Bloc Fondamental

Inchangé en structure ; mécanique de cours uniquement.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $74.9B | Yahoo Finance (↓ vs $81.4B à 13h) |
| P/E (TTM) | 83.91 | Yahoo Finance (↓ mécanique vs 91.19) |
| Forward P/E | 27.58 | Yahoo Finance |
| EV/EBITDA | 31.21 | Yahoo Finance |
| P/B | 3.05 | Yahoo Finance (↓ vs 3.32) |
| Beta | 0.781 | Yahoo Finance |
| Dividend Yield | 1.12% | Yahoo Finance |
| Short Interest | 1.08% | Yahoo Finance |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé). Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 83.91 vs P/E FMP 45.81. La baisse du cours réduit mécaniquement le P/E Yahoo mais ne modifie pas le verdict consensus calibré sur l'ADR.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API |
| Max pain options | **$15.00** | `data/latest.json` |
| Put/Call ratio | **0.78** | `data/latest.json` |
| Call OI % | **56.2%** | `data/latest.json` |
| Expiration nearest | **2026-06-12** | Yahoo Finance |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_latest.json` |

**Structure options (inchangée vs 13h) :**
- Max pain **$15.00** inchangé. Cours $13.425 < max pain (−10.5%) — le pin risk s'inverse : le cours est désormais loin sous le max pain. Les writers de puts sont en position favorable.
- Put/call **0.78** inchangé — structure call-biased persistante malgré la baisse, ce qui peut refléter une prise de bénéfices sur calls plutôt qu'un achat de protection.
- Call OI **56.2%** inchangé.
- Expiration dans 3 jours (2026-06-12). Le gap a éloigné le cours du max pain ; le risque de pin s'est déplacé vers un potentiel rebond technique vers $15.00, mais la probabilité est faible sans catalyseur.

**News / Événements :**
- `events_2026-06-09.json` : **0 événement** corporate pour NOK
- `news_2026-06-09.json` : **0 article** pour NOK
- Aucune mention Reddit, aucun pump/dump détecté
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_latest.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (momentum score 0.0, RS20d −4.03% vs SPY). Malus structurel pour NOK — le gap baissier s'inscrit dans la sous-performance sectorielle.
- **Exposition FX :** 25% revenus hors-USD, impact neutre (`fx_exposure_2026-06-09.json` : fx_impact_score 0.0, flag 🟢). Aucune divergence détectée.
- **Géopolitique :** Score politique 2/10, non exposé (`geo_risk_2026-06-09.json` : aucun événement politique détecté pour NOK)
- **Quant :** Insuffisant (`quant_2026-06-09.json` : 0 signaux historiques, p-value 1.0)

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-09.json` (snapshot 17:00 UTC)

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.3/10** | C:4.0 V:3.5 M:6.0 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 83.9, premium consensus +24.3% |
| **Score Momentum** | 6.0/10 | 🟡 Tendance haussière structurelle fragilisée (cours +8.3% vs MM50, ↓ vs +18.7% à 13h) |
| **Score Global ajusté** | **48.0/100** | **SURVEILLER** (seuil 35–49) |
| **Timing technique** | Défavorable | Gap baissier, RSI sous 50, volume vendeur |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 08/06 21:00 : Score Global 51.2 — ATTENDRE
- Le 09/06 13:00 : Score Global **51.2** — **ATTENDRE**
- Le 09/06 17:00 : Score Global **48.0** — **SURVEILLER** (rétrogradation)

Le scoring recule de **3.2 pts** sous l'effet de la baisse de cours qui pèse sur le Score Momentum (7.3 → 6.0) et surtout qui fait passer l'action sous le seuil ATTENDRE. Les scores Catalyseur (4.0) et Valorisation (3.5) sont inchangés. Le Filtre Qualité 2.5/6 maintient le plafond sur la valorisation. Aucun catalyseur fondamental n'est apparu pour contrebalancer la détérioration technique.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (13:00 UTC) | Valeur actuelle (17:00 UTC) | Justification |
|--------|-------------------------------|----------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé |
| **Stop-loss** | $12.37 | **$11.12** | Cours − 2×ATR révisé ($13.425 − $2.30) |
| **Take-profit** | $17.92 | **$16.88** | Cours + 3×ATR révisé ($13.425 + $3.45) |
| **Upside / Downside** | −26.9% / −15.2% | **−19.6%** / **−17.2%** | Révisé |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (asymétrie réduite mais ratio inchangé) |
| **Sizing** | — | **—** | Pas de position |

---

## 8. Scénarios & Probabilités

Révisés post-gap.

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 15% | Rebond vers $14.58 (open du jour) | Absorption du gap sur volume faible, retour rapide vers la zone $14.50. Nécessite absence de vente institutionnelle et stabilisation du secteur XLC |
| **Central** | 50% | Range $13.20–$14.00 | Consolidation autour de $13.50. La MM50 ($12.40) sert d'ancre si le cours dérive à la baisse. Pas de catalyseur = pas de direction claire |
| **Pessimiste** | 35% | Cassure $13.18 → test $12.40 (MM50) | Distribution continue, retour vers la MM50. Si cassure de la MM50 avec volume, objectif $11.12 (SL) puis $10.8 (consensus). Volume élevé aujourd'hui = possible distribution institutionnelle |

---

## 9. Conclusion — Thèse modifiée

**Verdict :** La thèse **ATTENDRE** est **modifiée en SURVEILLER** suite au gap baissier de -7.98% et à la détérioration du score global (51.2 → 48.0).

**Ce qui a changé :**
- **Cours** : chute de -7.98% ($13.425 vs $14.59), effaçant le gain de la veille et cassant la consolidation des 8–9 juin.
- **Volume** : 141.5M (+38% vs 13h), 1.13× la moyenne 20j — participation vendeuse confirmée, pas un gap technique sans volume.
- **RSI** : 48.82 (sortie de la zone neutre constructive >50), signal technique de fragilisation.
- **Score Global** : passage de **ATTENDRE (51.2)** à **SURVEILLER (48.0)** — rétrogradation mécanique.
- **Niveaux SL/TP** : révisés à la baisse ($11.12 / $16.88) en raison du nouveau cours et de l'ATR élargi.
- **DRAFT_refresh archivé** : triggers PRICE_GAP (-7.98%) et ATR_SPIKE (8.57%) confirmés comme réels.

**Ce qui n'a pas changé :**
- Filtre Qualité hors périmètre (2.5/6) — pas de changement qualitatif.
- Aucun catalyseur fondamental détecté (0 news, 0 événement corporate).
- Consensus analystes $10.8 (7 analysts) — premium persistant +24.3% (vs +35.1% à $14.59).
- XLC bottom 3 du sector rotation.
- Options structure call-biased (put/call 0.78, call OI 56.2%) inchangée.
- Exposition FX neutre.

**Recommandation révisée :** **SURVEILLER** — Pas de position. Le gap baissier de -7.98% avec volume supérieur à la moyenne rompt la stabilité apparente des derniers jours. La thèse précédente « ATTENDRE » reposait sur une consolidation au-dessus de $14.50 avec RSI neutre ; cette configuration est invalidée. Une entrée reste exclue sans :
- Test et rebond sur la MM50 ($12.40) avec volume > moyenne et pattern de reversal
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel (contrat 5G, upgrade, news structurante)

**Risque immédiat :** La proximité de la MM50 ($12.40, soit -7.6% sous le cours) est le prochain niveau clé. Une cassure sous cette MM50 avec volume confirmerait un renversement de tendance de moyen terme.

**Prochain point de contrôle :** Earnings Q2 FY2026 le **2026-07-23** (dans 44 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-09 17:00 UTC), `data/recommandations_2026-06-09.json`, `data/geo_2026-06-09.json`, `data/sector_rotation_2026-06-09.json`, `data/fx_exposure_2026-06-09.json`, et fichiers JSON agents.*

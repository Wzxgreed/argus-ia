# NOK — Mise à jour quotidienne (Snapshot 10:00 UTC)

> **Date :** 2026-06-15
> **Type :** Update + Full Refresh (triggers PRICE_GAP +5.04%, ATR_SPIKE 7.50%)
> **Fichier précédent :** [NOK_2026-06-10_13h_update.md](./NOK_2026-06-10_13h_update.md)

---

## 1. Résumé des changements

| Métrique | 2026-06-10 13:00 UTC | 2026-06-15 10:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Previous close** | $14.59 | **$14.09** | −$0.50 (−3.4%) |
| **Close session** | NaN | **$14.80** | [DONNÉES PARTIELLES RÉSOLUES] |
| **Change %** | — | **+5.04%** | Gap haussier overnight |
| **RSI 14j** | 55.0 | **46.61** | −8.39 pts |
| **Volume session** | 178.7M (carry-forward) | **117,658,200** | −34.1% |
| **Volume vs moy. 20j** | 1.40× | **0.95×** | Retour sous moyenne |
| **ATR 14j** | null | **$1.11** | [DONNÉES RESTAURÉES] |
| **MM 50j** | null | **$12.77** | [DONNÉES RESTAURÉES] |
| **MM 200j** | null | **null** | [DONNÉES MANQUANTES] |
| **Options max pain** | $15.00 (expiration 06-12) | **$1.00** (expiration 06-18) | 🔴 Corrompu — ignoré |
| **Put/Call ratio** | 0.75 | **null** | [DONNÉES MANQUANTES] |
| **Call OI %** | 57.1% | **null** | [DONNÉES MANQUANTES] |
| **Score Global ajusté** | 50.5 — ATTENDRE | **51.8 — ATTENDRE** | +1.3 pt (mécanique) |
| **Recommandation** | ATTENDRE | **ATTENDRE** | Confirmée |

**Verdict :** Le snapshot du 15/06 matérialise un **gap haussier de +5.04%** ($14.09 → $14.80) sur volume **sous-moyen** (0.95×). Les données techniques manquantes depuis le 10/06 sont restaurées (ATR $1.11, MM50 $12.77), confirmant un gap intraday de $14.24–$15.07. Le RSI recule de 55.0 à **46.61** (sortie de la zone neutre constructive), révélant une divergence baissière momentum/prix : le rebond du jour s'accompagne d'une **perte de momentum**. Les données options sont corrompues ($1.00 aberrant) — le max pain opérationnel du 10/06 ($15.00, expiration 06-12) est obsolète ; la nouvelle expiration est le **06-18** sans données fiables. Aucun catalyseur fondamental, aucune news, aucun événement corporate. Le Score Global ajusté progresse mécaniquement de 50.5 à **51.8/100** (seuil ATTENDRE), tiré par la hausse du Score Momentum (6.0 → 7.5), mais les scores Catalyseur (5.0 → 4.0) et Valorisation (4.5 → 3.5) se dégradent. La thèse **ATTENDRE** reste strictement inchangée.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$14.09** | `data/latest.json` | Close du 14/06 |
| Open | **$14.34** | `data/latest.json` | Gap haussier +1.77% |
| High | **$15.07** | `data/latest.json` | Test de la résistance $15.00 |
| Low | **$14.24** | `data/latest.json` | Support intraday |
| Close | **$14.80** | `data/latest.json` | +5.04% vs previous close |
| Volume | **117,658,200** | `data/latest.json` | −34% vs carry-forward 10/06 |
| Volume vs moy. 20j | **0.95×** | Calcul (123.6M) | Sous-moyenne — participation faible |
| RSI 14j | **46.61** | `data/latest.json` | Sortie zone neutre constructive (50+) |
| ATR 14j | **$1.11** | `data/latest.json` | Volatilité relative 7.50% (seuil 5.0% dépassé) |
| MM 50j | **$12.77** | `data/latest.json` | Cours +15.9% au-dessus |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Golden Cross | **Non** | `data/latest.json` | — |
| 52w high / low | **$17.45 / $4.00** | `data/latest.json` | Cours à −15.2% du 52w high |

**Niveaux clés (révisés avec données consolidées) :**
- Support immédiat : **$14.24** (low du jour)
- Support structurel : **$12.77** (MM50)
- Résistance gap : **$15.07** (high du jour) / **$15.00** (résistance psychologique + ancien max pain)
- Stop-loss ATR (2×) : **$12.58** ($14.80 − 2×$1.11)
- Take-profit ATR (3×) : **$18.13** ($14.80 + 3×$1.11)
- Ratio R/R : **1.5×**

**Verdict timing :** **Neutre** — Le cours reste au-dessus de la MM50 (+15.9%), ce qui est constructif de moyen terme. Cependant, le RSI à 46.61 (sous 50) et le volume sous-moyen (0.95×) invalident la notion de momentum haussier confirmé. Le range intraday élevé ($0.83, 5.6% du cours) génère un ATR relatif de 7.50% qui déclenche le seuil d'alerte volatilité, mais en l'absence de catalyseur, ce spike est interprété comme un **faux positif technique** (volatilité sans direction). Le gap du jour n'est pas comblé à la hausse — il s'agit d'un gap de continuation haussière, mais sur liquidité réduite.

---

## 3. Bloc Fondamental

Inchangé en structure. [DONNÉES PARTIELLES] sur quality gate (validation report).

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $82.6B (Yahoo) / $29.8B (FMP) | `data/latest.json` |
| P/E (TTM) | 92.5 (Yahoo) / 45.81 (FMP) | `data/latest.json` |
| Forward P/E | 30.40 | `data/latest.json` |
| EV/EBITDA | 31.68 (Yahoo) / 13.13 (FMP) | `data/latest.json` |
| P/B | 3.37 (Yahoo) / 1.42 (FMP) | `data/latest.json` |
| Beta | 0.781 | `data/latest.json` |
| Dividend Yield | 1.11% (Yahoo) / 2.55% (FMP) | `data/latest.json` |
| Short Interest | 1.19% | `data/latest.json` |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |
| FMP Gross Margin | 43.5% | FMP Stable API |
| FMP Operating Margin | 3.9% | FMP Stable API |
| FMP ROIC | 1.9% | FMP Stable API |
| FMP D/E | 0.25 | FMP Stable API |
| FMP Net Debt/EBITDA | −0.11 (net cash) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé).
- Assets/Liabilities > 1.0 : ✅ (bilan solide, net cash)
- FCF positif : ✅ (FCF yield 4.9%)
- Revenue CAGR ≥ 20% : ❌ (marché mature)
- Profit CAGR ≥ 20% : ❌ (rentabilité erratique)
- Moat structurel : ❌ (concurrence Ericsson/Huawei/Samsung)
- TAM ×5 / 10 ans : ❌ (marché telecom equipment saturé)

**Divergence structurelle Yahoo/FMP persistante et amplifiée :**
- P/E Yahoo 92.5 vs FMP 45.81 (écart +102%)
- Market cap Yahoo $82.6B vs FMP $29.8B (écart +177%)
- Cette divergence n'affecte pas le verdict consensus : les 7 analystes FMP ciblent **$10.8**, soit **−27.0%** de downside vs le cours $14.80.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé — premium consensus +37.0% |
| Max pain options | **$1.00** | `data/latest.json` | 🔴 Corrompu — aberrant, ignoré |
| Put/Call ratio | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Call OI % | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Expiration nearest | **2026-06-18** | `data/latest.json` | Dans 3 jours |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_2026-06-15.json` | Aucune mention, aucun pump |

**Structure options :**
- Données options corrompues dans `latest.json` (max pain $1.00, put/call et call OI null). La structure de la semaine dernière (max pain $15.00, expiration 06-12) est obsolète.
- Avec un close $14.80 et une nouvelle expiration le 06-18, le pin risk est **indéterminé** faute de données fiables. L'écart historique au dernier max pain opérationnel ($15.00) est de **−1.3%** — proche du pin, mais cette donnée est périmée.
- Le volume options n'est pas disponible.

**News / Événements :**
- `events_2026-06-15.json` : **0 événement** corporate pour NOK
- `news_latest.json` : **0 article** pour NOK
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 38 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_2026-06-15.json` — VIX et taux non disponibles)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_2026-06-15.json` : momentum score 0.0). Malus structurel persistant.
- **Exposition FX :** 25% revenus hors-USD, impact neutre (`fx_exposure_2026-06-15.json` : fx_impact_score 0.0, flag 🟢). Aucune divergence détectée.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_latest.json` du 2026-05-17 : 0 ticker flaggé)
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent — pas de donnée M-Score/Z-Score disponible. Le Data Quality Gate mentionne "Quality hors périmètre 2–2.5/6".

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-15.json`

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.7/10** | C:4.0 V:3.5 M:7.5 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 92.5, premium consensus +37.0% |
| **Score Momentum** | 7.5/10 | 🟢 Tendance haussière structurelle (cours > MM50) |
| **Score Global ajusté** | **51.8/100** | **ATTENDRE** (seuil 50–59) |
| **Timing technique** | Neutre | RSI 46.61 sous 50, volume sous-moyen, MM50 validée |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 08/06 21h : Score Global 51.2 — ATTENDRE
- Le 09/06 21h : Score Global 48.0 — SURVEILLER
- Le 10/06 13h : Score Global **50.5** — **ATTENDRE**
- Le 15/06 : Score Global **46.8** (ajusté **51.8**) — **ATTENDRE**

Le scoring brut recule de 50.5 à 46.8 (−3.7 pts), mais l'ajustement global reste à **51.8/100** — **ATTENDRE** (seuil 50–59 inchangé). La dégradation des scores Catalyseur (−1.0 pt) et Valorisation (−1.0 pt) reflète l'absence de nouvelles et l'amplification du premium de valorisation (cours $14.80 vs consensus $10.8). Le Score Momentum progresse de 6.0 à 7.5 grâce à la confirmation du cours au-dessus de la MM50 ($12.77), mais cette progression est **mécanique** et non fondée sur un volume confirmant. Le Filtre Qualité 2.5/6 maintient le plafond structurel.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (10/06 13h) | Valeur actuelle (15/06) | Justification |
|--------|-------------------------------|------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé — 7 analystes FMP |
| **Stop-loss** | $11.55 | **$12.58** | Révisé — ATR $1.11 restauré, close $14.80 |
| **Take-profit** | $17.30 | **$18.13** | Révisé — ATR $1.11 restauré, close $14.80 |
| **Upside / Downside** | −22.0% / −16.6% | **−27.0% / −15.0%** | Cours $14.80 vs consensus $10.8 |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (ATR-based) |
| **Sizing** | — | **—** | Pas de position |

**Note :** Les niveaux sont révisés à la hausse (SL $11.55 → $12.58, TP $17.30 → $18.13) car le close de session ($14.80) et l'ATR ($1.11) sont désormais disponibles. Le SL reste protecteur : une cassure sous $12.58 placerait le cours sous la MM50 ($12.77), invalidant la tendance de moyen terme.

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 15% | Rebond vers $15.07+ | Le gap haussier du jour se confirme avec volume > moyenne en séance suivante. Test du high $15.07 puis franchissement vers $15.50. Nécessite catalyseur (news 5G, upgrade, contrat) |
| **Central** | 60% | Range $13.80–$14.80 | Consolidation autour du close $14.80. Pas de catalyseur = pas de direction claire. Support $14.24 validé, résistance $15.00 agit comme plafond. Attente des earnings du 23/07 |
| **Pessimiste** | 25% | Retest $13.80 puis $12.77 (MM50) | Le gap du jour est un faux signal (volume faible). Retour vers la MM50 si le momentum technique s'érode davantage (RSI sous 40). Cassure MM50 = renversement de tendance de moyen terme |

**Probabilité ajustée :** Le scénario central reste dominant (60%) car l'absence de catalyseur et le volume sous-moyen rendent improbable une continuation haussière immédiate. Le scénario optimiste est réduit à 15% (vs 20% précédemment) en raison de la dégradation du RSI et de l'absence de flux institutionnels.

---

## 9. Conclusion — Thèse confirmée

**Verdict :** La thèse **ATTENDRE** est strictement **confirmée**. Les triggers PRICE_GAP et ATR_SPIKE du 15/06 ne modifient pas la structure fondamentale.

**Ce qui a changé :**
- **Cours et technique :** Gap +5.04% ($14.09 → $14.80), high $15.07, low $14.24. RSI reculé à 46.61. ATR $1.11 et MM50 $12.77 restaurés. Volume 117.7M (0.95×), sous-moyen.
- **Options :** Données corrompues (max pain $1.00 aberrant, put/call et call OI null). Expiration 06-18 dans 3 jours. Pin risk indéterminé.
- **Scoring :** Score Global ajusté 51.8/100 (ATTENDRE), mais scores bruts Catalyseur (4.0) et Valorisation (3.5) en dégradation. Score Momentum 7.5 mécaniquement élevé (cours > MM50).
- **Niveaux :** SL/TP révisés à $12.58/$18.13 (ATR-based). Downside vs consensus élargi à −27.0%.

**Ce qui n'a pas changé :**
- Filtre Qualité hors périmètre (2.5/6) — bilan solide mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).
- Consensus analystes $10.8 (7 analysts) — premium +37.0%.
- Divergence Yahoo/FMP persistante et amplifiée (P/E 92.5 vs 45.81, market cap $82.6B vs $29.8B).
- XLC bottom 3 du sector rotation (momentum 0.0).
- Aucun catalyseur fondamental, aucune news structurante, aucun événement corporate.
- Exposition FX neutre, géopolitique neutre, social sentiment nul.
- Quant insuffisant, accounting non disponible.

**Recommandation révisée :** **ATTENDRE** — Pas de position. Une entrée reste exclue sans :
- Volume de confirmation > 1.2× moyenne 20j sur un test du support $14.24
- Stabilisation du RSI au-dessus de 50 avec un close confirmé
- Test et rebond sur la MM50 avec pattern de reversal
- Franchissement durable au-dessus de $15.07 (high du jour) avec volume
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel (contrat 5G, upgrade, guidance positive)

**Risque immédiat :** L'expiration des options le 2026-06-18 (dans 3 jours) avec des données corrompues empêche toute analyse de pin risk fiable. La volatilité relative élevée (ATR 7.50%) peut générer des faux signaux intraday.

**Prochain point de contrôle :** Attendre le snapshot post-ouverture du 15/06 (17h/21h UTC) pour consolider le volume de clôture et valider la tenue du gap. Earnings Q2 FY2026 le **2026-07-23** (dans 38 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-15 10:00 UTC), `data/recommandations_2026-06-15.json`, `data/sector_rotation_2026-06-15.json`, `data/fx_exposure_2026-06-15.json`, `data/social_sentiment_2026-06-15.json`, `data/upcoming_events_2026-06-15.json`, `data/events_2026-06-15.json`, et fichiers JSON agents.*
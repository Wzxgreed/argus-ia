# NOK — Mise à jour quotidienne (Snapshot 10:00 UTC)

> **Date :** 2026-06-17
> **Type :** Update — snapshot pré-ouverture NY 10:00 UTC
> **Fichier précédent :** [NOK_2026-06-16_21h_update.md](./NOK_2026-06-16_21h_update.md) (snapshot 21:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-16 21:00 UTC (précédent) | Snapshot actuel | Δ |
|----------|-----------------------------------|-----------------|---|
| **Close** | **$13.855** | **$13.98** | **+$0.125 (+0.90%)** |
| **Open** | $14.76 | **$14.76** | Inchangé |
| **High** | $14.79 | **$14.79** | Inchangé |
| **Low** | $13.81 | **$13.75** | **−$0.06** |
| **Previous close** | $14.82 | **$14.82** | Inchangé |
| **RSI 14j** | 39.98 | **40.53** | **+0.55 pt** |
| **ATR 14j** | $1.08 | **$1.09** | **+$0.01** |
| **MM 50j** | $12.99 | **$12.99** | Inchangé |
| **Volume session** | 81,575,372 | **123,742,900** | **+51.6%** |
| **Volume vs moy. 20j** | 0.66× | **0.98×** | **+0.32×** |
| **Options max pain** | $14.00 | **$14.00** | Inchangé (opérationnel) |
| **Put/Call ratio** | 0.47 | **0.47** | Inchangé (opérationnel) |
| **Call OI %** | 68.1% | **68.1%** | Inchangé (opérationnel) |
| **Score Global ajusté** | 44.2 — SURVEILLER | **44.2 — SURVEILLER** [^1] | Inchangé |
| **Score Opportunité** | 3.9/10 | **3.9/10** [^1] | Inchangé |
| **Score Momentum** | 4.5/10 | **4.5/10** [^1] | Inchangé |

[^1]: `data/recommandations_2026-06-17.json` ne contient pas de scoring pour NOK. Les scores du 16/06 sont reportés à titre indicatif. Le snapshot technique indique une légère amélioration du momentum (RSI remonté, volume normalisé) sans modifier la classification.

**Verdict :** Le snapshot 10h UTC enregistre un **léger rebond technique** de +0.90% à **$13.98** par rapport au close du 16/06 21h ($13.855), bien que le change vs previous close reste à **−5.67%** (gap baissier overnight confirmé). Le volume a fortement récupéré de 81.6M à **123.7M**, ramenant la participation de 0.66× à **0.98×** la moyenne 20j — **normalisation significative** invalidant le signal de désengagement du snapshot précédent. Le RSI remonte à **40.53** (+0.55 pt), sortant de la zone de survente stricte (<40). Le low du jour est légèrement plus bas à **$13.75** (−$0.06), marquant un nouveau test du support avant le rebond. Les données options restent **corrompues** dans `latest.json` ; les valeurs opérationnelles du 16/06 ($14.00 / 0.47 / 68.1%) sont conservées. L'expiration est **demain** (2026-06-18).

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$14.82** | `data/latest.json` | Carry-forward |
| Open | **$14.76** | `data/latest.json` | −0.40% vs previous close |
| High | **$14.79** | `data/latest.json` | Résistance intraday non renouvelée |
| Low | **$13.75** | `data/latest.json` | **Nouveau low** — test support étendu |
| Close | **$13.98** | `data/latest.json` | −5.67% vs previous close |
| Volume | **123,742,900** | `data/latest.json` | Normalisation post-session |
| Volume vs moy. 20j | **0.98×** | Calcul (126.3M) | Participation revenue à la moyenne |
| RSI 14j | **40.53** | `data/latest.json` | Sortie de la survente stricte |
| ATR 14j | **$1.09** | `data/latest.json` | Volatilité stable |
| MM 50j | **$12.99** | `data/latest.json` | Cours +7.6% au-dessus |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Golden Cross | **Non** | `data/latest.json` | — |
| 52w high / low | **$17.45 / $4.00** | `data/latest.json` | Cours à −19.9% du 52w high |

**Niveaux clés (révisés) :**
- Support immédiat : **$13.75** (low du jour)
- Support intermédiaire : **$13.50** (zone de consolidation du 08/06)
- Support structurel : **$12.99** (MM50)
- Résistance gap : **$14.00** (max pain options / ancien support psychologique)
- Résistance technique : **$14.27** (ancien support devenu résistance) / **$14.82** (previous close)
- Stop-loss ATR (2×) : **$11.80** ($13.98 − 2×$1.09)
- Take-profit ATR (3×) : **$17.25** ($13.98 + 3×$1.09)
- Ratio R/R : **1.5×**

**Verdict timing :** **Neutre à légèrement défavorable** — Le gap baissier de −5.67% vs previous close reste le facteur dominant. Cependant, le volume normalisé (0.98×) et le RSI remonté à 40.53 atténuent le biais baissier du snapshot précédent. Le cours reste au-dessus de la MM50 (+7.6%). Le low $13.75 est un nouveau test du support avant rebond intraday vers $13.98. L'ATR relatif ($1.09 / $13.98 = 7.8%) reste élevé. Configuration de consolidation post-gap sans direction claire.

---

## 3. Bloc Fondamental

Inchangé en structure. Quality gate passé aujourd'hui (`quality_gate_2026-06-17.json` : status **ok**).

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $78.0B (Yahoo) / $29.8B (FMP) | `data/latest.json` |
| P/E (TTM) | 87.38 (Yahoo) / 45.81 (FMP) | `data/latest.json` |
| Forward P/E | 28.72 | `data/latest.json` |
| EV/EBITDA | 29.87 (Yahoo) / 13.13 (FMP) | `data/latest.json` |
| P/B | 3.18 (Yahoo) / 1.42 (FMP) | `data/latest.json` |
| Beta | 0.781 | `data/latest.json` |
| Dividend Yield | 1.17% (Yahoo) / 2.55% (FMP) | `data/latest.json` |
| Short Interest | 1.19% | `data/latest.json` |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |
| FMP Gross Margin | 43.5% | FMP Stable API |
| FMP Operating Margin | 3.9% | FMP Stable API |
| FMP ROIC | 1.9% | FMP Stable API |
| FMP D/E | 0.25 | FMP Stable API |
| FMP Net Debt/EBITDA | −0.11 (net cash) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé).

**Divergence structurelle Yahoo/FMP persistante :**
- P/E Yahoo 87.38 vs FMP 45.81 (écart +91%)
- Market cap Yahoo $78.0B vs FMP $29.8B (écart +162%)
- Consensus FMP cible **$10.8**, soit **−22.7%** de downside vs le cours $13.98.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé — premium consensus réduit à +28.7% |
| Max pain options | **$14.00** | Opérationnel (16/06) | Valeur `latest.json` corrompue ($1.00) — conservée $14.00 |
| Put/Call ratio | **0.47** | Opérationnel (16/06) | Valeur `latest.json` null — conservée 0.47 |
| Call OI % | **68.1%** | Opérationnel (16/06) | Valeur `latest.json` null — conservée 68.1% |
| Expiration nearest | **2026-06-18** | `data/latest.json` | **Demain** (1 jour) |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_2026-06-17.json` | Aucune mention, aucun pump |

**Structure options (valeurs opérationnelles du 16/06 conservées) :**
- Max pain **$14.00** (opérationnel). Cours $13.98 = **−0.14% sous le max pain**. Le pin risk est quasiment nul : le cours est aligné sur le max pain. L'inversion du pin risk observée au snapshot 21h (cours −1.0% sous max pain) est atténuée.
- Put/call 0.47 et call OI 68.1% inchangés — structure haussière des options préservée.
- Expiration **demain** (2026-06-18). Le risque de pin est minimisé par l'alignement cours/max pain.

**News / Événements :**
- `events_2026-06-17.json` : **0 événement** corporate pour NOK
- `news_2026-06-17.json` : **0 article** pour NOK
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 36 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_2026-06-17.json` — VIX et taux non disponibles)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_2026-06-17.json` : return 20j −3.98%, return 60j +0.40%, momentum score 0.0). Malus structurel persistant.
- **Exposition FX :** Données indisponibles pour NOK dans `fx_exposure_2026-06-17.json`. Contexte précédent : 25% revenus hors-USD, impact neutre. Aucune divergence détectée historiquement.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_2026-06-17.json` : geo_risk_score 2/10, flag 🟢, 0 événement).
- **Quant :** Insuffisant (`quant_report_2026-06-17.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent (`accounting_risk_latest.json`) — pas de donnée M-Score/Z-Score disponible.
- **Validation :** Quality gate **ok** aujourd'hui (`quality_gate_2026-06-17.json`). Les warnings précédents (Quality hors périmètre, P/E élevé, cours +50% vs consensus) sont des caractéristiques structurelles, non des anomalies de données.

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-17.json` ne contient pas de scoring pour NOK. Scores du 16/06 reportés avec ajustement manuel du momentum.

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **3.9/10** [est.] | C:4.0 V:3.5 M:4.5 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 87.4, premium consensus +28.7% |
| **Score Momentum** | 4.5/10 | 🔴 Faible — RSI 40.53, volume normalisé, low plus bas |
| **Score Global ajusté** | **44.2/100** [est.] | **SURVEILLER** (seuil 35–49) |
| **Timing technique** | Neutre à défavorable | RSI remonté mais sous 50, MM50 validée, gap baissier −5.67% |

**Évolution du scoring :**
- Le 15/06 13h : Score Global 51.8 — ATTENDRE
- Le 15/06 17h : Score Global 46.8 — SURVEILLER
- Le 15/06 21h : Score Global 46.8 — SURVEILLER
- Le 16/06 10h : Score Global **46.8** — **SURVEILLER**
- Le 16/06 17h : Score Global **46.8** — **SURVEILLER**
- Le 16/06 21h : Score Global **44.2** — **SURVEILLER**
- Snapshot actuel : Score Global **44.2** — **SURVEILLER** (stable)

Le scoring reste stable dans la zone SURVEILLER. Le léger rebond technique (+0.90%) et la normalisation du volume (0.98×) compensent le nouveau low plus bas ($13.75) et le gap baissier persistant (−5.67%). Le Filtre Qualité 2.5/6 maintient le plafond structurel. Aucun agent n'a généré de nouveau scoring pour NOK ce matin.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (21h UTC 16/06) | Valeur actuelle | Justification |
|--------|-----------------------------------|-----------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé — 7 analystes FMP |
| **Stop-loss** | $11.70 | **$11.80** | Révisé — ATR $1.09, close $13.98 |
| **Take-profit** | $17.09 | **$17.25** | Révisé — ATR $1.09, close $13.98 |
| **Upside / Downside** | −22.1% / −15.5% | **−22.7% / −15.6%** | Cours $13.98 vs consensus $10.8 |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (ATR-based) |
| **Sizing** | — | **—** | Pas de position |

**Note :** Les niveaux sont révisés à la hausse en raison du rebond du cours ($13.855 → $13.98) et de l'ATR légèrement plus élevé ($1.08 → $1.09). Le SL à $11.80 correspond à 2×ATR sous le close actuel. Une cassure sous $12.99 (MM50) invaliderait la tendance haussière de moyen terme.

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 15% | Rebond vers $14.27–$14.50 | Le cours tient le support $13.75 et rebondit avec volume confirmé > moyenne 20j. Test de la résistance $14.27 (ancien support). Le max pain $14.00 agit comme aimant modéré. Nécessite catalyseur (news 5G, upgrade, contrat). |
| **Central** | 60% | Range $13.75–$14.20 | Consolidation autour du close $13.98. Le max pain $14.00 minimise le pin risk (cours −0.14%). Support $13.75 validé, résistance $14.27 agit comme plafond. Attente des earnings du 23/07. Pas de direction claire sans catalyseur. |
| **Pessimiste** | 25% | Retest $13.50 puis $12.99 (MM50) | Le gap baissier de −5.67% se poursuit. Test du support $13.50 (base du gap du 08/06). Si cassure, objectif MM50 $12.99. Volume normalisé (0.98×) ne garantit pas l'accumulation. RSI sous 50 = biais baissier sous-jacent. |

**Probabilité ajustée :** Le scénario central reste dominant (60%). L'expiration options **demain** (2026-06-18) avec max pain $14.00 et cours quasi-aligné (−0.14%) élimine pratiquement le pin risk. Le support $13.75 (low du jour) est le niveau critique à surveiller. La normalisation du volume est une nuance constructive mais non suffisante pour modifier la trajectoire sans catalyseur.

---

## 9. Conclusion — Thèse confirmée

**Verdict :** La thèse **SURVEILLER** est **confirmée** sans modification. Le snapshot du matin apporte un **léger rebond technique** (+0.90% vs close 21h) avec une **normalisation du volume** (0.98×), atténuant la pression baissière du snapshot précédent. Cependant, le gap baissier de −5.67% vs previous close et le nouveau low $13.75 maintiennent le biais défavorable.

**Ce qui a changé :**
- **Cours :** Rebond de **+$0.125 (+0.90%)** à **$13.98** (vs $13.855 au snapshot 21h). Change vs previous close **−5.67%**.
- **Volume :** Normalisation de 81.6M à **123.7M** (0.98× moyenne 20j) — participation revenue à la moyenne, invalidant le signal de désengagement du snapshot précédent.
- **RSI :** Remontée à **40.53** (+0.55 pt), sortie de la zone de survente stricte (<40).
- **Low :** Nouveau low **$13.75** (−$0.06 vs $13.81), marquant un test étendu du support.
- **ATR :** Légère hausse à **$1.09** (+$0.01).
- **Max pain :** Alignement quasi-parfait : cours **−0.14% sous le max pain $14.00** (vs −1.0% précédemment). Pin risk atténué.
- **Niveaux SL/TP :** Révisés à la hausse (**$11.80 / $17.25**) en raison du rebond du cours.
- **Quality gate :** Passé aujourd'hui (status **ok**).

**Ce qui n'a pas changé :**
- MM50 stable à **$12.99**. Cours +7.6% au-dessus.
- Options structurellement inchangées (max pain $14.00, put/call 0.47, call OI 68.1%, expiration demain).
- Filtre Qualité hors périmètre (2.5/6) — bilan solide mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).
- Consensus analystes **$10.8** (7 analysts) — premium +28.7%.
- Divergence Yahoo/FMP persistante (P/E 87.4 vs 45.81, market cap $78.0B vs $29.8B).
- XLC bottom 3 du sector rotation (momentum score 0.0).
- Aucun catalyseur fondamental, aucune news structurante, aucun événement corporate.
- Exposition FX historiquement neutre, géopolitique neutre (score 2/10), social sentiment nul.
- Quant insuffisant, accounting non disponible.
- Score Global **44.2/100 — SURVEILLER** (stable).

**Recommandation révisée :** **SURVEILLER** — Pas de position. Une entrée reste exclue sans :
- Stabilisation du cours au-dessus de **$14.27** avec volume de confirmation > 1.1× moyenne 20j
- Retour du RSI au-dessus de **45** avec un close confirmé
- Test et rebond sur la MM50 ($12.99) avec pattern de reversal
- Franchissement durable au-dessus de **$14.82** (previous close) avec volume
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel (contrat 5G, upgrade, guidance positive)

**Risque immédiat :** L'expiration des options **demain** (2026-06-18) avec max pain $14.00. Le cours quasi-aligné (−0.14%) minimise le pin risk. Cependant, la structure call-dominated (call OI 68.1%) pourrait générer une pression haussière modérée si les calls ITM sont exercés.

**Prochain point de contrôle :** Snapshot post-session du 17/06 pour valider la tenue du support $13.75 et le volume de clôture. Earnings Q2 FY2026 le **2026-07-23** (dans 36 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-17 10:00 UTC), `data/recommandations_2026-06-17.json`, `data/sector_rotation_2026-06-17.json`, `data/fx_exposure_2026-06-17.json`, `data/social_sentiment_2026-06-17.json`, `data/upcoming_events_2026-06-17.json`, `data/events_2026-06-17.json`, `data/geo_risk_2026-06-17.json`, `data/quality_gate_2026-06-17.json`, et fichiers JSON agents.*

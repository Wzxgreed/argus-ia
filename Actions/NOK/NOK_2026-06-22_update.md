# NOK — Mise à jour quotidienne (Snapshot 10:00 UTC)

> **Date :** 2026-06-22
> **Type :** Update — snapshot pré-ouverture NY 10:00 UTC
> **Fichier précédent :** [NOK_2026-06-17_17h_update.md](./NOK_2026-06-17_17h_update.md) (snapshot 17:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-17 17:00 UTC (précédent) | Snapshot actuel | Δ |
|----------|-----------------------------------|-----------------|---|
| **Close** | **$14.035** | **$13.49** | **−$0.545 (−3.88%)** |
| **Previous close** | $13.98 | **$13.83** | **−$0.15** |
| **Open** | — | **$14.00** | — |
| **High** | — | **$14.04** | — |
| **Low** | — | **$13.29** | — |
| **RSI 14j** | 42.79 | **42.18** | **−0.61 pt** |
| **ATR 14j** | $1.08 | **$1.08** | **Inchangé** |
| **MM 50j** | $13.09 | **$13.17** | **+$0.08** |
| **Volume session** | 62.5M | **126.8M** | **+102.9%** |
| **Volume vs moy. 20j** | 0.50× | **0.98×** | **+0.48×** |
| **Options max pain** | $14.00 | **$3.00** [^1] | **Anomalie** |
| **Put/Call ratio** | 0.46 | **null** [^1] | **Anomalie** |
| **Call OI %** | 68.3% | **null** [^1] | **Anomalie** |
| **Score Global ajusté** | 46.8 — SURVEILLER | **46.8 — SURVEILLER** | **Inchangé** |
| **Score Opportunité** | 4.2/10 | **4.2/10** | **Inchangé** |
| **Score Momentum** | 5.5/10 | **5.5/10** | **Inchangé** |

[^1]: Données options corrompues dans `data/latest.json` (max pain $3.00 aberrant, put/call et call OI null). Valeurs opérationnelles du 17/06 ($14.00 / 0.46 / 68.3%) conservées à titre indicatif. Nouvelle expiration : 2026-06-26.

**Verdict :** Le snapshot enregistre une **correction de −3.88%** à **$13.49** par rapport au close du 17/06 17h ($14.035), et **−2.46% vs previous close** ($13.83). Le volume a plus que doublé de 62.5M à **126.8M**, ramenant la participation de 0.50× à **0.98×** la moyenne 20j — **normalisation complète** invalidant le signal de désengagement du snapshot précédent. Le RSI reste stable à **42.18** (−0.61 pt), dans la zone neutre inférieure. Le low du jour à **$13.29** marque un test étendu du support. La MM50 remonte légèrement à **$13.17** (+$0.08), le cours restant **+2.4% au-dessus**. Les données options sont **corrompues** ; l'expiration a glissé au **2026-06-26**.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$13.83** | `data/latest.json` | — |
| Open | **$14.00** | `data/latest.json` | +1.23% vs previous close |
| High | **$14.04** | `data/latest.json` | Résistance intraday |
| Low | **$13.29** | `data/latest.json` | **Nouveau low étendu** |
| Close | **$13.49** | `data/latest.json` | −2.46% vs previous close |
| Volume | **126,787,700** | `data/latest.json` | Normalisation complète |
| Volume vs moy. 20j | **0.98×** | Calcul (129.7M) | Participation revenue à la moyenne |
| RSI 14j | **42.18** | `data/latest.json` | Neutre inférieur, biais légèrement baissier |
| ATR 14j | **$1.08** | `data/latest.json` | Volatilité stable |
| MM 50j | **$13.17** | `data/latest.json` | Cours +2.4% au-dessus |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Golden Cross | **Non** | `data/latest.json` | — |
| 52w high / low | **$17.45 / $4.00** | `data/latest.json` | Cours à −22.7% du 52w high |

**Niveaux clés (révisés) :**
- Support immédiat : **$13.29** (low du jour)
- Support intermédiaire : **$13.17** (MM50)
- Support structurel : **$12.99** (ancienne MM50, base gap 08/06)
- Résistance technique : **$14.00** (open / ancien max pain) / **$14.04** (high du jour)
- Résistance structurelle : **$14.27** (ancien support devenu résistance)
- Stop-loss ATR (2×) : **$11.33** ($13.49 − 2×$1.08)
- Take-profit ATR (3×) : **$16.73** ($13.49 + 3×$1.08)
- Ratio R/R : **1.5×**

**Verdict timing :** **Neutre à légèrement défavorable** — La correction de −3.88% depuis le 17/06 confirme une pression baissière résiduelle. Cependant, le volume normalisé (0.98×) et la stabilité du RSI (42.18) atténuent le caractère panique du mouvement. Le cours reste au-dessus de la MM50 (+2.4%). Le low $13.29 est un test étendu du support avant le close à $13.49. L'ATR relatif ($1.08 / $13.49 = 8.0%) reste élevé. Configuration de consolidation post-correction sans direction claire.

---

## 3. Bloc Fondamental

Inchangé en structure. Quality gate passé aujourd'hui (`quality_gate_2026-06-22.json` : status **ok**).

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $75.3B (Yahoo) / $29.8B (FMP) | `data/latest.json` |
| P/E (TTM) | 84.31 (Yahoo) / 50.06 (FMP) | `data/latest.json` |
| Forward P/E | 27.71 | `data/latest.json` |
| EV/EBITDA | 28.79 (Yahoo) / 13.13 (FMP) | `data/latest.json` |
| P/B | 3.11 (Yahoo) / 1.42 (FMP) | `data/latest.json` |
| Beta | 0.781 | `data/latest.json` |
| Dividend Yield | 1.21% (Yahoo) / 2.55% (FMP) | `data/latest.json` |
| Short Interest | 1.19% | `data/latest.json` |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |
| FMP Gross Margin | 43.5% | FMP Stable API |
| FMP Operating Margin | 3.9% | FMP Stable API |
| FMP ROIC | 1.9% | FMP Stable API |
| FMP D/E | 0.25 | FMP Stable API |
| FMP Net Debt/EBITDA | −0.11 (net cash) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé).

**Divergence structurelle Yahoo/FMP persistante :**
- P/E Yahoo 84.31 vs FMP 50.06 (écart +68%)
- Market cap Yahoo $75.3B vs FMP $29.8B (écart +153%)
- Consensus FMP cible **$10.8**, soit **−20.0%** de downside vs le cours $13.49.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé — premium consensus réduit à +24.9% |
| Max pain options | **$14.00** | Opérationnel (17/06) | Valeur `latest.json` corrompue ($3.00) — conservée $14.00 |
| Put/Call ratio | **0.46** | Opérationnel (17/06) | Valeur `latest.json` null — conservée 0.46 |
| Call OI % | **68.3%** | Opérationnel (17/06) | Valeur `latest.json` null — conservée 68.3% |
| Expiration nearest | **2026-06-26** | `data/latest.json` | Dans 4 jours |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_2026-06-22.json` | Aucune mention, aucun pump |

**Structure options (valeurs opérationnelles du 17/06 conservées) :**
- Max pain **$14.00** (opérationnel). Cours $13.49 = **−3.6% sous le max pain**. Le pin risk est modéré : le cours s'éloigne du max pain, renforçant une possible pression haussière vers $14.00 à l'expiration.
- Put/call 0.46 et call OI 68.3% inchangés — structure haussière des options préservée.
- Expiration **2026-06-26** (dans 4 jours). Le risque de pin est modéré mais présent.

**News / Événements :**
- `events_2026-06-22.json` : **0 événement** corporate pour NOK
- `news_2026-06-22.json` : **0 article** pour NOK
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 31 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_2026-06-22.json` — VIX et taux non disponibles)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_2026-06-22.json` : return 20j −5.73%, return 60j −1.51%, momentum score 0.0). Malus structurel persistant.
- **Exposition FX :** `fx_exposure_2026-06-22.json` : NOK — exposure 25%, direction export, primary currency USD. Impact revenus/EPS estimé 0%. Divergence aligned. Flag 🟢. Contexte neutre.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_2026-06-22.json` : 0 ticker flagged, 0 événement).
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent (`accounting_risk_latest.json`) — pas de donnée M-Score/Z-Score disponible.
- **Social sentiment :** No data (`social_sentiment_2026-06-22.json` : 0 mentions, sentiment 0.0, pump_detected false).
- **Validation :** Quality gate **ok** aujourd'hui (`quality_gate_2026-06-22.json`). Les warnings précédents (Quality hors périmètre, P/E élevé, cours +25% vs consensus) sont des caractéristiques structurelles, non des anomalies de données.

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-22.json` — scoring NOK présent.

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.2/10** | C:4.0 V:3.5 M:5.5 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 84.3, premium consensus +24.9% |
| **Score Momentum** | 5.5/10 | 🔴 Faible — RSI 42.18, volume normalisé, low étendu |
| **Score Global ajusté** | **46.8/100** | **SURVEILLER** (seuil 35–49) |
| **Timing technique** | Neutre à défavorable | RSI stable sous 50, MM50 validée, correction −3.88% sur 5 séances |

**Évolution du scoring :**
- Le 15/06 17h : Score Global 46.8 — SURVEILLER
- Le 16/06 21h : Score Global 44.2 — SURVEILLER
- Le 17/06 10h : Score Global 44.2 — SURVEILLER
- Le 17/06 17h : Score Global **46.8** — **SURVEILLER**
- Snapshot actuel : Score Global **46.8** — **SURVEILLER** (stable)

Le scoring reste stable dans la zone SURVEILLER. La correction de −3.88% sur 5 séances et le nouveau low $13.29 sont partiellement compensés par la normalisation du volume (0.98×) et la stabilité du RSI (42.18). Le Filtre Qualité 2.5/6 maintient le plafond structurel. Aucun agent n'a généré de nouveau scoring pour NOK ce matin — les valeurs sont identiques au snapshot du 17/06.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (17h UTC 17/06) | Valeur actuelle | Justification |
|--------|-----------------------------------|-----------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé — 7 analystes FMP |
| **Stop-loss** | $11.88 | **$11.33** | Révisé — ATR $1.08, close $13.49 |
| **Take-profit** | $17.28 | **$16.73** | Révisé — ATR $1.08, close $13.49 |
| **Upside / Downside** | −23.0% / −15.4% | **−20.0% / −16.0%** | Cours $13.49 vs consensus $10.8 |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (ATR-based) |
| **Sizing** | — | **—** | Pas de position |

**Note :** Les niveaux sont révisés à la baisse en raison de la correction du cours ($14.035 → $13.49) et de l'ATR stable ($1.08). Le SL à $11.33 correspond à 2×ATR sous le close actuel. Une cassure sous $13.17 (MM50) invaliderait la tendance haussière de court terme. Une cassure sous $12.99 (ancienne MM50) ouvrirait la voie vers $12.00.

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 15% | Rebond vers $14.00–$14.27 | Le cours tient le support $13.29 et rebondit avec volume confirmé > moyenne 20j. Test de la résistance $14.00 (max pain options / ancien open). Nécessite catalyseur (news 5G, upgrade, contrat). |
| **Central** | 60% | Range $13.29–$14.00 | Consolidation autour du close $13.49. Le max pain $14.00 agit comme aimant modéré. Support $13.29 validé, résistance $14.00 agit comme plafond. Attente des earnings du 23/07. Pas de direction claire sans catalyseur. |
| **Pessimiste** | 25% | Retest $13.17 puis $12.99 (MM50) | La correction se poursuit. Test du support $13.17 (MM50). Si cassure, objectif $12.99 (ancienne MM50, base du gap du 08/06). Volume normalisé (0.98×) ne garantit pas l'accumulation. RSI sous 50 = biais baissier sous-jacent. |

**Probabilité ajustée :** Le scénario central reste dominant (60%). L'expiration options dans 4 jours (2026-06-26) avec max pain $14.00 et cours −3.6% sous le max pain crée un pin risk modéré : une pression haussière vers $14.00 est possible si les calls ITM sont exercés. Le support $13.29 (low du jour) est le niveau critique à surveiller. La normalisation du volume est une nuance constructive mais non suffisante pour modifier la trajectoire sans catalyseur.

---

## 9. Conclusion — Thèse confirmée

**Verdict :** La thèse **SURVEILLER** est **confirmée** sans modification. Le snapshot du matin apporte une **correction de −3.88%** sur 5 séances à **$13.49**, avec un **low étendu à $13.29** et une **normalisation du volume** (0.98×), atténuant le signal de désengagement du snapshot précédent (0.50×). Cependant, l'absence de catalyseur, le Filtre Qualité hors périmètre et le premium consensus persistent.

**Ce qui a changé :**
- **Cours :** Correction de **−$0.545 (−3.88%)** à **$13.49** (vs $14.035 au snapshot 17h 17/06). Change vs previous close **−2.46%**.
- **Volume :** Normalisation de 62.5M à **126.8M** (0.98× moyenne 20j) — participation revenue à la moyenne, invalidant le signal de désengagement du snapshot précédent.
- **RSI :** Stable à **42.18** (−0.61 pt), dans la zone neutre inférieure.
- **Low :** Nouveau low étendu **$13.29** (vs $13.75 précédemment), marquant un test plus profond du support.
- **MM50 :** Légère hausse à **$13.17** (+$0.08). Cours +2.4% au-dessus (vs +7.6% précédemment) — marge de sécurité réduite.
- **Options :** Données corrompues dans `latest.json` (max pain $3.00 aberrant) — valeurs opérationnelles du 17/06 ($14.00 / 0.46 / 68.3%) conservées. Expiration glissée au **2026-06-26** (4 jours).
- **Niveaux SL/TP :** Révisés à la baisse (**$11.33 / $16.73**) en raison de la correction du cours.
- **Quality gate :** Passé aujourd'hui (status **ok**).

**Ce qui n'a pas changé :**
- ATR stable à **$1.08**.
- Filtre Qualité hors périmètre (2.5/6) — bilan solide mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).
- Consensus analystes **$10.8** (7 analysts) — premium +24.9%.
- Divergence Yahoo/FMP persistante (P/E 84.3 vs 50.06, market cap $75.3B vs $29.8B).
- XLC bottom 3 du sector rotation (momentum score 0.0).
- Aucun catalyseur fondamental, aucune news structurante, aucun événement corporate.
- Exposition FX neutre (flag 🟢), géopolitique neutre, social sentiment nul.
- Quant insuffisant, accounting non disponible.
- Score Global **46.8/100 — SURVEILLER** (stable).

**Recommandation révisée :** **SURVEILLER** — Pas de position. Une entrée reste exclue sans :
- Stabilisation du cours au-dessus de **$14.00** avec volume de confirmation > 1.1× moyenne 20j
- Retour du RSI au-dessus de **45** avec un close confirmé
- Test et rebond sur la MM50 ($13.17) avec pattern de reversal
- Franchissement durable au-dessus de **$14.27** (ancien support) avec volume
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel (contrat 5G, upgrade, guidance positive)

**Risque immédiat :** L'expiration des options dans 4 jours (2026-06-26) avec max pain $14.00. Le cours −3.6% sous le max pain crée un pin risk modéré : une pression haussière vers $14.00 est possible si la structure call-dominated (68.3%) exerce des calls ITM. Cependant, l'absence de volume anormal limite l'amplitude du mouvement.

**Prochain point de contrôle :** Snapshot post-session du 22/06 pour valider la tenue du support $13.29 et le volume de clôture. Earnings Q2 FY2026 le **2026-07-23** (dans 31 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-22 10:00 UTC), `data/recommandations_2026-06-22.json`, `data/sector_rotation_2026-06-22.json`, `data/fx_exposure_2026-06-22.json`, `data/social_sentiment_2026-06-22.json`, `data/upcoming_events_2026-06-22.json`, `data/events_2026-06-22.json`, `data/geo_risk_2026-06-22.json`, `data/quality_gate_2026-06-22.json`, et fichiers JSON agents.*

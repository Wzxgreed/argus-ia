# NOK — Mise à jour quotidienne (Snapshot 10:00 UTC)

> **Date :** 2026-06-16
> **Type :** Update — snapshot pré-ouverture NY 10:00 UTC
> **Fichier précédent :** [NOK_2026-06-15_21h_update.md](./NOK_2026-06-15_21h_update.md) (snapshot 21:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-15 21:00 UTC | 2026-06-16 10:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Close** | **$14.82** | **$14.82** | $0.00 (0.00%) |
| **Open** | $14.855 | **$14.86** | +$0.005 (+0.03%) |
| **High** | $14.92 | **$14.92** | Inchangé |
| **Low** | $14.27 | **$14.27** | Inchangé |
| **Previous close** | $14.80 | **$14.80** | Inchangé |
| **RSI 14j** | 40.81 | **40.81** | 0.00 pts |
| **ATR 14j** | $1.08 | **$1.08** | Inchangé |
| **MM 50j** | $12.89 | **$12.89** | Inchangé |
| **Volume session** | 121,846,864 | **130,650,800** | +8.8M (+7.2%) |
| **Volume vs moy. 20j** | 0.98× | **1.05×** | +0.07× |
| **Options max pain** | $14.00 | **$1.00** [CORROMPU] | — |
| **Put/Call ratio** | 0.46 | **null** [CORROMPU] | — |
| **Call OI %** | 68.6% | **null** [CORROMPU] | — |
| **Score Global ajusté** | 46.8 — SURVEILLER | **46.8 — SURVEILLER** | Inchangé |
| **Score Opportunité** | 4.2/10 | **4.2/10** | Inchangé |
| **Score Momentum** | 5.5/10 | **5.5/10** | Inchangé |

**Verdict :** Le snapshot 10h UTC matérialise une **stabilité parfaite** des données de cours et technique. Le close est strictement inchangé à **$14.82**, le RSI reste à **40.81** et l'ATR à **$1.08**. Le volume de session passe de 121.8M à **130.7M** (+7.2%), ramenant la participation de 0.98× à **1.05×** la moyenne 20j (124.6M). Cette légère augmentation de volume au-dessus de la moyenne n'est pas suffisante pour modifier le Score Momentum (5.5/10). Les données options sont à nouveau **corrompues** dans `latest.json` (max pain $1.00, put/call et call OI null) — les valeurs opérationnelles du 15/06 ($14.00 / 0.46 / 68.6%) sont conservées. Les scores agents et les fondamentaux sont strictement inchangés.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$14.80** | `data/latest.json` | Carry-forward |
| Open | **$14.86** | `data/latest.json` | +0.40% vs previous close |
| High | **$14.92** | `data/latest.json` | Résistance intraday non renouvelée |
| Low | **$14.27** | `data/latest.json` | Support intraday validé |
| Close | **$14.82** | `data/latest.json` | +0.14% vs previous close |
| Volume | **130,650,800** | `data/latest.json` | +7.2% vs snapshot 21h 15/06 |
| Volume vs moy. 20j | **1.05×** | Calcul (124.6M) | Légèrement au-dessus de la moyenne |
| RSI 14j | **40.81** | `data/latest.json` | Zone neutre-baisse, proche survente 40 |
| ATR 14j | **$1.08** | `data/latest.json` | Volatilité stable |
| MM 50j | **$12.89** | `data/latest.json` | Cours +15.0% au-dessus |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Golden Cross | **Non** | `data/latest.json` | — |
| 52w high / low | **$17.45 / $4.00** | `data/latest.json` | Cours à −15.1% du 52w high |

**Niveaux clés (révisés avec données 10h UTC) :**
- Support immédiat : **$14.27** (low du jour)
- Support structurel : **$12.89** (MM50)
- Résistance gap : **$14.92** (high du jour) / **$15.00** (résistance psychologique)
- Stop-loss ATR (2×) : **$12.66** ($14.82 − 2×$1.08)
- Take-profit ATR (3×) : **$18.06** ($14.82 + 3×$1.08)
- Ratio R/R : **1.5×**

**Verdict timing :** **Neutre à légèrement défavorable** — Le cours reste au-dessus de la MM50 (+15.0%), structurellement constructif. Le RSI à 40.81 (sous 50, proche de 40) maintient un biais baissier sous-jacent. Le volume à 1.05× moyenne est une nuance marginalement constructive par rapport au 0.98× d'hier, mais ne constitue pas un signal de momentum haussier significatif. L'ATR relatif ($1.08 / $14.82 = 7.3%) reste élevé mais stable. La configuration est de consolidation sans direction claire.

---

## 3. Bloc Fondamental

Inchangé en structure. [DONNÉES PARTIELLES] sur quality gate.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $82.7B (Yahoo) / $29.8B (FMP) | `data/latest.json` |
| P/E (TTM) | 92.6 (Yahoo) / 45.81 (FMP) | `data/latest.json` |
| Forward P/E | 30.44 | `data/latest.json` |
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

**Divergence structurelle Yahoo/FMP persistante :**
- P/E Yahoo 92.6 vs FMP 45.81 (écart +102%)
- Market cap Yahoo $82.7B vs FMP $29.8B (écart +177%)
- Consensus FMP cible **$10.8**, soit **−27.1%** de downside vs le cours $14.82.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé — premium consensus +37.2% |
| Max pain options | **$1.00** | `data/latest.json` | [CORROMPU] — valeur opérationnelle $14.00 conservée |
| Put/Call ratio | **null** | `data/latest.json` | [CORROMPU] — valeur opérationnelle 0.46 conservée |
| Call OI % | **null** | `data/latest.json` | [CORROMPU] — valeur opérationnelle 68.6% conservée |
| Expiration nearest | **2026-06-18** | `data/latest.json` | Dans 2 jours |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_2026-06-16.json` | Aucune mention, aucun pump |

**Structure options (valeurs opérationnelles du 15/06 conservées) :**
- Max pain **$14.00** (opérationnel). Cours $14.82 = +5.9% au-dessus du max pain. Pin risk modéré persistant.
- Put/call 0.46 (call-biased), call OI 68.6% (call-dominated) — structure haussière des options inchangée.
- Expiration dans 2 jours (2026-06-18). Le risque de pin vers $14.00 reste actif.

**News / Événements :**
- `events_2026-06-16.json` : **0 événement** corporate pour NOK
- `news_2026-06-16.json` : **0 article** pour NOK
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 37 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_2026-06-16.json` — VIX et taux non disponibles)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_2026-06-16.json` : return 20j −3.35%, return 60j −0.52%). Malus structurel persistant.
- **Exposition FX :** 25% revenus hors-USD, impact neutre (`fx_exposure_2026-06-16.json` : fx_impact_score 0.0, flag 🟢). Aucune divergence détectée.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_latest.json` du 2026-05-17 : 0 ticker flaggé)
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent — pas de donnée M-Score/Z-Score disponible.
- **Validation :** [WARNING] sur NOK dans `validation_report.txt` (Quality hors périmètre, P/E élevé, cours +50% vs consensus) — déjà documenté.

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-16.json`

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.2/10** | C:4.0 V:3.5 M:5.5 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 92.6, premium consensus +37.2% |
| **Score Momentum** | 5.5/10 | 🟡 Neutre — cours > MM50 mais RSI 40.81, volume légèrement au-dessus de la moyenne |
| **Score Global ajusté** | **46.8/100** | **SURVEILLER** (seuil 35–49) |
| **Timing technique** | Défavorable | RSI sous 50, MM50 validée, volume marginalement au-dessus de la moyenne |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 08/06 21h : Score Global 51.2 — ATTENDRE
- Le 09/06 21h : Score Global 48.0 — SURVEILLER
- Le 10/06 13h : Score Global 50.5 — ATTENDRE
- Le 15/06 13h : Score Global 51.8 — ATTENDRE
- Le 15/06 21h : Score Global 46.8 — SURVEILLER
- Le 16/06 10h : Score Global **46.8** — **SURVEILLER**

Le scoring est **strictement inchangé** vs le snapshot 21h du 15/06. La légère augmentation du volume à 1.05× moyenne 20j n'a pas été capturée comme un changement de momentum suffisant pour modifier le Score Momentum (5.5/10). Les scores Catalyseur (4.0) et Valorisation (3.5) sont inchangés. Le Filtre Qualité 2.5/6 maintient le plafond structurel.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (15/06 21h) | Valeur actuelle (16/06 10h) | Justification |
|--------|-------------------------------|-----------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé — 7 analystes FMP |
| **Stop-loss** | $12.66 | **$12.66** | Inchangé — ATR $1.08, close $14.82 |
| **Take-profit** | $18.06 | **$18.06** | Inchangé — ATR $1.08, close $14.82 |
| **Upside / Downside** | −27.1% / −14.5% | **−27.1% / −14.5%** | Cours $14.82 vs consensus $10.8 |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (ATR-based) |
| **Sizing** | — | **—** | Pas de position |

**Note :** Les niveaux sont inchangés car l'ATR ($1.08) et le cours de clôture ($14.82) sont strictement identiques au snapshot précédent. Le SL reste protecteur : une cassure sous $12.66 placerait le cours sous la MM50 ($12.89), invalidant la tendance de moyen terme.

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 10% | Rebond vers $15.00 | Le cours tient le support $14.27 et rebondit avec volume confirmé > moyenne. Test de $15.00 puis franchissement vers $15.50. Nécessite catalyseur (news 5G, upgrade, contrat). Le volume à 1.05× est une condition nécessaire mais non suffisante. |
| **Central** | 65% | Range $14.00–$14.90 | Consolidation autour du close $14.82. Le range se resserre avec l'expiration des options le 06-18 (pin risk vers $14.00). Pas de catalyseur = pas de direction claire. Support $14.27 validé, résistance $14.92 agit comme plafond. Attente des earnings du 23/07. |
| **Pessimiste** | 25% | Retest $14.00 puis $12.89 (MM50) | Le gap du matin se dissipe. Retour vers le max pain $14.00 à l'expiration. Si cassure sous $14.00, test de la MM50 $12.89. RSI sous 40 = survente technique mais sans soutien. Volume légèrement au-dessus de la moyenne ne garantit pas la tenue du support. |

**Probabilité ajustée :** Inchangée vs snapshot 21h du 15/06. Le scénario central reste dominant (65%). Le scénario optimiste reste à 10% — l'augmentation marginale du volume ne modifie pas la trajectoire sans catalyseur. Le scénario pessimiste reste à 25% avec le risque de pin vers $14.00 à l'expiration.

---

## 9. Conclusion — Thèse confirmée

**Verdict :** La thèse **SURVEILLER** est **confirmée** sans modification. Les données du snapshot 10h UTC n'apportent aucun changement structurel à la configuration technique ou fondamentale.

**Ce qui a changé :**
- **Volume :** De 121.8M à **130.7M** (+7.2%), ramenant la participation de 0.98× à **1.05×** moyenne 20j (124.6M). Cette augmentation marginale est notée comme constructive mais non significative pour le momentum.
- **Options :** Données **corrompues** dans `latest.json` (max pain $1.00, put/call null, call OI null). Les valeurs opérationnelles du 15/06 ($14.00 / 0.46 / 68.6%) sont conservées pour l'analyse.
- **DRAFT_refresh :** Un fichier `NOK_2026-06-16_DRAFT_refresh.md` a été détecté avec trigger **ATR_SPIKE** (7.29%). Ce trigger est **stale** — l'ATR était déjà à $1.08 (7.29%) au snapshot 21h du 15/06 et a déjà été intégré dans l'analyse précédente. Aucun nouveau spike ATR n'est observé. Le DRAFT est archivé.

**Ce qui n'a pas changé :**
- Cours inchangé à $14.82, RSI 40.81, ATR $1.08, MM50 $12.89.
- Filtre Qualité hors périmètre (2.5/6) — bilan solide mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).
- Consensus analystes $10.8 (7 analysts) — premium +37.2%.
- Divergence Yahoo/FMP persistante (P/E 92.6 vs 45.81, market cap $82.7B vs $29.8B).
- XLC bottom 3 du sector rotation.
- Score Global ajusté **46.8/100** — **SURVEILLER**.
- Aucun catalyseur fondamental, aucune news structurante, aucun événement corporate.
- Exposition FX neutre, géopolitique neutre, social sentiment nul.
- Quant insuffisant, accounting non disponible.

**Recommandation révisée :** **SURVEILLER** — Pas de position. Une entrée reste exclue sans :
- Volume de confirmation > 1.2× moyenne 20j sur un test du support $14.27
- Stabilisation du RSI au-dessus de 45 avec un close confirmé
- Test et rebond sur la MM50 avec pattern de reversal
- Franchissement durable au-dessus de $14.92 (high du jour) avec volume
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel (contrat 5G, upgrade, guidance positive)

**Risque immédiat :** L'expiration des options le 2026-06-18 (dans 2 jours) avec max pain opérationnel $14.00. Le cours à +5.9% au-dessus du max pain expose à un risque de pin baissier vers $14.00 si la structure call-dominated se désassemble. La volatilité relative (ATR 7.3%) reste élevée et peut générer des faux signaux intraday.

**Prochain point de contrôle :** Snapshot du 16/06 post-session pour valider la tenue du support $14.27 et le volume de clôture. Earnings Q2 FY2026 le **2026-07-23** (dans 37 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-16 10:00 UTC), `data/recommandations_2026-06-16.json`, `data/sector_rotation_2026-06-16.json`, `data/fx_exposure_2026-06-16.json`, `data/social_sentiment_2026-06-16.json`, `data/upcoming_events_2026-06-16.json`, `data/events_2026-06-16.json`, et fichiers JSON agents.*

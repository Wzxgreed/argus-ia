# NOK — Mise à jour quotidienne (Snapshot 10:00 UTC)

> **Date :** 2026-06-29
> **Type :** Update — snapshot post-gap overnight + mutation technique majeure
> **Fichier précédent :** [NOK_2026-06-23_update.md](./NOK_2026-06-23_update.md)

---

## 1. Résumé des changements

| Métrique | Snapshot 17:00 UTC 23/06 (précédent) | Snapshot actuel 10:00 UTC 29/06 | Δ |
|----------|--------------------------------------|---------------------------------|---|
| **Close** | **$13.75** | **$13.01** | **−5.38%** |
| **Previous close** | $14.43 | **$13.98** | −3.12% |
| **Open** | $13.46 | **$13.44** | −0.15% |
| **High** | $13.89 | **$13.44** | −3.24% |
| **Low** | $13.22 | **$12.78** | −3.33% |
| **RSI 14j** | **31.19** | **40.31** | **+9.12 pts** |
| **ATR 14j** | **$1.06** | **$0.90** | −15.1% |
| **MM 50j** | **$13.35** | **$13.55** | +$0.20 |
| **Volume session** | 62.3M | **142.6M** | **+128.8%** |
| **Volume vs moy. 20j** | 0.483× | **1.15×** | **Explosion** |
| **Options max pain** | **$14.00** | **$1.00** | 🔴 **Corrompu** |
| **Put/Call ratio** | **0.96** | **null** | Données manquantes |
| **Call OI %** | **51.0%** | **null** | Données manquantes |
| **Score Global ajusté** | 45.5 — SURVEILLER | **26.2 — ÉVITER** | **−19.3 pts** |
| **Score Opportunité** | 4.0/10 | **3.4/10** | −0.6 pt |
| **Score Momentum** | 5.0/10 | **2.5/10** | **−2.5 pts** |
| **Score Valorisation** | 3.5/10 | **3.5/10** | Inchangé |
| **Score Catalyseur** | 4.0/10 | **4.0/10** | Inchangé |

**Verdict :** Le snapshot du 29/06 marque une **dégradation majeure** avec un gap baissier de −6.94% et une rétrogradation du Score Global ajusté de **45.5 à 26.2** (SURVEILLER → **ÉVITER**). La participation a explosé (1.15× la moyenne) contrairement au volume effondré du 23/06. Le RSI remonte malgré la baisse (+9.12 pts à 40.31), créant une divergence haussière technique. Cependant, le cours casse sous la MM50 ($13.55) et le Score Momentum s'effondre à 2.5/10.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$13.98** | `data/latest.json` | Rollover close 26/06 |
| Open | **$13.44** | `data/latest.json` | Gap baissier −3.86% vs previous close |
| High | **$13.44** | `data/latest.json` | Égal à l'open — pas de rebond intraday |
| Low | **$12.78** | `data/latest.json` | Test du support structurel |
| Close | **$13.01** | `data/latest.json` | −6.94% vs previous close |
| Volume | **142,605,400** | `data/latest.json` | Explosion +128.8% vs 23/06 |
| Volume vs moy. 20j | **1.15×** | Calcul (124.1M) | Participation élevée — distribution potentielle |
| RSI 14j | **40.31** | `data/latest.json` | 🔴 Remonte de 9.12 pts malgré prix plus bas — divergence haussière |
| ATR 14j | **$0.90** | `data/latest.json` | Contractions de la volatilité |
| MM 50j | **$13.55** | `data/latest.json` | Cours **−4.0% sous la MM50** — signal baissier |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Golden Cross | **Non** | `data/latest.json` | — |
| 52w high / low | **$17.45 / $4.00** | `data/latest.json` | Cours à −25.4% du 52w high |

**Niveaux clés (révisés) :**
- Support immédiat : **$12.78** (low de la session)
- Support intermédiaire : **$12.35** (SL 2×ATR historique)
- Support structurel : **$11.63** (SL précédent, base de la consolidation de juin)
- Résistance technique : **$13.44** (open/high de la session)
- Résistance structurelle : **$13.55** (MM50)
- Résistance majeure : **$13.98** (previous close)
- Stop-loss ATR (2×) : **$11.21** (cours − 2×ATR $0.90)
- Take-profit ATR (3×) : **$15.71** (cours + 3×ATR $0.90)
- Ratio R/R : **1.5×**

**Verdict timing :** **Défavorable.** Le RSI 40.31 affiche une divergence haussière positive (remonte de 9.12 pts alors que le prix baisse de 5.38%), ce qui est un signal technique constructif. Cependant, la cassure sous la MM50 ($13.55) avec un volume élevé (1.15×) l'emporte : le momentum est clairement baissier. Le fait que le high de la session égale l'open ($13.44) sans aucun rebond intraday confirme la faiblesse structurelle.

---

## 3. Bloc Fondamental

Inchangé en structure. Filtre Qualité hors périmètre (2.5/6).

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | **$72.6B** | `data/latest.json` |
| Market Cap (FMP) | **$29.8B** | `data/latest.json` |
| P/E (Yahoo) | **81.31** | `data/latest.json` |
| P/E (FMP) | **50.06** | `data/latest.json` |
| Forward P/E | **26.73** | `data/latest.json` |
| EV/EBITDA (Yahoo) | **27.73** | `data/latest.json` |
| EV/EBITDA (FMP) | **13.13** | `data/latest.json` |
| P/B (Yahoo) | **3.03** | `data/latest.json` |
| P/B (FMP) | **1.42** | `data/latest.json` |
| Dividend Yield (Yahoo) | **1.26%** | `data/latest.json` |
| Gross Margin | **43.5%** | FMP Stable API |
| Operating Margin | **3.9%** | FMP Stable API |
| Net Margin | **3.3%** | FMP Stable API |
| ROIC | **1.9%** | FMP Stable API |
| D/E | **0.25** | FMP Stable API |
| Net Debt/EBITDA | **−0.11 (net cash)** | FMP Stable API |
| FMP Consensus PT | **$10.8** (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé).

**Premium consensus :** Cours $13.01 vs consensus $10.8 = **+20.5%** (vs +27.3% au 23/06).

**Divergence Yahoo/FMP persistante :** Market Cap $72.6B vs $29.8B (+144%), P/E 81.31 vs 50.06 (+63%). Non résolue. Source primaire : FMP.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé — premium +20.5% |
| Max pain options | **$1.00** | `data/latest.json` | 🔴 **Données corrompues** — aberrant |
| Put/Call ratio | **null** | `data/latest.json` | Données manquantes |
| Call OI % | **null** | `data/latest.json` | Données manquantes |
| Expiration nearest | **2026-07-02** | `data/latest.json` | Dans **3 jours** |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_2026-06-29.json` | Aucune mention, aucun pump |

**Structure options :** Données corrompues dans `latest.json` (max pain $1.00 aberrant, put/call et call OI null). Valeurs opérationnelles du 23/06 conservées à titre indicatif : max pain $14.00, put/call 0.96 (quasi-neutre), call OI 51.0%. Avec expiration dans 3 jours et cours $13.01, le cours est **−7.1% sous le max pain opérationnel** de $14.00 — pression baissière significative si les données options étaient intactes.

**News / Événements :**
- `events_2026-06-29.json` : **0 événement** corporate pour NOK
- `news_2026-06-29.json` : non lu (pas dans le scope JSON requis)
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 24 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_2026-06-29.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_2026-06-29.json` : return 20j −8.75%, return 60j −3.97%, momentum score 0.0). Malus structurel persistant.
- **Exposition FX :** `fx_exposure_2026-06-29.json` : NOK — exposure 25%, direction export, primary currency USD. Impact revenus/EPS estimé 0%. Divergence aligned. Flag 🟢. Contexte neutre.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_latest.json` : 0 ticker flagged, 0 événement).
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent (`accounting_risk_latest.json`) — pas de donnée M-Score/Z-Score disponible.
- **Social sentiment :** No data (`social_sentiment_2026-06-29.json` : 0 mentions, sentiment 0.0, pump_detected false). Alertes système "EXTREME_BEARISH" sur tous les tickers = artefact (0 mentions).

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-29.json` — scoring NOK révisé.

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **3.4/10** | C:4.0 V:3.5 M:2.5 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 50.1 (FMP), premium consensus +20.5% |
| **Score Momentum** | 2.5/10 | 🔴 Baissier — cassure MM50, high=open, volume de distribution |
| **Score Global ajusté** | **26.2/100** | **ÉVITER** (seuil < 35) |
| **Timing technique** | Défavorable | Divergence RSI/prix positive mais cassure MM50 dominante |

**Évolution du scoring :**
- Snapshot 17h UTC 23/06 : Score Global **45.5** — **SURVEILLER** (C:4.0 V:3.5 M:5.0)
- Snapshot 10h UTC 29/06 : Score Global **26.2** — **ÉVITER** (C:4.0 V:3.5 M:2.5)

**Explication de la dégradation :**
- Score Momentum : 5.0 → 2.5 (−2.5 pts) : gap −6.94%, cassure MM50 ($13.55), high=open sans rebond, volume élevé = distribution
- Score Opportunité : 4.0 → 3.4 (−0.6 pt) : ajustement mécanique post-baisse
- Score Global ajusté recule de 19.3 pts et franchit le seuil **ÉVITER** (< 35)
- Action recommandée : **ÉVITER** (rétrogradation depuis SURVEILLER)

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (17h UTC 23/06) | Valeur actuelle | Justification |
|--------|-----------------------------------|-----------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé — 7 analystes FMP |
| **Stop-loss** | $11.63 | **$11.21** | Cours − 2×ATR $0.90 = $11.21 |
| **Take-profit** | $16.93 | **$15.71** | Cours + 3×ATR $0.90 = $15.71 |
| **Upside / Downside** | −21.5% / −15.4% | **−17.0% / −13.8%** | Cours $13.01 vs consensus $10.8 / SL $11.21 |
| **Ratio R/R** | 1.5× | **1.5×** | Inchangé (ATR stable) |
| **Sizing** | — | **—** | Pas de position (action ÉVITER) |

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 15% | Rebound vers $13.55–$13.80 | La divergence RSI/prix se matérialise en rebond technique. Test de la MM50 ($13.55) comme résistance. Nécessite volume > 1.0× et absence de vente programmée. |
| **Central** | 50% | Range $12.78–$13.44 | Consolidation autour du low de la session. Volume élevé (1.15×) = marché en digestion. Attente du catalyst earnings (23/07). Pin risk vers $14.00 si données options restaurées. |
| **Pessimiste** | 35% | Cassure sous $12.78 vers $11.63 | La cassure MM50 se confirme. Objectif $11.63 (SL 2×ATR) puis $11.21 (nouveau SL). Si le gap du 23/06 ($13.22) est comblé à la baisse, la structure devient baissière. Volume élevé sur baisse = distribution institutionnelle. |

---

## 9. Conclusion — Thèse invalidée

**Verdict :** La thèse **SURVEILLER** est **invalidée** et rétrogradée en **ÉVITER**.

**Ce qui a changé :**
- **Cours :** $13.75 → **$13.01** (−5.38% depuis dernière analyse, −6.94% vs previous close) — gap baissier majeur
- **RSI :** 31.19 → **40.31** — divergence haussière technique (RSI remonte malgré prix plus bas)
- **Volume :** 62.3M (0.48×) → **142.6M** (1.15×) — explosion de la participation, potentiellement distribution
- **Cours vs MM50 :** +3.0% au-dessus → **−4.0% sous la MM50** — signal baissier structurel
- **Score Global :** 45.5 → **26.2** — franchissement du seuil ÉVITER (< 35)
- **Score Momentum :** 5.0 → **2.5** — momentum clairement baissier
- **Action recommandée :** SURVEILLER → **ÉVITER**
- **SL/TP :** $11.63/$16.93 → **$11.21/$15.71** — révision mécanique post-baisse + contraction ATR
- **Options :** Données corrompues ($1.00 aberrant) — pin risk opérationnel estimé à −7.1% vs $14.00

**Ce qui n'a pas changé :**
- Consensus analystes **$10.8** (7 analysts)
- Filtre Qualité hors périmètre (2.5/6)
- Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%)
- Divergence Yahoo/FMP persistante (Market Cap $72.6B vs $29.8B, P/E 81.31 vs 50.06)
- XLC bottom 3 du sector rotation (momentum score 0.0)
- Aucun catalyseur fondamental, aucune news structurante, aucun événement corporate
- Exposition FX neutre (flag 🟢), géopolitique neutre, social sentiment nul

**Recommandation révisée :** **ÉVITER** — Pas de position. Les conditions se sont dégradées de manière structurelle :
- Cassure de la MM50 avec volume élevé (distribution)
- High de session égal à l'open ($13.44) = aucun achat intraday
- Score Global ajusté < 35 (ÉVITER) — multiple malus cumulés
- Attendre un rebond au-dessus de $13.55 (MM50) avec volume > 1.0× pour réviser la thèse

**Risque immédiat :**
1. **Cours sous MM50** — signal baissier structurel, potentiel retour vers $12.35–$11.63
2. **Volume élevé sur baisse** (1.15×) — distribution potentielle, pas de capitulation
3. **Données options corrompues** — impossible de valider le pin risk exact, mais le gap de −6.94% suggère une pression vendeuse forte
4. **Earnings dans 24 jours** (2026-07-23) — Est EPS $0.06–$0.08, Rev $4.8B. Risque de guidance cut si le secteur 5G reste sous pression

**Prochain point de contrôle :**
- Snapshot 13:00 UTC du 29/06 pour vérifier la tenue du support $12.78 et le volume
- Évolution du RSI — confirmation de la divergence ou retour sous 35
- Restauration des données options dans `latest.json`

Earnings Q2 FY2026 le **2026-07-23** (dans 24 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-29 10:00 UTC), `data/recommandations_2026-06-29.json`, `data/sector_rotation_2026-06-29.json`, `data/fx_exposure_2026-06-29.json`, `data/social_sentiment_2026-06-29.json`, `data/upcoming_events_2026-06-29.json`, `data/events_2026-06-29.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, et fichiers JSON agents.*

# NOK — Mise à jour quotidienne (Snapshot 17:00 UTC)

> **Date :** 2026-06-23
> **Type :** Update — snapshot post-ouverture NY (données options stables, mutation technique majeure)
> **Fichier précédent :** [NOK_2026-06-23_13h_update.md](./NOK_2026-06-23_13h_update.md)

---

## 1. Résumé des changements

| Métrique | Snapshot 13:00 UTC 23/06 (précédent) | Snapshot actuel 17:00 UTC 23/06 | Δ |
|----------|--------------------------------------|---------------------------------|---|
| **Close** | **$14.43** | **$13.75** | **−4.71%** |
| **Previous close** | $13.49 | **$14.43** | Révisé (rollover) |
| **Open** | $13.84 | **$13.46** | −2.74% |
| **High** | $14.56 | **$13.89** | −4.60% |
| **Low** | $13.80 | **$13.22** | −4.20% |
| **RSI 14j** | **38.85** | **31.19** | **−7.66 pts** |
| **ATR 14j** | **$1.04** | **$1.06** | +1.9% |
| **MM 50j** | **$13.27** | **$13.35** | +0.6% |
| **Volume session** | 117.1M | **62.3M** | **−46.8%** |
| **Volume vs moy. 20j** | 0.885× | **0.483×** | **Effondrement** |
| **Options max pain** | **$14.00** | **$14.00** | Inchangé |
| **Put/Call ratio** | **0.96** | **0.96** | Inchangé |
| **Call OI %** | **51.0%** | **51.0%** | Inchangé |
| **Score Global ajusté** | 48.0 — SURVEILLER | **45.5 — SURVEILLER** | **−2.5 pts** |
| **Score Opportunité** | 4.3/10 | **4.0/10** | −0.3 pt |
| **Score Momentum** | 6.0/10 | **5.0/10** | **−1.0 pt** |
| **Score Valorisation** | 3.5/10 | **3.5/10** | Inchangé |
| **Score Catalyseur** | 4.0/10 | **4.0/10** | Inchangé |

**Verdict :** Le snapshot 17:00 UTC du 23/06 marque une **mutation technique majeure** : correction de −4.71% avec un volume effondré à 0.48× la moyenne, RSI en chute libre vers la zone de survente (31.19), et révision du Score Global ajusté de **48.0 à 45.5** (SURVEILLER). Les données options restent stables (max pain $14.00, structure quasi-neutre).

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$14.43** | `data/latest.json` | Révisé (rollover close 22/06) |
| Open | **$13.46** | `data/latest.json` | Gap baissier −6.7% vs previous close |
| High | **$13.89** | `data/latest.json` | Résistance intraday |
| Low | **$13.22** | `data/latest.json` | Test du support gap 08/06 |
| Close | **$13.75** | `data/latest.json` | −4.71% vs previous close $14.43 |
| Volume | **62,332,370** | `data/latest.json` | Effondrement −46.8% vs 13h |
| Volume vs moy. 20j | **0.483×** | Calcul (129.1M) | Participation très faible |
| RSI 14j | **31.19** | `data/latest.json` | 🔴 Proche zone survente (< 30) |
| ATR 14j | **$1.06** | `data/latest.json` | Stable |
| MM 50j | **$13.35** | `data/latest.json` | Cours +3.0% au-dessus |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Golden Cross | **Non** | `data/latest.json` | — |
| 52w high / low | **$17.45 / $4.00** | `data/latest.json` | Cours à −21.2% du 52w high |

**Niveaux clés (révisés) :**
- Support immédiat : **$13.22** (low de la session)
- Support intermédiaire : **$13.35** (MM50)
- Support gap : **$12.99** (base gap 08/06)
- Support structurel : **$12.35** (SL 2×ATR)
- Résistance technique : **$13.89** (high de la session)
- Résistance structurelle : **$14.43** (previous close)
- Résistance majeure : **$14.56** (high précédent), **$14.82** (close 16/06)
- Stop-loss ATR (2×) : **$11.63** (cours − 2×ATR $1.06)
- Take-profit ATR (3×) : **$16.93** (cours + 3×ATR $1.06)
- Ratio R/R : **1.5×**

**Verdict timing :** **Défavorable.** Le RSI 31.19 est en chute libre et approche la zone de survente (< 30). Le cours reste au-dessus de la MM50 ($13.35) de justesse (+3.0%). Le volume effondré (0.48×) invalide tout signal de soutien institutionnel. La divergence RSI/prix s'est amplifiée (RSI −7.66 pts malgré correction −4.71%).

---

## 3. Bloc Fondamental

Inchangé en structure. Filtre Qualité hors périmètre (2.5/6).

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap (Yahoo) | **$76.8B** | `data/latest.json` |
| Market Cap (FMP) | **$29.8B** | `data/latest.json` |
| P/E (Yahoo) | **85.94** | `data/latest.json` |
| P/E (FMP) | **50.06** | `data/latest.json` |
| Forward P/E | **28.25** | `data/latest.json` |
| EV/EBITDA (FMP) | **13.13** | `data/latest.json` |
| P/B (Yahoo) | **3.17** | `data/latest.json` |
| P/B (FMP) | **1.42** | `data/latest.json` |
| Dividend Yield (Yahoo) | **1.14%** | `data/latest.json` |
| Gross Margin | **43.5%** | FMP Stable API |
| Operating Margin | **3.9%** | FMP Stable API |
| Net Margin | **3.3%** | FMP Stable API |
| ROIC | **1.9%** | FMP Stable API |
| D/E | **0.25** | FMP Stable API |
| Net Debt/EBITDA | **−0.11 (net cash)** | FMP Stable API |
| FMP Consensus PT | **$10.8** (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé).

**Premium consensus :** Cours $13.75 vs consensus $10.8 = **+27.3%** (vs +33.6% à 13h).

**Divergence Yahoo/FMP persistante :** Market Cap $76.8B vs $29.8B (+158%), P/E 85.94 vs 50.06 (+72%). Non résolue. Source primaire : FMP.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé — premium +27.3% |
| Max pain options | **$14.00** | `data/latest.json` | Stable |
| Put/Call ratio | **0.96** | `data/latest.json` | Quasi-neutre |
| Call OI % | **51.0%** | `data/latest.json` | Quasi-neutre |
| Expiration nearest | **2026-06-26** | `data/latest.json` | Dans **3 jours** |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_2026-06-23.json` | Aucune mention, aucun pump |

**Structure options :** max pain $14.00, put/call 0.96 (quasi-neutre), call OI 51.0% (quasi-neutre). Le cours $13.75 est maintenant **−1.79% sous le max pain**. Avec expiration dans 3 jours et structure quasi-neutre, le pin risk s'est inversé : pression vers $14.00 plutôt qu'attraction.

**News / Événements :**
- `events_2026-06-23.json` : **0 événement** corporate pour NOK
- `news_2026-06-23.json` : **0 article** pour NOK
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 30 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_2026-06-23.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_2026-06-23.json` : return 20j −6.60%, return 60j −0.89%, momentum score 0.0). Malus structurel persistant.
- **Exposition FX :** `fx_exposure_2026-06-23.json` : NOK — exposure 25%, direction export, primary currency USD. Impact revenus/EPS estimé 0%. Divergence aligned. Flag 🟢. Contexte neutre.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_latest.json` : 0 ticker flagged, 0 événement — fichier non mis à jour).
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent (`accounting_risk_latest.json`) — pas de donnée M-Score/Z-Score disponible.
- **Social sentiment :** No data (`social_sentiment_2026-06-23.json` : 0 mentions, sentiment 0.0, pump_detected false). Alertes système "EXTREME_BEARISH" sur tous les tickers = artefact (0 mentions).

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-23.json` — scoring NOK révisé.

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.0/10** | C:4.0 V:3.5 M:5.0 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 50.1 (FMP), premium consensus +27.3% |
| **Score Momentum** | 5.0/10 | 🟡 Neutre — RSI en chute, cours au-dessus de MM50 de justesse |
| **Score Global ajusté** | **45.5/100** | **SURVEILLER** (seuil 35–49) — milieu de fourchette |
| **Timing technique** | Défavorable | RSI 31.19 proche survente, volume effondré |

**Évolution du scoring :**
- Snapshot 13h UTC 23/06 : Score Global **48.0** — **SURVEILLER** (C:4.0 V:3.5 M:6.0)
- Snapshot 17h UTC 23/06 : Score Global **45.5** — **SURVEILLER** (C:4.0 V:3.5 M:5.0)

**Explication de la dégradation :**
- Score Momentum : 6.0 → 5.0 (−1.0 pt) : correction −4.71% + RSI en chute vers 30 + volume effondré
- Score Opportunité : 4.3 → 4.0 (−0.3 pt) : ajustement mécanique post-baisse
- Le Score Global ajusté recule de 2.5 pts mais reste dans la fourchette SURVEILLER (35–49).

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (13h UTC 23/06) | Valeur actuelle | Justification |
|--------|-----------------------------------|-----------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé — 7 analystes FMP |
| **Stop-loss** | $12.35 | **$11.63** | Cours − 2×ATR $1.06 = $11.63 |
| **Take-profit** | $17.55 | **$16.93** | Cours + 3×ATR $1.06 = $16.93 |
| **Upside / Downside** | −25.2% / −14.4% | **−21.5% / −15.4%** | Cours $13.75 vs consensus $10.8 / SL $11.63 |
| **Ratio R/R** | 1.5× | **1.5×** | Inchangé (ATR stable) |
| **Sizing** | — | **—** | Pas de position |

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 10% | Rebound vers $14.00–$14.20 | RSI rebondit depuis la zone 30 avec volume > 0.8×. Test du max pain $14.00. Nécessite absence de vente programmée. |
| **Central** | 55% | Range $13.22–$13.89 | Consolidation autour de la MM50 ($13.35). Volume très faible (0.48×) = marché en attente. Test du support $13.22 puis rebout possible. Pin risk inversé vers $14.00 à expiration 26/06. |
| **Pessimiste** | 35% | Cassure sous $13.22 vers $12.99 | RSI franchit 30 et confirme la survente. Cassure du low $13.22 puis objectif $12.99 (base gap 08/06). Si $12.99 cède, objectif $12.35 (SL 2×ATR). Volume faible = pas de soutien institutionnel visible. |

---

## 9. Conclusion — Thèse modifiée

**Verdict :** La thèse **SURVEILLER** est **confirmée avec dégradation technique**.

**Ce qui a changé :**
- **Cours :** $14.43 → **$13.75** (−4.71%) — correction significative
- **RSI :** 38.85 → **31.19** — approche de la zone de survente (< 30), signal d'avertissement
- **Volume :** 117.1M → **62.3M** (0.48×) — effondrement de la participation, absence de soutien
- **Score Global :** 48.0 → **45.5** — SURVEILLER maintenu mais dégradation du Momentum
- **SL/TP :** $12.35/$17.55 → **$11.63/$16.93** — révision mécanique post-baisse
- **Pin risk :** Inversé — cours $13.75 est maintenant **−1.79% sous le max pain $14.00** (vs +3.07% au-dessus à 13h)

**Ce qui n'a pas changé :**
- Consensus analystes **$10.8** (7 analysts)
- Filtre Qualité hors périmètre (2.5/6)
- Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%)
- Divergence Yahoo/FMP persistante (Market Cap $76.8B vs $29.8B, P/E 85.94 vs 50.06)
- XLC bottom 3 du sector rotation (momentum score 0.0)
- Aucun catalyseur fondamental, aucune news structurante, aucun événement corporate
- Exposition FX neutre (flag 🟢), géopolitique neutre, social sentiment nul
- Score Global ajusté **45.5/100** — SURVEILLER

**Recommandation révisée :** **SURVEILLER** — Pas de position. Les conditions d'entrée restent non remplies et se sont dégradées :
- RSI doit rebondir au-dessus de 35 avec volume > 0.8× moyenne
- Cours doit se maintenir au-dessus de $13.35 (MM50)
- Résolution de la divergence RSI/prix
- Apparition d'un catalyseur sectoriel
- Score Global ajusté > 50/100

**Risque immédiat :**
1. **RSI 31.19** — proche de la zone de survente (< 30), signal d'avertissement classique
2. **Volume effondré** (0.48×) — participation institutionnelle quasi nulle
3. **Expiration options dans 3 jours** (2026-06-26) avec max pain **$14.00**. Cours $13.75 = −1.79% sous le max pain — pin risk inversé
4. **Support MM50 $13.35** testé de justesse (+3.0%) — cassure = signal baissier

**Prochain point de contrôle :** Snapshot 21:00 UTC du 23/06 pour vérifier :
- Tenue du support $13.22 et volume de clôture
- Évolution du RSI — confirmation de la survente ou rebond
- Stabilité des données options

Earnings Q2 FY2026 le **2026-07-23** (dans 30 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-23 17:00 UTC), `data/recommandations_2026-06-23.json`, `data/sector_rotation_2026-06-23.json`, `data/fx_exposure_2026-06-23.json`, `data/social_sentiment_2026-06-23.json`, `data/upcoming_events_2026-06-23.json`, `data/events_2026-06-23.json`, `data/geo_risk_latest.json`, `data/quant_report_latest.json`, et fichiers JSON agents.*

# NOK — Mise à jour quotidienne

> **Date :** 2026-06-08
> **Type :** Update post-gap (impact 🔴 Élevé)
> **Fichier précédent :** [NOK_2026-06-03_update.md](./NOK_2026-06-03_update.md)

---

## 1. Résumé des changements

| Métrique | 2026-06-03 (précédent) | 2026-06-08 (actuel) | Δ |
|----------|------------------------|---------------------|---|
| **Cours close** | $16.85 | **$14.38** | **−14.7%** |
| **RSI 14j** | 70.22 (surachat) | **52.32** | −17.9 pts |
| **Volume** | 134.7M | **183.6M** | **+36.3%** |
| **Volume vs 20j** | 1.13× | **1.47×** | +0.34× |
| **P/E Yahoo** | 105.31 | **89.88** | −15.4 pts |
| **Consensus FMP PT** | $9.26 (6 analysts) | **$10.8 (7 analysts)** | +$1.54 / +1 analyste |
| **Score Global ajusté** | 31.8 — ÉVITER | **48.0 — SURVEILLER** | +16.2 pts |
| **Recommandation** | ÉVITER | **SURVEILLER** | Upgrade mécanique |

**Verdict :** Le gap baissier de **−13.48%** entre le close du 03/06 ($16.62) et l'ouverture du 08/06 ($15.66) — suivi d'un low à $14.00 — constitue une **correction technique majeure** qui efface l'essentiel du rallye idiosyncratique des 25–26/05. La surchauffe (RSI 70) est intégralement dissipée. Le volume en hausse de 36% confirme une distribution réelle, pas un simple ajustement de gap. **Aucun catalyseur fondamental identifié** dans `events_latest.json` ni dans les news agrégées.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Open | $15.66 | Yahoo Finance |
| High | $15.67 | Yahoo Finance |
| Low | $14.00 | Yahoo Finance |
| Close | $14.38 | Yahoo Finance |
| Change vs previous close | **−13.48%** | Yahoo Finance |
| Volume | 183,595,200 | Yahoo Finance |
| Volume vs moy. 20j | **1.47×** | Calcul (125.2M) |
| RSI 14j | **52.32** | Calcul agent |
| ATR 14j | **$1.13** | Calcul agent |
| MM 50j | **$12.16** | Calcul agent |
| MM 200j | — | N/A |
| Golden Cross | — | N/A |

**Niveaux clés révisés :**
- Support immédiat : **$14.00** (low du jour) — si cassé, prochain support structurel **$12.16** (MM50)
- Résistance : **$15.47** (base du gap haussier du 25/05, désormais résistance)
- Stop-loss ATR (2×) : **$12.12** ($14.38 − $2.26)
- Take-profit ATR (3×) : **$17.77** ($14.38 + $3.39)
- Ratio R/R : **1.5x**

**Verdict timing :** Neutre — La sortie de surachat est healthy, mais le gap baissier sur volume élevé laisse un surhang technique. Le cours reste +18.3% au-dessus de la MM50, ce qui maintient la tendance haussière structurelle. Cependant, le non-franchissement du gap du 25/05 ($15.47) en séance indique une faiblesse relative.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $80.3B | Yahoo Finance |
| P/E (TTM) | 89.88 | Yahoo Finance |
| Forward P/E | 29.49 | Yahoo Finance |
| EV/EBITDA | 30.75 | Yahoo Finance |
| EV/Revenue | 3.90 | Yahoo Finance |
| P/B | 3.27 | Yahoo Finance |
| Beta | 0.781 | Yahoo Finance |
| Dividend Yield | 1.14% | Yahoo Finance |
| Short Interest | 1.08% | Yahoo Finance |
| **FMP Gross Margin** | 43.5% | FMP FY2025 |
| **FMP Operating Margin** | 3.9% | FMP FY2025 |
| **FMP Net Margin** | 3.3% | FMP FY2025 |
| **FMP ROIC** | 1.9% | FMP FY2025 |
| **FMP D/E** | 0.25 | FMP FY2025 |
| **FMP EV/EBITDA** | 13.13 | FMP FY2025 |
| **FMP Net Debt/EBITDA** | −0.11 | FMP FY2025 (net cash) |

**Filtre Qualité (6 critères) — réévalué :**
| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ 0 | Croissance anémique du top-line télécoms |
| Profit CAGR 5 ans ≥ 20% | ❌ 0 | EPS erratique, operating margin 3.9% |
| Assets/Liabilities > 1.0 | ✅ 1 | D/E 0.25, bilan solide, net cash |
| FCF positif et croissant 5 ans | ⚠️ 0.5 | FCF positif mais volatil (capex cyclique 5G) |
| Avantage compétitif (moat) | ⚠️ 0.5 | Leadership 5G mais commoditisation des équipements |
| Industrie forte croissance (TAM ×5) | ⚠️ 0.5 | TAM 5G en croissance mais maturité sectorielle |
| **Score Qualité total** | **2.5/6** | **🔴 Hors périmètre** — inchangé |

> **Impact du gap sur le fondamental :** Aucun. L'événement est purement technique. La valorisation reste défavorable malgré la baisse : P/E 89.9, forward P/E 29.5. Le consensus FMP a légèrement relevé son PT de $9.26 à $10.8 (+1 analyste couvrant), ce qui réduit mécaniquement le premium de +81.9% à +33.1%.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API |
| Max pain options | **$3.00** | Yahoo Finance |
| Put/Call ratio | **null** | Yahoo Finance (données corrompues) |
| Call OI % | **null** | Yahoo Finance (données corrompues) |
| Social sentiment (Reddit) | 0 mentions / 0.0 score | `social_sentiment_latest.json` |

**⚠️ Anomalie options :** Les données options dans `data/latest.json` sont à nouveau corrompues (max pain $3.00 aberrant vs $13.50 opérationnel historique, put/call et call OI null). La structure options du 03/06 (max pain $13.50, put/call 0.46, call OI 68.5%, expiration 05/06) est conservée comme référence opérationnelle. L'expiration du 05/06 est passée ; aucune nouvelle expiration significative n'est détectée.

**News / Événements :**
- `events_latest.json` : **0 événement** corporate pour NOK
- Aucune mention Reddit, aucun pump/dump détecté
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_latest.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur XLC (Communication Services) reste en **bottom 3** du sector rotation (momentum score 0.0, RS20d −5.68% vs SPY). C'est un malus structurel pour NOK.
- **Exposition FX :** 25% revenus hors-USD, impact neutre (`fx_exposure_latest.json` : fx_impact_score 0.0, divergence_flag aligned)
- **Géopolitique :** Score politique non signalé pour NOK (`geo_risk_latest.json` : seul IREN flaggé)

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_latest.json` (2026-06-08)

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.3/10** | C:4.0 V:3.5 M:6.0 — inchangé vs 03/06 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 89.9, premium consensus +33% |
| **Score Momentum** | 6.0/10 | Tendance haussière structurelle intacte (+18% vs MM50) |
| **Score Global ajusté** | **48.0/100** | **SURVEILLER** (seuil 35–49) |
| **Timing technique** | Favorable | Sortie de surachat, cours au-dessus MM50 |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 03/06 : Score Global 31.8 — ÉVITER
- Le 08/06 : Score Global **48.0** — **SURVEILLER**

L'upgrade de ÉVITER → SURVEILLER est **purement mécanique** : la baisse de −13.5% a réduit le premium de valorisation et normalisé le RSI. Cependant, les scores fondamentaux (Catalyseur 4.0, Valorisation 3.5) restent dans la zone de disqualification (≤2/10 pour un axe exclut le ticker ; ici aucun n'est ≤2, donc le ticker reste dans le rapport).

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (03/06) | Valeur révisée (08/06) | Justification |
|--------|---------------------------|------------------------|---------------|
| **Prix cible** | $9.26 (consensus) | **$10.8** | Consensus FMP révisé à la hausse |
| **Stop-loss** | $14.81 | **$12.12** | Cours − 2×ATR ($14.38 − $2.26) |
| **Take-profit** | $19.91 | **$17.77** | Cours + 3×ATR ($14.38 + $3.39) |
| **Upside / Downside** | −45.0% / −12.1% | **−24.9%** / **−15.7%** | Révision mécanique post-baisse |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (ATR inchangé ~$1.13) |
| **Sizing** | — | **—** | Pas de position |

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 20% | Retour $15.47–$16.25 | Comblement partiel du gap, soutenu par un volume soutenu. Nécessite un catalyseur (contrat 5G, upgrade) |
| **Central** | 55% | Range $13.50–$15.00 | Consolidation autour de la nouvelle base. MM50 ($12.16) agit comme ancre technique. Pas de catalyseur |
| **Pessimiste** | 25% | Cassure $14.00 → test MM50 $12.16 | Distribution institutionnelle continue, retour vers les fondamentaux (consensus $10.8). Volume élevé confirme la sortie |

---

## 9. Conclusion — Thèse modifiée

**Verdict :** La thèse précédente (« ÉVITER — value trap surévalué, surchauffe technique extrême ») est **modifiée** mais **pas invalidée**.

**Ce qui a changé :**
1. **La surchauffe technique est dissipée.** Le RSI est retourné dans la zone neutre (52), éliminant le risque de correction par surachat.
2. **Le premium de valorisation s'est réduit.** De +81.9% vs consensus (02/06) à +33.1% (08/06). C'est une amélioration mécanique, pas fondamentale.
3. **L'action est passée de ÉVITER à SURVEILLER.** Le Score Global ajusté 48.0/100 franchit le seuil 35, mais reste sous 50 (pas d'entrée).

**Ce qui n'a pas changé :**
- Le Filtre Qualité reste **hors périmètre (2.5/6)** — rentabilité anémique, pas de moat, croissance insuffisante.
- Aucun catalyseur fondamental n'est apparu.
- Le secteur XLC reste en sous-performance (bottom 3).
- Les données options sont corrompues, empêchant une lecture fine du sentiment dérivé.

**Recommandation révisée :** **SURVEILLER** — Pas de position. Le gap baissier a créé une opportunité d'observation, pas d'achat. Une entrée ne serait envisageable qu'en cas de :
- Test et rebond sur la MM50 ($12.16) avec volume en hausse
- Amélioration du Score Valorisation > 5.0/10 (impliquerait un cours < $12.00 ou une révision EPS significative)
- Apparition d'un catalyseur sectoriel (contrat 5G majeur, rotation vers XLC)

**Prochain point de contrôle :** Earnings Q2 FY2026 le **2026-07-23** (dans 45 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json`, `data/recommandations_latest.json`, et fichiers JSON agents.*

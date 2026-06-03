# FLY — Mise à Jour (2026-06-03, snapshot 10h UTC)

> **Type :** `_update.md` — Stabilité totale vs close 02/06, consensus révisé à la hausse, anomalie max pain détectée
> **Référence précédente :** [FLY_2026-06-02_update_21h.md](FLY_2026-06-02_update_21h.md) (snapshot 21:00 UTC 02/06)
> **Données source :** `data/latest.json` (timestamp 2026-06-03T10:00:10.085787+00:00), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Validation data :** FLY status `ok` dans `data/validation_report.txt`. Aucun warning. 24/29 tickers OK.

---

## Résumé — Stabilité totale vs close 02/06, consensus révisé +1.9%, thèse ATTENDRE confirmée (58.0)

Le snapshot 10h UTC du 2026-06-03 reflète la **clôture US du 02/06** avec une **stabilité totale** du cours à **$43.37** (inchangé vs close 21h UTC 02/06). Le marché US n'étant pas encore ouvert, aucun nouveau prix n'est disponible.

Le **consensus analystes FMP a été révisé à la hausse** : **$43.25** (12 analysts) vs **$42.45** (11 analysts) précédemment, soit **+$0.80 (+1.9%)** et l'ajout d'un 12ème analyste de couverture. Le consensus passe désormais à **−0.3% sous le spot** (vs −2.1% hier), signalant un léger réalignement haussier des estimations.

**Anomalie data quality détectée** : le max pain options dans `data/latest.json` est affiché à **$20.00** (vs $41.00 hier), clairement aberrant pour un spot à $43.37. Cette valeur est traitée comme une erreur de fetch et la valeur opérationnelle **$41.00** est conservée.

L'**Agent Recommandation maintient ATTENDRE (58.0)** — scores strictement inchangés. Le volume de session reste à **6.18M (0.64× moy. 20j)**. Le RSI 14j est stable à **54.62**. La MM50 remonte légèrement à **$37.79**.

| Métrique | 2026-06-02 21:00 UTC | 2026-06-03 10:00 UTC | Variation |
|----------|----------------------|----------------------|-----------|
| Cours close | $43.37 | **$43.37** | **Inchangé** |
| Open | $44.03 | **$44.03** | **Inchangé** |
| High intraday | $46.44 | **$46.44** | **Inchangé** |
| Low intraday | $43.03 | **$43.03** | **Inchangé** |
| Change % vs prior close | −1.97% | **−1.97%** | **Inchangé** |
| RSI 14j | 54.62 | **54.62** | **Inchangé** |
| MM 50j | $37.79 | **$37.79** | **Inchangé** |
| ATR 14j | $5.91 | **$5.91** | **Inchangé** |
| Volume session | 6.15M | **6.18M** | **+0.5% (ajustement mécanique)** |
| Volume vs moy. 20j | 0.64x | **0.64x** | **Inchangé** |
| Forward P/E | −36.99 | **−36.99** | **Inchangé** |
| EV/Revenue (Yahoo) | 35.646x | **34.892x** | **−2.1% (mécanique)** |
| P/B (Yahoo) | 6.283 | **6.283** | **Inchangé** |
| Market Cap (Yahoo) | $7.12B | **$7.12B** | **Inchangé** |
| Consensus PT (FMP) | $42.45 (11 analysts) | **$43.25 (12 analysts)** | **+$0.80 (+1.9%) — révision haussière** |
| Écart consensus | −2.1% sous le spot | **−0.3% sous le spot** | **Moins baissier** |
| Short Interest | 9.78% | **9.78%** | **Stable** |
| Options — Max Pain | $41.00 | **$20.00** | **⚠️ ANOMALIE DATA — valeur opérationnelle $41.00 conservée** |
| Options — Put/Call | 0.64 | **null** | **Données manquantes** |
| Options — Call OI % | 61.0% | **null** | **Données manquantes** |
| Score Opportunité (agent) | 5.3/10 | **5.3/10** | **Inchangé** |
| Score Momentum (agent) | 7.0/10 | **7.0/10** | **Inchangé** |
| Score Global Ajusté (agent) | 58.0 | **58.0** | **Inchangé — ATTENDRE confirmé** |
| Action | ATTENDRE | **ATTENDRE** | **Confirmé** |

**Verdict :** Stabilité totale overnight. Seule évolution matérielle : le consensus analystes a été révisé à la hausse (+$0.80, 12ème analyste). Anomalie max pain $20.00 identifiée comme erreur de fetch. **Pas de changement de thèse — ATTENDRE (58.0) confirmé.**

---

## Mise à jour technique — Inchangée, consolidation $41–$46 intacte

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $43.37 | −1.97% vs prior close $44.24, −27.5% vs sommet $60.32 (27/05) |
| Open | $44.03 | Gap down vs prior close $44.24 |
| High | $46.44 | Résistance intraday testée mais rejetée — non dépassée en clôture |
| Low | $43.03 | Support proche du max pain $41.00 |
| RSI 14j | **54.62** | **Neutre** — normalisation complète, loin du surachat |
| MM 50j | $37.79 | Cours supérieur de **+14.8%** — tendance haussière à MT intacte |
| Volume | 6,181,000 | **0.64× moy. 20j** — volume faible, pas de conviction |
| ATR 14j | $5.91 | Volatilité élevée persistante (13.63% rel.) |
| Support 1 | $41.00 (Max Pain opérationnel) | Aimant options stable — support psychologique |
| Support 2 | $43.03 (Low du 02/06) | Support intraday proche |
| Support 3 | $37.79 (MM 50j) | Support structurel majeur |
| Résistance 1 | $46.44 (High du 02/06) | Testé et rejeté — résistance immédiate |
| Résistance 2 | $44.24 (Prior close) | Ancien support devenu résistance |
| Résistance 3 | $46.49 (Close 01/06) | Gap fill objectif |

**Timing verdict :** **Neutre** — Aucun changement technique vs le close 02/06. La consolidation $41–$46 reste le scénario central. Le spot reste à +5.8% au-dessus du max pain opérationnel ($41.00). L'expiration options du 05/06 (J-2) approche — le risque de pin négatif reste quasi nul compte tenu du put/call historique de 0.64 et du call OI dominant (61.0% au dernier snapshot valide).

---

## Mise à jour fondamentale — Consensus révisé à la hausse, fondamentaux inchangés

Données croisées Yahoo / FMP (annual FY 2025) — **strictement inchangés sur le plan opérationnel** :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $7.12B | Stable |
| Market Cap (FMP) | $3.40B | Stable — divergence Yahoo/FMP persistante |
| Forward P/E | **−36.99** | Stable — valorisation incompatible avec un profil sans profit |
| EV/Revenue (Yahoo) | 34.892x | −2.1% vs 35.646x — mécanique (cours inchangé, ajustement Yahoo) |
| EV/Revenue (FMP) | 18.23x | Stable |
| P/B (Yahoo) | 6.283 | Stable |
| P/B (FMP) | 2.855 | Stable |
| Gross Margin (FMP) | 15.56% | Faible, stable |
| Operating Margin (FMP) | −154.25% | Fortement négatif, stable |
| Net Margin (FMP) | −186.63% | Fortement négatif, stable |
| Debt/Equity (FMP) | 0.259 | Levier modéré, stable |
| Current Ratio (FMP) | 4.51 | Liquidité solide, stable |
| Short Interest | 9.78% | Stable — pression vendeuse persistante |
| FMP Consensus PT | **$43.25 (12 analysts)** | **+$0.80 (+1.9%) vs hier, 12ème analyste ajouté** |

**Filtre Qualité** : **2/6** (Hors périmètre) — **strictement inchangé**.

| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans >= 20% | ❌ | Pas de données >20% (FY 2025 Revenue/Share $1.05) |
| Profit CAGR 5 ans >= 20% | ❌ | Marges négatives |
| Assets/Liabilities > 1.0 | ✅ | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | ❌ | FCF yield négatif (−7.0%) |
| Avantage compétitif (moat) | ❌ | Aucun moat structurel identifié |
| Industrie forte croissance (TAM x5) | ❌ | Aerospace & Defense en croissance, mais pas x5 pour ce profil |
| **Score Qualité total** | **2/6** | 🔴 Hors périmètre |

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10. L'Agent Recommandation applique **4.5/10**.

**Note sur le consensus** : La révision à la hausse de $42.45 à $43.25 avec l'ajout d'un 12ème analyste est un signal marginallement positif. Cependant, le consensus reste à −0.3% sous le spot, ce qui n'indique pas un enthousiasme débordant. Le multiple de 12 analystes reste faible pour un ticker de cette capitalisation.

---

## Mise à jour sentiment / options / news — Anomalie max pain, consensus révisé, aucune news

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $43.25 (12 analysts) | FMP Stable API | PT **−0.3% sous le spot** — révision haussière de +$0.80, 12ème analyste. Signal marginalement positif. |
| Max Pain | $20.00 | Yahoo Finance 10:00 UTC | **⚠️ ANOMALIE DATA** — valeur aberrante pour un spot à $43.37. Valeur opérationnelle **$41.00** conservée du snapshot 02/06. |
| Put/Call Ratio | null | Yahoo Finance 10:00 UTC | **Données manquantes** — dernière valeur valide 0.64 (02/06). |
| Call OI % | null | Yahoo Finance 10:00 UTC | **Données manquantes** — dernière valeur valide 61.0% (02/06). |
| Short Interest | 9.78% | Yahoo Finance | Stable — pression vendeuse persistante, pas de setup squeeze. |
| Social Sentiment | 0 mention | `data/social_sentiment_2026-06-03.json` | Pas d'activité retail (alerte EXTREME_BEARISH ignorée — artefact). |
| Event-Driven | Aucun | `data/events_2026-06-03.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (62 jours) | `data/upcoming_events_2026-06-03.json` | Est EPS −$0.47 à −$0.45, Rev $0.1B. |
| News FLY | Aucune | Pas de fichier news | **Aucune news spécifique** — le mouvement reste non expliqué par un catalyst. |

**Score Catalyseur** : **5.0/10** (données agents). L'absence de news et d'événements est compensée par la stabilisation technique et la légère révision du consensus. L'anomalie max pain n'est pas un catalyseur.

---

## Scoring global — Stable : ATTENDRE (58.0)

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 7.0/10 | 25% | 1.75 |
| **Score Opportunité** | **5.3/10** | | |
| **Score Global** | **53.0** | | |
| **Score Global Ajusté** | **58.0** | | |

**Action** : **ATTENDRE**
**Direction** : Neutre
**Timing** : Favorable
**Horizon** : —

**Note sur le scoring :** L'Agent Recommandation maintient FLY en **ATTENDRE (58.0)**. Tous les scores sont strictement inchangés vs le close 02/06. Le Score Opportunité (5.3/10) franchit le seuil 5.0 mais reste fragile. Le Score Valorisation (4.5/10) est plafonné par le Filtre Qualité 2/6.

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant depuis le 2026-05-17) — pas d'ajustement.
- **Agent Geo** : FLY non flaggé (geo_risk absent du rapport 2026-05-17) — pas de malus.
- **Agent Sector Rotation** : XLI sous-performant SPY (RS 20j −3.91%, momentum_score 0.0) — headwind sectoriel persistant (−0.5 pt).
- **Agent Social** : 0 mention — neutre (alerte pipeline EXTREME_BEARISH ignorée car artefact).
- **Agent FX** : Exposition 25%, fx_impact_score 0.0 — pas d'ajustement.
- **Agent Event-Driven** : 0 événement — neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible — pas d'ajustement.

---

## Révision des niveaux SL / TP — Inchangés

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $43.37 | Close 02/06 (snapshot 10h UTC 03/06) | −1.97% vs prior close |
| Stop-loss | $31.55 | Agent Recommandation | Support technique majeur — sous MM50 |
| Take-profit | $61.10 | Agent Recommandation | Ancienne zone de résistance $55–$60 |
| Ratio R/R | 1.5:1 | Agent Recommandation | Standard agent |

Les niveaux sont issus de l'Agent Recommandation. Le SL $31.55 correspond à une zone sous la MM50 ($37.79) et sous le support structurel. Le TP $61.10 reflète un rebond partiel vers la zone $55–$60. Le ratio reste limité pour un profil sans rentabilité.

---

## Conclusion — Thèse défavorable confirmée, consensus légèrement révisé à la hausse — ATTENDRE (58.0)

**Verdict : Thèse défavorable CONFIRMÉE, consensus analystes légèrement révisé à la hausse — ATTENDRE (58.0).**

Le snapshot 10h UTC du 03/06 confirme la **stabilité totale** du cours à **$43.37** vs le close 02/06. L'Agent Recommandation maintient **ATTENDRE (58.0)** avec scores inchangés.

**Ce qui confirme la thèse défavorable :**
- **Aucun catalyst identifié** : aucune news, aucun événement corporate. Le test de $46.44 a été rejeté sans volume.
- **Filtre Qualité 2/6, Forward P/E −36.99, EV/Revenue 34.9x** : fondamentaux inchangés et défavorables.
- **Headwind sectoriel XLI** : sous-performant SPY (RS 20j −3.91%, momentum_score 0.0).
- **Short Interest 9.78%** : stable, pression vendeuse persistante.
- **Volume faible 0.64×** : pas de conviction derrière le test de résistance.
- **Anomalie data options** : max pain $20.00 aberrant dans latest.json — [DONNÉES PARTIELLES].

**Ce qui modifie la thèse (marginalement moins négatif) :**
- **Consensus révisé à la hausse** : $43.25 (+$0.80, +1.9%) avec un 12ème analyste. Le consensus passe de −2.1% à −0.3% sous le spot — léger réalignement haussier.
- **RSI 54.62** : normalisation complète, loin du surachat extrême.
- **Support $43.03 tenu** : pas de test du max pain $41.00, la tendance haussière à MT reste intacte.

**Catalyseurs forward** (inchangés) :
1. **Earnings Q2 2026** (2026-08-04, 62 jours) : Est EPS −$0.45 à −$0.47, Rev $0.1B.
2. **Expiration options 2026-06-05** (2 jours) : max pain opérationnel $41.00 vs spot $43.37 — spot +5.8% au-dessus, risque de pin quasi nul.

**Risques** (inchangés) :
1. Rentabilité non démontrée et non attendue à court terme.
2. Multiple incompatible avec un profil quality compounding.
3. **Résistance $46.44** — testée mais rejetée en clôture, consolidation possible.
4. Short Interest 9.78% : pression vendeuse persistante.
5. Divergence Yahoo/FMP sur Market Cap ($7.12B vs $3.40B) et P/B (6.28 vs 2.86) persistante — [DONNÉES PARTIELLES].
6. Headwind sectoriel XLI persistant.
7. Forward P/E −36.99 : valorisation reste incompatible avec un profil sans profit.
8. **Anomalie data options** : max pain $20.00 aberrant dans latest.json — valeur opérationnelle $41.00 conservée.

**Prochaine étape :**
- **Ne pas prendre de position** — ATTENDRE (58.0).
- **Surveiller l'open US du 03/06** : si le cours tient au-dessus de $41.00, la consolidation se poursuit. Si retour sous $41.00, risque de retest de $39.75.
- **Si cassure de $46.44** (high du 02/06) sur volume > 1.5× moy. 20j → possible signal de retournement court terme.
- **Si cassure de $43.03** (low du 02/06) → risque de retour vers $41.00 (max pain).
- **Si un catalyst fondamental émerge** → réévaluer Score Catalyseur et Filtre Qualité. Sans cela, le mouvement reste spéculatif.

---

*Snapshot 10:00 UTC 03/06 — Cours $43.37 (inchangé vs close 02/06, −27.5% vs 27/05), RSI 54.62 neutre, volume 6.18M (0.64× moy. 20j). Consensus révisé à la hausse $43.25 (12 analysts). Anomalie max pain $20.00 détectée et signalée (valeur opérationnelle $41.00 conservée). Options partiellement corrompues dans latest.json. Aucun catalyst. Fondamentaux inchangés et défavorables. Agent Recommandation : ATTENDRE (58.0). Thèse défavorable confirmée, consensus marginalement moins négatif.*

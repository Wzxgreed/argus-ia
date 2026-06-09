# FLY — Mise à Jour (2026-06-09, snapshot 10h UTC)

> **Type :** `_update.md` — Snapshot pré-marché 10h UTC, stabilité totale vs close officiel 08/06, thèse SURVEILLER (43.8) confirmée
> **Référence précédente :** [FLY_2026-06-08_update.md](FLY_2026-06-08_update.md) (close officiel 21h UTC 08/06)
> **Données source :** `data/latest.json` (timestamp 2026-06-09T10:00:02.122584+00:00), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Validation data :** FLY status `ok` dans `data/validation_report.txt`. Aucun warning. 25/29 tickers OK.

---

## Résumé — Stabilité totale vs close 08/06, thèse SURVEILLER (43.8) confirmée

Le snapshot pré-marché 10h UTC du 2026-06-09 enregistre un cours de **$36.18** (+0.22% vs prior close $36.10), sur un **volume de 4.21M (0.45× moy. 20j)**. Toutes les données techniques, fondamentales et de scoring sont strictement identiques au close officiel 21h UTC du 08/06. L'absence de changement matériel confirme que la séance du 08/06 s'est close sans évolution post-markets.

**Changements majeurs vs close 21h UTC 08/06 :**
- **Cours close** : $36.18 → **$36.18** (inchangé)
- **RSI 14j** : 41.52 → **41.52** (inchangé)
- **ATR 14j** : $5.79 → **$5.79** (inchangé)
- **MM 50j** : $38.81 → **$38.81** (inchangé)
- **Volume session** : 4.19M → **4.21M** (+0.5%, révision marginale)
- **Volume vs moy. 20j** : 0.45x → **0.45x** (inchangé)
- **Score Momentum (agent)** : 3.5/10 → **3.5/10** (inchangé)
- **Score Global Ajusté (agent)** : 43.8 → **43.8** (inchangé)
- **Timing** : Défavorable → **Défavorable** (inchangé)
- **Forward P/E** : −27.78 → **−27.78** (inchangé)
- **Options** : **Anomalie data** — max pain $19.00 aberrant (vs $40.00 opérationnel), put/call et call OI null. Valeurs opérationnelles du 08/06 conservées.
- **Sector Rotation (XLI)** : momentum_score 2.65 → **2.65** (inchangé)

| Métrique | 2026-06-08 21h UTC | 2026-06-09 10h UTC | Variation |
|----------|--------------------|--------------------|-----------|
| Cours close | $36.18 | **$36.18** | Inchangé (+0.22% vs prior) |
| RSI 14j | 41.52 | **41.52** | Inchangé |
| MM 50j | $38.81 | **$38.81** | Inchangé |
| Position vs MM50 | −6.8% | **−6.8%** | Inchangé |
| ATR 14j | $5.79 | **$5.79** | Inchangé |
| Volume session | 4.19M | **4.21M** | +0.5% (révision marginale) |
| Volume vs moy. 20j | 0.45x | **0.45x** | Inchangé |
| Options — Max Pain | $40.00 | **$19.00** | ⚠️ Anomalie data (valeur opérationnelle $40.00 conservée) |
| Options — Put/Call | 1.08 | **null** | ⚠️ Anomalie data (valeur opérationnelle 1.08 conservée) |
| Options — Call OI % | 48.1% | **null** | ⚠️ Anomalie data (valeur opérationnelle 48.1% conservée) |
| Score Opportunité (agent) | 5.2/10 | **5.2/10** | Inchangé |
| Score Momentum (agent) | 3.5/10 | **3.5/10** | Inchangé |
| Score Global Ajusté (agent) | 43.8 | **43.8** | Inchangé |
| Action | SURVEILLER | **SURVEILLER** | Confirmée |
| Timing | Défavorable | **Défavorable** | Confirmé |

**Verdict :** Le snapshot 10h UTC confirme la **stabilité totale** des données. L'Agent Recommandation maintient **SURVEILLER (43.8)**. L'anomalie options détectée dans `latest.json` (max pain $19.00, put/call null) est un artefact data récurrent post-expiration ; les valeurs opérationnelles du 08/06 ($40.00 / 1.08 / 48.1%) restent la référence jusqu'à confirmation.

---

## Mise à jour technique — Stabilité totale, configuration inchangée

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours close | $36.18 | +0.22% vs prior close $36.10, −51.0% vs 52W high $73.80 |
| Open | $37.18 | Gap haussier minime vs prior close |
| High | $38.20 | Résistance intraday inchangée — zone $38.00–$38.20 non conquise |
| Low | $35.68 | Support du jour inchangé |
| RSI 14j | **41.52** | **Neutre-basse, inchangé** |
| MM 50j | $38.81 | Cours inférieur de **−6.8%** — cassure technique confirmée |
| Volume | 4,211,600 | **0.45× moy. 20j** — participation faible, inchangée |
| ATR 14j | $5.79 | Volatilité stable |
| Support 1 | $35.68 (Low du jour) | Support immédiat — zone $35.55–$35.70 |
| Support 2 | $35.55 (Low 08/06 17h) | Support de session précédente |
| Support 3 | $35.00 (psychologique) | Ancien support de consolidation (fin mai) |
| Résistance 1 | $38.81 (MM 50j) | Ancien support devenu résistance |
| Résistance 2 | $40.00 (Max Pain) | Aimant options — niveau de référence |
| Résistance 3 | $38.20 (High du jour) | Résistance intraday testée et rejetée |

**Timing verdict :** **Défavorable** — Inchangé. Le cours $36.18 reste sous la MM50 ($38.81) de −6.8%, avec un RSI stable à 41.52 et un Score Momentum à 3.5/10. L'expiration options J-3 (2026-06-12) avec max pain opérationnel $40.00 et spot $36.18 (−9.6%) positionne le marché options légèrement favorable aux puts. La zone $35.55–$35.70 reste le support critique à surveiller.

---

## Mise à jour fondamentale — Inchangée

Données croisées Yahoo / FMP (annual FY 2025) — **strictement inchangées** :

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market Cap (Yahoo) | $5.94B | Stable |
| Market Cap (FMP) | $3.40B | Stable — divergence Yahoo/FMP persistante |
| Forward P/E | **−27.78** | Stable — valorisation incompatible avec profil sans profit |
| EV/Revenue (Yahoo) | 28.66x | Stable |
| EV/Revenue (FMP) | 18.23x | Stable |
| P/B (Yahoo) | 5.241 | Stable |
| P/B (FMP) | 2.855 | Stable |
| Gross Margin (FMP) | 15.56% | Faible, stable |
| Operating Margin (FMP) | −154.25% | Fortement négatif, stable |
| Net Margin (FMP) | −186.63% | Fortement négatif, stable |
| Debt/Equity (FMP) | 0.259 | Levier modéré, stable |
| Current Ratio (FMP) | 4.51 | Liquidité solide, stable |
| Short Interest | 9.78% | Stable — pression vendeuse persistante |
| FMP Consensus PT | **$43.25 (12 analysts)** | **Inchangé** — upside mécanique +19.5% |

**Filtre Qualité** : **2/6** (Hors périmètre) — **strictement inchangé**. Aucun critère qualité n'est modifié par l'absence d'événement.

| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ | Pas de données >20% (FY 2025 Revenue/Share $1.05) |
| Profit CAGR 5 ans ≥ 20% | ❌ | Marges négatives |
| Assets/Liabilities > 1.0 | ✅ | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | ❌ | FCF yield négatif (−7.0%) |
| Avantage compétitif (moat) | ❌ | Aucun moat structurel identifié |
| Industrie forte croissance (TAM ×5) | ❌ | Aerospace & Defense en croissance, mais pas ×5 pour ce profil |
| **Score Qualité total** | **2/6** | 🔴 Hors périmètre |

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10. L'Agent Recommandation applique **5.5/10** (inchangé).

---

## Mise à jour sentiment / options / news — Silence total, anomalie options récurrente

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $43.25 (12 analysts) | FMP Stable API | PT **+19.5% au-dessus du spot** — inchangé. |
| Max Pain | **$19.00** | Yahoo Finance 10:00 UTC | ⚠️ **Anomalie data** — valeur aberrante (vs $40.00 opérationnel 08/06). Valeur opérationnelle conservée. |
| Put/Call Ratio | **null** | Yahoo Finance 10:00 UTC | ⚠️ **Anomalie data** — valeur opérationnelle 1.08 conservée. |
| Call OI % | **null** | Yahoo Finance 10:00 UTC | ⚠️ **Anomalie data** — valeur opérationnelle 48.1% conservée. |
| Short Interest | 9.78% | Yahoo Finance | Stable — pression vendeuse persistante, pas de setup squeeze. |
| Social Sentiment | 0 mention | `data/social_sentiment_2026-06-09.json` | Pas d'activité retail. |
| Event-Driven | Aucun | `data/events_2026-06-09.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (56 jours) | `data/upcoming_events_2026-06-09.json` | Est EPS −$0.61 à −$0.45, Rev $0.1B. |
| News FLY | Aucune | Pas de fichier news | **Aucune news spécifique** — silence médiatique persistant. |
| Expiration options | **2026-06-12 (J-3)** | Yahoo Finance | Max pain opérationnel $40.00 vs spot $36.18. |

**Score Catalyseur** : **6.0/10** (données agents). Aucun catalyseur nouveau. Le silence médiatique et l'absence d'événement corporate confirment que le cours stable à $36.18 est dénué de fondamental. La configuration options (max pain opérationnel $40.00, put/call 1.08) reste globalement neutre avec une légère coloration baissière. L'approche de l'expiration (J-3) pourrait créer une pression mécanique si le spot reste significativement sous $40.00.

---

## Scoring global — SURVEILLER (43.8) confirmé, stabilité totale

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 6.0/10 | 35% | 2.10 |
| Valorisation | 5.5/10 | 40% | 2.20 |
| Momentum | 3.5/10 | 25% | 0.88 |
| **Score Opportunité** | **5.2/10** | | |
| **Score Global** | **51.8** | | |
| **Score Global Ajusté** | **43.8** | | |

**Action :** **SURVEILLER**
**Direction :** Neutre
**Timing :** Défavorable
**Horizon :** —

**Note sur le scoring :** L'Agent Recommandation maintient FLY en **SURVEILLER (43.8)**. Tous les scores sont strictement identiques au close 08/06. Le Score Opportunité (5.2/10) franchit le seuil 5.0 mais le Score Global Ajusté tombe dans la fourchette 35–49 (SURVEILLER).

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (p-value 1.0, insuffisant depuis le 2026-05-17) — pas d'ajustement.
- **Agent Geo** : FLY non flaggé (geo_risk absent du rapport 2026-05-17) — pas de malus.
- **Agent Sector Rotation** : XLI momentum_score **2.65/10** — inchangé, headwind sectoriel persistant. Malus sectoriel −0.5 pt inchangé.
- **Agent Social** : 0 mention — neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0 — pas d'ajustement.
- **Agent Event-Driven** : 0 événement — neutre.
- **Agent Accounting** : `data/accounting_risk_latest.json` indisponible — pas d'ajustement.

---

## Révision des niveaux SL / TP — Inchangés (stabilité ATR)

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $36.18 | Snapshot 10h UTC 09/06 | +0.22% vs prior close $36.10 |
| Stop-loss | $24.60 | Agent Recommandation (2×ATR $5.79) | Inchangé |
| Take-profit | $53.55 | Agent Recommandation (3×ATR $5.79) | Inchangé |
| Ratio R/R | 1.5:1 | Agent Recommandation | Standard agent — limité pour un profil sans profit |

Les niveaux sont issus de l'Agent Recommandation et restent inchangés du fait de la stabilité de l'ATR. Le SL $24.60 correspond à une zone sous le support structurel $35.55. Le TP reflète un rebond partiel vers la zone $40–$46.

**Risque technique persistant :** L'expiration options J-3 (2026-06-12) avec max pain opérationnel $40.00 et spot $36.18 (−9.6%) pourrait créer une pression mécanique. En dessous de $35.55, le prochain support structuré reste vers $33.00–$34.00 (zone de gap fill du rally de mai). Une cassure de cette zone sur volume > 1.0× moy. 20j ouvrirait le chemin vers les $30.00.

---

## Conclusion — Thèse défavorable confirmée, stabilité totale sans catalyst — SURVEILLER (43.8)

**Verdict : Thèse défavorable CONFIRMÉE — SURVEILLER (43.8). Le snapshot à $36.18 (+0.22%) sur volume 0.45× n'est pas significatif. Aucun changement matériel depuis le close 08/06.**

Le snapshot 10h UTC du 09/06 confirme la **stabilité complète** de la dégradation technique : cours $36.18 (+0.22% vs prior close), volume 4.21M (0.45× moy. 20j), RSI stable à 41.52, Score Momentum stable à 3.5/10. L'Agent Recommandation maintient la thèse à **SURVEILLER (43.8)**.

**Ce qui renforce la thèse défavorable :**
- **Volume faible** : 0.45× moy. 20j — le cours stable est dénué de conviction acheteuse.
- **Score Momentum faible** : 3.5/10, Timing Défavorable.
- **Cassure MM50** : cours −6.8% sous la MM50 ($38.81) — tendance MT baissière confirmée.
- **Aucun catalyst identifié** : aucune news, aucun événement corporate.
- **Filtre Qualité 2/6, Forward P/E −27.78, EV/Revenue 28.6x** : fondamentaux inchangés et défavorables.
- **Short Interest 9.78%** : stable, pression vendeuse persistante.
- **Spot sous max pain** $40.00 de −9.6% — expiration J-3 potentiellement favorable aux puts.
- **Anomalie data options** : max pain $19.00 aberrant dans `latest.json` — [DONNÉES PARTIELLES].

**Ce qui modifie la thèse (aucun) :**
- Aucun changement matériel depuis le close 08/06.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 56 jours) : Est EPS −$0.61 à −$0.45, Rev $0.1B.
2. **Expiration options** (2026-06-12, J-3) : surveillance du comportement autour de $40.00.
3. **Reconstitution technique** : surveillance du comportement autour de $35.55 et $38.81.

**Risques :**
1. Rentabilité non démontrée et non attendue à court terme.
2. Multiple incompatible avec un profil quality compounding.
3. **Cassure MM50** — tendance MT retournée à la baissière.
4. Short Interest 9.78% : pression vendeuse persistante.
5. Divergence Yahoo/FMP sur Market Cap ($5.94B vs $3.40B) et P/B (5.24 vs 2.86) persistante — [DONNÉES PARTIELLES].
6. **Volume faible** : 0.45× moy. 20j — manque d'intérêt acheteur, risque de retournement baissier.
7. Forward P/E −27.78 : valorisation reste incompatible avec un profil sans profit.
8. **Absence de support technique** sous $35.55 — risque de retour vers $33.00–$34.00.
9. **Pin risk options J-3** : max pain opérationnel $40.00, spot $36.18 — puts $40.00 in-the-money.
10. **Anomalie data options récurrente** : max pain aberrant ($19.00) dans `latest.json` — nécessite vérification systématique des données brutes.

**Prochaine étape :**
- **Ne pas prendre de position** — SURVEILLER (43.8).
- **Surveiller le comportement autour de $35.55** : si cassure en clôture sur volume > 0.5× moy. 20j → risque d'accélération vers $33.00–$34.00.
- **Surveiller l'expiration options 2026-06-12** : comportement autour de $40.00.
- **Si rebond au-dessus de $38.81** (MM50) sur volume > 1.0× moy. 20j → possible réintégration technique, mais nécessite confirmation.
- **Si un catalyst fondamental émerge** → réévaluer Score Catalyseur et Filtre Qualité. Sans cela, le mouvement reste spéculatif.

---

*Snapshot 10:00 UTC 09/06 — Cours $36.18 (+0.22% vs prior close $36.10, −51.0% vs 52W high), RSI 41.52 neutre-basse, volume 4.21M (0.45× moy. 20j). Consensus inchangé $43.25 (12 analysts). Options : anomalie data max pain $19.00 (valeur opérationnelle conservée $40.00), put/call 1.08, call OI 48.1%, expiration 2026-06-12 (J-3). Aucun catalyst. Fondamentaux inchangés et défavorables. Agent Recommandation : SURVEILLER (43.8). Thèse défavorable confirmée.*

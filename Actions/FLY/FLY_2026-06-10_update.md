# FLY — Mise à Jour (2026-06-10, snapshot 10h UTC pré-ouverture NY)

> **Type :** `_update.md` — Snapshot 10h UTC, révision majeure du close 09/06, short interest en hausse, scores agents modifiés, thèse SURVEILLER confirmée avec nuance
> **Référence précédente :** [FLY_2026-06-09_update.md](FLY_2026-06-09_update.md) (close officiel 21h UTC 09/06)
> **Données source :** `data/latest.json` (timestamp 2026-06-10T10:00:08.820973+00:00), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Validation data :** FLY status `ok` dans `data/validation_report.txt`. Aucun warning. 25/29 tickers OK.

---

## Résumé — Révision majeure du close 09/06 à $36.18 (+8.18% vs 33.445 rapporté), short interest +23.9%, scores agents modifiés, SURVEILLER (46.8) maintenu

Le snapshot 10h UTC du 2026-06-10 révise le **`previous_close` à $36.18**, contre $33.445 rapporté hier en close officiel 21h UTC. Cette révision de **+8.18%** invalide la lecture du **gap baissier −7.56%** et du **rebond mécanique de clôture** construits sur le snapshot 21h. Le volume reporté est inchangé à **6.31M (0.69× moy. 20j)** — identique au snapshot 09/06, ce qui suggère un report de données de session dans le snapshot pré-ouverture. [DONNÉES PARTIELLES — open/high/low/close NaN, ATR/MM50/MM200 null.]

Le **short interest grimpe à 12.12%** (+2.34 pts vs 9.78% hier, soit +23.9% relative), signalant une pression vendeuse accrue. L'Agent Recommandation maintient **SURVEILLER** avec un **Score Global Ajusté de 46.8** (+1.8 pt vs 45.0), mais la composition des scores se dégrade : Score Catalyseur **5.0/10** (−1.5 pt), Score Valorisation **4.5/10** (−1.5 pt), tandis que le Score Momentum remonte mécaniquement à **4.5/10** (+2.0 pts) sur le close révisé. Le timing passe de **Défavorable** à **Neutre**.

**Changements significatifs vs close 09/06 (21h UTC) :**

| Métrique | 2026-06-09 21h UTC | 2026-06-10 10h UTC | Variation |
|----------|--------------------|--------------------|-----------|
| Cours close | $33.445 | **$36.18** (révision) | **+8.18%** |
| RSI 14j | 40.32 | **42.81** | +2.49 pts |
| MM 50j | $39.01 | **null** | [DONNÉES MANQUANTES] |
| Position vs MM50 | −14.3% | **—** | Indisponible |
| ATR 14j | $5.88 | **null** | [DONNÉES MANQUANTES] |
| Volume session | 6.31M | **6.31M (reporté)** | Inchangé — probable report |
| Volume vs moy. 20j | 0.69x | **0.69x** | Identique |
| Short Interest | 9.78% | **12.12%** | **+2.34 pts (+23.9%)** |
| Score Catalyseur | 6.5/10 | **5.0/10** | **−1.5 pt** |
| Score Valorisation | 6.0/10 | **4.5/10** | **−1.5 pt** |
| Score Momentum | 2.5/10 | **4.5/10** | **+2.0 pts** |
| Score Opportunité | 5.3/10 | **4.7/10** | **−0.6 pt** |
| Score Global Ajusté | 45.0 | **46.8** | +1.8 pt |
| Action | SURVEILLER | **SURVEILLER** | Confirmée |
| Timing | Défavorable | **Neutre** | Modifié |

**Verdict :** La révision du close à $36.18 invalide le récit du gap baissier −7.56% et du rebond mécanique de fin de séance. Le cours a en réalité clôturé stable vs le 08/06 ($36.18), invalidant la destruction de valeur intraday rapportée hier. Cependant, la **hausse du short interest à 12.12%** et la **détérioration des scores Catalyseur (−1.5 pt) et Valorisation (−1.5 pt)** confirment que la prudence reste de mise. L'absence de données techniques (ATR, MM50) et l'anomalie options persistante (max pain $19.00 aberrant) limitent la lisibilité. Thèse **SURVEILLER (46.8)** confirmée avec nuance — le timing passe à Neutre, mais la dégradation des fondamentaux perçus par l'agent (C↓, V↓) contrebalance le répit mécanique du close révisé.

---

## Mise à jour technique — Close révisé stable, données MT indisponibles

| Indicateur | Valeur | Verdict |
|------------|--------|---------|
| Cours (previous_close) | $36.18 | Révision +8.18% vs $33.445 rapporté hier — stable vs 08/06 |
| RSI 14j | **42.81** | Zone neutre dégradée, légère amélioration vs 40.32 |
| MM 50j | null | [DONNÉES MANQUANTES] — cassure MT non vérifiable dans ce snapshot |
| Volume | 6,312,138 | Reporté identique au 09/06 — [DONNÉES PARTIELLES] |
| Volume vs moy. 20j | 0.69× | Identique au 09/06 — manque d'intérêt structurel |
| ATR 14j | null | [DONNÉES MANQUANTES] — impossible de calculer les niveaux SL/TP |
| Support 1 | $31.91 (low 09/06) | Zone testée hier, tenue si close révisé confirmé |
| Support 2 | $30.00 (psychologique) | Support structurel majeur |
| Résistance 1 | $39.00–$39.50 (zone MM50 ancienne) | Résistance MT si MM50 reste autour de $39 |
| Résistance 2 | $40.00 (max pain opérationnel ancien) | Ancienne résistance options |
| 52W Range | $16.00 – $73.80 | Midpoint $44.90 — cours $36.18 = −19.4% sous midpoint |

**Timing verdict :** **Neutre** — Modifié depuis Défavorable. Le close révisé à $36.18 élimine le gap baissier −7.56% et améliore mécaniquement le momentum. Cependant, l'absence de MM50 et d'ATR dans `latest.json` rend impossible toute confirmation de la structure technique. L'expiration options **J-2 (2026-06-12)** approche avec un **max pain aberrant à $19.00** dans le snapshot (vs $40.00 opérationnel précédent) — [ANOMALIE DATA]. La zone $36.00–$37.00 est le niveau clé à surveiller en ouverture.

---

## Mise à jour fondamentale — Multiples inchangés, Filtre Qualité stable, divergence Yahoo/FMP persistante

Données croisées Yahoo / FMP (annual FY 2025) :

| Métrique | Valeur | Variation vs 09/06 | Commentaire |
|----------|--------|--------------------|-------------|
| Market Cap (Yahoo) | **$5.49B** | +8.2% | Mécanique révision du close |
| Market Cap (FMP) | $3.40B | Inchangé | Divergence Yahoo/FMP persistante |
| Forward P/E (Yahoo) | **−25.68** | Inchangé | Profil sans profit |
| EV/Revenue (Yahoo) | 26.29x | Inchangé | Multiple incompatible avec profil sans profit |
| EV/Revenue (FMP) | 18.23x | Inchangé | Stable |
| P/B (Yahoo) | 4.845 | +8.2% | Mécaniquement ajusté au close révisé |
| P/B (FMP) | 2.855 | Inchangé | Stable |
| Gross Margin (FMP) | 15.56% | Inchangé | Faible |
| Operating Margin (FMP) | −154.25% | Inchangé | Fortement négatif |
| Net Margin (FMP) | −186.63% | Inchangé | Fortement négatif |
| Debt/Equity (FMP) | 0.259 | Inchangé | Levier modéré |
| Current Ratio (FMP) | 4.51 | Inchangé | Liquidité solide |
| Short Interest | **12.12%** | **+2.34 pts** | 🔴 Pression vendeuse accrue |
| FMP Consensus PT | $43.25 (12 analysts) | Inchangé | Upside mécanique +19.5% vs $36.18 |

**Filtre Qualité** : **2/6** (Hors périmètre) — strictement inchangé. L'événement prix (révision du close) n'a aucun impact sur la structure fondamentale.

| Critère | Score | Justification |
|---------|-------|---------------|
| Revenue CAGR 5 ans ≥ 20% | ❌ | Pas de données >20% (FY 2025 Revenue/Share $1.05) |
| Profit CAGR 5 ans ≥ 20% | ❌ | Marges négatives |
| Assets/Liabilities > 1.0 | ✅ | Current Ratio 4.51 |
| FCF positif et croissant 5 ans | ❌ | FCF yield négatif (−7.0%) |
| Avantage compétitif (moat) | ❌ | Aucun moat structurel identifié |
| Industrie forte croissance (TAM ×5) | ❌ | Aerospace & Defense en croissance, mais pas ×5 pour ce profil |
| **Score Qualité total** | **2/6** | 🔴 Hors périmètre |

**Règle** : Score ≤ 3/6 → Score Valorisation plafonné à 5/10. L'Agent Recommandation applique **4.5/10** — la détente mécanique du close révisé n'améliore pas la qualité intrinsèque, et l'agent a en fait baissé le score Valorisation de 6.0 à 4.5.

---

## Mise à jour sentiment / options / news — Short interest accrue, silence médiatique persistant, anomalie options

| Signal | Valeur | Source | Interprétation |
|--------|--------|--------|----------------|
| Consensus analystes (FMP) | $43.25 (12 analysts) | FMP Stable API | PT **+19.5% au-dessus du spot révisé** — upside mécanique stable. |
| Max Pain | **$19.00** | `latest.json` 10:00 UTC | 🔴 **ANOMALIE DATA** — valeur aberrante (vs $40.00 opérationnel 09/06). Valeurs opérationnelles conservées : $40.00. |
| Put/Call Ratio | null | `latest.json` | Anomalie data persistante. |
| Call OI % | null | `latest.json` | Anomalie data persistante. |
| Short Interest | **12.12%** | Yahoo Finance | 🔴 **Hausse significative** (+2.34 pts, +23.9%) — pression vendeuse accrue, pas de setup squeeze. |
| Social Sentiment | 0 mention | `data/social_sentiment_2026-06-10.json` | Pas d'activité retail. |
| Event-Driven | Aucun | `data/events_2026-06-10.json` | Pas de M&A, buyback, guidance change, activism. |
| Upcoming Events | Earnings Q2 2026 le 2026-08-04 (55 jours) | `data/upcoming_events_2026-06-10.json` | Est EPS −$0.61 à −$0.45, Rev $0.1B. |
| News FLY | Aucune | Pas de fichier news | **Silence médiatique persistant.** |
| Expiration options | **2026-06-12 (J-2)** | Yahoo Finance | Max pain opérationnel $40.00 vs spot révisé $36.18 (−9.6%) — puts partiellement ITM. |

**Score Catalyseur** : **5.0/10** (−1.5 pt vs 09/06). Aucun catalyst fondamental nouveau. La dégradation du score catalyseur par l'agent reflète probablement la hausse du short interest et l'absence de momentum positif. La divergence consensus/spot ($43.25 vs $36.18 = +19.5%) reste le principal facteur de soutien, mais atténué. L'anomalie data options (max pain $19.00 aberrant) persiste — valeurs opérationnelles $40.00 conservées.

---

## Scoring global — SURVEILLER (46.8) confirmé, composition dégradée

| Axe | Score | Pondération | Contribution |
|-----|-------|-------------|------------|
| Catalyseur | 5.0/10 | 35% | 1.75 |
| Valorisation | 4.5/10 | 40% | 1.80 |
| Momentum | 4.5/10 | 25% | 1.13 |
| **Score Opportunité** | **4.7/10** | | |
| **Score Global** | **46.8** | | |
| **Score Global Ajusté** | **46.8** | | |

**Action :** **SURVEILLER**
**Direction :** Neutre
**Timing :** Neutre
**Horizon :** —

**Note sur le scoring :** L'Agent Recommandation maintient FLY en **SURVEILLER (46.8)** (+1.8 pt vs 45.0). Le Score Opportunité recule de 5.3 à **4.7/10**, mais le Score Global Ajusté reste dans la fourchette 35–49 (SURVEILLER). La composition des scores se dégrade : Catalyseur et Valorisation chutent de −1.5 pt chacun, tandis que le Momentum remonte mécaniquement (+2.0 pts) sur le close révisé. Le **Score Valorisation à 4.5/10** est désormais le facteur dominant négatif.

**Ajustements agents complémentaires :**
- **Agent Quant** : Signaux non significatifs (p-value null, n=0, insuffisant) — pas d'ajustement.
- **Agent Geo** : FLY non flaggé (geo_risk_score absent) — pas de malus.
- **Agent Sector Rotation** : Données corrompues dans `latest.json` (tous momentum_score 10.0, returns NaN) — [DONNÉES PARTIELLES], pas d'ajustement.
- **Agent Social** : 0 mention — neutre.
- **Agent FX** : Exposition 25%, fx_impact_score 0.0, flag 🟢 — pas d'ajustement.
- **Agent Event-Driven** : 0 événement — neutre.
- **Agent Accounting** : Fichier indisponible — pas d'ajustement.

---

## Révision des niveaux SL / TP — [DONNÉES MANQUANTES] (ATR indisponible)

| Niveau | Valeur | Méthode | Commentaire |
|--------|--------|---------|-------------|
| Cours actuel | $36.18 | Previous close révisé 10h UTC | Révision +8.18% vs $33.445 |
| Stop-loss | **—** | [DONNÉES MANQUANTES] | ATR 14j null dans `latest.json` — impossible de calculer |
| Take-profit | **—** | [DONNÉES MANQUANTES] | ATR 14j null dans `latest.json` — impossible de calculer |
| Ratio R/R | — | — | Non calculable sans ATR |

Les niveaux SL/TP ne peuvent pas être révisés en l'absence d'ATR dans le snapshot 10h UTC. Les derniers niveaux opérationnels étaient SL $21.69 / TP $51.09 (basés sur ATR $5.88 du 09/06), mais ces niveaux sont obsolètes si le close révisé à $36.18 est confirmé. Sur la base de l'ancien ATR $5.88, les niveaux révisés mécaniquement seraient SL $24.42 / TP $53.82 — à confirmer dès rétablissement des données techniques.

**Risque technique persistant :** L'expiration options **J-2 (2026-06-12)** avec max pain opérationnel $40.00 et spot révisé $36.18 (−9.6%) positionne le marché options favorable aux puts $35.00–$40.00. La zone $31.91 (low 09/06) demeure le support technique clé. Une cassure de $31.91 en clôture sur volume > 1.0× moy. 20j ouvrirait le chemin vers $30.00–$28.00.

---

## Conclusion — Thèse modifiée : le close révisé invalide le gap baissier, mais la dégradation des scores C/V et le short interest ↑ maintiennent la prudence

**Verdict : Thèse modifiée — SURVEILLER (46.8). Le snapshot 10h UTC révise le close 09/06 à $36.18 (vs $33.445 précédemment), invalidant le récit du gap baissier −7.56% et du rebond mécanique. Cependant, la dégradation des scores agents (C −1.5 pt, V −1.5 pt) et la hausse du short interest à 12.12% confirment qu'aucun catalyst positif n'est en vue.**

Le close révisé à $36.18 signifie que le cours a clôturé **stable vs le 08/06** ($36.18), et non en gap baissier. Cela élimine la destruction de valeur intraday rapportée hier et améliore mécaniquement le momentum (RSI 42.81, Score Momentum 4.5/10). Le timing passe de Défavorable à Neutre.

**Ce qui renforce la prudence :**
- **Short Interest 12.12%** (+23.9% vs 09/06) : pression vendeuse accrue, pas de setup squeeze.
- **Score Catalyseur 5.0/10** (−1.5 pt) : dégradation de la perception des catalysts par l'agent.
- **Score Valorisation 4.5/10** (−1.5 pt) : valorisation désormais vue comme défavorable.
- **Filtre Qualité 2/6, Forward P/E −25.68, EV/Revenue 26.3x** : fondamentaux inchangés et défavorables.
- **Aucun catalyst identifié** : aucune news, aucun événement corporate, 0 mention social.
- **Anomalie data options persistante** : max pain $19.00 aberrant dans `latest.json`.
- **Données techniques partielles** : ATR, MM50, MM200 null — impossible de confirmer la structure technique.
- **Divergence Yahoo/FMP** sur Market Cap ($5.49B vs $3.40B) et P/B (4.845 vs 2.855) persistante.

**Ce qui modifie la thèse en nuance positive (révision du close) :**
- Close révisé $36.18 vs $33.445 : **+8.18% de correction** — pas de gap baissier.
- RSI 42.81 vs 40.32 : léger répit technique.
- Score Momentum 4.5/10 vs 2.5/10 : répit mécanique.
- Timing passe de Défavorable à Neutre.

**Catalyseurs forward :**
1. **Earnings Q2 2026** (2026-08-04, 55 jours) : Est EPS −$0.61 à −$0.45, Rev $0.1B.
2. **Expiration options** (2026-06-12, J-2) : surveillance du comportement autour de $35.00–$40.00 avec spot révisé $36.18.
3. **Rétablissement des données techniques** : ATR, MM50, MM50 attendus dans le prochain snapshot pour confirmer la structure.

**Risques :**
1. Rentabilité non démontrée et non attendue à court terme.
2. Multiple incompatible avec un profil quality compounding.
3. Short Interest 12.12% : pression vendeuse accrue.
4. Divergence Yahoo/FMP sur Market Cap et P/B persistante — [DONNÉES PARTIELLES].
5. Forward P/E −25.68 : valorisation incompatible avec un profil sans profit.
6. **Absence de support technique confirmé** sous $31.91 — risque de retour vers $30.00–$28.00.
7. **Volatilité élevée** : ATR historique ~$5.88, range intraday 09/06 $31.91–$38.00 (19.1%).
8. Données techniques indisponibles (ATR, MM50) — impossible de calibrer les niveaux de sortie.

**Prochaine étape :**
- **Ne pas prendre de position** — SURVEILLER (46.8).
- **Attendre le snapshot post-ouverture NY** pour confirmer le close $36.18 et récupérer ATR/MM50.
- **Surveiller le comportement autour de $36.00–$37.00** : si le cours tient ce niveau en session → répit technique confirmé.
- **Surveiller le short interest** : si dépasse 15% → risque de squeeze ou de pression accrue.
- **Surveiller l'expiration options 2026-06-12** : comportement autour de $35.00–$40.00 avec spot révisé.
- **Si un catalyst fondamental émerge** → réévaluer Score Catalyseur et Filtre Qualité. Sans cela, le mouvement reste spéculatif / technique.

---

*Snapshot 10:00 UTC 10/06 — Previous close révisé $36.18 (vs $33.445 précédemment), RSI 42.81, volume 6.31M (reporté, 0.69× moy. 20j), Short Interest 12.12% (+23.9%). Consensus inchangé $43.25 (12 analysts). Options : max pain aberrant $19.00 dans latest.json (valeur opérationnelle conservée $40.00), expiration 2026-06-12 (J-2). Aucun catalyst. Fondamentaux inchangés et défavorables. Données techniques partielles (ATR/MM50 null). Agent Recommandation : SURVEILLER (46.8). Thèse modifiée — révision du close invalide le gap baissier, mais prudence maintenue.*

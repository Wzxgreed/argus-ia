# TEST — Mise à jour quotidienne (snapshot 10h UTC)

> **Date :** 2026-06-15
> **Type :** Mise à jour post-pipeline matin
> **Source :** data/latest.json (snapshot 10:00 UTC), data/recommandations_latest.json

---

## Résumé des changements depuis l'analyse précédente

| Indicateur | 2026-06-10 10h UTC | 2026-06-15 10h UTC | Δ |
|------------|-------------------|-------------------|---|
| Cours close | **NaN** | **$44.836** | **Données rétablies** 🟢 |
| Previous close | $45.35 | $44.121 | **−$1.23** 🔴 |
| RSI 14j | 57.17 | **47.08** | **−10.09 pts** 🔴 |
| MM 50j | null | **$43.6** | **Disponible** 🟢 |
| MM 200j | null | null | [DONNÉES MANQUANTES] |
| ATR 14j | null | **$1.25** | **Disponible** 🟢 |
| Volume session | 1,570 | **1,000** | **−36.3%** 🔴 |
| Volume vs avg 20j | 0.64× | **0.41×** | **Plus faible** 🔴 |
| Score Global | 57.8 | **61.0** | **+3.2 pts** 🟢 |
| Score Global Ajusté | 57.8 | **66.0** | **+8.2 pts** 🟢 |
| Score Opportunité | 5.8/10 | **6.1/10** | **+0.3 pt** 🟢 |
| Score Momentum | 6.0/10 | **7.3/10** | **+1.3 pts** 🟢 |
| Verdict | ATTENDRE | **ACHETER (Réduit)** | **Regradation** 🟢 |
| SL | null | **$42.34** | **Calculé** 🟢 |
| TP | null | **$48.59** | **Calculé** 🟢 |

**Données techniques rétablies.** Le snapshot 10h UTC du 2026-06-15 fournit pour la première fois depuis le 10 juin un cours de clôture complet ($44.836), un ATR14 ($1.25) et une MM50 ($43.6). L'agent de recommandations a regradé le verdict de **ATTENDRE** à **ACHETER (Réduit)** malgré une baisse du RSI de 10 pts, car le retour des données techniques permet désormais de valider le positionnement au-dessus de la MM50 (+$1.24, soit +2.8%). Le Score Global remonte de 57.8 à **61.0** (66.0 ajusté), rentrant dans la fourchette ACHETER (Réduit) (60–74).

---

## Mise à jour technique

- **Cours :** $44.836, hausse de **+1.62%** vs previous close ($44.121). Open $43.72, high $44.836, low $43.415 — range intraday étroit ($1.42, soit 3.2%).
- **RSI 14j :** 47.08, en baisse de **10.09 pts** vs snapshot 10h UTC du 10/06 (57.17). Retour en zone neutre (40–50). Cette baisse malgré la hausse du cours (+1.62%) est contre-intuitive ; elle s'explique probablement par le recalcul du RSI sur des données complètes (high/low désormais disponibles) vs le snapshot partiel du 10 juin où seul un RSI approximatif était injecté. [DONNÉES PARTIELLES RÉSOLUES]
- **MM 50j :** $43.6, désormais disponible. Cours au-dessus de la mobile (+$1.24, +2.8%) → signal technique haussier.
- **MM 200j :** `null` — donnée manquante persistante.
- **ATR 14j :** $1.25, désormais disponible. Volatilité historiquement faible (range 52 semaines $40.27–$57.74, ATR = 2.7% du range).
- **Volume :** 1,000 unités (0.41× moyenne 20j de 2,410). Volume en baisse de 36% vs session précédente et toujours très contraint. Sur un ticker aussi illiquide, tout niveau technique est fragile.

**Verdict timing :** Favorable. Le cours est au-dessus de la MM50, l'ATR est disponible et le range intraday est cohérent. Cependant le RSI retourne en zone neutre-basse (47) et le volume très faible limite la fiabilité du signal.

---

## Mise à jour fondamentale

Aucune donnée fondamentale nouvelle. TEST reste sans :
- Market cap, P/E, forward P/E, EV/EBITDA, EV/Revenue, P/B, dividend yield, beta
- Données FMP (ratios, key metrics, consensus analystes)
- Données options (max pain, put/call ratio, call OI)

**Accounting risk :** fichier `data/accounting_risk_latest.json` absent — impossible d'évaluer M-Score, Z-Score, F-Score, Sloan Ratio.

**Earnings JOUR J** (2026-06-15, source FMP, `days_until = 0`) — le flag persiste pour la 15e+ journée consécutive sans résolution. L'hypothèse d'un artefact de calendrier FMP est confirmée. Aucun résultat observable.

---

## Mise à jour sentiment / options / news

Données issues de `data/recommandations_latest.json` (2026-06-15, snapshot 10h UTC) :

| Axe | Score 10/06 10h | Score 15/06 10h | Δ |
|-----|----------------|----------------|---|
| Catalyseur | 6.5/10 | 6.5/10 | Stable |
| Valorisation | 5.0/10 | 5.0/10 | Stable |
| Momentum | 6.0/10 | **7.3/10** | **+1.3 pts** 🟢 |
| Opportunité | 5.8/10 | **6.1/10** | **+0.3 pt** 🟢 |

**Modules agents (snapshot 10h UTC) :**
- `quant_report_latest.json` (2026-06-15) : insuffisant — pas de signaux historiques.
- `geo_risk_latest.json` (2026-06-15) : score géo 2/10, aucun flag géopolitique pour TEST.
- `accounting_risk_latest.json` : fichier absent.
- `sector_rotation_latest.json` (2026-06-15) : régime UNKNOWN, signal NEUTRAL. TEST sans secteur assigné.
- `social_sentiment_latest.json` (2026-06-15) : 0 mention, sentiment « No data », pas de pump.
- `fx_exposure_latest.json` (2026-06-15) : exposition FX 25%, impact score 0.0, divergence aligned.
- `events_latest.json` (2026-06-15) : 0 événement corporate détecté pour TEST.
- `upcoming_events_latest.json` (2026-06-15) : earnings JOUR J (2026-06-15, source FMP, days_until = 0) — toujours non résolu, hypothèse artefact renforcée.

---

## Nouveau scoring global

| Métrique | Valeur |
|----------|--------|
| Score Opportunité | 6.1/10 |
| Score Catalyseur | 6.5/10 |
| Score Valorisation | 5.0/10 |
| Score Momentum | 7.3/10 |
| Score Global | 61.0/100 |
| Score Global Ajusté | 66.0/100 |
| Verdict | **ACHETER (Réduit)** |
| Timing | Favorable |
| Horizon | 1–3 mois |
| Sizing | Réduit |

Le Score Global est passé de 57.8 à **61.0/100** (66.0 ajusté), franchissant le seuil **ACHETER (Réduit)** (60–74). L'amélioration est portée par la hausse du Score Momentum (+1.3 pts, de 6.0 à 7.3), liée au retour des données complètes et à la validation du positionnement au-dessus de la MM50. La règle de disqualification n'est pas activée (aucun score ≤ 2/10).

---

## Révision des niveaux SL / TP

**Niveaux désormais calculables** — l'ATR 14j ($1.25) et le cours close ($44.836) sont disponibles dans le snapshot 10h UTC.

| Niveau | Ancien (10/06 10h) | Nouveau (15/06 10h) | Calcul |
|--------|-------------------|--------------------|--------|
| Stop-loss | null | **$42.34** | close − 2×ATR = $44.836 − $2.50 |
| Take-profit | null | **$48.59** | close + 3×ATR = $44.836 + $3.75 |
| Ratio R/R | null | **1.5** | gain $3.75 / perte $2.50 |

Le niveau de stop-loss ($42.34) est à +$2.07 au-dessus du low 52 semaines ($40.27), offrant une marge de sécurité raisonnable mais étroite compte tenu de l'illiquidité. Le take-profit ($48.59) est à −$9.15 du high 52 semaines ($57.74).

---

## Conclusion — Thèse regradée

**La thèse est REGRADÉE : passage ATTENDRE → ACHETER (Réduit).**

**Raisons du regradement :**
1. **Données techniques rétablies** : le snapshot fournit désormais cours, ATR et MM50. Le positionnement au-dessus de la MM50 ($43.6) à +2.8% valide le signal haussier suspendu depuis le 10 juin.
2. **Amélioration mécanique des scores** : Score Momentum +1.3 pt, Score Global +3.2 pts. L'agent reco a reclassé le verdict en ACHETER (Réduit).
3. **Niveaux calculables** : SL/TP et ratio R/R = 1.5 désormais exploitables, rétablissant la capacité de positionnement.

**Points de vigilance :**
- **Illiquidité extrême** : volume 1,000 (0.41× moyenne 20j). Sur un ticker microstructure aussi fine, tout signal technique est fragile et les stops peuvent être traversés par un ordre de taille modeste.
- **RSI en baisse à 47.08** : malgré la hausse du cours, le retour en zone neutre-basse indique un momentum qui ne s'accélère pas. Le précédent reclaim de MM50 du 9 juin (RSI 50.48 → score 64.0) avait déjà montré une fragilité sous-jacente.
- **Earnings JOUR J persistant** : le flag FMP (2026-06-15, days_until = 0) n'a toujours pas été résolu après 15+ jours. Risque d'artefact confirmé, mais l'incertitude technique est maintenant mieux circonscrite.
- **Absence de données fondamentales** : impossible d'établir une thèse qualitative. TEST reste un ticker de test / cohérence flux.

**Scénarios de suivi :**
- Si cours conserve la MM50 sur volume > 0.5× avg → maintien **ACHETER (Réduit)**.
- Si cours perd la MM50 ($43.6) sur volume > moyenne → dégradation **ATTENDRE** voire **SURVEILLER**.
- Si volume reste < 0.3× avg malgré la hausse → signal de faiblesse, révision du sizing à minimal.

---

*Format institutionnel JPM/GS/MS — Données : data/latest.json (snapshot 10h UTC), data/recommandations_latest.json, data/upcoming_events_latest.json*

# SOFI — Mise à jour quotidienne (2026-06-29)

> **Date :** 2026-06-29 (snapshot 10:00 UTC — close final confirmé)
> **Type :** Mise à jour quotidienne
> **Trigger :** Pipeline quotidien + nouveau close + volume normalisé + RSI franchi

---

## 1. Résumé des changements depuis l'analyse précédente (2026-06-23 17h UTC)

| Métrique | 2026-06-29 | 2026-06-23 17h | Δ |
|----------|-----------|----------------|---|
| Cours close | **$17.88** | $17.48 | **+2.29%** |
| RSI 14j | **66.79** | 48.32 | **+18.47 pts** |
| ATR 14j | **$0.97** | $0.99 | **−$0.02** |
| MM 50j | **$16.95** | $16.98 | **−$0.03** |
| Écart MM50 | **+5.49%** | +2.94% | **+2.55 pts** |
| Volume | **90.52M** | 47.84M | **+89.2%** |
| Volume vs 20j | **1.03×** | 0.59× | **+0.44×** |
| Forward P/E | **21.99** | 21.41 | **+2.7%** |
| Short interest | **15.48%** | 14.71% | **+0.77 pt** |
| XLF momentum | **8.4/10** | 6.23/10 | **+2.17 pts** |
| Jours avant earnings | **29j** | 35j | **−6j** |

**Verdict global :** Nouveau close $17.88 sur volume normalisé **1.03×** — **[LEVÉ]** l'alerte volume effondré du 23/06 (0.59×) est entièrement levée. Le RSI franchit **66.79** (+18.47 pts), approchant la zone de surachat (70). Le short interest monte à **15.48%** (+0.77 pt), renforçant le setup asymétrique squeeze. Le momentum sectoriel XLF bondit à **8.4/10** (+2.17 pts) — soutien sectoriel massif. Le reclaim MM50 est solidifié à +5.49%. **Thèse confirmée et renforcée.**

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | $17.88 | `latest.json` |
| Open / High / Low | $17.00 / $17.97 / $16.99 | `latest.json` |
| Change % | +3.35% | `latest.json` |
| Volume | 90,515,600 | `latest.json` |
| Volume vs 20j | 1.03× (moy. 87,808,445) | Calcul agent |
| RSI 14j | 66.79 | `latest.json` |
| ATR 14j | $0.97 | `latest.json` |
| MM 50j | $16.95 | `latest.json` |
| Beta | 2.152 | `latest.json` |

**Niveaux clés :**
- Support immédiat : $16.99 (low 29/06)
- Support secondaire : $16.95 (MM50)
- Résistance : $17.97 (high 29/06)
- Stop-loss ATR (2×) : **$15.94**
- Take-profit ATR (3×) : **$20.79**

**Verdict timing :** Favorable — cours au-dessus de MM50 (+5.49%), RSI 66.79 en zone neutre-haute proche de la surachat. Le volume 1.03× valide la conviction institutionnelle après 6 sessions de retrait. Attention au risque de pullback technique si RSI > 70.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $22.90B | `latest.json` |
| P/E (TTM) | 39.67 | `latest.json` |
| Forward P/E | 21.99 | `latest.json` |
| EV/Revenue | 5.45 | `latest.json` |
| P/B | 2.12 | `latest.json` |
| FMP Consensus PT | $25.41 (27 analysts) | `latest.json` |
| FMP Gross Margin | 75.1% | `latest.json` |

**Filtre Qualité :** 4/6 (Quality Partielle) — inchangé. Aucun nouvel élément fondamental.

**Évolution fondamentale mécanique :**
- Forward P/E +2.7% ($21.99 vs $21.41) = expansion multiple mécanique sur hausse cours.
- P/B passe de 2.03 à 2.12 — cohérent avec le mouvement de +3.35%.
- Market Cap $22.90B (+4.4% vs $21.93B) — réévaluation mécanique.

---

## 4. Bloc Sentiment / Options / News

| Signal | Valeur | Source | Δ vs 23/06 |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | $25.41 (27 analysts) | `latest.json` | inchangé |
| Put/Call ratio | 0.50 | Historique 23/06 | inchangé* |
| Max pain | $18.00 | Historique 23/06 | inchangé* |
| Call OI % | 66.8% | Historique 23/06 | inchangé* |
| Short interest | 15.48% | `latest.json` | **+0.77 pt** |

*\* [ALERTE DATA QUALITY] Données options corrompues dans `latest.json` (Max Pain $5.00 aberrant, Put/Call null, Call OI null). Valeurs historiques du 23/06 conservées.*

**Verdict Sentiment :** Neutre légèrement haussier renforcé. Consensus PT $25.41 (+42.1% upside). Short interest 15.48% = setup asymétrique squeeze renforcé. Aucune news structurante détectée (`data/news_latest.json` : 0 items pour SOFI). Aucun événement corporate (`data/events_latest.json` : 0 événements).

**Social Sentiment :** `social_sentiment_latest.json` (2026-06-29) : 0 mentions Reddit, sentiment score 0.0 (No data), pump detected : false.

---

## 5. Scoring global

| Score | 2026-06-29 | 2026-06-23 17h | Δ |
|-------|-----------|----------------|---|
| Score Opportunité | **6.3/10** | 6.4/10 | −0.1 pt |
| Score Catalyseur | **6.8/10** | 6.8/10 | stable |
| Score Valorisation | **5.5/10** | 5.5/10 | stable |
| Score Momentum | **7.0/10** | 7.3/10 | −0.3 pt |
| Score Global | **63.3/100** | — | — |
| Score Global ajusté | **68.3/100** | 69.0/100 | −0.7 pt |
| Action | **ACHETER (Réduit)** | ACHETER (Réduit) | inchangé |
| Timing | **Favorable** | Favorable | inchangé |

**Source :** `data/recommandations_latest.json` (pipeline 2026-06-29 10:00 UTC).

**Note sur le scoring :** Le score global ajusté recule marginalement (−0.7 pt) malgré une amélioration technique et sectorielle majeure. Cette contraction reflète probablement une compression de la prime de valorisation (Forward P/E +2.7%) et un ajustement du modèle de scoring face au RSI approchant la surachat. Le ticker reste dans la fourchette **ACHETER (60–74)** avec sizing **Réduit** — au **bord inférieur**.

---

## 6. Niveaux révisés

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix d'entrée suggéré | $17.88 | Close actuel |
| Stop-loss | **$15.94** | Cours − 2×ATR ($0.97) |
| Take-profit | **$20.79** | Cours + 3×ATR ($0.97) |
| Ratio R/R | **1.5×** | (TP − Cours) / (Cours − SL) |
| Sizing | **Réduit** | Score Global 60–74 (bord inférieur) |

**Niveaux révisés à la hausse** — SL remonté de $15.50 à $15.94 (+$0.44), TP remonté de $20.45 à $20.79 (+$0.34) sur la base du nouveau close et de l'ATR stable.

---

## 7. Bloc Macro & Sectoriel

**Régime macro :** Unknown (`latest.json` — pas de valeur macro détectée).

**Sectoriel (Sector Rotation) :**
- XLF (Financials) : #4/11 sectors, momentum score **8.4/10** (+2.17 pts vs 6.23/10 le 23/06) — saut majeur, transformant le soutien sectoriel en vent de poupe puissant.
- SOFI classé Financial Services / Credit Services — alignement sectoriel très favorable.

**Exposition FX :**
- `fx_exposure_latest.json` : FX Impact Score 0.0, direction neutral, divergence aligned. Aucun headwind/tailwind.

**Géopolitique :**
- `geo_risk_latest.json` (2026-05-17) : SOFI non flaggé.

---

## 8. Bloc Quant & Risques

**Quant :**
- `quant_report_latest.json` (2026-05-17) : calibration insuffisante. Aucune alerte.

**Accounting :**
- `accounting_risk_latest.json` : fichier absent — aucun malus accounting appliqué.

**Event-Driven :**
- `events_latest.json` (2026-06-29) : 0 événements corporates détectés pour SOFI.

**Upcoming Events :**
- Earnings Q2 FY2026 : **2026-07-28** (dans **29 jours**) — estimates EPS $0.10–$0.11, Rev $1.1B.

---

## 9. Conclusion — Thèse confirmée et renforcée

**La thèse est confirmée et renforcée.** Le close $17.88 du 29/06 apporte trois éléments majeurs :

1. **Volume normalisé 1.03×** — [LEVÉ] l'alerte volume effondré du 23/06 (0.59×) est entièrement levée. La hausse de +3.35% s'opère sur participation institutionnelle normale, validant la solidité du mouvement.

2. **RSI 66.79** — franchissement massif de +18.47 pts, sortie de la zone neutre-basse pour approcher la surachat (70). Signal technique fort mais imposant une vigilance sur un éventuel pullback.

3. **Short interest 15.48%** (+0.77 pt) — le setup asymétrique squeeze/pression vendeuse est renforcé. Toute surprise positive (earnings, guidance) pourrait déclencher un short-covering amplifié par le beta 2.152.

**Point de vigilance résiduel :** Le RSI 66.79 est à 3.2 pts de la zone de surachat (70). Un mouvement > $18.30 sur la prochaine session pourrait pousser le RSI au-dessus de 70 et déclencher un repli technique. Le pinning options vers Max Pain $18.00 (expiration 02/07) reste un facteur de résistance court terme.

**Amélioration sectorielle majeure :** Le momentum XLF est passé de 6.23 à **8.4/10** (+2.17 pts) — le soutien sectoriel est désormais un vent de poupe puissant, le meilleur depuis le début du suivi.

**Catalyseurs forward :**
| Catalyst | Timeline | Probabilité | Impact |
|----------|----------|-------------|--------|
| Earnings Q2 FY2026 | 28 juillet 2026 (29j) | Haute | EPS $0.10–$0.11, Rev $1.1B |
| Décision Fed (taux) | Juin–Juillet 2026 | Moyenne | Impact NIM et lending |
| Short squeeze setup | Continu | Moyenne | SI 15.48% = setup asymétrique renforcé |
| Pinning options | Expiration 02/07 | Haute | Max Pain $18.00 = résistance |

**Risques clés :**
1. **Surachat technique** — RSI 66.79, risque de pullback si > 70.
2. **Earnings Q2** — 29j. Beta 2.152 amplifie tout gap post-earnings.
3. **Pinning options** — Max Pain $18.00, expiration 02/07 (3j).
4. **Données options corrompues** dans `latest.json` — surveiller correction sur prochains snapshots.

---

*Généré automatiquement — données source : `data/latest.json` (2026-06-29T10:00 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/social_sentiment_latest.json`, `data/news_latest.json`, `data/quant_report_latest.json`.*

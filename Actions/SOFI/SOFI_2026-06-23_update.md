# SOFI — Mise à jour snapshot matinal (2026-06-23 10:00 UTC)

> **Date :** 2026-06-23 (snapshot 10:00 UTC — pré-ouverture US)
> **Type :** Mise à jour snapshot matinal
> **Trigger :** Pipeline quotidien + micro-révision données + amélioration sectorielle XLF

---

## 1. Résumé des changements depuis l'analyse précédente (2026-06-22 21h UTC)

| Métrique | 2026-06-23 10h UTC | 2026-06-22 21h UTC | Δ |
|----------|-------------------|---------------------|---|
| Cours close | **$17.10** | $17.10 | **stable** |
| RSI 14j | **40.98** | 40.98 | **stable** |
| ATR 14j | **$1.00** | $1.00 | **stable** |
| MM 50j | **$16.96** | $16.96 | **stable** |
| Écart MM50 | **+0.83%** | +0.83% | **stable** |
| Volume (final) | **75.33M** | 73.98M | **+1.8%** |
| Volume vs 20j | **0.90×** | 0.90× | **stable** |
| Forward P/E | **20.94** | 20.94 | **stable** |
| Short interest | **14.71%** | 14.71% | **stable** |
| XLF momentum | **5.45/10** | 5.08/10 | **+0.37 pt** |
| Jours avant earnings | **35j** | 36j | **−1j** |

**Verdict global :** Snapshot matinal pré-ouverture US. Aucun nouveau close n'est disponible depuis le close final du 22/06 ($17.10). Les métriques techniques et fondamentales sont strictement inchangées. **La seule évolution significative est l'amélioration du momentum sectoriel XLF (+0.37 pt à 5.45/10),** qui renforce légèrement le contexte de soutien sectoriel. Le volume final a été micro-révisé à la hausse (+1.8%) sans changer la lecture (0.90×). [ALERTE DATA QUALITY] Les données options dans `latest.json` sont corrompues (Max Pain $5.00 aberrant, Put/Call et Call OI null) — valeurs historiques du 22/06 conservées. **Thèse confirmée.**

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Cours close | $17.10 | `latest.json` (close 22/06) |
| Open / High / Low | $17.59 / $18.06 / $17.07 | `latest.json` |
| Change % | −4.52% | `latest.json` |
| Volume | 75,334,700 | `latest.json` |
| Volume vs 20j | 0.90× (moy. 82,114,745) | Calcul agent |
| RSI 14j | 40.98 | `latest.json` |
| ATR 14j | $1.00 | `latest.json` |
| MM 50j | $16.96 | `latest.json` |
| Beta | 2.152 | `latest.json` |

**Niveaux clés :**
- Support immédiat : $17.07 (low 22/06)
- Support secondaire : $16.96 (MM50)
- Résistance : $17.59 (open 22/06)
- Stop-loss ATR (2×) : **$15.10**
- Take-profit ATR (3×) : **$20.10**

**Verdict timing :** Favorable — cours au-dessus de MM50 (+0.83%), RSI 40.98 en zone neutre-basse proche de la survente. Aucun nouveau signal technique depuis le close 22/06.

---

## 3. Bloc Fondamental

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $21.93B | `latest.json` |
| P/E (TTM) | 38.00 | `latest.json` |
| Forward P/E | 20.94 | `latest.json` |
| EV/Revenue | 5.19 | `latest.json` |
| P/B | 2.03 | `latest.json` |
| FMP Consensus PT | $25.41 (27 analysts) | `latest.json` |
| FMP Gross Margin | 75.1% | `latest.json` |

**Filtre Qualité :** 4/6 (Quality Partielle) — inchangé. Aucun nouvel élément fondamental.

---

## 4. Bloc Sentiment / Options / News

| Signal | Valeur | Source | Δ vs 21h UTC |
|--------|--------|--------|--------------|
| Consensus analystes (FMP) | $25.41 (27 analysts) | `latest.json` | inchangé |
| Put/Call ratio | 0.51 | Historique 22/06 | inchangé* |
| Max pain | $18.00 | Historique 22/06 | inchangé* |
| Call OI % | 66.4% | Historique 22/06 | inchangé* |
| Short interest | 14.71% | `latest.json` | stable |

*\* [ALERTE DATA QUALITY] Données options corrompues dans `latest.json` (Max Pain $5.00 aberrant, Put/Call null, Call OI null). Valeurs historiques du 22/06 conservées.*

**Verdict Sentiment :** Neutre légèrement haussier inchangé. Consensus PT $25.41 (+48.6% upside). Short interest 14.71% maintenu = setup asymétrique intact.

**News & Événements :**
- Aucune news structurante détectée.
- Aucun événement corporate (`data/events_latest.json` : 0 événements).
- Earnings Q2 FY2026 : **2026-07-28** (dans **35 jours**) — estimates EPS $0.10–$0.11, Rev $1.1B.

---

## 5. Scoring global

| Score | 2026-06-23 10h | 2026-06-22 21h | Δ |
|-------|---------------|----------------|---|
| Score Opportunité | **5.8/10** | 5.8/10 | stable |
| Score Catalyseur | **6.8/10** | 6.8/10 | stable |
| Score Valorisation | **5.5/10** | 5.5/10 | stable |
| Score Momentum | **5.0/10** | 5.0/10 | stable |
| Score Global | **58.3/100** | 58.3/100 | stable |
| Score Global ajusté | **63.3/100** | 63.3/100 | stable |
| Action | **ACHETER (Réduit)** | ACHETER (Réduit) | inchangé |
| Timing | **Favorable** | Favorable | inchangé |

**Source :** `data/recommandations_latest.json` (pipeline 2026-06-23 10:00 UTC).

---

## 6. Niveaux révisés

| Niveau | Valeur | Méthode |
|--------|--------|---------|
| Prix d'entrée suggéré | $17.10 | Close actuel |
| Stop-loss | **$15.10** | Cours − 2×ATR ($1.00) |
| Take-profit | **$20.10** | Cours + 3×ATR ($1.00) |
| Ratio R/R | **1.5×** | (TP − Cours) / (Cours − SL) |
| Sizing | **Réduit** | Score Global 60–74 (bord inférieur) |

**Niveaux inchangés** — aucun nouveau close depuis le 22/06.

---

## 7. Bloc Macro & Sectoriel

**Régime macro :** Unknown (`latest.json`).

**Sectoriel (Sector Rotation) :**
- XLF (Financials) : #3/11 sectors, momentum score **5.45/10** (+0.37 pt vs 5.08/10 le 22/06) — léger vent de poupe modéré atténué.
- SOFI classé Financial Services / Credit Services — alignement sectoriel neutre-légèrement amélioré.

**Exposition FX :**
- `fx_exposure_latest.json` : FX Impact Score 0.0, direction neutral, divergence aligned. Aucun headwind/tailwind.

**Géopolitique :**
- `geo_risk_latest.json` (2026-05-17) : SOFI non flaggé.

---

## 8. Bloc Quant & Risques

**Quant :**
- `quant_report_latest.json` (2026-05-17) : calibration insuffisante. Aucune alerte.

**Accounting :**
- `accounting_risk_latest.json` : fichier absent.

**Social Sentiment :**
- `social_sentiment_latest.json` (2026-06-23) : 0 mentions Reddit, sentiment score 0.0 (No data), pump detected : false.

**DRAFT_refresh :**
- Trigger ATR_SPIKE 5.85% (seuil 5.0%) détecté par le pipeline matinal — **archivé comme faux positif** (ATR absolu stable à $1.00, même motif que les 15–17/06 et 22/06).

---

## 9. Conclusion — Thèse confirmée

**La thèse reste confirmée.** Le snapshot matinal du 23/06 n'apporte aucun nouveau close ni signal technique. Le cours $17.10 maintient le reclaim MM50 ($16.96) avec un écart de +0.83%. Le RSI 40.98 reste en zone neutre-basse favorable à l'entrée patiente. L'ATR stable à $1.00 confirme une volatilité contenue.

**Amélioration marginale :** Le momentum sectoriel XLF est remonté de 5.08 à 5.45/10, atténuant le vent de poupe modéré observé hier. C'est un facteur de contexte positif mais non décisif.

**Point de vigilance résiduel :** Le reclaim MM50 reste très rétréci (+0.83%). Un close sous $16.96 sur la prochaine session invaliderait le breakout technique du 01/06 et justifierait un reclassement en ATTENDRE/SURVEILLER. Le pinning options vers Max Pain $18.00 (expiration 26/06) reste un facteur de résistance court terme.

**Catalyseurs forward :**
| Catalyst | Timeline | Probabilité | Impact |
|----------|----------|-------------|--------|
| Earnings Q2 FY2026 | 28 juillet 2026 (35j) | Haute | EPS $0.10–$0.11, Rev $1.1B |
| Décision Fed (taux) | Juin–Juillet 2026 | Moyenne | Impact NIM et lending |
| Short squeeze setup | Continu | Moyenne | SI 14.71% = setup asymétrique |

**Risques clés :**
1. **Retour sous MM50** — un close sous $16.96 invaliderait le breakout.
2. **Earnings Q2** — 35j. Beta 2.152 amplifie tout gap post-earnings.
3. **Pinning options** — Max Pain $18.00, expiration 26/06.
4. **Données options corrompues** dans `latest.json` — surveiller correction sur prochains snapshots.

---

*Généré automatiquement — données source : `data/latest.json` (2026-06-23T10:00 UTC), `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/social_sentiment_latest.json`, `data/quant_report_latest.json`.*

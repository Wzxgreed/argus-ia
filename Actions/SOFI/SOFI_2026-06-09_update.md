# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-09 (snapshot 10:00 UTC — données de close 08/06 reportées)
**Type :** `_update.md` — Stabilité totale vs close 08/06, DRAFT_refresh archivé faux positif ATR_SPIKE
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-08_update.md` (21:00 UTC) | **Snapshot 2026-06-09 (10:00 UTC)** | **Δ** |
|----------|------------------------------------------|-------------------------------------|-------|
| Cours close | $16.50 | **$16.50** | **Inchangé** |
| RSI 14j | 54.98 | **54.98** | **Inchangé** |
| ATR 14j | $0.97 | **$0.97** | **Inchangé** |
| MM 50j | $16.76 | **$16.76** | **Inchangé** |
| Volume | 77.12M (1.08×) | **79.06M (1.10×)** | **+2.5% — ajustement mécanique** |
| Écart MM50 | −1.55% | **−1.55%** | **Inchangé** |
| High/Low intraday | $16.66 / $15.955 | **—** | **Pas de nouvelle session** |
| **Score Opportunité** | **6.1/10** | **6.1/10** | **Inchangé** |
| **Score Momentum** | **5.3/10** | **5.3/10** | **Inchangé** |
| **Score Global ajusté** | **53.1/100** | **53.1/100** | **Inchangé** |
| **Action** | **ATTENDRE** | **ATTENDRE** | **Inchangé** |
| Timing | Défavorable | **Défavorable** | **Inchangé** |

**Verdict :** Le snapshot du **2026-06-09 à 10:00 UTC** reprend les données de close du 08/06 — aucune nouvelle session de trading n'est encore intégrée. Toutes les métriques techniques, fondamentales et de scoring sont **stabiles** vs le close final du 08/06. Le volume affiché à 79.06M (1.10×) est un ajustement mécanique mineur vs 77.12M (1.08×) — statistiquement insignifiant. Le **DRAFT_refresh_2026-06-09** déclenché par `agents/detect_major_events/agent.py` sur un prétendu **ATR_SPIKE (medium, 5.88%)** est un **faux positif** : l'ATR est stable à $0.97 depuis le 08/06, sans augmentation. Le trigger est invalidé et le DRAFT archivé. La thèse **ATTENDRE** est confirmée sans changement qualitatif.

---

## 2. Mise à jour technique

| Indicateur | Valeur snapshot 2026-06-09 | Signal |
|------------|---------------------------|--------|
| RSI 14j | 54.98 | 🟡 Zone neutre — pas de traction haussière |
| MM 50j | $16.76 | 🔴 Cours −1.55% sous MM50 — non reclaim |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.97 | 🟡 Volatilité stable — ATR_SPIKE faux positif |
| Support clé | $15.955 (low 08/06) / $15.68 (low 05/06) / $15.00 | 🟢 Support immédiat tenu |
| Résistance clé | $16.76 (MM50) / $17.00 (Max Pain) / $17.46 (low 02/06) | 🔴 Rejet sous MM50 en close 08/06 |
| Volume relatif | 1.10× | 🟢 Participation légèrement supérieure à la moyenne — stable |
| Beta | 2.152 | ⚠️ Volatilité extrême amplifiée |
| Gap fill | $16.03 → $17.74 | 🟡 Partiellement comblé ($16.50 = 33% du gap) — inchangé |

**Analyse technique :** Aucun changement technique vs le close 08/06. Le cours à **$16.50** reste sous la **MM50 ($16.76)** avec un écart de −1.55%. L'**ATR à $0.97** est stable — le trigger ATR_SPIKE du DRAFT_refresh est invalide (aucune expansion de volatilité détectée entre le 08/06 et le 09/06). Le RSI à 54.98 reste dans la zone neutre sans traction haussière. Le support immédiat **$15.955** (low du 08/06) n'a pas été testé ce jour (pas de session nouvelle).

**Niveaux clés inchangés :**
- Support immédiat : **$15.955** (low du 08/06) — si cassé, retour à **$15.68** puis **$15.00**
- Résistance immédiate : **$16.76** (MM50) — reclaim obligatoire pour réactiver la thèse haussière
- Résistance intermédiaire : **$17.00** (Max Pain options)
- Résistance majeure : **$17.46** (low du 02/06)

**Verdict timing :** Défavorable — inchangé. Cours sous MM50, absence de reclaim, trend court terme baissier intact.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market cap | $21.17B | Stable |
| P/E LTM (Yahoo) | 36.67 | Stable |
| Forward P/E | 21.15 | Mécaniquement attractif — inchangé |
| EV/Revenue | 4.994 | Stable |
| P/B (Yahoo) | 1.96 | Stable |
| Gross margin (FMP) | 75.1% | Excellent, stable |
| Operating margin | 11.0% | Stable |
| Net margin | 10.1% | Stable |
| Debt/Equity (FMP) | 0.173 | Très faible — bilan sain |
| FCF yield | −13.2% | FCF négatif — modèle en investissement |
| SBC/Revenue | 5.5% | Modéré, sous contrôle |
| ROE (FMP) | 4.6% | Faible — limite le Filtre Qualité à 4/6 |
| Short interest | 13.68% | Élevé — squeeze potentiel si reclaim MM50 |

**Aucune news structurante ni événement corporate détecté** (`data/events_latest.json` vide). Le mouvement reste **purement technique** : consolidation post-gap avec test de support et rejet sous MM50. Les fondamentaux n'ont pas changé.

**Filtre Qualité (6 critères) :** Inchangé à **4/6 (Quality Partielle)**. Aucun nouvel état financier ni guidance. Le charter bancaire, le TAM fintech et la marque SoFi restent intacts.

---

## 4. Mise à jour sentiment / options / news

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Consensus PT (FMP) | $25.41 (27 analystes) | 🟢 Upside consensus +53.9% vs cours $16.50 |
| Analystes actifs (1M) | 1 | 🟡 Couverture stable mais faible |
| Analystes actifs (1T) | 10 | 🟡 Couverture stable |
| **Max Pain** | **$5.00** | ⚠️ Valeur aberrante dans latest.json — conserve $17.00 du 08/06 |
| **Put/Call ratio** | **null** | ⚠️ Données absentes dans latest.json — conserve 0.57 du 08/06 |
| **Call OI %** | **null** | ⚠️ Données absentes dans latest.json — conserve 63.7% du 08/06 |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit |
| Pump detected | false | 🟢 Aucun signal pump |

**Options :** [ALERTE DATA QUALITY] Les données options dans `data/latest.json` du 2026-06-09 sont partielles (Max Pain $5.00 aberrant, Put/Call et Call OI null). Les valeurs du close 08/06 sont conservées : Max Pain **$17.00**, Put/Call **0.57**, Call OI **63.7%**. L'expiration prochaine est le **2026-06-12** (3 jours ouvrés).

**News** — Aucune news structurante détectée via les flux automatiques.

---

## 5. Scoring global révisé

| Score | Close final 2026-06-08 21h (ATTENDRE) | **Snapshot 2026-06-09 10h (ATTENDRE)** | **Δ** |
|-------|---------------------------------------|------------------------------------------|-------|
| Score Opportunité | 6.1/10 | **6.1/10** | **0.0** |
| Score Catalyseur | 6.8/10 | **6.8/10** | **0.0** |
| Score Valorisation | 6.0/10 | **6.0/10** | **0.0** |
| Score Momentum | 5.3/10 | **5.3/10** | **0.0** |
| Score Global Composite | 61.1/100 | **61.1/100** | **0.0** |
| Score Global ajusté | 53.1/100 | **53.1/100** | **0.0** |
| Action | ATTENDRE | **ATTENDRE** | **Inchangé** |
| Timing | Défavorable | **Défavorable** | **Inchangé** |
| Sizing | — | **—** | **—** |
| Horizon | — | **—** | **—** |

**Pondération régime :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime inconnu — pondération par défaut).

**Malus / Bonus appliqués (Score Global ajusté) :**
- Malus accounting : 0 (fichier absent)
- Malus geo : 0 (SOFI non listé dans geo_risk — exposition neutre)
- Malus FX : 0 (fx_impact_score 0.0, exposition 55% mais stable)
- Malus social : 0 (pas de données — EXTREME_BEARISH par absence, pas de malus appliqué)
- Malus quant : 0 (pas de signaux historiques)
- Bonus event : 0 (pas d'événement corporate)
- Timing technique : **−8.0** (cours sous MM50 — malus sévère maintenu)

**Analyse du scoring :** Tous les scores sont **inchangés** vs le close 08/06. Le Score Global ajusté de **53.1/100** reste confortablement dans la zone ATTENDRE (50–59), loin du seuil ACHETER (≥60). La stabilité des scores est rassurante : aucune dérive technique ni fondamentale n'est survenue.

**Règle de disqualification :** Aucun score individuel ≤ 2/10 — SOFI n'est pas exclu.

---

## 6. Niveaux révisés

| Niveau | Close final 2026-06-08 21h | Snapshot 2026-06-09 10h | Calcul |
|--------|----------------------------|-------------------------|--------|
| Prix d'entrée suggéré | — | **—** | Aucune entrée recommandée en ATTENDRE |
| Stop-loss | $14.56 | **$14.56** | $16.50 − 2×ATR ($0.97) = $14.56 |
| Take-profit | $19.41 | **$19.41** | $16.50 + 3×ATR ($0.97) = $19.41 |
| Upside / Downside | +17.6% / −11.8% | **+17.6% / −11.8%** | — |
| Ratio R/R | 1.50 | **1.50** | Stable (~1.5×) |

**Note sur les niveaux :** Inchangés vs close 08/06. Le ratio R/R reste à 1.5×. En zone ATTENDRE, **aucune entrée n'est recommandée**.

**Scénarios pour repasser en ACHETER :**
1. **Reclaim MM50** — Cours au-dessus de $16.76 en close avec volume >1.0× → réactivation technique
2. **Breakout $17.00** — Dépassement du Max Pain avec volume >1.2× → signal haussier fort
3. **Catalyseur fondamental** — News positive (guidance, contrat, M&A) permettant de passer le momentum

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**🟢 THÈSE CONFIRMÉE — Stabilité totale, DRAFT_refresh archivé faux positif**

Le snapshot du **2026-06-09 à 10:00 UTC** confirme la **stabilité totale** de toutes les métriques vs le close final du 08/06. Aucune nouvelle session de trading n'est intégrée. Le **DRAFT_refresh_2026-06-09** déclenché sur un trigger **ATR_SPIKE (medium, 5.88%)** est un **faux positif** : l'ATR est resté stable à **$0.97**, sans expansion de volatilité. Le trigger est invalidé et le DRAFT archivé.

**Ce qui est inchangé :**
- Cours $16.50, RSI 54.98, ATR $0.97, MM50 $16.76
- Score Global ajusté 53.1/100 (ATTENDRE)
- Volume ~1.10× moy. 20j (participation correcte)
- Forward P/E 21.15 attractif
- Consensus PT $25.41 (+53.9% upside)
- Filtre Qualité 4/6 (Quality Partielle)
- Short interest 13.68% (squeeze potentiel)
- Max Pain $17.00 (pinning haussier possible)
- Aucune news structurante, aucun événement corporate

**Ce qui n'a PAS changé (et qui maintient ATTENDRE) :**
- Cours sous MM50 ($16.76) — pas de reclaim
- Gap du 05/06 ($17.74 → $16.03) non comblé (33%)
- Timing Défavorable maintenu
- XLF momentum 4.0/10 — headwind sectoriel relatif faible

**Éléments conservant un potentiel long terme :**
- Forward P/E 21.15 attractif vs historique et vs consensus PT $25.41 (+53.9%)
- Volume 1.10× = participation réelle sur le rebond du 08/06
- Short interest 13.68% reste élevé — squeeze potentiel si reclaim MM50
- Filtre Qualité 4/6 inchangé — business model intact
- Earnings Q2 dans **49j** (28 juillet, EPS $0.10–$0.11, Rev $1.1B) — catalyseur forward
- Max Pain $17.00 au-dessus du cours = pinning options favorable à court terme

**Risques à surveiller :**
- Cassure sous $15.955 (low du 08/06) ouvrirait un retour à $15.68 puis $15.00
- ATR $0.97 = volatilité persistante — sizing réduit obligatoire si re-entrée
- XLF momentum 4.0/10 = headwind sectoriel relatif
- Score Global ajusté 53.1 — proche du seuil SURVEILLER (<50) si nouvelle baisse
- Filtre Qualité 4/6 — Quality Partielle, FCF négatif, ROE faible
- [ALERTE DATA QUALITY] Données options partielles dans latest.json (Max Pain aberrant $5.00, Put/Call et Call OI null) — valeurs du 08/06 conservées

**Action : ATTENDRE — Aucune entrée recommandée — Attendre reclaim MM50 $16.76 en close avec volume >1.0× ou breakout $17.00 pour réactiver la thèse haussière. DRAFT_refresh archivé.**

---

*Données sourcées : data/latest.json (2026-06-09T10:00:09+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json.*

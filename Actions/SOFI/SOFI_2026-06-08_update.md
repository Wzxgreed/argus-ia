# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-08 (snapshot 17:00 UTC — session US du 08/06)
**Type :** `_update.md` — Rebound +3.56% post-gap, reclassement SURVEILLER → ATTENDRE
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-08_update.md` (13:00 UTC) | **Snapshot 2026-06-08 (17:00 UTC)** | **Δ** |
|----------|-----------------------------------------|-------------------------------------|-------|
| Cours close | $16.03 (close 05/06) | **$16.60** | **+3.56%** |
| RSI 14j | 52.78 | **55.54** | **+2.76 pts** |
| ATR 14j | $0.99 | **$0.97** | **−$0.02 (−2.0%)** |
| MM 50j | $16.75 | **$16.76** | **+$0.01** |
| Volume | 81.21M (1.15×) | **43.33M (0.62×)** | **−47.2%** |
| Écart MM50 | −0.43% | **−0.95%** | **Écart élargi** |
| **Score Opportunité** | **5.8/10** | **6.2/10** | **+0.4 pt** |
| **Score Momentum** | **4.0/10** | **5.5/10** | **+1.5 pts** |
| **Score Global ajusté** | **49.8/100** | **53.6/100** | **+3.8 pts** |
| **Action** | **SURVEILLER** | **ATTENDRE** | **🟢 Reclassement** |
| Timing | Défavorable | **Défavorable** | **Inchangé** |

**Verdict :** La session du 08/06 enregistre un rebond technique de **+3.56%** à **$16.60** après le gap baissier de **−6.53%** du 05/06 ($17.74 → $16.03). Le rebound est mécanique et salvateur : il évite une cassure immédiate du support $15.68 et ramène le RSI dans la zone neutre supérieure (55.54). Cependant, le volume de **43.33M (0.62× moy. 20j)** est faible — **pas de conviction institutionnelle** sur ce rebond. Le cours reste sous la MM50 ($16.76) avec un écart de −0.95%. Le **Score Global ajusté remonte de 49.8 à 53.6/100**, juste au-dessus du seuil ATTENDRE (50–59). Le reclassement **SURVEILLER → ATTENDRE** est marginal et fragile.

**[RÉSOLU] Alerte data quality** : le flag `stale_price_history` du `quality_report_latest.json` (close identique sur 4 jours consécutifs jusqu'au 05/06) est levé par la mutation de prix à $16.60.

---

## 2. Mise à jour technique

| Indicateur | Valeur 2026-06-08 (17h) | Signal |
|------------|-------------------------|--------|
| RSI 14j | 55.54 | 🟡 Zone neutre — amélioration mais pas de traction haussière |
| MM 50j | $16.76 | 🔴 Cours −0.95% sous MM50 — non reclaim |
| MM 200j | [UNSOURCED] | — |
| ATR 14j | $0.97 | 🟡 Volatilité stable, légère compression vs 0.99 |
| Support clé | $15.955 (low du 08/06) / $15.68 (low 05/06) / $15.00 | 🟢 Support immédiat tenu |
| Résistance clé | $16.76 (MM50) / $17.00 (Max Pain) / $17.46 (low 02/06) | 🔴 MM50 reste résistance dynamique |
| Volume relatif | 0.62× | 🔴 Rebound sur volume faible = conviction limitée |
| Beta | 2.152 | ⚠️ Volatilité extrême amplifiée |
| Gap fill | $16.03 → $17.74 | 🟡 Partiellement comblé ($16.60 = 38% du gap) |

**Analyse technique :** Le rebound du 08/06 s'est effectué dans un range intraday de **$15.955–$16.66**, avec un close à **$16.60** proche du high. Cette structure de bougie est positive (close près du high), mais le **volume de 43.33M (0.62×)** est le plus faible depuis le 25/05 (0.59× intraday). À comparer avec le volume du gap baissier du 05/06 : **81.21M (1.15×)**. La distribution institutionnelle du 05/06 n'a pas été invalidée par un rebond acheteur massif — il s'agit plutôt d'un **rebound technique mécanique** sur support ($15.68) dans un contexte de faible participation.

Le **RSI à 55.54** est en nette amélioration (+2.76 pts) mais reste loin de la zone surachat (>70) qui avait prévalu le 01/06 (69.63). Il n'y a pas de divergence haussière visible. L'**ATR à $0.97** se compresse légèrement (−2.0%), signe que la volatilité post-gap s'atténue.

**Niveaux clés révisés :**
- Support immédiat : **$15.955** (low du 08/06) — si cassé, retour à **$15.68** puis **$15.00**
- Résistance immédiate : **$16.76** (MM50) — reclaim obligatoire pour réactiver la thèse haussière
- Résistance intermédiaire : **$17.00** (Max Pain options) — pinning probable si dépassement
- Résistance majeure : **$17.46** (low du 02/06) — comblement du gap à 100%

**Verdict timing :** Défavorable — cours sous MM50, rebound sur volume faible, trend court terme baissier intact.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market cap | $21.30B | +3.56% mécanique avec le cours |
| P/E LTM (Yahoo) | 36.9 | Stable |
| Forward P/E | 21.28 | Mécaniquement attractif |
| EV/Revenue | 4.839 | Stable |
| P/B (Yahoo) | 1.97 | Stable |
| Gross margin (FMP) | 75.1% | Excellent, stable |
| Operating margin | 11.0% | Stable |
| Net margin | 10.1% | Stable |
| Debt/Equity (FMP) | 0.173 | Très faible — bilan sain |
| FCF yield | −13.2% | FCF négatif — modèle en investissement |
| SBC/Revenue | 5.5% | Modéré, sous contrôle |
| ROE (FMP) | 4.6% | Faible — limite le Filtre Qualité à 4/6 |

**Aucune news structurante ni événement corporate détecté** (`data/events_latest.json` vide, `data/news_latest.json` vide). Le mouvement reste **purement technique** : rebond mécanique post-gap sur support. Les fondamentaux n'ont pas changé.

**Filtre Qualité (6 critères) :** Inchangé à **4/6 (Quality Partielle)**. Aucun nouvel état financier ni guidance. Le charter bancaire, le TAM fintech et la marque SoFi restent intacts.

**Short interest 13.68%** (inchangé) — élevé mais le potentiel de squeeze nécessite un reclaim de MM50 avec volume pour déclencher un short covering massif.

---

## 4. Mise à jour sentiment / options / news

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Consensus PT (FMP) | $25.41 (27 analystes) | 🟢 Upside consensus +53.1% vs cours $16.60 |
| Analystes actifs (1M) | 1 | 🟡 Couverture stable mais faible |
| Analystes actifs (1T) | 10 | 🟡 Couverture stable |
| **Max Pain** | **$17.00** | 🟢 Cohérent — au-dessus du cours, pinning haussier possible |
| **Put/Call ratio** | **0.57** | 🟡 Inchangé — légèrement haussier |
| **Call OI %** | **63.7%** | 🟡 Inchangé — majorité calls |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit |
| Pump detected | false | 🟢 Aucun signal pump |

**Options :** Aucun changement vs snapshot 13:00 UTC. Le Max Pain à **$17.00** reste au-dessus du cours ($16.60), créant une pression de pinning favorable à très court terme. L'expiration prochaine est le **2026-06-12** (4 jours ouvrés). Le Put/Call 0.57 et le Call OI 63.7% sont stables.

**News** — Aucune news structurante détectée via les flux automatiques.

---

## 5. Scoring global révisé

| Score | Snapshot 2026-06-03 (ACHETER) | Snapshot 2026-06-08 13h (SURVEILLER) | **Snapshot 2026-06-08 17h (ATTENDRE)** | **Δ vs 13h** |
|-------|-------------------------------|-------------------------------------|----------------------------------------|--------------|
| Score Opportunité | 6.1/10 | 5.8/10 | **6.2/10** | **+0.4** |
| Score Catalyseur | 6.8/10 | 6.8/10 | **6.8/10** | 0.0 |
| Score Valorisation | 5.5/10 | 6.0/10 | **6.0/10** | 0.0 |
| Score Momentum | 6.0/10 | 4.0/10 | **5.5/10** | **+1.5 pts** |
| Score Global Composite | 60.8/100 | 57.8/100 | **61.6/100** | **+3.8 pts** |
| Score Global ajusté | 65.8/100 | 49.8/100 | **53.6/100** | **+3.8 pts** |
| Action | ACHETER | SURVEILLER | **ATTENDRE** | **🟢 Reclassement** |
| Timing | Favorable | Défavorable | **Défavorable** | **Inchangé** |
| Sizing | Réduit | — | **—** | **—** |
| Horizon | 1–3 mois | — | **—** | **—** |

**Pondération régime :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime inconnu — pondération par défaut).

**Malus / Bonus appliqués (Score Global ajusté) :**
- Malus accounting : 0 (fichier absent)
- Malus geo : 0 (SOFI non listé dans geo_risk — exposition neutre)
- Malus FX : 0 (fx_impact_score 0.0, exposition 55% mais stable)
- Malus social : 0 (pas de données — EXTREME_BEARISH par absence, pas de malus appliqué)
- Malus quant : 0 (pas de signaux historiques)
- Bonus event : 0 (pas d'événement corporate)
- Timing technique : **−8.0** (cours sous MM50 + rebound sur volume faible — malus sévère maintenu)

**Analyse du reclassement :** Le rebond de +3.56% améliore mécaniquement le Score Momentum de 4.0 à 5.5/10 (retour à neutre). Le Score Valorisation reste stable à 6.0/10 (Forward P/E 21.28 attractif). Le résultat est un **Score Global ajusté de 53.6/100**, juste au-dessus du seuil ATTENDRE (50–59). Ce reclassement est **marginal et fragile** : une baisse de −3.6 pts ramènerait SOFI en zone SURVEILLER.

**Règle de disqualification :** Aucun score individuel ≤ 2/10 — SOFI n'est pas exclu.

---

## 6. Niveaux révisés

| Niveau | Snapshot 2026-06-08 13h | Snapshot 2026-06-08 17h | Calcul |
|--------|-------------------------|-------------------------|--------|
| Prix d'entrée suggéré | — | **—** | Aucune entrée recommandée en ATTENDRE |
| Stop-loss | $14.05 | **$14.66** | $16.60 − 2×ATR ($0.97) = $14.66 |
| Take-profit | $19.00 | **$19.51** | $16.60 + 3×ATR ($0.97) = $19.51 |
| Upside / Downside | +18.5% / −12.4% | **+17.5% / −11.7%** | — |
| Ratio R/R | 1.50 | **1.50** | Stable (~1.5×) |

**Note sur les niveaux :** Les niveaux SL/TP sont recalculés sur la base du cours ($16.60) et de l'ATR ($0.97). Le ratio R/R reste à 1.5×. En zone ATTENDRE, **aucune entrée n'est recommandée**, mais la posture est moins défensive que SURVEILLER.

**Scénarios pour repasser en ACHETER :**
1. **Reclaim MM50** — Cours au-dessus de $16.76 en close avec volume >1.0× → réactivation technique
2. **Breakout $17.00** — Dépassement du Max Pain avec volume >1.2× → signal haussier fort
3. **Catalyseur fondamental** — News positive (guidance, contrat, M&A) permettant de passer le momentum

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**🟡 THÈSE LÉGÈREMENT AMÉLIORÉE — Reclassement SURVEILLER → ATTENDRE, mais trend baissier court terme intact**

Le rebond de **+3.56%** à $16.60 du 08/06 est un soulagement technique après le gap baissier de −6.53% du 05/06, mais il ne constitue **pas une confirmation haussière**. Le volume de 0.62× est trop faible pour signaler un retour d'acheteurs institutionnels. Le cours reste sous la MM50 ($16.76), et le trend court terme (gap du 01/06 à $18.58 → pullback à $17.74 → gap baissier à $16.03 → rebond à $16.60) reste baissier.

**Ce qui a changé :**
- Cours +3.56% à $16.60 — rebond mécanique sur support
- RSI remonté à 55.54 — zone neutre supérieure
- Score Momentum remonté de 4.0 à 5.5/10 (neutre)
- Score Global ajusté remonté de 49.8 à 53.6/100 (ATTENDRE)
- Action reclasseée SURVEILLER → ATTENDRE

**Ce qui n'a PAS changé :**
- Cours sous MM50 ($16.76) — trend baissier intact
- Volume faible (0.62×) — pas de conviction institutionnelle
- Aucune news structurante ni événement corporate
- Filtre Qualité 4/6 inchangé
- Forward P/E 21.28 attractif mais non suffisant seul
- Timing Défavorable maintenu

**Éléments invalidant la thèse haussière (ACHETER) :**
- Cours sous MM50 — pas de reclaim
- Rebound sur volume 0.62× = pas de conviction
- Gap du 05/06 ($17.74 → $16.03) non comblé (seulement 38%)
- Score Global ajusté 53.6 — loin du seuil ACHETER (≥60)
- XLF momentum 3.99/10 — headwind sectoriel relatif faible

**Éléments conservant un potentiel long terme :**
- Forward P/E 21.28 attractif vs historique et vs consensus PT $25.41 (+53.1%)
- Short interest 13.68% reste élevé — squeeze potentiel si reclaim MM50
- Filtre Qualité 4/6 inchangé — business model intact
- Earnings Q2 dans 50j (28 juillet, EPS $0.10–$0.11) — catalyseur forward
- Max Pain $17.00 au-dessus du cours = pinning options favorable à court terme

**Risques à surveiller :**
- Cassure sous $15.955 (low du 08/06) ouvrirait un retour à $15.68 puis $15.00
- ATR $0.97 = volatilité persistante — sizing réduit obligatoire si re-entrée
- XLF momentum 3.99/10 = headwind sectoriel relatif (top3 par exclusion)
- Score Global ajusté 53.6 — proche du seuil SURVEILLER (< 50) si nouvelle baisse
- Filtre Qualité 4/6 — Quality Partielle, FCF négatif, ROE faible

**Action : ATTENDRE — Aucune entrée recommandée — Attendre reclaim MM50 $16.76 avec volume >1.0× ou breakout $17.00 pour réactiver la thèse haussière**

---

*Données sourcées : data/latest.json (2026-06-08T17:00:08+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json.*

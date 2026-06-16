# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-16 (snapshot 10:00 UTC — pré-ouverture US, données identiques close 15/06)
**Type :** `_update.md` — Stabilité mécanique pré-session, DRAFT_refresh faux positif traité
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-15_update.md` (21:00 UTC) | **Snapshot 2026-06-16 (10:00 UTC)** | **Δ** |
|----------|----------------------------------------|-------------------------------------|-------|
| Cours close | $17.13 | **$17.13** | **Inchangé** |
| RSI 14j | 56.66 | **56.66** | **Inchangé** |
| ATR 14j | $1.05 | **$1.05** | **Inchangé** |
| MM 50j | $16.86 | **$16.86** | **Inchangé** |
| Écart MM50 | +1.60% | **+1.60%** | **Reclaim maintenu** |
| Volume | 75.98M (1.03×) | **76.40M (1.03×)** | **Ajustement mécanique** |
| Volume vs moy. 20j | +3% | **+3%** | **Stable** |
| Short interest | 14.71% | **14.71%** | **Stable** |
| Max Pain | $1.00 [ALERTE] | **$1.00** | **[ALERTE PERSISTANTE]** |
| Put/Call ratio | 0.42 | **0.42** [conservé] | **Données partielles JSON** |
| Call OI % | 70.5% | **70.5%** [conservé] | **Données partielles JSON** |
| **Score Opportunité** | **6.5/10** | **6.5/10** | **Inchangé** |
| **Score Catalyseur** | **6.8/10** | **6.8/10** | **Inchangé** |
| **Score Valorisation** | **5.5/10** | **5.5/10** | **Inchangé** |
| **Score Momentum** | **7.5/10** | **7.5/10** | **Inchangé** |
| **Score Global ajusté** | **69.5/100** | **69.5/100** | **Inchangé** |
| **Action** | **ACHETER (Réduit)** | **ACHETER (Réduit)** | **Confirmé** |
| Timing | Favorable | **Favorable** | **Stable** |

**Verdict :** Le snapshot **2026-06-16 à 10:00 UTC** correspond à la **pré-ouverture US** (6:00 AM ET, marché fermé). Les données techniques sont **strictement identiques** au close final du 2026-06-15 21:00 UTC : cours $17.13, RSI 56.66, ATR $1.05, MM50 $16.86. Le volume est ajusté mécaniquement de 75.98M à **76.40M** (même ratio 1.03× la moy. 20j). Le **DRAFT_refresh trigger ATR_SPIKE 6.13%** est de nouveau détecté — il s'agit du **même faux positif que le 2026-06-15** (ATR stable à $1.05, compression). Aucune nouvelle information ne modifie la thèse.

---

## 2. Mise à jour technique

| Indicateur | Valeur snapshot 10:00 UTC | Signal |
|------------|---------------------------|--------|
| RSI 14j | 56.66 | 🟡 Zone neutre haussière |
| MM 50j | $16.86 | 🟢 Cours $17.13 = +1.60% au-dessus — reclaim validé |
| MM 200j | null | ⚪ [DONNÉES PARTIELLES] |
| ATR 14j | $1.05 | 🟢 Compression — améliore R/R |
| Support clé | $17.01 (low 15/06) / $16.86 (MM50) | 🟢 Support immédiat = MM50 |
| Résistance clé | $17.43 (high 15/06) / $17.00 (Max Pain historique) | 🟡 Resistance intraday testée |
| Volume relatif | **1.03×** | 🟢 Légèrement supérieur à la moyenne — stable |
| Beta | 2.152 | ⚠️ Volatilité amplifiée |
| Short interest | 14.71% | 🔴 Élevé — squeeze potentiel intact |

**Analyse technique :** Aucun changement par rapport au close final 15/06. Le cours reste à **$17.13**, au-dessus de la MM50 ($16.86) pour le deuxième jour consécutif. Le RSI à **56.66** reste en zone neutre haussière (pas de surachat). L'**ATR $1.05** est stable en compression.

**Options :**
- Max Pain : **$1.00** — [ALERTE DATA QUALITY] persistante (historique $17.00 conservé)
- Put/Call : **0.42** — conservé du snapshot 15/06 (données `null` dans latest.json)
- Call OI : **70.5%** — conservé du snapshot 15/06 (données `null` dans latest.json)
- Expiration prochaine : **2026-06-18** (2 jours ouvrés restants)

**Niveaux (ATR = $1.05) :**
- Support immédiat : **$16.86** (MM50) — doit tenir en close pour confirmer le reclaim
- Support intermédiaire : **$16.23** (low du matin 15/06)
- Support majeur : **$15.651** (low du 09/06)
- Résistance immédiate : **$17.43** (high du 15/06)
- Résistance intermédiaire : **$17.00** (Max Pain historique)
- Résistance majeure : **$18.22** (high du 01/06, gap)

**Verdict timing :** Favorable — reclaim MM50 maintenu, données pré-ouverture sans surprise.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market cap | $21.97B | Stable |
| P/E LTM (Yahoo) | 38.07 | Stable |
| Forward P/E | 21.95 | Stable — mécaniquement attractif |
| EV/Revenue | 5.2 | Stable |
| P/B (Yahoo) | 2.03 | Stable |
| Gross margin (FMP) | 75.1% | Excellent, stable |
| Operating margin | 11.0% | Stable |
| Net margin | 10.1% | Stable |
| Debt/Equity (FMP) | 0.184 | Très faible — bilan sain |
| FCF yield | −13.2% | FCF négatif — modèle en investissement |
| SBC/Revenue | 5.49% | Modéré, stable |
| ROE (FMP key metrics) | 4.59% | Faible — limite Filtre Qualité à 4/6 |

**Aucune news structurante ni événement corporate détecté** (`data/events_latest.json` vide pour SOFI). Le mouvement reste **purement technique/stabile**. Les fondamentaux n'ont pas changé.

**Filtre Qualité (6 critères) :** Inchangé à **4/6 (Quality Partielle)**. Aucun nouvel état financier ni guidance.

---

## 4. Mise à jour sentiment / options / news

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Consensus PT (FMP) | $25.41 (27 analystes) | 🟢 Upside consensus +48.3% vs cours $17.13 |
| Analystes actifs (1M) | 0 | 🟡 Aucune couverture récente |
| Analystes actifs (1T) | 10 | 🟡 Couverture stable |
| **Short interest** | **14.71%** | 🔴 Élevé — squeeze potentiel renforcé |
| **Max Pain** | **$1.00** [ALERTE] | 🔴 Données aberrantes — historique $17.00 conservé |
| **Put/Call ratio** | **0.42** [conservé] | 🟢 Stable — sentiment légèrement haussier |
| **Call OI %** | **70.5%** [conservé] | 🟢 Stable — repositionnement haussier confirmé |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit |
| Pump detected | false | 🟢 Aucun signal pump |

**Short interest :** Stable à **14.71%**. Le setup asymétrique squeeze/pression vendeuse est inchangé.

**Options :** Données partielles dans `data/latest.json` (Put/Call et Call OI `null`). Valeurs du snapshot 15/06 conservées : Put/Call **0.42** et Call OI **70.5%** confirment le repositionnement haussier à très court terme. Max Pain **$1.00** aberrant persistant.

**News** — Aucune news structurante détectée via les flux automatiques.

---

## 5. Scoring global révisé

| Score | Snapshot 15/06 21:00 UTC | **Snapshot 16/06 10:00 UTC** | **Δ** |
|-------|--------------------------|------------------------------|-------|
| Score Opportunité | 6.5/10 | **6.5/10** | **Inchangé** |
| Score Catalyseur | 6.8/10 | **6.8/10** | **Inchangé** |
| Score Valorisation | 5.5/10 | **5.5/10** | **Inchangé** |
| Score Momentum | 7.5/10 | **7.5/10** | **Inchangé** |
| Score Global Composite | 64.5/100 | **64.5/100** | **Inchangé** |
| Score Global ajusté | 69.5/100 | **69.5/100** | **Inchangé** |
| Action | ACHETER (Réduit) | **ACHETER (Réduit)** | **Confirmé** |
| Timing | Favorable | **Favorable** | **Stable** |
| Sizing | Réduit | **Réduit** | **Inchangé** |
| Horizon | 1–3 mois | **1–3 mois** | **Inchangé** |

**Pondération régime :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime Unknown — pondération par défaut).

**Malus / Bonus appliqués (Score Global ajusté) :**
- Malus accounting : 0 (fichier absent)
- Malus geo : 0 (SOFI non listé dans geo_risk — exposition neutre)
- Malus FX : 0 (fx_impact_score 0.0, exposition 55% mais stable)
- Malus social : 0 (pas de données — pas de malus appliqué)
- Malus quant : 0 (pas de signaux historiques)
- Bonus event : 0 (pas d'événement corporate)
- Timing technique : **+5.0** (cours au-dessus de MM50, reclaim maintenu)
- Sector rotation : XLF non listé dans `data/sector_rotation_latest.json` — pas de malus/bonus sectoriel applicable aujourd'hui

**Analyse du scoring :** Les scores restent **strictement inchangés** par rapport au snapshot 15/06 21:00 UTC. Le snapshot 16/06 étant pré-ouverture US, aucune nouvelle donnée de prix n'est disponible. La thèse **ACHETER (Réduit)** est maintenue.

**Règle de disqualification :** Aucun score individuel ≤ 2/10 — SOFI n'est pas exclu.

---

## 6. Niveaux révisés

| Niveau | Snapshot 15/06 21:00 UTC | Snapshot 16/06 10:00 UTC | Calcul |
|--------|--------------------------|--------------------------|--------|
| Prix d'entrée suggéré | $17.13 | **$17.13** | Entrée au close |
| Stop-loss | $15.03 | **$15.03** | $17.13 − 2×ATR ($1.05) = $15.03 |
| Take-profit | $20.28 | **$20.28** | $17.13 + 3×ATR ($1.05) = $20.28 |
| Upside / Downside | +18.4% / −12.3% | **+18.4% / −12.3%** | — |
| Ratio R/R | 1.50 | **1.50** | Stable (~1.5×) |

**Scénarios pour confirmer le reclaim :**
1. **Hold MM50 en close aujourd'hui (16/06)** — Cours au-dessus de $16.86 avec volume >0.8× → validation technique
2. **Breakout $17.43** — Dépassement du high du 15/06 avec volume >1.0× → signal haussier fort
3. **Volume normalisé** — Un maintien au-dessus de 0.8× moy. 20j confirmerait la participation institutionnelle

**Scénarios de vigilance (risque retour ATTENDRE) :**
1. **Rejet sous MM50 $16.86** en close — invaliderait le reclaim et le signal d'achat
2. **Cassure sous $16.23** (low 15/06) — ouvre le retour à $15.651
3. **Guidance cut ou news macro négative** (taux, prêts étudiants) — catalyseur baissier

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**🟢 THÈSE CONFIRMÉE — Données pré-ouverture identiques au close 15/06, ACHETER (Réduit) maintenu.**

Le snapshot du **2026-06-16 à 10:00 UTC** est une **capture pré-ouverture US** (6:00 AM ET) qui réplique intégralement les données du close final du 2026-06-15 21:00 UTC. Le cours reste à **$17.13**, la MM50 à **$16.86** (+1.60% écart), le RSI à **56.66** et l'ATR à **$1.05**. Le volume est ajusté mécaniquement à **76.40M (1.03×)** vs 75.98M hier — différence négligeable.

**Ce qui a changé :**
- **Aucun changement qualitatif** — données pré-ouverture, marché fermé
- **DRAFT_refresh trigger ATR_SPIKE 6.13% traité et archivé** — même faux positif que le 2026-06-15 (ATR stable à $1.05, compression)
- **Earnings Q2 dans 42j** (vs 43j hier) — compte à rebours mécanique

**Ce qui est inchangé :**
- Cours $17.13, RSI 56.66, ATR $1.05, MM50 $16.86 — tous identiques au close 15/06
- Score Global ajusté **69.5/100** — ACHETER (Réduit) maintenu
- Score Opportunité **6.5/10**, Catalyseur **6.8/10**, Valorisation **5.5/10**, Momentum **7.5/10**
- Aucune news structurante, aucun événement corporate
- Filtre Qualité **4/6** (Quality Partielle)
- Short interest **14.71%** (setup squeeze intact)
- Forward P/E **21.95** attractif
- Consensus PT **$25.41** (+48.3% upside)
- Options : Put/Call 0.42, Call OI 70.5% — repositionnement haussier stable (valeurs conservées du 15/06)
- [ALERTE DATA QUALITY] Max Pain $1.00 aberrant persistant — historique $17.00 conservé

**Action : ACHETER (Réduit) — Entrée suggérée $17.13, SL $15.03, TP $20.28, Ratio R/R 1.5×. Sizing réduit (Quality Partielle 4/6). Le reclaim MM50 est maintenu. Attention : les données options (Put/Call et Call OI) sont partielles dans le snapshot du jour — valeurs du 15/06 conservées. Surveiller la session du 16/06 pour confirmer la tenue au-dessus de MM50 $16.86 en close. Un rejet sous MM50 invaliderait le signal et justifierait un retour en ATTENDRE. Attention au short interest 14.71% qui crée un setup asymétrique squeeze/pression. [ALERTE DATA QUALITY] Max Pain $1.00 aberrant persistant — historique $17.00 conservé.**

---

*Données sourcées : data/latest.json (2026-06-16T10:00:08+00:00), data/recommandations_latest.json, data/upcoming_events_latest.json, data/fx_exposure_latest.json, data/social_sentiment_latest.json, data/validation_report.txt.*

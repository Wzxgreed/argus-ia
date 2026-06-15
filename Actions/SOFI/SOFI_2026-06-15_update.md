# SOFI (SoFi Technologies, Inc.) — Mise à jour quotidienne

**Date :** 2026-06-15 (snapshot 10:00 UTC)
**Type :** `_update.md` — Données techniques complètes, scores révisés, volume en retrait, anomalie options
**Analyste :** Desk Argus-IA

---

## 1. Résumé des changements depuis l'analyse précédente

| Métrique | `SOFI_2026-06-10_update.md` | **Snapshot 2026-06-15 (10:00 UTC)** | **Δ** |
|----------|-----------------------------|-------------------------------------|-------|
| Cours close | $16.50 | **$16.58** | **+0.48%** |
| RSI 14j | 58.52 | **55.69** | **−2.83 pts** |
| ATR 14j | null [DONNÉES PARTIELLES] ($1.02 hist.) | **1.08** | **Disponible — +5.9%** |
| MM 50j | null [DONNÉES PARTIELLES] ($16.78 hist.) | **16.83** | **Disponible — +$0.05** |
| Écart MM50 | −1.68% (estimé) | **−1.49%** | **Légèrement amélioré** |
| Volume | 79.33M (1.10×) | **50.31M (0.69×)** | **−37% relatif — retrait significatif** |
| Short interest | 14.71% | **14.71%** | **Stable** |
| Max Pain | $17.00 | **$1.00** | **[ALERTE DATA QUALITY] Anomalie JSON** |
| Put/Call ratio | 0.48 | **null** | **[ALERTE DATA QUALITY]** |
| Call OI % | 67.7% | **null** | **[ALERTE DATA QUALITY]** |
| **Score Opportunité** | **5.2/10** | **6.0/10** | **+0.8 pt** |
| **Score Catalyseur** | **5.3/10** | **6.8/10** | **+1.5 pt** |
| **Score Valorisation** | **4.5/10** | **6.0/10** | **+1.5 pt** |
| **Score Momentum** | **6.0/10** | **5.0/10** | **−1.0 pt** |
| **Score Global ajusté** | **51.5/100** | **52.3/100** | **+0.8 pt** |
| **Action** | **ATTENDRE** | **ATTENDRE** | **Inchangée** |
| Timing | Neutre | **Défavorable** | **Sous MM50 confirmé** |

**Verdict :** Le snapshot du **2026-06-15** apporte un **rétablissement des données techniques** (ATR et MM50 désormais disponibles) et une **révision à la hausse des scores Catalyseur (+1.5 pt) et Valorisation (+1.5 pt)** par l'Agent Recommandation. Cependant, le **Score Momentum recule de −1.0 pt** et le **volume chute de −37%** relatif (0.69× vs 1.10×), indiquant un retrait de la conviction institutionnelle. Le cours reste sous la MM50 ($16.83) avec un écart de −1.49%. **Anomalie options** : Max Pain $1.00, Put/Call et Call OI null dans `data/latest.json` — valeurs historiques ($17.00 / 0.48 / 67.7%) conservées avec mention [DONNÉES PARTIELLES]. La thèse **ATTENDRE** est confirmée, le timing repassé en **Défavorable** (cours sous MM50).

---

## 2. Mise à jour technique

| Indicateur | Valeur snapshot 2026-06-15 | Signal |
|------------|---------------------------|--------|
| RSI 14j | 55.69 | 🟡 Zone neutre — légèrement en retrait vs 58.52 |
| MM 50j | $16.83 | 🔴 Cours $16.58 = −1.49% sous MM50 — résistance proche |
| MM 200j | null | ⚪ [DONNÉES PARTIELLES] |
| ATR 14j | $1.08 | 🟢 Disponible — expansion mineure +5.9% vs $1.02 |
| Support clé | $15.651 (low 09/06) / $16.23 (low 15/06) | 🟢 Support immédiat tenu |
| Résistance clé | $16.83 (MM50) / $17.00 (Max Pain historique) | 🔴 MM50 = résistance immédiate |
| Volume relatif | 0.69× | 🔴 Retrait significatif — manque de conviction |
| Beta | 2.152 | ⚠️ Volatilité extrême amplifiée |
| Short interest | 14.71% | 🔴 Élevé — squeeze potentiel intact |

**Analyse technique :** Les données techniques sont désormais **complètes** après plusieurs snapshots partiels. Le RSI a reculé de −2.83 pts à **55.69** (zone neutre, légèrement moins favorable que le 58.52 précédent). La MM50 est établie à **$16.83** (vs estimation $16.78), confirmant que le cours est encore **−1.49% sous la moyenne**. L'ATR à **$1.08** représente une expansion mécanique de +5.9% — le trigger `ATR_SPIKE` détecté par le pipeline est un **faux positif** (pas d'événement structurant, seulement une volatilité légèrement plus élevée).

Le **volume à 0.69×** est le signal technique le plus marquant du jour. Après des volumes soutenus autour de 1.10× sur les sessions précédentes, ce retrait de −37% relatif indique un **assèchement de la participation** — ni achat ni vente agressifs. C'est cohérent avec la stabilité du cours (+0.48%) et le retrait du RSI.

**Options :** [ALERTE DATA QUALITY] Les données options dans `data/latest.json` sont à nouveau corrompues :
- Max Pain : **$1.00** (aberrant — historique $17.00 conservé)
- Put/Call : **null** (historique 0.48 conservé)
- Call OI : **null** (historique 67.7% conservé)
- Expiration prochaine : **2026-06-18** (3 jours ouvrés restants)

**Niveaux (ATR = $1.08) :**
- Support immédiat : **$16.23** (low du 15/06)
- Support intermédiaire : **$15.651** (low du 09/06)
- Support majeur : **$15.00** (psychologique)
- Résistance immédiate : **$16.83** (MM50)
- Résistance intermédiaire : **$17.00** (Max Pain historique)
- Résistance majeure : **$17.10** (high du 09/06)

**Verdict timing :** Défavorable — cours sous MM50 confirmé ($16.58 vs $16.83), volume en retrait. Reclaim de la MM50 en close avec volume >1.0× nécessaire pour revenir Neutre/Favorable.

---

## 3. Mise à jour fondamentale

| Métrique | Valeur | Commentaire |
|----------|--------|-------------|
| Market cap | $21.27B | Stable — mécanique |
| P/E LTM (Yahoo) | 36.84 | Stable |
| Forward P/E | 21.25 | Stable — mécaniquement attractif |
| EV/Revenue | 5.02 | Stable |
| P/B (Yahoo) | 1.965 | Stable |
| Gross margin (FMP) | 75.1% | Excellent, stable |
| Operating margin | 11.0% | Stable |
| Net margin | 10.1% | Stable |
| Debt/Equity (FMP) | 0.173 | Très faible — bilan sain |
| FCF yield | −13.2% | FCF négatif — modèle en investissement |
| SBC/Revenue | 5.5% | Modéré, stable |
| ROE (FMP) | 4.59% | Faible — limite Filtre Qualité à 4/6 |

**Aucune news structurante ni événement corporate détecté** (`data/events_latest.json` vide pour SOFI). Le mouvement reste **purement technique/sentiment**. Les fondamentaux n'ont pas changé.

**Filtre Qualité (6 critères) :** Inchangé à **4/6 (Quality Partielle)**. Aucun nouvel état financier ni guidance.

---

## 4. Mise à jour sentiment / options / news

| Métrique | Valeur | Signal |
|----------|--------|--------|
| Consensus PT (FMP) | $25.41 (27 analystes) | 🟢 Upside consensus +53.3% vs cours $16.58 |
| Analystes actifs (1M) | 0 | 🟡 Aucune couverture récente (vs 1 précédemment) |
| Analystes actifs (1T) | 10 | 🟡 Couverture stable |
| **Short interest** | **14.71%** | 🔴 Élevé — squeeze potentiel renforcé |
| **Max Pain** | **$1.00** [ALERTE] | 🟡 Données aberrantes — historique $17.00 conservé |
| **Put/Call ratio** | **null** [ALERTE] | 🟡 Données manquantes — historique 0.48 conservé |
| **Call OI %** | **null** [ALERTE] | 🟡 Données manquantes — historique 67.7% conservé |
| Social sentiment | 0.0 / No data | ⚪ Pas de données Reddit |
| Pump detected | false | 🟢 Aucun signal pump |

**Short interest :** Stable à **14.71%**. Le setup asymétrique squeeze/pression vendeuse est inchangé.

**Options :** [ALERTE DATA QUALITY] Les données options sont corrompues dans le snapshot 2026-06-15. Les valeurs historiques du 10/06 sont conservées : Max Pain **$17.00**, Put/Call **0.48**, Call OI **67.7%**.

**News** — Aucune news structurante détectée via les flux automatiques.

---

## 5. Scoring global révisé

| Score | Snapshot 2026-06-10 (ATTENDRE) | **Snapshot 2026-06-15 (ATTENDRE)** | **Δ** |
|-------|--------------------------------|-----------------------------------|-------|
| Score Opportunité | 5.2/10 | **6.0/10** | **+0.8 pt** |
| Score Catalyseur | 5.3/10 | **6.8/10** | **+1.5 pt** |
| Score Valorisation | 4.5/10 | **6.0/10** | **+1.5 pt** |
| Score Momentum | 6.0/10 | **5.0/10** | **−1.0 pt** |
| Score Global Composite | 51.5/100 | **52.3/100** | **+0.8 pt** |
| Score Global ajusté | 51.5/100 | **52.3/100** | **+0.8 pt** |
| Action | ATTENDRE | **ATTENDRE** | **Inchangée** |
| Timing | Neutre | **Défavorable** | **Sous MM50** |
| Sizing | — | **—** | **—** |
| Horizon | — | **—** | **—** |

**Pondération régime :** Catalyseur 35% / Valorisation 40% / Momentum 25% (régime inconnu — pondération par défaut).

**Malus / Bonus appliqués (Score Global ajusté) :**
- Malus accounting : 0 (fichier absent)
- Malus geo : 0 (SOFI non listé dans geo_risk — exposition neutre)
- Malus FX : 0 (fx_impact_score 0.0, exposition 55% mais stable)
- Malus social : 0 (pas de données — pas de malus appliqué)
- Malus quant : 0 (pas de signaux historiques)
- Bonus event : 0 (pas d'événement corporate)
- Timing technique : **−5.0** (cours sous MM50)
- Sector rotation : XLF #2 (momentum 6.73) — léger vent de poupe sectoriel

**Analyse du scoring :** Le **Score Global ajusté 52.3/100** progresse de **+0.8 pt** vs le 2026-06-10. SOFI reste en zone **ATTENDRE** (50–59), désormais à **2.3 pt du seuil SURVEILLER** (<50) — légèrement plus de marge qu'auparavant (1.5 pt). La hausse des scores Catalyseur (+1.5) et Valorisation (+1.5) compense le recul du Momentum (−1.0). Le Score Valorisation à **6.0/10** sort de la zone de vigilance (était à 4.5/10), ce qui est positif. Cependant, le Score Momentum **5.0/10** est désormais exactement au seuil de neutralité — ni haussier ni baissier.

**Règle de disqualification :** Aucun score individuel ≤ 2/10 — SOFI n'est pas exclu.

---

## 6. Niveaux révisés

| Niveau | Snapshot 2026-06-10 | Snapshot 2026-06-15 | Calcul |
|--------|---------------------|---------------------|--------|
| Prix d'entrée suggéré | — | **—** | Aucune entrée recommandée en ATTENDRE |
| Stop-loss | $14.46 | **$14.42** | $16.58 − 2×ATR ($1.08) = $14.42 |
| Take-profit | $19.56 | **$19.82** | $16.58 + 3×ATR ($1.08) = $19.82 |
| Upside / Downside | +18.5% / −12.4% | **+19.5% / −12.4%** | — |
| Ratio R/R | 1.50 | **1.50** | Stable (~1.5×) |

**Note sur les niveaux :** L'ATR est désormais disponible à **$1.08** (vs historique $1.02). Les niveaux sont recalculés avec cette valeur actualisée. Le ratio R/R reste stable à **1.5×**. En zone ATTENDRE, **aucune entrée n'est recommandée**.

**Scénarios pour repasser en ACHETER :**
1. **Reclaim MM50** — Cours au-dessus de $16.83 en close avec volume >1.0× → réactivation technique
2. **Breakout $17.00** — Dépassement du Max Pain historique avec volume >1.2× → signal haussier fort
3. **Short squeeze** — Short interest 14.71% + catalyseur positif → mouvement amplifié
4. **Catalyseur fondamental** — News positive (guidance, contrat, M&A) permettant de repasser Momentum >6/10

**Scénarios de vigilance (risque SURVEILLER) :**
1. **Cassure sous $16.23** (low 15/06) — ouvre le retour à $15.651
2. **Score Global < 50** — À 2.3 pt du seuil. Une baisse du Momentum ou de la Valorisation pourrait basculer en SURVEILLER
3. **Guidance cut ou news macro négative** (taux, prêts étudiants) — catalyseur baissier
4. **Augmentation short interest > 15%** — Niveau critique de pression vendeuse

---

## 7. Conclusion — Thèse confirmée, modifiée ou invalidée ?

**🟢 THÈSE CONFIRMÉE — Données techniques complètes, scores révisés à la hausse, volume en retrait, timing repassé Défavorable. SOFI à 2.3 pt du seuil SURVEILLER.**

Le snapshot du **2026-06-15** confirme une **stabilité mécanique** du cours à **$16.58** (vs $16.50) avec un **volume en retrait significatif** (0.69×). Les données techniques sont désormais **complètes** : ATR **$1.08**, MM50 **$16.83**. Le RSI a légèrement reculé à **55.69** (zone neutre). Le scoring de l'Agent Recommandation a été **révisé à la hausse** : Catalyseur **6.8/10** (+1.5), Valorisation **6.0/10** (+1.5), mais Momentum **5.0/10** (−1.0). Le Score Global ajusté progresse à **52.3/100** (+0.8 pt), toujours en zone **ATTENDRE**.

**Ce qui a changé :**
- **[NOUVEAU] Données techniques complètes** — ATR $1.08 et MM50 $16.83 désormais disponibles (vs null précédemment)
- **[RÉVISÉ] Scores agents** — Catalyseur 6.8 (+1.5), Valorisation 6.0 (+1.5), Momentum 5.0 (−1.0)
- **[ALERTE] Données options** — Max Pain $1.00 aberrant (historique $17.00 conservé), Put/Call et Call OI null
- **[SIGNAL] Volume en retrait** — 0.69× vs 1.10× (−37% relatif) = manque de conviction

**Ce qui est inchangé :**
- Cours stable autour de **$16.50–$16.58**
- Short interest **14.71%** (setup squeeze intact)
- Forward P/E **21.25** attractif
- Consensus PT **$25.41** (+53.3% upside)
- Filtre Qualité **4/6** (Quality Partielle)
- Aucune news structurante, aucun événement corporate
- Earnings Q2 dans **43j** (28 juillet, EPS $0.10–$0.11, Rev $1.1B)
- XLF (Financials) #2 sector rotation (momentum 6.73) — vent de poupe sectoriel

**Ce qui maintient ATTENDRE :**
- Score Global **52.3** — à **2.3 pt du seuil SURVEILLER** (<50)
- Cours sous MM50 **$16.83** = timing Défavorable
- Volume **0.69×** — retrait de participation, pas de conviction haussière
- Score Momentum **5.0/10** — exactement au seuil de neutralité
- [ALERTE DATA QUALITY] Données options corrompues — impossible d'évaluer le sentiment options en temps réel

**Ce qui pourrait rebasculer vers ACHETER :**
- Reclaim complet de la MM50 ($16.83) avec volume >1.0×
- Breakout $17.00 (Max Pain historique) avec volume >1.2×
- Catalyseur fondamental positif guidant le momentum au-dessus de 6/10
- Short squeeze sur short interest 14.71% si catalyseur inattendu

**Risques à surveiller :**
- **Proximité du seuil SURVEILLER** — Score Global 52.3, une baisse de 2.3 pt basculerait la recommandation
- **Short interest 14.71%** — niveau critique ; >15% = pression vendeuse très élevée
- **Volume faible** — 0.69× = manque de conviction, risque de faux mouvements
- **Filtre Qualité 4/6** — Quality Partielle, FCF négatif, ROE faible
- **Beta 2.152** — exposition accrue aux mouvements macro
- **Anomalie options JSON** — Max Pain $1.00 aberrant, données Put/Call et Call OI manquantes

**Action : ATTENDRE — Aucune entrée recommandée — Surveiller de près la proximité avec le seuil SURVEILLER (<50). Attendre reclaim MM50 $16.83 en close avec volume >1.0× ou breakout $17.00 pour réactiver la thèse haussière. Surveiller le support $16.23 (low du jour). Si cassé, risque de retour à $15.651. Attention au short interest 14.71% qui crée un setup asymétrique squeeze/pression. [ALERTE DATA QUALITY] Données options corrompues dans latest.json — historiques conservés.**

---

*Données sourcées : data/latest.json (2026-06-15T10:00:08+00:00), data/recommandations_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/geo_risk_latest.json, data/upcoming_events_latest.json, data/events_latest.json, data/fx_exposure_latest.json.*

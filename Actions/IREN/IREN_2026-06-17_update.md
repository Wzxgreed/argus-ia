# IREN — Mise à Jour (2026-06-17, snapshot 10:00 UTC)

> **Type :** `_update.md` — Révision post-pipeline (snapshot 10h UTC)
> **Référence précédente :** [IREN_2026-06-16_update_17h00.md](IREN_2026-06-16_update_17h00.md) (snapshot 17h UTC 2026-06-16)
> **Données source :** `data/latest.json` (fetched_at 2026-06-17T10:00:07 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/crypto_correlation_latest.json`
> **Trigger :** Pipeline matin 2026-06-17

---

## Résumé des Changements (vs Snapshot 17h UTC 2026-06-16)

| Métrique | 17h UTC 16/06 | 10h UTC 17/06 | Δ |
|----------|---------------|---------------|---|
| **Cours close** | **$60.335** | **$59.18** | **−2.74%** |
| **Previous close** | $60.85 | **$60.85** | **=** |
| **Open** | $59.99 | **$60.06** | **+$0.07** |
| **High** | $62.02 | **$62.02** | **=** |
| **Low** | $59.05 | **$58.94** | **−$0.11** |
| **Volume** | 16.82 M | **32.00 M** | **+90.2%** (close officiel vs snapshot intra-session) |
| **Volume vs 20j** | 35.2% | **65.9%** | **+30.7 pts** |
| **RSI 14j** | 41.06 | **39.96** | **−1.1 pt** |
| **ATR 14j** | $5.80 | **$5.81** | **+$0.01** |
| **MM 50j** | $53.09 | **$53.06** | **−$0.03** |
| **P/E TTM** | 78.36× | **76.86×** | **−1.5 pt** (mécanique) |
| **Forward P/E** | −64.19× | **−62.96×** | **+1.23 pt** (mécanique) |
| **P/B** | 7.72× | **7.57×** | **−0.15 pt** (mécanique) |
| **EV/EBITDA** | 159.66× | **155.61×** | **−4.05 pts** (mécanique) |
| **EV/Revenue** | 31.04× | **30.25×** | **−0.79 pt** (mécanique) |
| **Score Catalyseur** | 5.8/10 | **6.3/10** | **🟢 +0.5 pt** |
| **Score Valorisation** | 3.5/10 | **4.0/10** | **🟢 +0.5 pt** (mécanique) |
| **Score Momentum** | 5.5/10 | **5.5/10** | **=** |
| **Score Opportunité** | 4.8/10 | **5.2/10** | **🟢 +0.4 pt** |
| **Score Global ajusté** | 53.0/100 | **56.8/100** | **🟢 +3.8 pts** |
| **Action recommandée** | **ATTENDRE** | **ATTENDRE** | **=** |

**Verdict global : STABILISATION POST-SESSION AVEC LÉGERE DÉGRADATION DU COURS, SCORING RÉVISÉ À LA HAUSSE PAR EFFET MÉCANIQUE DE VALORISATION.**

Le snapshot 10h UTC du 2026-06-17 confirme une **session de consolidation baissière** (−2.74%) à **$59.18**, portant le repli cumulé à **−1.9%** vs le previous close officiel du 16/06 ($60.85). Les données brutes révèlent un **high identique** ($62.02) et un **low légèrement plus bas** ($58.94 vs $59.05), signifiant que la résistance immédiate a été testée puis rejetée, tandis que le support a tenu à quelques cents près.

L'événement structurel principal est le **franchissement de la zone RSI 40** : le RSI passe de **41.06 à 39.96** (−1.1 pt), entrant dans la zone neutre inférieure proche de la survente légère. Cependant, le scoring global est révisé à la hausse de **53.0 à 56.8/100** (+3.8 pts) du fait d'une amélioration mécanique des scores Catalyseur (+0.5 pt) et Valorisation (+0.5 pt) liée à la baisse du cours. L'action reste **ATTENDRE**.

> **[ANOMALIE OPTIONS]** — `data/latest.json` du 2026-06-17 retourne des valeurs incohérentes pour IREN : Max Pain **$5.00** (vs $35.00 précédent), put/call **null**, call OI **0.0%**. Ces valeurs sont structurellement impossibles (Max Pain $5.00 à 91.5% sous le cours). La structure du 2026-06-16 (Max Pain $35.00, put/call 1.44, call OI 41.0%) est conservée comme référence fiable jusqu'à confirmation.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 39.96 | Zone neutre inférieure. Franchissement psychologique de la zone 40 — pression vendeuse persistante mais non critique |
| **ATR 14j** | $5.81 | Volatilité journalière moyenne 9.82% du cours. Stable vs $5.80 |
| **MM 50j** | $53.06 | Cours à +11.5% au-dessus, tendance haussière intermédiaire maintenue mais marge de sécurité réduite (+13.7% hier) |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 48.52 M | Volume session 32.00 M = **65.9%** moyenne — participation modérée, nette amélioration vs snapshot intra-session 35.2% hier |
| **52-week high/low** | $76.87 / $9.633 | Close à **77.0%** du 52W high (vs 78.5% hier) |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |
| **Open / High / Low** | $60.06 / $62.02 / $58.94 | Range intraday 5.2% — volatilité normale pour le beta |

**Niveaux clés (révisés vs snapshot 17h UTC 16/06) :**
- Support immédiat : **$58.94** (low du 2026-06-17)
- Support secondaire : **$59.05** (low révisé du 2026-06-16)
- Support critique : **$53.06** (MM50) — cassure = révision en SURVEILLER
- Support structurel : **$48.75** (ancienne MM50, breakout level rally 25/05)
- Support majeur : **$47.56** (stop-loss ATR 2× = $59.18 − $11.62)
- Résistance immédiate : **$62.02** (high du 2026-06-16 et 17 — double test)
- Résistance : **$63.17** (high du 2026-06-15)
- Résistance majeure : **$69.12** (consensus PT FMP)
- Résistance extrême : **$76.87** (52-week high)
- Stop-loss (2×ATR) : **$47.56** (−19.7% vs close)
- Take-profit (3×ATR) : **$76.61** (+29.4% vs close)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Neutre.** Le RSI à 39.96 est en zone neutre inférieure proche de la survente, signalant une pression vendeuse continue mais pas une accélération panique. Le cours se tient encore au-dessus de la MM50 ($53.06), avec une marge de sécurité réduite (+11.5%). Le volume à 65.9% de la moyenne 20j est modéré — participation en reprise par rapport au snapshot intra-session d'hier, mais encore en dessous de la moyenne.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-17 (23 jours après le J0 annoncé). Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$21.15 B** | $3.13 B | **−85%** | Yahoo |
| P/E (TTM) | **76.86×** | 35.96× | **−53%** | Yahoo |
| P/B | **7.57×** | 1.72× | **−77%** | Yahoo |
| Forward P/E | **−62.96×** | N/A | — | Yahoo |
| EV/EBITDA | **155.61×** | 12.34× | **−92%** | Yahoo |
| EV/Revenue | **30.25×** | 7.04× | **−77%** | Yahoo |
| Short Interest | **16.05%** | N/A | — | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−62.96)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **76.86×** — niveau extrêmement élevé, mécaniquement amélioré par la baisse du cours
- Forward P/E **−62.96×** — profitabilité attendue éloignée, légèrement moins négatif
- EV/EBITDA Yahoo **155.61×** — extrême, amélioration mécanique
- **Close $59.18 vs Consensus PT $69.12** — upside **+16.8%** (vs +14.6% hier)

> **[DONNÉES MANQUANTES]** — `data/accounting_risk_latest.json` inexistant.
> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, multiples extrêmes.

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur 10h UTC | Évolution vs 17h UTC 16/06 | Commentaire |
|--------|---------------|---------------------------|-------------|
| **Consensus PT (FMP)** | **$69.12 (26 analysts)** | = | Inchangé |
| **Max Pain** | **$5.00** ⚠️ | 🔴 Anomalie | Valeur structurellement impossible — structure précédente ($35.00) conservée comme référence |
| **Put/Call ratio** | **null** ⚠️ | 🔴 Anomalie | Valeur indisponible dans latest.json — structure précédente (1.44) conservée |
| **Call OI %** | **0.0%** ⚠️ | 🔴 Anomalie | Valeur incohérente — structure précédente (41.0%) conservée |
| **Short Interest** | **16.05%** | = | Défiance accrue stable |
| **Social Sentiment** | Aucun buzz retail | = | 0 mentions |
| **Event-Driven** | Aucun événement | = | Aucun événement corporate détecté |
| **News Yahoo** | Aucune | = | Aucune news significative |
| **Geo Risk** | Score 3/10, flag "low" | = | Risque géopolitique faible |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = | Impact FX neutre |

**Agent Sector Rotation (2026-06-17) :**
- Régime macro : **UNKNOWN** (VIX indisponible, SPY returns 20j +1.58%, 60j +15.69%)
- Top3 sectors : Technology (XLK, momentum 10.0), Materials (XLB, 5.85), Industrials (XLI, 5.6)
- Bottom3 sectors : Utilities (XLU, 0.0), Consumer Staples (XLP, 0.0), Communication Services (XLC, 0.0)
- Alignement macro : **NON ÉVALUABLE** — régime UNKNOWN
- IREN est classé "Financial Services" par Yahoo — pas d'alignement sectoriel direct avec les top3

**Agent Crypto-Correlation (2026-05-17) :**
- Corrélation 30j BTC : **0.82**
- Beta BTC : **2.1**
- Divergence Score : **4/10**
- Verdict : Fortement corrélé — pivot IA non encore pricé comme découplage

**Interprétation institutionnelle :**
La structure options dans `latest.json` est **anormale** (Max Pain $5.00, put/call null, call OI 0.0%). Ces valeurs sont structurellement impossibles et suggèrent un artefact de fetch Yahoo ou un manque de liquidité sur les options proches. La structure du 2026-06-16 (Max Pain $35.00, put/call 1.44, call OI 41.0%) est conservée comme référence fiable. L'expiration du 2026-06-18 est dans **1 jour** — le Max Pain à $35.00 reste éloigné du cours ($59.18), ce qui conforte la lecture d'une volatilité anormale et d'une dispersion des strikes étendue.

L'absence totale de news, de mentions Reddit et d'événements corporates confirme un mouvement purement technique / algorithmique. Le volume à 65.9% de la moyenne 20j (close officiel) est modéré — en nette reprise vs le snapshot intra-session d'hier (35.2%) mais encore sous la moyenne, signalant une participation institutionnelle réservée.

---

## Scoring Global (Agent Recommandation — 2026-06-17, snapshot 10h UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.3/10 | 35% | 2.21 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 5.5/10 | 25% | 1.38 |
| **Score Opportunité** | **5.2/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Le Score Global ajusté de **56.8/100** reflète le Score Opportunité × 10 (52.0) avec un ajustement de +4.8 pts. Le Score Global brut de **51.8/100** confirme le maintien dans la fourchette ATTENDRE (50–59) par l'ajustement.

**Action recommandée : ATTENDRE**
- Prix d'entrée suggéré : **$59.18** — **ne pas entrer**
- Stop-loss : **$47.56** (−19.7%, basé sur ATR réel $5.81)
- Take-profit : **$76.61** (+29.4%, basé sur ATR réel $5.81)
- Ratio R/R : **1.5 : 1**
- Horizon : **1–3 mois**
- Timing : **Favorable** (RSI proche survente, au-dessus MM50)
- Sizing : **—** (pas de nouvelle position)

> **⚠️ Avertissements :**
> 1. **Anomalie options** — Max Pain $5.00, put/call null, call OI 0.0% dans latest.json = artefact de données. Structure précédente conservée comme référence.
> 2. **RSI sous 40** — 39.96, franchissement psychologique de la zone 40. Surveillance si poursuite sous 35.
> 3. **Volume modéré** — 65.9% de la moyenne 20j (close officiel). En reprise vs hier mais sous la moyenne.
> 4. **Multiples extrêmes** — P/E 76.9×, EV/EBITDA ~156×, Forward P/E −63.0×.
> 5. **Short Interest élevé stable** — 16.05% = défiance accrue du marché maintenue, fuel squeeze inactif.
> 6. **Forward P/E négatif** : −62.96× — profitabilité attendue éloignée.
> 7. **Corrélation BTC** : Beta 2.1, corrélation 0.82 — position IREN = pari implicite sur BTC. Seuil critique BTC ~$75k.
> 8. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (23 jours après le J0 annoncé). Prochain earnings Q2 2026 : **2026-08-27** (71 jours).
> 9. **MM200 indisponible** — tendance long terme non évaluable.
> 10. **Accounting risk** : `data/accounting_risk_latest.json` inexistant — pas de scan M-Score/Z-Score/F-Score disponible.
> 11. **Quant report stale** : `data/quant_report_latest.json` daté 2026-05-17 — pas de signaux historiques (p-value 1.0, insuffisant).
> 12. Si le cours casse **$53.06** (MM50) sans rebond → **passer en SURVEILLER**.
> 13. Si le cours casse **$48.75** (ancienne MM50) → **stopper toute position existante**.
> 14. Si le cours casse **$47.56** (SL 2×ATR) → **stopper la position**.
> 15. Si rebond confirme au-dessus de **$62.02** (high 16-17/06) avec volume > moyenne 20j → réviser vers ACHETER.

---

## Conclusion

**Thèse : CONFIRMÉE — statut ATTENDRE maintenu, stabilisation post-session avec RSI sous zone 40.**

Le snapshot 10h UTC du 2026-06-17 apporte trois événements structurels :

1. **Consolidation baissière modérée** : Le cours recule de **−2.74%** à **$59.18** vs le previous close officiel $60.85. Le repli est ordonné — le low $58.94 est à quelques cents du low révisé d'hier ($59.05), et le high $62.02 est identique (double test de la résistance puis rejet).

2. **Franchissement psychologique du RSI 40** : Le RSI passe de **41.06 à 39.96** (−1.1 pt), entrant dans la zone neutre inférieure proche de la survente légère. Ce n'est pas un signal d'achat automatique (pas de zone 30), mais un signal de vigilance accrue : la pression vendeuse persiste sans accélération panique.

3. **Révision algorithmique à la hausse du scoring** : Malgré la baisse du cours, le Score Global ajusté remonte de **53.0 à 56.8/100** (+3.8 pts) du fait d'une amélioration mécanique des scores Catalyseur (+0.5 pt) et Valorisation (+0.5 pt). Le Score Opportunité remonte de 4.8 à **5.2/10**. L'action reste **ATTENDRE**.

**Différentiels clés vs snapshot 17h UTC 16/06 :**
1. **Cours** : $60.335 → **$59.18** (−2.74%)
2. **Volume** : 16.82 M (snapshot intra-session) → **32.00 M** (close officiel) = 65.9% moyenne
3. **RSI** : 41.06 → **39.96** (−1.1 pt) — franchissement zone 40
4. **ATR** : $5.80 → **$5.81** (+$0.01)
5. **MM50** : $53.09 → **$53.06** (−$0.03)
6. **Scores** : Opportunité 4.8→**5.2**, Global ajusté 53.0→**56.8** — amélioration mécanique
7. **Action** : ATTENDRE → **ATTENDRE** (=)
8. **SL/TP** : $48.73/$77.73 → **$47.56/$76.61** (R/R 1.5 inchangé)

**Recommandation :**
- **Nouvelle position** : **ATTENDRE** — Ne pas entrer à $59.18. Attendre un test de la MM50 ($53.06) ou un rebond confirmé au-dessus de $62.02 avec volume > moyenne 20j.
- **Position existante** (sizing réduit ouverte à ≤$59.77) : Maintenir avec les niveaux SL $47.56 / TP $76.61. Surveiller la MM50 ($53.06) comme seuil critique.
- **Attention expiration 18/06** : le Max Pain fiable à $35.00 reste un niveau bas éloigné du cours. Risque de volatilité anormale. Structure options dans latest.json = anomalie (Max Pain $5.00) — ignorer.
- Premier objectif haussier : **$62.02** (high 16-17/06, résistance testée 2x)
- Deuxième objectif : **$63.17** (high du 15/06)
- Troisième objectif : **$69.12** (consensus PT)
- Si rupture sous **$53.06** (MM50) sans rebond → **passer en SURVEILLER** et réduire la position
- Si rupture sous **$48.75** (ancienne MM50) → **stopper toute position**
- Si rupture sous **$47.56** (SL 2×ATR) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds (23 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (71 jours). Sizing réduit obligatoire si ré-entrée (beta 4.232, ATR 9.82% historique). Surveiller BTC — seuil critique $75k.

---

*Rapport rédigé le 2026-06-17 — Données sources : `data/latest.json` (fetched_at 2026-06-17T10:00:07 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`, `data/crypto_correlation_latest.json`.*

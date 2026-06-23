# IREN — Mise à Jour (2026-06-23 — Snapshot 10h UTC)

> **Type :** `_update.md` — Mise à jour pré-ouverture (snapshot 10:00 UTC, données close 22/06 finalisées)
> **Référence précédente :** [IREN_2026-06-22_update_21h00.md](IREN_2026-06-22_update_21h00.md) (snapshot 21h UTC 2026-06-22)
> **Données source :** `data/latest.json` (fetched_at 2026-06-23T10:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Trigger :** DRAFT_refresh 2026-06-23 détecté — traité comme faux positif (triggers hérités du close 22/06, données brutes identiques)
> **Validation :** [WARNING] IREN — Quality Partielle 4/6; Forward PE négatif; FCF négatif. [ANOMALIE OPTIONS] `latest.json` retourne Max Pain $20.00 / put/call null / call OI null — structure fiable du 22/06 21h UTC conservée comme référence ($40.00 / 4.99 / 16.7%). [DONNÉES MANQUANTES] `data/accounting_risk_latest.json` inexistant. [DONNÉES MANQUANTES] `data/crypto_correlation_latest.json` inexistant.

---

## Résumé des Changements (vs Snapshot 21h UTC 2026-06-22)

| Métrique | 21h UTC 22/06 | 10h UTC 23/06 | Δ |
|----------|---------------|---------------|---|
| **Cours close** | **$56.87** | **$56.87** | **=** |
| **Previous close** | $59.96 | $59.96 | = |
| **Open** | $60.68 | $60.68 | = |
| **High** | $61.28 | $61.28 | = |
| **Low** | $56.30 | $56.30 | = |
| **Volume** | 34.48 M | **34.93 M** | **+1.3%** (révision marginale) |
| **Volume vs 20j** | 72.7% | **73.6%** | **+0.9 pp** (stable) |
| **RSI 14j** | 40.17 | **40.17** | **=** (stable) |
| **ATR 14j** | $5.66 | **$5.66** | **=** (stable) |
| **MM 50j** | $54.37 | $54.37 | = |
| **P/E TTM** | 73.86× | **73.86×** | **=** |
| **Forward P/E** | −60.50× | **−60.50×** | **=** |
| **Max Pain** | $40.00 | **$20.00** | **[ANOMALIE]** — structure fiable $40.00 conservée |
| **Put/Call ratio** | 4.99 | **null** | **[ANOMALIE]** — structure fiable 4.99 conservée |
| **Call OI %** | 16.7% | **null** | **[ANOMALIE]** — structure fiable 16.7% conservée |
| **Consensus PT** | $69.48 (27 analysts) | $69.48 (27 analysts) | = |
| **Score Catalyseur** | 6.3/10 | 6.3/10 | = |
| **Score Valorisation** | 4.0/10 | 4.0/10 | = |
| **Score Momentum** | 4.5/10 | 4.5/10 | = |
| **Score Opportunité** | 4.9/10 | 4.9/10 | = |
| **Score Global ajusté** | 54.3/100 | 54.3/100 | = |
| **Action recommandée** | **ATTENDRE** | **ATTENDRE** | = |

**Verdict global : STABILITÉ TOTALE DES DONNÉES BRUTES — AUCUNE NOUVELLE SESSION DE TRADING DEPUIS LE CLOSE 22/06. DRAFT_refresh DU 23/06 TRAITÉ ET ARCHIVÉ COMME FAUX POSITIF.**

Le snapshot 10h UTC du 2026-06-23 est un snapshot pré-ouverture qui reprend les données de clôture finalisées du 2026-06-22. Aucune donnée brute n'a évolué. Trois points de vigilance :

1. **Anomalie options majeure dans `latest.json`** : Max Pain révisé à **$20.00** (vs $40.00 structure cohérente du 22/06), put/call et call OI passés à **null**. Cette anomalie est identique aux patterns observés lors des snapshots pré-ouverture précédents (2026-06-03, 2026-06-09, 2026-06-16). La structure fiable du 22/06 21h UTC (**Max Pain $40.00, put/call 4.99, call OI 16.7%**) est conservée comme référence opérationnelle jusqu'à confirmation d'une structure options cohérente en séance.

2. **Scores algorithmiques inchangés** : Score Global ajusté **54.3/100** (=), Opportunité **4.9/10** (=). L'action **ATTENDRE** est confirmée avec timing **Favorable** (artefact RSI 40.17).

3. **Aucun événement nouveau** : Pas de news Yahoo, pas d'événement corporate (events_latest.json vide), pas de changement géopolitique (geo_risk_score 3/10 stable), pas de mouvement FX (exposition CAD 15%, neutral).

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 40.17 | **Stable à la limite de la zone 40** — pas de survente (<30), mais sortie confirmée de la zone neutre favorable |
| **ATR 14j** | $5.66 | Volatilité journalière moyenne 9.95% du cours — stable |
| **MM 50j** | $54.37 | Cours à **+4.6%** au-dessus — marge de sécurité inchangée |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 47.43 M | Volume session 34.93 M = **73.6%** moyenne — **participation normale** |
| **52-week high/low** | $76.87 / $10.92 | Close à **74.0%** du 52W high |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |
| **Open / High / Low / Close** | $60.68 / $61.28 / $56.30 / $56.87 | Range intraday **8.8%** — close proche du low |

**Niveaux clés (inchangés vs snapshot 21h UTC 22/06) :**
- Support immédiat : **$56.30** (low final du 2026-06-22)
- Support critique : **$54.37** (MM50) — cassure sans rebond = révision en SURVEILLER
- Support structurel : **$53.97** (ancienne MM50 du snapshot 13h UTC 22/06, breakout level rally 08/06)
- Support majeur : **$52.30** (low du 2026-06-09)
- Résistance immédiate : **$58.00** (ancien support)
- Résistance : **$59.96** (previous close du 2026-06-22)
- Résistance : **$61.28** (high du 2026-06-22)
- Résistance majeure : **$69.48** (consensus PT FMP)
- Stop-loss (2×ATR) : **$45.55** (−19.9% vs close)
- Take-profit (3×ATR) : **$73.85** (+29.9% vs close)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable (artefact RSI 40.17).** Le RSI à 40.17 est techniquement dans une zone où un rebond est possible, mais le close proche du low ($56.87 vs low $56.30) et l'absence de rebond en fin de session du 22/06 sont des signaux de faiblesse. Le cours ne se tient qu'à +4.6% au-dessus de la MM50 ($54.37).

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-23 (29 jours après le J0 annoncé). Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$20.32 B** | $3.13 B | **−85%** | Yahoo |
| P/E (TTM) | **73.86×** | 35.54× | **−52%** | Yahoo |
| P/B | **7.28×** | 1.72× | **−76%** | Yahoo |
| Forward P/E | **−60.50×** | N/A | — | Yahoo |
| EV/EBITDA | **150.00×** | 12.34× | **−92%** | Yahoo |
| EV/Revenue | **29.16×** | 7.04× | **−76%** | Yahoo |
| Short Interest | **16.05%** | N/A | — | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−60.50)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **73.86×** — niveau extrêmement élevé
- Forward P/E **−60.50×** — profitabilité attendue éloignée
- EV/EBITDA Yahoo **150.00×** — extrême
- **Close $56.87 vs Consensus PT $69.48** — upside **+22.2%**

> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, multiples extrêmes.
> **[ANOMALIE OPTIONS]** — `latest.json` retourne Max Pain $20.00 / put/call null / call OI null. Structure fiable conservée : Max Pain $40.00, put/call 4.99, call OI 16.7% (du 22/06 21h UTC).
> **[DONNÉES MANQUANTES]** — `data/accounting_risk_latest.json` inexistant.
> **[DONNÉES MANQUANTES]** — `data/crypto_correlation_latest.json` inexistant (dernier dispo : 2026-05-17).

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur 23/06 (10h UTC) | Évolution vs 21h UTC 22/06 | Commentaire |
|--------|------------------------|----------------------|-------------|
| **Consensus PT (FMP)** | **$69.48 (27 analysts)** | = | Consensus inchangé — upside +22.2% |
| **Max Pain** | **$20.00** | [ANOMALIE] | Valeur aberrante — structure fiable $40.00 conservée |
| **Put/Call ratio** | **null** | [ANOMALIE] | Structure fiable 4.99 conservée |
| **Call OI %** | **null** | [ANOMALIE] | Structure fiable 16.7% conservée |
| **Short Interest** | **16.05%** | = | Défiance accrue stable — fuel squeeze inactif |
| **Social Sentiment** | Aucun buzz retail | = | 0 mentions — alerte EXTREME_BEARISH automatique (artefact score 0.0) |
| **Event-Driven** | Aucun événement | = | Aucun événement corporate détecté |
| **News Yahoo** | Aucune | = | Aucune news significative |
| **Geo Risk** | Score 3/10, flag "low" | = | Risque géopolitique faible |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = | Impact FX neutre |

**Agent Sector Rotation (2026-06-23) :**
- Régime macro : **UNKNOWN** (SPY returns 20j +0.48%, 60j +13.62%)
- Top3 sectors : Technology (XLK, momentum 10.0), Industrials (XLI, 7.54), Financials (XLF, 5.45)
- Bottom3 sectors : Consumer Staples (XLP, 0.0), Consumer Discretionary (XLY, 0.0), Communication Services (XLC, 0.0)
- Alignement macro : **NON ÉVALUABLE** — régime UNKNOWN
- IREN est classé "Financial Services" par Yahoo — le secteur Financials est 3e du ranking sectoriel (momentum 5.45), ce qui est neutre à légèrement favorable. L'exposition thématique Technology/IA via le pivot HPC est indirecte.

**Agent Crypto-Correlation :**
- [DONNÉES MANQUANTES] `data/crypto_correlation_latest.json` inexistant au 2026-06-23. Dernier snapshot disponible : 2026-05-17 (corrélation 30j BTC 0.82, beta BTC 2.1, Divergence Score 4/10).
- **Hypothèse de travail** : la corrélation reste le driver dominant à court terme. Tout mouvement BTC >±5% impactera IREN de ±10%+ via le beta 2.1.

**Interprétation institutionnelle :**
Le snapshot 10h UTC du 23 est un **snapshot pré-ouverture** sans nouvelles données de marché. Les triggers PRICE_GAP −5.15% et ATR_SPIKE 9.95% du DRAFT_refresh sont des **faux positifs hérités** du mouvement du 22/06. Le DRAFT_refresh a été archivé sans modification de thèse.

La structure options dans `latest.json` est corrompue (Max Pain $20.00, put/call null) — un pattern récurrent des snapshots pré-ouverture. La structure fiable du 22/06 21h UTC (**Max Pain $40.00, put/call 4.99, puts 83.3% OI**) reste la référence opérationnelle. Cette défiance options record n'a pas bougé car les données de session n'ont pas changé.

L'alerte `EXTREME_BEARISH` dans `social_sentiment_latest.json` reste un **artefact algorithmique** (sentiment_score 0.0 sur 0 mentions) — à ignorer en l'absence de données Reddit collectées.

---

## Scoring Global (Agent Recommandation — 2026-06-23, 10h UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.3/10 | 35% | 2.21 |
| **Valorisation** | 4.0/10 | 40% | 1.60 |
| **Momentum** | 4.5/10 | 25% | 1.13 |
| **Score Opportunité** | **4.9/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Score Global ajusté **54.3/100** — stable vs le snapshot 21h UTC du 22/06 (54.3). Le Score Opportunité × 10 (49.0) avec ajustement de +5.3 pts place l'action dans la fourchette **ATTENDRE** (50–59).

**Action recommandée : ATTENDRE**
- Prix d'entrée suggéré : **$56.87**
- Stop-loss : **$45.55** (−19.9%, basé sur ATR réel $5.66)
- Take-profit : **$73.85** (+29.9%, basé sur ATR réel $5.66)
- Ratio R/R : **1.5 : 1**
- Horizon : **—**
- Timing : **Favorable** (RSI 40.17 — zone de rebond possible, mais faiblesse confirmée)
- Sizing : **—**

> **⚠️ Avertissements :**
> 1. **Anomalie options** — `latest.json` retourne Max Pain $20.00 / put/call null / call OI null. Structure fiable conservée : Max Pain $40.00, put/call 4.99, call OI 16.7% (22/06 21h UTC).
> 2. **RSI 40.17** — stable à la limite de la zone 40. Pas de survente (<30), mais signal de faiblesse maintenu.
> 3. **Multiples extrêmes** — P/E 73.9×, EV/EBITDA ~150×, Forward P/E −60.5×.
> 4. **Short Interest élevé stable** — 16.05% = défiance accrue du marché maintenue, fuel squeeze inactif.
> 5. **Forward P/E négatif** : −60.50× — profitabilité attendue éloignée.
> 6. **Corrélation BTC** : Hypothèse beta 2.1, corrélation 0.82 (dernier dispo 2026-05-17) — position IREN reste un pari implicite sur BTC. Seuil critique BTC ~$75k.
> 7. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (29 jours après le J0 annoncé). Prochain earnings Q2 2026 : **2026-08-27** (65 jours).
> 8. **MM200 indisponible** — tendance long terme non évaluable.
> 9. **Accounting risk** : `data/accounting_risk_latest.json` inexistant — pas de scan M-Score/Z-Score/F-Score disponible.
> 10. **Quant report stale** : `data/quant_report_latest.json` daté 2026-05-17 — pas de signaux historiques (p-value 1.0, insuffisant).
> 11. **Défiance options record** : put/call 4.99, puts 83.3% OI — signal contradictoire maintenu.
> 12. **Close proche du low** : $56.87 vs low $56.30 = absence de rebond en fin de session du 22/06.
> 13. Si le cours casse **$54.37** (MM50) sans rebond → **passer en SURVEILLER** et réduire la position.
> 14. Si le cours casse **$53.97** (ancienne MM50) → **stopper toute position existante**.
> 15. Si le cours casse **$45.55** (SL 2×ATR) → **stopper la position**.

---

## Conclusion

**Thèse : CONFIRMÉE ATTENDRE — STABILITÉ TOTALE DES DONNÉES BRUTES, DRAFT_refresh DU 23/06 ARCHIVÉ COMME FAUX POSITIF, ANOMALIE OPTIONS MAJEURE DÉTECTÉE ET CORRIGÉE.**

Le snapshot 10h UTC du 2026-06-23 n'apporte aucune donnée de marché nouvelle par rapport au close 21h UTC du 2026-06-22. Trois éléments structurants :

1. **DRAFT_refresh archivé** : Les triggers PRICE_GAP −5.15% et ATR_SPIKE 9.95% sont hérités du mouvement du 22/06. Aucune donnée brute n'a changé. Le DRAFT_refresh a été archivé (`IREN_2026-06-23_DRAFT_refresh.md` → `_ARCHIVED_DRAFT_refresh_IREN_2026-06-23_DRAFT_refresh_archived.md`).

2. **Anomalie options majeure** : `latest.json` retourne Max Pain $20.00, put/call null, call OI null — structure incohérente identique aux patterns des snapshots pré-ouverture précédents. La structure fiable du 22/06 21h UTC (**Max Pain $40.00, put/call 4.99, call OI 16.7%**) est conservée comme référence opérationnelle.

3. **Scores algorithmiques stables** : Score Global ajusté **54.3/100** (=), Opportunité **4.9/10** (=). L'action reste en **ATTENDRE** avec timing **Favorable** (artefact RSI 40).

**Différentiels clés vs snapshot 21h UTC 22/06 :**
1. **Cours** : $56.87 → **$56.87** (=)
2. **Volume** : 34.48 M → **34.93 M** (+1.3%, révision marginale — participation normale maintenue)
3. **RSI** : 40.17 → **40.17** (=)
4. **ATR** : $5.66 → **$5.66** (=)
5. **Options** : Max Pain $40.00/4.99/16.7% → **[ANOMALIE $20.00/null/null]** — structure fiable conservée
6. **Consensus PT** : $69.48 (27) → **=** (inchangé)
7. **Scores** : Opportunité 4.9→**4.9** (=), Global ajusté 54.3→**54.3** (=)
8. **Action** : ATTENDRE → **ATTENDRE** (confirmée)
9. **SL/TP** : $45.55/$73.85 → **$45.55/$73.85** (=)

**Recommandation :**
- **Nouvelle position** : **ATTENDRE** à $56.87 — la tendance baissière est confirmée sur volume normal. Attendre une consolidation au-dessus de la MM50 ($54.37) ou un signal de reprise du momentum avant toute entrée.
- **Position existante** (si entrée à $59.96 le 22/06) : **Réduire** — le SL $45.55 est lointain (−19.9%), mais le franchissement de la zone RSI 40 et l'absence de rebond en fin de session sont des signaux de faiblesse. Réduire de 30–50% et surveiller $54.37 (MM50).
- Premier support à surveiller : **$56.30** (low final du 22/06)
- Deuxième support : **$54.37** (MM50)
- Troisième support : **$53.97** (ancienne MM50)
- Si rupture sous **$54.37** (MM50) sans rebond → **passer en SURVEILLER** et réduire la position
- Si rupture sous **$53.97** (ancienne MM50) → **stopper toute position existante**
- Si rupture sous **$45.55** (SL 2×ATR) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds (29 jours après le J0 annoncé). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (65 jours). [DONNÉES PARTIELLES] — Quality Partielle 4/6, Forward PE négatif, FCF négatif. Baisse de −5.15% sur participation volume normale (73.6% moyenne 20j) = pression vendeuse réelle, pas distribution institutionnelle.

---

*Rapport rédigé le 2026-06-23 — Données sources : `data/latest.json` (fetched_at 2026-06-23T10:00:01 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`.*

# IREN — Mise à Jour (2026-06-23 — Snapshot 17h UTC)

> **Type :** `_update.md` — Mise à jour post-session (snapshot 17:00 UTC, données session 23/06)
> **Référence précédente :** [IREN_2026-06-23_update_13h00.md](IREN_2026-06-23_update_13h00.md) (snapshot 13h UTC 2026-06-23)
> **Données source :** `data/latest.json` (fetched_at 2026-06-23T17:00:02 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`
> **Trigger :** DRAFT_refresh 2026-06-23 détecté — traité comme faux positif (ATR_SPIKE 10.13% hérité, volatilité déjà intégrée)
> **Validation :** [WARNING] IREN — Quality Partielle 4/6; Forward PE négatif; FCF négatif. [DONNÉES MANQUANTES] `data/accounting_risk_latest.json` inexistant. [DONNÉES MANQUANTES] `data/crypto_correlation_latest.json` inexistant (dernier dispo : 2026-05-17). [DONNÉES MANQUANTES] `data/quant_report_latest.json` daté 2026-05-17 (stale, p-value 1.0).

---

## Résumé des Changements (vs Snapshot 13h UTC 2026-06-23)

| Métrique | 13h UTC 23/06 | 17h UTC 23/06 | Δ |
|----------|---------------|---------------|---|
| **Cours close** | **$56.87** | **$55.485** | **−2.44%** |
| **Previous close** | $59.96 | $56.87 | −5.15% (nouvelle session) |
| **Open** | $60.68 | **$53.405** | **−12.0% gap down** |
| **High** | $61.28 | **$57.54** | **−6.1%** |
| **Low** | $56.30 | **$52.76** | **−6.3%** (test sous MM50) |
| **Volume** | 34.93 M | **19.42 M** | **−44.4%** (effondrement) |
| **Volume vs 20j** | 73.6% | **41.7%** | **−31.9 pp** (participation très faible) |
| **RSI 14j** | 40.17 | **37.12** | **−3.05 pts** (approche survente <30) |
| **ATR 14j** | $5.66 | **$5.62** | **−$0.04** (stable) |
| **MM 50j** | $54.37 | **$54.69** | **+$0.32** (légère hausse) |
| **P/E TTM** | 73.86× | **72.04×** | **−1.82×** (amélioration mécanique) |
| **Forward P/E** | −60.50× | **−59.01×** | **+1.49×** (amélioration marginale) |
| **Max Pain** | $40.00 | **$40.00** | **=** (stable) |
| **Put/Call ratio** | 3.67 | **3.67** | **=** (stable) |
| **Call OI %** | 21.4% | **21.4%** | **=** (stable) |
| **Consensus PT** | $69.48 (27 analysts) | $69.48 (27 analysts) | = |
| **Score Catalyseur** | 6.3/10 | **6.8/10** | **+0.5 pt** (upgrade algorithmique) |
| **Score Valorisation** | 4.0/10 | **4.5/10** | **+0.5 pt** (upgrade algorithmique) |
| **Score Momentum** | 4.5/10 | **5.5/10** | **+1.0 pt** (upgrade algorithmique) |
| **Score Opportunité** | 4.9/10 | **5.6/10** | **+0.7 pt** (upgrade algorithmique) |
| **Score Global ajusté** | 54.3/100 | **60.5/100** | **+6.2 pts** (upgrade algorithmique) |
| **Action recommandée** | **ATTENDRE** | **ACHETER (Sizing Réduit)** | **UPGRADE** |

**Verdict global : UPGRADE ALGORITHMIQUE CONTRE-INTUITIF — COURS EN BAISSE DE −2.44% ET VOLUME EFFONDRE À 41.7% DE LA MOYENNE 20J, MAIS LES SCORES AGENTS RÉVISENT À LA HAUSSE. VIGILANCE ACCRUE REQUISE.**

Le snapshot 17h UTC du 2026-06-23 capture la première session de trading réelle depuis le close 22/06. Trois points structurants :

1. **Nouvelle session avec gap down et recovery partielle** : Open à **$53.405** (−12.0% vs previous close $60.68 du 22/06), mais recovery intra-session jusqu'à **$55.485** (close). Le low **$52.76** a cassé la MM50 ($54.69) en intraday de **−3.6%** avant rebond. Cette dynamique V-shaped intraday est un signal technique mitigé.

2. **Volume effondré** : **19.42 M** = seulement **41.7%** de la moyenne 20j (46.59 M). C'est le niveau de participation le plus faible depuis le 2026-06-17 (15.69 M, 33.1%). Un mouvement de −2.44% sur volume très faible = absence de conviction vendeuse institutionnelle, mais aussi absence d'achat soutenu. La baisse est « silencieuse ».

3. **Upgrade algorithmique vs dégradation technique** : Les scores agents révisent tous les axes à la hausse malgré la baisse du cours et du RSI. L'algorithme interprète le RSI à **37.12** comme proche de la zone de survente (<30), créant un timing « Favorable ». Cependant, le volume faible et le franchissement de la MM50 en intraday sont des signaux de faiblesse réelle qui ne soutiennent pas mécaniquement l'upgrade.

---

## Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **RSI 14j** | 37.12 | **−3.05 pts vs 13h UTC** — proche de la zone survente (<30). L'algorithme interprète cela comme un signal de rebond, mais le momentum est cassé |
| **ATR 14j** | $5.62 | Volatilité journalière moyenne 10.13% du cours — stable |
| **MM 50j** | $54.69 | Cours à **+1.4%** au-dessus — marge de sécurité **très réduite** (vs +4.6% à 13h UTC) |
| **MM 200j** | N/A | **Indisponible** dans `latest.json` — [DONNÉES MANQUANTES] |
| **Volume 20j moy.** | 46.59 M | Volume session 19.42 M = **41.7%** moyenne — **participation très faible** |
| **52-week high/low** | $76.87 / $10.92 | Close à **72.1%** du 52W high (vs 74.0% à 13h UTC) |
| **Beta** | 4.232 | Volatilité systématique extrême inchangée |
| **Open / High / Low / Close** | $53.405 / $57.54 / $52.76 / $55.485 | Range intraday **8.9%** — close au milieu du range, recovery du low |

**Niveaux clés (révisés vs snapshot 13h UTC 23/06) :**
- Support immédiat : **$52.76** (low du 2026-06-23) — testé et défendu
- Support critique : **$54.69** (MM50) — **cassée en intraday** ($52.76 = −3.6% sous MM50), reprise en clôture mais fragilité confirmée
- Support structurel : **$52.30** (low du 2026-06-09)
- Support majeur : **$50.67** (MM50 du snapshot 17h UTC 09/06)
- Résistance immédiate : **$56.87** (previous close du 2026-06-22)
- Résistance : **$57.54** (high du 2026-06-23)
- Résistance : **$58.00** (ancien support pré-22/06)
- Résistance majeure : **$69.48** (consensus PT FMP)
- Stop-loss (2×ATR) : **$44.24** (−20.3% vs close)
- Take-profit (3×ATR) : **$72.34** (+30.4% vs close)
- Ratio R/R : **1.5 : 1**

**Verdict timing : Favorable (RSI 37.12 — zone de survente approche, rebond possible).** Le RSI à 37.12 est techniquement dans une zone où un rebond est historiquement probable, mais le volume très faible (41.7%) et le fait que le low ait cassé la MM50 en intraday sont des signaux de faiblesse structurelle. La recovery du low ($52.76 → $55.485 = +5.2%) est positive, mais sans volume elle manque de conviction. Le cours ne se tient qu'à +1.4% au-dessus de la MM50 ($54.69) — une marge critique.

---

## Mise à Jour Fondamentale

**Aucun nouveau flux post-earnings Q1 2026** intégré dans les sources Yahoo/FMP au 2026-06-23 (29 jours après le J0 annoncé). Les métriques FMP restent au FY 2025 (clos 2025-06-30).

| Métrique | Yahoo Finance | FMP Stable API | Écart | Source préférée |
|----------|---------------|----------------|-------|-----------------|
| Market Cap | **$19.82 B** | $3.13 B | **−84%** | Yahoo |
| P/E (TTM) | **72.04×** | 35.54× | **−51%** | Yahoo |
| P/B | **7.10×** | 1.72× | **−76%** | Yahoo |
| Forward P/E | **−59.01×** | N/A | — | Yahoo |
| EV/EBITDA | **150.00×** | 12.34× | **−92%** | Yahoo |
| EV/Revenue | **29.16×** | 7.04× | **−76%** | Yahoo |
| Short Interest | **16.05%** | N/A | — | Yahoo |

**Filtre Qualité : 4/6 — ⚠️ Quality Partielle** (inchangé)
- ❌ Forward P/E négatif (−59.01)
- ❌ FCF négatif (price_to_fcf = −2.77 FMP, FCF yield −36%)
- ✅ Assets/Liabilities > 1.0 (current ratio 4.29, quick ratio 4.29)
- ✅ Gross Margin 68.3%, EBITDA Margin 57.0%
- ⚠️ Moat : contrat NVIDIA $3.4B = catalyseur, pas encore moat structurel prouvé
- ⚠️ TAM / croissance industrie : pivot IA HPC en cours, TAM non quantifié dans FMP

**Valorisation :**
- P/E TTM Yahoo **72.04×** — niveau extrêmement élevé (légère amélioration mécanique vs 73.86×)
- Forward P/E **−59.01×** — profitabilité attendue éloignée (amélioration marginale vs −60.50×)
- EV/EBITDA Yahoo **150.00×** — extrême
- **Close $55.485 vs Consensus PT $69.48** — upside **+25.2%** (vs +22.2% à 13h UTC)

> **[WARNING]** — Quality Partielle 4/6, Forward PE négatif, FCF négatif, multiples extrêmes.
> **[DONNÉES MANQUANTES]** — `data/accounting_risk_latest.json` inexistant.
> **[DONNÉES MANQUANTES]** — `data/crypto_correlation_latest.json` inexistant (dernier dispo : 2026-05-17).

---

## Mise à Jour Sentiment / Options / News

| Signal | Valeur 23/06 (17h UTC) | Évolution vs 13h UTC 23/06 | Commentaire |
|--------|------------------------|----------------------|-------------|
| **Consensus PT (FMP)** | **$69.48 (27 analysts)** | = | Consensus inchangé — upside +25.2% (amélioré mécaniquement par la baisse du cours) |
| **Max Pain** | **$40.00** | = | Stable — structure cohérente |
| **Put/Call ratio** | **3.67** | = | Stable — défiance record maintenue |
| **Call OI %** | **21.4%** | = | Stable — puts 78.6% OI |
| **Short Interest** | **16.05%** | = | Défiance accrue stable — fuel squeeze inactif |
| **Social Sentiment** | Aucun buzz retail | = | 0 mentions — alerte EXTREME_BEARISH automatique (artefact score 0.0) |
| **Event-Driven** | Aucun événement | = | Aucun événement corporate détecté (events_latest.json vide) |
| **News Yahoo** | Aucune | = | Aucune news significative |
| **Geo Risk** | Score 3/10, flag "low" | = | Risque géopolitique faible |
| **FX Exposure** | 15% revenus CAD, Score 0/10 | = | Impact FX neutre |

**Agent Sector Rotation (2026-06-23) :**
- Régime macro : **UNKNOWN** (SPY returns 20j −0.86%, 60j +14.59%)
- Top3 sectors : Technology (XLK, momentum 10.0), Industrials (XLI, 7.13), Financials (XLF, 6.23)
- Bottom3 sectors : Utilities (XLU, 0.0), Consumer Discretionary (XLY, 0.0), Communication Services (XLC, 0.0)
- Alignement macro : **NON ÉVALUABLE** — régime UNKNOWN
- IREN est classé "Financial Services" par Yahoo — le secteur Financials est 3e du ranking sectoriel (momentum 6.23), ce qui est neutre à légèrement favorable. L'exposition thématique Technology/IA via le pivot HPC est indirecte.

**Agent Crypto-Correlation :**
- [DONNÉES MANQUANTES] `data/crypto_correlation_latest.json` inexistant au 2026-06-23. Dernier snapshot disponible : 2026-05-17 (corrélation 30j BTC 0.82, beta BTC 2.1, Divergence Score 4/10).
- **Hypothèse de travail** : la corrélation reste le driver dominant à court terme. Tout mouvement BTC >±5% impactera IREN de ±10%+ via le beta 2.1.

**Interprétation institutionnelle :**
Le snapshot 17h UTC capture une session caractérisée par un **gap down sévère** (−12.0% vs open précédent) suivi d'une **recovery partielle** (+3.8% du low au close). Cette configuration en « marteau » ou « doji » est techniquement favorable à court terme, mais le volume effondré (41.7%) enlève toute conviction à ce pattern.

La structure options reste **inchangée et stable** (Max Pain $40.00, put/call 3.67, call OI 21.4%) — la défiance record n'a pas évolué pendant la session, ce qui est rassurant (pas d'accélération de la panique options). Cependant, le ratio put/call >3.0 reste un signal de défiance significative.

L'alerte `EXTREME_BEARISH` dans `social_sentiment_latest.json` reste un **artefact algorithmique** (sentiment_score 0.0 sur 0 mentions) — à ignorer en l'absence de données Reddit collectées.

---

## Scoring Global (Agent Recommandation — 2026-06-23, 17h UTC)

| Axe | Score | Pondération | Poids ajusté |
|-----|-------|-------------|--------------|
| **Catalyseur** | 6.8/10 | 35% | 2.38 |
| **Valorisation** | 4.5/10 | 40% | 1.80 |
| **Momentum** | 5.5/10 | 25% | 1.38 |
| **Score Opportunité** | **5.6/10** | | |

**Malus/Bonus appliqués (agent recommandation) :**
Score Global ajusté **60.5/100** — vs 54.3/100 au snapshot 13h UTC. Le Score Opportunité × 10 (56.0) avec ajustement de +4.5 pts place l'action dans la fourchette **ACHETER (Sizing Réduit)** (60–74).

**Action recommandée : ACHETER (Sizing Réduit)**
- Prix d'entrée suggéré : **$55.485**
- Stop-loss : **$44.24** (−20.3%, basé sur ATR réel $5.62)
- Take-profit : **$72.34** (+30.4%, basé sur ATR réel $5.62)
- Ratio R/R : **1.5 : 1**
- Horizon : **1–3 mois**
- Timing : **Favorable** (RSI 37.12 — zone de survente approche, rebond possible)
- Sizing : **Réduit** (beta 4.232, volatilité extrême)

> **⚠️ Avertissements :**
> 1. **Upgrade algorithmique contre-intuitif** — Les scores montent malgré la baisse de −2.44% et le RSI qui descend. L'algorithme valorise le « timing » (RSI proche survente) mais ignore le volume.
> 2. **Volume effondré** — 41.7% de la moyenne 20j = participation institutionnelle très faible. Pas de distribution massive, mais pas d'accumulation non plus.
> 3. **Cassure de la MM50 en intraday** — Low $52.76 a cassé la MM50 ($54.69) de −3.6%. Reprise en clôture, mais fragilité confirmée.
> 4. **RSI 37.12** — proche de la survente (<30), mais pas encore dedans. Zone de rebond possible, pas garantie.
> 5. **Multiples extrêmes** — P/E 72.0×, EV/EBITDA ~150×, Forward P/E −59.0×.
> 6. **Short Interest élevé stable** — 16.05% = défiance accrue du marché maintenue, fuel squeeze inactif.
> 7. **Forward P/E négatif** : −59.01× — profitabilité attendue éloignée.
> 8. **Corrélation BTC** : Hypothèse beta 2.1, corrélation 0.82 (dernier dispo 2026-05-17) — position IREN reste un pari implicite sur BTC. Seuil critique BTC ~$75k.
> 9. **Réserve earnings Q1 2026** : résultats toujours non intégrés dans les feeds Yahoo/FMP (29 jours après le J0 annoncé). Prochain earnings Q2 2026 : **2026-08-27** (65 jours).
> 10. **MM200 indisponible** — tendance long terme non évaluable.
> 11. **Accounting risk** : `data/accounting_risk_latest.json` inexistant — pas de scan M-Score/Z-Score/F-Score disponible.
> 12. **Quant report stale** : `data/quant_report_latest.json` daté 2026-05-17 — pas de signaux historiques (p-value 1.0, insuffisant).
> 13. **Défiance options record** : put/call 3.67, puts 78.6% OI — signal contradictoire maintenu.
> 14. **Gap down sévère** : Open $53.405 = −12.0% vs open précédent $60.68. La recovery partielle n'a pas comblé le gap.
> 15. Si le cours casse **$54.69** (MM50) en clôture sans rebond → **passer en ATTENDRE** et réduire la position.
> 16. Si le cours casse **$52.30** (low du 09/06) → **stopper toute position existante**.
> 17. Si le cours casse **$44.24** (SL 2×ATR) → **stopper la position**.

---

## Conclusion

**Thèse : MODIFIÉE — UPGRADE ALGORITHMIQUE DE ATTENDRE À ACHETER (Sizing Réduit), MAIS AVEC VIGILANCE ACCRUE DUE AU VOLUME EFFONDRE ET À LA CASSURE INTRADAY DE LA MM50.**

Le snapshot 17h UTC du 2026-06-23 apporte trois éléments structurants :

1. **Nouvelle session de trading réelle** : Pour la première fois depuis le close 22/06, de nouvelles données de marché sont disponibles. Le cours a ouvert en **gap down de −12.0%** ($53.405), a testé un low à **$52.76** (cassure de la MM50 de −3.6%), puis a rebondi pour clôturer à **$55.485** (recovery de +5.2% du low). Cette dynamique V-shaped est techniquement favorable, mais le volume très faible (41.7%) manque de conviction.

2. **Upgrade algorithmique contre-intuitif** : L'Agent Recommandation a upgradé l'action de **ATTENDRE (54.3/100)** à **ACHETER Réduit (60.5/100)**. Les trois axes (Catalyseur +0.5 pt, Valorisation +0.5 pt, Momentum +1.0 pt) montent simultanément malgré la baisse du cours. L'explication mécanique : le RSI proche de la survente (37.12) est interprété comme un timing favorable, et la baisse du cours mécaniquement améliore le ratio R/R (upside consensus passe de +22.2% à +25.2%). Cependant, cet upgrade ne reflète pas la faiblesse structurelle observée (volume, cassure MM50).

3. **Stabilité options et absence de news** : La structure options reste stable (Max Pain $40.00, put/call 3.67, call OI 21.4%), confirmant que le marché options n'a pas paniqué pendant la session. Aucune news Yahoo, aucun événement corporate, aucun changement géopolitique. Le mouvement est purement technique/mécanique.

**Différentiels clés vs snapshot 13h UTC 23/06 :**
1. **Cours** : $56.87 → **$55.485** (−2.44%, nouvelle session)
2. **Volume** : 34.93 M → **19.42 M** (−44.4%, participation très faible 41.7%)
3. **RSI** : 40.17 → **37.12** (−3.05 pts, approche survente)
4. **ATR** : $5.66 → **$5.62** (−$0.04, stable)
5. **MM50** : $54.37 → **$54.69** (+$0.32, cours à +1.4% vs +4.6%)
6. **Options** : Max Pain $40.00/3.67/21.4% → **=** (stable)
7. **Consensus PT** : $69.48 (27) → **=** (inchangé)
8. **Scores** : Opportunité 4.9→**5.6** (+0.7 pt), Global ajusté 54.3→**60.5** (+6.2 pts)
9. **Action** : ATTENDRE → **ACHETER (Sizing Réduit)** (upgrade algorithmique)
10. **SL/TP** : $45.55/$73.85 → **$44.24/$72.34** (révisés à la baisse avec ATR et cours)

**Recommandation :**
- **Nouvelle position** : **ACHETER (Sizing Réduit)** à $55.485 — l'upgrade algorithmique suggère une entrée, mais le volume très faible (41.7%) impose une taille de position réduite (max 5% du portefeuille, beta 4.232). Attendre une confirmation de volume >60% moyenne 20j avant d'augmenter le sizing.
- **Position existante** (si entrée à des niveaux supérieurs) : **Maintenir** avec vigilance — le SL $44.24 est lointain (−20.3%), mais la cassure intraday de la MM50 ($52.76 < $54.69) est un signal d'alerte. Si le cours clôture sous la MM50 à la prochaine session → réduire de 30–50%.
- Premier support à surveiller : **$52.76** (low du 23/06, testé et défendu)
- Deuxième support : **$54.69** (MM50) — cassure en clôture = révision en ATTENDRE
- Troisième support : **$52.30** (low du 2026-06-09)
- Si rupture sous **$54.69** (MM50) en clôture sans rebond → **passer en ATTENDRE** et réduire la position
- Si rupture sous **$52.30** (low du 09/06) → **stopper toute position existante**
- Si rupture sous **$44.24** (SL 2×ATR) → **stopper la position**

> **⚠️ Réserve earnings :** Les résultats Q1 2026 ne sont toujours pas intégrés dans les feeds (FY 2025 uniquement). Toute position IREN est soumise à un risque de publication surprise élevé. Prochain earnings Q2 2026 : **2026-08-27** (65 jours). [DONNÉES PARTIELLES] — Quality Partielle 4/6, Forward PE négatif, FCF négatif. Baisse de −2.44% sur volume très faible (41.7% moyenne 20j) = pas de conviction vendeuse, mais pas d'accumulation non plus. L'upgrade algorithmique est à valider par un rebond sur volume à la session suivante.

---

*Rapport rédigé le 2026-06-23 — Données sources : `data/latest.json` (fetched_at 2026-06-23T17:00:02 UTC), `data/recommandations_latest.json`, `data/quant_report_latest.json`, `data/geo_risk_latest.json`, `data/sector_rotation_latest.json`, `data/social_sentiment_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json`, `data/events_latest.json`.*

# PLTR — Mise à Jour Quotidienne (2026-06-08, snapshot 10:00 UTC)

> **Source :** `data/2026-06-08.json` (snapshot 10:00 UTC, fetched_at 2026-06-08T10:00:10Z) + agents quant, geo, accounting, sector, social, FX, watchman, events
> **Référence précédente :** [PLTR_2026-06-03_13-00_update.md](PLTR_2026-06-03_13-00_update.md) (snapshot 13:00 UTC)
> **Contexte :** **Gap baissier de −4.35%** ce matin et **cassure sous MM50** après 4 jours de fermeture du marché (week-end + gap post-séance). Le cours est revenu de $152.17 à $135.53 (−10.9% vs dernier snapshot analysé), invalidant le retournement haussier de court terme initié le 01/06. RSI sorti de la zone élevée (64.74 → 51.25), ATR en expansion ($6.69 → $7.29), volume faible (38.11M = 0.93× moyenne). Options anomalie JSON détectée (Max Pain $50.00 aberrant). Thèse **modifiée** : passage **ATTENDRE → SURVEILLER**.

---

## Résumé des Changements depuis l'Analyse Précédente (2026-06-03 13:00 UTC)

| Indicateur | Snapshot 03/06 13:00 UTC | Snapshot 08/06 10:00 UTC | Δ vs Prior |
|-----------|-------------------------|-------------------------|------------|
| Cours close | $152.17 | **$135.53** | **−10.93%** — gap baissier + continuation |
| Change % vs prev close | −5.28% | **−4.35%** | Gap overnight baissier ce matin |
| Open du jour | $156.69 | **$140.33** | −10.5% — ouverture sous le close précédent |
| High intraday | $159.55 | **$141.97** | −11.0% — rejet immédiat sous $142 |
| Low intraday | $149.80 | **$134.03** | −10.5% — test du support $134 |
| RSI 14j | 64.74 | **51.25** | **−13.49 pts** — retour en zone neutre |
| ATR 14j | $6.69 | **$7.29** | **+$0.60 / +8.97%** — expansion volatilité |
| MM 50j | $141.92 | **$140.90** | −$1.02 / −0.72% — légère décroissance |
| Volume du jour | 42.73M vs 44.89M avg | **38.11M vs 41.14M avg** | −10.8% — **0.93× moyenne**, sous-moyen |
| Short Interest | 3.31% | **3.31%** | Inchangé — pas de squeeze setup |
| Consensus FMP PT | $186.15 (34 analystes) | **$186.15 (34 analystes)** | Inchangé — aucune révision |
| Upside vs PT | +22.3% | **+37.4%** | Mécanique (baisse du cours) — upside artificiellement gonflé |
| P/E Yahoo (LTM) | 172.9x | **152.3x** | Mécanique — baisse du cours |
| Forward P/E Yahoo | 73.4x | **65.3x** | Mécanique |
| Options Max Pain | $160.00 | **$50.00 ([ANOMALIE JSON])** | 🔴 Anomalie détectée — valeur opérationnelle non disponible |
| Options Put/Call | 0.48 | **null ([ANOMALIE JSON])** | 🔴 Données corrompues dans snapshot |
| Options Call OI % | 67.4% | **null ([ANOMALIE JSON])** | 🔴 Données corrompues dans snapshot |
| Score Opportunité agent | 5.2/10 | **5.3/10** | **+0.1 pt** — valorisation mécaniquement moins extrême |
| Score Global ajusté | 56.8/100 | **45.0/100** | **−11.8 pts** — malus timing défavorable (cassure MM50) |
| Recommandation agent | ATTENDRE | **SURVEILLER** | 🔴 **Modifiée** — invalidation technique |
| Stop-loss agent | $138.79 | **$120.95** | Révisé à la baisse (ATR + cours plus bas) |
| Take-profit agent | $172.24 | **$157.40** | Révisé à la baisse |

**Verdict :** Le snapshot du 2026-06-08 enregistre une **détérioration technique majeure** par rapport au snapshot du 03/06. Le cours a chuté de −10.9% ($152.17 → $135.53), invalidant le franchissement haussier de la MM50 initié le 01/06. Le RSI est retombé en zone neutre (51.25), l'ATR s'est expandu (+8.97%) et le volume reste faible (0.93× moyenne), confirmant une absence d'achat institutionnel sur les niveaux actuels. La structure options est à nouveau corrompue dans `latest.json` (anomalie identique au 01/06 et 03/06 10h). Le Score Global ajusté est passé de 56.8 à 45.0/100, entraînant un **changement de recommandation de ATTENDRE à SURVEILLER**.

> **[DONNÉES VALIDATION WARNING]** — `data/validation_report.txt` du 2026-06-08 enregistre **5 erreurs globales** (VRT schema violation, AST/AXA/ASTSPACE/QTBS fetch failed) et 3 warnings. **PLTR est OK** (0 error, 0 warning). Le pipeline n'est pas bloqué pour PLTR.

---

## Mise à Jour Technique

| Indicateur | Valeur | Signal |
|-----------|--------|--------|
| Cours | $135.53 | −4.35% vs previous close ($141.70) ; −10.93% vs dernier snapshot analysé ($152.17) |
| RSI 14j | 51.25 | 🟢 **Neutre** — sortie complète de la zone élevée (>60), zone d'entrée potentielle si momentum se confirme |
| ATR 14j | $7.29 | 🟡 **Expansion** (+8.97% vs 03/06) — volatilité en hausse, élargissement des bandes |
| MM 50j | $140.90 | 🔴 Cours **−3.8% sous MM50** — **invalidation du retournement haussier** de court terme |
| MM 200j | null | [DONNÉES MANQUANTES] |
| Volume 20j | 41,140,970 | 🟡 **38.11M = 0.93× moyenne** — volume faible sur la baisse, pas de capitulation |
| Volume jour | 38,108,100 | −10.8% vs snapshot 03/06, sous-moyen — signal de faiblesse |
| 52W Range | $118.93–$207.52 | Cours à 30.7% du 52W low, 34.7% sous le 52W high |
| Support clé | $134.03 | Low intraday — zone de défense immédiate testée ce matin |
| Support secondaire | $130.00 | Zone psychologique — gap de consolidation du 23–26/05 |
| Support ATR | $120.95 | Cours − 2×ATR = $135.53 − $14.58 |
| Support MM50 | $140.90 | Résistance dynamique désormais — ancien support devenu résistance |
| Résistance | $141.97 | High intraday — rejet immédiat sous $142 |
| Résistance majeure | $160.00 | Max Pain opérationnel (dernière valeur valide 03/06) — écart +18.1% |
| Résistance consensus | $186.15 | Price Target moyen FMP (34 analystes) — écart +37.4% |
| Short Interest | 3.31% | 🟡 Modéré — inchangé, pas de setup short squeeze |

**Options — Anomalie JSON Récurrente :**

| Métrique | Valeur opérationnelle (03/06 13:00 UTC) | Valeur JSON 08/06 10:00 UTC | Interprétation |
|----------|----------------------------------------|---------------------------|----------------|
| Put/Call Ratio | 0.48 | **null** | 🔴 Anomalie JSON identique au pattern 01/06 et 03/06 10h |
| Max Pain | $160.00 | **$50.00 (aberrant)** | 🔴 Valeur corrompue — non exploitable |
| Call OI % | 67.4% | **null** | 🔴 Anomalie JSON |
| Expiration proche | 2026-06-05 | **2026-06-12** | Nouvelle expiration vendredi prochain (4 jours) |

> **Note anomalie :** Le fichier `data/2026-06-08.json` retourne à nouveau des valeurs options aberrantes pour PLTR (`max_pain: 50.0`, `put_call_ratio: null`, `call_oi_pct: null`). Ce pattern est récurrent sur les snapshots 10h UTC (01/06, 03/06 10h, 08/06). Les valeurs opérationnelles du snapshot 03/06 13:00 UTC ($160.00 / 0.48 / 67.4%) restent la dernière référence valide. L'expiration proche a glissé au 2026-06-12 (4 jours). Le Max Pain opérationnel $160.00 constitue désormais une résistance éloignée (+18.1%).

**Interprétation technique :**
- **RSI 51.25** : 🟢 Retour en zone neutre. La sortie de la zone élevée (>60) est positive pour un potentiel d'entrée, mais le RSI seul n'est pas suffisant sans confirmation de volume et de support.
- **Cassure MM50 ($140.90)** : 🔴 **Signal baissier majeur**. Le retournement haussier initié le 01/06 (franchissement à $156.54) est invalidé. La MM50 redevient une résistance dynamique. Tant que le cours reste sous $140.90, la tendance de court terme est baissière.
- **Volume 38.11M (0.93× moyenne)** : 🟡 La baisse de −10.9% s'est faite sur un volume légèrement sous la moyenne. Pas de capitulation, pas de panique, mais pas de soutien acheteur non plus. C'est un "sinking on low volume" — typique d'un manque de conviction.
- **ATR $7.29** : 🟡 Expansion de volatilité (+8.97%). Les swings intrajournaliers s'élargissent. Le range ATR-based élargit les stops.
- **Low intraday $134.03** : Zone de support immédiat. Un test sous $134 sur volume faible ouvrirait la voie vers $130.
- **Niveau critique : $140.90** (MM50). Un retour en clôture au-dessus de ce niveau est nécessaire pour réactiver la thèse haussière de court terme.
- **Niveau de vigilance : $134.03** (low du jour). Cassure = test de $130 puis $120.95 (SL).

---

## Mise à Jour Fondamentale

### Consensus Analystes — Stable
- **Price Target moyen FMP : $186.15** (34 analystes, 1 mise à jour le mois dernier, 6 le trimestre dernier)
- **Upside implicite : +37.4%** vs cours $135.53 — mécaniquement gonflé par la chute du cours, pas par une révision haussière
- **Couverture :** 34 analystes — coverage significatif et actif, inchangé

> **Note :** Aucune révision de consensus entre le 03/06 et le 08/06. Aucune mise à jour d'analyste détectée. Le consensus ne justifie pas la baisse de −10.9%.

### Ratios FMP / Yahoo — Mécaniquement Atténués (Cours Plus Bas)
| Ratio | Valeur (Yahoo snapshot 08/06) | Valeur (FMP FY2025) | Signal |
|-------|-------------------------------|---------------------|--------|
| Market Cap | $324.9 Md | $421.2 Md | 🔴 Écart +29.6% entre sources — FMP retardé |
| P/E (LTM) | 152.3x | 259.2x | 🔴 Extrême (moins qu'avant, mais encore extrême) |
| Forward P/E | 65.3x | — | 🔴 Élevé |
| EV/Revenue | 60.7x | 93.8x | 🔴 Extrême |
| EV/EBITDA | 157.2x | 291.6x | 🔴 Extrême |
| P/B | 38.4x | 57.0x | 🔴 Extrême |
| Gross Margin | — | 82.4% | 🟢 Excellente |
| Operating Margin | — | 31.6% | 🟢 Très élevée |
| Net Margin | — | 36.3% | 🟢 Excellente |
| Current Ratio | — | 7.11 | 🟢 Liquidité exceptionnelle |
| Debt/Equity | — | 0.031 | 🟢 Quasi-zero dette |
| ROIC (FMP) | — | 17.9% | 🟢 Création de valeur confirmée |
| SBC / Revenue | — | 15.3% | 🔴 Dilution significative |

**Interprétation :** Les fondamentaux de qualité restent intacts (marges élevées, bilan quasi-sans dette, ROIC 18%). La baisse du cours a mécaniquement amélioré les multiples (P/E de 172.9x à 152.3x, EV/Revenue de 68.4x à 60.7x), mais ils restent **extrêmes et incompatibles avec un environnement de taux élevés**. Aucun changement qualitatif sur les fondamentaux — la baisse est purement technique.

### Filtre Qualité (6 critères)
- Données Agent Accounting (M-Score, Z-Score, F-Score, Sloan) : `[DONNÉES MANQUANTES]` — fichier `data/accounting_risk_latest.json` toujours absent
- Score Qualité : `[NON ÉVALUABLE]` sur les critères comptables
- Sur les critères qualitatifs disponibles (marges, bilan, ROIC) : fondamentaux solides inchangés
- Verdict : Le Filtre Qualité ne peut pas être pleinement appliqué sans les signaux comptable agents. Cette absence est un risque méthodologique persistant.

---

## Mise à Jour Sentiment / Options / Flux / Macro

### Sentiment Analystes
- **Actif :** 34 analystes FMP, PT $186.15. Aucune mise à jour entre le 03/06 et le 08/06.
- **Implication :** L'absence de downgrade malgré une baisse de −10.9% suggère que le consensus institutionnel considère le mouvement comme technique. Cependant, la faiblesse du volume indique un désengagement plutôt qu'un achat institutionnel.

### Social Sentiment
- **Reddit / Yahoo Community :** 0 mentions. Aucun pump/dump détecté.
- **Label agent :** No data — absence de buzz retail. La baisse n'est pas portée par un sentiment retail extrême.

### Options — Anomalie JSON Récurrente
- **Put/Call** : null (anomalie JSON) — dernière valeur valide 0.48 (03/06 13:00 UTC)
- **Max Pain** : $50.00 (aberrant) — dernière valeur valide $160.00 (03/06 13:00 UTC)
- **Call OI %** : null (anomalie JSON) — dernière valeur valide 67.4% (03/06 13:00 UTC)
- **Expiration proche** : 2026-06-12 (4 jours)
- **Interprétation :** La structure options réelle est inconnue pour ce snapshot. Le pattern d'anomalie 10h UTC suggère un bug de parsing JSON côté Yahoo. En l'absence de données valides, on conserve la dernière structure connue (biais call modéré) comme hypothèse de travail, mais avec un niveau de confiance faible.

### Exposition Macro
| Facteur | Exposition | Mise à jour |
|---------|-----------|-------------|
| Taux 10Y US | 🟡 Modérée | Inchangée — Beta 1.515 amplifie les rotations sectorielles |
| Pétrole (WTI) | 🟢 Faible | Inchangée — business model software |
| DXY | 🟡 Modérée | 🟢 FX Exposure Score 0.0 (neutral, pas de headwind/tailwind) |
| Technology (XLK) | 🟢 Favorable | **XLK reste top sectoriel mais momentum atténué** (RS20 vs SPY +5.44% vs +16.5% le 03/06) |

### Sector Rotation
- **Technology (XLK)** : return 20d +6.25%, RS20 vs SPY +5.44%. **Top1** du ranking sectoriel avec momentum score 10.0/10.
- **Signal :** NEUTRAL (régime inconnu)
- **Impact :** 🟡 **Vent de secteur atténué**. XLK reste le top sectoriel, mais la force relative 20j a chuté de +16.5% (03/06) à +5.44% (08/06) — le momentum sectoriel s'est fortement dégradé. PLTR bénéficie moins du vent de secteur qu'il y a 5 jours.

### Géopolitique
- **Score Politique :** 2/10 (`geo_risk_latest.json`, date 2026-05-17) — PLTR faiblement exposé aux événements géopolitiques actuels.
- **Pas d'ajustement** sur le score global.

### Accounting Risk / Quant
- **Accounting risk :** Fichier `accounting_risk_latest.json` **indisponible**. Le Filtre Qualité ne peut pas être appliqué.
- **Quant report :** Données insuffisantes — 0 signaux historiques (n=0), calibration en cours. Pas d'alerte de significativité.

---

## Score Opportunité Révisé

| Axe | 03/06 13:00 UTC /10 | 08/06 10:00 UTC /10 | Δ | Justification |
|-----|----------------------|----------------------|---|---------------|
| Catalyseur | 6.3 | **6.8** | +0.5 | Consensus PT $186.15 inchangé. Earnings 08/03 reste le catalyseur clé. Aucune news structurante, mais le calendrier avance (56 jours). |
| Valorisation | 4.0 | **4.5** | +0.5 | Multiples mécaniquement plus bas (P/E 152x vs 173x, EV/Rev 60.7x vs 68.4x), mais toujours extrêmes. |
| Momentum | 5.5 | **4.5** | −1.0 | RSI retombé en zone neutre (positif), mais **cassure sous MM50** = signal baissier de court terme. Volume faible = absence de confirmation. |
| **Score Opportunité** | **5.2** | **5.3** | **+0.1** | Pondération 35/40/25 (régime inconnu = default). Le léger gain provient de la valorisation, compensé par le momentum baissier. |

**Score Global Composite agent :** 53.0/100 → **Ajusté 45.0/100**
- Malus : geo 0, FX 0, event 0, social 0, quant 0
- Timing : **Défavorable** (cassure MM50, volume faible sur la baisse) → malus estimé **−8.0 pts**
- **Recommandation agent : SURVEILLER**

**Verdict institutionnel Argus-IA :** La thèse est **MODIFIÉE** — passage de **ATTENDRE à SURVEILLER**. Le Score Opportunité est quasi stable (5.2 → 5.3/10), mais le Score Global ajusté a chuté de 11.8 points (56.8 → 45.0/100) en raison du **timing défavorable** lié à la cassure sous MM50 ($140.90). Le cours a perdu −10.9% en 5 jours, invalidant le retournement haussier du 01/06. Le mouvement est purement technique (pas de news, pas de downgrade, fondamentaux inchangés), mais la structure technique de court terme est dégradée.

---

## Niveaux SL / TP Révisés

| | 03/06 13:00 UTC | 08/06 10:00 UTC | Justification |
|---|-------------------|-------------------|---------------|
| Entrée suggérée | Attendre $145–$149 | **Attendre retour > $140.90 (MM50)** | La zone d'observation précédente est invalidée par la cassure. Nouveau critère : clôture au-dessus de MM50 + volume > 40M. |
| Stop-Loss | $138.79 | **$120.95** | Cours − 2×ATR = $135.53 − $14.58. ATR expandu. |
| Take-Profit | $172.24 | **$157.40** | Cours + 3×ATR = $135.53 + $21.87. TP conservateur vs consensus $186.15. |
| Ratio R/R | 1.5 | **1.5** | — |

**Note institutionnelle :** Les niveaux sont révisés à la baisse en raison de la baisse du cours et de l'expansion de l'ATR. Le SL $120.95 correspond à la zone $121–$125 (support technique + gap de consolidation historique). Le TP $157.40 est conservateur par rapport au consensus $186.15. Tant que le cours reste sous MM50 ($140.90), aucune entrée n'est justifiée — la tendance de court terme est baissière.

---

## Conclusion — Thèse Confirmée, Modifiée ou Invalidée ?

**Verdict : MODIFIÉE — Passage ATTENDRE → SURVEILLER.**

Le snapshot du 2026-06-08 enregistre une **détérioration technique majeure** par rapport au snapshot du 03/06. Le cours a chuté de −10.9% ($152.17 → $135.53), invalidant le retournement haussier de court terme initié le 01/06. La **cassure sous MM50 ($140.90)** est le signal clé : la tendance de court terme est de nouveau baissière. Le RSI est retombé en zone neutre (51.25), ce qui est mécaniquement positif pour une entrée future, mais il n'y a aucune confirmation de volume (38.11M = 0.93× moyenne) ni de support institutionnel. L'absence totale de news structurante pour PLTR dans le snapshot du jour confirme que le mouvement est technique et non fondamental.

### Ce qui a changé (snapshot 08/06 2026-06-08) :
1. **🔴 Cours −10.93%** : $152.17 → $135.53. Gap baissier ce matin.
2. **🔴 Cassure MM50** : Cours $135.53 sous MM50 $140.90 (−3.8%). Invalidation du retournement haussier.
3. **🟢 RSI 51.25** : Sortie de la zone élevée (64.74 → 51.25), retour en zone neutre — amélioration potentielle pour timing d'entrée futur.
4. **🟡 ATR $7.29** : Expansion de volatilité (+8.97%).
5. **🟡 Volume 38.11M** : Sous-moyen (0.93×) sur la baisse — pas de capitulation, pas de soutien.
6. **🔴 Anomalie options JSON** : Max Pain $50.00 aberrant, Put/Call et Call OI null — pattern récurrent 10h UTC.
7. **🟡 Sector Rotation XLK** : RS20 vs SPY +5.44% (vs +16.5% le 03/06) — vent de secteur atténué.
8. **🔴 Score Global ajusté 45.0/100** : Chute de 11.8 pts (56.8 → 45.0), passage sous le seuil ATTENDRE.
9. **🔴 Recommandation SURVEILLER** : Passage de ATTENDRE à SURVEILLER.
10. **🟢 Multiples mécaniquement plus bas** : P/E 152x, EV/Rev 60.7x, Forward P/E 65.3x — valorisation légèrement moins extrême.

### Ce qui n'a PAS changé :
1. **Consensus analyste FMP** : PT $186.15 inchangé (34 analystes) — aucune révision.
2. **Short Interest 3.31%** — pas de squeeze.
3. **Fondamentaux FMP FY2025** : marges excellentes (82/32/36%), bilan quasi-sans dette, ROIC 18% inchangés.
4. **Aucun événement corporate** (`data/events_2026-06-08.json` vide pour PLTR).
5. **Aucune news structurante** (`data/news_2026-06-08.json` vide pour PLTR).
6. **Accounting risk non quantifié** — absence persistante.
7. **Geo risk score 2/10** — exposition négligeable.
8. **Social sentiment 0 mentions** — pas de buzz retail.
9. **Earnings Q2 FY2026** : 2026-08-03 (56 jours) — catalyseur clé inchangé.
10. **FX Exposure Score 0.0** — neutral.
11. **SBC / Revenue 15.3%** — dilution significative persistante.

### Risques identifiés (snapshot 08/06 2026-06-08)
1. **Cassure MM50** — 🔴 Signal baissier de court terme. Retour au-dessus de $140.90 en clôture nécessaire pour réactiver la thèse haussière.
2. **Volume faible sur la baisse** — 🟡 Pas de capitulation = la baisse peut continuer par manque d'acheteurs.
3. **ATR en expansion** — 🟡 Volatilité croissante, swings élargis.
4. **Valorisation extrême** — 🔴 Multiples restent incompatibles avec un environnement de taux élevés, même mécaniquement atténués.
5. **Beta 1.515** — 🟡 En cas de correction tech globale, PLTR surperformerait à la baisse.
6. **Accounting risk non quantifié** — 🟡 Absence de scan comptable.
7. **Anomalie options JSON** — 🟡 Impossibilité de valider la structure options réelle.
8. **SBC / Revenue 15.3%** — 🔴 Dilution significative via stock-based compensation.
9. **Écart consensus/cours +37.4%** — 🟡 Si le consensus ne se révise pas à la hausse, l'upside est purement mécanique et fragile.

### Positionnement Argus-IA
- **Action : SURVEILLER** — Pas d'entrée. La cassure sous MM50 invalide le setup technique de court terme.
- **Horizon :** 1–3 mois (jusqu'à earnings Q2 FY2026 le 03/08)
- **Catalyseur clé :** Earnings 2026-08-03 (Est. EPS $0.32–$0.40, Rev $1.8B). Préparer `_preview.md` à ≤ 5j.
- **Si retour > $140.90 (MM50) en clôture + volume > 40M :** Réactivation de la thèse ATTENDRE — la tendance haussière de court terme serait rétablie.
- **Si consolidation > $135 sur volume > 40M sur 2–3 jours :** Signal de stabilisation — réévaluer vers ATTENDRE.
- **Si test de $130–$134 sur volume faible :** Zone d'observation pour accumulation potentielle, mais risque de cassure.
- **Si cassure < $130 en clôture :** Risque de retour vers $120.95 (SL) — renforcement de la thèse SURVEILLER/ÉVITER.
- **Si pullback vers $121–$125 (zone SL) :** Zone d'entrée idéale (support ATR + gap historique) mais forte probabilité de continuation baissière si momentum négatif.

---

## [UNSOURCED]
- MACD, MM200, IV Rank, earnings whisper, insider trades détaillés, 13F complets, ETF flows, dark pool, transcripts NLP, job postings.
- Accounting risk (M-Score, Z-Score, F-Score, Sloan) — fichier `data/accounting_risk_latest.json` indisponible.
- Données quantitatives significatives (p-value, Sharpe) — insuffisantes (n=0).
- Options réelles (Put/Call, Call OI, Max Pain valide) — anomalie JSON dans snapshot 10h UTC.

---

## Références
- `data/2026-06-08.json` (snapshot 10:00 UTC) — Cours $135.53, RSI 51.25, ATR $7.29, MM50 $140.90, volume 38,108,100, short interest 3.31%, consensus FMP $186.15, options anomalie (max_pain $50.00 aberrant)
- `data/recommandations_2026-06-08.json` — Score Opportunité 5.3/10, Score Global 53.0/100 (ajusté 45.0), Recommandation SURVEILLER, SL $120.95, TP $157.40
- `data/validation_report.txt` (2026-06-08) — PLTR OK, 0 warning, 0 error. 5 erreurs globales non-impactantes pour PLTR.
- `data/sector_rotation_2026-06-08.json` — XLK top sector (momentum 10.0/10, RS20 +5.44%)
- `data/fx_exposure_2026-06-08.json` — FX Impact Score 0.0, neutral
- `data/social_sentiment_2026-06-08.json` — Sentiment retail 0 mentions (No data)
- `data/upcoming_events_2026-06-08.json` — Earnings 2026-08-03, 56 jours
- `data/events_2026-06-08.json` — Aucun événement corporate détecté pour PLTR
- `data/news_2026-06-08.json` — Aucune news détectée pour PLTR
- `data/geo_risk_latest.json` (2026-05-17) — Geo Risk Score 2/10, exposition négligeable
- `data/quant_report_latest.json` — Données quantitatives insuffisantes (n=0)
- Agents/AGENT_FONDAMENTAL.md — Méthodologie Filtre Qualité
- Agents/AGENT_TECHNIQUE.md — Méthodologie technique
- Agents/AGENT_SENTIMENT.md — Méthodologie sentiment

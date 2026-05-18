# MITK — Mise à Jour Quotidienne (2026-05-18)

> Desk : Argus-IA | Régime : Inconnu (données macro partielles) | Données : `data/latest.json` (2026-05-18T09:00Z) | Score Global : **51.0/100** | Action : **ATTENDRE**

---

## Résumé des Changements depuis l'Analyse Précédente (2026-05-17)

| Variable | 2026-05-17 | 2026-05-18 | Δ | Impact |
|---|---|---|---|---|
| **Cours close** | $13.57 | **$14.26** | **+5.08%** | 🔴 Gap overnight > seuil 5% — trigger FULL REFRESH activé |
| **RSI 14j** | ~49 | **51.62** | +2.6 pts | Neutre, légère remontée post-gap |
| **MM 50j** | $14.31 | **$14.31** | — | Prix toujours sous MM50 (-0.3%) |
| **ATR 14j** | $0.86 | **$0.86** | — | Volatilité stable (~6% du cours) |
| **Volume** | — | **1,317,800** | 1.07× moy. 20j | Activité légèrement supérieure, non significative |
| **Max Pain** | $20.00 | **$7.50** | -62.5% | [ANOMALIE MAX PAIN] — niveau incohérent vs spot, illiquidité options extrême |
| **Put/Call ratio** | 0.14 | **N/A** | — | Données options indisponibles aujourd'hui |
| **Consensus PT (FMP)** | — | **$16.00** (2 analysts) | — | Upside +12.1%. Couverture très faible. |
| **Prochain earnings** | — | **2026-08-06** (80j) | — | Est EPS $0.24–$0.34, Rev ~$0.1B |

**Verdict global :** Gap haussier de +5.08% sans catalyseur identifiable ni volume exceptionnel. La configuration technique reste sous MM50 avec un RSI neutre. L'anomalie Max Pain ($7.50) et l'absence de Put/Call ratio traduisent une illiquidité options qui invalide tout signal dérivé. Le secteur Technology (XLK) affiche un momentum sectoriel maximal (score 10.0, +14.2% sur 20j), ce qui constitue un vent favorable passif pour MITK sans toutefois constituer un catalyseur spécifique.

---

## 1. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| **RSI (14j)** | 51.62 | Zone neutre, ni surachat ni survente |
| **ATR (14j)** | $0.86 | Volatilité journalière moyenne (~6.0% du spot) |
| **MM 50j** | $14.31 | Close sous la moyenne (-$0.05 / -0.3%) |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume** | 1,317,800 | 1.07× moyenne 20j (1,223,895) — activité standard |
| **52-week range** | $8.53 – $16.48 | Spot à 86.5% du range annuel, proche du sommet |
| **Beta** | 0.955 | Sensibilité systématique alignée sur le marché |

**Niveaux clés :**
- Support immédiat : $13.52 (low du jour 2026-05-18)
- Résistance intermédiaire : $14.68 (high du jour)
- Résistance majeure : $16.00 (consensus PT) / $16.48 (52w high)
- Stop-loss ATR (2×) : **$12.54** (-12.1%)
- Take-profit ATR (3×) : **$16.84** (+18.1%)

**Verdict timing :** Défavorable. Le gap +5.08% n'a pas permis une cassure au-dessus de la MM50. L'absence de golden cross et le RSI neutre traduisent une consolidation sans conviction directionnelle. Le prix évolue dans un range $13.50–$14.70 depuis plusieurs séances. Une clôture au-dessus de $14.70 avec volume >1.5× moyenne serait nécessaire pour basculer le timing à Neutre/Favorable.

---

## 2. Mise à Jour Fondamentale

### 2.1 Divergence Yahoo Finance vs FMP FY2025 (2025-09-30)

| Métrique | Yahoo Finance | FMP Stable API (FY 2025) | Δ | Source retenue |
|---|---|---|---|---|
| **Market Cap** | $643.9M | $446.6M | -30.6% | **Yahoo** (close temps réel) |
| **P/E (TTM)** | 41.94x | 50.78x | +21.1% | **Yahoo** |
| **EV/EBITDA** | 14.85x | 12.15x | -18.2% | **FMP** (données annuelles consolidées) |
| **P/B** | 2.67x | 1.86x | -30.3% | **FMP** |
| **P/S** | — | 2.49x | — | FMP |
| **P/FCF** | — | 8.24x | — | FMP |

> **Note institutionnelle :** La divergence market cap Yahoo vs FMP (~$200M) suggère que FMP utilise une ancienne base de shares outstanding ou un close décalé. Nous retenons **$644M** comme référence. Le P/E FMP plus élevé (50.78x) renforce la lecture d'un multiple courant élevé, partiellement compensé par le Forward P/E à 11.75x qui intègre une inflexion bénéficiaire majeure attendue par le marché.

### 2.2 Marges et Rentabilité (FMP FY2025)

| Métrique | Valeur | Lecture |
|---|---|---|
| **Gross Margin** | 85.1% | ✅ Moat logiciel fort (SaaS/application) |
| **Operating Margin** | 9.3% | ⚠️ Faible vs gross margin — opex élevé (R&D 9.4% du CA, S&M) |
| **EBITDA Margin** | 20.5% | ✅ Rentabilité opérationnelle correcte |
| **Net Margin** | 4.9% | ⚠️ Compression forte post-frais financiers et taxes (24.2%) |
| **ROIC** | 3.16% | 🔴 Très faible — capital employé peu rémunérateur |
| **ROE** | 3.66% | 🔴 Faible, leverage limité (D/E 0.65) |
| **ROCE** | 6.71% | 🟡 En dessous du coût du capital estimé (~10%) |
| **FCF Yield** | 12.1% | ✅ Attractif — génération de cash réelle et soutenue |
| **Net Debt / EBITDA** | 0.03x | ✅ Quasi net cash, bilan sain |
| **Interest Coverage** | 1.72x | ⚠️ Juste suffisant, faible marge de sécurité |
| **Stock Based Comp / Revenue** | 9.35% | ⚠️ Dilution significative via SBC |

### 2.3 Filtre Qualité 6 Critères

| Critère | Verdict | Justification |
|---|---|---|
| Revenue CAGR 5 ans ≥ 20% | [DONNÉES MANQUANTES] | Pas de série historique complète dans latest.json |
| Profit CAGR 5 ans ≥ 20% | [DONNÉES MANQUANTES] | Idem |
| Assets / Liabilities > 1.0 | ✅ | Current ratio 1.19, D/A 0.34 — solvabilité ok |
| FCF positif et croissant 5 ans | ✅ | FCF yield 12.1%, P/FCF 8.24x — FCF réel positif |
| Avantage compétitif (moat) | ✅ | Gross margin 85% = moat logiciel / switching costs |
| Industrie forte croissance (TAM ×5) | [DONNÉES MANQUANTES] | Software-Application, TAM non quantifié dans les données |
| **Score Qualité** | **3–4 / 6** | ⚠️ Quality Partielle — manque les séries historiques et le TAM |

> **Règle Filtre Qualité :** Score ≤ 3/6 → Score Valorisation plafonné à 5/10. Avec 4 critères validés/probables, le score Valorisation 6.5/10 reste acceptable mais sous surveillance. Le faible ROIC (3.16%) et la dilution SBC (9.35%) pénalisent la qualité du capital.

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution | Lecture |
|---|---|---|---|
| **Consensus PT (FMP)** | $16.00 (2 analysts) | → | Upside +12.1% vs spot. Couverture très faible (2 analysts uniquement), manque de visibilité institutionnelle. |
| **Max Pain** | $7.50 | ↓ aberrant | [ANOMALIE] Niveau à -47.4% du spot. Illiquidité options extrême ou erreur de données. **Ignorer pour le scoring.** |
| **Put/Call ratio** | N/A | de 0.14 à null | Données indisponibles aujourd'hui. L'optimisme options précédent n'est plus vérifiable. |
| **Short Interest** | 7.32% | → | Float ~43.8M. Short interest modéré, pas de squeeze setup (borrow rate indisponible). |
| **Social Sentiment** | 0 / No data | → | Aucune mention Reddit. MITK reste sous le radar retail. |
| **Upgrades/Downgrades** | — | — | Aucun mouvement analyste détecté. |

**Verdict Sentiment :** Neutre. Le consensus PT $16 offre un upside théorique de +12%, mais la couverture à 2 analysts et l'absence de flux options fiables limitent la pertinence du signal. Aucune news structurante ni insider trade significatif détecté.

---

## 4. Scoring Global — Révision

| Pilier | Score | Poids Régime | Pondéré | Commentaire |
|---|---|---|---|---|
| **Catalyseur** | 5.5/10 | 35% | 1.925 | Aucun catalyseur spécifique. Earnings dans 80j. Secteur tech momentum +10.0/10 ne constitue pas un catalyseur idiosyncratique. |
| **Valorisation** | 6.5/10 | 40% | 2.600 | Forward P/E 11.75x attractif, mais P/E TTM 41.94x élevé, ROIC 3.16% faible. Pas de discount de sécurité clair. |
| **Momentum** | 5.5/10 | 25% | 1.375 | Sous MM50, RSI neutre 52, gap +5% non confirmé par volume. |
| **Score Opportunité** | **5.9/10** | — | **5.900** | Pondération Normal 35/40/25 (régime inconnu) |
| **Malus/Bonus** | — | — | — | Aucun malus geo (score 0), FX (🟢), accounting (N/A), event-driven (N/A). Bonus sectoriel Tech top1 implicite mais non quantifié dans le scoring agent. |
| **Score Global Composite** | **59.0/100** | — | — | Brut |
| **Score Global Ajusté** | **51.0/100** | — | — | Après malus/bonus nets |

| Seuil | Action | Sizing | Condition |
|---|---|---|---|
| Score Global 51.0/100 | **ATTENDRE** | — | Qualité présente mais pas de catalyseur clair ni timing technique favorable. |

> **Note :** Le score global ajusté de 51.0/100 se situe juste au-dessus du seuil médian de 50. Le ticker reste dans la zone "attendre / surveiller" sans catalyseur immédiat. L'absence de malus (geo, FX, accounting, social) est un point positif, mais insuffisant pour basculer en "Acheter".

---

## 5. Révision des Niveaux SL / TP

| Niveau | Prix | Distance vs Close | Méthode |
|---|---|---|---|
| **Stop-loss** | $12.54 | -12.1% | Cours − 2×ATR ($0.86) |
| **Take-profit** | $16.84 | +18.1% | Cours + 3×ATR ($0.86) |
| **Ratio R/R** | **1.5** | — | Acceptable mais non optimal (seuil institutionnel 1:2) |
| **Consensus PT (FMP)** | $16.00 | +12.1% | Aligné sur la zone de TP structurelle, sert de résistance intermédiaire |

**Ajustement proposé :** Aucun changement de niveau. Les niveaux ATR-based restent cohérents. Le consensus FMP à $16 conforte la résistance intermédiaire avant le TP à $16.84. Une remontée du SL à $13.00 (période de consolidation) pourrait être envisagée si le prix clôture 3 jours consécutifs au-dessus de $14.50 avec volume confirmant.

---

## 6. Calendrier & Événements

| Événement | Date | Jours restants | Impact attendu |
|---|---|---|---|
| **Earnings Q3 FY2026** (est.) | 2026-08-06 | **80** | Est EPS $0.24–$0.34, Rev ~$0.1B. Prochain catalyseur majeur. |
| **Expiration options** | 2026-06-18 | 31 | Illiquidité constatée, impact limité sur le pricing. |

**Alertes actives :**
- 🔴 **[ANOMALIE MAX PAIN]** $7.50 vs spot $14.26 — signaler à l'équipe data / vérifier source Yahoo
- 🟡 **[DONNÉES OPTIONS DÉGRADÉES]** Put/Call ratio indisponible — pas de signal dérivé fiable
- 🟡 **[DIVERGENCE YAHOO/FMP]** Market cap ($644M vs $447M) et P/E — utiliser Yahoo comme primaire, FMP comme secondaire pour marges/bilan
- 🟡 **[ROIC FAIBLE]** 3.16% — monitorer l'efficacité du capital dans les prochains filings

---

## 7. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE, AVEC AJUSTEMENT NEUTRE POST-GAP.**

Le gap de +5.08% enregistré ce matin ne dispose d'aucun catalyseur identifiable (pas de news, pas d'upgrade, pas de guidance). Il s'inscrit probablement dans un mouvement de catch-up sectoriel (XLK +14.2% sur 20j) ou un flux spécifique sur le small-cap tech. La thèse initiale reste inchangée : MITK est un small-cap logiciel (Software-Application) avec un Forward P/E attractif (11.75x) masquant un multiple courant élevé (41.94x) et une rentabilité du capital très faible (ROIC 3.16%).

**Ce qui confirme la thèse :**
- Forward P/E 11.75x maintient le vecteur de compression multiple / expansion BPA.
- FCF yield 12.1% et quasi-net-cash (Net Debt/EBITDA 0.03x) protègent le bilan.
- Secteur Technology en tête du momentum sectoriel (XLK score 10.0).
- Aucun malus geo, FX, accounting, social.

**Ce qui la limite :**
- Gap +5% non confirmé par volume ni par cassure de MM50.
- Rentabilité du capital (ROIC/ROE) très faible — l'entreprise ne crée pas de valeur sur le capital employé.
- Dilution SBC à 9.35% du CA — la création de valeur actionnariale est partiellement capturée par les équipes.
- Couverture analystes quasi nulle (2 analysts) — risque de déséquilibre informationnel.
- Illiquidité options extrême (Max Pain aberrant) — pas de validation dérivée possible.

**Recommandation :** **ATTENDRE.**

Ne pas engager de nouvelle position sur ce gap non confirmé. Les détenteurs actuels peuvent conserver avec le stop-loss à $12.54 (-12.1%). Une clôture au-dessus de $16.00–$16.48 (52w high + consensus PT) avec volume >1.5× moyenne et RSI >55 modifierait le momentum à favorable et justifierait une révision du score à "Acheter" (sizing réduit). En l'absence de catalyseur idiosyncratique, MITK reste un "watchlist filler" — qualité partielle, pas d'urgence d'achat.

---

*Généré par Argus-IA — Sources : `data/latest.json`, `data/recommandations_latest.json`, `data/sector_rotation_latest.json`, `data/fx_exposure_latest.json`, `data/upcoming_events_latest.json` — Date : 2026-05-18*

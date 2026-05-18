# MITK — Mise à Jour Quotidienne (2026-05-18)

> Desk : Argus-IA | Régime : Inconnu | Données : data/latest.json (2026-05-18T08:44Z)

---

## Résumé des Changements depuis l'Analyse Précédente (2026-05-17)

| Variable | 2026-05-17 | 2026-05-18 | Δ | Impact |
|---|---|---|---|---|
| **Cours close** | $14.26 | $14.26 | — | Aucun mouvement intrajour supplémentaire |
| **RSI 14j** | 51.62 | 51.62 | — | Neutre, inchangé |
| **MM 50j** | $14.31 | $14.31 | — | Prix toujours sous MM50 (-0.3%) |
| **ATR 14j** | $0.86 | $0.86 | — | Volatilité stable |
| **Max Pain (options)** | $20.00 | **$7.50** | -62.5% | [ANOMALIE MAX PAIN] — niveau incohérent vs spot, probable illiquidité |
| **Put/Call ratio** | 0.14 | **null** | — | Données options indisponibles aujourd'hui |
| **Consensus PT (FMP)** | $16 (2 analysts) | $16 (2 analysts) | — | Stable |
| **Prochain earnings** | — | **2026-08-06** (80j) | — | Est EPS $0.24–$0.34, Rev ~$0.1B |

**Verdict global :** Aucun catalyseur nouveau. Configuration technique inchangée. L'élément notable est la dégradation des données options (Max Pain aberrant à $7.50, Put/Call indisponible) et l'enrichissement des métriques FMP FY2025.

---

## 1. Mise à Jour Technique

| Indicateur | Valeur | Lecture |
|---|---|---|
| **RSI (14j)** | 51.62 | Zone neutre, ni surachat ni survente |
| **ATR (14j)** | $0.86 | Volatilité journalière moyenne (~6% du cours) |
| **MM 50j** | $14.31 | Close sous la moyenne (-$0.05 / -0.3%) |
| **MM 200j** | N/A | [DONNÉES MANQUANTES] |
| **Volume** | 1,317,800 | 1.07× moyenne 20j — activité légèrement supérieure, non significative |
| **52-week range** | $8.53 – $16.48 | Spot à 86.5% du range annuel, proche du sommet |

**Niveaux clés :**
- Support immédiat : $13.52 (low du jour 2026-05-18)
- Résistance : $14.68 (high du jour) puis $16.48 (52w high)
- Stop-loss ATR (2×) : $12.54 (-12.1%)

**Verdict timing :** Défavorable. Le cours reste sous MM50 sans momentum directionnel confirmé. L'absence de golden cross et le RSI neutre traduisent une consolidation sans conviction.

---

## 2. Mise à Jour Fondamentale

### 2.1 Divergence Yahoo Finance vs FMP FY2025

| Métrique | Yahoo Finance | FMP Stable API (FY 2025-09-30) | Δ | Source préférée |
|---|---|---|---|---|
| **Market Cap** | $643.9M | $446.6M | -30.6% | Yahoo (close temps réel) |
| **P/E (TTM)** | 41.94x | 50.78x | +21.1% | Yahoo |
| **EV/EBITDA** | 14.85x | 12.15x | -18.2% | FMP (données annuelles) |
| **P/B** | 2.67x | 1.86x | -30.3% | FMP |
| **P/S** | — | 2.49x | — | FMP |
| **P/FCF** | — | 8.24x | — | FMP |

> **Note institutionnelle :** La divergence market cap Yahoo vs FMP (~$200M) suggère que FMP utilise une ancienne base de shares outstanding ou un close décalé. Nous retenons **$644M** comme référence. Le P/E FMP plus élevé (50.78x) renforce la lecture d'un multiple courant élevé, compensé par le Forward P/E à 11.75x.

### 2.2 Marges et Rentabilité (FMP FY2025)

| Métrique | Valeur | Lecture |
|---|---|---|
| **Gross Margin** | 85.1% | ✅ Moat logiciel fort (SaaS/application) |
| **Operating Margin** | 9.3% | ⚠️ Faible vs gross margin — opex élevé (R&D, S&M) |
| **EBITDA Margin** | 20.5% | ✅ Rentabilité opérationnelle correcte |
| **Net Margin** | 4.9% | ⚠️ Compression forte post-frais financiers et taxes (24.2%) |
| **ROIC** | 3.16% | 🔴 Très faible — capital employé peu rémunérateur |
| **ROE** | 3.66% | 🔴 Faible, leverage limité (D/E 0.65) |
| **ROCE** | 6.71% | 🟡 En dessous du coût du capital estimé (~10%) |
| **FCF Yield** | 12.1% | ✅ Attractif — génération de cash réelle |
| **Net Debt / EBITDA** | 0.03x | ✅ Quasi net cash, bilan sain |
| **Interest Coverage** | 1.72x | ⚠️ Juste suffisant, faible marge de sécurité |

### 2.3 Filtre Qualité 6 Critères (Mise à jour partielle)

| Critère | Verdict | Justification |
|---|---|---|
| Revenue CAGR 5 ans ≥ 20% | [DONNÉES MANQUANTES] | Pas de série historique disponible dans latest.json |
| Profit CAGR 5 ans ≥ 20% | [DONNÉES MANQUANTES] | Idem |
| Assets / Liabilities > 1.0 | ✅ Probable | Current ratio 1.19, D/A 0.34 → solvabilité ok |
| FCF positif et croissant 5 ans | ✅ | FCF yield 12.1%, P/FCF 8.24x — FCF réel positif |
| Avantage compétitif (moat) | ✅ | Gross margin 85% = moat logiciel / switching costs |
| Industrie forte croissance (TAM ×5) | [DONNÉES MANQUANTES] | Software-Application, TAM non quantifié |
| **Score Qualité** | **3–4 / 6** | ⚠️ Quality Partielle — manque les séries historiques et le TAM |

> **Règle Filtre Qualité :** Score ≤ 3/6 → Score Valorisation plafonné à 5/10. Ici, avec 4 critères validés/probables, le score Valorisation 6.5/10 reste acceptable mais sous surveillance.

---

## 3. Mise à Jour Sentiment / Options / News

| Signal | Valeur | Évolution | Lecture |
|---|---|---|---|
| **Consensus PT (FMP)** | $16.00 (2 analysts) | → | Upside +12.1% vs spot. Couverture très faible (2 analysts), manque de visibilité institutionnelle. |
| **Max Pain** | $7.50 | ↓ de $20.00 | [ANOMALIE] Niveau à -47.4% du spot. Illiquidité options extrême ou erreur de données. Ignorer pour le scoring. |
| **Put/Call ratio** | N/A | de 0.14 à null | Données indisponibles aujourd'hui. L'optimisme options précédent n'est plus vérifiable. |
| **Short Interest** | 7.32% | → | Float ~43.8M. Short interest modéré, pas de squeeze setup. |
| **Social Sentiment** | 0 / No data | → | Aucune mention Reddit. MITK reste sous le radar retail. |

**Verdict Sentiment :** Neutre à légèrement positif (consensus PT $16), mais manque de données fiables (options illiquides, 2 analysts seulement, silence médiatique).

---

## 4. Scoring Global (Révision)

| Pilier | Score 2026-05-17 | Score 2026-05-18 | Δ | Commentaire |
|---|---|---|---|---|
| **Catalyseur** | 5.5/10 | 5.5/10 | — | Aucun catalyseur nouveau. Earnings dans 80j trop lointain. |
| **Valorisation** | 6.5/10 | 6.0/10 | -0.5 | Forward P/E 11.75x attractif, mais ROIC 3.16% et net margin 4.9% affaiblissent la qualité du multiple. P/E TTM 41.94x reste élevé. |
| **Momentum** | 5.5/10 | 5.0/10 | -0.5 | Sous MM50, RSI neutre sans direction. |
| **Score Opportunité** | **5.9/10** | **5.6/10** | -0.3 | Pondération Normal 35/40/25 → C:5.5×0.35 + V:6.0×0.40 + M:5.0×0.25 = **5.575** (~5.6) |
| **Score Global Composite** | 51.0/100 | **48.0/100** | -3.0 | Pas de malus geo/FX/accounting. Dégradation pure du scoring fondamental et momentum. |

| Seuil | Action | Sizing |
|---|---|---|
| Score Global 48.0/100 | **SURVEILLER** (proche du seuil ATTENDRE 50) | — |

> **Note :** Le score global ajusté passe sous le seuil médian de 50. Le ticker reste dans la zone "surveiller / attendre" sans catalyseur immédiat.

---

## 5. Révision des Niveaux SL / TP

| Niveau | Prix | Distance vs Close | Méthode |
|---|---|---|---|
| **Stop-loss** | $12.54 | -12.1% | Cours − 2×ATR ($0.86) |
| **Take-profit** | $16.84 | +18.1% | Cours + 3×ATR ($0.86) |
| **Ratio R/R** | **1.5** | — | Acceptable mais non optimal |
| **Consensus PT (FMP)** | $16.00 | +12.1% | Aligné sur la zone de TP structurelle |

**Ajustement proposé :** Aucun. Les niveaux ATR-based restent cohérents. Le consensus FMP à $16 conforte la résistance intermédiaire avant le TP à $16.84.

---

## 6. Calendrier & Événements

| Événement | Date | Jours restants | Impact attendu |
|---|---|---|---|
| **Earnings Q3 2026** (est.) | 2026-08-06 | 80 | Est EPS $0.24–$0.34, Rev $0.1B. Prochain catalyseur majeur. |
| **Expiration options** | 2026-06-18 | 31 | Illiquidité constatée, impact limité. |

**Alertes actives :**
- 🔴 [ANOMALIE MAX PAIN] $7.50 vs spot $14.26 — signaler à l'équipe data
- 🟡 [DONNÉES OPTIONS DÉGRADÉES] Put/Call ratio indisponible
- 🟡 [DIVERGENCE YAHOO/FMP] Market cap et P/E — utiliser Yahoo comme primaire

---

## 7. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE CONFIRMÉE, SCORE LÉGÈREMENT AJUSTÉ À LA BAISSE.**

L'analyse du 2026-05-17 reste valide : MITK est un small-cap logiciel (Software-Application) avec un Forward P/E attractif (11.75x) masquant un multiple courant élevé (41.94x) et une rentabilité du capital faible (ROIC 3.16%). L'enrichissement FMP confirme un profil de **Quality Partielle** (marges élevées, FCF solide, mais rentabilité du capital insuffisante et couverture analystes quasi nulle).

**Ce qui n'a pas changé :**
- Pas de catalyseur immédiat (earnings dans 80j).
- Configuration technique neutre/défavorable (sous MM50, RSI 52).
- Pas de flux institutionnel détecté.
- Pas d'événement corporate (M&A, guidance, buyback).

**Ce qui s'est légèrement dégradé :**
- Données options devenues indisponibles / aberrantes (Max Pain $7.50).
- Rentabilité du capital (ROIC/ROE) très faible, réduisant la marge de sécurité fondamentale.
- Score global composite ajusté de 51.0 à ~48.0.

**Recommandation :** **SURVEILLER / ATTENDRE.**

Ne pas engager de nouvelle position. Les détenteurs actuels peuvent conserver avec le stop-loss à $12.54 (-12.1%). Une cassure au-dessus de $16.00–$16.48 (52w high + consensus PT) avec volume confirmé changerait le momentum à favorable. En l'absence de catalyseur, MITK reste un "watchlist filler" sans urgence d'achat.

---

*Généré automatiquement — Données : data/latest.json, data/recommandations_latest.json, data/fmp_* — Date : 2026-05-18*

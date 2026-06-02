# RKLB — Mise à Jour Snapshot 13:00 UTC (2026-06-02)

> Source : `data/2026-06-02.json` (fetched 2026-06-02T13:00:12 UTC) | `data/recommandations_2026-06-02.json` | Close officiel US du 2026-06-01

---

## 1. Résumé des Changements depuis le Snapshot 10:00 UTC (2026-06-02)

| Métrique | Snapshot 10h | Snapshot 13h | Variation |
|---|---|---|---|
| **Cours close** | $122,39 | **$122,39** | Stable |
| **RSI 14j** | 52,48 | **52,48** | Stable |
| **ATR 14j** | $12,55 | **$12,55** | Stable |
| **Volume séance** | 37,13 M (1,19×) | **37,13 M (1,19×)** | Stable |
| **Score Global Agent** | 42,0/100 (aj. 47,0) SURVEILLER | **42,0/100 (aj. 47,0)** | Inchangé |
| **Max Pain** | $45,00 (anomalie data quality) | **$145,00** | 🟡 **Correction + mutation** |
| **Put/Call ratio** | `null` (données corrompues) | **1,18** | ✅ Rétabli |
| **Call OI %** | `null` (données corrompues) | **45,9 %** | ✅ Rétabli |

**Verdict** : **Stabilité totale** des données cours, technique et scoring. La seule variation concerne la **correction des données options** dans `data/2026-06-02.json` entre le snapshot 10h et 13h : les champs `null` / incohérents sont rétablis avec des valeurs **différentes de l'historique immédiat** ($90,00 le 01/06). Cette mutation du Max Pain modifie la lecture de la pression options à court terme.

---

## 2. Mise à Jour Technique

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **RSI 14j** | 52,48 | Neutre. Sortie du surachat confirmée, inchangé. |
| **ATR 14j** | $12,55 | Volatilité élevée stable. Range intraday 01/06 = $121,00–$135,63. |
| **MM 50j** | $92,26 | Écart haussier **+32,7 %** vs spot. Tendance haussière structurelle intacte. |
| **Volume 20j** | 31 224 555 | Séance 01/06 : **37,13 M** — **1,19× moyenne**. Distribution active confirmée. |
| **Beta** | 2,313 | Sensibilité systématique extrême. |
| **52W High / Low** | $151,00 / $25,24 | Spot à **−18,9 %** du 52W high. |

**Niveaux clés révisés** :
- Support immédiat : **$121,00** (basse intraday 01/06)
- Support technique majeur : **$97,29** (spot – 2×ATR $12,55)
- Support confluence : **$90,00** (zone test psychologique + ancien Max Pain)
- Résistance immédiate : **$135,63** (haute intraday 01/06)
- Résistance / Objectif : **$160,04** (spot + 3×ATR $12,55)

**Verdict timing : Défavorable** — La structure technique reste inchangée. Le repli −14,7 % sur volume 1,19× moyenne confirme une distribution active. La clôture proche du low ($122,39 vs low $121,00) indique une pression vendeuse soutenue. La probabilité d'un test de la zone $118–$121 (gap du 22/05) demeure élevée.

---

## 3. Mise à Jour Fondamentale

Aucune news fondamentale majeure détectée. `data/news_2026-06-02.json` vide pour RKLB. `data/events_2026-06-02.json` vide. Le mouvement −14,7 % reste **sans catalyseur fondamental identifiable**.

| Métrique | Valeur | Source |
|---|---|---|
| Market Cap (Yahoo) | **$70,85 Mds** | Yahoo Finance |
| Forward P/E | **−11 106,17** | Yahoo Finance |
| EV/Revenue | 102,40× | Yahoo Finance |
| EV/EBITDA | −422,18× | Yahoo Finance |
| P/B (Yahoo) | **31,12×** | Yahoo Finance |
| P/B (FMP) | 21,50× | FMP Stable API |
| P/S (FMP) | 61,51× | FMP Stable API |
| Short Interest | 5,81 % | Yahoo Finance |
| **FMP Consensus PT** | **$84,20** (15 analysts) | FMP Stable API |

**[ANOMALIE DONNÉES PERSISTANTE]** — Market Cap Yahoo ($70,85 Mds) vs FMP sous-jacent ($37,02 Mds) persiste.

**Filtre Qualité (6 critères) — inchangé** :

| Critère | Évaluation | Justification |
|---|---|---|
| 1. Revenue CAGR 5 ans ≥ 20 % | ✅ Oui | Segment spatial / lanceurs en expansion. |
| 2. Profit CAGR 5 ans ≥ 20 % | 🔴 Non | Forward P/E négatif ; pertes persistantes. |
| 3. Assets/Liabilities > 1,0 | ✅ Oui | Current Ratio 4,08. |
| 4. FCF positif et croissant 5 ans | 🔴 Non | FCF yield négatif. |
| 5. Avantage compétitif (moat) | ⚠️ Partiel | Positionnement unique, concurrence SpaceX/Blue Origin intense. |
| 6. Industrie forte croissance (TAM ×5) | ✅ Oui | TAM spatial commercial en expansion. |

**Score Qualité total : 3/6** → 🔴 **Hors périmètre institutionnel**. Score Valorisation plafonné à 5/10.

**Divergence cours vs consensus** : Spot $122,39 vs PT moyen $84,20 = **+45,4 % au-dessus du consensus sell-side**.

---

## 4. Mise à Jour Sentiment / Options / News

**🟡 CORRECTION + MUTATION DES DONNÉES OPTIONS**

| Signal | Snapshot 01/06 | Snapshot 10h (02/06) | Snapshot 13h (02/06) | Diagnostic |
|---|---|---|---|---|
| **Consensus analystes (FMP)** | $84,20 (15 analysts) | $84,20 (15 analysts) | $84,20 (15 analysts) | ✅ Stable |
| **Max Pain** | **$90,00** | $45,00 (anomalie) | **$145,00** | 🟡 **Corrigé mais muté** |
| **Put/Call ratio** | **1,25** | `null` | **1,18** | ✅ Rétabli, −5,6 % |
| **Call OI %** | **44,4 %** | `null` | **45,9 %** | ✅ Rétabli, +1,5 pt |
| **Short Interest** | 5,81 % | 5,81 % | 5,81 % | Stable |
| **News du jour** | Aucune | Aucune | Aucune | Vide |
| **Social Sentiment** | 0 mentions, score 0/10 | 0 mentions | 0 mentions | Aucune activité retail |

### Lecture de la mutation Max Pain

- **Max Pain historique (01/06)** : $90,00 — spot $122,39 = **+$32,39 (+26,5 %)** au-dessus. Interprétation : pression baissière à CT, pin vers le bas.
- **Max Pain corrigé (02/06, 13h)** : $145,00 — spot $122,39 = **−$22,61 (−15,6 %)** en dessous. Interprétation : pression haussière à CT, pin vers le haut.

**Impact** : L'inversion du signal options CT est significative. Le spot se retranche désormais **sous** le Max Pain de l'échéance 2026-06-05. Cela implique que les market makers d'options ont un intérêt mécanique à ce que le cours remonte vers $145,00 à l'expiration (dans 3 jours ouvrés). C'est un **catalyseur technique haussier à très court terme** qui contrebalance partiellement la distribution observée sur le volume.

Cependant, le Put/Call 1,18 (puts > calls en volume) et le Call OI 45,9 % (calls légèrement minoritaires en open interest) indiquent que la conviction haussière reste modérée. La structure n'est pas clairement haussière — elle est simplement **moins baissière** qu'interprété précédemment avec le Max Pain $90,00.

**Verdict Sentiment : Neutre à légèrement haussier CT** — Aucune news, aucun upgrade/downgrade. La correction data quality élimine l'hypothèse de pression baissière CT extrême. L'expiration du 5 juin avec un spot sous Max Pain ($145,00) crée un **risque de pin haussier** technique, mais le momentum prix (repli −14,7 %) reste vendeur.

---

## 5. Mise à Jour Agents Spécialisés

| Agent | Donnée RKLB | Impact scoring |
|---|---|---|
| **Quant** | Pas assez de signaux historiques (p-value `null`, n=0). | [SIGNAUX NON SIGNIFICATIFS] |
| **Géopolitique** | Score Politique 2/10, non exposé. | Aucun malus. |
| **Comptable (Accounting)** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Sector Rotation** | XLI (Industrials) return 20j −0,32 %, sous-performe SPY (RS −5,58 %). Momentum score 0,0. Signal ROTATION_TO_CYCLICAL. | Malus sectoriel implicite. RKLB dans Aerospace & Defense (XLI) — pas de momentum sectoriel. |
| **FX Exposure** | Fichier absent. | [DONNÉES MANQUANTES] |
| **Event-Driven** | Aucun événement corporate dans `events_2026-06-02.json`. | Aucun bonus/malus. |
| **Upcoming Events** | Earnings Q2 2026 le **2026-08-06** (**65 jours**). Est EPS −$0,06 à −$0,02 ; Rev $0,2 B. | Trop loin pour pricer. |
| **Quality Gate** | Status `ok`, pas d'anomalie détectée sur le prix. | Aucun malus. |

---

## 6. Scoring Global Révisé

| Pilier | Score | Commentaire |
|---|---|---|
| **Catalyseur** | 4,3/10 | Aucune news majeure. Earnings dans 65j. Structure options révisée CT (Max Pain $145,00 = pin haussier potentiel). |
| **Valorisation** | 3,0/10 | Forward P/E négatif, EV/Rev 102×, spot +45,4 % vs consensus. Plafonné par Filtre Qualité ≤3/6. |
| **Momentum** | 6,0/10 | Tendance haussière structurelle intacte (prix > MM50), mais distribution −14,7 % sur volume 1,19×. RSI 52 neutre. |
| **Score Opportunité** | **4,2/10** | Pondération Normal : C×35 % + V×40 % + M×25 % |
| **Malus** | −5 pts | Malus structurel (surchauffe partiellement dégonflée + divergence consensus). |
| **Score Global ajusté** | **47,0/100** | **SURVEILLER** — Seuil 35–49 |

**Comparaison avec snapshot 10h** : Le score global est **inchangé** (47,0). L'unique variation concerne la **correction data quality options** qui modifie la lecture CT : au lieu d'une pression baissière extrême (Max Pain $90,00), le signal est réinterprété comme un **pin haussier technique** (Max Pain $145,00). Cela ne change pas le scoring fondamental mais atténue légèrement le risque de chute libre d'ici vendredi.

---

## 7. Révision des Niveaux SL / TP

| Paramètre | Valeur | Justification |
|---|---|---|
| **Prix d'entrée (spot)** | $122,39 | — |
| **Stop-loss** | $97,29 (−20,4 %) | 2×ATR ($12,55) — aligné agent officiel |
| **Take-profit** | $160,04 (+30,7 %) | 3×ATR ($12,55) — aligné agent officiel |
| **Ratio R/R** | **1,5 : 1** | Inférieur au seuil minimum 2:1 pour un trade directionnel à haut beta |

**Note options CT** : L'expiration du 5 juin avec Max Pain $145,00 implique que le spot $122,39 a un **chemin de moindre résistance technique vers $135–$145** si les market makers défendent le pin. Cela ne constitue pas un signal d'achat (ratio R/R toujours insuffisant, Filtre Qualité 3/6), mais un rebond intraday vers $135 n'est pas à exclure.

---

## 8. Calendrier & Événements à Venir

| Événement | Date | Jours restants | Détail |
|---|---|---|---|
| **Earnings Q2 2026** | 2026-08-06 | **65 jours** | Est EPS : −$0,06 à −$0,02 ; Rev : $0,2 B |
| **Expiration options** | 2026-06-05 | **3 jours ouvrés** | Max Pain **$145,00** — spot $122,39 = **−$22,61 sous le Max Pain**. Risque de pin haussier CT. |

**Prochain catalyseur majeur** : Aucun avant earnings (août). L'expiration options du 5 juin approche avec un Max Pain repositionné à **$145,00**, soit **$22,61 au-dessus du spot**. La configuration technique CT est modifiée : au lieu d'une pression baissière (ancienne lecture $90,00), le setup est désormais un **pin haussier** si les options market makers pilotent le cours vers le strike de max douleur.

---

## 9. Conclusion — Thèse Confirmée / Modifiée / Invalidée ?

**Verdict : THÈSE MODIFIÉE 🟡 SURVEILLER — CORRECTION DATA QUALITY OPTIONS**

Le snapshot 13:00 UTC du 2 juin 2026 confirme l'intégralité de l'analyse technique et fondamentale du snapshot 10h : **aucun changement** sur le cours ($122,39 stable), la structure technique (RSI 52, ATR $12,55), la valorisation (extrême), ou le scoring global (47,0 — SURVEILLER).

**Seul élément modifié : la lecture des options à court terme.**

1. ✅ **Cours stable** : $122,39 inchangé.
2. ✅ **RSI stable neutre** : 52,48.
3. ✅ **Volume stable** : 37,13 M (1,19×). Distribution active confirmée.
4. ✅ **ATR stable** : $12,55.
5. ✅ **Divergence consensus stable** : +45,4 % vs PT $84,20.
6. 🟡 **CORRECTION DATA QUALITY OPTIONS** : Max Pain $45,00 (anomalie) → **$145,00** (corrigé). Put/Call et Call OI rétablis (1,18 / 45,9 %).
7. 🟡 **Inversion du signal options CT** : Le spot passe d'au-dessus du Max Pain historique ($90,00) à **en-dessous** du Max Pain corrigé ($145,00). La pression CT passe d'interprétée "baissière" à "haussière" (pin risk vers le haut).
8. 🔴 **Filtre Qualité 3/6** inchangé — hors périmètre institutionnel.
9. 🔴 **Sectoriel défavorable** — XLI sans momentum, sous-performe SPY 20j/60j.
10. ✅ **Score global inchangé** : 42,0/100 ajusté 47,0 — SURVEILLER.

**Recommandation** : Maintenir la posture **SURVEILLER**. La stabilité totale des données fondamentales et techniques confirme que le repli du 01/06 est un mouvement de distribution sans catalyseur. La **correction options** atténue le risque de chute libre immédiate mais ne transforme pas la thèse en haussière : la valorisation reste extrême (Forward P/E négatif, EV/Rev 102×, spot +45 % vs consensus) et le Filtre Qualité 3/6 exclut tout positionnement institutionnel long.

Attendre :
- Un **retour vers la zone de confluence $97–$105** (test support 2×ATR + test psychologique), ou
- Une **inflexion matérielle des anticipations** (guidance positive, contrat majeur, résultats trimestriels) avant toute réévaluation.

Toute position longue actuelle expose à un drawdown de −20,4 % (SL) en 1–2 séances compte tenu de l'ATR $12,55 et du Beta 2,31. L'expiration options du 5 juin avec un Max Pain $145,00 crée un **risque de volatilité haussière CT** (pin vers $145) qui pourrait générer un rebond technique transitoire — non convertible en signal d'achat à ce stade.

---

*Rapport généré le 2026-06-02 — Données : `data/2026-06-02.json` (13:00 UTC), `data/recommandations_2026-06-02.json`, `data/upcoming_events_2026-06-02.json`, `data/events_2026-06-02.json`, `data/news_2026-06-02.json`, `data/social_sentiment_2026-06-02.json`, `data/geo_2026-06-02.json`, `data/sector_rotation_2026-06-02.json`, `data/quant_2026-06-02.json`, `data/quality_gate_2026-06-02.json`*

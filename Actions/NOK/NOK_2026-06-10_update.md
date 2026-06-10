# NOK — Mise à jour quotidienne (Snapshot 10:00 UTC)

> **Date :** 2026-06-10
> **Type :** Update — snapshot pré-ouverture, upgrade scoring mécanique SURVEILLER → ATTENDRE, données partielles
> **Fichier précédent :** [NOK_2026-06-09_21h_update.md](./NOK_2026-06-09_21h_update.md)

---

## 1. Résumé des changements

| Métrique | 2026-06-09 21:00 UTC | 2026-06-10 10:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Previous close** | $14.59 | **$14.59** | — |
| **Close session** | $13.85 | **NaN** | [DONNÉES PARTIELLES] |
| **RSI 14j** | 50.91 | **55.0** | **+4.09 pts** 🟢 |
| **Volume session** | 178.7M (1.40×) | **178.7M** | Carry-forward |
| **ATR 14j** | $1.15 | **null** | [DONNÉES MANQUANTES] |
| **MM 50j** | $12.41 | **null** | [DONNÉES MANQUANTES] |
| **Max pain options** | $15.00 | **$3.00** | Anomalie — conservé $15.00 opérationnel |
| **Put/Call ratio** | 0.78 | **null** | [DONNÉES MANQUANTES] |
| **Call OI %** | 56.2% | **null** | [DONNÉES MANQUANTES] |
| **Score Global ajusté** | 48.0 — SURVEILLER | **50.5 — ATTENDRE** | **+2.5 pts** 🟢 |
| **Recommandation** | SURVEILLER | **ATTENDRE** | Upgrade mécanique |

**Verdict :** Le snapshot 10:00 UTC du 2026-06-10 est un **snapshot pré-ouverture NY** (6h heure locale) : les champs `open`, `high`, `low`, `close` sont `NaN` pour l'ensemble de la watchlist, l'ATR et les moyennes mobiles sont `null`, et les données options sont corrompues (max pain $3.00 aberrant). Le seul signal fiable est le **RSI 14j remonté à 55.0** (+4.09 pts vs 50.91 à 21h le 09/06), sortie confirmée de la zone de fragilisation post-gap. L'agent recommandation répond par un **upgrade mécanique de 48.0 à 50.5/100** (SURVEILLER → ATTENDRE), entraîné par l'amélioration des scores Catalyseur (+1.0 pt) et Valorisation (+1.0 pt) en réponse au RSI remonté. Aucun catalyseur fondamental ne justifie ce mouvement.

**[DONNÉES PARTIELLES]** : `validation_report.txt` n'a pas été relu (absent du snapshot), mais les warnings qualité historiques sur NOK persistent : Quality hors périmètre 2.5/6, P/E Yahoo élevé. L'anomalie options (max pain $3.00) est traitée comme corrompue — les valeurs opérationnelles du 09/06 ($15.00 / 0.78 / 56.2%) sont conservées pour l'analyse.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$14.59** | `data/latest.json` | Carry-forward du close 08/06 ou close 09/06 non consolidé |
| Open / High / Low / Close | **NaN** | `data/latest.json` | Marché non ouvert à 10h UTC (6h NY) |
| Volume | **178,662,201** | `data/latest.json` | Identique au 09/06 — carry-forward |
| Volume vs moy. 20j | **1.40×** | Calcul (127.3M) | Inchangé |
| RSI 14j | **55.0** | `data/latest.json` | Zone neutre constructive, +4.1 pts |
| ATR 14j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| MM 50j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |

**Niveaux clés (conservés du 09/06 21h, faute de données actualisées) :**
- Support immédiat : **$13.18** (low du 09/06, validé)
- Support structurel : **$12.41** (MM50 du 09/06)
- Résistance gap : **$15.47** (base du gap haussier du 25/05)
- Max pain options : **$15.00** (opérationnel, expiration 2026-06-12 dans 2 jours)
- Stop-loss ATR (2×) : **$11.55** (basé sur cours $13.85 et ATR $1.15 du 09/06) — *non révisé, ATR manquant*
- Take-profit ATR (3×) : **$17.30** (basé sur cours $13.85 et ATR $1.15 du 09/06) — *non révisé, ATR manquant*
- Ratio R/R : **1.5×** (stable)

**Verdict timing :** Neutre — Le RSI à 55.0 confirme la sortie de la zone de fragilisation post-gap du 08/06. Cependant, l'absence de données de session (close, ATR, MM) empêche toute conclusion technique ferme. Le snapshot pré-ouverture ne permet pas de valider si le momentum du rebond de +3.17% (21h le 09/06) s'est maintenu en after-hours ou en pré-market. Les niveaux clés restent ceux du 09/06 jusqu'à consolidation des données post-ouverture.

---

## 3. Bloc Fondamental

Inchangé en structure ; mécanique de cours uniquement.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $77.3B | Yahoo Finance |
| P/E (TTM) | 86.56 | Yahoo Finance |
| Forward P/E | 28.45 | Yahoo Finance |
| EV/EBITDA | 29.58 | Yahoo Finance |
| P/B | 3.15 | Yahoo Finance |
| Beta | 0.781 | Yahoo Finance |
| Dividend Yield | 1.18% | Yahoo Finance |
| Short Interest | 1.19% | Yahoo Finance |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé). Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).

**Divergence structurelle Yahoo/FMP persistante :** P/E Yahoo 86.56 vs P/E FMP 45.81. La valorisation reste défavorable quel que soit le multiple de référence.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé |
| Max pain options | **$15.00** | Valeur opérationnelle 09/06 | `latest.json` corrompu ($3.00) — conservé $15.00 |
| Put/Call ratio | **0.78** | Valeur opérationnelle 09/06 | `latest.json` null — conservé 0.78 |
| Call OI % | **56.2%** | Valeur opérationnelle 09/06 | `latest.json` null — conservé 56.2% |
| Expiration nearest | **2026-06-12** | Yahoo Finance | Dans 2 jours |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_latest.json` | Aucune mention, aucun pump |

**Structure options :**
- Max pain **$15.00** conservé opérationnellement. Si le cours effectif est proche de $14.59 (previous_close), l'écart au max pain se réduit à ~−2.7% (vs −7.7% à 21h le 09/06 avec cours $13.85). Le pin risk baissier s'atténue significativement.
- Put/call **0.78** — structure call-biased persistante.
- Call OI **56.2%** inchangé.
- Expiration dans 2 jours (2026-06-12). Avec un cours ~$14.59, la probabilité de fermeture proche du max pain $15.00 est réactivée. Le risque de pin est modéré et symétrique.

**News / Événements :**
- `events_latest.json` (2026-06-10) : **0 événement** corporate pour NOK
- `news_latest.json` : **0 article** pour NOK
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 43 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_latest.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_latest.json` : momentum score 10.0 artificiel suite à données NaN, mais classification bottom 3 conservée). Malus structurel pour NOK persistant.
- **Exposition FX :** 25% revenus hors-USD, impact neutre (`fx_exposure_latest.json` : fx_impact_score 0.0, flag 🟢). Aucune divergence détectée.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_latest.json` du 2026-05-17 : 0 ticker flaggé)
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent — pas de donnée M-Score/Z-Score disponible

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-10.json`

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **5.0/10** | C:5.0 V:4.5 M:6.0 |
| **Score Catalyseur** | 5.0/10 | 🟡 Modéré — aucun catalyseur identifié, upgrade mécanique lié au RSI |
| **Score Valorisation** | 4.5/10 | 🔴 Défavorable — P/E 86.6, premium consensus +35.1% |
| **Score Momentum** | 6.0/10 | 🟡 Tendance haussière structurelle préservée (RSI 55) |
| **Score Global ajusté** | **50.5/100** | **ATTENDRE** (seuil 50–59) |
| **Timing technique** | Neutre | RSI 55, zone neutre favorable, données session manquantes |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 08/06 21h : Score Global 51.2 — ATTENDRE
- Le 09/06 17h : Score Global 48.0 — SURVEILLER (rétrogradation)
- Le 09/06 21h : Score Global 48.0 — SURVEILLER (confirmé)
- Le 10/06 10h : Score Global **50.5** — **ATTENDRE** (upgrade mécanique)

Le scoring gagne **+2.5 pts** (48.0 → 50.5) et franchit le seuil ATTENDRE (50). L'amélioration est purement mécanique : les scores Catalyseur (+1.0 pt, 4.0 → 5.0) et Valorisation (+1.0 pt, 3.5 → 4.5) sont révisés à la hausse par l'agent en réponse au RSI remonté à 55.0. Aucun catalyseur fondamental n'intervient. Le Filtre Qualité 2.5/6 maintient le plafond structurel. Le Score Momentum reste à 6.0/10.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (09/06 21h) | Valeur actuelle (10/06 10h) | Justification |
|--------|-------------------------------|----------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé |
| **Stop-loss** | $11.55 | **$11.55** | Non révisé — ATR null dans `latest.json` |
| **Take-profit** | $17.30 | **$17.30** | Non révisé — ATR null dans `latest.json` |
| **Upside / Downside** | −22.0% / −16.6% | **—** | Cours session manquant |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (hypothétique) |
| **Sizing** | — | **—** | Pas de position |

**Note :** Si l'ATR précédent ($1.15) s'appliquait au previous_close ($14.59), les niveaux mécaniques seraient SL $12.29 / TP $18.04. Ces niveaux ne sont pas retenus faute de donnée ATR actualisée dans les fichiers JSON.

---

## 8. Scénarios & Probabilités

Inchangés vs 09/06 21h, avec ajustement mineur sur le pin risk.

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 20% | Rebond vers $15.00 | Poursuite de l'absorption au-dessus de $14.50, test du max pain $15.00 à l'expiration du 12/06. Nécessite volume maintenu > moyenne |
| **Central** | 55% | Range $13.80–$14.80 | Consolidation autour du previous_close $14.59. Pas de catalyseur = pas de direction claire. Support $13.18 validé, résistance $15.00 options |
| **Pessimiste** | 25% | Retest $13.18 puis cassure → $12.41 (MM50) | Distribution continue si le rebond du 09/06 s'avère un dead cat bounce. Cassure MM50 = renversement de tendance de moyen terme |

---

## 9. Conclusion — Thèse modifiée (upgrade mécanique)

**Verdict :** La thèse évolue de **SURVEILLER** à **ATTENDRE** sur la base d'un **upgrade mécanique du scoring (+2.5 pts)** lié au RSI remonté à 55.0. Aucun élément fondamental ne justifie ce changement.

**Ce qui a changé :**
- **RSI 14j** : 50.91 → **55.0** (+4.09 pts), sortie confirmée de la zone de fragilisation post-gap.
- **Score Global** : 48.0 → **50.5/100** (+2.5 pts), franchissement du seuil ATTENDRE.
- **Score Catalyseur** : 4.0 → **5.0/10** (+1.0 pt) — révision mécanique de l'agent.
- **Score Valorisation** : 3.5 → **4.5/10** (+1.0 pt) — révision mécanique de l'agent.
- **Action recommandée** : SURVEILLER → **ATTENDRE**.
- **Pin risk options** : atténué. Si previous_close $14.59 est confirmé comme proche du cours effectif, l'écart au max pain $15.00 se réduit à ~−2.7% (vs −7.7% à 21h le 09/06).

**Ce qui n'a pas changé :**
- Filtre Qualité hors périmètre (2.5/6) — pas de changement qualitatif.
- Aucun catalyseur fondamental détecté (0 news, 0 événement corporate).
- Consensus analystes $10.8 (7 analysts) — premium persistant +35.1%.
- XLC bottom 3 du sector rotation.
- Options structure call-biased (put/call 0.78, call OI 56.2%) inchangée.
- Exposition FX neutre.
- Volume et données de session : carry-forward du 09/06 (snapshot pré-ouverture).

**Recommandation révisée :** **ATTENDRE** — Pas de position. L'upgrade à 50.5/100 est un franchissement technique du seuil, non une amélioration qualitative. Une entrée reste exclue sans :
- Données de session consolidées (close, ATR, MM) pour valider la stabilité du rebond
- Test et rebond sur la MM50 avec volume > moyenne et pattern de reversal
- Franchissement durable au-dessus de $15.00 (max pain) avec volume
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel (contrat 5G, upgrade, news structurante)

**Risque immédiat :** L'expiration des options le 2026-06-12 (dans 2 jours) avec max pain $15.00 crée un risque de pin modéré. Si le cours effectif est proche de $14.59, la fermeture vendredi au-dessus de $14.50 est plausible et une pin vers $15.00 reste possible si le momentum se maintient.

**Prochain point de contrôle :** Attendre le snapshot post-ouverture du 10/06 (13h/17h UTC) pour consolider les données de session (close, ATR, volume) et valider ou infirmer cet upgrade mécanique. Earnings Q2 FY2026 le **2026-07-23** (dans 43 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-10 10:00 UTC), `data/recommandations_2026-06-10.json`, `data/sector_rotation_2026-06-10.json`, `data/fx_exposure_2026-06-10.json`, `data/social_sentiment_2026-06-10.json`, `data/upcoming_events_2026-06-10.json`, `data/events_2026-06-10.json`, et fichiers JSON agents.*

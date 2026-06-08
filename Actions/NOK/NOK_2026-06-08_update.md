# NOK — Mise à jour quotidienne (Snapshot 13:00 UTC)

> **Date :** 2026-06-08
> **Type :** Update post-gap — confirmation thèse
> **Fichier précédent :** [NOK_2026-06-08_update.md](./NOK_2026-06-08_update.md) (snapshot 10:00 UTC)

---

## 1. Résumé des changements

| Métrique | 2026-06-08 10:00 UTC | 2026-06-08 13:00 UTC | Δ |
|----------|----------------------|----------------------|---|
| **Cours close** | $14.38 | **$14.38** | — |
| **RSI 14j** | 52.32 | **52.32** | — |
| **Volume** | 183.6M | **183.6M** | — |
| **Max pain options** | $3.00 (corrompu) | **$15.00** | ✅ Restauré |
| **Put/Call ratio** | null (corrompu) | **1.00** | ✅ Restauré |
| **Call OI %** | null (corrompu) | **49.9%** | ✅ Restauré |
| **Score Global ajusté** | 48.0 — SURVEILLER | **48.0 — SURVEILLER** | — |
| **Recommandation** | SURVEILLER | **SURVEILLER** | Confirmée |

**Verdict :** Données de prix/volume/technique **strictement inchangées** vs snapshot 10:00 UTC (même source `data/2026-06-08.json`, fetched_at 13:00). **Mutation options majeure** : les données corrompues du matin (max pain $3.00, put/call null) sont intégralement restaurées dans `latest.json` : max pain **$15.00**, put/call **1.00**, call OI **49.9%**, expiration **2026-06-12**. Le cours ($14.38) passe **sous le max pain** (−4.1%) pour la première fois depuis le 25/05, inversant la dynamique options. Aucun événement corporate (`events_latest.json` vide). Le **DRAFT_refresh** déclenché par PRICE_GAP (−13.48%) et ATR_SPIKE (7.86%) est traité : la thèse SURVEILLER est confirmée, pas invalidée.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source |
|----------|--------|--------|
| Open | $15.66 | Yahoo Finance |
| High | $15.67 | Yahoo Finance |
| Low | $14.00 | Yahoo Finance |
| Close | $14.38 | Yahoo Finance |
| Change vs previous close | **−13.48%** | Yahoo Finance |
| Volume | 183,595,200 | Yahoo Finance |
| Volume vs moy. 20j | **1.47×** | Calcul (125.2M) |
| RSI 14j | **52.32** | Calcul agent |
| ATR 14j | **$1.13** | Calcul agent |
| MM 50j | **$12.16** | Calcul agent |
| MM 200j | — | N/A |

**Niveaux clés révisés :**
- Support immédiat : **$14.00** (low du jour) — si cassé, prochain support structurel **$12.16** (MM50)
- Résistance : **$15.47** (base du gap haussier du 25/05)
- Stop-loss ATR (2×) : **$12.12** ($14.38 − $2.26)
- Take-profit ATR (3×) : **$17.77** ($14.38 + $3.39)
- Ratio R/R : **1.5x**

**Verdict timing :** Neutre — La sortie de surachat est healthy, le gap baissier sur volume élevé laisse un surhang technique. Le cours reste +18.3% au-dessus de la MM50. Cependant, le non-franchissement du gap du 25/05 ($15.47) et la position sous le max pain options ($15.00) indiquent une faiblesse relative à court terme.

---

## 3. Bloc Fondamental

Inchangé vs snapshot 10:00 UTC. Voir [NOK_2026-06-08_update.md](./NOK_2026-06-08_update.md) pour le détail complet.

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $80.3B | Yahoo Finance |
| P/E (TTM) | 89.88 | Yahoo Finance |
| Forward P/E | 29.49 | Yahoo Finance |
| EV/EBITDA | 30.75 | Yahoo Finance |
| P/B | 3.27 | Yahoo Finance |
| Beta | 0.781 | Yahoo Finance |
| Dividend Yield | 1.14% | Yahoo Finance |
| Short Interest | 1.08% | Yahoo Finance |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé). Bilan solide (net cash, D/E 0.25) mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).

> **[DONNÉES PARTIELLES]** : `validation_report.txt` du 2026-06-08 signale un warning qualité sur NOK (P/E élevé, premium vs consensus). Ce warning est hérité du snapshot du 17/05 et ne reflète pas la correction de −13.5% qui a réduit le premium à +33.1%.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source |
|--------|--------|--------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API |
| Max pain options | **$15.00** | Yahoo Finance (restauré) |
| Put/Call ratio | **1.00** | Yahoo Finance (restauré) |
| Call OI % | **49.9%** | Yahoo Finance (restauré) |
| Expiration nearest | **2026-06-12** | Yahoo Finance |
| Social sentiment (Reddit) | 0 mentions / 0.0 score | `social_sentiment_latest.json` |

**⚠️ Mutation options majeure :**
- **Max pain remonté** de $13.50 (opérationnel historique) à **$15.00** (données 13:00 propres)
- **Structure inversée** : call OI 49.9% (vs 68.5% historique call-dominated) → équilibre put/call
- **Cours sous max pain** : $14.38 < $15.00 (−4.1%) — la première fois depuis le gap du 25/05. Cela crée une pression baissière à l'expiration du 12/06 (dans 4 jours) car le pin vers $15.00 favorise les vendeurs.
- Put/call à 1.0 indique un sentiment neutre, loin de l'optimisme extrême du début juin (put/call 0.45).

**News / Événements :**
- `events_latest.json` : **0 événement** corporate pour NOK
- Aucune mention Reddit, aucun pump/dump détecté
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_latest.json`)
- **Sectoriel :** Technology / Communication Equipment. Le secteur XLC (Communication Services) reste en **bottom 3** du sector rotation (momentum score 0.0, RS20d −5.68% vs SPY). Malus structurel pour NOK.
- **Exposition FX :** 25% revenus hors-USD, impact neutre (`fx_exposure_latest.json` : fx_impact_score 0.0)
- **Géopolitique :** Score politique 2/10, non exposé (`geo_risk_latest.json`)

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_latest.json` (2026-06-08)

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.3/10** | C:4.0 V:3.5 M:6.0 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 89.9, premium consensus +33% |
| **Score Momentum** | 6.0/10 | Tendance haussière structurelle intacte (+18% vs MM50) |
| **Score Global ajusté** | **48.0/100** | **SURVEILLER** (seuil 35–49) |
| **Timing technique** | Favorable | Sortie de surachat, cours au-dessus MM50 |

**Évolution du scoring :**
- Le 02/06 : Score Global 31.8 — ÉVITER
- Le 03/06 : Score Global 31.8 — ÉVITER
- Le 08/06 10:00 : Score Global 48.0 — SURVEILLER
- Le 08/06 13:00 : Score Global **48.0** — **SURVEILLER** (confirmé)

L'upgrade de ÉVITER → SURVEILLER reste **purement mécanique** (post-baisse). Les scores fondamentaux (Catalyseur 4.0, Valorisation 3.5) restent dans la zone de disqualification relative.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (10:00) | Valeur révisée (13:00) | Justification |
|--------|---------------------------|------------------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé |
| **Stop-loss** | $12.12 | **$12.12** | Cours − 2×ATR |
| **Take-profit** | $17.77 | **$17.77** | Cours + 3×ATR |
| **Upside / Downside** | −24.9% / −15.7% | **−24.9%** / **−15.7%** | Inchangé |
| **Ratio R/R** | 1.5× | **1.5×** | Stable |
| **Sizing** | — | **—** | Pas de position |

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 20% | Retour $15.47–$16.25 | Comblement partiel du gap, soutenu par un catalyseur (contrat 5G, upgrade). Nécessite cassure du max pain $15.00 |
| **Central** | 50% | Range $13.50–$15.00 | Consolidation autour de la nouvelle base. MM50 ($12.16) agit comme ancre technique. Pin options $15.00 capte le cours |
| **Pessimiste** | 30% | Cassure $14.00 → test MM50 $12.16 | Distribution continue, retour vers les fondamentaux (consensus $10.8). Volume élevé confirme la sortie |

---

## 9. Conclusion — Thèse confirmée

**Verdict :** La thèse précédente (« SURVEILLER — value trap, surchauffe dissipée mais pas d'opportunité d'achat ») est **confirmée** après traitement du DRAFT_refresh.

**Ce qui a changé :**
1. **Données options restaurées.** Max pain remonté à $15.00 (vs $3.00 corrompu à 10:00). Le cours passe sous le pin (−4.1%), créant une pression baissière à l'expiration du 12/06.
2. **Structure options inversée.** Call OI tombe de 68.5% à 49.9% ; put/call passe de 0.46 à 1.00. Sentiment neutre, plus call-dominated.
3. **DRAFT_refresh traité.** Les triggers PRICE_GAP (−13.48%) et ATR_SPIKE (7.86%) ont été analysés. Ils ne modifient pas la thèse mais confirment la volatilité post-gap.

**Ce qui n'a pas changé :**
- Données prix/volume/technique/fondamentales strictement identiques au snapshot 10:00.
- Filtre Qualité hors périmètre (2.5/6).
- Aucun catalyseur fondamental.
- Score Global 48.0 — SURVEILLER.
- XLC bottom 3.

**Recommandation révisée :** **SURVEILLER** — Pas de position. La correction de −13.5% a dissipé la surchauffe mais le retournement sous le max pain options ($15.00) et la structure put/call équilibrée ajoutent une incertitude à court terme (expiration 12/06). Une entrée reste exclue sans :
- Test et rebond sur la MM50 ($12.16) avec volume en hausse
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel

**Prochain point de contrôle :** Earnings Q2 FY2026 le **2026-07-23** (dans 45 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json`, `data/recommandations_latest.json`, et fichiers JSON agents.*

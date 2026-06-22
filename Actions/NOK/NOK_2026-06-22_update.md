# NOK — Mise à jour quotidienne (Snapshot 13:00 UTC)

> **Date :** 2026-06-22
> **Type :** Update — snapshot post-midi 13:00 UTC
> **Fichier précédent :** [NOK_2026-06-22_update.md](./NOK_2026-06-22_update.md) (snapshot 10:00 UTC)

---

## 1. Résumé des changements

| Métrique | Snapshot 10:00 UTC (précédent) | Snapshot actuel 13:00 UTC | Δ |
|----------|--------------------------------|---------------------------|---|
| **Close** | **$13.49** | **$13.49** | **Inchangé** |
| **Previous close** | $13.98 | **$13.83** | **−$0.15** (correction source) |
| **Open** | $14.00 | **$14.00** | **Inchangé** |
| **High** | $14.04 | **$14.04** | **Inchangé** |
| **Low** | $13.29 | **$13.29** | **Inchangé** |
| **RSI 14j** | 42.18 | **42.18** | **Inchangé** |
| **ATR 14j** | $1.08 | **$1.08** | **Inchangé** |
| **MM 50j** | $13.17 | **$13.17** | **Inchangé** |
| **Volume session** | 126.8M | **126.8M** | **Inchangé** |
| **Volume vs moy. 20j** | 0.98× | **0.98×** | **Inchangé** |
| **Options max pain** | $14.00 (opérationnel 17/06) | **$14.00** | **Confirmé** |
| **Put/Call ratio** | 0.46 (opérationnel 17/06) / null (corrompu) | **1.03** | **Révisé +124%** |
| **Call OI %** | 68.3% (opérationnel 17/06) / null (corrompu) | **49.3%** | **Révisé −19.0 pp** |
| **Score Global ajusté** | 46.8 — SURVEILLER | **46.8 — SURVEILLER** | **Inchangé** |
| **Score Opportunité** | 4.2/10 | **4.2/10** | **Inchangé** |
| **Score Momentum** | 5.5/10 | **5.5/10** | **Inchangé** |

**Verdict :** Le snapshot 13:00 UTC confirme la **stabilité parfaite** des données prix/volume/technique vs le snapshot 10:00 UTC. La principale évolution est la **restauration complète des données options** dans `data/latest.json` : le max pain aberrant ($3.00) est corrigé en **$14.00** (confirmé), mais les ratios options sont significativement révisés — le put/call passe de 0.46 (opérationnel du 17/06) à **1.03**, et le call OI de 68.3% à **49.3%**. La structure passe d'un biais call-dominated fort à une configuration **quasi-neutre** (put légèrement majoritaire). Cette révision atténue le pin risk haussier précédemment identifié. Le cours à **$13.49** reste **−3.6% sous le max pain** $14.00, mais sans domination call, la pression de rappel vers $14.00 est moindre.

---

## 2. Bloc Prix & Technique

| Métrique | Valeur | Source | Commentaire |
|----------|--------|--------|-------------|
| Previous close | **$13.83** | `data/latest.json` | Corrigé vs $13.98 du snapshot 10h |
| Open | **$14.00** | `data/latest.json` | +1.23% vs previous close |
| High | **$14.04** | `data/latest.json` | Résistance intraday |
| Low | **$13.29** | `data/latest.json` | Low étendu testé |
| Close | **$13.49** | `data/latest.json` | −2.46% vs previous close |
| Volume | **126,787,700** | `data/latest.json` | Normalisation complète |
| Volume vs moy. 20j | **0.98×** | Calcul (129.7M) | Participation à la moyenne |
| RSI 14j | **42.18** | `data/latest.json` | Neutre inférieur, biais légèrement baissier |
| ATR 14j | **$1.08** | `data/latest.json` | Volatilité stable (8.0% du cours) |
| MM 50j | **$13.17** | `data/latest.json` | Cours +2.4% au-dessus |
| MM 200j | **null** | `data/latest.json` | [DONNÉES MANQUANTES] |
| Golden Cross | **Non** | `data/latest.json` | — |
| 52w high / low | **$17.45 / $4.00** | `data/latest.json` | Cours à −22.7% du 52w high |

**Niveaux clés (inchangés) :**
- Support immédiat : **$13.29** (low du jour)
- Support intermédiaire : **$13.17** (MM50)
- Support structurel : **$12.99** (ancienne MM50, base gap 08/06)
- Résistance technique : **$14.00** (open / max pain options) / **$14.04** (high du jour)
- Résistance structurelle : **$14.27** (ancien support devenu résistance)
- Stop-loss ATR (2×) : **$11.33** ($13.49 − 2×$1.08)
- Take-profit ATR (3×) : **$16.73** ($13.49 + 3×$1.08)
- Ratio R/R : **1.5×**

**Verdict timing :** **Neutre à légèrement défavorable** — Aucune mutation technique entre 10h et 13h. La correction de −2.46% vs previous close ($13.83) reflète la continuité de la pression baissière résiduelle. Le RSI stable à 42.18 et le volume normalisé (0.98×) maintiennent une configuration de consolidation sans direction claire. Le cours reste au-dessus de la MM50 (+2.4%). La nouveauté est la **révision des ratios options** qui retire le biais haussier de la structure call-dominated observée le 17/06.

---

## 3. Bloc Fondamental

Inchangé en structure. Filtre Qualité hors périmètre (2.5/6).

| Métrique | Valeur | Source |
|----------|--------|--------|
| Market Cap | $75.3B (Yahoo) / $29.8B (FMP) | `data/latest.json` |
| P/E (TTM) | 84.31 (Yahoo) / 50.06 (FMP) | `data/latest.json` |
| Forward P/E | 27.71 | `data/latest.json` |
| EV/EBITDA | 28.79 (Yahoo) / 13.13 (FMP) | `data/latest.json` |
| P/B | 3.11 (Yahoo) / 1.42 (FMP) | `data/latest.json` |
| Beta | 0.781 | `data/latest.json` |
| Dividend Yield | 1.21% (Yahoo) / 2.55% (FMP) | `data/latest.json` |
| Short Interest | 1.19% | `data/latest.json` |
| FMP Consensus PT | $10.8 (7 analysts) | FMP Stable API |
| FMP Gross Margin | 43.5% | FMP Stable API |
| FMP Operating Margin | 3.9% | FMP Stable API |
| FMP ROIC | 1.9% | FMP Stable API |
| FMP D/E | 0.25 | FMP Stable API |
| FMP Net Debt/EBITDA | −0.11 (net cash) | FMP Stable API |

**Filtre Qualité :** 2.5/6 — 🔴 Hors périmètre (inchangé).

**Divergence structurelle Yahoo/FMP persistante :**
- P/E Yahoo 84.31 vs FMP 50.06 (écart +68%)
- Market cap Yahoo $75.3B vs FMP $29.8B (écart +153%)
- Consensus FMP cible **$10.8**, soit **−20.0%** de downside vs le cours $13.49.

---

## 4. Bloc Sentiment, Options & News

| Signal | Valeur | Source | Commentaire |
|--------|--------|--------|-------------|
| Consensus analystes (FMP) | **$10.8** (7 analysts) | FMP Stable API | Inchangé — premium consensus +24.9% |
| Max pain options | **$14.00** | `data/latest.json` | ✅ Corrigé de $3.00 (aberrant) → confirmé |
| Put/Call ratio | **1.03** | `data/latest.json` | ✅ Corrigé de null — structure quasi-neutre, puts légèrement majoritaires |
| Call OI % | **49.3%** | `data/latest.json` | ✅ Corrigé de null — quasi-équilibre calls/puts |
| Expiration nearest | **2026-06-26** | `data/latest.json` | Dans 4 jours |
| Social sentiment (Reddit) | 0 mentions / No data | `social_sentiment_2026-06-22.json` | Aucune mention, aucun pump |

**Structure options (révisée) :**
- Max pain **$14.00** (confirmé). Cours $13.49 = **−3.6% sous le max pain**.
- **Put/call 1.03** (vs 0.46 opérationnel du 17/06) : la structure passe d'un fort biais haussier (calls majoritaires) à une configuration **quasi-neutre avec légère domination put**. Cela indique que les participants options ont couvert leur exposition à la baisse après la correction récente.
- **Call OI 49.3%** (vs 68.3% opérationnel du 17/06) : confirme la normalisation du sentiment. La domination call est dissipée.
- **Pin risk atténué** : avec une structure quasi-neutre, la pression de rappel vers le max pain $14.00 est moins forte qu'anticipée ce matin (où la domination call 68.3% suggérait une pression haussière). Cependant, le cours −3.6% sous le max pain reste un écart significatif à 4 jours de l'expiration.

**News / Événements :**
- `events_2026-06-22.json` : **0 événement** corporate pour NOK
- `news_2026-06-22.json` : **0 article** pour NOK
- Aucun upgrade/downgrade, insider trade ou contrat gouvernemental signalé
- Earnings Q2 FY2026 confirmé le **2026-07-23** (dans 31 jours) — Est EPS $0.06–$0.08, Rev $4.8B

---

## 5. Bloc Macro & Sectoriel

- **Régime macro :** UNKNOWN (`recommandations_2026-06-22.json` — VIX et taux non disponibles)
- **Sectoriel :** Technology / Communication Equipment. Le secteur **XLC** (Communication Services) reste en **bottom 3** du sector rotation (`sector_rotation_2026-06-22.json` : return 20j −5.73%, return 60j −1.51%, momentum score 0.0). Malus structurel persistant.
- **Exposition FX :** `fx_exposure_2026-06-22.json` : NOK — exposure 25%, direction export, primary currency USD. Impact revenus/EPS estimé 0%. Divergence aligned. Flag 🟢. Contexte neutre.
- **Géopolitique :** Aucun événement politique détecté pour NOK (`geo_risk_2026-06-22.json` : 0 ticker flagged, 0 événement).
- **Quant :** Insuffisant (`quant_report_latest.json` : 0 signaux historiques, p-value 1.0)
- **Accounting :** Fichier absent (`accounting_risk_latest.json`) — pas de donnée M-Score/Z-Score disponible.
- **Social sentiment :** No data (`social_sentiment_2026-06-22.json` : 0 mentions, sentiment 0.0, pump_detected false).

---

## 6. Nouveau Scoring Global

**Source :** `data/recommandations_2026-06-22.json` — scoring NOK inchangé.

| Score | Valeur | Commentaire |
|-------|--------|-------------|
| **Score Opportunité** | **4.2/10** | C:4.0 V:3.5 M:5.5 |
| **Score Catalyseur** | 4.0/10 | 🔴 Faible — aucun catalyseur identifié |
| **Score Valorisation** | 3.5/10 | 🔴 Défavorable — P/E 84.3, premium consensus +24.9% |
| **Score Momentum** | 5.5/10 | 🔴 Faible — RSI 42.18, volume normalisé, low étendu |
| **Score Global ajusté** | **46.8/100** | **SURVEILLER** (seuil 35–49) |
| **Timing technique** | Neutre à défavorable | RSI stable sous 50, MM50 validée, correction −2.46% session |

**Évolution du scoring :**
- Snapshot 10h UTC : Score Global **46.8** — **SURVEILLER**
- Snapshot 13h UTC : Score Global **46.8** — **SURVEILLER** (stable)

Le scoring des agents est inchangé. La révision des données options n'a pas impacté les scores quantitatifs (les agents ne semblent pas intégrer le put/call ratio dans le scoring automatique). La structure quasi-neutre des options n'améliore ni ne dégrade le profil risque/rendement fondamental.

---

## 7. Révision des Niveaux SL / TP / Sizing

| Niveau | Valeur précédente (10h UTC) | Valeur actuelle | Justification |
|--------|-------------------------------|-----------------|---------------|
| **Prix cible** | $10.8 (consensus) | **$10.8** | Inchangé — 7 analystes FMP |
| **Stop-loss** | $11.33 | **$11.33** | Inchangé — ATR $1.08, close $13.49 |
| **Take-profit** | $16.73 | **$16.73** | Inchangé — ATR $1.08, close $13.49 |
| **Upside / Downside** | −20.0% / −16.0% | **−20.0% / −16.0%** | Cours $13.49 vs consensus $10.8 |
| **Ratio R/R** | 1.5× | **1.5×** | Stable (ATR-based) |
| **Sizing** | — | **—** | Pas de position |

**Note :** Les niveaux sont conservés. La stabilité du cours ($13.49) et de l'ATR ($1.08) justifient le maintien des seuils. Une cassure sous $13.17 (MM50) invaliderait la tendance haussière de court terme. Une cassure sous $12.99 ouvrirait la voie vers $12.00.

---

## 8. Scénarios & Probabilités

| Scénario | Probabilité | Impact cours | Description |
|----------|-------------|--------------|-------------|
| **Optimiste** | 15% | Rebond vers $14.00 | Le cours tient le support $13.29 et rebondit avec volume confirmé > moyenne 20j. Test de la résistance $14.00 (max pain options). La structure options quasi-neutre (call OI 49.3%) offre moins de soutien haussier qu'anticipé ce matin, mais l'absence de domination put limite la pression vendeuse. Nécessite catalyseur (news 5G, upgrade, contrat). |
| **Central** | 60% | Range $13.29–$14.00 | Consolidation autour du close $13.49. Le max pain $14.00 agit comme aimant modéré mais la structure options quasi-neutre réduit la force du pin. Support $13.29 validé, résistance $14.00 agit comme plafond. Attente des earnings du 23/07. Pas de direction claire sans catalyseur. |
| **Pessimiste** | 25% | Retest $13.17 puis $12.99 | La correction se poursuit. Test du support $13.17 (MM50). Si cassure, objectif $12.99 (ancienne MM50, base du gap du 08/06). La structure put/call 1.03 confirme un léger biais défensif des participants options. Volume normalisé (0.98×) ne garantit pas l'accumulation. RSI sous 50 = biais baissier sous-jacent. |

**Probabilité ajustée :** Le scénario central reste dominant (60%). La principale nuance par rapport au snapshot 10h est l'**atténuation du pin risk haussier** : la structure options quasi-neutre (call OI 49.3%, put/call 1.03) invalide l'hypothèse d'une pression haussière vers $14.00 due à une domination call massive. L'expiration dans 4 jours (2026-06-26) avec max pain $14.00 crée toujours un aimant modéré, mais sans la couverture call-dominated du 17/06, le risque de clôture proche du max pain est moins asymétrique à la hausse. Le support $13.29 (low du jour) reste le niveau critique.

---

## 9. Conclusion — Thèse confirmée avec ajustement options

**Verdict :** La thèse **SURVEILLER** est **confirmée sans modification de recommandation**, mais avec un **ajustement significatif de l'interprétation des options**. Le snapshot 13:00 UTC apporte une **correction des données options** qui modifie la lecture du sentiment dérivé : passage d'une structure call-dominated (68.3% call OI, put/call 0.46) à une structure **quasi-neutre** (49.3% call OI, put/call 1.03). Cette révision atténue le pin risk haussier et confirme l'absence de conviction directionnelle forte du marché options.

**Ce qui a changé :**
- **Données options :** Correction complète dans `data/latest.json` — max pain confirmé **$14.00** (vs $3.00 aberrant), put/call révisé **1.03** (vs null/0.46), call OI révisé **49.3%** (vs null/68.3%). La structure passe de bullish à **quasi-neutre**.
- **Previous close :** Corrigé à **$13.83** (vs $13.98 dans le snapshot 10h — erreur source corrigée).
- **Pin risk :** Atténué — sans domination call, la pression de rappel vers $14.00 est moins forte. Le cours −3.6% sous le max pain reflète plutôt un consensus options légèrement défensif.

**Ce qui n'a pas changé :**
- Cours stable à **$13.49**, RSI 42.18, ATR $1.08, volume 0.98×.
- Filtre Qualité hors périmètre (2.5/6) — bilan solide mais rentabilité anémique (ROIC 1.9%, operating margin 3.9%).
- Consensus analystes **$10.8** (7 analysts) — premium +24.9%.
- Divergence Yahoo/FMP persistante (P/E 84.3 vs 50.1, market cap $75.3B vs $29.8B).
- XLC bottom 3 du sector rotation (momentum score 0.0).
- Aucun catalyseur fondamental, aucune news structurante, aucun événement corporate.
- Exposition FX neutre (flag 🟢), géopolitique neutre, social sentiment nul.
- Quant insuffisant, accounting non disponible.
- Score Global **46.8/100 — SURVEILLER** (stable).

**Recommandation révisée :** **SURVEILLER** — Pas de position. Une entrée reste exclue sans :
- Stabilisation du cours au-dessus de **$14.00** avec volume de confirmation > 1.1× moyenne 20j
- Retour du RSI au-dessus de **45** avec un close confirmé
- Test et rebond sur la MM50 ($13.17) avec pattern de reversal
- Franchissement durable au-dessus de **$14.27** (ancien support) avec volume
- Amélioration du Score Valorisation > 5.0/10
- Apparition d'un catalyseur sectoriel (contrat 5G, upgrade, guidance positive)

**Risque immédiat :** L'expiration des options dans 4 jours (2026-06-26) avec max pain $14.00. La structure quasi-neutre (call OI 49.3%) élimine le risque d'un squeeze haussier massif, mais le cours −3.6% sous le max pain expose à une fermeture contrariante si les puts ITM sont exercés. L'amplitude probable du mouvement reste contenue par l'ATR ($1.08).

**Prochain point de contrôle :** Snapshot post-session du 22/06 pour valider la tenue du support $13.29 et le volume de clôture. Earnings Q2 FY2026 le **2026-07-23** (dans 31 jours) — Est EPS $0.06–$0.08, Rev $4.8B.

---

*Généré automatiquement — données sourcées exclusivement depuis `data/latest.json` (snapshot 2026-06-22 13:00 UTC), `data/recommandations_2026-06-22.json`, `data/sector_rotation_2026-06-22.json`, `data/fx_exposure_2026-06-22.json`, `data/social_sentiment_2026-06-22.json`, `data/upcoming_events_2026-06-22.json`, `data/events_2026-06-22.json`, `data/geo_risk_2026-06-22.json`, et fichiers JSON agents.*

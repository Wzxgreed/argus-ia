# CTMX — Mise a Jour — 2026-06-23 (Snapshot 13h UTC)

> **Societe :** CytomX Therapeutics, Inc.
> **Secteur :** Healthcare / Biotechnology — Probody therapeutics
> **Exchange :** NASDAQ
> **Date :** 2026-06-23
> **Snapshot :** 13:00 UTC
> **Analyste :** Desk Argus-IA

---

## Resume Executif

**Stabilite mecanique totale** vs snapshot 10h UTC. Le cours se maintient a **$3.04** (inchangé vs cloture officielle $3.04 du 22/06, +3.05% vs previous close $2.95), le **RSI reste a 31.53** (survente persistante mais attenuee), l'**ATR a $0.17** (stable) et le volume se normalise a **3.78M (0.91x moyenne 20j)** — en ligne avec la session precedente (3.74M, 0.90x).

**ANOMALIE OPTIONS JSON RESOLUE** : `data/latest.json` du snapshot 13h UTC retourne desormais des **valeurs propres** pour les options. Le max_pain est confirme a **$4.00**, le put/call ratio a **2.87** (vs 8.91 valeur operationnelle conservee au snapshot 10h), et le call OI a **25.8%** (vs 10.1%). Cette resolution confirme que les valeurs aberrantes du snapshot 10h (max_pain $1.00, put/call `null`, call OI `null`) etaient bien un faux positif algorithmique, et la structure reelle s'est **nettement amelioree** par rapport a l'extreme baissiere du snapshot 10h.

**Recommandation et scores** : **SURVEILLER** avec **Score Global Ajuste 48.8/100** (inchangé). Score Opportunite **5.7/10** (C:6.5 V:6.0 M:4.0). Le timing reste **Defavorable**.

---

## Changements depuis l'Analyse Precedente (Snapshot 10h UTC 2026-06-23)

### 1. Technique — Stabilite mecanique totale

| Indicateur | 2026-06-23 (10h UTC) | 2026-06-23 (13h UTC) | Signal |
|---|---|---|---|
| Cours close | **$3.04** | **$3.04** | **Inchange** |
| Previous close | $2.95 | **$2.95** | — |
| Open / High / Low | 2.98 / 3.0777 / 2.95 | **2.98 / 3.078 / 2.95** | Range identique |
| Volume | 3,780,400 | **3,780,400** | **Inchange** |
| Volume rel. 20j | 0.91x | **0.91x** | **NORMALISE** |
| RSI 14j | 31.53 | **31.53** | **Inchange** — survente persistante |
| ATR 14j | $0.17 | **$0.17** | **Stable** |
| MM 50j | $3.80 | **$3.80** | **Stable**, ecart **-20.0%** |
| MM 200j | null | **null** | [DONNEES PARTIELLES] |
| Short Interest | 14.97% | **14.97%** | **Stable** |
| 52W High / Low | $8.21 / $1.72 | **$8.21 / $1.72** | — |

**Verdict technique :** Aucun mouvement significatif entre le snapshot 10h UTC et le snapshot 13h UTC. Le cours $3.04, le RSI 31.53 et l'ATR $0.17 sont strictement identiques. Le volume a 0.91x confirme la normalisation post-expiration du 18/06. Le cours reste sous MM50 ($3.80, ecart -20.0%). Le support $2.86 (low du 16/06) n'est pas teste (low $2.95). Le timing reste **Defavorable**.

### 2. Options — Amelioration structurelle majeure

| Indicateur | Snapshot 10h UTC (anomalie traitee) | Snapshot 13h UTC (valeurs propres) | Signal |
|---|---|---|---|
| Max Pain | $4.00 (conserve) | **$4.00** | **Confirme** |
| Put/Call Ratio | 8.91 (operationnel conserve) | **2.87** | **AMELIORATION** — baissiere → moderee |
| Call OI % | 10.1% (operationnel conserve) | **25.8%** | **AMELIORATION** — triple vs 10h |
| Expiration proche | 2026-07-17 | **2026-07-17** | Inchangee |

**Verdict options :** La resolution de l'anomalie JSON confirme que la structure optionnelle reelle est **nettement moins baissiere** que l'extreme observe au snapshot 10h. Le put/call a **2.87** (vs 8.91) reste au-dessus de 1.0 (faveur puts) mais sort de la zone extreme (>5.0). Le call OI a **25.8%** (vs 10.1%) indique une re-entree partielle des positions haussieres. Ces valeurs sont **propres dans le JSON source** (`latest.json` 13h UTC) et constituent une **amelioration technique significative**.

**Implications :**
- La domination puts persiste (put/call 2.87 > 1.0) mais l'extreme baissier du snapshot 10h (8.91) etait un artefact algorithmique.
- Le max pain a $4.00 reste au-dessus du spot ($3.04), maintenant une pression technique vers le haut, mais la convergence est desormais moins contrariee.
- L'amelioration du call OI (25.8%) suggere que des acheteurs haussiers re-emergent apres l'expiration du 18/06.

### 3. Fondamental — Aucun changement

Donnees FMP FY2025 inchangées. Pas de nouveau filing SEC, pas de guidance update, pas de nouvelles collaborations annoncees depuis le snapshot 10h UTC.

| Metrique | Valeur | Statut |
|----------|--------|--------|
| Market Cap (Yahoo) | **$661.8M** | Stable |
| Market Cap (FMP) | $587.6M | — |
| EV/Revenue | 8.946 (Yahoo) / 7.60 (FMP) | Eleve pour biotech pre-commercial |
| Forward P/E | -6.26 | Pertes attendues |
| Short Interest | **14.97%** | Stable |
| Current Ratio | 3.09 | Tresorerie confortable |
| Cash / Working Capital | $97.3M / $97.3M | Runway ~2–3 ans |
| Filtre Qualite | **2/6** | Hors perimetre (inchange) |

**Consensus Analystes (FMP) :**
- Price target moyen : **$9.05** (+198% upside vs $3.04)
- Nombre d'analystes : **11** (0 ce mois, 2 ce trimestre)
- Sources : TheFly, StreetInsider, Benzinga

### 4. Sentiment / News / Social

| Indicateur | Snapshot 10h UTC | Snapshot 13h UTC | Signal |
|---|---|---|---|
| News pipeline | Aucune | **Aucune** | — |
| Social Sentiment | 0/10 | **0/10** | Aucun interet retail |
| Pump detection | Non | **Non** | — |

**Verdict sentiment :** Neutre a baissier. Aucune news, aucun interet retail. Le consensus analystes reste le seul soutien haussier structurel (PT +198%). Le short interest stable a 14.97% maintient le potentiel de short squeeze, et l'amelioration de la structure optionnelle (call OI 25.8%) renforce legerement la probabilite d'un squeeze haussier en cas de catalyseur.

---

## Contexte Sectoriel & Macro

| Facteur | Impact | Detail |
|---------|--------|--------|
| **XLV (Healthcare)** | Defensif sous-performant | `data/sector_rotation_2026-06-23.json` : regime UNKNOWN, XLV momentum_score **1.53** (rang 6e/11), return_20d +1.74% vs SPY +0.48% — surperformance relative marginale. |
| **Biotech specifique** | Risque eleve | Sous-secteur biotech early-stage reste penalise. |
| **Rotation sectorielle** | `NEUTRAL` | Signal macro du jour : top3 = XLK / XLI / XLF, bottom3 = XLP / XLY / XLC. Healthcare neutre. |
| **DXY / FX** | Neutre | `data/fx_exposure_2026-06-23.json` : CTMX exposure ~55% EUR/CNY, FX Impact Score **0.0** — aucun headwind/tailwind. |
| **Geo risk** | Non flagge | `data/geo_risk_latest.json` (2026-05-17) : CTMX non present, aucun risque geo detecte. |
| **Accounting risk** | Scan indisponible | `data/accounting_risk_latest.json` absent — pas de M-Score/Z-Score. |
| **Event-driven** | Aucun | `data/events_2026-06-23.json` : 0 evenement corporate detecte pour CTMX. |
| **Earnings** | J+44 | Earnings confirme le **2026-08-06** (Est EPS $-0.13 a $-0.07, Rev $0.0B). Pas de preview requis. |
| **Quant** | Calibration en cours | `data/quant_report_latest.json` (2026-05-17) : 0 signaux, p-value null — pas assez d'historique. |
| **Social Sentiment** | Aucun | `data/social_sentiment_2026-06-23.json` : CTMX 0 mentions, sentiment 0/10, pump non detecte. |
| **Upcoming Events** | J+44 | `data/upcoming_events_2026-06-23.json` : earnings **2026-08-06** (J+44). Aucun autre evenement structurant. |
| **Validation** | OK | `data/validation_report.txt` (2026-06-23) : 0 CRITICAL, CTMX non concerne par les 4 errors / 0 warnings. |

---

## Scoring Global (Agents) — Actualise Snapshot 13h UTC

| Axe | Score | Pondération Regime Normal | Contribution | Justification |
|-----|-------|---------------------------|------------|---------------|
| Catalyseur | **6.5/10** | 35% | 2.28 | Pipeline Probody + partenariats majeurs. Aucun catalyseur immediat. Amelioration structurelle options (put/call 2.87 vs 8.91, call OI 25.8% vs 10.1%) reduit le malus technique. Volume normalise 0.91x. |
| Valorisation | **6.0/10** | 40% | 2.40 | Biotech pre-profit, PT consensus +198% offre upside asymetrique accru sur le cours faible. Plafonne par Filtre Qualite 2/6. |
| Momentum | **4.0/10** | 25% | 1.00 | RSI 31.53 survente persistante mais attenuee. Volume 0.91x normalise. Cours sous MM50 ($3.80, ecart -20.0%). |
| **Score Opportunite** | **5.7/10** | — | — | **Inchange** vs snapshot 10h UTC |
| **Malus** | | | -8.0 | Biotech pre-revenue + pertes (Filtre Qualite <= 3/6) + sous-performance sectorielle XLV |
| **Bonus** | | | +0.0 | Aucun bonus detecte |
| **Score Global** | **56.8/100** | | | **Inchange** |
| **Score Global Ajuste** | **48.8/100** | | | **Inchange** — sous le seuil institutionnel (50) |

**Action recommandee :** **SURVEILLER** *(inchangee depuis snapshot 10h UTC)*
**Timing :** Defavorable *(inchange)*
**Sizing :** — (pas de position recommandee)

**Note de fiabilite :** Score Global Ajuste 48.8/100 — sous le seuil institutionnel. La stabilite mecanique totale (cours, RSI, ATR, volume inchanges) est un signal neutre. L'amelioration de la structure options (put/call 2.87 vs 8.91, call OI 25.8% vs 10.1%) est un signal technique positif mais non suffisant pour modifier le scoring global, qui reste contraint par le Filtre Qualite 2/6 et le malus sectoriel. Aucun catalyseur fondamental n'est detecte.

---

## Revision des Niveaux SL / TP

Revision mecanique sur base ATR $0.17 et close $3.04.

| Niveau | Valeur | Methode |
|--------|--------|---------|
| Prix de reference | **$3.04** | Close 2026-06-23 (13h UTC) |
| Stop-loss suggere | **$2.70** | Cours ref - 2xATR ($3.04 - $0.34) — aligne avec JSON agent |
| Take-profit technique | **$3.55** | Cours ref + 3xATR ($3.04 + $0.51) — aligne avec JSON agent |
| Take-profit consensus | **$9.05** | Price target moyen analystes |
| Ratio R/R (technique) | **1.5** | $0.51 / $0.34 |
| Ratio R/R (consensus) | **17.5** | $6.01 / $0.34 |

**Attention :** Le ratio R/R consensus reste trompeur pour une biotech pre-revenue. Le risque de gap-down en cas d'echec clinique peut depasser 50%. Le support $2.86 (low du 16/06) n'a pas ete teste aujourd'hui (low $2.95). Si le cours cloture au-dessus de $3.20 avec volume > 1.0x moyenne, cela confirmerait un rebond technique. Un retour sous $2.86 avec volume > 1.0x activerait la degradation vers EVITER.

---

## Conclusion — Snapshot 13h UTC

**These : NON ETABLIE — PROFIL SPECULATIF BIOTECH — SURVEILLER (INCHANGE)**

Le snapshot du 2026-06-23 a 13h UTC confirme la **stabilite mecanique totale** vs le snapshot 10h UTC : cours **$3.04** (inchangé), RSI **31.53** (survente persistante attenuee), ATR **$0.17** (stable), volume **3.78M (0.91x)** — normalisation confirmee. Aucun nouveau signal technique, fondamental ou sentiment n'est apparu.

**L'anomalie JSON sur les options est RESOLUE** et confirme une **amelioration structurelle** : put/call **2.87** (vs 8.91 au snapshot 10h), call OI **25.8%** (vs 10.1%). Ces valeurs propres indiquent une structure moins extreme que l'artefact algorithmique du matin. Le pivot baissier du 2026-06-22 (put/call 8.91, call OI 10.1%) est partiellement attenué — la structure n'est plus ultra-baissiere mais reste defensive (put/call > 1.0).

**La recommandation reste SURVEILLER** avec **Score Global Ajuste 48.8/100** (sous seuil 50). L'amelioration optionnelle est un signal positif mais insuffisant pour compenser le Filtre Qualite 2/6 et le malus sectoriel. Aucune mutation fondamentale n'est detectee. Le support $2.86 n'est pas casse. Le biotech early-stage reste sous-performant sectoriellement (XLV momentum 1.53/10).

**Ce qui a change depuis le snapshot 10h UTC :**
- :green_circle: Cours : **$3.04** (inchangé)
- :green_circle: RSI : **31.53** (inchangé — survente persistante attenuee)
- :green_circle: ATR : **$0.17** (stable)
- :green_circle: Volume : **3.78M (0.91x)** — stabilisation post-expiration
- :yellow_circle: MM50 : **$3.80** (stable, ecart -20.0%)
- :green_circle: Options : **ANOMALIE JSON RESOLUE** — valeurs propres confirmees (max_pain $4.00, put/call **2.87**, call OI **25.8%**)
- :green_circle: Structure options : **Amelioration** — put/call passe de 8.91 a 2.87 (extreme baissier → modere baissier)
- :yellow_circle: Recommandation : **SURVEILLER** (inchangee)
- :yellow_circle: Score Global Ajuste : **48.8/100** (inchange — sous seuil 50)
- :yellow_circle: SL/TP : **$2.70 / $3.55** (inchanges)
- :yellow_circle: Timing : **Defavorable** (inchange)
- :x: Aucune news majeure
- :x: Structure optionnelle baissiere persistante mais attenuée (put/call 2.87)

**Conditions de passage a ATTENDRE (upgrade) :**
1. Cloture au-dessus de $3.20 avec volume > 1.0x moyenne (recapture MM50)
2. Retournement de la structure options vers put/call < 1.0 avec call OI > 60%
3. Catalyseur fondamental (data readout, annonce partenariat majeur)
4. Score Global Ajuste > 50 avec malus sectoriel reduit

**Conditions de passage a EVITER (degradation) :**
1. Retour sous $2.86 avec volume > 1.0x moyenne (support casse)
2. Echec clinique majeur (stop essai)
3. Dilution capitale > 20% sans catalyseur
4. Maintien de la structure optionnelle baissiere (put/call > 2.0) jusqu'a l'expiration 2026-07-17

**Alertes actives :**
- :yellow_circle: Cours $3.04 — stable sous MM50 ($3.80, ecart -20.0%)
- :green_circle: Volume **0.91x** — normalise post-expiration
- :red_circle: RSI 31.53 — survente persistante
- :green_circle: Support $2.86 **NON TESTE** (low $2.95)
- :green_circle: Short interest 14.97% — stable, potentiel short squeeze si catalyseur
- :red_circle: Cours sous MM50 ($3.80) avec ecart -20.0%
- :red_circle: Score Global Ajuste 48.8/100 — **sous le seuil institutionnel (50)**
- :red_circle: Recommandation SURVEILLER — degradee depuis ATTENDRE
- :yellow_circle: Options — **PIVOT BAISSIER ATTENUE** (put/call 2.87, call OI 25.8%, max pain $4.00) — amelioration vs 8.91/10.1%
- :yellow_circle: Expiration options **2026-07-17** — J+24 avec structure baissiere attenuée
- [WARNING] Donnees MM200 manquantes
- [WARNING] Biotech pre-revenue — scoring standard peu fiable
- [INFO] Earnings confirme le 2026-08-06 (J+44) — Est EPS $-0.13 a $-0.07
- [INFO] Anomalie options JSON du snapshot 10h UTC **RESOLUE** au snapshot 13h UTC (valeurs propres confirmees)

---

*Rapport genere automatiquement — snapshot 2026-06-23 13:00 UTC.*
*Analyse precedente : `CTMX_2026-06-23_update.md` (snapshot 10h UTC) — close $3.04, SURVEILLER, anomalie options JSON traitee.*

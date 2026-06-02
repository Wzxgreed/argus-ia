# ASTS — Mise à Jour Snapshot 10h UTC (2026-06-02)

> **Stabilité apparente, baisse officielle** : cours **$105,65** à 10h UTC (vs close officiel 2026-06-01 à **$113,41**), soit une baisse de **−6,84%** en séance. RSI stable à **61,89**, volume **normalisé 1,00×**, mais **anomalie data quality options détectée** (Max Pain $40,00 vs historique $120,00, Put/Call et Call OI null). Score global ajusté **44,8/100 (SURVEILLER)**. Thèse **SURVEILLER confirmée**.

---

## Résumé des Changements depuis l'Analyse Précédente

| Indicateur | Snapshot 21h UTC 2026-06-01 | Snapshot 10h UTC 2026-06-02 | Delta |
|-----------|-----------------------------|-----------------------------|-------|
| **Cours** | **$105,65** | **$105,65** | **—** 🟢 |
| vs previous close | $113,41 | $113,41 | **−6,84%** 🔴 |
| RSI 14j | **61,89** | **61,89** | **—** |
| ATR 14j | **$12,18** | **$12,18** | **—** |
| MM50 | **$87,11** | **$87,11** | **—** |
| Volume rel. | **1,00×** | **1,00×** | **—** |
| Market Cap | **$41,01B** | **$41,01B** | **—** |
| Forward P/E | **−355,57** | **−355,57** | **—** |
| EV/Revenue (Yahoo) | **405,30×** | **378,00×** | **−27,30×** 🟢 |
| P/B (Yahoo) | **15,16×** | **15,16×** | **—** |
| 52W high | **$133,86** | **$133,86** | **—** |
| Consensus PT | **$94,54** | **$94,54** | **—** |
| Downside consensus | **−10,5%** | **−10,5%** | **—** |
| Short Interest | **17,60%** | **17,60%** | **—** |
| Score Global ajusté | **44,8** | **44,8** | **—** |
| Max Pain | **$120,00** | **$40,00** | **−$80,00** 🔴 [ANOMALIE] |
| Put/Call Ratio | **0,92** | **null** | **[DONNÉES MANQUANTES]** 🔴 |
| Call OI % | **52,2%** | **null** | **[DONNÉES MANQUANTES]** 🔴 |

**Verdict :** le cours à 10h UTC ($105,65) est **inchangé** vs le snapshot 21h UTC du 2026-06-01, mais le **close officiel** de la veille était $113,41, ce qui signifie que la baisse de −6,84% vs previous close s'est déroulée **en dehors des heures de négociation principales** (after-hours / pre-market) ou est reflétée dans le previous_close du système. Les données techniques (RSI, ATR, MM50) sont **stables**, le volume reste normalisé. La divergence consensus est maintenue à **−10,5%**. L'écart notable est la **correction de l'EV/Revenue Yahoo** (405× → 378×), probablement un ajustement data feed, et surtout l'**anomalie options** : Max Pain bascule de $120 à $40 (aberrant), Put/Call et Call OI deviennent null — **signal de data quality dégradée**.

---

## Mise à Jour Technique

- **Cours :** $105,65 — **inchangé** vs snapshot 21h 2026-06-01 ; **−6,84%** vs previous close officiel $113,41
- **Range intraday :** $101,21–$111,28 (mêmes niveaux que la veille, pas de nouveau high/low en 10h UTC)
- **RSI 14j :** **61,89** — stable, zone neutre/haussière
- **ATR 14j :** $12,18 (ATR relatif **11,5%** du cours) — **[TRIGGER HAUT]** volatilité extrême persistante
- **MM50 :** $87,11 — cours **+21,3%** au-dessus, support éloigné
- **MM200 :** N/A
- **Volume 10h :** 27,14M vs moy. 20j 27,02M (**1,00×**) — volume parfaitement normalisé, aucun signal de distribution ni d'accumulation
- **52W high :** $133,86 — repli total depuis le sommet : **−21,1%**
- **52W low :** $23,80
- **Supports clés :** $100,00 (psychologique, testé à $101,21) ; MM50 $87,11
- **Résistances clés :** previous close $113,41 ; high intraday $111,28
- **Timing verdict :** **Neutre** (RSI stable, volume normalisé, mais volatilité extrême persistante et gap −6,84% vs close officiel)
- **Score Momentum :** 5,5/10 — **inchangé**. Le gap baissier −6,84% vs close officiel est mécanique (probablement after-hours) et non accompagné d'expansion volume, ce qui atténue son impact sur le momentum intraday

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. La mutation reste **exclusivement technique/data quality**.

- **Market Cap :** $41,01B (stable)
- **Forward P/E :** −355,57 (profil non rentable, stable)
- **EV/EBITDA :** −101,47 (stable)
- **EV/Revenue :** 378,00× (Yahoo) — **ajustement data feed** (−27× vs 405× rapporté hier). Le FMP EV/Revenue est 355,70×. La fourchette reste dans le domaine spéculatif extrême
- **P/B :** 15,16× (Yahoo) / 10,10× (FMP annual) — stable
- **Beta :** 2,598 — sensibilité très supérieure au marché
- **Short Interest :** 17,60% (stable, pas de short squeeze setup)
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes, 5 couverts le mois dernier, 7 le trimestre dernier) — inchangé. Downside consensus **−10,5%** vs cours $105,65
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK** (pas d'exclusion, `accounting_risk_latest.json` absent)

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-02 émet un signal macro **ROTATION_TO_CYCLICAL**. XLK (Technology) #1 du ranking (momentum score 10,0). XLC (Communication Services) est dans le **bottom 3** (momentum score 0,0). Faiblesse sectorielle persistante — le mouvement d'ASTS reste **découplé** de son secteur. Malus sectoriel maintenu.

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence stable à **−10,5%**
- **Options :** 🔴 **ANOMALIE DATA QUALITÉ DÉTECTÉE**
  - Max Pain **$40,00** (vs $120,00 historique cohérent) — **valeur aberrante**, probable corruption du feed options
  - Put/Call Ratio **null** (données manquantes)
  - Call OI % **null** (données manquantes)
  - Nearest expiry : **2026-06-05 (J+3)**
  - **Lecture :** les données options du 2026-06-02 sont **inutilisables** en l'état. Le Max Pain $40 est manifestement erroné (historique $120, spot $105,65). Toute analyse gamma/GEX est suspendue jusqu'à résolution
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_latest.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_risk_latest.json` absent pour ASTS)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-02 (`news_2026-06-02.json` vide pour ASTS)

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+69) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-06-05 (J+3)** — données corrompues, monitoring requis

---

## Scoring Global — Snapshot 10h UTC (2026-06-02)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4,0/10 | 35% | Aucun catalyseur imminent, earnings dans 69j, pas de news structurante — stabilité totale |
| Valorisation | 3,0/10 | 40% | Multiples spéculatifs extrêmes (EV/Revenue 378×, P/B 15,16×), consensus $94,54 = −10,5% sous le cours. Ajustement EV/Revenue Yahoo mais reste extrême |
| Momentum | 5,5/10 | 25% | Gap −6,84% vs close officiel mais sans volume, RSI 61,89 stable, cours +21,3% au-dessus MM50 — momentum haussier de moyen terme intact mais surveillé |
| **Score Opportunité** | **4,0/10** | | |

**Malus / Bonus appliqués (Agent Recommandation) :**
- Malus ATR_SPIKE : volatilité intraday extrême persistante (11,5% du cours)
- Malus sectoriel (XLC bottom 3) : −0,5 pt — faiblesse sectorielle persistante
- Malus consensus sous cours : price target $94,54 vs cours $105,65 = upside négatif −10,5%
- Bonus RSI normalisé : sortie de surachat maintenue, risque de correction technique réduit
- Bonus volume normalisé : 1,00× moyenne 20j = aucun signal de distribution
- Aucun malus comptable (Quality Gate OK, `accounting_risk_latest.json` absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite :** 40,0/100 (ajusté **44,8/100**) — **inchangé** vs 2026-06-01 21h UTC. Confortablement dans la zone SURVEILLER (35–49) → **SURVEILLER**.

---

## Niveaux et Ratio R/R

- **Cours actuel :** $105,65
- **Stop-loss suggéré :** $81,29 (cours − 2×ATR = $105,65 − $24,36) — **inchangé**
- **Take-profit suggéré :** $142,19 (cours + 3×ATR = $105,65 + $36,54) — **inchangé**
- **Ratio R/R :** 1,5:1 — **inchangé**

**Révision :** niveaux maintenus. Le gap −6,84% vs close officiel n'est pas accompagné de volume et n'a pas modifié les niveaux techniques intraday ($101,21–$111,28). Le SL à $81,29 correspond approximativement à la MM50 ($87,11) moins une marge de volatilité. En cas de rupture sous $100 puis $87, la tendance haussière de moyen terme serait invalidée. Le TP $142,19 reste 6,2% au-dessus du 52W high ($133,86). Probabilité d'atteinte faible sans catalyseur majeur.

---

## Conclusion

**Thèse confirmée : SURVEILLER — stabilité totale vs snapshot 21h 2026-06-01 à $105,65, RSI 61,89, volume normalisé 1,00×, divergence consensus −10,5% stable, mais anomalie data quality options détectée (Max Pain $40 aberrant, Put/Call et Call OI null). Gap −6,84% vs close officiel $113,41 non accompagné de volume — probablement mécanique after-hours/pre-market.**

Le snapshot 10h UTC enregistre une **stabilité technique complète** vs le snapshot 21h UTC de la veille. Cours, RSI, ATR, MM50, volume, consensus, market cap, multiples fondamentaux sont **tous inchangés**. Le seul mouvement notable est le **gap baissier −6,84% vs le previous_close officiel $113,41**, qui s'est produit en dehors des heures de négociation standard et sans expansion de volume, suggérant un ajustement mécanique plutôt qu'une distribution active.

**Changements structurants :**
1. **Stabilité technique totale** — cours $105,65, RSI 61,89, ATR $12,18, MM50 $87,11, volume 1,00×. Aucun nouveau signal technique
2. **Gap mécanique −6,84% vs close officiel** — sans volume, non catalysé. Probablement after-hours/pre-market drift
3. **Ajustement EV/Revenue Yahoo** — 405× → 378× (−27×). Reste spéculatif extrême. Le FMP confirme 355,70×
4. **🔴 Anomalie data quality options** — Max Pain $40 (vs $120 historique), Put/Call null, Call OI null. Données inutilisables. Nécessite monitoring J+3 (expiration 2026-06-05)
5. **Sectoriel inchangé** — XLC bottom 3, malus sectoriel maintenu

**Alertes actives :**
- **ATR_SPIKE (haut)** — ATR relatif 11,5% du cours, volatilité extrême persistante
- **Profil non rentable** — multiples négatifs, aucune visibilité sur la rentabilité
- **Cours au-dessus du consensus** — $105,65 vs $94,54 = +11,7%. Risque de downgrades maintenu
- **Test du support $100** — low intraday $101,21, niveau psychologique en vue
- **🔴 ANOMALIE DATA QUALITY OPTIONS** — Max Pain $40 aberrant, Put/Call et Call OI null. Ne pas utiliser ces données pour le scoring options
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (momentum score 0,0). Signal macro ROTATION_TO_CYCLICAL du 2026-06-02

**Verdict opérationnel :** ne pas entrer long à ces niveaux. La stabilité technique est rassurante à court terme, mais le gap −6,84% vs close officiel et l'anomalie options soulignent la fragilité du setup. Le ratio R/R mécanique de 1,5:1 reste masqué par une probabilité d'atteinte du TP faible sans catalyseur et un risque de continuation baissière vers $95–$100 ou la MM50. **Attendre la résolution de l'anomalie options avant toute réévaluation du pinning gamma J+3.**

**Prochaines étapes :**
- Surveiller la résolution de l'anomalie options (Max Pain devrait revenir vers $120, monitoring quotidien)
- Tenue du niveau $105 (support technique) et $100 (psychologique)
- Monitoring de l'expiration options 2026-06-05 — comportement autour du max pain historique $120 (si données corrigées)
- Attendre un retour vers $95–$100 (zone consensus) ou $87–$88 (MM50) pour réévaluer
- Revoir le scoring si earnings preview à générer (dans ~69j)
- **Ne pas entrer long à ces niveaux** — risque/rendement asymétriquement défavorable

---

*Généré par le système Argus-IA — Snapshot 2026-06-02 10:00 UTC (cours $105,65 stable vs 21h 01/06, gap −6,84% vs close officiel, RSI 61,89, volume 1,00× normalisé, score global 44,8 SURVEILLER, anomalie data quality options détectée)*

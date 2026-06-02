# ASTS — Mise à Jour Snapshot 13h UTC (2026-06-02)

> **Stabilité totale, anomalie options résolue** : cours **$105,65** à 13h UTC (inchangé vs snapshot 10h), RSI stable **61,89**, volume **normalisé 1,00×**. L'anomalie data quality options détectée au snapshot 10h (Max Pain $40 aberrant, Put/Call et Call OI null) est **résolue** : Max Pain rétabli à **$120,00**, Put/Call **1,09**, Call OI **47,9%**. Spot **−12,0% sous Max Pain** : pinning gamma haussier réactivé vers $120 d'ici expiration 05/06. Score global ajusté **44,8/100 (SURVEILLER)**. Thèse **SURVEILLER confirmée**.

---

## Résumé des Changements depuis le Snapshot 10h UTC

| Indicateur | Snapshot 10h UTC 2026-06-02 | Snapshot 13h UTC 2026-06-02 | Delta |
|-----------|-----------------------------|-----------------------------|-------|
| **Cours** | **$105,65** | **$105,65** | **—** 🟢 |
| RSI 14j | **61,89** | **61,89** | **—** |
| ATR 14j | **$12,18** | **$12,18** | **—** |
| MM50 | **$87,11** | **$87,11** | **—** |
| Volume rel. | **1,00×** | **1,00×** | **—** |
| Market Cap | **$41,01B** | **$41,01B** | **—** |
| Forward P/E | **−355,57** | **−355,57** | **—** |
| EV/Revenue (Yahoo) | **378,00×** | **378,00×** | **—** |
| P/B (Yahoo) | **15,16×** | **15,16×** | **—** |
| 52W high | **$133,86** | **$133,86** | **—** |
| Consensus PT | **$94,54** | **$94,54** | **—** |
| Downside consensus | **−10,5%** | **−10,5%** | **—** |
| Short Interest | **17,60%** | **17,60%** | **—** |
| Score Global ajusté | **44,8** | **44,8** | **—** |
| Max Pain | **$40,00** (anomalie) | **$120,00** | **+$80,00** 🟢 [RÉSOLU] |
| Put/Call Ratio | **null** (manquant) | **1,09** | **Rétabli** 🟢 |
| Call OI % | **null** (manquant) | **47,9%** | **Rétabli** 🟢 |

**Verdict :** stabilité absolue du cours à $105,65 entre les snapshots 10h et 13h UTC. Tous les indicateurs techniques (RSI, ATR, MM50, volume) et fondamentaux (market cap, multiples, consensus) sont **strictement inchangés**. La seule mutation significative est la **correction de l'anomalie data quality options** : Max Pain revient de $40 (aberrant) à $120,00 (cohérent avec l'historique), Put/Call Ratio passe de null à 1,09, et Call OI % de null à 47,9%. Cette résolution réactive la lecture options : le spot $105,65 est **−12,0% sous le Max Pain $120**, configuration qui exerce un **pinning gamma haussier** vers $120 à l'approche de l'expiration du 2026-06-05 (J+3).

---

## Mise à Jour Technique

- **Cours :** $105,65 — **inchangé** vs snapshot 10h UTC ; **−6,84%** vs previous close officiel $113,41
- **Range intraday :** $101,21–$111,28 (mêmes niveaux, pas de nouveau high/low)
- **RSI 14j :** **61,89** — stable, zone neutre/haussière
- **ATR 14j :** $12,18 (ATR relatif **11,5%** du cours) — **[TRIGGER HAUT]** volatilité extrême persistante
- **MM50 :** $87,11 — cours **+21,3%** au-dessus, support éloigné
- **MM200 :** N/A
- **Volume 13h :** 27,11M vs moy. 20j 27,02M (**1,00×**) — volume parfaitement normalisé, aucun signal de distribution ni d'accumulation
- **52W high :** $133,86 — repli total depuis le sommet : **−21,1%**
- **52W low :** $23,80
- **Supports clés :** $100,00 (psychologique, testé à $101,21) ; MM50 $87,11
- **Résistances clés :** previous close $113,41 ; high intraday $111,28 ; Max Pain options $120,00
- **Timing verdict :** **Neutre** (RSI stable, volume normalisé, volatilité extrême persistante, mais pinning gamma haussier réactivé J+3)
- **Score Momentum :** 5,5/10 — **inchangé**. La stabilité du cours et du volume maintient le momentum haussier de moyen terme intact mais surveillé

---

## Mise à Jour Fondamentale

Aucun nouveau résultat comptable ni guidance. La mutation reste **exclusivement technique/data quality**.

- **Market Cap :** $41,01B (stable)
- **Forward P/E :** −355,57 (profil non rentable, stable)
- **EV/EBITDA :** −101,47 (stable)
- **EV/Revenue :** 378,00× (Yahoo) / 355,70× (FMP annual) — stable, domaine spéculatif extrême
- **P/B :** 15,16× (Yahoo) / 10,10× (FMP annual) — stable
- **Beta :** 2,598 — sensibilité très supérieure au marché
- **Short Interest :** 17,60% (stable, pas de short squeeze setup)
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes, 5 couverts le mois dernier, 7 le trimestre dernier) — inchangé. Downside consensus **−10,5%** vs cours $105,65
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK** (pas d'exclusion, `accounting_risk_latest.json` absent)

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-02 émet un signal macro **ROTATION_TO_CYCLICAL**. XLK (Technology) #1 du ranking (momentum score 10,0). XLC (Communication Services) est dans le **bottom 3** (momentum score 0,0). Faiblesse sectorielle persistante — le mouvement d'ASTS reste **découplé** de son secteur. Malus sectoriel maintenu.

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence stable à **−10,5%**
- **Options :** 🟢 **ANOMALIE RÉSOLUE — données rétablies**
  - Max Pain **$120,00** (vs $40 aberrant au snapshot 10h) — **valeur cohérente avec l'historique**
  - Put/Call Ratio **1,09** (vs null) — skew put modéré, sentiment légèrement baissier
  - Call OI **47,9%** (vs null) — domination call modérée, en retrait vs 52,2% du snapshot 21h 2026-06-01
  - Nearest expiry : **2026-06-05 (J+3)**
  - **Lecture :** avec le cours $105,65 bien sous le max pain $120, le pinning gamma à l'expiration J+3 exerce une **pression haussière** vers $120. Le put/call 1,09 est légèrement plus baissier que le 0,92 précédent, mais le delta reste faible. Le passage du Call OI de 52,2% à 47,9% indique un **léger repositionnement baissier** des options, attenuant partiellement le signal haussier du pinning gamma
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTS (`events_latest.json` vide)
- **Géopolitique :** ASTS non flaggé (`geo_risk_latest.json` absent pour ASTS)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-02

**Catalyseurs à venir :**
- Prochain earnings : **2026-08-10** (J+69) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Expiration options 2026-06-05 (J+3)** — données rétablies, Max Pain $120 au-dessus du spot : pinning gamma haussier réactivé

---

## Scoring Global — Snapshot 13h UTC (2026-06-02)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4,0/10 | 35% | Aucun catalyseur imminent, earnings dans 69j, pas de news structurante — stabilité totale. Pinning gamma J+3 léger bonus technique |
| Valorisation | 3,0/10 | 40% | Multiples spéculatifs extrêmes (EV/Revenue 378×, P/B 15,16×), consensus $94,54 = −10,5% sous le cours |
| Momentum | 5,5/10 | 25% | Cours stable $105,65, RSI 61,89 stable, cours +21,3% au-dessus MM50 — momentum haussier de moyen terme intact mais surveillé |
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

**Score Global Composite :** 40,0/100 (ajusté **44,8/100**) — **inchangé** vs snapshot 10h UTC. Confortablement dans la zone SURVEILLER (35–49) → **SURVEILLER**.

---

## Niveaux et Ratio R/R

- **Cours actuel :** $105,65
- **Stop-loss suggéré :** $81,29 (cours − 2×ATR = $105,65 − $24,36) — **inchangé**
- **Take-profit suggéré :** $142,19 (cours + 3×ATR = $105,65 + $36,54) — **inchangé**
- **Ratio R/R :** 1,5:1 — **inchangé**

**Révision :** niveaux maintenus. La stabilité technique totale entre les snapshots 10h et 13h ne modifie pas la structure de risque. Le SL à $81,29 correspond approximativement à la MM50 ($87,11) moins une marge de volatilité. En cas de rupture sous $100 puis $87, la tendance haussière de moyen terme serait invalidée. Le TP $142,19 reste 6,2% au-dessus du 52W high ($133,86). Probabilité d'atteinte faible sans catalyseur majeur.

**Nouveau facteur J+3 :** le Max Pain rétabli à $120 crée un **aimant haussier technique** pour les 3 prochains jours. Si le cours consolide autour de $105–$108, le pinning gamma pourrait pousser vers $120 à l'expiration du 2026-06-05. Cela représente un **upside technique de +13,6%** sur 3 jours, mais dépend entièrement de la tenue du support $105 et de l'absence de choc macro/nouvelles négatives.

---

## Conclusion

**Thèse confirmée : SURVEILLER — stabilité totale vs snapshot 10h UTC 2026-06-02 à $105,65, RSI 61,89, volume normalisé 1,00×, divergence consensus −10,5% stable. Anomalie options RÉSOLUE (Max Pain $120,00 rétabli, Put/Call 1,09, Call OI 47,9%). Pinning gamma haussier réactivé J+3 vers $120 (+13,6%).**

Le snapshot 13h UTC enregistre une **stabilité technique et fondamentale complète** vs le snapshot 10h UTC. Cours, RSI, ATR, MM50, volume, consensus, market cap, multiples fondamentaux sont **tous strictement inchangés**. La seule mutation significative est la **résolution de l'anomalie data quality options** : Max Pain revient à $120 (cohérent historique), Put/Call et Call OI sont rétablis.

**Changements structurants :**
1. **Stabilité technique totale** — cours $105,65, RSI 61,89, ATR $12,18, MM50 $87,11, volume 1,00×. Aucun nouveau signal technique
2. **🟢 Anomalie options RÉSOLUE** — Max Pain $120,00 (vs aberration $40 au 10h), Put/Call 1,09, Call OI 47,9%. Données utilisables à nouveau
3. **Pinning gamma haussier réactivé J+3** — spot $105,65 sous Max Pain $120 (−12,0%). Upside technique +13,6% si le pinning s'exerce
4. **Léger repositionnement baissier options** — Call OI 47,9% (vs 52,2% au 21h 01/06), Put/Call 1,09 (vs 0,92). Atténuation modérée du signal haussier
5. **Sectoriel inchangé** — XLC bottom 3, malus sectoriel maintenu

**Alertes actives :**
- **ATR_SPIKE (haut)** — ATR relatif 11,5% du cours, volatilité extrême persistante
- **Profil non rentable** — multiples négatifs, aucune visibilité sur la rentabilité
- **Cours au-dessus du consensus** — $105,65 vs $94,54 = +11,7%. Risque de downgrades maintenu
- **Test du support $100** — low intraday $101,21, niveau psychologique en vue
- **Pinning gamma J+3** — Max Pain $120 au-dessus du spot. Risque de whipsaw élevé à l'expiration 2026-06-05
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (momentum score 0,0). Signal macro ROTATION_TO_CYCLICAL du 2026-06-02

**Verdict opérationnel :** ne pas entrer long à ces niveaux. La stabilité technique est rassurante à court terme, mais le profil fondamental reste spéculatif extrême. Le pinning gamma J+3 constitue un **facteur technique haussier de court terme** (+13,6% vers $120) mais est contrebalancé par le repositionnement baissier des options (Call OI en baisse, Put/Call en hausse) et l'absence totale de catalyseur fondamental. Le ratio R/R mécanique de 1,5:1 reste masqué par une probabilité d'atteinte du TP faible sans catalyseur et un risque de continuation baissière vers $95–$100 ou la MM50. **Attendre la résolution de l'expiration J+3 avant toute réévaluation.**

**Prochaines étapes :**
- Surveiller le comportement autour du Max Pain $120 à l'expiration 2026-06-05 (J+3)
- Tenue du niveau $105 (support technique) et $100 (psychologique)
- Monitoring du Call OI et Put/Call Ratio en approche de l'expiration
- Attendre un retour vers $95–$100 (zone consensus) ou $87–$88 (MM50) pour réévaluer
- Revoir le scoring si earnings preview à générer (dans ~69j)
- **Ne pas entrer long à ces niveaux** — risque/rendement asymétriquement défavorable

---

*Généré par le système Argus-IA — Snapshot 2026-06-02 13:00 UTC (cours $105,65 stable vs 10h, RSI 61,89, volume 1,00× normalisé, score global 44,8 SURVEILLER, anomalie options RÉSOLUE Max Pain $120,00, Put/Call 1,09, Call OI 47,9%)*

# ASTSPACE — Mise à Jour Snapshot 10h UTC (2026-06-02)

> **Stabilité totale vs 21h UTC 2026-06-01** : aucun nouveau cours disponible pour ASTSPACE (erreur Yahoo `No price history` >30 snapshots). Proxy ASTS stable à **$105,65** (close identique), RSI **61,89** inchangé, volume **1,00×** moyenne 20j. **Anomalie data quality options réapparue** (Max Pain $40,00 vs historique $120,00 — Put/Call et Call OI corrompus). Score agent ASTSPACE **55,2/100 (ATTENDRE)** — placeholder non fondé. Score agent proxy ASTS **44,8/100 (SURVEILLER)** — stable. Thèse **INVALIDÉE PAR L'ABSENCE DE DONNÉES confirmée**.

---

## Résumé des Changements depuis l'Analyse Précédente

| Indicateur | Snapshot 21h UTC 2026-06-01 | Snapshot 10h UTC 2026-06-02 | Delta |
|-----------|-----------------------------|-----------------------------|-------|
| **Cours ASTSPACE** | `[No price history]` | `[No price history]` | **—** 🔴 |
| **Cours ASTS (proxy)** | **$105,65** | **$105,65** | **—** |
| RSI 14j ASTS | **61,89** | **61,89** | **—** |
| ATR 14j ASTS | **$12,18** | **$12,18** | **—** |
| MM50 ASTS | **$87,11** | **$87,11** | **—** |
| Volume rel. ASTS | **1,00×** | **1,00×** | **—** |
| Market Cap ASTS | **$41,01B** | **$41,01B** | **—** |
| Forward P/E ASTS | **−355,57** | **−355,57** | **—** |
| EV/Revenue ASTS (Yahoo) | **405,30×** | **378,00×** | **−27,30×** 🟢 |
| P/B ASTS (Yahoo) | **15,16×** | **15,16×** | **—** |
| Consensus PT ASTS | **$94,54** | **$94,54** | **—** |
| Downside consensus ASTS | **−10,5%** | **−10,5%** | **—** |
| Short Interest ASTS | **17,60%** | **17,60%** | **—** |
| Max Pain ASTS | **$120,00** | **$40,00** | **−$80,00** 🔴 |
| Put/Call Ratio ASTS | **0,92** | **null** | **Corrompu** 🔴 |
| Call OI % ASTS | **52,2%** | **null** | **Corrompu** 🔴 |
| Score ASTSPACE (agent) | **55,2** | **55,2** | **—** |
| Score ASTS ajusté (agent) | **44,8** | **44,8** | **—** |
| Earnings placeholder ASTSPACE | 2026-06-01 (J=0) | **2026-06-02 (J=0)** | **Glissement +1j** 🔴 |

**Verdict :** aucune mutation de marché entre le close du 01/06 et l'ouverture du 02/06 (snapshot pré-ouverture US). Le cours proxy ASTS reste à **$105,65** avec des indicateurs techniques strictement identiques. La seule variation détectée est la **correction mécanique de l'EV/Revenue** (378,00× vs 405,30× dans le JSON précédent — probablement ajustement de données comptables source Yahoo) et la **réapparition de l'anomalie options** (Max Pain $40,00, Put/Call et Call OI null), déjà observée le 2026-05-20 et résolue le 2026-05-26.

---

## Mise à Jour Technique (Proxy ASTS)

- **Cours :** $105,65 — **stable** vs close 2026-06-01 $105,65. Variation vs previous close $113,41 : **−6,84%** (stable)
- **Range intraday (01/06) :** $101,21–$111,28 — données inchangées, marché US non ouvert au moment du snapshot
- **RSI 14j :** **61,89** — inchangé, zone neutre/haussière. Sortie complète de la zone de surachat maintenue
- **ATR 14j :** $12,18 (ATR relatif **11,5%** du cours) — **[TRIGGER HAUT]** volatilité intraday extrême persistante
- **MM50 :** $87,11 — cours **+21,3%** au-dessus, support éloigné
- **MM200 :** N/A
- **Volume :** 27,11M vs moy. 20j 27,02M (**1,00×**) — volume normalisé stable
- **52W high :** $133,86 — repli total depuis le sommet : **−21,1%** (stable)
- **52W low :** $23,80 (source data/latest.json)
- **Supports clés :** $100,00 (psychologique, testé à $101,21) ; MM50 $87,11
- **Résistances clés :** previous close $113,41 ; high intraday $111,28 ; consensus $94,54
- **Timing verdict :** **Neutre** — aucun changement technique depuis le snapshot 21h UTC. Configuration inchangée
- **Score Momentum :** 5,5/10 — **inchangé** (rebond technique stabilisé, volume normalisé, RSI 61,89)

**Anomalie options détectée :**
- Max Pain **$40,00** (vs historique cohérent $120,00) — aberration probable de la source Yahoo
- Put/Call Ratio : **null** (données corrompues)
- Call OI % : **null** (données corrompues)
- Nearest expiry : **2026-06-05 (J+3)**
- **Lecture :** en raison de l'anomalie data quality, le bloc options est **non interprétable** aujourd'hui. Le Max Pain historique cohérent ($120,00) reste la référence implicite, mais avec une fiabilité dégradée. L'expiration J+3 constitue un risque de volatilité gamma non quantifiable

---

## Mise à Jour Fondamentale (Proxy ASTS)

Aucun nouveau résultat comptable ni guidance. La mutation reste **exclusivement technique**.

- **Market Cap :** $41,01B (stable)
- **Forward P/E :** −355,57 (profil non rentable, stable)
- **EV/EBITDA :** −101,47 (stable)
- **EV/Revenue :** 378,00× — **correction mécanique** vs 405,30× noté dans l'analyse précédente. Reste un multiple spéculatif extrême
- **P/B :** 15,16× (Yahoo) — stable
- **Beta :** 2,598 — sensibilité très supérieure au marché, stable
- **Short Interest :** 17,60% (stable, pas de short squeeze setup)
- **Consensus analystes :** Price target moyen **$94,54** (12 analystes, 5 couverts le mois dernier, 7 le trimestre dernier) — inchangé. Downside consensus **−10,5%** vs cours $105,65 — stable
- **Filtre Qualité :** ⚠️ Partielle — profil non rentable, marges négatives. Quality Gate : **OK** (pas d'exclusion)

**Risque sectoriel :** ASTS est classé dans Communication Equipment (Technology). L'Agent Sector Rotation du 2026-06-02 émet un signal macro **ROTATION_TO_CYCLICAL** stable. XLK (Technology) #1 du ranking (momentum score 10,0). XLC (Communication Services) est dans le **bottom 3** (momentum score 0,0). Faiblesse sectorielle persistante — le mouvement d'ASTS reste **découplé** de son secteur. Malus sectoriel maintenu.

---

## Mise à Jour Sentiment / Options / News

- **Consensus analystes :** inchangé à $94,54. Divergence consensus stable à **−10,5%**
- **Options :** données **corrompues** (Max Pain $40,00 aberrant, Put/Call null, Call OI null). Anomalie déjà observée le 2026-05-20 et résolue le 2026-05-26. Réapparition aujourd'hui = dégradation data quality. Nearest expiry : **2026-06-05 (J+3)**
  - **Verdict options :** bloc non interprétable. Le Max Pain historique cohérent ($120) reste la référence implicite, mais la fiabilité est compromise
- **Social Sentiment :** 0 mention Reddit ; Score 0,0/10 (no data) ; Pump detected : False — stable
- **Event-Driven :** aucun événement corporate détecté pour ASTSPACE (events_2026-06-02.json vide)
- **Géopolitique :** ASTSPACE non flaggé (geo_risk absent)
- **FX Exposure :** Exposition 25%, direction export, devise USD. FX Impact Score 0,0/10 — impact neutre, divergence "aligned"
- **News :** aucune news spécifique ASTS dans le flux du 2026-06-02 (news_2026-06-02.json vide pour ASTS)

**Catalyseurs à venir :**
- Prochain earnings ASTS : **2026-08-10** (J+69) — Est. EPS $−0,29 à $−0,17, Revenus $0,0B
- Aucun preview auto-généré (earnings > 3j)
- **Earnings placeholder ASTSPACE (FMP)** : signalé le **2026-06-02** (`days_until: 0`) — glissement persistant depuis le 29/05. Non résolu
- **Expiration options 2026-06-05 (J+3)** — données corrompues, risque gamma non quantifiable

---

## Scoring Global — Snapshot 10h UTC (2026-06-02)

### ASTSPACE (données officielles — placeholder)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 6,5/10 (placeholder) | 35% | [NON FONDÉ] |
| Valorisation | 5,0/10 (placeholder) | 40% | [NON FONDÉ] |
| Momentum | 5,0/10 (placeholder) | 25% | [NON FONDÉ] |
| **Score Opportunité** | **5,5/10** | — | Placeholder — **non utilisable** |
| **Score Global** | **55,2/100** | — | Placeholder — **non utilisable** |

**Action recommandée par l'agent :** ATTENDRE (par défaut système)

> **Règle absolue :** sans données de cours, le scoring est un placeholder algorithmique. Il ne reflète aucune réalité de marché.

### ASTS (proxy, à titre indicatif uniquement)

| Axe | Score | Pondération | Commentaire |
|-----|-------|-------------|-------------|
| Catalyseur | 4,0/10 | 35% | Aucun catalyseur imminent, earnings dans 69j, pas de news structurante |
| Valorisation | 3,0/10 | 40% | EV/Revenue 378×, P/B 15,16×, consensus $94,54 = −10,5% sous le cours. Profil non rentable |
| Momentum | 5,5/10 | 25% | Cours stable $105,65, RSI 61,89, volume 1,00× — momentum neutre post-correction |
| **Score Opportunité** | **4,0/10** | — | Non qualifié pour position (score < 6) |

**Malus / Bonus appliqués (Agent Recommandation) :**
- Malus ATR_SPIKE : volatilité intraday extrême persistante (11,5% du cours)
- Malus sectoriel (XLC bottom 3) : −0,5 pt — faiblesse sectorielle persistante
- Malus consensus sous cours : price target $94,54 vs cours $105,65 = upside négatif −10,5%
- Malus options data quality : Max Pain aberrant $40,00, Put/Call et Call OI null — fiabilité technique dégradée
- Bonus RSI normalisé : sortie de surachat maintenue, risque de correction technique réduit
- Bonus volume normalisé : 1,00× moyenne 20j = liquidité stable
- Aucun malus comptable (Quality Gate OK, accounting_risk absent)
- Aucun malus géopolitique
- Aucun malus FX
- Aucun bonus event-driven

**Score Global Composite ASTS :** 39,8/100 (ajusté **44,8/100**) — **stable** selon Agent Recommandation. Confortablement dans la zone SURVEILLER (35–49) → **SURVEILLER**.

---

## Niveaux et Ratio R/R (Proxy ASTS)

- **Cours actuel :** $105,65
- **Stop-loss suggéré :** $81,29 (cours − 2×ATR = $105,65 − $24,36)
- **Take-profit suggéré :** $142,19 (cours + 3×ATR = $105,65 + $36,54)
- **Ratio R/R :** 1,5:1

**Révision :** niveaux inchangés — aucune mutation technique depuis le snapshot 21h UTC.
- Le SL à $81,29 correspond approximativement à la MM50 ($87,11) moins une marge de volatilité. En cas de rupture sous $100 puis $87, la tendance haussière de moyen terme serait invalidée
- Le TP $142,19 est **6,2% au-dessus du 52W high ($133,86)**. Probabilité d'atteinte faible sans catalyseur majeur post-correction
- Le consensus analystes ($94,54) est **$11,11 sous le cours actuel**, zone vers laquelle un retest est plausible en cas de consolidation
- **Zone d'intérêt potentielle :** $95–$100 (alignement avec consensus et test du support psychologique)
- **Risque options J+3 :** données corrompues (Max Pain aberrant) — exposition gamma non quantifiable

---

## Conclusion

**Thèse confirmée : INVALIDÉE PAR L'ABSENCE DE DONNÉES — STABILITÉ TOTALE DU PROXY ASTS À $105,65, ANOMALIE OPTIONS RÉAPPARUE**

Le snapshot 10h UTC du 2026-06-02 enregistre une **stabilité totale** des paramètres techniques et fondamentaux du proxy ASTS par rapport au snapshot 21h UTC du 2026-06-01. Le cours reste à **$105,65**, le RSI à **61,89**, le volume normalisé à **1,00×**.

**Changements structurants :**
1. **Cours stable** — $105,65 inchangé vs close 21h UTC 2026-06-01
2. **Volume stable** — 1,00× moyenne 20j (27,11M vs 27,02M)
3. **Divergence consensus stable** — $105,65 vs PT $94,54 = −10,5%
4. **Valorisation stable** — P/B 15,16×, Forward P/E −355,57. EV/Revenue corrigé à 378× vs 405× précédemment (ajustement source)
5. **Anomalie options réapparue** — Max Pain $40,00 (aberrant vs $120 historique), Put/Call et Call OI null. Même signature que le 2026-05-20
6. **Sectoriel inchangé** — XLC bottom 3, malus sectoriel maintenu
7. **Placeholder earnings ASTSPACE glissant** — FMP signale encore J=0 (2026-06-02), glissement persistant depuis le 29/05

**Alertes actives :**
- **ATR_SPIKE (haut)** — ATR relatif 11,5% du cours, volatilité extrême persistante
- **Profil non rentable** — multiples négatifs, aucune visibilité sur la rentabilité
- **Cours au-dessus du consensus** — $105,65 vs $94,54 = +11,7%
- **Test du support $100** — low intraday $101,21, niveau psychologique en vue
- **Anomalie data quality options** — Max Pain aberrant $40,00, Put/Call et Call OI null depuis le snapshot 2026-06-02
- **Secteur Communication Services (XLC)** — bottom 3 du ranking sectoriel (momentum score 0,0). Signal macro ROTATION_TO_CYCLICAL stable
- **Placeholder earnings glissant** — ASTSPACE FMP J=0 depuis >4j sans résolution

**Verdict opérationnel :** ASTSPACE n'est toujours pas évaluable en l'état. L'anomalie structurelle (doublon probable d'ASTS) persiste. Le proxy ASTS affiche une stabilité technique totale mais avec une **dégradation de la qualité des données options** qui rend le monitoring gamma impraticable pour l'expiration J+3. Le ratio R/R mécanique de 1,5:1 reste masqué par une probabilité d'atteinte du TP faible sans catalyseur et un risque de continuation baissière vers $95–$100 ou la MM50. **Ne pas entrer long à ces niveaux.**

**Prochaines étapes :**
- Résoudre l'anomalie structurelle ASTSPACE (supprimer de watchlist ou marquer `excluded`)
- Surveiller la résolution de l'anomalie options Max Pain (retour à $120 attendu)
- Monitoring de l'expiration options 2026-06-05 — comportement non prévisible en raison des données corrompues
- Attendre un retour vers $95–$100 (zone consensus) ou $87–$88 (MM50) pour réévaluer
- Revoir le scoring si earnings preview à générer (dans ~69j pour ASTS)
- **Ne pas engager de capital sur ASTSPACE** tant que les données de cours ne sont pas disponibles

---

*Généré par le système Argus-IA — Snapshot 2026-06-02 10:00 UTC (ASTSPACE : données indisponibles, proxy ASTS stable $105,65, anomalie options détectée, score global 55,2 placeholder ATTENDRE / proxy 44,8 SURVEILLER)*

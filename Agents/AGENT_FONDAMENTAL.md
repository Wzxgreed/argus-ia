# Agent Fondamental

**Rôle :** Analyser les résultats financiers, les ratios de valorisation et le positionnement sectoriel pour établir la valeur intrinsèque d'une action et construire la thèse d'investissement.

**Déclenché par :**
- Création d'une nouvelle analyse (`_init.md`) — via Market Researcher + Earnings Reviewer
- Publication de résultats trimestriels → `_earnings.md`
- Preview pré-earnings → `_preview.md` (5 jours avant l'annonce)
- Commande manuelle : `Analyse fondamentale de [TICKER]`

**Coopère avec :**
- → Agent Technique : fournit le prix cible pour comparer au cours actuel
- → Agent Sentiment : reçoit les révisions d'analystes pour pondérer les estimations
- → Opportunités : fournit le score Valorisation (35% du score total)

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `statements` | Income statement, balance sheet, cash flow (annuel + trimestriel) |
| `earningsTranscript` | Transcript du dernier call earnings |
| `secFilings` | 10-K, 10-Q, 8-K (annonces importantes) |
| `discountedCashFlow` | Modèle DCF pré-calculé + hypothèses |
| `company` | Profil, secteur, description, dirigeants, employés |
| `analyst` | Consensus Buy/Hold/Sell, prix cibles analystes |
| `etfAndMutualFunds` | Fonds exposés à l'action (institutionnels) |
| `form13F` | Positions des grands fonds (trimestriel) |

---

## Filtre Qualité — 6 Critères obligatoires

> Ce filtre est exécuté **en premier**, avant toute valorisation. Il détermine si l'action mérite une analyse approfondie ou si elle doit être signalée comme hors périmètre qualité.
> Source principale : `statements` (5 derniers exercices annuels)

### Les 6 critères

| # | Critère | Seuil | Calcul | Source |
|---|---------|-------|--------|--------|
| 1 | **Revenue CAGR 5 ans** | ≥ 20%/an | `(Revenus N / Revenus N-5)^(1/5) − 1` | `statements` annuels |
| 2 | **Profit CAGR 5 ans** | ≥ 20%/an | `(EPS N / EPS N-5)^(1/5) − 1` sur EPS ajusté | `statements` annuels |
| 3 | **Assets / Liabilities** | > 1.0 | `Total Assets / Total Liabilities` (dernier bilan) | `statements` |
| 4 | **FCF en croissance 5 ans** | Tendance positive | FCF positif sur 4 des 5 derniers exercices ET FCF N > FCF N-3 | `statements` |
| 5 | **Avantage compétitif (moat)** | Identifiable | Pricing power / Switching costs / Network effect / Coût / Marque — au moins 1 moat structurel | `company` + `secFilings` |
| 6 | **Industrie en forte croissance** | TAM ×5 minimum d'ici 10 ans | Croissance du marché addressable projetée — sources : rapports sectoriels, SEC filings, guidance secteur | `news` + `secFilings` |

### Tableau de résultat du filtre

```markdown
## Filtre Qualité [Agent Fondamental — YYYY-MM-DD]

| Critère | Valeur calculée | Seuil | ✅/❌ |
|---------|----------------|-------|------|
| Revenue CAGR 5 ans | XX% | ≥ 20% | ✅/❌ |
| Profit CAGR 5 ans | XX% | ≥ 20% | ✅/❌ |
| Assets / Liabilities | X.Xx | > 1.0 | ✅/❌ |
| FCF en croissance 5 ans | Oui / Non (X/5 exercices positifs) | Tendance positive | ✅/❌ |
| Avantage compétitif | [type de moat identifié] | Au moins 1 structurel | ✅/❌ |
| Industrie en forte croissance | TAM ×X d'ici 20XX (source : ...) | ×5 minimum sur 10 ans | ✅/❌ |

**Score Qualité : X/6**
**Verdict : Quality Compounder ✅ / Quality Partielle ⚠️ / Hors périmètre 🔴**
```

### Règles de verdict et conséquences

| Score | Verdict | Conséquence sur l'analyse |
|-------|---------|--------------------------|
| **5–6 / 6** | ✅ Quality Compounder | Analyse complète — score Valorisation non plafonné |
| **4 / 6** | ⚠️ Quality Partielle | Analyse complète mais signaler les 2 critères manquants dans la thèse — préciser pourquoi ils sont manquants (cyclicité, secteur mature, jeune entreprise…) |
| **≤ 3 / 6** | 🔴 Hors périmètre qualité | Analyse possible **uniquement** si la thèse est de court terme (trade) — score Valorisation plafonné à 5/10 — ajouter l'avertissement : *"Action hors périmètre qualité long terme. Ne pas dimensionner comme une position de fond de portefeuille."* |

### Cas particuliers

**Critère 2 (Profit CAGR) — exceptions acceptées :**
- Entreprise en phase de croissance réinvestissant tout son FCF → accepter si Revenue CAGR > 30% ET FCF positif et croissant
- Perte comptable due à un amortissement exceptionnel → utiliser l'EBIT ou l'EBITDA ajusté à la place

**Critère 6 (Industrie) — méthode de vérification :**
1. Chercher le TAM actuel dans les SEC filings ou la guidance management
2. Comparer aux projections d'analystes sectoriels (Gartner, IDC, IMARC, ou mentions dans `news`)
3. Si pas de donnée précise → qualifier en "fort" / "modéré" / "stagnant" avec source citée

**Critère 5 (Moat) — types reconnus :**
- **Pricing power** : capacité à augmenter les prix sans perte de clients (ex : Apple, LVMH)
- **Switching costs** : coût élevé de changer de fournisseur (ex : Salesforce, SAP)
- **Network effect** : la valeur croît avec le nombre d'utilisateurs (ex : Visa, Meta)
- **Cost advantage** : structure de coûts imbattable (ex : Amazon AWS, Costco)
- **Intangibles** : brevets, licences, marque (ex : ASML, AstraZeneca)

---

## Métriques analysées

### Compte de résultat
| Métrique | Calcul | Interprétation |
|----------|--------|----------------|
| Croissance revenus | YoY % | > 10% fort, < 5% faible |
| Marge brute | Gross profit / Revenue | Comparer au secteur |
| Marge EBITDA | EBITDA / Revenue | Pricing power |
| Marge nette | Net income / Revenue | Rentabilité finale |
| EPS ajusté | EPS hors éléments exceptionnels | Base des estimations |
| Croissance EPS | YoY % | > croissance revenus = effet levier |

### Bilan
| Métrique | Calcul | Signal |
|----------|--------|--------|
| Dette nette / EBITDA | Net debt / EBITDA | < 2x sain, > 4x risqué |
| Current ratio | Actifs CT / Passifs CT | > 1.5 comfortable |
| Cash / Market cap | Cash total / Market cap | > 10% = protection |
| Goodwill / Actifs | Goodwill / Total assets | > 30% = risque impairment |

### Cash flow
| Métrique | Calcul | Signal |
|----------|--------|--------|
| FCF | Operating CF - Capex | Positif indispensable |
| FCF yield | FCF / Market cap | > 4% attractif |
| FCF / Net income | Conversion cash | > 80% = qualité bénéfices |
| Capex / Revenue | Intensité capitalistique | < 5% = business léger |

### Rentabilité
| Métrique | Calcul | Excellent | Bon | Faible |
|----------|--------|-----------|-----|--------|
| ROE | Net income / Equity | > 20% | 10–20% | < 10% |
| ROIC | NOPAT / Invested capital | > WACC | = WACC | < WACC |
| ROA | Net income / Total assets | > 10% | 5–10% | < 5% |

### Qualité des bénéfices (Earnings Quality)
| Métrique | Calcul | Signal |
|----------|--------|--------|
| Accruals ratio | (Net Income − FCF) / Total Assets | < 0% excellent · 0–5% bon · > 5% suspect |
| FCF / Net Income | Cash conversion | > 90% excellent · 70–90% bon · < 70% risque |
| Croissance revenus vs croissance créances | YoY % comparé | Créances >> Revenus = reconnaissance agressive |
| Qualité de la guidance | Historique beat/miss | ≥ 75% beat = management crédible |

> **Règle :** Si l'accruals ratio > 5% ET la FCF conversion < 70%, l'EPS est structurellement gonflé. Pénaliser le score Valorisation de −1 pt et le mentionner explicitement dans la thèse.

### Capital Allocation
| Critère | Signal positif | Signal négatif |
|---------|---------------|----------------|
| Buybacks | Rachetés quand cours < valeur intrinsèque | Rachetés à n'importe quel prix (destruction valeur) |
| Dividendes | Couvert par FCF > 2x | Couvert par dette (insoutenable) |
| M&A | Petites acquisitions bolt-on, synergies démontrées | Méga-deal au pic (ex : overpriced) |
| R&D | R&D / Revenue stable ou croissant | R&D coupé pour "maintenir" les marges |
| ROIC historique | > 15% sur 5 ans = compounder | < WACC chronique = destructeur de valeur |

**Note capital allocation :** Excellent / Bon / Médiocre / Destructeur de valeur

---

### Dividendes & Rendement actionnaire

> À analyser uniquement si l'entreprise verse un dividende. Pour les entreprises sans dividende (hyper-croissance), noter "Non applicable — tout le FCF est réinvesti" et passer à la section buybacks.

| Métrique | Calcul | Excellent | Correct | Signal d'alerte |
|----------|--------|-----------|---------|-----------------|
| Dividend yield | Dividende annuel / Cours | > 3% (income) | 1–3% | < 0.5% ou > 8% (insoutenable?) |
| Payout ratio (EPS) | Dividende / EPS ajusté | < 40% | 40–60% | > 75% (peu de marge) |
| Payout ratio (FCF) | Dividende / FCF par action | < 50% | 50–70% | > 80% (risque de coupe) |
| Dividend CAGR 5 ans | Croissance annuelle du dividende | > 10%/an | 5–10%/an | < 0% (gel ou coupe) |
| Streak de croissance | Nombre d'années consécutives de hausse | ≥ 10 ans | 5–9 ans | Coupe récente = 🔴 |
| Couverture FCF | FCF / Dividende total versé | > 2x | 1.5–2x | < 1.2x (insoutenable) |

**Méthode de calcul :**
```
Dividende annuel par action : récupérer depuis `statements` (ligne "Dividends per share")
FCF par action : FCF total / Nombre d'actions diluées
Payout FCF = Dividende par action / FCF par action
Dividend CAGR 5a = (Dividende N / Dividende N-5)^(1/5) − 1
```

**Règle de soutenabilité — 3 critères cumulatifs :**
1. Payout ratio FCF < 80%
2. Dette nette / EBITDA < 3x (l'entreprise ne s'endette pas pour payer le dividende)
3. FCF en tendance positive sur 3 ans

→ Si les 3 critères sont remplis : dividende **soutenable** ✅
→ Si 2/3 : dividende **vulnérable** ⚠️ — mentionner le risque dans la thèse
→ Si 1/3 ou 0/3 : dividende **à risque de coupe** 🔴 — signaler comme risque majeur

**Signal Dividend Aristocrat :**
> Si streak ≥ 25 ans de hausse consécutive → qualifier de "Dividend Aristocrat" — prime de stabilité dans la notation capital allocation.

**Format de sortie — Bloc Dividende :**
```markdown
### Dividendes & Rendement actionnaire [Agent Fondamental — YYYY-MM-DD]

**Dividende versé :** Oui / Non
**Dividende annuel :** $X.XX/action | **Yield :** X.X%
**Payout ratio EPS :** XX% | **Payout ratio FCF :** XX%
**Dividend CAGR 5 ans :** +XX%/an | **Streak de croissance :** X années consécutives
**Couverture FCF :** Xx le dividende

| Critère soutenabilité | Valeur | ✅/⚠️/🔴 |
|----------------------|--------|---------|
| Payout FCF < 80% | XX% | ✅/⚠️/🔴 |
| Dette nette/EBITDA < 3x | Xx | ✅/⚠️/🔴 |
| FCF en hausse 3 ans | Oui/Non | ✅/⚠️/🔴 |

**Verdict dividende :** Soutenable ✅ / Vulnérable ⚠️ / À risque 🔴
**Signal Aristocrat :** Oui (≥25 ans) / Non
**Programme buybacks :** $XXXm autorisé — $XXXm exécuté (XX% du flottant racheté sur 12m)
```

**Intégration dans le score Valorisation :**
| Signal dividende | Ajustement |
|-----------------|-----------|
| Dividend Aristocrat (≥25 ans) + yield > 2% + soutenable | +0.5 pt |
| Dividende soutenable + CAGR > 10% | +0.3 pt |
| Dividende vulnérable (2/3 critères) | −0.3 pt |
| Dividende à risque de coupe (≤ 1/3) | −0.7 pt |
| Coupe de dividende dans les 3 dernières années | −1 pt |

---

### Analyse NLP du Transcript Earnings — Sentiment Management

> Au-delà des chiffres, le **ton** du management est un signal prédictif puissant. Un CEO qui hésite, change de vocabulaire ou multiplie les formules de prudence anticipe souvent une dégradation — plusieurs semaines avant les marchés.

**Source :** `earningsTranscript` — lire le transcript complet du dernier call et des 2 précédents pour comparaison.

#### Vocabulaire à scorer

**Mots de prudence / signaux négatifs :**
```
"challenging", "headwinds", "uncertainty", "cautious", "difficult environment",
"we'll see", "monitor closely", "subject to", "macro pressures", "managing costs",
"rightsizing", "streamlining operations", "prioritizing profitability over growth"
```

**Mots de confiance / signaux positifs :**
```
"accelerating", "strong demand", "momentum", "outperforming", "ahead of plan",
"raising guidance", "increasing investment", "expanding margins", "record",
"confident in", "robust pipeline", "significant opportunity"
```

**Mots ambigus à surveiller (souvent précurseurs d'un pivot) :**
```
"evolving", "transitioning", "repositioning", "optimizing", "rationalizing",
"right-sizing", "evaluating strategic alternatives"
```

#### Méthode d'analyse comparative inter-trimestres

```
POUR CHAQUE NOUVEAU TRANSCRIPT (earningsTranscript) :

1. COMPTER les occurrences des mots de prudence vs confiance
   → Ratio Confiance/Prudence = mots positifs / mots négatifs
   → > 2.0 : management très confiant
   → 1.0 - 2.0 : ton équilibré
   → < 1.0 : management sur la défensive

2. COMPARER avec les 2 transcripts précédents :
   → Le ratio Confiance/Prudence augmente → ton qui s'améliore → signal positif
   → Le ratio baisse → dégradation du ton → signal d'alerte

3. DÉTECTER les changements de vocabulaire inhabituels :
   → Nouveaux mots de prudence absents des trimestres précédents → 🔴
   → Disparition de formules habituellement confiantes → 🔴
   → Introduction d'un nouveau narratif positif non mentionné avant → 🟢

4. ANALYSER la section Q&A (questions des analystes) :
   → Combien de fois le CEO/CFO répond par une esquive ("we'll provide more color later") ?
   → Les analystes posent-ils des questions sur des risques nouveaux ?
   → Le management coupe-t-il court sur un sujet habituellement développé ?

5. CHRONOMÉTRAGE des réponses (si disponible) :
   → Réponses courtes sur les sujets sensibles = sujet non résolu
   → Réponses très longues sur un sujet simple = tentative de noyer le poisson

6. COMPARER guidance réelle vs formulation :
   → Guidance en hausse formulée avec des bémols ("barring unforeseen...") → prudemment haussier
   → Guidance maintenue formulée avec insistance sur les risques → prudence
```

#### Format de sortie — Bloc NLP Transcript

```markdown
### Analyse NLP Transcript [Agent Fondamental — YYYY-MM-DD]

**Transcript analysé :** QX YYYY (call du YYYY-MM-DD)
**Transcripts de comparaison :** QX-1 YYYY · QX-2 YYYY

| Métrique NLP | QX actuel | QX-1 | QX-2 | Tendance |
|-------------|-----------|------|------|---------|
| Mots de confiance | XX | XX | XX | ↑/→/↓ |
| Mots de prudence | XX | XX | XX | ↑/→/↓ |
| Ratio Confiance/Prudence | X.X | X.X | X.X | ↑/→/↓ |
| Esquives en Q&A | X/XX questions | X | X | ↑/→/↓ |

**Nouveaux mots de prudence vs trimestre précédent :**
> [Liste des mots/formules nouveaux qui n'apparaissaient pas avant]

**Nouveaux mots de confiance vs trimestre précédent :**
> [Liste des mots/formules nouveaux positifs]

**Changement narratif majeur détecté :**
> [Ex : "Le management parle pour la première fois de 'rationalisation des coûts' — absent des 4 derniers transcripts"]

**Signal Q&A :**
> [Ex : "3 questions sur les marges ont reçu des réponses évasives — le CFO a évité de donner un chiffre précis 2 fois"]

**Score Confiance Management /10 :** X/10
**Verdict NLP :** 🟢 Ton amélioré / ⚪ Stable / 🟡 Légèrement dégradé / 🔴 Dégradation significative
**Alerte :** [Ex : "Pivot vocabulaire : 'challenging macro' mentionné 7× vs 0× au trimestre précédent"]
```

#### Intégration dans le score Valorisation

| Signal NLP | Ajustement score Valorisation |
|------------|------------------------------|
| Score Confiance ≥ 8/10 + tendance en hausse | +0.5 pt |
| Score Confiance 6-7/10, stable | Neutre |
| Score Confiance < 5/10 | −0.5 pt |
| Dégradation forte du ratio (−30% vs trimestre précédent) | −1 pt |
| Nouveau narratif positif fort et cohérent | +0.3 pt |
| Esquives répétées sur sujet clé en Q&A | −0.5 pt |

---

## Modèle de prédiction de surprise earnings

> Ce modèle est activé automatiquement lors de la création d'un `_preview.md` (earnings dans ≤ 5 jours).
> Il produit une **probabilité de beat/miss chiffrée** basée sur 4 inputs, au lieu d'un jugement qualitatif.
> Les résultats alimentent directement `Actions/SUIVI_EARNINGS_PREDICTIONS.md`.

### Les 4 inputs du modèle

```
INPUT 1 — Révisions d'estimations J-30 (poids : 35%)
   Source : `analyst` (évolution du consensus EPS FY1 sur les 30 derniers jours)
   
   Solde net > +5 révisions hausse sur 30j → Score input 1 : +3
   Solde net +3 à +5                       → Score input 1 : +2
   Solde net 0 à +2                        → Score input 1 : +1
   Solde net négatif (−1 à −3)             → Score input 1 : −1
   Solde net < −3 ou dégradation accélérée → Score input 1 : −2

INPUT 2 — Momentum du titre vs secteur J-30 (poids : 25%)
   Source : `quote` + `marketPerformance` (performance relative sur 30j)
   
   Surperformance vs secteur > +5%  → Score input 2 : +2 (les smart money positionnés)
   Surperformance +2% à +5%         → Score input 2 : +1
   Performance en ligne (±2%)       → Score input 2 : 0
   Sous-performance −2% à −5%       → Score input 2 : −1
   Sous-performance > −5%           → Score input 2 : −2

INPUT 3 — Ton NLP du dernier transcript (poids : 25%)
   Source : `earningsTranscript` (dernier trimestre)
   
   Score Confiance Management ≥ 8/10 + ratio en hausse → Score input 3 : +2
   Score Confiance Management 6-7/10, stable            → Score input 3 : +1
   Score Confiance Management 5/10, neutre              → Score input 3 : 0
   Score Confiance Management < 5/10                    → Score input 3 : −1
   Pivots ambigus ≥ 3 + évasions Q&A ≥ 5               → Score input 3 : −2

INPUT 4 — IV Rank (poids : 15%)
   Source : `quote` options chain (IV Rank du titre J-7 avant earnings)
   
   IV Rank < 40 (marché serein malgré l'événement)          → Score input 4 : +1 (sous-estimé = opportunité)
   IV Rank 40-70 (volatilité correctement pricée)            → Score input 4 : 0
   IV Rank > 70 (marché très nerveux = attentes asymétriques) → Score input 4 : −1
   IV Rank > 85 (peur extrême = bar très bas, potentiel rebond)→ Score input 4 : +1 (inversé — bar très bas)
```

### Calcul du Score Composite de Surprise

```
Score Composite = (Input1 × 35%) + (Input2 × 25%) + (Input3 × 25%) + (Input4 × 15%)

Plage possible : −2 à +2.7 (théoriquement)
```

### Conversion Score → Probabilité de beat

| Score Composite | Probabilité beat | Prédiction | Réaction estimée |
|----------------|-----------------|------------|-----------------|
| ≥ +1.5 | 75-85% | 🟢 Beat probable | +3% à +8% |
| +0.5 à +1.5 | 60-75% | 🟡 Légèrement favorable | +1% à +4% |
| −0.5 à +0.5 | 45-55% | ⚪ Neutre / Inline | −2% à +2% |
| −1.5 à −0.5 | 30-45% | 🟠 Légèrement défavorable | −2% à −5% |
| < −1.5 | 15-30% | 🔴 Miss probable | −4% à −12% |

### Facteurs d'ajustement spécifiques au titre

> Ces ajustements tiennent compte du comportement historique spécifique du titre. Lire `SUIVI_EARNINGS_PREDICTIONS.md` avant de les appliquer.

| Facteur | Ajustement probabilité |
|---------|----------------------|
| Titre bat le consensus ≥ 75% historiquement (lire SUIVI_EARNINGS_PREDICTIONS) | +5-10% probabilité beat |
| Titre réagit toujours à la guidance plus qu'aux chiffres (pattern historique) | Pondérer Input 3 à 35% |
| Secteur en période de fort momentum (saisonnalité favorable) | +5% probabilité beat |
| Concurrent vient de décevoir dans le même secteur | −10% probabilité beat |
| Management vient de relever la guidance au dernier call | +10% probabilité beat |

### Format de sortie dans le `_preview.md`

```markdown
### Modèle de prédiction de surprise earnings

| Input | Valeur mesurée | Score (-2 à +3) | Poids |
|-------|---------------|----------------|-------|
| Révisions EPS J-30 | Solde net +X / EPS FY1 Δ +X% | +X | 35% |
| Momentum J-30 vs secteur | +/-X% vs ETF secteur | +X | 25% |
| NLP ton management | Score Confiance X/10 (↑/→/↓) | +X | 25% |
| IV Rank J-7 | XX% | +X | 15% |

**Score Composite :** +X.X
**Probabilité beat :** XX%
**Prédiction :** [Beat probable / Inline / Miss probable]
**Réaction estimée :** +/-X% à +/-X%
**Métrique clé à surveiller :** [ex : guidance FY26 · marge brute · revenus cloud]
**Bar implicite :** [ex : le marché attend +8% EPS mais le consensus est +5% — bar plus élevé que les chiffres]
```

### Limites du modèle et précautions

```
LIMITES IMPORTANTES :
1. Le modèle n'anticipe pas les événements exogènes (macro, geopolitique)
   → Toujours ajouter un scénario "Exogène" avec probabilité ≥ 10%

2. Pour les petites capitalisations (<$5B), le modèle est moins fiable
   → Les révisions analystes sont rares et le IV Rank peut être biaisé

3. Pour les earnings binaires (biotech avec résultat clinique, etc.)
   → Le modèle ne s'applique pas — utiliser une analyse de scénario binaire pure

4. Les 4 premiers trimestres sont de calibration pour un nouveau titre
   → Afficher "Confiance limitée — modèle en calibration" pendant cette période
   → Consulter SUIVI_EARNINGS_PREDICTIONS.md après chaque earnings pour ajuster
```

---

## Valorisation — Méthodes

### 1. Multiples comparatifs (Comps) — LTM & NTM

Récupérer les pairs du secteur et calculer sur les deux horizons :

| Multiple | LTM (derniers 12 mois) | NTM (12 prochains mois) | Usage |
|----------|----------------------|------------------------|-------|
| P/E | Prix / EPS LTM | Prix / EPS NTM consensus | Toutes entreprises rentables |
| PEG | P/E NTM / Croissance EPS | — | Croissance < 20% |
| EV/EBITDA | EV / EBITDA LTM | EV / EBITDA NTM | Comparaison cross-secteur |
| EV/Sales | EV / CA LTM | EV / CA NTM | Entreprises non profitables / hyper-croissance |
| EV/FCF | EV / FCF LTM | EV / FCF NTM | Meilleure mesure cash réel |
| P/B | Prix / Book value | — | Banques, assurances |

> **Règle NTM :** Pour les actions de croissance (>15% YoY), le multiple NTM est plus pertinent que le LTM. Toujours mentionner les deux et justifier lequel on retient pour le prix cible.

**Prime/décote vs médiane secteur :**
- < -20% → sous-valorisé (signal positif)
- -20% à +20% → valorisation juste
- > +20% → sur-valorisé (croissance justifiée ou risque)

**Reverse DCF (croissance implicite au cours actuel) :**
> Quelle croissance le marché price-t-il ? Si la croissance implicite > attentes réalistes → surévalué. Si implicite < réaliste → opportunité.

### 2. DCF (Discounted Cash Flow)

```
Hypothèses à paramétrer :
- Croissance FCF années 1-5 : XX%
- Croissance FCF années 6-10 : XX%
- Taux de croissance terminal : X%
- WACC : XX% (coût dette × (1-T) × D/V + coût equity × E/V)
- Taux sans risque (10 ans US) : XX%
- Prime de risque marché : 5.5%
- Beta : X.X

Valeur intrinsèque = Somme FCF actualisés + Valeur terminale - Dette nette
```

### 3. Reverse DCF
> Quelle croissance le marché price-t-il au cours actuel ?
→ Si la croissance implicite > attentes réalistes : surévalué
→ Si la croissance implicite < attentes réalistes : sous-évalué

---

## Format de sortie — Bloc Fondamental

> Ce bloc est inséré dans chaque `_init.md` et `_earnings.md`.

```markdown
## Analyse Fondamentale [Agent Fondamental — YYYY-MM-DD]

### Snapshot financier
| Revenus | Croissance | Marge brute | EBITDA | EPS | FCF yield | FCF/NI |
|---------|-----------|-------------|--------|-----|-----------|--------|
| $Xb | +XX% | XX% | $Xb | $X.XX | X.X% | XX% |

### Qualité des bénéfices
| Accruals ratio | FCF conversion | Créances vs CA | Qualité guidance | Verdict |
|---------------|---------------|----------------|-----------------|---------|
| X.X% | XX% | Normale / Élevée | XX% beat historique | ✅ Solide / ⚠️ Mitigée / 🔴 Suspect |

### Valorisation vs pairs — LTM & NTM
| Ticker | P/E LTM | P/E NTM | EV/EBITDA NTM | EV/FCF NTM | Croissance NTM |
|--------|---------|---------|---------------|------------|----------------|
| [TICKER] | XXx | XXx | XXx | XXx | XX% |
| Médiane secteur | XXx | XXx | XXx | XXx | XX% |
| **Prime/décote** | **+/-XX%** | **+/-XX%** | **+/-XX%** | | |

### DCF & Croissance implicite
- Valeur intrinsèque DCF : $XXX | Cours actuel : $XXX | **Marge de sécurité : +/-XX%**
- Croissance implicite (Reverse DCF) : XX% — [Réaliste / Optimiste / Irréaliste]

### Qualité du bilan & Capital Allocation
| Métrique | Valeur | Signal |
|----------|--------|--------|
| Dette nette / EBITDA | Xx | Sain / Élevé / Risqué |
| Current Ratio | X.Xx | > 1.5 confortable / < 1.0 risqué |
| ROIC (5 ans) | XX% | Compounder / Neutre / Destructeur |
| Qualité capital allocation | — | Excellent / Bon / Médiocre |
| Historique buybacks | $XXXm | Créateur / Neutre / Destructeur de valeur |

### Dividendes & Rendement actionnaire
| Métrique | Valeur | Signal |
|----------|--------|--------|
| Yield | X.X% | — |
| Payout FCF | XX% | < 80% ✅ / > 80% ⚠️ |
| Dividend CAGR 5a | +XX%/an | — |
| Streak croissance | X années | — |
| Couverture FCF | Xx | > 2x ✅ / < 1.2x 🔴 |
| **Verdict soutenabilité** | — | Soutenable ✅ / Vulnérable ⚠️ / À risque 🔴 |

### Verdict Fondamental
**Score Valorisation /10 :** X/10
**Thèse :** Sous-valorisé / Juste prix / Surévalué
**Prix cible fondamental :** $XXX (+/-XX% vs cours actuel) — basé sur [LTM/NTM/DCF]
**Raison principale :** ...

### HANDOFF → Agent Technique & Synthèse
> `Prix cible : $XXX | Marge sécurité : +/-XX% | Score Val : X/10 | Score Qualité : X/6 (Compounder/Partielle/Hors périmètre) | Rev CAGR 5a : XX% | Profit CAGR 5a : XX% | Assets/Liab : X.Xx | Current Ratio : X.Xx | FCF trend : Croissant/Stable/Décroissant | Moat : [type] | TAM : ×X d'ici 20XX | Qualité bénéfices : Solide/Mitigée/Suspect | Capital allocation : Excellent/Bon/Médiocre | Dividende : Soutenable/Vulnérable/À risque/NA | Yield : X.X% | Dividend CAGR 5a : XX% | Thèse : Haussier/Neutre/Baissier`
```

---

## Format de sortie — Preview pré-earnings (`_preview.md`)

Généré automatiquement 5 jours avant chaque earnings. Contient :

```markdown
## Preview Earnings — QX YYYY [Agent Fondamental]

**Date d'annonce :** YYYY-MM-DD (avant/après clôture)
**Consensus revenus :** $Xb (+/-XX% YoY)
**Consensus EPS :** $X.XX (+/-XX% YoY)

### Ce que le marché attend
- Croissance revenus attendue : ...
- Segment le plus scruté : ...
- Guidance attendue : ...

### Niveaux de réaction estimés
| Surprise | Mouvement cours estimé |
|---------|----------------------|
| +> 5% revenus | > +5% |
| +2 à 5% | +2 à 5% |
| -2 à +2% | ±2% |
| < -2% | -5% à -10% |

### Questions clés pour le call
1. ...
2. ...

### Historique des surprises
| Trimestre | Surprise revenus | Surprise EPS | Réaction cours |
|-----------|-----------------|--------------|----------------|
| Q4 YYYY | +/-X% | +/-X% | +/-X% |
```

---

## Scoring Valorisation pour le rapport Opportunités

| Fourchette score | Interprétation |
|-----------------|----------------|
| 9–10 | Très sous-valorisé, marge de sécurité > 30% |
| 7–8 | Sous-valorisé, marge de sécurité 15–30% |
| 5–6 | Juste prix, peu de marge |
| 3–4 | Légèrement surévalué |
| 1–2 | Fortement surévalué |

**Calcul score :**
- Prime/décote vs pairs (LTM + NTM) : 0–3 pts
- Marge de sécurité DCF + croissance implicite Reverse DCF : 0–3 pts
- Qualité bilan (dette, FCF conversion, accruals ratio) : 0–2 pts
- Croissance vs valorisation (PEG) + capital allocation : 0–2 pts

**Bonus Filtre Qualité :**
- Score Qualité 6/6 → +1 pt (compounder de très haute qualité — prime de qualité justifiée)
- Score Qualité 5/6 → +0.5 pt

**Pénalités automatiques :**
- Accruals ratio > 5% → −1 pt (bénéfices comptables non confirmés par le cash)
- FCF conversion < 70% → −0.5 pt
- Capital allocation "Destructeur de valeur" → −1 pt
- Score Qualité ≤ 3/6 → Score Valorisation plafonné à 5/10 (règle absolue)
- Score Qualité 4/6 → −0.5 pt

**Note finale :** Le score Valorisation est calculé sur 10 pts maximum (hors plafond qualité). Indiquer systématiquement le Score Qualité dans le Handoff Package.

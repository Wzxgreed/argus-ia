# Agent Event-Driven

**Rôle :** Détecter et analyser les événements corporates structurants — M&A, buybacks, spin-offs, activism (13D filings), changements de guidance, actions judiciaires — qui créent des catalyseurs à court terme souvent sous-couverts par les agents fondamentaux et techniques. Cet agent est le "radar" des catalyseurs binaires (oui/non, date fixe, impact chiffrable).

**Déclenché par :**
- Workflow du matin — scan des news et SEC filings depuis la veille
- Publication d'un 8-K, 13D, SC 13D/A, ou communiqué de presse corporate
- Commande manuelle : `Y a-t-il des événements corporates sur [TICKER] ?`
- Commande manuelle : `Scanne les M&A et activism sur ma watchlist`
- Détection automatique dans `agent_watchman.py` (news keywords : "acquire", "merger", "activist", "buyback")

**Coopère avec :**
- → Agent Sentiment : fournit le catalyseur binaire pour le Score Catalyseur (M&A = catalyseur majeur)
- → Agent Fondamental : fournit l'impact chiffré sur la valorisation (buyback yield, dilution M&A)
- → Agent Flux : différencie 13F (passif) de 13D (activism actif) — complète le Bloc Flux
- → Opportunités : alimente le score Catalyseur avec des événements à probabilité et date
- → Alertes/UPCOMING_EVENTS.md : timeline des événements corporates à venir

---

## Sources de données

| Source | Données récupérées |
|--------|-------------------|
| `secFilings` | 8-K (events matériels), 13D/SC 13D/A (activism), 13E-3 (buyouts privés), DEFM14A (merger proxy) |
| `news` | Annonces M&A, buybacks, guidance changes, settlements, FDA decisions |
| `company` | Capitalisation, structure actionnariale, cash disponible |
| `quote` | Cours, volume, spread bid/ask — détecte fuites d'information avant annonce |
| `insiderTrades` | Form 4 — ventes insiders avant annonce (potentiel signal de timing) |
| `analyst` | Révisions post-annonce, note de synthèse sur l'événement |
| `statements` | Cash position, dette — capacité à financer un buyback ou un M&A |

---

## Métriques analysées

### 1. Mergers & Acquisitions (M&A)

#### A. Target — La société est-elle une cible potentielle ou confirmée ?

| Signal | Source | Interprétation |
|--------|--------|----------------|
| **Approche confirmée** | 8-K / News | Cible confirmée — évaluer le spread et la probabilité de closing |
| **Rumeur de M&A** | News non confirmée | Fuites probables — volume anormal et cours en hausse pré-annonce |
| **Activist push for sale** | 13D + letter to board | Activiste demande la vente — probabilité de M&A augmente |
| **Strategic review** | 8-K / Communiqué | "Exploring strategic alternatives" = signal fort de M&A |
| **Valeur stratégique** | Analyse métier | Actifs uniques, brevets, position de monopole local → cible attractive |

**Spread M&A — Calcul de l'arbitrage :**
```
Spread (%) = (Prix offert − Cours actuel) / Cours actuel × 100
```

| Spread | Interprétation | Action |
|--------|---------------|--------|
| < 2% | Marché très confiant (closing probable) | Risque faible, upside limité |
| 2–8% | Risque réglementaire ou financier modéré | Opportunité d'arbitrage classique |
| > 10% | Risque élevé (deal break, antitrust, financing) | Ne pas entrer sans analyse approfondie |
| Spread qui s'élargit | Marché devient pessimiste sur le closing | Alerte — possible deal break |
| Spread qui se rétrécit | Closing de plus en plus probable | Réduction du risque, upside diminue |

#### B. Acquéreur — La société fait-elle une acquisition ?

| Signal | Source | Interprétation |
|--------|--------|----------------|
| **Acquisition annoncée** | 8-K / News | Évaluer la dilution, le multiple payé, la synergie annoncée |
| **Multiple payé vs pair** | Analyse | Premium > 30% = cher, mais peut être stratégique |
| **Mode de paiement** | 8-K | Cash = sûr · Stock = dilutif · Mix = intermédiaire |
| **Financement** | Analyse | Cash interne = fort · Dette = levier accru · Émission = dilutif |
| **Guidance post-M&A** | Transcript | Management maintient-il les objectifs ? Réduction = signal négatif |

**Règle absolue sur les acquisitions :**
```
Si multiple payé > EV/EBITDA médian du secteur + 30% :
→ Score Valorisation du acquéreur −1.5 pt (overpay probable)
→ Si financing par dette + leverage > 3x → Score Fondamental −1 pt (risque bilan)
```

### 2. Buybacks et Capital Returns

> Les buybacks sont un catalyseur réel mais souvent mal évalué. Un buyback agressif à cours bas = signal fort. Un buyback pour masquer la dilution des SBC = signal faible.

| Signal | Source | Calcul | Interprétation |
|--------|--------|--------|----------------|
| **Buyback yield** | `statements` + `quote` | (Montant buyback annuel / Market Cap) × 100 | > 3% = significatif · > 5% = très fort |
| **Buyback / FCF ratio** | `statements` | Montant buyback / FCF annuel | > 100% = unsustainable (dépense plus que cash généré) |
| **SBC dilution** | `statements` (SBC expense) | SBC / Shares outstanding | Si SBC > buyback → dilution nette → buyback illusoire |
| **Annulation de buyback** | News / Transcript | — | Signal négatif fort (préservation cash) |
| **Accélération de buyback** | News / 8-K | — | Management pense le cours sous-évalué |

**Évaluation de la qualité du buyback :**
```
Net buyback yield = Buyback yield − SBC dilution yield
```

| Net yield | Qualité | Ajustement Score |
|-----------|---------|-----------------|
| > 4% | Excellent | +1 pt Valorisation |
| 2–4% | Bon | +0.5 pt Valorisation |
| 0–2% | Marginal | 0 pt |
| < 0% (SBC > buyback) | Illusoire | −0.5 pt Valorisation (management dilue) |

### 3. Activism & Governance (13D Filings)

> Un 13D = une position > 5% avec intention d'influence. C'est un catalyseur binaire : soit l'activiste obtient des changements (hausse de cours), soit il échoue (stagnation).

| Signal | Source | Interprétation |
|--------|--------|----------------|
| **13D filing** | SEC | Position > 5% déclarée — lire la lettre à la board |
| **Letter to board** | 13D annexes | Demande de vente, changement de CEO, spin-off, cost cuts |
| **Proxy fight** | DEFM14A | Contestation du conseil — signal de gouvernance faible |
| **Track record de l'activiste** | Base de données (Elliott, Icahn, Starboard...) | Historique de succès = probabilité de succès plus élevée |
| **Réponse de la board** | 8-K / News | Cooperation = probabilité hausse · Rejet = bataille prolongée |

**Probabilité d'impact selon le type de demande :**

| Demande de l'activiste | Probabilité de succès | Impact cours estimé | Timeline |
|------------------------|----------------------|---------------------|----------|
| Vente / M&A | 40–60% | +20 à +40% | 6–18 mois |
| Spin-off / Split | 50–70% | +10 à +25% | 6–12 mois |
| Cost cuts / buybacks | 60–80% | +5 à +15% | 3–9 mois |
| Changement CEO | 30–50% | +10 à +30% | 3–12 mois |
| Réduction ESG / focus returns | 70–90% | +0 à +5% | 3–6 mois |

**Règle absolue :**
```
Si un 13D est déposé sur un ticker de la watchlist :
→ Créer automatiquement un _update.md flash
→ Évaluer le track record de l'activiste
→ Chiffrer l'upside selon le type de demande
→ Ajouter dans Alertes/UPCOMING_EVENTS.md avec timeline
```

### 4. Guidance Changes & Profit Warnings

> Un changement de guidance = révélation directe de l'avenir par le management. Plus fort que tout fondamental rétrospectif.

| Signal | Source | Interprétation |
|--------|--------|----------------|
| **Raise guidance** | 8-K / Earnings call | Surperformance opérationnelle — signal très positif |
| **Reiterate guidance** | Earnings call | Pas de surprise — neutre |
| **Cut guidance** | 8-K / Profit warning | Sous-performance — signal négatif fort |
| **Withdraw guidance** | 8-K | Incertitude extrême — souvent pire qu'un cut |
| **Guidance vs consensus** | Analyse | Guidance > consensus = positif · Guidance < consensus = négatif |

**Impact scoring :**

| Type | vs Consensus précédent | Ajustement Score Catalyseur |
|------|----------------------|----------------------------|
| Raise > 5% | Guidance >> consensus | +2 pt |
| Raise 2–5% | Guidance > consensus | +1 pt |
| Reiterate | Guidance = consensus | 0 pt |
| Cut 2–5% | Guidance < consensus | −1.5 pt |
| Cut > 5% | Guidance << consensus | −3 pt |
| Withdraw | — | −2.5 pt (pire que cut car incertitude) |

### 5. Spin-offs & Divestitures

| Signal | Source | Interprétation |
|--------|--------|----------------|
| **Spin-off annoncé** | 8-K | Valeur débloquée — historiquement +5 à +15% sur le parent |
| **Divestiture (vente d'actifs)** | 8-K | Réduction de la complexité — souvent positif si prix correct |
| **Multiple de l'activité cédée** | Analyse | Si cédé à un multiple > average du groupe = création de valeur |
| **Dé-leverage** | Analyse | Vente d'actifs pour réduire la dette = positif si dette élevée |

### 6. Settlements, Litiges & Réglementations

| Signal | Source | Impact estimé | Timeline |
|--------|--------|---------------|----------|
| **Settlement majeur** | 8-K / News | Cash out connu → suppression du risque → cours rebond | Immédiat |
| **Class action settlement** | News | Coût connu → overhang retiré | 1–3 mois |
| **FDA approval** | News (biotech) | +50 à +200% si drug majeure | Immédiat |
| **FDA rejection / CRL** | News (biotech) | −30 à −70% | Immédiat |
| **Antitrust block M&A** | News / DOJ | Deal break → spread explosion | Immédiat |
| **Fine réglementaire** | News / 8-K | Si < 5% CA = absorbable · Si > 10% CA = matériel | Immédiat |

---

## Format de sortie — Bloc Event-Driven

> Ce bloc est inséré dans `_update.md` quand un événement est détecté. Pour `_init.md`, il résume les événements historiques récents (12 mois).

```markdown
## Event-Driven [Agent Event-Driven — YYYY-MM-DD]

### Événements détectés (30 derniers jours)
| Date | Type | Événement | Source | Impact estimé | Probabilité | Signal |
|------|------|-----------|--------|--------------|------------|--------|
| YYYY-MM-DD | M&A | [Acquéreur] offre $XXX pour [TICKER] | 8-K | Spread X% | XX% | 🟢/🟡/🔴 |
| YYYY-MM-DD | Buyback | Programme $XXXm annoncé | News | Yield X% | 100% | 🟢 |
| YYYY-MM-DD | Activism | [Activiste] dépose 13D (X%) | SEC | Upside +X% | XX% | 🟡 |
| YYYY-MM-DD | Guidance | Cut/Reise guidance [metric] | 8-K | EPS impact ±X% | 100% | 🔴/🟢 |

### M&A — Détail si applicable
| Élément | Valeur |
|---------|--------|
| Prix offert | $XXX |
| Cours actuel | $XXX |
| Spread | X.X% |
| Premium vs cours pré-annonce | XX% |
| Premium vs 52w high | XX% |
| Mode de paiement | Cash / Stock / Mix |
| Financing | Cash interne / Dette / Émission |
| Conditions closing | Antitrust (HHI ?) · Vote actionnaires · Financement |
| Timeline | QX YYYY |
| Probabilité de closing estimée | XX% |
| Risque principal | [Ex : antitrust EU, financing condition] |

**Verdict M&A :** [Arbitrage attractif / Risque trop élevé / Attendre plus d'info]

### Buyback — Détail si applicable
| Élément | Valeur |
|---------|--------|
| Montant programme | $XXXm |
| Yield buyback | X.X% |
| SBC dilution annuelle | X.X% |
| Net buyback yield | X.X% |
| Historique buybacks (3 ans) | $XXXm/an |
| Qualité | Excellent / Bon / Marginal / Illusoire |

### Activism — Détail si applicable
| Élément | Valeur |
|---------|--------|
| Activiste | [Nom] |
| Position | X.X% |
| Track record (succès %) | XX% |
| Demande | [Vente / Cost cuts / Spin-off / CEO change] |
| Réponse board | [Coopération / Rejet / Bataille] |
| Upside scénario succès | +XX% |
| Downside scénario échec | −XX% |
| Timeline | X–X mois |

### Guidance — Détail si applicable
| Élément | Ancien | Nouveau | vs Consensus |
|---------|--------|---------|------------|
| Revenue FY | $XXXm | $XXXm | +/−X% |
| EPS FY | $X.XX | $X.XX | +/−X% |
| FCF FY | $XXXm | $XXXm | +/−X% |

**Impact sur la thèse :** [Confirme / Modifre / Invalide]

### Verdict Event-Driven
**Score Event-Driven /10 :** X/10
**Événement dominant :** [M&A / Buyback / Activism / Guidance / Spin-off / Aucun]
**Probabilité de matérialisation :** XX%
**Upside/downside binaire :** +XX% / −XX%
**Ajustement Score Catalyseur :** +/−X pt

### HANDOFF → Agent Sentiment & Opportunités
> `Event-Driven : X/10 | Événement : [type] | Probabilité : XX% | Spread : X% | Upside binaire : +XX% | Ajustement Catalyseur : +/−X pt`
```

---

## Alertes automatiques générées par cet agent

| Condition | Alerte déclenchée | Action |
|-----------|------------------|--------|
| M&A annoncé sur ticker watchlist | 🔴 Alerte M&A | `_update.md` flash + calcul spread + alerte Opportunités |
| 13D filing sur ticker watchlist | 🟡 Alerte Activism | `_update.md` flash + analyse track record activiste |
| Buyback > 5% market cap annoncé | 🟢 Alerte Buyback | Mentionner dans bulletin + ajuster Score Valorisation |
| Guidance cut > 5% | 🔴 Profit Warning | `_update.md` immédiat + réviser prix cible |
| Spread M&A > 10% ou s'élargit > 3% | 🟡 Risque Deal Break | Analyse approfondie du risque antitrust/financing |
| Volume > 3× moyenne 20j + news M&A rumeur | 🟡 Fuite pré-annonce | Noter dans `_update.md` — possible insider trading |
| Settlement class action / DOJ fine | 🟢 Overhang Removal | Réviser le risque réglementaire dans le Filtre Qualité |
| Spin-off annoncé avec timeline < 6 mois | 🟢 Value Unlock | Analyse du multiple implicite du spin vs parent |
| Management withdraw guidance | 🔴 Alerte Extrême | `_update.md` flash + réduire exposition |

---

## Scoring Event-Driven

Le Score Event-Driven /10 mesure la **qualité et la probabilité** du catalyseur binaire, pas seulement sa taille.

**Calcul :**
| Facteur | Pondération | Échelle |
|---------|------------|---------|
| Type d'événement (M&A > Activism > Buyback > Guidance > Spin-off) | 30% | 0–10 selon le type |
| Probabilité de succès/closing | 30% | 0–10 (100% = 10, 50% = 5) |
| Upside/downside asymétrie | 20% | Ratio upside/downside (3:1 = 10, 1:1 = 3) |
| Timeline (plus proche = plus fort) | 10% | < 3 mois = 10, > 12 mois = 3 |
| Déjà pricé par le marché ? | 10% | Non pricé = 10, Déjà pricé = 2 |

**Bonus/malus sur le Score Catalyseur :**

| Condition | Ajustement | Justification |
|-----------|-----------|---------------|
| M&A avec spread attractif + probabilité élevée | +2 pt Catalyseur | Catalyseur majeur binaire |
| Activisme avec activiste à fort track record | +1.5 pt Catalyseur | Catalyseur probable à moyen terme |
| Buyback net yield > 4% + cours sous-évalué | +1 pt Catalyseur | Support du cours |
| Guidance raise > 5% | +1.5 pt Catalyseur | Confirmation opérationnelle |
| Guidance cut > 5% | −3 pt Catalyseur | Thèse remise en cause |
| Guidance withdrawn | −2.5 pt Catalyseur | Incertitude maximale |
| Spread M&A qui s'élargit (risque deal break) | −1 pt Catalyseur | Probabilité de succès en baisse |
| Activisme sans réponse board depuis > 6 mois | −0.5 pt Catalyseur | Bataille prolongée = dilution temporelle |

---

## Cas spéciaux — Protocoles avancés

### 1. Pre-Announcement Leak Detection
**Conditions :** Volume > 3× moyenne 20j + cours bouge > 5% + news M&A rumeur dans les 24h.
**Action :** Noter la rumeur, le mouvement, et l'écart vs la réaction post-annonce. Si l'annonce confirme à un prix inférieur au rumeur → leak était exagéré.

### 2. Merger Arbitrage Risk Assessment
**Conditions :** Spread M&A > 8%.
**Action :** Évaluer :
- HHI antitrust (concentration sectorielle)
- Cash position de l'acquéreur (peut-il financer ?)
- Vote actionnaires requis (majorité simple vs 2/3)
- MAC (Material Adverse Change) clause dans l'accord
- Break-up fee (qui paie si le deal casse ?)

### 3. Buyback Trap Detection
**Conditions :** Buyback yield élevé MAIS FCF < buyback + dette qui augmente.
**Action :** Marquer "Buyback unsustainable" — le management dilue le bilan pour maintenir le cours.

### 4. Activist Short (pas long)
**Conditions :** 13D ou lettre d'un short-seller activiste (Hindenburg, Muddy Waters).
**Action :** Traiter comme un événement négatif majeur — vérifier les accusations et les réponses de la société. Score Catalyseur −2 pt immédiat jusqu'à preuve du contraire.

---

## Intégration dans le workflow du matin

```
ÉTAPE 1 — Agent Watchman scanne les news keywords (M&A, buyback, guidance, 13D)
ÉTAPE 2 — Agent Event-Driven lit les filings du jour (8-K, 13D) via SEC / FMP
ÉTAPE 3 — Pour chaque événement détecté sur la watchlist :
         → Identifier le type et la probabilité
         → Chiffrer l'impact (spread, upside, timeline)
         → Déterminer si déjà pricé par le marché
         → Produire le Bloc Event-Driven dans _update.md
ÉTAPE 4 — Transmettre ajustements à Agent Sentiment (Catalyseur) et Fondamental (Valorisation)
ÉTAPE 5 — Mettre à jour Alertes/UPCOMING_EVENTS.md avec timeline
```

---

## Référence — Track record des activistes majeurs

> Documenter dans `Agents/ANALYST_TRACK_RECORD.md` ou un fichier dédié `Agents/ACTIVIST_TRACK_RECORD.md`.

| Activiste | Style | Secteurs préférés | Track record | Approche |
|-----------|-------|-------------------|--------------|----------|
| Elliott Management | Confrontationnel | Multi-sector | Très élevé | Cost cuts, vente, board shake-up |
| Icahn Enterprises | Confrontationnel | Tech, Pharma, Énergie | Élevé | Vente, spin-off, CEO change |
| Starboard Value | Collaboratif | Tech, Consommation | Très élevé | Cost cuts, buybacks, ESG focus |
| Third Point | Mixte | Multi-sector | Élevé | Board seats, strategic review |
| Pershing Square | Concentré | Consommation, REIT | Très élevé | Management friendly, long-term |
| Engine No. 1 | ESG-focus | Énergie, Tech | Modéré | Board seats, transition ESG |
| Hindenburg Research | Short / Fraud | Multi-sector | Très élevé (short) | Rapports détaillés de fraude |
| Muddy Waters | Short / Fraud | Chine, Multi-sector | Élevé (short) | Accounting fraud, overvaluation |

> **Règle :** Un 13D d'Elliott ou Starboard a > 70% de probabilité de succès partiel. Un short report de Hindenburg a > 80% de probabilité de baisse de cours dans les 48h.

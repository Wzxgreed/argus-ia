# Suivi des Prix Cibles — Registre centralisé

Ce fichier recense **tous les prix cibles émis** dans les fichiers `_init.md` et `_update.md` de chaque ticker. Il permet de mesurer si l'agent évalue correctement la valeur des actions — pas seulement les opportunités formellement scorées.

**Mise à jour :** Automatique à chaque création d'un `_init.md` ou `_update.md`. Vérification des fenêtres ouvertes chaque matin dans l'Étape 0.

**Fichier lié :** `Agents/APPRENTISSAGES.md` — reçoit les règles extraites des post-mortems sur prix cibles.

---

## Protocole d'enregistrement obligatoire

```
À CHAQUE CRÉATION D'UN _init.md OU _update.md :
1. Extraire : Ticker · Date · Recommandation · Prix cible · Cours au moment · Upside/Downside
2. Ajouter une ligne dans le journal ci-dessous
3. Calculer les dates de fenêtre : J+30, J+90, J+180
4. Ajouter dans "Fenêtres ouvertes"

À CHAQUE MATIN (Étape 0) :
1. Vérifier si des fenêtres J+30, J+90 ou J+180 arrivent à échéance (±3 jours)
2. Pour chaque fenêtre : récupérer le cours actuel via `quote`
3. Calculer la performance et enregistrer le verdict
4. Si verdict = ❌ Miss → déclencher le post-mortem prix cible (protocole ci-dessous)
```

---

## Définition des verdicts

| Verdict | Condition | Interprétation |
|---------|-----------|----------------|
| ✅ Hit | Prix cible atteint OU direction correcte avec +10% minimum | Analyse juste |
| ⚠️ Partiel | Direction correcte mais prix cible non atteint (<50% du chemin) | Thèse juste, amplitude surestimée |
| ❌ Miss | Direction incorrecte (Buy → cours baisse, Sell → cours monte) | Erreur d'analyse |
| 🔄 Invalidé | Événement externe imprévisible (OPA, fraud, black swan) | Pas une erreur du système |
| ⏳ En cours | Fenêtre pas encore échue | À vérifier plus tard |

---

## Journal des prix cibles

| Date analyse | Ticker | Type fichier | Reco | Prix cible | Cours à l'analyse | Upside/Down | J+30 | J+90 | J+180 | Verdict final | Post-mortem |
|-------------|--------|-------------|------|-----------|------------------|-------------|------|------|-------|--------------|-------------|
| 2026-05-17 | IREN | `_init.md` | ATTENDRE | $65.86 | $52.94 | +24.4% | ❌ Miss | 2026-08-15 | 2026-11-13 | ❌ Miss | — |
| 2026-05-17 | VRT | `_init.md` | SURVEILLER | $400.00 | $370.94 | +7.8% | ❌ Miss | 2026-08-15 | 2026-11-13 | ❌ Miss | — |
| 2026-05-17 | NOK | `_init.md` | SURVEILLER | $9.26 | $13.95 | −33.6% | ❌ Miss | 2026-08-15 | 2026-11-13 | ❌ Miss | — |
| 2026-05-17 | SOFI | `_init.md` | ATTENDRE | $19.51 | $15.61 | +24.9% | ❌ Miss | 2026-08-15 | 2026-11-13 | ❌ Miss | — |
| 2026-05-17 | AAL | `_init.md` | SURVEILLER | $14.00 | $12.31 | +13.7% | ❌ Miss | 2026-08-15 | 2026-11-13 | ❌ Miss | — |
| 2026-05-26 | CTMX | `_init.md` | ATTENDRE | $9.05 | $3.60 | +151.4% | ❌ Miss | 2026-08-24 | 2026-11-22 | ❌ Miss | — |

---

## Fenêtres ouvertes (à vérifier chaque matin)

| Ticker | Date analyse | Prix cible | Cours analyse | J+30 prévu | J+90 prévu | J+180 prévu | Statut |
|--------|-------------|-----------|--------------|-----------|-----------|------------|--------|
| **IREN** | 2026-05-17 | $65.86 | $52.94 | 2026-06-16 | 2026-08-15 | 2026-11-13 | ⏳ En cours |
| **VRT** | 2026-05-17 | $400.00 | $370.94 | 2026-06-16 | 2026-08-15 | 2026-11-13 | ⏳ En cours |
| **NOK** | 2026-05-17 | $9.26 | $13.95 | 2026-06-16 | 2026-08-15 | 2026-11-13 | ⏳ En cours |
| **SOFI** | 2026-05-17 | $19.51 | $15.61 | 2026-06-16 | 2026-08-15 | 2026-11-13 | ⏳ En cours |
| **AAL** | 2026-05-17 | $14.00 | $12.31 | 2026-06-16 | 2026-08-15 | 2026-11-13 | ⏳ En cours |
| **CTMX** | 2026-05-26 | $9.05 | $3.60 | 2026-06-25 | 2026-08-24 | 2026-11-22 | ⏳ En cours |

---

## Performance agrégée des prix cibles

### Par horizon
| Horizon | Total | Hits | Partiels | Misses | Invalidés | Taux de réussite |
|---------|-------|------|---------|--------|-----------|-----------------|
| J+30 | 0 | 0 | 0 | 0 | 0 | — |
| J+90 | 0 | 0 | 0 | 0 | 0 | — |
| J+180 | 0 | 0 | 0 | 0 | 0 | — |

### Par type d'analyse
| Type | Total | Hits J+90 | Taux réussite |
|------|-------|----------|--------------|
| `_init.md` (analyse initiale) | 0 | 0 | — |
| `_update.md` (mise à jour) | 0 | 0 | — |

### Par recommandation
| Reco | Total | Hits J+90 | Taux réussite |
|------|-------|----------|--------------|
| Achat | 0 | 0 | — |
| Neutre | 0 | 0 | — |
| Vente | 0 | 0 | — |

### Précision de l'amplitude (prix cible vs cours réel)
| Horizon | Écart moyen prix cible vs cours réel | Biais (sur/sous-estimation) |
|---------|-------------------------------------|---------------------------|
| J+90 | — | — |
| J+180 | — | — |

---

## Protocole Post-Mortem Prix Cible

> Déclenché automatiquement quand verdict = ❌ Miss à J+90 ou J+180.

```
ÉTAPE 1 — COLLECTE
→ Lire Actions/[TICKER]/[TICKER]_YYYY-MM-DD_[init/update].md (fichier source)
→ Récupérer les cours day-by-day sur la période via `quote`
→ Récupérer les news majeures sur [TICKER] sur la période via `news`
→ Identifier ce qui a fait dévier le cours de la trajectoire anticipée

ÉTAPE 2 — DIAGNOSTIC
→ L'erreur vient-elle de :
   A) DIRECTION incorrecte : l'agent était bullish sur une action qui a baissé
      → Problème fondamental (surévaluation non détectée ?) ou macro (régime ignoré ?)
   B) AMPLITUDE incorrecte : direction juste mais prix cible trop ambitieux
      → Hypothèses DCF trop optimistes ? Croissance surestimée ?
   C) TIMING incorrect : la thèse était juste mais trop tôt
      → Signal technique ignoré ? Force relative déjà dégradée ?
   D) RISQUE non modélisé : événement non anticipé
      → Était-il anticipable ? Des signaux existaient-ils ?

ÉTAPE 3 — RÈGLE EXTRAITE
→ Formuler une règle corrective universelle (ex: "Si DCF croissance > 25% sur 5 ans
  sans earnings track record solide → appliquer marge de sécurité supplémentaire de 20%")

ÉTAPE 4 — DOCUMENTATION
→ Écrire le post-mortem dans Agents/APPRENTISSAGES.md (section Prix Cibles)
→ Ajouter la règle dans "Règles actives"
→ Mettre à jour colonne "Post-mortem" dans ce journal
```

---

## Statistiques d'apprentissage

| Métrique | Valeur |
|----------|--------|
| Prix cibles enregistrés | 1 |
| Post-mortems prix cibles réalisés | 0 |
| Taux de réussite global J+90 | — |
| Biais principal identifié | — |
| Dernière révision des paramètres DCF | — |
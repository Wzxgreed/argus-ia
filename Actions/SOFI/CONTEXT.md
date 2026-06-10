# CONTEXT — SOFI — Dernière mise à jour : 2026-06-10

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ATTENDRE
**Prix cible :** $19.56 (cours + 3×ATR historique)
**Stop-loss :** $14.46 (cours − 2×ATR historique)
**Upside/Downside :** +18.5% / −12.4%
**Dernière mise à jour :** 2026-06-10 (snapshot 10:00 UTC — stabilité des prix, scores agents en baisse, short interest en hausse significative)

SoFi est une fintech-banque hybride avec un écosystème complet (lending + banking + investing) et une marque forte chez les millennials. Le charter bancaire 2022 crée une barrière réglementaire modérée vs les fintechs non-banques. Le snapshot du **2026-06-10 à 10h UTC** montre une **stabilité mécanique** du cours à **$16.50** (+0.18% vs close 09/06) mais révèle une **détérioration sous-jacente des scores agents**. Le **Score Global ajusté recule de 52.3 à 51.5/100** (zone ATTENDRE), rapprochant SOFI du seuil SURVEILLER (<50) de seulement **1.5 pt**. Cette baisse est tirée par le **Catalyseur** (6.8 → 5.3/10, −1.5 pt) et la **Valorisation** (6.0 → 4.5/10, −1.5 pt), partiellement compensée par l'amélioration du **Momentum** (5.0 → 6.0/10, +1.0 pt). Le timing passe de Défavorable à **Neutre**. Le changement le plus significatif est l'**augmentation du short interest de 13.68% à 14.71%** (+1.03 pt) — un niveau élevé qui renforce à la fois le risque de pression baissière et le **potentiel de short squeeze** en cas de catalyseur positif. Le RSI reste stable à **58.52** (zone neutre). Les données techniques (ATR, MM50, MM200) et options (Max Pain, Put/Call, Call OI) sont **partiellement indisponibles** dans ce snapshot matinal — les valeurs historiques sont conservées avec mention [DONNÉES PARTIELLES]. La dépendance aux taux d'intérêt et l'exposition aux prêts étudiants créent des risques macro majeurs. Le Forward P/E **21.11** reste mécaniquement attractif. Le consensus PT **$25.41** (+53.9% upside) est inchangé. Le Filtre Qualité **4/6** (Quality Partielle) n'est pas remis en cause. Earnings Q2 dans **48j** (28 juillet, estimates EPS $0.10–$0.11, Rev $1.1B). ⚠️ Cours encore sous MM50 historique (−1.68% si $16.78 confirmée) = timing Neutre. Attendre reclaim MM50 $16.78 en close avec volume >1.0× ou breakout $17.00 pour réactiver la thèse haussière. Surveiller le support $15.651 — une cassure ouvrirait le retour à $15.00 et risquerait de pousser le Score Global en zone SURVEILLER. Attention au short interest 14.71% qui crée un setup asymétrique squeeze/pression vendeuse.
**Score 5.2/10. Score Global 51.5/100. ATTENDRE — Aucune entrée.**

**Données complètes** — Cours, RSI, P/E, beta disponibles dans `data/latest.json` (snapshot 2026-06-10T10:00 UTC). Données techniques partielles : ATR, MM50, MM200 null. Options : données corrompues (Max Pain $5.00 aberrant) — valeur historique $17.00 conservée. Expiration prochaine 2026-06-12 (2 jours ouvrés).

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $19.56
- **Stop-loss :** $14.46
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Baisse — $13.78 (SL 2×ATR) — 🟢 Active
- Hausse — $18.88 (prix cible) — 🟢 Active
- Volume — >2× moy. 20j (>140.7M) — 🟢 Active

---

## 📅 Prochains événements

- Aucun événement à venir.

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** 58.52
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** 72059377

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-10
- **Type :** update
- **Fichier :** `SOFI_2026-06-10_update.md`
- **Conclusion :** **Date :** 2026-06-10 (snapshot 10:00 UTC — données partielles, pre-market/début de séance)

---

## 🔄 Triggers détectés (full refresh)

- ATR_SPIKE (medium) : ATR relatif 5.13% (seuil 5.0%)
- Le trigger ATR_SPIKE 5.88% est un **faux positif** : l'ATR est resté stable à **$0.97** entre le close 08/06 et le snapshot 09/06. Aucune expansion de volatilité n'est survenue.

---

*Généré automatiquement — ne pas éditer manuellement.*

# CONTEXT — SPCX — Dernière mise à jour : 2026-06-21

> Ce fichier est la **mémoire court terme** du ticker. Les agents LLM le lisent avant chaque analyse pour conserver le contexte sans relire tout l'historique.
> Mise à jour automatique par `agents/update_context/agent.py` à chaque passage du pipeline.

---

## 🎯 Thèse active

- **Recommandation :** ÉVITER (artefact mécanique — fondamentalement non-actionnable)
**Prix cible :** N/A (données insuffisantes — cours fictif)
**Stop-loss :** N/A
**Upside :** —
**Dernière mise à jour :** 2026-06-17 (snapshot 13h UTC)

> SPCX est un ETF thématique SPAC/post-IPO. Le snapshot 13h UTC du 17/06 confirme la **stabilité mécanique totale** vs 10h sur le cours ($201.80 inchangé), le volume (322.1M) et le market cap ($2.66T). Le **conflit de symbole FMP chronique** persiste : FMP renvoie un **cours fictif $201.80** (+4.83% vs previous close $192.50), accompagné d'un faux market cap de **$2.66T** et d'un forward P/E de **−2,242**. L'Agent Recommandation **maintient ÉVITER** avec un Score Global de **20.0/100** (Score Opportunité 2.0/10 : C:5.5 V:2.0 M:5.5), timing Neutre. Le Score Valorisation à **2.0/10** reste exactement sur le seuil de disqualification (≤ 2/10). Le secteur persiste `Industrials` / `Aerospace & Defense` au lieu de `Financial Services` / `Asset Management`. Deux évolutions significatives : (1) **résolution de l'anomalie validation report** — le `[WARNING] SPCX: volume is 0` du snapshot 10h a disparu, confirmant la cohérence pipeline ; (2) **mutation majeure des données options** — `max_pain` est passé de `25.0` (10h) à **210.0** (13h), avec apparition d'un `put_call_ratio` à **0.66** et d'un `call_oi_pct` à **60.3%**. Le niveau 210.0 est quasi-aligné sur le faux cours 201.80, confirmant que ces options sont celles de l'entité étrangère mappée par FMP. Le module sector rotation est stable (NEUTRAL, 11/11 secteurs OK, XLK momentum_score 10.0, XLF momentum_score 5.32). Aucun catalyseur fondamental, news, ni social. SL/TP non calculables (prix et ATR absents). Rétablissement possible si retour d'une source de prix fiable avec sector correct (`Financial Services`) + volume >1 000 + options cohérentes. Si le flux fiable ne revient pas ou si les données continuent de muter → maintien **ÉVITER**.

---

## Actualités ayant impacté ce dossier
- **Score global :** —/10
- **Prix cible :** $—
- **Stop-loss :** $—
- **Statut thèse :** validée
- **Horizon :** —

---

## 📉 Erreurs de prédiction récentes

- Aucune erreur enregistrée.

---

## 🚨 Alertes actives

- Aucune alerte active.

---

## 📅 Prochains événements

- **2026-06-22** · earnings · Earnings ...

---

## 📊 Contexte technique (dernier snapshot)

- **RSI 14j :** —
- **MM 50j :** —
- **MM 200j :** —
- **ATR 14j :** —
- **Volume moy. 20j :** 288941860

---

## 📝 Résumé dernière analyse

- **Date :** 2026-06-21
- **Type :** preview
- **Fichier :** `SPCX_2026-06-21_preview.md`
- **Conclusion :** > **Date :** 2026-06-21

---

## 🔄 Triggers détectés (full refresh)

- Aucun trigger récent.

---

*Généré automatiquement — ne pas éditer manuellement.*

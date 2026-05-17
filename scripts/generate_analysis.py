#!/usr/bin/env python3
"""
generate_analysis.py — Génère automatiquement une analyse initiale pour un ticker
en appelant le LLM proxy avec un prompt structuré.

Usage :
  python3 scripts/generate_analysis.py AAPL
"""
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ACTIONS_DIR = BASE_DIR / "Actions"

sys.path.insert(0, str(BASE_DIR / "scripts"))
from ask_llm import ask_llm


def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def build_prompt(ticker: str, data: dict) -> str:
    price = data.get("price", {})
    tech = data.get("technical", {})
    fund = data.get("fundamentals", {})
    options = data.get("options", {})

    return f"""Tu es l'Agent Analyste d'Argus-IA, un système institutionnel d'analyse d'actions. Génère une analyse initiale complète pour le ticker {ticker} au format markdown standardisé ci-dessous.

## DONNÉES BRUTES DU TICKER

**Cours :**
- Close : ${price.get('close', 'N/A')}
- Open : ${price.get('open', 'N/A')}
- High : ${price.get('high', 'N/A')}
- Low : ${price.get('low', 'N/A')}
- Previous Close : ${price.get('previous_close', 'N/A')}
- Change % : {price.get('change_pct', 'N/A')}%
- Volume : {price.get('volume', 'N/A'):,}
- Volume moyen 20j : {price.get('volume_avg_20d', 'N/A'):,}

**Technique :**
- RSI 14j : {tech.get('rsi14', 'N/A')}
- ATR 14j : ${tech.get('atr14', 'N/A')}
- MM 50j : ${tech.get('mm50', 'N/A')}
- MM 200j : ${tech.get('mm200', 'N/A') or 'N/A'}
- Golden/Death Cross : {tech.get('golden_cross', 'N/A') or 'Non'}

**Fondamentaux :**
- Market Cap : ${fund.get('market_cap', 'N/A'):,}
- Secteur : {fund.get('sector', 'N/A')}
- Industrie : {fund.get('industry', 'N/A')}
- P/E : {fund.get('pe_ratio', 'N/A') or 'N/A'}
- Forward P/E : {fund.get('forward_pe', 'N/A') or 'N/A'}
- EV/EBITDA : {fund.get('ev_ebitda', 'N/A') or 'N/A'}
- EV/Revenue : {fund.get('ev_revenue', 'N/A') or 'N/A'}
- P/B : {fund.get('price_to_book', 'N/A') or 'N/A'}
- Dividend Yield : {fund.get('dividend_yield', 'N/A') or 'N/A'}%
- Beta : {fund.get('beta', 'N/A') or 'N/A'}
- Short Interest : {fund.get('short_interest_pct', 'N/A') or 'N/A'}%
- Float : {fund.get('shares_float', 'N/A'):,}
- Outstanding : {fund.get('shares_outstanding', 'N/A'):,}
- 52W High : ${fund.get('fifty_two_week_high', 'N/A')}
- 52W Low : ${fund.get('fifty_two_week_low', 'N/A')}

**Options :**
- Max Pain : ${options.get('max_pain', 'N/A')}
- Put/Call Ratio : {options.get('put_call_ratio', 'N/A')}
- Call OI % : {options.get('call_oi_pct', 'N/A')}%

## FORMAT ATTENDU

Crée le rapport en suivant EXACTEMENT cette structure :

```markdown
# {ticker} — Analyse Initiale ({now_str()})

## Résumé Exécutif
[1-2 phrases sur la thèse principale]

## Filtre Qualité (6 critères)
| Critère | Score | Commentaire |
|---------|-------|-------------|
| Revenue CAGR 5 ans | ?/1 | [justification] |
| Profit CAGR 5 ans | ?/1 | [justification] |
| Assets/Liabilities > 1.0 | ?/1 | [justification] |
| FCF positif croissant | ?/1 | [justification] |
| Moat structurel | ?/1 | [justification] |
| TAM ×5 / 10 ans | ?/1 | [justification] |

**Score Qualité : X/6** → [✅/⚠️/🔴]

## Bloc Technique
- RSI 14j : {tech.get('rsi14', 'N/A')} → [interprétation]
- ATR 14j : ${tech.get('atr14', 'N/A')} → Stop-loss suggéré = close − 2×ATR = ${price.get('close', 0) - 2 * tech.get('atr14', 0) if price.get('close') and tech.get('atr14') else 'N/A'}
- MM50j : ${tech.get('mm50', 'N/A')} → [position vs cours]
- MM200j : {tech.get('mm200', 'N/A') or 'N/A'} → [position vs cours]
- Volume : {price.get('volume', 'N/A'):,} vs moyenne 20j {price.get('volume_avg_20d', 'N/A'):,} → [interprétation]

**Verdict Timing :** [Favorable / Neutre / Défavorable]

## Bloc Fondamental
- Market Cap : ${fund.get('market_cap', 'N/A'):,}
- P/E : {fund.get('pe_ratio', 'N/A') or 'N/A'} | Forward P/E : {fund.get('forward_pe', 'N/A') or 'N/A'}
- EV/EBITDA : {fund.get('ev_ebitda', 'N/A') or 'N/A'}
- P/B : {fund.get('price_to_book', 'N/A') or 'N/A'}
- Beta : {fund.get('beta', 'N/A') or 'N/A'}
- Short Interest : {fund.get('short_interest_pct', 'N/A') or 'N/A'}%

## Bloc Options
- Max Pain : ${options.get('max_pain', 'N/A')}
- Put/Call Ratio : {options.get('put_call_ratio', 'N/A')}

## Bloc Sentiment
[Analyse des news récentes si disponibles, sinon "Données sentiment à compléter"]

## Scoring
| Score | Valeur | Pondération |
|-------|--------|-------------|
| Catalyseur | X/10 | 35% |
| Valorisation | X/10 | 40% |
| Momentum | X/10 | 25% |
| **Score Opportunité** | **X/10** | |

## Niveaux et Ratio R/R
- Cours actuel : ${price.get('close', 'N/A')}
- Stop-loss suggéré : ${round(price.get('close', 0) - 2 * tech.get('atr14', 0), 2) if price.get('close') and tech.get('atr14') else 'N/A'}
- Take-profit suggéré : ${round(price.get('close', 0) + 3 * tech.get('atr14', 0), 2) if price.get('close') and tech.get('atr14') else 'N/A'}
- Ratio Risque/Rendement : X:1

## Scénarios
1. **Optimiste** (XX%) : [description]
2. **Central** (XX%) : [description]
3. **Pessimiste** (XX%) : [description]

## Risques Clés
1. [risque 1]
2. [risque 2]
3. [risque 3]

## Conclusion
[ACHETER / ATTENDRE / SURVEILLER / ÉVITER]

---
*Généré automatiquement par Argus-IA le {now_str()}*
```

RÈGLES :
- Utilise UNIQUEMENT les chiffres fournis ci-dessus. Ne devine aucune métrique.
- Si une donnée est manquante, note "[DONNÉES MANQUANTES]".
- Le Filtre Qualité doit être réaliste : si les données manquent pour un critère, donne 0 ou 0.5 avec explication.
- Le rapport doit être professionnel, concis et actionnable.
- Le score global doit refléter les données réelles (pas de biais haussier par défaut).
"""


def generate_analysis(ticker: str) -> tuple[str, str]:
    """Génère l'analyse complète et retourne (chemin_fichier, contenu)."""
    ticker = ticker.upper()
    today = now_str()

    # Charger les données
    latest = load_json(DATA_DIR / "latest.json")
    ticker_data = latest.get("prices", {}).get(ticker)
    if not ticker_data:
        raise ValueError(f"Aucune donnée trouvée pour {ticker} dans data/latest.json")

    # Construire le prompt
    prompt = build_prompt(ticker, ticker_data)
    print(f"[generate_analysis] Appel LLM pour {ticker}...")

    # Appeler le LLM
    system = "Tu es un analyste financier senior spécialisé en actions US/Europe. Tu produis des rapports institutionnels concis et structurés."
    response = ask_llm(prompt, model="kimi-k2.6:cloud", system=system)

    if response.startswith("[ERREUR]"):
        raise RuntimeError(f"Échec LLM : {response}")

    # Nettoyer la réponse (enlever les balises markdown si présentes)
    content = response.strip()
    if content.startswith("```markdown"):
        content = content[len("```markdown"):].strip()
    if content.endswith("```"):
        content = content[:-3].strip()

    # Créer le dossier
    ticker_dir = ACTIONS_DIR / ticker
    ticker_dir.mkdir(parents=True, exist_ok=True)

    # Sauvegarder le rapport
    filename = f"{ticker}_{today}_init.md"
    filepath = ticker_dir / filename
    filepath.write_text(content, encoding="utf-8")
    print(f"[generate_analysis] Rapport sauvegardé : {filepath}")

    # Créer INDEX.md
    index_path = ticker_dir / "INDEX.md"
    if not index_path.exists():
        index_content = f"""# {ticker}

## Thèse courante
À définir après lecture du rapport initial.

## Historique
| Date | Fichier | Type |
|------|---------|------|
| {today} | [{filename}]({filename}) | Analyse initiale |

## Agenda
- Prochain earnings : [à compléter]

## Alertes actives
- Aucune
"""
        index_path.write_text(index_content, encoding="utf-8")
        print(f"[generate_analysis] INDEX.md créé : {index_path}")
    else:
        # Ajouter la ligne dans l'historique
        lines = index_path.read_text(encoding="utf-8").splitlines()
        # Trouver la table et insérer la nouvelle ligne
        for i, line in enumerate(lines):
            if line.startswith("| Date | Fichier | Type |"):
                # Insert after separator line
                if i + 1 < len(lines) and lines[i + 1].startswith("|"):
                    lines.insert(i + 2, f"| {today} | [{filename}]({filename}) | Analyse initiale |")
                break
        index_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"[generate_analysis] INDEX.md mis à jour")

    # Créer CONTEXT.md
    context_path = ticker_dir / "CONTEXT.md"
    if not context_path.exists():
        context_content = f"""# Contexte {ticker}

## Thèse active
[À compléter après lecture du rapport]

## Score actuel
- Opportunité : X/10
- Valorisation : X/10
- Momentum : X/10

## Niveaux
- Cours : ${ticker_data.get('price', {}).get('close', 'N/A')}
- SL : [à définir]
- TP : [à définir]

## Statut
[ACTIVE / EN SURVEILLANCE / CLOS]
"""
        context_path.write_text(context_content, encoding="utf-8")
        print(f"[generate_analysis] CONTEXT.md créé")

    return str(filepath), content


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Génère une analyse initiale LLM pour un ticker")
    parser.add_argument("ticker", help="Ticker à analyser (ex: AAPL)")
    args = parser.parse_args()

    try:
        path, content = generate_analysis(args.ticker)
        print(f"\n✅ Analyse générée avec succès : {path}")
        print(f"   Longueur : {len(content)} caractères")
    except Exception as e:
        print(f"\n❌ Erreur : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

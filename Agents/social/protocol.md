# Agent Social Sentiment — Protocole de Sentiment Retail

**Script associé :** `agents/social/agent.py`
**Output :** `data/social_sentiment_YYYY-MM-DD.json`

---

## Mission

Scanner le sentiment retail sur les réseaux sociaux pour compléter le sentiment institutionnel. Détecter les extremes de euphorie/panique et les setups pump/dump.

---

## Sources

| Source | Endpoint / Méthode |
|--------|-------------------|
| Reddit | API publique (r/wallstreetbets, r/stocks, r/investing, r/StockMarket) |
| Yahoo Finance | Mentions dans les commentaires news |
| StockTwits | Symbol stream (scraping léger) |

---

## Signaux Calculés

### 1. Mention Count
Nombre de posts/comments mentionnant le ticker sur une fenêtre glissante (24h / 7j).

### 2. Sentiment Score /10
Analyse lexicale simple via wordlists :
- **Positif** : bull, moon, hold, buy, undervalued, strong, beat
- **Négatif** : bear, crash, sell, overvalued, weak, miss, fraud
- **Neutre** : thoughts?, what do, any news

Formule :
```
sentiment = (mentions_positives − mentions_négatives) / total_mentions
score = 5 + (sentiment × 5)  # normalisé 0-10
```

### 3. Pump Detection
Mots-clés de euphorie excessive :
- "YOLO", "lambo", "all-in", "diamond hands", "to the moon", "100x"
- Ratio pump-words / total_words > 15% → **pump detected**

### 4. Mention Spike
```
spike_ratio = mentions_24h / moyenne_mentions_7j
```
- Spike > 3× → noter comme événement social majeur
- Spike > 5× + sentiment > 8.5 → probable pump coordonné

### 5. Top Posts par Engagement
Posts avec le plus de upvotes/comments sur le ticker → lire le contenu pour extraire la thèse retail dominante.

---

## Seuils d'Alerte

| Condition | Action |
|-----------|--------|
| Sentiment > 8.5 | 🔴 Extrême euphorie — probable top retail, prendre avec recul |
| Sentiment < 1.5 | 🔴 Panique excessive — possible opportunité de contre-attaque |
| Pump detected + spike > 3× | ⚠️ Alerter [PUMP ALERT] dans l'analyse |
| Spike > 5× sans news majeure | ⚠️ Vérifier manipulation / rumeur non fondée |

---

## Intégration Scoring

- Sentiment > 8.5 + pas de catalyseur institutionnel confirmé → malus −5 sur Score Global (beware retail hype)
- Sentiment < 1.5 + fondamentaux intacts → bonus +2 sur Score Catalyseur (contraire retail)
- Pump detected → mentionner [PUMP ALERT] et vérifier avec sources institutionnelles avant tout sizing

---

## Output JSON

```json
{
  "AAPL": {
    "mention_count_24h": 1420,
    "sentiment_score": 6.2,
    "pump_detected": false,
    "spike_ratio": 1.1,
    "top_posts": [
      {"subreddit": "r/stocks", "title": "AAPL post-earnings thoughts", "engagement": 340}
    ]
  }
}
```

---

*Protocole lu par l'agent LLM et implémenté dans `agents/social/agent.py`.*

#!/usr/bin/env python3
"""
agent_social.py — Agent Social Media Sentiment (Retail).

Protocol : `agents/social/protocol.md`

Scanne les réseaux sociaux retail pour détecter le sentiment de la foule
sur les tickers de la watchlist :
  • Reddit (r/wallstreetbets, r/stocks, r/investing, r/StockMarket)
  • Yahoo Finance Community (mentions dans les news comments)
  • StockTwits (symbol stream via scraping léger)

Méthodologie :
  1. Collecte des posts/comments mentionnant les tickers
  2. Analyse lexicale simple (wordlists positifs/négatifs)
  3. Score Retail Sentiment /10 par ticker
  4. Détection de pump/dump (volume anormal de mentions + sentiment extrême)
  4. Alertes : mention volume >3x moyenne 7j ou sentiment >8 ou <2

Output :
  data/social_sentiment_YYYY-MM-DD.json + symlink latest

Usage :
    python agents/social/agent.py
"""

import json
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"

SUBREDDITS = ["wallstreetbets", "stocks", "investing", "StockMarket", "wallstreetbetsOGs"]

# Simple English sentiment word lists (Reddit is primarily English)
POSITIVE_WORDS = {
    "bullish", "bull", "long", "buy", "moon", "rocket", "tendies", "gain", "gains",
    "green", "up", "surge", "rally", "breakout", " ATH", "all time high", "strong",
    "beat", "crush", "moonshot", "lambo", "rich", "pump", "hodl", "hold", "diamond hands",
    "calls", "call", "undervalued", "cheap", "discount", "opportunity", "gold",
    "printing", "tendie", "squeeze", "short squeeze", "gamma", "ramp", "explode",
    "massive", "huge", "epic", "insane", "crazy good", "beautiful", "perfect",
    "solid", "great", "amazing", "excellent", "outstanding", "phenomenal", "love",
    "win", "winning", "winner", "champion", "mooning", "flying", "soaring",
    "parabolic", "vertical", "rip", "ripping", "send it", "yolo", "all in",
}

NEGATIVE_WORDS = {
    "bearish", "bear", "short", "sell", "crash", "dump", "tank", "plunge", "drop",
    "red", "down", "fall", "decline", "collapse", "implode", "disaster", "bad",
    "loss", "losses", "lose", "losing", "bagholder", "bagholders", "bag holding",
    "puts", "put", "overvalued", "expensive", "bubble", "ponzi", "scam", "fraud",
    "rug pull", "rugpull", "dumping", "cratering", "nosedive", "freefall",
    "panic", "fear", "worried", "concern", "concerned", "doom", "doomed",
    "death", "dying", "dead", "crap", "trash", "garbage", "shit", "fuck",
    "damn", "hell", "disaster", "nightmare", "terrible", "awful", "horrible",
    "worst", "fail", "failed", "failure", "bankruptcy", "bankrupt", "delist",
    "sec investigation", "lawsuit", "investigation", " subpoena",
    "margin call", "liquidation", "forced sell", "stop loss", "stopped out",
}

PUMP_INDICATORS = {
    "to the moon", "lambo", "millionaire", "get rich quick", "guaranteed",
    "can't lose", "sure thing", "100x", "1000x", "10x", "easy money",
    "free money", "no brainer", "can't go tits up", "literally can't go down",
    "YOLO", "all in", "mortgage", "refinance", "sell everything", "life savings",
    "retirement account", "401k", "irresponsible", "diamond hands", "hold forever",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_tickers() -> list[str]:
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
        return [t["ticker"] for t in config.get("tickers", [])]
    except Exception:
        return []


def reddit_search(subreddit: str, query: str, limit: int = 25) -> list[dict]:
    """
    Search Reddit via public JSON API (no auth required for read-only).
    Rate limited: max ~30 req/min.
    """
    url = (
        f"https://www.reddit.com/r/{subreddit}/search.json"
        f"?q={query}&restrict_sr=1&sort=new&t=day&limit={limit}"
    )
    req = Request(url, headers={"User-Agent": "Argus-IA/1.0 (by /u/argus-ia-bot)"})
    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        if e.code == 429:
            print(f"[social] Reddit rate limit on r/{subreddit}. Sleeping 60s...", file=sys.stderr)
            time.sleep(60)
            return reddit_search(subreddit, query, limit)
        print(f"[social] Reddit HTTP {e.code} for r/{subreddit} q={query}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"[social] Reddit error r/{subreddit}: {e}", file=sys.stderr)
        return []

    posts = []
    for child in data.get("data", {}).get("children", []):
        p = child.get("data", {})
        posts.append({
            "title": p.get("title", ""),
            "selftext": p.get("selftext", ""),
            "author": p.get("author", ""),
            "subreddit": p.get("subreddit", ""),
            "created_utc": p.get("created_utc", 0),
            "score": p.get("score", 0),
            "num_comments": p.get("num_comments", 0),
            "url": f"https://reddit.com{p.get('permalink', '')}",
        })
    return posts


def analyze_sentiment(text: str) -> dict:
    """
    Simple lexicon-based sentiment analysis.
    Returns: {"positive_count", "negative_count", "neutral_count", "sentiment_score"}
    """
    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)

    pos = sum(1 for w in words if w in POSITIVE_WORDS)
    neg = sum(1 for w in words if w in NEGATIVE_WORDS)

    # Also check multi-word phrases
    for phrase in PUMP_INDICATORS:
        if phrase in text_lower:
            pos += 2  # Pump phrases counted as strong positive signal (but flagged separately)

    total_sentiment_words = pos + neg
    if total_sentiment_words == 0:
        sentiment_score = 0.0  # neutral
    else:
        sentiment_score = (pos - neg) / total_sentiment_words  # -1.0 to +1.0

    return {
        "positive_count": pos,
        "negative_count": neg,
        "total_words": len(words),
        "sentiment_score": round(sentiment_score, 3),
    }


def aggregate_ticker_sentiment(posts: list[dict], ticker: str) -> dict:
    """Aggregate sentiment across all posts for a ticker."""
    if not posts:
        return {
            "mention_count": 0,
            "avg_score": 0.0,
            "avg_comments": 0.0,
            "sentiment_score": 0.0,
            "sentiment_label": "No data",
            "pump_detected": False,
            "top_posts": [],
        }

    total_score = 0
    total_comments = 0
    total_pos = 0
    total_neg = 0
    pump_detected = False
    sentiment_scores = []
    top_posts = []

    for p in posts:
        text = f"{p['title']} {p['selftext']}"
        analysis = analyze_sentiment(text)
        total_score += p["score"]
        total_comments += p["num_comments"]
        total_pos += analysis["positive_count"]
        total_neg += analysis["negative_count"]
        sentiment_scores.append(analysis["sentiment_score"])

        # Pump detection
        text_lower = text.lower()
        for phrase in PUMP_INDICATORS:
            if phrase in text_lower:
                pump_detected = True
                break

        # Keep top posts by engagement
        top_posts.append({
            "title": p["title"][:100] + "..." if len(p["title"]) > 100 else p["title"],
            "score": p["score"],
            "comments": p["num_comments"],
            "subreddit": p["subreddit"],
            "sentiment": analysis["sentiment_score"],
        })

    n = len(posts)
    avg_score = total_score / n if n > 0 else 0
    avg_comments = total_comments / n if n > 0 else 0

    # Overall sentiment
    total_sentiment = total_pos + total_neg
    if total_sentiment == 0:
        overall_sentiment = 0.0
    else:
        overall_sentiment = (total_pos - total_neg) / total_sentiment

    # Scale to /10
    score_10 = round((overall_sentiment + 1) * 5, 2)
    score_10 = max(0.0, min(10.0, score_10))

    label = (
        "🔴 Very Bearish" if score_10 <= 2 else
        "🟠 Bearish" if score_10 <= 4 else
        "🟡 Neutral" if score_10 <= 6 else
        "🟢 Bullish" if score_10 <= 8 else
        "🟢 Very Bullish"
    )

    top_posts.sort(key=lambda x: x["score"] + x["comments"] * 2, reverse=True)

    return {
        "mention_count": n,
        "avg_score": round(avg_score, 1),
        "avg_comments": round(avg_comments, 1),
        "sentiment_score": score_10,
        "sentiment_label": label,
        "raw_sentiment": round(overall_sentiment, 3),
        "positive_words": total_pos,
        "negative_words": total_neg,
        "pump_detected": pump_detected,
        "top_posts": top_posts[:5],
    }


def load_historical_mentions(ticker: str, days: int = 7) -> list[int]:
    """Load historical mention counts from past reports."""
    counts = []
    for i in range(1, days + 1):
        date = (datetime.now(timezone.utc) - timedelta(days=i)).strftime("%Y-%m-%d")
        path = DATA_DIR / f"social_sentiment_{date}.json"
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                ticker_data = data.get("analysis", {}).get(ticker, {})
                counts.append(ticker_data.get("mention_count", 0))
            except Exception:
                pass
    return counts


def main():
    print("[social] Starting social media sentiment scan...", file=sys.stderr)
    tickers = load_tickers()
    if not tickers:
        print("[social] No tickers found. Skipping.", file=sys.stderr)
        return 0

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    results = {}
    alerts = []

    for ticker in tickers:
        print(f"[social] Scanning {ticker}...", file=sys.stderr)
        all_posts = []

        for subreddit in SUBREDDITS:
            posts = reddit_search(subreddit, ticker, limit=25)
            all_posts.extend(posts)
            if posts:
                print(f"[social]   r/{subreddit}: {len(posts)} posts", file=sys.stderr)
            time.sleep(2)  # Rate limit protection

        # Also search with $ prefix (common on WSB)
        for subreddit in ["wallstreetbets", "stocks"]:
            posts = reddit_search(subreddit, f"${ticker}", limit=15)
            all_posts.extend(posts)
            time.sleep(2)

        # Deduplicate by URL
        seen = set()
        unique_posts = []
        for p in all_posts:
            if p["url"] not in seen:
                seen.add(p["url"])
                unique_posts.append(p)

        agg = aggregate_ticker_sentiment(unique_posts, ticker)

        # Historical comparison
        hist = load_historical_mentions(ticker, days=7)
        avg_mentions = sum(hist) / len(hist) if hist else 0
        mention_spike = agg["mention_count"] >= avg_mentions * 3 if avg_mentions > 0 else False

        # Alerts
        if mention_spike:
            alerts.append({
                "ticker": ticker,
                "type": "MENTION_SPIKE",
                "value": agg["mention_count"],
                "avg_7d": round(avg_mentions, 1),
            })
        if agg["sentiment_score"] >= 8.5:
            alerts.append({
                "ticker": ticker,
                "type": "EXTREME_BULLISH",
                "value": agg["sentiment_score"],
            })
        if agg["sentiment_score"] <= 1.5:
            alerts.append({
                "ticker": ticker,
                "type": "EXTREME_BEARISH",
                "value": agg["sentiment_score"],
            })
        if agg["pump_detected"]:
            alerts.append({
                "ticker": ticker,
                "type": "PUMP_INDICATORS",
                "value": True,
            })

        results[ticker] = {
            **agg,
            "mention_spike": mention_spike,
            "avg_mentions_7d": round(avg_mentions, 1),
        }

        print(
            f"[social]   {ticker}: {agg['mention_count']} mentions, "
            f"sentiment={agg['sentiment_score']}/10 ({agg['sentiment_label']}), "
            f"pump={agg['pump_detected']}",
            file=sys.stderr
        )

    report = {
        "meta": {
            "date": date_str,
            "tickers_scanned": len(tickers),
            "subreddits": SUBREDDITS,
            "total_posts_collected": sum(r["mention_count"] for r in results.values()),
            "alerts_count": len(alerts),
        },
        "analysis": results,
        "alerts": alerts,
    }

    output_path = DATA_DIR / f"social_sentiment_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "social_sentiment_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(f"[social] Report → {output_path} | Alerts: {len(alerts)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

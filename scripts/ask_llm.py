#!/usr/bin/env python3
"""
ask_llm.py — Client simplifié qui passe par le proxy local avec tracking.
Usage :
  python3 scripts/ask_llm.py --prompt "Analyse AAPL" --model kimi-k2.6
  echo '{"role":"user","content":"Hello"}' | python3 scripts/ask_llm.py --stdin
"""
import argparse
import json
import os
import sys
import urllib.request

PROXY_URL = os.getenv("LLM_PROXY_URL", "http://127.0.0.1:11435/v1/chat/completions")


def ask_llm(prompt: str, model: str = "kimi-k2.6", system: str = "", stream: bool = False) -> str:
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": model,
        "messages": messages,
        "stream": stream,
        "temperature": 0.7,
    }

    req = urllib.request.Request(
        PROXY_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = json.loads(resp.read())
            choices = body.get("choices", [])
            if choices:
                return choices[0].get("message", {}).get("content", "")
            return body.get("response", str(body))
    except urllib.error.HTTPError as e:
        return f"[ERREUR] {e.code}: {e.read().decode(errors='ignore')}"
    except Exception as e:
        return f"[ERREUR] {e}"


def main():
    parser = argparse.ArgumentParser(description="Pose une question au LLM via le proxy local")
    parser.add_argument("--prompt", "-p", required=True, help="Question/prompt")
    parser.add_argument("--model", "-m", default="kimi-k2.6", help="Modèle")
    parser.add_argument("--system", "-s", default="", help="Instruction système")
    parser.add_argument("--json", action="store_true", help="Sortie JSON brute")
    args = parser.parse_args()

    result = ask_llm(args.prompt, args.model, args.system)

    if args.json:
        print(result)
    else:
        print("=" * 60)
        print(result)
        print("=" * 60)


if __name__ == "__main__":
    main()

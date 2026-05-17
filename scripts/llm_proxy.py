#!/usr/bin/env python3
"""
llm_proxy.py — Proxy OpenAI-compatible avec tracking d'usage automatique.
Écoute sur localhost:11435 et forward les requêtes vers Ollama/Anthropic
en comptant les appels et tokens automatiquement.

Usage :
  python3 scripts/llm_proxy.py                  # Démarrer le proxy
  python3 scripts/llm_proxy.py --stop             # Arrêter le proxy
  python3 scripts/llm_proxy.py --status         # Voir si le proxy tourne
  python3 scripts/llm_proxy.py --daemon         # Mode daemon (background)

Configuration (env vars ou data/ollama_config.json) :
  LLM_TARGET_URL    — Endpoint cible (défaut: http://localhost:11434/v1/chat/completions)
  LLM_API_KEY       — Clé API si nécessaire
  LLM_PROXY_PORT    — Port du proxy (défaut: 11435)
"""
import argparse
import http.client
import json
import os
import socket
import signal
import sys
import threading
import time
import urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
USAGE_FILE = BASE_DIR / "data" / "ollama_usage.json"
CONFIG_FILE = BASE_DIR / "data" / "ollama_config.json"
PID_FILE = BASE_DIR / "data" / ".llm_proxy.pid"


# ─────────────────────────── Helpers ───────────────────────────

def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def save_json(path: Path, data: dict):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def load_dotenv(path: Path):
    """Charge un fichier .env dans os.environ."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())


def load_config() -> dict:
    """Charge config depuis JSON puis override par env vars."""
    # Charge .env.local s'il existe
    load_dotenv(BASE_DIR / ".env.local")

    config = load_json(CONFIG_FILE)
    # Env vars priment sur le fichier de config
    if os.getenv("LLM_TARGET_URL"):
        config["endpoint"] = os.getenv("LLM_TARGET_URL")
    if os.getenv("LLM_API_KEY"):
        config["api_key"] = os.getenv("LLM_API_KEY")
    if os.getenv("LLM_PROXY_PORT"):
        config["proxy_port"] = int(os.getenv("LLM_PROXY_PORT"))
    # Valeurs par défaut
    config.setdefault("endpoint", "http://localhost:11434/v1/chat/completions")
    config.setdefault("api_key", "")
    config.setdefault("proxy_port", 11435)
    return config


def estimate_tokens(text: str) -> int:
    """Estimation rapide : ~4 caractères/token (moyenne anglais)."""
    return max(len(text) // 4, 1)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def update_usage(req_tokens: int, resp_tokens: int, calls: int = 1):
    """Incrémente le compteur d'usage Ollama localement (fenêtre 5h + hebdo)."""
    usage = load_json(USAGE_FILE)
    now = now_utc()

    # ── Fenêtre glissante 5h ───────────────────────────
    window_start_str = usage.get("window_5h_start")
    if window_start_str:
        window_start = datetime.fromisoformat(window_start_str.replace("Z", "+00:00"))
    else:
        window_start = now

    # Reset si la fenêtre de 5h est dépassée
    if (now - window_start).total_seconds() >= 5 * 3600:
        usage["window_5h_start"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        usage["window_5h_calls"] = 0
        usage["window_5h_tokens_input"] = 0
        usage["window_5h_tokens_output"] = 0

    usage["window_5h_calls"] = usage.get("window_5h_calls", 0) + calls
    usage["window_5h_tokens_input"] = usage.get("window_5h_tokens_input", 0) + req_tokens
    usage["window_5h_tokens_output"] = usage.get("window_5h_tokens_output", 0) + resp_tokens

    # ── Semaine (lundi 00:00 UTC) ──────────────────────
    week_start_str = usage.get("week_start")
    current_week_start = now.strftime("%Y-%m-%d")
    # Trouver le lundi de cette semaine
    monday = now - __import__("datetime").timedelta(days=now.weekday())
    monday_str = monday.strftime("%Y-%m-%d")

    if week_start_str != monday_str:
        usage["week_start"] = monday_str
        usage["weekly_calls"] = 0
        usage["weekly_tokens_input"] = 0
        usage["weekly_tokens_output"] = 0

    usage["weekly_calls"] = usage.get("weekly_calls", 0) + calls
    usage["weekly_tokens_input"] = usage.get("weekly_tokens_input", 0) + req_tokens
    usage["weekly_tokens_output"] = usage.get("weekly_tokens_output", 0) + resp_tokens

    save_json(USAGE_FILE, usage)

    # Sync vers frontend/dist/data/ pour le dashboard
    dist_file = BASE_DIR / "frontend" / "dist" / "data" / "ollama_usage.json"
    if dist_file.parent.exists():
        save_json(dist_file, usage)

    return usage


def openai_to_ollama(payload: dict) -> dict:
    """Convertit une requête OpenAI en format Ollama natif."""
    return {
        "model": payload.get("model", "ministral-3:3b"),
        "messages": payload.get("messages", []),
        "stream": payload.get("stream", False),
        "options": {
            "temperature": payload.get("temperature", 0.7),
        },
    }


def ollama_to_openai(ollama_resp: dict, req_tokens: int) -> dict:
    """Convertit une réponse Ollama natif en format OpenAI."""
    msg = ollama_resp.get("message", {})
    prompt_eval = ollama_resp.get("prompt_eval_count", req_tokens)
    eval_count = ollama_resp.get("eval_count", 0)
    return {
        "id": f"ollama-{ollama_resp.get('model', 'unknown')}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": ollama_resp.get("model", "unknown"),
        "choices": [{
            "index": 0,
            "message": {
                "role": msg.get("role", "assistant"),
                "content": msg.get("content", ""),
            },
            "finish_reason": "stop" if ollama_resp.get("done") else "length",
        }],
        "usage": {
            "prompt_tokens": prompt_eval,
            "completion_tokens": eval_count,
            "total_tokens": prompt_eval + eval_count,
        },
    }


def forward_request(target_url: str, api_key: str, body: bytes, headers: dict) -> tuple:
    """Forward la requête vers le LLM cible."""
    req = urllib.request.Request(
        target_url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            **({"Authorization": f"Bearer {api_key}"} if api_key else {}),
        },
        method="POST",
    )
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            resp_body = resp.read()
            status = resp.status
    except urllib.error.HTTPError as e:
        resp_body = e.read()
        status = e.code
    latency = time.time() - start
    return status, resp_body, latency


# ─────────────────────────── Handler ───────────────────────────

class ProxyHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Réduit le bruit — log seulement les erreurs
        pass

    def _send_json(self, status: int, body: dict):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()

    def do_GET(self):
        # Endpoint healthcheck
        if self.path == "/health":
            self._send_json(200, {"status": "ok", "proxy": "llm_proxy"})
            return
        self._send_json(404, {"error": "Only /v1/chat/completions is supported"})

    def do_POST(self):
        if self.path not in ("/v1/chat/completions", "/api/chat"):
            self._send_json(404, {"error": "Path not supported. Use /v1/chat/completions"})
            return

        content_length = int(self.headers.get("Content-Length", 0))
        if content_length == 0:
            self._send_json(400, {"error": "Empty body"})
            return

        body = self.rfile.read(content_length)

        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            self._send_json(400, {"error": "Invalid JSON"})
            return

        # Estimation tokens input
        messages = payload.get("messages", [])
        prompt_text = " ".join(m.get("content", "") for m in messages)
        req_tokens = estimate_tokens(prompt_text)

        # Forward vers le LLM cible
        config = load_config()
        target_url = config.get("endpoint", "http://localhost:11434/v1/chat/completions")
        api_key = config.get("api_key", "")

        # Conversion OpenAI → Ollama natif si nécessaire
        is_ollama_native = "ollama.com" in target_url or "/api/chat" in target_url
        if is_ollama_native:
            ollama_payload = openai_to_ollama(payload)
            forward_body = json.dumps(ollama_payload).encode()
        else:
            forward_body = body

        status, resp_body, latency = forward_request(target_url, api_key, forward_body, dict(self.headers))

        # Estimation tokens output + conversion inverse
        resp_text = ""
        prompt_eval = req_tokens
        eval_count = 0
        try:
            resp_json = json.loads(resp_body)
            if is_ollama_native and "message" in resp_json:
                # Format Ollama natif → OpenAI
                prompt_eval = resp_json.get("prompt_eval_count", req_tokens)
                eval_count = resp_json.get("eval_count", 0)
                resp_text = resp_json.get("message", {}).get("content", "")
                # Convertir la réponse pour le client
                openai_resp = ollama_to_openai(resp_json, req_tokens)
                resp_body = json.dumps(openai_resp).encode()
                status = 200
            elif "choices" in resp_json:
                resp_text = resp_json["choices"][0].get("message", {}).get("content", "")
                prompt_eval = resp_json.get("usage", {}).get("prompt_tokens", req_tokens)
                eval_count = resp_json.get("usage", {}).get("completion_tokens", 0)
            elif "message" in resp_json:
                resp_text = resp_json["message"].get("content", "")
            elif "response" in resp_json:
                resp_text = resp_json.get("response", "")
        except Exception:
            resp_text = resp_body.decode(errors="ignore")

        resp_tokens = eval_count if eval_count else estimate_tokens(resp_text)

        # Mise à jour usage
        usage = update_usage(prompt_eval, resp_tokens)
        window_calls = usage.get("window_5h_calls", 0)
        window_limit = load_json(CONFIG_FILE).get("window_5h_limit", 0)
        window_pct = window_calls / window_limit * 100 if window_limit else 0
        weekly = usage.get("weekly_calls", 0)
        weekly_limit = load_json(CONFIG_FILE).get("weekly_limit", 0)
        weekly_pct = weekly / weekly_limit * 100 if weekly_limit else 0

        print(
            f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] "
            f"LLM call tracked — in:{prompt_eval} out:{resp_tokens} "
            f"5h:{window_calls}/{window_limit} ({window_pct:.0f}%) "
            f"week:{weekly}/{weekly_limit} ({weekly_pct:.0f}%) "
            f"latency:{latency:.2f}s",
            flush=True,
        )

        # Retourne la réponse au client
        self.send_response(status)
        for h in ("Content-Type", "Cache-Control"):
            v = self.headers.get(h)
            if v:
                self.send_header(h, v)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("X-Proxy-Latency", f"{latency:.3f}")
        self.send_header("X-Usage-Window5h", str(window_calls))
        self.send_header("X-Usage-Limit5h", str(window_limit))
        self.send_header("X-Usage-Weekly", str(weekly))
        self.send_header("X-Usage-LimitWeekly", str(weekly_limit))
        self.end_headers()
        self.wfile.write(resp_body)


# ─────────────────────────── Daemon ───────────────────────────

def is_proxy_running() -> bool:
    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text().strip())
            os.kill(pid, 0)
            return True
        except (ProcessLookupError, ValueError, OSError):
            PID_FILE.unlink(missing_ok=True)
    return False


def start_daemon(config: dict):
    if is_proxy_running():
        print("[llm_proxy] Déjà en cours (voir --status)")
        sys.exit(0)

    port = config.get("proxy_port", 11435)
    server = HTTPServer(("127.0.0.1", port), ProxyHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    PID_FILE.write_text(str(os.getpid()))
    print(f"[llm_proxy] Proxy démarré sur http://127.0.0.1:{port}")
    print(f"[llm_proxy] Target: {config.get('endpoint')}")
    print(f"[llm_proxy] Usage file: {USAGE_FILE}")
    print("[llm_proxy] Ctrl+C pour arrêter")

    def shutdown(signum, frame):
        print("\n[llm_proxy] Arrêt...")
        server.shutdown()
        PID_FILE.unlink(missing_ok=True)
        sys.exit(0)

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        shutdown(None, None)


def stop_proxy():
    if not PID_FILE.exists():
        print("[llm_proxy] Pas de PID file — le proxy ne tourne probablement pas.")
        return
    try:
        pid = int(PID_FILE.read_text().strip())
        os.kill(pid, signal.SIGTERM)
        PID_FILE.unlink(missing_ok=True)
        print(f"[llm_proxy] Signal d'arrêt envoyé au PID {pid}")
    except ProcessLookupError:
        PID_FILE.unlink(missing_ok=True)
        print("[llm_proxy] PID mort — nettoyage effectué.")
    except Exception as e:
        print(f"[llm_proxy] Erreur arrêt: {e}")


def status_proxy():
    if is_proxy_running():
        pid = int(PID_FILE.read_text().strip())
        config = load_config()
        print(f"[llm_proxy] ✅ Actif (PID {pid}) sur port {config.get('proxy_port', 11435)}")
        print(f"[llm_proxy] Target: {config.get('endpoint')}")
        try:
            req = urllib.request.Request(f"http://127.0.0.1:{config.get('proxy_port', 11435)}/health")
            with urllib.request.urlopen(req, timeout=2) as resp:
                print(f"[llm_proxy] Healthcheck: {resp.read().decode()}")
        except Exception as e:
            print(f"[llm_proxy] ⚠️  Healthcheck échoué: {e}")
    else:
        print("[llm_proxy] ❌ Inactif")


def main():
    parser = argparse.ArgumentParser(description="LLM Proxy avec tracking d'usage")
    parser.add_argument("--stop", action="store_true", help="Arrêter le proxy")
    parser.add_argument("--status", action="store_true", help="Vérifier le statut")
    parser.add_argument("--daemon", action="store_true", help="Mode daemon (background)")
    args = parser.parse_args()

    if args.stop:
        stop_proxy()
        return

    if args.status:
        status_proxy()
        return

    config = load_config()

    if args.daemon:
        # Fork en background
        pid = os.fork()
        if pid > 0:
            print(f"[llm_proxy] Daemon lancé (PID {pid})")
            sys.exit(0)
        os.setsid()
        # Redirige stdout/stderr vers log
        log_file = open(BASE_DIR / "logs" / "llm_proxy.log", "a")
        os.dup2(log_file.fileno(), sys.stdout.fileno())
        os.dup2(log_file.fileno(), sys.stderr.fileno())
        log_file.close()

    start_daemon(config)


if __name__ == "__main__":
    main()

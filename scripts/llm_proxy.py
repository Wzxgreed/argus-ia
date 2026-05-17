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


def load_config() -> dict:
    """Charge config depuis env puis JSON."""
    config = load_json(CONFIG_FILE)
    config.setdefault("endpoint", os.getenv("LLM_TARGET_URL", "http://localhost:11434/v1/chat/completions"))
    config.setdefault("api_key", os.getenv("LLM_API_KEY", ""))
    config.setdefault("proxy_port", int(os.getenv("LLM_PROXY_PORT", "11435")))
    return config


def estimate_tokens(text: str) -> int:
    """Estimation rapide : ~4 caractères/token (moyenne anglais)."""
    return max(len(text) // 4, 1)


def update_usage(req_tokens: int, resp_tokens: int, calls: int = 1):
    """Incrémente le compteur d'usage Ollama localement."""
    usage = load_json(USAGE_FILE)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Reset journalier si changement de date
    if usage.get("date") != today:
        usage["daily_calls"] = 0
        usage["daily_tokens_input"] = 0
        usage["daily_tokens_output"] = 0
        usage["date"] = today

    usage["daily_calls"] = usage.get("daily_calls", 0) + calls
    usage["daily_tokens_input"] = usage.get("daily_tokens_input", 0) + req_tokens
    usage["daily_tokens_output"] = usage.get("daily_tokens_output", 0) + resp_tokens
    usage["monthly_calls"] = usage.get("monthly_calls", 0) + calls
    usage["monthly_tokens_input"] = usage.get("monthly_tokens_input", 0) + req_tokens
    usage["monthly_tokens_output"] = usage.get("monthly_tokens_output", 0) + resp_tokens

    save_json(USAGE_FILE, usage)

    # Sync vers frontend/dist/data/ pour le dashboard
    dist_file = BASE_DIR / "frontend" / "dist" / "data" / "ollama_usage.json"
    if dist_file.parent.exists():
        save_json(dist_file, usage)

    return usage


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

        status, resp_body, latency = forward_request(target_url, api_key, body, dict(self.headers))

        # Estimation tokens output
        resp_text = ""
        try:
            resp_json = json.loads(resp_body)
            choices = resp_json.get("choices", [])
            if choices:
                resp_text = choices[0].get("message", {}).get("content", "")
            elif "message" in resp_json:
                resp_text = resp_json["message"].get("content", "")
            elif "response" in resp_json:
                # Format Ollama natif
                resp_text = resp_json.get("response", "")
        except Exception:
            resp_text = resp_body.decode(errors="ignore")

        resp_tokens = estimate_tokens(resp_text)

        # Mise à jour usage
        usage = update_usage(req_tokens, resp_tokens)
        daily = usage.get("daily_calls", 0)
        limit = load_json(CONFIG_FILE).get("daily_limit", 0)
        pct = daily / limit * 100 if limit else 0

        print(
            f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] "
            f"LLM call tracked — in:{req_tokens} out:{resp_tokens} "
            f"daily:{daily}/{limit} ({pct:.0f}%) "
            f"latency:{latency:.2f}s",
            flush=True,
        )

        # Retourne la réponse au client
        self.send_response(status)
        for h in ("Content-Type", "Content-Length", "Cache-Control"):
            v = self.headers.get(h)
            if v:
                self.send_header(h, v)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("X-Proxy-Latency", f"{latency:.3f}")
        self.send_header("X-Usage-Daily", str(daily))
        self.send_header("X-Usage-Limit", str(limit))
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

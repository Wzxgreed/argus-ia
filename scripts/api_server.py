#!/usr/bin/env python3
"""
api_server.py — Petit serveur HTTP pour lancer des analyses depuis le dashboard.
Écoute sur localhost:5000, nginx proxifie /api/ vers lui.

Routes :
  POST /api/analyse?ticker=XXX  → Lance scripts/analyse_ticker.sh
  GET  /api/status/<job_id>     → Retourne le statut et les logs
"""
import json
import os
import subprocess
import sys
import threading
import uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BASE_DIR = Path(__file__).resolve().parent.parent

# Charge .env.local pour FMP_API_KEY et autres secrets
_dotenv = BASE_DIR / ".env.local"
if _dotenv.exists():
    for line in _dotenv.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        os.environ.setdefault(key.strip(), val.strip())

JOBS: dict[str, dict] = {}
JOBS_LOCK = threading.Lock()


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def _stream_process(job_id: str, process: subprocess.Popen, logs: list):
    """Lit les logs d'un process en temps réel."""
    for line in process.stdout:  # type: ignore
        line = line.rstrip("\n")
        logs.append(f"[{now_str()}] {line}")
        with JOBS_LOCK:
            JOBS[job_id]["logs"] = logs.copy()


def run_job(job_id: str, ticker: str, name: str = "", sector: str = "", priority: str = "medium", exchange: str = "NASDAQ"):
    """Exécute le fetch des données dans un thread séparé."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR / "agents") + ":" + str(BASE_DIR / "scripts") + ":" + str(BASE_DIR)

    cmd = ["bash", str(BASE_DIR / "scripts" / "analyse_ticker.sh"), ticker]
    if name:
        cmd.append(name)
    if sector:
        cmd.extend([sector, priority, exchange])

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=BASE_DIR,
        env=env,
    )

    with JOBS_LOCK:
        JOBS[job_id]["pid"] = process.pid
        JOBS[job_id]["status"] = "running"

    logs = JOBS[job_id].get("logs", [])
    _stream_process(job_id, process, logs)

    returncode = process.wait()

    with JOBS_LOCK:
        JOBS[job_id]["status"] = "success" if returncode == 0 else "failed"
        JOBS[job_id]["returncode"] = returncode
        JOBS[job_id]["finished_at"] = now_str()


def run_full_analysis(job_id: str, ticker: str, name: str = "", sector: str = "", priority: str = "medium", exchange: str = "NASDAQ"):
    """Exécute l'analyse complète : fetch + génération LLM."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR / "agents") + ":" + str(BASE_DIR / "scripts") + ":" + str(BASE_DIR)
    env["LLM_PROXY_URL"] = "http://127.0.0.1:11435/v1/chat/completions"

    logs = JOBS[job_id].get("logs", [])

    # ── Étape 1 : Fetch données ──
    with JOBS_LOCK:
        JOBS[job_id]["status"] = "running"
        logs.append(f"[{now_str()}] 📡 Étape 1/2 — Fetch des données pour {ticker}...")
        JOBS[job_id]["logs"] = logs.copy()

    cmd1 = ["bash", str(BASE_DIR / "scripts" / "analyse_ticker.sh"), ticker]
    if name:
        cmd1.append(name)
    if sector:
        cmd1.extend([sector, priority, exchange])

    process1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=BASE_DIR, env=env)
    _stream_process(job_id, process1, logs)
    rc1 = process1.wait()

    if rc1 != 0:
        with JOBS_LOCK:
            logs.append(f"[{now_str()}] ❌ Échec du fetch (code {rc1})")
            JOBS[job_id]["status"] = "failed"
            JOBS[job_id]["returncode"] = rc1
            JOBS[job_id]["finished_at"] = now_str()
        return

    # ── Étape 2 : Compilation agents réels + LLM unique ──
    with JOBS_LOCK:
        logs.append(f"[{now_str()}] 🧠 Étape 2/2 — Compilation agents réels + LLM unique pour {ticker}...")
        JOBS[job_id]["logs"] = logs.copy()

    cmd2 = ["python3", str(BASE_DIR / "scripts" / "compile_report.py"), ticker]
    process2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=BASE_DIR, env=env)
    _stream_process(job_id, process2, logs)
    rc2 = process2.wait()

    with JOBS_LOCK:
        if rc2 == 0:
            logs.append(f"[{now_str()}] ✅ Rapport compilé (agents réels + LLM) — rapport dans Actions/{ticker}/")
            JOBS[job_id]["status"] = "success"
        else:
            logs.append(f"[{now_str()}] ❌ Échec de la compilation du rapport (code {rc2})")
            JOBS[job_id]["status"] = "failed"
        JOBS[job_id]["returncode"] = rc2
        JOBS[job_id]["finished_at"] = now_str()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # réduit le bruit

    def _send_json(self, status: int, body: dict):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/health":
            self._send_json(200, {"status": "ok", "service": "api_server"})
            return

        if path.startswith("/api/status/"):
            job_id = path.split("/")[-1]
            with JOBS_LOCK:
                job = JOBS.get(job_id)
            if not job:
                self._send_json(404, {"error": "Job not found"})
                return
            self._send_json(200, {
                "job_id": job_id,
                "ticker": job["ticker"],
                "status": job["status"],
                "started_at": job["started_at"],
                "finished_at": job.get("finished_at"),
                "returncode": job.get("returncode"),
                "logs": job["logs"][-200:],  # derniers 200 logs
            })
            return

        self._send_json(404, {"error": "Not found"})

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/api/analyse":
            ticker = query.get("ticker", [""])[0].upper().strip()
            if not ticker or len(ticker) < 1 or len(ticker) > 10:
                self._send_json(400, {"error": "Invalid ticker"})
                return

            name = query.get("name", [""])[0].strip()
            sector = query.get("sector", [""])[0].strip()
            priority = query.get("priority", ["medium"])[0].strip()
            exchange = query.get("exchange", ["NASDAQ"])[0].strip()

            job_id = str(uuid.uuid4())[:8]
            with JOBS_LOCK:
                JOBS[job_id] = {
                    "ticker": ticker,
                    "status": "queued",
                    "started_at": now_str(),
                    "logs": [f"[{now_str()}] 🚀 Démarrage de l'analyse pour {ticker}..."],
                }

            thread = threading.Thread(
                target=run_job,
                args=(job_id, ticker, name, sector, priority, exchange),
                daemon=True,
            )
            thread.start()

            self._send_json(202, {
                "job_id": job_id,
                "ticker": ticker,
                "status": "queued",
                "message": f"Analyse de {ticker} lancée. Suivez le statut avec /api/status/{job_id}",
            })
            return

        if path == "/api/analyse-complete":
            ticker = query.get("ticker", [""])[0].upper().strip()
            if not ticker or len(ticker) < 1 or len(ticker) > 10:
                self._send_json(400, {"error": "Invalid ticker"})
                return

            name = query.get("name", [""])[0].strip()
            sector = query.get("sector", [""])[0].strip()
            priority = query.get("priority", ["medium"])[0].strip()
            exchange = query.get("exchange", ["NASDAQ"])[0].strip()

            job_id = str(uuid.uuid4())[:8]
            with JOBS_LOCK:
                JOBS[job_id] = {
                    "ticker": ticker,
                    "status": "queued",
                    "started_at": now_str(),
                    "logs": [f"[{now_str()}] 🚀 Démarrage de l'analyse COMPLÈTE pour {ticker} (fetch + LLM)..."],
                }

            thread = threading.Thread(
                target=run_full_analysis,
                args=(job_id, ticker, name, sector, priority, exchange),
                daemon=True,
            )
            thread.start()

            self._send_json(202, {
                "job_id": job_id,
                "ticker": ticker,
                "status": "queued",
                "message": f"Analyse complète de {ticker} lancée (fetch + LLM). Suivez le statut avec /api/status/{job_id}",
            })
            return

        self._send_json(404, {"error": "Not found"})


def main():
    port = int(os.environ.get("API_SERVER_PORT", "5000"))
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"[api_server] Listening on http://127.0.0.1:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[api_server] Arrêt...")
        server.shutdown()


if __name__ == "__main__":
    main()

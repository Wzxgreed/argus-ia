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
import time
import uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BASE_DIR = Path(__file__).resolve().parent.parent
PYTHON = str(BASE_DIR / "venv" / "bin" / "python3")

# Import ask_llm via proxy Ollama
sys.path.insert(0, str(BASE_DIR / "scripts"))
from ask_llm import ask_llm

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

    cmd2 = [PYTHON, str(BASE_DIR / "scripts" / "compile_report.py"), ticker]
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


def _clean_ticker(raw: str) -> str:
    """Extrait le ticker d'une chaîne utilisateur (ex: 'ANALYSE RKLB' → 'RKLB')."""
    raw = raw.upper().strip()
    # Supprime les mots parasites courants
    parasites = {"ANALYSE", "ANALYSIS", "FETCH", "GET", "TICKER", "STOCK", "ACTION", "PRICE"}
    tokens = raw.split()
    candidates = [t for t in tokens if t not in parasites and t.isalnum() and 1 <= len(t) <= 8]
    if candidates:
        return candidates[0]
    # Fallback : prend le premier token alphanumérique majuscule trouvé
    import re
    m = re.search(r"[A-Z]{1,8}", raw)
    return m.group(0) if m else raw[:8]


def _load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def _build_data_context(ticker: str, data: dict) -> str:
    """Construit le contexte de données brutes pour le prompt LLM."""
    price = data.get("price", {})
    tech = data.get("technical", {})
    fund = data.get("fundamentals", {})
    options = data.get("options", {})
    macro = data.get("macro", {})
    def _fmt(val, prefix: str = "", suffix: str = "", default: str = "N/A") -> str:
        if val is None:
            return f"{prefix}{default}{suffix}"
        if isinstance(val, (int, float)):
            if isinstance(val, float) and val == int(val):
                return f"{prefix}{int(val):,}{suffix}"
            return f"{prefix}{val:,.2f}{suffix}" if isinstance(val, float) else f"{prefix}{val:,}{suffix}"
        return f"{prefix}{val}{suffix}"
    lines = [
        f"## DONNÉES BRUTES POUR {ticker}", "",
        "**Cours :**",
        f"- Close : {_fmt(price.get('close'), '$')}",
        f"- Change % : {_fmt(price.get('change_pct'), suffix='%')}",
        f"- Volume : {_fmt(price.get('volume'))}",
        "",
        "**Technique :**",
        f"- RSI 14j : {_fmt(tech.get('rsi14'))}",
        f"- ATR 14j : {_fmt(tech.get('atr14'), '$')}",
        f"- MM 50j : {_fmt(tech.get('mm50'), '$')}",
        f"- MM 200j : {_fmt(tech.get('mm200'), '$')}",
        "",
        "**Fondamentaux :**",
        f"- Market Cap : {_fmt(fund.get('market_cap'), '$')}",
        f"- Secteur : {fund.get('sector', 'N/A')}",
        f"- P/E : {_fmt(fund.get('pe_ratio'))}",
        f"- Forward P/E : {_fmt(fund.get('forward_pe'))}",
        f"- Beta : {_fmt(fund.get('beta'))}",
        "",
        "**Options :**",
        f"- Max Pain : {_fmt(options.get('max_pain'), '$')}",
        f"- Put/Call Ratio : {_fmt(options.get('put_call_ratio'))}",
        "",
        "**Macro :**",
        f"- VIX : {_fmt(macro.get('vix'))}",
        f"- DXY : {_fmt(macro.get('dxy'))}",
    ]
    return "\n".join(lines)


def _load_agent_data(ticker: str) -> dict:
    """Charge les données des agents Python réels pour ce ticker."""
    result = {}
    DATA_DIR = BASE_DIR / "data"
    rec = _load_json(DATA_DIR / "recommandations_latest.json")
    for r in rec.get("recommandations", []):
        if r.get("ticker") == ticker:
            result["recommandation"] = r
            break
    acc = _load_json(DATA_DIR / "accounting_risk_latest.json")
    result["accounting"] = acc.get("analysis", {}).get(ticker)
    geo = _load_json(DATA_DIR / "geo_risk_latest.json")
    result["geo"] = geo.get("ticker_exposure", {}).get(ticker)
    crypto = _load_json(DATA_DIR / "crypto_correlation_latest.json")
    result["crypto"] = crypto.get("analysis", {}).get(ticker)
    sr = _load_json(DATA_DIR / "sector_rotation_latest.json")
    for s in sr.get("ranking", []):
        if s.get("ticker") == ticker:
            result["sector_rotation"] = s
            break
    social = _load_json(DATA_DIR / "social_sentiment_latest.json")
    result["social"] = social.get("analysis", {}).get(ticker)
    fx = _load_json(DATA_DIR / "fx_exposure_latest.json")
    for f in fx.get("tickers", []):
        if f.get("ticker") == ticker:
            result["fx"] = f
            break
    ev = _load_json(DATA_DIR / "events_latest.json")
    result["events"] = ev.get("ticker_events", {}).get(ticker, [])
    ue = _load_json(DATA_DIR / "upcoming_events_latest.json")
    result["upcoming"] = [e for e in ue.get("events", []) if e.get("ticker") == ticker]
    qg = _load_json(DATA_DIR / "quality_report_latest.json")
    result["quality"] = qg.get("tickers", {}).get(ticker)
    quant = _load_json(DATA_DIR / "quant_report_latest.json")
    result["quant"] = quant
    return result


def _format_agent_context(ticker: str, agent_data: dict) -> str:
    lines = [f"## DONNÉES AGENTS POUR {ticker}", ""]
    rec = agent_data.get("recommandation")
    if rec:
        lines.extend([
            "**Agent Recommandation :**",
            f"- Action : {rec.get('action', 'N/A')} | Direction : {rec.get('direction', 'N/A')}",
            f"- Score Global : {rec.get('score_global_ajuste', rec.get('score_global', 'N/A'))}/100",
            f"- Score Opportunité : {rec.get('score_opportunite', 'N/A')}/10",
            f"- Prix actuel : ${rec.get('prix_actuel', 'N/A')}",
            f"- Stop-loss : ${rec.get('stop_loss', 'N/A')}",
            f"- Take-profit : ${rec.get('take_profit', 'N/A')}",
            f"- Ratio R/R : {rec.get('risque_rendement_ratio', 'N/A')}",
        ])
        lines.append("")
    acc = agent_data.get("accounting")
    if acc:
        lines.append("**Agent Accounting :**")
        lines.append(f"- Risk Level : {acc.get('risk_level', 'N/A')}")
        lines.append("")
    geo = agent_data.get("geo")
    if geo:
        lines.append("**Agent Géopolitique :**")
        lines.append(f"- Geo Risk Score : {geo.get('geo_risk_score', 'N/A')}/10")
        lines.append("")
    if len(lines) == 2:
        lines.append("*Aucune donnée agent disponible pour ce ticker.*")
    return "\n".join(lines)


def _save_report(ticker: str, report: str, agent_data: dict):
    """Sauvegarde le rapport et met à jour INDEX.md / CONTEXT.md."""
    ACTIONS_DIR = BASE_DIR / "Actions"
    ticker_dir = ACTIONS_DIR / ticker
    ticker_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    filename = f"{ticker}_{today}_claude.md"
    filepath = ticker_dir / filename
    filepath.write_text(report, encoding="utf-8")

    # INDEX.md
    index_path = ticker_dir / "INDEX.md"
    if not index_path.exists():
        index_path.write_text(f"""# {ticker}

## Thèse courante
[Rapport généré le {today}]

## Historique
| Date | Fichier | Type |
|------|---------|------|
| {today} | [{filename}]({filename}) | Analyse approfondie (LLM) |

## Agenda
- Prochain earnings : [à compléter]

## Alertes actives
- Aucune
""", encoding="utf-8")
    else:
        text = index_path.read_text(encoding="utf-8")
        if "| Date | Fichier | Type |" in text:
            text = text.replace("| Date | Fichier | Type |", f"| Date | Fichier | Type |\n| {today} | [{filename}]({filename}) | Analyse approfondie (LLM) |")
        index_path.write_text(text, encoding="utf-8")

    # CONTEXT.md
    ctx_path = ticker_dir / "CONTEXT.md"
    rec = agent_data.get("recommandation", {})
    ctx_path.write_text(f"""# Contexte {ticker}

## Thèse active
[Rapport généré le {today}]

## Score actuel
- Opportunité : {rec.get('score_opportunite', 'N/A')}/10
- Valorisation : {rec.get('score_valorisation', 'N/A')}/10
- Momentum : {rec.get('score_momentum', 'N/A')}/10

## Niveaux
- SL : {rec.get('stop_loss', '[voir rapport]')}
- TP : {rec.get('take_profit', '[voir rapport]')}

## Statut
[ACTIVE / EN SURVEILLANCE / CLOS]
""", encoding="utf-8")
    return str(filepath)


def run_prepare_for_claude(job_id: str, ticker: str, custom_prompt: str = ""):
    """Prépare les données (fetch + agents) pour une analyse par Claude CLI.
    L'analyse LLM interactive est faite par l'utilisateur dans Claude CLI, pas ici."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR / "agents") + ":" + str(BASE_DIR / "scripts") + ":" + str(BASE_DIR)

    logs = JOBS[job_id].get("logs", [])

    # ── Étape 1 : Fetch données ──
    with JOBS_LOCK:
        JOBS[job_id]["status"] = "running"
        logs.append(f"[{now_str()}] 📡 Étape 1/2 — Fetch des données pour {ticker}...")
        JOBS[job_id]["logs"] = logs.copy()

    cmd1 = ["bash", str(BASE_DIR / "scripts" / "analyse_ticker.sh"), ticker]
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

    logs.append(f"[{now_str()}] ✅ Fetch terminé — {ticker} dans data/latest.json")

    # ── Étape 2 : Lancer les agents réels ──
    with JOBS_LOCK:
        logs.append(f"[{now_str()}] 🔧 Étape 2/2 — Exécution des agents Python réels...")
        JOBS[job_id]["logs"] = logs.copy()

    agents = ["accounting", "geo", "crypto", "sector_rotation", "social", "fx", "event_driven", "watchman", "detect_major_events", "recommandation"]
    ok_count = 0
    for agent in agents:
        lockfile = BASE_DIR / "data" / ".pipeline.lock"
        for _ in range(5):
            if not lockfile.exists():
                break
            try:
                data = json.loads(lockfile.read_text())
                old_pid = data.get("pid")
                if old_pid:
                    os.kill(old_pid, 0)
                    time.sleep(2)
                    continue
            except (ProcessLookupError, ValueError, OSError):
                pass
            lockfile.unlink(missing_ok=True)
            break
        else:
            lockfile.unlink(missing_ok=True)

        cmd_agent = [PYTHON, str(BASE_DIR / "agents" / "orchestrator.py"), f"--agent={agent}"]
        proc = subprocess.Popen(cmd_agent, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=BASE_DIR, env=env)
        _stream_process(job_id, proc, logs)
        rc = proc.wait()
        if rc == 0:
            ok_count += 1
        else:
            logs.append(f"[{now_str()}] ⚠️  Agent {agent} exit={rc}")

    logs.append(f"[{now_str()}] ✅ Agents terminés — {ok_count}/{len(agents)} OK")

    # ── Étape 3 : Préparer le fichier de contexte pour Claude CLI ──
    latest = _load_json(BASE_DIR / "data" / "latest.json")
    ticker_data = latest.get("prices", {}).get(ticker, {})
    data_ctx = _build_data_context(ticker, ticker_data)
    agent_data = _load_agent_data(ticker)
    agent_ctx = _format_agent_context(ticker, agent_data)

    # Écrire un fichier de requête que Claude CLI peut lire
    request_file = BASE_DIR / ".claude" / "analysis_requests" / f"{ticker}_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.json"
    request_file.parent.mkdir(parents=True, exist_ok=True)
    request_payload = {
        "ticker": ticker,
        "date": datetime.now(timezone.utc).isoformat(),
        "status": "ready",
        "custom_prompt": custom_prompt.strip(),
        "data_summary": data_ctx,
        "agent_summary": agent_ctx,
        "files_to_read": [
            "data/latest.json",
            "data/recommandations_latest.json",
            "data/quant_report_latest.json",
            "data/accounting_risk_latest.json",
            "data/geo_risk_latest.json",
            "data/sector_rotation_latest.json",
            "data/social_sentiment_latest.json",
            "data/fx_exposure_latest.json",
            "data/upcoming_events_latest.json",
        ],
        "instructions": f"L'utilisateur a demandé une analyse de {ticker}. Les données fraîches sont prêtes. Demande-lui 'Analyse {ticker}' pour que je produise l'analyse complète.",
    }
    request_file.write_text(json.dumps(request_payload, indent=2, ensure_ascii=False), encoding="utf-8")
    logs.append(f"[{now_str()}] ✅ Contexte préparé pour Claude CLI : {request_file}")

    # Sauvegarder aussi un fichier de note dans Actions/
    ACTIONS_DIR = BASE_DIR / "Actions"
    ticker_dir = ACTIONS_DIR / ticker
    ticker_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    note_file = ticker_dir / f"{ticker}_{today}_ready_for_claude.md"
    note_file.write_text(
        f"""# {ticker} — Données prêtes pour analyse Claude CLI ({today})

Les agents ont tourné et les données sont à jour.

## Pour lancer l'analyse
Dans Claude Code, demande : **Analyse {ticker}**

Claude lira automatiquement :
- `data/latest.json` (cours, technique, fondamentaux)
- `data/recommandations_latest.json` (scores agents)
- Tous les rapports agents récents
- L'historique dans `Actions/{ticker}/`

## Résumé données brutes

{data_ctx}

## Résumé agents

{agent_ctx}

---
*Ce fichier est un marqueur — l'analyse réelle sera produite par Claude CLI.*
""",
        encoding="utf-8",
    )
    logs.append(f"[{now_str()}] ✅ Note créée : {note_file}")
    logs.append(f"[{now_str()}] ⏳ ATTENTE — Ouvrez Claude Code et demandez 'Analyse {ticker}' pour obtenir l'analyse complète.")

    with JOBS_LOCK:
        JOBS[job_id]["status"] = "success"
        JOBS[job_id]["returncode"] = 0
        JOBS[job_id]["logs"] = logs.copy()
        JOBS[job_id]["finished_at"] = now_str()
        JOBS[job_id]["request_file"] = str(request_file)


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
            ticker = _clean_ticker(query.get("ticker", [""])[0])
            if not ticker or len(ticker) < 1 or len(ticker) > 20:
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
            ticker = _clean_ticker(query.get("ticker", [""])[0])
            if not ticker or len(ticker) < 1 or len(ticker) > 20:
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

        if path == "/api/analyse-claude":
            ticker = _clean_ticker(query.get("ticker", [""])[0])
            if not ticker or len(ticker) < 1 or len(ticker) > 20:
                self._send_json(400, {"error": "Invalid ticker"})
                return

            custom_prompt = query.get("prompt", [""])[0].strip()

            job_id = str(uuid.uuid4())[:8]
            with JOBS_LOCK:
                JOBS[job_id] = {
                    "ticker": ticker,
                    "status": "queued",
                    "started_at": now_str(),
                    "logs": [f"[{now_str()}] 🚀 Préparation des données pour {ticker} (fetch + agents réels) — l'analyse interactive se fera dans Claude CLI..."],
                }

            thread = threading.Thread(
                target=run_prepare_for_claude,
                args=(job_id, ticker, custom_prompt),
                daemon=True,
            )
            thread.start()

            self._send_json(202, {
                "job_id": job_id,
                "ticker": ticker,
                "status": "queued",
                "message": f"Préparation des données pour {ticker} lancée (fetch + agents réels). L'analyse interactive se fera dans Claude CLI. Suivez le statut avec /api/status/{job_id}",
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

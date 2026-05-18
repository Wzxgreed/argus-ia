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
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BASE_DIR = Path(__file__).resolve().parent.parent
PYTHON = str(BASE_DIR / "venv" / "bin" / "python3")
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"

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
    """Prépare les données (fetch + agents) et lance Claude CLI via Ollama (kimi-k2.6:cloud).
    Utilise `ollama launch claude --model kimi-k2.6:cloud -y -- -p ... --permission-mode auto --cwd ...`."""
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

    # ── Étape 2 : Lancer les agents réels (parallèle, max 5 workers) ──
    with JOBS_LOCK:
        logs.append(f"[{now_str()}] 🔧 Étape 2/2 — Exécution des agents Python réels (parallèle)...")
        JOBS[job_id]["logs"] = logs.copy()

    agents = ["accounting", "geo", "crypto", "sector_rotation", "social", "fx", "event_driven", "watchman", "detect_major_events", "recommandation"]
    ok_count = 0

    def _run_one_agent(agent: str) -> tuple[str, int]:
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
        return agent, rc

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(_run_one_agent, a): a for a in agents}
        for future in as_completed(futures):
            agent, rc = future.result()
            if rc == 0:
                ok_count += 1
            else:
                logs.append(f"[{now_str()}] ⚠️  Agent {agent} exit={rc}")

    logs.append(f"[{now_str()}] ✅ Agents terminés — {ok_count}/{len(agents)} OK")

    # ── Étape 3 : Lancer Claude CLI via Ollama (kimi-k2.6:cloud) ──
    with JOBS_LOCK:
        logs.append(f"[{now_str()}] 🤖 Étape 3/3 — Lancement Claude CLI via Ollama (kimi-k2.6:cloud) pour {ticker}...")
        JOBS[job_id]["logs"] = logs.copy()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ACTIONS_DIR = BASE_DIR / "Actions"
    ticker_dir = ACTIONS_DIR / ticker
    ticker_dir.mkdir(parents=True, exist_ok=True)
    report_file = ticker_dir / f"{ticker}_{today}_claude.md"

    claude_prompt = f"""Tu es l'analyste institutionnel senior du desk Argus-IA. Rédige une analyse approfondie pour **{ticker}**.

Protocole obligatoire :
1. Lis data/latest.json et extrait les données pour {ticker} (cours, RSI, ATR, MM50/200, fondamentaux, options)
2. Lis data/recommandations_latest.json pour les scores agents
3. Lis data/quant_report_latest.json, data/geo_risk_latest.json, data/accounting_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json pour enrichir l'analyse
4. Lis l'historique dans Actions/{ticker}/ (si le dossier existe)
5. Rédige le rapport dans Actions/{ticker}/{ticker}_{today}_claude.md avec cette structure institutionnelle :
   - Résumé Exécutif (3-4 phrases)
   - Market Researcher (TAM, peers, landscape)
   - Macro (régime, exposition, sensibilités)
   - Technique (RSI, MACD, MM, niveaux, timing)
   - Fondamental (Filtre Qualité 6 critères, valorisation)
   - Sentiment (consensus, options, insiders)
   - Flux Institutionnels (13F, ETF, dark pool)
   - Scoring Global (Catalyseur / Valorisation / Momentum)
   - Niveaux et Ratio R/R
   - Conclusion (ACHETER / ATTENDRE / SURVEILLER / ÉVITER)
6. Crée ou met à jour Actions/{ticker}/INDEX.md et Actions/{ticker}/CONTEXT.md avec la thèse courante, score, niveaux

Règles absolues :
- Utilise EXCLUSIVEMENT les chiffres des fichiers JSON
- Ne devine jamais un cours, un multiple ou une métrique
- Marque [DONNÉES MANQUANTES] si absent
- Format institutionnel JPM/GS/MS, concis et chiffré
- Ne mentionne pas que tu es un LLM

Instructions supplémentaires de l'utilisateur : {custom_prompt.strip() or "Aucune"}

Commence l'analyse maintenant."""

    claude_cmd = [
        "ollama", "launch", "claude",
        "--model", "kimi-k2.6:cloud",
        "-y",
        "--",
        "-p", claude_prompt,
        "--permission-mode", "auto",
    ]

    logs.append(f"[{now_str()}] 📤 Envoi du prompt à Claude CLI via Ollama ({len(claude_prompt)} caractères)...")
    with JOBS_LOCK:
        JOBS[job_id]["logs"] = logs.copy()

    try:
        claude_proc = subprocess.Popen(
            claude_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=str(BASE_DIR),
            env=env,
        )
        _stream_process(job_id, claude_proc, logs)
        claude_rc = claude_proc.wait(timeout=600)  # 10 min max

        if claude_rc != 0:
            logs.append(f"[{now_str()}] ⚠️ Claude CLI via Ollama exit={claude_rc}")

        # Vérifier si le rapport a été créé
        if report_file.exists():
            logs.append(f"[{now_str()}] ✅ Rapport Claude CLI (Ollama/kimi) sauvegardé : {report_file}")
        else:
            logs.append(f"[{now_str()}] ⚠️ Rapport non trouvé à l'emplacement attendu ({report_file})")

        logs.append(f"[{now_str()}] ✅ Analyse Claude CLI via Ollama terminée pour {ticker}")

        with JOBS_LOCK:
            JOBS[job_id]["status"] = "success"
            JOBS[job_id]["returncode"] = 0
            JOBS[job_id]["logs"] = logs.copy()
            JOBS[job_id]["finished_at"] = now_str()
            JOBS[job_id]["report_file"] = str(report_file)

    except subprocess.TimeoutExpired:
        claude_proc.kill()
        logs.append(f"[{now_str()}] ⏱ Claude CLI via Ollama timeout (10 min)")
        with JOBS_LOCK:
            JOBS[job_id]["status"] = "failed"
            JOBS[job_id]["returncode"] = -9
            JOBS[job_id]["logs"] = logs.copy()
            JOBS[job_id]["finished_at"] = now_str()
    except Exception as e:
        logs.append(f"[{now_str()}] ❌ Erreur Claude CLI via Ollama : {e}")
        with JOBS_LOCK:
            JOBS[job_id]["status"] = "failed"
            JOBS[job_id]["returncode"] = 1
            JOBS[job_id]["logs"] = logs.copy()
            JOBS[job_id]["finished_at"] = now_str()


def _run_claude_update(job_id: str, ticker: str, env: dict, today: str):
    """Lance Claude CLI via Ollama pour générer un _update.md pour un ticker."""
    logs = JOBS[job_id].get("logs", [])
    ACTIONS_DIR = BASE_DIR / "Actions"
    ticker_dir = ACTIONS_DIR / ticker
    report_file = ticker_dir / f"{ticker}_{today}_update.md"

    update_prompt = f"""Tu es l'analyste institutionnel senior du desk Argus-IA. Mets à jour l'analyse de **{ticker}**.

Protocole obligatoire :
1. Lis l'analyse précédente dans Actions/{ticker}/ (le fichier le plus récent)
2. Lis data/latest.json et extrait les nouvelles données pour {ticker}
3. Lis data/recommandations_latest.json pour les scores agents actualisés
4. Lis data/quant_report_latest.json, data/geo_risk_latest.json, data/accounting_risk_latest.json, data/sector_rotation_latest.json, data/social_sentiment_latest.json, data/fx_exposure_latest.json, data/upcoming_events_latest.json, data/events_latest.json
5. Compare avec l'analyse précédente : qu'est-ce qui a changé ? Cours, RSI, nouvelles, scores, alertes
6. Rédige le rapport dans Actions/{ticker}/{ticker}_{today}_update.md avec :
   - Résumé des changements depuis l'analyse précédente
   - Mise à jour technique (nouveaux niveaux, RSI, momentum)
   - Mise à jour fondamentale (si nouvelles données)
   - Mise à jour sentiment/options/news
   - Nouveau scoring global si les scores ont changé
   - Révision des niveaux SL/TP si nécessaire
   - Conclusion : la thèse est-elle confirmée, modifiée ou invalidée ?
7. Mets à jour Actions/{ticker}/INDEX.md avec la nouvelle thèse courante
8. Mets à jour Actions/{ticker}/CONTEXT.md

Règles absolues :
- Utilise EXCLUSIVEMENT les chiffres des fichiers JSON
- Compare explicitement avec les données de l'analyse précédente
- Mentionne tout changement significatif (cours ±5%, RSI franchi, news majeure)
- Format institutionnel JPM/GS/MS, concis et chiffré
- Ne mentionne pas que tu es un LLM

Commence la mise à jour maintenant."""

    claude_cmd = [
        "ollama", "launch", "claude",
        "--model", "kimi-k2.6:cloud",
        "-y",
        "--",
        "-p", update_prompt,
        "--permission-mode", "auto",
    ]

    logs.append(f"[{now_str()}] 📤 Mise à jour {ticker} — envoi prompt Claude CLI ({len(update_prompt)} caractères)...")
    with JOBS_LOCK:
        JOBS[job_id]["logs"] = logs.copy()

    try:
        claude_proc = subprocess.Popen(
            claude_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=str(BASE_DIR),
            env=env,
        )
        _stream_process(job_id, claude_proc, logs)
        claude_rc = claude_proc.wait(timeout=600)

        if claude_rc != 0:
            logs.append(f"[{now_str()}] ⚠️  Mise à jour {ticker} — exit={claude_rc}")
        elif report_file.exists():
            logs.append(f"[{now_str()}] ✅ Mise à jour {ticker} sauvegardée : {report_file}")
        else:
            logs.append(f"[{now_str()}] ⚠️  Mise à jour {ticker} — rapport non trouvé")

        with JOBS_LOCK:
            JOBS[job_id]["logs"] = logs.copy()

    except subprocess.TimeoutExpired:
        claude_proc.kill()
        logs.append(f"[{now_str()}] ⏱ Mise à jour {ticker} — timeout")
        with JOBS_LOCK:
            JOBS[job_id]["logs"] = logs.copy()
    except Exception as e:
        logs.append(f"[{now_str()}] ❌ Mise à jour {ticker} — erreur : {e}")
        with JOBS_LOCK:
            JOBS[job_id]["logs"] = logs.copy()


def _run_single_agent_api(agent: str, env: dict) -> tuple[str, int, str]:
    """Exécute un agent individuel. Retourne (agent_name, returncode, output)."""
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
    try:
        result = subprocess.run(
            cmd_agent,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=BASE_DIR,
            env=env,
            timeout=300,
        )
        return agent, result.returncode, result.stdout or ""
    except subprocess.TimeoutExpired:
        return agent, -9, "Timeout"
    except Exception as e:
        return agent, 1, str(e)


def run_update_all(job_id: str, custom_prompt: str = ""):
    """Met à jour les analyses de tous les tickers de la watchlist existants dans Actions/."""
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(BASE_DIR / "agents") + ":" + str(BASE_DIR / "scripts") + ":" + str(BASE_DIR)

        logs = JOBS[job_id].get("logs", [])

        # ── Lister les tickers à mettre à jour ──
        config = _load_json(CONFIG_PATH)
        all_tickers = [t["ticker"].upper() for t in config.get("tickers", [])]
        ACTIONS_DIR = BASE_DIR / "Actions"
        tickers_to_update = [t for t in all_tickers if (ACTIONS_DIR / t).exists()]

        if not tickers_to_update:
            logs.append(f"[{now_str()}] ⚠️  Aucun ticker à mettre à jour (pas de dossiers dans Actions/)")
            with JOBS_LOCK:
                JOBS[job_id]["status"] = "success"
                JOBS[job_id]["returncode"] = 0
                JOBS[job_id]["logs"] = logs.copy()
                JOBS[job_id]["finished_at"] = now_str()
            return

        logs.append(f"[{now_str()}] 📋 {len(tickers_to_update)} ticker(s) à mettre à jour : {', '.join(tickers_to_update)}")
        with JOBS_LOCK:
            JOBS[job_id]["logs"] = logs.copy()

        # ── Étape 1 : Fetch données ──
        with JOBS_LOCK:
            JOBS[job_id]["status"] = "running"
            logs.append(f"[{now_str()}] 📡 Étape 1/3 — Fetch des données pour toute la watchlist...")
            JOBS[job_id]["logs"] = logs.copy()

        cmd1 = ["bash", str(BASE_DIR / "scripts" / "analyse_ticker.sh"), tickers_to_update[0]]
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

        logs.append(f"[{now_str()}] ✅ Fetch terminé")

        # ── Étape 2 : Agents réels (parallèle, max 5) ──
        with JOBS_LOCK:
            logs.append(f"[{now_str()}] 🔧 Étape 2/3 — Exécution des agents Python réels (parallèle)...")
            JOBS[job_id]["logs"] = logs.copy()

        agents = ["accounting", "geo", "crypto", "sector_rotation", "social", "fx", "event_driven", "watchman", "detect_major_events", "recommandation"]
        ok_count = 0

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(_run_single_agent_api, a, env): a for a in agents}
            for future in as_completed(futures):
                agent, rc, out = future.result()
                if out:
                    for line in out.strip().splitlines()[-3:]:
                        logs.append(f"[{now_str()}]    {line}")
                if rc == 0:
                    ok_count += 1
                    logs.append(f"[{now_str()}]    ✅ {agent} ok")
                else:
                    logs.append(f"[{now_str()}]    ⚠️  {agent} exit={rc}")
                with JOBS_LOCK:
                    JOBS[job_id]["logs"] = logs.copy()

        logs.append(f"[{now_str()}] ✅ Agents terminés — {ok_count}/{len(agents)} OK")

        # ── Étape 3 : Mises à jour Claude CLI via Ollama (parallèle, max 3) ──
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        with JOBS_LOCK:
            logs.append(f"[{now_str()}] 🤖 Étape 3/3 — Mise à jour {len(tickers_to_update)} analyse(s) via Claude CLI (Ollama/kimi)...")
            JOBS[job_id]["logs"] = logs.copy()

        completed = 0
        failed = 0
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {executor.submit(_run_claude_update, job_id, t, env, today): t for t in tickers_to_update}
            for future in as_completed(futures):
                ticker = futures[future]
                try:
                    future.result()
                    completed += 1
                except Exception as e:
                    logs.append(f"[{now_str()}] ❌ Exception mise à jour {ticker} : {e}")
                    failed += 1
                    with JOBS_LOCK:
                        JOBS[job_id]["logs"] = logs.copy()

        logs.append(f"[{now_str()}] ✅ Mises à jour terminées — {completed} OK, {failed} échec(s)")

        with JOBS_LOCK:
            JOBS[job_id]["status"] = "success" if failed == 0 else "failed"
            JOBS[job_id]["returncode"] = 0 if failed == 0 else 1
            JOBS[job_id]["logs"] = logs.copy()
            JOBS[job_id]["finished_at"] = now_str()
    except Exception as e:
        import traceback
        err = f"[{now_str()}] 💥 Erreur critique dans run_update_all : {e}\n{traceback.format_exc()}"
        logs.append(err)
        with JOBS_LOCK:
            JOBS[job_id]["status"] = "failed"
            JOBS[job_id]["returncode"] = 1
            JOBS[job_id]["logs"] = logs.copy()
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
                    "logs": [f"[{now_str()}] 🚀 Préparation des données pour {ticker} (fetch + agents réels + Claude CLI via Ollama)..."],
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
                "message": f"Préparation des données pour {ticker} lancée (fetch + agents réels + Claude CLI via Ollama). Suivez le statut avec /api/status/{job_id}",
            })
            return

        if path == "/api/analyse-update-all":
            custom_prompt = query.get("prompt", [""])[0].strip()

            job_id = str(uuid.uuid4())[:8]
            with JOBS_LOCK:
                JOBS[job_id] = {
                    "ticker": "UPDATE_ALL",
                    "status": "queued",
                    "started_at": now_str(),
                    "logs": [f"[{now_str()}] 🚀 Mise à jour automatique de toutes les analyses (fetch + agents + Claude CLI via Ollama)..."],
                }

            thread = threading.Thread(
                target=run_update_all,
                args=(job_id, custom_prompt),
                daemon=True,
            )
            thread.start()

            self._send_json(202, {
                "job_id": job_id,
                "ticker": "UPDATE_ALL",
                "status": "queued",
                "message": f"Mise à jour de toutes les analyses lancée. Suivez le statut avec /api/status/{job_id}",
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

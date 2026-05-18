#!/usr/bin/env python3
"""
run_update_all.py — Met à jour automatiquement toutes les analyses de la watchlist.
Fetch une fois + agents une fois + Claude CLI via Ollama (kimi-k2.6:cloud) par ticker.

Usage:
    python3 scripts/run_update_all.py [--prompt="instructions custom"]
    # ou via cron : 0 10 * * * bash /home/argus/argus-ia/scripts/run_update_all_cron.sh

Output:
    Actions/[TICKER]/[TICKER]_YYYY-MM-DD_update.md pour chaque ticker existant
"""
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PYTHON = str(BASE_DIR / "venv" / "bin" / "python3")
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
ACTIONS_DIR = BASE_DIR / "Actions"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(BASE_DIR / "scripts"))


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def log(msg: str):
    line = f"[{now_str()}] {msg}"
    print(line, flush=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_file = LOG_DIR / f"{today}_update_all.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def run_cmd(cmd: list, cwd=None, env=None, timeout=300) -> tuple[int, str]:
    """Exécute une commande, retourne (returncode, stdout)."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd or str(BASE_DIR),
            env=env or os.environ.copy(),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.returncode, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return -9, "Timeout"
    except Exception as e:
        return 1, str(e)


def wait_for_pipeline_lock(max_wait=60):
    """Attend que le lockfile du pipeline matinal soit libre."""
    lockfile = BASE_DIR / "data" / ".pipeline.lock"
    waited = 0
    while lockfile.exists() and waited < max_wait:
        try:
            data = json.loads(lockfile.read_text())
            old_pid = data.get("pid")
            if old_pid:
                os.kill(old_pid, 0)
                log(f"⏳ Pipeline lock actif (PID {old_pid}), attente...")
                time.sleep(5)
                waited += 5
                continue
        except (ProcessLookupError, ValueError, OSError):
            pass
        lockfile.unlink(missing_ok=True)
        break
    if waited >= max_wait:
        log("⚠️ Lockfile toujours actif après 60s — tentative de suppression")
        lockfile.unlink(missing_ok=True)


def acquire_update_lock() -> bool:
    """Crée un lockfile pour éviter les doublons de run_update_all."""
    lockfile = BASE_DIR / "data" / ".update_all.lock"
    if lockfile.exists():
        try:
            data = json.loads(lockfile.read_text())
            old_pid = data.get("pid")
            if old_pid and os.kill(old_pid, 0) is None:
                log(f"⚠️ Mise à jour déjà en cours (PID {old_pid}) — arrêt.")
                return False
        except (ProcessLookupError, ValueError, OSError):
            pass
        lockfile.unlink(missing_ok=True)
    lockfile.write_text(json.dumps({"pid": os.getpid(), "started": now_str()}))
    return True


def release_update_lock():
    lockfile = BASE_DIR / "data" / ".update_all.lock"
    lockfile.unlink(missing_ok=True)


def fetch_data() -> bool:
    """Fetch les données pour toute la watchlist via fetch_prices.py."""
    log("📡 Fetch des données pour toute la watchlist...")
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR / "agents") + ":" + str(BASE_DIR / "scripts") + ":" + str(BASE_DIR)
    rc, out = run_cmd(
        [PYTHON, str(BASE_DIR / "scripts" / "fetch_prices.py")],
        env=env,
        timeout=120,
    )
    if rc != 0:
        log(f"❌ Échec du fetch (code {rc})")
        log(out[-500:] if len(out) > 500 else out)
        return False
    log("✅ Fetch terminé")

    # Copie des données vers le frontend
    dist_data = BASE_DIR / "frontend" / "dist" / "data"
    dist_data.mkdir(parents=True, exist_ok=True)
    files_to_copy = [
        "latest.json", "recommandations_latest.json", "quant_report_latest.json",
        "quality_report_latest.json", "geo_risk_latest.json", "fx_exposure_latest.json",
        "crypto_correlation_latest.json", "social_sentiment_latest.json",
        "upcoming_events_latest.json", "events_latest.json", "sector_rotation_latest.json",
        "accounting_risk_latest.json", "transcripts_NLP_latest.json", "news_latest.json",
        "ollama_config.json", "ollama_usage.json",
    ]
    for fname in files_to_copy:
        src = BASE_DIR / "data" / fname
        if src.exists():
            dst = dist_data / fname
            try:
                import shutil
                shutil.copy2(str(src.resolve()), str(dst))
            except Exception:
                pass
    log("📦 Données syncées vers frontend/dist/data/")
    return True


def run_agents() -> tuple[int, int]:
    """Lance les agents réels. Retourne (ok_count, total)."""
    log("🔧 Exécution des agents Python réels...")
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR / "agents") + ":" + str(BASE_DIR / "scripts") + ":" + str(BASE_DIR)

    agents = ["accounting", "geo", "crypto", "sector_rotation", "social", "fx",
              "event_driven", "watchman", "detect_major_events", "recommandation"]
    ok_count = 0

    for agent in agents:
        wait_for_pipeline_lock(max_wait=10)
        log(f"  → Agent {agent}...")
        rc, out = run_cmd(
            [PYTHON, str(BASE_DIR / "agents" / "orchestrator.py"), f"--agent={agent}"],
            env=env,
            timeout=300,
        )
        if rc == 0:
            ok_count += 1
            log(f"    ✅ {agent} ok")
        else:
            log(f"    ⚠️  {agent} exit={rc}")
            if out:
                last = out.strip().splitlines()[-3:]
                for line in last:
                    log(f"       {line}")

    log(f"✅ Agents terminés — {ok_count}/{len(agents)} OK")
    return ok_count, len(agents)


def _build_update_prompt(ticker: str) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"""Tu es l'analyste institutionnel senior du desk Argus-IA. Mets à jour l'analyse de **{ticker}**.

Protocole obligatoire :
1. Lis l'analyse précédente dans Actions/{ticker}/ (le fichier .md le plus récent)
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


def run_claude_update(ticker: str, today: str) -> bool:
    """Lance Claude CLI via Ollama pour générer un _update.md pour un ticker."""
    ticker_dir = ACTIONS_DIR / ticker
    report_file = ticker_dir / f"{ticker}_{today}_update.md"

    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR / "agents") + ":" + str(BASE_DIR / "scripts") + ":" + str(BASE_DIR)

    prompt = _build_update_prompt(ticker)
    claude_cmd = [
        "ollama", "launch", "claude",
        "--model", "kimi-k2.6:cloud",
        "-y",
        "--",
        "-p", prompt,
        "--permission-mode", "auto",
    ]

    log(f"  🤖 Mise à jour {ticker} — lancement Claude CLI via Ollama...")

    try:
        result = subprocess.run(
            claude_cmd,
            cwd=str(BASE_DIR),
            env=env,
            capture_output=True,
            text=True,
            timeout=600,
        )

        if result.returncode != 0:
            log(f"    ⚠️  {ticker} — exit={result.returncode}")
            err = result.stderr.strip().splitlines()[-3:] if result.stderr else []
            for line in err:
                log(f"       {line}")
            return False

        if report_file.exists():
            log(f"    ✅ {ticker} — {report_file.name}")
            return True
        else:
            log(f"    ⚠️  {ticker} — rapport non trouvé ({report_file.name})")
            return False

    except subprocess.TimeoutExpired:
        log(f"    ⏱ {ticker} — timeout (10 min)")
        return False
    except Exception as e:
        log(f"    ❌ {ticker} — erreur : {e}")
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Mise à jour automatique de toutes les analyses Argus-IA")
    parser.add_argument("--prompt", default="", help="Instructions personnalisées (ajoutées au prompt)")
    args = parser.parse_args()

    # ── Lock ──
    if not acquire_update_lock():
        sys.exit(0)

    try:
        log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        log(" Argus-IA — Mise à jour automatique des analyses")
        log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        # ── Attendre le pipeline si en cours ──
        wait_for_pipeline_lock(max_wait=120)

        # ── Lister les tickers ──
        config = load_json(CONFIG_PATH)
        all_tickers = [t["ticker"].upper() for t in config.get("tickers", [])]
        tickers_to_update = [t for t in all_tickers if (ACTIONS_DIR / t).exists()]

        if not tickers_to_update:
            log("⚠️  Aucun ticker à mettre à jour (pas de dossiers dans Actions/)")
            sys.exit(0)

        log(f"📋 {len(tickers_to_update)} ticker(s) à mettre à jour : {', '.join(tickers_to_update)}")

        # ── Étape 1 : Fetch ──
        if not fetch_data():
            sys.exit(1)

        # ── Étape 2 : Agents ──
        ok, total = run_agents()
        if ok < total - 2:  # Tolère 2 agents en échec
            log("⚠️  Trop d'agents en échec — poursuite malgré tout")

        # ── Étape 3 : Mises à jour Claude CLI (parallèle, max 3) ──
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        log(f"🤖 Mise à jour {len(tickers_to_update)} analyse(s) via Claude CLI (Ollama/kimi)...")

        completed = 0
        failed = 0
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {executor.submit(run_claude_update, t, today): t for t in tickers_to_update}
            for future in as_completed(futures):
                ticker = futures[future]
                try:
                    ok = future.result()
                    if ok:
                        completed += 1
                    else:
                        failed += 1
                except Exception as e:
                    log(f"❌ Exception mise à jour {ticker} : {e}")
                    failed += 1

        log(f"✅ Terminé — {completed} OK, {failed} échec(s)")
        log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        # ── Auto-push GitHub ──
        log("🚀 Auto-push GitHub...")
        rc, out = run_cmd(["bash", str(BASE_DIR / "scripts" / "auto_push.sh"), f"Mise à jour analyses — {today}"])
        if rc == 0:
            log("✅ Push OK")
        else:
            log(f"⚠️  Push exit={rc}")

        return 0 if failed == 0 else 1
    finally:
        release_update_lock()


if __name__ == "__main__":
    sys.exit(main())

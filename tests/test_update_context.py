import tempfile
from pathlib import Path

import pytest

from scripts.update_context import (
    parse_index_md,
    get_latest_analysis,
    parse_tracking_errors,
    parse_alertes,
    parse_upcoming_events,
    get_technical_context,
    build_context_md,
)


class TestParseIndexMd:
    def test_parse_full_index(self, tmp_path: Path):
        index = tmp_path / "INDEX.md"
        index.write_text(
            "# Ticker\n\n"
            "**Recommandation :** 🟡 SURVEILLER / ATTENDRE earnings | **Prix cible :** $72 (+36% vs $52.94) | **Stop-loss :** $41.94 (révisé post-gap)\n"
            "**Score :** 5.8/10 (downgrade de 7.55/10) | **Horizon :** 6-12 mois | **Quality :** ⚠️ Partielle (4/6)\n"
            "\n## Thèse courante\nThèse MODIFIÉE — intacte mais timing dégradé.\n",
            encoding="utf-8",
        )
        result = parse_index_md(index)
        assert result["recommandation"] == "🟡 SURVEILLER / ATTENDRE earnings"
        assert result["score"] == 5.8
        assert result["prix_cible"] == "72"
        assert result["stop_loss"] == "41.94"
        assert result["statut_thesis"] == "modifiée"
        assert result["horizon"] == "6-12 mois"

    def test_parse_missing(self, tmp_path: Path):
        result = parse_index_md(tmp_path / "missing.md")
        assert result == {}


class TestGetLatestAnalysis:
    def test_find_latest_init(self, tmp_path: Path):
        (tmp_path / "TICK_2026-05-10_init.md").write_text("# Init\n\nConclusion: Buy.")
        (tmp_path / "TICK_2026-05-12_update.md").write_text("# Update\n\nConclusion: Hold.")
        result = get_latest_analysis(tmp_path)
        assert result["date"] == "2026-05-12"
        assert result["type"] == "update"
        assert result["file"] == "TICK_2026-05-12_update.md"

    def test_no_dated_files(self, tmp_path: Path):
        result = get_latest_analysis(tmp_path)
        assert result == {}


class TestParseTrackingErrors:
    def test_miss_detected(self, tmp_path: Path):
        suivi = tmp_path / "SUIVI.md"
        suivi.write_text(
            "| Date | Ticker | Type | Reco | Prix | Cours | Upside | J+30 | J+90 | J+180 | Verdict |\n"
            "|------|--------|------|------|------|-------|--------|------|------|-------|---------|\n"
            "| 2026-05-10 | IREN | init | Achat | 85 | 61 | +39 | 2026-06 | 2026-08 | 2026-11 | ❌ Miss |\n",
            encoding="utf-8",
        )
        errors = parse_tracking_errors("IREN", suivi)
        assert len(errors) == 1
        assert errors[0]["error"] == "Miss / Imprécis"

    def test_no_errors(self, tmp_path: Path):
        suivi = tmp_path / "SUIVI.md"
        suivi.write_text("| Date | Ticker | Verdict |\n|------|--------|---------|\n", encoding="utf-8")
        errors = parse_tracking_errors("IREN", suivi)
        assert errors == []


class TestParseAlertes:
    def test_alerte_found(self, tmp_path: Path):
        alertes = tmp_path / "ALERTES.md"
        alertes.write_text(
            "| Ticker | Type | Seuil | Cours réf. | Statut | Créée le |\n"
            "|--------|------|-------|------------|--------|----------|\n"
            "| **IREN** | Baisse | $54.20 | $61.20 | 🟢 Active | 2026-05-10 |\n",
            encoding="utf-8",
        )
        # parse_alertes reads from global ALERTES_PATH; we monkeypatch via a fixture if needed
        # For simplicity, override the global constant in the test by patching the module attribute
        import scripts.update_context as uc
        orig = uc.ALERTES_PATH
        uc.ALERTES_PATH = alertes
        try:
            result = parse_alertes("IREN")
            assert len(result) == 1
            assert "Baisse" in result[0]
        finally:
            uc.ALERTES_PATH = orig


class TestParseUpcomingEvents:
    def test_event_found(self, tmp_path: Path):
        upcoming = tmp_path / "UPCOMING.md"
        upcoming.write_text(
            "| Ticker | Type | Date | Jours | Détail | Source |\n"
            "|--------|------|------|-------|--------|--------|\n"
            "| IREN | earnings | 2026-05-17 | 0j | Earnings Q4 | fmp |\n",
            encoding="utf-8",
        )
        import scripts.update_context as uc
        orig = uc.UPCOMING_PATH
        uc.UPCOMING_PATH = upcoming
        try:
            result = parse_upcoming_events("IREN")
            assert len(result) == 1
            assert result[0]["type"] == "earnings"
        finally:
            uc.UPCOMING_PATH = orig


class TestGetTechnicalContext:
    def test_extract(self):
        latest = {
            "prices": {
                "AAPL": {
                    "price": {"volume_avg_20d": 50_000_000},
                    "technical": {"rsi14": 55.0, "mm50": 150.0, "mm200": 140.0, "atr14": 2.5},
                }
            }
        }
        ctx = get_technical_context("AAPL", latest)
        assert ctx["rsi14"] == 55.0
        assert ctx["mm50"] == 150.0
        assert ctx["mm200"] == 140.0
        assert ctx["atr14"] == 2.5
        assert ctx["volume_avg_20d"] == 50_000_000


class TestBuildContextMd:
    def test_structure(self):
        ctx = {
            "ticker": "AAPL",
            "thesis": {
                "recommandation": "ACHETER",
                "score": 7.5,
                "prix_cible": "200",
                "stop_loss": "180",
                "statut_thesis": "validée",
                "horizon": "6-12 mois",
            },
            "latest_analysis": {"date": "2026-05-10", "type": "init", "file": "AAPL_init.md", "summary": "Buy thesis intact."},
            "errors": [{"date": "2026-05-01", "type": "prix cible", "error": "Miss", "lesson": "Overestimated."}],
            "alertes": ["Baisse — $180 — Active"],
            "events": [{"date": "2026-06-01", "type": "earnings", "detail": "Q2"}],
            "technical": {"rsi14": 55, "mm50": 150, "mm200": 140, "atr14": 2.5, "volume_avg_20d": 50_000_000},
            "triggers": ["PRICE_GAP -5%"],
        }
        md = build_context_md("AAPL", ctx)
        assert "# CONTEXT — AAPL" in md
        assert "ACHETER" in md
        assert "7.5/10" in md
        assert "$200" in md
        assert "Buy thesis intact." in md
        assert "Baisse" in md
        assert "earnings" in md
        assert "PRICE_GAP" in md

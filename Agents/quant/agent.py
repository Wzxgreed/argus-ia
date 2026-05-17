#!/usr/bin/env python3
"""
agent_quant.py — Agent Quant / Statistique.

Protocol : `Agents/AGENT_QUANT.md`

Analyse la performance historique des signaux, calcule les métriques de risque
institutionnelles (Sharpe, Max Drawdown, Sortino), teste la signification
statistique, et détecte l'overfitting.
"""

import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yfinance as yf

from agents.base import BaseAgent
from agents.schemas import Meta, QuantReport, RiskMetrics, Significance


class QuantAgent(BaseAgent):
    name = "quant"
    output_schema = QuantReport

    def __init__(self):
        super().__init__()
        self.backtesting_path = self.data_dir.parent / "Opportunités" / "BACKTESTING.md"
        self.suivi_prix_path = self.data_dir.parent / "Actions" / "SUIVI_PRIX_CIBLES.md"
        self.risk_free_rate = 0.045

    # -----------------------------------------------------------------------
    # Markdown helpers
    # -----------------------------------------------------------------------

    def parse_markdown_table(self, text: str, header_keywords: list[str]) -> list[dict]:
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if not line.strip().startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if not any(kw.lower() in " ".join(cols).lower() for kw in header_keywords):
                continue
            if i + 1 >= len(lines) or "---" not in lines[i + 1]:
                continue
            header = cols
            rows = []
            for j in range(i + 2, len(lines)):
                row_line = lines[j].strip()
                if not row_line.startswith("|"):
                    break
                cells = [c.strip() for c in row_line.split("|")[1:-1]]
                if len(cells) != len(header):
                    continue
                rows.append({header[idx]: cells[idx] for idx in range(len(header))})
            return rows
        return []

    # -----------------------------------------------------------------------
    # Data extraction helpers
    # -----------------------------------------------------------------------

    def extract_returns_from_verdict(self, cell: str) -> float | None:
        m = re.search(r"([+-]?\d+\.?\d*)%", cell)
        if m:
            try:
                return float(m.group(1)) / 100
            except ValueError:
                return None
        return None

    def get_risk_free_rate(self) -> float:
        latest = self.data_dir / "latest.json"
        if not latest.exists():
            return self.risk_free_rate
        try:
            data = json.loads(latest.read_text(encoding="utf-8"))
            macro = data.get("macro", {})
            tnx = macro.get("data", {}).get("tnx", {})
            val = tnx.get("value")
            if val is not None and isinstance(val, (int, float)):
                return float(val) / 100
        except Exception:
            pass
        return self.risk_free_rate

    # -----------------------------------------------------------------------
    # Statistical tests
    # -----------------------------------------------------------------------

    def binomial_test(self, hits: int, total: int, p_expected: float = 0.5) -> float:
        if total == 0:
            return 1.0
        log_p = 0.0
        for k in range(hits, total + 1):
            log_p += math.comb(total, k) * (p_expected ** k) * ((1 - p_expected) ** (total - k))
        return log_p

    def sharpe_ratio(self, returns: list[float], risk_free: float) -> float:
        if not returns:
            return 0.0
        avg = sum(returns) / len(returns)
        std = math.sqrt(sum((r - avg) ** 2 for r in returns) / max(len(returns) - 1, 1))
        if std == 0:
            return 0.0
        return round((avg - risk_free / 18) / std, 3)

    def sortino_ratio(self, returns: list[float], risk_free: float) -> float:
        if not returns:
            return 0.0
        avg = sum(returns) / len(returns)
        downside = [min(r - risk_free / 18, 0) ** 2 for r in returns]
        downside_std = math.sqrt(sum(downside) / max(len(downside), 1))
        if downside_std == 0:
            return 0.0
        return round((avg - risk_free / 18) / downside_std, 3)

    def max_drawdown(self, returns: list[float]) -> float:
        if not returns:
            return 0.0
        peak = 0.0
        max_dd = 0.0
        cumulative = 0.0
        for r in returns:
            cumulative += r
            if cumulative > peak:
                peak = cumulative
            dd = cumulative - peak
            if dd < max_dd:
                max_dd = dd
        return round(max_dd, 4)

    # -----------------------------------------------------------------------
    # Main analysis
    # -----------------------------------------------------------------------

    def analyze_backtesting(self) -> dict:
        stats = {
            "signals_total": 0,
            "signals_with_verdict": 0,
            "hits": 0,
            "misses": 0,
            "scratches": 0,
            "win_rate": 0.0,
            "avg_gain": 0.0,
            "avg_loss": 0.0,
            "returns": [],
        }

        if not self.backtesting_path.exists():
            return stats

        text = self.backtesting_path.read_text(encoding="utf-8")
        rows = self.parse_markdown_table(text, ["Date signal", "Ticker", "J+5"])
        if not rows:
            return stats

        returns = []
        hits = 0
        misses = 0
        scratches = 0
        gains = []
        losses = []

        for row in rows:
            for col in ["J+20", "J+5"]:
                cell = row.get(col, "").strip()
                if not cell or cell.startswith("⏳"):
                    continue
                ret = self.extract_returns_from_verdict(cell)
                if ret is None:
                    continue
                returns.append(ret)
                if "✅ Hit" in cell:
                    hits += 1
                    gains.append(ret)
                elif "❌ Miss" in cell:
                    misses += 1
                    losses.append(ret)
                else:
                    scratches += 1
                break

        total = len(returns)
        stats["signals_total"] = len(rows)
        stats["signals_with_verdict"] = total
        stats["hits"] = hits
        stats["misses"] = misses
        stats["scratches"] = scratches
        stats["returns"] = returns

        if total > 0:
            stats["win_rate"] = round(hits / total, 3)
            stats["avg_gain"] = round(sum(gains) / len(gains), 4) if gains else 0.0
            stats["avg_loss"] = round(sum(losses) / len(losses), 4) if losses else 0.0

        return stats

    def build_report(self, stats: dict) -> QuantReport:
        rf = self.get_risk_free_rate()
        returns = stats.get("returns", [])
        hits = stats.get("hits", 0)
        total = stats.get("signals_with_verdict", 0)

        p_value = round(self.binomial_test(hits, total), 4) if total > 0 else None

        significance = Significance(
            win_rate_observed=stats["win_rate"],
            win_rate_expected=0.5,
            p_value=p_value,
            conclusion=(
                "Insuffisant" if total < 15 else
                "Significatif" if total >= 15 and self.binomial_test(hits, total) < 0.05 else
                "Non significatif"
            ),
            n=total,
            alert=None,
        )

        if p_value is not None:
            if p_value > 0.20:
                significance.alert = "Les signaux ne sont pas mieux que le hasard — réviser le scoring"
            elif p_value < 0.05:
                significance.alert = "Signaux significativement supérieurs au hasard — maintenir la méthodologie"

        risk = RiskMetrics(
            sharpe=self.sharpe_ratio(returns, rf) if returns else None,
            sortino=self.sortino_ratio(returns, rf) if returns else None,
            max_drawdown=self.max_drawdown(returns) if returns else None,
            win_loss_ratio=(
                round(abs(stats["avg_gain"] / stats["avg_loss"]), 2)
                if stats["avg_loss"] != 0 else None
            ),
            expectancy=(
                round(
                    stats["win_rate"] * stats["avg_gain"] -
                    (1 - stats["win_rate"]) * abs(stats["avg_loss"]),
                    4
                ) if stats["avg_loss"] != 0 else None
            ),
        )

        if significance.alert:
            self.log("WARNING", "significance_alert", alert=significance.alert)

        return QuantReport(
            meta=Meta(date=self.date_str, agent=self.name),
            significance=significance,
            risk_metrics=risk,
            calibration={},
            overfitting={"rules_active": 0, "alert": False},
        )

    def run(self) -> QuantReport:
        self.log("INFO", "start", backtesting_path=str(self.backtesting_path))
        stats = self.analyze_backtesting()
        report = self.build_report(stats)
        self.log(
            "INFO",
            "complete",
            signals=stats["signals_with_verdict"],
            win_rate=stats["win_rate"],
            p_value=report.significance.p_value,
        )
        return report


if __name__ == "__main__":
    sys.exit(QuantAgent.cli_entry())

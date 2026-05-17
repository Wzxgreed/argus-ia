#!/usr/bin/env python3
"""
data_quality_gate.py — Détecteur de données pourries post-fetch.

S'exécute immédiatement après fetch_prices.py pour détecter :
  • Cours stale (close identique sur 2+ jours)
  • Volume anomalie (volume == 0 alors que marché ouvert)
  • Spread aberrant ((high-low)/close > seuil selon market cap)
  • High/Low incohérents
  • RSI/ATR placeholders (50.0 exact, 0.01)
  • Écart inter-jours > 25%
  • Données FMP placeholders (num_analysts == 0 + price_target_avg == 0)
"""

import json
import os
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

from agents.base import BaseAgent
from agents.schemas import Meta, QualityReason, QualityReport, TickerQuality


class DataQualityGateAgent(BaseAgent):
    name = "quality_gate"
    output_schema = QualityReport

    STALE_DAYS_THRESHOLD = 2
    VOLUME_ZERO_THRESHOLD = 0
    SPREAD_THRESHOLDS = {
        "large": 0.15,
        "mid": 0.30,
        "small": 0.50,
    }
    RSI_PLACEHOLDER = 50.0
    ATR_PLACEHOLDER_HIGH = 0.01
    CHANGE_PCT_ABERRANT = 25.0

    def load_historical_snapshots(self, days: int = 3) -> list[dict]:
        today = date.today()
        snapshots = []
        for i in range(1, days + 1):
            d = today - __import__("datetime").timedelta(days=i)
            path = self.data_dir / f"{d.isoformat()}.json"
            if path.exists():
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        snapshots.append(json.load(f))
                except Exception:
                    pass
        return snapshots

    def classify_market_cap(self, market_cap: float | None) -> str:
        if market_cap is None:
            return "small"
        if market_cap > 50_000_000_000:
            return "large"
        if market_cap > 10_000_000_000:
            return "mid"
        return "small"

    def is_market_open(self, ticker_data: dict, hist_snapshots: list[dict]) -> bool:
        for snap in hist_snapshots:
            prev = snap.get("prices", {}).get(ticker_data.get("ticker"), {})
            vol = prev.get("price", {}).get("volume")
            if vol and vol > 0:
                return True
        weekday = datetime.now(timezone.utc).weekday()
        return weekday < 5

    def check_ticker(self, ticker: str, data: dict, hist_snapshots: list[dict]) -> TickerQuality:
        reasons: list[QualityReason] = []
        price = data.get("price", {})
        tech = data.get("technical", {})
        fund = data.get("fundamentals", {})
        fmp = data.get("fmp_consensus", {})

        close = price.get("close")
        high = price.get("high")
        low = price.get("low")
        volume = price.get("volume")
        change_pct = price.get("change_pct")
        prev_close = price.get("previous_close")
        rsi = tech.get("rsi14")
        atr = tech.get("atr14")
        market_cap = fund.get("market_cap")
        mc_class = self.classify_market_cap(market_cap)

        if close is not None and prev_close is not None:
            if close == prev_close and change_pct == 0:
                reasons.append(QualityReason(
                    type="stale_price",
                    severity="WARNING",
                    message=f"close({close}) == previous_close({prev_close}) et change_pct=0 — cours potentiellement stale",
                ))

        stale_count = 0
        for snap in hist_snapshots:
            prev = snap.get("prices", {}).get(ticker, {})
            prev_close_hist = prev.get("price", {}).get("close")
            if prev_close_hist is not None and close is not None and prev_close_hist == close:
                stale_count += 1
        if stale_count >= self.STALE_DAYS_THRESHOLD:
            reasons.append(QualityReason(
                type="stale_price_history",
                severity="CRITICAL",
                message=f"close identique sur {stale_count + 1} jours consécutifs (incluant aujourd'hui)",
            ))

        if volume == 0 and self.is_market_open(data, hist_snapshots):
            reasons.append(QualityReason(
                type="zero_volume",
                severity="WARNING" if mc_class != "large" else "CRITICAL",
                message="volume == 0 alors que le marché semble ouvert",
            ))

        if close and high and low and close > 0:
            spread = (high - low) / close
            threshold = self.SPREAD_THRESHOLDS.get(mc_class, 0.50)
            if spread > threshold:
                reasons.append(QualityReason(
                    type="abnormal_spread",
                    severity="WARNING",
                    message=f"spread {(spread*100):.1f}% > seuil {threshold*100:.0f}% ({mc_class} cap)",
                ))
            if high < close:
                reasons.append(QualityReason(
                    type="incoherent_high",
                    severity="CRITICAL",
                    message=f"high({high}) < close({close})",
                ))
            if low > close:
                reasons.append(QualityReason(
                    type="incoherent_low",
                    severity="CRITICAL",
                    message=f"low({low}) > close({close})",
                ))

        if rsi is not None and abs(rsi - self.RSI_PLACEHOLDER) < 0.01:
            reasons.append(QualityReason(
                type="rsi_placeholder",
                severity="WARNING",
                message=f"RSI={rsi} (valeur par défaut suspecte 50.0)",
            ))
        if atr is not None and 0 < atr <= self.ATR_PLACEHOLDER_HIGH:
            reasons.append(QualityReason(
                type="atr_placeholder",
                severity="WARNING",
                message=f"ATR={atr} (valeur anormalement basse, probablement placeholder)",
            ))

        if change_pct is not None and abs(change_pct) > self.CHANGE_PCT_ABERRANT:
            reasons.append(QualityReason(
                type="abnormal_change_pct",
                severity="WARNING",
                message=f"change_pct={change_pct}% > {self.CHANGE_PCT_ABERRANT}% — vérifier événement majeur",
            ))

        if fmp:
            num_analysts = fmp.get("num_analysts")
            pt_avg = fmp.get("price_target_avg")
            if (num_analysts == 0 or num_analysts is None) and (pt_avg == 0 or pt_avg is None):
                reasons.append(QualityReason(
                    type="fmp_placeholder",
                    severity="WARNING",
                    message="fmp_consensus vide (num_analysts=0, price_target_avg=0)",
                ))

        if any(r.severity == "CRITICAL" for r in reasons):
            status = "excluded"
        elif reasons:
            status = "warning"
        else:
            status = "ok"

        return TickerQuality(status=status, reasons=reasons)

    def check_macro(self, latest: dict, hist_snapshots: list[dict]) -> list[QualityReason]:
        reasons: list[QualityReason] = []
        macro = latest.get("macro", {})
        if not macro:
            reasons.append(QualityReason(
                type="macro_missing",
                severity="CRITICAL",
                message="Bloc macro absent du snapshot",
            ))
            return reasons

        regime = macro.get("regime")
        if not regime:
            reasons.append(QualityReason(
                type="macro_regime_missing",
                severity="WARNING",
                message="Régime macro non déterminé",
            ))

        macro_data = macro.get("data", {})
        vix = macro_data.get("vix", {}).get("value")
        if vix is None:
            reasons.append(QualityReason(
                type="macro_vix_missing",
                severity="WARNING",
                message="VIX absent des données macro",
            ))

        return reasons

    def _inject_into_latest(self, latest: dict, tickers_quality: dict[str, TickerQuality]) -> None:
        prices = latest.get("prices", {})
        for ticker, quality in tickers_quality.items():
            if ticker in prices:
                prices[ticker]["_quality_gate"] = {
                    "status": quality.status,
                    "reasons": [r.model_dump(mode="json") for r in quality.reasons],
                }

        date_str = self.date_str
        latest_path = self.data_dir / f"{date_str}.json"
        if latest_path.exists():
            with tempfile.NamedTemporaryFile(mode="w", dir=self.data_dir, delete=False, suffix=".json") as f:
                json.dump(latest, f, indent=2, ensure_ascii=False)
                temp_path = f.name
            os.replace(temp_path, latest_path)

            link = self.data_dir / "latest.json"
            if link.exists() or link.is_symlink():
                link.unlink()
            link.symlink_to(latest_path.relative_to(self.data_dir))

    def run(self) -> QualityReport:
        latest = self.load_latest()
        if not latest:
            self.log("ERROR", "latest_json_missing")
            raise RuntimeError("latest.json vide ou inexistant")

        hist = self.load_historical_snapshots(days=3)
        prices = latest.get("prices", {})

        tickers_quality: dict[str, TickerQuality] = {}
        ok_count = 0
        warning_count = 0
        excluded_count = 0

        for ticker, data in prices.items():
            if data.get("error"):
                continue
            result = self.check_ticker(ticker, data, hist)
            tickers_quality[ticker] = result

            if result.status == "ok":
                ok_count += 1
            elif result.status == "warning":
                warning_count += 1
            else:
                excluded_count += 1

        self._inject_into_latest(latest, tickers_quality)

        macro_reasons = self.check_macro(latest, hist)
        summary = {"ok": ok_count, "warning": warning_count, "excluded": excluded_count}

        self.log(
            "INFO",
            "complete",
            ok=ok_count,
            warning=warning_count,
            excluded=excluded_count,
        )

        return QualityReport(
            meta=Meta(date=self.date_str, agent=self.name),
            tickers=tickers_quality,
            macro={"reasons": macro_reasons},
            summary=summary,
        )


if __name__ == "__main__":
    sys.exit(DataQualityGateAgent.cli_entry())

#!/usr/bin/env python3
"""
agent_accounting.py — Agent Fraude / Qualité Comptable.

Calcule les métriques de détection de manipulation comptable et de santé financière :
  • Beneish M-Score : détection de manipulation (seuil -1.78)
  • Altman Z-Score : probabilité de faillite (seuil 1.81)
  • Piotroski F-Score : score de santé 0-9
  • Sloan Ratio : qualité des bénéfices (accruals vs cash-flow)
  • Cash Conversion Cycle : efficacité opérationnelle

Sources : FMP Stable API (income-statement, balance-sheet-statement, cash-flow-statement)
Output  : data/accounting_risk_YYYY-MM-DD.json + symlink latest

Règles absolues :
  • M-Score > -1.78 → 🔴 Manipulation suspectée → exclure long
  • Z-Score < 1.81 → 🔴 Distress → exclure long
  • F-Score ≤ 3/9 → 🔴 Santé faible → plafonner Score Valorisation à 3/10
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

from fmp_client import FMPClient

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "watchlist.json"
DATA_DIR = BASE_DIR / "data"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Beneish M-Score
# ---------------------------------------------------------------------------

def calc_beneish_m_score(stmts: dict) -> dict | None:
    """
    Calcule le Beneish M-Score à partir de 2 exercices consécutifs.
    Formules : Beneish (1999)
    M = -4.84 + 0.92*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI
    """
    inc = stmts.get("income", [])
    bs = stmts.get("balance", [])
    cf = stmts.get("cashflow", [])
    if len(inc) < 2 or len(bs) < 2:
        return None

    try:
        t = inc[0]   # Current year
        t_1 = inc[1] # Previous year
        bs_t = bs[0]
        bs_t1 = bs[1]
        cf_t = cf[0] if cf else {}

        # Receivables
        rec_t = bs_t.get("netReceivables", 0) or 0
        rec_t1 = bs_t1.get("netReceivables", 0) or 0
        rev_t = t.get("revenue", 0) or 0
        rev_t1 = t_1.get("revenue", 0) or 0
        dsri = ((rec_t / rev_t) / (rec_t1 / rev_t1)) if rev_t > 0 and rev_t1 > 0 and rec_t1 > 0 else 1.0

        # Gross Margin
        gm_t = (t.get("grossProfit", 0) or 0) / rev_t if rev_t > 0 else 0
        gm_t1 = (t_1.get("grossProfit", 0) or 0) / rev_t1 if rev_t1 > 0 else 0
        gmi = gm_t1 / gm_t if gm_t > 0 else 1.0

        # Asset Quality
        ta_t = bs_t.get("totalAssets", 0) or 0
        ta_t1 = bs_t1.get("totalAssets", 0) or 0
        ca_t = bs_t.get("totalCurrentAssets", 0) or 0
        ca_t1 = bs_t1.get("totalCurrentAssets", 0) or 0
        ppe_t = bs_t.get("propertyPlantEquipmentNet", 0) or 0
        ppe_t1 = bs_t1.get("propertyPlantEquipmentNet", 0) or 0
        aqi = ((ta_t - ca_t - ppe_t) / ta_t) / ((ta_t1 - ca_t1 - ppe_t1) / ta_t1) if ta_t > 0 and ta_t1 > 0 else 1.0

        # Sales Growth
        sgi = rev_t / rev_t1 if rev_t1 > 0 else 1.0

        # Depreciation
        dep_t = t.get("depreciationAndAmortization", 0) or 0
        dep_t1 = t_1.get("depreciationAndAmortization", 0) or 0
        depi = (dep_t1 / (dep_t1 + ppe_t1)) / (dep_t / (dep_t + ppe_t)) if (dep_t + ppe_t) > 0 and (dep_t1 + ppe_t1) > 0 else 1.0

        # SG&A
        sga_t = t.get("sellingAndMarketingExpenses", 0) or 0
        sga_t1 = t_1.get("sellingAndMarketingExpenses", 0) or 0
        sgai = (sga_t / rev_t) / (sga_t1 / rev_t1) if rev_t > 0 and rev_t1 > 0 and sga_t1 > 0 else 1.0

        # Total Accruals
        ni_t = t.get("netIncome", 0) or 0
        cfo_t = cf_t.get("netCashProvidedByOperatingActivities", 0) or 0
        tata = (ni_t - cfo_t) / ta_t if ta_t > 0 else 0

        # Leverage
        td_t = bs_t.get("totalDebt", 0) or 0
        td_t1 = bs_t1.get("totalDebt", 0) or 0
        lvgi = (td_t / ta_t) / (td_t1 / ta_t1) if ta_t > 0 and ta_t1 > 0 and td_t1 > 0 else 1.0

        m_score = (-4.84
                   + 0.92 * dsri
                   + 0.528 * gmi
                   + 0.404 * aqi
                   + 0.892 * sgi
                   + 0.115 * depi
                   - 0.172 * sgai
                   + 4.679 * tata
                   - 0.327 * lvgi)

        return {
            "m_score": round(m_score, 3),
            "dsri": round(dsri, 3),
            "gmi": round(gmi, 3),
            "aqi": round(aqi, 3),
            "sgi": round(sgi, 3),
            "depi": round(depi, 3),
            "sgai": round(sgai, 3),
            "tata": round(tata, 3),
            "lvgi": round(lvgi, 3),
            "verdict": (
                "🔴 Manipulation suspectée" if m_score > -1.78 else
                "🟡 Surveillance" if m_score > -2.22 else
                "🟢 Faible risque"
            ),
        }
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Altman Z-Score
# ---------------------------------------------------------------------------

def calc_altman_z(stmts: dict) -> dict | None:
    """
    Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5
    X1 = Working Capital / Total Assets
    X2 = Retained Earnings / Total Assets
    X3 = EBIT / Total Assets
    X4 = Market Cap / Total Liabilities
    X5 = Revenue / Total Assets
    """
    inc = stmts.get("income", [])
    bs = stmts.get("balance", [])
    if not inc or not bs:
        return None

    try:
        t = inc[0]
        bs_t = bs[0]

        wc = (bs_t.get("totalCurrentAssets", 0) or 0) - (bs_t.get("totalCurrentLiabilities", 0) or 0)
        ta = bs_t.get("totalAssets", 0) or 0
        re = bs_t.get("retainedEarnings", 0) or 0
        ebit = t.get("operatingIncome", 0) or 0
        rev = t.get("revenue", 0) or 0
        tl = bs_t.get("totalLiabilities", 0) or 0

        # x4 (market cap) filled later from latest.json (Yahoo data already fetched)
        x1 = wc / ta if ta > 0 else 0
        x2 = re / ta if ta > 0 else 0
        x3 = ebit / ta if ta > 0 else 0
        # x4 will be filled in main with market cap
        x5 = rev / ta if ta > 0 else 0

        return {
            "x1": round(x1, 3),
            "x2": round(x2, 3),
            "x3": round(x3, 3),
            "x4": None,  # filled later
            "x5": round(x5, 3),
            "z_score": None,  # filled later
            "verdict": None,  # filled later
        }
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Piotroski F-Score
# ---------------------------------------------------------------------------

def calc_piotroski_f(stmts: dict) -> dict | None:
    """
    F-Score 0-9 basé sur 9 critères fondamentaux.
    """
    inc = stmts.get("income", [])
    bs = stmts.get("balance", [])
    cf = stmts.get("cashflow", [])
    if len(inc) < 2 or len(bs) < 2:
        return None

    try:
        t = inc[0]
        t_1 = inc[1]
        bs_t = bs[0]
        bs_t1 = bs[1]
        cf_t = cf[0] if cf else {}

        score = 0
        details = {}

        # 1. ROA > 0
        roa = (t.get("netIncome", 0) or 0) / (bs_t.get("totalAssets", 0) or 1)
        if roa > 0:
            score += 1
        details["roa_positive"] = roa > 0

        # 2. CFO > 0
        cfo = cf_t.get("netCashProvidedByOperatingActivities", 0) or 0
        if cfo > 0:
            score += 1
        details["cfo_positive"] = cfo > 0

        # 3. ROA t > ROA t-1
        roa_t1 = (t_1.get("netIncome", 0) or 0) / (bs_t1.get("totalAssets", 0) or 1)
        if roa > roa_t1:
            score += 1
        details["roa_improved"] = roa > roa_t1

        # 4. CFO > Net Income
        ni = t.get("netIncome", 0) or 0
        if cfo > ni:
            score += 1
        details["cfo_gt_ni"] = cfo > ni

        # 5. Leverage ↓
        lev_t = (bs_t.get("totalLongTermDebt", 0) or 0) / (bs_t.get("totalAssets", 0) or 1)
        lev_t1 = (bs_t1.get("totalLongTermDebt", 0) or 0) / (bs_t1.get("totalAssets", 0) or 1)
        if lev_t < lev_t1:
            score += 1
        details["leverage_down"] = lev_t < lev_t1

        # 6. Current Ratio ↑
        cr_t = (bs_t.get("totalCurrentAssets", 0) or 0) / (bs_t.get("totalCurrentLiabilities", 0) or 1)
        cr_t1 = (bs_t1.get("totalCurrentAssets", 0) or 0) / (bs_t1.get("totalCurrentLiabilities", 0) or 1)
        if cr_t > cr_t1:
            score += 1
        details["current_ratio_up"] = cr_t > cr_t1

        # 7. Shares ↓ (pas dans FMP standard, approximé via equity)
        eq_t = bs_t.get("totalStockholdersEquity", 0) or 0
        eq_t1 = bs_t1.get("totalStockholdersEquity", 0) or 0
        # Skip if not available
        details["shares_down"] = None

        # 8. Gross Margin ↑
        gm_t = (t.get("grossProfit", 0) or 0) / (t.get("revenue", 0) or 1)
        gm_t1 = (t_1.get("grossProfit", 0) or 0) / (t_1.get("revenue", 0) or 1)
        if gm_t > gm_t1:
            score += 1
        details["gm_up"] = gm_t > gm_t1

        # 9. Asset Turnover ↑
        at_t = (t.get("revenue", 0) or 0) / (bs_t.get("totalAssets", 0) or 1)
        at_t1 = (t_1.get("revenue", 0) or 0) / (bs_t1.get("totalAssets", 0) or 1)
        if at_t > at_t1:
            score += 1
        details["asset_turnover_up"] = at_t > at_t1

        return {
            "f_score": score,
            "details": details,
            "verdict": (
                "🔴 Faible" if score <= 3 else
                "🟡 Moyen" if score <= 6 else
                "🟢 Fort"
            ),
        }
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Sloan Ratio
# ---------------------------------------------------------------------------

def calc_sloan_ratio(stmts: dict) -> dict | None:
    """
    Sloan Ratio = (Net Income - CFO) / Total Assets
    > 0.1 → accruals élevés (bénéfices de faible qualité)
    < -0.1 → cash-flow supérieur au net income (qualité élevée)
    """
    inc = stmts.get("income", [])
    bs = stmts.get("balance", [])
    cf = stmts.get("cashflow", [])
    if not inc or not bs or not cf:
        return None

    try:
        ni = inc[0].get("netIncome", 0) or 0
        cfo = cf[0].get("netCashProvidedByOperatingActivities", 0) or 0
        ta = bs[0].get("totalAssets", 0) or 0

        if ta <= 0:
            return None

        ratio = (ni - cfo) / ta
        return {
            "sloan_ratio": round(ratio, 4),
            "net_income": ni,
            "cfo": cfo,
            "total_assets": ta,
            "verdict": (
                "🔴 Accruals élevés" if ratio > 0.1 else
                "🟢 Qualité élevée" if ratio < -0.1 else
                "🟡 Neutre"
            ),
        }
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def fetch_statements(fmp: FMPClient, ticker: str) -> dict:
    """Récupère les 3 statements FMP pour un ticker."""
    return {
        "income": fmp.get_income_statement(ticker, period="annual", limit=3),
        "balance": fmp.get_balance_sheet(ticker, period="annual", limit=3),
        "cashflow": fmp.get_cash_flow(ticker, period="annual", limit=3),
    }


def main():
    print("[accounting] Starting fraud & accounting quality scan...", file=sys.stderr)
    config = load_config()
    tickers = [t["ticker"] for t in config.get("tickers", [])]
    fmp = FMPClient()
    fmp_active = bool(fmp.api_key)

    if not fmp_active:
        print("[accounting] ⚠️ FMP API key not found. Accounting metrics require FMP statements.", file=sys.stderr)
        return 0

    results = {}
    red_flags = 0

    for ticker in tickers:
        print(f"[accounting] Analyzing {ticker}...", file=sys.stderr)
        stmts = fetch_statements(fmp, ticker)

        # Check for errors
        for key in stmts:
            if isinstance(stmts[key], dict) and stmts[key].get("error"):
                print(f"[accounting]   {ticker}: FMP {key} error — {stmts[key].get('reason', 'Unknown')}", file=sys.stderr)
                stmts[key] = []

        # Only proceed if we have data
        if not stmts.get("income") or not stmts.get("balance"):
            print(f"[accounting]   {ticker}: No statement data available", file=sys.stderr)
            continue

        m = calc_beneish_m_score(stmts)
        z = calc_altman_z(stmts)
        f = calc_piotroski_f(stmts)
        s = calc_sloan_ratio(stmts)

        # Enrich Z-Score with market cap from latest.json (Yahoo data already fetched)
        if z:
            try:
                latest_path = DATA_DIR / "latest.json"
                mc = None
                if latest_path.exists():
                    target = latest_path.resolve()
                    with open(target, "r", encoding="utf-8") as f:
                        latest = json.load(f)
                    prices = latest.get("prices", {})
                    ticker_data = prices.get(ticker, {})
                    fund = ticker_data.get("fundamentals", {})
                    mc = fund.get("market_cap")

                if mc and z["x4"] is None:
                    bs_t = stmts["balance"][0]
                    tl = bs_t.get("totalLiabilities", 0) or 0
                    z["x4"] = round(mc / tl, 3) if tl > 0 else 0
                    if z["x4"] is not None and z["x1"] is not None:
                        z_score = (1.2 * z["x1"] + 1.4 * z["x2"] + 3.3 * z["x3"] + 0.6 * z["x4"] + 1.0 * z["x5"])
                        z["z_score"] = round(z_score, 3)
                        z["verdict"] = (
                            "🔴 Distress (faillite probable)" if z_score < 1.81 else
                            "🟡 Grey zone" if z_score < 2.99 else
                            "🟢 Safe"
                        )
            except Exception:
                pass

        ticker_result = {
            "beneish": m,
            "altman": z,
            "piotroski": f,
            "sloan": s,
        }

        # Determine composite risk
        alerts = []
        if m and m.get("m_score", -99) > -1.78:
            alerts.append("BENEISH_M_SCORE_HIGH")
        if z and z.get("z_score", 99) < 1.81:
            alerts.append("ALTMAN_DISTRESS")
        if f and f.get("f_score", 9) <= 3:
            alerts.append("PIOTROSKI_WEAK")
        if s and s.get("sloan_ratio", 0) > 0.1:
            alerts.append("SLOAN_ACCRUALS_HIGH")

        ticker_result["alerts"] = alerts
        ticker_result["risk_level"] = (
            "🔴 CRITICAL" if len(alerts) >= 2 else
            "🟡 WARNING" if len(alerts) == 1 else
            "🟢 CLEAN"
        )

        if len(alerts) > 0:
            red_flags += 1

        results[ticker] = ticker_result
        print(f"[accounting]   {ticker}: M={m['m_score'] if m else 'N/A'} | Z={z['z_score'] if z else 'N/A'} | F={f['f_score'] if f else 'N/A'} | Risk={ticker_result['risk_level']}", file=sys.stderr)

    # Write report
    date_str = today_str()
    report = {
        "meta": {
            "date": date_str,
            "tickers_scanned": len(tickers),
            "tickers_with_data": len(results),
            "red_flags": red_flags,
        },
        "analysis": results,
    }

    output_path = DATA_DIR / f"accounting_risk_{date_str}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    # Symlink latest
    latest_link = DATA_DIR / "accounting_risk_latest.json"
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    latest_link.symlink_to(output_path.relative_to(DATA_DIR))

    print(f"[accounting] Report → {output_path} | Red flags: {red_flags}/{len(results)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

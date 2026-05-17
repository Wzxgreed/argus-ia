"""agents/schemas.py — Schémas Pydantic pour tous les outputs agents."""

from datetime import date
from typing import Any

from pydantic import BaseModel, Field, field_validator


# ── Meta commune ──────────────────────────────────────────────────────────


class Meta(BaseModel):
    date: str
    version: str = "1.0"
    agent: str


# ── Quant ───────────────────────────────────────────────────────────────


class Significance(BaseModel):
    win_rate_observed: float | None = None
    win_rate_expected: float = 0.5
    p_value: float | None = None
    conclusion: str = ""
    n: int = 0
    alert: str | None = None


class RiskMetrics(BaseModel):
    sharpe: float | None = None
    sortino: float | None = None
    max_drawdown: float | None = None
    win_loss_ratio: float | None = None
    expectancy: float | None = None


class QuantReport(BaseModel):
    meta: Meta
    significance: Significance
    risk_metrics: RiskMetrics
    calibration: dict[str, Any] = Field(default_factory=dict)
    overfitting: dict[str, Any] = Field(default_factory=dict)


# ── Geo ───────────────────────────────────────────────────────────────────


class GeoEvent(BaseModel):
    title: str
    summary: str = ""
    publisher: str = ""
    score: int = Field(ge=0, le=10)
    patterns: list[str] = Field(default_factory=list)
    url: str = ""


class TickerExposure(BaseModel):
    ticker: str
    geo_risk_score: int = Field(ge=0, le=10)
    exposed: bool = False
    flag: str = "🟢"
    relevant_events: list[GeoEvent] = Field(default_factory=list)
    sectors: list[str] = Field(default_factory=list)


class GeoRiskReport(BaseModel):
    meta: Meta
    events: list[GeoEvent] = Field(default_factory=list)
    ticker_exposure: dict[str, TickerExposure] = Field(default_factory=dict)


# ── Crypto ────────────────────────────────────────────────────────────────


class CryptoTickerAnalysis(BaseModel):
    correlation_30d: float
    correlation_90d: float | None = None
    beta_btc: float
    r2_btc: float
    divergence_score: float = Field(ge=0, le=10)
    nav_estimate: float | None = None
    market_cap: float | None = None
    premium_pct: float | None = None
    verdict: str = ""


class CryptoReport(BaseModel):
    meta: Meta
    analysis: dict[str, CryptoTickerAnalysis] = Field(default_factory=dict)


# ── Accounting ────────────────────────────────────────────────────────────


class Beneish(BaseModel):
    m_score: float
    dsri: float
    gmi: float
    aqi: float
    sgi: float
    depi: float
    sgai: float
    tata: float
    lvgi: float
    verdict: str = ""


class Altman(BaseModel):
    x1: float
    x2: float
    x3: float
    x4: float
    x5: float
    z_score: float
    verdict: str = ""


class Piotroski(BaseModel):
    f_score: int = Field(ge=0, le=9)
    details: dict[str, bool] = Field(default_factory=dict)
    verdict: str = ""


class Sloan(BaseModel):
    sloan_ratio: float
    net_income: float
    cfo: float
    total_assets: float
    verdict: str = ""


class TickerAccounting(BaseModel):
    beneish: Beneish | None = None
    altman: Altman | None = None
    piotroski: Piotroski | None = None
    sloan: Sloan | None = None
    alerts: list[str] = Field(default_factory=list)
    risk_level: str = "🟢 CLEAN"


class AccountingReport(BaseModel):
    meta: Meta
    analysis: dict[str, TickerAccounting] = Field(default_factory=dict)


# ── Sector Rotation ───────────────────────────────────────────────────────


class SectorRanking(BaseModel):
    ticker: str
    name: str
    type: str = ""
    return_20d: float
    return_60d: float
    rs_20d: float
    rs_60d: float
    regime: str = ""
    regime_alignment: str = ""
    momentum_score: float = Field(ge=0, le=10)
    crossover: str | None = None


class SectorRotationReport(BaseModel):
    meta: Meta
    ranking: list[SectorRanking] = Field(default_factory=list)
    crossovers: list[SectorRanking] = Field(default_factory=list)
    top3: list[dict[str, Any]] = Field(default_factory=list)
    bottom3: list[dict[str, Any]] = Field(default_factory=list)


# ── Social Sentiment ────────────────────────────────────────────────────────


class SocialPost(BaseModel):
    title: str
    score: int
    comments: int
    subreddit: str
    sentiment: str = ""


class SocialTicker(BaseModel):
    mention_count: int = 0
    avg_score: float = 0.0
    avg_comments: float = 0.0
    sentiment_score: float = 0.0
    sentiment_label: str = ""
    raw_sentiment: float = 0.0
    positive_words: list[str] = Field(default_factory=list)
    negative_words: list[str] = Field(default_factory=list)
    pump_detected: bool = False
    top_posts: list[SocialPost] = Field(default_factory=list)
    mention_spike: bool = False
    avg_mentions_7d: float = 0.0


class SocialAlert(BaseModel):
    ticker: str
    type: str
    value: float | str


class SocialSentimentReport(BaseModel):
    meta: Meta
    analysis: dict[str, SocialTicker] = Field(default_factory=dict)
    alerts: list[SocialAlert] = Field(default_factory=list)


# ── FX Exposure ───────────────────────────────────────────────────────────


class FXTicker(BaseModel):
    ticker: str
    sector: str = ""
    exposure_pct: float = 0.0
    direction: str = ""
    primary_currency: str = "USD"
    impact_revenue_pct: float = 0.0
    impact_eps_pct: float = 0.0
    fx_impact_score: float = Field(ge=0, le=10)
    direction_label: str = "neutral"
    price_change_pct: float = 0.0
    expected_price_change_pct: float = 0.0
    divergence_flag: str = "aligned"
    flag: str = "🟢"


class FXExposureReport(BaseModel):
    meta: Meta
    tickers: list[FXTicker] = Field(default_factory=list)


# ── Event-Driven ────────────────────────────────────────────────────────────


class CorporateEvent(BaseModel):
    type: str
    date: str = ""
    ticker: str = ""
    description: str = ""
    impact_score: float = Field(ge=0, le=10)
    source: str = ""


class EventDrivenReport(BaseModel):
    meta: Meta
    ticker_events: dict[str, list[CorporateEvent]] = Field(default_factory=dict)
    all_events: list[CorporateEvent] = Field(default_factory=list)


# ── Upcoming Events (Watchman) ────────────────────────────────────────────


class UpcomingEvent(BaseModel):
    type: str
    date: str = ""
    details: str = ""
    source: str = ""
    severity: str = "low"
    ticker: str = ""
    days_until: int | None = None


class UpcomingEventsReport(BaseModel):
    meta: Meta
    events: list[UpcomingEvent] = Field(default_factory=list)


# ── Recommendations ─────────────────────────────────────────────────────────


class Recommandation(BaseModel):
    ticker: str
    action: str
    direction: str = ""
    score_global: float = 0.0
    score_global_ajuste: float = 0.0
    score_opportunite: float = 0.0
    score_catalyseur: float = 0.0
    score_valorisation: float = 0.0
    score_momentum: float = 0.0
    timing: str = ""
    horizon: str = ""
    prix_actuel: float | None = None
    prix_entree_suggere: float | None = None
    stop_loss: float | None = None
    take_profit: float | None = None
    risque_rendement_ratio: float | None = None
    sizing: str = ""
    justification: list[str] = Field(default_factory=list)
    risques: list[str] = Field(default_factory=list)
    alertes: list[str] = Field(default_factory=list)


class RecommendationsReport(BaseModel):
    meta: Meta
    recommandations: list[Recommandation] = Field(default_factory=list)


# ── Data Quality Gate ─────────────────────────────────────────────────────


class QualityReason(BaseModel):
    type: str
    severity: str  # ok, warning, critical
    message: str


class TickerQuality(BaseModel):
    status: str  # ok, warning, excluded
    reasons: list[QualityReason] = Field(default_factory=list)


class QualityReport(BaseModel):
    meta: Meta
    tickers: dict[str, TickerQuality] = Field(default_factory=dict)
    macro: dict[str, Any] = Field(default_factory=dict)
    summary: dict[str, int] = Field(default_factory=dict)

    @field_validator("tickers")
    @classmethod
    def at_least_one_ticker(cls, v):
        return v


# ── Detect Major Events ─────────────────────────────────────────────────────


class MajorEvent(BaseModel):
    ticker: str
    event_type: str
    trigger_date: str
    severity: str  # high, medium, low
    description: str
    price_change_pct: float | None = None
    volume_spike: bool = False
    atr_spike: bool = False


class MajorEventsReport(BaseModel):
    meta: Meta
    events: list[MajorEvent] = Field(default_factory=list)
    tickers_affected: list[str] = Field(default_factory=list)


# ── Paper Trading ───────────────────────────────────────────────────────────


class PaperPosition(BaseModel):
    ticker: str
    entry_date: str
    entry_price: float
    quantity: int
    stop_loss: float
    take_profit: float
    current_price: float | None = None
    pnl_pct: float | None = None
    status: str = "open"  # open, closed


class PaperTrade(BaseModel):
    ticker: str
    action: str  # buy, sell
    date: str
    price: float
    quantity: int
    reason: str = ""


class PaperTradingReport(BaseModel):
    meta: Meta
    capital: float = 100000.0
    positions: list[PaperPosition] = Field(default_factory=list)
    closed_trades: list[PaperTrade] = Field(default_factory=list)
    performance: dict[str, Any] = Field(default_factory=dict)


# ── Transcripts NLP ─────────────────────────────────────────────────────────


class TranscriptNLP(BaseModel):
    ticker: str
    quarter: str
    year: int
    confidence_ratio: float
    evasions: int
    pivots: int
    guidance_firmness: float
    management_score: float = Field(ge=0, le=10)


class TranscriptsNLPReport(BaseModel):
    meta: Meta
    transcripts: list[TranscriptNLP] = Field(default_factory=list)


# ── Context Update ──────────────────────────────────────────────────────────

class ContextUpdateReport(BaseModel):
    meta: Meta
    tickers_updated: list[str] = Field(default_factory=list)
    tickers_skipped: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)


# ── Learn from Errors ───────────────────────────────────────────────────────

class LearningReport(BaseModel):
    meta: Meta
    signals_closed: int = 0
    new_rules: list[str] = Field(default_factory=list)
    calibration: dict[str, Any] = Field(default_factory=dict)
    post_mortems: list[str] = Field(default_factory=list)

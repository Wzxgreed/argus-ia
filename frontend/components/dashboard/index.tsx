"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from "recharts";
import {
  Activity,
  TrendingUp,
  TrendingDown,
  Minus,
  Shield,
  AlertTriangle,
  CheckCircle2,
  Globe,
  Cpu,
  Zap,
  BarChart3,
  DollarSign,
  Bitcoin,
  MessageSquare,
  Eye,
  ArrowRight,
  Target,
  Crosshair,
  Scale,
  Clock,
  Calendar,
} from "lucide-react";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
};

const stagger = {
  animate: { transition: { staggerChildren: 0.06 } },
};

/* ─── Types ─── */

interface Reco {
  ticker: string;
  action: string;
  direction: string;
  score_global_ajuste: number;
  score_opportunite: number;
  score_catalyseur: number;
  score_valorisation: number;
  score_momentum: number;
  timing: string;
  prix_actuel: number;
  stop_loss: number;
  take_profit: number;
  risque_rendement_ratio: number;
  sizing: string;
  horizon: string;
  justification: string[];
  risques: string[];
}

interface TickerData {
  ticker: string;
  price: {
    close: number;
    change_pct: number;
    volume: number;
    volume_avg_20d: number;
  };
  technical: {
    rsi14: number;
    atr14: number;
    mm50: number | null;
  };
  fundamentals: {
    sector: string;
    market_cap: number;
    pe_ratio: number;
    forward_pe: number | null;
    beta: number;
  };
  options?: {
    max_pain: number;
    put_call_ratio: number;
  };
  _quality_gate: { status: string; reasons: string[] };
}

interface QuantReport {
  meta: { date: string; signals_total: number; signals_with_verdict: number };
  significance: {
    win_rate_observed: number;
    p_value: number;
    conclusion: string;
    alert?: string;
  };
  risk_metrics: {
    sharpe: number;
    sortino: number;
    max_drawdown: number;
    win_loss_ratio: number;
    expectancy: number;
  };
  overfitting: { rules_active: number; alert: boolean };
}

interface QualityReport {
  meta: { date: string; tickers_scanned: number };
  tickers: Record<string, { status: string; reasons: string[] }>;
  global: { summary: { ok: number; warning: number; excluded: number } };
}

interface GeoReport {
  meta: { date: string; events_detected: number; tickers_flagged: number };
  ticker_exposure: Record<string, { geo_risk_score: number; flag: string }>;
}

interface FXReport {
  meta: { date: string; tickers_analyzed: number; flagged_high: number; dxy_change_pct: number };
  tickers: Array<{
    ticker: string;
    exposure_pct: number;
    fx_impact_score: number;
    direction_label: string;
    price_change_pct: number;
    divergence_flag: string;
    flag: string;
  }>;
}

interface CryptoReport {
  meta: { date: string; btc_price: number };
  analysis: Record<string, {
    correlation_30d: number;
    beta_btc: number;
    divergence_score: number;
    premium_pct: number;
    verdict: string;
  }>;
}

interface SocialReport {
  meta: { date: string; tickers_scanned: number; alerts_count: number };
  analysis: Record<string, {
    mention_count: number;
    sentiment_score: number;
    sentiment_label: string;
    pump_detected: boolean;
    mention_spike: boolean;
  }>;
}

/* ─── Helpers ─── */

function fmtPrice(n: number) {
  return n?.toFixed(2) ?? "—";
}

function fmtPct(n: number) {
  return `${n > 0 ? "+" : ""}${n?.toFixed(2)}%`;
}

function fmtB(n: number) {
  if (!n) return "—";
  if (n >= 1e12) return `$${(n / 1e12).toFixed(2)}T`;
  if (n >= 1e9) return `$${(n / 1e9).toFixed(2)}B`;
  if (n >= 1e6) return `$${(n / 1e6).toFixed(2)}M`;
  return `$${n.toFixed(0)}`;
}

function actionColor(action: string) {
  const a = action.toLowerCase();
  if (a.includes("acheter")) return "bg-accent/15 text-emerald-400 border-emerald-500/20";
  if (a.includes("attendre")) return "bg-yellow-500/10 text-yellow-400 border-yellow-500/20";
  if (a.includes("surveiller")) return "bg-orange-500/10 text-orange-400 border-orange-500/20";
  if (a.includes("eviter") || a.includes("éviter")) return "bg-red-500/10 text-red-400 border-red-500/20";
  return "bg-white/[0.04] text-muted-foreground border-white/[0.08]";
}

function scoreColor(score: number) {
  if (score >= 70) return "text-emerald-400";
  if (score >= 55) return "text-yellow-400";
  if (score >= 40) return "text-orange-400";
  return "text-red-400";
}

function regimeColor(regime: string) {
  const r = regime.toLowerCase();
  if (r.includes("risk-off") || r.includes("recession")) return "text-red-400";
  if (r.includes("risk-on") || r.includes("bull")) return "text-emerald-400";
  if (r.includes("stagflation")) return "text-orange-400";
  return "text-blue-400";
}

/* ─── RegimeBanner ─── */

export function RegimeBanner({
  regime,
  weights,
  vix,
  dxy,
  date,
}: {
  regime: string;
  weights: Record<string, number>;
  vix: number;
  dxy: number;
  date: string;
}) {
  return (
    <motion.div
      variants={fadeIn}
      initial="initial"
      animate="animate"
      className="glass rounded-2xl border border-white/[0.06] p-6"
    >
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex items-center gap-4">
          <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-accent/10 text-accent">
            <Globe className="h-6 w-6" />
          </div>
          <div>
            <div className="text-sm text-muted-foreground">Régime macro du {date}</div>
            <div className={`text-2xl font-bold ${regimeColor(regime)}`}>{regime}</div>
          </div>
        </div>

        <div className="flex flex-wrap gap-3">
          <div className="rounded-xl border border-white/[0.06] bg-white/[0.02] px-4 py-2">
            <div className="text-xs text-muted-foreground">VIX</div>
            <div className="text-sm font-semibold text-foreground">{vix}</div>
          </div>
          <div className="rounded-xl border border-white/[0.06] bg-white/[0.02] px-4 py-2">
            <div className="text-xs text-muted-foreground">DXY</div>
            <div className="text-sm font-semibold text-foreground">{dxy > 0 ? "+" : ""}{dxy}%</div>
          </div>
          <div className="rounded-xl border border-white/[0.06] bg-white/[0.02] px-4 py-2">
            <div className="text-xs text-muted-foreground">Pondération</div>
            <div className="text-sm font-semibold text-foreground">
              C:{Math.round((weights.catalyseur ?? 0.35) * 100)} / V:{Math.round((weights.valorisation ?? 0.4) * 100)} / M:{Math.round((weights.momentum ?? 0.25) * 100)}
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
}

/* ─── SummaryCards ─── */

export function SummaryCards({
  tickersCount,
  recoCounts,
}: {
  tickersCount: number;
  recoCounts: Record<string, number>;
}) {
  const cards = [
    {
      label: "Tickers analysés",
      value: tickersCount.toString(),
      icon: Eye,
      color: "text-accent",
      bg: "bg-accent/10",
    },
    {
      label: "ACHETER",
      value: (recoCounts.acheter ?? 0).toString(),
      icon: TrendingUp,
      color: "text-emerald-400",
      bg: "bg-emerald-500/10",
    },
    {
      label: "SURVEILLER / ATTENDRE",
      value: ((recoCounts.surveiller ?? 0) + (recoCounts.attendre ?? 0)).toString(),
      icon: Clock,
      color: "text-yellow-400",
      bg: "bg-yellow-500/10",
    },
    {
      label: "ÉVITER",
      value: (recoCounts.eviter ?? 0).toString(),
      icon: TrendingDown,
      color: "text-red-400",
      bg: "bg-red-500/10",
    },
  ];

  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {cards.map((card, i) => (
        <motion.div
          key={card.label}
          variants={fadeIn}
          initial="initial"
          whileInView="animate"
          viewport={{ once: true }}
          transition={{ delay: i * 0.05 }}
          className="glass rounded-2xl border border-white/[0.06] p-5"
        >
          <div className="flex items-center gap-3 mb-3">
            <div className={`flex h-9 w-9 items-center justify-center rounded-lg ${card.bg} ${card.color}`}>
              <card.icon className="h-4 w-4" />
            </div>
            <span className="text-xs font-medium text-muted-foreground">{card.label}</span>
          </div>
          <div className={`text-3xl font-bold ${card.color}`}>{card.value}</div>
        </motion.div>
      ))}
    </div>
  );
}

/* ─── ScoreChart ─── */

export function ScoreChart({ recos }: { recos: Reco[] }) {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  const data = recos.map((r) => ({
    ticker: r.ticker,
    score: r.score_global_ajuste,
    catalyseur: r.score_catalyseur,
    valorisation: r.score_valorisation,
    momentum: r.score_momentum,
  }));

  return (
    <motion.div
      variants={fadeIn}
      initial="initial"
      whileInView="animate"
      viewport={{ once: true }}
      className="glass rounded-2xl border border-white/[0.06] p-6"
    >
      <div className="flex items-center gap-2 mb-4">
        <BarChart3 className="h-5 w-5 text-accent" />
        <h3 className="font-semibold text-foreground">Scores par ticker</h3>
      </div>
      <div className="h-64">
        {mounted ? (
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data} barGap={4}>
              <XAxis dataKey="ticker" tick={{ fill: "#94a3b8", fontSize: 12 }} axisLine={false} tickLine={false} />
              <YAxis domain={[0, 80]} tick={{ fill: "#94a3b8", fontSize: 12 }} axisLine={false} tickLine={false} />
              <Tooltip
                contentStyle={{
                  background: "#111827",
                  border: "1px solid rgba(255,255,255,0.08)",
                  borderRadius: "12px",
                  fontSize: "12px",
                }}
                itemStyle={{ color: "#e2e8f0" }}
              />
              <Bar dataKey="score" radius={[4, 4, 0, 0]}>
                {data.map((entry, i) => (
                  <Cell key={i} fill={entry.score >= 65 ? "#059669" : entry.score >= 50 ? "#eab308" : "#ef4444"} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        ) : (
          <div className="h-full w-full rounded-xl bg-white/[0.02] animate-pulse" />
        )}
      </div>
      <div className="mt-4 flex items-center gap-4 text-xs text-muted-foreground">
        <div className="flex items-center gap-1.5"><span className="h-2 w-2 rounded-full bg-emerald-500" /> Score global ajusté</div>
      </div>
    </motion.div>
  );
}

/* ─── RecommendationsTable ─── */

export function RecommendationsTable({ recos }: { recos: Reco[] }) {
  return (
    <motion.div
      variants={fadeIn}
      initial="initial"
      whileInView="animate"
      viewport={{ once: true }}
      className="glass rounded-2xl border border-white/[0.06] p-6"
    >
      <div className="flex items-center gap-2 mb-4">
        <Target className="h-5 w-5 text-accent" />
        <h3 className="font-semibold text-foreground">Recommandations</h3>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-white/[0.06] text-xs text-muted-foreground">
              <th className="pb-3 pr-4 text-left font-medium">Ticker</th>
              <th className="pb-3 pr-4 text-left font-medium">Action</th>
              <th className="pb-3 pr-4 text-right font-medium">Score</th>
              <th className="pb-3 pr-4 text-right font-medium">Catalyseur</th>
              <th className="pb-3 pr-4 text-right font-medium">Valorisation</th>
              <th className="pb-3 pr-4 text-right font-medium">Momentum</th>
              <th className="pb-3 pr-4 text-right font-medium">Prix</th>
              <th className="pb-3 text-right font-medium">R/R</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/[0.04]">
            {recos.map((r) => (
              <tr key={r.ticker} className="group hover:bg-white/[0.02] transition-colors">
                <td className="py-3 pr-4 font-semibold text-foreground">{r.ticker}</td>
                <td className="py-3 pr-4">
                  <span className={`inline-flex rounded-lg border px-2 py-0.5 text-xs font-semibold ${actionColor(r.action)}`}>
                    {r.action}
                  </span>
                </td>
                <td className={`py-3 pr-4 text-right font-bold ${scoreColor(r.score_global_ajuste)}`}>
                  {r.score_global_ajuste}
                </td>
                <td className="py-3 pr-4 text-right text-muted-foreground">{r.score_catalyseur}</td>
                <td className="py-3 pr-4 text-right text-muted-foreground">{r.score_valorisation}</td>
                <td className="py-3 pr-4 text-right text-muted-foreground">{r.score_momentum}</td>
                <td className="py-3 pr-4 text-right text-muted-foreground">${fmtPrice(r.prix_actuel)}</td>
                <td className="py-3 text-right text-muted-foreground">{r.risque_rendement_ratio}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </motion.div>
  );
}

/* ─── TickerDetailModal ─── */

interface UpcomingEvent {
  type: string;
  date: string;
  days_until: number;
  details: string;
  severity: string;
}

function TickerDetailModal({
  ticker,
  price,
  reco,
  events,
  onClose,
}: {
  ticker: string;
  price: TickerData;
  reco: Reco | undefined;
  events: UpcomingEvent[];
  onClose: () => void;
}) {
  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
      onClick={onClose}
    >
      <motion.div
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.95, y: 20 }}
        transition={{ duration: 0.2 }}
        onClick={(e) => e.stopPropagation()}
        className="glass rounded-2xl border border-white/[0.08] p-6 max-w-lg w-full max-h-[80vh] overflow-y-auto shadow-2xl"
      >
        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <div>
            <div className="text-xl font-bold text-foreground">{ticker}</div>
            <div className="text-xs text-muted-foreground">{price.fundamentals.sector}</div>
          </div>
          <div className="flex items-center gap-2">
            {reco && (
              <span
                className={`inline-flex rounded-lg border px-2 py-0.5 text-xs font-semibold ${actionColor(reco.action)}`}
              >
                {reco.action}
              </span>
            )}
            <button
              onClick={onClose}
              className="ml-1 inline-flex h-7 w-7 items-center justify-center rounded-lg text-muted-foreground hover:bg-white/[0.06] hover:text-foreground transition-colors"
            >
              ✕
            </button>
          </div>
        </div>

        {/* Prix & Niveaux */}
        <div className="grid grid-cols-2 gap-3 mb-5">
          <div className="rounded-xl bg-white/[0.03] border border-white/[0.04] p-3">
            <div className="text-xs text-muted-foreground mb-0.5">Prix actuel</div>
            <div className="text-lg font-bold text-foreground">${fmtPrice(price.price.close)}</div>
          </div>
          <div className="rounded-xl bg-white/[0.03] border border-white/[0.04] p-3">
            <div className="text-xs text-muted-foreground mb-0.5">Prix cible</div>
            <div className="text-lg font-bold text-emerald-400">
              ${fmtPrice(reco?.take_profit ?? price.options?.max_pain ?? 0)}
            </div>
          </div>
          <div className="rounded-xl bg-white/[0.03] border border-white/[0.04] p-3">
            <div className="text-xs text-muted-foreground mb-0.5">Stop-loss</div>
            <div className="text-lg font-bold text-red-400">${fmtPrice(reco?.stop_loss ?? 0)}</div>
          </div>
          <div className="rounded-xl bg-white/[0.03] border border-white/[0.04] p-3">
            <div className="text-xs text-muted-foreground mb-0.5">Ratio R/R</div>
            <div className="text-lg font-bold text-foreground">{reco?.risque_rendement_ratio ?? "—"}</div>
          </div>
        </div>

        {/* Scores */}
        {reco && (
          <div className="grid grid-cols-4 gap-2 mb-5">
            {[
              { label: "Global", value: reco.score_global_ajuste },
              { label: "Catalyseur", value: reco.score_catalyseur },
              { label: "Valorisation", value: reco.score_valorisation },
              { label: "Momentum", value: reco.score_momentum },
            ].map((s) => (
              <div key={s.label} className="rounded-lg bg-white/[0.03] border border-white/[0.04] p-2 text-center">
                <div className="text-[10px] text-muted-foreground uppercase tracking-wide">{s.label}</div>
                <div className={`text-sm font-bold ${scoreColor(s.value)}`}>{s.value}</div>
              </div>
            ))}
          </div>
        )}

        {/* Justification */}
        {reco?.justification && reco.justification.length > 0 && (
          <div className="mb-5">
            <div className="text-sm font-semibold text-foreground mb-2 flex items-center gap-1.5">
              <TrendingUp className="h-4 w-4 text-accent" />
              Pourquoi acheter
            </div>
            <ul className="space-y-2">
              {reco.justification.map((j, i) => (
                <li key={i} className="text-xs text-muted-foreground flex items-start gap-2">
                  <ArrowRight className="h-3 w-3 mt-0.5 text-accent shrink-0" />
                  <span className="leading-relaxed">{j}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Risques */}
        {reco?.risques && reco.risques.length > 0 && (
          <div className="mb-5">
            <div className="text-sm font-semibold text-foreground mb-2 flex items-center gap-1.5">
              <AlertTriangle className="h-4 w-4 text-red-400" />
              Risques identifiés
            </div>
            <ul className="space-y-2">
              {reco.risques.map((r, i) => (
                <li key={i} className="text-xs text-red-400 flex items-start gap-2">
                  <span className="mt-1 h-1 w-1 rounded-full bg-red-400 shrink-0" />
                  <span className="leading-relaxed">{r}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Horizon objectif */}
        {reco && (
          <div className="mb-5 rounded-xl bg-accent/5 border border-accent/15 px-3 py-2.5 flex items-center gap-2">
            <Clock className="h-4 w-4 text-accent" />
            <span className="text-xs text-muted-foreground">Objectif de prix cible : </span>
            <span className="text-xs font-semibold text-foreground">{reco.horizon}</span>
          </div>
        )}

        {/* Prochains événements */}
        {events.length > 0 && (
          <div className="mb-5">
            <div className="text-sm font-semibold text-foreground mb-2 flex items-center gap-1.5">
              <Calendar className="h-4 w-4 text-accent" />
              Prochains événements
            </div>
            <ul className="space-y-2">
              {events.map((ev, i) => {
                const isSoon = ev.days_until <= 7;
                const isVerySoon = ev.days_until <= 3;
                return (
                  <li
                    key={i}
                    className={`text-xs flex items-start gap-2 rounded-lg border p-2 ${
                      isVerySoon
                        ? "bg-red-500/5 border-red-500/20 text-red-400"
                        : isSoon
                        ? "bg-yellow-500/5 border-yellow-500/20 text-yellow-400"
                        : "bg-white/[0.03] border-white/[0.04] text-muted-foreground"
                    }`}
                  >
                    <span className="mt-0.5 shrink-0">
                      {isVerySoon ? "🔴" : isSoon ? "🟡" : "🟢"}
                    </span>
                    <div className="leading-relaxed">
                      <span className="font-medium">{ev.type.toUpperCase()}</span>{" "}
                      — dans <span className="font-medium">{ev.days_until}j</span>{" "}
                      ({ev.date})
                      <br />
                      <span className="opacity-80">{ev.details}</span>
                    </div>
                  </li>
                );
              })}
            </ul>
          </div>
        )}

        {/* Meta */}
        {reco && (
          <div className="flex flex-wrap gap-2 text-xs text-muted-foreground">
            <span className="rounded-lg bg-white/[0.03] border border-white/[0.04] px-2 py-1">
              Timing: <span className="text-foreground font-medium">{reco.timing}</span>
            </span>
            <span className="rounded-lg bg-white/[0.03] border border-white/[0.04] px-2 py-1">
              Sizing: <span className="text-foreground font-medium">{reco.sizing}</span>
            </span>
          </div>
        )}
      </motion.div>
    </div>
  );
}

/* ─── TickerGrid ─── */

export function TickerGrid({
  tickers,
  recos,
  events,
}: {
  tickers: Record<string, TickerData>;
  recos: Record<string, Reco>;
  events: Record<string, UpcomingEvent[]>;
}) {
  const [selectedTicker, setSelectedTicker] = useState<string | null>(null);
  const selectedPrice = selectedTicker ? tickers[selectedTicker] : undefined;
  const selectedReco = selectedTicker ? recos[selectedTicker] : undefined;
  const selectedEvents = selectedTicker ? events[selectedTicker] ?? [] : [];

  return (
    <>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {Object.values(tickers).map((t, i) => {
          const change = t.price.change_pct;
          const changeColor = change > 0 ? "text-emerald-400" : change < 0 ? "text-red-400" : "text-muted-foreground";
          const ChangeIcon = change > 0 ? TrendingUp : change < 0 ? TrendingDown : Minus;
          const rsi = t.technical.rsi14;
          const rsiColor = rsi > 70 ? "text-red-400" : rsi < 30 ? "text-emerald-400" : "text-muted-foreground";
          const volRatio = t.price.volume / t.price.volume_avg_20d;
          const reco = recos[t.ticker];
          const targetPrice = reco?.take_profit ?? t.options?.max_pain ?? 0;
          const upside = targetPrice > 0 && t.price.close > 0 ? ((targetPrice - t.price.close) / t.price.close) * 100 : 0;
          const tickerEvents = events[t.ticker] ?? [];
          const nearestEvent = tickerEvents[0];
          const hasUrgentEvent = nearestEvent && nearestEvent.days_until <= 7;

          return (
            <motion.div
              key={t.ticker}
              variants={fadeIn}
              initial="initial"
              whileInView="animate"
              viewport={{ once: true }}
              transition={{ delay: i * 0.06 }}
              whileHover={{ y: -3 }}
              onClick={() => setSelectedTicker(t.ticker)}
              className="glass rounded-2xl border border-white/[0.06] p-5 hover:border-white/[0.12] transition-colors cursor-pointer"
            >
              <div className="flex items-center justify-between mb-3">
                <div>
                  <div className="text-lg font-bold text-foreground">{t.ticker}</div>
                  <div className="text-xs text-muted-foreground">{t.fundamentals.sector}</div>
                </div>
                <div className={`flex items-center gap-1 rounded-lg px-2 py-1 text-xs font-semibold ${changeColor} bg-white/[0.03]`}>
                  <ChangeIcon className="h-3 w-3" />
                  {fmtPct(change)}
                </div>
              </div>

              <div className="mb-4">
                <span className="text-2xl font-bold text-foreground">${fmtPrice(t.price.close)}</span>
                <span className="ml-2 text-xs text-muted-foreground">Vol {volRatio.toFixed(1)}× avg</span>
              </div>

              {/* Prix cible + horizon */}
              {targetPrice > 0 && (
                <div className="mb-3">
                  <div className="flex items-center justify-between rounded-lg bg-emerald-500/5 border border-emerald-500/10 px-3 py-2">
                    <div className="flex items-center gap-1.5 text-xs text-muted-foreground">
                      <Target className="h-3 w-3 text-emerald-400" />
                      Prix cible
                    </div>
                    <div className="text-sm font-semibold text-emerald-400">
                      ${fmtPrice(targetPrice)}
                      <span className="ml-1.5 text-xs font-normal text-emerald-400/80">
                        {upside > 0 ? `+${upside.toFixed(1)}%` : `${upside.toFixed(1)}%`}
                      </span>
                    </div>
                  </div>
                  {reco?.horizon && (
                    <div className="mt-1 flex items-center gap-1 text-[10px] text-muted-foreground">
                      <Clock className="h-2.5 w-2.5" />
                      Objectif : {reco.horizon}
                    </div>
                  )}
                </div>
              )}

              {/* Badge événement urgent */}
              {hasUrgentEvent && nearestEvent && (
                <div className={`mb-3 flex items-center gap-1.5 rounded-lg px-2 py-1.5 text-xs ${
                  nearestEvent.days_until <= 3
                    ? "bg-red-500/10 border border-red-500/20 text-red-400"
                    : "bg-yellow-500/10 border border-yellow-500/20 text-yellow-400"
                }`}>
                  <Calendar className="h-3 w-3" />
                  <span className="font-medium">{nearestEvent.type.toUpperCase()}</span>
                  <span>— dans {nearestEvent.days_until}j</span>
                </div>
              )}

              <div className="grid grid-cols-3 gap-2 text-xs">
                <div className="rounded-lg bg-white/[0.03] p-2 text-center">
                  <div className="text-muted-foreground mb-0.5">RSI</div>
                  <div className={`font-semibold ${rsiColor}`}>{rsi.toFixed(1)}</div>
                </div>
                <div className="rounded-lg bg-white/[0.03] p-2 text-center">
                  <div className="text-muted-foreground mb-0.5">ATR</div>
                  <div className="font-semibold text-foreground">{t.technical.atr14?.toFixed(2)}</div>
                </div>
                <div className="rounded-lg bg-white/[0.03] p-2 text-center">
                  <div className="text-muted-foreground mb-0.5">MM50</div>
                  <div className="font-semibold text-foreground">{t.technical.mm50 ? fmtPrice(t.technical.mm50) : "—"}</div>
                </div>
              </div>

              <div className="mt-3 flex items-center justify-between text-xs text-muted-foreground">
                <span>Cap: {fmtB(t.fundamentals.market_cap)}</span>
                <span>P/E: {t.fundamentals.pe_ratio?.toFixed(1) ?? "—"}</span>
                <span>Beta: {t.fundamentals.beta?.toFixed(2) ?? "—"}</span>
              </div>

              {t._quality_gate.status !== "ok" && (
                <div className="mt-2 flex items-center gap-1.5 rounded-lg bg-red-500/10 px-2 py-1 text-xs text-red-400">
                  <AlertTriangle className="h-3 w-3" />
                  Quality gate: {t._quality_gate.status}
                </div>
              )}

              {reco && (
                <div className="mt-2 flex items-center gap-1.5 text-xs text-muted-foreground">
                  <ArrowRight className="h-3 w-3 text-accent" />
                  <span className="text-foreground font-medium">{reco.action}</span>
                  <span>· Score {reco.score_global_ajuste}</span>
                </div>
              )}
            </motion.div>
          );
        })}
      </div>

      <AnimatePresence>
        {selectedTicker && selectedPrice && (
          <TickerDetailModal
            ticker={selectedTicker}
            price={selectedPrice}
            reco={selectedReco}
            events={selectedEvents}
            onClose={() => setSelectedTicker(null)}
          />
        )}
      </AnimatePresence>
    </>
  );
}

/* ─── QuantPanel ─── */

export function QuantPanel({ quant }: { quant: QuantReport }) {
  const sig = quant.significance;
  const risk = quant.risk_metrics;

  const metrics = [
    { label: "Win rate", value: `${(sig.win_rate_observed * 100).toFixed(1)}%`, color: sig.win_rate_observed >= 0.5 ? "text-emerald-400" : "text-red-400", icon: Target },
    { label: "P-value", value: sig.p_value.toFixed(3), color: sig.p_value < 0.05 ? "text-emerald-400" : "text-yellow-400", icon: Crosshair },
    { label: "Sharpe", value: risk.sharpe.toFixed(2), color: risk.sharpe > 0 ? "text-emerald-400" : "text-red-400", icon: TrendingUp },
    { label: "Max DD", value: `${(risk.max_drawdown * 100).toFixed(1)}%`, color: "text-red-400", icon: TrendingDown },
    { label: "W/L ratio", value: risk.win_loss_ratio.toFixed(2), color: "text-foreground", icon: Scale },
    { label: "Expectancy", value: risk.expectancy.toFixed(3), color: risk.expectancy > 0 ? "text-emerald-400" : "text-red-400", icon: DollarSign },
  ];

  return (
    <motion.div
      variants={fadeIn}
      initial="initial"
      whileInView="animate"
      viewport={{ once: true }}
      className="glass rounded-2xl border border-white/[0.06] p-6"
    >
      <div className="flex items-center gap-2 mb-4">
        <Cpu className="h-5 w-5 text-accent" />
        <h3 className="font-semibold text-foreground">Validation Quant</h3>
        <span className={`ml-auto inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-xs font-medium ${sig.conclusion === "Significatif" ? "bg-emerald-500/10 text-emerald-400" : "bg-yellow-500/10 text-yellow-400"}`}>
          {sig.conclusion}
        </span>
      </div>

      {sig.alert && (
        <div className="mb-4 flex items-center gap-2 rounded-xl bg-yellow-500/10 border border-yellow-500/20 px-3 py-2 text-xs text-yellow-400">
          <AlertTriangle className="h-4 w-4" />
          {sig.alert}
        </div>
      )}

      <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
        {metrics.map((m) => (
          <div key={m.label} className="rounded-xl border border-white/[0.06] bg-white/[0.02] p-3">
            <div className="flex items-center gap-1.5 mb-1 text-xs text-muted-foreground">
              <m.icon className="h-3 w-3" />
              {m.label}
            </div>
            <div className={`text-lg font-bold ${m.color}`}>{m.value}</div>
          </div>
        ))}
      </div>
    </motion.div>
  );
}

/* ─── RiskPanels ─── */

export function RiskPanels({
  quality,
  geo,
  fx,
  crypto,
  social,
}: {
  quality: QualityReport;
  geo: GeoReport;
  fx: FXReport;
  crypto: CryptoReport;
  social: SocialReport;
}) {
  const okTickers = Object.values(quality.tickers).filter((t) => t.status === "ok").length;
  const flaggedGeo = Object.values(geo.ticker_exposure).filter((t) => t.geo_risk_score >= 5).length;
  const flaggedFX = fx.tickers.filter((t) => t.fx_impact_score >= 5).length;
  const pumpAlerts = Object.values(social.analysis).filter((s) => s.pump_detected).length;
  const sentimentAlerts = Object.values(social.analysis).filter((s) => s.sentiment_score >= 8.5 || s.sentiment_score <= 1.5).length;

  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {/* Quality Gate */}
      <motion.div
        variants={fadeIn}
        initial="initial"
        whileInView="animate"
        viewport={{ once: true }}
        className="glass rounded-2xl border border-white/[0.06] p-5"
      >
        <div className="flex items-center gap-2 mb-3">
          <Shield className="h-4 w-4 text-accent" />
          <span className="text-sm font-medium text-foreground">Quality Gate</span>
        </div>
        <div className="flex items-center gap-2 mb-2">
          <CheckCircle2 className="h-5 w-5 text-emerald-400" />
          <span className="text-2xl font-bold text-emerald-400">{okTickers}</span>
          <span className="text-sm text-muted-foreground">/ {quality.meta.tickers_scanned} OK</span>
        </div>
        {quality.global.summary.warning > 0 && (
          <div className="text-xs text-yellow-400">{quality.global.summary.warning} warning(s)</div>
        )}
        {quality.global.summary.excluded > 0 && (
          <div className="text-xs text-red-400">{quality.global.summary.excluded} excluded</div>
        )}
      </motion.div>

      {/* Geo Risk */}
      <motion.div
        variants={fadeIn}
        initial="initial"
        whileInView="animate"
        viewport={{ once: true }}
        className="glass rounded-2xl border border-white/[0.06] p-5"
      >
        <div className="flex items-center gap-2 mb-3">
          <Globe className="h-4 w-4 text-accent" />
          <span className="text-sm font-medium text-foreground">Géopolitique</span>
        </div>
        <div className="text-2xl font-bold text-foreground mb-1">
          {geo.meta.events_detected} <span className="text-sm font-normal text-muted-foreground">événements</span>
        </div>
        {flaggedGeo > 0 ? (
          <div className="text-xs text-red-400">{flaggedGeo} ticker(s) à risque élevé</div>
        ) : (
          <div className="text-xs text-emerald-400">Aucun risque élevé détecté</div>
        )}
      </motion.div>

      {/* FX */}
      <motion.div
        variants={fadeIn}
        initial="initial"
        whileInView="animate"
        viewport={{ once: true }}
        className="glass rounded-2xl border border-white/[0.06] p-5"
      >
        <div className="flex items-center gap-2 mb-3">
          <DollarSign className="h-4 w-4 text-accent" />
          <span className="text-sm font-medium text-foreground">FX Exposure</span>
        </div>
        <div className="text-2xl font-bold text-foreground mb-1">
          {fx.meta.flagged_high} <span className="text-sm font-normal text-muted-foreground">flagged</span>
        </div>
        <div className="text-xs text-muted-foreground">
          {fx.meta.tickers_analyzed} tickers analysés · DXY {fx.meta.dxy_change_pct > 0 ? "+" : ""}{fx.meta.dxy_change_pct}%
        </div>
      </motion.div>

      {/* Social + Crypto */}
      <motion.div
        variants={fadeIn}
        initial="initial"
        whileInView="animate"
        viewport={{ once: true }}
        className="glass rounded-2xl border border-white/[0.06] p-5"
      >
        <div className="flex items-center gap-2 mb-3">
          <MessageSquare className="h-4 w-4 text-accent" />
          <span className="text-sm font-medium text-foreground">Sentiment</span>
        </div>
        <div className="flex items-center gap-3 mb-2">
          <div className="text-2xl font-bold text-foreground">{pumpAlerts}</div>
          <div className="text-xs text-muted-foreground">pump alerts</div>
        </div>
        <div className="flex items-center gap-3">
          <div className="text-2xl font-bold text-foreground">{sentimentAlerts}</div>
          <div className="text-xs text-muted-foreground">extrêmes</div>
        </div>
        {crypto.meta.btc_price && (
          <div className="mt-2 flex items-center gap-1.5 text-xs text-muted-foreground">
            <Bitcoin className="h-3 w-3" />
            BTC ${crypto.meta.btc_price.toLocaleString()}
          </div>
        )}
      </motion.div>
    </div>
  );
}

/* ─── PipelineStatus ─── */

export function PipelineStatus({
  agents = ["learn", "quant", "geo", "crypto", "prices", "macro", "watchman", "accounting", "sector", "social", "fx", "event", "reco", "paper", "validate", "transcripts", "news", "calendar"],
  okAgents = 18,
}: {
  agents?: string[];
  okAgents?: number;
}) {
  return (
    <motion.div
      variants={fadeIn}
      initial="initial"
      whileInView="animate"
      viewport={{ once: true }}
      className="glass rounded-2xl border border-white/[0.06] p-6"
    >
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Activity className="h-5 w-5 text-accent" />
          <h3 className="font-semibold text-foreground">Pipeline Status</h3>
        </div>
        <span className="inline-flex items-center gap-1.5 rounded-full bg-emerald-500/10 px-2.5 py-1 text-xs font-medium text-emerald-400">
          <span className="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse" />
          {okAgents}/{agents.length} agents OK
        </span>
      </div>

      <div className="flex flex-wrap gap-2">
        {agents.map((a) => (
          <div
            key={a}
            className="inline-flex items-center gap-1.5 rounded-lg border border-white/[0.06] bg-white/[0.02] px-2.5 py-1 text-xs text-muted-foreground"
          >
            <CheckCircle2 className="h-3 w-3 text-emerald-400" />
            {a}
          </div>
        ))}
      </div>
    </motion.div>
  );
}

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
  Cloud,
  Server,
  RefreshCw,
  Play,
  Terminal,
  Loader2,
  Search,
  Database,
  FileText,
  Check,
  X,
  ListChecks,
  Sparkles,
  UserCheck,
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

export interface TickerData {
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
  _no_data?: boolean;
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
  geo,
  onClose,
}: {
  ticker: string;
  price: TickerData;
  reco: Reco | undefined;
  events: UpcomingEvent[];
  geo: { geo_risk_score: number; flag: string } | undefined;
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
        className="glass rounded-2xl border border-white/[0.08] p-4 sm:p-6 max-w-lg w-full max-h-[85vh] overflow-y-auto shadow-2xl"
      >
        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <div>
            <div className="text-xl font-bold text-foreground">{ticker}</div>
            <div className="text-xs text-muted-foreground">{price.fundamentals?.sector ?? "—"}</div>
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
        {price._no_data ? (
          <div className="mb-5 rounded-xl bg-yellow-500/5 border border-yellow-500/20 p-3 flex items-center gap-2 text-xs text-yellow-400">
            <AlertTriangle className="h-4 w-4" />
            Données techniques manquantes — exécuter fetch_prices.py pour obtenir RSI, ATR, consensus, options.
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-5">
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
        )}

        {/* Scores */}
        {reco && (
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-5">
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

        {/* Géopolitique */}
        {geo && (
          <div className="mb-5">
            <div className="text-sm font-semibold text-foreground mb-2 flex items-center gap-1.5">
              <Globe className="h-4 w-4 text-accent" />
              Risque géopolitique
            </div>
            <div className={`flex items-center gap-3 rounded-lg border p-2.5 ${
              geo.flag === "high"
                ? "bg-red-500/5 border-red-500/20 text-red-400"
                : geo.flag === "moderate"
                ? "bg-yellow-500/5 border-yellow-500/20 text-yellow-400"
                : "bg-emerald-500/5 border-emerald-500/20 text-emerald-400"
            }`}>
              <div className="text-lg font-bold">{geo.geo_risk_score}/10</div>
              <div className="text-xs leading-relaxed">
                <span className="font-medium">
                  {geo.flag === "high" ? "Risque élevé" : geo.flag === "moderate" ? "Risque modéré" : "Risque faible"}
                </span>
                {ticker === "IREN" && (
                  <span className="block mt-0.5 opacity-80">Régulation crypto aux US = impact majeur potentiel sur le business legacy</span>
                )}
              </div>
            </div>
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
  geo,
}: {
  tickers: Record<string, TickerData>;
  recos: Record<string, Reco>;
  events: Record<string, UpcomingEvent[]>;
  geo: GeoReport;
}) {
  const [selectedTicker, setSelectedTicker] = useState<string | null>(null);
  const selectedPrice = selectedTicker ? tickers[selectedTicker] : undefined;
  const selectedReco = selectedTicker ? recos[selectedTicker] : undefined;
  const selectedEvents = selectedTicker ? events[selectedTicker] ?? [] : [];
  const selectedGeo = selectedTicker ? geo.ticker_exposure?.[selectedTicker] : undefined;

  return (
    <>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {Object.values(tickers).map((t, i) => {
          const hasData = !t._no_data && t.price != null;
          const change = t.price?.change_pct ?? 0;
          const changeColor = change > 0 ? "text-emerald-400" : change < 0 ? "text-red-400" : "text-muted-foreground";
          const ChangeIcon = change > 0 ? TrendingUp : change < 0 ? TrendingDown : Minus;
          const rsi = t.technical?.rsi14 ?? 0;
          const rsiColor = rsi > 70 ? "text-red-400" : rsi < 30 ? "text-emerald-400" : "text-muted-foreground";
          const volRatio = t.price?.volume_avg_20d ? (t.price?.volume ?? 0) / t.price.volume_avg_20d : 0;
          const reco = recos[t.ticker];
          const targetPrice = reco?.take_profit ?? t.options?.max_pain ?? 0;
          const upside = targetPrice > 0 && (t.price?.close ?? 0) > 0 ? ((targetPrice - t.price.close) / t.price.close) * 100 : 0;
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
                  <div className="text-xs text-muted-foreground">{t.fundamentals?.sector ?? "—"}</div>
                </div>
                {hasData ? (
                  <div className={`flex items-center gap-1 rounded-lg px-2 py-1 text-xs font-semibold ${changeColor} bg-white/[0.03]`}>
                    <ChangeIcon className="h-3 w-3" />
                    {fmtPct(change)}
                  </div>
                ) : (
                  <div className="flex items-center gap-1 rounded-lg px-2 py-1 text-xs font-semibold text-yellow-400 bg-yellow-500/10">
                    <AlertTriangle className="h-3 w-3" />
                    Données à venir
                  </div>
                )}
              </div>

              <div className="mb-4">
                {hasData ? (
                  <>
                    <span className="text-2xl font-bold text-foreground">${fmtPrice(t.price?.close ?? 0)}</span>
                    <span className="ml-2 text-xs text-muted-foreground">Vol {Number.isFinite(volRatio) ? volRatio.toFixed(1) : "—"}× avg</span>
                  </>
                ) : (
                  <span className="text-2xl font-bold text-muted-foreground/50">$—</span>
                )}
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
                        {typeof upside === 'number' ? (upside > 0 ? `+${upside.toFixed(1)}%` : `${upside.toFixed(1)}%`) : "—"}
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

              {/* Badge événement urgent — hauteur fixe pour alignement entre cartes */}
              <div className="mb-3 min-h-[28px] flex items-center">
                {hasUrgentEvent && nearestEvent ? (
                  <div className={`flex items-center gap-1.5 rounded-lg px-2 py-1.5 text-xs w-full ${
                    nearestEvent.days_until <= 3
                      ? "bg-red-500/10 border border-red-500/20 text-red-400"
                      : "bg-yellow-500/10 border border-yellow-500/20 text-yellow-400"
                  }`}>
                    <Calendar className="h-3 w-3" />
                    <span className="font-medium">{nearestEvent.type.toUpperCase()}</span>
                    <span>— dans {nearestEvent.days_until}j</span>
                  </div>
                ) : null}
              </div>

              {/* RSI / ATR / MM50 — aligné entre tickets via grille unifiée */}
              <div className="mt-3 grid grid-cols-3 gap-0 text-xs border-t border-white/[0.04] pt-3">
                <div className="text-center px-1">
                  <div className="text-[10px] text-muted-foreground uppercase tracking-wide mb-0.5">RSI</div>
                  <div className={`font-semibold tabular-nums ${hasData ? rsiColor : "text-muted-foreground/50"}`}>
                    {hasData && rsi != null ? rsi.toFixed(1) : "—"}
                  </div>
                </div>
                <div className="text-center px-1 border-x border-white/[0.04]">
                  <div className="text-[10px] text-muted-foreground uppercase tracking-wide mb-0.5">ATR</div>
                  <div className="font-semibold text-foreground tabular-nums">
                    {hasData ? t.technical.atr14?.toFixed(2) : "—"}
                  </div>
                </div>
                <div className="text-center px-1">
                  <div className="text-[10px] text-muted-foreground uppercase tracking-wide mb-0.5">MM50</div>
                  <div className="font-semibold text-foreground tabular-nums">
                    {hasData ? (t.technical.mm50 ? fmtPrice(t.technical.mm50) : "—") : "—"}
                  </div>
                </div>
              </div>

              {/* Cap / P/E / Beta — même alignement */}
              <div className="mt-2 grid grid-cols-3 gap-0 text-[10px] text-muted-foreground border-t border-white/[0.04] pt-2">
                <div className="text-center px-1 tabular-nums">
                  Cap: {hasData ? fmtB(t.fundamentals.market_cap) : "—"}
                </div>
                <div className="text-center px-1 border-x border-white/[0.04] tabular-nums">
                  P/E: {hasData ? (t.fundamentals.pe_ratio?.toFixed(1) ?? "—") : "—"}
                </div>
                <div className="text-center px-1 tabular-nums">
                  Beta: {hasData ? (t.fundamentals.beta?.toFixed(2) ?? "—") : "—"}
                </div>
              </div>

              <div className="mt-2 min-h-[22px] flex items-center">
                {t._quality_gate && t._quality_gate.status !== "ok" && (
                  <div className="flex items-center gap-1.5 rounded-lg bg-red-500/10 px-2 py-1 text-xs text-red-400">
                    <AlertTriangle className="h-3 w-3" />
                    Quality gate: {t._quality_gate.status}
                  </div>
                )}
              </div>

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
            geo={selectedGeo}
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
    { label: "Win rate", value: `${((sig?.win_rate_observed ?? 0) * 100).toFixed(1)}%`, color: (sig?.win_rate_observed ?? 0) >= 0.5 ? "text-emerald-400" : "text-red-400", icon: Target },
    { label: "P-value", value: (sig?.p_value ?? 1)?.toFixed(3), color: (sig?.p_value ?? 1) < 0.05 ? "text-emerald-400" : "text-yellow-400", icon: Crosshair },
    { label: "Sharpe", value: (risk?.sharpe ?? 0)?.toFixed(2), color: (risk?.sharpe ?? 0) > 0 ? "text-emerald-400" : "text-red-400", icon: TrendingUp },
    { label: "Max DD", value: `${((risk?.max_drawdown ?? 0) * 100).toFixed(1)}%`, color: "text-red-400", icon: TrendingDown },
    { label: "W/L ratio", value: (risk?.win_loss_ratio ?? 0)?.toFixed(2), color: "text-foreground", icon: Scale },
    { label: "Expectancy", value: (risk?.expectancy ?? 0)?.toFixed(3), color: (risk?.expectancy ?? 0) > 0 ? "text-emerald-400" : "text-red-400", icon: DollarSign },
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
        <span className={`ml-auto inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-xs font-medium ${(sig?.conclusion ?? "") === "Significatif" ? "bg-emerald-500/10 text-emerald-400" : "bg-yellow-500/10 text-yellow-400"}`}>
          {sig?.conclusion ?? "N/A"}
        </span>
      </div>

      {sig?.alert && (
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

/* ─── OllamaUsagePanel ─── */

interface OllamaConfig {
  tier: string;
  tier_label: string;
  window_5h_limit: number;
  weekly_limit: number;
  model: string;
  endpoint: string;
  enabled: boolean;
}

interface OllamaUsage {
  window_5h_start: string;
  window_5h_calls: number;
  window_5h_tokens_input: number;
  window_5h_tokens_output: number;
  week_start: string;
  weekly_calls: number;
  weekly_tokens_input: number;
  weekly_tokens_output: number;
}

export function OllamaUsagePanel({
  config: initialConfig,
  usage: initialUsage,
}: {
  config: OllamaConfig | null;
  usage: OllamaUsage | null;
}) {
  const [config, setConfig] = useState<OllamaConfig | null>(initialConfig);
  const [usage, setUsage] = useState<OllamaUsage | null>(initialUsage);
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  const fetchData = async () => {
    try {
      setRefreshing(true);
      const [uRes, cRes] = await Promise.all([
        fetch(`/data/ollama_usage.json?_=${Date.now()}`, { cache: "no-store" }),
        fetch(`/data/ollama_config.json?_=${Date.now()}`, { cache: "no-store" }),
      ]);
      if (uRes.ok) {
        const u = await uRes.json();
        setUsage(u);
      }
      if (cRes.ok) {
        const c = await cRes.json();
        setConfig(c);
      }
      setLastUpdated(new Date());
    } catch {
      // ignore network errors silently
    } finally {
      setRefreshing(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 10000); // refresh every 10s
    return () => clearInterval(interval);
  }, []);

  if (!config || !config.enabled) {
    return (
      <motion.div
        variants={fadeIn}
        initial="initial"
        whileInView="animate"
        viewport={{ once: true }}
        className="glass rounded-2xl border border-white/[0.06] p-6"
      >
        <div className="flex items-center gap-2 mb-4">
          <Cloud className="h-5 w-5 text-accent" />
          <h3 className="font-semibold text-foreground">Ollama Cloud</h3>
        </div>
        <div className="text-sm text-muted-foreground">
          Intégration Ollama non configurée. Créer <code className="text-xs bg-white/[0.04] px-1.5 py-0.5 rounded">data/ollama_config.json</code> pour activer.
        </div>
      </motion.div>
    );
  }

  const winPct = config.window_5h_limit > 0 ? Math.min((usage?.window_5h_calls ?? 0) / config.window_5h_limit, 1) : 0;
  const weeklyPct = config.weekly_limit > 0 ? Math.min((usage?.weekly_calls ?? 0) / config.weekly_limit, 1) : 0;
  const winRemaining = Math.max(config.window_5h_limit - (usage?.window_5h_calls ?? 0), 0);
  const weeklyRemaining = Math.max(config.weekly_limit - (usage?.weekly_calls ?? 0), 0);

  const windowStart = usage?.window_5h_start ? new Date(usage.window_5h_start) : new Date();
  const windowReset = new Date(windowStart.getTime() + 5 * 60 * 60 * 1000);
  const hoursUntilReset = Math.max(0, Math.floor((windowReset.getTime() - Date.now()) / 3600000));
  const minsUntilReset = Math.max(0, Math.floor(((windowReset.getTime() - Date.now()) % 3600000) / 60000));

  return (
    <motion.div
      variants={fadeIn}
      initial="initial"
      whileInView="animate"
      viewport={{ once: true }}
      className="glass rounded-2xl border border-white/[0.06] p-6"
    >
      <div className="flex items-center justify-between mb-5">
        <div className="flex items-center gap-2">
          <Cloud className="h-5 w-5 text-accent" />
          <h3 className="font-semibold text-foreground">Ollama Cloud</h3>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={fetchData}
            className="inline-flex items-center gap-1 rounded-lg border border-white/[0.06] bg-white/[0.02] px-2 py-1 text-[10px] text-muted-foreground hover:bg-white/[0.04] transition-colors"
            title="Rafraîchir"
          >
            <RefreshCw className={`h-3 w-3 ${refreshing ? "animate-spin" : ""}`} />
            {lastUpdated ? `${lastUpdated.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit", second: "2-digit" })}` : "—"}
          </button>
          <span className="inline-flex items-center gap-1.5 rounded-full bg-accent/10 px-2.5 py-1 text-xs font-medium text-accent">
            <Server className="h-3 w-3" />
            {config.tier_label}
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-5">
        <div className="rounded-xl border border-white/[0.06] bg-white/[0.02] p-3">
          <div className="text-xs text-muted-foreground mb-1">Fenêtre 5h</div>
          <div className="text-2xl font-bold text-foreground">{usage?.window_5h_calls ?? 0}</div>
          <div className="text-[10px] text-muted-foreground">limite {config.window_5h_limit.toLocaleString()}</div>
        </div>
        <div className="rounded-xl border border-white/[0.06] bg-white/[0.02] p-3">
          <div className="text-xs text-muted-foreground mb-1">Cette semaine</div>
          <div className="text-2xl font-bold text-foreground">{usage?.weekly_calls ?? 0}</div>
          <div className="text-[10px] text-muted-foreground">limite {config.weekly_limit.toLocaleString()}</div>
        </div>
      </div>

      {/* Barre fenêtre 5h */}
      <div className="mb-4">
        <div className="flex items-center justify-between text-xs mb-1.5">
          <span className="text-muted-foreground">Quota 5h</span>
          <span className="text-foreground font-medium">{winRemaining.toLocaleString()} restants · reset dans {hoursUntilReset}h{minsUntilReset}m</span>
        </div>
        <div className="h-2 w-full rounded-full bg-white/[0.04] overflow-hidden">
          <div
            className={`h-full rounded-full transition-all duration-500 ${
              winPct >= 0.9 ? "bg-red-500" : winPct >= 0.7 ? "bg-yellow-500" : "bg-emerald-500"
            }`}
            style={{ width: `${winPct * 100}%` }}
          />
        </div>
        <div className="text-[10px] text-muted-foreground mt-1">{Math.round(winPct * 100)}% utilisé</div>
      </div>

      {/* Barre hebdo */}
      <div className="mb-4">
        <div className="flex items-center justify-between text-xs mb-1.5">
          <span className="text-muted-foreground">Quota hebdo</span>
          <span className="text-foreground font-medium">{weeklyRemaining.toLocaleString()} restants</span>
        </div>
        <div className="h-2 w-full rounded-full bg-white/[0.04] overflow-hidden">
          <div
            className={`h-full rounded-full transition-all duration-500 ${
              weeklyPct >= 0.9 ? "bg-red-500" : weeklyPct >= 0.7 ? "bg-yellow-500" : "bg-emerald-500"
            }`}
            style={{ width: `${weeklyPct * 100}%` }}
          />
        </div>
        <div className="text-[10px] text-muted-foreground mt-1">{Math.round(weeklyPct * 100)}% utilisé</div>
      </div>

      {/* Tokens */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs border-t border-white/[0.04] pt-3">
        <div className="text-center">
          <div className="text-[10px] text-muted-foreground uppercase tracking-wide mb-0.5">Tokens IN</div>
          <div className="font-semibold text-foreground tabular-nums">{(usage?.window_5h_tokens_input ?? 0).toLocaleString()}</div>
        </div>
        <div className="text-center border-l border-white/[0.04]">
          <div className="text-[10px] text-muted-foreground uppercase tracking-wide mb-0.5">Tokens OUT</div>
          <div className="font-semibold text-foreground tabular-nums">{(usage?.window_5h_tokens_output ?? 0).toLocaleString()}</div>
        </div>
      </div>

      <div className="mt-3 text-[10px] text-muted-foreground">
        Modèle : <span className="text-foreground font-medium">{config.model}</span>
      </div>
    </motion.div>
  );
}

/* ─── LaunchAnalysis ─── */

export function LaunchAnalysis() {
  const [ticker, setTicker] = useState("");
  const [name, setName] = useState("");
  const [sector, setSector] = useState("");
  const [priority, setPriority] = useState("medium");
  const [exchange, setExchange] = useState("NASDAQ");
  const [customPrompt, setCustomPrompt] = useState("");
  const [showOptions, setShowOptions] = useState(false);
  const [jobId, setJobId] = useState<string | null>(null);
  const [status, setStatus] = useState<string | null>(null);
  const [logs, setLogs] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  async function startAnalysis() {
    const t = ticker.trim().toUpperCase();
    if (!t || t.length < 1 || t.length > 20) return;
    setLoading(true);
    setStatus("queued");
    setLogs([]);
    try {
      const params = new URLSearchParams({ ticker: t });
      if (name.trim()) params.set("name", name.trim());
      if (sector.trim()) params.set("sector", sector.trim());
      if (priority) params.set("priority", priority);
      if (exchange) params.set("exchange", exchange);

      const res = await fetch(`/api/analyse?${params.toString()}`, { method: "POST" });
      const data = await res.json();
      if (data.job_id) {
        setJobId(data.job_id);
        setStatus("queued");
      } else {
        setStatus("error");
        setLogs([data.error || "Erreur inconnue"]);
      }
    } catch (e) {
      setStatus("error");
      setLogs(["Impossible de contacter le serveur API"]);
    } finally {
      setLoading(false);
    }
  }

  async function startFullAnalysis() {
    const t = ticker.trim().toUpperCase();
    if (!t || t.length < 1 || t.length > 20) return;
    setLoading(true);
    setStatus("queued");
    setLogs([]);
    try {
      const params = new URLSearchParams({ ticker: t });
      if (name.trim()) params.set("name", name.trim());
      if (sector.trim()) params.set("sector", sector.trim());
      if (priority) params.set("priority", priority);
      if (exchange) params.set("exchange", exchange);

      const res = await fetch(`/api/analyse-complete?${params.toString()}`, { method: "POST" });
      const data = await res.json();
      if (data.job_id) {
        setJobId(data.job_id);
        setStatus("queued");
      } else {
        setStatus("error");
        setLogs([data.error || "Erreur inconnue"]);
      }
    } catch (e) {
      setStatus("error");
      setLogs(["Impossible de contacter le serveur API"]);
    } finally {
      setLoading(false);
    }
  }

  async function startClaudeAnalysis() {
    const t = ticker.trim().toUpperCase();
    if (!t || t.length < 1 || t.length > 20) return;
    setLoading(true);
    setStatus("queued");
    setLogs([]);
    try {
      const params = new URLSearchParams({ ticker: t });
      if (customPrompt.trim()) params.set("prompt", customPrompt.trim());

      const res = await fetch(`/api/analyse-claude?${params.toString()}`, { method: "POST" });
      const data = await res.json();
      if (data.job_id) {
        setJobId(data.job_id);
        setStatus("queued");
      } else {
        setStatus("error");
        setLogs([data.error || "Erreur inconnue"]);
      }
    } catch (e) {
      setStatus("error");
      setLogs(["Impossible de contacter le serveur API"]);
    } finally {
      setLoading(false);
    }
  }

  async function startUpdateAllAnalysis() {
    setLoading(true);
    setStatus("queued");
    setLogs([]);
    try {
      const params = new URLSearchParams();
      if (customPrompt.trim()) params.set("prompt", customPrompt.trim());

      const res = await fetch(`/api/analyse-update-all?${params.toString()}`, { method: "POST" });
      const data = await res.json();
      if (data.job_id) {
        setJobId(data.job_id);
        setStatus("queued");
      } else {
        setStatus("error");
        setLogs([data.error || "Erreur inconnue"]);
      }
    } catch (e) {
      setStatus("error");
      setLogs(["Impossible de contacter le serveur API"]);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    if (!jobId || status === "success" || status === "failed") return;
    const interval = setInterval(async () => {
      try {
        const res = await fetch(`/api/status/${jobId}?_=${Date.now()}`, { cache: "no-store" });
        if (!res.ok) return;
        const data = await res.json();
        setStatus(data.status);
        setLogs(data.logs || []);
      } catch {
        // ignore
      }
    }, 2000);
    return () => clearInterval(interval);
  }, [jobId, status]);

  const isRunning = status === "queued" || status === "running";

  // ── Détection de progression à partir des logs ──
  const allText = logs.join(" ");
  const isFullAnalysis = allText.includes("analyse COMPLÈTE");
  const isClaudeAnalysis = allText.includes("Claude CLI via Ollama") || allText.includes("Mise à jour automatique") || allText.includes("kimi-k2.6");
  const steps = isClaudeAnalysis
    ? [
        {
          label: "Watchlist",
          icon: ListChecks,
          done:
            allText.includes("déjà dans la watchlist") ||
            allText.includes("ajouté à la watchlist"),
          active: allText.includes("Ajout"),
        },
        {
          label: "Fetch données",
          icon: Database,
          done: allText.includes("Fetch terminé") || allText.includes("Données récupérées"),
          active: allText.includes("Fetch des données") || allText.includes("Étape 1/3"),
        },
        {
          label: "Agents réels",
          icon: Cpu,
          done: allText.includes("Agents terminés") || allText.includes("Agent"),
          active: allText.includes("Exécution des agents") || allText.includes("Étape 2/3"),
        },
        {
          label: "Claude CLI (Ollama/kimi)",
          icon: Terminal,
          done: allText.includes("Rapport Claude CLI (Ollama/kimi) sauvegardé") || allText.includes("Analyse Claude CLI via Ollama terminée"),
          active: allText.includes("Claude CLI via Ollama") || allText.includes("Envoi du prompt à Claude CLI via Ollama"),
        },
        {
          label: "Terminé",
          icon: CheckCircle2,
          done: status === "success",
          active: false,
        },
      ]
    : isFullAnalysis
    ? [
        {
          label: "Watchlist",
          icon: ListChecks,
          done:
            allText.includes("déjà dans la watchlist") ||
            allText.includes("ajouté à la watchlist"),
          active: allText.includes("Ajout"),
        },
        {
          label: "Fetch données",
          icon: Database,
          done: allText.includes("Fetch des données") || allText.includes("Données récupérées"),
          active: allText.includes("Fetch des données") || allText.includes("Étape 1/2"),
        },
        {
          label: "Agents réels",
          icon: Cpu,
          done: allText.includes("Données agents déjà disponibles") || allText.includes("Lancement agent"),
          active: allText.includes("Compilation agents réels") || allText.includes("Lancement agent"),
        },
        {
          label: "LLM unique",
          icon: Sparkles,
          done: allText.includes("Rapport compilé") || allText.includes("Rapport sauvegardé"),
          active: allText.includes("Compilation LLM"),
        },
        {
          label: "Terminé",
          icon: CheckCircle2,
          done: status === "success",
          active: false,
        },
      ]
    : [
        {
          label: "Watchlist",
          icon: ListChecks,
          done:
            allText.includes("déjà dans la watchlist") ||
            allText.includes("ajouté à la watchlist"),
          active: allText.includes("Ajout"),
        },
        {
          label: "Fetch données",
          icon: Database,
          done:
            allText.includes("Données récupérées") ||
            allText.includes("Cours:") ||
            allText.includes("prêt pour analyse"),
          active: allText.includes("Fetch des données"),
        },
        {
          label: "Sync dashboard",
          icon: FileText,
          done:
            allText.includes("Copie des données dans frontend/dist/data") ||
            allText.includes("Data files synced"),
          active: allText.includes("Copie"),
        },
        {
          label: "Terminé",
          icon: CheckCircle2,
          done: status === "success",
          active: false,
        },
      ];

  const completedSteps = steps.filter((s) => s.done).length;
  const progressPct = status === "success" ? 100 : Math.min((completedSteps / steps.length) * 100, 95);

  return (
    <motion.div
      variants={fadeIn}
      initial="initial"
      whileInView="animate"
      viewport={{ once: true }}
      className="glass rounded-2xl border border-white/[0.06] p-6"
    >
      <div className="flex items-center gap-2 mb-5">
        <Play className="h-5 w-5 text-accent" />
        <h3 className="font-semibold text-foreground">Nouvelle analyse</h3>
      </div>

      <div className="flex gap-2 mb-3">
        <input
          type="text"
          value={ticker}
          onChange={(e) => setTicker(e.target.value.toUpperCase())}
          onKeyDown={(e) => e.key === "Enter" && startAnalysis()}
          placeholder="Ticker seul (ex: AAPL, RKLB)"
          maxLength={20}
          disabled={isRunning}
          className="flex-1 rounded-xl border border-white/[0.06] bg-white/[0.02] px-3 py-2 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-1 focus:ring-accent disabled:opacity-50"
        />
        <button
          onClick={startAnalysis}
          disabled={isRunning || !ticker.trim()}
          className="inline-flex items-center gap-1.5 rounded-xl bg-accent px-4 py-2 text-sm font-medium text-white hover:bg-emerald-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          title="Fetch des données uniquement"
        >
          {isRunning ? <Loader2 className="h-4 w-4 animate-spin" /> : <Play className="h-4 w-4" />}
          {isRunning ? "En cours..." : "Préparer"}
        </button>
        <button
          onClick={startFullAnalysis}
          disabled={isRunning || !ticker.trim()}
          className="inline-flex items-center gap-1.5 rounded-xl bg-violet-500 px-4 py-2 text-sm font-medium text-white hover:bg-violet-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          title="Fetch + génération automatique du rapport LLM"
        >
          {isRunning ? <Loader2 className="h-4 w-4 animate-spin" /> : <Sparkles className="h-4 w-4" />}
          {isRunning ? "En cours..." : "Analyser LLM"}
        </button>
        <button
          onClick={startClaudeAnalysis}
          disabled={isRunning || !ticker.trim()}
          className="inline-flex items-center gap-1.5 rounded-xl bg-amber-500 px-4 py-2 text-sm font-medium text-white hover:bg-amber-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          title="Fetch + agents réels + Claude CLI via Ollama (kimi-k2.6:cloud)"
        >
          {isRunning ? <Loader2 className="h-4 w-4 animate-spin" /> : <Terminal className="h-4 w-4" />}
          {isRunning ? "Analyse..." : "Analyse IA (Ollama)"}
        </button>
        <button
          onClick={startUpdateAllAnalysis}
          disabled={isRunning}
          className="inline-flex items-center gap-1.5 rounded-xl bg-rose-500 px-4 py-2 text-sm font-medium text-white hover:bg-rose-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          title="Mise à jour automatique de toutes les analyses existantes (fetch + agents + Claude CLI via Ollama)"
        >
          {isRunning ? <Loader2 className="h-4 w-4 animate-spin" /> : <RefreshCw className="h-4 w-4" />}
          {isRunning ? "Mise à jour..." : "Mise à jour analyses"}
        </button>
      </div>

      {/* Prompt personnalisé — textarea large pour instructions utilisateur */}
      <div className="mb-3">
        <div className="flex items-center justify-between mb-1.5">
          <div className="flex items-center gap-1.5">
            <MessageSquare className="h-3.5 w-3.5 text-amber-400" />
            <span className="text-[10px] font-medium text-muted-foreground uppercase tracking-wide">Instructions personnalisées (optionnel)</span>
          </div>
          <span className="text-[10px] text-muted-foreground tabular-nums">{customPrompt.length} caractères</span>
        </div>
        <textarea
          value={customPrompt}
          onChange={(e) => setCustomPrompt(e.target.value)}
          placeholder="Écris ici les instructions pour l'analyse IA. Exemples :&#10;• 'Analyse RKLB avec focus sur le marché spatial et comparaison avec SpaceX'&#10;• 'Inclure un DCF, une matrice de scénarios et une analyse ESG'&#10;• 'Focus sur les contrats gouvernementaux et le risque géopolitique'"
          rows={8}
          disabled={isRunning}
          className="w-full rounded-xl border border-white/[0.06] bg-white/[0.02] px-3 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-1 focus:ring-accent disabled:opacity-50 resize-y min-h-[200px]"
        />
      </div>

      <button
        onClick={() => setShowOptions((v) => !v)}
        className="mb-3 text-[10px] text-muted-foreground hover:text-foreground transition-colors"
      >
        {showOptions ? "▲ Masquer les options" : "▼ Options avancées (nom, secteur, exchange)"}
      </button>

      {showOptions && (
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-4">
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Nom entreprise"
            disabled={isRunning}
            className="rounded-xl border border-white/[0.06] bg-white/[0.02] px-3 py-2 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-1 focus:ring-accent disabled:opacity-50"
          />
          <input
            type="text"
            value={sector}
            onChange={(e) => setSector(e.target.value)}
            placeholder="Secteur"
            disabled={isRunning}
            className="rounded-xl border border-white/[0.06] bg-white/[0.02] px-3 py-2 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-1 focus:ring-accent disabled:opacity-50"
          />
          <select
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
            disabled={isRunning}
            className="rounded-xl border border-white/[0.06] bg-white/[0.02] px-3 py-2 text-sm text-foreground focus:outline-none focus:ring-1 focus:ring-accent disabled:opacity-50"
          >
            <option value="high">Haute</option>
            <option value="medium">Moyenne</option>
            <option value="low">Basse</option>
          </select>
          <select
            value={exchange}
            onChange={(e) => setExchange(e.target.value)}
            disabled={isRunning}
            className="rounded-xl border border-white/[0.06] bg-white/[0.02] px-3 py-2 text-sm text-foreground focus:outline-none focus:ring-1 focus:ring-accent disabled:opacity-50"
          >
            <option value="NASDAQ">NASDAQ</option>
            <option value="NYSE">NYSE</option>
            <option value="Euronext">Euronext</option>
          </select>
        </div>
      )}

      {status && (
        <div className="mb-4 space-y-4">
          {/* Statut + Job */}
          <div className="flex items-center gap-2 text-xs">
            <span
              className={`inline-flex items-center gap-1 rounded-full px-2 py-0.5 font-medium ${
                status === "success"
                  ? "bg-emerald-500/10 text-emerald-400"
                  : status === "failed"
                  ? "bg-red-500/10 text-red-400"
                  : status === "running"
                  ? "bg-accent/10 text-accent"
                  : "bg-white/[0.04] text-muted-foreground"
              }`}
            >
              {status === "success" && <CheckCircle2 className="h-3 w-3" />}
              {status === "failed" && <AlertTriangle className="h-3 w-3" />}
              {status === "running" && <Loader2 className="h-3 w-3 animate-spin" />}
              {status === "queued" && <Clock className="h-3 w-3" />}
              {status === "success" ? "Terminé" : status === "failed" ? "Échec" : status === "running" ? "En cours" : "En attente"}
            </span>
            {jobId && <span className="text-muted-foreground font-mono">job {jobId}</span>}
          </div>

          {/* Barre de progression */}
          <div>
            <div className="flex items-center justify-between text-[10px] text-muted-foreground mb-1.5">
              <span>Progression</span>
              <span>{Math.round(progressPct)}%</span>
            </div>
            <div className="h-1.5 w-full rounded-full bg-white/[0.04] overflow-hidden">
              <motion.div
                className={`h-full rounded-full ${
                  status === "success"
                    ? "bg-emerald-500"
                    : status === "failed"
                    ? "bg-red-500"
                    : "bg-accent"
                }`}
                initial={{ width: 0 }}
                animate={{ width: `${progressPct}%` }}
                transition={{ duration: 0.5 }}
              />
            </div>
          </div>

          {/* Étapes visuelles */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
            {steps.map((step, i) => {
              const Icon = step.icon;
              return (
                <div
                  key={i}
                  className={`flex flex-col items-center gap-1.5 rounded-xl border p-2 transition-colors ${
                    step.done
                      ? "border-emerald-500/20 bg-emerald-500/5"
                      : step.active
                      ? "border-accent/20 bg-accent/5"
                      : "border-white/[0.04] bg-white/[0.01]"
                  }`}
                >
                  <div
                    className={`flex h-6 w-6 items-center justify-center rounded-full ${
                      step.done
                        ? "bg-emerald-500/20 text-emerald-400"
                        : step.active
                        ? "bg-accent/20 text-accent"
                        : "bg-white/[0.04] text-muted-foreground"
                    }`}
                  >
                    {step.done ? (
                      <Check className="h-3 w-3" />
                    ) : step.active ? (
                      <Loader2 className="h-3 w-3 animate-spin" />
                    ) : (
                      <Icon className="h-3 w-3" />
                    )}
                  </div>
                  <span
                    className={`text-[9px] font-medium text-center leading-tight ${
                      step.done
                        ? "text-emerald-400"
                        : step.active
                        ? "text-accent"
                        : "text-muted-foreground"
                    }`}
                  >
                    {step.label}
                  </span>
                </div>
              );
            })}
          </div>

          {/* Message spécial : Rapport Claude CLI via Ollama généré */}
          {status === "success" && isClaudeAnalysis && (
            <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/5 p-4">
              <div className="flex items-start gap-3">
                <CheckCircle2 className="h-5 w-5 text-emerald-400 shrink-0 mt-0.5" />
                <div className="space-y-1">
                  <div className="text-sm font-semibold text-emerald-400">Rapport Claude CLI (Ollama/kimi) généré</div>
                  <p className="text-xs text-muted-foreground">
                    L'analyse a été produite par Claude CLI via Ollama avec le modèle kimi-k2.6:cloud.
                    Rapport sauvegardé dans <code className="text-foreground">Actions/{ticker}/{ticker}_YYYY-MM-DD_claude.md</code>.
                  </p>
                  <a
                    href={`/Actions/${ticker}/`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1.5 rounded-lg bg-emerald-500/10 px-3 py-1.5 text-xs font-medium text-emerald-400 hover:bg-emerald-500/20 transition-colors"
                  >
                    <FileText className="h-3 w-3" />
                    Ouvrir le dossier Actions/{ticker}
                  </a>
                </div>
              </div>
            </div>
          )}

          {/* Logs */}
          {logs.length > 0 && (
            <div className="rounded-xl border border-white/[0.06] bg-black/30 p-3 max-h-40 overflow-y-auto">
              <div className="flex items-center gap-1.5 text-[10px] text-muted-foreground uppercase tracking-wide mb-2">
                <Terminal className="h-3 w-3" />
                Logs
              </div>
              <div className="space-y-1">
                {logs.map((line, i) => (
                  <div key={i} className="text-[10px] font-mono text-muted-foreground leading-tight">
                    {line}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      <div className="text-[10px] text-muted-foreground space-y-1">
        <p><strong className="text-accent">Préparer</strong> — Fetch des données + ajout à la watchlist uniquement.</p>
        <p><strong className="text-violet-400">Analyser LLM</strong> — Fetch + génération automatique du rapport via IA (crée Actions/{ticker}/_init.md).</p>
        <p><strong className="text-amber-400">Analyse IA (Ollama)</strong> — Fetch + agents réels + Claude CLI via Ollama (kimi-k2.6:cloud). Lance `ollama launch claude --model kimi-k2.6:cloud` avec lecture des fichiers, outils natifs et historique. Rapport sauvegardé dans Actions/{ticker}/{ticker}_YYYY-MM-DD_claude.md. Ajoute des instructions personnalisées ci-dessus.</p>
        <p><strong className="text-rose-400">Mise à jour analyses</strong> — Met à jour automatiquement toutes les analyses existantes de la watchlist. Fetch + agents une seule fois, puis lance Claude CLI en parallèle (max 3) pour générer un `_update.md` par ticker avec les nouvelles données.</p>
      </div>
    </motion.div>
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

"use client";

import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { BarChart3, ArrowLeft, Loader2 } from "lucide-react";
import Link from "next/link";

import {
  RegimeBanner,
  SummaryCards,
  ScoreChart,
  RecommendationsTable,
  TickerGrid,
  QuantPanel,
  RiskPanels,
  PipelineStatus,
  TickerData,
  OllamaUsagePanel,
  LaunchAnalysis,
} from "@/components/dashboard";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
};

const DATA_FILES = [
  "recommandations_latest.json",
  "latest.json",
  "quant_report_latest.json",
  "quality_report_latest.json",
  "geo_risk_latest.json",
  "fx_exposure_latest.json",
  "crypto_correlation_latest.json",
  "social_sentiment_latest.json",
  "upcoming_events_latest.json",
  "ollama_config.json",
  "ollama_usage.json",
];

async function safeFetch(url: string) {
  try {
    // Cache-busting pour forcer le rechargement des données fraîches
    const busted = `${url}?_t=${Date.now()}`;
    const res = await fetch(busted, { cache: "no-store" });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

function SkeletonCard() {
  return (
    <div className="glass rounded-2xl border border-white/[0.06] p-5">
      <div className="h-5 w-24 rounded bg-white/[0.04] animate-pulse mb-3" />
      <div className="h-8 w-32 rounded bg-white/[0.04] animate-pulse mb-4" />
      <div className="grid grid-cols-3 gap-2">
        <div className="h-12 rounded bg-white/[0.04] animate-pulse" />
        <div className="h-12 rounded bg-white/[0.04] animate-pulse" />
        <div className="h-12 rounded bg-white/[0.04] animate-pulse" />
      </div>
    </div>
  );
}

export default function DashboardPage() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState<Record<string, any>>({});
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      setLoading(true);
      setError(null);

      const results = await Promise.all(
        DATA_FILES.map((f) => safeFetch(`/data/${f}`))
      );

      const map: Record<string, any> = {};
      DATA_FILES.forEach((f, i) => {
        const key = f.replace(/_latest\.json$|\.json$/, "");
        map[key] = results[i] ?? {};
      });

      // Vérifier que les fichiers critiques existent
      if (!map.recommandations?.recommandations?.length) {
        setError("Données indisponibles — le pipeline n'a pas encore généré de rapports.");
      }

      setData(map);
      setLoading(false);
    }
    load();
  }, []);

  const recos = data.recommandations?.recommandations ?? [];
  const recosMap = Object.fromEntries(recos.map((r: any) => [r.ticker, r]));
  const meta = data.recommandations?.meta ?? {};
  const allPrices: Record<string, TickerData> = data.latest?.prices ?? {};
  const qualityTickers: Record<string, { status: string; reasons: string[] }> = data.quality_report?.tickers ?? {};

  // Construire la liste des tickers : ceux avec données + placeholders pour les nouveaux
  const prices: Record<string, TickerData> = {};
  for (const r of recos) {
    const t = r.ticker as string;
    if (allPrices[t]) {
      prices[t] = allPrices[t];
    } else {
      // Placeholder pour les tickers sans données dans latest.json
      prices[t] = {
        ticker: t,
        price: { close: 0, change_pct: 0, volume: 0, volume_avg_20d: 1 },
        technical: { rsi14: 0, atr14: 0, mm50: null },
        fundamentals: {
          sector: r.sector ?? "—",
          market_cap: 0,
          pe_ratio: 0,
          forward_pe: null,
          beta: 0,
        },
        options: { max_pain: 0, put_call_ratio: 0 },
        _quality_gate: qualityTickers[t] ?? { status: "ok", reasons: [] },
        _no_data: true,
      };
    }
  }

  const quant = data.quant_report ?? {};
  const quality = data.quality_report ?? {};
  const geo = data.geo_risk ?? {};
  const fx = data.fx_exposure ?? {};
  const crypto = data.crypto_correlation ?? {};
  const social = data.social_sentiment ?? {};
  const upcoming = data.upcoming_events ?? {};
  const ollamaConfig = data.ollama_config ?? null;
  const ollamaUsage = data.ollama_usage ?? null;

  const eventsByTicker: Record<string, any[]> = {};
  for (const ev of upcoming.events ?? []) {
    const t = ev.ticker;
    if (!eventsByTicker[t]) eventsByTicker[t] = [];
    eventsByTicker[t].push(ev);
  }
  for (const t of Object.keys(eventsByTicker)) {
    eventsByTicker[t].sort((a: any, b: any) => a.days_until - b.days_until);
  }

  if (loading) {
    return (
      <div className="flex flex-col gap-8 pt-24 pb-20">
        <div className="mx-auto max-w-7xl w-full px-4 sm:px-6 lg:px-8 flex items-center gap-3">
          <Loader2 className="h-5 w-5 text-accent animate-spin" />
          <span className="text-sm text-muted-foreground">Chargement des données des agents...</span>
        </div>
        <div className="mx-auto max-w-7xl w-full px-4 sm:px-6 lg:px-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <SkeletonCard key={i} />
          ))}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col gap-8 pt-24 pb-20">
        <div className="mx-auto max-w-7xl w-full px-4 sm:px-6 lg:px-8">
          <div className="glass rounded-2xl border border-red-500/20 bg-red-500/5 p-6 text-center">
            <div className="text-red-400 font-semibold mb-2">Données indisponibles</div>
            <p className="text-sm text-muted-foreground">{error}</p>
            <button
              onClick={() => window.location.reload()}
              className="mt-4 inline-flex items-center gap-2 rounded-xl bg-accent px-4 py-2 text-sm font-medium text-white hover:bg-emerald-600 transition-colors"
            >
              <Loader2 className="h-4 w-4" />
              Réessayer
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-8 pt-24 pb-20">
      {/* Header */}
      <motion.div
        variants={fadeIn}
        initial="initial"
        animate="animate"
        className="mx-auto max-w-7xl w-full px-4 sm:px-6 lg:px-8"
      >
        <div className="flex items-center gap-3 mb-2">
          <Link
            href="/"
            className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground transition-colors"
          >
            <ArrowLeft className="h-4 w-4" />
            Accueil
          </Link>
        </div>
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-accent/10 text-accent">
            <BarChart3 className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-2xl font-bold tracking-tight text-foreground">Dashboard</h1>
            <p className="text-sm text-muted-foreground">
              Résultats des agents · {meta.date ?? "—"}
            </p>
          </div>
        </div>
      </motion.div>

      <div className="mx-auto max-w-7xl w-full px-4 sm:px-6 lg:px-8 space-y-8">
        {/* Regime & Summary */}
        <RegimeBanner
          regime={meta.regime_macro ?? "Normal"}
          weights={meta.regime_weights ?? { catalyseur: 0.35, valorisation: 0.4, momentum: 0.25 }}
          vix={meta.vix ?? 0}
          dxy={meta.dxy_trend ?? 0}
          date={meta.date ?? ""}
        />

        <SummaryCards
          tickersCount={Object.keys(prices).length}
          recoCounts={meta.recommandations_count ?? {}}
        />

        {/* Launch Analysis */}
        <LaunchAnalysis />

        {/* Pipeline */}
        <PipelineStatus okAgents={18} />

        {/* Ollama Cloud Usage + Score Chart */}
        <div className="grid gap-6 lg:grid-cols-3">
          <div className="lg:col-span-1">
            <OllamaUsagePanel config={ollamaConfig} usage={ollamaUsage} />
          </div>
          <div className="lg:col-span-2">
            <RecommendationsTable recos={recos} />
          </div>
        </div>

        {/* Charts */}
        <div className="grid gap-6 lg:grid-cols-3">
          <div className="lg:col-span-3">
            <ScoreChart recos={recos} />
          </div>
        </div>

        {/* Tickers */}
        <div>
          <motion.div variants={fadeIn} initial="initial" whileInView="animate" viewport={{ once: true }} className="mb-4">
            <h2 className="text-lg font-semibold text-foreground">Cours & Technique</h2>
          </motion.div>
          <TickerGrid tickers={prices} recos={recosMap} events={eventsByTicker} geo={geo} />
        </div>

        {/* Quant */}
        <QuantPanel quant={quant} />

        {/* Risk panels */}
        <RiskPanels
          quality={quality}
          geo={geo}
          fx={fx}
          crypto={crypto}
          social={social}
        />
      </div>
    </div>
  );
}

"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import {
  Eye,
  Brain,
  Zap,
  Shield,
  BarChart3,
  TrendingUp,
  Globe,
  Cpu,
  ArrowRight,
  ChevronRight,
  Activity,
  Terminal,
  Radio,
} from "lucide-react";

const fadeInUp = {
  initial: { opacity: 0, y: 30 },
  animate: { opacity: 1, y: 0 },
};

const staggerContainer = {
  animate: {
    transition: {
      staggerChildren: 0.08,
    },
  },
};

export function HeroSection() {
  return (
    <section className="relative overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-28">
      <div className="absolute inset-0 -z-10">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 h-[600px] w-[800px] rounded-full bg-accent/5 blur-[120px]" />
        <div className="absolute bottom-0 right-0 h-[400px] w-[600px] rounded-full bg-primary/5 blur-[100px]" />
      </div>

      <motion.div
        variants={staggerContainer}
        initial="initial"
        animate="animate"
        className="mx-auto max-w-5xl px-4 text-center sm:px-6 lg:px-8"
      >
        <motion.div
          variants={fadeInUp}
          transition={{ duration: 0.6 }}
          className="inline-flex items-center gap-2 rounded-full border border-accent/20 bg-accent/5 px-4 py-1.5 text-sm font-medium text-accent mb-8"
        >
          <Zap className="h-3.5 w-3.5" />
          18 agents IA analysent votre watchlist chaque matin
        </motion.div>

        <motion.h1
          variants={fadeInUp}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="text-4xl font-extrabold tracking-tight text-foreground sm:text-5xl md:text-6xl lg:text-7xl"
        >
          L'<span className="text-gradient-accent">Intelligence Artificielle</span>
          <br />
          au service de vos investissements
        </motion.h1>

        <motion.p
          variants={fadeInUp}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="mx-auto mt-6 max-w-2xl text-lg text-muted-foreground sm:text-xl"
        >
          Argus-IA est un pipeline multi-agent qui scrute les marchés,
          analyse les fondamentaux et détecte les opportunités sur votre watchlist
          — automatiquement, chaque matin.
        </motion.p>

        <motion.div
          variants={fadeInUp}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row"
        >
          <Link
            href="/dashboard"
            className="inline-flex items-center gap-2 rounded-xl bg-accent px-8 py-3.5 text-base font-semibold text-white shadow-lg shadow-accent/20 hover:bg-emerald-600 transition-all hover:shadow-accent/30"
          >
            <BarChart3 className="h-5 w-5" />
            Voir le Dashboard
          </Link>
          <a
            href="https://github.com/Wzxgreed/argus-ia"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-xl border border-white/[0.12] bg-white/[0.03] px-8 py-3.5 text-base font-medium text-foreground hover:bg-white/[0.06] transition-colors"
          >
            <Terminal className="h-5 w-5" />
            Explorer le Code
          </a>
        </motion.div>

        <motion.div
          variants={fadeInUp}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="mt-16 mx-auto max-w-5xl"
        >
          <div className="glass rounded-2xl border border-white/[0.08] p-2 shadow-2xl">
            <div className="rounded-xl bg-background/80 p-4 sm:p-6">
              <div className="flex items-center gap-2 mb-4">
                <div className="flex gap-1.5">
                  <div className="h-3 w-3 rounded-full bg-red-500/80" />
                  <div className="h-3 w-3 rounded-full bg-yellow-500/80" />
                  <div className="h-3 w-3 rounded-full bg-green-500/80" />
                </div>
                <span className="text-xs text-muted-foreground ml-2 font-mono">argus-ia — pipeline du matin</span>
              </div>
              <div className="font-mono text-xs sm:text-sm text-muted-foreground space-y-1">
                <div className="flex items-center gap-2">
                  <span className="text-accent">{'>'}</span>
                  <span>Phase A: 3 agents indépendants — </span>
                  <span className="text-green-400">OK</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-accent">{'>'}</span>
                  <span>Phase B: fetch données brutes — </span>
                  <span className="text-green-400">OK</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-accent">{'>'}</span>
                  <span>Phase C: 8 agents dépendants — </span>
                  <span className="text-green-400">OK</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-accent">{'>'}</span>
                  <span>Phase D: agrégation finale — </span>
                  <span className="text-green-400">OK</span>
                </div>
                <div className="flex items-center gap-2 pt-1">
                  <span className="text-accent">{'>'}</span>
                  <span className="text-foreground">Dashboard généré: </span>
                  <span className="text-accent">logs/dashboard_2026-05-17.html</span>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </section>
  );
}

export function StatsSection() {
  const stats = [
    { label: "Agents IA", value: "18", icon: Cpu },
    { label: "Tickers analysés", value: "50+", icon: Eye },
    { label: "Pipeline / jour", value: "21", icon: Activity },
    { label: "Données traitées", value: "10K+", icon: TrendingUp },
  ];

  return (
    <section className="border-y border-white/[0.06] bg-white/[0.02]">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 gap-8 md:grid-cols-4">
          {stats.map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className="flex flex-col items-center gap-2 text-center"
            >
              <stat.icon className="h-6 w-6 text-accent" />
              <div className="text-3xl font-bold text-foreground sm:text-4xl">
                {stat.value}
              </div>
              <div className="text-sm text-muted-foreground">{stat.label}</div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function FeaturesSection() {
  const features = [
    {
      title: "Analyse Multi-Agent",
      description:
        "18 agents spécialisés (Macro, Technique, Fondamental, Sentiment, Quant, Géo, Crypto, etc.) travaillent en parallèle chaque matin.",
      icon: Brain,
    },
    {
      title: "Pipeline Automatisé",
      description:
        "DAG de dépendances avec orchestrateur Python. Phase A/B/C/D en parallèle. Rapport JSON + dashboard HTML à la fin.",
      icon: Zap,
    },
    {
      title: "Qualité & Validation",
      description:
        "Data Quality Gate, validation des schémas Pydantic, protocoles exécutables, et tests d'intégration end-to-end.",
      icon: Shield,
    },
    {
      title: "Scoring Régime-Aware",
      description:
        "Score Opportunité = (Catalyseur × A%) + (Valorisation × B%) + (Momentum × C%). Pondération ajustée selon le régime macro.",
      icon: TrendingUp,
    },
    {
      title: "Surveillance Proactive",
      description:
        "Détection automatique d'événements majeurs (gap >5%, volume >3×, news M&A, earnings) avec full refresh.",
      icon: Radio,
    },
    {
      title: "Observabilité Complète",
      description:
        "Logging JSONL structuré, métriques par agent, Event Bus pub/sub, et dashboard HTML auto-généré post-pipeline.",
      icon: BarChart3,
    },
  ];

  return (
    <section id="features" className="py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mx-auto max-w-2xl text-center mb-16"
        >
          <h2 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
            Une architecture pensée pour la fiabilité
          </h2>
          <p className="mt-4 text-lg text-muted-foreground">
            Du fetch des données au scoring final, chaque étape est standardisée,
            validée et observable.
          </p>
        </motion.div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature, i) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              whileHover={{ y: -4 }}
              className="group relative rounded-2xl border border-white/[0.06] bg-card p-6 hover:border-accent/20 transition-colors"
            >
              <div className="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-xl bg-accent/10 text-accent">
                <feature.icon className="h-5 w-5" />
              </div>
              <h3 className="text-lg font-semibold text-foreground mb-2">
                {feature.title}
              </h3>
              <p className="text-sm text-muted-foreground leading-relaxed">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function AgentsSection() {
  const agents = [
    { name: "Macro", desc: "Régime macro, banques centrales, VIX", color: "bg-blue-500/10 text-blue-400" },
    { name: "Quant", desc: "Signification statistique, Sharpe, calibration", color: "bg-purple-500/10 text-purple-400" },
    { name: "Géo", desc: "Risques politiques, tarifs, sanctions", color: "bg-orange-500/10 text-orange-400" },
    { name: "Crypto", desc: "Corrélation BTC, beta, NAV", color: "bg-yellow-500/10 text-yellow-400" },
    { name: "Accounting", desc: "M-Score, Z-Score, F-Score, Sloan", color: "bg-red-500/10 text-red-400" },
    { name: "Sector", desc: "Rotation sectorielle, RS vs SPY", color: "bg-cyan-500/10 text-cyan-400" },
    { name: "Social", desc: "Sentiment Reddit, pump detection", color: "bg-pink-500/10 text-pink-400" },
    { name: "FX", desc: "Exposition change, impact EPS", color: "bg-indigo-500/10 text-indigo-400" },
    { name: "Event", desc: "M&A, buybacks, activism, guidance", color: "bg-emerald-500/10 text-emerald-400" },
    { name: "Watchman", desc: "Earnings, insiders, upgrades", color: "bg-teal-500/10 text-teal-400" },
    { name: "Reco", desc: "Scoring 3 axes, reco ACHETER/ÉVITER", color: "bg-lime-500/10 text-lime-400" },
    { name: "Paper", desc: "Paper trading, sizing ATR, journal", color: "bg-violet-500/10 text-violet-400" },
  ];

  return (
    <section id="agents" className="py-24 sm:py-32 border-y border-white/[0.06] bg-white/[0.02]">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mx-auto max-w-2xl text-center mb-16"
        >
          <h2 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
            18 agents spécialisés
          </h2>
          <p className="mt-4 text-lg text-muted-foreground">
            Chaque agent est un expert dans son domaine. Ils communiquent via Event Bus
            et partagent leurs résultats dans un pipeline DAG coordonné.
          </p>
        </motion.div>

        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {agents.map((agent, i) => (
            <motion.div
              key={agent.name}
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.05 }}
              whileHover={{ scale: 1.03 }}
              className="rounded-xl border border-white/[0.06] bg-card p-4 hover:border-white/[0.12] transition-colors cursor-default"
            >
              <div className={`inline-flex rounded-lg px-2 py-1 text-xs font-semibold mb-2 ${agent.color}`}>
                {agent.name}
              </div>
              <p className="text-sm text-muted-foreground">{agent.desc}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function DashboardPreview() {
  return (
    <section className="py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mx-auto max-w-2xl text-center mb-16"
        >
          <h2 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
            Dashboard en temps réel
          </h2>
          <p className="mt-4 text-lg text-muted-foreground">
            Visualisez l'état du pipeline, les résultats des agents, et les opportunités
            détectées sur votre watchlist.
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="glass rounded-2xl border border-white/[0.08] p-2 shadow-2xl"
        >
          <div className="rounded-xl bg-background/80 p-6">
            <div className="grid gap-6 lg:grid-cols-3">
              <div className="lg:col-span-2 space-y-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Activity className="h-5 w-5 text-accent" />
                    <span className="font-semibold text-foreground">Pipeline Status</span>
                  </div>
                  <span className="inline-flex items-center gap-1.5 rounded-full bg-green-500/10 px-2.5 py-1 text-xs font-medium text-green-400">
                    <span className="h-1.5 w-1.5 rounded-full bg-green-400 animate-pulse" />
                    Success
                  </span>
                </div>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                  {[
                    { label: "Agents OK", value: "18", color: "text-green-400" },
                    { label: "Duration", value: "124s", color: "text-foreground" },
                    { label: "Tickers", value: "12", color: "text-foreground" },
                    { label: "DRAFTs", value: "2", color: "text-yellow-400" },
                  ].map((s) => (
                    <div
                      key={s.label}
                      className="rounded-xl border border-white/[0.06] bg-white/[0.03] p-3"
                    >
                      <div className={`text-xl font-bold ${s.color}`}>{s.value}</div>
                      <div className="text-xs text-muted-foreground">{s.label}</div>
                    </div>
                  ))}
                </div>
              </div>
              <div className="space-y-4">
                <div className="flex items-center gap-2">
                  <Globe className="h-5 w-5 text-accent" />
                  <span className="font-semibold text-foreground">Régime Macro</span>
                </div>
                <div className="rounded-xl border border-white/[0.06] bg-white/[0.03] p-4">
                  <div className="text-sm font-medium text-foreground mb-1">Normal</div>
                  <div className="text-xs text-muted-foreground mb-3">
                    Pondération: 35/40/25
                  </div>
                  <div className="flex items-center gap-2">
                    <div className="h-2 flex-1 rounded-full bg-white/[0.06] overflow-hidden">
                      <div className="h-full w-[35%] rounded-full bg-accent" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

export function CTASection() {
  return (
    <section className="py-24 sm:py-32">
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="relative overflow-hidden rounded-3xl border border-accent/20 bg-accent/5 px-8 py-16 text-center sm:px-16"
        >
          <div className="absolute inset-0 -z-10">
            <div className="absolute top-0 left-1/2 -translate-x-1/2 h-[300px] w-[500px] rounded-full bg-accent/10 blur-[80px]" />
          </div>

          <h2 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
            Prêt à analyser vos actions ?
          </h2>
          <p className="mx-auto mt-4 max-w-lg text-lg text-muted-foreground">
            Consultez le dashboard pour voir les résultats du dernier pipeline
            et les opportunités détectées sur la watchlist.
          </p>
          <div className="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Link
              href="/dashboard"
              className="inline-flex items-center gap-2 rounded-xl bg-accent px-8 py-3.5 text-base font-semibold text-white shadow-lg shadow-accent/20 hover:bg-emerald-600 transition-all"
            >
              Ouvrir le Dashboard
              <ArrowRight className="h-5 w-5" />
            </Link>
            <a
              href="https://github.com/Wzxgreed/argus-ia"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
            >
              Voir sur GitHub
              <ChevronRight className="h-4 w-4" />
            </a>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

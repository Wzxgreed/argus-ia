"use client";

import { motion } from "framer-motion";
import {
  HeroSection,
  StatsSection,
  FeaturesSection,
  AgentsSection,
  DashboardPreview,
  CTASection,
} from "@/components/sections";

export default function HomePage() {
  return (
    <div className="flex flex-col">
      <HeroSection />
      <StatsSection />
      <FeaturesSection />
      <AgentsSection />
      <DashboardPreview />
      <CTASection />
    </div>
  );
}

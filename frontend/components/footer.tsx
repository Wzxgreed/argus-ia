import { Eye, GitBranch, Heart } from "lucide-react";

export function Footer() {
  return (
    <footer className="border-t border-white/[0.06] bg-background">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="flex flex-col items-center justify-between gap-6 sm:flex-row">
          <div className="flex items-center gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-accent/10 text-accent">
              <Eye className="h-4 w-4" />
            </div>
            <span className="text-sm font-semibold text-foreground">Argus-IA</span>
          </div>

          <p className="text-sm text-muted-foreground">
            Système d'analyse d'actions IA — Multi-agent pipeline
          </p>

          <div className="flex items-center gap-4">
            <a
              href="https://github.com/Wzxgreed/argus-ia"
              target="_blank"
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              <GitBranch className="h-5 w-5" />
            </a>
          </div>
        </div>

        <div className="mt-8 flex flex-col items-center gap-2 border-t border-white/[0.06] pt-8">
          <p className="text-xs text-muted-foreground">
            Construit avec <Heart className="inline h-3 w-3 text-accent" /> pour l'analyse boursière
          </p>
          <p className="text-xs text-muted-foreground/60">
            © {new Date().getFullYear()} Argus-IA. Outil d'analyse, pas de conseil en investissement.
          </p>
        </div>
      </div>
    </footer>
  );
}

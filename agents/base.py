"""agents/base.py — BaseAgent abstrait pour tous les agents Argus-IA."""

import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from agents.observability import log_structured, timer, record_metric
from scripts.agent_utils import (
    load_config,
    load_latest,
    today_str,
    write_json_with_symlink,
    get_data_dir,
    ensure_scripts_path,
)


class BaseAgent(ABC):
    """
    Classe de base abstraite pour tous les agents.

    Usage minimal :
        class MonAgent(BaseAgent):
            name = "mon_agent"
            output_schema = MonSchema

            def run(self) -> BaseModel:
                ...
                return MonSchema(meta=Meta(...), ...)
    """

    name: str = ""
    output_schema: type[BaseModel] | None = None
    allow_fail: bool = False

    def __init__(self):
        ensure_scripts_path()
        self.data_dir = get_data_dir()
        self.config = load_config()
        self.date_str = today_str()

    # ── Méthodes utilitaires ───────────────────────────────────────────────

    def load_latest(self) -> dict:
        return load_latest()

    def write_output(
        self,
        data: BaseModel,
        dated_filename: str | None = None,
        symlink_name: str | None = None,
    ) -> Path:
        """
        Écrit le output Pydantic en JSON daté et crée le symlink latest.
        Retourne le chemin du fichier daté.
        """
        if dated_filename is None:
            dated_filename = f"{self.name}_{self.date_str}.json"
        if symlink_name is None:
            symlink_name = f"{self.name}_latest.json"

        record_metric(self.name, "json_outputs", 1)
        raw = data.model_dump(mode="json")
        return write_json_with_symlink(
            raw,
            dated_filename,
            symlink_name,
            output_dir=self.data_dir,
        )

    def log(self, level: str, event: str, **kwargs: Any) -> None:
        log_structured(self.name, level, event, **kwargs)

    def tickers(self) -> list[str]:
        return [t["ticker"] for t in self.config.get("tickers", [])]

    # ── Point d'entrée principal ───────────────────────────────────────────

    @abstractmethod
    def run(self) -> BaseModel:
        """
        Implémenter dans chaque sous-classe.
        Doit retourner une instance du `output_schema`.
        """
        ...

    def main(self) -> int:
        """Orchestre run() avec timer, logging et gestion d'erreurs."""
        try:
            with timer(self.name, "run"):
                self.log("INFO", "start", tickers=self.tickers())
                result = self.run()

                if self.output_schema and not isinstance(result, self.output_schema):
                    raise TypeError(
                        f"run() doit retourner {self.output_schema.__name__}, "
                        f"pas {type(result).__name__}"
                    )

                path = self.write_output(result)
                self.log("INFO", "complete", output=str(path))
                print(f"[{self.name}] Output written → {path}", file=sys.stderr)
                return 0

        except Exception as exc:
            self.log("ERROR", "failed", error=str(exc), error_type=type(exc).__name__)
            print(f"[{self.name}] FAILED: {exc}", file=sys.stderr)
            if self.allow_fail:
                return 0
            return 1

    @classmethod
    def cli_entry(cls) -> int:
        """Point d'entrée pour if __name__ == '__main__'."""
        agent = cls()
        return agent.main()

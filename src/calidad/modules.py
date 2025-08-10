from __future__ import annotations
from dataclasses import dataclass
from typing import final

from .base import BaseComponent
from .interfaces import Versionable, Documentable


def _parse_semver(v: str) -> tuple[int, int, int]:
    try:
        major, minor, patch = (int(x) for x in v.split(".", 2))
        return major, minor, patch
    except Exception as exc:
        raise ValueError(f"Versión inválida: {v}") from exc


@final
@dataclass
class WebServiceModule(BaseComponent, Versionable, Documentable):
    """Módulo de servicio web."""
    version: str = "1.0.0"
    base_url: str = "/api/v1"

    def validate(self) -> None:
        if not self.name or not self.owner:
            raise ValueError("name/owner no pueden estar vacíos")
        if not self.base_url.startswith("/"):
            raise ValueError("base_url debe iniciar con '/'")
        if " " in self.base_url:
            raise ValueError("base_url no debe contener espacios")
        self.log("Validación OK")

    def bump_version(self, major: int = 0, minor: int = 1, patch: int = 0) -> None:
        M, m, p = _parse_semver(self.version)
        self.version = f"{M+major}.{m+minor}.{p+patch}"
        self.log(f"Versión actualizada a {self.version}")

    def generate_docs(self) -> str:
        return (
            f"# {self.name}\n"
            f"- Tipo: WebServiceModule\n"
            f"- Dueño: {self.owner}\n"
            f"- Versión: {self.version}\n"
            f"- Base URL: {self.base_url}\n"
            f"- Estándar: {self.QUALITY_STANDARD}\n"
        )


@final
@dataclass
class DataProcessingModule(BaseComponent, Versionable, Documentable):
    """Módulo de procesamiento de datos."""
    version: str = "0.1.0"
    batch_size: int = 1000

    def validate(self) -> None:
        if self.batch_size <= 0:
            raise ValueError("batch_size debe ser > 0")
        if self.batch_size > 1_000_000:
            raise ValueError("batch_size demasiado grande")
        self.log("Validación OK")

    def bump_version(self, major: int = 0, minor: int = 1, patch: int = 0) -> None:
        M, m, p = _parse_semver(self.version)
        self.version = f"{M+major}.{m+minor}.{p+patch}"
        self.log(f"Versión actualizada a {self.version}")

    def generate_docs(self) -> str:
        return (
            f"# {self.name}\n"
            f"- Tipo: DataProcessingModule\n"
            f"- Dueño: {self.owner}\n"
            f"- Versión: {self.version}\n"
            f"- Batch size: {self.batch_size}\n"
            f"- Estándar: {self.QUALITY_STANDARD}\n"
        )


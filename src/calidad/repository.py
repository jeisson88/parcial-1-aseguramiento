from __future__ import annotations
from dataclasses import dataclass, field
from typing import final, Dict, Any

from .base import BaseComponent
from .interfaces import Versionable, Documentable


@final
@dataclass
class InMemoryRepository(BaseComponent, Versionable, Documentable):
    """
    Repositorio simple en memoria (simula persistencia).
    """
    version: str = "1.0.0"
    _store: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.name or not self.owner:
            raise ValueError("name/owner no pueden estar vacíos")
        self.log("Validación OK (repositorio)")

    def save(self, key: str, entity: Dict[str, Any]) -> None:
        self._store[key] = entity
        self.log(f"Entidad guardada con clave {key}")

    def get(self, key: str) -> Dict[str, Any] | None:
        return self._store.get(key)

    def all_ids(self) -> list[str]:
        return list(self._store.keys())

    # Versionable
    def bump_version(self, major: int = 0, minor: int = 1, patch: int = 0) -> None:
        M, m, p = (int(x) for x in self.version.split(".", 2))
        self.version = f"{M+major}.{m+minor}.{p+patch}"
        self.log(f"Versión de repositorio actualizada a {self.version}")

    # Documentable
    def generate_docs(self) -> str:
        return (
            f"# {self.name}\n"
            f"- Tipo: InMemoryRepository\n"
            f"- Dueño: {self.owner}\n"
            f"- Versión: {self.version}\n"
            f"- Registros: {len(self._store)}\n"
            f"- Estándar: {self.QUALITY_STANDARD}\n"
        )

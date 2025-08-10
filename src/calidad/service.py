from __future__ import annotations
from dataclasses import dataclass
from typing import final, Dict, Any

from .base import BaseComponent
from .interfaces import Versionable, Documentable
from .repository import InMemoryRepository


@final
@dataclass
class UserService(BaseComponent, Versionable, Documentable):
    """
    Capa de servicio con 'lógica de negocio' mínima.
    Depende de un repositorio para persistencia.
    """
    version: str = "1.0.0"
    repo: InMemoryRepository | None = None

    def validate(self) -> None:
        if not self.name or not self.owner:
            raise ValueError("name/owner no pueden estar vacíos")
        if self.repo is None:
            raise ValueError("Debe inyectarse un repositorio")
        self.repo.validate()  # valida también el repositorio
        self.log("Validación OK (servicio)")

    # “Reglas de negocio” mínimas:
    def register_user(self, user_id: str, data: Dict[str, Any]) -> None:
        if not user_id or "email" not in data:
            raise ValueError("user_id y email son obligatorios")
        self.repo.save(user_id, data)
        self.log(f"Usuario {user_id} registrado")

    def get_user(self, user_id: str) -> Dict[str, Any] | None:
        return self.repo.get(user_id)

    # Versionable
    def bump_version(self, major: int = 0, minor: int = 1, patch: int = 0) -> None:
        M, m, p = (int(x) for x in self.version.split(".", 2))
        self.version = f"{M+major}.{m+minor}.{p+patch}"
        self.log(f"Versión de servicio actualizada a {self.version}")

    # Documentable
    def generate_docs(self) -> str:
        return (
            f"# {self.name}\n"
            f"- Tipo: UserService\n"
            f"- Dueño: {self.owner}\n"
            f"- Versión: {self.version}\n"
            f"- Repo: {self.repo.name if self.repo else 'N/D'}\n"
            f"- Estándar: {self.QUALITY_STANDARD}\n"
        )

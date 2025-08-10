from __future__ import annotations
from typing import Protocol


class Versionable(Protocol):
    """Interfaz para versionado semántico."""
    version: str

    def bump_version(self, major: int = 0, minor: int = 1, patch: int = 0) -> None:
        ...


class Documentable(Protocol):
    """Interfaz para documentación mínima."""
    def generate_docs(self) -> str:
        ...

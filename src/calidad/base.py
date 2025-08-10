from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Final


@dataclass
class BaseComponent(ABC):
    """
    Clase base ABSTRACTA para componentes de software bajo estándares de calidad.
    """
    name: str
    owner: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    QUALITY_STANDARD: Final[str] = "UMG-QA-1.0"

    @abstractmethod
    def validate(self) -> None:
        """Debe verificar precondiciones de calidad (levanta ValueError si falla)."""
        raise NotImplementedError

    def log(self, message: str) -> None:
        timestamp = datetime.utcnow().isoformat(timespec="seconds")
        print(f"[{timestamp}] [{self.name}] {message}")

"""Base class for actions."""

from __future__ import annotations

from abc import abstractmethod
from typing import Protocol

import tcod.ecs


class BaseAction(Protocol):

    @abstractmethod
    def __call__(self, actor: tcod.ecs.Entity) -> None:
        """Perform action."""

"""Base class for states."""

from __future__ import annotations

from abc import abstractmethod
from typing import Protocol

import tcod.console
import tcod.event


class BaseState(Protocol):

    @abstractmethod
    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

    @abstractmethod
    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the state is being drawn."""

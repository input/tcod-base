from __future__ import annotations

from typing import Final

import attrs

from game.constants import COLOR_WHITE
from game.managers import global_manager
from game.managers.event_manager import Observer


class LogManager(Observer):

    def __init__(self) -> None:
        # Observe events.
        Observer.__init__(self)
        self.observe("inventory_item_added", self.on_inventory_item_added)

    def on_inventory_item_added(self, data: str) -> None:
        """Callback for the inventory_item_added event."""

        add_message("Added: " + data)


@attrs.define
class Message:
    """A message."""

    text: str
    fg: tuple[int, int, int]
    count: int = 1

    @property
    def full_text(self) -> str:
        """The full text of this message, including the count if necessary."""

        if self.count > 1:
            return f"{self.text} (x{self.count})"
        return self.text


Log: Final = list[Message]
"""Message log component."""


def add_message(text: str, fg: tuple[int, int, int] = COLOR_WHITE) -> None:
    """Append a message to the log, stacking if necessary."""

    log = global_manager.world[None].components[Log]
    if log and log[-1].text == text:
        log[-1].count += 1
        return
    log.append(Message(text, fg))

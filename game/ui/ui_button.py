"""A UI button."""

from __future__ import annotations

from collections.abc import Callable

import tcod.event
from tcod.event import KeySym


class UIButton():

    def __init__(self, label: str, key: KeySym, callback: Callable[[], None]) -> None:
        self.label = label
        self.key = key
        self.callback = callback

    def on_event(self, event: tcod.event.Event) -> None:
        """Handle events passed to the button."""

        if isinstance(event, tcod.event.KeyDown):
            if event.sym == self.key:
                return self.callback()

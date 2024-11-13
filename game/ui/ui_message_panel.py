"""A UI panel which draws messages."""

from __future__ import annotations

import tcod.console
import tcod.event

import game.managers.global_manager as global_manager
from game.ui.ui_panel import UIPanel


class UIMessagePanel(UIPanel):

    def __init__(self) -> None:
        self.is_visible = True

    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the panel is being drawn."""

        # Draw information text at the bottom left of the screen.
        if text := global_manager.world[None].components.get(("Text", str)):
            console.print(0, console.height - 1, text, (255, 255, 255), (0, 0, 0))

"""A UI panel which displays log messages."""

from __future__ import annotations

from collections.abc import Reversible

import tcod.console
import tcod.event

import game.managers.global_manager as global_manager
from game.constants import COLOR_BLACK
from game.managers.log_manager import Message, Log
from game.ui.ui_panel import UIPanel


class UILogPanel(UIPanel):

    log_height: int = 3

    def __init__(self) -> None:
        self.is_visible = True

    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the panel is being drawn."""

        self.draw_frame(console)
        self.draw_body(console)

    def draw_frame(self, console: tcod.console.Console) -> None:
        console.draw_rect(
            0,
            console.height - self.log_height,
            console.width,
            self.log_height,
            0,
            COLOR_BLACK,
            COLOR_BLACK
        )

    def draw_body(self, console: tcod.console.Console) -> None:
        messages: Reversible[Message] = global_manager.world[None].components[Log]
        y = self.log_height
        i = 0

        for message in reversed(messages):
            console.print_box(
                0,
                console.height - self.log_height + i,
                console.width,
                0,
                message.full_text,
                message.fg
            )
            if y <= 0:
                # No more space to print messages.
                break
            y -= 1
            i += 1

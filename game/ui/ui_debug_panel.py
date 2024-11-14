"""A UI panel which draws debug information."""

from __future__ import annotations

import tcod.console
import tcod.event

import game.managers.global_manager as global_manager
from game.components import Position
from game.constants import COLOR_NAVY, COLOR_WHITE
from game.tags import IsPlayer
from game.ui.ui_panel import UIPanel


class UIDebugPanel(UIPanel):

    def __init__(self) -> None:
        self.is_visible = False

    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the panel is being drawn."""

        # A selection of test frame drawing.
        console.draw_frame(x=0, y=0, width=3, height=3, decoration="╔═╗║ ║╚═╝")
        console.draw_frame(x=3, y=0, width=3, height=3, decoration="┌─┐│ │└─┘")
        console.draw_frame(x=6, y=0, width=3, height=3, decoration="123456789")
        console.draw_frame(x=9, y=0, width=3, height=3, decoration="/-\\| |\\-/")

        # A test rectangle.
        console.draw_rect(15, 15, 6, 6, 0, COLOR_WHITE, COLOR_NAVY)

        # Get the player entity.
        (player,) = global_manager.world.Q.all_of(tags=[IsPlayer])

        # Draw debug info at the top center of the screen.
        console.print_box(
            0,
            0,
            console.width,
            0,
            f"\nPlayer pos: {player.components[Position].x, player.components[Position].y}",
            COLOR_WHITE,
            COLOR_NAVY,
            1,
            2,
        )

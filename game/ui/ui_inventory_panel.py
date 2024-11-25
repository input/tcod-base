from __future__ import annotations

import tcod.console
import tcod.event
from tcod.event import KeySym

from game.components import Name, Quantity
from game.constants import COLOR_GRAY
from game.managers import global_manager, inventory_manager
from game.managers.event_manager import Event
from game.tags import IsPlayer
from game.ui.ui_panel import UIPanel


class UIInventoryPanel(UIPanel):

    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown():
                # i = show/hide the UI inventory panel.
                if event.sym == KeySym.i:
                    # Raise an event which the play state can listen for and
                    # update its ui_full_panel value.
                    Event('ui_full_panel_closed')

    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the panel is being drawn."""

        self.draw_frame(console)
        self.draw_title(console)
        self.draw_body(console)

    def draw_frame(self, console: tcod.console.Console) -> None:
        console.draw_rect(0, 0, console.width, console.height, 0, bg=COLOR_GRAY)

    def draw_title(self, console: tcod.console.Console) -> None:
        console.print(
            console.width // 2,
            3,
            "Inventory",
            alignment=tcod.constants.CENTER,
        )

    def draw_body(self, console: tcod.console.Console) -> None:
        # Get the player entity.
        (player,) = global_manager.world.Q.all_of(tags=[IsPlayer])

        text: str = ""

        for item in inventory_manager.get_items(player):
            text += f"\n{item.components.get(Name)}: {item.components.get(Quantity)}"

        console.print(
            console.width // 2,
            5,
            text,
            alignment=tcod.constants.CENTER
        )

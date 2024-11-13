from __future__ import annotations

import tcod.console
import tcod.event
from tcod.event import KeySym

from game.managers.event_manager import Event
from game.ui.ui_button import UIButton
from game.ui.ui_panel import UIPanel


class UISettingsPanel(UIPanel):

    buttons: tuple[UIButton, ...] | None = None

    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

        if isinstance(event, tcod.event.Quit):
            raise SystemExit()
        elif isinstance(event, tcod.event.KeyDown):
            for i, button in enumerate(self.buttons):
                button.on_event(event)

    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the panel is being drawn."""

        self.draw_title(console)
        self.draw_buttons(console)

    def draw_title(self, console: tcod.console.Console) -> None:
        console.print(
            console.width // 2,
            3,
            "Settings",
            alignment = tcod.constants.CENTER,
        )

    def draw_buttons(self, console: tcod.console.Console) -> None:
        self.buttons = (
            UIButton("[c] Cancel", KeySym.c, self.cancel_button_clicked),
        )

        for i, button in enumerate(self.buttons):
            console.print(
                console.width // 2,
                5 + i,
                button.label,
                (255, 255, 255),
                (64, 64, 64),
                alignment=tcod.constants.CENTER
            )

    def cancel_button_clicked(self) -> None:
        """Callback for the 'Cancel' button."""

        Event('cancel_button_clicked', '')

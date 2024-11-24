from __future__ import annotations

import tcod.event
from tcod.event import KeySym

from game.constants import COLOR_GRAY, COLOR_WHITE, TITLE, DIRECTION_KEYS
from game.managers.event_manager import Event
from game.ui.ui_button import UIButton
from game.ui.ui_panel import UIPanel


class UIMainMenuPanel(UIPanel):

    buttons: tuple[UIButton, ...] | None = None

    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown():
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
            TITLE,
            alignment = tcod.constants.CENTER,
        )

    def draw_buttons(self, console: tcod.console.Console) -> None:
        self.buttons = (
            UIButton("[n] New game", KeySym.n, self.new_game_button_clicked),
            UIButton("[s] Settings", KeySym.s, self.settings_button_clicked),
            UIButton("[q] Quit", KeySym.q, self.quit_button_clicked),
        )

        for i, button in enumerate(self.buttons):
            console.print(
                console.width // 2,
                5 + i,
                button.label,
                COLOR_WHITE,
                COLOR_GRAY,
                alignment=tcod.constants.CENTER
            )

    def new_game_button_clicked(self) -> None:
        """Callback for the 'New game' button."""

        Event('new_game_button_clicked', '')

    def settings_button_clicked(self) -> None:
        """Callback for the 'Settings' button."""

        Event('settings_button_clicked', '')

    def quit_button_clicked(self) -> None:
        """Callback for 'Quit' button."""

        raise SystemExit

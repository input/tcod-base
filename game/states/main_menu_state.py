from __future__ import annotations

import tcod.console
import tcod.event

from game.managers.event_manager import Observer
from game.states.base_state import BaseState
from game.ui.ui_main_menu_panel import UIMainMenuPanel
from game.ui.ui_panel import UIPanel
from game.ui.ui_settings_panel import UISettingsPanel


class MainMenuState(BaseState, Observer):

    active_panel: UIPanel | None = None
    ui_main_menu_panel: UIMainMenuPanel | None = None
    ui_settings_panel: UISettingsPanel | None = None

    def __init__(self) -> None:
        # Initialise UI.
        self.ui_main_menu_panel = UIMainMenuPanel()
        self.ui_settings_panel = UISettingsPanel()
        self.active_panel = self.ui_main_menu_panel

        # Observe events.
        Observer.__init__(self)
        self.observe("settings_button_clicked", self.on_settings_button_clicked)
        self.observe("cancel_button_clicked", self.on_cancel_button_clicked)

    def on_event(self, event: tcod.event.Event) -> None:
        """Called on events."""

        self.active_panel.on_event(event)

    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the state is being drawn."""

        self.active_panel.on_draw(console)

    def on_settings_button_clicked(self, data: str) -> None:
        """Callback for the settings_button_clicked event."""

        self.active_panel = self.ui_settings_panel

    def on_cancel_button_clicked(self, data: str) -> None:
        """Callback for the cancel_button_clicked event."""

        self.active_panel = self.ui_main_menu_panel

"""
The top-level manager.
It sits above and can dictate to everything else.
"""

from __future__ import annotations

from typing import Any

import tcod.console
import tcod.context
import tcod.tileset

import game.managers.global_manager as global_manager
import game.managers.world_manager as world_manager
from game.constants import CONSOLE_WIDTH, CONSOLE_HEIGHT, TITLE
from game.managers.event_manager import Observer
from game.states.base_state import BaseState
from game.states.init_state import InitState
from game.states.main_menu_state import MainMenuState
from game.states.play_state import PlayState


class GameManager(Observer):

    def __init__(self) -> None:
        self.set_state(InitState())
        self.set_state(MainMenuState())

        # Observe events.
        Observer.__init__(self)
        self.observe("new_game_button_clicked", self.on_new_game_button_clicked)

        # Start the main loop.
        self.main_loop()

    def set_state(self, state: BaseState | InitState) -> None:
        """Set the current state."""

        global_manager.state = state

    def main_loop(self) -> None:
        """Run the main loop."""

        # Instantiate a console object and assign it to the global console variable.
        global_manager.console = tcod.console.Console(CONSOLE_WIDTH, CONSOLE_HEIGHT)

        # Create a new context using the console and tileset.
        # Assign it to the global context variable.
        # Start the main loop.
        with tcod.context.new(
            console = global_manager.console,
            tileset = global_manager.tileset,
            title = TITLE
        ) as global_manager.context:
            # Run the current state forever.
            while global_manager.state:
                # Create a new console each frame (rather than clearing the
                # current console). `new_console` returns a console sized for
                # the context, which is helpful when window resizing.
                console = global_manager.context.new_console(CONSOLE_WIDTH, CONSOLE_HEIGHT)

                # Execute the state's drawing.
                global_manager.state.on_draw(console)

                # Present the console.
                global_manager.context.present(console, keep_aspect=True, integer_scaling=True)

                # Handle events.
                for event in tcod.event.wait():
                    if global_manager.state:
                        # Execute the state's event handling.
                        # Pass the original 'event' to each state and, if
                        # required, let an individual state use `convert_event`.
                        # See play_state.on_event() for an example.
                        global_manager.state.on_event(event)

    def on_new_game_button_clicked(self, data: str) -> None:
        """Callback for the new_game_button_clicked event."""

        # Generate a new world.
        global_manager.world = world_manager.new_world()

        # Begin playing.
        self.set_state(PlayState())

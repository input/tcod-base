from __future__ import annotations

from game.managers import global_manager
from game.managers.event_manager import Observer


class UIManager(Observer):

    def __init__(self) -> None:
        # Observe events.
        Observer.__init__(self)
        self.observe("inventory_item_added", self.on_inventory_item_added)

    def on_inventory_item_added(self, data: str) -> None:
        """Callback for the inventory_item_added event."""

        # Update the UI text.
        text = "Added item to inventory: " + data
        global_manager.world[None].components[("Text", str)] = text

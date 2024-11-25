from __future__ import annotations

import tcod.ecs

from game.actions.base_action import BaseAction
from game.components import Position
from game.managers import inventory_manager
from game.tags import IsItem


class PickupItemAction(BaseAction):
    """Pickup an item."""

    def __call__(self, actor: tcod.ecs.Entity) -> None:
        # Pickup any items the actor has stepped on.
        for item in actor.registry.Q.all_of(tags=[actor.components[Position], IsItem]):
            inventory_manager.add_item(actor, item)

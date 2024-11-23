from __future__ import annotations

import attrs
import tcod.ecs

from game.actions.base_action import BaseAction
from game.components import Gold, Position
from game.managers import global_manager
from game.tags import IsItem, IsPlayer


@attrs.define
class MoveAction(BaseAction):
    """Moves the player within a map."""

    direction: tuple[int, int]

    def __call__(self, actor: tcod.ecs.Entity) -> None:
        # Move the actor.
        actor.components[Position] += self.direction

        # Handle player-specific action.
        if IsPlayer in actor.tags:
            # Check whether the player has stepped on gold and, if so,
            # automatically pick it up. If the player has stepped on gold, there
            # will be an entity with:
            # - component: Gold
            # - tags: player's current position; IsItem
            for gold in actor.registry.Q.all_of(components=[Gold], tags=[actor.components[Position], IsItem]):
                # Modify the player's gold total by the value of the gold
                # collected.
                actor.components[Gold] += gold.components[Gold]

                # Update the text.
                text = f"Picked up {gold.components[Gold]}g, total: {actor.components[Gold]}g"
                global_manager.world[None].components[("Text", str)] = text

                gold.clear()

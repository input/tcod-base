from __future__ import annotations

import attrs
import tcod.ecs

from game.actions.base_action import BaseAction
from game.actions.pickup_item_action import PickupItemAction
from game.components import Position
from game.managers.actor_manager import do_action
from game.tags import IsPlayer


@attrs.define
class MoveAction(BaseAction):
    """Move an actor within a map."""

    direction: tuple[int, int]

    def __call__(self, actor: tcod.ecs.Entity) -> None:
        # Move the actor.
        actor.components[Position] += self.direction

        # Handle player-specific item pickup.
        if IsPlayer in actor.tags:
            do_action(actor, PickupItemAction())

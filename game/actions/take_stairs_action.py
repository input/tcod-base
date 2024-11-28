from __future__ import annotations

from typing import Literal

import attrs
import tcod.ecs

from game.actions.base_action import BaseAction
from game.components import Position
from game.constants import COLOR_MAGENTA
from game.managers import global_manager, log_manager
from game.tags import IsIn


@attrs.define
class TakeStairsAction(BaseAction):
    """Move an actor from one level/map to another."""

    direction: Literal["down", "up"]

    def __call__(self, actor: tcod.ecs.Entity) -> None:
        stairs_found = actor.registry.Q.all_of(tags=[actor.components[Position], self.direction]).get_entities()
        if not stairs_found:
            log_manager.add_message(f"There are no {self.direction}ward stairs here!", COLOR_MAGENTA)
            return

        if self.direction == "down":
            actor.relation_tag[IsIn] = global_manager.maps["map1"]
        else:
            actor.relation_tag[IsIn] = global_manager.maps["map0"]

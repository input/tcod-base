from __future__ import annotations

import tcod.ecs

from game.actions.base_action import BaseAction


def do_action(actor: tcod.ecs.Entity, action: BaseAction) -> None:
    action(actor)

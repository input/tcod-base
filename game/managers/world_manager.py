"""Manages the world."""

from __future__ import annotations

from random import Random

import numpy as np
from tcod.ecs import Registry

from game.components import Gold, Graphic, Position, Tiles
from game.constants import GROUND, MAP_HEIGHT, MAP_WIDTH
from game.tags import IsActor, IsItem, IsPlayer


def new_world() -> Registry:
    """Generate a new world."""

    world = Registry()

    # Create entities and assign components and tags to them.
    # https://python-tcod.readthedocs.io/en/latest/tutorial/part-02.html
    player = world[object()]
    player.components[Position] = Position(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    player.components[Graphic] = Graphic(ord("@"))
    player.components[Gold] = 0
    player.tags |= {IsPlayer, IsActor}

    map = world[object()]
    map.components[Tiles] = GROUND[np.random.randint(GROUND.size, size=(MAP_HEIGHT, MAP_WIDTH))]

    rng = Random()

    for _ in range(50):
        gold = world[object()]
        gold.components[Position] = Position(rng.randint(0, MAP_WIDTH), rng.randint(0, MAP_HEIGHT))
        gold.components[Graphic] = Graphic(ord("$"), fg=(255, 255, 0))
        gold.components[Gold] = rng.randint(1, 10)
        gold.tags |= {IsItem}

    return world

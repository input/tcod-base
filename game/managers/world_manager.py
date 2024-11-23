"""Manages the world."""

from __future__ import annotations

from random import Random

import numpy as np
from tcod.ecs import Registry

import game.managers.global_manager as global_manager
from game.components import Gold, Graphic, Position, Tiles
from game.constants import COLOR_BLACK, COLOR_GOLD, COLOR_MAGENTA, GROUND, MAP_HEIGHT, MAP_WIDTH, WATER
from game.tags import IsActor, IsIn, IsItem, IsPlayer


def new_world() -> Registry:
    """Generate a new world."""

    world = Registry()

    # Create entities and assign components and tags to them.
    # https://python-tcod.readthedocs.io/en/latest/tutorial/part-02.html
    map0 = world[object()]
    map0.components[Tiles] = GROUND[np.random.randint(GROUND.size, size=(MAP_HEIGHT, MAP_WIDTH))]
    global_manager.maps["map0"] = map0

    map1 = world[object()]
    map1.components[Tiles] = WATER[np.random.randint(WATER.size, size=(MAP_HEIGHT, MAP_WIDTH))]
    global_manager.maps["map1"] = map1

    player = world[object()]
    player.components[Position] = Position(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    player.components[Graphic] = Graphic(ord("@"))
    player.components[Gold] = 0
    player.tags |= {IsPlayer, IsActor}
    player.relation_tag[IsIn] = map0

    stairs_up = world[object()]
    stairs_up.components[Position] = Position(55, 55)
    stairs_up.components[Graphic] = Graphic(ord("<"), COLOR_BLACK, COLOR_MAGENTA)
    stairs_up.tags.add("up")
    stairs_up.relation_tag[IsIn] = map1

    stairs_down = world[object()]
    stairs_down.components[Position] = Position(58, 58)
    stairs_down.components[Graphic] = Graphic(ord(">"), COLOR_BLACK, COLOR_MAGENTA)
    stairs_down.tags.add("down")
    stairs_down.relation_tag[IsIn] = map0

    rng = Random()

    for _ in range(50):
        gold = world[object()]
        gold.components[Position] = Position(rng.randint(0, MAP_WIDTH), rng.randint(0, MAP_HEIGHT))
        gold.components[Graphic] = Graphic(ord("$"), COLOR_GOLD)
        gold.components[Gold] = rng.randint(1, 10)
        gold.tags |= {IsItem}
        gold.relation_tag[IsIn] = map0

    return world

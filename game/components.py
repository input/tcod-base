"""Components."""

from __future__ import annotations

from numpy.typing import NDArray
from typing import Any, Final, Self

import attrs
import tcod.ecs.callbacks
from tcod.ecs import Entity

from game.constants import COLOR_WHITE


@attrs.define(frozen=True)
class Position:
    """An entity's position."""

    x: int
    y: int

    def __add__(self, direction: tuple[int, int]) -> Self:
        """Add a vector to this position."""

        x, y = direction
        return self.__class__(self.x + x, self.y + y)


@tcod.ecs.callbacks.register_component_changed(component=Position)
def on_position_changed(entity: Entity, old: Position | None, new: Position | None) -> None:
    """Mirror position components as a tag."""

    if old == new:
        return
    if old is not None:
        entity.tags.discard(old)
    if new is not None:
        entity.tags.add(new)


@attrs.define(frozen=True)
class Graphic:
    """An entity's icon and color."""

    ch: int = ord("!")
    fg: tuple[int, int, int] = COLOR_WHITE
    bg: tuple[int, int, int] | None = None


Tiles = ("Tiles", NDArray[Any])
"""Map tiles."""

Gold: Final = ("Gold", int)
"""Amount of gold."""

from __future__ import annotations

import tcod.tileset

import game.managers.global_manager as global_manager
from game.constants import TILE_SOURCE
if TILE_SOURCE == "font":
    from game.constants import FONT_PATH, FONT_WIDTH, FONT_HEIGHT
elif TILE_SOURCE == "tilesheet":
    from game.constants import TILESHEET_PATH, TILESHEET_COLUMNS, TILESHEET_ROWS, TILESHEET_CHAR_MAP


def __init__() -> None:
    load_tileset()


def load_tileset() -> None:
    """Load the tileset using either a font or tilesheet."""

    if TILE_SOURCE == "font":
        tileset = tcod.tileset.load_truetype_font(FONT_PATH, FONT_WIDTH, FONT_HEIGHT)
    elif TILE_SOURCE == "tilesheet":
        tileset = tcod.tileset.load_tilesheet(TILESHEET_PATH, TILESHEET_COLUMNS, TILESHEET_ROWS, TILESHEET_CHAR_MAP)

    # Optionally, generate unicode block elements.
    # tcod.tileset.procedural_block_elements(tileset=tileset)

    global_manager.tileset = tileset

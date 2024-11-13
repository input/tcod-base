"""Constants."""

from __future__ import annotations

from pathlib import Path
from typing import Final

import numpy as np
from numpy.typing import NDArray

from tcod.event import KeySym
import tcod.tileset


# Title. Displayed as the window title and on the main menu screen.
TITLE = "tcod-base"

# Console.
CONSOLE_WIDTH = 35
CONSOLE_HEIGHT = 30

# Map.
MAP_WIDTH = 100
MAP_HEIGHT = 100

# The tile source. Must be one of 'font' or 'tilesheet'.
TILE_SOURCE = "tilesheet"

# Font.
FONT_DIR = Path("assets/fonts/")
FONT = "DejaVuSansMono.ttf"
FONT_WIDTH = 20
FONT_HEIGHT = 20
FONT_PATH = FONT_DIR / FONT

# Tilesheet.
TILESHEET_DIR = Path("assets/tilesheets/")
TILESHEET = "terminal16x16_gs_ro.png"
TILESHEET_CHAR_MAP = tcod.tileset.CHARMAP_CP437
TILESHEET_COLUMNS = 16
TILESHEET_ROWS = 16
TILESHEET_PATH = TILESHEET_DIR / TILESHEET

# Graphics.
GROUND: NDArray[np.int32] = np.array([ord(ch) for ch in "    ,.'`"], dtype=np.int32)

# Keys.
DIRECTION_KEYS: Final = {
    # Arrow keys.
    KeySym.UP: (0, -1),
    KeySym.DOWN: (0, 1),
    KeySym.LEFT: (-1, 0),
    KeySym.RIGHT: (1, 0),
    # Diagonals.
    KeySym.HOME: (-1, -1),
    KeySym.END: (-1, 1),
    KeySym.PAGEUP: (1, -1),
    KeySym.PAGEDOWN: (1, 1),
    # Numpad.
    KeySym.KP_1: (-1, 1),
    KeySym.KP_2: (0, 1),
    KeySym.KP_3: (1, 1),
    KeySym.KP_4: (-1, 0),
    KeySym.KP_6: (1, 0),
    KeySym.KP_7: (-1, -1),
    KeySym.KP_8: (0, -1),
    KeySym.KP_9: (1, -1),
    # Vi keys.
    KeySym.h: (-1, 0),
    KeySym.l: (1, 0),
    KeySym.k: (0, -1),
    KeySym.j: (0, 1),
    KeySym.y: (-1, -1),
    KeySym.b: (-1, 1),
    KeySym.u: (1, -1),
    KeySym.n: (1, 1),
}

# An alternative set of direction keys, which use Scancode instead of KeySym.
# Note: By default, tcod-base does not support Scancode. However, KeySym
#       could be replaced by Scancode if required.
# DIRECTION_KEYS = {
#     # Arrow keys.
#     Scancode.UP: (0, -1),
#     Scancode.DOWN: (0, 1),
#     Scancode.LEFT: (-1, 0),
#     Scancode.RIGHT: (1, 0),
#     Scancode.HOME: (-1, -1),
#     Scancode.END: (-1, 1),
#     Scancode.PAGEUP: (1, -1),
#     Scancode.PAGEDOWN: (1, 1),
#     # Numpad keys.
#     Scancode.KP_1: (-1, 1),
#     Scancode.KP_2: (0, 1),
#     Scancode.KP_3: (1, 1),
#     Scancode.KP_4: (-1, 0),
#     Scancode.KP_6: (1, 0),
#     Scancode.KP_7: (-1, -1),
#     Scancode.KP_8: (0, -1),
#     Scancode.KP_9: (1, -1),
#     # Vi keys.
#     Scancode.H: (-1, 0),
#     Scancode.J: (0, 1),
#     Scancode.K: (0, -1),
#     Scancode.L: (1, 0),
#     Scancode.Y: (-1, -1),
#     Scancode.U: (1, -1),
#     Scancode.B: (-1, 1),
#     Scancode.N: (1, 1),
#     # WASD/WAXD keys.
#     Scancode.Z: (-1, 1),
#     Scancode.X: (0, 1),
#     Scancode.C: (1, 1),
#     Scancode.A: (-1, 0),
#     Scancode.S: (0, 1),
#     Scancode.D: (1, 0),
#     Scancode.Q: (-1, -1),
#     Scancode.W: (0, -1),
#     Scancode.E: (1, -1),
# }

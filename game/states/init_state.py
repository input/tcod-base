"""
The initial state.
It is always the first state to run and is only run once.
"""

from __future__ import annotations

import game.managers.tile_manager as tile_manager


class InitState:

    def __init__(self) -> None:
        tile_manager.__init__()

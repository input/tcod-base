"""Manages global, mutable variables."""

from __future__ import annotations

import tcod.console
import tcod.context
import tcod.ecs
import tcod.tileset

from game.states.base_state import BaseState
from game.states.init_state import InitState

console: tcod.console.Console
"""The current main console."""

context: tcod.context.Context
"""The window managed by tcod."""

state: BaseState | InitState
"""The current state."""

tileset: tcod.tileset.Tileset

world: tcod.ecs.Registry
"""The active ECS registry and current session."""

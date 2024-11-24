from __future__ import annotations

import tcod.camera
import tcod.console
import tcod.constants
import tcod.event
from tcod.event import KeySym, Modifier

import game.managers.global_manager as global_manager
from game.actions.move_action import MoveAction
from game.actions.take_stairs_action import TakeStairsAction
from game.components import Gold, Graphic, Position, Tiles
from game.constants import COLOR_BLACK, COLOR_GROUND, COLOR_WATER, COLOR_WHITE, DIRECTION_KEYS
from game.managers.actor_manager import do_action
from game.states.base_state import BaseState
from game.tags import IsIn, IsItem, IsPlayer
from game.ui.ui_debug_panel import UIDebugPanel
from game.ui.ui_message_panel import UIMessagePanel
from game.ui.ui_panel import UIPanel


class PlayState(BaseState):
    """The play state."""

    camera_ij: tuple[int, ...] = (1, 1)

    # Cursor position in screen space.
    cursor_screen_xy: None | tuple[int, int] = None

    # Cursor position in world space.
    cursor_world_xy: None | tuple[int, int] = None

    # UI.
    ui_debug_panel: UIDebugPanel | None = None
    ui_message_panel: UIMessagePanel | None = None
    ui_panels: dict[str, UIPanel] = {}

    def __init__(self) -> None:
        self.ui_debug_panel = UIDebugPanel()
        self.ui_message_panel = UIMessagePanel()
        self.ui_panels["ui_debug_panel"] = self.ui_debug_panel
        self.ui_panels["ui_message_panel"] = self.ui_message_panel

    def on_event(self, event: tcod.event.Event) -> None:
        """Handle events for the play state."""

        # Get the player entity.
        (player,) = global_manager.world.Q.all_of(tags=[IsPlayer])

        # Convert 'event' into a modified copy of itself which includes
        # additional data about the mouse's coordinates.
        global_manager.context.convert_event(event)

        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown():
                # DIRECTION_KEYS = move the player.
                if event.sym in DIRECTION_KEYS:
                    return do_action(player, MoveAction(DIRECTION_KEYS[event.sym]))
                # d = show/hide the UI debug panel.
                if event.sym == KeySym.d:
                    self.ui_debug_panel.is_visible = not self.ui_debug_panel.is_visible
                # > (. + shift) = take stairs down.
                # < (, + shift) = take stairs up.
                if event.mod & tcod.event.Modifier.SHIFT:
                    if event.sym == KeySym.PERIOD:
                        return do_action(player, TakeStairsAction("down"))
                    if event.sym == KeySym.COMMA:
                        return do_action(player, TakeStairsAction("up"))
            case tcod.event.MouseMotion():
                self.cursor_screen_xy = event.tile.x, event.tile.y

    def draw_world(self, console: tcod.console.Console) -> None:
        """Draw everything except the UI."""

        # Get the player entity.
        (player,) = global_manager.world.Q.all_of(tags=[IsPlayer])

        # Get the map entity.
        map = player.relation_tag[IsIn]

        # Center the camera on the player.
        self.camera_ij = tcod.camera.get_camera(console.rgb.shape, (player.components[Position].y, player.components[Position].x))

        # Clamp the camera to prevent it leaving the world bounds.
        # Note: this doesn't prevent the _player character_ from leaving the
        #       world bounds.
        self.camera_ij = tcod.camera.clamp_camera(console.rgb.shape, map.components[Tiles].shape, self.camera_ij, (0.5, 0.5))

        # Any movements of the camera have to be reflected in the cursor world
        # position.
        self.cursor_world_xy = None
        if self.cursor_screen_xy:
            self.cursor_world_xy = self.cursor_screen_xy[0] + self.camera_ij[1], self.cursor_screen_xy[1] + self.camera_ij[0]

        # Draw the map.
        screen_view, world_view = tcod.camera.get_views(console.rgb, map.components[Tiles], self.camera_ij)
        screen_view["ch"] = world_view
        screen_view["bg"] = COLOR_GROUND if map == global_manager.maps["map0"] else COLOR_WATER

        # Draw the @, $, etc.
        for entity in global_manager.world.Q.all_of(components=[Position, Graphic], relations=[(IsIn, map)]):
            pos = entity.components[Position]
            pos_y = pos.y - self.camera_ij[0]
            pos_x = pos.x - self.camera_ij[1]
            # Cull out-of-bounds objects.
            if not (0 <= pos_x < console.width and 0 <= pos_y < console.height):
                continue
            graphic = entity.components[Graphic]
            if graphic.bg:
                console.rgb[["ch", "fg", "bg"]][pos_y, pos_x] = graphic.ch, graphic.fg, graphic.bg
            else:
                console.rgb[["ch", "fg"]][pos_y, pos_x] = graphic.ch, graphic.fg

        # Highlight the tile under the mouse.
        if self.cursor_screen_xy and 0 <= self.cursor_screen_xy[0] < console.width and 0 <= self.cursor_screen_xy[1] < console.height:
            console.rgb[["fg", "bg"]][self.cursor_screen_xy[1], self.cursor_screen_xy[0]] = COLOR_BLACK, COLOR_WHITE

    def draw_ui(self, console: tcod.console.Console) -> None:
        """Draw the UI."""

        # Draw panels.
        for k, v in self.ui_panels.items():
            if v.is_visible:
                v.on_draw(console)

    def on_draw(self, console: tcod.console.Console) -> None:
        """Handle drawing for the play state."""

        self.draw_world(console)
        self.draw_ui(console)

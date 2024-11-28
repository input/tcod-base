from __future__ import annotations

import tcod.camera
import tcod.console
import tcod.constants
import tcod.event
from tcod.event import KeySym, Modifier

import game.managers.global_manager as global_manager
from game.actions.move_action import MoveAction
from game.actions.take_stairs_action import TakeStairsAction
from game.components import Graphic, Position, Tiles
from game.constants import COLOR_BLACK, COLOR_GROUND, COLOR_WATER, COLOR_WHITE, DIRECTION_KEYS
from game.managers.actor_manager import do_action
from game.managers.event_manager import Observer
from game.managers.log_manager import LogManager
from game.states.base_state import BaseState
from game.tags import IsIn, IsPlayer
from game.ui.ui_debug_panel import UIDebugPanel
from game.ui.ui_inventory_panel import UIInventoryPanel
from game.ui.ui_log_panel import UILogPanel
from game.ui.ui_panel import UIPanel


class PlayState(BaseState, Observer):
    """The play state."""

    camera_ij: tuple[int, ...] = (1, 1)

    # Cursor position in screen space.
    cursor_screen_xy: None | tuple[int, int] = None

    # Cursor position in world space.
    cursor_world_xy: None | tuple[int, int] = None

    # UI.
    ui_debug_panel: UIDebugPanel
    ui_inventory_panel: UIInventoryPanel
    ui_log_panel: UILogPanel
    ui_panels: dict[str, UIPanel] = {}

    # A UI panel which covers the whole screen.
    # For example, the inventory panel.
    ui_full_panel: UIPanel | None = None

    def __init__(self) -> None:
        self.log_manager = LogManager()

        # Initialise UI.
        self.ui_debug_panel = UIDebugPanel()
        self.ui_inventory_panel = UIInventoryPanel()
        self.ui_log_panel = UILogPanel()
        self.ui_panels["ui_debug_panel"] = self.ui_debug_panel
        self.ui_panels["ui_log_panel"] = self.ui_log_panel

        # Observe events.
        Observer.__init__(self)
        self.observe("ui_full_panel_closed", self.on_ui_full_panel_closed)

    def on_event(self, event: tcod.event.Event) -> None:
        """Handle events for the play state."""

        # If a full UI panel is open, only handle its specific events.
        if self.ui_full_panel is not None:
            self.ui_full_panel.on_event(event)
        # Else, handle events for everything else.
        else:
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
                    # i = show/hide the UI inventory panel.
                    if event.sym == KeySym.i:
                        self.ui_full_panel = self.ui_inventory_panel
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

        # If a full UI panel is open, only draw it and nothing else.
        if self.ui_full_panel is not None:
            self.ui_full_panel.on_draw(console)
        # Else, draw everything else.
        else:
            self.draw_world(console)
            self.draw_ui(console)

    def on_ui_full_panel_closed(self, data: str) -> None:
        """Callback for the ui_full_panel_closed event."""

        self.ui_full_panel = None

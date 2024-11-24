# UI

`tcod-base` features a UI (user interface) implementation which is used to build both the modular, in-play UI (for example, the [message panel](/game/ui/ui_message_panel.py) and the [debug panel](/game/ui/ui_debug_panel.py)) and all non-in-play screens (for example, the [main menu screen](/game/ui/ui_main_menu_panel.py)).


## How it works

Conceptually, the UI system comprises elements (for example, a [UI button](/game/ui/ui_button.py) or a [UI panel](/game/ui/ui_panel.py)) which can be combined and/or overridden to compose a complete UI piece. A complete UI piece can then be drawn as required, for example by a state's `on_draw` method.

Each UI element and each complete UI piece is defined in its own module (in [`/game/ui`](/game/ui)).

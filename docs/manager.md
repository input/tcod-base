# Manager

A manager manages a specific aspect of the game.

Conceptually, `tcod-base` implementes a two-tier hierarchy for managers, whereby the game manager ([`game_manager.py`](/game/managers/game_manager.py)) is the top-level manager and all other managers are on the level below.

Accordingly:
- the game manager may dictate to any other manager
- any non-game-manager manager may call to any other non-game-manager manager
- a non-game-manager manager may _not_ dictate to the game-manager


## Managers

`tcod-base` includes the following managers (in [`/game/managers`](/game/managers)):

| File | Description |
| -----| ----------- |
| `actor_manager.py` | Manages actors. |
| `event_manager.py` | Defines `Event` and `Observer` classes for implementing the observer pattern. |
| `game_manager.py` | The top-level manager. It sits above and can dictate to everything else. Manages the main loop and state changes. |
| `global_manager.py` | Manages global, mutable variables. |
| `inventory_manager.py` | Manages inventory. |
| `log_manager.py` | Manages the message log. |
| `tile_manager.py` | Manages the tileset. |
| `world_manager.py` | Generates the game world. |


## Create a new manager

@todo

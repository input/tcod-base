# Architecture

`tcod-base`'s architecture predominantly encompasses the following concepts/implementations: `game`, `state`, `manager`, `world`, and `UI`.


## Game

'Game' refers to the entire application, from the `main.py` entry point through to quitting.


## State

When the game runs, there is always, and only, one active state.

A state can be thought of as a container within which a specific part of the game functions.

*[Further documentation](state.md)*


## Manager

A manager manages a specific aspect of the game.

Conceptually, `tcod-base` implementes a two-tier hierarchy for managers, whereby the game manager (`game/managers/game_manager.py`) is the top-level manager and all other managers are on the level below.

*[Further documentation](manager.md)*


## World

'World' refers to everything accessed during play, _except for_ the UI. This includes the map, the player character, and so on.


## UI

'UI' refers both to the modular, in-play UI (for example, the message panel and the debug panel) and to all non-in-play screens (for example, the main menu screen), which are built using UI.

*[Further documentation](ui.md)*

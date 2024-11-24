# State

When the game runs, there is always, and only, one active state.

A state can be thought of as a container within which a specific part of the game functions.


## States

`tcod-base` includes the following states (in [`/game/states`](/game/states)):

| File | Description |
| -----| ----------- |
| `base_state.py` | A base class from which all states, except `init_state`, inherit. |
| `init_state.py` | The initial state. It is always the first state to run and is only run once. |
| `main_menu_state.py` | The state within which the main menu functions. It is always initially run immediately after `init_state`. |
| `play_state.py` | The state within which the game world functions and is played. |


## How it works

The game manager ([`game_manager.py`](/game/managers/game_manager.py)) has sole responsibility for setting a state (via `game_manager.set_state`).

When the game starts, the game manager sets the current state to `InitState`. Once `InitState` has finished, the game manager sets the current state to `MainMenuState`. From here, clicking the `[n] New game` button raises an event. The game manager observes the event and sets the current state to `PlayState`.

Note: a more detailed explanation of this process can be found in the '[Events and observers](event-observer.md#example)' documentation.

### State flow

Game start --> `InitState` --> `MainMenuState` <----> `PlayState`

### Current state

The current state is stored in the global manager ([`global_manager.py`](/game/managers/global_manager.py)).
```
state: BaseState
```

If it is instead necessary to store a history comprising multiple states, one solution would be to use a list, like so:

1. Modify [`global_manager.py`](/game/managers/global_manager.py):
```
states: list[BaseState] = []
```

2. Modify [`game_manager.py`](/game/managers/game_manager.py):
```
global_manager.states.append(state)
...
while global_manager.states:
...
global_manager.states[-1].on_draw(console)
...
if global_manager.states:
    global_manager.states[-1].on_event(event)
```


## Create a new state

@todo

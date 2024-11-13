# Events and observers

`tcod-base` implements a minimal, general-purpose event-observer system for utilising the observer pattern.

See `game/managers/event_manager.py` for the two key classes - `Observer` and `Event`. These are discussed in more detail below.

Note: [`tcod-ecs`](https://github.com/HexDecimal/python-tcod-ecs) (tcod's entity component system) already implements an ECS-specific solution for observing component changes.


## Naming convention

Events are named in the format: `thing_done`. Example:
```
new_game_button_clicked
```

Callbacks are named in the format: `on_thing_done`. Example:
```
on_new_game_button_clicked
```

## The `Observer` class

This the base observer class.

Classes wishing to observe, and then act on, an event should:

1. Subclass this class:
```
from game.managers.event_manager import Observer


class C(Observer):
```

2. Call the base class's `__init__`:
```
def __init__(self):
    Observer.__init__(self)
```

3. Register:
```
self.observe("thing_clicked", self.on_thing_clicked)
```

4. Add a callback for the event:
```
def on_thing_clicked(self, data):
    print(data)
```

## The `Event` class

This class defines an observable event.

To raise an event, a module should:

1. Import this class:
```
from game.managers.event_manager import Event
```

2. Instantiate an event (for example, when a button is clicked):
```
Event("thing_clicked", "data goes here")
```

## Example

One example of the observer pattern can be found in the code which handles starting a new game.

The main menu UI module (`game/ui/ui_main_menu_panel.py`) imports the `Event` class and defines a `[n] New game` button.
```
from game.managers.event_manager import Event

...

UIButton("[n] New game", KeySym.n, self.new_game_button_clicked)
```

When this button is clicked, the button's callback raises an event.
```
def new_game_button_clicked(self):
    """Callback for the 'New game' button."""
    Event('new_game_button_clicked', '')
```

The `GameManager` class (`game/managers/game_manager.py`) observes this event and then proceeds as needed (in this case, first instructing the world manager to generate a new world, and then starting the play state).
```
from game.managers.event_manager import Observer


class GameManager(Observer):

    def __init__(self):
        Observer.__init__(self)
        self.observe("new_game_button_clicked", self.on_new_game_button_clicked)

    def on_new_game_button_clicked(self, data):
        """Callback for the new_game_button_clicked event."""

        # Generate a new world.
        global_manager.world = world_manager.new_world()

        # Begin playing.
        self.set_state(PlayState())
```

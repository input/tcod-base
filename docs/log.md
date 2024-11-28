# Log

`tcod-base` displays a message log during play. The log is positioned at the bottom of the screen and lists messages in reverse chronological order, beginning with the most recent.


## Add a message

```
from game.constants import COLOR_MAGENTA
from game.managers import log_manager

log_manager.add_message("This is a message. By default, it will be white.")
log_manager.add_message("This message has a custom color.", COLOR_MAGENTA)
```


## How it works

In [log_manager.py](/game/managers/log_manager.py), define a `Message` class, a `Log` component, and an `add_message` function.

In [world_manager.py](/game/managers/world_manager.py), add a `Log` component to the `world`.
```
world[None].components[Log] = Log()
```

In [ui_log_panel.py](/game/ui/ui_log_panel.py), draw the message log.

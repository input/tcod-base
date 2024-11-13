# Map

`tcod-base` implements a minimal, 'blank canvas'-style map which comprises a 100x100 area of ground tiles. This is a useful base example. However, a full game will likely require a more advanced map generation method.


## How it works

In `game/constants.py`:

1. Define the map's dimensions (in tiles).
```
MAP_WIDTH = 100
MAP_HEIGHT = 100
```

2. Define an [N-dimensional array](https://numpy.org/doc/stable/reference/arrays.ndarray.html) of ground character unicode code points.
```
GROUND: NDArray[np.int32] = np.array([ord(ch) for ch in "    ,.'`"], dtype=np.int32)
```

In `game/components.py`, create a `Tiles` component:
```
Tiles = ("Tiles", NDArray[Any])
```

In `game/managers/world_manager.py`, create a `map` entity and add the `Tiles` component:
```
map = world[object()]
map.components[Tiles] = GROUND[np.random.randint(GROUND.size, size=(MAP_HEIGHT, MAP_WIDTH))]
```

In `game/states/play_state.py`:
```
screen_view, world_view = tcod.camera.get_views(console.rgb, map.components[Tiles], self.camera_ij)
```

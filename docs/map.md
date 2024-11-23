# Map

`tcod-base` implements two minimal, 'blank canvas'-style maps which each comprise a 100x100 area of tiles. One map represents ground and the other map represents water. These are useful base examples. However, a full game will likely require a more advanced map generation method.


## How it works

In `game/constants.py`:

1. Define the maps' dimensions (in tiles).
```
MAP_WIDTH = 100
MAP_HEIGHT = 100
```

2. Define two [N-dimensional arrays](https://numpy.org/doc/stable/reference/arrays.ndarray.html) containing unicode code points, one for ground characters and the other for water characters.
```
GROUND: NDArray[np.int32] = np.array([ord(ch) for ch in "    ,.'`"], dtype=np.int32)
WATER: NDArray[np.int32] = np.array([ord(ch) for ch in "    ~≈"], dtype=np.int32)
```

In `game/components.py`, create a `Tiles` component:
```
Tiles = ("Tiles", NDArray[Any])
```

In `game/managers/world_manager.py`, create two `map` entities and give each a `Tiles` component which references the relevant unicode array:
```
map0 = world[object()]
map0.components[Tiles] = GROUND[np.random.randint(GROUND.size, size=(MAP_HEIGHT, MAP_WIDTH))]
global_manager.maps["map0"] = map0

map1 = world[object()]
map1.components[Tiles] = WATER[np.random.randint(WATER.size, size=(MAP_HEIGHT, MAP_WIDTH))]
global_manager.maps["map1"] = map1
```

In `game/states/play_state.py`:
```
screen_view, world_view = tcod.camera.get_views(console.rgb, map.components[Tiles], self.camera_ij)
screen_view["ch"] = world_view
screen_view["bg"] = COLOR_GROUND if map == global_manager.maps["map0"] else COLOR_WATER
```

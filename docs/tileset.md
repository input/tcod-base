# Tileset

`tcod-base` supports the use of a single tileset, which can be created either from a `.ttf` or `.otf` font file or a `.png` tilesheet.

See `python-tcod`'s documentation for details: [`tcod.tileset`](https://python-tcod.readthedocs.io/en/latest/tcod/tileset.html)


## Change the font/tilesheet

### Add a font/tilesheet

If necessary, add a new font or tilesheet to the relevant `assets` directory.

Fonts are stored in [`/assets/fonts`](/assets/fonts). Tilesheets are stored in [`/assets/tilesheets`](/assets/tilesheets).

### Modify font/tilesheet values

In [`constants.py`](/game/constants.py):

1. Set the `TILE_SOURCE` to either `font` or `tilesheet`.
```
TILE_SOURCE = "font"
or
TILE_SOURCE = "tilesheet"
```

2. Modify the default font or tilesheet values.

The default font values, which may need modifying, are:
```
FONT = "DejaVuSansMono.ttf"
FONT_WIDTH = 20
FONT_HEIGHT = 20
```

See `python-tcod`'s documentation for details: [`tcod.tileset.load_tilesheet`](https://python-tcod.readthedocs.io/en/latest/tcod/tileset.html#tcod.tileset.load_tilesheet)

The default tilesheet values, which may need modifying, are:
```
TILESHEET = "terminal16x16_gs_ro.png"
TILESHEET_CHAR_MAP = tcod.tileset.CHARMAP_CP437
TILESHEET_COLUMNS = 16
TILESHEET_ROWS = 16
```

See `python-tcod`'s documentation for details: [`tcod.tileset.load_truetype_font`](https://python-tcod.readthedocs.io/en/latest/tcod/tileset.html#tcod.tileset.load_truetype_font)


## How it works

The tileset is initialised during the `InitState`.

- `GameManager.__init__()` ([`game_manager.py`](/game/managers/game_manager.py)) sets the state to `InitState`

- `InitState.__init__()` ([`init_state.py`](/game/states/init_state.py)) calls `tile_manager.__init__()`

- `tile_manager.__init__()` ([`tile_manager.py`](/game/managers/tile_manager.py)) calls `tile_manager.load_tileset()`

- `tile_manager.load_tileset()` loads the tileset using either a font or tilesheet (as defined by the `TILE_SOURCE` value)

# README

`tcod-base` is a minimal starter kit for building projects with [`python-tcod`](https://github.com/libtcod/python-tcod).

`tcod-base` was primarily inspired by HexDecimal's [Roguelikedev tutorial engine](https://github.com/HexDecimal/roguelikedev-tutorial-engine-2024) repo, but diverges somewhat in its [code architecture](docs/architecture.md).


## Features

Features include base implementations of:
- state management
- UI system
- general-purpose event-observer system
- keyboard controls
- map generation
- inventory
- message log


## Screenshots

![tcod-base main menu](/assets/screenshots/main-menu.png)
*Main menu*

![tcod-base ground map](/assets/screenshots/map-ground.png)
*Ground map*

![tcod-base water map](/assets/screenshots/map-water.png)
*Water map*

![tcod-base inventory](/assets/screenshots/inventory.png)
*Inventory*


## Install

Download or clone the repository:
```
git clone https://github.com/input/tcod-base
```

Install the requirements:
```
cd tcod-base
[activate a virtual environment]
pip install -r requirements.txt
```

Launch:
```
python main.py
```


## Documentation

Documentation for `tcod-base` can be found in the [`docs`](docs) directory.

Also see `python-tcod`'s [documentation](https://python-tcod.readthedocs.io/en/latest/index.html).


## License

`tcod-base` is released under the 3-Clause BSD License.

"""Classes for using the observer pattern."""

from __future__ import annotations

from collections.abc import Callable


class Observer():
    """The base observer class."""

    _observers = []

    def __init__(self) -> None:
        self._observers.append(self)
        self._observables = {}

    def observe(self, event_name: str, callback: Callable) -> None:
        self._observables[event_name] = callback


class Event():
    """An observable event."""

    def __init__(self, name: str, data: str = "", autofire: bool = True) -> None:
        self.name = name
        self.data = data
        if autofire:
            self.fire()

    def fire(self) -> None:
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](self.data)

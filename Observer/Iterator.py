from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class Iterador(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: ProductoIterador) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value

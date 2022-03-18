from __future__ import annotations
from collections.abc import Iterable, Iterator
from Producto import Producto
from Iterator import Iterador
from typing import Any, List

class ProductoIterador(Iterable):

    def __init__(self, collection: List[Producto] = []) -> None:
        self._collection = collection

    def __iter__(self) -> Iterador:
        return Iterador(self._collection)

    def get_reverse_iterator(self) -> Iterador:
        return Iterador(self._collection)

    def addProducto(self, item: Any):
        self._collection.append(item)

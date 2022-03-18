from IObserver import IObserver
from IObservable import IObservable
from Observador import Observador
from Implementador import Implementador
from abc import ABC, abstractmethod
from typing import List
from ProductoBuilder import ProductoBuilder

class Producto(IObservable, ProductoBuilder,ABC):
    _state: int = None
    _inventario: int = 0
    _observers: List[IObserver] = []
    _implementador: Implementador

    def __init__(self, implementador: Implementador):
        self._implementador = implementador

    def printImplementador(self):
        self.implementador.procesar()

    def agregarObservador(self, observer: IObserver) -> None:
        print("Se añadio el observador")
        self._observers.append(observer)

    def quitarObservador(self, observer: IObserver) -> None:
        self._observers.remove(observer)

    def notificarObservador(self) -> None:
        print("Se esta notificando a los observadores")
        for observer in self._observers:
            observer.actualizar(self)

    def agregarInventario(self, cantidad: int) -> None:
        self._inventario += cantidad
        self.notificarObservador()

    def eliminarInventario(self, cantidad: int) -> None:
        self._inventario -= cantidad
        self.notificarObservador()

    def setNombre(self, nombre):
        self.nombre = nombre
        return self

    def setPrecio(self, precio):
        self.precio = precio
        return self

    def setImplementador(self, implementador: Implementador):
        self.implementador = implementador
        return self

    @abstractmethod
    def clone():
        """Metodo para implementar la clonacion"""

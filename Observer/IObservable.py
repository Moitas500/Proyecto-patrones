from __future__ import annotations
from abc import ABC, abstractmethod

class IObservable(ABC):
    @abstractmethod
    def agregarObservador(self, observer: IObserver) -> None:
        """
        Agrega un observador al producto
        """
        pass

    @abstractmethod
    def quitarObservador(self, observer: IObserver) -> None:
        """
        Elimina un observador del producto
        """
        pass

    @abstractmethod
    def notificarObservador(self) -> None:
        """
        Notifica a los observadores 
        """
        pass

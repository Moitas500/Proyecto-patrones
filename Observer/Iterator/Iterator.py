from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next():
        """Devuelve un booleando dependiendo si esta al final de la listra o no"""

    @abstractmethod
    def next():
        """Devuelve el objeto de la coleccion"""

from abc import ABC, abstractmethod
from Implementador import Implementador

class ProductoBuilder(ABC):
    @abstractmethod
    def setNombre(self, nombre):
        """Metodo para agregar el nombre del producto"""

    @abstractmethod
    def setPrecio(self, precio):
        """"Metodo para agregar el precio del producto"""
        
    @abstractmethod
    def setImplementador(self, implementador: Implementador):
        """Metodo para agregar el implementador del producto"""

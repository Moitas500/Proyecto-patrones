from Producto import Producto
from ProductoBuilder import ProductoBuilder
from Implementador import Implementador

class Variados():
    def __init__(self) -> None:
        self._builder = None

    def builder(self)->ProductoBuilder:
        return self._builder

    def builder(self, builder: ProductoBuilder)-> None:
        self._builder = builder

    def buildProducto(self, nombre, precio, implementador: Implementador)-> None:
        self.builder.setNombre(nombre)
        self.builder.setPrecio(precio)
        self.builder.setImplementador(implementador)

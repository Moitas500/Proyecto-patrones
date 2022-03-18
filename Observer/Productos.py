from Producto import Producto
from ProductoBuilder import ProductoBuilder
from Implementador import Implementador

class Gelatina(Producto):
    def __init__(self, precio, implementador: Implementador, nombre = "Gelatina YOVI"):
        self.precio = precio
        self.implementador = implementador
        self.nombre = nombre

    def clone(self):
        return type(self)(
            self.precio,
            self.implementador)
    
    def __str__(self):
        return f"Nombre= {self.nombre}"
    
class Galletas(Producto):
    def __init__(self, precio, implementador: Implementador, nombre = "Galletas ERPOS"):
        self.precio = precio
        self.implementador = implementador
        self.nombre = nombre

    def clone(self):
        return type(self)(
            self.precio,
            self.implementador)

    def __str__(self):
        return f"Nombre= {self.nombre}"

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

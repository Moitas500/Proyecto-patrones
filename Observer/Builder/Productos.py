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
        return f"Precio= {self.precio}"
    
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
        return f"Precio= {self.precio}"
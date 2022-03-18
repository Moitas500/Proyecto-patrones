from Productos import Variados
from Observador import Observador
from Peso import Peso
from Unidad import Unidad
from Producto import Producto
from Productos import Gelatina

if __name__ == "__main__":
    unidad = Unidad(50)
    peso = Peso(20, "Kg")
    
    producto = Variados()
    galleta = Gelatina(1000, peso)
    producto.builder = galleta
    
    observer_a = Observador()
    producto.builder.agregarObservador(observer_a)

    """
    Patron builder
    """

    producto.builder.agregarInventario(50)
    producto.builder.eliminarInventario(20)

    producto.buildProducto("papas",2000, unidad)

    print(producto.builder.nombre)
    print(producto.builder.precio)
    print(producto.builder.implementador)
    

from Productos import Gelatina
from Productos import Galletas
from Productos import Variados
from Peso import Peso
from Unidad import Unidad
from ProductoIterador import ProductoIterador

if __name__ == "__main__":
    """
    Creacioón de productos para la lista a iterar
    """
    unidad = Unidad(50)
    peso = Peso(20, "Kg")
    
    gelatina = Gelatina(1000, peso)
    galleta1 = Galletas(2000, unidad)
    galleta = Galletas(2000, unidad)

    papas = Variados()
    galleta = Gelatina(1000, peso)
    papas.builder = galleta
    
    papas.buildProducto("papas",2000, unidad)

    """
    Inicio patron Iterador
    """
    lista = ProductoIterador()
    
    lista.addProducto(gelatina)
    lista.addProducto(galleta1)
    lista.addProducto(papas.builder)

    iterador = lista.__iter__()

    producto = iterador.__next__()

    print(producto)

    producto = iterador.__next__()

    print(producto)

    producto = iterador.__next__()

    print(producto)


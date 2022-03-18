from Producto import Producto
from Observador import Observador
from Peso import Peso
from Unidad import Unidad
from Productos import Gelatina

if __name__ == "__main__":
    unidad = Unidad(50)
    peso = Peso(20, "Kg")
    
    galleta = Gelatina(1000, peso)

    print("La galleta pesa: ")
    print(galleta.implementador.getPeso())
    print(galleta.implementador.getMedida())

    galleta.printImplementador()

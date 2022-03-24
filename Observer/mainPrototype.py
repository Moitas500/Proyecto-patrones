from Productos import Gelatina
from Productos import Galletas
from Productos import Variados
from Peso import Peso
from Unidad import Unidad

if __name__ == "__main__":
    peso = Peso(20, "Kg")
    producto1 = Gelatina(1000,peso)
    print(producto1)
    producto2 = producto1.clone()
    print(producto2)
    producto2.precio = 2000
    print(producto2)

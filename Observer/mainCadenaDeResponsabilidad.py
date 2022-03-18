from Administrador import Administrador
from Vendedor import Vendedor
from Cliente import Cliente

if __name__ == "__main__":
    cliente = Cliente("Pedro", "Rey")
    vendedor = Vendedor(cliente)
    administrador = Administrador(vendedor)

    administrador.setSiguiente(vendedor)
    vendedor.setSiguiente(cliente)

    rol = input('Digite el rol que desea asignar: ')

    administrador.handle(rol)

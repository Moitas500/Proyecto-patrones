from Cliente import Cliente
from UserGeneral import Usuario
from Administrador import Administrador
from Vendedor import Vendedor

def client_code(usuario: Usuario) -> None:
    print(f"{usuario.operaciones()}", end="")

if __name__ == "__main__":
    usuarioSimple = Cliente("Pedro", "Rey")
    print("Cliente")
    client_code(usuarioSimple)
    print("\n")

    decoradorVendedor = Vendedor(usuarioSimple)
    print("Vendedor")
    client_code(decoradorVendedor)

    print("\n")

    decoradorAdministrador = Administrador(decoradorVendedor)
    print("Administrador")
    client_code(decoradorAdministrador)

from Command import Command

class Agregar(Command):
    def __init__(self):
        print("Creando comando agregar")

    def execute(self) -> None:
        print("Agregando producto al carrito")

class Eliminar(Command):
    def __init__(self):
        print("Creando comando eliminar")

    def execute(self) -> None:
        print("Eliminando producto del carrito")

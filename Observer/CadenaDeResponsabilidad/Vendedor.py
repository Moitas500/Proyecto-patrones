from Decorator import Decorator
from IHandler import IHandler

class Vendedor(Decorator, IHandler):
    def operaciones(self):
        return f"Puede vender({self.usuario.operaciones()})"

    def __intir__(self):
        self.siguiente = None

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def handle(self, rol):
        if "Vendedor" == rol:
            self.rol = "Vendedor"
            print("Es un vendedor")
        else:
            self.siguiente.handle(rol)

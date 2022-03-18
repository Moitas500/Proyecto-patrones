from Decorator import Decorator

class Vendedor(Decorator):
    def operaciones(self):
        return f"Puede vender({self.usuario.operaciones()})"

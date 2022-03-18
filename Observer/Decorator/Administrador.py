from Decorator import Decorator

class Administrador(Decorator):
    def operaciones(self):
        return f"Puede ver informes, facturas, etc({self.usuario.operaciones()})"

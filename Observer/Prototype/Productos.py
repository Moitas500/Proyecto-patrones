from Producto import Producto

class Gelatina(Producto):
    def __init__(self, precio):
        self.precio = precio

    def clone(self):
        return type(self)(
            self.precio)

    
class Galletas(Producto):
    def __init__(self, precio):
        self.precio = precio

    def clone(self):
        return type(self)(
            self.precio)

class Variados(Producto):
    def __init__(self, precio):
        self.precio = precio

    def clone(self):
        return type(self)(
            self.precio)

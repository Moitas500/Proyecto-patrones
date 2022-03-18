from Implementador import Implementador

class Unidad(Implementador):
    unidad: int = 0

    def __init__(self, unidad: int):
        self.unidad = unidad
    
    def procesar(self):
        print("añadido unidad")

    def getUnidad(self):
        return self.unidad

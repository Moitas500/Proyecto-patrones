from Implementador import Implementador

class Peso(Implementador):
    peso: int = 0
    medida = ""
    
    def __init__(self, peso: int, medida):
        self.peso = peso
        self.medida = medida
    
    def procesar(self):
        print("añadido peso")

    def getMedida(self):
        return self.medida

    def getPeso(self):
        return self.peso

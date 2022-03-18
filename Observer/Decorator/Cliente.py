from UserGeneral import Usuario

class Cliente(Usuario):
    nombre = ""
    apellido = ""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def operaciones(self):
        return("Puede comprar productos")

    
        

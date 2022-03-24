from UserGeneral import Usuario
from IHandler import IHandler

class Cliente(Usuario, IHandler):
    nombre = ""
    apellido = ""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def operaciones(self):
        return("Puede comprar productos")

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def handle(self, rol):
        if "Cliente" == rol:
            self.rol = "Cliente"
            print("Es un cliente")
        else:
            print("Digito un rol no existente")
    
        

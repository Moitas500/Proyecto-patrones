from ServicioLogin import ServicioLogin
from Servicio import Servicio

class Proxy(ServicioLogin):
    def __init__(self, servicio: Servicio)-> None:
        self.servicio = servicio

    def request(self, nombre, passw, rol)-> None:
        """
        Aqui se verifica que el logueo sea correcto
        """
        if(self.verificarLogin(nombre, passw, rol)):
            self.accesoDeLogueo()
        else:
            print("Los datos especificados son invalidos")

    def verificarLogin(self, nombre, passw, rol)-> bool:
        """
        Codigo para verificar que los datos sean correctos
        """
        if(nombre == "Pedro" and passw == "Rey" and rol == "Administrador"): 
            print("verificado")
            return True
    
        return False

    def accesoDeLogueo(self)-> None:
        print("accedido")

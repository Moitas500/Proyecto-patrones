from Observer.UserGeneral import Usuario
from ServicioLogin import ServicioLogin
from Servicio import Servicio

class Proxy(ServicioLogin):
    def __init__(self, servicio: Servicio)-> None:
        self.servicio = servicio
        usuario = Usuario()

    def request(self, nombre, passw, rol)-> None:
        """
        Aqui se verifica que el logueo sea correcto
        """
        if(self.verificarLogin(nombre, passw)):
            return self.accesoDeLogueo()
        else:
            return "Los datos especificados son invalidos"

    def verificarLogin(self, db, nombre, passw)-> bool:
        """
        Codigo para verificar que los datos sean correctos
        """
        try:
            conn = db.connect("users.db")
            cur = conn.cursor()
            # Realizamos el Query. 
            check = cur.execute('select * from users where username=? and password=?', (nombre, passw))
            if check.fetchone():
                return True
            else:
                return False
        finally:
            cur.close()
            conn.close()

    def accesoDeLogueo(self)-> None:
        self.usuario = 

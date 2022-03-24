from Decorator.Administrador import Administrador
from Decorator.Cliente import Cliente
from Decorator.UserGeneral import Usuario
from Decorator.Vendedor import Vendedor
from ServicioLogin import ServicioLogin
from Servicio import Servicio

class Proxy(ServicioLogin):
    def __init__(self, usuario: Usuario)-> None:
        self.servicio = Servicio()
        self.usuario = usuario

    def request(self, db, nombre, passw)-> Usuario:
        """
        Aqui se verifica que el logueo sea correcto
        """
        self.usuario = Cliente(nombre, passw)
        
        if(self.verificarLogin(db, nombre, passw)):
            return self.accesoDeLogueo(db, nombre, passw)
        else:
            return self.usuario

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

    def accesoDeLogueo(self, db, nombre, passw)-> None:

        conn = db.connect("users.db")
        cur = conn.cursor()
        user = cur.execute('select * from users where username=? and password=?', (nombre, passw))
        cur.close()
        conn.close()
        
        if user.Rol == "Vendedor":
            return Vendedor(self.usuario)
        elif user.Rol == "Administrador":
            return Administrador(self.usuario)
        

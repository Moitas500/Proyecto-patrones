from BD.BaseDatos import BaseDeDatos
from Command.Comandos import Agregar
from Command.Invoker import Invoker
from Proxy.Proxy import Proxy
from Decorator.UserGeneral import Usuario
from codigo.Command.Comandos import Eliminar

class Controlador():
    def __init__(self)-> None:
        self._bd = BaseDeDatos()
        self.user = Usuario()
        self.invoker = Invoker()
        
    def ingresoUsuario(self, nombre, passw):
        __auth = Proxy(self.user)
        self.user = __auth.request(self._bd, nombre, passw)

    def clickAgregar(self):
        ordenAgregar = Agregar()
        self.invoker = Invoker(ordenAgregar)
        self.invoker.run()
        
    def clickEliminar(self):
        ordenEliminar = Eliminar()
        self.invoker = Invoker(ordenEliminar)
        self.invoker.run()
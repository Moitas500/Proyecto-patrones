from msilib.schema import Class
from tabnanny import check
from weakref import proxy
from Observer.BaseDatos import BaseDeDatos
from Observer.Proxy import Proxy
from Observer.Servicio import Servicio


class Controlador():
    def __init__(self)-> None:
        __bd = BaseDeDatos()
        
        _con = __bd.connect('db.sqlite3')
        _cur = _con.cursor()
        
    def ingresoUsuario(nombre, passw, self):
        __auth = Proxy()
        
        __auth.verificarLogin(self.__bd, nombre, passw, '')
        
    def clickN():
        
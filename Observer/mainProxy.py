from Servicio import Servicio
from Proxy import Proxy
from Cliente import Cliente
from UserGeneral import Usuario
from Administrador import Administrador
from Vendedor import Vendedor

if __name__ == "__main__":
    """
    Decorator
    """
    
    usuario = Cliente("Pedro", "Rey")

    vendedor = Vendedor(usuario)

    admin = Administrador(vendedor)

    """
    Cadena de mando
    """

    admin.setSiguiente(vendedor)
    vendedor.setSiguiente(usuario)

    rol = input('Digite el rol que desea asignar: ')

    admin.handle(rol)
    
    """
    Patron Proxy
    """
    servicio = Servicio()
    
    servicio.request(usuario.nombre, usuario.contraseña, admin.rol)
    
    proxy = Proxy(servicio)

    proxy.request(servicio.nombre, servicio.contraseña, servicio.rol)


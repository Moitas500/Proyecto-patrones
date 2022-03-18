from ServicioLogin import ServicioLogin

class Servicio(ServicioLogin):
    
    def request(self, nombre, contraseña, rol) -> None:
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol

from ServicioLogin import ServicioLogin

class Servicio(ServicioLogin):
    
    def request(self, nombre, passw, rol) -> None:
        self.nombre = nombre
        self.passw = passw
        self.rol = rol

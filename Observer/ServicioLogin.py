from abc import ABC, abstractmethod

class ServicioLogin(ABC):
    @abstractmethod
    def request(self, nombre, passw, rol) -> None:
        pass

    

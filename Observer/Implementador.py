from abc import ABC, abstractmethod

class Implementador(ABC):
    @abstractmethod
    def procesar(self):
        pass

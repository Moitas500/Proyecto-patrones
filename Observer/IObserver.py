from abc import ABC, abstractmethod
from IObservable import IObservable

class IObserver(ABC):
    @abstractmethod
    def actualizar(self, subject: IObservable) -> None:
        """
        Recibe actualizaciones del producto
        """
        pass

from IObserver import IObserver
from IObservable import IObservable

class Observador(IObserver):
    def actualizar(self, subject: IObservable) -> None:
        if subject._inventario < 10:
            print("Se esta acabando el inventario del producto")

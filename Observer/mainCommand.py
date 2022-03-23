from Invoker import Invoker
from Comandos import Agregar
from Comandos import Eliminar

if __name__ == "__main__":
    ordenAgregar = Agregar()
    invoker = Invoker(ordenAgregar)
    invoker.run()

    ordenEliminar = Eliminar()
    invoker = Invoker(ordenEliminar)
    invoker.run()

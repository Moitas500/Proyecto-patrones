from Invoker import Invoker
from Comandos import Agregar
from Comandos import Eliminar

if __name__ == "__main__":
    ordenAgregar = Agregar()
    ordenEliminar = Eliminar()
    
    invoker = Invoker(ordenAgregar)
    invoker.run()

    invoker = Invoker(ordenEliminar)
    invoker.run()
